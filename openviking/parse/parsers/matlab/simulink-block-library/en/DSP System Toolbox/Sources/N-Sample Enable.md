---
type: simulink-block
title: 'N-Sample Enable'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Management / Switches and Counters'
documentation_page: 'nsampleenable'
documentation_source_path: 'ref/nsampleenable.html'
language: en
---

# N-Sample Enable

## Ports
```yaml
ports:
- name: Rst
  summary: Reset signal scalar
  direction: input
  data_types: Boolean
- name: Port_1
  summary: Output signal scalar
  direction: output
  data_types: Boolean
```

### Input

### **Rst** — Reset signal scalar

Reset input signal, specified as a scalar. At any time during the
count, a trigger event at the input port resets the counter to its
initial state.

**Tip**

The N-Sample Enable block supports triggered
subsystems when you select the **Reset input**
check box to enable the **Rst** input port.

#### Dependencies

To enable this input port, select the **Reset
input** check box.

**Data Types:** `Boolean`
### Output

### **Port\_1** — Output signal scalar

Scalar output containing the inactive value (`0` or
`1`, whichever is not selected in the
**Active level** parameter) during the first
*N* sample times, where *N* is the
**Trigger count** value. Beginning with output
sample *N*+1, the block outputs the active value
(`1` or `0`, whichever you select
in the **Active level** parameter) until a reset event
occurs or the simulation terminates.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Trigger count, N
  summary: Number of samples to output the active value 8 (default) | scalar integer
  group: ''
- name: Active level
  summary: Active level Low (0) (default) | High (1)
  group: ''
- name: Reset input
  summary: Enable reset input port off (default) | on
  group: ''
- name: Trigger type
  summary: Type of triggering event Rising edge (default) | Falling edge | Either edge | Non-zero sample
  group: ''
- name: Sample time
  summary: Output sample period 1 (default) | positive scalar
  group: ''
- name: Output data type
  summary: Output data type Logical (default) | Boolean
  group: ''
```

### **Trigger count, N** — Number of samples to output the active value `8` (default) | scalar integer

Specify the number of samples for which the block outputs the active value
as a scalar integer, greater than or equal to zero.

**Tunable:** Yes

### **Active level** — Active level `Low (0)` (default) | `High (1)`

Specify the value to output after the first *N* sample
times as `0` or `1`.

**Tunable:** Yes

### **Reset input** — Enable reset input port `off` (default) | `on`

To enable the reset (**Rst**) input port, select this
check box. When you clear this check box, the **Rst** input
port is disabled.

**Tip**

When you select the **Reset input** check box, the
N-Sample Enable block supports triggered
subsystems.

### **Trigger type** — Type of triggering event `Rising edge` (default) | `Falling edge` | `Either edge` | `Non-zero sample`

Select type of event that triggers a reset when the
**Rst** port is enabled.

You can specify the triggering event as:

- `Rising edge` — Triggers a reset
  operation when the `Rst` input does one of the
  following:

  - Rises from a negative value to a positive value or
    zero
  - Rises from zero to a positive value, where the rise is not
    a continuation of a rise from a negative value to zero (see
    the following figure)
- `Falling edge` — Triggers a reset
  operation when the **Rst** input does one of the
  following:

  - Falls from a positive value to a negative value or
    zero
  - Falls from zero to a negative value, where the fall is not
    a continuation of a fall from a positive value to zero (see
    the following figure)
- `Either edge` — Triggers a reset
  operation when the **Rst** input is a
  `Rising edge` or `Falling
  edge`.
- `Non-zero sample` — Triggers a reset
  operation at each sample time that the **Rst**
  input is not zero.

#### Dependencies

To enable this parameter, select the **Reset input**
check box.

### **Sample time** — Output sample period `1` (default) | positive scalar

Specify the sample period, Ts, for the block's
counter as a positive finite scalar. The block switches from the active
value to the inactive value at
*t*`=`Ts(*N*+1).

### **Output data type** — Output data type `Logical` (default) | `Boolean`

Specify the output data type as `Logical` or
`Boolean`.
## Libraries

DSP System Toolbox / Sources DSP System Toolbox / Signal Management / Switches and Counters

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Output ones or zeros for specified number of sample times

The N-Sample Enable block outputs the inactive value
(`0` or `1`, whichever is not selected in the
**Active level** parameter) during the first *N*
sample times, where *N* is the **Trigger count**
value. Beginning with output sample *N*+1, the block outputs the active
value (`1` or `0`, whichever you select in the
**Active level** parameter) until a reset event occurs or the
simulation terminates.

The output of the block is always a scalar.

The **Reset input** check box enables the **Rst**
input port. At any time during the count, a trigger event at the input port resets the
counter to its initial state. You specify the type of trigger event using the
**Trigger type** parameter. This block supports triggered
subsystems when you select the **Reset input** check box.
