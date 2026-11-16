---
type: simulink-block
title: 'FOC Default Controller Gains'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Controllers'
documentation_page: 'focdefaultcontrollergains'
documentation_source_path: 'ref/focdefaultcontrollergains.html'
language: en
---

# FOC Default Controller Gains

## Ports

### Input

The display of input ports depends on the selection – **Empirical
method** or **Based on Optimum theory** – in the block. For
information on input ports, refer to the below sections: Empirical method or Optimum Theory.

#### Empirical method

### **Rs** — Stator resistance scalar

Stator resistance of the motor (in ohms).

#### Dependencies

To enable this port, select one or both of these parameters in the
**Block Output** section of the
**Parameters** tab:

- **Current controller (d,q-axes)**
- **Field-weakening controller**

**Data Types:** `single` | `double`

### **Ld** — *d*-axis inductance scalar

The *d*-axis inductance of a permanent magnet synchronous
motor (PMSM) (in henries).

#### Dependencies

To enable this port:

- Set the **Motor selection** parameter to
  `PMSM`.
- Select the **Current controller (d,q-axes)**
  parameter available in the **Block Output** section
  of the **Parameters** tab.

**Data Types:** `single` | `double`

### **Lq** — *q*-axis inductance scalar

The *q*-axis inductance of a permanent magnet synchronous
motor (PMSM) (in henries).

#### Dependencies

To enable this port:

- Set the **Motor selection** parameter to
  `PMSM`.
- Select one or both of the these parameters in the **Block
  Output** section of the **Parameters**
  tab:

  - **Current controller (d,q-axes)**
  - **Field-weakening controller**

**Data Types:** `single` | `double`

### **Lm** — Magnetizing inductance scalar

The magnetizing inductance of an AC induction motor (ACIM) (in
henries).

#### Dependencies

To enable this port:

- Set the **Motor selection** parameter to
  `ACIM`.
- Select one or both of the these parameters in the **Block
  Output** section of the **Parameters**
  tab:

  - **Current controller (d,q-axes)**
  - **Field-weakening controller**

**Data Types:** `single` | `double`

### **Lls** — Stator leakage inductance scalar

The stator leakage inductance of an AC induction motor (ACIM) (in
henries).

#### Dependencies

To enable this port:

- Set the **Motor selection** parameter to
  `ACIM`.
- Select one or both of the these parameters in the **Block
  Output** section of the **Parameters**
  tab:

  - **Current controller (d,q-axes)**
  - **Field-weakening controller**

**Data Types:** `single` | `double`

### **Llr** — Rotor leakage inductance scalar

The rotor leakage inductance of an AC induction motor (ACIM) (in
henries).

#### Dependencies

To enable this port:

- Set the **Motor selection** parameter to
  `ACIM`.
- Select one or both of the these parameters in the **Block
  Output** section of the **Parameters**
  tab:

  - **Current controller (d,q-axes)**
  - **Field-weakening controller**

**Data Types:** `single` | `double`

### **J** — Motor inertia scalar

Inertia of the motor (in kg.m2).

#### Dependencies

To enable this port, select the **Speed controller**
parameter in the **Block Output** section of the
**Parameters** tab.

**Data Types:** `single` | `double`

### **Ts** — Current controller sample time scalar

Sample time (in seconds) of the current PI controller used in the FOC based
motor control algorithm.

**Data Types:** `single` | `double`

### **Tsc** — Speed controller sample time scalar

Sample time (in seconds) of the speed PI controller used in the FOC based
motor control algorithm.

#### Dependencies

To enable this port, select the **Speed controller**
parameter in the **Block Output** section of the
**Parameters** tab.

**Data Types:** `single` | `double`

### **SlowdownFactor** — Factor to slow down system response scalar in the range of [1, 20]

A factor, in the range of [1, 20], that you can provide to modify the output
PI gains. A higher value makes the controller parameters less aggressive and
slows down the system response.

#### Dependencies

To enable this port, clear the **Specify filter and sensor
delays** parameter available in the **Delays**
tab.

**Data Types:** `single` | `double`

### **IMax** — Maximum measurable peak-neutral current scalar

Maximum AC current magnitude (peak value) in an inverter-based motor drive
system (in amperes).

#### Dependencies

To enable this port, either:

- Select the **Speed controller** parameter in
  **Block output** section of
  **Parameters** tab.

or

- Select the **Current controller (d,q-axes)**
  parameter in **Block output** section of
  **Parameters** tab.
- Set the **Output unit** parameter to
  `Per-Unit`.

**Data Types:** `single` | `double`

### **Vdc** — DC link voltage scalar

DC link voltage of the inverter (in volts). The block uses Vdc3 as a base value for per-unit calculations when you set the
**Output unit** parameter to
`Per-Unit`.

#### Dependencies

To enable this port:

- Select the **Current controller (d,q-axes)**
  parameter in **Block output** section of
  **Parameters** tab.
- Set the **Output unit** parameter to
  `Per-Unit`.

**Data Types:** `single` | `double`

### **Nbase** — Motor rated speed scalar

Base value of the speed of the motor (in rpm) for per-unit
computation.

