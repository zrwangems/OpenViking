---
type: simulink-block
title: 'Predict'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Neural Networks'
documentation_page: 'predict'
documentation_source_path: 'ref/predict.html'
language: en
---

# Predict

## Ports
```yaml
ports:
- name: input
  summary: Image, feature, sequence, or time series data numeric array
  direction: input
- name: output
  summary: Predicted scores, responses, or activations numeric array
  direction: output
```

### Input

### **input** — Image, feature, sequence, or time series data numeric array

The input ports of the Predict block takes the names of the input
layers of the loaded network. For example, if you specify
`imagePretrainedNetwork` for `MATLAB
function`, then the input port of the Predict block has the
label **data**. Based on the network loaded, the input to the predict
block can be image, sequence, or time series data.

The layout of the input depend on the type of data.

| Data | Layout of Predictors |
| --- | --- |
| 2-D images | A *h*-by-*w*-by-*c*-by-*N* numeric array, where *h*, *w*, and *c* are the height, width, and number of channels of the images, respectively, and *N* is the number of images. |
| Vector sequences | *s*-by-*c* matrices, where *s* is the sequence length, and *c* is the number of features of the sequences. |
| 2-D image sequences | *h*-by-*w*-by-*c*-by-*s* arrays, where *h*, *w*, and *c* correspond to the height, width, and number of channels of the images, respectively, and *s* is the sequence length. |
| Features | A *N*-by-`numFeatures` numeric array, where *N* is the number of observations, and `numFeatures` is the number of features of the input data. |

If the array contains `NaN`s, then they are propagated through
the network.
### Output

### **output** — Predicted scores, responses, or activations numeric array

The outputs port of the Predict block takes the names of the output
layers of the network loaded. For example, if you specify
`imagePretrainedNetwork` for `MATLAB
function`, then the output port of the Predict block is
labeled **prob\_flatten**. Based on the network loaded, the output of
the Predict block can represent predicted scores or responses.

The predicted scores or responses is returned as a
*K*-by-*N* array, where *K* is
the number of classes, and *N* is the number of observations.

If you enable `Activations` for a network layer, the
Predict block creates a new output port with the name of the selected
network layer. This port outputs the activations from the selected network
layer.

The activations from the network layer is returned as a numeric array. The format
of output depends on the type of input data and the type of layer output.

For 2-D image output, activations is an
*h*-by-*w*-by-*c*-by-*n*
array, where *h*, *w*, and *c* are
the height, width, and number of channels for the output of the chosen layer,
respectively, and *n* is the number of images.

For a single time-step containing vector data, activations is a
*c*-by-*n* matrix, where *c* is
the number of features in the sequence and *n* is the number of
sequences.

For a multi time-step containing vector data, activations is a
*c*-by-*n*-by-*s* matrix, where
*c* is the number of features in the sequence, *n*
is the number of sequences and *s* is the sequence length.

For a single time-step containing 2-D image data, activations is a
*h*-by-*w*-by-*c*-by-*n*
array, where *n* is the number of sequences, *h*,
*w*, and *c* are the height, width, and the number
of channels of the images, respectively.
## Parameters
```yaml
parameters:
- name: Network
  summary: Source for trained network Network from MAT file (default) | Network from MATLAB function
  group: ''
  block_parameter: Network
  type: character vector, string
  values: '''Network from MAT file'' | ''Network from MATLAB function'''
  default: '''Network from MAT file'''
- name: File path
  summary: MAT file containing trained network untitled.mat (default) | MAT file path or name
  group: ''
  block_parameter: NetworkFilePath
  type: character vector, string
  values: MAT file path or name
  default: '''untitled.mat'''
- name: MATLAB function
  summary: MATLAB function name squeezenet (default) | MATLAB function name
  group: ''
  block_parameter: NetworkFunction
  type: character vector, string
  values: MATLAB function name
  default: '''squeezenet'''
- name: Mini-batch size
  summary: Size of mini-batches 128 (default) | positive integer
  group: ''
  block_parameter: MiniBatchSize
  type: character vector, string
  values: positive integer
  default: '''128'''
- name: Predictions
  summary: Output predicted scores or responses on (default) | off
  group: ''
  block_parameter: Predictions
  type: character vector, string
  values: '''off'' | ''on'''
  default: '''on'''
- name: Input data formats
  summary: Input data format of dlnetwork character vector | string
  group: ''
  block_parameter: InputDataFormats
  type: character vector, string
  values: 'For a network with one or more inputs, specify text in the form of: "{''inputlayerName1'', ''SSC''; ''inputlayerName2'',
    ''SSCB''; ...}". For a network with no input layer and multiple input ports, specify text in the form of: "{''inputportName1/inport1,
    ''SSC''; ''inputportName2/inport2, ''SSCB''; ...}".'
  default: Data format that the network expects. For more information, see Deep Learning Data Formats.
- name: Activations
  summary: Output network activations for a specific layer layers of the network
  group: ''
  block_parameter: Activations
  type: character vector, string
  values: character vector in the form of '{'layerName1',layerName2',...}'
  default: ''''''
```

### **Network** — Source for trained network `Network from MAT file` (default) | `Network from MATLAB function`

Specify the source for the trained network. Select one of the following:

