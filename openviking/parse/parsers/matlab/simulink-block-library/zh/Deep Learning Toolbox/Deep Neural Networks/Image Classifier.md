---
type: simulink-block
title: 'Image Classifier'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Neural Networks'
documentation_page: 'imageclassifier'
documentation_source_path: 'ref/imageclassifier.html'
language: zh-CN
chinese_source: worker-translation
---

# Image Classifier

## 端口

### 输入

### **image** — 图像或特征数据 数值数组

一个
*h*×*w*×*c*×*N*
数值数组，其中 *h*、*w* 和
*c* 分别是图像的高度、宽度和通道数，
*N* 是图像的数量。

一个 *N*×`numFeatures` 数值数组，其中
*N* 是观测值的数量，
`numFeatures` 是输入数据的特征数量。

如果数组中包含 `NaN`，则它们会通过网络传播。
### 输出

### **ypred** — 预测的类别标签 枚举

具有最高分数的预测类别标签，以
*N*×1 的枚举标签向量形式返回，其中 *N* 是
观测值的数量。

### **scores** — 预测的类别分数 矩阵

预测分数，以 *K*×*N*
矩阵形式返回，其中 *K* 是类别数，*N*
是观测值的数量。

### **labels** — 预测分数的类别标签 矩阵

与预测分数相关联的标签，以
*N*×*K* 矩阵形式返回，其中 *N* 是
观测值的数量，*K* 是类别数。

## 参数

### **Network** — 训练网络的来源 `Network from MAT file`（默认）| `Network from MATLAB function`

指定训练网络的来源。选择以下之一：

- `Network from MAT file`— 从包含 `dlnetwork`
  对象的 MAT 文件中导入训练好的网络。
- `Network from MATLAB function`—
  从 MATLAB 函数中导入预训练网络。例如，要使用预训练的 GoogLeNet，请在 MATLAB M 文件中创建函数
  `pretrainedGoogLeNet`，
  然后导入此函数。

  ```
  function net = pretrainedGoogLeNet
    net = imagePretrainedNetwork("googlenet");
  end
  ```

#### 程序化使用

|  |
| --- |
| **模块参数：** `Network` |
| **类型：** 字符向量、字符串 |
| **值：** `'Network from MAT file'` | `'Network from MATLAB function'` |
| **默认：** `'Network from MAT file'` |

### **File path** — 包含训练网络的 MAT 文件 `untitled.mat`（默认）| MAT 文件路径或名称

此参数
指定包含要加载的训练深度学习网络的 MAT 文件的名称。如果该文件不在 MATLAB 路径上，请使用 **Browse** 按钮
定位该文件。

#### 依赖关系

要启用此参数，请将 **Network**
参数设置为 `Network from MAT
file`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `NetworkFilePath` |
| **类型：** 字符向量、字符串 |
| **值：** MAT 文件路径或名称 |
| **默认：**  `'untitled.mat'` |

### **MATLAB function** — MATLAB 函数名称 `squeezenet`（默认）| MATLAB 函数名称

此参数指定预训练深度学习网络的 MATLAB 函数的名称。例如，要使用预训练的 GoogLeNet，请在 MATLAB M 文件中创建函数
`pretrainedGoogLeNet`，然后导入此
函数。

```
function net = pretrainedGoogLeNet
  net = imagePretrainedNetwork("googlenet");
end
```

#### 依赖关系

要启用此参数，请将 **Network** 参数设置为 `Network from MATLAB function`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `NetworkFunction` |
| **类型：** 字符向量、字符串 |
| **值：** MATLAB 函数名称 |
| **默认：** `'squeezenet'` |

### **Mini-batch size** — 小批量的大小 128（默认）| 正整数

用于预测的小批量的大小，指定为正整数。较大的小批量大小需要更多内存，但可以加快预测速度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MiniBatchSize` |
| **类型：** 字符向量、字符串 |
| **值：** 正整数 |
| **默认：** `'128'` |

### **Resize input** — 调整输入维度 `on`（默认）| `off`

将输入端口的数据调整为
网络的输入大小。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ResizeInput` |
| **类型：** 字符向量、字符串 |
| **值：** `'off'` | `'on'` |
| **默认：** `'on'` |

### **Classification** — 输出具有最高分数的预测标签 `on`（默认）| `off`

