---
type: simulink-block
title: 'Compute Parameter'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Signal Management'
documentation_page: 'computeparameter'
documentation_source_path: 'ref/computeparameter.html'
language: en
---

# Compute Parameter

## Ports

### Input

### **Npp** — Number of pole pairs available in motor scalar

Number of pole pairs available in the motor.

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the Flux Observer or I-F
Controller block in the current model.

**Data Types:** `single` | `double` | `fixed point`

### **R** — Stator winding resistance scalar

Stator phase winding resistance of the motor (in ohms).

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the Flux Observer block in the current
model.

**Data Types:** `single` | `double` | `fixed point`

### **Rs** — Stator winding resistance scalar

Stator phase winding resistance of the motor (in ohms).

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the Extended EMF Observer block in the
current model.

**Data Types:** `single` | `double` | `fixed point`

### **Ld** — Stator winding inductance along *d*-axis scalar

Stator winding inductance of the motor along the *d*-axis
(in henries).

#### Dependencies

To enable this port:

- Set the **Relative path of compatible block that needs
  functional extension** parameter to indicate the relative
  path of the Flux Observer block or Extended EMF
  Observer block in the current model.
- If the compatible clock is Flux Observer, set the **Motor
  selection** parameter of the Flux Observer
  block to `PMSM`.

**Data Types:** `single` | `double` | `fixed point`

### **Lq** — Stator winding inductance along *q*-axis scalar

Stator winding inductance of the motor along the *q*-axis
(in henries).

#### Dependencies

To enable this port:

- Set the **Relative path of compatible block that needs
  functional extension** parameter to indicate the relative
  path of the Extended EMF Observer block in the current
  model.

**Data Types:** `single` | `double` | `fixed point`

### **Lls** — Stator leakage inductance of induction motor scalar

Leakage inductance of the induction motor stator winding (in
henries).

#### Dependencies

To enable this port:

- Set the **Relative path of compatible block that needs
  functional extension** parameter to indicate the relative
  path of the Flux Observer block in the current
  model.
- Set the **Motor selection** parameter of the
  Flux Observer block to
  `ACIM`.

**Data Types:** `single` | `double` | `fixed point`

### **Llr** — Rotor leakage inductance of induction motor scalar

Leakage inductance of the induction motor rotor winding (in henries).

#### Dependencies

To enable this port:

- Set the **Relative path of compatible block that needs
  functional extension** parameter to indicate the relative
  path of the Flux Observer block in the current
  model.
- Set the **Motor selection** parameter of the
  Flux Observer block to
  `ACIM`.

**Data Types:** `single` | `double` | `fixed point`

### **Lm** — Magnetizing inductance of induction motor scalar

Magnetizing inductance of the induction motor (in henries).

#### Dependencies

To enable this port:

- Set the **Relative path of compatible block that needs
  functional extension** parameter to indicate the relative
  path of the Flux Observer block in the current
  model.
- Set the **Motor selection** parameter of the
  Flux Observer block to
  `ACIM`.

**Data Types:** `single` | `double` | `fixed point`

### **fcutoff** — Cutoff frequency of internal highpass filter scalar

Cutoff frequency (in hertz) of the internal highpass filter that filters
noise.

The Flux Observer block uses an internal first-order IIR
highpass filter. Specify a frequency at this port that is lower than the lowest
frequency corresponding to the minimum speed of the motor. For example, you can
enter a value that is one-tenth of the lowest electrical frequency of the
stator voltages and currents. You can adjust the value you specify at this port
to determine a more accurate cutoff frequency that generates the desired block
output.

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the Flux Observer block in the current
model.

**Data Types:** `single` | `double` | `fixed point`

### **NumSlits** — Number of slits per phase scalar

The number of slits available in each phase of the quadrature
encoder.

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the Quadrature Decoder block in the current
model.

**Data Types:** `single` | `double` | `fixed point`

### **CountsPerSlit** — Number of counts generated for every slit scalar

