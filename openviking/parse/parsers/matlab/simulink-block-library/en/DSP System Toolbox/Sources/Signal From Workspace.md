---
type: simulink-block
title: 'Signal From Workspace'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'signalfromworkspace'
documentation_source_path: 'ref/signalfromworkspace.html'
language: en
---

# Signal From Workspace

## Ports
```yaml
ports:
- name: Port_1
  summary: Signal imported from workspace scalar | vector | matrix | 3-D array
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### Output

### **Port\_1** — Signal imported from workspace scalar | vector | matrix | 3-D array

Signal imported from workspace, as a scalar, vector, matrix, or 3-D
array.

When the **Signal** parameter specifies an
*M*-by-*N* matrix
(*M*≠1), each of the *N* columns
is treated as a distinct channel. You specify the frame size in the
**Samples per frame** parameter,
*M*o. The output is an
*M*o-by-*N*
matrix containing *M*o
consecutive samples from each signal channel. You specify the output
sample period in the **Sample time** parameter,
*T*s, and the output frame
period is
*M*o*T*s.
For convenience, an imported row vector (*M*=1) is
treated as a single channel, so the output dimension is
*M*o-by-1.

When the **Signal** parameter specifies an
*M*-by-*N*-by-*P*
array, each of the *P* pages (an
*M*-by-*N* matrix) is output in
sequence with period *T*s. The
**Samples per frame** parameter must be set to
`1`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## Parameters
```yaml
parameters:
- name: Signal
  summary: Signal to import 1:10 (default) | MATLAB workspace variable | MATLAB expression
  group: ''
- name: Sample time
  summary: Output sample period 1 (default) | scalar
  group: ''
- name: Samples per frame
  summary: Samples per frame 1 (default) | positive integer
  group: ''
- name: Form output after final data value by
  summary: Values to output after final imported signal value Setting to zero (default) | Holding final value | Cyclic repetition
  group: ''
- name: Warn when frame size does not evenly divide input length
  summary: Warn when input length is not an integer multiple of frame size off (default) | on
  group: ''
```

### **Signal** — Signal to import `1:10` (default) | MATLAB workspace variable | MATLAB expression

The name of the MATLAB workspace variable from which to import the signal, or a valid
MATLAB expression specifying the signal.

### **Sample time** — Output sample period `1` (default) | scalar

The sample period, *T*s, of the output, specified
as a scalar. The output frame period is
*M*o*T*s.

### **Samples per frame** — Samples per frame `1` (default) | positive integer

The number of samples, *M*o, to
buffer into each output frame, specified as a positive integer scalar. This
value must be `1` when you specify a 3-D array in the
**Signal** parameter.

### **Form output after final data value by** — Values to output after final imported signal value `Setting to zero` (default) | `Holding final value` | `Cyclic repetition`

Specifies the output after all of the specified signal samples have been
generated.

- When you specify `Setting To Zero`, the
  block generates zero-valued outputs for the duration of the
  simulation after generating the last frame of the signal.
- When you specify `Holding Final Value`,
  the block repeats the final sample for the duration of the
  simulation after generating the last frame of the signal.
- When you specify `Cyclic Repetition`, the
  block repeats the signal from the beginning after it reaches the
  last sample in the signal. If the frame size you specify in the
  **Samples per frame** parameter does not evenly
  divide the input length, a buffer block is inserted into the Signal
  From Workspace subsystem, and the model becomes multirate. If you do
  not want your model to become multirate, make sure that the frame
  size evenly divides the input signal length.

The block does not extrapolate the imported signal beyond the last
sample.

### **Warn when frame size does not evenly divide input length** — Warn when input length is not an integer multiple of frame size `off` (default) | `on`

Select the **Warn when frame size does not evenly divide input
length** parameter to be alerted when the input length is not
an integer multiple of the frame size. When the input length is not an
integer multiple of the frame size, the model becomes multirate. Use the
Model Explorer to turn these warnings on or off
model-wide:

1. In the **Modeling** tab, click **Model
   Explorer**.
2. In the **Search** bar of the Model
   Explorer, search `by Property
   Name` for the
   `ignoreOrWarnInputAndFrameLengths`
   property. Each block with the **Warn when frame size does
   not evenly divide input length** check box appears in
   the list in the **Contents** pane.
3. Select each of the blocks for which you want to toggle the warning
   parameter, and select or clear the check box in the
   `ignoreOrWarnInputAndFrameLengths`
   column.

#### Dependencies

To enable this parameter set **Form output after final data
value by** to `Cyclic
Repetition`.
## Libraries

DSP System Toolbox / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Import signal from MATLAB workspace

The Signal From Workspace block imports a signal from the MATLAB® workspace into the Simulink® model. The **Signal** parameter specifies the name of a
MATLAB workspace variable containing the signal to import, or any valid
MATLAB expression defining a matrix or 3-D array.

Unlike the Simulink
From Workspace (Simulink) block, the Signal
From Workspace block holds the output value constant between successive
output frames (that is, no linear interpolation takes place). Also, the initial signal
values are always produced immediately at *t*=0.
