---
type: simulink-block
title: 'SOC Estimator (Kalman Filter)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'BMS / Estimators'
documentation_page: 'socestimatorkalmanfilter'
documentation_source_path: 'ref/socestimatorkalmanfilter.html'
language: en
---

# SOC Estimator (Kalman Filter)

## Ports
```yaml
ports:
- name: Current
  summary: Battery current scalar | vector
  direction: input
- name: CellVoltage
  summary: Cell voltage scalar | vector
  direction: input
- name: CellTemperature
  summary: Cell temperature scalar | vector
  direction: input
- name: InitialSOC
  summary: Initial state of charge scalar | vector
  direction: input
- name: SOC
  summary: State of charge scalar | vector
  direction: output
```

### Input

### **Current** — Battery current scalar | vector

Battery current, in ampere, specified as a scalar for a single cell or
a vector for multiple cells. To specify this input as a vector of cell
currents, select the **Specify Current input as cell
current(s)** parameter.

### **CellVoltage** — Cell voltage scalar | vector

Cell voltage, in volt, specified as a scalar for a single cell or a
vector for multiple cells. The size of this input port must be equal to
the size of the **CellTemperature** and
**InitialSOC** input ports.

### **CellTemperature** — Cell temperature scalar | vector

Cell temperature, specified as a scalar for a single cell or a vector
for multiple cells. The size of this input port must be equal to the
size of the **CellVoltage** and
**InitialSOC** input ports.

### **InitialSOC** — Initial state of charge scalar | vector

Initial state of charge, specified as a scalar or vector of entries in
the range [0, 1]. The size of this input port must be equal to the size
of the **CellVoltage** and
**CellTemperature** input ports.
### Output

### **SOC** — State of charge scalar | vector

State of charge of the battery, returned as a scalar or a vector. The
size of this output port is equal to the size of the
**CellVoltage**,
**CellTemperature**, and
**InitialSOC** input ports.
## Parameters
```yaml
parameters:
- name: Specify Current input as cell current(s)
  summary: Option to specify current input port as vector on (default) | off
  group: Main
- name: Filter type
  summary: Kalman filter type Extended Kalman filter (default) | Extended Kalman-Bucy filter | Unscented Kalman filter | Unscented
    Kalman-Bucy filter
  group: Main
- name: Alpha
  summary: Alpha coefficient 1 (default) | scalar in the range [0, 1]
  group: Main
- name: Beta
  summary: Beta coefficient 2 (default) | nonnegative scalar
  group: Main
- name: Kappa
  summary: Kappa coefficient 0 (default) | scalar in the range [0, 3]
  group: Main
- name: Covariance of the process noise, Q
  summary: Covariance of the process noise [1e-6 0; 0 1e-6] (default) | matrix of scalars
  group: Main
- name: Covariance of the measurement noise, R
  summary: Covariance of the measurement noise 0.1 (default) | scalar
  group: Main
- name: Initial state error covariance, P0
  summary: Initial state error covariance [1e-5 0; 0 1] (default) | matrix of scalars
  group: Main
- name: Sample time (-1 for inherited)
  summary: Block sample time 1 (default) | 0 | -1 | integer
  group: Main
- name: Charge dynamics
  summary: Option to model battery charge dynamics One time-constant dynamics (default) | Two time-constant dynamics
  group: System Model
- name: Vector of state-of-charge values, SOC (-)
  summary: SOC breakpoints [0, .1, .25, .5, .75, .9, 1] (default) | vector of scalars in the range [0, 1]
  group: System Model
- name: Vector of temperatures, T
  summary: Temperature breakpoints [278, 293, 313] (default) | vector of positive scalars
  group: System Model
- name: Terminal resistance, R0(SOC,T), (ohm)
  summary: R0 lookup table with temperature breakpoint [.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107,
    .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089] (default) | matrix of positive entries
  group: System Model
- name: First polarization resistance, R1(SOC,T), (ohm)
  summary: First RC resistance at temperature breakpoints [.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013;
    .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011] (default) | matrix of positive entries
  group: System Model
- name: First time constant, tau1(SOC,T), (s)
  summary: First RC time constant at temperature breakpoints [20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67;
    40, 33, 29; 25, 39, 33] (default) | matrix of positive entries
  group: System Model
- name: Second polarization resistance, R2(SOC,T), (ohm)
  summary: Second RC resistance at temperature breakpoints [.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013;
    .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011] (default) | matrix of positive entries
  group: System Model
- name: Second time constant, tau2(SOC,T), (s)
  summary: Second RC time constant at temperature breakpoints [20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67;
    40, 33, 29; 25, 39, 33] (default) | matrix of positive entries
  group: System Model
- name: No-load voltage, V0(SOC,T), (V)
  summary: '*V*0 lookup table [3.49, 3.5, 3.51; 3.55, 3.57, 3.56; 3.62, 3.63, 3.64; 3.71, 3.71, 3.72; 3.91, 3.93, 3.94; 4.07,
    4.08, 4.08; 4.19, 4.19, 4.19] (default) | matrix of nonnegative entries'
  group: System Model
- name: Cell capacity, AH (A\*Hr)
  summary: Battery capacity when fully charged 27 (default) | nonnegative scalar
  group: System Model
- name: Algorithm data type
  summary: 'Option to choose data type for block algorithm Inherit: auto (default) | double | single | <data type expression>'
  group: Signal Attributes
```

