---
type: simulink-block
title: 'Outport'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Utilities'
documentation_page: 'outport'
documentation_source_path: 'ref/outport.html'
language: en
---

# Outport

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Sensor type
  summary: Type of signal measured by sensor Ideal voltage (default) | Ideal current | Power
  group: ''
- name: Load impedance (Ohm)
  summary: Load impedance of RF circuit inf (default) | vector of positive integers in ohms
  group: ''
- name: Output
  summary: Format of output signals Complex Baseband (default) | In-phase and Quadrature Baseband | Magnitude and Angle Baseband
    | Real Passband
  group: ''
- name: Automatically compute output step size
  summary: Determine optimal time step to resolve highest listed carrier frequency on (default) | off
  group: ''
- name: Step size
  summary: Time step 1e-6 s (default) | positive integer in seconds
  group: ''
- name: Interpolation Filter Half Polyphase Length
  summary: Half-polyphase length of filter 12 (default) | nonnegative integer
  group: ''
- name: Carrier frequencies
  summary: Carrier frequencies 0 Hz (default) | vector of positive integers in Hz
  group: ''
- name: Ground and hide negative terminals
  summary: Ground RF circuit terminals on (default) | off
  group: ''
```

### **Sensor type** — Type of signal measured by sensor `Ideal voltage` (default) | `Ideal current` | `Power`

Type of signal measured by sensor, specified as:

- `Ideal voltage` — The block outputs the modulations of the
  voltage signal at the specified **Carrier
  frequencies** in the format specified by the
  **Output** parameter. This is the
  recommended option to sense a signal without adding a loading
  impedance and changing matching conditions.
- `Ideal current` —
  The block outputs the modulations of the current signal at the specified **Carrier
  frequencies** in the format specified by the **Output** parameter.
- `Power` — The block outputs the modulations of the voltage
  signal at the specified **Carrier frequencies**
  and scaled with respect to the specified load impedance. This is
  the recommended option to sense a signal generated in RF
  Blockset 50 Ohm environment or a different reference impedance.
  When you use the power option , the output port automatically
  inserts a load impedance in your circuit.

  Re(Zl)Zlv(t)

  where
  *Zl* is the value of
  the **Load
  impedance (Ohm)** parameter.

### **Load impedance (Ohm)** — Load impedance of RF circuit `inf` (default) | vector of positive integers in ohms

Load impedance of RF circuit used to measure signal power, specified as a vector of positive
integers in ohms. When you use the power option , the output port
automatically inserts a load impedance in your circuit. When you use
multiple Outport blocks as power sources at the same node in
a given circuit, the resulting load is the parallel combination of the
specified load impedances.

#### Dependencies

To enable this parameter, select `Power` in **Sensor
type**.

### **Output** — Format of output signals `Complex Baseband` (default) | `In-phase and Quadrature Baseband` | `Magnitude and Angle Baseband` | `Real Passband`

Format of output signals, specified as one of the following:

- `Complex Baseband` —
  The block outputs a vector of complex-valued signals *Ik*(*t*) + *j* · *Qk*(*t*)
  at the port labeled **SL**. The *k*th
  element of the vector is the *k*th frequency specified
  by the **Carrier frequencies** parameter.
- `In-phase and Quadrature Baseband` — The block outputs two
  vectors of real-valued signals
  *Ik*(*t*)
  and
  *Qk*(*t*)
  at the **I** port and **Q** port,
  respectively. The signal at the **I** port contains
  the in-phase components, and the signal at the
  **Q** port contains the quadrature components.
  The *k*th element of the vector is the
  *k*th frequency specified by the
  **Carrier frequencies** parameter. The
  quadrature component of a signal with carrier frequency equal to 0
  Hz is zero.
- `Magnitude and Angle Baseband` —
  The block outputs two real-valued vectors, whose elements are the
  magnitude and phase angle of the modulation. The **Mag** port
  outputs |*Ik*(*t*) + *j* · *Qk*(*t*)|
  and the **Ang** port outputs Arg[*Ik*(*t*) + *j* · *Qk*(*t*)].
  The *k*th element of the vector is the *k*th
  frequency specified by the **Carrier frequencies** parameter.
- `Real Passband` — The block outputs real passband signals by
  combining envelope and carrier signals for all frequencies listed
  under **Carrier frequencies**. When using the
  `Real Passband` option, the solver
  takes time steps small enough to resolve the carrier. Thus,
  simulation speed improvements from envelope simulation may be
  limited.

  out=Real(∑k=1N(Ik(t)+j·Qk(t))·ej2πfkt)

  where `t` is the value of
  **Load impedance
  (Ohm)** parameter.

### **Automatically compute output step size** — Determine optimal time step to resolve highest listed carrier frequency `on` (default) | `off`

Determine optimal time step to resolve highest listed carrier frequency, specified as a
`on` or `off`. Select this parameter
to allow RF Blockset to determine the optimal time step to resolve the highest
listed carrier frequency. Clear the parameter selection to enter a value for
step size.

### **Step size** — Time step `1e-6 s` (default) | positive integer in seconds

Time step, specified as a positive integer in seconds. The step size should be small enough to
resolve the fastest carrier signal. The size helps to avoid passband output
undersampling and aliasing effects.

Set the time step value to `-1` to inherit
the time step specified from `Step size` in Configuration block.

### **Interpolation Filter Half Polyphase Length** — Half-polyphase length of filter `12` (default) | nonnegative integer

*Since R2023a*

Half-polyphase length of filter, specified as a nonegative integer. Set
the half-polyphase length to a value greater than zero to mitigate undesired
spectral images on a real passband output. If you set this parameter to
`0`, then the block does not filter.

#### Dependencies

To enable this parameter, set **Output** to
`Real Passband`.

### **Carrier frequencies** — Carrier frequencies `0 Hz` (default) | vector of positive integers in Hz

Carrier frequencies, specified as a vector of positive integers
in Hz. In carrier frequencies, the elements are a combination of fundamental
tones and corresponding harmonics in the Configuration block.

### **Ground and hide negative terminals** — Ground RF circuit terminals `on` (default) | `off`

Ground RF circuit terminals, specified as a `on` or `off`.
Select this parameter to ground and hide the negative terminals. Clear the
parameter to expose the negative terminals. By exposing these terminals, you
can connect them to other parts of your model.

By default, this option is selected.
## Libraries

RF Blockset / Circuit Envelope / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2010b**

### R2023a: FIR interpolation filter for real passband output in Outport block

The Outport block now supports an FIR interpolation filter for real
passband output to mitigate undesired spectral images.

### R2022b: Outport block icon updated

The Outport block icon now changes based on how you set the
**Sensor type**,
**Ground and hide
negative terminals**, and **Output** parameters. When
you open a model created before R2022b containing an Outport block,
the software replaces the block icon with the R2022b version.

### R2021b: Outport block icon updated

The Outport block icon was updated in R2021b. When you open a model
created before R2021b containing an Outport block, the software
replaces the block icon with the R2021b version.

## Description

Convert RF Blockset signal to Simulink output signals

The Outport block outputs carrier modulation
signals in the RF Blockset™ circuit envelope simulation environment
as Simulink® signal. For an introduction to RF simulation, see
the example, Simulate High Frequency Components.

The output port senses current and voltage complex envelope or real passband signals.
Complex baseband signals consist of in-phase (*Ik*) and quadrature (*Qk*) components centered around each specified
center frequency *fk*. The
**Sensor type** parameter determines which signal the block
measures, and the **Output** parameter defines the format of the
Simulink signal. For more information, see How to Use Outport Block.

Outport block icons are dynamic and show the current format of the
output signal. For more information, see Outport Block Icons.

**Note**

Outport block `Real passband` output does
not support frame-based processing (supported by the Configuration blocks). This block errors if the **Samples per
frame** is more than 1 in the Configuration block.
