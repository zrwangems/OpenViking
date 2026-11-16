---
type: simulink-block
title: 'VbyF Controller'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Controllers'
documentation_page: 'vbyfcontroller'
documentation_source_path: 'ref/vbyfcontroller.html'
language: en
---

# VbyF Controller

## Ports

### Input

### **ωmref** — Reference speed scalar

Reference mechanical speed for V/F control.

**Data Types:** `single` | `double` | `fixed point`

### **ωmrated** — Motor rated speed scalar

Rated mechanical speed of the motor.

**Data Types:** `single` | `double` | `fixed point`

### **Npp** — Number of motor pole pairs scalar

Number of pole pairs available in the three-phase motor.

**Data Types:** `single` | `double` | `fixed point` | `uint` | `int`

### **Vrated** — Rated phase voltage amplitude of motor scalar

Amplitude (peak value) of the rated phase voltage of the motor corresponding
to the rated speed of the motor.

**Data Types:** `single` | `double` | `fixed point`

### **Vmin** — Minimum output voltage scalar

Minimum amplitude (peak value) of the block output voltage that should be
applied to the motor.

**Data Types:** `single` | `double` | `fixed point`

### **NRamp** — Steps for initial ramp up scalar

Number of discrete time steps used for initial ramp up of motor
speed.

**Data Types:** `single` | `double` | `fixed point` | `uint` | `int`

### **Enable** — Enable block outputs scalar

Signal that enables block outputs:

- `1` — Enables block outputs.
- `0` — Reset internal integrators.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **Vabc** — Motor phase voltages vector

Stator phase *a*, *b*, and
*c* voltages that drive the motor.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### **Input speed unit** — Unit of the speed inputs `Radians/Sec` (default) | `RPM` | `Degrees/Sec` | `Per unit based on dialog`

Units of the
**ωmref**
and **ωmrated**
inputs.

Select `Per unit based on dialog` to use per-unit
system for the two speed inputs. For more information about the per-unit system,
see Per-Unit System.

### **Per unit speed (RPM)** — Base speed of the motor (RPM) `1200` (default) | scalar

Rated speed of the motor (in rpm) that the block uses in the per-unit
computations. For more information about the per-unit system, see Per-Unit System.

#### Dependencies

To enable this parameter, set **Input speed unit** to
`Per unit based on dialog`.

### **Discrete step size (s) (-1 for inherit)** — Sample time after which block executes again `50e-6` (default) | scalar

The fixed time interval (in seconds) between two consecutive instances of block
execution.

## Libraries

Motor Control Blockset / Controls / Controllers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

**Restrictions**

If you specify 16-bit fixed-point inputs, the block might not produce an accurate
output due to insufficient resolution.

## Version History

**Introduced in R2023b**

## Description

Implement V/F (open-loop or scalar) control for three-phase motors

The VbyF Controller block implements V/F (open-loop or scalar) control
for a three-phase permanent magnet synchronous motor (PMSM) or an AC induction motor
(ACIM).

You can specify reference speed, motor rated speed, number of motor pole pairs, motor
rated voltage, minimum block output voltage, as well as number of discrete time steps for
initial ramp up as inputs to compute the three-phase voltages that drive the motor.

When you start up the motor, the block uses the
**NRamp** input to identify the number of block
samples that it needs to gradually ramp up the motor speed to the reference speed.

NRamp=TrampDiscrete step size (s)

The block's output voltage amplitude varies according to the reference motor speed
(*ωref*), while keeping the ratio of rated
voltage to rated frequency constant.

Vabc\_amplitude=  (Vratedfrated)fref=(Vratedωrated)ωref

where:

- *Vabc\_amplitude* is the amplitude of the
  output voltage **Vabc**.
- *Vrated* is the amplitude of rated phase
  voltage of the motor.
- *frated* is the rated frequency of the
  motor.
- *fref* is the reference frequency of
  the motor.
- *ωrated* is the rated speed of the
  motor.
- *ωref* is the reference speed of the
  motor.

The V/F control technique does not require any feedback from the motor. This control
technique ensures a constant stator magnetic flux by keeping the motor phase voltage
proportional to its frequency. For more information about this technique, see Open-Loop Motor Control.

**Note**

- It is recommended that you use this block to start the motor and run it at
  lower speeds and then switch to other control methods, such as field-oriented
  control (FOC), to operate the motor at higher speeds.
- If you specify 16-bit fixed-point inputs, the block might not produce an
  accurate output due to insufficient resolution.
