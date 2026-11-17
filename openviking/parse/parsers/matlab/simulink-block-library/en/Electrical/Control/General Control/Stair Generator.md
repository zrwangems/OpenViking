---
type: simulink-block
title: 'Stair Generator'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'stairgenerator'
documentation_source_path: 'ref/stairgenerator.html'
language: en
---

# Stair Generator

## Ports
```yaml
ports:
- name: Port_1
  summary: Stair signal Simulink® signal
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64
```

### Output

### **Port\_1** — Stair signal Simulink® signal

Stair signal, returned as a Simulink output signal.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
## Parameters
```yaml
parameters:
- name: Time (s)
  summary: Transition times [0.5 1 3 3.5] (default) | row vector of nonnegative values
  group: Main
- name: Amplitude
  summary: Amplitudes of stair signal values [1 -1 2.5 0] (default) | row vector
  group: Main
- name: Sample time (-1 for inherited)
  summary: Block sample time -1 (default) | 0 | positive scalar
  group: Main
- name: Repeat stair pattern indefinitely
  summary: Stair pattern repetition off (default) | on
  group: Main
- name: Output data type
  summary: 'Specify the output data type double (default) | Inherit: auto | Inherit: Inherit via internal rule | Inherit:
    Inherit via back propagation | single | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64 | uint64 | <data type expression>'
  group: Signal Attributes
  block_parameter: OutDataTypeStr
  type: character vector
  values: '''Inherit: auto'' | ''Inherit: Inherit via internal rule''| ''Inherit: Inherit via back propagation'' | ''single''
    | ''double'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32''|''int64''|''uint64''| ''<data type
    expression>'''
  default: '''Inherit: Inherit via internal rule'''
```

### Main

### **Time (s)** — Transition times `[0.5 1 3 3.5]` (default) | row vector of nonnegative values

Transition times at which the output changes to the value specified in
the **Amplitude** parameter, in seconds. The value of
this parameter must be strictly ascending.

### **Amplitude** — Amplitudes of stair signal values `[1 -1 2.5 0]` (default) | row vector

Amplitudes of the stair signal at the time specified by the
**Time (s)** parameter. This vector must have the
same number of elements as the **Time (s)**
parameter.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | `0` | positive scalar

Time between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

For inherited discrete-time operation, set this parameter to `-1`.
For discrete-time operation, set this parameter to a positive integer. For
continuous-time operation, set this parameter to `0`.

If this block is in a masked subsystem or a variant subsystem that supports switching
between continuous operation and discrete operation, promote this parameter to ensure
correct switching between the continuous and discrete implementations of the block. For
more information, see Promote Block Parameters on a Mask.

### **Repeat stair pattern indefinitely** — Stair pattern repetition `off` (default) | `on`

Whether to indefinitely repeat the stair pattern. If you select this
parameter, the output repeats the stair pattern defined by the
**Time (s)** and **Amplitude**
parameters indefinitely.

If you clear this parameter, the output executes the stair pattern
only once and then keeps the last amplitude active for all subsequent
times.

### Signal Attributes

### **Output data type** — Specify the output data type `double` (default) | `Inherit: auto` | `Inherit: Inherit via internal rule` | `Inherit: Inherit via back propagation` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `<data type expression>`

Data type for the output. The type can be inherited, specified
directly, or expressed as a data type object such as
`Simulink.NumericType`.

When you select an inherited option, the block exhibits these
behaviors:

- `Inherit: Inherit via internal rule`
  — Simulink chooses a data type to balance numerical accuracy,
  performance, and generated code size, while taking into account
  the properties of the embedded target hardware. If you change
  the embedded target settings, the data type selected by the
  internal rule might change. It is not always possible for the
  software to optimize efficiency and numerical accuracy at the
  same time.
- `Inherit: Inherit via back
  propagation` — Simulink automatically
  determines the output data type of the block during data type
  propagation (see Data Type Propagation). In this case, the
  block uses the data type of a downstream block or signal
  object.
- `Inherit: auto` — Use a rule that
  inherits a data type.

For more information, see Control Data Types of Signals.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: auto'` | `'Inherit: Inherit via internal rule'`| `'Inherit: Inherit via back propagation'` | `'single'` | `'double'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'`|`'int64'`|`'uint64'`| `'<data type expression>'` |
| **Default**: `'Inherit: Inherit via internal rule'` |
## Libraries

Simscape / Electrical / Control / General Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020a**

## Description

Discrete-time or continuous-time stair signal generator

The Stair Generator block generates a stair signal based on the values
specified in the **Time (s)** and **Amplitude**
parameters.

The block can output a repeating stair pattern or execute the pattern only once by keeping
the last amplitude active for all subsequent times.
