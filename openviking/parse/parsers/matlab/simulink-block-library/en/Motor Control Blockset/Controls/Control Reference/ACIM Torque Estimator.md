---
type: simulink-block
title: 'ACIM Torque Estimator'
family: 'motor-control-blockset-hdl-support'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'acimtorqueestimator'
documentation_source_path: 'ref/acimtorqueestimator.html'
language: en
---

# ACIM Torque Estimator

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

### **Te** — Electromechanical torque scalar

Electromechanical torque of the rotor.

**Data Types:** `single` | `double` | `fixed point`

### **Pe** — Electromechanical power scalar

Electromechanical power of the rotor.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### **Number of pole pairs** — Number of pole pairs available in motor `2` (default) | scalar

Number of pole pairs available in the induction motor.

### **Motor parameter input method** — Type of motor parameters `Linear model with lumped parameters` (default) | `Non-linear model with D,Q-flux linkage LUTs`

*Since R2025a*

Motor parameters that the block uses to generate power and torque estimates. Set the
parameter to one of these values:

- `Linear model with lumped parameters` — Generate torque
  and power estimates using lumped circuit values for the machine inductances
  *Ls*,*Lr*,*Lm*, and the rated flux.
- `Non-linear model with D,Q-flux linkage LUTs` —
  Generate torque and power estimates using *d*-axis and
  *q*-axis flux linkage lookup tables.

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

### **Base torque (Nm)** — Base torque for per-unit system `0.50072` (default) | scalar

Base torque (in Nm) for per-unit system. See Per-Unit System page for more
details.

This parameter is not configurable and uses a value that is internally computed
using other parameters.

#### Dependencies

To display this parameter, set **Input units** to
`Per-Unit (PU)`.

### **Base power (W)** — Base power for per-unit system `111.4284` (default) | scalar

Base power (in W) for per-unit system. See Per-Unit System page for more
details.

This parameter is not configurable and uses a value that is internally computed
using other parameters.

#### Dependencies

To display this parameter, set **Input units** to
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

### R2025a: Compute power and torque estimates using new block parameters

The Block Parameters dialog box now includes parameters that enable you to compute power
and torque estimates from flux linkage lookup table data.

## Description

Estimate electromechanical torque and power

The ACIM Torque Estimator block generates electromechanical torque and
power estimates for an induction motor. The block outputs the mathematically computed
electromechanical torque for constant motor parameters. To measure an accurate torque value,
we recommend that you use a physical sensor.

The block accepts feedback values of *d-* and *q*-axis
stator current and mechanical speed as inputs.

### Equations

If you select `Per-Unit (PU)` in the **Input
units** parameter, the block converts the inputs to SI units before performing
any computation. After calculating the output, the block converts the output back to per
unit values.

These equations describe the computation of electromechanical torque and power estimates
by the block.

Te=32p(LmLr)λrdisq

Pe=Te⋅ωm

For detailed set of equations and assumptions, see Mathematical Model of Induction Motor.

where:

- p is the number of pole pairs available in the motor.
- Lm is the magnetizing inductance of the motor (Henry).
- Lr is the rotor inductance (Henry).
- λrd is the *d*-axis flux linkage of the rotor
  (Weber).
- isq is the stator *q*-axis current (Amperes).
- ωm is the mechanical speed of the rotor (Radians/ sec).
