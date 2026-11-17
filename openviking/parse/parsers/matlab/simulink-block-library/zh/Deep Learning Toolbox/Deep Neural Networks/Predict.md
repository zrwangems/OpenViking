---
type: simulink-block
title: 'Predict'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Neural Networks'
documentation_page: 'predict'
documentation_source_path: 'ref/predict.html'
language: zh-CN
chinese_source: worker-translation
---

# Predict

## 端口

### 输入

### **input** — 图像、特征、序列或时间序列数据 数值数组

Predict 模块的输入端口采用所加载网络的输入层名称。例如，如果为 `MATLAB function` 指定 `imagePretrainedNetwork`，则 Predict 模块的输入端口标签为 **data**。根据所加载的网络，Predict 模块的输入可以是图像、序列或时间序列数据。

输入的布局取决于数据类型。

| 数据 | 预测变量布局 |
| --- | --- |
| 二维图像 | 一个 *h*×*w*×*c*×*N* 数值数组，其中 *h*、*w* 和 *c* 分别为图像的高度、宽度和通道数，*N* 为图像数量。 |
| 向量序列 | *s*×*c* 矩阵，其中 *s* 为序列长度，*c* 为序列的特征数。 |
| 二维图像序列 | *h*×*w*×*c*×*s* 数组，其中 *h*、*w* 和 *c* 分别对应图像的高度、宽度和通道数，*s* 为序列长度。 |
| 特征 | 一个 *N*×`numFeatures` 数值数组，其中 *N* 为观测值数量，`numFeatures` 为输入数据的特征数。 |

如果数组中包含 `NaN`，则它们会通过网络传播。
### 输出

### **output** — 预测得分、响应或激活值 数值数组

Predict 模块的输出端口采用所加载网络的输出层名称。例如，如果为 `MATLAB function` 指定 `imagePretrainedNetwork`，则 Predict 模块的输出端口标签为 **prob\_flatten**。根据所加载的网络，Predict 模块的输出可以表示预测得分或响应。

预测得分或响应以 *K*×*N* 数组形式返回，其中 *K* 为类别数，*N* 为观测值数量。

如果为某个网络层启用 `Activations`，则 Predict 模块会创建一个以所选网络层名称命名的新输出端口。此端口输出所选网络层的激活值。

来自网络层的激活值以数值数组形式返回。输出的格式取决于输入数据类型和层输出类型。

对于二维图像输出，激活值为一个 *h*×*w*×*c*×*n* 数组，其中 *h*、*w* 和 *c* 分别为所选层输出的高度、宽度和通道数，*n* 为图像数量。

对于包含向量数据的单个时间步，激活值为一个 *c*×*n* 矩阵，其中 *c* 为序列中的特征数，*n* 为序列数量。

对于包含向量数据的多个时间步，激活值为一个 *c*×*n*×*s* 矩阵，其中 *c* 为序列中的特征数，*n* 为序列数量，*s* 为序列长度。

对于包含二维图像数据的单个时间步，激活值为一个 *h*×*w*×*c*×*n* 数组，其中 *n* 为序列数量，*h*、*w* 和 *c* 分别为图像的高度、宽度和通道数。

## 参数

### **Network** — 训练网络的来源 `Network from MAT file`（默认）| `Network from MATLAB function`

指定训练网络的来源。选择以下选项之一：

- `Network from MAT file`— 从包含 `dlnetwork` 对象的 MAT 文件导入训练网络。
- `Network from MATLAB function`— 从 MATLAB 函数导入预训练网络。例如，要使用预训练的 GoogLeNet，请在 MATLAB M 文件中创建函数 `pretrainedGoogLeNet`，然后导入此函数。

  ```
  function net = pretrainedGoogLeNet
    net = imagePretrainedNetwork("googlenet");
  end
  ```

#### 编程用法

|  |
| --- |
| **模块参数：** `Network` |
| **类型：** 字符向量、字符串 |
| **值：** `'Network from MAT file'` | `'Network from MATLAB function'` |
| **默认值：** `'Network from MAT file'` |

