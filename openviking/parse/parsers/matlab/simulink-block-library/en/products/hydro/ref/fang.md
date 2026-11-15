---
type: simulink-block
title: 'Fan (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Gas Library / Turbomachinery'
documentation_page: 'fang'
documentation_source_path: 'ref/fang.html'
language: en
---

# Fan (G)

## Ports

### Conserving

### **A** — Fluid entry gas

Gas conserving port associated with the fluid.

### **B** — Fluid exit gas

Gas conserving port associated with the fluid.

### **R** — Shaft mechanical rotational

Mechanical rotational conserving port associated with the
shaft.

### **C** — Casing mechanical rotational

Mechanical rotational conserving port associated with the
casing.

## Parameters

### **Fan parameterization** — Fan performance model `Static pressure and flow rate at reference shaft speed` (default) | `1D tabulated data - static pressure vs. flow rate at reference shaft speed` | `2D tabulated data - static pressure vs. shaft speed and flow rate` | `2D tabulated data - flow rate vs. shaft speed and static pressure`

Fan performance model, specified as:

- `Static pressure and flow rate at reference shaft
  speed`: Specify fan performance based on
  typical, nominal, or rated pressure gain and volumetric flow
  rate.
- `1D tabulated data – static pressure vs flow rate
  at reference shaft speed`: Specify fan
  performance based on interpolation of pressure gain data as a
  function of volumetric flow rate.
- `2D tabulated data – static pressure vs shaft
  speed and flow rate`: Specify fan performance
  based on the interpolation of pressure gain data as a function
  of shaft speed and volumetric flow rate.
- `2D tabulated data – flow rate vs
  shaft speed and static pressure`: Specify fan
  performance based on the interpolation of volumetric flow rate
  data as a function of shaft speed and pressure gain.

### **Shaft power specification** — Power definition `Fan efficiency` (default) | `Brake power`

Fan power specification, specified as:

- `Fan efficiency`: Derive
  the mechanical power from the fan efficiency.
- `Mechanical power`: Specify
  the mechanical power directly.

### **Nominal volumetric flow rate** — Flow rate at reference shaft speed `0.12` m^3/s (default) | positive scalar

Volumetric flow rate through the fan at the reference shaft speed under
nominal, typical, or rated operating conditions.

#### Dependencies

To enable this parameter, set **Fan
parameterization** to `Static pressure and flow
rate at reference shaft speed`.

### **Nominal static pressure gain** — Pressure gain at reference shaft speed `5400` Pa (default) | positive scalar

Pressure increase from port **A** to port
**B** at the reference shaft speed under nominal,
typical, or rated operating conditions.

#### Dependencies

To enable this parameter, set **Fan
parameterization** to `Static pressure and flow
rate at reference shaft speed`.

### **Nominal efficiency** — Efficiency at reference shaft speed `0.40` (default) | positive scalar

Efficiency of converting the shaft power to fluid power at the reference
shaft speed under nominal, typical, or rated operating conditions.

#### Dependencies

To enable this parameter, set:

- **Fan parameterization** to
  `Static pressure and flow rate at reference
  shaft speed`.
- **Shaft power specification** to
  `Fan efficiency`.

### **Nominal mechanical power** — Power at nominal efficiency `1620` `W` (default) | positive scalar

Mechanical power driving moist air flow at the reference shaft speed under
nominal, typical, or rated operating conditions.

#### Dependencies

To enable this parameter, set:

- **Fan parameterization** to
  `Static pressure and flow rate at reference
  shaft speed`.
- **Shaft power specification** to
  `Brake power`.

### **Maximum static pressure gain at zero flow** — Maximum pressure at reference shaft speed `6400` `Pa` (default) | positive scalar

Pressure increase from port **A** to port
**B** at the reference shaft speed when there is no
flow through the fan.

#### Dependencies

To enable this parameter, set **Fan
parameterization** to `Static pressure and flow
rate at reference shaft speed`.

### **Maximum volumetric flow rate at zero pressure** — Maximum flow rate at reference shaft speed `0.24` `m^3/s` (default) | positive scalar

