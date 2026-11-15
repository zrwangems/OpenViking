---
type: simulink-block
title: 'Variable Overlapping Orifice (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid Library / Valves and Orifices / Orifices'
documentation_page: 'variableoverlappingorificeil'
documentation_source_path: 'ref/variableoverlappingorificeil.html'
language: en
---

# Variable Overlapping Orifice (IL)

## Ports

### Conserving

### **A** — Liquid port isothermal liquid

Entry or exit point to the orifice.

### **B** — Liquid port isothermal liquid

Entry or exit point to the orifice.
### Input

### **S** — Sleeve displacement, m physical signal

Sleeve position with respect to the case, in m.

## Parameters

### **Sleeve hole diameter** — Sleeve hole diameter `5e-3 m` (default) | positive scalar

Diameter of the hole in the moving element.

### **Case hole diameter** — Case hole diameter `5.5e-3 m` (default) | positive scalar

Diameter of hole in the fixed element.

### **Sleeve position when holes are concentric** — Moving element position when hole centers are aligned `0 m` (default) | scalar

Moving element position when hole centers are aligned. This parameter is
used to the determine instantaneous overlap of the moving and stationary
holes during simulation by comparison with the signal received at port
**S**.

### **Number of interacting pairs** — Number of overlapping orifices, in pairs `1` (default) | positive scalar

Number of overlapping orifices, in pairs. The sleeve-case pairs do not
need to be aligned in the physical hardware being modeled.

### **Leakage area** — Gap area when in fully closed position `1e-10 m^2` (default) | positive scalar

Sum of all gaps when the valve is in the fully closed position. Any area
smaller than this value is maintained at the specified leakage area. This
contributes to numerical stability by maintaining continuity in the
flow.

### **Cross-sectional area at ports A and B** — Orifice area at conserving ports `inf m^2` (default) | positive scalar

Areas at the entry and exit ports **A** and
**B**, which are used in the pressure-flow rate
equation that determines the mass flow rate through the orifice.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Correction factor that accounts for discharge losses in theoretical
flows.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the orifice.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range [0,1]

Continuous smoothing factor that introduces a layer of gradual change to the flow response
when the valve is in near-open or near-closed positions. Set this value to a
nonzero value less than one to increase the stability of your simulation in
these regimes.

### **Pressure recovery** — Whether to account for pressure increase in area expansions `Off` (default) | `On`

Whether to account for pressure increase when fluid flows from a region of
smaller cross-sectional area to a region of larger cross-sectional
area.

## Libraries

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Orifices

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Orifice created by open segments with variable overlap in an isothermal liquid system

The Variable Overlapping Orifice (IL) block models flow through round holes with
varying overlapping areas, such as a moving sleeve within a fixed case. The overlapping
holes can have different diameters, but additional holes along the spool or sleeve have
the same diameter.

### Overlapping Area

The flow rate depends on the variable open area created by overlapping holes in
the sleeve and casing. This instantaneous opening area is calculated as:

Aoverlap=r2[cos−1(C2+r2−R22Cr)−(C2+r2−R22Cr)1−(C2+r2−R22Cr)2]+R2[cos−1(C2−r2+R22CR)−(C2−r2+R22CR)1−(C2−r2+R22CR)2],

where:

- *r* is the diameter of the smaller hole.
- *R* is the diameter of the larger hole.
- *C* is the absolute distance between the hole centers,
  calculated from the physical signal at port **S**, the
  instantaneous sleeve position, and the **Sleeve position when holes
  are concentric**, *S*0: C=|S−S0|.

If the holes on the sleeve and casing have the same diameter, the overlap area
becomes:

Aoverlap=2r2[cos−1(C2r)−(C2r)1−(C2r)2].

You can maintain numerical robustness in your simulation by adjusting the block
**Smoothing factor** at the nearest and farthest points
between hole centers. The block applies a smoothing function to the normalized hole
center distance,

C^=(C−R+r)(2r).

The function smoothly saturates the normalized hole center distance between
`0` and `1`.

For more information, see Numerical Smoothing

### Mass Flow Rate Equation

The flow through an orifice pair is calculated from the pressure-area relationship:

m˙=CdAorifice2ρ¯PRloss(1−(AorificeAport)2)Δp[Δp2+Δpcrit2]1/4,

where:

- *C*d is the
  **Discharge coefficient**.
- *A*orifice is the area open to
  flow, Aorifice=Aoverlap+Aleak.
- *A* is the **Cross-sectional area at ports A
  and B**.
- ρ¯ is the average fluid density.

*Pressure loss* describes the reduction of pressure in the
valve due to a decrease in area. The pressure loss term,
*PR*loss is calculated as:

PRloss=1−(AoverlappingAport)2(1−Cd2)−CdAoverlappingAport1−(AoverlappingAport)2(1−Cd2)+CdAoverlappingAport.

*Pressure recovery* describes the positive
pressure change in the valve due to an increase in area. If you do not wish to
capture this increase in pressure, set **Pressure recovery** to
`Off`. In this case,
*PR*loss is 1.

The critical pressure difference,
*Δp*crit, is the pressure differential
associated with the **Critical Reynolds number**,
*Re*crit, the flow regime transition
point between laminar and turbulent flow:

Δpcrit=πρ¯8Aoverlapping(νRecritCd)2.
