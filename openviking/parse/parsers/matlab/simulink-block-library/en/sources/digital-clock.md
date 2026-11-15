---
type: simulink-block
title: 'Digital Clock'
family: sources
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'digitalclock'
language: en
---

# Digital Clock

## Ports

### Output

### **Port\_1** — Sample time scalar

Sample time, in seconds, at the specified sampling interval. At other times, the block
holds the output at the previous value.

**Data Types:** `double`

## Parameters

### **Sample time** — Sampling interval `1` (default) | scalar | vector

Specify the sampling interval in seconds. You can specify the sampling interval in one of
two ways:

- As the period, specified as a real-valued scalar with data type
  double.
- As the period and offset, specified as a real-valued vector of
  length 2 with data type double. The period and offset must be finite
  and non-negative, and the offset value must be less than the
  period.

For more information, see Specifying Sample Time.

**Tip**

Do not specify a continuous sample time, either `0`
or `[0,0]`. Also, avoid specifying
`-1` (inheriting the sample time) because this
block is a source.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'1'` |

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

Output simulation time at specified sampling interval

The Digital Clock block outputs the simulation time only at the specified
sampling interval. At other times, the block holds the output at the previous value. To
control the precision of this block, use the **Sample time** parameter
in the block dialog box.

Use this block rather than the Clock block, which outputs continuous
time, when you need the current simulation time within a discrete system.
