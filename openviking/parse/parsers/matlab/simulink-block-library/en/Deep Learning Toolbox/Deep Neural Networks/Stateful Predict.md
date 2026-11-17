---
type: simulink-block
title: 'Stateful Predict'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Neural Networks'
documentation_page: 'statefulpredict'
documentation_source_path: 'ref/statefulpredict.html'
language: en
---

# Stateful Predict

## Ports
```yaml
ports:
- name: input
  summary: Sequence or time series data numeric array
  direction: input
- name: output
  summary: Predicted scores or responses numeric array
  direction: output
```

### Input

### **input** — Sequence or time series data numeric array

The input ports of the Stateful Predict block takes the names of
the input layers of the network loaded. Based on the network loaded, the input to the
predict block can be sequence or time series data.

The dimensions of the numeric arrays containing the sequences depend on the type
of data.

| Input | Description |
| --- | --- |
| Vector sequences | *s*-by-*c* matrices, where *s* is the sequence length, and *c* is the number of features of the sequences. |
| 2-D image sequences | *h*-by-*w*-by-*c*-by-*s* arrays, where *h*, *w*, and *c* correspond to the height, width, and number of channels of the images, respectively, and *s* is the sequence length. |
### Output

### **output** — Predicted scores or responses numeric array

The outputs port of the Stateful Predict block takes the names of
the output layers of the network loaded. Based on the network loaded, the output of
the Stateful Predict block can represent predicted scores or responses.

For sequence-to-label classification, the output is a
*K*-by-*N* matrix, where *K* is
the number of classes, and *N* is the number of observations.

For sequence-to-sequence classification problems, the output is a
*K*-by-*S* matrix of scores, where
*K* is the number of classes, and *S* is the total
number of time steps in the corresponding input sequence.
## Parameters
```yaml
parameters:
- name: Network
  summary: Source for trained recurrent neural network Network from MAT-file (default) | Network from MATLAB function
  group: ''
  block_parameter: Network
  type: character vector, string
  values: '''Network from MAT-file'' | ''Network from MATLAB function'''
  default: '''Network from MAT-file'''
- name: File path
  summary: MAT file containing trained recurrent neural network untitled.mat (default) | MAT file name
  group: ''
  block_parameter: NetworkFilePath
  type: character vector, string
  values: MAT file path or name
  default: '''untitled.mat'''
- name: MATLAB function
  summary: MATLAB function name untitled (default) | MATLAB function name
  group: ''
  block_parameter: NetworkFunction
  type: character vector, string
  values: MATLAB function name
  default: '''untitled'''
- name: Sample time
  summary: Output sample period and optional time offset -1 (default) | scalar | vector
  group: ''
  block_parameter: SampleTime
  type: character vector
  values: scalar | vector
  default: '''-1'''
- name: Input data formats
  summary: Input data format of dlnetwork character vector | string
  group: ''
  block_parameter: InputDataFormats
  type: character vector, string
  values: 'For a network with one or more inputs, use character vector in the form of: {''inputlayerName1'', ''SSC''; ''inputlayerName2'',
    ''SSCB''; ...}''. For a network with no input layer and multiple input ports, use character vector in the form of: ''{''inputportName1/inport1,
    ''SSC''; ''inputportName2/inport2, ''SSCB''; ...}''.'
  default: Data format that the network expects. For more information, see Deep Learning Data Formats.
```

### **Network** — Source for trained recurrent neural network `Network from MAT-file` (default) | `Network from MATLAB function`

Specify the source for the trained recurrent neural network. The trained network
must have at least one recurrent layer (for example, an LSTM network). Select one of the following:

- `Network from MAT-file`— Import a trained recurrent
  neural network from a MAT-file containing a `dlnetwork` object.
- `Network from MATLAB function`— Import a pretrained
  recurrent neural network from a MATLAB function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Network` |
| **Type:** character vector, string |
| **Values:** `'Network from MAT-file'` | `'Network from MATLAB function'` |
| **Default:** `'Network from MAT-file'` |

### **File path** — MAT file containing trained recurrent neural network `untitled.mat` (default) | MAT file name

This parameter
specifies the name of the MAT file that contains the trained
recurrent neural network to load. If the file is not on the
MATLAB path, use the **Browse** button to
locate the file.

#### Dependencies

To enable this parameter, set the **Network**
parameter to `Network from MAT
file`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NetworkFilePath` |
| **Type:** character vector, string |
| **Values:** MAT file path or name |
| **Default:**  `'untitled.mat'` |

### **MATLAB function** — MATLAB function name `untitled` (default) | MATLAB function name

This parameter specifies the name of the MATLAB function for the pretrained recurrent neural network.

#### Dependencies

To enable this parameter, set the **Network** parameter to `Network from MATLAB function`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NetworkFunction` |
| **Type:** character vector, string |
| **Values:** MATLAB function name |
| **Default:** `'untitled'` |

### **Sample time** — Output sample period and optional time offset `-1` (default) | scalar | vector

The **Sample time** parameter specifies when the block computes a new output value during simulation. For details, see Specify Sample Time (Simulink).

Specify the **Sample time** parameter as a scalar when you do not want the output to have a time offset. To add a time offset to the output, specify the **Sample time** parameter as a `1`-by-`2` vector where the first element is the sampling period and the second element is the offset.

By default, the **Sample time** parameter value is `-1` to inherit the value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'-1'` |

