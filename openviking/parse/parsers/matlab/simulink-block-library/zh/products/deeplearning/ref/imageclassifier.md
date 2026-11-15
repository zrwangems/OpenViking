---
type: simulink-block
title: 'Image Classifier'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning with Simulink / Networks'
documentation_page: 'imageclassifier'
documentation_source_path: 'ref/imageclassifier.html'
language: zh-CN
chinese_source: official
---

# Image Classifier

## 端口

### 输入

### **image** — 图像或特征数据 数值数组

*h*×*w*×*c*×*N* 数值数组，其中 *h*、*w* 和 *c* 分别是图像的高度、宽度和通道数，*N* 是图像的数量。

*N*×`numFeatures` 数值数组，其中 *N* 是观测值数量，`numFeatures` 是输入数据的特征数。

如果数组包含 `NaN`，则它们会通过网络传播。
### 输出

### **ypred** — 预测的类标签 枚举

具有最高分数的预测类标签，以 *N*×1 标签枚举向量形式返回，其中 *N* 是观测值数量。

### **scores** — 预测的类分数 矩阵

预测的分数，以 *K*×*N* 矩阵形式返回，其中 *K* 是类数，*N* 是观测值数量。

### **labels** — 预测的分数的类标签 矩阵

与预测分数相关联的标签，以 *N*×*K* 矩阵形式返回，其中 *N* 是观测值数量，*K* 是类数。

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

### **调整输入大小** — 调整输入维度大小 `on` (默认) | `off`

将输入端口的数据大小调整为网络的输入大小。

#### 编程用法

|  |
| --- |
| **模块参数：**`ResizeInput` |
| **类型：**字符向量、字符串 |
| **值：**`'off'` | `'on'` |
| **默认值：** `'on'` |

### **分类** — 输出具有最高分数的预测标签 `on` (默认) | `off`

启用输出具有最高分数的标签的输出端口 `ypred`。

#### 编程用法

|  |
| --- |
| **模块参数：**`Classification` |
| **类型：**字符向量、字符串 |
| **值：**`'off'` | `'on'` |
| **默认值：** `'on'` |

### **预测** — 输出所有分数和相关联的标签 `off` (默认) | `on`

启用输出所有预测分数和相关联的类标签的输出端口 `scores` 和 `labels`。

#### 编程用法

|  |
| --- |
| **模块参数：**`Predictions` |
| **类型：**字符向量、字符串 |
| **值：**`'off'` | `'on'` |
| **默认值：** `'off'` |

### **类名称工作区变量** — 包含网络输出类名称的工作区变量 `classNames` (默认) | 分类向量变量 | 字符串数组变量 | 字符向量元胞数组变量名称

包含类名称的变量，指定为分类向量、字符串数组或字符向量元胞数组。

网络的输出大小必须与类的数量匹配。

#### 依赖关系

要启用此参数，请将**网络**参数设置为**从 MAT 文件创建网络**，以便从 MAT 文件导入经过训练的 `dlnetwork` 对象。

#### 编程用法

|  |
| --- |
| **模块参数：**`classNames` |
| **类型：**分类向量、字符串数组或字符向量元胞数组的变量名称。 |
| **值：**包含类名称的变量的名称，指定为分类向量、字符串数组或字符向量元胞数组。 |

|  |
| --- |
| **默认值：**工作区变量 `classNames`。 |

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
- 要了解有关为包含 Image Classifier 模块的 Simulink 模型生成代码的详细信息，请参阅Code Generation for a Deep Learning Simulink Model to Classify ECG Signals (GPU Coder)。

## 版本历史

**在 R2020b 中推出**

### R2024a: 不推荐使用 `SeriesNetwork` 和 `DAGNetwork`

从 R2024a 开始，不推荐使用 `SeriesNetwork` 和 `DAGNetwork` 对象。这意味着，不推荐将 `SeriesNetwork` 和 `DAGNetwork` 用作 Image Classifier 模块的输入。请改用 `dlnetwork` 对象。`dlnetwork` 对象具有以下优势：

- `dlnetwork` 对象是一种统一的数据类型，支持网络构建、预测、内置训练、可视化、压缩、验证和自定义训练循环。
- `dlnetwork` 对象支持更广泛的网络架构，您可以创建或从外部平台导入这些网络架构。
- `trainnet` 函数支持 `dlnetwork` 对象，这使您能够轻松指定损失函数。您可以从内置损失函数中进行选择或指定自定义损失函数。
- 使用 `dlnetwork` 对象进行训练和预测通常比使用 `LayerGraph` 和 `trainNetwork` 工作流更快。

包含 `dlnetwork` 对象的 Simulink 模块模型具有不同的行为。预测分数以 *K*×*N* 矩阵形式返回，其中 *K* 是类数，*N* 是观测值的数量。如果您有一个现有的 Simulink 模块模型，其中包含 `SeriesNetwork` 或 `DAGNetwork` 对象，请按照以下步骤改用 `dlnetwork` 对象：

1. 使用 `dag2dlnetwork` 函数将 `SeriesNetwork` 或 `DAGNetwork` 对象转换为 `dlnetwork`。
2. 定义包含网络输出类名称的工作区变量，该变量与模块参数**类名称工作区变量**相对应。
3. 使用转置模块将预测分数转置为 *N*×*K* 数组，其中 *N* 是观测值数量，*K* 是类数。

## 描述

使用经过训练的深度学习神经网络对数据进行分类

Image Classifier 模块使用通过模块参数指定的已训练网络来预测输入端数据的类标签。此模块允许从 MAT 文件或使用 MATLAB® 函数将预训练网络加载到 Simulink® 模型中。
