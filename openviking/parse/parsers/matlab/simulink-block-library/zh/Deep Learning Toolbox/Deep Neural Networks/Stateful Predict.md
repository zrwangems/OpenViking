---
type: simulink-block
title: 'Stateful Predict'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Neural Networks'
documentation_page: 'statefulpredict'
documentation_source_path: 'ref/statefulpredict.html'
language: zh-CN
chinese_source: official
---

# Stateful Predict

## 端口

### 输入

### **input** — 序列或时间序列数据 数值数组

Stateful Predict 模块的输入端口接受所加载网络的输入层名称。根据加载的网络，Predict 模块的输入可以是序列或时间序列数据。

包含序列的数值数组的维度取决于数据的类型。

| 输入 | 描述 |
| --- | --- |
| 向量序列 | *s*×*c* 矩阵，其中 *s* 是序列长度，*c* 是序列的特征数。 |
| 二维图像序列 | *h*×*w*×*c*×*s* 数组，其中 *h*、*w* 和 *c* 分别对应于图像的高度、宽度和通道数，*s* 是序列长度。 |
### 输出

### **output** — 预测的分数或响应 数值数组

Stateful Predict 模块的输出端口接受所加载网络的输出层名称。基于加载的网络，Stateful Predict 模块的输出可以表示预测的分数或响应。

对于“序列到标签”分类，输出是一个 *K*×*N* 矩阵，其中 *K* 是类的数目，*N* 是观测值数目。

对于“序列到标签”分类问题，输出是一个 *K*×*S* 分数矩阵，其中 *K* 是类的数目，*S* 是相应输入序列中的时间步总数。

## 参数

### **网络** — 经过训练的循环神经网络的源 **从 MAT 文件创建网络** (默认) | **从 MATLAB 函数创建网络**

指定经过训练的循环神经网络的源。经过训练的网络（例如，LSTM 网络）必须至少有一个循环层。选择下列项之一：

- **从 MAT 文件创建网络** - 从包含 `dlnetwork` 对象的 MAT 文件中导入经过训练的循环神经网络。
- **从 MATLAB 函数创建网络** - 从 MATLAB 函数导入预训练循环神经网络。

#### 编程用法

|  |
| --- |
| **模块参数：**`Network` |
| **类型：**字符向量、字符串 |
| **值：**`'Network from MAT-file'` | `'Network from MATLAB function'` |
| **默认值：** `'Network from MAT-file'` |

### **文件路径** — 包含经过训练的循环神经网络的 MAT 文件 `untitled.mat` (默认) | MAT 文件名

此参数指定 MAT 文件的名称，该文件包含要加载的已训练循环神经网络。如果该文件不在 MATLAB 路径中，请使用**浏览**按钮找到该文件。

#### 依赖关系

要启用此参数，请将**网络**参数设置为**从 MAT 文件创建网络**。

#### 编程用法

|  |
| --- |
| **模块参数：**`NetworkFilePath` |
| **类型：**字符向量、字符串 |
| **值：**MAT 文件路径或名称 |
| **默认值：** `'untitled.mat'` |

### **MATLAB 函数** — MATLAB 函数名称 `untitled` (默认) | MATLAB 函数名称

此参数指定预训练循环神经网络的 MATLAB 函数的名称。

#### 依赖关系

要启用此参数，请将**网络**参数设置为**从 MATLAB 函数创建网络**。

#### 编程用法

|  |
| --- |
| **模块参数：**`NetworkFunction` |
| **类型：**字符向量、字符串 |
| **值：**MATLAB 函数名称 |
| **默认值：**`'untitled'` |

### **采样时间** — 输出采样周期和可选时间偏移量 `-1` (默认) | 标量 | 向量

**采样时间**参数指定模块在仿真期间计算新输出值的时间。有关详细信息，请参阅指定采样时间 (Simulink)。

当您不希望输出有时间偏移量时，请将**采样时间**参数指定为标量。要向输出添加时间偏移量，请将**采样时间**参数指定为 `1`×`2` 向量，其中第一个元素是采样周期，第二个元素是偏移量。

默认情况下，**采样时间**参数值为 `-1`，表示继承该值。

#### 编程用法

|  |
| --- |
| **模块参数：**`SampleTime` |
| **类型：**字符向量 |
| **值：** 标量 | 向量 |
| **默认值：**`'-1'` |

### **输入数据格式** — `dlnetwork` 的输入数据格式 字符向量 | 字符串

此参数指定经过训练的 `dlnetwork` 要求的输入数据格式。

数据格式，指定为字符串标量或字符向量。字符串中的每个字符必须为以下维度标签之一：

- `"S"` - 空间
- `"C"` - 通道
- `"B"` - 批量
- `"T"` - 时间
- `"U"` - 未指定

