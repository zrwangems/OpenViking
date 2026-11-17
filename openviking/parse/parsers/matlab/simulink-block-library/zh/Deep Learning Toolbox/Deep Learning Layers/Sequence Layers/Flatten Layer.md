---
type: simulink-block
title: 'Flatten Layer'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning Layers / Sequence Layers'
documentation_page: 'flattenlayer'
documentation_source_path: 'ref/flattenlayer.html'
language: zh-CN
chinese_source: worker-translation
---

# Flatten Layer

## 端口

### 输入

### **Port\_1** — 输入数据数组

要展平的输入数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 展平后的输出数据数组

展平后的输出数据。输出数据将输入数据的空间维度折叠到通道维度中。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的**仿真**选项卡中，在**准备**库中选择**属性检查器**。

### 主

### **Flattened output size** — 展平后输出矩阵的大小 `[1 1 1]`（默认）| 正标量数组

展平后输出矩阵的大小，指定为正标量数组。要确定 `flattenLayer` 对象的激活输出，可以使用 `analyzeNetwork` 函数并忽略批量（`B`）维度。

#### 编程使用

|  |
| --- |
| **模块参数：**  `FlattenedOutputSize` |
| **类型：** 数组 |
| **值：** `[1 1 1]` | `'<array>'` |
| **默认值：**  `'[1 1 1]'` |

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### 执行

### **Sample time** — 用于指定采样时间的选项 `-1`（默认）| 标量

指定采样时间命中之间的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`-1`）。有关更多选项，请参阅采样时间类型 (Simulink)。

默认情况下，模块根据其在模型中的上下文继承采样时间。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |
| --- |
| **参数：** `SampleTime` |
| **数据类型：** `char` |
| **值：** `'-1'`（默认）| 标量 |

## 所属库

Deep Learning Toolbox / Deep Learning Layers / Sequence Layers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

展平层

Flatten Layer 模块将层输入的空间维度折叠到通道维度中。

例如，如果层的输入是 *H*×*W*×*C*×*N*×*S* 数组（图像序列），则展平后的输出是 (*H*\**W*\**C*)×*N*×*S* 数组。

`exportNetworkToSimulink` 函数生成此模块以表示 `flattenLayer` 对象。
