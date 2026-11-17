---
type: simulink-block
title: 'Protection Relay'
family: 'motor-control-blockset-hdl-support'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Protection and Diagnostics'
documentation_page: 'protectionrelay'
documentation_source_path: 'ref/protectionrelay.html'
language: en
---

# Protection Relay

## Ports
```yaml
ports:
- name: Imax
  summary: Upper limit for current scalar
  direction: input
  data_types: single | double | fixed point
- name: Ifb
  summary: Actual current in feedback loop scalar
  direction: input
  data_types: single | double | fixed point
- name: ⍵m max
  summary: Rotor speed limit for overspeed protection scalar
  direction: input
  data_types: single | double | fixed point
- name: ⍵m fb
  summary: Actual rotor speed scalar
  direction: input
  data_types: single | double | fixed point
- name: Vmax
  summary: Upper voltage limit for overvoltage protection scalar
  direction: input
  data_types: single | double | fixed point
- name: Vmin
  summary: Lower voltage limit for undervoltage protection scalar
  direction: input
  data_types: single | double | fixed point
- name: Vfb
  summary: Actual voltage across feedback loop scalar
  direction: input
  data_types: single | double | fixed point
- name: Reset
  summary: External reset pulse scalar
  direction: input
  data_types: single | double | fixed point
- name: y
  summary: Latched fault signal scalar
  direction: output
  data_types: single | double | fixed point
```

### Input

### **Imax** — Upper limit for current scalar

Upper limit for current (in amperes) in the feedback loop, so as to provide
overcurrent protection. The block generates a latched fault signal when the current in
the feedback loop (`Ifb`) exceeds this
value.

#### Dependencies

To enable this port, set **Select Protection** to
`Overcurrent`.

**Data Types:** `single` | `double` | `fixed point`

### **Ifb** — Actual current in feedback loop scalar

Actual current (in amperes) in the feedback loop at a given time.

#### Dependencies

To enable this port, set **Select Protection** to
`Overcurrent`.

**Data Types:** `single` | `double` | `fixed point`

### **⍵m max** — Rotor speed limit for overspeed protection scalar

Speed limit of the rotor (in RPM). The block generates a latched fault signal when
the rotor speed (`⍵m fb`) exceeds this
value.

#### Dependencies

To enable this port, set **Select Protection** to
`Overspeed`.

**Data Types:** `single` | `double` | `fixed point`

### **⍵m fb** — Actual rotor speed scalar

Actual rotor speed (in RPM) at a given time.

#### Dependencies

To enable this port, set **Select Protection** to
`Overspeed`.

**Data Types:** `single` | `double` | `fixed point`

### **Vmax** — Upper voltage limit for overvoltage protection scalar

Upper limit for voltage (in volts) across the feedback loop. The block generates a
latched fault signal when the voltage across the feedback loop
(`Vfb`) exceeds this value.

#### Dependencies

To enable this port, set **Select Protection** to
`Overvoltage`.

**Data Types:** `single` | `double` | `fixed point`

### **Vmin** — Lower voltage limit for undervoltage protection scalar

Lower limit for voltage (in volts) across the feedback loop. The block generates a
latched fault signal when the voltage across the feedback loop
(`Vfb`) is less than this value.

#### Dependencies

To enable this port, set **Select Protection** to
`Undervoltage`.

**Data Types:** `single` | `double` | `fixed point`

### **Vfb** — Actual voltage across feedback loop scalar

Actual voltage (in volts) across the feedback loop at a given time.

#### Dependencies

To enable this port, set **Select Protection** to either
`Overvoltage` or
`Undervoltage`.

**Data Types:** `single` | `double` | `fixed point`

### **Reset** — External reset pulse scalar

External pulse that resets the fault latch.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **y** — Latched fault signal scalar

Latched fault signal that the block generates during the overcurrent, overspeed,
overvoltage, and undervoltage conditions to protect the hardware and the motor.

**Data Types:** `single` | `double` | `fixed point`
## Parameters
```yaml
parameters:
- name: Select Protection
  summary: Type of protection relay Overcurrent (default) | Overspeed | Overvoltage | Undervoltage
  group: ''
- name: Maximum count input type
  summary: Input method for maximum count Specify via dialog (default) | Input port
  group: ''
- name: Maximum count
  summary: Counter limit 100 (default) | scalar
  group: ''
- name: Samples for debounce filter
  summary: Number of debounce samples 3 (default) | scalar
  group: ''
```

### **Select Protection** — Type of protection relay `Overcurrent` (default) | `Overspeed` | `Overvoltage` | `Undervoltage`

Available protection types to configure block behavior during the overcurrent,
overspeed, overvoltage, and undervoltage conditions.

### **Maximum count input type** — Input method for maximum count `Specify via dialog` (default) | `Input port`

Use one of these methods to specify the counter limit:

- `Specify via dialog` — Specify the counter limit using
  the **Maximum count** parameter.
- `Input port` — Specify the counter limit using the
  input port **Cntmax**.

### **Maximum count** — Counter limit `100` (default) | scalar

The maximum count supported by the counter that the block uses for evaluating a
threshold violation by the feedback signal.

### **Samples for debounce filter** — Number of debounce samples `3` (default) | scalar

The number of block samples used by the debounce algorithm to test each threshold
violation cease. This value determines the debounce period.
## Libraries

Motor Control Blockset HDL Support / Protection and Diagnostics Motor Control Blockset / Protection and Diagnostics

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

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020a**

## Description

Implement protection relay with definite minimum time (DMT) trip characteristics

The Protection Relay block implements a protection relay for the hardware
and the motor with definite minimum time (DMT) trip characteristics using the reference limit,
feedback, and reset input signals. In the event of a fault, the block generates a latched
fault signal that you can use to protect the hardware and the motor. You can reset the fault
latch using an external reset signal.

For more details about the algorithm used by the block, see Algorithms.
