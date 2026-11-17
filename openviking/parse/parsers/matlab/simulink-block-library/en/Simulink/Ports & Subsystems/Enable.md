---
type: simulink-block
title: 'Enable'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Ports & Subsystems'
documentation_page: 'enable'
documentation_source_path: 'slref/enable.html'
language: en
---

# Enable

## Ports
```yaml
ports:
- name: Enable signal
  summary: External enable signal for a subsystem or model scalar
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    expression
```

### Output

### **Enable signal** — External enable signal for a subsystem or model scalar

Enable signal attached externally to the outside of an Enabled
Subsystem block and passed to the inside of the subsystem.
An enable signal port is added to an Enable block when
you select the **Show output port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `expression`
## Parameters
```yaml
parameters:
- name: States when enabling
  summary: Select block states when subsystem or model is disabled held (default) | reset
  group: ''
  block_parameter: StatesWhenEnabling
  type: character vector
  values: '''held'' | ''reset'''
  default: '''held'''
- name: Propagate sizes of variable-size signals
  summary: Select when to propagate a variable-size signal Only when enabling (default) | During execution
  group: ''
  block_parameter: PropagateVarSize
  type: character vector
  values: '''Only when enabling'' | ''During execution'''
  default: '''Only when enabling'''
- name: Show output port
  summary: Control display of output port for enable signal off (default) | on
  group: ''
  block_parameter: ShowOutputPort
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Enable zero-crossing detection
  summary: Control zero-crossing detection on (default) | off
  group: ''
  block_parameter: ZeroCross
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Port dimensions
  summary: Specify dimensions for the enable signal 1 (default) | [n] | [m n]
  group: ''
  block_parameter: PortDimensions
  type: character vector
  values: '''1'' | ''[n]'' | ''[m n]'''
  default: '''1'''
- name: Sample time
  summary: Specify time interval -1 (default) | Ts | [Ts, To]
  group: ''
  block_parameter: SampleTime
  type: character vector
  values: '''-1'' | ''Ts'' | ''[Ts, To]'''
  default: '''-1'''
- name: Minimum
  summary: Specify minimum output value for the enable signal [] (default) | real scalar
  group: ''
  block_parameter: OutMin
  type: character vector
  values: '''[]'' | real scalar in quotes'
  default: '''[]'''
- name: Maximum
  summary: Specify maximum output value for the enable signal [] (default) | real scalar
  group: ''
  block_parameter: OutMax
  type: character vector
  values: '''[]'' | real scalar in quotes'
  default: '''[]'''
- name: Data type
  summary: Specify output data type for the enable signal double (default) | single | int8 | uint8 | int16 | uint16 | int32
    | uint32 | int64 | uint64 | boolean | fixdt(1,16) | fixdt(1,16,0) | fixdt(1,16,2^,0) | <data type expression>
  group: ''
  block_parameter: OutDataTypeStr
  type: character vector
  values: '''double'' | ''single'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32'' | ''int64'' |
    ''uint64'' | ''boolean'' | ''<fixdt(1,16)'' | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)'' | ''<data type expression>'''
  default: '''double'''
- name: Mode
  summary: Select data type category Built in (default) | Fixed point | Expression
  group: ''
- name: Interpolate data
  summary: Specify value of missing workspace data on (default) | off
  group: ''
  block_parameter: Interpolate
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
```

### **States when enabling** — Select block states when subsystem or model is disabled `held` (default) | `reset`

When a Subsystem block or Model block is
disabled, select what happens to block states for the blocks within the
subsystem or model.

`held`
:   Hold block states at their previous values.

`reset`
:   Reset block states to their initial conditions (zero if not
    defined).

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `StatesWhenEnabling` |
| **Type:** character vector |
| **Values:** `'held'` | `'reset'` |
| **Default:** `'held'` |

### **Propagate sizes of variable-size signals** — Select when to propagate a variable-size signal `Only when enabling` (default) | `During execution`

Select when to propagate a variable-size signal.

`Only when enabling`
:   Propagate a variable-size signal when reenabling a
    Subsystem block or Model block
    containing an Enable port block. When you select
    this option, sample time must be periodic.

`During execution`
:   Propagate variable-size signals at each time step.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `PropagateVarSize` |
| **Type:** character vector |
| **Values:** `'Only when enabling'` | `'During execution'` |
| **Default:** `'Only when enabling'` |

### **Show output port** — Control display of output port for enable signal `off` (default) | `on`

The output port passes the enable signal attached externally to the
outside of an Enabled Subsystem block or enabled
Model block to the inside.

off
:   Remove the output port on the Enable port
    block.

on
:   Display an output port on the Enable port
    block. Selecting this option allows the subsystem or model to
    process the enable signal.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `ShowOutputPort` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Enable zero-crossing detection** — Control zero-crossing detection `on` (default) | `off`

Control zero-crossing detection for a model.

on
:   Detect zero crossings.

off
:   Do not detect zero crossings.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `ZeroCross` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Port dimensions** — Specify dimensions for the enable signal `1` (default) | `[n]` | `[m n]`

