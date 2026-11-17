---
type: simulink-block
title: 'Custom Python Model Predict'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Python Neural Networks'
documentation_page: 'custompythonmodelpredict'
documentation_source_path: 'ref/custompythonmodelpredict.html'
language: zh-CN
chinese_source: worker-translation
---

# Custom Python Model Predict

## 端口

### 输入

### **In1** — 输入数据数值数组

输入数据，指定为数值数组。您可以通过在“模块参数”对话框的 **Inputs** 选项卡上指定置换向量，重新排列模块传递给 Python `predict()` 函数的输入数据的维度（请参阅 Inputs）。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Out1** — 预测响应数值数组

预测响应，以数值数组形式返回。您可以通过在“模块参数”对话框的 **Outputs** 选项卡上指定置换向量，重新排列 Python 模型返回的输出数据的维度（请参阅 Outputs）。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，从 **Prepare** 库中选择 **Property Inspector**。

### 指定模型文件

### **Path to Python file defining load\_model() and predict()** — 自定义 Python 模型文件的名称或路径 `untitled`（默认）| 字符向量

指定 Python 模型文件的名称或路径，或点击 **Browse** 按钮。该文件必须包含两个函数的定义：`load_model()` 和 `predict()`，并且可以选择性地包含 `reset_model()` 函数。

- `load_model()` 函数必须具有以下签名

  ```
  model = load_model(input1,input2, ...)
  ```

  其中 `model` 可以是任意 Python 数据类型，`input` 参数对应于 Arguments to load\_model() 中的列表项。
- `predict()` 函数必须具有以下签名

  ```
  outputList = predict(model,inputList)
  ```

  其中 `model` 是 `load_model()` 返回的模型对象。`inputList` 是一个 Python 列表，其元素对应于“模块参数”对话框 **Inputs** 选项卡上指定的模块输入端口。每个元素都是一个 NumPy `ndarray`。`outputList` 是一个 Python 列表，其元素对应于 `predict()` 函数的输出。每个元素都是一个 NumPy `ndarray`。
- 如果 `model` 是有状态的 Python 模型，您可以定义 `reset_model()` 函数，该函数必须具有以下签名

  ```
  updated_model = reset_model(model)
  ```

  其中 `model` 是 `load_model()` 返回的模型对象，`updated_model` 是状态已更新的 `model` 副本。如果您定义了 `reset_model()` 函数，Custom Python Model Predict 模块会在调用 `load_model()` 之后在 Python 中调用 `reset_model()` 函数。

#### 编程用法

|  |
| --- |
| **模块参数：** `PythonModulePath` |
| **类型：** 字符向量 |
| **值：** Python 文件 | Python 文件路径 |
| **默认值：** `"untitled"` |

### **Arguments to load\_model()** — Python `load_model()` 函数的参数 字符串或数值数组的列表

指定一个以逗号分隔的字符串或数值数组列表，Custom Python Model Predict 模块将其传递给由 Path to Python file defining load\_model() and predict() 指定的 `load_model()` 函数。

#### 编程用法

|  |
| --- |
| **模块参数：** `LoadModelArgs` |
| **类型：** 逗号分隔列表 |
| **值：** 字符串 | 数值数组 |

### **Sample time (–1 for inherited)** — 用于指定采样时间的选项 `–1`（默认）| 标量

指定采样时间命中之间的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`–1`）。有关更多选项，请参阅 Types of Sample Time (Simulink)。

默认情况下，Custom Python Model Predict 模块根据模块在模型中的上下文继承采样时间。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** 字符串标量或字符向量 |
| **值：** 标量 |
| **默认值：** `"–1"` |

### 输入

### **Inputs** — 输入端口属性表

输入端口属性，指定为表。表的每一行对应于 Custom Python Model Predict 模块的一个输入端口。双击表格单元格条目以编辑其值，并使用 **Up** 和 **Down** 按钮重新排列表格行。分别点击 **New** 和 **Delete** 按钮来添加和删除输入端口。如果您指定多个输入端口，其顺序必须与 Python `predict()` 函数中的 `inputList` 顺序相对应（请参阅 Path to Python file defining load\_model() and predict()）。

