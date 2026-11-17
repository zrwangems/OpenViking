---
type: simulink-block
title: 'Compressor (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Turbomachinery'
documentation_page: 'compressorma'
documentation_source_path: 'ref/compressorma.html'
language: en
---

# Compressor (MA)

## Ports
```yaml
ports:
- name: A
  summary: Moist air inlet moist air
  direction: conserving
- name: B
  summary: Moist air outlet moist air
  direction: conserving
- name: C
  summary: Compressor casing mechanical translational
  direction: conserving
- name: R
  summary: Compressor shaft mechanical translational
  direction: conserving
- name: SM
  summary: Surge margin physical signal
  direction: output
```

### Conserving

### **A** — Moist air inlet moist air

Moist air conserving port associated with the compressor inlet.

### **B** — Moist air outlet moist air

Moist air conserving port associated with the compressor outlet.

### **C** — Compressor casing mechanical translational

Mechanical translational conserving port associated with the compressor casing.

### **R** — Compressor shaft mechanical translational

Mechanical translational conserving port associated with the compressor shaft torque and
angular velocity.
### Output

### **SM** — Surge margin physical signal

Physical signal output port associated with the surge margin at a
given mass flow rate. The block calculates the surge margin as

SM(m˙corr)=pr,surge(m˙corr)pr(m˙corr)−1.

#### Dependencies

To enable this port, set **Parameterization** to
`Tabulated`.
## Parameters
```yaml
parameters:
- name: Parameterization
  summary: Compressor performance parameterization Analytical (default) | Tabulated
  group: Compressor Map
- name: Corrected speed at design point
  summary: Operational corrected shaft speed 10000 rpm (default) | positive scalar
  group: Compressor Map
- name: Pressure ratio at design point
  summary: Operational outlet-to-inlet pressure ratio 7.5 (default) | positive scalar
  group: Compressor Map
- name: Corrected mass flow rate at design point
  summary: Operational corrected mass flow rate 33 kg/s (default) | positive scalar
  group: Compressor Map
- name: Efficiency specification
  summary: Isentropic efficiency model Analytical (default) | Constant
  group: Compressor Map
- name: Maximum isentropic efficiency
  summary: Maximum compressor efficiency 0.887 (default) | positive scalar in the range (0,1]
  group: Compressor Map
- name: Minimum isentropic efficiency
  summary: Minimum compressor efficiency 0.5 (default) | positive scalar in the range (0,1]
  group: Compressor Map
- name: Corrected mass flow rate at maximum efficiency point
  summary: Corrected mass flow rate at compressor maximum efficiency 30 kg/s (default) | positive scalar
  group: Compressor Map
- name: Pressure ratio at maximum efficiency point
  summary: Pressure ratio at compressor maximum efficiency 7 (default) | positive scalar
  group: Compressor Map
- name: Constant isentropic efficiency
  summary: Constant isentropic efficiency value 0.8 (default) | positive scalar in the range (0,1]
  group: Compressor Map
- name: Corrected speed index vector, N
  summary: Vector of corrected shaft speeds [5000, 6000, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 11000] rpm (default) |
    vector
  group: Compressor Map
- name: Beta index vector, beta
  summary: 'Vector of corrected speed line intervals 0 : 1 / 6 : 1 (default) | vector of elements in the range [0,1]'
  group: Compressor Map
- name: Pressure ratio table, pr(N,beta)
  summary: Compressor map pressure ratio data *M*-by-*N* matrix (default)
  group: Compressor Map
- name: Corrected mass flow rate table, mdot(N,beta)
  summary: Compressor map corrected mass flow rate data *M*-by-*N* matrix (default)
  group: Compressor Map
- name: Isentropic efficiency table, eta(N,beta)
  summary: Compressor map isentropic efficiency data *M*-by-*N* matrix (default)
  group: Compressor Map
- name: Report when surge margin is negative
  summary: Whether to notify if pressure ratio exceeds surge pressure ratio None (default) | Warning | Error
  group: Compressor Map
- name: Spine shape, a
  summary: Spine shape exponent 1.5 (default) | positive scalar
  group: Map Coefficients
- name: Speed line spread, b
  summary: Constant speed line spacing exponent 5 (default) | positive scalar
  group: Map Coefficients
- name: Speed line roundness, k
  summary: Constant speed line shape coefficient 0.03 (default) | positive scalar
  group: Map Coefficients
- name: Efficiency peak flatness orthogonal to spine, c
  summary: Exponent characterizing shape of analytical isentropic efficiency 3 (default) | positive scalar
  group: Map Coefficients
- name: Efficiency peak flatness along spine, d
  summary: Exponent characterizing shape of analytical isentropic efficiency 4 (default) | positive scalar
  group: Map Coefficients
- name: Efficiency contour gradient orthogonal to spine, C
  summary: Coefficient characterizing shape of analytical isentropic efficiency 15 (default) | positive scalar
  group: Map Coefficients
- name: Efficiency contour gradient along spine, D
  summary: Coefficient characterizing shape of analytical isentropic efficiency 1 (default) | positive scalar in the range
    (0,1]
  group: Map Coefficients
- name: Reference pressure for corrected flow
  summary: Correcting pressure 0.101325 MPa (default) | positive scalar
  group: Parameters
- name: Reference temperature for corrected flow
  summary: Correcting temperature 288.15 K (default) | positive scalar
  group: Parameters
- name: Reference relative humidity for corrected flow
  summary: Correcting humidity 0 (default) | positive scalar in the range [0,1]
  group: Parameters
- name: Mechanical efficiency
  summary: Efficiency of conversion to torque 0.9 (default) | positive scalar in the range [0,1]
  group: Parameters
- name: Model water droplets evaporation
  summary: Option to model water droplet evaporation off (default) | on
  group: Parameters
- name: Relative humidity at saturation
  summary: Relative humidity above which condensation occurs 1 (default) | positive scalar
  group: Parameters
- name: Inlet area at port A
  summary: Compressor inlet area 1 m^2 (default) | positive scalar
  group: Parameters
- name: Outlet area at port B
  summary: Compressor outlet area 1 m^2 (default) | positive scalar
  group: Parameters
```

