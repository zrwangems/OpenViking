---
type: simulink-block
title: 'Clock'
family: 'simulink-extras'
product_id: 'simulink-extras'
product_name: 'Simulink Extras'
documentation_release: R2025b
official_category: 'Flip Flops'
documentation_page: 'clock'
documentation_source_path: '../simulink/slref/clock.html'
language: en
---

# Clock

## Ports
```yaml
ports:
- name: Port_1
  summary: Sample time scalar
  direction: output
  data_types: double
```

### Output

### **Port\_1** — Sample time scalar

Sample time, specified as the current simulation time at each
simulation time step.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Display time
  summary: Display simulation time on block icon off (default) | on
  group: ''
  block_parameter: DisplayTime
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Decimation
  summary: Interval at which to update block icon 10 (default) | positive integer
  group: ''
  block_parameter: Decimation
  type: character vector
  values: scalar
  default: '''10'''
```

### **Display time** — Display simulation time on block icon `off` (default) | `on`

Select this check box to display the simulation time as part of the Clock
block icon. When you clear this check box, the simulation time does not
appear on the block icon.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DisplayTime` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Decimation** — Interval at which to update block icon `10` (default) | positive integer

Specify the interval at which Simulink® updates the Clock icon as a positive integer.

Suppose that the decimation is 1000. For a fixed integration step of 1
millisecond, the Clock icon updates at 1 second, 2 seconds, and so
on.

#### Dependencies

To display the simulation time on the block icon, you must select the
**Display time** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Decimation` |
| **Type:** character vector |
| **Value:** scalar |
| **Default:** `'10'` |
## Libraries

Simulink / Sources

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

Not recommended for production code. Relates to resource limits and restrictions on speed
and memory often found in embedded systems. Generated code can contain dynamic
allocation and freeing of memory, recursion, additional memory overhead, and
widely-varying execution times. While the code is functionally valid and generally
acceptable in resource-rich environments, smaller embedded targets often cannot
support such code. Usually, blocks evolve toward being suitable for production code.
Thus, blocks suitable for production code remain suitable.

## Version History

**Introduced before R2006a**

## Description

Display and provide simulation time

The Clock block outputs the current simulation time at each simulation step.
This block is useful for other blocks that need the simulation time.

When you need the current time within a discrete system, use the Digital Clock block.