### **Input data formats** — Input data format of `dlnetwork` character vector | string

This parameter specifies the input data format expected by the trained `dlnetwork`.

Data format, specified as a string scalar or a character vector. Each character in
the string must be one of these dimension labels:

- `"S"` — Spatial
- `"C"` — Channel
- `"B"` — Batch
- `"T"` — Time
- `"U"` — Unspecified

For example, for an array containing a batch of sequences where the first, second,
and third dimension correspond to channels, observations, and time steps, respectively,
you can specify that it has the format `"CBT"`.

You can specify multiple dimensions labeled `"S"` or `"U"`.
You can use the labels `"C"`, `"B"`, and
`"T"` once each, at most. The software ignores singleton trailing
`"U"` dimensions after the second dimension.

For more information, see Deep Learning Data Formats.

By default, the parameter uses the data format that the network expects.

#### Dependencies

To enable this parameter, set the **Network** parameter to
`Network from MAT-file` to import a trained `dlnetwork` object from a
MAT-file.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputDataFormats` |
| **Type:** character vector, string |
| **Values:** For a network with one or more inputs, use character vector in the form of: `{'inputlayerName1', 'SSC'; 'inputlayerName2', 'SSCB'; ...}'`. For a network with no input layer and multiple input ports, use character vector in the form of: `'{'inputportName1/inport1, 'SSC'; 'inputportName2/inport2, 'SSCB'; ...}'`. |
| **Default:** Data format that the network expects. For more information, see Deep Learning Data Formats. |
## Libraries

Deep Learning Toolbox / Deep Neural Networks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

- To generate generic C code that does not depend on third-party libraries, in the
  **Configuration Parameters** > **Code Generation**
  general category, set the **Language** parameter to
  `C`.
- To generate C++ code, in the **Configuration Parameters** >
  **Code Generation** general category, set the
  **Language** parameter to `C++`. To
  specify the target library for code generation, in the **Code
  Generation** > **Interface** category, set the
  **Target Library** parameter. Setting this parameter to
  `None` generates generic C++ code that does not depend on
  third-party libraries.
- For ERT-based targets, the **Support: variable-size signals**
  parameter in the **Code Generation**>
  **Interface** pane must be enabled.
- For a list of networks and layers supported for code generation, see Networks and Layers Supported for Code Generation (MATLAB Coder).

### GPU Code Generation Generate CUDA® code for NVIDIA® GPUs using GPU Coder™.

Usage notes and limitations:

- The **Language** parameter in the **Configuration
  Parameters** > **Code Generation** general category must
  be set to `C++`.
- GPU code generation supports this block only when targeting the cuDNN
  library.

## Version History

**Introduced in R2021a**

### R2024a: `SeriesNetwork` and `DAGNetwork` are not recommended

Starting in R2024a, the `SeriesNetwork` and `DAGNetwork`
objects are not recommended. This recommendation means that `SeriesNetwork`
and `DAGNetwork` inputs to the Stateful Predict block are not
recommended. Use the `dlnetwork` objects instead.
`dlnetwork` objects have these advantages:

- `dlnetwork` objects are a unified data type that supports network building, prediction, built-in training, visualization, compression, verification, and custom training loops.
- `dlnetwork` objects support a wider range of network architectures that you can create or import from external platforms.
- The `trainnet` function supports `dlnetwork` objects, which enables you to easily specify loss functions. You can select from built-in loss functions or specify a custom loss function.
- Training and prediction with `dlnetwork` objects is typically faster than `LayerGraph` and `trainNetwork` workflows.

Simulink block models with `dlnetwork` objects behave differently. The
predicted scores are returned as a *K*-by-*N* matrix, where *K* is the
number of classes, and *N* is the number of observations.
If you have an existing Simulink block model with a `SeriesNetwork` or
`DAGNetwork` object, follow these steps to use a `dlnetwork` object instead:

1. Convert the `SeriesNetwork` or `DAGNetwork` object to
   a `dlnetwork` using the `dag2dlnetwork` function.
2. If the input to your block is a vector sequence, transpose the matrix using a
   transpose block to a size *s*-by-*c*, where
   *s* is the sequence length, and *c* is the number of
   features of the sequences.
3. Transpose the predicted scores using a transpose block to an
   *N*-by-*K* array, where *N* is the
   number of observations, and *K* is the number of classes.

## Description

Predict responses using a trained recurrent neural network

The Stateful Predict block predicts responses for the data at the input by
using the trained recurrent neural network specified through the block parameter. This block
allows loading of a pretrained network into the Simulink® model from a MAT-file or from a MATLAB® function. This block updates the state of the network with every
prediction.

To reset the state of recurrent neural network to its initial state, place the
Stateful Predict block inside a Resettable Subsystem (Simulink) block and use the `Reset` control signal as
trigger.
