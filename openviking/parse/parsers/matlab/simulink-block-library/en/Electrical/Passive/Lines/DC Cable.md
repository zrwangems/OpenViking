---
type: simulink-block
title: 'DC Cable'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Lines'
documentation_page: 'dccable'
documentation_source_path: 'ref/dccable.html'
language: en
---

# DC Cable

## Ports
```yaml
ports:
- name: c+
  summary: Core conductor positive terminal electrical
  direction: conserving
- name: c-
  summary: Core conductor negative terminal electrical
  direction: conserving
- name: s+
  summary: Sheath positive terminal electrical
  direction: conserving
- name: s-
  summary: Sheath negative terminal electrical
  direction: conserving
- name: a+
  summary: Armor positive terminal electrical
  direction: conserving
- name: a-
  summary: Armor negative terminal electrical
  direction: conserving
- name: c1+
  summary: Positive terminal of first cable core conductor electrical
  direction: conserving
- name: c1-
  summary: Negative terminal of first cable core conductor electrical
  direction: conserving
- name: s1+
  summary: Positive terminal of first cable sheath electrical
  direction: conserving
- name: s1-
  summary: Negative terminal of first cable sheath electrical
  direction: conserving
- name: a1+
  summary: Positive terminal of first cable armor electrical
  direction: conserving
- name: a1-
  summary: Negative terminal of first cable armor electrical
  direction: conserving
- name: c2+
  summary: Positive terminal of second cable core conductor electrical
  direction: conserving
- name: c2-
  summary: Negative terminal of second cable core conductor electrical
  direction: conserving
- name: s2+
  summary: Positive terminal of second cable sheath electrical
  direction: conserving
- name: s2-
  summary: Negative terminal of second cable sheath electrical
  direction: conserving
- name: a2+
  summary: Positive terminal of second cable armor electrical
  direction: conserving
- name: a2-
  summary: Negative terminal of second cable armor electrical
  direction: conserving
```

### Conserving

### **c+** — Core conductor positive terminal electrical

Electrical conserving port associated with the positive terminal of the cable core
conductor.

#### Dependencies

To enable this port, set the **Configuration** parameter to
`Single cable`.

### **c-** — Core conductor negative terminal electrical

Electrical conserving port associated with the negative terminal of the cable core
conductor.

#### Dependencies

To enable this port, set the **Configuration** parameter to
`Single cable`.

### **s+** — Sheath positive terminal electrical

Electrical conserving port associated with the positive terminal of the cable
sheath.

#### Dependencies

To enable this port, set the **Configuration** parameter to
`Single cable`.

### **s-** — Sheath negative terminal electrical

Electrical conserving port associated with the negative terminal of the cable
sheath.

#### Dependencies

To enable this port, set the **Configuration** parameter to
`Single cable`.

### **a+** — Armor positive terminal electrical

Electrical conserving port associated with the positive terminal of the cable
armor.

#### Dependencies

To enable this port, set the **Configuration** parameter to
`Single cable`.

### **a-** — Armor negative terminal electrical

Electrical conserving port associated with the negative terminal of the cable
sheath.

#### Dependencies

To enable this port, set the **Configuration** parameter to
`Single cable`.

### **c1+** — Positive terminal of first cable core conductor electrical

Electrical conserving port associated with the positive terminal of the core
conductor of the first cable.

#### Dependencies

To enable this port, set the **Configuration** parameter to
`Double cable`.

### **c1-** — Negative terminal of first cable core conductor electrical

Electrical conserving port associated with the negative terminal of the core
conductor of the first cable.

#### Dependencies

To enable this port, set the **Configuration** parameter to
`Double cable`.

### **s1+** — Positive terminal of first cable sheath electrical

Electrical conserving port associated with the positive terminal of the sheath of
the first cable.

#### Dependencies

To enable this port, set the **Configuration** parameter to
`Double cable`.

### **s1-** — Negative terminal of first cable sheath electrical

Electrical conserving port associated with the negative terminal of the sheath of
the first cable.

#### Dependencies

To enable this port, set the **Configuration** parameter to
`Double cable`.

### **a1+** — Positive terminal of first cable armor electrical

Electrical conserving port associated with the positive terminal of the armor of
the first cable.

#### Dependencies

To enable this port, set the **Configuration** parameter to
`Double cable`.

### **a1-** — Negative terminal of first cable armor electrical

Electrical conserving port associated with the negative terminal of the armor of
the first cable.

#### Dependencies

To enable this port, set the **Configuration** parameter to
`Double cable`.

### **c2+** — Positive terminal of second cable core conductor electrical

