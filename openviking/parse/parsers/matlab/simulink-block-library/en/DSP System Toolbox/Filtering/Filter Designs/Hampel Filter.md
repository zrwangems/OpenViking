---
type: simulink-block
title: 'Hampel Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Designs'
documentation_page: 'hampelfilter'
documentation_source_path: 'ref/hampelfilter.html'
language: en
---

# Hampel Filter

## Ports

### Input

### **x** — Data input vector | matrix

The block accepts multichannel inputs, that is,
*m*-by-*n* size inputs, where
*m* ≥ 1, and *n* ≥ 1.
*m* is the number of samples in each frame
(channel), and *n* is the number of channels. The block
also accepts variable-size inputs. That is, you can change the size of
each input channel during simulation. However, the number of channels
cannot change.

This port is unnamed until you select the **Specify threshold
from input port** parameter.

**Data Types:** `single` | `double`

### **T** — Threshold real scalar greater than or equal to 0

Threshold for outlier detection, specified as a real scalar greater
than or equal to 0. For information on how this parameter is used to
detect the outlier, see Algorithms.

#### Dependencies

This port appears when you select the **Specify threshold
from input port** parameter.

**Data Types:** `single` | `double`
### Output

### **y** — Filtered output vector | matrix

The size and data type of this output matches the size and data type
of the input.

This port is unnamed until you select the **Output outlier
status** check box.

**Data Types:** `single` | `double`

### **outlier** — Output the outlier status vector | matrix

A value of `1` in this output indicates that the
corresponding element in the input is an outlier. This output has the
same size as the input.

#### Dependencies

To enable this port, select the **Output outlier
status** check box.

**Data Types:** `Boolean`

## Parameters

If a parameter is listed as tunable, then you can change its value during
simulation.

### **Window length** — Length of sliding window `11` (default) | positive odd scalar integer

Length of the sliding window, specified as a positive odd scalar integer.
The window of finite length slides over the data, and the block computes the
median and median absolute deviation of the data in the window.

### **Specify threshold from input port** — Flag to specify threshold off (default) | on

When you select this check box, the threshold is input through the
**T** port. When you clear this check box, the
threshold is specified on the block dialog through the **Threshold
for outlier detection (standard deviations)** parameter.

### **Threshold for outlier detection (standard deviations)** — Threshold 3 (default) | real scalar greater than or equal to 0

Threshold for outlier detection, specified as a real scalar greater than
or equal to 0. For information on how this parameter is used to detect the
outlier, see Algorithms.

**Tunable:** Yes

#### Dependencies

This parameter appears when you clear the **Specify threshold
from input port** check box.

### **Output outlier status** — Flag to output the outlier status off (default) | on

Select this parameter to output a matrix of `boolean`
values that has the same size as the input. Each element in this matrix
indicates whether the corresponding element in the input is an outlier. A
value of `1` indicates an outlier.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run. You can set this parameter to:

- `Interpreted execution` –– Simulate model using
  the MATLAB® interpreter. This option shortens startup time.
- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for
  subsequent simulations as long as the model does not change. This option
  requires additional startup time but provides faster subsequent
  simulations.

## Libraries

DSP System Toolbox / Filtering / Filter Designs

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Filter outliers using Hampel identifier

The Hampel Filter block detects and removes the outliers of the input
signal by using the Hampel identifier. The Hampel identifier is a variation of the
three-sigma rule of statistics, which is robust against outliers. For each sample of the
input signal, the block computes the median of a window composed of the current sample
and Len−12 adjacent samples on each side of the current sample.
*Len* is the window length you specify through the **Window
length** parameter. The block also estimates the standard deviation of each
sample about its window median by using the median absolute deviation. If a sample
differs from the median by more than the threshold multiplied by the standard deviation,
the filter replaces the sample with the median. For more information, see Algorithms.
