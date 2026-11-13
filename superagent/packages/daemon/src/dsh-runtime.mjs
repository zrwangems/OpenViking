// Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
// SPDX-License-Identifier: AGPL-3.0

import { createHash } from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { sanitizeAgentChildEnv } from './process-utils.mjs';
import { homeDir as platformHomeDir } from './platform/index.mjs';
import { preparePrivateDirectory } from './private-temp.mjs';
import { getRuntimeDefinition } from './runtime-catalog.mjs';

const RUNTIME = getRuntimeDefinition('dsh');
export const DSH_BRIDGE_PATH = fileURLToPath(new URL('./dsh-bridge.mjs', import.meta.url));
const DSH_SUPPORTED = Object.freeze({ min: '0.2.2-rc.1', belowMajorMinor: '0.3' });
// The full set DSH understands for a route (`llm-pi-ai/src/catalog.ts`); which
// of them a model offers is answered per model by `superagent/llm/model/info`.
export const DSH_EFFORTS = RUNTIME?.efforts
  ?? Object.freeze(['off', 'minimal', 'low', 'medium', 'high', 'xhigh', 'max']);
// The built-in route the adapter falls back on when a requested one is unknown.
// Operator routes live in DSH's own settings document, not in this process.
export const DSH_DEFAULT_MODEL = 'deepseek-official/deepseek-flash';

// How one instance keeps the DSH home it runs against:
//
//   isolated (the default) -- `<dataDir>/dsh/{home,agents}`: credentials,
//     sessions and model settings belong to this instance alone. Every release
//     before the setting existed behaved this way, so an omitted field keeps it.
//   shared -- `~/.dsh` (DSH_HOME) and `~/.agents` (DSH_AGENTS_HOME): the same
//     home the operator's own DeepSeek Harness uses, so credentials, sessions
//     and model routes are shared with it. The launch patch stays per instance,
//     under `<dataDir>/dsh/run`.
export const DSH_HOME_MODES = Object.freeze(['isolated', 'shared']);
const DSH_SHARED_HOME_DIR = '.dsh';
// DSH's default shared agent root, independent of DSH_HOME (`dsh-home-paths`).
const DSH_SHARED_AGENTS_DIR = '.agents';
// `<DSH_HOME>/profiles/sdk/cordis.patch.yml`: DSH's settings service writes this
// file; it is the single source of truth for model configuration (design §1), so
// the daemon only ever reads it.
const DSH_PROFILE_PATCH_SEGMENTS = Object.freeze(['profiles', 'sdk', 'cordis.patch.yml']);

/**
 * The configured placement, or the documented default for a missing value.
 * @param {*} value - `agents[].dshHomeMode` (or the equivalent daemon env value).
 * @returns {'isolated'|'shared'} the normalized mode.
 */
export function normalizeDshHomeMode(value) {
  const mode = String(value ?? '').trim() || DSH_HOME_MODES[0];
  if (!DSH_HOME_MODES.includes(mode)) {
    throw new Error(`invalid DSH home mode: ${mode}; expected ${DSH_HOME_MODES.join(' or ')}`);
  }
  return mode;
}

function absoluteHomeDir(homeDir) {
  const value = homeDir ?? platformHomeDir() ?? '';
  const normalized = typeof value === 'string' ? value.trim() : '';
  if (!normalized || !path.isAbsolute(normalized)) {
    throw new Error('dsh homeDir must be an absolute path');
  }
  return path.normalize(normalized);
}

/**
 * Where one instance's DSH home, shared agent root and launch-patch directory
 * live. Paths only: nothing is created here.
 * @param {object} options
 * @param {string} options.dataDir - the instance data directory.
 * @param {'isolated'|'shared'} [options.home] - the configured placement.
 * @param {string} [options.homeDir] - the operator's home directory; only the
 *   shared placement reads it.
 * @returns {{mode: string, root: string, home: string, agents: string, run: string}}
 */
export function dshDirectoryLayout({ dataDir, home = DSH_HOME_MODES[0], homeDir } = {}) {
  if (typeof dataDir !== 'string' || !dataDir) throw new Error('dsh dataDir is required');
  const mode = normalizeDshHomeMode(home);
  if (mode === 'shared') {
    const userHome = absoluteHomeDir(homeDir);
    return Object.freeze({
      mode,
      root: userHome,
      home: path.join(userHome, DSH_SHARED_HOME_DIR),
      agents: path.join(userHome, DSH_SHARED_AGENTS_DIR),
      // The generated launch patch is OpenViking SuperAgent's own document and
      // names this instance's bridge, prompt and action socket: it stays local
      // to the instance even when the home is shared.
      run: path.join(dataDir, 'dsh', 'run'),
    });
  }
  const root = path.join(dataDir, 'dsh');
  return Object.freeze({
    mode,
    root,
    home: path.join(root, 'home'),
    agents: path.join(root, 'agents'),
    run: path.join(root, 'run'),
  });
}

