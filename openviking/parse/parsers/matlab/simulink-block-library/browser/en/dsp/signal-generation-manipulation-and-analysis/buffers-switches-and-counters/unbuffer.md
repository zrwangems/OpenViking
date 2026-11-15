---
type: simulink-block
title: 'Unbuffer'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Buffers, Switches, and Counters'
documentation_page: 'unbuffer'
documentation_source_path: 'ref/unbuffer.html'
language: en
---

# Unbuffer

## Ports

### Input

### **Input** — Input signal scalar | vector | matrix

Specify the signal to unbuffer as a scalar, vector, or a matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Output** — Unbuffered signal scalar | row vector

The Unbuffer block unbuffers an
*M*i-by-*N*
input into a `1`-by-*N* output. The
block unbuffers the inputs row-wise so that each matrix row becomes an
independent time-sample in the output.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### **Initial conditions** — Initial conditions `0` (default) | scalar | vector | matrix

Specify the block's initial output for cases of nonzero latency as a:

- Scalar to be repeated for the first
  *M*i output samples
  of every channel
- Length-*M*i vector
  containing the values of the first
  *M*i output samples
  for every channel
- *M*i-by-*N*
  matrix containing the values of the first
  *M*i output samples
  in each of *N* channels

**Note**

For more information on latency and the Simulink® tasking modes, see Excess Algorithmic Delay (Tasking Latency) and Time-Based Scheduling and Code Generation (Simulink Coder).

## Libraries

DSP System Toolbox / Signal Management / Buffers

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The Unbuffer block supports code generation for Simulink
Real-Time™. The code generated for this
target is executed concurrently. To generate this code, set the system target file
of the model to `speedgoat.tlc` or to any other target file
supported by Simulink
Real-Time..

To set the system target file:

1. In the Simulink model window, on the **Modeling** tab,
   click **Model Settings**.
2. In the Model Settings > **Code Generation** pane, set
   the **System target file** to
   `speedgoat.tlc` or to any other target file
   supported by Simulink
   Real-Time.

## Version History

**Introduced before R2006a**

## Description

Unbuffer input frame into sequence of scalar outputs

The Unbuffer block unbuffers an
*M*i-by-*N* input into a
`1`-by-*N* output. The block unbuffers the input
row-wise so that each matrix row becomes an independent time-sample in the output. The
rate at which the block receives inputs is generally less than the rate at which the
block produces outputs.

For example, consider this illustration. The block receives inputs only once every
three sample periods, but produces an output once every sample period. To rebuffer
inputs to a larger or smaller frame size, use the Buffer block.

The block adjusts the output rate so that the *sample period* is the same
at both the input and output, *T*so =
*T*si. Therefore, the output sample period
for an input of frame size *M*i and frame period
*T*fi is
Tfi/*M*i, which
represents a rate *M*i times higher than the
input frame rate.

In the following illustration, the block unbuffers a four-channel input with a frame size of
three. The **Initial conditions** parameter is set to zero and the
tasking mode is set to multitasking, so the first three outputs are zero vectors.