### **File path** — 包含训练网络的 MAT 文件 `untitled.mat`（默认）| MAT 文件路径或名称

此参数指定包含要加载的训练深度学习网络的 MAT 文件的名称。如果文件不在 MATLAB 路径上，请使用 **Browse** 按钮定位该文件。

#### 依赖关系

要启用此参数，请将 **Network** 参数设置为 `Network from MAT file`。

#### 编程用法

|  |
| --- |
| **模块参数：** `NetworkFilePath` |
| **类型：** 字符向量、字符串 |
| **值：** MAT 文件路径或名称 |
| **默认值：**  `'untitled.mat'` |

### **MATLAB function** — MATLAB 函数名称 `squeezenet`（默认）| MATLAB 函数名称

此参数指定预训练深度学习网络的 MATLAB 函数的名称。例如，要使用预训练的 GoogLeNet，请在 MATLAB M 文件中创建函数 `pretrainedGoogLeNet`，然后导入此函数。

```
function net = pretrainedGoogLeNet
  net = imagePretrainedNetwork("googlenet");
end
```

#### 依赖关系

要启用此参数，请将 **Network** 参数设置为 `Network from MATLAB function`。

#### 编程用法

|  |
| --- |
| **模块参数：** `NetworkFunction` |
| **类型：** 字符向量、字符串 |
| **值：** MATLAB 函数名称 |
| **默认值：** `'squeezenet'` |

### **Mini-batch size** — 小批量大小 128（默认）| 正整数

用于预测的小批量大小，指定为正整数。较大的小批量大小需要更多内存，但可以加快预测速度。

#### 编程用法

|  |
| --- |
| **模块参数：** `MiniBatchSize` |
| **类型：** 字符向量、字符串 |
| **值：** 正整数 |
| **默认值：** `'128'` |

### **Predictions** — 输出预测得分或响应 `on`（默认）| `off`

启用返回预测得分或响应的输出端口。

#### 编程用法

|  |
| --- |
| **模块参数：** `Predictions` |
| **类型：** 字符向量、字符串 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'on'` |

### **Input data formats** — `dlnetwork` 的输入数据格式 字符向量 | 字符串

此参数指定训练后的 `dlnetwork` 所期望的输入数据格式。

数据格式，指定为字符串标量或字符向量。字符串中的每个字符必须是以下维度标签之一：

- `"S"` — 空间
- `"C"` — 通道
- `"B"` — 批量
- `"T"` — 时间
- `"U"` — 未指定

例如，对于包含一批序列的数组，其中第一、第二和第三维分别对应通道、观测值和时间步，可以指定其格式为 `"CBT"`。

可以指定多个标记为 `"S"` 或 `"U"` 的维度。标签 `"C"`、`"B"` 和 `"T"` 最多各使用一次。软件会忽略第二维之后的单例尾随 `"U"` 维度。

有关详细信息，请参阅 Deep Learning Data Formats。

默认情况下，该参数使用网络所期望的数据格式。

#### 依赖关系

要启用此参数，请将 **Network** 参数设置为 `Network from MAT file`，以从 MAT 文件导入训练后的 `dlnetwork` 对象。

#### 编程用法

|  |
| --- |
| **模块参数：** `InputDataFormats` |
| **类型：** 字符向量、字符串 |
| **值：** 对于具有一个或多个输入的网络，以如下形式指定文本：`"{'inputlayerName1', 'SSC'; 'inputlayerName2', 'SSCB'; ...}"`。对于没有输入层且具有多个输入端口的网络，以如下形式指定文本：`"{'inputportName1/inport1, 'SSC'; 'inputportName2/inport2, 'SSCB'; ...}"`。 |
| **默认值：** 网络所期望的数据格式。有关详细信息，请参阅 Deep Learning Data Formats。 |

### **Activations** — 输出特定层的网络激活值 网络的层

使用 **Activations** 列表选择要从中提取特征的层。所选层将作为 Predict 模块的输出端口出现。

#### 编程用法

|  |
| --- |
| **模块参数：** `Activations` |
| **类型：** 字符向量、字符串 |
| **值：** 形式为 `'{'layerName1',layerName2',...}'` 的字符向量 |
| **默认值：** `''` |