/**
 * The `llm-pi-ai` settings document of one instance.
 * @param {object} options
 * @param {string} options.dataDir - the instance data directory.
 * @param {'isolated'|'shared'} [options.home] - the configured placement.
 * @param {string} [options.homeDir] - the operator's home directory.
 * @returns {string} the absolute path, whether or not it exists yet.
 */
export function dshProfilePatchPath({ dataDir, home, homeDir } = {}) {
  return path.join(dshDirectoryLayout({ dataDir, home, homeDir }).home, ...DSH_PROFILE_PATCH_SEGMENTS);
}

/**
 * The credential store that sits beside the settings document.
 * @param {object} options - as {@link dshProfilePatchPath}.
 * @returns {string} the absolute path, whether or not it exists yet.
 */
export function dshCredentialsDocumentPath({ dataDir, home, homeDir } = {}) {
  return path.join(dshDirectoryLayout({ dataDir, home, homeDir }).home, '.credentials.yaml');
}

/**
 * Content hash of the settings document, never its mtime: DSH rewrites the
 * document through its settings service, and a touched-but-identical file must
 * not restart the process (design §4.4).
 * @param {object} options
 * @param {string} options.dataDir - the instance data directory.
 * @param {'isolated'|'shared'} [options.home] - the configured placement.
 * @param {string} [options.homeDir] - the operator's home directory.
 * @returns {string|null} lowercase sha256 hex, or null when there is no document.
 */
export function dshProfilePatchHash({ dataDir, home, homeDir } = {}) {
  try {
    return createHash('sha256').update(fs.readFileSync(dshProfilePatchPath({ dataDir, home, homeDir }))).digest('hex');
  } catch {
    return null;
  }
}

// The bridge's own protocol version and the methods each caller depends on.
// v2 adds the model catalogue, model selection, the `llm-pi-ai` settings
// document, and credential writes. Names live under `superagent/` so a future SDK
// method with the same purpose can never be shadowed by this bridge.
export const DSH_BRIDGE_ID = 'superagent-dsh-bridge';
export const DSH_BRIDGE_VERSION = 2;
export const DSH_BRIDGE_DAEMON_METHODS = Object.freeze([
  'session/steer', 'session/cancel',
  'superagent/llm/models', 'superagent/llm/model/info', 'superagent/session/model/select',
]);
export const DSH_BRIDGE_CLI_METHODS = Object.freeze([
  ...DSH_BRIDGE_DAEMON_METHODS,
  'superagent/settings/describe', 'superagent/settings/mutate',
  'superagent/credentials/set', 'superagent/credentials/unset',
]);

/**
 * Whether a `superagent/hello` reply is the bridge this release drives.
 * @param hello - the reply result.
 * @param methods - methods the caller will use.
 * @returns true when the bridge id, version, and every method match.
 */
export function bridgeHelloSupports(hello, methods) {
  return hello?.bridge === DSH_BRIDGE_ID
    && Number.isSafeInteger(hello?.version) && hello.version >= DSH_BRIDGE_VERSION
    && Array.isArray(hello?.methods)
    && methods.every(method => hello.methods.includes(method));
}

// JSON-RPC code the bridge answers while a DSH service has not activated yet.
// `credentials` is the one that lags: it appeared ~1s after the bridge began
// answering, so every caller retries this code and nothing else.
export const DSH_NOT_READY_CODE = -32002;
// 100/200/400 then a 400ms floor, bounded by a 3s ceiling: the observed
// activation window is ~1s, and an unbounded retry would outlive the caller's
// own timeout.
const NOT_READY_BACKOFF_MS = Object.freeze([100, 200, 400]);
const NOT_READY_CEILING_MS = 3_000;

/**
 * Whether an error is the bridge's "service not mounted yet" answer.
 * @param error - the rejection from an SDK request.
 * @returns true for the retryable NOT_READY code only.
 */
export function isDshNotReady(error) {
  return error?.code === DSH_NOT_READY_CODE || error?.rpcCode === DSH_NOT_READY_CODE;
}

/**
 * Retry a request while the bridge reports NOT_READY. Every other error is
 * rethrown on the first attempt, so a real failure never costs 3 seconds.
 * @param run - issues one request attempt.
 * @param options.backoff - backoff schedule in milliseconds.
 * @param options.ceilingMs - total retry budget.
 * @param options.sleep - injectable timer for tests.
 * @param options.now - injectable clock for tests.
 * @returns the first successful result.
 */
