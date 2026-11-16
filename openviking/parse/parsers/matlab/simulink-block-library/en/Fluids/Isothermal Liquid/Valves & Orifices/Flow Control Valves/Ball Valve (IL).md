---
type: simulink-block
title: 'Ball Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Flow Control Valves'
documentation_page: 'ballvalveil'
documentation_source_path: 'ref/ballvalveil.html'
language: en
---

# Ball Valve (IL)

## Ports

### Input

### **S** — Valve position, rad physical signal

Physical signal port associated with the position of the valve, in rad. A value of 0
represents a fully shut valve and a value of π/2 represents a fully open
valve.
### Conserving

### **A** — Valve port A isothermal liquid

Isothermal liquid conserving port associated with valve port A.

### **B** — Valve port B isothermal liquid

Isothermal liquid conserving port associated with valve port B.

## Parameters

### **Valve parameterization** — Option to parameterize given flow coefficient `Orifice area based on geometry` (default) | `Cv flow coefficient` | `Kv flow coefficient`

Whether to parameterize the flow using
*Kv*,
*Cv*, or
*Cd*. The block uses these
coefficient definitions:

- *Kv* is the flow
  capacity of water through the fully open valve at 15℃ with a
  pressure drop of 1 bar, in
  m3/h.
- *Cv* is the flow
  capacity of water through the fully open valve at 60℉ with a
  pressure drop of 1 psi, in gpm.
- *Cd* is the unitless
  discharge coefficient that defines the efficiency of the
  valve.

### **Opening characteristic** — Ball valve parameterization `Area of overlapping circles` (default) | `Tabulated`

Option to parameterize the block using the method of area of overlapping
circles or to use tabulated data.

### **Maximum Cv flow coefficient** — Maximum valve flow coefficient `32` `gpm` (default) | positive scalar

Maximum value of the valve flow coefficient. This value should correspond
to the fully open position.

#### Dependencies

To enable this parameter, set **Opening
characteristic** to `Area of overlapping
circles` and **Valve
parameterization** to `Cv flow
coefficient`.

### **Maximum Kv flow coefficient** — Maximum valve flow factor `49` `m^3/hr` (default) | positive scalar

Maximum value of the valve flow factor. This value should correspond to
the fully open position.

#### Dependencies