Free-delivery volumetric flow rate at the reference shaft speed and
constant pressure.

#### Dependencies

To enable this parameter, set **Fan
parameterization** to `Static pressure and flow
rate at reference shaft speed`.

### **Reference shaft speed** — Fan curve reference speed `3000` `rpm` (default) | positive scalar

Reference shaft angular velocity corresponding to the fan characteristic
curve data.

#### Dependencies

To enable this parameter, set **Fan
parameterization** to `Static pressure and flow
rate at reference shaft speed` or `1D
tabulated data - static pressure vs. flow rate at reference shaft
speed`.

### **Minimum shaft speed threshold as fraction of reference** — Threshold for minimum shaft speed `1e-2` (default) | positive scalar

Threshold for the minimum shaft speed as a fraction of the reference shaft
speed. The block uses this value to prevent the shaft speed from becoming
zero and causing a division by zero error in the expression for
*qref*.

#### Dependencies

To enable this parameter, set **Fan
parameterization** to `Static pressure and flow
rate at reference shaft speed` or `1D
tabulated data - static pressure vs. flow rate at reference shaft
speed`.

### **Volumetric flow rate vector** — Fan curve flow rate vector `[.0278, .0556, .0833, .111, .139, .167]` `m^3/s` (default) | vector

Vector of volumetric flow rate grid points for the 1-D interpolation of the fan
characteristic curve. When **Shaft power specification** is
`Brake power`, the fan data can extend beyond
the normal operating region, and these values can be negative.

#### Dependencies

To enable this parameter, set **Fan
parameterization** to `1D tabulated data -
static pressure vs. flow rate at reference shaft
speed`.

### **Static pressure gain vector** — Pressure gain for given volumetric flow rate `[6410, 6375, 6018, 5366, 4501, 3609]` `Pa` (default) | vector

Vector of pressure gain data points. Each element in the vector corresponds to an element
in the **Volumetric flow rate vector** parameter. The
pressure gain is the increase in pressure from port **A**
to port **B** at the reference shaft speed. When
**Shaft power specification** is `Brake
power`, the fan data can extend beyond the normal operating
region, and these values can be negative.

#### Dependencies

To enable this parameter, set **Fan
parameterization** to `1D tabulated data -
static pressure vs. flow rate at reference shaft
speed`.

### **Efficiency vector** — Efficiency for given volumetric flow rate `[.257, .394, .453, .47, .459, .415]` (default) | vector

Vector of fan efficiency data points. Each element in the vector
corresponds to an element in the **Volumetric flow rate
vector** parameter. The efficiency is the ratio of fluid power
to shaft mechanical power at the reference shaft speed.

#### Dependencies

To enable this parameter, set **Fan
parameterization** to `1D tabulated data -
static pressure vs. flow rate at reference shaft speed`
and **Shaft power specification** to `Fan
efficiency`.

### **Mechanical power vector** — Power for parameterization of torque `[693, 900, 1107, 1267, 1363, 1452]` W (default) | 1-by-*n* vector

Vector of shaft mechanical power data points. Each element in the vector corresponds to
an element in the **Volumetric flow rate vector**
parameter. The mechanical power is the power that drives the fan at the
reference shaft speed. These values can be negative if the fan data extends
beyond the normal operating region.

#### Dependencies

To enable this parameter, set **Fan
parameterization** to `1D tabulated data -
static pressure vs. flow rate at reference shaft speed`
and **Shaft power specification** to `Brake
power`.

### **Reference density** — Density associated with fan curve data `1.2` kg/m^3 (default) | positive scalar

Moist air density for a given characteristic fan curve.

#### Dependencies

To enable this parameter, set **Fan
parameterization** to `1D tabulated data -
static pressure vs. flow rate at reference shaft
speed`, `2D tabulated data - static pressure
vs. shaft speed and flow rate` or `2D
tabulated data - flow rate vs. shaft speed and static
pressure`.

### **Shaft speed vector, w** — Shaft angular velocity for given `[2400; 3000; 3600]` rpm (default) | vector

Vector of shaft angular velocity grid points for the 2-D interpolation of
the fan characteristic curves.

