---
type: simulink-block
title: 'PyTorch Model Predict'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Python Neural Networks'
documentation_page: 'pytorchmodelpredict'
documentation_source_path: 'ref/pytorchmodelpredict.html'
language: en
---

# PyTorch Model Predict

## Ports

### Input

### **In1** — Input data numeric array

Input data, specified as a numeric array. You can rearrange the dimensions of the
input data that the block passes to the Python model by specifying a permutation
vector on the **Inputs** tab of the Block Parameters dialog box (see
Inputs).

The software attempts to automatically populate the table on the
**Inputs** tab when you click the **Autofill Fields From
Model File** button on the **Specify model
file** tab.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Out1** — Predicted responses numeric array

Predicted responses, returned as a numeric array. You can rearrange the dimensions
of the output data returned by the Python model by specifying a permutation vector on
the **Outputs** tab of the Block Parameters dialog box (see Outputs).

The software attempts to automatically populate the table on the
**Outputs** tab when you click the **Autofill Fields From
Model File** button on the **Specify model
file** tab.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Specify model file

### **Load command** — Load command for Python model `torch.load()` (default) | `torch.jit.load()` | `load_state_dict()`

Select the load command for the Python model. The PyTorch Model Predict block
supports models saved in Python using `torch.save()` and
`torch.jit.save()`.

**Note**

If you select `torch.load()` or
`load_state_dict()`, you must define the PyTorch model class in a
`.py` file before you save the model using
`torch.save()`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LoadCommandPopup` |
| **Type:** character vector |
| **Values:** `"torch.load()" | "torch.jit.load()" | "load_state_dict()"` |
| **Default:** `"torch.load()"` |

### **Path to model file or state\_dict file** — Name or path of Python PyTorch model file or `state_dict` file `untitled` (default) | character vector

Specify the name or path of a Python PyTorch model file or
`state_dict` file, or click the **Browse**
button. You must save the file in Python using `torch.save()` or
`torch.jit.save()`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ModelFile` |
| **Type:** character vector |
| **Values:** path to PyTorch model file | path to `state_dict` file |
| **Default:** `"untitled"` |

### **Model class name and optional arguments (if using load\_state\_dict)** — Model class name and optional arguments character vector

PyTorch model class name, specified as a character vector. Specify this parameter
only if **Load command** is `load_state_dict()`. You
can optionally specify arguments to the model using function call format (for example,
`"torchvision.models.alexnet(num_classes=1000,
dropout=0.2)"`).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ModelClassName` |
| **Type:** character vector |
| **Values:** PyTorch model class name | function call to PyTorch model class |

### **Execution device** — Execution device for Python model `cpu` (default) | `cuda` | device name

Specify the name of the execution device for the Python model. If you provide the
name of an execution device, do not enclose the name in quotation marks. When you
click the **Autofill Fields From Model File** button, the software
selects `cuda` for the execution device if Parallel Computing Toolbox™ is installed and a GPU device is available. Otherwise, the software
selects `cpu`.

To specify a CUDA execution device, you must first install Parallel Computing Toolbox and have a GPU device. For information on supported GPU devices, see
GPU Computing Requirements (Parallel Computing Toolbox).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DeviceComboBox` |
| **Type:** unquoted text |
| **Values:** `cpu` |`cuda` | device name |
| **Default:** `cpu` |

### **Sample time (–1 for inherited)** — Option to specify sample time `–1` (default) | scalar

Specify the discrete interval between sample time hits or specify another type of
sample time, such as continuous (`0`) or inherited
(`–1`). For more options, see Types of Sample Time (Simulink).

By default, the PyTorch Model Predict block inherits sample time based on the
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
an individual input port of the PyTorch Model Predict block. The software
attempts to automatically populate the input port properties table when you click the
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
  which the PyTorch Model Predict block converts incoming data before passing
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
  row and column dimensions. The PyTorch Model Predict block passes the
  rearranged array to the Python model (or Python preprocessing function, if
  specified).
- **Python NumDims** — Number of dimensions for the
  input data, specified as a nonnegative integer. The default value is
  `"inherit"`, which corresponds to the dimensionality of the
  Simulink input signal. The PyTorch Model Predict block converts the input
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
an individual output port of the PyTorch Model Predict block. The software
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
  ordering for the array that the PyTorch Model Predict block passes to the
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
the PyTorch Model Predict receives data, it converts it to a NumPy array. The
preprocessing function processes the converted data in Python, and then passes the
data to the Python model.

The preprocessing file must define the Python function with the signature

```
outputList = preprocess(model,inputList)
```

where
`outputList` is a list of NumPy `ndarray` and
PyTorch
`torch.Tensor` objects, `model` is the Python model
object, and `inputList` is a list of `ndarray`
objects. The number of elements in `inputList` must match the number
of input ports in the PyTorch Model Predict block. The number of elements in
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
PyTorch Model Predict block processes the output data from the Python model
using the Python function, and then outputs the data from the block.

The postprocessing file must define the Python function with the signature

```
outputList = postprocess(model,inputList)
```

where
`outputList` is a list of NumPy `ndarray` and
PyTorch
`torch.Tensor` objects, `model` is the Python model
object, and `inputList` is a list of `torch.Tensor`
objects. The number of elements in `inputList` must match the number
of outputs in the Python model. The number of elements in
`outputList` must match the number of output ports in the
PyTorch Model Predict block. The postprocessing file can be the same as the
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

### R2025a: Execute a Python deep learning model on a GPU (requires Parallel Computing Toolbox)

Specify the execution device for a Python model using the **Execution
device** field on the **Specify model file** tab.
Select `cuda` or `cpu`, or enter the name of a
device.

## Description

Predict responses using pretrained Python PyTorch model

The PyTorch Model Predict block predicts responses using a pretrained Python®
PyTorch® model running in the MATLAB® Python environment. MATLAB supports the reference implementation of Python,
often called CPython. If you use a Mac or Linux® platform, you already have Python installed. If you use Windows®, you need to install a distribution, such as those found at https://www.python.org/downloads/. For
more information, see Configure Your System to Use Python. Your MATLAB Python environment must have the
`torch` module installed. The PyTorch Model Predict block has been
tested using Python version 3.10 and `torch` version 2.0.1.

Load a Python model into the block by specifying the path to a PyTorch model file that you
saved in Python using `torch.save()` or `torch.jit.save()`.
You can optionally load a Python function to preprocess the input data that Simulink® passes to the Python model, and a Python function to postprocess the predicted
responses from the model. The PyTorch Model Predict block also allows you to specify the
execution device for the Python model.

The input port **In1** receives input data, optionally rearranges the
input array dimensions, and converts the input data to a Python array. The preprocessing
function (if specified) processes the converted data in Python and passes it to the PyTorch
model. The model generates predicted responses for the input data in Python and passes the
responses to the Python postprocessing function (if specified). The output port
**Out1** returns the predicted responses.

You can add and configure input and output ports using the **Inputs** and
**Outputs** tabs of the Block Parameters dialog box (see Inputs and Outputs). The software attempts
to automatically populate the table in each tab when you click the **Autofill Fields
From Model File** button on the **Specify model
file** tab.

**Note**

You cannot run the PyTorch Model Predict block in Rapid Accelerator mode.