### Compressor Map

### **Parameterization** — Compressor performance parameterization `Analytical` (default) | `Tabulated`

Compressor performance parameterization. Choose the analytical or tabulated parameterization:

- `Analytical`: A pressure
  ratio–corrected mass flow rate curve defines the peak
  compressor performance. You can choose to model isentropic
  efficiency as a constant or analytically.
- `Tabulated`: A user-supplied
  compressor map defines the compressor performance. The block
  determines the compressor operating points by using linear
  interpolation between the corrected mass flow rate, pressure
  ratio, and isentropic efficiency tables at given points in
  the user-provided corrected shaft speed and β vectors. The
  default map comes from data reported in [3].

### **Corrected speed at design point** — Operational corrected shaft speed `10000` `rpm` (default) | positive scalar

Shaft speed at the intended compressor pressure ratio and corrected
mass flow rate, corrected for temperature.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Analytical`.

### **Pressure ratio at design point** — Operational outlet-to-inlet pressure ratio `7.5` (default) | positive scalar

Outlet-to-inlet pressure ratio at the intended compressor corrected
mass flow rate.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Analytical`.

### **Corrected mass flow rate at design point** — Operational corrected mass flow rate `33` `kg/s` (default) | positive scalar

Mass flow rate at the intended compressor pressure ratio, corrected
for temperature and pressure.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Analytical`.

### **Efficiency specification** — Isentropic efficiency model `Analytical` (default) | `Constant`

Isentropic efficiency model type. Choose a constant or analytical model. Use
`Analytical` to specify variable
values.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Analytical`.

### **Maximum isentropic efficiency** — Maximum compressor efficiency `0.887` (default) | positive scalar in the range (0,1]