### Main

### **Specify Current input as cell current(s)** — Option to specify current input port as vector `on` (default) | `off`

*Since R2023b*

Option to specify the value of the **Current** input port as a vector
of cell currents. If you select this parameter, the value at the
**Current** input port can be a scalar or a vector of size equal to
the size of the block inputs.

### **Filter type** — Kalman filter type `Extended Kalman filter` (default) | `Extended Kalman-Bucy filter` | `Unscented Kalman filter` | `Unscented Kalman-Bucy filter`

Type of Kalman filter that this block uses to estimate the battery state of
charge.

### **Alpha** — Alpha coefficient `1` (default) | scalar in the range [0, 1]

Coefficient that controls the spread of the sigma points. The block uses this parameter
in its implementation of the equations for the unscented Kalman filter
and the unscented Kalman-Bucy filter.

#### Dependencies

To enable this parameter, set **Filter type** to
`Unscented Kalman filter` or
`Unscented Kalman-Bucy filter`.

### **Beta** — Beta coefficient `2` (default) | nonnegative scalar

Coefficient related to the distribution. The block uses this parameter in its
implementation of the unscented Kalman filter and the unscented
Kalman-Bucy filter.

#### Dependencies

To enable this parameter, set **Filter type** to
`Unscented Kalman filter` or
`Unscented Kalman-Bucy filter`.

### **Kappa** — Kappa coefficient `0` (default) | scalar in the range [0, 3]

Coefficient that controls the spread of the sigma points. The block uses this parameter
in its implementation of the equations for the unscented Kalman filter
and the unscented Kalman-Bucy filter.

#### Dependencies

To enable this parameter, set **Filter type** to
`Unscented Kalman filter` or
`Unscented Kalman-Bucy filter`.

### **Covariance of the process noise, Q** — Covariance of the process noise `[1e-6 0; 0 1e-6]` (default) | matrix of scalars

`2`-by-`2` covariance matrix of the noise in the
states.

### **Covariance of the measurement noise, R** — Covariance of the measurement noise `0.1` (default) | scalar

Covariance of the noise in the measurements.

### **Initial state error covariance, P0** — Initial state error covariance `[1e-5 0; 0 1]` (default) | matrix of scalars

`2`-by-`2` covariance matrix of the
initial state error. This parameter defines the deviation in the
initialization of the state.

### **Sample time (-1 for inherited)** — Block sample time `1` (default) | 0 | -1 | integer

Time between consecutive block executions.
During execution, the block produces outputs and, if appropriate,
updates its internal state. For more information, see What Is Sample Time? and
Specify Sample Time.

For inherited discrete-time operation, specify this parameter as
`-1`. For discrete-time operation, specify this
parameter as a positive integer. For continuous-time operation, specify
this parameter as `0`.

