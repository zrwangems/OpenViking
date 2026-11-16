---
type: simulink-block
title: 'M-Way N-Position Directional Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: 'mwaynpositiondirectionalvalveil'
documentation_source_path: 'ref/mwaynpositiondirectionalvalveil.html'
language: en
---

# M-Way N-Position Directional Valve (IL)

## Ports

### Input

### **S** — Spool displacement, m physical signal

Physical signal input port associated with the spool displacement, in
m.
### Conserving

### **1** — Port 1 isothermal liquid

Isothermal liquid conserving port associated with port 1.

### **2,...,10** — Ports with parameter dependencies isothermal liquid

Isothermal liquid conserving ports associated with port 2 through 10, where the number
of ports is equal to the **Number of ports**
parameter.

#### Dependencies

To enable ports 2 through 10, set **Number of ports** to the number of
ports you want.

## Parameters

### Valve Configuration

### **Number of ports** — Number of valve ports `2` (default) | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10`

Number of ports associated with the valve, *M*. You
can select up to ten.

### **Number of spool positions** — Number of spool positions `2` (default) | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10`

Number of spool positions, *N*. You can select up to
ten.

### **Spool travel at each spool position index** — Spool travel `[-2, 0, 2, 4]` `mm` (default) | vector of length *N*

Spool travel values. Each element corresponds to a different spool
position index. The length of this vector must be equal to length of the
**Number of spool positions** parameter,
*N*. A value of `0` represents a
neutral spool position.

### **Number of orifices** — Number of orifices `1` (default) | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12` | `13` | `14` | `15` | `16` | `17` | `18` | `19` | `20`

Number of orifices. You can select up to 20.

### **Area characteristics** — Area characteristic parameterization option `Identical for all flow paths` (default) | `Different for each flow path`

Whether to apply identical or different parameterizations for each
orifice.

### **Orifice parameterization** — Orifice parameterization `Linear – Area vs. spool travel` (default) | `Tabulated data – Volumetric flow rate vs. pressure drop (linear with spool travel)` | `Tabulated data – Area vs. spool travel`

Whether to parameterize each orifice linearly, with tabulated data by area, or by
tabulated volumetric flow rate data according to pressure drop.

When **Area characteristics** is
`Identical for all flow paths`, you can set
this parameter to `Linear – Area vs. spool
travel` or `Tabulated data – Volumetric
flow rate vs. pressure drop (linear with spool
travel)`. To enable the `Tabulated data – Area
vs. spool travel` option for this parameter, set
**Area characteristics** to `Different
for each flow path`.

### **Inter-position spool travel fraction for which orifices remain fully open** — Fully open flow between spool positions `0.5` (default) | scalar in the range [0,1)

Fractional distance between adjacent spool positions for which each
orifice remains at the maximum opening area.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths`.

### **Inter-position spool travel fraction for which orifices transition between open-closed** — Spool travel from open to closed `0.1` (default) | nonnegative scalar

Fractional distance between adjacent spool positions over which the
orifice area transitions between maximum area and leakage area.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths`.

### **Maximum orifice area** — Maximum orifice area `1e-4` `m^2` (default) | positive scalar

Maximum opening area for all orifices.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Linear – Area vs.
spool travel`.

### **Leakage area fraction** — Leakage area fraction `0.01` (default) | positive scalar

Leakage area as a fraction of the value of the **Maximum
orifice area** parameter.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to `Linear – Area vs.
spool travel`.

### **Cross-sectional area at ports** — Cross-sectional area for all ports `inf` `m^2` (default) | positive scalar

Cross-sectional area for all ports.

#### Dependencies

To enable this parameter, set either:

- **Orifice parameterization** to
  `Linear – Area vs. spool
  travel`.
- **Area characteristics** to
  `Different for each path`
  and **Orifice parameterization** to
  `Tabulated data – Area vs. spool
  travel`.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Correction factor that accounts for discharge losses in theoretical
flows.

#### Dependencies

To enable this parameter, set either:

- **Orifice parameterization** to
  `Linear – Area vs. spool
  travel`.
- **Area characteristics** to
  `Different for each path`
  and **Orifice parameterization** to
  `Tabulated data – Area vs. spool
  travel`.

### **Critical Reynolds number** — Critical Reynolds number `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the
orifice.

