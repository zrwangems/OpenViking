---
type: simulink-block
title: 'Baseband PLL'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Architectures'
documentation_page: 'basebandpll'
documentation_source_path: 'ref/basebandpll.html'
language: en
---

# Baseband PLL

## Ports
```yaml
ports:
- name: In
  summary: Input signal from baseband VCO scalar
  direction: input
  data_types: double
- name: Filt
  summary: Output of loop filter scalar
  direction: output
  data_types: double
- name: PD
  summary: Output of phase detector scalar
  direction: output
  data_types: double
- name: VCO
  summary: Output of VCO scalar
  direction: output
  data_types: double
```

### Input

### **In** — Input signal from baseband VCO scalar

Input signal, specified as a scalar. The input signal is the output of a baseband
VCO in the phase domain.

**Data Types:** `double`
### Output

### **Filt** — Output of loop filter scalar

Output of the loop filter in the phase domain, returned as a scalar.

**Data Types:** `double`

### **PD** — Output of phase detector scalar

Output of the phase detector in the phase domain, returned as a scalar.

**Data Types:** `double`

### **VCO** — Output of VCO scalar

Output of the VCO in the phase domain, returned as a scalar.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Loop filter type
  summary: Determine how to define loop filter Transfer function (default) | 2nd order passive | 3rd order passive | 4th order
    passive
  group: ''
  block_parameter: Ftype
  type: double
  values: Transfer function | 2nd order passive | 3rd order passive | 4th order passive
  default: Transfer function
- name: VCO input sensitivity (Hz/V)
  summary: Measure of change in output frequency of VCO 100e6 (default) | positive real scalar
  group: ''
  block_parameter: Kvco
  type: double
  values: positive real scalar
  default: 100e6
- name: Charge pump current (A)
  summary: Charge pump output current 5e3 (default) | positive real scalar
  group: ''
  block_parameter: Icp
  type: double
  values: positive real scalar
  default: 5e3
- name: Min clock divider value
  summary: Minimum value by which the clock divider can divide input frequency 100 (default) | positive real scalar
  group: ''
  block_parameter: Nmin
  type: double
  values: positive real scalar
  default: '100'
- name: Loop bandwidth (Hz)
  summary: Frequency at which magnitude of open loop transfer function becomes 1 50e3 (default) | positive real scalar
  group: ''
  block_parameter: Fc
  type: double
  values: positive real scalar
  default: 50e3
- name: Phase margin (degrees)
  summary: Phase of open loop transfer function at loop bandwidth subtracted from 180° 45 (default) | positive real scalar
  group: ''
  block_parameter: phi
  type: double
  values: positive real scalar
  default: '45'
- name: Numerator
  summary: Numerator of loop filter transfer function [1.9212e-10, 5e-05] (default) | real scalar | real valued vector
  group: ''
  block_parameter: Fn
  type: double
  values: real scalar | real valued scalar
  default: '[1.9212e-10, 5e-05]'
- name: Denominator
  summary: Denominator of loop filter transfer function [2.0157e-15, 3.0576e-09, 0] (default) | real valued vector
  group: ''
  block_parameter: Fd
  type: double
  values: real valued vector
  default: '[2.0157e-15, 3.0576e-09, 0]'
- name: Open loop analysis
  summary: Plot open loop presimulation analysis on (default) | off
  group: ''
- name: Close loop analysis
  summary: Plot closed loop presimulation analysis on (default) | off
  group: ''
- name: Plot loop dynamic
  summary: Plot loop dynamics of PLL system button
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Loop filter type** — Determine how to define loop filter `Transfer function` (default) | `2nd order passive` | `3rd order passive` | `4th order passive`

Determine how to define the loop filter. You can define a passive loop filter
between the orders two to four, or you can represent a loop filter using transfer
function.

If you are defining a passive loop filter, you have to define the **Charge
pump current (A)**, **Min clock divider value**.
**Loop bandwidth (Hz)**, and **Phase margin
(degrees)** of the PLL system.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Ftype` |
| **Type:** `double` |
| **Values:** `Transfer function` | `2nd order passive` | `3rd order passive` | `4th order passive` |
| **Default:** `Transfer function` |

### **VCO input sensitivity (Hz/V)** — Measure of change in output frequency of VCO `100e6` (default) | positive real scalar

Measure of change in output frequency for input voltage change, specified as a
positive real scalar in Hz/V.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Kvco` |
| **Type:** `double` |
| **Values:** positive real scalar |
| **Default:** `100e6` |

