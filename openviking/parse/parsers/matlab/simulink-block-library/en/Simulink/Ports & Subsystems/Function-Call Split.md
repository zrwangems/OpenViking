---
type: simulink-block
title: 'Function-Call Split'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Ports & Subsystems'
documentation_page: 'functioncallsplit'
documentation_source_path: 'slref/functioncallsplit.html'
language: en
---

# Function-Call Split

## Ports
```yaml
ports:
- name: Function Call
  summary: Function-call line scalar
  direction: input
- name: Function Call
  summary: Function-call signal scalar
  direction: output
```

### Input

### **Function Call** — Function-call line scalar

A Function-Call Generator block, an
S-Function block, a Hit Crossing
block, or a Stateflow® chart can provide function-call events.
### Output

### **Function Call** — Function-call signal scalar

Function-call line connected to a function-call subsystem or
function-call model.
## Parameters
```yaml
parameters:
- name: Icon shape
  summary: Select block icon shape distinctive (default) | round
  group: ''
  block_parameter: IconShape
  type: character vector
  values: '''distinctive'' | ''round'''
  default: '''distinctive'''
- name: Number of output ports
  summary: Specify number of output ports 2 (default) | integer
  group: ''
  block_parameter: NumOutputPorts
  type: character vector
  values: '''2'' | ''<integer>'''
  default: '''2'''
- name: Output port layout
  summary: Select order of output ports default (default) | reverse
  group: ''
  block_parameter: OutputPortLayout
  type: character vector
  values: '''default'' | ''reverse'''
  default: '''default'''
```

### **Icon shape** — Select block icon shape `distinctive` (default) | `round`

Select block icon shape.

#### Settings

`distinctive`
:   Rectangular block icon.

`round`
:   Circular block icon.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IconShape` |
| **Type**: character vector |
| **Values**: `'distinctive'` | `'round'` |
| **Default**: `'distinctive'` |

### **Number of output ports** — Specify number of output ports `2` (default) | integer

Specify the number of function-call signal output ports.

#### Settings

`2`
:   Two function-call output ports.

integer
:   Integer number

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumOutputPorts` |
| **Type**: character vector |
| **Values**: `'2'` | `'<integer>'` |
| **Default**: `'2'` |

### **Output port layout** — Select order of output ports `default` (default) | `reverse`

Select the order of function-call output ports with respect to which port
provides a function-call first.

#### Settings

`default`
:   Top port provides function-call first.

`reverse`
:   Bottom port provides function-call first.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutputPortLayout` |
| **Type**: character vector |
| **Values**: `'default'` | `'reverse'` |
| **Default**: `'default'` |
## Libraries

Simulink / Ports & Subsystems

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2010a**

## Description

Provide junction for splitting function-call line

The Function-Call Split block allows a function-call line to branch and
connect to several function-call subsystems or function-call models.

The function-call subsystem or function-call model connected to the output port of the
Function-Call Split block that is marked with a dot executes before
the subsystems or models connected to other output ports. If data dependencies between
subsystems or models do not support the specified execution order, the
Function-Call Split block returns an error. To eliminate this error,
consider selecting the **Latch input for feedback signals of function-call
subsystem outputs** parameter on one or more Inport blocks
of the function-call subsystems or models involved in a data-dependency loop. Selecting
this option delays the corresponding function-call, thereby eliminating the
data-dependency loop.

To display the execution order of function-call subsystems connected to branches of a
given function-call signal, in the Simulink Editor, on the **Debug**
tab, select **Information Overlays** and click **Execution
Order**. A pane opens on the Simulink canvas that represents the
**Execution Order Block List**. In the list, the execution order of
the function-call subsystems is represented in the form
[`n`]←[`m`] `subsystem block
name`, where:

- `n` indicates the execution order of the
  subsystem.
- `m` indicates the execution order of the block that
  generates the function-call signal.
- `subsystem block name` indicates the name of the
  function-call subsystem.

The Function-Call Split block supports Signal Label Propagation.

The following model shows how to apply the **Latch input for feedback signals
of function-call subsystem outputs** parameter to work around a
data-dependency error caused by a Function-Call Split block. By turning
this parameter on in the `f1` subsystem's Inport block,
the Function-Call Split block ignores the data dependency of signal b.
The block breaks the loop of data dependencies between subsystems `f1`
and `g1`. The model achieves the behavior of consistently calling f1 to
execute before g1. For a given execution step, subsystem `f1` uses the
`g1` output computed at the previous execution step.
