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
language: zh-CN
chinese_source: worker-translation
---

# Scikit-learn Model Predict

## 端口

### 输入

### **x** — 预测变量数据数值矩阵

预测变量数据，指定为数值矩阵。默认情况下，行对应观测值，列对应预测变量。您可以通过在“模块参数”对话框的**输入**选项卡上指定置换向量，重新排列软件传递给 Python 模型的预测变量数据的维度（参见输入）。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **yfit** — 预测响应数值向量

预测响应，以数值向量形式返回。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink 工具条的**仿真**选项卡上，在**准备**库中，选择**属性检查器**。

### 指定模型文件

### **Path to scikit-learn model file** — Python scikit-learn 模型文件的名称或路径 `untitled`（默认）| 字符向量

指定 Python scikit-learn 模型文件的名称或路径，或点击**浏览**按钮。您必须使用 `pickle.dumps()`、`joblib.dump()` 或 `skops.io.dumps()` 在 Python 中保存模型（参见 https://scikit-learn.org/stable/model\_persistence.html 和 https://pypi.org/project/skops/）。模型必须支持 Python 中相应的 `predict()` 方法。有关详细信息，请参见 https://scikit-learn.org/stable/。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ModelFile` |
| **类型：** 字符向量 |
| **值：** Python 文件 | Python 文件路径 |
| **默认值：** `"untitled"` |

### **Sample time (–1 for inherited)** — 用于指定采样时间的选项 `–1`（默认）| 标量

指定采样时间命中的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`–1`）。有关更多选项，请参见采样时间类型 (Simulink)。

默认情况下，Scikit-learn Model Predict 模块根据模块在模型中的上下文继承采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** 字符串标量或字符向量 |
| **值：** 标量 |
| **默认值：** `"–1"` |

### 输入

### **Input** — 输入端口属性表

输入端口属性，指定为表。该表包含以下列：

- **Input Name** — 模块输入端口标签，指定为字符向量。模块不会将输入端口标签传递给 Python 模型。
- **Python Datatype** — Scikit-learn Model Predict 模块在将传入数据传递给 Python 之前将其转换成的 Python 或 NumPy 数据类型，指定为字符向量。该模块支持 Python 数值数据类型 `"int"` 和 `"float"`，以及 NumPy 数值数据类型 `"float16"`、`"float32"`、`"float64"`、`"int8"`、`"uint8"`、`"int16"`、`"uint16"`、`"int32"`、`"uint32"`、`"int64"` 和 `"uint64"`。默认值为 `"float32"`。
- **Permutation to Python** — 输入数据的新维度排列，指定为包含唯一正整数元素的数值向量，这些元素表示 **x** 的维度（参见 `permute`）。您可以指定 `[2 1]` 来交换 **x** 的行维度和列维度。Scikit-learn Model Predict 模块将重新排列后的数组传递给 Python 模型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InputTable` |
| **类型：** 元胞数组 |

### 输出

### **Output** — 输出端口属性表

输出端口属性，指定为表。该表包含以下列：

- **Output Name** — Scikit-learn Model Predict 模块输出端口的标签，指定为字符向量。
- **Max Batch Size** — 输出的最大批量大小，指定为正整数。仅当你的 Python 模型能够在单次仿真运行期间返回可变大小的输出时，才指定此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutputTable` |
| **类型：** 元胞数组 |

### 预处理/后处理

### **Path to Python file defining preprocess()** — 定义 preprocess() 的 Python 文件的名称或路径 字符向量

指定定义输入数据可选 Python 预处理函数的文件的名称或路径，或点击 **Browse** 按钮。当 Scikit-learn Model Predict 接收观测值时，会将其转换为 NumPy 数组。预处理函数在 Python 中处理转换后的观测值，并将其传递给 Python 模型。

预处理文件必须定义一个具有以下签名的 Python 函数

```
outputList = preprocess(model,inputList)
```

其中 `outputList` 和 `inputList` 是长度为 1 的 NumPy `ndarray` 对象列表，`model` 是模型对象。如果该文件同时包含两个定义函数，则预处理文件可以与 Path to Python file defining postprocess() 指定的后处理文件相同。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PreprocessingFilePath` |
| **类型：** 字符向量 |
| **值：** Python 文件 | Python 文件路径 |

### **Path to Python file defining postprocess()** — 定义 postprocess() 的 Python 文件的名称或路径 字符向量

指定定义输出数据可选 Python 后处理函数的文件的名称或路径，或点击 **Browse** 按钮。Scikit-learn Model Predict 模块使用该 Python 函数处理来自 Python 模型的输出数据，并从模块输出。

后处理文件必须定义一个具有以下签名的 Python 函数

```
outputList = postprocess(model,inputList)
```

其中 `outputList` 和 `inputList` 是 NumPy `ndarray` 对象列表，`model` 是模型对象。如果该文件同时包含两个定义函数，则后处理文件可以与 Path to Python file defining preprocess() 指定的预处理文件相同。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PostprocessingFilePath` |
| **类型：** 字符向量 |
| **值：** Python 文件 | Python 文件路径 |

## 所属库

Statistics and Machine Learning Toolbox / Python Models

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

## 描述

使用预训练的 Python scikit-learn 模型预测响应

Scikit-learn Model Predict 模块使用在 MATLAB® Python 环境中运行的预训练 Python® scikit-learn® 模型来预测响应。MATLAB 支持 Python 的参考实现，通常称为 CPython。如果您使用 Mac 或 Linux® 平台，则已经安装了 Python。如果您使用 Windows®，则需要安装一个发行版，例如 https://www.python.org/downloads/ 上提供的发行版。有关详细信息，请参阅 Configure Your System to Use Python。您的 MATLAB Python 环境必须安装 `scikit-learn` 模块。Scikit-learn Model Predict 模块已使用 Python 3.10 版本和 `scikit-learn` 1.2.0 版本进行测试。

通过指定 scikit-learn 模型文件的路径，将 Python 模型加载到模块中。您可以选择性地加载一个 Python 函数来预处理 Simulink® 传递给 Python 模型的观测值（预测变量数据），以及一个 Python 函数来后处理来自模型的预测响应。

输入端口 **x** 接收观测值，可选地重新排列输入数组维度，然后将观测值转换为 Python 数组。预处理函数（如果指定）在 Python 中处理转换后的观测值，并将它们传递给 Python 模型。模型在 Python 中为观测值生成预测响应，并将响应传递给 Python 后处理函数（如果指定）。输出端口 **Out1** 返回来自模型的预测响应。

**注意**

Scikit-learn Model Predict 模块无法在 Rapid Accelerator 模式下运行。
