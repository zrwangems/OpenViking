---
type: simulink-block
title: 'TensorFlow Model Predict'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Python Neural Networks'
documentation_page: 'tensorflowmodelpredict'
documentation_source_path: 'ref/tensorflowmodelpredict.html'
language: en
---

# TensorFlow Model Predict

## Ports
```yaml
ports:
- name: In1
  summary: Input data numeric array
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Out1
  summary: Predicted responses numeric array
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean
```

### Input

### **In1** — Input data numeric array

Input data, specified as a numeric array. You can rearrange the dimensions of the
data that the block passes to the Python model by specifying a permutation vector on
the **Inputs** tab of the Block Parameters dialog box (see Inputs).

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Out1** — Predicted responses numeric array

Predicted responses, returned as a numeric array. You can rearrange the dimensions
of the output data that the Python model returns by specifying a permutation vector on
the **Outputs** tab of the Block Parameters dialog box (see Outputs).

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`
## Parameters
```yaml
parameters:
- name: Path to model (SavedModel folder or Keras HDF5 file)
  summary: Name or path of Python TensorFlow model untitled (default) | character vector
  group: Specify model file
  block_parameter: ModelFile
  type: character vector
  values: path to Python TensorFlow SavedModel folder | path to Python Keras HDF5 file
  default: '"untitled"'
- name: Sample time (–1 for inherited)
  summary: Option to specify sample time –1 (default) | scalar
  group: Specify model file
  block_parameter: SampleTime
  type: string scalar or character vector
  values: scalar
  default: '"–1"'
- name: Inputs
  summary: Input port properties table
  group: Inputs
  block_parameter: InputTable
  type: cell array
- name: Outputs
  summary: Output port properties table
  group: Outputs
  block_parameter: OutputTable
  type: cell array
- name: Path to Python file defining preprocess()
  summary: Name or path of Python preprocessing function file character vector
  group: Pre/Post-processing
  block_parameter: PreprocessingFilePath
  type: character vector
  values: Python file | path to Python file
- name: Path to Python file defining postprocess()
  summary: Name or path of Python postprocessing function file character vector
  group: Pre/Post-processing
  block_parameter: PostprocessingFilePath
  type: character vector
  values: Python file | path to Python file
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Specify model file

### **Path to model (SavedModel folder or Keras HDF5 file)** — Name or path of Python TensorFlow model `untitled` (default) | character vector

