---
type: simulink-block
title: 'Custom Python Model Predict'
family: 'python-models'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Python Models'
documentation_page: 'custompythonmodelpredict'
documentation_source_path: 'custompythonmodelpredict.html'
language: zh-CN
chinese_source: worker-translation
---

# Custom Python Model Predict

## 端口

### 输入

### **In1** — 输入数据数值数组

输入数据，指定为数值数组。您可以通过在模块参数对话框的 **输入** 选项卡上指定置换向量，重新排列模块传递给 Python `predict()` 函数的输入数据的维度（参见输入）。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Out1** — 预测响应数值数组

预测响应，以数值数组形式返回。您可以通过在模块参数对话框的 **输出** 选项卡上指定置换向量，重新排列 Python 模型返回的输出数据的维度（参见输出）。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

### 指定模型文件

### **用于定义 load\_model() 和 predict() 的 Python 文件路径** — 自定义 Python 模型文件的名称或路径 `untitled`（默认）| 字符向量

指定 Python 模型文件的名称或路径，或点击 **浏览** 按钮。该文件必须包含两个函数的定义：`load_model()` 和 `predict()`，并且可以选择性地包含一个 `reset_model()` 函数。

- `load_model()` 函数必须具有以下签名

  ```
  model = load_model(input1,input2, ...)
  ```

  其中 `model` 可以是任何 Python 数据类型，`input` 参数对应于 load\_model() 的参数中的列表项。
- `predict()` 函数必须具有以下签名

  ```
  outputList = predict(model,inputList)
  ```

  其中 `model` 是 `load_model()` 返回的模型对象。`inputList` 是一个 Python 列表，其元素对应于在模块参数对话框的 **输入** 选项卡上指定的模块输入端口。每个元素都是一个 NumPy `ndarray`。`outputList` 是一个 Python 列表，其元素对应于 `predict()` 函数的输出。每个元素都是一个 NumPy `ndarray`。
- 如果 `model` 是有状态的 Python 模型，您可以定义一个 `reset_model()` 函数，该函数必须具有以下签名

  ```
  updated_model = reset_model(model)
  ```

  其中 `model` 是 `load_model()` 返回的模型对象，`updated_model` 是状态已更新的 `model` 副本。如果定义了 `reset_model()` 函数，Custom Python Model Predict 模块在调用 `load_model()` 之后会在 Python 中调用 `reset_model()` 函数。

#### 编程用法

|  |
| --- |
| **模块参数：** `PythonModulePath` |
| **类型：** 字符向量 |
| **值：** Python 文件 | Python 文件的路径 |
| **默认值：** `"untitled"` |

### **load\_model() 的参数** — Python `load_model()` 函数的参数，字符串或数值数组的列表

指定一个逗号分隔的字符串或数值数组列表，Custom Python Model Predict 模块会将其传递给由用于定义 load\_model() 和 predict() 的 Python 文件路径指定的 `load_model()` 函数。

#### 编程用法

|  |
| --- |
| **模块参数：** `LoadModelArgs` |
| **类型：** 逗号分隔列表 |
| **值：** 字符串 | 数值数组 |

### **采样时间（继承时为 –1）** — 用于指定采样时间的选项 `–1`（默认）| 标量

指定采样时间命中之间的离散间隔，或指定另一种类型的采样时间，例如连续（`0`）或继承（`–1`）。有关更多选项，请参阅采样时间类型 (Simulink)。

默认情况下，Custom Python Model Predict 模块根据模块在模型中的上下文继承采样时间。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** 字符串标量或字符向量 |
| **值：** 标量 |
| **默认值：** `"–1"` |

### 输入

### **输入** — 输入端口属性表

输入端口属性，指定为表。该表的每一行对应于 Custom Python Model Predict 模块的一个输入端口。双击表单元格条目以编辑其值，并使用 **上移** 和 **下移** 按钮重新排列表格行。分别点击 **新建** 和 **删除** 按钮来添加和删除输入端口。如果指定多个输入端口，其顺序必须对应于 Python `predict()` 函数中的 `inputList` 顺序（参见用于定义 load\_model() 和 predict() 的 Python 文件路径）。