#### Dependencies

To enable this parameter, set **Fan parameterization** to
`2D tabulated data - static pressure vs. shaft speed and
flow rate` or `2D tabulated data - flow
rate vs. shaft speed and static pressure`.

### **Volumetric flow rate vector, q** — Flow rate for parameterization of pressure gain `[.0278, .0556, .0833, .111, .139, .167]` m^3/s (default) | 1-by-*n* vector

Vector of volumetric flow rate grid points for the 2-D interpolation of the fan
characteristic curves. When **Shaft power specification**
is `Brake power`, the fan data can extend beyond
the normal operating region, and these values can be negative.

#### Dependencies

To enable this parameter, set **Fan
parameterization** to `2D tabulated data -
static pressure vs. shaft speed and flow rate`.

### **Static pressure gain table, dp(w,q)** — Pressure for parameterization of pressure `[4111, 4010, 3551, 2881, 2167, 1453; 6410, 6375, 6018, 5366, 4501, 3609; 9217, 9285, 9022, 8428, 7552, 6482]` `Pa` (default) | *M*-by-*N* matrix

*M*-by-*N* matrix of pressure gain data points for the
2-D interpolation of the pressure gain. The pressure gain is the increase in
pressure from port **A** to port **B**.
When **Shaft power specification** is `Brake
power`, the fan data can extend beyond the normal operating
region, and these values can be negative. *M* and
*N* are the sizes of the corresponding vectors:

- *M* is the number of elements in the
  **Shaft speed vector, w** parameter. The
  elements corresponding to zero flow rate must be in strictly
  ascending order.
- *N* is the number of elements in the
  **Volumetric flow rate vector, q**
  parameter.

If your table has unknown data points, use `NaN` in place of these
values. The block fills in the `NaN` elements by
extrapolating based on the average slope of the fan curves. Do not use
artificial numerical values because these values distort fan behavior when
operating in that region. When using unknown data:

- The `NaN` elements in the table must be
  contiguous.
- The positions of the `NaN` elements in the
  **Static pressure gain table, dp(w,q)**,
  **Efficiency table, eta(w,q)**, and
  **Mechanical power table, W(w,q)**
  parameters must match each other.
- `NaN` elements must be located in the
  upper-right portion of the table, which corresponds to the
  highest volumetric flow rate and lowest shaft speed.

#### Dependencies

To enable this parameter, set **Fan
parameterization** to `2D tabulated data -
static pressure vs. shaft speed and flow rate`.

### **Efficiency table, eta(w,q)** — Efficiency for parameterization of torque `[.3, .434, .468, .459, .4, .3; .257, .394, .453, .47, .459, .415; .225, .359, .434, .461, .47, .459]` 1 (default) | *M*-by-*N* matrix

*M*-by-*N* matrix of efficiency data
points for the 2-D interpolation of
torque.
The efficiency is the ratio of fluid power to shaft mechanical power.
*M* and *N* are the sizes of the
corresponding vectors:

- *M* is the number of elements in the
  **Shaft speed vector, w** parameter.
- *N* is the number of elements in the
  **Volumetric flow rate vector, q**
  parameter.

If your table has unknown data points, use `NaN` in place of these
values. The block fills in the `NaN` elements by
extrapolating based on the average slope of the fan curves. Do not use
artificial numerical values because these values distort fan behavior when
operating in that region. When using unknown data:

- The `NaN` elements in the table must be
  contiguous.
- The positions of the `NaN` elements in the
  **Static pressure gain table, dp(w,q)**,
  **Efficiency table, eta(w,q)**, and
  **Mechanical power table, W(w,q)**
  parameters must match each other.
- `NaN` elements must be located in the
  upper-right portion of the table, which corresponds to the
  highest volumetric flow rate and lowest shaft speed.

#### Dependencies

To enable this parameter, set **Fan
parameterization** to `2D tabulated data -
static pressure vs. shaft speed and flow rate` and
**Shaft power specification** to `Fan
efficiency`.

