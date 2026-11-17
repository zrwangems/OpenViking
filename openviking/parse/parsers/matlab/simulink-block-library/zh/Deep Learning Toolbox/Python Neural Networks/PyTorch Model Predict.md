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
language: zh-CN
chinese_source: worker-translation
---

# PyTorch Model Predict

## 端口
```yaml
ports:
- name: In1
  summary: 输入数据数值数组
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Out1
  summary: 预测响应数值数组
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean
```

### 输入

### **In1** — 输入数据数值数组

输入数据，指定为数值数组。您可以通过在“模块参数”对话框的 **Inputs** 选项卡上指定置换向量来重新排列模块传递给 Python 模型的输入数据的维度（请参阅输入）。

当您单击 **Specify model file** 选项卡上的 **Autofill Fields From Model File** 按钮时，软件会尝试自动填充 **Inputs** 选项卡上的表格。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Out1** — 预测响应数值数组

预测响应，以数值数组形式返回。您可以通过在“模块参数”对话框的 **Outputs** 选项卡上指定置换向量来重新排列 Python 模型返回的输出数据的维度（请参阅输出）。

当您单击 **Specify model file** 选项卡上的 **Autofill Fields From Model File** 按钮时，软件会尝试自动填充 **Outputs** 选项卡上的表格。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`
## 参数
```yaml
parameters:
- name: Load command
  summary: Python 模型的加载命令 torch.load()（默认）| torch.jit.load() | load_state_dict()
  group: 指定模型文件
  block_parameter: LoadCommandPopup
  type: 字符向量
  values: '"torch.load()" | "torch.jit.load()" | "load_state_dict()"'
  default: '"torch.load()"'
- name: Path to model file or state_dict file
  summary: Python PyTorch 模型文件或 state_dict 文件的名称或路径 untitled（默认）| 字符向量
  group: 指定模型文件
  block_parameter: ModelFile
  type: 字符向量
  values: PyTorch 模型文件的路径 | state_dict 文件的路径
  default: '"untitled"'
- name: Model class name and optional arguments (if using load_state_dict)
  summary: 模型类名称和可选参数 字符向量
  group: 指定模型文件
  block_parameter: ModelClassName
  type: 字符向量
  values: PyTorch 模型类名称 | 对 PyTorch 模型类的函数调用
- name: Execution device
  summary: Python 模型的执行设备 cpu（默认）| cuda | 设备名称
  group: 指定模型文件
  block_parameter: DeviceComboBox
  type: 不带引号的文本
  values: cpu |cuda | 设备名称
  default: cpu
- name: Sample time (–1 for inherited)
  summary: 用于指定采样时间的选项 –1（默认）| 标量
  group: 指定模型文件
  block_parameter: SampleTime
  type: 字符串标量或字符向量
  values: 标量
  default: '"–1"'
- name: Inputs
  summary: 输入端口属性表
  group: 输入
  block_parameter: InputTable
  type: 元胞数组
- name: Outputs
  summary: 输出端口属性表
  group: 输出
  block_parameter: OutputTable
  type: 元胞数组
- name: Path to Python file defining preprocess()
  summary: 定义 Python 预处理函数的文件的名称或路径 字符向量
  group: 预处理/后处理
  block_parameter: PreprocessingFilePath
  type: 字符向量
  values: Python 文件 | Python 文件的路径
- name: Path to Python file defining postprocess()
  summary: 定义 Python 后处理函数的文件的名称或路径 字符向量
  group: 预处理/后处理
  block_parameter: PostprocessingFilePath
  type: 字符向量
  values: Python 文件 | Python 文件的路径
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### 指定模型文件

### **Load command** — Python 模型的加载命令 `torch.load()`（默认）| `torch.jit.load()` | `load_state_dict()`

选择 Python 模型的加载命令。PyTorch Model Predict 模块支持使用 `torch.save()` 和 `torch.jit.save()` 在 Python 中保存的模型。

**注意**

如果您选择 `torch.load()` 或 `load_state_dict()`，则必须先在一个 `.py` 文件中定义 PyTorch 模型类，然后才能使用 `torch.save()` 保存模型。

#### 编程用法

|  |
| --- |
| **模块参数：** `LoadCommandPopup` |
| **类型：** 字符向量 |
| **值：** `"torch.load()" | "torch.jit.load()" | "load_state_dict()"` |
| **默认值：** `"torch.load()"` |

### **Path to model file or state\_dict file** — Python PyTorch 模型文件或 `state_dict` 文件的名称或路径 `untitled`（默认）| 字符向量

指定 Python PyTorch 模型文件或 `state_dict` 文件的名称或路径，或单击 **Browse** 按钮。您必须使用 `torch.save()` 或 `torch.jit.save()` 在 Python 中保存该文件。

#### 编程用法

|  |
| --- |
| **模块参数：** `ModelFile` |
| **类型：** 字符向量 |
| **值：** PyTorch 模型文件的路径 | `state_dict` 文件的路径 |
| **默认值：** `"untitled"` |