The number of counts that the quadrature encoder generates for every slit. A
count indicates a slit position. For example, set this port to 4 (quadrature
mode) if you want the encoder to generate four counts corresponding to 00, 10,
11, and 01 slit positions or values. If you select the quadrature mode:

Encoder counts per revolution (post-quadrature) = **Encoder counts
per slit** ✖ **Encoder slits**

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the Quadrature Decoder block in the current
model.

**Data Types:** `single` | `double` | `fixed point`

### **ω1 (RPM)** — Speed (after motor starts) at which I-F control stops scalar

Speed (after motor starts) until which the I-F controller remains active (in
RPM). When the motor speed exceeds this value, the I-F controller becomes
inactive and the **Status** block output turns true.

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the I-F Controller block in the current
model.

**Data Types:** `single` | `double` | `fixed point`

### **ω2 (RPM)** — Speed required to re-enter I-F control scalar

After exiting I-F control (and entering closed-loop control), speed required
to reactivate the I-F controller (in RPM). When the motor speed falls below
this value, the I-F controller becomes active again and the
**Status** block output turns false.

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the I-F Controller block in the current
model.

**Data Types:** `single` | `double` | `fixed point`

### **ωmax** — Maximum supported mechanical speed scalar

Maximum mechanical speed (in RPM) that the block can support. If you set the
speed to a value higher than this value, the block generates incorrect
outputs.

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the Extended EMF Observer block in the
current model.

**Data Types:** `single` | `double` | `fixed point`

### **Imax (A)** — Maximum motor current during I-F control scalar

Maximum current (in amperes) that is supplied to the motor when I-F control
is active.

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the I-F Controller block in the current
model.

**Data Types:** `single` | `double` | `fixed point`

### **Max(Δω/Δt) (RPM/s)** — Maximum rate of speed change during I-F control scalar

Maximum rate at which motor speed can change (in RPM/s) when I-F control is
active.

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the I-F Controller block in the current
model.

**Data Types:** `single` | `double` | `fixed point`

### **IDecayRate (A/s)** — Maximum rate of current decay during I-F control scalar

Maximum rate at which motor current can decay (in amperes/s) when I-F
control is active.

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the I-F Controller block in the current
model.

**Data Types:** `single` | `double` | `fixed point`

### **ζ** — Speed oscillation damping coefficient value scalar

Value of the speed oscillation damping coefficient that the I-F
Controller block should use.

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the I-F Controller block in the current
model. The I-F Controller block must also be configured to enable speed
damping.

**Data Types:** `single` | `double` | `fixed point`

### **TIdle (s)** — Time of constant speed and current scalar

Time (in seconds) during which both motor speed and current remains constant
when I-F control is active.

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the I-F Controller block in the current
model.

**Data Types:** `single` | `double` | `fixed point`

### **KEEMF** — Extended EMF observer gain scalar

Gain of the linear extended EMF state observer.

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the Extended EMF Observer block in the
current model.

**Data Types:** `single` | `double` | `fixed point`

### **fEEMFcutoff** — Cutoff frequency of EEMF filter scalar

Cutoff frequency (in Hz) of the lowpass filter that the block uses to remove
noise in the estimated back-EMF value.

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the Extended EMF Observer block in the
current model.

**Data Types:** `single` | `double` | `fixed point`

### **fSpdcutoff** — Cutoff frequency of speed filter scalar

Cutoff frequency (in Hz) of the lowpass filter that the block uses to remove
noise in the estimated speed.

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the Extended EMF Observer block in the
current model.

**Data Types:** `single` | `double` | `fixed point`

### **fcutoff** — Cutoff frequency of lowpass filter scalar

Cutoff frequency (in Hz) of the lowpass filter that the block uses to filter
the estimated angular frequency.

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the PLL with Feed Forward block in the
current model.

**Data Types:** `single` | `double` | `fixed point`

### **KSpdp** — Proportional gain of the speed observer scalar

Proportional gain of the speed observer.

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the Extended EMF Observer block in the
current model.

**Data Types:** `single` | `double` | `fixed point`

### **KSpdi** — Integral gain of the speed observer scalar

