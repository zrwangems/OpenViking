---
type: simulink-block
title: 'DRMS'
family: 'sldo'
product_id: 'sldo'
product_name: 'Simulink Design Optimization'
documentation_release: R2025b
official_category: 'RMS Blocks'
documentation_page: 'drms'
documentation_source_path: 'ref/drms.html'
language: en
---

# DRMS

## Ports

### Input

### **Port\_1** — Input signal scalar

Input value, specified as a scalar signal.
### Output

### **Port\_1** — DRMS value scalar

Computed discrete-time, root mean square value, output as a scalar signal.

## Parameters

### **Sampling interval** — Sample time `1` (default) | positive scalar

Sample time for computing DRMS value.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `Ts` |
| **Value:** positive scalar in quotes |
| **Default:** `'1'` |

## Libraries

Simulink Design Optimization / RMS Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2009a**

## Description

Compute discrete-time, cumulative root mean square (DRMS) of signal

Attach the DRMS block to a signal to compute its discrete-time, cumulative
root mean square (DRMS) value, which provides a measure of the average energy in a signal.

The discrete-time, cumulative root mean square value of a signal
*u*(*t*) is defined as

DRMS=1N∑i=1N‖u(ti)‖2

To optimize the signal energy, use this block in conjunction with the Check Custom
Bounds block.
