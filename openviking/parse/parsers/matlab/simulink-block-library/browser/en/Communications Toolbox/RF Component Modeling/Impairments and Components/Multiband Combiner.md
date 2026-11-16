---
type: simulink-block
title: 'Multiband Combiner'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Component Modeling / Impairments and Components'
documentation_page: 'multibandcombiner'
documentation_source_path: 'ref/multibandcombiner.html'
language: en
---

# Multiband Combiner

## Ports

### Input

### **In** — Input signals *N*samp-by-*N*chan matrix

Input signals, specified as an
*N*samp-by-*N*chan
matrix. *N*samp is the number of input samples
per channel and *N*chan is the number of
channels.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes
### Output

### **Out** — Output signal *N*out-by-1 vector

Output signal, returned as an *N*out-by-1
vector of the same data type as input signal `In`.
*N*out is the number of output samples. The
**Rate
options** parameter specifies single-rate or multirate mode. For more
information, see Algorithms.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Input sample rate (Hz)** — Input signal sample rate `1e6` (default) | positive scalar

Input signal sample rate in Hz, specified as a positive scalar.

### **Frequency offsets (Hz)** — Frequency offsets `[0 1e6]` (default) | scalar | 1-by-*N*chan vector

Frequency offsets in Hz, specified as one of these options.

- Scalar — Each channel of the input signal is frequency-shifted by this scalar
  value.
- 1-by-*N*chan vector — Each channel of
  the input signal is frequency-shifted by the corresponding value in this vector.
  *N*chan is the number of channels in the
  input signal `In`.

### **Rate options** — Options for processing rate `Enforce single-rate processing` (default) | `Allow multirate processing`

Options for the processing rate, specified as one of these values.

- `Enforce single-rate processing` — The output sample rate
  must be an integer multiple of the input sample rate. The number of rows in the
  output is higher than or equal to the number of rows in the input signal. The
  output frame rate is equal to the input frame rate.
- `Allow multirate processing` — The output has the same number
  of rows as the input. The output frame rate is higher than or equal to the input
  frame rate.

For more information, see the Algorithms section.

### **Output sample rate options** — Options for output sample rate `Auto` (default) | `Specify via property`

Options for the output sample rate, specified as one of these values.

- `Auto` — The block interpolates the input signals to ensure
  that the resulting sample rate of the signals is sufficient to avoid distorting the
  frequency content of the original signals after they are frequency-shifted to
  produce the output signal.
- `Specify via property` — Specify the output sample rate by
  using the **Output sample rate
  (Hz)** parameter.

### **Output sample rate (Hz)** — Output signal sample rate `3e6` (default) | positive scalar

Output signal sample rate in Hz, specified as a positive scalar.

#### Tips

To avoid distortion, specify this value to be greater than or equal to the
automatically computed output sample rate. To determine the automatically computed
output sample rate, first run the block with the **Output sample rate
options** parameter set to `Auto`.

#### Dependencies

To enable this parameter, set the **Output sample rate
options** parameter to `Specify via property`.

### **Output delay (samples)** — Output delay Read-only: `36` (default) | positive scalar

This parameter is read-only.

Output delay in samples, specified as a positive scalar.

## Libraries

Communications Toolbox / RF Impairments and Components

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Frequency-shift and combine signals

The Multiband Combiner block interpolates, shifts input signals to the specified frequency bands,
and then combines them into a single signal. For more information, see the Algorithms section.
