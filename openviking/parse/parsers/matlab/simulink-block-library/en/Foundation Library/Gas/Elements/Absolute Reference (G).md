---
type: simulink-block
title: 'Absolute Reference (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Gas / Elements'
documentation_page: 'absolutereferenceg'
documentation_source_path: 'ref/absolutereferenceg.html'
language: en
---

# Absolute Reference (G)

## Ports
```yaml
ports:
- name: A
  summary: Pressure and temperature are zero gas
  direction: conserving
```

### Conserving

### **A** — Pressure and temperature are zero gas

Gas conserving port where the pressure and temperature are both equal
to zero.
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Simscape / Foundation Library / Gas / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

### R2023a: Absolute Reference (G) block no longer recommended

The Pressure & Temperature Sensor (G) block now
contains an implicit reference node, which means that you need only one port to make
absolute measurements of pressure or temperature. Expose the second port only if you
need to measure the difference in pressure or temperature between two nodes in the
model.

In previous releases, to measure the absolute pressure and absolute temperature at
port **A**, you needed to connect port **B** to an
Absolute Reference (G) block. This is no longer
necessary because you can now make absolute measurements by setting the
**Measurement reference** parameter of the
Pressure & Temperature Sensor (G) block to
`Absolute`.

This change has no compatibility impact. Existing models that have an
Absolute Reference (G) block connected to a
Pressure & Temperature Sensor (G) block
continue to work as before.

## Description

(Not recommended) Reference point at zero absolute temperature and pressure

The Absolute Reference (G) block represents an absolute reference for
the pressure and temperature in a gas network. At port **A**, the
pressure and temperature are both equal to zero.

Unlike other domains, where each topologically distinct circuit within a domain must
contain at least one reference block, gas networks do not have this requirement. For
more information, see Reference Node and Grounding Rules.

The purpose of the Absolute Reference (G) block is to provide a
reference for the Pressure & Temperature Sensor (G). To measure the
absolute pressure and absolute temperature of a node, connect that node to the
**A** port of a Pressure & Temperature Sensor
(G) block. Connect the **B** port of the Pressure
& Temperature Sensor (G) block to an Absolute Reference
(G) block.

If you use the Absolute Reference (G) block elsewhere in a gas network,
it triggers a simulation assertion because gas pressure and temperature cannot be at
absolute zero.
