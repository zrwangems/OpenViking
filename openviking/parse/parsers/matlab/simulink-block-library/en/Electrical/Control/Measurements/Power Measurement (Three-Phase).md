---
type: simulink-block
title: 'Power Measurement (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Measurements'
documentation_page: 'powermeasurementthreephase'
documentation_source_path: 'ref/powermeasurementthreephase.html'
language: en
---

# Power Measurement (Three-Phase)

## Ports
```yaml
ports:
- name: V
  summary: Input voltage vector
  direction: input
  data_types: single | double
- name: I
  summary: Input current vector
  direction: input
  data_types: single | double
- name: P
  summary: Real power scalar or vector | vector
  direction: output
  data_types: single | double
- name: Q
  summary: Reactive power scalar or vector | vector
  direction: output
  data_types: single | double
```

### Input

### **V** — Input voltage vector

Three-phase voltage across element from which to measure power, in
V.

**Data Types:** `single` | `double`

### **I** — Input current vector

Three-phase current through element from which to measure power, in
A.

**Data Types:** `single` | `double`
### Output

### **P** — Real power scalar or vector | vector

Real power for selected frequency components, in W. If the
**Harmonic numbers** parameter value is a scalar,
this output is also a scalar.

**Data Types:** `single` | `double`

### **Q** — Reactive power scalar or vector | vector

Reactive power for selected frequency components, in var. If the
**Harmonic numbers** parameter value is a scalar,
this output is also a scalar.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Base frequency (Hz)
  summary: Fundamental frequency 60 (default) | positive number
  group: ''
- name: Harmonic numbers
  summary: Frequency components [0 1 2 3] (default) | scalar or vector
  group: ''
- name: Sequence
  summary: Symmetrical sequence Positive (default) | Negative | Zero
  group: ''
- name: Sample time
  summary: Block sample time 0 (default) | positive number
  group: ''
```

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

### **Sequence** — Symmetrical sequence `Positive` (default) | `Negative` | `Zero`

Symmetrical sequence of the power output.

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

Calculate three-phase real and reactive power

The Power Measurement (Three-Phase) block measures the real and
reactive power of an element in a three-phase network. The block outputs the power
quantities for each frequency component you specify in the selected symmetrical
sequence.

Use this block to measure power for both sinusoidal and nonsinusoidal periodic
signals. For single-phase power measurement, consider using the Power
Measurement block.

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
*Qk* for the specified sequence from
the phasor equation:

Pk+jQk=32(VkejθVk)(IkejθIk¯),

where:

- VkejθVk is the phasor representing the
  *k*-component voltage of the selected sequence.
- IkejθIk¯ is the complex conjugate of IkejθIk, the phasor representing the
  *k*-component current of the selected sequence.

Select the symmetrical sequence used in the power calculation using the
**Sequence** parameter:

- `Positive`:

  VkejθVk=Vk+ejθVk+, IkejθIk=Ik+ejθIk+
- `Negative`:

  VkejθVk=Vk−ejθVk−, IkejθIk=Ik−ejθIk−
- `Zero`:

  VkejθVk=Vk0ejθVk0, IkejθIk=Ik0ejθIk0

The block calculates the symmetrical set of *+-0* voltage phasors
from the set of *abc* voltage phasors using the symmetrical
components transform *S*:

[Vk+ejθVk+Vk−ejθVk−Vk0ejθVk0]=S[VkaejθVkaVkbejθVkbVkcejθVkc].

For more information about this transform, see Symmetrical
Components Transform.

The block obtains this set of *abc* voltage phasors from the
three-phase input voltage *V(t)* as:

[VkaejθVkaVkbejθVkbVkcejθVkc]=2T∫t−TtV(t)sin(2πkFt)dt+j2T∫t−TtV(t)cos(2πkFt)dt,

where *T* is the period of the input signal, or
equivalently the inverse of its base frequency *F*.

The block calculates the symmetrical set of current phasors in the same way as it
does the voltage.

If the input signals have a finite number of harmonics *n*, the
total real power *P* and total reactive power *Q*
for the specified sequence can be calculated from their components:

P=∑k=0nPk

Q=∑k=1nQk.

The summation for *Q* does not include the DC
component (*k = 0*), because this component only contributes to
real power.