Maximum compressor isentropic efficiency. Isentropic efficiency is the
ratio of isentropic change to actual change.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Analytical` and **Efficiency
specification** to
`Analytical`.

### **Minimum isentropic efficiency** — Minimum compressor efficiency `0.5` (default) | positive scalar in the range (0,1]

Minimum compressor isentropic efficiency. Isentropic efficiency is the
ratio of isentropic change to actual change.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Analytical` and **Efficiency
specification** to
`Analytical`.

### **Corrected mass flow rate at maximum efficiency point** — Corrected mass flow rate at compressor maximum efficiency `30` `kg/s` (default) | positive scalar

Mass flow rate at maximum efficiency, corrected for temperature and
pressure. The point of maximum efficiency does not necessarily coincide
with the compressor design point.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Analytical` and **Efficiency
specification** to
`Analytical`.

### **Pressure ratio at maximum efficiency point** — Pressure ratio at compressor maximum efficiency `7` (default) | positive scalar

Pressure ratio at maximum efficiency. The point of maximum efficiency
does not necessarily coincide with the compressor design point.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Analytical` and **Efficiency
specification** to
`Analytical`.

### **Constant isentropic efficiency** — Constant isentropic efficiency value `0.8` (default) | positive scalar in the range (0,1]

Value of the constant isentropic efficiency in the analytical
parameterization.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Analytical` and **Efficiency
specification** to
`Constant`.

### **Corrected speed index vector, N** — Vector of corrected shaft speeds `[5000, 6000, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 11000]` `rpm` (default) | vector

Vector of corrected shaft speeds.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Tabulated`.

### **Beta index vector, beta** — Vector of corrected speed line intervals `0 : 1 / 6 : 1` (default) | vector of elements in the range [0,1]

Vector of relative positions along the corrected speed lines. Choked
flow occurs when β = 0 and surge flow occurs at β = 1. β lines are
perpendicular to the compressor shaft constant speed lines,
*N*.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Tabulated`.

### **Pressure ratio table, pr(N,beta)** — Compressor map pressure ratio data *M*-by-*N* matrix (default)

*M*-by-*N* matrix of compressor outlet-to-inlet
pressure ratios at the specified corrected shaft speed and β value. The
block employs linear interpolation between table elements.
*M* and *N* are the sizes of the
corresponding vectors:

- *M* is the number of vector elements in
  the **Corrected speed index vector, N**
  parameter.
- *N* is the number of vector elements in
  the **Beta index vector, beta**
  parameter.

The default value is:

`[1.369, 1.459, 1.587, 1.654, 1.734, 1.775, 1.82; 1.918,
2.075, 2.229, 2.318, 2.405, 2.456, 2.481; 2.706, 2.966, 3.168,
3.334, 3.404, 3.445, 3.435; 3.203, 3.533, 3.833, 4.021, 4.127,
4.135, 4.066; 3.782, 4.222, 4.565, 4.867, 5.065, 5.07, 4.934; 4.302,
4.861, 5.285, 5.821, 6.161, 6.334, 6.142; 4.841, 5.445, 5.988,
6.628, 7.222, 7.623, 7.573; 5.358, 5.997, 6.589, 7.334, 8.012,
8.668, 9; 5.851, 6.491, 7.124, 7.982, 8.754, 9.57, 9.814; 6.707,
7.321, 8.034, 9.047, 9.94, 10.834, 10.998]`

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Tabulated`.

### **Corrected mass flow rate table, mdot(N,beta)** — Compressor map corrected mass flow rate data *M*-by-*N* matrix (default)

*M*-by-*N* matrix of corrected mass flow rates at the
specified corrected shaft speed and β value. The block employs linear
interpolation between table elements. *M* and
*N* are the sizes of the corresponding vectors:

- *M* is the number of vector elements in
  the **Corrected speed index vector, N**
  parameter.
- *N* is the number of vector elements in
  the **Beta index vector, beta**
  parameter.

The default value is:

