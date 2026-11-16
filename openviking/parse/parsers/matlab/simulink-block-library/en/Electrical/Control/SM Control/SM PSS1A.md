---
type: simulink-block
title: 'SM PSS1A'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smpss1a'
documentation_source_path: 'ref/smpss1a.html'
language: en
---

# SM PSS1A

## Ports

### Input

### **V\_SI** — Speed, frequency, or power scalar

Per-unit speed, frequency of the terminal bus voltage, compensated frequency, or
electrical power, specified as a scalar.

**Data Types:** `single` | `double`
### Output

### **V\_ST** — Stabilization speed, frequency, or power scalar

Automatic voltage regulator input stabilization signal, as limited by
*VST\_min* and
*VST\_max*, returned as a
scalar.

**Data Types:** `single` | `double`

## Parameters

### **Power system stabilizer (PSS) gain, K\_S (pu)** — Power system stabilizer gain 3.15 (default) | scalar

Power system stabilizer forward path gain.

### **PSS denominator constant for second-order block, A\_1** — Filter constant 1 `0` (default) | scalar

Power system stabilizer signal conditioning filter coefficient 1.

### **PSS denominator constant for second-order block, A\_2** — Filter constant 2 `0` (default) | scalar

Power system stabilizer signal conditioning filter coefficient 2.

### **PSS numerator (lead) compensating time constant, T\_1 (s)** — Lead time constant 1 `0.76` (default) | scalar

Lead time constant 1, associated with the first Lead-Lag block in the diagram.

### **PSS denominator (lag) compensating time constant, T\_2 (s)** — Lag time constant 2 `0.01` (default) | scalar

Lag time constant 2, associated with the first Lead-Lag block in the diagram.

### **PSS numerator (lead) compensating time constant, T\_3 (s)** — Lead time constant 3 `0.76` (default) | scalar

Lead time constant 3, associated with the second Lead-Lag block in the diagram.

### **PSS denominator (lag) compensating time constant, T\_4 (s)** — Lag time constant 4 `0.01` (default) | scalar

Lag time constant 4, associated with the second Lead-Lag block in the diagram.

### **PSS washout time constant, T\_5 (s)** — Washout time constant `10` (default) | scalar

Washout time constant, associated with the Washout block in the diagram.

### **PSS transducer time constant, T\_6 (s)** — Transducer time constant `0` (default) | scalar

Transducer time constant, associated with the Low-Pass Filter block in the
diagram.

### **Maximum PSS output, V\_STmax (pu)** — Maximum stabilization `0.09` (default) | scalar

Maximum power system stabilizer output to the automatic voltage regulator (AVR).

### **Minimum PSS output, V\_STmin (pu)** — Minimum stabilization `-0.09` (default) | scalar

Minimum power system stabilizer output to the automatic voltage regulator (AVR).

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | 0 | positive scalar

Time between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

For inherited discrete-time operation, set the sample time to `-1`.
For discrete-time operation, set the sample time to a positive scalar. For
continuous-time operation, set the sample time to `0`.

## Libraries

Simscape / Electrical / Control / SM Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

Discrete-time or continuous-time single input PSS1A power system stabilizer

The SM PSS1A block implements a single-input PSS1A power system stabilizer
(PSS) that maintains rotor angle stability in a synchronous machine (SM) in conformance
with IEEE 421.5-2016[1].
Typically, you use a PSS to enhance the damping of power system oscillations through
excitation control.

You can switch between continuous and discrete implementations of the block by using the
**Sample time (-1 for inherited)** parameter. To configure the
integrator for continuous time, set the **Sample time (-1 for
inherited)** property to `0`. To configure the integrator
for discrete time, set the **Sample time (-1 for inherited)** property
to a positive, nonzero value, or to `-1` to inherit the sample time
from an upstream block.

This diagram illustrates the overall structure of the PSS1A power system
stabilizer:

In the diagram:

- *V\_SI* is the power system stabilizer input. Commonly
  used inputs are speed, frequency, or power. For more information, see V\_SI.
- The Low-Pass Filter (Discrete or Continuous) block can
  be used to model a transducer, with a time constant
  *T6*.
- *Ks* models the stabilizer
  gain.
- The Washout (Discrete or Continuous) block
  models a high-pass filter. Here,
  *T5* is the time
  constant.
- The Second-Order Low-Pass Filter (Discrete or Continuous) block
  takes into account the low-frequency effects of the high-frequency torsional
  filters. Here, *A1* and
  *A2* are the stabilizer
  denominator constants for the second-order block.
- The two Lead-Lag (Discrete or Continuous) blocks
  models additional dynamics associated with the power system stabilizer, and
  represent two stages of the lead-lag compensation.
