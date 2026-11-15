---
type: simulink-block
title: 'Manual Switch'
family: signal-routing
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'manualswitch'
---

# Manual Switch

Switch between two inputs

## Libraries

Simulink / Signal Routing

## Description

The Manual Switch block is a toggle switch that selects one of its two
inputs to pass through to the output. To toggle between inputs, double-click the block.
You control the signal flow by setting the switch before you start the simulation or by
changing the switch while the simulation is executing. The Manual Switch
block retains its current state when you save the model.

To programmatically toggle the switch, set the `set_param`
`sw` property to `'0'` or `'1'`. For
example, to connect the second input to the output:

```
set_param(gcb,'sw','0')
```

To connect the first input to the output:

```
set_param(gcb,'sw','1')
```

**Note**

Double-clicking the Manual Switch block does not open the block
dialog box. Instead, it toggles the input choice.

## Ports

### Input

### **Port\_1** — First input signal scalar | vector

First of two inputs to the Manual Switch block. The block propagates the
selected input to the output. To select the input signal, toggle the
switch by double-clicking the block.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Port\_2** — Second input signal scalar | vector

Second of two inputs to the Manual Switch block. The block propagates the
selected input to the output. To select the input signal, toggle the
switch by double-clicking the block.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Port\_1** — Output signal scalar | vector

Output signal propagated from either the first or second input signal.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

To view the block parameters, right-click the block and select `Block Parameters
(ManualSwitch)`.

### **Allow the two inputs to differ in size (Results in variable-size output signal)** — Allow inputs of different sizes `off` (default) | `on`

Select this check box to allow inputs with different sizes and propagate the selected
input signal size to the output signal. If you clear the box, the block
expands scalar inputs to have the same dimensions as nonscalar inputs. See
Scalar Expansion of Inputs and Parameters.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `varsize` |
| **Type:** character vector |
| **Value:** `'on'` | `'off'` |
| **Default:** `'off'` |

### **Sample time (-1 for inherited)** — Interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples. To inherit the sample time, set this
parameter to `-1`. For more information, see Specify Sample Time.

#### Dependencies

This parameter is visible only if you set it to a value other than
`-1`. To learn more, see Blocks for Which Sample Time Is Not Recommended.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | scalar or vector in quotes |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