If this block is in a masked subsystem or a variant subsystem that
supports switching between continuous operation and discrete operation,
promote the sample time parameter. Promoting the sample time parameter
ensures correct switching between the continuous and discrete
implementations of the block. For more information, see Promote Block Parameters on a Mask.

#### Dependencies

To enable this parameter, set **Filter type** to
`Extended Kalman filter` or
`Unscented Kalman filter`.

### System Model

### **Charge dynamics** — Option to model battery charge dynamics `One time-constant dynamics` (default) | `Two time-constant dynamics`

*Since R2024a*

Option to model the battery charge dynamics. This parameter determines the number of
parallel RC sections in the equivalent circuit:

- `One time-constant dynamics` — The equivalent circuit
  contains one parallel RC section. Specify the polarization resistance and the
  time constant using the **First polarization resistance, R1(SOC,T),
  (ohm)** and **First time constant, tau1(SOC,T),
  (s)** parameters.
- `Two time-constant dynamics` — The equivalent circuit
  contains two parallel RC sections. Specify the polarization resistances and the
  time constants using the **First polarization resistance, R1(SOC,T),
  (ohm)**, **First time constant, tau1(SOC,T),
  (s)**, **Second polarization resistance, R2(SOC,T),
  (ohm)**, and **Second time constant, tau2(SOC,T),
  (s)** parameters.

### **Vector of state-of-charge values, SOC (-)** — SOC breakpoints `[0, .1, .25, .5, .75, .9, 1]` (default) | vector of scalars in the range [0, 1]

Vector of the state of charge breakpoints defining the points at which
you specify lookup data. The entries of this vector must be in strictly
ascending order. The block calculates the state of charge value with
respect to the nominal battery capacity specified in the **Cell
capacity, AH (A\*Hr)** parameter. The SOC is the ratio of
the available battery charge
*q*battery and the nominal
battery capacity
*q*nom*(T,n)*.
You must make sure that, for each temperature value, an SOC of 1
represents the battery charge capacity for the corresponding element of
the **Cell capacity, AH (A\*Hr)** parameter when you
model a fresh battery with a number of cycles *N* equal
to 1 and *δAH(n = 1,
Tfade)* equal to 0:.

SOC=qbatteryqnom(T,n)  for N=1 and δAH(n,Tfade)=0,  qnom(T,n)=AH.

### **Vector of temperatures, T** — Temperature breakpoints `[278, 293, 313]` (default) | vector of positive scalars

Vector of temperature breakpoints defining the points at which you
specify lookup data. This vector must be strictly ascending and greater
than 0 K. The physical unit of this parameter must be the same as the
physical unit of the **CellTemperature** input
port.

### **Terminal resistance, R0(SOC,T), (ohm)** — R0 lookup table with temperature breakpoint `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]` (default) | matrix of positive entries

Lookup data for series resistance of the battery at the specified SOC
and temperature breakpoints.

### **First polarization resistance, R1(SOC,T), (ohm)** — First RC resistance at temperature breakpoints `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` (default) | matrix of positive entries

Lookup data, in ohm, for the first parallel RC resistance at the specified SOC and
temperature breakpoints. The number of rows of this matrix is equal to
the size of the **Vector of state-of-charge values, SOC
(-)** parameter. The number of columns of this matrix is
equal to the size of the **Vector of temperatures, T**
parameter.

### **First time constant, tau1(SOC,T), (s)** — First RC time constant at temperature breakpoints `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` (default) | matrix of positive entries

Lookup data, in second, for the first parallel RC time constant at the
specified SOC and temperature breakpoints. The number of rows of this
matrix is equal to the size of the **Vector of state-of-charge
values, SOC (-)** parameter. The number of columns of this
matrix is equal to the size of the **Vector of temperatures,
T** parameter.

### **Second polarization resistance, R2(SOC,T), (ohm)** — Second RC resistance at temperature breakpoints `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` (default) | matrix of positive entries

*Since R2024a*

Lookup data, in ohm, for the second parallel RC resistance at the specified SOC and
temperature breakpoints. The number of rows of this
matrix is equal to the size of the **Vector of state-of-charge values, SOC
(-)** parameter. The number of columns of this matrix is equal to the size
of the **Vector of temperatures, T** parameter.