`[10.45, 10.203, 9.784, 9.526, 9.144, 8.947, 8.615; 13.315,
13.018, 12.525, 11.984, 11.455, 11.086, 10.914; 17.601, 17.204,
16.502, 15.8, 14.903, 14.179, 13.184; 20.331, 19.983, 19.39, 18.492,
17.435, 16.293, 14.895; 23.466, 23.092, 22.572, 21.807, 20.687,
19.3, 17.682; 26.295, 26.091, 25.766, 25.28, 24.453, 23.26, 21.311;
29.013, 28.747, 28.641, 28.412, 28.06, 27.098, 25.306; 31.424,
31.379, 31.273, 31.103, 30.849, 30.484, 29.718; 33.688, 33.606,
33.561, 33.513, 33.392, 33.258, 33.059; 37.678, 37.621, 37.575,
37.598, 37.501, 37.415, 37.413] kg/s`

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Tabulated`.

### **Isentropic efficiency table, eta(N,beta)** — Compressor map isentropic efficiency data *M*-by-*N* matrix (default)

*M*-by-*N* matrix of compressor isentropic
efficiencies at the specified corrected shaft speed and β value. The
block employs linear interpolation between table elements.
*M* and *N* are the sizes of the
corresponding vectors:

- *M* is the number of vector elements in
  the **Corrected speed index vector, N**
  parameter.
- *N* is the number of vector elements in
  the **Beta index vector, beta**
  parameter.

The default value is:

`[.68, .69, .695, .7, .701, .705, .704; .7, .725, .75, .755,
.745, .73, .725; .77, .795, .81, .805, .78, .765, .745; .795, .812,
.825, .82, .805, .78, .75; .82, .837, .848, .849, .835, .805, .78;
.83, .845, .856, .86, .855, .84, .8; .83, .848, .859, .869, .86,
.852, .83; .828, .845, .857, .869, .862, .855, .85; .806, .83, .85,
.86, .859, .857, .853; .79, .8, .82, .835, .845, .848,
.849]`

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Tabulated`.

### **Report when surge margin is negative** — Whether to notify if pressure ratio exceeds surge pressure ratio `None` (default) | `Warning` | `Error`

Whether the block does nothing, generates a warning, or generates an
error when it detects a negative surge margin.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Tabulated`.

### Map Coefficients

To enable the **Map Coefficients** parameters, set
**Parameterization** to
`Analytical`.

### **Spine shape, a** — Spine shape exponent `1.5` (default) | positive scalar

Exponent in the analytical parameterization of the compressor map that
characterizes the spine shape.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Analytical`.

### **Speed line spread, b** — Constant speed line spacing exponent `5` (default) | positive scalar

Exponent in the analytical parameterization of the compressor map that
characterizes the constant speed line spacing.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Analytical`.

### **Speed line roundness, k** — Constant speed line shape coefficient `0.03` (default) | positive scalar

Coefficient in the analytical parameterization of the compressor map
that characterizes the constant speed line shape.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Analytical`.

### **Efficiency peak flatness orthogonal to spine, c** — Exponent characterizing shape of analytical isentropic efficiency `3` (default) | positive scalar

Exponent associated with the compressor map peak flatness orthogonal
to the spine.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Analytical` and **Efficiency
specification** to
`Analytical`.

### **Efficiency peak flatness along spine, d** — Exponent characterizing shape of analytical isentropic efficiency `4` (default) | positive scalar

Exponent associated with the efficiency map peak flatness along the
spine.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Analytical` and **Efficiency
specification** to
`Analytical`.

### **Efficiency contour gradient orthogonal to spine, C** — Coefficient characterizing shape of analytical isentropic efficiency `15` (default) | positive scalar

Coefficient associated with the efficiency contour gradient orthogonal
to the spine.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Analytical` and **Efficiency
specification** to
`Analytical`.

### **Efficiency contour gradient along spine, D** — Coefficient characterizing shape of analytical isentropic efficiency `1` (default) | positive scalar in the range (0,1]

Coefficient associated with the efficiency contour gradient along the
spine.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Analytical` and **Efficiency
specification** to
`Analytical`.

### Parameters

### **Reference pressure for corrected flow** — Correcting pressure `0.101325` `MPa` (default) | positive scalar