#### Dependencies

To enable this parameter, set either:

- **Orifice parameterization** to
  `Linear – Area vs. spool
  travel`.
- **Area characteristics** to
  `Different for each path`
  and **Orifice parameterization** to
  `Tabulated data – Area vs. spool
  travel`.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar

Continuous smoothing factor that introduces a layer of gradual change
to the flow response when the valve is in near-open or near-closed
positions. Set this value to a nonzero value less than one to improve
the stability of your simulation in these regimes.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to `Linear – Area vs.
spool travel`.

### **Pressure recovery** — Option to account for pressure increases in area expansions `Off` (default) | `On`

Whether to account for pressure increase when fluid flows from a
region of smaller restriction area to a region of larger cross-sectional
area.

#### Dependencies

To enable this parameter, set either:

- **Orifice parameterization** to
  `Linear – Area vs. spool
  travel`.
- **Area characteristics** to
  `Different for each path`
  and **Orifice parameterization** to
  `Tabulated data – Area vs. spool
  travel`.

### **Pressure drop vector** — Tabulated pressure drop `[-.1, .3, .5, .7]` `MPa` (default) | vector of length *X*

Tabulated pressure drop values for all orifices. The elements of this
vector correspond one-to-one with the **Fully open volumetric
flow rate vector** parameter.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Tabulated data –
Volumetric flow rate vs. pressure drop (linear with spool
travel)`.

### **Fully open volumetric flow rate vector** — Tabulated volumetric flow rate `[-.0009, .0016, .002, .0024]` `m^3/s` (default) | vector of length *X*

Volumetric flow rate for a fully open orifice at a given pressure
drop. The elements of this vector correspond one-to-one with the
**Pressure drop vector** parameter.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Tabulated data –
Volumetric flow rate vs. pressure drop (linear with spool
travel)`.

### **Leakage flow rate fraction** — Leakage flow rate fraction `0.01` (default) | positive scalar

Leakage as a fraction of the **Fully open volumetric flow rate
vector** parameter.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to `Tabulated data –
Volumetric flow rate vs. pressure drop (linear with spool
travel)`.

### Orifice 1

This section includes only the parameters for orifice 1. The remaining orifice
parameters are identical to orifice 1 except for their number and the cases
mentioned in the parameter descriptions for orifice 1. To learn more, see Orifice Parameterization.

### **Ports connected by orifice 1** — Ports connected by orifice 1 `[3, 2]` (default) | vector of length 2

The two fluid ports connected by orifice 1. The first element is the
valve port connected to the orifice A port. The second element is the
valve port connected to the orifice B port. In the Simscape Results
Explorer app, the variables `mdot_A` and
`mdot_B` are mass flow rates into the
Orifice (IL) block A and B ports,
respectively. `p_diff` is the pressure drop from port A
to port B of the orifice. In the block icon, for ports connected to a
single orifice, the arrow points to the port represented by the second
element of this parameter. The default values for the other orifices are:

- Orifice 2: `[4, 5]`
- Orifice 3: `[2, 1]`
- Orifice 4: `[3, 4]`
- Orifice 5–Orifice 20: `[1, 2]`

### **Spool position indices where orifice 1 is open** — Orifice 1 open positions `[1, 4]` (default) | vector of length 1 to *N*

Spool positions for which orifice 1 is open. The vector must be
strictly monotonically increasing with values between 1 and the value of
the **Number of spool positions** parameter. The
default values for the other orifices are:

