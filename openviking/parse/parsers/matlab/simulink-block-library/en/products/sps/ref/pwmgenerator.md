---
type: simulink-block
title: 'PWM Generator'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Pulse Width Modulation'
documentation_page: 'pwmgenerator'
documentation_source_path: 'ref/pwmgenerator.html'
language: en
---

# PWM Generator

## Ports

### Input

### **DC** — Duty cycle scalar

Duty cycle in the range `[0,1]`.

**Data Types:** `single` | `double`
### Output

### **PWM** — PWM signal scalar

Pulse width modulation signal.

**Data Types:** `single` | `double`

## Parameters

### **Carrier counter** — Carrier counter strategy `Up` (default) | `Down` | `Up-Down`

Use the carrier counter strategy to change the initial behavior of the PWM output:

- Up counter — PWM output begins at the start of the
  `on` state.
- Down counter — PWM output begins at the start of the
  `off` state.
- Up-down counter — PWM output begins in the middle of the
  `on` state.

### **Timer period (s)** — PWM period `0.001` (default) | positive number

PWM timer period.

If you set **Carrier counter** to `Up
counter` or `Down counter`, the
**Timer period (s)** parameter is specified as 1fsw, where fsw is the switching frequency. If you set **Carrier
counter** to `Up-down counter`, the
**Timer period (s)** parameter is specified as 12fsw.

### **Phase delay (s)** — Phase delay `0` (default) | nonnegative number

Phase delay, in seconds. Add a phase delay to change the initial state of
the counter.

### **Sample time** — Block sample time `5e-5` (default) | positive number

Sample time for the block. For continuous-time simulation, set to zero.
For discrete-time simulation, to ensure adequate resolution in the generated
signal, specify a positive value that is less than or equal to
`Tper/10`,
where *Tper* is the **Timer
period (s)**.

## Libraries

Simscape / Electrical / Control / Pulse Width Modulation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Generate pulse width modulated signal or waveform

The PWM Generator block implements a PWM generator. The pulse width
modulation technique controls power transfer from one electrical component to another by
quickly switching between full power transfer and no power transfer.

### Working Principle

The PWM generator block outputs either `1` when the duty cycle is
greater than the carrier counter value, or `0` otherwise. You can
set the period of each cycle by specifying the timer period *Tper*.
You can change the initial output, or phase, of the PWM output by specifying one of
three types of carrier counters:

- Up counter — The PWM output signal initializes at the start of the
  `on` cycle. This graphic shows the carrier counter
  signal and the corresponding PWM output.
- Down counter — The PWM output signal initializes at the start of the
  `off` cycle. This graphic shows the carrier counter
  signal and the corresponding PWM output.
- Up-down counter — The PWM output signal initializes halfway through
  the `on` cycle. This graphic shows the carrier counter
  signal and the corresponding PWM output.