### **Mechanical power table, W(w,q)** — Mechanical power for parameterization of torque `[381, 514, 632, 697, 753, 809; 693, 900, 1107, 1267, 1363, 1452; 1139, 1438, 1732, 2029, 2233, 2358]` W (default) | *M*-by-*N* matrix

*M*-by-*N* table of mechanical power data points for
the 2-D interpolation of torque. These values can be negative if the fan
data extends beyond the normal operating region. The mechanical power is the
power that drives the fan. *M* and *N* are
the sizes of the corresponding vectors:

- *M* is the number of elements in the
  **Shaft speed vector, w** parameter. The
  elements corresponding to zero flow rate must be in strictly
  ascending order.
- *N* is the number of elements in the
  **Volumetric flow rate vector, q**
  parameter.

If your table has unknown data points, use `NaN` in place of these
values. The block fills in the `NaN` elements by
extrapolating based on the average slope of the fan curves. Do not use
artificial numerical values because these values distort fan behavior when
operating in that region. When using unknown data:

- The `NaN` elements in the table must be
  contiguous.
- The positions of the `NaN` elements in the
  **Static pressure gain table, dp(w,q)**,
  **Efficiency table, eta(w,q)**, and
  **Mechanical power table, W(w,q)**
  parameters must match each other.
- `NaN` elements must be located in the
  upper-right portion of the table, which corresponds to the
  highest volumetric flow rate and lowest shaft speed.

#### Dependencies

To enable this parameter, set **Fan
parameterization** to `2D tabulated data -
static pressure vs. shaft speed and flow rate` and
**Shaft power specification** to `Brake
power`.

### **Static pressure gain vector, dp** — Pressure for parameterization of flow rate `[31, 62, 93, 124]` Pa (default) | 1-by-*N* vector

Vector of pressure gain grid points for the 2-D interpolation of the fan characteristic
curves. When **Shaft power specification** is
`Brake power`, the fan data can extend beyond
the normal operating region, and these values can be negative.

#### Dependencies

To enable this parameter, set **Fan
parameterization** to `2D tabulated data - flow
rate vs. shaft speed and static pressure`.

### **Volumetric flow rate table, q(w,dp)** — Flow rate for parameterization of flow rate `[.802, .759, .703, .611; .936, .902, .862, .81; 1.056, 1.027, .994, .956]` m^3/s (default) | *M*-by-*N* matrix

*M*-by-*N* matrix of volumetric flow rate data points
for the 2-D interpolation of volumetric flow rate. When **Shaft
power specification** is `Brake
power`, the fan data can extend beyond the normal operating
region, and these values can be negative. *M* and
*N* are the sizes of the corresponding vectors:

- *M* is the number of elements in the
  **Shaft speed vector, w** parameter. The
  elements corresponding to zero flow rate must be in strictly
  ascending order.
- *N* is the number of elements in the
  **Static pressure gain vector, Dp**
  parameter.

If your table has unknown data points, use `NaN` in place of these
values. The block fills in the `NaN` elements by
extrapolating based on the average slope of the fan curves. Do not use
artificial numerical values because these values distort fan behavior when
operating in that region. When using unknown data:

- The `NaN` elements in the table must be
  contiguous.
- The positions of the `NaN` elements in the
  **Volumetric flow rate table, q(w,dp)**,
  **Efficiency table, eta(w,dp)**, and
  **Mechanical power table, W(w,dp)**
  parameters must match each other.
- `NaN` elements must be located in the
  upper-right portion of the table, which corresponds to the
  highest volumetric flow rate and lowest shaft speed.

#### Dependencies

To enable this parameter, set **Fan
parameterization** to `2D tabulated data - flow
rate vs. shaft speed and static pressure`.

### **Efficiency table, eta(w,dp)** — Efficiency for parameterization of torque `[.088, .162, .22, .261; .068, .128, .18, .222; .055, .105, .148, .188]` (default) | *M*-by-*N* matrix

*M*-by-*N* matrix of efficiency data
points for the 2-D interpolation of torque. The efficiency is the ratio of
fluid power to shaft mechanical power. *M* and
*N* are the sizes of the corresponding vectors:

- *M* is the number of elements in the
  **Shaft speed vector, w** parameter.
