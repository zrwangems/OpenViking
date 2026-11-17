---
type: simulink-block
title: 'Position Generator'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'positiongenerator'
documentation_source_path: '../mcb/ref/positiongenerator.html'
language: en
---

# Position Generator

## Ports
```yaml
ports:
- name: ∆θ
  summary: Position increment value scalar
  direction: input
  data_types: single | double | fixed point
- name: θ0
  summary: Initial position signal scalar
  direction: input
  data_types: single | double | fixed point
- name: Reset
  summary: External reset signal scalar
  direction: input
  data_types: single | double | fixed point
- name: θe
  summary: Reference voltage position scalar
  direction: output
  data_types: single | double | fixed point
```

### Input

### **∆θ** — Position increment value scalar

Position increment value of a fixed frequency reference voltage signal (in either
per unit, radians, or degrees). These equations describe how you can compute the
position increment value:

- Δθ (per unit) = Frequency × Sample Time
- Δθ (radians) = 2π × Frequency × Sample Time
- Δθ (degrees) = 360 × Frequency × Sample Time

**Note**

If the preceding Δθ computation causes a precision loss in the block input, the
block might not replicate the actual *Frequency* accurately.

**Data Types:** `single` | `double` | `fixed point`

### **θ0** — Initial position signal scalar

Initial position value of a fixed frequency reference voltage signal (in either
per unit, radians, or degrees).

#### Dependencies

To enable this port, set the **Initial state** parameter to
`Input port`.

**Data Types:** `single` | `double` | `fixed point`

### **Reset** — External reset signal scalar

External pulse that resets the position ramp output based on the value of the
**External reset** parameter.

#### Dependencies

To enable this port, set **External reset** to either
`active high resets to zero` or `active high
resets to initial condition`.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **θe** — Reference voltage position scalar

Position or phase value of the reference voltage signal (in either per unit,
radians, or degrees).

**Data Types:** `single` | `double` | `fixed point`
## Parameters
```yaml
parameters:
- name: Theta Units
  summary: Unit of *θ* Per-unit (default) | Radians | Degrees
  group: ''
- name: Initial state
  summary: Specify how to provide initial value of *θ* Specify via dialog (default) | Input port
  group: ''
- name: Initial theta value
  summary: Initial value of θe 0 (default) | scalar
  group: ''
- name: External reset
  summary: Output value on reset none (default) | active high resets to zero | active high resets to initial condition
  group: ''
```

### **Theta Units** — Unit of *θ* `Per-unit` (default) | `Radians` | `Degrees`

Unit of the input position increment value and the output reference voltage
position.

### **Initial state** — Specify how to provide initial value of *θ* `Specify via dialog` (default) | `Input port`

Specify whether to provide the initial position as a block parameter or as an input
port.

Set this parameter to one of these options:

- `Specify via dialog` — Select this option if you want
  to specify the initial position using the block parameters dialog box.
- `Input port` — Select this option if you want to
  specify the initial position using an input port.

### **Initial theta value** — Initial value of `θe` `0` (default) | scalar

Output position ramp value (in either per unit, radians, or degrees) at initial time
(0 seconds).

#### Dependencies

To enable this parameter, set the **Initial state** parameter to
`Specify via dialog`.

### **External reset** — Output value on reset `none` (default) | `active high resets to zero` | `active high resets to initial condition`

Output position ramp value (in either per unit, radians, or degrees) at the time
when the block receives an active high external reset pulse. You can reset the output to
either zero or to equal the value of the **Initial theta output**
parameter.
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

**Restriction**

The block supports HDL code generation only when you set the **External
reset** parameter to `none`.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020a**

### R2025a: New input port and block parameters added

The Block Parameters dialog box now includes the **Initial state**
parameter for you to specify the initial position value from a separate input port
**θ0**.

## Description

Generate position ramp of fixed frequency

The Position Generator block generates a position ramp signal (with a
frequency that is identical to that of the reference voltage signal) using the position
increment value of the reference signal.

We recommend that you use fixed-step discrete solver for this block to enable code
generation and ensure accurate simulation.
