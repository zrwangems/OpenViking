---
type: simulink-block
title: 'Power Measurement'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Measurements'
documentation_page: 'powermeasurement'
documentation_source_path: 'ref/powermeasurement.html'
language: en
---

# Power Measurement

## Ports

### Input

### **v** — Input voltage scalar

Voltage across element from which to measure power, in V.

**Data Types:** `single` | `double`

### **i** — Input current scalar

Current through element from which to measure power, in A.

**Data Types:** `single` | `double`
### Output

### **P** — Real power scalar or vector

Real power for selected frequency components, in W. If the
**Harmonic numbers** parameter value is a scalar,
this output is also a scalar.

**Data Types:** `single` | `double`

### **Q** — Reactive power scalar or vector

Reactive power for selected frequency components, in var. If the
**Harmonic numbers** parameter value is a scalar,
this output is also a scalar.

**Data Types:** `single` | `double`

## Parameters

### **Base frequency (Hz)** — Fundamental frequency `60` (default) | positive number

Fundamental frequency corresponding to component
*k=1*.

### **Harmonic numbers** — Frequency components `[0 1 2 3]` (default) | scalar or vector

Frequency components to include in the output. Specify either a scalar
value corresponding to the desired component or a vector of all desired components.

- The value *k = 0* corresponds to the DC
  component.
- The value *k = 1* corresponds to the
  fundamental frequency.
- Values *k > 1* correspond to higher-level
  harmonics.

If you specify a vector, the order of the power outputs
correspond to the order of this vector.

### **Sample time** — Block sample time `0` (default) | positive number

Time between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

For continuous operation, set this property to `0`. For discrete
operation, specify the sample time explicitly as a positive number. This block does not
support inherited sample time.

If this block is in a masked subsystem, or other variant subsystem that allows either
continuous and discrete operation, promote the sample time parameter. Promoting the
sample time parameter ensures correct switching between the continuous and discrete
implementations of the block. For more information, see Promote Block Parameters on a Mask.

## Libraries

Simscape / Electrical / Control / Measurements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Calculate single-phase real and reactive power

The Power Measurement block measures the real and reactive power of an
element in a single-phase network. The block outputs the power quantities for each
frequency component you specify. For three-phase measurements, consider using the Three-Phase Power
Measurement block.

Use this block to measure power for both sinusoidal and nonsinusoidal periodic
signals.

Set the **Sample time** parameter to `0` for
continuous-time operation, or explicitly for discrete-time operation.

Specify a vector of all frequency components to include in the power output using the
**Harmonic numbers** parameter:

- To output the DC component, specify `0`.
- To output the component corresponding to the fundamental frequency,
  specify `1`.
- To output components corresponding to higher-order harmonics, specify
  `n > 1`.

### Equations

For each specified harmonic *k*, the block calculates the real
power *Pk* and reactive power
*Qk* from the phasor equation:

Pk+jQk=G(VkejθVk)(IkejθIk¯),

where:

- *G* is equal to `0.25` for the DC
  component (*k = 0*) and `0.5` for the
  AC components (*k > 0*).
- VkejθVk is the phasor representation of the
  *k*-component input voltage.
- IkejθIk¯ is the complex conjugate of IkejθIk, the phasor representation of the
  *k*-component input current.

The block estimates the real-time *k*-component voltage and
current phasors using these relationships:

VkejθVk=2T∫t−TtV(t)sin(2πkFt)dt+j2T∫t−TtV(t)cos(2πkFt)dt

IkejθIk=2T∫t−TtI(t)sin(2πkFt)dt+j2T∫t−TtI(t)cos(2πkFt)dt.

In these phasor equations:

- *V(t)* and *I(t)* are the input
  voltage and current, respectively.
- *T* is the period of the input signal, or
  equivalently the inverse of its base frequency
  *F*.

If the input signals have a finite number of harmonics *n*, the
total real power *P* and total reactive power *Q*
can be calculated from their components:

P=∑k=0nPk

Q=∑k=1nQk.

The summation for *Q* does not include the DC
component (*k = 0*) because this component only contributes to real
power.