例如，对于包含一批序列的数组，其中第一个、第二个和第三个维度分别对应于通道、观测值和时间步，您可以指定其格式为 `"CBT"`。

您可以指定多个标注为 `"S"` 或 `"U"` 的维度。每个 `"C"`、`"B"` 和 `"T"` 标签最多可以使用一次。该软件忽略第二个维度后的单一尾部 `"U"` 维度。

有关详细信息，请参阅Deep Learning Data Formats。

默认情况下，该参数使用网络预期的数据格式。

#### 依赖关系

要启用此参数，请将**网络**参数设置为**从 MAT 文件创建网络**，以便从 MAT 文件导入经过训练的 `dlnetwork` 对象。

#### 编程用法

|  |
| --- |
| **模块参数：**`InputDataFormats` |
| **类型：**字符向量、字符串 |
| **值：**对于具有一个或多个输入的网络，请使用 `{'inputlayerName1', 'SSC'; 'inputlayerName2', 'SSCB'; ...}'` 形式的字符向量。对于没有输入层但有多个输入端口的网络，请使用 `'{'inputportName1/inport1, 'SSC'; 'inputportName2/inport2, 'SSCB'; ...}'` 形式的字符向量。 |
| **默认值：**网络预期的数据格式。有关详细信息，请参阅Deep Learning Data Formats。 |

## 所属库

Deep Learning Toolbox / Deep Neural Networks

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

用法说明和限制：

- 要生成不依赖第三方库的通用 C 代码，请在**配置参数** > **代码生成**常规类别中，将**语言**参数设置为 **C**。
- 要生成 C++ 代码，请在**配置参数** > **代码生成**常规类别中，将**语言**参数设置为 **C++**。要指定代码生成的目标库，请在**代码生成** > **接口**类别中，设置**目标库**参数。将此参数设置为**无**会生成不依赖第三方库的泛型 C++ 代码。
- 对于基于 ERT 的目标，必须启用**代码生成** > **接口**窗格中的**支持: 可变大小信号**参数。
- 有关代码生成支持的网络和层的列表，请参阅代码生成支持的网络和层 (MATLAB Coder)。

### GPU 代码生成 使用 GPU Coder™ 为 NVIDIA® GPU 生成 CUDA® 代码。

用法说明和限制：

- **配置参数** > **代码生成**常规类别中的**语言**参数必须设置为 **C++**。
- 仅当目标是 cuDNN 库时，GPU 代码生成才支持此模块。

## 版本历史

**在 R2021a 中推出**

### R2024a: 不推荐使用 `SeriesNetwork` 和 `DAGNetwork`

从 R2024a 开始，不推荐使用 `SeriesNetwork` 和 `DAGNetwork` 对象。这意味着，不推荐将 `SeriesNetwork` 和 `DAGNetwork` 用作 Stateful Predict 模块的输入。请改用 `dlnetwork` 对象。`dlnetwork` 对象具有以下优势：

- `dlnetwork` 对象是一种统一的数据类型，支持网络构建、预测、内置训练、可视化、压缩、验证和自定义训练循环。
- `dlnetwork` 对象支持更广泛的网络架构，您可以创建或从外部平台导入这些网络架构。
- `trainnet` 函数支持 `dlnetwork` 对象，这使您能够轻松指定损失函数。您可以从内置损失函数中进行选择或指定自定义损失函数。
- 使用 `dlnetwork` 对象进行训练和预测通常比使用 `LayerGraph` 和 `trainNetwork` 工作流更快。

包含 `dlnetwork` 对象的 Simulink 模块模型具有不同的行为。预测分数以 *K*×*N* 矩阵形式返回，其中 *K* 是类数，*N* 是观测值的数量。如果您有一个现有的 Simulink 模块模型，其中包含 `SeriesNetwork` 或 `DAGNetwork` 对象，请按照以下步骤改用 `dlnetwork` 对象：

1. 使用 `dag2dlnetwork` 函数将 `SeriesNetwork` 或 `DAGNetwork` 对象转换为 `dlnetwork`。
2. 如果模块的输入是向量序列，则使用转置模块将矩阵转置为大小为 *s*×*c*，其中 *s* 是序列长度，*c* 是序列的特征数。
3. 使用转置模块将预测分数转置为 *N*×*K* 数组，其中 *N* 是观测值数量，*K* 是类数。

## 描述

使用经过训练的循环神经网络预测响应

Stateful Predict 模块使用通过模块参数指定的已训练循环神经网络来预测输入端数据的响应。此模块允许从 MAT 文件或使用 MATLAB® 函数将预训练网络加载到 Simulink® 模型中。此模块会在每次预测后更新网络状态。

要将循环神经网络的状态重置为其初始状态，请将 Stateful Predict 模块放置在 Resettable Subsystem (Simulink) 模块内，并使用 `Reset` 控制信号作为触发器。
