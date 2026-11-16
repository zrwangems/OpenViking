---
type: simulink-block
title: 'Predict'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Applications / Reduced Order Modeling'
documentation_page: 'predict'
documentation_source_path: 'ref/predict.html'
language: zh-CN
chinese_source: official
---

# Predict

## 端口

### 输入

### **input** — 图像、特征、序列或时间序列数据 数值数组

Predict 模块的输入端口接受所加载网络的输入层名称。例如，如果您为 `MATLAB function` 指定 `imagePretrainedNetwork`，则 Predict 模块的输入端口具有标签**数据**。根据加载的网络，Predict 模块的输入可以是图像、序列或时间序列数据。

输入的布局取决于数据的类型。

| 数据 | 预测变量的布局 |
| --- | --- |
| 二维图像 | *h*×*w*×*c*×*N* 数值数组，其中 *h*、*w* 和 *c* 分别是图像的高度、宽度和通道数，*N* 是图像的数量。 |
| 向量序列 | *s*×*c* 矩阵，其中 *s* 是序列长度，*c* 是序列的特征数。 |
| 二维图像序列 | *h*×*w*×*c*×*s* 数组，其中 *h*、*w* 和 *c* 分别对应于图像的高度、宽度和通道数，*s* 是序列长度。 |
| 特征 | *N*×`numFeatures` 数值数组，其中 *N* 是观测值数目，`numFeatures` 是输入数据的特征数。 |

如果数组包含 `NaN`，则它们会通过网络传播。
### 输出

### **output** — 预测的分数、响应或激活 数值数组

Predict 模块的输出端口接受所加载网络的输出层名称。例如，如果您为 `MATLAB function` 指定 `imagePretrainedNetwork`，则 Predict 模块的输出端口标注为 **prob\_flatten**。基于加载的网络，Predict 模块的输出可以表示预测的分数或响应。

该预测的分数或响应，以 *K*×*N* 数组形式返回，其中 *K* 是类数，*N* 是观测值数目。

如果为一个网络层启用 `Activations`，则 Predict 模块会使用所选网络层的名称创建一个新输出端口。此端口输出来自所选网络层的激活值。

网络层的激活值以数值数组形式返回。输出格式取决于输入数据的类型和层输出的类型。

对于二维图像输出，activations 是一个 *h*×*w*×*c*×*n* 数组，其中 *h*、*w* 和 *c* 分别是所选层输出的高度、宽度和通道数，*n* 是图像的数量。

对于包含向量数据的单个时间步，激活值是一个 *c*×*n* 矩阵，其中 *c* 是序列中特征的数量，*n* 是序列的数量。

对于包含向量数据的多个时间步，激活值是一个 *c*×*n*×*s* 矩阵，其中 *c* 是序列中特征的数量，*n* 是序列的数量，*s* 是序列长度。

对于包含二维图像数据的单个时间步，activations 是一个 *h*×*w*×*c*×*n* 数组，其中 *n* 是序列数，*h*、*w* 和 *c* 分别是图像的高度、宽度和通道数。

## 参数

### **网络** — 经过训练的网络的源 **从 MAT 文件创建网络** (默认) | **从 MATLAB 函数创建网络**

指定经过训练的网络的源。选择下列项之一：

- **从 MAT 文件创建网络** - 从包含 `dlnetwork` 对象的 MAT 文件中导入经过训练的网络。
- **从 MATLAB 函数创建网络** - 从 MATLAB 函数导入预训练网络。例如，要使用预训练的 GoogLeNet，请在 MATLAB M 文件中创建一个函数 `pretrainedGoogLeNet`，然后导入此函数。

  ```
  function net = pretrainedGoogLeNet
    net = imagePretrainedNetwork("googlenet");
  end
  ```

#### 编程用法

|  |
| --- |
| **模块参数：**`Network` |
| **类型：**字符向量、字符串 |
| **值：**`'Network from MAT file'` | `'Network from MATLAB function'` |
| **默认值：** `'Network from MAT file'` |

### **文件路径** — 包含经过训练的网络的 MAT 文件 `untitled.mat` (默认) | MAT 文件路径或名称

此参数用于指定 MAT 文件的名称，该文件包含要加载的经过训练的深度学习网络。如果该文件不在 MATLAB 路径中，请使用**浏览**按钮找到该文件。

#### 依赖关系

要启用此参数，请将**网络**参数设置为**从 MAT 文件创建网络**。

#### 编程用法

|  |
| --- |
| **模块参数：**`NetworkFilePath` |
| **类型：**字符向量、字符串 |
| **值：**MAT 文件路径或名称 |
| **默认值：** `'untitled.mat'` |

### **MATLAB 函数** — MATLAB 函数名称 `squeezenet` (默认) | MATLAB 函数名称

此参数指定预训练深度学习网络的 MATLAB 函数的名称。例如，要使用预训练的 GoogLeNet，请在 MATLAB M 文件中创建一个函数 `pretrainedGoogLeNet`，然后导入此函数。

```
function net = pretrainedGoogLeNet
  net = imagePretrainedNetwork("googlenet");
end
```

#### 依赖关系

要启用此参数，请将**网络**参数设置为**从 MATLAB 函数创建网络**。

#### 编程用法

