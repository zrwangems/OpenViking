---
type: simulink-block
title: 'Function-Call Generator'
family: ports-and-subsystems
documentation_release: R2025b
official_category: 'Ports and Subsystems'
documentation_page: 'functioncallgenerator'
language: en
---

# Function-Call Generator

Provide function-call events to control execution of subsystem or model

## Libraries

Simulink / Ports & Subsystems

## Description

The Function-Call Generator block provides function-call events that
execute a function-call subsystem or function-call model at the rate you specify with
the **Sample time** parameter. A function-call subsystem or
function-call model is a subsystem or model containing a Trigger block
with its **Trigger type** parameter set to
`function-call`.

To iteratively execute each function-call subsystem or function-call model multiple
times at each time step, use the **Number of iterations**
parameter.

To execute multiple function-call subsystems or function-call models in a specified
order, use the Function-Call Generator block with a Function-Call
Split block. For an example, see Function-Call Split.

To execute a function-call subsystem or function-call model intermittently, meaning
not at every time step, select the **Show enable port** parameter. You
can then use the input at the enable port to control when the block outputs
function-call events. In effect, you can turn the block on and off as needed.

**Note**

Starting in R2025a, the Function-Call Generator block no longer
behaves as a masked, linked block. To locate this block in a model programmatically,
use the command `find_system('BlockType','FunctionCallGenerator')`.
When you update from another release to R2025a, it is recommended that you fix any
Function-Call Generator block whose link to a Simulink® library is broken. Otherwise, the block will not be updated, and it
will continue to behave as a masked block in the updated model. The mask behavior of
this block will be removed in a future release. For more information about
identifying broken library links in a model, see Display Library Links.

For versions prior to R2025a, to locate this block in a model programmatically,
use the command `find_system('MaskType','Function-Call
Generator')`.

## Ports

### Input

### **Enable** — Control signal input scalar

The block outputs function-call events only when the input at this
port is a positive number.

#### Dependencies

To enable this port, select the **Show enable
port** check box.
### Output

### **Function Call** — Function-call event output scalar | vector

Sends function-call events to the function-call input port of a
function-call subsystem or function-call model.

## Parameters

### **Sample time** — Specify time interval `1` (default) | scalar | vector | `-1`

Specify the time interval between function-call events to a function-call
subsystem or function-call model. If the actual calling rate for the
subsystem or model differs from the time interval this parameter specifies,
Simulink displays an error.

By default, the block uses a time interval of `1`. To set
a different interval, enter a valid sample time based on the table in Types of Sample Time, or
specify `-1` to inherit the time interval from the
model.

#### Dependencies

To enable this parameter, clear the **Show enable
port** check box. If you select **Show enable
port**, sample time is automatically set to
`-1` (inherited).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `sample_time` |
| **Type**: character vector |
| **Values**: `'1'` | scalar expression | vector expression | `'-1'` |
| **Default**: `'1'` |

### **Number of iterations** — Specify number of times to provide a function-call at each time step `1` (default) | integer

The value of this parameter can be a vector, where each element of the
vector specifies a number of times to execute a function-call subsystem or
model. If a vector is specified, then the block outputs a vector of
function-call events, which can be split into individual function-call
events using a Demux block and used to drive
multiple function-call subsystems or models.

Suppose that you specify **Number of iterations** to be
`[3 2]` and connect the output of this block to a
Demux block, which is connected to the control ports of
two function-call subsystems. In this case, the first function-call
subsystem executes three times at each time step, and the second
function-call subsystem executes two times at each time step.

If, however, you connect the output of this block to a single
function-call subsystem or model, the total number of times that the
function-call subsystem or model executes per time step is equal to the sum
of the vector element values. So in the example above, specifying
**Number of iterations** to be `[3 2]`
and connecting the output of this block to a single function-call subsystem
results in the function-call subsystem executing five times at each time
step.

#### Settings

`1`
:   Provide function-call once during each time step.

integer
:   Signed or unsigned integer number. Provide the specified
    number of function calls at each time step.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `numberOfIterations` |
| **Type**: character vector |
| **Values**: `'1'` | integer in quotes | vector of integers in quotes |
| **Default**: `'1'` |

### **Disallow wide output** — Prevent implicit expansion of output signal `off` (default) | `on`

Unless this parameter is
selected,
the output of this block is expanded into a vector, if necessary, to drive
the blocks to which it is connected. For example, if **Number of
iterations** is set to `2` and
**Disallow wide output** is not selected, and the
output of this block is connected to a Demux block, which is
in turn connected to three separate function-call subsystems, then each
function-call subsystem receives two function-call events at each time step.
A similar result occurs if the output of this block is connected to a
Stateflow® chart with multiple events. If **Disallow wide
output** is selected in these situations, the software produces
an error.

Select this parameter to prevent implicit expansion of the output
signal.

Clear this parameter to allow implicit expansion of the output signal when
appropriate.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DisallowWideOutput` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Show enable port** — Add input port for control signal `off` (default) | `on`

Select this parameter to add a control signal input port to the block. The
block outputs function-call events only when the value at the control signal
input port is a positive number.

Clear this parameter to remove the control signal input port. The block
outputs function-call events at every time step.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ShowEnablePort` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** |  |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

### R2025a: Function-Call Generator block no longer behaves as linked, masked block

The Function-Call Generator block now behaves as a built-in block.
For versions prior to R2025a, the block behaves as a masked, linked block. This
change in block behavior enables the block to execute faster during
simulation.