- Select the **Speed controller** parameter in
  **Block output** section of
  **Parameters** tab.
- Set the **Output unit** parameter to
  `Per-Unit`.

**Data Types:** `single` | `double`

#### Optimum Theory

### **Rs** — Stator resistance scalar

Stator resistance of the motor (in ohms).

**Data Types:** `single` | `double`

### **Ld** — *d*-axis inductance scalar

The *d*-axis inductance of a permanent magnet synchronous
motor (PMSM) (in henries).

**Data Types:** `single` | `double`

### **Lq** — *q*-axis inductance scalar

The *q*-axis inductance of a permanent magnet synchronous
motor (PMSM) (in henries).

**Data Types:** `single` | `double`

### **J** — Motor inertia scalar

Inertia of the motor (in kg.m2).

**Data Types:** `single` | `double`

### **p** — Number of pole pairs available in the motor scalar

Number of pole pairs available in the motor.

**Data Types:** `single` | `double`

### **FluxPM** — Peak permanent magnet flux linkage scalar

Peak permanent magnet flux linkage, in weber.

**Data Types:** `single` | `double`

### **Ts** — Current controller sample time scalar

Sample time (in seconds) of the current PI controller used in the FOC based
motor control algorithm.

**Data Types:** `single` | `double`

### **Tsc** — Speed controller sample time scalar

Sample time (in seconds) of the speed PI controller used in the FOC based
motor control algorithm.

**Data Types:** `single` | `double`

### **CurrLoopDelay** — Overall time constant value for the current delay present in feedback path scalar

Overall time constant value (in seconds) for the current delay present in
feedback path.

**Data Types:** `single` | `double`

### **SpeedLoopDelay** — Overall time constant value for the speed delay present in feedback path scalar

Overall time constant value (in seconds) for the speed delay present in
feedback path.

**Data Types:** `single` | `double`

### **Vbase** — Base voltage scalar

Base value of the voltage applied to the motor (in volts) for per-unit
computation.

#### Dependencies

To enable this port:

- Set the **Output unit** parameter to
  `Per-Unit`.

**Data Types:** `single` | `double`

### **Ibase** — Base current scalar

Base value of the current applied to the motor (in volts) for per-unit
computation.

#### Dependencies

To enable this port:

- Set the **Output unit** parameter to
  `Per-Unit`.

**Data Types:** `single` | `double`

### **Nbase** — Motor rated speed scalar

Base value of the speed of the motor (in rpm) for per-unit
computation.

#### Dependencies

To enable this port:

- Set the **Output unit** parameter to
  `Per-Unit`.

**Data Types:** `single` | `double`
### Output

### **PI Gains** — PI controller gains bus

Control gains of one or more of these PI controllers used in an FOC motor
control algorithm, for either Empirical method or Optimum theory.

If you select **Empirical method**, the value is also
based on based on the **Block output** parameter
selection:

- *d*- and *q*-axis current
  controller
- Speed controller
- Field-weakening controller

The following table summarizes the components of the **PI
Gains** output bus for **Empirical
method**:

| Type of PI Controller selected for Empirical Method | Bus component | | | Description |
| --- | --- | --- | --- | --- |
| *d*-axis current PI controller | *Daxis\_Kp* | | | Control gain *Kp* of the *d*-axis current PI controller |
| *Daxis\_Ki* | | | Control gain *Ki* of the *d*-axis current PI controller |
| *Daxis\_Ki\*Ts* | | | Control gain *Ki* of the *d*-axis current PI controller multiplied with the current controller sample time (*TS*) |
| *q*-axis current PI controller | *Qaxis\_Kp* | | | Control gain *Kp* of the *q*-axis current PI controller |
| *Qaxis\_Ki* | | | Control gain *Ki* of the *q*-axis current PI controller |
| *Qaxis\_Ki\*Ts* | | | Control gain *Ki* of the *q*-axis current PI controller multiplied with the current controller sample time (*TS*) |
| Speed PI controller | *Speed\_Kp* | | | Control gain *Kp* of the speed PI controller |
| *Speed\_Ki* | | | Control gain *Ki* of the speed PI controller |
| *Speed\_Ki\*Tsc* | | | Control gain *Ki* of the speed PI controller multiplied with the speed controller sample time (*TSC*) |
| Field-weakening PI controller | *FWC\_Kp* | | | Control gain *Kp* of the field-weakening PI controller |
| *FWC\_Ki* | | | Control gain *Ki* of the field-weakening PI controller |
| *FWC\_Ki\*Ts* | | | Control gain *Ki* of the field-weakening PI controller multiplied with the current controller sample time (*TS*) |

**Data Types:** `single` | `double`

### **Status** — PI gains computation status true | false

Computation status of the PI gains, returned as one of these values:

- True indicates that the block has successfully computed the PI
  controller gains available at the **PI Gains** output
  port.
- False indicates that the block could not compute the PI controller
  gains as the value of one or more inputs was incorrect.

**Data Types:** `Boolean`

## Parameters

### **Motor selection** — Type of motor `PMSM` (default) | `ACIM`

The type of motor for which you are implementing the control algorithm:

