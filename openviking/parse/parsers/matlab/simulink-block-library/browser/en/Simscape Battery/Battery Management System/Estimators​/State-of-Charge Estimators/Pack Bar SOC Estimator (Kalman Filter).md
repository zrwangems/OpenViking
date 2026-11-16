---
type: simulink-block
title: 'Pack Bar SOC Estimator (Kalman Filter)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Management System / Estimators\u200b / State-of-Charge Estimators'
documentation_page: 'packbarsocestimatorkalmanfilter'
documentation_source_path: 'ref/packbarsocestimatorkalmanfilter.html'
language: en
---

# Pack Bar SOC Estimator (Kalman Filter)

## Ports

### Input

### **AverageCurrent** — Average current of battery pack, ampere scalar

Average current of the battery pack, in ampere, specified as a scalar.

### **AverageVoltage** — Average voltage of battery pack, volt scalar

Average voltage of the battery pack, in volt, specified as a scalar.

### **AverageTemperature** — Average temperature of battery pack, K scalar

Average temperature of the battery pack, specified as a scalar.

### **AverageAH** — Average charge of battery pack, A\*Hr scalar

Average charge of the battery pack, in ampere-hour, specified as a scalar.

### **InitialSOC** — Initial state of charge, unitless scalar in the range [0,1]

Initial state of charge, specified as a scalar in the range [0,1].
### Output

### **SOC** — Average state of charge of battery pack scalar

Average state of charge of the battery pack, returned as a scalar.

### **Vdyn** — Average dynamic overpotential voltage of battery pack scalar

Average dynamic overpotential voltage of the battery pack, returned as a
scalar.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Filter type** — Kalman filter type `Extended Kalman filter` (default) | `Extended Kalman-Bucy filter` | `Unscented Kalman filter` | `Unscented Kalman-Bucy filter`

Type of Kalman filter that this block uses to estimate the average state of charge
of the battery pack.

### **Alpha** — Alpha coefficient `1` (default) | scalar in the range (0, 1]

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

### **Covariance of the process noise, Q** — Covariance of process noise `[1e-6 0; 0 1e-6]` (default) | `[1e-6 0 0;0 1e-6 0;0 0 1e-6]` | matrix of scalars

Covariance matrix of the noise in the states.

Specify a `2`-by-`2` matrix if you set the
**Charge dynamics** parameter to `One time-constant
dynamics` or a `3`-by-`3` matrix if
you set the **Charge dynamics** parameter to `Two
time-constant dynamics`.

### **Covariance of the measurement noise, R** — Covariance of measurement noise `0.1` (default) | scalar

Covariance of the noise in the measurements.

### **Initial state error covariance, P0** — Initial state error covariance `[1e-5 0; 0 1]` (default) | `[1e-5 0 0; 0 1 0;0 0 1]` | matrix of scalars

Covariance matrix of the initial state error. This parameter defines the deviation
in the initialization of the state.

Specify a `2`-by-`2` matrix if you set the
**Charge dynamics** parameter to `One time-constant
dynamics` or a `3`-by-`3` matrix if
you set the **Charge dynamics** parameter to `Two
time-constant dynamics`.

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

### **Charge dynamics** — Option to model battery charge dynamics `One time-constant dynamics` (default) | `Two time-constant dynamics`

Option to model the battery charge dynamics. This parameter determines the number
of parallel RC sections in the equivalent circuit:

- `One time-constant dynamics` — The equivalent circuit
  contains one parallel RC section. Specify the polarization resistance and the time
  constant using the **First polarization resistance, R1(SOC,T),
  (ohm)** and **First time constant, tau1(SOC,T), (s)**
  parameters.
- `Two time-constant dynamics` — The equivalent circuit
  contains two parallel RC sections. Specify the polarization resistances and the
  time constants using the **First polarization resistance, R1(SOC,T),
  (ohm)**; **First time constant, tau1(SOC,T), (s)**;
  **Second polarization resistance, R2(SOC,T), (ohm)**; and
  **Second time constant, tau2(SOC,T), (s)** parameters.

### **Vector of state-of-charge values, SOC (-)** — SOC breakpoints `[0, .1, .25, .5, .75, .9, 1]` (default) | vector of scalars in the range [0, 1]

Vector of the state of charge breakpoints defining the points at which you specify
lookup data. The entries of this vector must be in strictly ascending order.

### **Vector of temperatures, T** — Temperature breakpoints `[278, 293, 313]` (default) | vector of positive scalars

Vector of temperature breakpoints defining the points at which you specify lookup
data. This vector must be in strictly ascending order and greater than 0 K. The
physical unit of this parameter must be the same as the physical unit of the
**AverageTemperature** input port.