- *N* is the number of elements in the
  **Static pressure gain vector, Dp**
  parameter.

If your table has unknown data points, use `NaN` in place of these
values. The block fills in the `NaN` elements by
extrapolating based on the average slope of the fan curves. Do not use
artificial numerical values because these values distort fan behavior when
operating in that region. When using unknown data:

- The `NaN` elements in the table must be
  contiguous.
- The positions of the `NaN` elements in the
  **Volumetric flow rate table, q(w,dp)**,
  **Efficiency table, eta(w,dp)**, and
  **Mechanical power table, W(w,dp)**
  parameters must match each other.
- `NaN` elements must be located in the
  upper-right portion of the table, which corresponds to the
  highest volumetric flow rate and lowest shaft speed.

#### Dependencies

To enable this parameter, set **Fan
parameterization** to `2D tabulated data - flow
rate vs. shaft speed and static pressure` and
**Shaft power specification** to `Fan
efficiency`.

### **Mechanical power table, W(w,dp)** — Mechanical power for parameterization of torque `[283, 290, 297, 290; 427, 437, 445, 452; 595, 606, 625, 631]` `W` (default) | *M*-by-*N* matrix

*M*-by-*N* matrix of mechanical power data points for
the 2-D interpolation of torque. These values can be negative if the fan
data extends beyond the normal operating region. The mechanical power is the
power that drives the fan. *M* and *N* are
the sizes of the corresponding vectors:

- *M* is the number of elements in the
  **Shaft speed vector, w** parameter. The
  elements corresponding to zero flow rate must be in strictly
  ascending order.
- *N* is the number of elements in the
  **Static pressure gain vector, Dp**
  parameter.

If your table has unknown data points, use `NaN` in place of these
values. The block fills in the `NaN` elements by
extrapolating based on the average slope of the fan curves. Do not use
artificial numerical values because these values distort fan behavior when
operating in that region. When using unknown data:

- The `NaN` elements in the table must be
  contiguous.
- The positions of the `NaN` elements in the
  **Volumetric flow rate table, q(w,dp)**,
  **Efficiency table, eta(w,dp)**, and
  **Mechanical power table, W(w,dp)**
  parameters must match each other.
- `NaN` elements must be located in the
  upper-right portion of the table, which corresponds to the
  highest volumetric flow rate and lowest shaft speed.

#### Dependencies

To enable this parameter, set **Fan
parameterization** to `2D tabulated data - flow
rate vs. shaft speed and static pressure` and
**Shaft power specification** to `Brake
power`.

### **Fan diameter scale factor** — Model-to-reference scale factor `1` (default) | positive scalar

Geometric scale factor to increase or decrease the size of the simulated
fan from the given fan parameterization. The scaling may not be accurate for
scale factors much larger or much smaller than 1.

### **Mechanical orientation** — Rotational orientation `Positive angular velocity of port R relative to port C corresponds to normal fan operation` (default) | `Negative angular velocity of port R relative to port C corresponds to normal fan operation`

Normal operating shaft direction. By default, flow and pressure gain are
from port **A** to port **B**.

### **Inlet flow area (port A)** — Port A area `0.01` `m^2` (default) | positive scalar

Cross-sectional area of the moist air flow at the fan inlet.

### **Outlet flow area (port B)** — Port B area `0.01` `m^2` (default) | positive scalar

Cross-sectional area of the moist air flow at the fan outlet.

## Libraries

Simscape / Fluids / Gas / Turbomachinery

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

### R2023a: Expose threshold for low shaft speed

Use the **Minimum shaft speed threshold as fraction of
reference** parameter to control the minimum shaft speed threshold as a
fraction of the reference shaft speed. The **Minimum shaft speed threshold
as fraction of reference** parameter is available in the block when the
**Fan parameterization** parameter is `Static
pressure and flow rate at reference shaft speed` or `1D
tabulated data – static pressure vs flow rate at reference shaft
speed`.

### R2022b: Extend performance beyond normal operating conditions

Both the 1-D and 2-D parameterizations now allow negative values. When simulation
is outside the range of the provided table, block extrapolates the pressure based on
the average slope of the fan curves.