Reference inlet pressure for the compressor map. When you set
**Parameterization** to
`Tabulated`, the data supplier specifies
this value with respect to the tabulated compressor data. When you set
**Parameterization** to
`Analytical`, this value is the inlet
pressure at the design operating condition.

### **Reference temperature for corrected flow** — Correcting temperature `288.15` `K` (default) | positive scalar

Reference inlet temperature for the compressor map. When you set
**Parameterization** to
`Tabulated`, the data supplier specifies
this value with respect to the tabulated compressor data. When you set
**Parameterization** to
`Analytical`, this value is the inlet
temperature at the design operating condition.

### **Reference relative humidity for corrected flow** — Correcting humidity `0` (default) | positive scalar in the range [0,1]

Reference inlet humidity for the compressor map. When you set
**Parameterization** to
`Tabulated`, the data supplier specifies
this value with respect to the tabulated compressor data. When you set
**Parameterization** to
`Analytical`, this value is the inlet
humidity at the design operating condition.

### **Mechanical efficiency** — Efficiency of conversion to torque `0.9` (default) | positive scalar in the range [0,1]

Ratio of the power delivered to the fluid flow to the power driving
the mechanical shaft.

### **Model water droplets evaporation** — Option to model water droplet evaporation `off` (default) | `on`

Option to model evaporation of water droplets due to temperature
change in the compressor.

### **Relative humidity at saturation** — Relative humidity above which condensation occurs `1` (default) | positive scalar

Relative humidity above which condensation occurs in the
compressor.

#### Dependencies

To enable this parameter, select **Model water droplets
evaporation**.

### **Inlet area at port A** — Compressor inlet area `1` `m^2` (default) | positive scalar

Compressor inlet cross-sectional area.

### **Outlet area at port B** — Compressor outlet area `1` `m^2` (default) | positive scalar

Compressor outlet cross-sectional area.
## Libraries

Simscape / Fluids / Moist Air / Turbomachinery

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

### R2025a: Model water droplet evaporation

Model water droplet evaporation due to temperature change by using the **Model
water droplets evaporation** parameter.

### R2024b: Model water droplets suspended in moist air flow

Blocks in the moist air domain can now model water droplets suspended in a moist air flow. To
model water droplets, select **Enable entrained water droplets** in the
Moist Air Properties
(MA) block connected to your moist air network.

## Description

Compressor in a moist air network

The Compressor (MA) block represents a dynamic compressor,
such as a centrifugal or axial compressor, in a moist air network. You can use the
**Parameterization** parameter to parameterize the block
analytically based on the design point or by using a tabulated compressor map. A
positive rotation of port **R** relative to port **C**
causes fluid to flow from port **A** to port **B**.
Port **R** and port **C** are mechanical rotational
conserving ports associated with the compressor shaft and casing, respectively.

The surge margin is the ratio between the surge pressure ratio and the operating point
pressure ratio along the a constant speed line, minus one. When you set
**Parameterization** to `Tabulated`, the
block outputs the surge margin at port **SM**.

The design point is the design operational pressure ratio across and mass flow rate through
the compressor during simulation. The compressor operating point and the point of
maximum efficiency do not need to coincide.

### Compressor Map

The compressor map plots the isentropic efficiency of the compressor and the lines of
constant corrected shaft speed between the two extremes of choked flow and surge
flow. To visualize the block map, right-click the block and select **Fluids** > **Plot Compressor Map**. Each time you modify the block settings, click **Reload
Data** on the figure window.

Compressor map

Each corrected speed line shows how the pressure ratio varies with the corrected
mass flow rate when the shaft spins at the corresponding corrected speed. The
variable *β* indicates the relative position along the corrected
speed lines between the two extremes. Choked flow corresponds to *β* = 0 and surge flow corresponds to *β* = 1. The map also plots contours of isentropic efficiency as a
function of pressure ratio and corrected mass flow rate, which provides a relative
indication of how much power the compressor needs to operate at various combinations
of pressure ratio and corrected mass flow rate.

**Corrected Mass Flow Rate**

