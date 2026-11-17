---
type: simulink-block
title: 'ACIM Feed Forward Control'
family: 'motor-control-blockset-hdl-support'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'acimfeedforwardcontrol'
documentation_source_path: 'ref/acimfeedforwardcontrol.html'
language: en
---

# ACIM Feed Forward Control

## Ports

### Input

### **Isd** — D-axis stator current scalar

Stator current along the *d*-axis of the rotating
*dq* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **Isq** — Q-axis stator current scalar

Stator current along the *q*-axis of the rotating
*dq* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **ωm** — Mechanical speed of rotor scalar

Mechanical speed of the rotor.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **VsdFF** — D-axis feedforward voltage scalar

Feedforward voltage along the *d*-axis of the rotating
*dq* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **VsqFF** — Q-axis feedforward voltage scalar

Feedforward voltage along the *q*-axis of the rotating
*dq* reference frame.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### **Number of pole pairs** — Number of pole pairs available in motor `2` (default) | scalar

Number of pole pairs available in the induction motor.

### **Motor parameter input method** — Type of motor parameters `Linear model with lumped parameters` (default) | `Non-linear model with D,Q-flux linkage LUTs`

*Since R2025a*

Motor parameters that the block uses to generate feedforward voltage gains. Set the
parameter to one of these values:

- `Linear model with lumped parameters` — Generate
  voltage gains using lumped circuit values for the machine inductances
  *Ls*,*Lr*,*Lm*, and the rated flux.
- `Non-linear model with D,Q-flux linkage LUTs` —
  Generate voltage gains using *d*-axis and *q*-axis
  flux linkage lookup tables.

### **Stator leakage inductance (H)** — Leakage inductance of stator winding `6.81e-3` (default) | scalar

Inductance due to leakage flux linked to the stator winding (in Henry).

#### Dependencies

To enable this parameter, set the **Motor parameter input
method** parameter to `Linear model with lumped
parameters`.

### **Rotor leakage inductance (H)** — Leakage inductance of rotor winding `6.81e-3` (default) | scalar

Inductance due to leakage flux linked to the rotor winding (in Henry).

#### Dependencies

To enable this parameter, set the **Motor parameter input
method** parameter to `Linear model with lumped
parameters`.

### **Magnetizing Inductance (H)** — Magnetizing inductance of induction motor `30e-3` (default) | scalar

Inductance due to the magnetizing flux (in Henry).

#### Dependencies

To enable this parameter, set the **Motor parameter input
method** parameter to `Linear model with lumped
parameters`.

### **Rated Flux (Wb)** — Rated flux of motor `38.2e-3` (default) | scalar

Rated flux of the induction motor (in Weber).

#### Dependencies

To enable this parameter, set the **Motor parameter input
method** parameter to `Linear model with lumped
parameters`.

### **D-axis current breakpoint vector, id (A)** — *d*-axis current lookup vector `[0, 150, 350, 500]` (default) | vector

*Since R2025a*

The *d*-axis current lookup vector to use in the flux-linkage
lookup tables (in percentage). The vector can have any number of elements.

#### Dependencies

To enable this parameter, set the **Motor parameter input
method** parameter to `Non-linear model with D,Q-flux linkage
LUTs`.

### **Q-axis current breakpoint vector, id (A)** — *q*-axis current lookup vector `[0, 250, 500]` (default) | vector

*Since R2025a*

The *q*-axis current lookup vector to use in the flux-linkage
lookup tables (in percentage). The vector can have any number of elements.

#### Dependencies

To enable this parameter, set the **Motor parameter input
method** parameter to `Non-linear model with D,Q-flux linkage
LUTs`.

### **D-axis flux linkage LUT, FluxD (id,iq) (Wb)** — Reference *d*-axis flux linkage lookup data `4.4e-2 * repmat([0, 150, 350, 500]', 1, 3)` (default) | vector

*Since R2025a*

The *d*-axis flux linkage lookup table data (in weber).

#### Dependencies

To enable this parameter, set the **Motor parameter input
method** parameter to `Non-linear model with D,Q-flux linkage
LUTs`.

### **Q-axis flux linkage LUT, FluxD (id,iq) (Wb)** — Reference *q*-axis flux linkage lookup data `2.1e-3 * repmat([0, 250, 500], 4, 1)` (default) | vector

*Since R2025a*

The *q*-axis flux linkage lookup table data (in weber).

#### Dependencies

To enable this parameter, set the **Motor parameter input
method** parameter to `Non-linear model with D,Q-flux linkage
LUTs`.

### **Output Saturation (V)** — Saturation limit for output values `24/sqrt(3)` (default) | scalar

Saturation limit (in Volts) for the block outputs
`VsdFF` and
`VsqFF`.

### **Input units** — Unit of input values `Per-Unit (PU)` (default) | `SI Units`

Unit of the input values.

### **Base Voltage (V)** — Base voltage for per-unit system `24/sqrt(3)` (default) | scalar

Base voltage (in Volts) for per-unit system.

#### Dependencies

To enable this parameter, set **Input units** to
`Per-Unit (PU)`.

### **Base Current (A)** — Base current for per-unit system `5.3611` (default) | scalar

Base current (in Amperes) for per-unit system.

#### Dependencies

To enable this parameter, set **Input units** to
`Per-Unit (PU)`.

### **Base Speed (rpm)** — Base speed for per-unit system `1500` (default) | scalar

Base speed (in rpm) for per-unit system.

#### Dependencies

To enable this parameter, set **Input units** to
`Per-Unit (PU)`.

## Libraries

Motor Control Blockset / Controls / Control Reference Motor Control Blockset HDL Support / Controls / Control Reference

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing (HDL Coder). |

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020b**

### R2025a: Compute feedforward voltage gains using new block parameters

The Block Parameters dialog box now includes parameters that enable you to compute
feedforward voltage gains from flux linkage lookup table data.

## Description

Decouple d -axis and q -axis current to eliminate disturbance

The ACIM Feed Forward Control block decouples *d*-axis and
*q*-axis current controls and generates the corresponding feedforward
voltage gains for field-oriented control of the induction motor.

The block accepts feedback values of *d*-axis and
*q*-axis currents and the mechanical speed of the rotor.

### Equations

If you select `Per-Unit (PU)` in the **Input
units** parameter, the block converts the inputs to SI units before performing
any computation. After calculating the output, the block converts the values back to
per-unit (PU) values.

The machine inductances and stator flux are represented as,

Ls= Lls+ Lm

Lr= Llr+ Lm

σ=1−(Lm2Ls⋅Lr)

λsd= LmLrλrd+σLsisd

λsq= σLsisq

These equations describe how the block computes the feedforward gain.

VsdFF=−ωeλsq

VsqFF=ωeλsd

For detailed set of equations and assumptions, see Mathematical Model of Induction Motor.

where:

- ωe is the electrical speed corresponding to frequency of stator voltages
  (Radians/ sec).
- Lls is the stator leakage inductance (Henry).
- Llr is the rotor leakage inductance (Henry).
- Ls is the stator inductance (Henry).
- Lr is the rotor inductance (Henry).
- Lm is the magnetizing inductance of the motor (Henry).
- σ is the total leakage factor of the induction motor.
- λsd is the *d*-axis flux linkage of the stator
  (Weber).
- λsq is the *q*-axis flux linkage of the stator
  (Weber).
- λrd is the *d*-axis flux linkage of the rotor
  (Weber).
- isd and isq are the stator *d*- and *q*-axis
  currents (Amperes).
