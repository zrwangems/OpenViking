---
type: simulink-block
title: 'Battery Capacity Estimator (Kalman Filter)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Management System / Estimators\u200b / Health Estimation'
documentation_page: 'batterycapacityestimatorkalmanfilter'
documentation_source_path: 'ref/batterycapacityestimatorkalmanfilter.html'
language: en
---

# Battery Capacity Estimator (Kalman Filter)

## Ports

### Input

### **Current** — Battery current, ampere scalar | vector

Battery current, in ampere, specified as a scalar for a single cell or
a vector for multiple cells. To specify this input as a vector of cell
currents, select the **Specify Current input as cell
current(s)** parameter.

### **CellSOC** — Cell state of charge, unitless scalar | vector

State of charge of one or multiple cells, specified as a scalar or
vector of entries in the range [0, 1]. The size of this input port must
be equal to the size of the **InitialCellAH** input
port.

### **InitialCellAH** — Initial cell capacity, A\*Hr scalar | vector

Initial cell capacity of the battery, in ampere-hour, specified as a
scalar for a single cell or a vector for multiple cells. The size of
this input port must be equal to the size of the
**CellSOC** input port.
### Output

### **CellAH** — Estimated cell capacity scalar | vector

Estimated cell capacity of the battery, in ampere-hour, returned as a scalar or a
vector. The size of this output port is equal to the size of the
**InitialCellAH** input port.

## Parameters

### **Specify Current input as cell current(s)** — Option to specify current input port as vector `off` (default) | `on`

Option to specify the value of the **Current** input port as a vector
of cell currents. If you select this parameter, the value at the
**Current** input port can be a scalar or a vector of size equal to
the size of the block inputs.

### **Filter type** — Kalman filter type `Extended Kalman filter` (default) | `Extended Kalman-Bucy filter` | `Unscented Kalman filter` | `Unscented Kalman-Bucy filter`

Type of Kalman filter that this block uses to estimate the battery cell
capacity.

### **Alpha** — Alpha coefficient `1` (default) | scalar in the range [0, 1]

Coefficient that controls the spread of the sigma points. The block uses this parameter
in its implementation of the equations for the unscented Kalman filter and
the unscented Kalman-Bucy filter.

#### Dependencies

To enable this parameter, set **Filter type** to
`Unscented Kalman filter` or
`Unscented Kalman-Bucy filter`.

### **Beta** — Beta coefficient `2` (default) | nonnegative scalar

Coefficient related to the distribution. The block uses this parameter in its
implementation of the unscented Kalman filter and the unscented Kalman-Bucy
filter.

#### Dependencies

To enable this parameter, set **Filter type** to
`Unscented Kalman filter` or
`Unscented Kalman-Bucy filter`.

### **Kappa** — Kappa coefficient `0` (default) | scalar in the range [0, 3]

Coefficient that controls the spread of the sigma points. The block uses this parameter
in its implementation of the equations for the unscented Kalman filter and
the unscented Kalman-Bucy filter.

#### Dependencies

To enable this parameter, set **Filter type** to
`Unscented Kalman filter` or
`Unscented Kalman-Bucy filter`.

### **Covariance of the process noise, Q** — Covariance of process noise `3e-4` (default) | scalar

Covariance of the noise in the state.

### **Covariance of the measurement noise, R** — Covariance of measurement noise `5e-7` (default) | scalar

Covariance of the noise in the measurements.

### **Initial state error covariance, P0** — Initial state error covariance `1e-8` (default) | scalar | matrix

Covariance of the initial state error. This parameter defines the
deviation in the initialization of the state.

### **Sample time (-1 for inherited)** — Block sample time `1` (default) | 0 | -1 | integer

Time between consecutive block executions.
During execution, the block produces outputs and, if appropriate, updates
its internal state. For more information, see What Is Sample Time? and
Specify Sample Time.

For inherited discrete-time operation, specify this parameter as
`-1`. For discrete-time operation, specify this
parameter as a positive integer. For continuous-time operation, specify this
parameter as `0`.

If this block is in a masked subsystem or a variant subsystem that
supports switching between continuous operation and discrete operation,
promote the sample time parameter. Promoting the sample time parameter
ensures correct switching between the continuous and discrete
implementations of the block. For more information, see Promote Block Parameters on a Mask.