- `Network from MAT file`— Import a
  trained network from a MAT file containing a `dlnetwork`
  object.
- `Network from MATLAB function`—
  Import a pretrained network from a MATLAB function. For
  example, to use a pretrained GoogLeNet, create a function
  `pretrainedGoogLeNet` in a MATLAB M-file,
  and then import this function.

  ```
  function net = pretrainedGoogLeNet
    net = imagePretrainedNetwork("googlenet");
  end
  ```

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Network` |
| **Type:** character vector, string |
| **Values:** `'Network from MAT file'` | `'Network from MATLAB function'` |
| **Default:** `'Network from MAT file'` |

### **File path** — MAT file containing trained network `untitled.mat` (default) | MAT file path or name

This parameter
specifies the name of the MAT file that contains the trained deep
learning network to load. If the file is not on the MATLAB path, use the **Browse** button to
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

### **MATLAB function** — MATLAB function name `squeezenet` (default) | MATLAB function name

This parameter specifies the name of the MATLAB function for the pretrained deep learning
network. For example, to use a pretrained GoogLeNet, create a function
`pretrainedGoogLeNet` in a MATLAB M-file, and then import this
function.

```
function net = pretrainedGoogLeNet
  net = imagePretrainedNetwork("googlenet");
end
```

#### Dependencies

To enable this parameter, set the **Network** parameter to `Network from MATLAB function`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NetworkFunction` |
| **Type:** character vector, string |
| **Values:** MATLAB function name |
| **Default:** `'squeezenet'` |

### **Mini-batch size** — Size of mini-batches 128 (default) | positive integer

Size of mini-batches to use for prediction, specified as a positive integer. Larger mini-batch sizes require more memory, but can lead to faster predictions.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MiniBatchSize` |
| **Type:** character vector, string |
| **Values:** positive integer |
| **Default:** `'128'` |

### **Predictions** — Output predicted scores or responses `on` (default) | `off`

Enable output ports that return predicted scores or
responses.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Predictions` |
| **Type:** character vector, string |
| **Values:** `'off'` | `'on'` |
| **Default:** `'on'` |

### **Input data formats** — Input data format of `dlnetwork` character vector | string

This parameter specifies the input data format expected by the
trained `dlnetwork`.

Data format, specified as a string scalar or a character vector.
Each character in the string must be one of the following dimension
labels:

- `"S"` — Spatial
- `"C"` — Channel
- `"B"` — Batch
- `"T"` — Time
- `"U"` — Unspecified

For example, for an array containing a batch of sequences where
the first, second, and third dimension correspond to channels,
observations, and time steps, respectively, you can specify that it
has the format `"CBT"`.

You can specify multiple dimensions labeled `"S"` or `"U"`.
You can use the labels `"C"`, `"B"`, and
`"T"` once each, at most. The software ignores singleton trailing
`"U"` dimensions after the second dimension.

For more information, see Deep Learning Data Formats.

By default, the parameter uses the data format that the network
expects.

#### Dependencies

To enable this parameter, set the **Network**
parameter to `Network from MAT file` to
import a trained `dlnetwork` object
from a MAT file.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputDataFormats` |
| **Type:** character vector, string |
| **Values:** For a network with one or more inputs, specify text in the form of: `"{'inputlayerName1', 'SSC'; 'inputlayerName2', 'SSCB'; ...}"`. For a network with no input layer and multiple input ports, specify text in the form of: `"{'inputportName1/inport1, 'SSC'; 'inputportName2/inport2, 'SSCB'; ...}"`. |
| **Default:** Data format that the network expects. For more information, see Deep Learning Data Formats. |

### **Activations** — Output network activations for a specific layer layers of the network

Use the **Activations** list to select the
layer to extract features from. The selected layers appear as an
output port of the Predict block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Activations` |
| **Type:** character vector, string |
| **Values:** character vector in the form of `'{'layerName1',layerName2',...}'` |
| **Default:** `''` |
## Libraries

Deep Learning Toolbox / Deep Neural Networks

## Block Characteristics

Not documented in R2025b.

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

### GPU Code Generation Generate CUDA® code for NVIDIA® GPUs using GPU Coder™.

Usage notes and limitations:

- The **Language** parameter in the **Configuration
  Parameters** > **Code Generation** general category must
  be set to `C++`.
- For a list of networks and layers supported for CUDA® code generation, see Supported Networks, Layers, and Classes (GPU Coder).
- To learn more about generating code for Simulink models containing the Predict block, see Code Generation for a Deep Learning Simulink Model That Performs Lane and Vehicle Detection (GPU Coder).

## Version History

**Introduced in R2020b**

### R2024a: `SeriesNetwork` and `DAGNetwork` are not recommended

Starting in R2024a, the `SeriesNetwork` and `DAGNetwork`
objects are not recommended. This recommendation means that `SeriesNetwork`
and `DAGNetwork` inputs to the Predict block are not
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

Predict responses using a trained deep learning neural network

The Predict block predicts responses for the data at
the input by using the trained network specified through the block
parameter. This block allows loading of a pretrained network into the
Simulink® model from a MAT file or from a MATLAB® function.

**Note**

Use the Predict block to make predictions in Simulink. To make predictions programmatically using MATLAB code, use the `minibatchpredict`
or `predict` function.