Integral gain of the speed observer.

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the Extended EMF Observer block in the
current model.

**Data Types:** `single` | `double` | `fixed point`

### **Kp** — Proportional controller gain scalar

Proportional gain of the PID controller used by the block to compute the
angular frequency.

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the PLL with Feed Forward block in the
current model.

**Data Types:** `single` | `double` | `fixed point`

### **Ki** — Integral gain of the controller scalar

Integral gain of the PID controller used by the block to compute the angular
frequency.

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the PLL with Feed Forward block in the
current model.

**Data Types:** `single` | `double` | `fixed point`

### **UseInternalKpKi** — Use internal gains of the controller `0` | `1`

Option to use internal gains of the controller, instead of
Kp and Ki gains from the input
ports of this block. Set this port to accept `1` if you want
to use the Kp and Ki values
computed from the PLL with Feed Forward block.

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the PLL with Feed Forward block in the
current model.

**Data Types:** `Boolean`

### **fmax** — Maximum applicable input frequency scalar

Maximum possible frequency of the input signals (in Hz).

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the Extended EMF Observer block in the
current model.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **ParameterBus** — Computed parameters for compatible blocks bus

Computed parameters for the Flux Observer, I-F
Controller, Extended EMF, or PLL with Feed
Forward blocks.

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the Flux Observer, I-F
Controller, Extended EMF, or PLL with Feed Forward
block in the current model.

**Data Types:** `single`

### **CountsPerRev** — Number of counts per revolution scalar

Number of counts the quadrature encoder generates for each
revolution.

**CountsPerRev** = **Encoder slits** ⨯
**Encoder counts per slit**

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the Quadrature Decoder block in the current
model.

**Data Types:** `single`

### **1/CountsPerRev** — Inverse of number of counts per revolution scalar

The block outputs the inverse of the number of counts the quadrature encoder
generates for each revolution at this port.

**1/CountsPerRev** = 1/(**Encoder slits**
⨯ **Encoder counts per slit**)

#### Dependencies

To enable this port, set the **Relative path of compatible block
that needs functional extension** parameter to indicate the
relative path of the Quadrature Decoder block in the current
model.

**Data Types:** `single`

## Parameters

### **Relative path of compatible block that needs functional extension** — Relative path of compatible block blank (default) | string

Relative path of the compatible block from the current model that needs
functional extension.

### **Get a list of supported block paths in the model** — Obtain list of compatible block paths button

Click this button to obtain a list of relative paths of all compatible blocks
in the current model. The block displays this list in the **Supported
block paths** section.

Copy and paste the relevant path from the list in the **Relative path
of compatible block that needs functional extension** parameter to
configure this block.

### **Supported block paths** — List of compatible block paths display cell

This section displays the list of relative paths of the compatible blocks in
the current model.

## Libraries

Motor Control Blockset / Signal Management

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

## Description

Extend functionality of blocks by enabling additional inputs

The Compute Parameter block extends the functionality of compatible
blocks available in the current model. The block customizes itself according to the
settings of a compatible block and provides the parameters needed by the compatible block
through either an output bus or multiple output signals.

You can use the Compute Parameter block parameters dialog box to select a
compatible block by providing its relative path. The dialog box lists the relative paths of
all compatible blocks available in the current model, which you can then copy to the
**Relative path of compatible block that needs functional extension**
field in the dialog box.

For example, when you configure the Compute Parameter block to connect
with Flux Observer block, the Compute Parameter block
provides an output in the form of a bus. You can then connect this bus to the additional
input port **ParameterBus** available in the Flux Observer block.

For the other compatible blocks, you can connect the Compute Parameter
output signals to the corresponding additional input ports available in the compatible
blocks.

Therefore, the block provides a functional extension to the compatible blocks by
enabling them to accept parameter values at run-time. The block supports these compatible
blocks:

- Flux
  Observer
- Quadrature
  Decoder
- I-F
  Controller
- Extended EMF
  Observer
- PLL with Feed
  Forward

It is recommended that you run this block at a rate that is lower than the task rate of
compatible block to minimize the computation load in hardware targets.
