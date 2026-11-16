---
type: simulink-block
title: 'Turbine (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Moist Air Library / Turbomachinery'
documentation_page: 'turbinema'
documentation_source_path: 'ref/turbinema.html'
language: en
---

# Turbine (MA)

## Ports

### Input

### **VN** — Nozzle opening fraction, unitless physical signal

Variable nozzle opening fraction, specified as a unitless physical
signal. The corrected mass flow rate scales linearly with the value of
**VN**. A fraction of `1`
corresponds to the tabulated data. The nozzle opening fraction does not
influence the isentropic efficiency.

#### Dependencies

To enable this port, select **Model variable
nozzle**.
### Output

### **W** — Moist air condensation rate, kg/s physical signal

Rate of condensation that the block removes from the moist air flow.
The value of this port does not include the portion of condensation that
is entrained as water droplets.

#### Dependencies

To enable this port, select **Model water vapor
condensation**.
### Conserving

### **A** — Moist air inlet moist air

Moist air conserving port associated with the fluid entry port.

### **B** — Moist air outlet moist air

Moist air conserving port associated with the fluid exit port.

### **C** — Turbine case mechanical translational

Port associated with the turbine casing.

### **R** — Turbine shaft mechanical translational

Port associated with the turbine shaft torque and angular
velocity.

## Parameters

### Turbine Map

### **Turbine map parameterization** — Performance parameterization `Analytical - Nominal pressure ratio and corrected mass flow rate` (default) | `Tabulated data - Flow rate and efficiency vs. pressure ratio` | `Tabulated data - Flow rate and efficiency vs. corrected speed and pressure ratio`

Performance parameterization specification:

- `Analytical - Nominal pressure ratio and
  corrected mass flow rate`: Parameterize
  turbine isentropic efficiency and corrected mass flow rate
  analytically.
- `Tabulated data - Flow rate and efficiency vs.
  pressure ratio`: Parameterize turbine
  isentropic efficiency and corrected mass flow rate by
  pressure ratio.
- `Tabulated data - Flow rate and efficiency vs.
  corrected speed and pressure ratio`:
  Parameterize turbine isentropic efficiency and corrected
  mass flow rate by corrected speed and pressure ratio.

### **Model variable nozzle** — Whether to enable the variable nozzle input port `Off` (default) | `On`

Whether to enable the variable nozzle input port
**VN**. When you do not enable the
**VN** port, the nozzle remains constant at
`1`.

### **Minimum nozzle opening fraction** — Minimum opening fraction `1e-3` (default) | positive scalar in the range (0,1]

Minimum nozzle opening fraction. This value is the lower boundary to
the signal at **VN**. The block multiplies the value of
this parameter by the mass flow rate to obtain the minimum corrected
mass flow rate through the turbine.

#### Dependencies

To enable this parameter, select **Model variable
nozzle**.

### **Maximum nozzle opening fraction** — Maximum opening fraction `1` (default) | positive scalar in the range (0,1]

Maximum nozzle opening fraction. This value is the upper boundary to
the signal at **VN**. The block multiplies the value of
this parameter by the mass flow rate to obtain the maximum corrected
mass flow rate through the turbine.

#### Dependencies

To enable this parameter, select **Model variable
nozzle**.

### **Corrected speed index vector, N** — Tabulated data shaft speed indices `100 .* [50, 60, 70, 80, 90, 100, 110]` rpm (default) | vector of positive scalars

Vector of constant shaft speeds for tabular parameterization of
corrected mass flow rate and isentropic efficiency.

#### Dependencies

To enable this parameter, set **Turbine map
parameterization** to `Tabulated data -
Flow rate and efficiency vs. corrected speed and pressure
ratio`.

### Flow Rate Data

### **Nominal pressure ratio** — Pressure ratio value `2` (default) | positive scalar

Pressure ratio value under nominal operating conditions for the
analytical parameterization.

#### Dependencies

To enable this parameter, set **Turbine map
parameterization** to `Analytical - Nominal
pressure ratio and corrected mass flow
rate`.

### **Nominal corrected mass flow rate** — Corrected mass flow rate value `48` kg/s (default) | positive scalar

Corrected mass flow rate value under nominal operating conditions for
the analytical parameterization.

#### Dependencies

To enable this parameter, set **Turbine map
parameterization** to `Analytical - Nominal
pressure ratio and corrected mass flow
rate`.