启用输出端口 `ypred`，输出具有最高分数的标签。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Classification` |
| **类型：** 字符向量、字符串 |
| **值：** `'off'` | `'on'` |
| **默认：** `'on'` |

### **Predictions** — 输出所有分数和相关标签 `off`（默认）| `on`

启用输出端口 `scores` 和 `labels`，输出所有预测分数和相关的类别标签。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Predictions` |
| **类型：** 字符向量、字符串 |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **Class names workspace variable** — 包含网络输出类别名称的工作区变量 `classNames`（默认）| 分类向量变量 | 字符串数组变量 | 字符向量元胞数组变量名称

包含类别名称的变量，指定为分类
向量、字符串数组或字符向量元胞数组。

网络的输出大小必须与类别数匹配。

#### 依赖关系

要启用此参数，请将 **Network**
参数设置为 `Network from MAT file`，以
从 MAT 文件中导入训练好的 `dlnetwork` 对象。

#### 程序化使用

|  |
| --- |
| **模块参数：** `classNames` |
| **类型：** 分类向量、字符串数组或字符向量元胞数组的变量名称。 |
| **值：** 包含类别名称的变量名称，指定为分类向量、字符串数组或字符向量元胞数组。 |

|  |
| --- |
| **默认：** 工作区变量 `classNames`。 |

## 所属库

Deep Learning Toolbox / Deep Neural Networks

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 要生成不依赖于第三方库的通用 C 代码，请在
  **Configuration Parameters** > **Code
  Generation** 常规类别中，将 **Language**
  参数设置为 `C`。
- 要生成 C++ 代码，请在 **Configuration Parameters** >
  **Code Generation** 常规类别中，将
  **Language** 参数设置为 `C++`。要
  指定代码生成的目标库，请在 **Code
  Generation** > **Interface** 类别中，设置
  **Target Library** 参数。将此参数设置为
  `None` 会生成不依赖于第三方库的通用 C++ 代码。
- 有关支持代码生成的网络和层列表，请参阅 Networks and Layers Supported for Code Generation (MATLAB Coder)。

### GPU 代码生成 使用 GPU Coder™ 为 NVIDIA® GPU 生成 CUDA® 代码。

使用说明和限制：

- **Configuration
  Parameters** > **Code Generation** 常规类别中的 **Language** 参数必须
  设置为 `C++`。
- 有关支持 CUDA® 代码生成的网络和层列表，请参阅 Supported Networks, Layers, and Classes (GPU Coder)。
- 要详细了解如何为包含 Image Classifier 模块的 Simulink 模型生成代码，请参阅 Code Generation for a Deep Learning Simulink Model to Classify ECG Signals (GPU Coder)。

## 版本历史

**在 R2020b 中引入**

### R2024a：不推荐使用 `SeriesNetwork` 和 `DAGNetwork`

从 R2024a 开始，不推荐使用 `SeriesNetwork` 和 `DAGNetwork`
对象。此建议意味着不推荐将 `SeriesNetwork`
和 `DAGNetwork` 输入用于 Image Classifier 模块。请改用 `dlnetwork` 对象。
`dlnetwork` 对象具有以下优势：

- `dlnetwork` 对象是一种统一的数据类型，支持网络构建、预测、内置训练、可视化、压缩、验证和自定义训练循环。
- `dlnetwork` 对象支持更广泛的网络架构，您可以创建这些架构或从外部平台导入。
- `trainnet` 函数支持 `dlnetwork` 对象，这使您能够轻松指定损失函数。您可以从内置损失函数中选择，或指定自定义损失函数。
- 使用 `dlnetwork` 对象进行训练和预测通常比 `LayerGraph` 和 `trainNetwork` 工作流更快。

包含 `dlnetwork` 对象的 Simulink 模块模型行为有所不同。预测分数以 *K*×*N* 矩阵形式返回，其中 *K* 是
类别数，*N* 是观测值的数量。
如果您有包含 `SeriesNetwork` 或
`DAGNetwork` 对象的现有 Simulink 模块模型，请按照以下步骤改用 `dlnetwork` 对象：

1. 使用 `dag2dlnetwork` 函数将 `SeriesNetwork` 或 `DAGNetwork` 对象转换为
   `dlnetwork`。
2. 定义一个工作区变量，其中包含与模块参数 **Class names workspace
   variable** 对应的网络输出类别名称。
3. 使用转置模块将预测分数转置为
   *N*×*K* 数组，其中 *N* 是
   观测值的数量，*K* 是类别数。

## 描述

使用训练好的深度学习神经网络对数据进行分类

Image Classifier 模块通过使用由模块参数指定的训练网络，对输入处的数据进行预测类别标签。此模块允许从 MAT 文件或 MATLAB® 函数将预训练网络加载到
Simulink® 模型中。