该表具有以下列：

- **Input Name** — 模块输入端口标签，指定为字符向量。模块不会将输入端口标签传递给 Python 模型。
- **Python Datatype** — Custom Python Model Predict 模块在将传入数据传递给 Python `predict()` 函数之前将其转换为的 Python 或 NumPy 数据类型，指定为字符向量。该模块支持 Python 数值数据类型 `"int"` 和 `"float"`，以及 NumPy 数值数据类型 `"float16"`、`"float32"`、`"float64"`、`"int8"`、`"uint8"`、`"int16"`、`"uint16"`、`"int32"`、`"uint32"`、`"int64"` 和 `"uint64"`。默认值为 `"float32"`。
- **Permutation to Python** — 输入数据的新维度排列，指定为具有唯一正整数元素的数值向量，这些元素表示输入数据的维度（请参阅 `permute`）。例如，如果输入数据是二维矩阵，您可以指定 `[2 1]` 来交换行和列维度。Custom Python Model Predict 模块将重新排列后的数组传递给 Python 模型。
- **Python NumDims** — 输入数据的维度数，指定为非负整数。默认值为 `"inherit"`，对应于 Simulink 输入信号的维度。Custom Python Model Predict 模块将 Simulink 中的输入数据转换为具有指定维度的 Python 数组，然后将数据传递给 Python `predict()` 函数。输入数据包含的维度不能超过指定的数量，除非额外的维度是单一维度。模块不会将这些额外的单一维度传递给 Python。如果输入数据的维度少于指定的数量，模块会根据需要添加尾部单一维度。

#### 编程用法

|  |
| --- |
| **模块参数：** `InputTable` |
| **类型：** 元胞数组 |

### 输出

### **Outputs** — 输出端口属性表

输出端口属性，指定为表。表的每一行对应于 Custom Python Model Predict 模块的单个输出端口。双击表格单元格条目以编辑其值，并使用 **Up** 和 **Down** 按钮重新排列表格行。分别点击 **New** 和 **Delete** 按钮来添加或删除输出端口。如果您指定多个输出端口，其顺序必须与 Python 模型中的输出顺序相对应。

该表具有以下列：

- **Output Name** — 模块输出端口标签，指定为字符向量。
- **Permutation from Python** — Custom Python Model Predict 模块传递给输出端口的数组的新维度排序，指定为具有唯一正整数元素的数值向量（请参阅 `permute`）。
- **Max MATLAB Dim Sizes** — 模块输出沿每个维度的最大大小，指定为正整数数组。仅当您的 Python 模型能够在单次仿真运行期间返回可变大小输出时，才指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutputTable` |
| **类型：** 元胞数组 |

## 所属库

Statistics and Machine Learning Toolbox / Deep Learning Toolbox / Python Models / Python Neural Networks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

## 描述

使用预训练的自定义 Python 模型预测响应

Custom Python Model Predict 模块使用在 MATLAB® Python 环境中运行的预训练自定义 Python® 模型来预测响应。MATLAB 支持 Python 的参考实现，通常称为 CPython。如果您使用 Mac 或 Linux® 平台，则已安装 Python。如果您使用 Windows®，则需要安装发行版，例如 https://www.python.org/downloads/ 上提供的发行版。有关更多信息，请参阅 Configure Your System to Use Python。Custom Python Model Predict 模块已使用 Python 3.10 版本进行测试。

通过指定定义 `load_model()` 和 `predict()` 函数的 Python 文件路径，将自定义 Python 模型加载到模块中。Custom Python Model Predict 模块在 Python 中使用您在 Arguments to load\_model() 中指定的参数调用一次 `load_model()` 函数，然后在每个仿真步调用 `predict()` 函数。输入端口 **In1** 接收输入数据，输出端口 **Out1** 返回输入数据的预测响应。您可以使用“模块参数”对话框的 **Inputs** 和 **Outputs** 选项卡添加输入和输出端口（请参阅 Inputs 和 Outputs）。

**注意**

您无法在 Rapid Accelerator 模式下运行 Custom Python Model Predict 模块。