### **Model class name and optional arguments (if using load\_state\_dict)** — 模型类名称和可选参数 字符向量

PyTorch 模型类名称，指定为字符向量。仅当 **Load command** 为 `load_state_dict()` 时指定此参数。您可以选择使用函数调用格式为模型指定参数（例如，`"torchvision.models.alexnet(num_classes=1000, dropout=0.2)"`）。

#### 编程用法

|  |
| --- |
| **模块参数：** `ModelClassName` |
| **类型：** 字符向量 |
| **值：** PyTorch 模型类名称 | 对 PyTorch 模型类的函数调用 |

### **Execution device** — Python 模型的执行设备 `cpu`（默认）| `cuda` | 设备名称

指定 Python 模型的执行设备名称。如果提供执行设备的名称，请勿将名称用引号括起来。当您单击 **Autofill Fields From Model File** 按钮时，如果安装了 Parallel Computing Toolbox™ 并且有可用的 GPU 设备，软件会为执行设备选择 `cuda`。否则，软件会选择 `cpu`。

要指定 CUDA 执行设备，您必须首先安装 Parallel Computing Toolbox 并拥有 GPU 设备。有关支持的 GPU 设备的信息，请参阅 GPU Computing Requirements (Parallel Computing Toolbox)。

#### 编程用法

|  |
| --- |
| **模块参数：** `DeviceComboBox` |
| **类型：** 不带引号的文本 |
| **值：** `cpu` |`cuda` | 设备名称 |
| **默认值：** `cpu` |

### **Sample time (–1 for inherited)** — 用于指定采样时间的选项 `–1`（默认）| 标量

指定采样时间命中之间的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`–1`）。有关更多选项，请参阅 Types of Sample Time (Simulink)。

默认情况下，PyTorch Model Predict 模块根据模块在模型中的上下文继承采样时间。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** 字符串标量或字符向量 |
| **值：** 标量 |
| **默认值：** `"–1"` |

### 输入

### **Inputs** — 输入端口属性表

输入端口属性，指定为表。表的每一行对应于 PyTorch Model Predict 模块的一个单独输入端口。当您单击 **Specify model file** 选项卡上的 **Autofill Fields From Model File** 按钮时，软件会尝试自动填充输入端口属性表。

双击表格单元格条目以编辑其值，并使用 **Up** 和 **Down** 按钮重新排列表格行。分别单击 **New** 和 **Delete** 按钮来添加和删除输入端口。如果您指定多个输入端口，其顺序必须与 Python 模型（或 Python 预处理函数，如果已指定）中的输入顺序相对应。

该表包含以下列：

- **Input Name** — 模块输入端口标签，指定为字符向量。模块不会将输入端口标签传递给 Python 模型。
- **Python Datatype** — PyTorch Model Predict 模块在将传入数据传递给 Python 之前将其转换成的 Python 或 NumPy 数据类型，指定为字符向量。该模块支持 Python 数值数据类型 `"int"` 和 `"float"`，以及 NumPy 数值数据类型 `"float16"`、`"float32"`、`"float64"`、`"int8"`、`"uint8"`、`"int16"`、`"uint16"`、`"int32"`、`"uint32"`、`"int64"` 和 `"uint64"`。默认值为 `"float32"`。
- **Permutation to Python** — 输入数据的新维度排列，指定为具有唯一正整数元素的数值向量，这些元素表示输入数据的维度（请参阅 `permute`）。例如，如果输入数据是二维矩阵，您可以指定 `[2 1]` 来交换行和列维度。PyTorch Model Predict 模块将重新排列后的数组传递给 Python 模型（或 Python 预处理函数，如果已指定）。
- **Python NumDims** — 输入数据的维度数，指定为非负整数。默认值为 `"inherit"`，对应于 Simulink 输入信号的维度。PyTorch Model Predict 模块将 Simulink 中的输入数据转换为具有指定维度的 Python 数组，然后将数据传递给 Python `predict()` 函数（或 Python 预处理函数，如果已指定）。输入数据包含的维度不能多于指定的数量，除非额外维度是单一维度。模块不会将这些额外的单一维度传递给 Python。如果输入数据的维度少于指定的数量，模块会根据需要添加尾部单一维度。

#### 编程用法

|  |
| --- |
| **模块参数：** `InputTable` |
| **类型：** 元胞数组 |

### 输出

### **Outputs** — 输出端口属性表

输出端口属性，指定为表。表的每一行对应于 PyTorch Model Predict 模块的一个单独输出端口。当您单击 **Specify model file** 选项卡上的 **Autofill Fields From Model File** 按钮时，软件会尝试自动填充输出端口属性表。

双击表格单元格条目以编辑其值，并使用 **Up** 和 **Down** 按钮重新排列表格行。分别单击 **New** 和 **Delete** 按钮来添加或删除输出端口。如果您指定多个输出端口，其顺序必须与 Python 模型（或 Python 后处理函数，如果已指定）中的输出顺序相对应。

该表包含以下列：

