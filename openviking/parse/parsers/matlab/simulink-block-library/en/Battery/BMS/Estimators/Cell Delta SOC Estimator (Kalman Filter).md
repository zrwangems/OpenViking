---
type: simulink-block
title: 'Cell Delta SOC Estimator (Kalman Filter)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'BMS / Estimators'
documentation_page: 'celldeltasocestimatorkalmanfilter'
documentation_source_path: 'ref/celldeltasocestimatorkalmanfilter.html'
language: en
---

# Cell Delta SOC Estimator (Kalman Filter)

## Ports

### Input

### **Current** — Battery current, ampere scalar | vector

Battery current, in ampere, specified as a scalar for a single cell or a vector
for multiple cells. To specify this input as a vector of cell currents, select the
**Specify Current input as cell current(s)** parameter.

### **CellVoltage** — Cell voltage, volt scalar | vector

Cell voltage, in volt, specified as a scalar for a single cell or a vector for
multiple cells. The size of this input port must be equal to the size of the
**CellTemperature** and **dInvCellAH** input
ports.

### **CellTemperature** — Cell temperature, K scalar | vector

Cell temperature, specified as a scalar for a single cell or a vector for multiple
cells. The size of this input port must be equal to the size of the
**CellVoltage** and **dInvCellAH** input
ports.

### **dInvCellAH** — Inverse delta cell capacity, A\*Hr scalar | vector

Inverse delta cell capacity of the battery, in ampere-hour, specified as a scalar
for a single cell or a vector for multiple cells. The size of this input port must be
equal to the size of the **CellVoltage**,
**CellTemperature**, and **CellR0** input
ports.

### **PackSOC** — Average SOC of battery pack, unitless scalar

Average SOC of the battery pack, specified as a scalar.

### **Vdyn** — Average dynamic overpotential voltage of battery pack, volt scalar

Average dynamic overpotential voltage of the battery pack, in volt, specified as a
scalar.
### Output

### **CellSOC** — SOC of battery cell scalar | vector

SOC of the battery cell, returned as a scalar or a vector. The size of this output
port is equal to the size of the **CellVoltage**,
**CellTemperature**, and **dInvCellAH** input
ports.

## Parameters

### Main

### **Specify Current input as cell current(s)** — Option to specify current input port as vector `off` (default) | `on`

Option to specify the value of the **Current** input port as a vector
of cell currents. If you select this parameter, the value at the
**Current** input port can be a scalar or a vector of size equal to
the size of the block inputs.

### **Filter type** — Kalman filter type `Extended Kalman filter` (default) | `Extended Kalman-Bucy filter` | `Unscented Kalman filter` | `Unscented Kalman-Bucy filter`

Type of Kalman filter that this block uses to estimate the battery state of
charge.

### **Alpha** — Alpha coefficient `1` (default) | scalar in the range (0,1]

Coefficient that controls the spread of the sigma points. The block uses this
parameter in its implementation of the equations for the unscented Kalman filter and
the unscented Kalman-Bucy filter.

#### Dependencies

To enable this parameter, set **Filter type** to
`Unscented Kalman filter` or `Unscented
Kalman-Bucy filter`.

### **Beta** — Beta coefficient `2` (default) | nonnegative scalar

Coefficient related to the distribution. The block uses this parameter in its
implementation of the unscented Kalman filter and the unscented Kalman-Bucy
filter.

#### Dependencies

To enable this parameter, set **Filter type** to
`Unscented Kalman filter` or `Unscented
Kalman-Bucy filter`.

### **Kappa** — Kappa coefficient `0` (default) | scalar in the range [0, 3]

Coefficient that controls the spread of the sigma points. The block uses this
parameter in its implementation of the equations for the unscented Kalman filter and
the unscented Kalman-Bucy filter.

#### Dependencies

To enable this parameter, set **Filter type** to
`Unscented Kalman filter` or `Unscented
Kalman-Bucy filter`.

### **Covariance of the process noise, Q** — Covariance of the process noise `0.0001` (default) | scalar

Covariance of the noise in the states.

### **Covariance of the measurement noise, R** — Covariance of the measurement noise `0.7` (default) | scalar

Covariance of the noise in the measurements.

### **Initial state error covariance, P0** — Initial state error covariance `1e-3` (default) | scalar

Covariance of the initial state error. This parameter defines the deviation in the
initialization of the state.

### **Sample time (-1 for inherited)** — Block sample time `1` (default) | 0 | -1 | integer

Time between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

For inherited discrete-time operation, specify this parameter as
`-1`. For discrete-time operation, specify this parameter as a
positive integer. For continuous-time operation, specify this parameter as
`0`.

If this block is in a masked subsystem or a variant subsystem that supports
switching between continuous operation and discrete operation, promote the sample time
parameter. Promoting the sample time parameter ensures correct switching between the
continuous and discrete implementations of the block. For more information, see Promote Block Parameters on a Mask.

#### Dependencies

To enable this parameter, set **Filter type** to
`Extended Kalman filter` or `Unscented Kalman
filter`.

### System Model

### **Vector of state-of-charge values, SOC (-)** — SOC breakpoints `[0, .1, .25, .5, .75, .9, 1]` (default) | vector of scalars in the range [0, 1]

