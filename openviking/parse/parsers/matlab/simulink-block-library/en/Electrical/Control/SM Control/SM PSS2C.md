---
type: simulink-block
title: 'SM PSS2C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smpss2c'
documentation_source_path: 'ref/smpss2c.html'
language: en
---

# SM PSS2C

## Ports

### Input

### **V\_SI1** — Speed, frequency, or power scalar

Per-unit speed, frequency of the terminal bus voltage, compensated frequency, or
electrical power, specified as a scalar.

**Data Types:** `single` | `double`

### **V\_SI2** — Electrical power scalar

Per-unit electrical power, specified as a scalar.

**Data Types:** `single` | `double`
### Output

### **V\_ST** — Stabilization speed, frequency, or power scalar

Automatic voltage regulator input stabilization signal, as limited by
*VST\_min* and
*VST\_max*, returned as a
scalar.

**Data Types:** `single` | `double`

## Parameters

### **PSS gain, K\_S1 (pu)** — Power system stabilizer forward path gain 5 (default) | scalar

Power system stabilizer forward path gain.

### **PSS gain, K\_S2 (pu)** — Power system stabilizer transducer gain 1.4184 (default) | scalar

Power system stabilizer transducer gain.

### **PSS gain, K\_S3 (pu)** — Power system stabilizer gain 1 (default) | scalar

Power system stabilizer gain.

### **PSS transducer time constant, T\_6 (s)** — Transducer time constant 6 `0` (default) | scalar

Transducer time constant 6.

### **PSS transducer time constant, T\_7 (s)** — Transducer time constant 7 `10` (default) | scalar

Transducer time constant 7.

### **PSS washout time constant, T\_w1 (s)** — Washout time constant 1 `10` (default) | scalar

Washout time constant 1.

### **PSS washout time constant, T\_w2 (s)** — Washout time constant 2 `10` (default) | scalar

Washout time constant 2.

### **PSS washout time constant, T\_w3 (s)** — Washout time constant 3 `10` (default) | scalar

Washout time constant 3.

### **PSS washout time constant, T\_w4 (s)** — Washout time constant 4 `0` (default) | scalar

Washout time constant 4.

### **PSS transducer time constant, T\_8 (s)** — Transducer time constant 8 `0.5` (default) | scalar

Transducer time constant 8.

### **PSS washout time constant, T\_9 (s)** — Washout time constant 9 `0.1` (default) | scalar

Washout time constant 9.

### **Denominator exponent for ramp-track filter, M** — Exponent of the denominator of the ramp-track filter `5` (default) | scalar

Denominator exponent for ramp-track filter.

### **Overall exponent for ramp-track filter, N** — Overall exponent of ramp-track filter `1` (default) | scalar

Overall exponent for ramp-track filter.

### **PSS numerator (lead) compensating time constant (first block), T\_1 (s)** — Lead time constant 1 `0.16` (default) | scalar

Lead time constant 1, associated with the block labeled Lead-Lag1 in the
diagram.

### **PSS denominator (lag) compensating time constant (first block), T\_2 (s)** — Lag time constant 2 `0.04` (default) | scalar

Lag time constant 2, associated with the block labeled Lead-Lag1 in the diagram.

### **PSS numerator (lead) compensating time constant (second block), T\_3 (s)** — Lead time constant 3 `0.16` (default) | scalar

Lead time constant 3, associated with the block labeled Lead-Lag2 in the diagram.

### **PSS denominator (lag) compensating time constant (second block), T\_4 (s)** — Lag time constant 4 `0.04` (default) | scalar

Lag time constant 4, associated with the block labeled Lead-Lag2 in the diagram.

### **PSS denominator (lead) compensating time constant (third block), T\_10 (s)** — Lag time constant 10 `0.18` (default) | scalar

Lag time constant 10, associated with the block labeled Lead-Lag3 in the diagram.

### **PSS denominator (lag) compensating time constant (third block), T\_11 (s)** — Lag time constant 11 `0.03` (default) | scalar

Lag time constant 11, associated with the block labeled Lead-Lag3 in the diagram.