- **Output Name** — 模块输出端口标签，指定为字符向量。
- **Permutation from Python** — PyTorch Model Predict 模块传递给输出端口的数组的新维度排序，指定为具有唯一正整数元素的数值向量（请参阅 `permute`）。
- **Max MATLAB Dim Sizes** — 模块输出沿每个维度的最大大小，指定为正整数数组。仅当您的 Python 模型能够在单次仿真运行期间返回可变大小的输出时，才指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutputTable` |
| **类型：** 元胞数组 |

### 预处理/后处理

### **Path to Python file defining preprocess()** — 定义 Python 预处理函数的文件的名称或路径 字符向量

指定为输入数据定义可选 Python 预处理函数的文件的名称或路径，或单击 **Browse** 按钮。当 PyTorch Model Predict 接收数据时，它会将数据转换为 NumPy 数组。预处理函数在 Python 中处理转换后的数据，然后将数据传递给 Python 模型。

预处理文件必须定义具有以下签名的 Python 函数

```
outputList = preprocess(model,inputList)
```

其中 `outputList` 是 NumPy `ndarray` 和 PyTorch `torch.Tensor` 对象的列表，`model` 是 Python 模型对象，`inputList` 是 `ndarray` 对象的列表。`inputList` 中的元素数量必须与 PyTorch Model Predict 模块中的输入端口数量相匹配。`outputList` 中的元素数量必须与 Python 模型所需的输入数量相匹配。如果预处理文件同时包含两个定义函数，则预处理文件可以与 Path to Python file defining postprocess() 指定的后处理文件相同。

#### 编程用法

|  |
| --- |
| **模块参数：** `PreprocessingFilePath` |
| **类型：** 字符向量 |
| **值：** Python 文件 | Python 文件的路径 |

### **Path to Python file defining postprocess()** — 定义 Python 后处理函数的文件的名称或路径 字符向量

指定为输出数据定义可选 Python 后处理函数的文件的名称或路径，或单击 **Browse** 按钮。PyTorch Model Predict 模块使用 Python 函数处理来自 Python 模型的输出数据，然后从模块输出数据。

后处理文件必须定义具有以下签名的 Python 函数

```
outputList = postprocess(model,inputList)
```

其中 `outputList` 是 NumPy `ndarray` 和 PyTorch `torch.Tensor` 对象的列表，`model` 是 Python 模型对象，`inputList` 是 `torch.Tensor` 对象的列表。`inputList` 中的元素数量必须与 Python 模型中的输出数量相匹配。`outputList` 中的元素数量必须与 PyTorch Model Predict 模块中的输出端口数量相匹配。如果后处理文件同时包含两个定义函数，则后处理文件可以与 Path to Python file defining preprocess() 指定的预处理文件相同。

#### 编程用法

|  |
| --- |
| **模块参数：** `PostprocessingFilePath` |
| **类型：** 字符向量 |
| **值：** Python 文件 | Python 文件的路径 |
## 所属库

Deep Learning Toolbox / Python Neural Networks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

### R2025a: 在 GPU 上执行 Python 深度学习模型（需要 Parallel Computing Toolbox）

使用 **Specify model file** 选项卡上的 **Execution device** 字段指定 Python 模型的执行设备。选择 `cuda` 或 `cpu`，或输入设备名称。

## 描述

使用预训练的 Python PyTorch 模型预测响应

PyTorch Model Predict 模块使用在 MATLAB® Python 环境中运行的预训练 Python® PyTorch® 模型来预测响应。MATLAB 支持 Python 的参考实现，通常称为 CPython。如果您使用 Mac 或 Linux® 平台，则已安装 Python。如果您使用 Windows®，则需要安装发行版，例如 https://www.python.org/downloads/ 上提供的发行版。有关更多信息，请参阅 Configure Your System to Use Python。您的 MATLAB Python 环境必须安装 `torch` 模块。PyTorch Model Predict 模块已使用 Python 版本 3.10 和 `torch` 版本 2.0.1 进行测试。

通过指定您使用 `torch.save()` 或 `torch.jit.save()` 在 Python 中保存的 PyTorch 模型文件的路径，将 Python 模型加载到模块中。您可以选择加载一个 Python 函数来预处理 Simulink® 传递给 Python 模型的输入数据，以及一个 Python 函数来后处理来自模型的预测响应。PyTorch Model Predict 模块还允许您指定 Python 模型的执行设备。

输入端口 **In1** 接收输入数据，可选地重新排列输入数组维度，并将输入数据转换为 Python 数组。预处理函数（如果已指定）在 Python 中处理转换后的数据并将其传递给 PyTorch 模型。模型在 Python 中为输入数据生成预测响应，并将响应传递给 Python 后处理函数（如果已指定）。输出端口 **Out1** 返回预测响应。

您可以使用“模块参数”对话框的 **Inputs** 和 **Outputs** 选项卡来添加和配置输入和输出端口（请参阅输入和输出）。当您单击 **Specify model file** 选项卡上的 **Autofill Fields From Model File** 按钮时，软件会尝试自动填充每个选项卡中的表格。

**注意**

您无法在 Rapid Accelerator 模式下运行 PyTorch Model Predict 模块。