Electrical conserving port associated with the positive terminal of the core
conductor of the second cable.

#### Dependencies

To enable this port, set the **Configuration** parameter to
`Double cable`.

### **c2-** — Negative terminal of second cable core conductor electrical

Electrical conserving port associated with the negative terminal of the core
conductor of the second cable.

#### Dependencies

To enable this port, set the **Configuration** parameter to
`Double cable`.

### **s2+** — Positive terminal of second cable sheath electrical

Electrical conserving port associated with the positive terminal of the sheath of
the second cable.

#### Dependencies

To enable this port, set the **Configuration** parameter to
`Double cable`.

### **s2-** — Negative terminal of second cable sheath electrical

Electrical conserving port associated with the negative terminal of the sheath of
the second cable.

#### Dependencies

To enable this port, set the **Configuration** parameter to
`Double cable`.

### **a2+** — Positive terminal of second cable armor electrical

Electrical conserving port associated with the positive terminal of the armor of
the second cable.

#### Dependencies

To enable this port, set the **Configuration** parameter to
`Double cable`.

### **a2-** — Negative terminal of second cable armor electrical

Electrical conserving port associated with the negative terminal of the armor of
the second cable.

#### Dependencies

To enable this port, set the **Configuration** parameter to
`Double cable`.
## Parameters
```yaml
parameters:
- name: Configuration
  summary: Option to model single or double cables Single cable (default) | Double cable
  group: Main
- name: Environmental resistivity
  summary: Resistance of earth return 100 Ohm*m (default) | positive scalar
  group: Main
- name: Cable length
  summary: Length of cable 100 km (default) | scalar greater than 1 m
  group: Main
- name: Core conductor resistivity
  summary: Resistivity of core conductor 2.1e-8 Ohm*m (default) | positive scalar
  group: Electrical Parameters
- name: Core conductor relative permeability
  summary: Relative permeability of core conductor 1 (default) | positive scalar
  group: Electrical Parameters
- name: Insulation relative permeability
  summary: Relative permeability of insulation 1 (default) | positive scalar
  group: Electrical Parameters
- name: Insulation relative permittivity
  summary: Relative permittivity of insulation 2.5 (default) | positive scalar
  group: Electrical Parameters
- name: Sheath resistivity
  summary: Resistivity of sheath 2.2e-7 Ohm*m (default) | positive scalar
  group: Electrical Parameters
- name: Sheath relative permeability
  summary: Relative permeability of sheath 1 (default) | positive scalar
  group: Electrical Parameters
- name: Inner jacket relative permeability
  summary: Relative permeability of inner jacket 1 (default) | positive scalar
  group: Electrical Parameters
- name: Inner jacket relative permittivity
  summary: Relative permittivity of inner jacket 2.4 (default) | positive scalar
  group: Electrical Parameters
- name: Armor resistivity
  summary: Resistivity of armor 1.8e-7 Ohm*m (default) | positive scalar
  group: Electrical Parameters
- name: Armor relative permeability
  summary: Relative permeability of armor 10 (default) | positive scalar
  group: Electrical Parameters
- name: Serving relative permeability
  summary: Relative permeability of serving 1 (default) | positive scalar
  group: Electrical Parameters
- name: Serving relative permittivity
  summary: Relative permittivity of serving 2.4 (default) | positive scalar
  group: Electrical Parameters
- name: Core conductor radial thickness
  summary: Radial thickness of core conductor 25 mm (default) | positive scalar
  group: Geometric Dimensions
- name: Insulation radial thickness
  summary: Radial thickness of insulation 20 mm (default) | positive scalar
  group: Geometric Dimensions
- name: Sheath radial thickness
  summary: Radial thickness of sheath 3 mm (default) | positive scalar
  group: Geometric Dimensions
- name: Inner jacket radial thickness
  summary: Radial thickness of inner jacket 5 mm (default) | positive scalar
  group: Geometric Dimensions
- name: Armor radial thickness
  summary: Radial thickness of armor 6 mm (default) | positive scalar
  group: Geometric Dimensions
- name: Serving radial thickness
  summary: Radial thickness of serving 5 mm (default) | positive scalar
  group: Geometric Dimensions
- name: Vertical depth of the cable
  summary: Vertical position of cable 1 m (default) | [1, 1] | positive scalar or vector of two positive elements
  group: Geometric Dimensions
- name: Horizontal position of the cable
  summary: Horizontal position of cable [0, 1] m (default) | vector of two elements
  group: Geometric Dimensions
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Configuration** — Option to model single or double cables `Single cable` (default) | `Double cable`

Option to model the block as a single DC cable or double DC cables.

### **Environmental resistivity** — Resistance of earth return `100` `Ohm*m` (default) | positive scalar

Resistance of the earth return.

### **Cable length** — Length of cable `100` `km` (default) | scalar greater than `1` `m`

Length of the cable.

### Electrical Parameters

### **Core conductor resistivity** — Resistivity of core conductor `2.1e-8` `Ohm*m` (default) | positive scalar

Resistivity of the core conductor.

### **Core conductor relative permeability** — Relative permeability of core conductor `1` (default) | positive scalar

Relative permeability of the core conductor.

### **Insulation relative permeability** — Relative permeability of insulation `1` (default) | positive scalar

Relative permeability of the insulation.

### **Insulation relative permittivity** — Relative permittivity of insulation `2.5` (default) | positive scalar

Relative permittivity of the insulation.

### **Sheath resistivity** — Resistivity of sheath `2.2e-7` `Ohm*m` (default) | positive scalar

Resistivity of the sheath.

### **Sheath relative permeability** — Relative permeability of sheath `1` (default) | positive scalar

Relative permeability of the sheath.

### **Inner jacket relative permeability** — Relative permeability of inner jacket `1` (default) | positive scalar

Relative permeability of the inner jacket.

### **Inner jacket relative permittivity** — Relative permittivity of inner jacket `2.4` (default) | positive scalar

Relative permittivity of the inner jacket.

### **Armor resistivity** — Resistivity of armor `1.8e-7` `Ohm*m` (default) | positive scalar

Resistivity of the armor.

### **Armor relative permeability** — Relative permeability of armor `10` (default) | positive scalar

Relative permeability of the armor.

### **Serving relative permeability** — Relative permeability of serving `1` (default) | positive scalar

Relative permeability of the serving.

### **Serving relative permittivity** — Relative permittivity of serving `2.4` (default) | positive scalar

Relative permittivity of the serving.

### Geometric Dimensions

### **Core conductor radial thickness** — Radial thickness of core conductor `25` `mm` (default) | positive scalar

Radial thickness of the core conductor.

### **Insulation radial thickness** — Radial thickness of insulation `20` `mm` (default) | positive scalar

Radial thickness of the insulation.

### **Sheath radial thickness** — Radial thickness of sheath `3` `mm` (default) | positive scalar

Radial thickness of the sheath.

### **Inner jacket radial thickness** — Radial thickness of inner jacket `5` `mm` (default) | positive scalar

Radial thickness of the inner jacket.

### **Armor radial thickness** — Radial thickness of armor `6` `mm` (default) | positive scalar

Radial thickness of the armor.

### **Serving radial thickness** — Radial thickness of serving `5` `mm` (default) | positive scalar

Radial thickness of the serving

### **Vertical depth of the cable** — Vertical position of cable `1` `m` (default) | `[1, 1]` | positive scalar or vector of two positive elements

Vertical position, `y`, of the cable, as shown in this figure:

Cross section of the cable and its vertical position.

If you set the **Configuration** parameter to `Double
cable`, this parameter value is a vector of two positive elements,
`y1` and
`y2`, and the default value is
`[1, 1]`, as shown in this figure:

Cross section of two cables and their vertical and horizontal positions.

### **Horizontal position of the cable** — Horizontal position of cable `[0, 1]` `m` (default) | vector of two elements

Horizontal position of the cable.

This figure shows the horizontal positions for a double cables configuration:

Cross section of two cables and their vertical and horizontal positions.

You specify these values with respect to the origin point. As such,
these values can be positive or negative.

#### Dependencies

To enable this parameter, set **Configuration** to
`Double cable`.
## Libraries

Simscape / Electrical / Passive / Lines

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

High-fidelity frequency-dependent DC cable

The DC Cable block models a DC power cable that simulates
the transient response with high precision in high-voltage direct-current (HVDC) transmission
applications.

This figure shows the cross section of a cable. There are six concentric layers: core
conductor, insulation, sheath, inner jacket, armor, and serving.

Cross section of a cable. There are six concentric layers: core conductor, insulation, sheath, inner jacket, armor, and serving.

### Equations

To obtain an accurate transient response during simulation, this block models a DC cable
using a frequency-dependent modeling approach. For more information about the
frequency-dependent modeling of lines, see the Equations section of the
Frequency-Dependent Overhead Line (Three-Phase)
block.

To use the frequency-dependent modeling approach, the block must first calculate the
frequency-dependent cable parameters, such as the series impedance and shunt admittance
matrices by using Dommel electromagnetic transients program (EMTP) equations. For more
information about these equations, see [1].
