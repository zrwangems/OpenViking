---
type: simulink-block
title: 'Induction Machine Field-Oriented Control (Single-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Induction Machine Control'
documentation_page: 'inductionmachinefieldorientedcontrolsinglephase'
documentation_source_path: 'ref/inductionmachinefieldorientedcontrolsinglephase.html'
language: en
---

# Induction Machine Field-Oriented Control (Single-Phase)

## Ports

### Input

### **Reference** — Torque or angular velocity reference scalar

Specify the angular velocity reference, in rad/s, or the torque reference, in Nm.

**Data Types:** `single` | `double`

### **iab** — Stator currents scalar

Stator currents for main and auxiliary windings.

**Data Types:** `single` | `double`

### **wr** — Rotor angular speed scalar

Measured rotor angular speed, in rad/s.

**Data Types:** `single` | `double`
### Output

### **G** — Inverter gate pulses `0` | `1`

Inverter gate pulses, specified as a Boolean. The dead-time is not
considered.

**Data Types:** `single` | `double`

### **Visualization** — Internal signals for visualization `Reference` | `Rotor velocity` | `θ` | `iab` | `iabRef` | `TqRef` | `FluxRef`

Bus containing internal signals for visualization. The signals are:

- Reference torque or speed
- Rotor velocity, in rad/s
- *θ*, in radians
- Stator currents (*iab*), in A
- Stator current reference (*iabRef*), in
  A
- Torque Reference (*TqRef*), in Nm
- Flux Reference (*FluxRef*), in Wb

**Data Types:** `single` | `double` | `bus`

## Parameters

### General

### **Control mode** — Specify control mode `Speed control` (default) | `Torque control`

Specify the control mode. The reference input is taken as angular
speed, in rad/s, for `Speed control` and
torque, in Nm for `Torque control`.

### **Rated electrical frequency (Hz)** — Specify rated electrical frequency `60` (default) | positive scalar

Rated electrical frequency, in Hz.

### **Number of pole pairs** — Specify pole pairs `2` (default) | positive scalar

Number of pole pairs.

### **Main winding rotor resistance, Rar' (Ohm)** — Specify main winding rotor resistance `3.7080` (default) | positive scalar

Main winding rotor resistance, in Ohms.

### **Main winding rotor leakage inductance, Llar' (H)** — Specify main winding rotor leakage inductance `0.0050` (default) | positive scalar

Main winding rotor leakage inductance, in H.

### **Main winding mutual inductance, Lms (H)** — Specify main winding mutual inductance `0.1595` (default) | positive scalar

Main winding mutual inductance, in H.

### **Auxiliary/main windings turn ratio** — Specify the auxiliary-to-main windings turn ratio `1.1` (default) | positive scalar

Auxiliary-to-main windings turns ratio.

### **Fundamental sample time (s)** — Specify the block sample time `5e-6` (default) | positive scalar

Sample time for the block, in s.

### **Control sample time (s)** — Specify the control sample time `5e-5` (default) | positive scalar

Control sample time, in s.

### Outer Loop

This table shows how the visibility of some parameters in the **Outer
Loop** tab depend on the option that you choose for the **Control mode** parameter in the
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

Rated flux, in Wb. The rated flux is used to compute the flux
reference.

### Inner Loop

This table shows how the visibility of some parameters in the **Inner
Loop** tab depend on the option that you choose for the **Control type** parameter.

| Control type | Available Parameters |
| --- | --- |
| Hysteresis control | Current hysteresis band (A) |
| PI control | A-phase current proportional gain |
| A-phase current integral gain |
| A-phase current anti-windup gain |
| B-phase current proportional gain |
| B-phase current integral gain |
| B-phase current anti-windup gain |

### **Control type** — Specify the control type `Hysteresis control` (default) | `PI control`

Control type for current control loop.

### **Current hysteresis band (A)** — Specify the current hysteresis band `0.5` (default) | positive scalar

Current hysteresis band for the controller, in A.

### **A-phase current proportional gain** — Main winding current proportional gain `1` (default) | positive scalar

Proportional gain for the A-phase (main winding) controller
current.

### **A-phase current integral gain** — Main winding current integral gain `500` (default)

Integral gain for the A-phase (main winding) controller
current.

### **A-phase current anti-windup gain** — Main winding current anti-windup gain `1000` (default)

Anti-windup gain for the A-phase (main winding) controller
current.

### **B-phase current proportional gain** — Auxiliary winding current proportional gain `1` (default)

Proportional gain for the B-phase (auxiliary winding) controller
current.

### **B-phase current integral gain** — Auxiliary winding current integral gain `500` (default)

Integral gain for the B-phase (auxiliary winding) controller
current.

### **B-phase current anti-windup gain** — Auxiliary winding current anti-windup gain `1000` (default)

Anti-windup gain for the B-phase (auxiliary winding) controller
current.

## Libraries

Simscape / Electrical / Control / Induction Machine Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

Per-unit discrete-time single-phase induction machine field-oriented control

The Induction Machine Field-Oriented Control (Single-Phase) block implements
a single-phase induction machine field-oriented control structure.

### Equations

The field-oriented control architecture for a single-phase induction machine is:

You can provide the torque reference as an input, or, in the case of speed control,
generate the reference internally using a PI speed controller. The torque reference
as derived from a PI speed controller is:

T\*=(Kp\_ω+Ki\_ωTszz−1)(ωref−ωr)

where *ωr* is the rotor
angular mechanical speed in rad/s.

The block generates the flux reference as

ψ\*=2πfnψnpmin(|ωr|,2πfnp)

where:

- *p* is the number of pole pairs.
- *fn* is the rated
  frequency.
- *ψn* is the rated flux.

Current references are obtained from machine parameters:

iq\*=(Lms+Llar)T\*paLmsψ\*

id\*=ψ\*a2Lms

where:

- *Lms* is the main winding
  mutual inductance.
- *Llar* is the main winding
  rotor leakage inductance.
- *a* is the auxiliary-to-main windings turn
  ratio.

The angle is calculated by solving:

dθdt=pωr+a3LmsRarψ\*(Lms+Llar)

The transformation to the stationary reference frame is done by using:

(iaib)=(a2sin(θ)a2cos(θ)cos(θ)−sin(θ))(idiq)

### Limitations

- The control structure is implemented in a single sample rate.
