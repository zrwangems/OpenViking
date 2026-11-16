---
type: simulink-block
title: 'Depth Concatenation Layer'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning with Simulink / Combination Layers'
documentation_page: 'depthconcatenationlayer'
documentation_source_path: 'ref/depthconcatenationlayer.html'
language: zh-CN
chinese_source: worker-translation
---

# Depth Concatenation Layer

## 端口

### 输入

### **Port\_1** — 第一个输入数据数组

要拼接的第一个输入，以数组形式提供，其格式由 **Data format** 参数指定。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_2** — 第二个输入数据 标量 | 向量 | 矩阵

要拼接的第二个输入，以数组形式提供，其格式由 **Data format** 参数指定。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_N** — 第 *N* 个输入数据 标量 | 向量 | 矩阵

要拼接的第 *N* 个输入，以数组形式提供，其格式由 **Data format** 参数指定。该模块的输入端口数量等于通过 **Layer** 参数指定的对象的 `NumInputs` 属性值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 输出

### **Port\_1** — 拼接后的输出数据数组

拼接后的输出数据。输出数据的维度对应于通过 **Data format** 模块参数指定的格式。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### 主要

### **Layer** — 对应的层对象 `layerObject`（默认）| `depthConcatenationLayer` 对象

指定包含来自训练网络的 `depthConcatenationLayer` 对象的工作区变量名称。Depth Concatenation Layer 模块通过使用该对象的属性来配置自身。

#### 编程用法

|  |
| --- |
| **模块参数：** `Layer` |
| **类型：** 工作区变量 |
| **值：** `depthConcatenationLayer` 对象 |
| **默认值：** `'layerObject'` |

### **Data format** — 输入数据的格式 `SSC`（默认）| `C` | `CT` | `SC` | `SSSC`

输入数据的数据格式。这些选项使用与 `dlarray` 对象的 `fmt` 参数相同的表示法，但层模块不支持 Batch (`B`) 维度，而是假定观测数为 `1`。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataFormat` |
| **类型：** 字符向量 |
| **值：** `'SSC'` | `'C'` | `'CT'` | `'SC'` | `'SSSC'` |
| **默认值：** `'SSC'` |

### 执行

### **Sample time** — 用于指定采样时间的选项 `-1`（默认）| 标量

指定采样时间命中之间的离散间隔，或指定另一种采样时间类型，例如连续 (`0`) 或继承 (`-1`)。有关更多选项，请参阅 Types of Sample Time (Simulink)。

默认情况下，模块根据其在模型中的上下文继承采样时间。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |
| --- |
| **参数：** `SampleTime` |
| **数据类型：** `char` |
| **值：** `'-1'`（默认）| 标量 |

## 所属库

Deep Learning Toolbox / Deep Learning Layers / Combination Layers

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

### R2025a：**Layer** 参数默认值为 `'layerObject'`

从 R2025a 开始，**Layer** 参数的默认值为 `'layerObject'`。在以前的版本中，默认值为 `'layer'`。如果您的代码以编程方式创建 Simulink 并依赖名为 `'layer'` 的变量，请更新代码，使该变量名为 `'layerObject'`。

## 描述

深度拼接层

Depth Concatenation Layer 模块接收具有相同高度和宽度的输入，并沿通道维度将它们拼接。该模块接受的数据维度对应于通过 **Data format** 模块参数指定的格式。

`exportNetworkToSimulink` 函数生成此模块，以表示 `depthConcatenationLayer` 对象。
