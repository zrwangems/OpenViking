---
type: simulink-block
title: 'Scikit-learn Model Predict'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Python Models'
documentation_page: 'scikitlearnmodelpredict'
documentation_source_path: 'scikitlearnmodelpredict.html'
language: en
---

# Scikit-learn Model Predict

## Ports
```yaml
ports:
- name: x
  summary: Predictor data numeric matrix
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: yfit
  summary: Predicted responses numeric vector
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean
```

### Input

### **x** — Predictor data numeric matrix

Predictor data, specified as a numeric matrix. By default, the rows correspond to
observations, and the columns correspond to predictor variables. You can rearrange the
dimensions of the predictor data that the software passes to the Python model by
specifying a permutation vector on the **Input** tab of the Block
Parameters dialog box (see Input).

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **yfit** — Predicted responses numeric vector

Predicted responses, returned as a numeric vector.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`
## Parameters
```yaml
parameters:
- name: Path to scikit-learn model file
  summary: Name or path of Python scikit-learn model file untitled (default) | character vector
  group: Specify model file
  block_parameter: ModelFile
  type: character vector
  values: Python file | path to Python file
  default: '"untitled"'
- name: Sample time (–1 for inherited)
  summary: Option to specify sample time –1 (default) | scalar
  group: Specify model file
  block_parameter: SampleTime
  type: string scalar or character vector
  values: scalar
  default: '"–1"'
- name: Input
  summary: Input port properties table
  group: Input
  block_parameter: InputTable
  type: cell array
- name: Output
  summary: Output port properties table
  group: Output
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

### **Path to scikit-learn model file** — Name or path of Python scikit-learn model file `untitled` (default) | character vector

Specify the name or path of a Python scikit-learn model file, or click the
**Browse** button. You must save the model in Python using
`pickle.dumps()`, `joblib.dump()`, or
`skops.io.dumps()` (see https://scikit-learn.org/stable/model\_persistence.html and https://pypi.org/project/skops/). The model must support a
corresponding `predict()` method in Python. For more information, see
https://scikit-learn.org/stable/.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ModelFile` |
| **Type:** character vector |
| **Values:** Python file | path to Python file |
| **Default:** `"untitled"` |

### **Sample time (–1 for inherited)** — Option to specify sample time `–1` (default) | scalar

Specify the discrete interval between sample time hits or specify another type of
sample time, such as continuous (`0`) or inherited
(`–1`). For more options, see Types of Sample Time (Simulink).

By default, the Scikit-learn Model Predict block inherits sample time based on the
context of the block within the model.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** string scalar or character vector |
| **Values:** scalar |
| **Default:** `"–1"` |

### Input

### **Input** — Input port properties table

Input port properties, specified as a table. The table has the following
columns:

- **Input Name** — Block input port label,
  specified as a character vector. The block does not pass the input port label to
  the Python model.
- **Python Datatype** — Python or NumPy datatype
  to which the Scikit-learn Model Predict block converts incoming data before
  passing it to Python, specified as a character vector. The block supports the
  Python numeric datatypes `"int"` and `"float"`,
  and the NumPy numeric datatypes `"float16"`,
  `"float32"`, `"float64"`,
  `"int8"`, `"uint8"`,
  `"int16"`, `"uint16"`,
  `"int32"`, `"uint32"`,
  `"int64"`, and `"uint64"`. The default value
  is `"float32"`.
- **Permutation to Python** — New dimension
  arrangement for the input data, specified as a numeric vector with unique positive
  integer elements that represent the dimensions of **x** (see
  `permute`). You can specify
  `[2 1]` to switch the row and column dimensions of
  **x**. The Scikit-learn Model Predict block passes the
  rearranged array to the Python model.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputTable` |
| **Type:** cell array |

### Output

### **Output** — Output port properties table

Output port properties, specified as a table. The table has the following
columns:

- **Output Name** — Label for the
  Scikit-learn Model Predict block output port, specified as a character
  vector.
- **Max Batch Size** — Maximum batch size of the
  output, specified as a positive integer. Specify this parameter only if your
  Python model is capable of returning variable-sized output during a single
  simulation run.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputTable` |
| **Type:** cell array |

### Pre/Post-processing

### **Path to Python file defining preprocess()** — Name or path of Python preprocessing function file character vector

Specify the name or path of a file defining an optional Python preprocessing
function for the input data, or click the **Browse** button. When
the Scikit-learn Model Predict receives observations, it converts them to a NumPy
array. The preprocessing function processes the converted observations in Python and
passes them to the Python model.

The preprocessing file must define a Python function with the signature

```
outputList = preprocess(model,inputList)
```

where
`outputList` and `inputList` are lists of NumPy
`ndarray` objects of length 1, and `model` is the
model object. The preprocessing file can be the same as the postprocessing file
specified by Path to Python file defining postprocess() if the file contains
both defining functions.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PreprocessingFilePath` |
| **Type:** character vector |
| **Values:** Python file | path to Python file |

### **Path to Python file defining postprocess()** — Name or path of Python postprocessing function file character vector

Specify the name or path of a file defining an optional Python postprocessing
function for the output data, or click the **Browse** button. The
Scikit-learn Model Predict block processes the output data from the Python model
using the Python function and outputs it from the block.

The postprocessing file must define a Python function with the
signature

```
outputList = postprocess(model,inputList)
```

where
`outputList` and `inputList` are lists of NumPy
`ndarray` objects, and `model` is the model
object. The postprocessing file can be the same as the preprocessing file specified by
Path to Python file defining preprocess() if the file contains
both defining functions.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PostprocessingFilePath` |
| **Type:** character vector |
| **Values:** Python file | path to Python file |
## Libraries

Statistics and Machine Learning Toolbox / Python Models

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

Predict responses using pretrained Python scikit-learn model

The Scikit-learn Model Predict block predicts responses using a pretrained Python®
scikit-learn® model running in the MATLAB® Python environment. MATLAB supports the reference implementation of Python,
often called CPython. If you use a Mac or Linux® platform, you already have Python installed. If you use Windows®, you need to install a distribution, such as those found at https://www.python.org/downloads/. For
more information, see Configure Your System to Use Python. Your MATLAB Python environment must have the
`scikit-learn` module installed. The Scikit-learn Model Predict block has
been tested using Python version 3.10 and `scikit-learn` version
1.2.0.

Load a Python model into the block by specifying the path to a scikit-learn model file.
You can optionally load a Python function to preprocess the observations (predictor data) that
Simulink® passes to the Python model, and a Python function to postprocess the predicted
responses from the model.

The input port **x** receives observations, optionally rearranges the
input array dimensions, and then converts the observations to a Python array. The
preprocessing function (if specified) processes the converted observations in Python and
passes them to the Python model. The model generates predicted responses for the observations
in Python and passes the responses to the Python postprocessing function (if specified). The
output port **Out1** returns the predicted responses from the model.

**Note**

The Scikit-learn Model Predict block cannot be run in Rapid Accelerator mode.
