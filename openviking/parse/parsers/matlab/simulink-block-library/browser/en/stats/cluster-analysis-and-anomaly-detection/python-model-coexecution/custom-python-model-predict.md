---
type: simulink-block
title: 'Custom Python Model Predict'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Regression / Python Model Coexecution'
documentation_page: 'custompythonmodelpredict'
documentation_source_path: 'custompythonmodelpredict.html'
language: en
---

# Custom Python Model Predict

## Ports

### Input

### **In1** — Input data numeric array

Input data, specified as a numeric array. You can rearrange the dimensions of the
input data that the block passes to the Python `predict()` function
by specifying a permutation vector on the **Inputs** tab of the Block
Parameters dialog box (see Inputs).

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Out1** — Predicted responses numeric array

Predicted responses, returned as a numeric array. You can rearrange the dimensions
of the output data returned by the Python model by specifying a permutation vector on
the **Outputs** tab of the Block Parameters dialog box (see Outputs).

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Specify model file

### **Path to Python file defining load\_model() and predict()** — Name or path of custom Python model file `untitled` (default) | character vector

Specify the name or path of a Python model file, or click the
**Browse** button. The file must contain the definitions of two
functions: `load_model()` and `predict()`, and can
optionally contain a `reset_model()` function.

- The `load_model()` function must have the
  signature

  ```
  model = load_model(input1,input2, ...)
  ```

  where
  `model` can have any Python datatype, and the
  `input` arguments correspond to the list entries in Arguments to load\_model().
- The `predict()` function must have the
  signature

  ```
  outputList = predict(model,inputList)
  ```

  where
  `model` is the model object returned by
  `load_model()`. `inputList` is a Python list
  whose elements correspond to the block input ports specified on the
  **Inputs** tab of the Block Parameters dialog box. Each element
  is a NumPy `ndarray`. `outputList` is a Python
  list whose elements correspond to the outputs of the `predict()`
  function. Each element is a NumPy `ndarray`.
- If `model` is a Python stateful model, you can define a
  `reset_model()` function, which must have the
  signature

  ```
  updated_model = reset_model(model)
  ```

  where `model` is the model object returned by
  `load_model()`, and `updated_model` is a copy
  of `model` with its state updated. If you define a
  `reset_model()` function, the Custom Python Model Predict block
  calls the `reset_model()` function in Python after calling
  `load_model()`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PythonModulePath` |
| **Type:** character vector |
| **Values:** Python file | path to Python file |
| **Default:** `"untitled"` |

### **Arguments to load\_model()** — Arguments for Python `load_model()` function list of strings or numeric arrays

Specify a comma-separated list of strings or numeric arrays that the
Custom Python Model Predict block passes to the `load_model()`
function specified by Path to Python file defining load\_model() and predict().

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LoadModelArgs` |
| **Type:** comma-separated list |
| **Values:** string | numeric array |

### **Sample time (–1 for inherited)** — Option to specify sample time `–1` (default) | scalar

Specify the discrete interval between sample time hits or specify another type of
sample time, such as continuous (`0`) or inherited
(`–1`). For more options, see Types of Sample Time (Simulink).

By default, the Custom Python Model Predict block inherits sample time based on the
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
an input port of the Custom Python Model Predict block. Double-click a table cell entry
to edit its value, and use the **Up** and
**Down** buttons to reorder the table rows. Add and delete input
ports by clicking the **New** and **Delete**
buttons, respectively. If you specify multiple input ports, their order must
correspond to the `inputList` order in the Python
`predict()` function (see Path to Python file defining load\_model() and predict()).

The table has the following columns:

- **Input Name** — Block input port label,
  specified as a character vector. The block does not pass the input port label to
  the Python model.
- **Python Datatype** — Python or NumPy datatype to
  which the Custom Python Model Predict block converts incoming data before passing
  it to the Python `predict()` function, specified as a character
  vector. The block supports the Python numeric datatypes `"int"`
  and `"float"`, and the NumPy numeric datatypes
  `"float16"`, `"float32"`,
  `"float64"`, `"int8"`,
  `"uint8"`, `"int16"`,
  `"uint16"`, `"int32"`,
  `"uint32"`, `"int64"`, and
  `"uint64"`. The default value is
  `"float32"`.
- **Permutation to Python** — New dimension
  arrangement for the input data, specified as a numeric vector with unique positive
  integer elements that represent the dimensions of the input data (see `permute`). For example, if the
  input data is a 2D matrix, you can specify `[2 1]` to switch the
  row and column dimensions. The Custom Python Model Predict block passes the
  rearranged array to the Python model.
- **Python NumDims** — Number of dimensions for the
  input data, specified as a nonnegative integer. The default value is
  `"inherit"`, which corresponds to the dimensionality of the
  Simulink input signal. The Custom Python Model Predict block converts the input
  data in Simulink to a Python array with the specified dimensions, and then passes
  the data to the Python `predict()` function. The input data
  cannot contain more dimensions than the specified number, unless the extra
  dimensions are singletons. The block does not pass these extra singleton
  dimensions to Python. If the input data has fewer dimensions than the specified
  number, the block adds trailing singleton dimensions, as needed.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputTable` |
| **Type:** cell array |

### Outputs

### **Outputs** — Output port properties table

Output port properties, specified as a table. Each row of the table corresponds to
an individual output port of the Custom Python Model Predict block. Double-click a
table cell entry to edit its value, and use the **Up** and
**Down** buttons to reorder the table rows. Add or delete output
ports by clicking the **New** and **Delete**
buttons, respectively. If you specify multiple output ports, their order must
correspond to the output order in the Python model.

The table has the following columns:

- **Output Name** — Block output port label,
  specified as a character vector.
- **Permutation from Python** — New dimension
  ordering for the array that the Custom Python Model Predict block passes to the
  output port, specified as a numeric vector with unique positive integer elements
  (see `permute`).
- **Max MATLAB Dim Sizes** —
  Maximum size of the block output along each dimension,
  specified as an array of positive integers. Specify this
  parameter only if your Python model is capable of returning
  variable-size output during a single simulation run.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputTable` |
| **Type:** cell array |

## Libraries

Statistics and Machine Learning Toolbox / Deep Learning Toolbox / Python Models / Python Neural Networks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Predict responses using pretrained custom Python model

The Custom Python Model Predict block predicts responses using a pretrained custom
Python® model running in the MATLAB® Python environment. MATLAB supports the reference implementation of Python,
often called CPython. If you use a Mac or Linux® platform, you already have Python installed. If you use Windows®, you need to install a distribution, such as those found at https://www.python.org/downloads/. For
more information, see Configure Your System to Use Python. The Custom Python Model Predict block has been
tested using Python version 3.10.

Load a custom Python model into the block by specifying the path to a Python file that
defines `load_model()` and `predict()` functions. The
Custom Python Model Predict block calls the `load_model()` function once in
Python with arguments you specify in Arguments to load\_model(), and then calls the
`predict()` function at every simulation step. The input port
**In1** receives input data, and the output port **Out1**
returns predicted responses for the input data. You can add input and output ports using the
**Inputs** and **Outputs** tabs of the Block Parameters
dialog box (see Inputs and Outputs).

**Note**

You cannot run the Custom Python Model Predict block in Rapid Accelerator mode.