Vector of the state of charge breakpoints defining the points at which you specify
lookup data. The entries of this vector must be in strictly ascending order.

### **Vector of temperatures, T** — Temperature breakpoints `[278, 293, 313]` (default) | vector of positive scalars

Vector of temperature breakpoints defining the points at which you specify lookup
data. This vector must be in strictly ascending order and greater than 0 K. The
physical unit of this parameter must be the same as the physical unit of the
**CellTemperature** input port.

### **Terminal resistance, R0(SOC,T), (ohm)** — R0 lookup table with temperature breakpoint `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]` (default) | matrix of positive entries

Lookup data for series resistance of the battery at the specified SOC and
temperature breakpoints.

### **No-load voltage, V0(SOC,T), (V)** — *V*0 lookup table `[3.49, 3.5, 3.51; 3.55, 3.57, 3.56; 3.62, 3.63, 3.64; 3.71, 3.71, 3.72; 3.91, 3.93, 3.94; 4.07, 4.08, 4.08; 4.19, 4.19, 4.19]` (default) | matrix of nonnegative entries

Lookup data, in volt, for open-circuit voltages across the fundamental battery
model at the specified SOC. The number of rows of this matrix is equal to the size of
the **Vector of state-of-charge values, SOC (-)** parameter. The
number of columns of this matrix is equal to the size of the **Vector of
temperatures, T** parameter.

### Signal Attributes

### **Algorithm data type** — Option to choose data type for block algorithm `Inherit: auto` (default) | `double` | `single` | `<data type expression>`

*Since R2025a*

Option to choose the data type for the block algorithm, specified as one of these values:

- `Inherit: auto` — You can simulate the block in
  both `single` and `double`
  precision. You must explicitly provide the inputs and parameters as either
  `single` or
  `double`.
- `double` — The block algorithm casts all inputs
  and parameters to `double` data type.
- `single` — The block algorithm casts all inputs
  and parameters to `single` data type.
- `<data type expression>` — The block
  algorithm casts all inputs and parameters to the data type object you
  specify.

Click the **Show data type assistant** button  to display the **Data Type Assistant**, which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant and Control Data Types of Signals.

## Libraries

Simscape / Battery / BMS / Estimators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

State of charge estimator with cell delta Kalman filter

The Cell Delta SOC Estimator (Kalman Filter) block implements an estimator
that calculates the state of charge (SOC) of a battery by using the cell delta Kalman filter.
The delta SOC is the internal estimator state, the current is the control input, and the cell
voltage is the measurement.

This block supports single-precision and double-precision
floating-point simulation.

**Note**

To enable inherited single-precision floating-point simulation, the data type of all
inputs and parameters, except for the **Sample time (-1 for
inherited)** parameter, must be `single`.

For continuous-time simulation, set the **Filter type** parameter to
`Extended Kalman-Bucy filter` or `Unscented Kalman-Bucy
filter`.

**Note**

Continuous-time implementation of this block works only in a double-precision
floating-point simulation. If you provide single-precision floating-point parameters and
inputs, this block casts them to double-precision floating-point values to prevent
errors.

For discrete-time simulation, set the **Filter type** parameter to
`Extended Kalman filter` or `Unscented Kalman
filter` and the **Sample time (-1 for inherited)** parameter
to a positive value or `-1`.

### Equations

This equation defines the cell delta SOC:

ΔSOCi=SOCi−SOC¯,i=1,…,Ns,

where *SOC*i is the state of
charge of cell `i`, SOC¯ is the pack-average state of charge, and
`Ns` is the number of series-connected cells.

This equation defines the inverse delta cell capacity:

ΔAHinv,i=AHinv,i−AHinv¯,

where AHinv,i=1AHi is the inverse cell capacity of cell `i` and AH¯inv=1AH¯ is the average inverse capacity of the battery.

The state-space model for the delta SOC is

dΔSOCidt=−i⋅ΔAHinv,i3600Vt,i=V0(SOC¯+ΔSOCi,T¯)−iR0−V¯dyn

where `Vt,i` is the terminal
voltage of cell `i` and *R0* is the
terminal resistance.

For the Kalman filter algorithms, the block uses dΔSOCi as the state and these processes and observation functions:

f(ΔSOCi)=−i⋅ΔAHinv,i3600h(dΔSOCi)=V0(SOC¯+ΔSOCi,T¯)−iR0−V¯dyn

The extended Kalman filter (EKF) relies on a linearization at every time step to
approximate the nonlinear system. To linearize at every time step, the algorithm computes
these Jacobians online:

F=∂f∂ΔSOCi=0H=∂V0∂ΔSOCi

The EKF is a discrete-time algorithm. After the discretization, the Jacobians are:

Fd=1Hd=∂V0∂ΔSOCi

The unscented Kalman filter uses nonlinear transformations on a set of sigma points that
the algorithm chooses deterministically.

The block then computes the cell SOC using this equation:

SOCi=SOC¯+ΔSOCi.

The implementation of the Kalman filter for capacity estimation follows the theory in
the SOC Estimator (Kalman
Filter) block for the one-state model described in this section.
