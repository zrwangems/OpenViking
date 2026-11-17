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
chinese_source: worker-translation
---

# Stateful Predict

## 端口
```yaml
ports:
- name: input
  summary: 序列或时间序列数据 数值数组
  direction: input
- name: output
  summary: 预测分数或响应 数值数组
  direction: output
```

### 输入

### **input** — 序列或时间序列数据 数值数组

Stateful Predict 模块的输入端口采用所加载网络的输入层名称。根据所加载的网络，预测模块的输入可以是序列或时间序列数据。

包含序列的数值数组的维度取决于数据类型。

| 输入 | 描述 |
| --- | --- |
| 向量序列 | *s*×*c* 矩阵，其中 *s* 是序列长度，*c* 是序列的特征数。 |
| 二维图像序列 | *h*×*w*×*c*×*s* 数组，其中 *h*、*w* 和 *c* 分别对应图像的高度、宽度和通道数，*s* 是序列长度。 |
### 输出

### **output** — 预测分数或响应 数值数组

Stateful Predict 模块的输出端口采用所加载网络的输出层名称。根据所加载的网络，Stateful Predict 模块的输出可以表示预测分数或响应。

对于序列到标签分类，输出是 *K*×*N* 矩阵，其中 *K* 是类别数，*N* 是观测数。

对于序列到序列分类问题，输出是 *K*×*S* 的分数矩阵，其中 *K* 是类别数，*S* 是相应输入序列中的总时间步数。
## 参数
```yaml
parameters:
- name: Network
  summary: 训练好的循环神经网络的来源 Network from MAT-file（默认）| Network from MATLAB function
  group: ''
  block_parameter: Network
  type: 字符向量、字符串
  values: '''Network from MAT-file'' | ''Network from MATLAB function'''
- name: File path
  summary: 包含训练好的循环神经网络的 MAT 文件 untitled.mat（默认）| MAT 文件名
  group: ''
  block_parameter: NetworkFilePath
  type: 字符向量、字符串
  values: MAT 文件路径或名称
- name: MATLAB function
  summary: MATLAB 函数名称 untitled（默认）| MATLAB 函数名称
  group: ''
  block_parameter: NetworkFunction
  type: 字符向量、字符串
  values: MATLAB 函数名称
- name: Sample time
  summary: 输出采样周期和可选时间偏移 -1（默认）| 标量 | 向量
  group: ''
  block_parameter: SampleTime
  type: 字符向量
  values: 标量 | 向量
- name: Input data formats
  summary: dlnetwork 的输入数据格式 字符向量 | 字符串
  group: ''
  block_parameter: InputDataFormats
  type: 字符向量、字符串
  values: 对于具有一个或多个输入的网络，使用以下形式的字符向量：{'inputlayerName1', 'SSC'; 'inputlayerName2', 'SSCB'; ...}'。对于没有输入层且具有多个输入端口的网络，使用以下形式的字符向量：'{'inputportName1/inport1,
    'SSC'; 'inputportName2/inport2, 'SSCB'; ...}'。
```

### **Network** — 训练好的循环神经网络的来源 `Network from MAT-file`（默认）| `Network from MATLAB function`

指定训练好的循环神经网络的来源。训练好的网络必须至少有一个循环层（例如，LSTM 网络）。选择以下之一：

- `Network from MAT-file`— 从包含 `dlnetwork` 对象的 MAT 文件中导入训练好的循环神经网络。
- `Network from MATLAB function`— 从 MATLAB 函数中导入预训练的循环神经网络。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Network` |
| **类型：** 字符向量、字符串 |
| **值：** `'Network from MAT-file'` | `'Network from MATLAB function'` |
| **默认：** `'Network from MAT-file'` |

### **File path** — 包含训练好的循环神经网络的 MAT 文件 `untitled.mat`（默认）| MAT 文件名

此参数指定包含要加载的训练好的循环神经网络的 MAT 文件的名称。如果该文件不在 MATLAB 路径上，请使用 **Browse** 按钮定位该文件。

#### 依赖关系

要启用此参数，请将 **Network** 参数设置为 `Network from MAT file`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `NetworkFilePath` |
| **类型：** 字符向量、字符串 |
| **值：** MAT 文件路径或名称 |
| **默认：**  `'untitled.mat'` |

### **MATLAB function** — MATLAB 函数名称 `untitled`（默认）| MATLAB 函数名称

此参数指定预训练循环神经网络的 MATLAB 函数的名称。

#### 依赖关系

要启用此参数，请将 **Network** 参数设置为 `Network from MATLAB function`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `NetworkFunction` |
| **类型：** 字符向量、字符串 |
| **值：** MATLAB 函数名称 |
| **默认：** `'untitled'` |

### **Sample time** — 输出采样周期和可选时间偏移 `-1`（默认）| 标量 | 向量

**Sample time** 参数指定模块在仿真期间计算新输出值的时间。有关详细信息，请参阅 Specify Sample Time (Simulink)。

当您不希望输出具有时间偏移时，请将 **Sample time** 参数指定为标量。要向输出添加时间偏移，请将 **Sample time** 参数指定为 `1`×`2` 向量，其中第一个元素是采样周期，第二个元素是偏移量。

默认情况下，**Sample time** 参数值为 `-1` 以继承该值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 |
| **默认：** `'-1'` |

### **Input data formats** — `dlnetwork` 的输入数据格式 字符向量 | 字符串

此参数指定训练好的 `dlnetwork` 所期望的输入数据格式。

数据格式，指定为字符串标量或字符向量。字符串中的每个字符必须是以下维度标签之一：

- `"S"` — 空间
- `"C"` — 通道
- `"B"` — 批量
- `"T"` — 时间
- `"U"` — 未指定

例如，对于包含一批序列的数组，其中第一、第二和第三维度分别对应通道、观测和时间步，您可以指定其格式为 `"CBT"`。

您可以指定多个标记为 `"S"` 或 `"U"` 的维度。标签 `"C"`、`"B"` 和 `"T"` 每个最多只能使用一次。该软件会忽略第二维度之后的单例尾随 `"U"` 维度。

有关详细信息，请参阅 Deep Learning Data Formats。

默认情况下，该参数使用网络所期望的数据格式。

#### 依赖关系

要启用此参数，请将 **Network** 参数设置为 `Network from MAT-file`，以从 MAT 文件中导入训练好的 `dlnetwork` 对象。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InputDataFormats` |
| **类型：** 字符向量、字符串 |
| **值：** 对于具有一个或多个输入的网络，使用以下形式的字符向量：`{'inputlayerName1', 'SSC'; 'inputlayerName2', 'SSCB'; ...}'`。对于没有输入层且具有多个输入端口的网络，使用以下形式的字符向量：`'{'inputportName1/inport1, 'SSC'; 'inputportName2/inport2, 'SSCB'; ...}'`。 |
| **默认：** 网络所期望的数据格式。有关详细信息，请参阅 Deep Learning Data Formats。 |
## 所属库