- Orifice 2: `[1, 4]`
- Orifice 3: `[3, 4]`
- Orifice 4: `[3, 4]`
- Orifice 5–Orifice 20: `1`

If the **Spool position indices where orifice 1 is
open** parameter contains consecutive integers, it
indicates that the orifice is open in multiple adjacent discrete spool
positions. The block behavior in this case depends on the
**Orifice parameterization** parameter:

- If **Orifice parameterization** is
  `Linear – Area vs. spool
  travel` or `Tabulated data –
  Volumetric flow rate vs. pressure drop (linear with
  spool travel)`, the block maintains the
  value of the **Maximum orifice area**
  parameter or the **Fully open volumetric flow rate
  vector** parameter across the multiple adjacent
  discrete spool positions where the orifice is open.
- If **Orifice parameterization** is
  `Tabulated data – Area vs. spool
  travel`, the element in the
  **Vector of spool travel relative to discrete
  spool position for orifice 1** parameter equal
  to `0` corresponds to the smallest-valued
  discrete spool position of the adjacent positions.

### **Spool travel for which orifice 1 remains fully open** — Fully open spool travel `1` `mm` (default) | nonnegative scalar

Spool travel across which the orifice maintains the maximum opening
area. The center of this spool travel distance is at the value of the
**Spool position with open orifice 1**
parameter.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Different for each
flow path` and **Orifice
parameterization** to `Linear – Area vs.
spool travel` or `Tabulated data –
Volumetric flow rate vs. pressure drop (linear with spool
travel)`.

### **Spool travel for which orifice 1 transitions between open-closed** — Threshold spool travel `0.2` `mm` (default) | positive scalar

Spool travel across which the orifice transitions from fully open to
fully closed.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Different for each
flow path` and **Orifice
parameterization** to `Linear – Area vs.
spool travel` or `Tabulated data –
Volumetric flow rate vs. pressure drop (linear with spool
travel)`.

### **Maximum area of orifice 1** — Orifice area when fully open `1e-4` `m^2` (default) | positive scalar

Opening area of orifice 1.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Different for each
flow path` and **Orifice
parameterization** to `Linear – Area vs.
spool travel`.

### **Pressure drop vector of orifice 1** — Orifice 1 pressure drop `[-.1, .3, .5, .7]` `MPa` (default) | vector of length *X*

Vector of pressure drop values for orifice 1. These values correspond
one-to-one with the **Fully open volumetric flow rate vector of
orifice 1** parameter.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Different for each
flow path` and **Orifice
parameterization** to `Tabulated data –
Volumetric flow rate vs. pressure drop (linear with spool
travel)`.

### **Fully open volumetric flow rate vector of orifice 1** — Orifice 1 fully open volumetric flow rate `[-.0009, .0016, .002, .0024]` `m^3/s` (default) | vector of length *X*

Volumetric flow rate when orifice 1 is fully open for a given pressure
drop. These values correspond one-to-one with the **Pressure
drop vector of orifice 1** parameter.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Different for each
flow path` and **Orifice
parameterization** to `Tabulated data –
Volumetric flow rate vs. pressure drop (linear with spool
travel)`.

### **Vector of spool travel relative to discrete spool position for orifice 1** — Vector of spool travels `[-.7, -.4, -.35, -.3, -.25, 0]` `mm` (default) | vector

Vector of spool travel for orifice 1 that correspond to the elements in the
**Area vector for orifice 1** parameter. This
parameter must be the same length as the **Area vector for
orifice 1**  parameter, contain an element equal to
`0`, and be strictly monotonically increasing. The
`0`-valued element represents when the spool is in
a discrete spool position index. If the **Spool position indices
where orifice 1 is open** parameter contains multiple
adjacent discrete spool positions, then the `0`-valued
element of the **Vector of spool travel relative to discrete
spool position for orifice 1** parameter corresponds to the
smallest value in the sequence of adjacent positions. For example, if
the **Spool position indices where orifice 1 is open**
parameter is `[1 2]`, `[1 3 4 7]`, or
`[2 3 4 8 9]`, then the 0-valued element would
correspond to `1`, `3`, or
`{2,8}`, respectively.

If the **Spool position indices where orifice 1 is
open** parameter is open for all spool positions, meaning
the value is `[1:Number of spool positions]`, then the
`0`-valued element of the **Vector of spool
travel relative to discrete spool position for orifice 1**
parameter corresponds to the first discrete spool position. In this
case, you can set the **Area vector for orifice 1**
parameter to the same repeating value to model a constant area orifice.

The vector can contain negative and positive elements, which
represent spool travel in either direction relative to the discrete
spool position for which the orifice is open. If the parameter contains
only non-negative elements or only non-positive elements, then the
orifice opening behaves symmetrically for negative or positive spool
travel relative to the discrete position, respectively.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Different for each
flow path` and **Orifice
parameterization** to `Tabulated data –
Area vs. spool travel`.

