---
type: simulink-block
title: 'Sound Classifier'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning'
documentation_page: 'soundclassifier'
documentation_source_path: 'ref/soundclassifier.html'
language: en
---

# Sound Classifier

## Ports
```yaml
ports:
- name: audioIn
  summary: Sound data column vector
  direction: input
  data_types: single | double
- name: sound
  summary: Predicted sound label enumerated scalar
  direction: output
  data_types: enumerated
- name: scores
  summary: Predicted activations or scores vector
  direction: output
  data_types: single
- name: labels
  summary: Class labels for predicted scores vector
  direction: output
  data_types: enumerated
```

### Input

### **audioIn** — Sound data column vector

Sound data to classify, specified as a one-channel signal (column
vector). If **Sample rate of input signal (Hz)** is
16e3, there are no restrictions on the input frame length. If
**Sample rate of input signal (Hz)** is different
from 16e3, then the input frame length must be a multiple of the
decimation factor of the resampling operation that the block performs.
If the input frame length does not satisfy this condition, the block
throws an error message with information on the decimation
factor.

**Data Types:** `single` | `double`
### Output

### **sound** — Predicted sound label enumerated scalar

Predicted sound label, returned as an enumerated scalar.

**Data Types:** `enumerated`

### **scores** — Predicted activations or scores vector

Predicted activation or score values for each supported sound label,
returned as a 1-by-521 vector, where 521 is the number of classes in
YAMNet.

**Data Types:** `single`

### **labels** — Class labels for predicted scores vector

Class labels for predicted scores, returned as a 1-by-521
vector.

**Data Types:** `enumerated`
## Parameters
```yaml
parameters:
- name: Sample rate of input signal (Hz)
  summary: Sample rate of input signal in Hz 16e3 (default) | positive scalar
  group: ''
- name: Overlap percentage (%)
  summary: Overlap percentage between consecutive mel spectrograms 50 (default) | [0 100)
  group: ''
- name: Classification
  summary: Select to output sound classification on (default) | off
  group: ''
- name: Predictions
  summary: Output all scores and associated labels off (default) | on
  group: ''
```

### **Sample rate of input signal (Hz)** — Sample rate of input signal in Hz `16e3` (default) | positive scalar

Specify the sample rate of the input signal as a positive scalar in Hz. If
the sample rate is different from 16e3, then the block resamples the signal
to 16e3, which is the sample rate that YAMNet supports.

**Data Types:** `single` | `double`

### **Overlap percentage (%)** — Overlap percentage between consecutive mel spectrograms `50` (default) | [0 100)

Specify the overlap percentage between consecutive mel spectrograms as a
scalar in the range [0 100).

**Data Types:** `single` | `double`

### **Classification** — Select to output sound classification `on` (default) | `off`

Enable the output port **sound**, which outputs the
classified sound.

### **Predictions** — Output all scores and associated labels `off` (default) | `on`

Enable the output ports **scores** and
**labels**, which output all predicted scores and
associated class labels.
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

Classify sounds in audio signal

The Sound Classifier block uses YAMNet to classify audio segments into sound
classes described by the AudioSet ontology. The Sound Classifier block
combines necessary audio preprocessing and YAMNet network inference. The block returns
predicted sound labels, predicted scores from the sounds, and class labels for predicted
scores.