#### Dependencies

To enable this parameter, set **Charge dynamics** to
`Two time-constant dynamics`.

### **Second time constant, tau2(SOC,T), (s)** — Second RC time constant at temperature breakpoints `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` (default) | matrix of positive entries

*Since R2024a*

Lookup data, in second, for the second parallel RC time constant at the specified SOC
and temperature breakpoints. The number of rows of this matrix is equal to the size of
the **Vector of state-of-charge values, SOC (-)** parameter. The number
of columns of this matrix is equal to the size of the **Vector of temperatures,
T** parameter.

#### Dependencies

To enable this parameter, set **Charge dynamics** to
`Two time-constant dynamics`.

### **No-load voltage, V0(SOC,T), (V)** — *V*0 lookup table `[3.49, 3.5, 3.51; 3.55, 3.57, 3.56; 3.62, 3.63, 3.64; 3.71, 3.71, 3.72; 3.91, 3.93, 3.94; 4.07, 4.08, 4.08; 4.19, 4.19, 4.19]` (default) | matrix of nonnegative entries

Lookup data, in volt, for open-circuit voltages across the fundamental
battery model at the specified SOC. The number of rows of this matrix is
equal to the size of the **Vector of state-of-charge values, SOC
(-)** parameter. The number of columns of this matrix is
equal to the size of the **Vector of temperatures, T**
parameter.

### **Cell capacity, AH (A\*Hr)** — Battery capacity when fully charged `27` (default) | nonnegative scalar

Cell capacity of the battery, in ampere-hour. The block calculates the state of charge
by dividing the accumulated charge by this value. The block calculates
the accumulated charge by integrating the battery current.

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

**Introduced in R2022b**

### R2025a: Switch between single-precision and double-precision floating-point simulation using **Algorithm data type** parameter

You can now easily switch between single-precision and double-precision floating-point simulation of the block algorithm by using the **Algorithm data type** parameter.

### R2024a: Estimate SOC using equivalent models with two time-constant charge dynamics

You can now estimate the battery SOC by using equivalent models with two time-constant charge dynamics.

To select an equivalent model with two time-constant charge dynamics, set the **Charge dynamics** parameter to `Two time-constant dynamics` and specify the values of the new **Second polarization resistance, R2(SOC,T), (ohm)** and **Second time constant, tau2(SOC,T), (s)** parameters.

### R2023b: Specify the value of the Current input as a vector of cell currents

You can now specify the value of the **Current** input port as a
vector of cell currents.

To enable a vectorized input, select the **Specify Current input as cell
current(s)** parameter. If you select this parameter, the
**Current** input port must have the same size as the other
inputs and represents individual cell currents.

## Description

State of charge estimator with Kalman filter

The SOC Estimator (Kalman Filter) block implements an estimator that
calculates the state of charge (SOC) of a battery by using the Kalman filter algorithms.

The SOC is the ratio of the released capacity
*C*releasable to the rated capacity
*C*rated. Manufacturers provide the value of
the rated capacity of each battery, which represents the maximum amount of charge in the
battery:

SOC=CreleasableCrated.

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

These figures show the equivalent circuit for a battery with one-time-constant dynamics and
two time-constant dynamics, respectively:

The equations for the equivalent circuit with two time-constant dynamics are:

dSOCdt=−i3600AHdV1dt=iC1(SOC,T)−V1R1(SOC,T)C1(SOC,T)dV2dt=iC2(SOC,T)−V2R2(SOC,T)C2(SOC,T)Vt=V0(SOC,T)−iR0−V1−V2

where

- *SOC* is the state of charge.
- *i* is the current.
- *V*0 is the no-load
  voltage.
- *V*t is the terminal
  voltage.
- *AH* is the ampere-hour rating.
- *R*1 is the first polarization
  resistance.
- *C*1 is the first parallel RC
  capacitance.
- *R*2 is the second
  polarization resistance.
- *C*2 is the second parallel RC
  capacitance.
- *T* is the temperature.
- *V*1 is the polarization
  voltage over the first RC network.