### **PSS denominator (lead) compensating time constant (fourth block), T\_12 (s)** — Lag time constant 12 `0` (default) | scalar

Lag time constant 12, associated with the block labeled Lead-Lag4 in the diagram.

### **PSS denominator (lag) compensating time constant (fourth block), T\_13 (s)** — Lag time constant 13 `0` (default) | scalar

Lag time constant 13, associated with the block labeled Lead-Lag4 in the diagram.

### **Maximum PSS output, V\_STmax (pu)** — Maximum stabilization `0.1` (default) | scalar

Maximum power system stabilizer output to the automatic voltage regulator.

### **Minimum PSS output, V\_STmin (pu)** — Minimum stabilization `-0.1` (default) | scalar

Minimum power system stabilizer output to the automatic voltage regulator.

### **Input signal #1 maximum limit, V\_S1max (pu)** — Maximum limit for first input `2` (default) | scalar

Maximum signal value for the first stabilizer input.

### **Input signal #1 minimum limit, V\_S1min (pu)** — Minimum limit for first input `-2` (default) | scalar

Minimum signal value for the first stabilizer input.

### **Input signal #2 maximum limit, V\_S2max (pu)** — Maximum limit for second input `2` (default) | scalar

Maximum signal value for the second stabilizer input.

### **Input signal #2 minimum limit, V\_S2min (pu)** — Minimum limit for second input `-2` (default) | scalar

Minimum signal value for the second stabilizer input.

### **Generator MW threshold for PSS activation, P\_PSSon (pu)** — Generator threshold for power system stabilizer activation `0` (default) | scalar

Generator threshold for power system stabilizer activation.

### **Generator MW threshold for PSS de-activation, P\_PSSoff (pu)** — Generator threshold for power system stabilizer deactivation `0` (default) | scalar

Generator threshold for power system stabilizer deactivation.

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

**Introduced in R2020a**

## Description

Discrete-time or continuous-time single input PSS2C power system stabilizer

The SM PSS2C block implements a double-input PSS2C power system stabilizer
(PSS) that maintains rotor angle stability in a synchronous machine (SM) in conformance
with IEEE 421.5-2016[1].
Typically, you use a PSS to enhance the damping of power system oscillations through
excitation control.

You can represent two different types of dual-input power system stabilizers with this same model:

- A stabilizer that uses electrical power and speed (or frequency) signals
  to calculate the integral of the accelerating power. This makes the
  calculated stabilizer signal insensitive to mechanical changes.
- A stabilizer that uses a combination of electrical power and either speed
  or frequency. To achieve the desired stabilizing signal shaping, the system
  uses the speed directly, without phase-lead compensation, and adds a signal
  that is proportional to the electrical power.

You can switch between continuous and discrete implementations of the block by using the
**Sample time (-1 for inherited)** parameter. To configure the
integrator for continuous time, set the **Sample time (-1 for
inherited)** property to `0`. To configure the integrator
for discrete time, set the **Sample time (-1 for inherited)** property
to a positive, nonzero value, or to `-1` to inherit the sample time
from an upstream block.

This diagram illustrates the overall structure of the PSS2C power system
stabilizer:

In the diagram:

- *V\_SI1* and *V\_SI2* are the two power
  system stabilizer inputs. Commonly used inputs are speed, frequency, or
  power.
- Two Washout (Discrete or Continuous) blocks
  are represented for each stabilizer input, with time constants
  *TW1* to
  *TW4*, along with a
  transducer, represented by a Low-Pass Filter (Discrete or Continuous), with
  time constants *T6* and
  *T7*.
- To allow a ramp-tracking filter characteristic, the Ramp Tracking Filter
  subsystem models a network of lead-lag and low-pass filter blocks in
  series.
- To provide phase compensation, a Lead-Lag (Discrete or Continuous) network
  models additional dynamics associated with the power system stabilizer,
  representing four stages of lead-lag compensation, with time constants
  *T1* to
  *T4* and
  *T10* to
  *T13*.
- The PSS output logic subsystem allows the representation of the PSS output
  logic associated with the generator active power output.
  *PPSSon* and
  *PPSSoff* are the threshold
  values used to define a hysteresis.