Due to the large changes in pressure and temperature inside a compressor, the compressor
map plots performance in terms of the corrected mass flow rate. The map adjusts
the corrected mass flow rate from the inlet mass flow rate by using the
reference pressure and reference temperature,

m˙corr=m˙A(TARA/γATrefRref/γref/pApref),

where:

- *ṁA* is the mass flow rate
  at port **A**.
- *TA* is the temperature at
  port **A**.
- *Tref* is the value of the
  **Reference temperature for corrected flow**
  parameter. When you set **Parameterization** to
  `Analytical`, this value is the inlet
  temperature at the design operating condition.
- *RA* is the mixture
  specific gas constant at port **A**.
- *Rref* is the mixture
  specific gas constant calculated at the values of the
  **Reference pressure for corrected flow**,
  **Reference temperature for corrected flow**,
  and **Reference relative humidity for corrected
  flow** parameters.
- m˙*corr* is
  the corrected mass flow rate. When you set
  **Parameterization** to
  `Analytical`, the block uses the
  **Corrected mass flow rate at design point**
  parameter. When you set **Parameterization** to
  `Tabulated`, the block uses the
  **Corrected mass flow rate table,
  mdot(N,beta)** parameter.
- *γA* is the ratio of
  specific heats at port **A**.
- *γref* is the ratio of
  specific heats at the values of the **Reference pressure for
  corrected flow**, **Reference temperature for
  corrected flow**, and **Reference relative
  humidity for corrected flow** parameters.
- *pA* is the pressure at
  port **A**.
- *pref* is the value of the
  **Reference pressure for corrected flow**
  parameter. When using the analytical parameterization, this value is
  the inlet pressure at the design operating condition.

The block derives *TA*
from the specific internal energy, *uA*,
and specific pressure, *pA*.

**Corrected Speed**

The block also adjusts the shaft speed, *ω*, according to the
reference temperature, such that the corrected shaft speed is

ωcorr=ωTARA/γATrefRref/γref.

### Shaft Torque

The block calculates the shaft torque, *τ*, as

τ=m˙AΔhtotalηmω,

where:

- *Δhtotal* is the change in
  specific total enthalpy.
- *ηm* is the value of the
  **Mechanical efficiency** parameter.
- *ω* is the relative shaft angular velocity,
  *ωR -
  ωC*.

The block relates the efficiency in the compressor map as

Δhtotal=Δhisenηisen,

where:

- *Δhisen* is the isentropic
  change in specific total enthalpy.
- *ηisen* is the isentropic
  efficiency.

A threshold region when flow approaches zero ensures that the compressor generates no
torque when the flow rate is near zero or reversed.

### Analytical Parameterization

You can generate the compressor map analytically by setting
**Parameterization** to `Analytical`.
The block fits a model of the compressor map based on [1] to the specified values
for the **Corrected speed at design point**, **Pressure
ratio at design point**, and **Corrected mass flow rate at
design point** parameters. This method does not use
*β* lines and the block does not report a surge margin.

**Pressure Ratio**

The block finds the pressure ratio at a given shaft speed and mass flow rate as

π=1+(πD−1)[N˜ab+2N˜kln(1−m˜−N˜bk)],

where:

- *πD* is the value of the
  **Pressure ratio at design point**
  parameter.
- N˜ is the normalized corrected shaft speed,

  NND,

  where
  *ND* is the value of the
  **Corrected speed at design point**
  parameter.
- m˜ is the normalized corrected mass flow rate,

  m˙corrm˙D,

  where m˙*D* is the
  value of the **Corrected mass flow rate at design
  point** parameter.
- *a* is the value of the **Spine shape,
  a** parameter.
- *b* is the value of the **Speed line
  spread, b** parameter.
- *k* is the value of the **Speed line
  roundness, k** parameter.

The *spine* refers to the black line where the
isentropic efficiency contours start to bend. The map *speed
lines* are the shaft constant-speed lines that intersect the spine
perpendicularly.

Compressor analytical map

**Isentropic Efficiency Parameterization**