Specify dimensions for the enable signal attached externally to a
Model block and passed to the inside of the block.

`1`
:   Scalar signal.

`[n]`
:   Vector signal of width `n`.

`[m n]`
:   Matrix signal having `m` rows and
    `n` columns.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `PortDimensions` |
| **Type:** character vector |
| **Values:** `'1'` | `'[n]'` | `'[m n]'` |
| **Default:** `'1'` |

### **Sample time** — Specify time interval `-1` (default) | `Ts` | `[Ts, To]`

Specify time interval between block method execution. See Specify Sample Time.

`-1`
:   Sample time inherited from the model.

`Ts`
:   Scalar where Ts is the time interval.

`[Ts, To]`
:   Vector where Ts is the time interval and To is the initial
    time offset.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SampleTime` |
| **Type:** character vector |
| **Values:** `'-1'` | `'Ts'` | `'[Ts, To]'` |
| **Default:** `'-1'` |

### **Minimum** — Specify minimum output value for the enable signal `[]` (default) | real scalar

Specify minimum value for the enable signal attached externally to a
Model block and passed to the inside of the block.

Simulink® uses this value to perform:

- Simulation range checking. See Specify Signal Ranges.
- Automatic scaling of fixed-point data types.
- Optimization of generated code. This optimization can remove
  algorithmic code and affect the results of some simulation modes
  such as SIL or external mode. See Optimize using the specified minimum and maximum values (Embedded Coder).

`[]`
:   Unspecified minimum value.

real scalar
:   Real double scalar value.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OutMin` |
| **Type:** character vector |
| **Values:** `'[]'` | real scalar in quotes |
| **Default:** `'[]'` |

### **Maximum** — Specify maximum output value for the enable signal `[]` (default) | real scalar

Specify maximum value for the enable signal attached externally to a
Model block and passed to the inside of the block.

Simulink uses this value to perform:

- Simulation range checking. See Specify Signal Ranges.
- Automatic scaling of fixed-point data types.
- Optimization of generated code. This optimization can remove
  algorithmic code and affect the results of some simulation modes
  such as SIL or external mode. See Optimize using the specified minimum and maximum values (Embedded Coder).

`[]`
:   Unspecified maximum value.

real scalar
:   Real double scalar value.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OutMax` |
| **Type:** character vector |
| **Values:** `'[]'` | real scalar in quotes |
| **Default:** `'[]'` |

### **Data type** — Specify output data type for the enable signal `double` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^,0)` | `<data type expression>`

Specify data type for the enable signal attached externally to a
Model block and passed to the inside of the block.

`double`
:   Double-precision floating point.

`single`
:   Single-precision floating point.

`int8`
:   Signed 8-bit integer.

`uint8`
:   Unsigned 8-bit integer.

`int16`
:   Signed 16-bit integer.

`uint16`
:   Unsigned 16-bit integer.

`int32`
:   Signed 32-bit integer.

`uint32`
:   Unsigned 32-bit integer.

`int64`
:   Signed 64-bit integer.

`uint64`
:   Unsigned 64-bit integer.

`boolean`
:   Boolean with a value of `true` or
    `false`.

`fixdt(1,16)`
:   Signed 16-bit fixed point number with binary point
    undefined.

`fixdt(1,16,0)`
:   Signed 16-bit fixed point number with binary point set to
    zero.

`fixdt(1,16,2^,0)`
:   Signed 16-bit fixed point number with slope set to
    `2^0` and bias set to
    `0`.

`<data type expression>`
:   Data type object, for example
    `Simulink.NumericType`. You cannot enter
    the name of a `Simulink.Bus`
    object as a data type expression.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'<fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **Default:** `'double'` |

### **Mode** — Select data type category `Built in` (default) | `Fixed point` | `Expression`

Select data type category and display drop-down lists to help you define
the data type.

`Built in`
:   Display drop-down lists for data type and Data type
    override.

`Fixed point`
:   Display drop-down lists for Signedness, Scaling, and Data type
    override.

`Expression`
:   Display box for entering an expression.

#### Dependency

To enable this parameter, select the Show data type assistant
button.

#### Programmatic Use

No equivalent command-line parameter.

### **Interpolate data** — Specify value of missing workspace data `on` (default) | `off`

Specify value of missing workspace data when loading data from the
workspace.

on
:   Linearly Interpolate output at time steps for which no
    corresponding workspace data exists.

off
:   Do not interpolate output at time steps. The current output
    equals the output at the most recent time step for which data
    exists.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Interpolate` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |
## Libraries

Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

For more information, see HDL Code Generation in Enabled Subsystem.

**HDL Architecture**

This block has one default HDL architecture.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Add enable port to subsystem or model

The Enable block allows an external signal to control execution of a
subsystem or a model. To enable this functionality, add the block to a
Subsystem block or at the root level of a model that is referenced by a
Model block.

If you use an enable port at the root-level of a model:

- For multi-rate models, set the solver to single-tasking.
- For models with a fixed-step size, at least one block in the model must run at
  the specified fixed-step size rate.