### **Pressure ratio vector, pr** — Vector of pressure ratios `[1.251, 1.345, 1.442, 1.521, 1.596, 1.692, 1.849, 1.972, 2.1, 2.173, 2.259, 2.3424]` (default) | vector of positive scalars

Vector of pressure ratio values for the tabulated parameterization of
corrected mass flow rate. This vector must have the same number of
elements as the **Corrected mass flow rate vector,
mdot(pr)** parameter and all elements must be greater than
1. The last element must be the pressure ratio at choked
conditions.

#### Dependencies

To enable this parameter, set **Turbine map
parameterization** to `Tabulated data -
Flow rate and efficiency vs. pressure
ratio`.

### **Corrected mass flow rate vector, mdot(pr)** — Vector of corrected mass flow rate values `[39.439, 43.01, 45.556, 46.801, 47.792, 48.388, 48.634, 48.67, 48.689, 48.747, 48.825, 48.912]` kg/s (default) | vector of positive scalars

Vector of corrected mass flow rate values for the tabulated
parameterization of corrected mass flow rate. This vector must have the
same number of elements as the **Pressure ratio vector,
pr** parameter and all elements must be greater than 0. The
last element must be the corrected mass flow rate at choked
conditions.

#### Dependencies

To enable this parameter, set **Turbine map
parameterization** to `Tabulated data -
Flow rate and efficiency vs. pressure
ratio`.

### **Pressure ratio table, pr(N,beta)** — Turbine map pressure ratio data *M*-by-*N* matrix (default)

*M*-by-*N* matrix of turbine
outlet-to-inlet pressure ratios at the specified corrected shaft speed
and β value. The block employs linear interpolation between the table
elements. *M* and *N* are the sizes of
the corresponding vectors:

- *M* is the number of vector elements in
  the **Corrected speed index vector, N**
  parameter.
- *N* is the number of β indices in the
  table.

The default table values are:

`[1.217, 1.285, 1.323, 1.363, 1.402, 1.427, 1.495, 1.545, 1.6,
1.687, 1.747, 1.8074; 1.231, 1.302, 1.356, 1.404, 1.443, 1.473,
1.525, 1.577, 1.635, 1.709, 1.782, 1.845; 1.242, 1.328, 1.388,
1.437, 1.528, 1.617, 1.704, 1.811, 1.915, 1.979, 2.053, 2.1226;
1.244, 1.339, 1.417, 1.465, 1.528, 1.584, 1.692, 1.787, 1.899, 2,
2.075, 2.1492; 1.245, 1.34, 1.425, 1.492, 1.546, 1.684, 1.748,
1.882, 1.987, 2.084, 2.167, 2.2458; 1.251, 1.345, 1.442, 1.521,
1.596, 1.692, 1.849, 1.972, 2.1, 2.173, 2.259, 2.3424; 1.248, 1.348,
1.447, 1.516, 1.581, 1.651, 1.749, 1.839, 1.93, 2.024, 2.154,
2.242]`

#### Dependencies

To enable this parameter, set **Turbine map
parameterization** to `Tabulated data -
Flow rate and efficiency vs. corrected speed and pressure
ratio`.

### **Corrected mass flow rate table, mdot(N,beta)** — Turbine map corrected mass flow rate data *M*-by-*N* matrix (default)

*M*-by-*N* matrix of corrected mass
flow rates at the specified corrected shaft speed and β value. The block
employs linear interpolation between the table elements.
*M* and *N* are the sizes of the
corresponding vectors:

- *M* is the number of vector elements in
  the **Constant speed index vector, N**
  parameter.
- *N* is the number of β indices in the
  table.

The default table values are:

`[40.403, 44.417, 46.653, 47.966, 48.97, 49.544, 50.001,
50.081, 50.086, 50.095, 50.09, 50.0922; 40.044, 43.754, 46.125,
47.626, 48.513, 49.105, 49.481, 49.58, 49.597, 49.624, 49.638,
49.633; 39.941, 43.795, 46.017, 47.335, 48.795, 49.199, 49.279,
49.27, 49.248, 49.23, 49.255, 49.2428; 39.896, 43.512, 45.914,
47.061, 48.011, 48.558, 48.943, 49.042, 49.069, 49.01, 49.046,
49.0266; 39.524, 42.934, 45.686, 46.743, 47.715, 48.67, 48.777,
48.836, 48.876, 48.836, 48.845, 48.8184; 39.439, 43.01, 45.556,
46.801, 47.792, 48.388, 48.634, 48.67, 48.639, 48.647, 48.625,
48.5912; 39.502, 42.849, 45.336, 46.385, 47.312, 47.877, 48.222,
48.397, 48.459, 48.482, 48.455, 48.414]` kg/s