You can now use `NaN` elements where data is unavailable. These
2-D tabulated fan parameters support contiguous `NaN` elements in
the upper-right portion of the table:

- **Static pressure gain table, dp(w,q)**
- **Efficiency table, eta(w,q)**
- **Mechanical power table, W(w,q)**
- **Volumetric flow rate table, q(w,dp)**
- **Efficiency table, eta(w,dp)**
- **Mechanical power table, W(w,dp)**

For each block, if the shaft rotates opposite to the specified mechanical
orientation, the pressure difference across the block drops to zero and the results
may not be accurate.

### R2021b: 2-D Tabulated Data Parameterization: Flow Rate as a Function of Shaft Speed and Pressure Ratio

In R2021b, the block no longer supports the `2-D Tabulated Data
Parameterization: Flow Rate as a Function of Shaft Speed and Pressure
Ratio` parameterization. In R2021b and later, if you open models
created in a prior release that include the Fan (G)
block, Simscape™
Fluids™ replaces the block with the Fan (MA) -
Legacy block. This block supports the `2-D Tabulated
Data Parameterization: Flow Rate as a Function of Shaft Speed and Pressure
Ratio` setting.

You can preserve the functionality of a model using this parameterization by
setting **Fan parameterization** to `2D tabulated data
- flow rate vs. shaft speed and static pressure`1
and converting the ratios to absolute values. An example script that
performs this conversion takes in the legacy parameters
`omega_DpMax_TLU`, `DpMax_TLU`,
`omega_flow_TLU`, `Dp_DpMax_TLU`,
`flow_rate_TLU`, and `eta_flow_TLU` and
returns the converted parameters `omega_g_TLU`,
`pressure_g_TLU`, `pressure_g_TLU`, and
`eta_g_TLU`:

```
% Shaft speed vector for maximum pressure rise vector
omega_DpMax_TLU = [1800, 2400, 3000];

% Maximum pressure rise vector
DpMax_TLU       = [400, 1200, 2000];

% Shaft speed vector, omega
omega_flow_TLU  = [1800, 2400, 3000];

% Static pressure rise ratio vector, Dp/DpMax
Dp_DpMax_TLU    = linspace(0, 1, 4);

% Flow rate table, q(omega,Dp/DpMax)
flow_rate_TLU   = [
    0.33    0.26    0.18    0.07
    1.20    0.91    0.64    0.26
    1.84    1.61    1.13    0.46];

% Total efficiency table, Eta(omega,Dp/DpMax)
eta_flow_TLU    = [
    0.22    0.25    0.27    0.28
    0.48    0.52    0.55    0.53
    0.42    0.45    0.49    0.44];

% Create interpolants of the tables
DpMax_TLU_interp = griddedInterpolant(omega_DpMax_TLU, DpMax_TLU, ...
    'linear', 'linear');

flow_rate_TLU_interp = griddedInterpolant({omega_flow_TLU, Dp_DpMax_TLU}, flow_rate_TLU, ...
    'linear', 'linear');

eta_flow_TLU_interp = griddedInterpolant({omega_flow_TLU, Dp_DpMax_TLU}, eta_flow_TLU, ...
    'linear', 'nearest');

% Maximum pressure rise
DpMax = DpMax_TLU_interp(max(omega_flow_TLU, omega_DpMax_TLU(1)));

% Shaft speed vector, w
omega_q_TLU = omega_flow_TLU;

% Static pressure gain vector, Dp
pressure_q_TLU = unique(DpMax(:)*Dp_DpMax_TLU(:)');

% Interpolation query points as full grid arrays
omega_grid = omega_q_TLU(:)*ones(1, length(pressure_q_TLU));

Dp_DpMax_grid = pressure_q_TLU(:)' ./ DpMax(:);

% Volumetric flow rate table, q(w,Dp)
flow_rate_q_TLU = flow_rate_TLU_interp(omega_grid, Dp_DpMax_grid);

flow_rate_q_TLU = max(flow_rate_q_TLU, 1e-4*flow_rate_TLU(1,1)); % keep it > 0

% Efficiency table, eta(w,Dp)
eta_q_TLU = eta_flow_TLU_interp(omega_grid, Dp_DpMax_grid);
```

