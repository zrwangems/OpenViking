---
type: simulink-block
title: 'Absolute Reference (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Elements'
documentation_page: 'absolutereferencema'
documentation_source_path: 'ref/absolutereferencema.html'
language: en
---

# Absolute Reference (MA)

## Ports
```yaml
ports:
- name: A
  summary: Pressure, temperature, specific humidity, and trace gas mass fraction are zero moist air
  direction: conserving
```

### Conserving

### **A** — Pressure, temperature, specific humidity, and trace gas mass fraction are zero moist air

Moist air conserving port where the pressure and temperature are equal
to absolute zero, and specific humidity and trace gas mass fraction are
equal to zero.
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Simscape / Foundation Library / Moist Air / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2023a: Absolute Reference (MA) block no longer recommended

The Pressure & Temperature Sensor (MA) block
now contains an implicit reference node, which means that you need only one port to
make absolute measurements of pressure or temperature. Expose the second port only
if you need to measure the difference in pressure or temperature between two nodes
in the model.

In previous releases, to measure the absolute pressure and absolute temperature at
port **A**, you needed to connect port **B** to an
Absolute Reference (MA) block. This is no longer
necessary because you can now make absolute measurements by setting the
**Measurement reference** parameter of the
Pressure & Temperature Sensor (MA) block to
`Absolute`.

This change has no compatibility impact. Existing models that have an
Absolute Reference (MA) block connected to a
Pressure & Temperature Sensor (MA) block
continue to work as before.

## Description

(Not recommended) Reference point at zero absolute temperature and pressure

The Absolute Reference (MA) block represents an
absolute reference for the pressure and temperature in a moist air network. At port
**A**, the pressure and temperature are equal to absolute zero.
Specific humidity and trace gas mass fraction are also equal to zero.

Unlike other domains, where each topologically distinct circuit within a domain must
contain at least one reference block, moist air networks do not have this requirement.
For more information, see Reference Node and Grounding Rules.

The purpose of the Absolute Reference (MA) block is to
provide a reference for the Pressure & Temperature Sensor
(MA). For example, to measure the absolute pressure and absolute
temperature of a node, connect that node to the **A** port of a
Pressure & Temperature Sensor (MA) block. Connect
the **B** port of the Pressure & Temperature Sensor
(MA) block to an Absolute Reference
(MA) block.

If you use the Absolute Reference (MA) block elsewhere
in a moist air network, it triggers a simulation assertion because air mixture pressure
and temperature cannot be at absolute zero.
