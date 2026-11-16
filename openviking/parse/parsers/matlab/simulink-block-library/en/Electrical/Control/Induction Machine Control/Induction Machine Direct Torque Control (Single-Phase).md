---
type: simulink-block
title: 'Induction Machine Direct Torque Control (Single-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Induction Machine Control'
documentation_page: 'inductionmachinedirecttorquecontrolsinglephase'
documentation_source_path: 'ref/inductionmachinedirecttorquecontrolsinglephase.html'
language: en
---

# Induction Machine Direct Torque Control (Single-Phase)

## Ports

### Input

### **Reference** — Torque or angular velocity reference scalar

Specify the angular velocity reference in rad/s or the torque
reference in Nm.

**Data Types:** `single` | `double`

### **iab** — Stator currents scalar

Stator currents for main and auxiliary windings.

**Data Types:** `single` | `double`

### **vab** — Stator voltages scalar

Stator voltages for main and auxiliary windings.

**Data Types:** `single` | `double`

### **wr** — Rotor angular speed scalar

Measure rotor angular speed in rad/s.

**Data Types:** `single` | `double`
### Output

### **G** — Inverter gate pulses `0` | `1`

Inverter gate pulses, specified as a Boolean. The dead-time is not
considered.

**Data Types:** `single` | `double`

### **Visualization** — Internal signals for visualization `Reference` | `Rotor velocity` | `TqRef` | `FluxRef` | `Torque` | `Flux`

Bus containing internal signals for visualization. The signals are:

- Reference torque or speed
- Rotor velocity, in rad/s
- Torque Reference, in Nm
- Flux Reference, in Wb
- Torque, in Nm
- Flux, in Wb

**Data Types:** `single` | `double` | `bus`

## Parameters

### General

### **Control mode** — Specify control mode `Speed control` (default) | `Torque control`

Specify the control mode. The reference input is taken as angular speed, in rad/s, for
`Speed control` and torque, in Nm, for
`Torque control`.

### **Rated electrical frequency (Hz)** — Specify rated electrical frequency `60` (default) | positive scalar

Rated electrical frequency, in Hz.

### **Number of pole pairs** — Specify pole pairs `2` (default) | positive scalar

Number of pole pairs.

### **Main winding stator resistance, Ras (Ohm)** — Specify main winding stator resistance `1.8180` (default) | positive scalar

Resistance of the main winding stator, in Ohms.

### **Auxiliary winding stator resistance, Rbs (Ohm)** — Specify auxiliary winding stator resistance `6.4260` (default) | positive scalar

Resistance of the auxiliary winding stator, in Ohms.

### **Auxiliary/main windings turn ratio** — Specify the auxiliary-to-main windings turn ratio `1.1` (default) | positive scalar

Auxiliary-to-main windings turns ratio.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | positive scalar

Time, in s, between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

If this block is inside a triggered subsystem, inherit the
sample time by setting this parameter to `-1`. If this block is in a
continuous variable-step model, specify the sample time explicitly using a positive
scalar.

### Outer Loop

This table shows how the visibility of some parameters in the **Outer
Loop** tab depends on the option that you choose for the **Control mode** parameter in the
**General** tab.

| Control mode | Available Parameters |
| --- | --- |
| Speed control | Speed controller proportional gain |
| Speed controller integral gain |
| Speed controller integral anti-windup gain |
| Maximum torque (Nm) |
| Minimum torque (Nm) |
| Rated flux (Wb) |
| Torque control | Rated flux (Wb) |

### **Speed controller proportional gain** — Specify the speed controller proportional gain `1` (default) | positive scalar

Proportional gain for the PI speed controller.

### **Speed controller integral gain** — Specify the speed controller integral gain `10` (default) | positive scalar

Integral gain for the PI speed controller.

### **Speed controller integral anti-windup gain** — Specify the speed controller integral anti-windup gain `1000` (default) | positive scalar

Integral anti-windup gain.

### **Maximum torque (Nm)** — Specify the maximum torque `5` (default) | positive scalar

Maximum torque used in speed controller saturation, in Nm.

### **Minimum torque (Nm)** — Specify the minimum torque `-5` (default) | scalar

Minimum torque used in speed controller saturation, in Nm.

### **Rated flux (Wb)** — Specify the rated flux `0.5` (default) | positive scalar

Rated flux, in Wb. The rated flux is used to compute the flux reference.

### Inner Loop

### **Flux hysteresis band (Wb)** — Specify the flux hysteresis band `0.02` (default) | positive scalar

Flux hysteresis band for the controller, in Wb.

### **Torque hysteresis band (Nm)** — Specify the torque hysteresis band `0.1` (default) | positive scalar

Torque hysteresis band for the controller, in Nm.

## Libraries

Simscape / Electrical / Control / Induction Machine Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

Single-phase induction machine direct torque control

The Induction Machine Direct Torque Control (Single-Phase) block implements a
single-phase induction machine direct torque control structure.

### Equations

This diagram shows the direct torque control architecture for single-phase machines

The torque and flux estimation is based on machine voltage equations. The discrete-time
voltage equations using the backward Euler discretization method, are:

ψa=(va−iaRas)Tszz−1

ψb=(vb−ibRbs)Tszz−1

where:

- *Ras* and
  *Rbs* are the main
  winding resistance and the auxiliary winding resistance,
  respectively.
- *ia* and
  *ib* are the main
  winding current and the auxiliary winding current, respectively.
- *va* and
  *vb* are the main and
  auxiliary winding voltage, respectively.
- *ψa* and
  *ψb* are the main and
  auxiliary winding flux, respectively.

The torque and flux are obtained from:

T=−p(aψaib−1aψbia)

ψs=ψa2+ψb2

where:

- `p` is the number of pole pairs.
- `a` is the auxiliary to main windings turn
  ratio.

Employing simple hysteresis comparators detects the status of flux and torque errors. The
following figures illustrate the hysteresis comparators and the switching
sectors.

The table shows the optimum switching table (inverter high side).

| *cψ*, *cT*, *S(θ)* | | *S0* | *S1* | *S2* | *S3* |
| --- | --- | --- | --- | --- | --- |
| `cψ` = 1 | `cT` = 1 | 1, 0 | 1, 1 | 0, 1 | 0, 0 |
| `cT` = 0 | 1, 1 | 0, 1 | 0, 0 | 1, 0 |
| `cψ` = 0 | `cT` = 1 | 0, 0 | 1, 0 | 1, 1 | 0, 1 |
| `cT` = 0 | 0, 1 | 0, 0 | 1, 0 | 1, 1 |

The torque reference can be provided as an input, or, in the case of speed control, be
generated internally using a PI speed controller.

The flux reference is generated internally using:

ψs\*=2πfnψnpmin(|ωr|,2πfnp)

where,

- *ωr* is the rotor angular
  mechanical speed in rad/s.
- *fn* is the rated
  frequency.
- *ψn* is the rated flux.

### Limitations

- The power inverter dead-times are not considered in this block. For
  hardware implementation, add the dead-time externally.