### **Charge pump current (A)** — Charge pump output current `5e3` (default) | positive real scalar

Full scale magnitude of the charge pump output current, specified as a positive real
scalar in amperes.

#### Dependencies

To enable this parameter, set **Loop filter type** to
`2nd order passive`, `3rd order
passive`, or `4th order passive`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Icp` |
| **Type:** `double` |
| **Values:** positive real scalar |
| **Default:** `5e3` |

### **Min clock divider value** — Minimum value by which the clock divider can divide input frequency `100` (default) | positive real scalar

Minimum value by which the clock divider can divide the input frequency, specified
as a positive real scalar.

#### Dependencies

To enable this parameter, set **Loop filter type** to
`2nd order passive`, `3rd order
passive`, or `4th order passive`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Nmin` |
| **Type:** `double` |
| **Values:** positive real scalar |
| **Default:** `100` |

### **Loop bandwidth (Hz)** — Frequency at which magnitude of open loop transfer function becomes 1 `50e3` (default) | positive real scalar

Frequency at which the magnitude of the open loop transfer function becomes 1,
specified as a positive real scalar in Hz. Lower values of Loop bandwidth (Hz) result in
reduced phase noise and reference spurs at the expense of longer lock time and less
phase margin.

#### Dependencies

To enable this parameter, set **Loop filter type** to
`2nd order passive`, `3rd order
passive`, or `4th order passive`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Fc` |
| **Type:** `double` |
| **Values:** positive real scalar |
| **Default:** `50e3` |

### **Phase margin (degrees)** — Phase of open loop transfer function at loop bandwidth subtracted from 180° `45` (default) | positive real scalar

Phase of the open loop transfer function at the loop bandwidth subtracted from 180°,
specified as a positive real scalar in degrees. For optimum lock time, select a phase
margin between 40° and 55°.

#### Dependencies

To enable this parameter, set **Loop filter type** to
`2nd order passive`, `3rd order
passive`, or `4th order passive`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `phi` |
| **Type:** `double` |
| **Values:** positive real scalar |
| **Default:** `45` |

### **Numerator** — Numerator of loop filter transfer function `[1.9212e-10, 5e-05]` (default) | real scalar | real valued vector

Numerator of the loop filter transfer function. If you are defining a passive loop
filter, this is automatically calculated for you. You can also manually change it if you
are representing the loop filter using the transfer function.

#### Dependencies

To edit this parameter, set **Loop filter type** to
`Transfer function`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Fn` |
| **Type:** `double` |
| **Values:** real scalar | real valued scalar |
| **Default:** `[1.9212e-10, 5e-05]` |

### **Denominator** — Denominator of loop filter transfer function `[2.0157e-15, 3.0576e-09, 0]` (default) | real valued vector

Denominator of the loop filter transfer function. If you are defining a passive loop
filter, this is automatically calculated for you. You can also manually change it if you
are representing the loop filter using the transfer function.

#### Dependencies

To edit this parameter, set **Loop filter type** to
`Transfer function`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Fd` |
| **Type:** `double` |
| **Values:** real valued vector |
| **Default:** `[2.0157e-15, 3.0576e-09, 0]` |

### **Open loop analysis** — Plot open loop presimulation analysis on (default) | off

Select to plot the gain margin and phase margin of the PLL system before simulation.
By default, this option is selected.

### **Close loop analysis** — Plot closed loop presimulation analysis on (default) | off

Select to plot the pole-zero map, loop bandwidth, step response, and impulse
response of the PLL system before simulation. You must have a license to Control System Toolbox™ to plot the step response and impulse response of the PLL system. By
default, this option is selected.

### **Plot loop dynamic** — Plot loop dynamics of PLL system button

Click to plot the presimulation loop dynamics of the PLL system.
## Libraries

Mixed-Signal Blockset / PLL / Architectures

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2025a**

## Description

Phase-domain model of PLL

The Baseband PLL block models PLLs in the phase domain. The block accepts a
real-valued phase offset vector and produces the outputs for a loop filter, phase detector,
and VCO. The block acts as feedback control system that automatically adjusts the phase of a
locally generated signal to match the phase of an input signal.
