---
type: simulink-block
title: 'Absolute Reference (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Two-Phase Fluid Models / Elements'
documentation_page: 'absolutereference2p'
documentation_source_path: 'ref/absolutereference2p.html'
language: en
---

# Absolute Reference (2P)

## Ports

Not documented in R2025b.

## Parameters

Not documented in R2025b.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015b**

### R2023a: Absolute Reference (2P) block no longer recommended

The Pressure & Temperature Sensor (2P) block
now contains an implicit reference node, which means that you need only one port to
make absolute measurements of pressure or temperature. Expose the second port only
if you need to measure the difference in pressure or temperature between two nodes
in the model.

In previous releases, to measure the absolute pressure and absolute temperature at
port **A**, you needed to connect port **B** to an
Absolute Reference (2P) block. This is no longer
necessary because you can now make absolute measurements by setting the
**Measurement reference** parameter of the
Pressure & Temperature Sensor (2P) block to
`Absolute`.

This change has no compatibility impact. Existing models that have an
Absolute Reference (2P) block connected to a
Pressure & Temperature Sensor (2P) block
continue to work as before.

## Description

(Not recommended) Reference point at zero absolute pressure and specific internal energy