|  |
| --- |
| **模块参数：**`NetworkFunction` |
| **类型：**字符向量、字符串 |
| **值：**MATLAB 函数名称 |
| **默认值：** `'squeezenet'` |

### **小批量大小** — 小批量的大小 128 (默认) | 正整数

用于预测的小批量的大小，指定为正整数。小批量大小越大，需要的内存越多，但预测速度可能更快。

#### 编程用法

|  |
| --- |
| **模块参数：**`MiniBatchSize` |
| **类型：**字符向量、字符串 |
| **值：**正整数 |
| **默认值：** `'128'` |

### **预测** — 输出预测的分数或响应 `on` (默认) | `off`

启用返回预测的分数或响应的输出端口。

#### 编程用法

|  |
| --- |
| **模块参数：**`Predictions` |
| **类型：**字符向量、字符串 |
| **值：**`'off'` | `'on'` |
| **默认值：** `'on'` |

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
| **值：**对于具有一个或多个输入的网络，请以 `"{'inputlayerName1', 'SSC'; 'inputlayerName2', 'SSCB'; ...}"` 形式指定文本。对于没有输入层但有多个输入端口的网络，请将文本指定为 `"{'inputportName1/inport1, 'SSC'; 'inputportName2/inport2, 'SSCB'; ...}"` 形式。 |
| **默认值：**网络预期的数据格式。有关详细信息，请参阅Deep Learning Data Formats。 |

### **激活值** — 输出特定层的网络激活值 网络的层

使用**激活**列表选择要从中提取特征的层。所选层显示为 Predict 模块的输出端口。

#### 编程用法

|  |
| --- |
| **模块参数：**`Activations` |
| **类型：**字符向量、字符串 |
| **值：**`'{'layerName1',layerName2',...}'` 形式的字符向量 |
| **默认值：** `''` |

## 所属库

Deep Learning Toolbox / Deep Neural Networks

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

用法说明和限制：

- 要生成不依赖第三方库的通用 C 代码，请在**配置参数** > **代码生成**常规类别中，将**语言**参数设置为 **C**。
- 要生成 C++ 代码，请在**配置参数** > **代码生成**常规类别中，将**语言**参数设置为 **C++**。要指定代码生成的目标库，请在**代码生成** > **接口**类别中，设置**目标库**参数。将此参数设置为**无**会生成不依赖第三方库的泛型 C++ 代码。
- 有关代码生成支持的网络和层的列表，请参阅代码生成支持的网络和层 (MATLAB Coder)。

### GPU 代码生成 使用 GPU Coder™ 为 NVIDIA® GPU 生成 CUDA® 代码。

用法说明和限制：

- **配置参数** > **代码生成**常规类别中的**语言**参数必须设置为 **C++**。
- 有关 CUDA® 代码生成支持的网络和层的列表，请参阅Supported Networks, Layers, and Classes (GPU Coder)。
- 要了解有关为包含 Predict 模块的 Simulink 模型生成代码的详细信息，请参阅Code Generation for a Deep Learning Simulink Model That Performs Lane and Vehicle Detection (GPU Coder)。

## 版本历史

**在 R2020b 中推出**

### R2024a: 不推荐使用 `SeriesNetwork` 和 `DAGNetwork`

从 R2024a 开始，不推荐使用 `SeriesNetwork` 和 `DAGNetwork` 对象。这意味着，不推荐将 `SeriesNetwork` 和 `DAGNetwork` 用作 Predict 模块的输入。请改用 `dlnetwork` 对象。`dlnetwork` 对象具有以下优势：

- `dlnetwork` 对象是一种统一的数据类型，支持网络构建、预测、内置训练、可视化、压缩、验证和自定义训练循环。
- `dlnetwork` 对象支持更广泛的网络架构，您可以创建或从外部平台导入这些网络架构。
- `trainnet` 函数支持 `dlnetwork` 对象，这使您能够轻松指定损失函数。您可以从内置损失函数中进行选择或指定自定义损失函数。
- 使用 `dlnetwork` 对象进行训练和预测通常比使用 `LayerGraph` 和 `trainNetwork` 工作流更快。

包含 `dlnetwork` 对象的 Simulink 模块模型具有不同的行为。预测分数以 *K*×*N* 矩阵形式返回，其中 *K* 是类数，*N* 是观测值的数量。如果您有一个现有的 Simulink 模块模型，其中包含 `SeriesNetwork` 或 `DAGNetwork` 对象，请按照以下步骤改用 `dlnetwork` 对象：

1. 使用 `dag2dlnetwork` 函数将 `SeriesNetwork` 或 `DAGNetwork` 对象转换为 `dlnetwork`。
2. 如果模块的输入是向量序列，则使用转置模块将矩阵转置为大小为 *s*×*c*，其中 *s* 是序列长度，*c* 是序列的特征数。
3. 使用转置模块将预测分数转置为 *N*×*K* 数组，其中 *N* 是观测值数量，*K* 是类数。

## 描述

使用经过训练的深度学习神经网络预测响应

Predict 模块使用通过模块参数指定的已训练网络来预测输入端数据的响应。此模块允许从 MAT 文件或使用 MATLAB® 函数将预训练网络加载到 Simulink® 模型中。

**注意**

在 Simulink 中使用 Predict 模块进行预测。要使用 MATLAB 代码以编程方式进行预测，请使用 `minibatchpredict` 或 `predict` 函数。
