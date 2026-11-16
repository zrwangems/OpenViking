---
type: simulink-block
title: 'AGC'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Impairments Correction'
documentation_page: 'agc'
documentation_source_path: 'ref/agc.html'
language: en
---

# AGC

## Ports

### Input

### **In** — Input signal column vector

Input signal, specified as a column vector. This port is unnamed on
the block mask.

**Data Types:** `single` | `double` | `int` | `uint`
**Complex Number Support:** Yes
### Output

### **y** — Output signal *N*S-element column vector

Output signal, returned as an
*N*S-element column vector.
*N*S is the length of the
input signal. The output signal is the same data type as the input
signal.

### **Px** — Power level estimate *N*S-element column vector

Power level estimate, returned as an
*N*S-element column vector.
*N*S is the length of the
input signal. You can use `powerlevel` as an energy
detector output.

#### Dependencies

To enable this port, select the **Enable output of estimated input power**
parameter.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Step size for gain updates** — Step size for gain updates `0.01` | positive scalar

Step size for gain updates, specified as a positive scalar. Increasing the
step size enables the AGC to respond more quickly to changes in the input
signal level but increases variation in the output signal level after
reaching steady-state operation. For more information, see AGC Performance Criteria.

### **Target output power level** — Target output power level (W) `1` | positive scalar

Target output power level, specified as a positive scalar. The power level
is measured in watts referenced to 1 ohm.

### **Length of averaging window** — Length of averaging window (samples) `100` | positive integer

Length of the averaging window in samples, specified as a positive
integer. For more information on how the averaging length influences the
variance of the AGC output signal in steady-state operation and the
execution speed, see Tips.

### **Maximum power gain** — Maximum power gain (dB) `60` (default) | positive scalar

Maximum power gain in dB, specified as a positive scalar. Large gain
adjustments can cause clipping when a small input signal power suddenly
increases. Use this property to avoid large gain adjustments by limiting the
gain that the AGC applies to the input signal. For an example, see Compare AGC Performance for Different Maximum Gains.

### **Enable output of estimated input power** — Option to output estimated input power off (default) | on

Select this check box to provide an output port, `Px`,
that returns an estimate of the input signal power.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Type of simulation to run, specified as `Interpreted
execution` or `Code generation`.

- `Interpreted execution` — Simulate the model by
  using the MATLAB® interpreter. This option requires less startup time, but the
  speed of subsequent simulations is slower than with the `Code
  generation` option. In this mode, you can debug the source
  code of the block.
- `Code generation` — Simulate the model by using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The model reuses the C code
  for subsequent simulations unless the model changes. This option requires
  additional startup time, but the speed of the subsequent simulations is
  faster than with the `Interpreted execution`
  option.

For more information, see Interpreted Execution vs. Code Generation (Simulink).

## Libraries

Communications Toolbox / RF Impairments Correction

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013a**

## Description

Adaptively adjust gain for constant signal-level output

The automatic gain controller (AGC) block adaptively adjusts its gain to achieve a
constant signal level at the output.

This icon shows the AGC block with the optional Px port.AGC block with optional ports shown
