---
type: simulink-block
title: 'Parameter Smoother'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Signal Operations / Signal Operations'
documentation_page: 'parametersmoother'
documentation_source_path: 'ref/parametersmoother.html'
language: en
---

# Parameter Smoother

## Ports

### Input

### **P** — Input parameter to smooth scalar | vector | matrix

Specify the input parameters to smooth as a scalar, vector, or a matrix. If the
value of **Number of parameters** is greater than 1, then the block
labels the input ports as **P1**, **P2**, and so
on.

This port is unnamed until you select the **Specify smoothing factor from
input port** or **Specify smoothing time from input port**
parameters or you set **Number of parameters** to a value greater
than 1.

**Data Types:** `single` | `double`

### **alpha** — Smoothing factor scalar in the range [0, 1)

Specify the smoothing factor *α* as a scalar in the range [0, 1).
When *α* = 0, the block does not smooth the parameters. As
*α* approaches 1, smoothing and therefore the number of redesigns
increase. For more information on the effect of *α* on smoothing, see
Parameter Smoothing.

#### Dependencies

To enable this port:

- Set the **Smoothing mode** parameter to
  `Smoothing factor`.
- Select the **Specify smoothing factor from input port**
  parameter.

**Data Types:** `single` | `double`

### **tau** — Smoothing time nonnegative scalar

Specify the smoothing time *τ* in seconds as a nonnegative
scalar. This value indicates the time it takes for the parameter to change to
`exp`(−*T*/*τ*)×current value +
(1−`exp`(−*T*/*τ*))×target
value, where *T* is the value you specify in the **Sample
time (−1 for inherited)** parameter. For more information on the effect of
*τ* on smoothing, see Parameter Smoothing.

#### Dependencies

To enable this port:

- Set the **Smoothing mode** parameter to
  `Smoothing time`.
- Select the **Specify smoothing time from input port**
  parameter.

**Data Types:** `single` | `double`
### Output

### **Output** — Smoothed parameter scalar | vector | matrix

Smoothed value of the parameter, returned as a scalar, vector, or a matrix. This
is the instantaneous value of the parameter and it changes until the parameter reaches
the target value that you specify at the input port **P**.

**Data Types:** `single` | `double`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Number of parameters** — Number of input parameters `1` (default) | positive integer

Specify the number of parameters to smooth as a positive integer. The value of this
parameter determines the number of inputs ports on the block.

### **Smoothing mode** — Mode to use for smoothing `Smoothing factor` (default) | `Smoothing time`

Specify the mode to use for smoothing as one of these:

- `Smoothing factor` –– Specify the smoothing factor in
  the block dialog box or through the **alpha** port.
- `Smoothing time` –– Specify the smoothing time in the
  block dialog box or through the **tau** port.

For more information on these two modes, see Parameter Smoothing.

### **Specify smoothing factor from input port** — Option to specify smoothing factor from input port `off` (default) | `on`

Select this parameter to specify the smoothing factor from the input port
**alpha**. When you clear this parameter, you can specify the
smoothing factor in the block dialog box using the **Smoothing factor (between 0
and 1)** parameter.

#### Dependencies

- To enable this parameter, set the **Smoothing mode**
  parameter to `Smoothing factor`.

### **Smoothing factor (between 0 and 1)** — Smoothing factor `0.6` (default) | scalar in the range [0, 1)

Specify the smoothing factor *α* as a scalar in the range [0, 1).
When *α* = 0, the block does not smooth the parameters. As
*α* approaches 1, smoothing and therefore the number of redesigns
increase. For more information on the effect of *α* on smoothing, see
Parameter Smoothing.

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set the **Smoothing mode** parameter to
  `Smoothing factor`.
- Clear the **Specify smoothing factor from input port**
  parameter.

**Data Types:** `single` | `double`

### **Specify smoothing time from input port** — Option to specify smoothing time from input port `off` (default) | `on`

Select this parameter to specify the smoothing time from the input port
**tau**. When you clear this parameter, you can specify the smoothing
time in the block dialog box using the **Smoothing time constant
(seconds)** parameter.

#### Dependencies

- To enable this parameter, set the **Smoothing mode**
  parameter to `Smoothing time`.

### **Smoothing time constant (seconds)** — Smoothing time in seconds `10` (default) | nonnegative scalar

Specify the smoothing time *τ* in seconds as a nonnegative scalar.
This value indicates the time it takes for the parameter to change to
`exp`(−*T*/*τ*)×current value +
(1−`exp`(−*T*/*τ*))×target value,
where *T* is the value you specify in the **Sample time (−1 for
inherited)** parameter. For more information on the effect of
*τ* on smoothing, see Parameter Smoothing.

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set the **Smoothing mode** parameter to
  `Smoothing time`.
- Clear the **Specify smoothing time from input port**
  parameter.

**Data Types:** `single` | `double`

### **Sample time (−1 for inherited)** — Sample time of input parameters `-1` (default) | positive scalar

Specify the sample time of the input parameters *T* as
`-1` (for inherited) or a positive scalar in seconds. This value
determines the frequency with which the block updates the instantaneous values of the
input parameters until the target value is reached.

#### Dependencies

To enable this parameter, set the **Smoothing mode** parameter to
`Smoothing time`.

**Data Types:** `single` | `double`

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run. You can set this parameter to:

- `Interpreted execution` –– Simulate model using
  the MATLAB® interpreter. This option shortens startup time.
- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for
  subsequent simulations as long as the model does not change. This option
  requires additional startup time but provides faster subsequent
  simulations.

## Libraries

DSP System Toolbox / Signal Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

## Description

Smooth input parameters using exponential smoothing

The Parameter Smoother block gradually updates the input filter parameters
until the parameters reach the desired values. The block uses a first-order IIR filter to
smooth the parameter. For more information, see Parameter Smoothing.