Deep Learning Toolbox / Deep Neural Networks

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 要生成不依赖于第三方库的通用 C 代码，请在 **Configuration Parameters** > **Code Generation** 常规类别中，将 **Language** 参数设置为 `C`。
- 要生成 C++ 代码，请在 **Configuration Parameters** > **Code Generation** 常规类别中，将 **Language** 参数设置为 `C++`。要指定代码生成的目标库，请在 **Code Generation** > **Interface** 类别中，设置 **Target Library** 参数。将此参数设置为 `None` 会生成不依赖于第三方库的通用 C++ 代码。
- 对于基于 ERT 的目标，必须启用 **Code Generation** > **Interface** 窗格中的 **Support: variable-size signals** 参数。
- 有关支持代码生成的网络和层的列表，请参阅 Networks and Layers Supported for Code Generation (MATLAB Coder)。

### GPU 代码生成 使用 GPU Coder™ 为 NVIDIA® GPU 生成 CUDA® 代码。

使用说明和限制：

- **Configuration Parameters** > **Code Generation** 常规类别中的 **Language** 参数必须设置为 `C++`。
- GPU 代码生成仅在面向 cuDNN 库时支持此模块。

## 版本历史

**在 R2021a 中引入**

### R2024a：不建议使用 `SeriesNetwork` 和 `DAGNetwork`

从 R2024a 开始，不建议使用 `SeriesNetwork` 和 `DAGNetwork` 对象。此建议意味着不建议将 `SeriesNetwork` 和 `DAGNetwork` 输入用于 Stateful Predict 模块。请改用 `dlnetwork` 对象。`dlnetwork` 对象具有以下优势：

- `dlnetwork` 对象是一种统一的数据类型，支持网络构建、预测、内置训练、可视化、压缩、验证和自定义训练循环。
- `dlnetwork` 对象支持更广泛的网络架构，您可以创建这些架构或从外部平台导入。
- `trainnet` 函数支持 `dlnetwork` 对象，这使您可以轻松指定损失函数。您可以从内置损失函数中选择，或指定自定义损失函数。
- 使用 `dlnetwork` 对象进行训练和预测通常比 `LayerGraph` 和 `trainNetwork` 工作流更快。

使用 `dlnetwork` 对象的 Simulink 模块模型行为有所不同。预测分数以 *K*×*N* 矩阵形式返回，其中 *K* 是类别数，*N* 是观测值数。如果您已有使用 `SeriesNetwork` 或 `DAGNetwork` 对象的 Simulink 模块模型，请按照以下步骤改用 `dlnetwork` 对象：

1. 使用 `dag2dlnetwork` 函数将 `SeriesNetwork` 或 `DAGNetwork` 对象转换为 `dlnetwork`。
2. 如果模块的输入是向量序列，请使用转置模块将矩阵转置为 *s*×*c* 大小，其中 *s* 是序列长度，*c* 是序列的特征数。
3. 使用转置模块将预测分数转置为 *N*×*K* 数组，其中 *N* 是观测值数，*K* 是类别数。

## 描述

使用训练好的循环神经网络预测响应

Stateful Predict 模块通过模块参数指定的训练好的循环神经网络，对输入处的数据进行响应预测。此模块允许从 MAT 文件或 MATLAB® 函数将预训练网络加载到 Simulink® 模型中。此模块在每次预测时更新网络状态。

要将循环神经网络的状态重置为其初始状态，请将 Stateful Predict 模块放在 Resettable Subsystem (Simulink) 模块内，并使用 `Reset` 控制信号作为触发。