- *V*2 is the polarization
  voltage over the second RC network.

A time constant *τ*1 for the
first parallel section relates the first polarization resistance
*R*1 and the first parallel RC
capacitance *C*1 using the relationship C1=τ1/R1.

A time constant *τ*2 for the second
parallel section relates the second polarization resistance
*R*2 and the second parallel RC
capacitance *C*2 using the relationship C2=τ2/R2.

For the Kalman filter algorithms, the block uses this state and these process and
observation functions:

x=[SOCV1]Tf(x,i)=[−i3600AHiC1(SOC,T)−V1R1(SOC,T)C1(SOC,T)]h(x,i)=V0(SOC,T)−iR0−V1

If you set the **Charge dynamics** parameter to `Two
time-constant dynamics`, for the Kalman filter algorithms, the
block uses this state and these process and observation functions:

x=[SOCV1V2]Tf(x,i)=[−i3600AHiC1(SOC,T)−V1R1(SOC,T)C1(SOC,T)iC2(SOC,T)−V2R2(SOC,T)C2(SOC,T)]h(x,i)=V0(SOC,T)−iR0−V1−V2

**Extended Kalman Filter**

This diagram shows the structure of the extended Kalman filter (EKF):

The EKF technique relies on a linearization at every time step to approximate the
nonlinear system. To linearize the system at every time step, the algorithm
computes these Jacobians online:

F=∂f∂xH=∂h∂x

The EKF is a discrete-time algorithm. After the discretization, the Jacobians for the SOC
estimation of the battery are:

Fd=[100e−TSR1C1]Hd=[∂VOC∂SOC−1]

where *T*S is the
sample time and *V*OC is the
open-circuit voltage.

The EKF algorithm comprises these phases:

- **Initialization**

  - x^(0|0)⁠— State estimate at time step 0 using
    measurements at time step 0.
  - P^(0|0)⁠— State estimation error covariance
    matrix at time step 0 using measurements at time step
    0.
- **Prediction**

  - Project the states ahead (*a
    priori*):

    x^(k+1|k)=f(x^(k|k),i).
  - Project the error covariance ahead:

    P^(k+1|k)=Fd(k)P^(k|k)FdT(k)+Q,

    where **Q** is the
    covariance of the process noise.
- **Correction**

  - Compute the Kalman gain:

    K(k+1)=P^(k+1|k)HdT(k)(Hd(k)P^(k+1|k)HdT(k)+R)−1,

    where *R* is the
    covariance of the measurement noise.
  - Update the estimate with the measurement
    *y(k)* (*a
    posteriori*):

    x^(k+1|k+1)=x^(k+1|k)+K(k+1)(Vt(k)−h(x^(k|k),i)).
  - Update the error covariance:

    P^(k+1|k+1)=(I−K(k+1)Hd)P^(k+1|k).

**Extended Kalman-Bucy Filter**

This diagram shows the structure of the extended Kalman-Bucy filter (EKBF):

The EKBF is the continuous-time variant of the Kalman filter. In continuous time, the
prediction and correction steps are coupled.

- **Initialization**

  - x^(t0)⁠— State estimate at time
    *t*0.
  - P^(t0)⁠— State estimation error covariance matrix
    at time *t*0.
- **Prediction-Correction EKBF algorithm**

  K(t)=P(t)HT(t)R−1(t)dx^(t)dt=f(x^(t),i(t))+K(t)(Vt(t)−h(x^(t),i(t)))dP(t)dt=F(t)P(t)+P(t)FT(t)+Q(t)−K(t)H(t)P(t)

  where:

  F(t)=∂f∂xH(t)=∂h∂x

**Unscented Kalman Filter**

This diagram shows the structure of the unscented Kalman filter (UKF):

The EKF locally approximates nonlinear functions with the linear equations obtained from
the Taylor expansion by using only the first term of the expansion. In a highly
nonlinear system, these solutions are not very accurate.

The UKF uses nonlinear transformations on a set of sigma points that the algorithm chooses
deterministically. This technique is called *unscented
transformation*. The mean and the covariance matrix of the
transformed points are accurate to the second order of the Taylor series
expansion.