export async function retryDshNotReady(run, {
  backoff = NOT_READY_BACKOFF_MS, ceilingMs = NOT_READY_CEILING_MS,
  sleep = defaultSleep, now = Date.now,
} = {}) {
  const deadline = now() + ceilingMs;
  for (let attempt = 0; ; attempt += 1) {
    try {
      return await run();
    } catch (error) {
      if (!isDshNotReady(error)) throw error;
      const wait = backoff[attempt] ?? backoff[backoff.length - 1];
      if (now() + wait > deadline) throw error;
      await sleep(wait);
    }
  }
}

function defaultSleep(ms) {
  return new Promise(resolve => { const timer = setTimeout(resolve, ms); timer.unref?.(); });
}

const SEMVER = /^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*)(?:\.(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*))*))?(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$/;

function numeric(value, version) {
  if (!/^(?:0|[1-9]\d*)$/.test(value)) throw new Error(`invalid DSH version: ${version}`);
  const number = Number(value);
  if (!Number.isSafeInteger(number)) throw new Error(`invalid DSH version: ${version}`);
  return number;
}

export function parseDshVersion(value) {
  const raw = String(value ?? '').trim();
  const match = SEMVER.exec(raw);
  if (!match) throw new Error(`invalid DSH version: ${raw || '(empty)'}; expected semver such as 0.2.2-rc.1`);
  return Object.freeze({
    raw,
    major: numeric(match[1], raw),
    minor: numeric(match[2], raw),
    patch: numeric(match[3], raw),
    prerelease: Object.freeze((match[4] ?? '').split('.').filter(Boolean).map(part => /^\d+$/.test(part) ? numeric(part, raw) : part)),
  });
}

function compareIdentifiers(left, right) {
  if (left === right) return 0;
  if (typeof left === 'number' && typeof right === 'string') return -1;
  if (typeof left === 'string' && typeof right === 'number') return 1;
  return left < right ? -1 : 1;
}

export function compareDshVersions(left, right) {
  const a = typeof left === 'string' ? parseDshVersion(left) : left;
  const b = typeof right === 'string' ? parseDshVersion(right) : right;
  for (const field of ['major', 'minor', 'patch']) {
    if (a[field] !== b[field]) return a[field] < b[field] ? -1 : 1;
  }
  if (a.prerelease.length === 0 || b.prerelease.length === 0) {
    if (a.prerelease.length === b.prerelease.length) return 0;
    return a.prerelease.length === 0 ? 1 : -1;
  }
  for (let index = 0; index < Math.max(a.prerelease.length, b.prerelease.length); index += 1) {
    if (a.prerelease[index] === undefined) return -1;
    if (b.prerelease[index] === undefined) return 1;
    const comparison = compareIdentifiers(a.prerelease[index], b.prerelease[index]);
    if (comparison) return comparison;
  }
  return 0;
}

export function assertSupportedDshVersion(value) {
  const version = parseDshVersion(value);
  if (compareDshVersions(version, DSH_SUPPORTED.min) < 0
    || version.major !== 0 || version.minor !== 2) {
    throw new Error(`unsupported DSH version ${version.raw}; requires >=${DSH_SUPPORTED.min} <${DSH_SUPPORTED.belowMajorMinor}.0`);
  }
  return version.raw;
}

export function assertDshNodeVersion(value = process.versions.node) {
  const version = parseDshVersion(value);
  if (version.major < 24 || (version.major === 24 && version.minor < 9)) {
    throw new Error(`dsh requires Node >= 24.9 (daemon runs ${version.raw})`);
  }
  return version.raw;
}

export function parseDshModel(value) {
  const raw = String(value ?? '').trim() || DSH_DEFAULT_MODEL;
  const slash = raw.indexOf('/');
  const provider = slash < 0 ? 'deepseek-official' : raw.slice(0, slash);
  const model = slash < 0 ? raw : raw.slice(slash + 1);
  if (!provider || !model) throw new Error(`invalid DSH model: ${raw}; expected provider/model`);
  return { provider, model };
}

/**
 * Create the directories the DSH runtime needs and return their layout.
 *
 * A shared home belongs to the operator's own DeepSeek Harness: it is created
 * when missing but never tightened, while the launch-patch directory is always
 * this instance's private one.
 * @param {string} dataDir - the instance data directory.
 * @param {object} [options]
 * @param {'isolated'|'shared'} [options.home] - the configured placement.
 * @param {string} [options.homeDir] - the operator's home directory.
 * @returns {{mode: string, root: string, home: string, agents: string, run: string}}
 */
export function prepareDshEnvironment(dataDir, { home = DSH_HOME_MODES[0], homeDir } = {}) {
  const directories = dshDirectoryLayout({ dataDir, home, homeDir });
  preparePrivateDirectory(path.join(dataDir, 'dsh'));
  if (directories.mode === 'shared') {
    fs.mkdirSync(directories.home, { recursive: true, mode: 0o700 });
    return Object.freeze({
      ...directories,
      run: preparePrivateDirectory(directories.run),
    });
  }
  return Object.freeze({
    mode: directories.mode,
    root: preparePrivateDirectory(directories.root),
    home: preparePrivateDirectory(directories.home),
    agents: preparePrivateDirectory(directories.agents),
    run: preparePrivateDirectory(directories.run),
  });
}

/**
 * The child environment of one DSH process: every inherited `DSH_*` is dropped
 * (it belongs to the operator's own DSH, not to this instance), then the home,
 * shared-agent root and unattended-run flags are set from the placement.
 * @param {object} environment - the inherited environment.
 * @param {object} options - `profile`, `actions`, `cliBins`, `dataDir`, `home`,
 *   `homeDir` and `execPath` (as before).
 * @returns {object} the sanitized environment.
 */
export function sanitizeDshEnv(environment, {
  profile = '', actions = null, cliBins = [], dataDir, home = DSH_HOME_MODES[0], homeDir,
  execPath = process.execPath,
} = {}) {
  const safeEnv = sanitizeAgentChildEnv(environment, { profile, actions, cliBins });
  for (const key of Object.keys(safeEnv)) if (/^DSH_/i.test(key)) delete safeEnv[key];
  if (!dataDir) throw new Error('dsh dataDir is required');
  const directories = prepareDshEnvironment(dataDir, { home, homeDir });
  Object.assign(safeEnv, {
    DSH_HOME: directories.home,
    DSH_AGENTS_HOME: directories.agents,
    DSH_PERMISSION_MODE: 'danger-full-access',
    DSH_TELEMETRY_DISABLED: '1',
  });
  const inherited = (safeEnv.PATH || '/usr/bin:/bin').split(path.delimiter).filter(Boolean);
  const nodeDirectory = path.dirname(execPath);
  safeEnv.PATH = [nodeDirectory, ...inherited.filter(entry => entry !== nodeDirectory)].join(path.delimiter);
  return safeEnv;
}

export function escapeDshTemplate(text) {
  return String(text ?? '').replaceAll('{{', '{\u2060{');
}

export function dshCommand({ bin = 'dsh', patchPath }) {
  if (!patchPath) throw new Error('dsh patchPath is required');
  return { command: bin, args: ['--profile', 'sdk', '--patch', patchPath] };
}

// JSON is a YAML subset. Keeping this file generated and private prevents a
// policy or action authority token from becoming editable shell/YAML syntax.
//
// The patch deliberately carries no `llm-pi-ai` entry: model routes live in
// `<DSH_HOME>/profiles/sdk/cordis.patch.yml`, which DSH's own settings service
// writes (design §1). A provider section here would make `superagent/settings/mutate`
// answer "overridden by a home patch or command-line overlay", so the CLI would
// be editing a document nothing reads.
export function buildDshPatch({
  policy = '', bridgePath = DSH_BRIDGE_PATH, mcp = null,
} = {}) {
  const insert = [];
  const patch = [];
  if (bridgePath !== null) {
    patch.push({ id: 'sdk-jsonrpc-server', disabled: true });
    insert.push({
      id: 'superagent-dsh-bridge', name: bridgePath,
      inject: ['sdkAppStartup', 'loader'],
      config: { maxTokensAsSuccess: true },
    });
  }
  if (mcp !== null) insert.push({
    id: 'superagent-personal-agent', name: '@deepseek-ai/dsh-mcp-client',
    config: {
      serverName: 'personal_agent', transport: 'stdio',
      command: mcp.command, args: [...mcp.args],
      failOnStartupError: true,
      ...(mcp.toolCallTimeoutMs ? { toolCallTimeoutMs: mcp.toolCallTimeoutMs } : {}),
    },
  });
  if (insert.length > 0) patch.push({ insert });
  patch.push({ id: 'system-prompt', config: { personaPrefix: escapeDshTemplate(policy) } });
  for (const id of ['tool-ask-user', 'schedule', 'tool-schedule', 'tool-plugin-manager', 'present', 'tool-subagent-fork']) {
    patch.push({ id, disabled: true });
  }
  return patch;
}

export function writeDshPatch({
  dataDir, home = DSH_HOME_MODES[0], homeDir, policy = '', bridgePath = DSH_BRIDGE_PATH, mcp = null,
} = {}) {
  const { run } = prepareDshEnvironment(dataDir, { home, homeDir });
  const patch = buildDshPatch({ policy, bridgePath, mcp });
  const patchPath = path.join(run, 'patch.yml');
  const temporary = `${patchPath}.${process.pid}.tmp`;
  const content = `${JSON.stringify(patch, null, 2)}\n`;
  fs.writeFileSync(temporary, content, { encoding: 'utf8', mode: 0o600 });
  fs.chmodSync(temporary, 0o600);
  fs.renameSync(temporary, patchPath);
  return patchPath;
}

