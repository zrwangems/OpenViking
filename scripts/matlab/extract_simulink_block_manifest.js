// Extract the complete official Simulink Blocks category manifest.
// Usage: node extract_simulink_block_manifest.js [output.json]
// Uses MathWorks' versioned source XML directly. No browser or npm packages required.
const fs = require('fs');

const RELEASE = 'R2025b';
const SOURCE = `https://www.mathworks.com/help/releases/${RELEASE}/simulink/referencelist_block_cat.xml`;
const CATEGORIES = [
  'Continuous',
  'Dashboard',
  'Customizable Blocks',
  'Discontinuities',
  'Discrete',
  'Logic and Bit Operations',
  'Lookup Tables',
  'Math Operations',
  'Matrix Operations',
  'Messages & Events',
  'Model Verification',
  'Model-Wide Utilities',
  'Ports and Subsystems',
  'Signal Attributes',
  'Signal Routing',
  'Sinks',
  'Sources',
  'String',
  'User-Defined Functions',
  'Additional Math and Discrete',
];

function decode(value) {
  return value.replace(/&(?:#(\d+)|#x([0-9a-f]+)|([a-z]+));/gi, (_, decimal, hex, named) => {
    if (decimal) return String.fromCodePoint(Number(decimal));
    if (hex) return String.fromCodePoint(parseInt(hex, 16));
    return { amp: '&', lt: '<', gt: '>', quot: '"', apos: "'" }[named.toLowerCase()] || '';
  });
}

function text(value) {
  return decode(value.replace(/<[^>]+>/g, ' ')).replace(/\s+/g, ' ').trim();
}

function attribute(attributes, name) {
  const match = attributes.match(new RegExp(`\\b${name}="([^"]*)"`));
  if (!match) throw new Error(`Missing ${name} attribute in ${attributes}`);
  return decode(match[1]);
}

(async () => {
  const output = process.argv[2] || `${__dirname}/simulink-block-manifest.json`;
  const response = await fetch(SOURCE);
  if (!response.ok) throw new Error(`${response.status} ${response.statusText}: ${SOURCE}`);
  const xml = await response.text();
  const entries = [];
  for (const category of CATEGORIES) {
    const escaped = category
      .replace(/&/g, '&amp;')
      .replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const categoryPattern = new RegExp(
      `<(?:ns0:)?cat\\b[^>]*>\\s*<(?:ns0:)?title>${escaped}</(?:ns0:)?title>([\\s\\S]*?)</(?:ns0:)?cat>`,
    );
    const categoryMatch = xml.match(categoryPattern);
    if (!categoryMatch) throw new Error(`Missing official category: ${category}`);
    const categoryXml = categoryMatch[1];
    for (const ref of categoryXml.matchAll(/<(?:ns0:)?ref\b([^>]*)>([\s\S]*?)<\/(?:ns0:)?ref>/g)) {
      if (attribute(ref[1], 'type') !== 'block') continue;
      const purpose = ref[2].match(/<(?:ns0:)?purpose>([\s\S]*?)<\/(?:ns0:)?purpose>/);
      entries.push({
        category,
        name: attribute(ref[1], 'name'),
        path: attribute(ref[1], 'target'),
        summary: purpose ? text(purpose[1]) : '',
      });
    }
  }
  entries.sort((a, b) =>
    CATEGORIES.indexOf(a.category) - CATEGORIES.indexOf(b.category)
    || a.name.localeCompare(b.name, 'en'),
  );
  const uniquePaths = new Set(entries.map((entry) => entry.path));
  if (entries.length !== 341 || uniquePaths.size !== 333) {
    throw new Error(`Official manifest changed: ${entries.length} entries / ${uniquePaths.size} paths; review before updating`);
  }
  fs.writeFileSync(output, `${JSON.stringify(entries, null, 2)}\n`);
  console.log(`Wrote ${entries.length} entries / ${uniquePaths.size} document paths from ${SOURCE}`);
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
