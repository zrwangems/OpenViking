---
type: simulink-block
title: 'Median Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Designs'
documentation_page: 'medianfilter'
documentation_source_path: 'ref/medianfilter.html'
language: en
---

# Median Filter

## Ports

### Input

### **Port\_1** — Data input column vector | row vector | matrix

Data over which the block computes moving median. The block accepts
real-valued or complex-valued multichannel inputs, that is,
*m*-by-*n* size inputs, where
*m* ≥ 1, and *n* ≥ 1. The block
also accepts variable-size inputs. During simulation, you can change the
size of each input channel. However, the number of channels cannot
change.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Moving median output column vector | row vector | matrix

The size of the moving median output matches the size of the input.
The block uses the sliding window method to compute the moving median.
For more details, see Algorithms.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

## Parameters

### **Window length** — Length of the sliding window 5 (default) | positive scalar integer

**Window length** specifies the length of the sliding
window in samples.

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

DSP System Toolbox / Filtering / Filter Designs DSP System Toolbox / Statistics

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `No` |
| **Variable-Size Signals** | `Yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

### R2024a: Change in the default value of **Simulate using** parameter

The default value of the **Simulate using** parameter is now
`Interpreted execution`. With this change, the block uses the
MATLAB interpreter for simulation by default.

## Description

Median filter

The Median Filter block computes the moving median of the input signal
along each channel independently over time. The block uses the sliding window method to
compute the moving median. In this method, a window of specified length moves over each
channel sample by sample, and the block computes the median of the data in the window.
This block performs median filtering on the input data over time. For more details, see
Algorithms.
