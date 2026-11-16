---
type: simulink-block
title: 'Permanent Magnet'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Electromagnetic Models / Magnetic Elements'
documentation_page: 'permanentmagnet'
documentation_source_path: 'ref/permanentmagnet.html'
language: en
---

# Permanent Magnet

## Ports

### Conserving

### **N** — North terminal magnetic

Magnetic conserving port associated with the north terminal.

### **S** — South terminal magnetic

Magnetic conserving port associated with the south terminal.

## Parameters

### **Cross-sectional area** — Cross-sectional area of magnet `25 mm^2` (default) | positive scalar

Cross-sectional area of the magnet.

### **Length of magnet** — Length of magnet `0.02 m` (default) | positive scalar

Length of the magnet.

### **Remanent field parameterization** — Method of remanent field parameterization `Remanent flux density and relative permeability` (default) | `Remanent flux density and coercivity` | `Relative permeability and coercivity`

Method for parameterizing the linear *B*-*H*
relationship.

### **Relative magnetic permeability of material** — Relative magnetic permeability `1.05` (default) | positive scalar

Relative magnetic permeability of the material.

#### Dependencies

To enable this parameter, set **Remanent field parameterization**
to `Remanent flux density and relative permeability` or
`Relative permeability and coercivity`.

### **Remanent flux density of magnet** — Remanent flux density `1.2 T` (default) | positive scalar

Flux density of the magnet after you remove the external magnetic field.

#### Dependencies

To enable this parameter, set **Remanent field parameterization**
to `Remanent flux density and relative permeability` or
`Remanent flux density and coercivity`.

### **Coercivity of magnet** — Coercivity of magnet `1.2 / 1.05 / (4*pi*1e-7) A/m` (default) | positive scalar

Coercivity of the magnet.

#### Dependencies

To enable this parameter, set **Remanent field parameterization**
to `Remanent flux density and coercivity` or `Relative
permeability and coercivity`.

## Libraries

Simscape / Foundation Library / Magnetic / Magnetic Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

## Description

Permanent magnet that passively generates magnetic field

The Permanent Magnet block models a component that
passively generates a magnetic field. Use this block to model a magnet that does not magnetize
or demagnetize. The magnetic field of the permanent magnet has a magnetic flux density that
increases linearly with an increase in the strength of the external magnetic field.

The Permanent Magnet  block is equivalent to a
Flux Source block and a Reluctance block in parallel or an MMF
Source block and a Reluctance block in
series. To parameterize the magnet from manufacturer specifications of remanent flux density,
magnetic permeability, or coercivity, use the Permanent Magnet
block.

### Equations

When you subject the Permanent Magnet block to an
external magnetic field, the block approximates the flux density *B* of the
resultant magnetic field using one of these linear relationships:

B=Br+μmμ0H

B=BrHc(Hc+H)

B=μmμ0(Hc+H)

where:

- *B*r is the **Remanent flux
  density of magnet** parameter.
- *μ*m is the **Relative magnetic
  permeability of material** parameter.
- μ0 is the magnetic permeability in a vacuum.
- *H* is the strength of the external magnetic field.
- *H*c is the **Coercivity of
  magnet** parameter.

Specify which parameters the block uses to define the linear equation using the
**Remanent field parametrization** parameter.

The linear relationship is valid only when the magnet does not magnetize or demagnetize.
The block operates in the second quadrant of the *B*-*H*
curve:

- *B* ≥ 0
- *H* ≤ 0

The magnetic flux *φ* flowing through the magnet is defined as:

*φ* = *A**B*,

where *A* is the **Cross-sectional
area** parameter.

The magnetomotive force (mmf) across the block is defined as:

*MMF* =
*H**l*,

where *l* is the **Length of magnet**
parameter.

The mmf across the block is defined as:

*MMF* = *MMF(N)* -
*MMF(S)*,

where *N* and *S* are the north and
south terminals of the permanent magnet, respectively. The flux is positive when the flux
flows through the device from the north to the south terminal.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