#### Dependencies

To enable this parameter, set **Filter type** to
`Extended Kalman filter` or
`Unscented Kalman filter`.

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

**Introduced in R2023b**

### R2025a: Switch between single-precision and double-precision floating-point simulation using **Algorithm data type** parameter

You can now easily switch between single-precision and double-precision floating-point simulation of the block algorithm by using the **Algorithm data type** parameter.

## Description

Battery capacity estimator with Kalman filter

The Battery Capacity Estimator (Kalman Filter) block implements an
estimator that calculates the cell capacity of a battery by using the Kalman filter
algorithms.

Use this block in conjunction with another block that estimates the state of charge (SOC) of
the battery, such as SOC Estimator
(Kalman Filter) or SOC Estimator
(Adaptive Kalman Filter).

This block supports single-precision and double-precision
floating-point simulation.

**Note**

To enable inherited single-precision floating-point simulation, the data type of all
inputs and parameters, except for the **Sample time (-1 for
inherited)** parameter, must be `single`.

For continuous-time simulation, set the **Filter type** parameter to
`Extended Kalman-Bucy filter` or `Unscented
Kalman-Bucy filter`.

**Note**

Continuous-time implementation of this block works only in a double-precision
floating-point simulation. If you provide single-precision floating-point parameters and
inputs, this block casts them to double-precision floating-point values to prevent
errors.

For discrete-time simulation, set the **Filter type** parameter to
`Extended Kalman filter` or `Unscented Kalman
filter` and the **Sample time (-1 for inherited)**
parameter to a positive value or `-1`.

### Equations

To estimate the battery capacity, the Battery Capacity Estimator (Kalman
Filter) block starts from the equations of the derivative of the
capacity and the SOC:

dQdt=00=dSOCdt+i3600Q

where

- *SOC* is the state of charge.
- *i* is the current of the battery cell.
- *Q* is the capacity in Ampere-hour.

The first equation is the state equation. The second equation is the
output equation.

For the Kalman filter algorithms, the Battery Capacity Estimator (Kalman
Filter) block uses *Q* as the state and these process
and observation functions:

f(Q)=0h(Q,SOC)=dSOCdt+i3600Q

**Extended Kalman Filter**

This diagram shows the structure of the extended Kalman filter (EKF):

The EKF technique relies on a linearization at every time step to approximate the
nonlinear system. To linearize the system at every time step, the algorithm
computes these Jacobians online:

F=∂f∂Q=0H=∂h∂Q=−i3600Q2

The EKF is a discrete-time algorithm. After the discretization, the Jacobians for the SOC
estimation of the battery are:

Fd=1Hd=−iTs3600Q2

where *T*S is the
sample time.

For more information about the implementation of the EKF algorithm steps, see the Extended
Kalman Filter section of the SOC
Estimator (Kalman Filter) block.

**Extended Kalman-Bucy Filter**

This diagram shows the structure of the extended Kalman-Bucy filter (EKBF):

The EKBF is the continuous-time variant of the Kalman filter. In continuous time, the
prediction and correction steps are coupled.

For more information about the implementation of the EKF algorithm steps, see the Extended
Kalman-Bucy Filter section of the SOC Estimator (Kalman Filter)
block.

**Unscented Kalman Filter**

This diagram shows the structure of the unscented Kalman filter (UKF):

The EKF locally approximates nonlinear functions with the linear equations
obtained from the Taylor expansion by using only the first term of the
expansion. In a highly nonlinear system, these solutions are not very accurate.

The UKF uses nonlinear transformations on a set of sigma points that the
algorithm chooses deterministically. This technique is called
*unscented transformation*. The mean and the covariance
matrix of the transformed points are accurate to the second order of the Taylor
series expansion.

For more information about the implementation of the EKF algorithm steps, see the Unscented
Kalman Filter section of the SOC Estimator (Kalman Filter)
block.

**Unscented Kalman-Bucy Filter**

This diagram illustrates the structure of the unscented Kalman-Bucy filter (UKBF):

The derived continuous-time filtering equations of the UKBF are similar to the
EKBF equations.

For more information about the implementation of the EKF algorithm steps, see the Unscented
Kalman-Bucy Filter section of the SOC Estimator (Kalman Filter)
block.
