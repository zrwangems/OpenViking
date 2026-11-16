---
type: simulink-block
title: 'Fourier Analysis'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'fourieranalysis'
documentation_source_path: 'ref/fourieranalysis.html'
language: en
---

# Fourier Analysis

## Ports

### Input

### **u** — Fourier analysis input scalar | vector

Input signal to be analyzed. The input can be a single signal or multiple multiplexed
signals. Input signals can be AC currents or voltages in an electrical
system.

**Data Types:** `single` | `double`
### Output

### **Magnitude** — Signal magnitude scalar | vector

Signal magnitude corresponding to the harmonic number.

**Data Types:** `single` | `double`

### **Angle** — Signal angle scalar | vector

Signal angle corresponding to the harmonic number.

**Data Types:** `single` | `double`

## Parameters

### **Fundamental frequency (Hz)** — Signal fundamental frequency `60` (default) | positive scalar | vector with positive values

Fundamental frequency of the signal, in Hz. If you specify the fundamental frequency
using a vector, it must match the input vector dimensions.

### **Harmonic numbers** — Signal harmonic numbers `[1 2]` (default) | vector with elements ≥ `0`

Specify signal harmonic numbers. Vector elements must be greater than or
equal to 0.

### **Initial magnitude** — Initial signal magnitude `1` (default) | vector with elements ≥ `0`

Specify the initial magnitude of the signal. Vector elements must be
greater than or equal to 0.

### **Initial phase (rad)** — Initial signal phase `0` (default) | vector

Initial phase angle of the signal, in rad.

### **Buffer size** — Buffer size `8192` (default) | scalar

Size of the buffer.

#### Dependencies

To enable this parameter, set **Sample time (-1 for
inherited)** to `0`.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | `0` | positive scalar

Time between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

For inherited discrete-time operation, set this parameter to `-1`.
For discrete-time operation, set this parameter to a positive integer. For
continuous-time operation, set this parameter to `0`.

If this block is in a masked subsystem or a variant subsystem that supports switching
between continuous operation and discrete operation, promote this parameter to ensure
correct switching between the continuous and discrete implementations of the block. For
more information, see Promote Block Parameters on a Mask.

## Libraries

Simscape / Electrical / Control / General Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

Discrete or continuous time Fourier analysis

The Fourier Analysis block performs a Fourier analysis on the input signal in
either discrete or continuous time.

### Equations

A periodic function *x(t)* can be decomposed to an infinite sum
of sine and cosine functions as

x(t)=a02+∑n=1∞[ancos(nt)+bnsin(nt)]

where:

- *a0* is the DC
  component.
- *an* and
  *bn* are constant
  Fourier coefficients.
- *n* is the harmonic number.

The coefficients *an* and
*bn* are defined as:

an=2T0∫t0t0+T0x(t)cos(nΩ0t)dt, n=0,1,...

bn=2T0∫t0t0+T0x(t)sin(nΩ0t)dt, n = 1,2, ...

Ω0=2πT0

T0=1f

where *f* is the fundamental frequency.

These equations define the magnitude and angle corresponding to the harmonic number:

|Xn|=an2+bn2

θn=−tan−1[anbn]

**Note**

If you use this block for continuous-time operations and set the
**Sample time (-1 for inherited)** parameter to
`0`, you should also specify the value of the
**Buffer size** parameter to ensure it covers the moving
time window.
