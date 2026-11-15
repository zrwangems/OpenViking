---
type: simulink-block
title: 'Find Delay'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Signal Operations'
documentation_page: 'finddelay'
documentation_source_path: 'ref/finddelay.html'
language: en
---

# Find Delay

## Ports

### Input

### **sRef** — Reference signal vector | matrix

Original reference signal, specified as a vector or matrix. Dimensions
and sample times of **sRef** and **sDel** must match.

**Data Types:** `double`

### **sDel** — Delayed signal vector | matrix

Delayed or distorted version of reference signal, specified as a
vector or matrix. Dimensions and sample times of **sRef** and **sDel** must match.

**Data Types:** `double`
### Output

### **delay** — Delay output scalar | vector

Delay output, returned as a scalar or vector indicating number of
signal samples of delay between the **sRef** and **sDel** inputs.

For a matrix input, the output is a row vector, and finds the delay in
each channel of the input matrix independently

The delay output is a nonnegative integer less than the **Correlation window length (samples)** parameter
value.

**Data Types:** `double`

### **chg** — Delay flag `0` | `1`

Delay flag, returned as `0` or `1`.
The **chg** port outputs `1` when there is a
change from the delay computed at the previous sample, and
`0` when there is no change.

#### Dependencies

To enable this port, select the **Include "change signal" output port**
parameter.

**Data Types:** `Boolean`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Correlation window length (samples)** — Number of samples `200` (default) | positive integer

The number of samples the block uses to calculate the cross-correlations
of the two signals. Increasing the correlation window length increases the
reliability of the computed delay but also increases the processing time to
compute the delay.

### **Include "change signal" output port** — Add chg port to block `off` (default) | `on`

Select this parameter to add the **chg**
output port. The **chg** port outputs `1` when
there is a change from the delay computed at the previous sample, and
`0` when there is no change.

### **Disable recurring updates** — Select to set stop criteria for delay computation `off` (default) | `on`

Select to set stop criteria for delay computation. When selected, the
block stops updating delay after the same delay value is computed the number
of times specified by the **Number of
constant delay outputs to disable updates** parameter.

### **Number of constant delay outputs to disable updates** — Disable updates after this number of unchanging delay value computations `3` (default) | positive integer

Disable updates after this number of unchanging delay value computations,
specified as a positive integer. The value of this parameter indicates how
many times the block must compute the same delay before stopping
updates.

#### Dependencies

To enable this parameter, select the **Disable recurring updates** parameter.

## Libraries

Communications Toolbox / Utility Blocks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `enumerated` | `integera` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
|  |  |
| --- | --- |
| a Signed integers only. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Find delay between two signals

The Find Delay block finds the delay between a signal and a delayed,
and possibly distorted, version of itself. This is useful when you want to compare a
transmitted and received signal to find the bit error rate, but do not know the delay in
the received signal. This block accepts a column vector or matrix input signal. For a
matrix input, the block outputs a row vector, and finds the delay in each channel of the
matrix independently. For more information about signal delays, see Delays in Communication Systems.

This icon shows the block with the optional **chg** port. Find Delay block showing the optional 'chg' port.
