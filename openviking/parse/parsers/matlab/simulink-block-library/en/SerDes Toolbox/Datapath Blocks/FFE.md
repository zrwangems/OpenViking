---
type: simulink-block
title: 'FFE'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Datapath Blocks'
documentation_page: 'ffe'
documentation_source_path: 'ref/ffe.html'
language: en
---

# FFE

## Ports

### Input

### **WaveIn** — Input baseband signal scalar | vector

Input baseband signal. The input signal can be a sample-by-sample signal specified
as a scalar, or an impulse response vector signal.

**Data Types:** `double`
### Output

### **WaveOut** — Estimated channel output scalar | vector

Estimated channel output. If the input signal is a sample-by-sample signal
specified as a scalar, the output is also scalar. If the input signal is an impulse
response vector signal, the output is also a vector.

**Data Types:** `double`

## Parameters

### **Mode** — FFE operating mode `Fixed` (default) | `Off`

FFE operating mode:

- `Off` — FFE is bypassed and the input
  waveform remains unchanged.
- `Fixed` — FFE applies the FFE tap
  weights specified in **Tap weights** to input waveform.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Mode` |
| **Type:** character vector |
| **Values:** `Fixed` | `Off` |
| **Default:** `Fixed` |

### **Tap Spacing** — Fractional taps for sub-symbol equalization control `T-spaced` (default) | `T/2-spaced` | `T/4-spaced`

Fractional taps for sub-symbol equalization control, specified as
`T-spaced`, `T/2-spaced`, or
`T/4-spaced`. *T* represents the symbol
time.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `TapSpacing` |
| **Type:** character vector |
| **Values:** `T-spaced` | `T/2-spaced` | `T/4-spaced` |
| **Default:** `T-spaced` |

### **Tap weights** — FFE tap weights `[0,1,0,0,0]` (default) | row vector

FFE tap weights, specified as a row vector in volts. The length of the vector
specifies the number of taps. The vector element value specifies the strength of the tap
at that element position. The tap with the largest magnitude is the main tap and
therefore defines the number of pre- and post-cursor taps.

You can use a valid MATLAB expression to evaluate the **Initial tap weights
(V)** row vector.

**Example:** `set_param(gcb,'TapWeights',"zeros[(1,4) 1 zeros(1,15)]")`
creates an FFE with 20 taps where the fifth tap is the main tap.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `TapWeights` |
| **Type:** character vector |
| **Values:** row vector |
| **Default:** `[0,1,0,0,0]` |

- Use `get_param(gcb,'TapWeights')` to view the current FFE
  **Tap weights**.
- Use `set_param(gcb,'TapWeights',value)` to set FFE to a
  specific **Tap weights** vector.

**Data Types:** `double`

### **Normalize** — Normalize tap weights on (default) | fff

Select to normalize tap weight vectors so that the sum of the absolute values of the
**Tap weights** vector elements is one.

### **Visualize Response** — Plot FFE FIR filter response button

Click to plot the response of the FFE FIR (finite impulse response) filter.

#### IBIS-AMI parameters

### **Mode** — Include Mode parameter in IBIS-AMI model on (default) | off

Select to include **Mode** as a parameter in the IBIS-AMI file. If
you deselect **Mode**, it is removed from the AMI files, effectively
hard-coding **Mode** to its current value.

### **Tap weights** — Include Tap weights parameter in IBIS-AMI model on (default) | off

Select to include **Tap weights** as a parameter in the IBIS-AMI
file. If you deselect **Tap weights**, it is removed from the AMI
files, effectively hard-coding **Tap weights** to its current
value.

## Libraries

SerDes Toolbox / Datapath Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Models a feed-forward equalizer

The FFE block applies a feed-forward equalizer (FFE) as a finite-impulse
response (FIR) filter to a sample-by-sample input signal or an impulse response vector input
signal. This filtering reduces distortions due to channel loss impairments.