- ACIM — AC induction motor
- PMSM — Permanent magnet synchronous motor

#### Dependencies

This parameter is enabled for editing only if you select **Empirical
method** option to compute controller gain.

### **Output unit** — Unit of the block output `SI Unit` (default) | `Per-Unit`

Unit of the elements in the bus that the block outputs at the **PI
Gains** output port.

### **Block Output** — Output of the block `Current controller (d,q-axes)` | `Field-weakening controller` | `Speed controller`

Enable the block to compute and output one or more of the following elements
through the **PI Gains** port:

- `Current controller (d,q-axes)` — Control gains
  (*Kp* and
  *Ki*) of the PI controllers
  for *d*- and *q*-axis current
  control.
- `Field-weakening controller` — Control gains
  (*Kp* and
  *Ki*) of the PI controller
  operating in the field-weakening region.
- `Speed controller` — Control gains
  (*Kp* and
  *Ki*) of the speed PI
  controller.

#### Dependencies

This parameter is enabled for editing only if you select **Empirical
method** option to compute controller gain.

### Delays

### **Specify filter and sensor delays** — Enable addition of filter and sensor delays `off` (default) | `on`

Select this option to specify speed filter delay and current and speed
sensor delays. When you select this parameter, the block enables the
**Current sensor delay (s)**, **Speed sensor delay
(s)**, and **Speed filter delay (s)**
parameters.

#### Dependencies

This parameter selection appears only if you select **Empirical
method** option to compute controller gain.

### **Current sensor delay (s)** — Delay due to current sensor `50e-6` (default) | scalar

Time delay (in seconds) due to the current sensor.

#### Dependencies

To enable this parameter, select the **Specify filter and sensor
delays** parameter.

The **Specify filter and sensor delays** parameter
appears only if you select **Empirical method** option to
compute controller gain.

### **Speed sensor delay (s)** — Delay due to speed sensor `50e-6` (default) | scalar

Time delay (in seconds) due to the speed sensor.

#### Dependencies

To enable this parameter, select the **Specify filter and sensor
delays** parameter.

The **Specify filter and sensor delays** parameter
appears only if you select **Empirical method** option to
compute controller gain.

### **Speed filter delay (s)** — Delay due to speed filtering `0.02` (default) | scalar

Time delay (in seconds) introduced by speed filtering.

#### Dependencies

To enable this parameter, select the **Specify filter and sensor
delays** parameter.

The **Specify filter and sensor delays** parameter
appears only if you select **Empirical method** option to
compute controller gain.

## Libraries

Motor Control Blockset / Controls / Controllers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

## Description

Compute controller gains for the FOC based algorithms at run time based on empirical method or optimum theory

The FOC Default Controller Gains block computes controller gains for PI
controllers used in the field-oriented control (FOC) based algorithms based on empirical
method or optimum theory.

If you select **Empirical method** option:

- The block calculates controller gains using approximation of control loops to a
  lower-order linear time-invariant system and by applying optimal theories
  considering the fixed delays in the system.
- The block computes the PI controller gains used in the current controller,
  speed controller, and field-weakening controller using the *d-q*
  frame of reference-based motor model. The block uses the function
  `mcb.getPIControllerParameters` internally to compute the
  control gains. For more details about this function, see Obtain Controller Gains Using Empirical Method.
- The block accepts motor parameters along with the current and speed controller
  sample times to generate a bus containing proportional and integral control gains,
  which you can use for PI controllers in an FOC-based algorithm.
- The block uses the value that you specify at the
  **SlowdownFactor** input port to modify the PI gains output to
  make them less aggressive and slow down the system response.

**Note**

- The block uses empirical calculation to compute the control gains. The gains
  computed by the block might not be optimal and might require additional tuning
  to improve dynamic performance.
- It is recommended that you use the block inside a triggered subsystem or a
  slow-running control loop.
- The block inputs accept values greater than zero.

If you select **Based on optimum theory** option:

- The block calculates controller gains using approximation of control loops to
  lower-order linear time-invariant system, and by applying optimal theories with
  capability to consider any number of delays present in the system (for example,
  delays due to hardware filters and observers (in case of sensorless FOC)).
- The block uses:.

  - Modulus optimum theory for calculation of current controller
    gains
  - Symmetric optimum theory for calculation of speed controller
    gains
- The block computes the PI controller gains used in the current controller and
  speed controller using the *d-q* frame of reference-based motor
  model. The block uses the function `mcb.CalcFOCGains` internally
  to compute the control gains. For more details about the usage of this function
  and the block, see Obtain Controller Gains to Run Motor Using Field-Oriented Control.
- The block accepts motor parameters along with the current and speed controller
  sample times to generate a bus containing proportional and integral control gains,
  which can be used with PI controllers to implement control algorithms for motor
  drive systems.
- If you select `Per-unit` for Output unit parameter,
  provide Vbase (in Volts), Ibase (in
  Amperes) and Nbase (in RPM) as inputs via the corresponding
  ports.
- Provide overall time constant value for the delays present in feedback path of
  current loop and speed loop using the input ports **CurrLoopDelay** and
  **SpeedLoopDelay** respectively.
