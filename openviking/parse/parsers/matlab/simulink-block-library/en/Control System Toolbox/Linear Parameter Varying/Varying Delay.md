---
type: simulink-block
title: 'Varying Delay'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Linear Parameter Varying'
documentation_page: 'varyingdelay'
documentation_source_path: 'ref/varyingdelay.html'
language: en
---

# Varying Delay

## Ports

### Input

### **Port\_1** — Input signal scalar | vector

Input signal specified as a scalar or vector.

This port has direct feedthrough when you specify a signal delay as fixed using
the **Fixed delays (indices)** parameter and specify a value
`0` for the **Nominal delay** parameter.

**Data Types:** `double`

### **Port\_2** — Instantaneous time delay input scalar | vector

Instantaneous time delay input specified as a scalar or vector. This value is used
to specify the varying delay. The block treats any negative input values as
zero.

#### Dependencies

To enable this port, specify at least one index as varying, that is, the
**Fixed delays (indices)** parameter must not specify all
channels as fixed.

**Data Types:** `double`
### Output

### **Port\_1** — Delayed signal scalar | vector

Output signal specified as a scalar or vector.

**Data Types:** `double`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Nominal delay** — Nominal value of delay 1 (default) | positive scalar | vector of positive values

Specify the nominal value of delays in each input channel.

### **Maximum delay** — Maximum value of time delay input `10` (default) | nonnegative scalar | vector of nonnegative values

Set the maximum value of the time delay input. This value defines the largest time
delay input that this block allows. The block clips any delay that exceeds this
value.

### **Minimum delay** — Minimum value of time delay input `0` (default) | nonnegative scalar | vector of nonnegative values

Set the minimum value of the time delay input. This value defines the smallest time
delay input that this block allows. The block maintains this value for any delay that is
less than this value.

### **Fixed delays (indices)** — Signal indices with fixed delays `[]` (default) | positive scalar | vector of positive values

Specify the indices of the input signal channels where the delays are fixed. For
example, if you have a 4-by-1 input signal and you want to specify fixed delay in the
first and fourth channel, use a value `[1 4]` for this parameter. The
block uses the value specified at the corresponding index of the **Nominal
delay** parameter.

When you list all channels as fixed, the block disables the second input port
**Port\_2**.

### **Initial output** — Initial output `0` (default) | scalar | vector

For each input channel, specify the output value until the simulation time first
exceeds the time delay for the channel.

### **Initial buffer size** — Initial memory allocation `1024` (default) | scalar

Define the initial memory allocation for the number of input points to store. The
input points define the history of the input signal up to the current simulation
time.

- If the number of input points exceeds the initial buffer size, the block
  allocates additional memory.
- After simulation ends, a message displays if the buffer is not sufficient and
  more memory must be allocated.

#### Tips

- Because allocating memory slows down simulation, choose this value carefully
  if simulation speed is an issue.
- For long time delays, this block might use a large amount of memory,
  particularly for dimensionalized input.

### **Use fixed buffer size** — Use fixed-size buffer `off` (default) | `on`

Selecting this check box uses a fixed-size buffer to save input data from previous
time steps. When you clear this check box, the block does not use a fixed-size
buffer.

The **Initial buffer size** parameter specifies the buffer size. If
the buffer is full, new data replaces data already in the buffer. The software uses
linear extrapolation to estimate output values that are not in the buffer.

**Note**

ERT or GRT code generation uses a fixed-size buffer even if you do not select this
check box.

#### Tips

- If the input data is linear, selecting this check box can save memory.
- If the input data is nonlinear, do not select this check box. Doing so might
  yield inaccurate results.

### **Pade order (for linearization)** — Order of Pade approximation `0` (default) | positive integer | vector

Set the order of the Pade approximation for linearization routines.

- The default value is `0`, which results in a unity gain with no
  dynamic states.
- Setting the order to a positive integer `n` adds
  `n` states to your model, but results in a more accurate linear
  model of the delay.

Use a vector of positive integers to specify a different order for each input
channel.

## Libraries

Control System Toolbox / Linear Parameter Varying

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

## Description

Varying delay with support for fixed delay and zero delay (direct feedthrough)

The Varying Delay block extends the functionality of the Variable Transport Delay (Simulink) block in the `Simulink` /
`Continuous` library by providing additional support for specifying fixed
and zero delays. This block is helpful when you want to model a mix of zero, fixed, and
varying delays, which can occur in LPV models.