该表包含以下列：

- **输入名称** — 模块输入端口标签，指定为字符向量。模块不会将输入端口标签传递给 Python 模型。
- **Python 数据类型** — Custom Python Model Predict 模块在将传入数据传递给 Python `predict()` 函数之前，将传入数据转换为的 Python 或 NumPy 数据类型，指定为字符向量。该模块支持 Python 数值数据类型 `"int"` 和 `"float"`，以及 NumPy 数值数据类型 `"float16"`、`"float32"`、`"float64"`、`"int8"`、`"uint8"`、`"int16"`、`"uint16"`、`"int32"`、`"uint32"`、`"int64"` 和 `"uint64"`。默认值为 `"float32"`。
- **到 Python 的置换** — 输入数据的新维度排列，指定为包含唯一正整数元素的数值向量，这些元素表示输入数据的维度（参见 `permute`）。例如，如果输入数据是二维矩阵，您可以指定 `[2 1]` 来交换行和列维度。Custom Python Model Predict 模块会将重新排列后的数组传递给 Python 模型。
- **Python 维数** — 输入数据的维数，指定为非负整数。默认值为 `"inherit"`，对应于 Simulink 输入信号的维数。Custom Python Model Predict 模块将 Simulink 中的输入数据转换为具有指定维数的 Python 数组，然后将数据传递给 Python `predict()` 函数。输入数据包含的维数不能多于指定的数量，除非额外的维度是单一维度。模块不会将这些额外的单一维度传递给 Python。如果输入数据的维数少于指定的数量，模块会根据需要添加尾随单一维度。

#### 编程用法

|  |
| --- |
| **模块参数：** `InputTable` |
| **类型：** 元胞数组 |

### 输出

### **输出** — 输出端口属性表

输出端口属性，指定为表。该表的每一行对应于 Custom Python Model Predict 模块的一个输出端口。双击表单元格条目以编辑其值，并使用 **上移** 和 **下移** 按钮重新排列表格行。分别点击 **新建** 和 **删除** 按钮来添加或删除输出端口。如果指定多个输出端口，其顺序必须对应于 Python 模型中的输出顺序。

该表包含以下列：

- **输出名称** — 模块输出端口标签，指定为字符向量。
- **来自 Python 的置换** — Custom Python Model Predict 模块传递给输出端口的数组的新维度顺序，指定为包含唯一正整数元素的数值向量（参见 `permute`）。
- **最大 MATLAB 维度大小** — 模块输出沿每个维度的最大大小，指定为正整数数组。仅当您的 Python 模型能够在单次仿真运行期间返回可变大小输出时，才指定此参数。

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

在 R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

## 描述

使用预训练的自定义 Python 模型预测响应

Custom Python Model Predict 模块使用在 MATLAB® Python 环境中运行的预训练自定义 Python® 模型预测响应。MATLAB 支持 Python 的参考实现，通常称为 CPython。如果您使用 Mac 或 Linux® 平台，则已安装 Python。如果您使用 Windows®，则需要安装发行版，例如 https://www.python.org/downloads/ 中提供的发行版。有关详细信息，请参阅配置系统以使用 Python。Custom Python Model Predict 模块已使用 Python 3.10 版进行测试。

通过指定定义 `load_model()` 和 `predict()` 函数的 Python 文件路径，将自定义 Python 模型加载到模块中。Custom Python Model Predict 模块在 Python 中使用您在 load\_model() 的参数中指定的参数调用一次 `load_model()` 函数，然后在每个仿真步调用 `predict()` 函数。输入端口 **In1** 接收输入数据，输出端口 **Out1** 返回输入数据的预测响应。您可以使用模块参数对话框的 **输入** 和 **输出** 选项卡添加输入和输出端口（参见输入和输出）。

**注意**

您无法在快速加速模式下运行 Custom Python Model Predict 模块。
