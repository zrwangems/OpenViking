---
type: simulink-block
title: 'Neural State-Space Model'
family: 'ident'
product_id: 'ident'
product_name: 'System Identification Toolbox'
documentation_release: R2025b
official_category: 'Nonlinear Model Identification / Neural State-Space Models'
documentation_page: 'neuralstatespacemodel'
documentation_source_path: 'ref/neuralstatespacemodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Neural State-Space Model

## 端口

### 输入

### **u** — 神经状态空间模型的输入 标量 | 向量

神经状态空间模型的输入，指定为向量信号，其元素个数与创建相应 `idNeuralStateSpace` 对象时指定的输入数相同。如果模块对话框中指定的 `idNeuralStateSpace` 对象没有输入，则此端口不显示。

### **x0** — 神经状态空间模型的初始状态 标量 | 向量

神经状态空间模型的初始状态，指定为向量信号，其元素个数与创建相应 `idNeuralStateSpace` 对象时指定的状态数相同。

#### 依赖关系

要启用此输入端口，请将 **初始状态源** 参数选择为 `External`。然后，将该端口连接到提供初始状态值的上游信号。

### 输出

### **y** — 神经状态空间模型的输出 标量 | 向量

神经状态空间模型的输出，返回为向量信号，其元素个数与创建相应 `idNeuralStateSpace` 对象时指定的输出数相同。

### **x** — 神经状态空间模型的状态 标量 | 向量

神经状态空间模型的状态，输出为向量信号，其元素个数与创建相应 `idNeuralStateSpace` 对象时指定的状态数 *nx* 相同。这些值与 `y` 输出中的前 *nx* 个值相同。

#### 依赖关系

要启用此输出端口，请选择 **输出状态** 参数。

### **dx** — 神经状态空间模型的状态导数/差分 标量 | 向量

神经状态空间模型的状态导数或状态差分，输出为向量信号，其元素个数与创建相应 `idNeuralStateSpace` 对象时指定的状态数相同。

对于连续时间神经状态空间模型，此值为状态对时间的导数。对于离散时间神经状态空间模型，此值为下一状态与当前状态之差。

#### 依赖关系

要启用此输出端口，请选择 **输出状态导数/差分** 参数。

### **z** — 神经状态空间模型的潜在状态 标量 | 向量

神经状态空间模型的内部（潜在）状态，输出为向量信号，其元素个数与创建相应 `idNeuralStateSpace` 对象时指定的 LatentDim 属性值相同。

#### 依赖关系

要启用此输出端口，请将 `idNeuralStateSpace` 对象的 `LatentDim` 属性值指定为有限正标量，并选择 **输出状态** 参数。

### **dz** — 神经状态空间模型的潜在状态导数/差分 标量 | 向量

神经状态空间模型的内部（潜在）状态导数或潜在状态差分，输出为向量信号，其元素个数与创建相应 `idNeuralStateSpace` 对象时指定的 LatentDim 属性值相同。

对于连续时间神经状态空间模型，此值为潜在状态对时间的导数。对于离散时间神经状态空间模型，此值为下一潜在状态与当前潜在状态之差。

#### 依赖关系

要启用此输出端口，请将 `idNeuralStateSpace` 对象的 `LatentDim` 属性值指定为有限正标量，并选择 **输出状态导数/差分** 参数。

## 参数

### **模型** — 神经状态空间对象 `idNeuralStateSpace(1,'NumInputs',1,'NumOutputs',2)`（默认）| `idNeuralStateSpace` 对象

通过输入 MATLAB® 工作区中 `idNeuralStateSpace` 对象的名称，指定一个用于定义神经状态空间系统的 `idNeuralStateSpace` 对象。

目前，Neural State-Space Model 模块不支持神经网络层激活函数为 `elu`、`swish`、`softplus` 或 `scaling` 的 `idNeuralStateSpace` 对象。

**注意**

如果在工作区中更改了 `Model` 的输入/输出配置，请点击模块对话框中 **模型** 编辑字段旁边的 **...** 按钮，以刷新 Neural State-Space Model 模块。

#### 编程方式

|  |
| --- |
| **模块参数：** `sys` |
| **类型：** string, character vector |
| **默认值：** `"idNeuralStateSpace(1,'NumInputs',1,'NumOutputs',2)"` |

### **初始状态源** — 初始状态源 `internal`（默认）| `external`

指定是直接在对话框中输入初始条件，还是从输入端口接收初始条件。

- 如果将 **初始状态源** 设置为 `internal`，请在 **初始状态** 下的编辑字段中输入初始条件。
- 如果将 **初始状态源** 设置为 `external`，则会将输入端口 `x0` 添加到模块中。然后，必须将提供初始状态值的上游信号连接到 `x0` 输入端口。

#### 编程方式

|  |
| --- |
| **模块参数**：`x0type` |
| **类型**：character vector |
| **值**：`'internal'` | `'external'` |
| **默认值**：`'internal'` |

### **初始状态** — 初始状态 `0`（默认）| 标量 | 向量

将神经状态空间对象的初始状态指定为包含 *nx* 个条目的向量，其中 *nx* 是 `Model` 中的状态数。

使用此参数可确保在您的认知范围内，系统状态在仿真开始时反映真实被控对象环境。

#### 编程方式

|  |
| --- |
| **模块参数：** `ic` |
| **类型：** string, character vector |
| **默认值：** `"0"` |

### **输出状态** — 添加外部输出状态端口 `off`（默认）| `on`

选择此参数可将 **x** 输出端口添加到模块。在仿真期间，此端口输出 `Model` 中指定的 `idNeuralStateSpace` 对象的内部状态。

#### 编程方式

|  |
| --- |
| **模块参数：** `returnx` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **输出状态导数/差分** — 添加外部输出状态导数端口 `off`（默认）| `on`

选择此参数可将 **dx** 输出端口添加到模块。在仿真期间，此端口输出 **模型** 中指定的 `idNeuralStateSpace` 对象的内部状态时间导数。

#### 编程方式

|  |
| --- |
| **模块参数：** `returndx` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

## 所属库

System Identification Toolbox / Models

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

### R2024b：代码生成不创建临时 `.m` 文件

从 2024b 开始，在更新 Neural State-Space Model 模块以进行预测和代码生成时，将不再在当前文件夹中创建临时 `.m` 文件。

但是，如果分配给神经状态空间对象的状态网络或输出网络的 `dlnetwork` 对象的结构不是多层感知机 (MLP) 网络，则 Neural State-Space Model 模块的实现会使用 Predict (Deep Learning Toolbox) Block，并且仍会在当前文件夹中生成 `.mat` 文件。在所有其他情况下，也不会创建 `.mat` 文件。

## 描述

在 Simulink 中仿真神经状态空间模型

仿真神经状态空间 (`idNeuralStateSpace`) 模型。