## Description

Fan in gas network

The Fan (G) block represents a fan in a gas network. You can
model the torque and pressure gain over the fan as a function of static pressure and
flow rate or by using 1D or 2D tabulated reference pressure, shaft speed, and flow rate
data.

By default, flow and pressure gain are from port **A** to port
**B**. Port **C** represents the fan casing, and
port **R** represents the fan shaft. You can specify the normal
operating shaft direction in the **Mechanical orientation** parameter.
If the shaft begins to spin in the opposite direction, the pressure difference across
the fan drops to zero.

### Parameterization by Nominal Pressure, Flow Rate, and Shaft Speed

When you set the **Fan parameterization** parameter to `Static
pressure and flow rate at reference shaft speed`, the block uses
the analytical fan affinity laws and reference pressure differential to calculate
the pressure gain from port **A** to port **B**:

pB−pA=Δpref(ωωref)2(DDref)2,

where:

- *Δpref* is the reference
  pressure differential. The block uses a quadratic fit of the fan
  pressure differential values at the **Maximum static pressure
  gain at zero flow**, **Nominal static pressure
  gain**, and **Maximum volumetric flow rate at zero
  pressure** parameters.
- *ω* is the shaft angular velocity,
  *ωR* –
  *ωC*.
- *ωref* is the
  **Reference shaft speed** parameter.
- DDref is the **Fan diameter scale factor**
  parameter.

The block calculates the shaft torque from the reference mechanical
power and the fan affinity laws:

τ=Φrefω2ωref3(DDref)5.

Where *Φref* is the proportion of the pressure gain
to the fan efficiency:

Φref=qrefΔprefηref.

When you set the **Shaft power specification** parameter to
`Fan efficiency`, the block uses a quadratic fit of
efficiency between the fan peak performance,
*ηnom*, and 0.
*ηnom* is equivalent to the
**Nominal efficiency** parameter, which the block interprets as
the peak efficiency. If you set the **Shaft power specification**
parameter to `Brake power`, the block derives the nominal
fan efficiency from the nominal brake power,
*Φnom*, at peak or nominal conditions:

ηnom=qnomΔpnomΦnom.

The block assumes the efficiency is zero when there is no flow or when the flow reaches the
maximum volumetric flow rate at zero pressure. The block uses the current flow
*q* to compute the reference flow rate as:

qref=qωrefω(DrefD)3.

### 1-D Tabulated Data Parameterization: Pressure as a Function of Flow Rate at Reference Shaft Speed

When you set the **Fan parameterization** parameter to `1D
tabulated data - static pressure vs. flow rate at reference shaft
speed`, you can model fan performance as a function of volumetric
flow rate. The block interpolates the pressure gain from port **A**
to port **B** from the 1-D **Static pressure gain
vector** parameter,
*Δpref(qref)*:

pB−pA=Δpref(qref)(ρρref)(ωωref)2(DDref)2.

Here, *ρ* is the moist air density, and
*ρref* is the reference density,
which is equivalent to the **Reference density** parameter. The
block calculates the shaft torque from the reference mechanical power and the fan
affinity laws:

τ=Φref(qref)ω2ωref3(ρρref)(DDref)5,

where *ρref* is the **Reference
density**.

The block uses the current flow *q* to compute the reference flow rate:

qref=qωrefω(DrefD)3.

When the simulation is outside the range of the provided tables, the block
extrapolates pressure based on the average slope of the fan curves and the reference
torque to the nearest point.

### 2-D Tabulated Data Parameterization: Pressure as a Function of Shaft Speed and Flow Rate

When you set the **Fan parameterization** parameter to `2D
tabulated data - static pressure vs. shaft speed and flow rate`,
you can model fan performance as a 2-D function of volumetric flow rate and angular
velocity. The block interpolates the pressure gain from port **A**
to port **B** from the 2-D **Static pressure gain table,
dp(w,q)** parameter. The block defines the reference pressure gain,
*Δpref(qref,ω)*, as