When you set **Efficiency specification** to
`Analytical`, the block models variable compressor
efficiency as

η=η0(1−C|p˜m˜a+Δa−1−m˜|c−D|m˜m˜0−1|d),

where:

- *η0* is the value of the
  **Maximum isentropic efficiency**
  parameter.
- *C* is the value of the **Efficiency
  contour gradient orthogonal to spine, C**
  parameter.
- *D* is the value of the **Efficiency
  contour gradient along spine, D** parameter.
- *c* is the value of the **Efficiency peak
  flatness orthogonal to spine, c** parameter.
- *d* is the value of the **Efficiency peak
  flatness along spine, d** parameter.
- p˜ is the normalized corrected pressure ratio,

  π−1πD−1,

  where
  *πD* is the value of the
  **Corrected pressure ratio at design point**
  parameter.
- m˜*0* is the
  normalized corrected mass flow rate at which the compressor reaches
  the value of the **Maximum isentropic efficiency**
  parameter.

You can adjust the efficiency variables for different performance
characteristics. Alternatively, you can choose a constant efficiency value by
using the **Constant isentropic efficiency** parameter.

### Tabulated Data Parameterization

When you set **Parameterization** to
`Tabulated`, the isentropic efficiency, pressure ratio,
and corrected mass flow rate of the compressor are functions of the corrected speed,
*N*, and the map index, *β*. The block uses
linear interpolation between data points for the efficiency, pressure ratio, and
corrected mass flow rate.

If *β* exceeds 1, compressor surge occurs and the block assumes the
pressure ratio remains at *β* = 1, while the mass flow rate continues to change. If the simulation
conditions fall below *β* = 0, the block models the effects of choked flow, where the mass flow
rate remains at its value at *β* = 0 while the pressure ratio continues to change. To constrain the
compressor performance in the map boundaries, the block extrapolates isentropic
efficiency to the nearest point.

You can choose to be notified when the operating point pressure ratio exceeds the
surge pressure ratio. Set **Report when surge margin is negative**
to `Warning` to receive a warning or to
`Error` to stop the simulation when this occurs.

### Conservation of Mass

When you clear the **Model water droplets evaporation** parameter, the
block conserves mass such that

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

where:

- m˙*B* is the
  mixture mass flow rate at port **B**.
- m˙*wA* and m˙*wB* are the
  water vapor mass flow rates at ports **A** and
  **B**, respectively.
- m˙*gA* and m˙*gB* are the
  trace gas mass flow rates at ports **A** and
  **B**, respectively.
- m˙*dA* and m˙*dB* are the
  mass flow rates of the water droplets at ports **A**
  and **B**, respectively.

If you select **Model water droplets evaporation**, the mass
balance equations are

m˙A+m˙B+m˙devap=0m˙wA+m˙wB−m˙devap=0m˙gA+m˙gB=0m˙dA+m˙dB−m˙devap=0

The mass flow rate for the evaporated droplets, m˙*devap*, is

m˙devap=max{m˙A,0}rdevap.

*rdevap* is the mass
ratio of water droplets that can evaporate,

rdevap=min{rdA,xwcapacity},

which depends on *rdA*, the
mass ratio of water droplets to moist air at port **A**.

The capacity of the moist air to hold more water vapor is

xwcapacity=max{xwsB−xwA,0},

where *xwsB* is the
specific humidity at saturation, and
*xwA* is the
specific humidity.

### Conservation of Energy

The block computes the energy balance equation as

ΦA+ΦB+Pfluid=0,

where:

- *ΦA* is the energy flow rate
  at port **A**.
- *ΦB* is the energy flow rate
  at port **B**.
- *Pfluid* is the hydraulic
  power delivered to the fluid, which the block determines from the change
  in specific enthalpy, *Δh*, Pfluid=m˙AΔhtotal.

### Assumptions and Limitations

- The block assumes that superheated fluid enters at
  **A**.
- The block only defines compressor map flow from port
  **A** to port **B**. Reverse flow
  results may not be accurate.
- The block only represents dynamic compressors.
