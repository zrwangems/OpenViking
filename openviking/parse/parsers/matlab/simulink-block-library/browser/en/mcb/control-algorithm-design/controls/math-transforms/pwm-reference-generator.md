---
type: simulink-block
title: 'PWM Reference Generator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Control Algorithm Design / Controls / Math Transforms'
documentation_page: 'pwmreferencegenerator'
documentation_source_path: 'ref/pwmreferencegenerator.html'
language: en
---

# PWM Reference Generator

## Ports

### Input

### **Vα** — *α*-axis stator reference voltage component scalar

Stator reference voltage component along *α*-axis of the
*αβ* reference frame.

#### Dependencies

To enable this port, set **Input type** to
`Valphabeta`.

**Data Types:** `single` | `double` | `fixed point`

### **Vβ** — *β*-axis stator reference voltage component scalar

Stator reference voltage component along *β*-axis of the
*αβ* reference frame.

#### Dependencies

To enable this port, set **Input type** to
`Valphabeta`.

**Data Types:** `single` | `double` | `fixed point`

### **Va** — Phase component scalar

Component of the three-phase system in the *abc* reference
frame.

#### Dependencies

To enable this port, set **Input type** to
`Vabc`.

**Data Types:** `single` | `double` | `fixed point`

### **Vb** — Phase component scalar

Component of the three-phase system in the *abc* reference
frame.

#### Dependencies

To enable this port, set **Input type** to
`Vabc`.

**Data Types:** `single` | `double` | `fixed point`

### **Vc** — Phase component scalar

Component of the three-phase system in the *abc* reference
frame.

#### Dependencies

To enable this port, set **Input type** to
`Vabc`.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **Vao** — *a*-axis stator reference voltage component scalar

Stator reference voltage component along *a*-axis of the
*abc* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **Vbo** — *b*-axis stator reference voltage component scalar

Stator reference voltage component along *b*-axis of the
*abc* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **Vco** — *c*-axis stator reference voltage component scalar

Stator reference voltage component along *c*-axis of the
*abc* reference frame.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### **Input type** — Block input type `Valphabeta` (default) | `Vabc` | `Degrees`

Type of three-phase stator voltage representation that the block uses as input.
Select either the *abc* or *αβ* reference
frame.

### **Modulation method** — Pulse-width modulation (PWM) methods `SVM: space vector modulation` (default) | `SPWM: sinusoidal PWM` | `60 DPWM:60 degree discontinuous PWM` | `60 DPWM (+30 degree shift):+30 degree shift from 60 DPWM` | `60 DPWM (-30 degree shift):-30 degree shift from 60 DPWM` | `30 DPWM: 30 degree discontinuous PWM` | `120 DPWM: positive DC component` | `120 DPWM: negative DC component`

Pulse-width modulation (PWM) method that the block uses to modulate the input stator
phase or reference voltages.

## Libraries

Motor Control Blockset / Controls / Math Transforms Motor Control Blockset HDL Support / Controls / Math Transforms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**Supported Block Parameters**

For HDL code generation with the PWM Reference Generator block, set the
**Modulation method** to `SVM: space vector
modulation` or `SPWM: sinusoidal PWM`.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **FlattenHierarchy** | Remove PWM Reference Generator block hierarchy from generated HDL code. The default is `inherit`. See also FlattenHierarchy (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing (HDL Coder). |

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020a**

## Description

Generate modulated signals from phase voltages

The PWM Reference Generator block generates modulated voltage signals from
the stator phase or reference voltages.

The block accepts either the phase voltages
(*Vabc*) or the stator reference voltages
(*Vαβ*) described by the *α-β*
voltage components.

Use this block to perform sinusoidal PWM (SPWM) and space vector modulation (SVM) along
with these discrete pulse-width modulation (DPWM) methods that reduce switching losses:

**Note**

For the following DPWM methods the block supports only per-unit (PU) input signals. For
more information about the per-unit system, see Per-Unit System.

- 60 DPWM — 60 degree discontinuous PWM
- 60 DPWM (+30 degree shift) — +30 degree shift from 60 DPWM
- 60 DPWM (-30 degree shift) — -30 degree shift from 60 DPWM
- 30 DPWM — 30 degree discontinuous PWM
- 120 DPWM — Positive DC component
- 120 DPWM — Negative DC component

For discontinuous PWM (DPWM), the block clamps the modulation wave to the positive or
negative DC rail for a total of 120 degrees during each fundamental period per phase. During
each clamping interval, the modulation discontinues.

The figure shows the sinusoidal PWM (SPWM) waveform.

The figure shows the space vector modulation (SVM) waveform.

The figure shows a 60-degree DPWM waveform with two 60-degree clamped intervals per
fundamental period.

The figure shows a 60-degree DPWM waveform with a positive 30-degree phase shift.

The figure shows a 60-degree DPWM waveform with a negative 30-degree phase shift.

The figure shows a 30-degree DPWM waveform with four 30-degree clamped intervals per
fundamental period.

The figure shows a 120-degree DPWM waveform with positive DC clamping.

The figure shows a 120-degree DPWM waveform with negative DC clamping.