## 所属库

Deep Learning Toolbox / Deep Neural Networks

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 要生成不依赖第三方库的通用 C 代码，请在 **Configuration Parameters** > **Code Generation** 常规类别中，将 **Language** 参数设置为 `C`。
- 要生成 C++ 代码，请在 **Configuration Parameters** > **Code Generation** 常规类别中，将 **Language** 参数设置为 `C++`。要为代码生成指定目标库，请在 **Code Generation** > **Interface** 类别中，设置 **Target Library** 参数。将此参数设置为 `None` 会生成不依赖第三方库的通用 C++ 代码。
- 有关支持代码生成的网络和层列表，请参阅 Networks and Layers Supported for Code Generation (MATLAB Coder)。

### GPU 代码生成 使用 GPU Coder™ 为 NVIDIA® GPU 生成 CUDA® 代码。

使用说明和限制：

- **Configuration Parameters** > **Code Generation** 常规类别中的 **Language** 参数必须设置为 `C++`。
- 有关支持 CUDA® 代码生成的网络和层列表，请参阅 Supported Networks, Layers, and Classes (GPU Coder)。
- 要详细了解如何为包含 Predict 模块的 Simulink 模型生成代码，请参阅 Code Generation for a Deep Learning Simulink Model That Performs Lane and Vehicle Detection (GPU Coder)。

## 版本历史

**在 R2020b 中引入**

### R2024a：不推荐使用 `SeriesNetwork` 和 `DAGNetwork`

从 R2024a 开始，不推荐使用 `SeriesNetwork` 和 `DAGNetwork` 对象。此建议意味着不推荐将 `SeriesNetwork` 和 `DAGNetwork` 输入用于 Predict 模块。请改用 `dlnetwork` 对象。`dlnetwork` 对象具有以下优势：

- `dlnetwork` 对象是一种统一的数据类型，支持网络构建、预测、内置训练、可视化、压缩、验证和自定义训练循环。
- `dlnetwork` 对象支持更广泛的网络架构，可以从外部平台创建或导入。
- `trainnet` 函数支持 `dlnetwork` 对象，使您可以轻松指定损失函数。您可以从内置损失函数中选择，或指定自定义损失函数。
- 使用 `dlnetwork` 对象进行训练和预测通常比 `LayerGraph` 和 `trainNetwork` 工作流更快。

包含 `dlnetwork` 对象的 Simulink 模块模型行为有所不同。预测得分以 *K*×*N* 矩阵形式返回，其中 *K* 为类别数，*N* 为观测值数量。
如果您有包含 `SeriesNetwork` 或 `DAGNetwork` 对象的现有 Simulink 模块模型，请按照以下步骤改用 `dlnetwork` 对象：

1. 使用 `dag2dlnetwork` 函数将 `SeriesNetwork` 或 `DAGNetwork` 对象转换为 `dlnetwork`。
2. 如果模块的输入是向量序列，请使用转置模块将矩阵转置为 *s*×*c* 大小，其中 *s* 为序列长度，*c* 为序列的特征数。
3. 使用转置模块将预测得分转置为 *N*×*K* 数组，其中 *N* 为观测值数量，*K* 为类别数。

## 描述

使用训练后的深度学习神经网络预测响应

Predict 模块使用通过模块参数指定的训练网络，对输入处的数据进行响应预测。此模块允许从 MAT 文件或 MATLAB® 函数将预训练网络加载到 Simulink® 模型中。

**注意**

使用 Predict 模块在 Simulink 中进行预测。要使用 MATLAB 代码以编程方式进行预测，请使用 `minibatchpredict` 或 `predict` 函数。
