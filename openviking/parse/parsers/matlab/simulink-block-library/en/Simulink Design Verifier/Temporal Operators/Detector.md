---
type: simulink-block
title: 'Detector'
family: 'sldv'
product_id: 'sldv'
product_name: 'Simulink Design Verifier'
documentation_release: R2025b
official_category: 'Temporal Operators'
documentation_page: 'detector'
documentation_source_path: 'ref/detector.html'
language: en
---

# Detector

## Ports

### Input

### **Port\_1** — Input signal specified as boolean boolean

The inputs of the Detector block are of boolean
type.

**Data Types:** `Boolean`
### Output

### **Port\_1** — Output signal returns as boolean boolean

The outputs of the Detector block are of boolean
type.

**Data Types:** `Boolean`

## Parameters

### **External reset** — whether the block can be reset off (default) | on

Specify whether the block can be reset to the start of the input detection
by an external Boolean reset signal.

### **Output type** — specify a fixed true duration length for the output `Delayed fixed duration` (default) | `Synchronized`

Select `Delayed Fixed Duration` (the default) to
specify a fixed true duration length for the output after an optional delay.
Select `Synchronized` to synchronize the output
true duration with that of the input.

### **Time steps for input detection** — Length of the true duration for input detection `2` (default) | boolean

Length of the true duration for input detection (minimum is
`1`).

### **Time steps for delay** — specify the length of the delay duration `1` (default) | boolean

For `Delayed Fixed Duration`, optionally specify
the length of the delay duration, after which the output becomes
true.

### **Time steps for output durations** — specify the length of the output true duration `3` (default) | boolean

For `Delayed Fixed Duration`, specify the length
of the output true duration (minimum is
`1`).

## Libraries

Simulink Design Verifier / Temporal Operators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2011a**

## Description

Detect true duration on input and construct output true duration based on output type

This block detects a fixed number of consecutive time steps where the input signal is
true and constructs an output signal based on the selected output type. The terminology
used to explain the detector block is given below:

- *True duration* of a signal — Consecutive time
  steps during which a signal is true
- *Length* of the true duration of the signal —
  The number of time steps that constitute the true duration
- *Input detection* phase — The phase that is
  complete at the final time step of the expected length of the input true
  duration
- *Output construction* phase— The phase when
  the block constructs a true duration at the output based on the output type
  of the block
- *Delay duration* — The number of time steps of
  delay after input detection, after which the output signal is true

On input detection, the Detector block constructs an output signal
based on one of the two output types that you specify:

- `Delayed Fixed Duration`—After the input
  detection is complete and after an optional delay, the output signal becomes
  `true` for a fixed number of time steps. The true
  duration of the output is independent of the input.
- `Synchronized`—In the final time step of
  the input detection, the output becomes `true` and stays
  `true` as long as the input signal continues to be
  `true`. The true duration of the output varies and is
  synchronized with the true duration of the input.
