---
type: simulink-block
title: 'RMS Measurement'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Measurements'
documentation_page: 'rmsmeasurement'
documentation_source_path: 'ref/rmsmeasurement.html'
language: en
---

# RMS Measurement

## Ports

### Input

### **u** — Input signal scalar

Periodic input signal.

**Data Types:** `single` | `double`
### Output

### **RMS** — Root-mean-square scalar or vector

Estimated RMS of the input signal. If you select **Specify
harmonics**, the output is a vector with each element
corresponding to a specified harmonic. Otherwise, the output is a scalar
representing the total RMS.

**Data Types:** `single` | `double`

## Parameters

### **Base frequency (Hz)** — Fundamental frequency `60 Hz` (default) | scalar

Base frequency of the input signal corresponding to the first
harmonic.

### **Specify harmonics** — RMS output mode `off` (default) | on

Specify whether to output the total RMS of the input signals, or the
individual harmonics that you specify.

### **Harmonic numbers** — Harmonics specification `[0 1 2]` (default) | vector

Specify the harmonics for which to output an RMS.

#### Dependencies

To enable this parameter, select the **Specify
harmonics** parameter.

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

Calculate root-mean-square (RMS) properties of a signal

The RMS Measurement block measures root-mean-square (RMS) properties of
the input signal. You can use it to measure one of these properties:

- The total RMS of the input signal
- The RMS of the individual harmonics of the input signal that you
  specify.

Use the total RMS configuration with appropriate sensors to perform RMS voltage,
current, or power analyses in your system.

You can use the harmonics configuration to perform total harmonic distortion analyses
on systems with nonlinear loads such as:

- Converters
- Motor drives
- Inverters

### Equations

The total RMS value is calculated from the input signal
*xRMS* as:

xRMS(t)=1T∫t−Ttx(t)2dt,

where:

- *T* is the period of the input signal, or
  equivalently the inverse of its base frequency
  *F*.
- *x* is the input signal.

Because the calculation is performed over a period of time, the block requires
*T* seconds to respond to a step change in the input signal.
This condition also applies to startup.

The harmonic RMS component *xk,RMS* for
harmonic *k* is calculated as:

xk,RMS(t)=G(2T)(∫t−Ttx(t)sin(2πktT)dt)2+(∫t−Ttx(t)cos(2πktT)dt)2,

where *G* is equal to `0.5` for
the DC component (*k = 0*) and 1/2 for the AC components (*k > 0*).
