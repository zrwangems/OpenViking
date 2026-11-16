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

预测变量数据，指定为数值矩阵。默认情况下，行对应观测值，列对应预测变量。你可以通过在“模块参数”对话框的 **输入** 选项卡上指定置换向量，重新排列软件传递给 Python 模型的预测变量数据的维度（请参阅输入）。

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **yfit** — 预测响应数值向量

预测响应，以数值向量形式返回。

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink 工具条中，在 **仿真** 选项卡上的 **准备** 库中，选择 **属性检查器**。

### 指定模型文件

### **scikit-learn 模型文件的路径** — Python scikit-learn 模型文件的名称或路径 `untitled` (默认) | character vector

指定 Python scikit-learn 模型文件的名称或路径，或点击 **浏览** 按钮。必须使用 `pickle.dumps()`、`joblib.dump()` 或 `skops.io.dumps()` 在 Python 中保存模型（请参阅 https://scikit-learn.org/stable/model\_persistence.html 和 https://pypi.org/project/skops/）。该模型必须在 Python 中支持相应的 `predict()` 方法。有关更多信息，请参阅 https://scikit-learn.org/stable/。

#### 编程用法

|  |
| --- |
| **模块参数：** `ModelFile` |
| **类型：** character vector |
| **值：** Python 文件 | Python 文件的路径 |
| **默认值：** `"untitled"` |

### **采样时间（–1 表示继承）** — 用于指定采样时间的选项 `–1` (默认) | scalar

指定采样时间命中之间的离散间隔，或指定另一种采样时间类型，例如连续 (`0`) 或继承 (`–1`)。有关更多选项，请参阅采样时间类型 (Simulink)。

默认情况下，Scikit-learn Model Predict 模块根据该模块在模型中的上下文继承采样时间。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** string scalar or character vector |
| **值：** scalar |
| **默认值：** `"–1"` |

### 输入

### **输入** — 输入端口属性表

输入端口属性，指定为表。该表包含以下列：

- **输入名称** — 模块输入端口标签，指定为 character vector。该模块不会将输入端口标签传递给 Python 模型。
- **Python 数据类型** — Scikit-learn Model Predict 模块在将传入数据传递给 Python 之前，将其转换为的 Python 或 NumPy 数据类型，指定为 character vector。该模块支持 Python 数值数据类型 `"int"` 和 `"float"`，以及 NumPy 数值数据类型 `"float16"`、`"float32"`、`"float64"`、`"int8"`、`"uint8"`、`"int16"`、`"uint16"`、`"int32"`、`"uint32"`、`"int64"` 和 `"uint64"`。默认值为 `"float32"`。
- **向 Python 的置换** — 输入数据的新维度排列，指定为包含唯一正整数元素的数值向量，这些元素表示 **x** 的维度（请参阅 `permute`）。可以指定 `[2 1]` 来切换 **x** 的行维度和列维度。Scikit-learn Model Predict 模块将重新排列后的数组传递给 Python 模型。

#### 编程用法

|  |
| --- |
| **模块参数：** `InputTable` |
| **类型：** cell array |

### 输出

### **输出** — 输出端口属性表

输出端口属性，指定为表。该表包含以下列：

- **输出名称** — Scikit-learn Model Predict 模块输出端口的标签，指定为 character vector。
- **最大批量大小** — 输出的最大批量大小，指定为正整数。仅当你的 Python 模型能够在单次仿真运行期间返回可变大小的输出时，才指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutputTable` |
| **类型：** cell array |

### 预处理/后处理

### **定义 preprocess() 的 Python 文件路径** — Python 预处理函数文件的名称或路径，character vector

指定定义输入数据的可选 Python 预处理函数的文件的名称或路径，或点击 **浏览** 按钮。当 Scikit-learn Model Predict 接收观测值时，它会将这些观测值转换为 NumPy 数组。预处理函数在 Python 中处理转换后的观测值，并将它们传递给 Python 模型。

预处理文件必须定义具有以下签名的 Python 函数

```
outputList = preprocess(model,inputList)
```

其中 `outputList` 和 `inputList` 是长度为 1 的 NumPy `ndarray` 对象列表，`model` 是模型对象。如果该文件同时包含这两个定义函数，则预处理文件可以与由“定义 postprocess() 的 Python 文件路径”指定的后处理文件相同。

#### 编程用法

|  |
| --- |
| **模块参数：** `PreprocessingFilePath` |
| **类型：** character vector |
| **值：** Python 文件 | Python 文件的路径 |

### **定义 postprocess() 的 Python 文件路径** — Python 后处理函数文件的名称或路径，character vector

指定定义输出数据的可选 Python 后处理函数的文件的名称或路径，或点击 **浏览** 按钮。Scikit-learn Model Predict 模块使用该 Python 函数处理来自 Python 模型的输出数据，并将其从模块输出。

后处理文件必须定义具有以下签名的 Python 函数

```
outputList = postprocess(model,inputList)
```

其中 `outputList` 和 `inputList` 是 NumPy `ndarray` 对象列表，`model` 是模型对象。如果该文件同时包含这两个定义函数，则后处理文件可以与由“定义 preprocess() 的 Python 文件路径”指定的预处理文件相同。

#### 编程用法

|  |
| --- |
| **模块参数：** `PostprocessingFilePath` |
| **类型：** character vector |
| **值：** Python 文件 | Python 文件的路径 |

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

未在 R2025b 中记录。

## 版本历史

**在 R2024a 中引入**

## 描述

使用预训练的 Python scikit-learn 模型预测响应

Scikit-learn Model Predict 模块使用在 MATLAB® Python 环境中运行的预训练 Python® scikit-learn® 模型预测响应。MATLAB 支持 Python 的参考实现，通常称为 CPython。如果使用 Mac 或 Linux® 平台，则已安装 Python。如果使用 Windows®，则需要安装发行版，例如 https://www.python.org/downloads/ 中提供的发行版。有关更多信息，请参阅配置系统以使用 Python。你的 MATLAB Python 环境必须安装 `scikit-learn` 模块。Scikit-learn Model Predict 模块已使用 Python 版本 3.10 和 `scikit-learn` 版本 1.2.0 进行测试。

通过指定 scikit-learn 模型文件的路径，将 Python 模型加载到模块中。你可以选择加载一个 Python 函数来预处理 Simulink® 传递给 Python 模型的观测值（预测变量数据），并加载一个 Python 函数来后处理来自模型的预测响应。

输入端口 **x** 接收观测值，可选地重新排列输入数组维度，然后将观测值转换为 Python 数组。预处理函数（如果已指定）在 Python 中处理转换后的观测值，并将它们传递给 Python 模型。模型在 Python 中为观测值生成预测响应，并将这些响应传递给 Python 后处理函数（如果已指定）。输出端口 **Out1** 返回来自模型的预测响应。

**注意**

Scikit-learn Model Predict 模块无法在 Rapid Accelerator 模式下运行。
