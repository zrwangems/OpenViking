---
type: simulink-block
title: 'Discrete Varying Delay'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Dynamic System Models / Linear System Representation / LPV and LTV Models / Discrete-Time Varying Systems'
documentation_page: 'discretevaryingdelay'
documentation_source_path: 'ref/discretevaryingdelay.html'
language: en
---

# Discrete Varying Delay

## Ports

### Input

### **u** — Data input signal scalar | vector

Input data signal delayed according to parameters settings.

This port has direct feedthrough when you specify a signal delay as fixed using
the **Fixed delays (indices)** parameter and specify a value
`0` for the **Nominal delay** parameter.

### **d** — Delay length scalar | vector

Instantaneous delay length input specified as a scalar or vector. This value is
used to specify the varying delay. The block treats any negative input values as
zero.

When the delay length input is a noninteger value, the block rounds the value to
the nearest integer.
### Output

### **Port\_1** — Output signal scalar | vector

Output signal specified as a scalar or vector.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Nominal delay (number of samples)** — Nominal value of delay 1 (default) | nonnegative integer | vector of nonnegative integer values

Specify the nominal value of delays as the number of samples.

### **Maximum delay** — Maximum value of delay length input `10` (default) | nonnegative integer | vector of nonnegative integer values

Set the maximum value of the time delay input. This value defines the largest delay
length input that this block allows. The block clips any delay that exceeds this
value.

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

### **Sample time (-1 for inherited)** — Sample time `-1` (default) | positive scalar

Specify the time interval between samples. To inherit the sample time, set this
parameter to `-1`. This block supports discrete sample time, but not
continuous sample time.

### **Prevent direct feedthrough with minimum delay of 1** — Prevent direct feedthrough `off` (default) | `on`

Select to increase the minimum delay length from zero to 1.

Selecting this check box prevents direct feedthrough from the input port,
**u**, to the output port.

## Libraries

Control System Toolbox / Linear Parameter Varying

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

## Description

Discrete varying delay with support for fixed delay and zero delay (direct feedthrough)

The Discrete Varying Delay block extends the functionality of the Variable Integer Delay (Simulink) block in the `Simulink` /
`Discrete` library by providing additional support for specifying fixed and
zero delays. This block is helpful when you want to model a mix of zero, fixed, and varying
delays, which can occur in LPV models.
