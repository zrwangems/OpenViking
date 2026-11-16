---
type: simulink-block
title: 'YAMNet'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'AI for Audio / Pretrained Models / YAMNet'
documentation_page: 'yamnetblock'
documentation_source_path: 'ref/yamnetblock.html'
language: en
---

# YAMNet

## Ports

### Input

### **features** — Mel spectrograms 96-by-64 matrix | 96-by-64-by-1-by-*N* array

Mel spectrograms, specified as a 96-by-64 matrix or a
96-by-64-by-1-by-*N* array, where:

- `96` –– Represents the number of 25 ms frames in each mel
  spectrogram
- `64` –– Represents the number of mel bands spanning 125 Hz to
  7.5 kHz
- *N* –– Number of channels.

You can use the YAMNet
Preprocess block to generate mel spectrograms. The dimensions of these
spectrograms are 96-by-64.

**Data Types:** `single` | `double`
### Output

### **sound** — Predicted sound label enumerated scalar

Predicted sound label, returned as an enumerated scalar.

**Data Types:** `enumerated`

### **scores** — Predicted activations or scores vector

Predicted activation or score values for each supported sound label, returned as a
1-by-521 vector, where 521 is the number of classes in YAMNet.

**Data Types:** `single`

### **labels** — Class labels for predicted scores vector

Class labels for predicted scores, returned as a 1-by-521 vector.

**Data Types:** `enumerated`

## Parameters

### **Mini-batch size** — Size of mini-batches `128` (default) | positive integer

Size of mini-batches to use for prediction, specified as a positive integer. Larger
mini-batch sizes require more memory, but can lead to faster predictions.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Classification** — Select to output sound classification `on` (default) | `off`

Enable the output port **sound**, which outputs the classified
sound.

### **Predictions** — Output all scores and associated labels `off` (default) | `on`

Enable the output ports **scores** and **labels**,
which output all predicted scores and associated class labels.

## Libraries

Audio Toolbox / Deep Learning

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

- To generate generic C code that does not depend on third-party libraries, in the
  **Configuration Parameters** > **Code
  Generation** general category, set the **Language**
  parameter to `C`.
- To generate C++ code, in the **Configuration Parameters** >
  **Code Generation** general category, set the
  **Language** parameter to `C++`. To
  specify the target library for code generation, in the **Code
  Generation** > **Interface** category, set the
  **Target Library** parameter. Setting this parameter to
  `None` generates generic C++ code that does not depend
  on third-party libraries.
- For a list of networks and layers supported for code generation, see Networks and Layers Supported for Code Generation (MATLAB Coder).

## Version History

**Introduced in R2021b**

## Description

YAMNet sound classification network

The YAMNet block leverages a pretrained sound classification network that
is trained on the AudioSet dataset to predict audio events from the AudioSet ontology.
