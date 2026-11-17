---
type: simulink-block
title: 'Moving Minimum'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'movingminimum'
documentation_source_path: 'ref/movingminimum.html'
language: en
---

# Moving Minimum

## Ports
```yaml
ports:
- name: Port_1
  summary: Data input column vector | row vector | matrix
  direction: input
  data_types: single | double
- name: Port_1
  summary: Moving minimum output column vector | row vector | matrix
  direction: output
  data_types: single | double
```

### Input

### **Port\_1** — Data input column vector | row vector | matrix

Data over which the moving minimum is determined using the sliding
window method. The block accepts real-valued or complex-valued
multichannel inputs, that is,
*m*-by-*n* size inputs, where
*m* ≥ 1 and *n* ≥ 1. The block
also accepts variable-size inputs. During simulation, you can change the
size of each input channel. However, the number of channels cannot
change.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Moving minimum output column vector | row vector | matrix

Moving minimum output, determined using the sliding window method. The
size of the output matches the size of the input. The window slides
column-wise along each channel, and the block determines the minimum of
the data in the window. For more details, see Algorithms.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Specify window length
  summary: Flag to specify window length on (default) | off
  group: ''
- name: Window length
  summary: Length of the sliding window 4 (default) | positive scalar integer
  group: ''
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code generation
  group: ''
```

### **Specify window length** — Flag to specify window length on (default) | off

When you select this check box, the length of the sliding window is equal
to the value you specify through the **Window length**
parameter. When you clear this check box, the length of the sliding window
is infinite. In this mode, the block determines the minimum of the current
sample and all the previous samples in the channel.

### **Window length** — Length of the sliding window 4 (default) | positive scalar integer

**Window length** specifies the length of the sliding
window in samples.

#### Dependencies

This parameter appears when you select the **Specify window
length** check box.

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

DSP System Toolbox / Statistics

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

### R2024a: Change in the default value of **Simulate using** parameter

The default value of the **Simulate using** parameter is now
`Interpreted execution`. With this change, the block uses the
MATLAB interpreter for simulation by default.

## Description

Moving minimum

The Moving Minimum block determines the moving minimum of the input
signal along each channel independently over time. The block uses the sliding window
method to determine the moving minimum. In this method, a window of specified length
moves over each channel sample by sample, and the block determines the minimum over the
data in the window. For more details, see Algorithms.