### **Area vector for orifice 1** — Vector of orifice opening areas `[1e-10, 1e-05, 4e-05, 8e-05, .0001, .0001]` `m^2` (default) | vector

Vector of orifice areas for orifice 1 that correspond to the elements in the
**Vector of spool travel relative to discrete spool position
for orifice 1** parameter. This parameter must be the same
length as the **Vector of spool travel relative to discrete
spool position for orifice 1** parameter. If the orifice is
open in the first or last discrete spool position, then the orifice
remains fully open at the maximum area when the spool travels beyond the
first or last discrete spool position.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Different for each
flow path` and **Orifice
parameterization** to `Tabulated data –
Area vs. spool travel`.

## Libraries

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Directional Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022b**

### R2023b: Parameterize the block with tabulated data with respect to area and spool travel

You can now parameterize the orifice area characteristics by using tabulated data
of the area-versus-spool travel profile. When the **Area
characteristics** is `Different for each flow
path`, set the **Orifice parameterization**
parameter to `Tabulated data – Area vs. spool travel` to
use the new parameterization option. Specify the tabulated data with the
**Vector of spool travel relative to discrete spool position**
and **Orifice area vector** parameters.

## Description

M-way, N-position valve in an isothermal liquid network

The M-Way N-Position Directional Valve (IL) block represents
a spool-operated directional valve with an arbitrary configuration of ports, spool
positions, and orifices. The block accepts up to ten ports, ten spool positions, and 20
orifices. Valves with many configurations are most common in construction, agriculture,
and some vehicle applications. This block simplifies complex parameterizations by
allowing you to apply the same area characteristics to all flow paths. You can also
individually specify the area characteristics for each flow path. You can parameterize
the valve by specifying the opening area with tabulated or linear data or by using
tabulated data that represents volumetric flow rate for a fully open orifice at
varied
pressure drops. The block uses a variable orifice to control the flow
between a given pair of connected ports. The physical signal at port
**S** triggers the spool motion to open or shut the valve. For more
details about how the block calculates flow rate through a variable orifice, see Orifice (IL).

You can generate a characteristic plot of the valve by right-clicking the block and
selecting **Fluids** > **Plot Valve Characteristics**. To updated the plot after changing the block parameters, click the
**Reload Data** button. You can control the shape of the
characteristic plot. To select which lines are visible, click the appropriate orifice on
the legend.

The default valve characteristic plot is:

Default valve characteristic plot

The figure indicates locations A1, A2, B1, and B2.

Valve characteristic plot with points A1, B1, B2, and A2 labeled.

Position 1 is at spool travel of -1 mm. Position 2 is at spool travel of 0 mm, and Position
3 is at spool travel of 1 mm. Locations *A1* and *A2*
represent the left- and right-side transition regions of the orifice opening area,
respectively. Locations *B1* and *B2* represent the
left- and right-side fully open regions of the orifice opening area, respectively. The
current spool position is the separation between *B1* and
*B2*. When you set **Area characteristics** to
`Identical for all flow paths`.

- *A1* = (distance between spool positions 1 and 2) \*
  (value of the
  **Inter-position
  spool travel fraction for which orifices transition between
  open-closed** parameter)
- *A2* = (distance between spool positions 2 and 3) \*
  (value of the **Inter-position spool travel fraction for which
  orifices transition between open-closed** parameter)
- *B1* = (distance between spool positions 1 and 2) \*
  (value of the **Inter-position spool travel fraction for which
  orifices remain fully open** parameter)
- *B2* = (distance between spool positions 2 and 3) \*
  (value of the **Inter-position spool travel fraction for which
  orifices remain fully open** parameter)

When you set **Area characteristics** to `Different for each
flow path` and **Orifice parameterization** to
`Linear – Area vs. spool travel` or `Tabulated
data – Volumetric flow rate vs. pressure drop (linear with spool
travel)`:

- *A1* = *A2* = value of the
  **Spool travel for which orifice 2 transitions between
  open-closed** parameter.
- *B1* = *B2* = value of the
  **Spool travel for which orifice 2 remains fully open**
  parameter.

### Orifice Parameterization

When you set **Area parameterization** to `Different
for each flow path`, you can parameterize each orifice by using the
parameters in the **Orifice 1,…,20** sections. For example, if you
set **Number of orifices** to 3, the block includes sections for
**Orifice 1**, **Orifice 2**, and
**Orifice 3**. Each section has the same parameter names
followed by the number for that section.

The block icon updates automatically to indicate the orifice configuration, which
you control with the appropriate **Ports connected by orifice...**
parameter. If you connect one odd-numbered port to one even-numbered port, the block
icon shows an arrow that points to the second listed port. The block icon indicates
when a parameterization is invalid.

If you enable logging, the `Orifice.S` signal for each orifice
describes the spool position according to this table:

|  | **Area characteristic** parameter | |
| --- | --- | --- |
|  | `Identical for all flow paths` | `Different for each flow path` |
| If **Orifice parameterization** is `Linear – Area vs. spool travel` or `Tabulated data – Volumetric flow rate vs. pressure drop (linear with spool travel)` | `Orifice.S` = `0 m` when the orifice is fully open. The units m in the `Orifice.S` signal correspond to the inter-position spool travel fraction.  `Orifice.S = - Stravel` when the orifice is fully closed where *Stravel* is the value of the **Inter-position spool travel fraction for which orifices transition between open-closed** parameter. | `Orifice.S` = `0 m` when the orifice is fully open.  `Orifice.S = - Stravel` when the orifice is fully closed where *Stravel* is the value of the **Spool travel for which orifice transitions between open-closed** parameter. |
| If **Orifice parameterization** is `Tabulated data – Area vs. spool travel` | Not a parameterization option | `Orifice.S` = `0 m` when the orifice is fully open.  In all other positions, `Orifice.S` = the first or last element of an extended version of the  **Vector of spool travel relative to discrete spool position for Orifice** parameter when the orifice is fully closed. If the **Vector of spool travel relative to discrete spool position for Orifice** parameter does not contain a positive or negative region, the extended version of the parameters extend the spool travel vector and area vector to symmetric positive and negative regions.  The orifice leakage area corresponds to the first and last elements of the extended spool travel vector. The orifice can have different leakage areas if the **Vector of spool travel relative to discrete spool position for Orifice** parameter has both a negative and positive region. |

### Assumptions and Limitations

- The block assumes that each orifice has a symmetric opening and closing
  about the spool position when you set **Area
  characteristics** to `Different for each flow
  path`.
- The block assumes that each orifice has a symmetric opening and closing
  scaled with the spacing of the **Spool travel at each spool position
  index** parameter when you set **Area
  characteristics** to `Identical for all flow
  paths`.
