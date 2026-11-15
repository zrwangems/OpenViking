---
type: simulink-block
title: 'Laminar Leakage (IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Isothermal Liquid Models / Elements'
documentation_page: 'laminarleakageil'
documentation_source_path: 'ref/laminarleakageil.html'
language: en
---

# Laminar Leakage (IL)

## Ports

### Conserving

### **A** — Inlet or outlet isothermal liquid

Isothermal liquid conserving port associated with the inlet or outlet of the
laminar leakage. This block has no intrinsic directionality.

### **B** — Inlet or outlet isothermal liquid

Isothermal liquid conserving port associated with the inlet or outlet of the
laminar leakage. This block has no intrinsic directionality.

## Parameters

### **Cross-sectional geometry** — Select the shape of the leakage cross section `Circular` (default) | `Annular` | `Rectangular` | `Elliptical` | `Equilateral triangular` | `Custom`

Select a cross-sectional shape and then specify other parameter values based on the
selected option.

### **Diameter** — Diameter of the circular cross section `1e-3 m` (default) | positive scalar

Diameter of the circular cross section.

#### Dependencies

Enabled when the **Cross-sectional geometry** parameter is set to
`Circular`.

### **Inner diameter** — Inner diameter of the annular cross section `5e-4 m` (default) | positive scalar

Inner diameter of the annular cross section.

#### Dependencies

Enabled when the **Cross-sectional geometry** parameter is set to
`Annular`.

### **Outer diameter** — Outer diameter of the annular cross section `1e-3 m` (default) | positive scalar

Outer diameter of the annular cross section.

#### Dependencies

Enabled when the **Cross-sectional geometry** parameter is set to
`Annular`.

### **Width** — Width of the rectangular cross section `1e-3 m` (default) | positive scalar

Width of the rectangular cross section.

#### Dependencies

Enabled when the **Cross-sectional geometry** parameter is set to
`Rectangular`.

### **Height** — Height of the rectangular cross section `0.1 m` (default) | positive scalar

Height of the rectangular cross section.

#### Dependencies

Enabled when the **Cross-sectional geometry** parameter is set to
`Rectangular`.

### **Major axis** — Major axis of the elliptical cross section `1e-3 m` (default) | positive scalar

Major axis of the elliptical cross section.

#### Dependencies

Enabled when the **Cross-sectional geometry** parameter is set to
`Elliptical`.

### **Minor axis** — Minor axis of the elliptical cross section `5e-4 m` (default) | positive scalar

Minor axis of the elliptical cross section.

#### Dependencies

Enabled when the **Cross-sectional geometry** parameter is set to
`Elliptical`.

### **Side length** — Length of the triangle side for the equilateral triangular cross section `1e-3 m` (default) | positive scalar

Length of the triangle side for the equilateral triangular cross section.

#### Dependencies

Enabled when the **Cross-sectional geometry** parameter is set to
`Equilateral triangular`.

### **Longitudinal length** — Length of the flow passage `5 m` (default) | positive scalar

Length of the flow passage.

### **Linear pressure-flow resistance** — Ratio of pressure loss to mass flow rate 1e3 s\*MPa/m^3 (default) | positive scalar

Ratio of pressure loss to the mass flow rate. If cross-sectional geometry is not
known, the block acts as a linear hydraulic resistance.

#### Dependencies

Enabled when the **Cross-sectional geometry** parameter is set to
`Custom`.

## Libraries

Simscape / Foundation Library / Isothermal Liquid / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Isothermal liquid element that models laminar leakage flow for various geometries

The Laminar Leakage (IL) block models laminar flow in
isothermal liquid networks. The block includes several common flow passage geometries and a
custom geometry. Select a **Cross-sectional geometry** parameter value and
then specify other parameter values based on the selected option:

- `Circular` — Provide the diameter and longitudinal
  length.
- `Annular` — Provide the inner diameter, outer diameter, and
  longitudinal length.
- `Rectangular` — Provide the width, height, and longitudinal
  length.
- `Elliptical` — Provide the major axis, minor axis, and
  longitudinal length.
- `Equilateral triangular` — Provide the length of the triangle
  side and longitudinal length.
- `Custom` — Provide the flow resistance value, that is, the
  ratio of pressure loss to mass flow rate. In this configuration, the block acts as a
  linear hydraulic resistance.

The flow rate calculations are based on the Hagen-Poiseuille equation, which is valid for
fully developed laminar flow:

m˙A={KgeomνL(pA−pB),common geometriesρ¯R(pA−pB),custom

Kgeom={πd4128,circularπ128(do4−di4−(do2−di2)2log(do/di)),annularwh312(1−192hwπ5tanh(πw2h)),rectangularπ(ab)364(a2+b2),ellipticallside43320,triangular

ρ¯=ρA+ρB2

where:

- m˙A is the mass flow rate through port
  **A**.
- *p*A and
  *p*B are pressures at ports
  **A** and **B**, respectively.
- *K*geom is the coefficient calculated based on
  the cross-sectional geometry.
- *d* is the diameter of the circular cross section.
- *d*o is the outer diameter of the annular
  cross section.
- *d*i is the inner diameter of the annular
  cross section.
- *w* is the width of the rectangular cross section.
- *h* is the height of the rectangular cross section.
- *a* is the major axis of the elliptical cross section.
- *b* is the minor axis of the elliptical cross section.
- *l*side is the length of the side of the
  triangular cross section.
- *L* is the longitudinal length.
- *R* is the linear hydraulic resistance for custom geometry.
- *ν* is the liquid kinematic viscosity at atmospheric pressure, which
  is a global parameter defined by the Isothermal Liquid Properties
  (IL) block connected to the circuit.
- ρ¯ is the average fluid mixture density.
- *ρ*A and
  *ρ*B are fluid mixture density values at ports
  **A** and **B**, respectively. Equations used to
  compute the fluid mixture density depend on the selected isothermal liquid model. For
  detailed information, see Isothermal Liquid Modeling Options.