#### Dependencies

To enable this parameter, set **Turbine map
parameterization** to `Tabulated data -
Flow rate and efficiency vs. corrected speed and pressure
ratio`.

### Efficiency Data

### **Constant isentropic efficiency** — Isentropic efficiency value `0.8` (default) | positive scalar

Isentropic efficiency under nominal operating conditions for the
analytical parametrization.

#### Dependencies

To enable this parameter, set **Turbine map
parameterization** to `Analytical - Nominal
pressure ratio and corrected mass flow
rate`.

### **Pressure ratio vector, pr** — Vector of pressure ratios `[1.252, 1.328, 1.425, 1.544, 1.642, 1.757, 1.873, 2.005, 2.1, 2.204, 2.248, 2.28]` (default) | vector of positive scalars

Vector of pressure ratio values for the tabulated parameterization of
isentropic efficiency. This vector must have the same number of elements
as the **Isentropic efficiency vector, eta(pr))**
parameter and all elements must be greater than 1.

#### Dependencies

To enable this parameter, set **Turbine map
parameterization** to `Tabulated data -
Flow rate and efficiency vs. pressure
ratio`.

### **Isentropic efficiency vector, eta(pr)** — Vector of isentropic efficiencies `[.559, .61, .673, .741, .788, .835, .869, .895, .908, .899, .854, .751]` (default) | vector of elements in the range (0,1]

Vector of isentropic efficiency values for the tabulated
parameterization of isentropic efficiency. This vector must have the
same number of elements as the **Pressure ratio vector,
pr** parameter and all elements must be greater than 0 and
less than or equal to 1.

#### Dependencies

To enable this parameter, set **Turbine map
parameterization** to `Tabulated data -
Flow rate and efficiency vs. pressure
ratio`.

### **Pressure ratio table, pr(N,beta)** — Turbine map pressure ratio data *M*-by-*N* matrix (default)

*M*-by-*N* matrix of turbine
outlet-to-inlet pressure ratios at the specified corrected shaft speed
and β value. The block employs linear interpolation between the table
elements. *M* and *N* are the sizes of
the corresponding vectors:

- *M* is the number of vector elements in
  the **Constant speed index vector, N**
  parameter.
- *N* is the number of β indices in the
  table.

The default table values are:

`[1.224, 1.246, 1.292, 1.387, 1.457, 1.534, 1.61, 1.686,
1.743, 1.79, 1.871, 1.914; 1.237, 1.25, 1.28, 1.369, 1.459, 1.553,
1.629, 1.716, 1.799, 1.846, 1.927, 1.97; 1.241, 1.255, 1.283, 1.326,
1.401, 1.509, 1.591, 1.704, 1.806, 1.913, 1.994, 2.037; 1.25, 1.265,
1.308, 1.364, 1.456, 1.532, 1.637, 1.739, 1.851, 1.934, 2.042,
2.085; 1.281, 1.314, 1.371, 1.425, 1.498, 1.574, 1.647, 1.749,
1.878, 1.979, 2.091, 2.18; 1.252, 1.328, 1.425, 1.544, 1.642, 1.757,
1.873, 2.005, 2.1, 2.204, 2.248, 2.28; 1.382, 1.43, 1.495, 1.586,
1.688, 1.791, 1.887, 1.99, 2.079, 2.158, 2.249,
2.217]`

#### Dependencies

To enable this parameter, set **Turbine map
parameterization** to `Tabulated data -
Flow rate and efficiency vs. corrected speed and pressure
ratio`.

### **Isentropic efficiency table, eta(N,beta)** — Turbine map isentropic efficiency data *M*-by-*N* matrix (default)

*M*-by-*N* matrix of turbine
isentropic efficiencies at the specified constant shaft speed and β
value. The block employs linear interpolation between the table
elements. *M* and *N* are the sizes of
the corresponding vectors:

- *M* is the number of vector elements in
  the **Constant speed index vector, N**
  parameter.
- *N* is the number of β indices in the
  table.

The default table values are:

