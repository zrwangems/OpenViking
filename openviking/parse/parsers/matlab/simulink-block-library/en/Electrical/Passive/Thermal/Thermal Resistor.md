---
type: simulink-block
title: 'Thermal Resistor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Thermal'
documentation_page: 'thermalresistor'
documentation_source_path: 'ref/thermalresistor.html'
language: en
---

# Thermal Resistor

## Ports
```yaml
ports:
- name: A
  summary: Surface A thermal
  direction: conserving
- name: B
  summary: Surface B thermal
  direction: conserving
```

### Conserving

### **A** — Surface A thermal

Thermal conserving port associated with surface A of the material that
the heat flows through.

### **B** — Surface B thermal

Thermal conserving port associated with surface B of the material that
the heat flows through.
## Parameters
```yaml
parameters:
- name: Thermal resistance
  summary: Thermal resistance 1e-3 K/W (default)
  group: ''
```

### **Thermal resistance** — Thermal resistance `1e-3` `K/W` (default)

Thermal resistance,
*Rthermal*.
## Libraries

Simscape / Electrical / Passive / Thermal

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016a**

## Description

Heat transfer by conduction through a layer of material

The Thermal Resistor block represents heat transfer by
conduction through a layer of material. The heat transfer is:

- Governed by Fourier’s law
- Proportional to the temperature difference across the layer of
  material
- Inversely proportional to the thermal resistance of the material

The equation for conductive heat transfer is:

QAB=TABRthermal,

where:

- *QAB* is the heat flow through the
  material.
- *TAB* is the temperature
  difference across the layer of material.
- *Rthermal* is the thermal
  resistance of the material.

Thermal resistance can be calculated as:

Rthermal=DkA,

where:

- *D* is the thickness of the layer of material.
- *k* is the thermal conductivity of the material.
- *A* is the area normal to the heat flow direction.

Use the Thermal Resistor block to parameterize an
equivalent component in terms of thermal resistance of the material layer. To
parameterize an equivalent component in terms of the thickness, thermal conductivity,
and area of the material layer, use the Conductive Heat Transfer block from the Simscape™ Foundation library.

### Variables

To set the priority and initial target values for the block variables prior to simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