The UKF algorithm follows these steps:

- **Initialization**

  - x^(0|0)⁠— State estimate at time step 0 using
    measurements at time step 0.
  - P^(0|0)⁠— State estimation error covariance
    matrix at time step 0 using measurements at time step
    0.
- Generate sigma points and calculate the mean weight and covariance
  weight for each point.

  - Choose the sigma points *x(i)(k|k)*

    x(i)(k|k)={x^(k+1|k)i=1x^(k+1|k)+((n+λ)P(k|k))ii=2,…,n+1x^(k+1|k)−((n+λ)P(k|k))ii=n+2,…,2n+1Wm(i)={λn+λi=112(n+λ)i≠1Wc(i)={λn+λ+(1−α2+β)i=112(n+λ)i≠1

    where:

    - *n* is the dimension of the
      state vector, *x*.
    - λ=α2(n+κ)−n, α∈[0,1] describes the distance between
      the sigma point and the mean point. In a normal
      distribution, *β =* 2 and
      *κ =* 0.
    - ((n+λ)P)i is the *i*th
      row or column of cP. The block calculates the matrix
      square root by using numerically efficient and
      stable methods such as the Cholesky
      decomposition.
- Perform first estimation of the system state matrix:

  x^(i)(k+1|k)=f(x^(i)(k|k),i(k))x^(k+1|k)=∑i=12n+1Wm(i)x^(i)(k+1|k)
- Perform first estimation of the covariance matrix of the state variables:

  P(k+1|k)=∑i=12n+1Wc(i)(x^(i)(k+1|k)−x^(k+1|k))⋅(x^(i)(k+1|k)−x^(k+1|k))T+Q
- Estimate the measured variables:

  Vt(i)(k+1|k)=h(x^(i)(k+1|k),i(k))V^t(k+1|k)=∑i=12n+1Wm(i)V^t(i)(k+1|k)
- Estimate the covariance of the measurement
  (*Py*) and covariance
  between the measurement and the state
  (*Pxy*):

  Py=∑i=12n+1Wc(i)(V^t(i)(k+1|k)−V^t(k+1|k))⋅(V^t(i)(k+1|k)−V^t(k+1|k))T+RPxy=∑i=12n+1(x^(i)(k+1|k)−x^(k+1|k))⋅(V^t(i)(k+1|k)−V^t(k+1|k))T
- Compute the Kalman filter gain:

  K(k+1)=PxyPy−1
- Perform the second update of the state matrix and of the covariance of the state variables:

  x^(k+1|k+1)=x^(k+1|k)+K(k+1)(Vt(k+1)−V^t(k+1|k))P(k+1|k+1)=P(k+1|k)−K(k+1)PyKT(k+1)

**Unscented Kalman-Bucy Filter**

This diagram illustrates the overall structure of the unscented Kalman-Bucy filter (UKBF):

The derived continuous-time filtering equations of the UKBF are similar to the EKBF
equations.

Because the UKF uses matrix square roots in its sigma points, the algorithm obtains the
square-root version of the UKBF by formulating the filter as a differential
equation for the sigma points. The equations for the square-root UKBF are:

K(t)=X(t)WhT(X(t),t)R−1(t)M(t)=A−1(t)[X(t)WfT(X(t),t)+f(X(t),t)WXT(t)+Q(t)−K(t)R(t)KT(t)]A−T(t)dXi(t)dt=f(X(t),t)wm+K(t)(Vt(t)−h(X(t),t)wm)+c[0A(t)Φ(M(t))−A(t)Φ(M(t))]i

where

- X(t)=[m(t)…m(t)]+c[0A(t)−A(t)] is the sigma-point matrix.
- Φij(M(t))={Mij(t),i>j0.5Mij(t),i=j0,i<j is a function that returns the lower diagonal part
  of the argument.
- wm=[Wm(1)⋯Wm(2n+1)]T
- W=(1−[wm⋯wm])diag(Wc(1)⋯Wc(2n+1))(I−[wm⋯wm])T
- c=α2(n+κ)
- [0A(t)Φ(M(t))−A(t)Φ(M(t))]i is the *i*th column of the
  argument matrix.