`[.72, .754, .759, .739, .714, .679, .643, .603, .554, .524,
.494, .48; .716, .757, .794, .819, .812, .788, .761, .728, .692,
.662, .632, .618; .629, .691, .775, .831, .858, .869, .859, .842,
.816, .782, .752, .738; .594, .668, .757, .804, .857, .883, .892,
.893, .884, .865, .835, .821; .664, .72, .779, .823, .858, .883,
.897, .905, .904, .896, .883, .868; .559, .61, .673, .741, .788,
.835, .869, .895, .908, .899, .854, .751; .718, .785, .824, .855,
.882, .9, .908, .906, .884, .857, .804, .701]`

#### Dependencies

To enable this parameter, set **Turbine map
parameterization** to `Tabulated data -
Flow rate and efficiency vs. corrected speed and pressure
ratio`.

### Parameters

### **Reference pressure for corrected flow** — Correcting pressure `0.101325` MPa (default) | positive scalar

Pressure at which the turbine data consolidates to a corrected trend
line.

### **Reference temperature for corrected flow** — Correcting temperature `288.15` K (default) | positive scalar

Temperature at which the turbine data the turbine data consolidates to
a corrected trend line.

### **Reference relative humidity for corrected flow** — Correcting relative humidity `0` (default) | scalar in the range [0,1]

Relative humidity at which the turbine data consolidates to a
corrected trend line.

### **Mechanical efficiency** — Efficiency of conversion to torque `0.9` (default) | positive scalar in the range [0,1]

Efficiency of the conversion from reduction in specific enthalpy to
shaft torque.

### **Model water vapor condensation** — Option to model water vapor condensation `off` (default) | `on`

Option to model water vapor condensation due to temperature change in
the turbine.

### **Relative humidity at saturation** — Relative humidity above which condensation occurs `1` (default) | positive scalar

Relative humidity above which condensation occurs in the
compressor.

#### Dependencies

To enable this parameter, select **Model water vapor
condensation**.

### **Fraction of condensate entrained as water droplets** — Fraction of condensate in water droplets `1` (default) | scalar in the range [0,1]

Fraction of the condensate in the moist air that is entrained as water
droplets.

#### Dependencies

To enable this parameter, select **Model water vapor
condensation**.

### **Inlet area at port A** — Turbine inlet area `1` m^2 (default) | positive scalar

Turbine inlet cross-sectional area.

### **Outlet area at port B** — Turbine outlet area `1` m^2 (default) | positive scalar

Turbine outlet cross-sectional area.

## Libraries

Simscape / Fluids / Moist Air / Turbomachinery

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

Turbine in a moist air network

The Turbine (MA) block models a turbine in a moist air network. You can parameterize
the block as a tabulated turbine map that is either a 1-D function of pressure ratio or
2-D function of pressure ratio and corrected mass flow rate. Fluid flowing from port
**A** to port **B** generates torque. Port
**R** reports shaft torque and angular velocity relative to port
**C**, which represents the turbine casing.

When enabled, port **VN** represents the nozzle opening fraction.
This value linearly scales the corrected mass flow rate but does not influence the
turbine efficiency. A value of `1` corresponds to the data in the
turbine map.

### Turbine Map

To visualize the block map, right-click the block and select **Fluids** > **Plot Turbine Map**.

Each time you modify the block settings, click **Reload Data**
on the figure window.

The turbine map relates turbine performance, as a function of pressure ratio, to
the corrected mass flow rate and isentropic efficiency. The pressure ratio is the
ratio between the turbine inlet pressure and outlet pressure.

The turbine map plots two separate graphs: corrected mass flow rate versus
pressure ratio and isentropic efficiency versus pressure ratio. When you set the
**Turbine map parameterization** to  `Tabulated
data - flow rate and efficiency vs. corrected speed and pressure
ratio`, the plots also depend on the corrected rotor speed,
*N*. The indexing variable β does not need to be the same
between the mass flow rate and efficiency tables.

**Corrected Mass Flow Rate**

Due to the large changes in pressure and temperature inside a turbine, the
turbine map plots performance in terms of the corrected mass flow rate.

The map adjusts the corrected mass flow rate from the inlet mass flow rate by
using the reference pressure and reference temperature,

m˙corr=m˙A(TARA/γATrefRref/γref/pApref),

where:

- *ṁA* is the mass flow rate
  at port **A**.
- *TA* is the temperature at
  port **A**.
