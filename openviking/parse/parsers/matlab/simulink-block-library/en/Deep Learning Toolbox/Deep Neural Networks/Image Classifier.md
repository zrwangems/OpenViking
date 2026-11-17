---
type: simulink-block
title: 'Image Classifier'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Neural Networks'
documentation_page: 'imageclassifier'
documentation_source_path: 'ref/imageclassifier.html'
language: en
---

# Image Classifier

## Ports
```yaml
ports:
- name: image
  summary: Image or feature data numeric array
  direction: input
- name: ypred
  summary: Predicted class labels enumerated
  direction: output
- name: scores
  summary: Predicted class scores matrix
  direction: output
- name: labels
  summary: Class labels for predicted scores matrix
  direction: output
```

### Input

### **image** — Image or feature data numeric array

A
*h*-by-*w*-by-*c*-by-*N*
numeric array, where *h*, *w*, and
*c* are the height, width, and number of channels of the images,
respectively, and *N* is the number of images.

A *N*-by-`numFeatures` numeric array, where
*N* is the number of observations and
`numFeatures` is the number of features of the input data.

If the array contains `NaN`s, then they are propagated through
the network.
### Output

### **ypred** — Predicted class labels enumerated

Predicted class labels with the highest score, returned as a
*N*-by-1 enumerated vector of labels, where *N* is
the number of observations.

### **scores** — Predicted class scores matrix

Predicted scores, returned as a *K*-by-*N*
matrix, where *K* is the number of classes, and *N*
is the number of observations.

### **labels** — Class labels for predicted scores matrix

Labels associated with the predicted scores, returned as a
*N*-by-*K* matrix, where *N* is
the number of observations, and *K* is the number of classes.
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
- name: Resize input
  summary: Resize input dimensions on (default) | off
  group: ''
  block_parameter: ResizeInput
  type: character vector, string
  values: '''off'' | ''on'''
  default: '''on'''
- name: Classification
  summary: Output predicted label with highest score on (default) | off
  group: ''
  block_parameter: Classification
  type: character vector, string
  values: '''off'' | ''on'''
  default: '''on'''
- name: Predictions
  summary: Output all scores and associated labels off (default) | on
  group: ''
  block_parameter: Predictions
  type: character vector, string
  values: '''off'' | ''on'''
  default: '''off'''
- name: Class names workspace variable
  summary: Workspace variable containing class names of the network output classNames (default) | categorical vector variable
    | string array variable | cell array of character vectors variable name
  group: ''
  block_parameter: classNames
  type: variable name of a categorical vector, a string array, or a cell array of character vectors.
  values: Name of a variable containing class names, specified as a categorical vector, a string array, or a cell array of
    character vectors.
  default: The workspace variable classNames.
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

### **Resize input** — Resize input dimensions `on` (default) | `off`

Resize the data at the input port to the input size of the
network.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ResizeInput` |
| **Type:** character vector, string |
| **Values:** `'off'` | `'on'` |
| **Default:** `'on'` |

### **Classification** — Output predicted label with highest score `on` (default) | `off`

Enable output port `ypred` that outputs the label with the highest score.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Classification` |
| **Type:** character vector, string |
| **Values:** `'off'` | `'on'` |
| **Default:** `'on'` |

### **Predictions** — Output all scores and associated labels `off` (default) | `on`

Enable output ports `scores` and `labels` that output all predicted scores and associated class labels.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Predictions` |
| **Type:** character vector, string |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Class names workspace variable** — Workspace variable containing class names of the network output `classNames` (default) | categorical vector variable | string array variable | cell array of character vectors variable name

Variable containing class names, specified as a categorical
vector, a string array, or a cell array of character vectors.

The output size of the network must match the number of classes.

#### Dependencies

To enable this parameter, set the **Network**
parameter to `Network from MAT file` to
import a trained `dlnetwork` object
from a MAT file.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `classNames` |
| **Type:**variable name of a categorical vector, a string array, or a cell array of character vectors. |
| **Values:** Name of a variable containing class names, specified as a categorical vector, a string array, or a cell array of character vectors. |

|  |
| --- |
| **Default:** The workspace variable `classNames`. |
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
- To learn more about generating code for Simulink models containing the Image Classifier block, see Code Generation for a Deep Learning Simulink Model to Classify ECG Signals (GPU Coder).

## Version History

**Introduced in R2020b**

### R2024a: `SeriesNetwork` and `DAGNetwork` are not recommended

Starting in R2024a, the `SeriesNetwork` and `DAGNetwork`
objects are not recommended. This recommendation means that `SeriesNetwork`
and `DAGNetwork` inputs to the Image Classifier block are not
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
2. Define a workspace variable containing class names of the network output
   corresponding to the block parameter **Class names workspace
   variable**.
3. Transpose the predicted scores using a transpose block to an
   *N*-by-*K* array, where *N* is the
   number of observations, and *K* is the number of classes.

## Description

Classify data using a trained deep learning neural network

The Image Classifier block predicts class labels for
the data at the input by using the trained network specified through the
block parameter. This block allows loading of a pretrained network into
the Simulink® model from a MAT file or from a MATLAB® function.