### **Terminal resistance, R0(SOC,T), (ohm)** — R0 lookup table with temperature breakpoint `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]` (default) | matrix of positive entries

Lookup data for series resistance of the battery at the specified SOC and
temperature breakpoints.

### **First polarization resistance, R1(SOC,T), (ohm)** — First RC resistance at temperature breakpoints `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` (default) | matrix of positive entries

Lookup data, in ohm, for the first parallel RC resistance at the specified SOC and
temperature breakpoints. The number of rows of this matrix is equal to the size of the
**Vector of state-of-charge values, SOC (-)** parameter. The number
of columns of this matrix is equal to the size of the **Vector of
temperatures, T** parameter.

### **First time constant, tau1(SOC,T), (s)** — First RC time constant at temperature breakpoints `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` (default) | matrix of positive entries

Lookup data, in second, for the first parallel RC time constant at the specified
SOC and temperature breakpoints. The number of rows of this matrix is equal to the
size of the **Vector of state-of-charge values, SOC (-)** parameter.
The number of columns of this matrix is equal to the size of the **Vector of
temperatures, T** parameter.

### **Second polarization resistance, R2(SOC,T), (ohm)** — Second RC resistance at temperature breakpoints `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` (default) | matrix of positive entries

Lookup data, in ohm, for the second parallel RC resistance at the specified SOC
and temperature breakpoints. The number of rows of this matrix is equal to the size of
the **Vector of state-of-charge values, SOC (-)** parameter. The
number of columns of this matrix is equal to the size of the **Vector of
temperatures, T** parameter.

#### Dependencies

To enable this parameter, set **Charge dynamics** to
`Two time-constant dynamics`.

### **Second time constant, tau2(SOC,T), (s)** — Second RC time constant at temperature breakpoints `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` (default) | matrix of positive entries

Lookup data, in seconds, for the second parallel RC time constant at the specified
SOC and temperature breakpoints. The number of rows of this matrix is equal to the
size of the **Vector of state-of-charge values, SOC (-)** parameter.
The number of columns of this matrix is equal to the size of the **Vector of
temperatures, T** parameter.

#### Dependencies

To enable this parameter, set **Charge dynamics** to
`Two time-constant dynamics`.

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

Average state-of-charge estimator for battery pack with Kalman filter

The Pack Bar SOC Estimator (Kalman Filter) block implements an estimator
that calculates the average state of charge (SOC) of a battery pack by using the Kalman filter
algorithms. The average state of charge and polarization voltage are the internal estimator
states, the current is the control input, and the average pack voltage is the
measurement.

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

The bar filter technique estimates the average states of the battery pack. The equations
for the average mathematical model for a battery pack with two time-constant dynamics are:

dSOC¯dt=−i3600⋅AH¯dV1¯dt=iC1(SOC¯,T¯)−V1¯R1(SOC¯,T¯)⋅C1(SOC¯,T¯)dV2¯dt=iC2(SOC¯,T¯)−V2¯R2(SOC¯,T¯)⋅C2(SOC¯,T¯)V¯t=V0(SOC¯,T¯)−iR0¯−V1¯−V2¯

where:

- SOC¯=1Ns∑i=1NsSOCi is the average state of charge of the battery pack.
- *i* is the current.
- *V*0 is the no-load voltage.
- Vt¯ is the average terminal voltage of the battery pack.
- AH¯ is the average ampere-hour rating of the battery pack.
- R0¯ is the terminal resistance of the battery pack.
- *R*1 is the first polarization
  resistance.
- *C*1 is the first parallel RC
  capacitance.
- *R*2 is the second polarization
  resistance.
- *C*2 is the second parallel RC
  capacitance.
- T¯ is the average temperature of the battery pack.
- V1¯ is the polarization voltage over the first RC network.
- V2¯ is the polarization voltage over the second RC network.

A time constant *τ*1 for the first parallel
section relates the first polarization resistance
*R*1 and the first parallel RC capacitance
*C*1 using the relationship C1=τ1/R1.

A time constant *τ*2 for the second parallel
section relates the second polarization resistance
*R*2 and the second parallel RC capacitance
*C*2 using the relationship C2=τ2/R2.

For series-connected cells, the cell currents are equal. When balancing the battery, the
cell currents might not be equal and the currents must be averaged.

The outputs from the bar filter are the estimated average state of charge of the battery
pack, SOC¯, and the average dynamic overpotential voltage, Vdyn¯=V1¯+V2¯.

To learn more about the internal implementation and equations of each Kalman filter
algorithm of this block, see the Equations section of the
SOC Estimator (Kalman Filter) block.