Specify the name or path of a Python TensorFlow model folder or file. You can also
click the **Browse to SavedModel folder** or **Browse to
Keras HDF5 file** button. You must save the model in Python in
`SavedModel` format or as a `Keras HDF5` file (see
https://www.tensorflow.org/guide/keras). The block does not
support the `Keras v3` save format.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ModelFile` |
| **Type:** character vector |
| **Values:** path to Python TensorFlow `SavedModel` folder | path to Python `Keras HDF5` file |
| **Default:** `"untitled"` |

### **Sample time (–1 for inherited)** — Option to specify sample time `–1` (default) | scalar

Specify the discrete interval between sample time hits or specify another type of
sample time, such as continuous (`0`) or inherited
(`–1`). For more options, see Types of Sample Time (Simulink).

By default, the TensorFlow Model Predict block inherits sample time based on the
context of the block within the model.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** string scalar or character vector |
| **Values:** scalar |
| **Default:** `"–1"` |

### Inputs

### **Inputs** — Input port properties table

Input port properties, specified as a table. Each row of the table corresponds to
an input port of the TensorFlow Model Predict block. The software attempts to
automatically populate the input port properties table when you click the
**Autofill Fields From Model File** button on the **Specify model file** tab.

Double-click a table cell entry to edit its value, and use the
**Up** and **Down** buttons to reorder the
table rows. Add and delete input ports by clicking the **New** and
**Delete** buttons, respectively. If you specify multiple input
ports, their order must correspond to the input order in the Python model (or Python
preprocessing function, if specified).

The table has the following columns:

- **Input Name** — Block input port label,
  specified as a character vector. The block does not pass the input port label to
  the Python model.
- **Python Datatype** — Python or NumPy datatype to
  which the TensorFlow Model Predict block converts incoming data before passing
  it to Python, specified as a character vector. The block supports the Python
  numeric datatypes `"int"` and `"float"`, and the
  NumPy numeric datatypes `"float16"`,
  `"float32"`, `"float64"`,
  `"int8"`, `"uint8"`,
  `"int16"`, `"uint16"`,
  `"int32"`, `"uint32"`,
  `"int64"`, and `"uint64"`. The default value
  is `"float32"`.
- **Permutation to Python** — New dimension
  arrangement for the input data, specified as a numeric vector with unique positive
  integer elements that represent the dimensions of the input data (see `permute`). For example, if the
  input data is a 2D matrix, you can specify `[2 1]` to switch the
  row and column dimensions. The TensorFlow Model Predict block passes the
  rearranged array to the Python model (or Python preprocessing function, if
  specified).
- **Python NumDims** — Number of dimensions for the
  input data, specified as a nonnegative integer. The default value is
  `"inherit"`, which corresponds to the dimensionality of the
  Simulink input signal. The TensorFlow Model Predict block converts the input
  data in Simulink to a Python array with the specified dimensions, and then passes
  the data to the Python `predict()` function (or Python
  preprocessing function, if specified). The input data cannot contain more
  dimensions than the specified number, unless the extra dimensions are singletons.
  The block does not pass these extra singleton dimensions to Python. If the input
  data has fewer dimensions than the specified number, the block adds trailing
  singleton dimensions, as needed.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputTable` |
| **Type:** cell array |

### Outputs

### **Outputs** — Output port properties table

Output port properties, specified as a table. Each row of the table corresponds to
an individual output port of the TensorFlow Model Predict block. The software
attempts to automatically populate the output port properties table when you click the
**Autofill Fields From Model File** button on the **Specify model file** tab.

Double-click a table cell entry to edit its value, and use the
**Up** and **Down** buttons to reorder the
table rows. Add or delete output ports by clicking the **New** and
**Delete** buttons, respectively. If you specify multiple output
ports, their order must correspond to the output order in the Python model (or Python
postprocessing function, if specified).

The table has the following columns:

- **Output Name** — Block output port label,
  specified as a character vector.
- **Permutation from Python** — New dimension
  ordering for the array that the TensorFlow Model Predict block passes to the
  output port, specified as a numeric vector with unique positive integer elements
  (see `permute`).
- **Max MATLAB Dim Sizes** —
  Maximum size of the block output along each dimension,
  specified as an array of positive integers. Specify this
  parameter only if your Python model is capable of returning
  variable sized output during a single simulation run.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputTable` |
| **Type:** cell array |

### Pre/Post-processing

### **Path to Python file defining preprocess()** — Name or path of Python preprocessing function file character vector

Specify the name or path of a file defining an optional Python preprocessing
function for the input data, or click the **Browse** button. When
the TensorFlow Model Predict receives data, it converts it to a NumPy array. The
preprocessing function processes the converted data in Python, and then passes the
data to the Python model.

The preprocessing file must define a Python function with the
signature

```
outputList = preprocess(model,inputList)
```

where
`outputList` and `inputList` are lists of NumPy
`ndarray` objects, and `model` is the Python model
object. The number of elements in `inputList` must match the number
of input ports in the TensorFlow Model Predict block. The number of elements in
`outputList` must match the number of inputs required by the Python
model. The preprocessing file can be the same as the postprocessing file specified by
Path to Python file defining postprocess() if the file contains both
defining functions.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PreprocessingFilePath` |
| **Type:** character vector |
| **Values:** Python file | path to Python file |

### **Path to Python file defining postprocess()** — Name or path of Python postprocessing function file character vector

Specify the name or path of a file defining an optional Python postprocessing
function for the output data, or click the **Browse** button. The
TensorFlow Model Predict block processes the output data from the Python model
using the Python function, and then outputs the data from the block.

The postprocessing file must define a Python function with the
signature

```
outputList = postprocess(model,inputList)
```

where
`outputList` and `inputList` are lists of NumPy
`ndarray` objects, and `model` is the model
object. The number of elements in `inputList` must match the number
of outputs in the Python model. The number of elements in
`outputList` must match the number of output ports in the
TensorFlow Model Predict block. The postprocessing file can be the same as the
preprocessing file specified by Path to Python file defining preprocess() if the file contains both
defining functions.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PostprocessingFilePath` |
| **Type:** character vector |
| **Values:** Python file | path to Python file |
## Libraries

Deep Learning Toolbox / Python Neural Networks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Predict responses using pretrained Python TensorFlow model

The TensorFlow Model Predict block predicts responses using a pretrained Python®
TensorFlow™ model running in the MATLAB® Python environment. MATLAB supports the reference implementation of Python,
often called CPython. If you use a Mac or Linux® platform, you already have Python installed. If you use Windows®, you need to install a distribution, such as those found at https://www.python.org/downloads/. For
more information, see Configure Your System to Use Python. Your MATLAB Python environment must have the
`tensorflow` module installed. The TensorFlow Model Predict block has
been tested using Python version 3.10 and `tensorflow` version 2.12.0.

Load a Python model into the block by specifying the path to a TensorFlow model that you
saved in Python in `SavedModel` format or as a `Keras HDF5`
file. You can optionally load a Python function to preprocess the input data that Simulink® passes to the Python model, and a Python function to postprocess the predicted
responses from the model.

The input port **In1** receives input data, optionally rearranges the
input array dimensions, and converts the input data to a Python array. The preprocessing
function (if specified) processes the converted data in Python and passes it to the TensorFlow
model. The model generates predicted responses for the input data in Python and passes the
responses to the Python postprocessing function (if specified). The output port
**Out1** returns the predicted responses.

You can add and configure input and output ports using the **Inputs** and
**Outputs** tabs of the Block Parameters dialog box (see Inputs and Outputs). The software attempts
to automatically populate the table in each tab when you click the **Autofill Fields
From Model File** button on the **Specify model
file** tab.

**Note**

You cannot run the TensorFlow Model Predict block in Rapid Accelerator mode.