To enable this parameter, set **Opening
characteristic** to `Area of overlapping
circles` and **Valve
parameterization** to `Kv flow
coefficient`.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Discharge coefficient of the valve. This value is a correction factor that
accounts for losses in the theoretical flow.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Orifice area based on
geometry`.

### **Cross-sectional area at ports A and B** — Valve port cross-sectional area `pi * (25 ^ 2) / 4` `mm^2` (default) | positive scalar

Cross-sectional area of the valve ports. The valve ports are the paths in the valve body
where the flow meets the ball bore.

#### Dependencies

To enable this parameter, set **Opening characteristic** to
`Area of overlapping circles`.

### **Ball bore area** — Area of ball bore `pi * (20 ^ 2) / 4` `mm^2` (default) | positive scalar

Cross-sectional area of the bore in the valve ball.

#### Dependencies

To enable this parameter, set **Opening characteristic** to
`Area of overlapping circles`.

### **Cv flow coefficient vector** — Flow coefficient for given ball rotation `[1e-06, .58, 1.15, 1.9, 2.8, 4.3, 7, 10.5, 17, 26, 32]` `gpm` (default) | vector

Valve flow coefficient for a given ball rotation. Each element corresponds
one-to-one with the **Ball rotation vector** parameter. The
first element corresponds to the valve leakage and must be nonzero.

#### Dependencies

To enable this parameter, set **Opening
characteristic** to `Tabulated`
and **Valve parameterization** to `Cv flow
coefficient`.

### **Kv flow coefficient vector** — Flow factor for given ball rotation `[1e-06, .34, .76, 1.6, 2.45, 4.1, 5.75, 9.4, 13, 28, 50]` `m^3/hr` (default) | vector

Valve flow factor for a given ball rotation. Each element corresponds
one-to-one with the **Ball rotation vector** parameter. The
first element corresponds to the valve leakage and must be nonzero.

#### Dependencies

To enable this parameter, set **Opening
characteristic** to `Tabulated`
and **Valve parameterization** to `Kv flow
coefficient`.

### **Area vector** — Area for given ball rotation `[1e-10, 62.5, 125, 187.5, 250, 312.5, 375, 437.5, 500, 562.5, 625]` `mm^2` (default) | vector

Flow area for a given ball rotation. Each element corresponds one-to-one with the
**Ball rotation vector** parameter. The first element
corresponds to the valve leakage and must be nonzero.

#### Dependencies

To enable this parameter, set **Opening characteristic** to
`Tabulated` and **Valve
parameterization** to `Orifice area based on
geometry`.

### **Ball rotation vector** — Ball rotation `pi / 2 .* [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1]` `rad` (default) | vector

Ball rotation for a given flow coefficient or area. The elements is this vector must
align one-to-one with the elements in either the **Cv flow
coefficient vector** parameter, the **Kv flow
coefficient vector** parameter, or the **Area
vector** parameter.

#### Dependencies

To enable this parameter, set **Opening characteristic** to
`Tabulated`.

### **Leakage area** — Valve gap area when in fully shut position `1e-10` `m^2` (default) | positive scalar

Sum of all gaps when the valve is in the fully shut position. The block saturates any
area smaller than this value to the specified leakage area. This value
contributes to numerical stability by maintaining continuity in the
flow.

#### Dependencies

To enable this parameter, set **Opening characteristic** to
`Area of overlapping circles`.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the valve.

## Libraries

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Flow Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

### R2024b: Updated parameter and parameter setting names

The names of the parameter and parameter settings in the Ball Valve (IL) block have been
updated to be consistent with other valve blocks. The behavior of the block has not
changed. This table summarizes the new parameter and parameter setting names.

| Previous Parameter or Setting Name | Updated Parameter or Setting Name |
| --- | --- |
| **Ball valve parameterization** | **Opening characteristic** |
| **Flow coefficient parameterization** | **Valve parameterization** |
| `Kv coefficient (SI)` | `Kv flow coefficient` |
| `Cv coefficient (USCS)` | `Cv flow coefficient` |
| `Cd coefficient and area` | `Orifice area based on geometry` |
| **Discharge coefficient (Cd)** | **Discharge coefficient** |
| **Maximum valve flow coefficient (Cv)** | **Maximum Cv flow coefficient** |
| **Maximum valve flow factor (Kv)** | **Maximum Kv flow coefficient** |
| **Valve flow coefficient (Cv) vector** | **Cv flow coefficient vector** |
| **Valve flow factor (Kv) vector** | **Kv flow coefficient vector** |

## Description

Ball valve in an isothermal liquid network

The Ball Valve (IL) block represents a ball valve in an
isothermal liquid network. A ball valve consists of a ball with a bore that can pivot
inside of a valve body. When the valve is open, the bore fully overlaps with the valve
body port. As the valve shuts, the ball rotates and reduces the amount of overlap,
thereby reducing the effective area of the orifice. Ball valves are common for flow
isolation purposes because they can securely shut off flow for many cycles. Ball valves
are less common in applications where precise throttling is necessary.

You can parameterize the block analytically or by using tabulated data. When you set
**Opening characteristic** to `Area of overlapping
circles`, the block considers the area of the overlap between the valve
port and the ball bore as the opening area such that

Aopen=sin(φ)Rbore2[cos−1(λbore)−λbore1−λ2bore]+Rport2[cos−1(λport)−λport1−λ2port]λbore=Rbore2−Rport2+l22Rborelλport=Rport2−Rbore2+l22Rportl

where:

- *Rport* and
  *Rbore* are the radii of the
  valve port and the ball bore, respectively.
- *l* is the displacement of the bore center from the valve
  port center.
- *φ* is the rotation of the ball valve given by the
  physical signal **S**. The valve is fully shut at 0 rad and
  fully open at π/2 rad.

### Mass Flow Rate

The block calculates flow through the valve using the pressure-area relationship for
orifices such that

m˙=CdA2ρ¯Δp(Δp2+Δpcrit2)14,

where:

- *Cd* is the discharge
  coefficient.
- ρ¯ is the average fluid density.
- *A* is the area open to flow, where *A* =
  *Aopen* +
  *Aleak*, and *Aleak*
  is the **Leakage area** parameter.
- *Δpcrit* is the critical
  pressure differential associated with the critical Reynolds number,
  *Recrit*.

The block calculates *Δpcrit* as

Δpcrit=πρ¯8A(vRecritCd)2.

When you set **Valve parameterization** to
`Orifice area based on geometry`, you can specify
*Cd* using the **Discharge
coefficient** parameter. When you set **Valve
parameterization** to `Cv flow coefficient`,
the block calculates *Cd* as

Cd=CvAρwater,60°F2ΔpCv,

where *Cv* is the
**Maximum Cv flow coefficient** parameter. When you set
**Valve parameterization** to `Kv flow
coefficient`, the block uses

Cd=KvAρwater,15°C2ΔpKv,

where *Kv* is the
**Maximum Kv flow coefficient** parameter. In either equation,
*ΔpCv* is
1 psi and *ΔpKv* is 1
bar.