pB−pA=Δpref(qref,ω)(ρρref)(DDref)2.

The block calculates shaft torque from the reference mechanical
power and the fan affinity laws:

τ=Φref(qref,ω)ω(ρρref)(DDref)5,

where the reference mechanical power is a function of the reference flow rate and
the current shaft speed.

The block uses the current flow *q* to compute the reference flow rate:

qref=q(DrefD)3.

When the simulation is outside the range of the provided tables, the block
extrapolates pressure based on the average slope of the fan curves and the reference
torque to the nearest point.

**Missing Data**

If your table has unknown data points, use `NaN` in place of these
values. The block fills in the `NaN` elements by extrapolating
based on the average slope of the fan curves. Do not use artificial numerical
values because these values distort fan behavior when operating in that region.
When using unknown data:

- The `NaN` elements in the table must be
  contiguous.
- The positions of the `NaN` elements in the
  **Static pressure gain table, dp(w,q)**,
  **Efficiency table, eta(w,q)**, and
  **Mechanical power table, W(w,q)** parameters
  must match each other.
- `NaN` elements must be located in the upper-right
  portion of the table, which corresponds to the highest volumetric
  flow rate and lowest shaft speed.

### 2-D Tabulated Data Parameterization: Flow Rate as a Function of Shaft Speed and Pressure

When you set the **Fan parameterization** parameter to `2D
tabulated data - flow rate vs. shaft speed and static pressure`,
you can model the flow rate through the fan as a 2-D function of pressure and
angular velocity. The volumetric flow rate is interpolated from the 2-D
**Volumetric flow rate table, q(w,dp)** parameter,
*qref*. The reference flow rate is a
function of the reference pressure gain,
*Δpref*, and the current shaft speed,
*ω*:

q=qref(Δpref,ω)(DDref)3,

where the reference pressure gain derives from the pressure
differential over the fan:

Δpref=(pB−pA)(ρrefρ)(DrefD)2.

The shaft torque derives from the reference mechanical power and the fan affinity laws:

τ=Φref(Δpref,ω)ω(ρρref)(DDref)5,

where the reference mechanical power is a function of the reference flow rate and
the current shaft speed.

When the simulation is outside the range of the provided tables, the block
extrapolates pressure based on the average slope of the fan curves and the reference
torque to the nearest point.

**Missing Data**

If your table has unknown data points, use `NaN` in place of these
values. The block fills in the `NaN` elements by extrapolating
based on the average slope of the fan curves. Do not use artificial numerical
values because these values distort fan behavior when operating in that region.
When using unknown data:

- The `NaN` elements in the table must be
  contiguous.
- The positions of the `NaN` elements in the
  **Volumetric flow rate table, q(w,dp)**,
  **Efficiency table, eta(w,dp)**, and
  **Mechanical power table, W(w,dp)**
  parameters must match each other.
- `NaN` elements must be located in the upper-right
  portion of the table, which corresponds to the highest volumetric
  flow rate and lowest shaft speed.

### Power and Efficiency

You can specify shaft power as either fan efficiency or brake power.

The block calculates efficiency as

η=ΦfluidΦbrake,

where the *brake power*, or mechanical power
measured at the shaft, is

Φbrake=τω.

The block calculates fluid power as

Φfluid=q(pB−pA).

The block calculates torque as

τ=Φbrakeω.

### Visualizing the Fan Curve

You can check the parameterized fan performance by plotting the pressure, power,
efficiency, and torque as a function of the flow. To generate a plot of the current
fan settings, right-click on the block and select **Fluids** > **Plot Fan Characteristics**. If you change settings or data, click **Apply** on
the block parameters and click **Reload Data** on the fan curve
figure.

The default block parameterization results in these plots:

Plot of fan characteristic curves

### Assumptions and Limitations

- If the shaft rotates opposite to the specified mechanical orientation,
  pressure difference across the block drops to zero and the results may not
  be accurate.
- The block assumes that the fan is quasi-steady.
- The block simulates fan performance in terms of static pressure rise, and
  not total fan pressure.