- *Tref* is the value of the
  **Reference temperature for corrected flow**
  parameter.
- *RA* is the mixture
  specific gas constant at port **A**.
- *Rref* is the mixture
  specific gas constant calculated at the values of the
  **Reference pressure for corrected flow**,
  **Reference temperature for corrected flow**,
  and **Reference relative humidity for corrected
  flow** parameters.
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
  parameter.

**Corrected Speed**

The block also adjusts the shaft speed, *ω*, according to the
reference temperature, such that the corrected shaft speed is

ωcorr=ωTARA/γATrefRref/γref.

### Shaft Torque

The block calculates the shaft torque, *τ*, as

τ=ηmm˙AΔhtotalω,

where:

- *Δhtotal* is the total change
  in the fluid specific enthalpy.
- *ηm* is the value of the
  **Mechanical efficiency** parameter.
- *ω* is the relative shaft angular velocity,
  *ωR -
  ωC*.

Reversed flow, from port **B** to port **A**, is
outside of the typical turbine operation mode and may not return accurate results. A
threshold region when flow approaches zero ensures the block generates no torque
when the flow rate is near zero or reversed.

### Analytical Parametrization

Use the analytical parametrization to create a turbine based on the expected
nominal operating conditions. When **Turbine map parameterization**
is `Analytical – nominal pressure ratio and corrected mass flow
rate`, the turbine isentropic efficiency is constant and the mass
flow rate is a function of the pressure ratio.

This image shows the default turbine map when you use the analytical
parameterization.

Analytical Turbine map

### Parameterization by Pressure Ratio

When **Turbine map parameterization** is `Tabulated
data - Flow rate and efficiency vs. pressure ratio`, the turbine
isentropic efficiency and mass flow rate are a function of the pressure ratio and do
not account for any changes in the turbine rotational speed.

The last element of the **Corrected mass flow rate vector,
mdot(pr)** and the **Pressure ratio vector, pr**
parameters represents the corrected mass flow rate and pressure ratio at choked flow
conditions.

This image shows the default turbine map when you use the 1-D parameterization.

1D Turbine map

### Parameterization by Pressure Ratio and Corrected Mass Flow Rate

When **Turbine map parameterization** is `Tabulated
data - Flow rate and efficiency vs. corrected speed and pressure
ratio`, the turbine isentropic efficiency, pressure ratio, and
corrected mass flow rate are a function of the corrected speed,
*N*, and the map index, *β*. The block uses linear
interpolation between data points for the efficiency, pressure ratio, and corrected
mass flow rate parameters.

The last column of the **Corrected mass flow rate table,
mdot(N,beta)** and the **Pressure ratio table,
pr(N,beta)** parameters represents the corrected mass flow rate and
pressure ratio at choked flow conditions.

This image shows the default turbine map when you use the 2-D
parameterization.

2D Turbine map

### Conservation of Mass

When you clear the **Model water vapor condensation** parameter,
the block conserves mass such that

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

If you select **Model water vapor condensation**, the mass
balance equations are

m˙A+m˙B−m˙wcond=0m˙wA+m˙wB−m˙wcond=0m˙gA+m˙gB=0m˙dA+m˙dB+γm˙wcond=0

where *γ* is the value of the **Fraction of condensate
entrained as water droplets** parameter.

The rate of water vapor condensation, m˙*wcond*, is

m˙wcond=max{m˙A,0}xwcond.

*xwcond* is the mass
fraction of water vapor that can condense,

xwcond=max{xwA−xwsB,0},

where *xwsB* is the
specific humidity at saturation and
*xwA* is the
specific humidity.

### Conservation of Energy

When you clear the **Model water vapor condensation** parameter,

ΦA+ΦB−Pfluid=0,

where:

- *ΦA* is the energy flow rate
  at port **A**.
- *ΦB* is the energy flow rate
  at port **B**.
- *Pfluid* is the hydraulic
  power delivered to the fluid, which the block determines from the change
  in specific enthalpy, *Δh*, Pfluid=m˙AΔhtotal.

If you select **Model water vapor condensation**, the block
computes the energy balance equation as

ΦA+ΦB−Pfluid−m˙wcond(1−λ)hdcond=0,

where
*hdcond* is
the specific enthalpy of the water that is removed from the moist air flow by
condensation.

### Assumptions and Limitations

- The shaft does not rotate under reversed flow conditions. Results
  during reversed flows may not be accurate.
