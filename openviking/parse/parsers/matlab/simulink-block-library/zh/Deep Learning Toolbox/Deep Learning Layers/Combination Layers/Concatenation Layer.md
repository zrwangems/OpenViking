---
type: simulink-block
title: 'Concatenation Layer'
family: 'deep-learning-layers'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning Layers / Combination Layers'
documentation_page: 'concatenationlayer'
documentation_source_path: 'ref/concatenationlayer.html'
language: zh-CN
chinese_source: worker-translation
---

# Concatenation Layer

## 端口

### 输入

### **Port\_1** — 第一个输入数据数组

要串联的第一个输入，以数组形式提供，该数组遵循使用 **数据格式** 参数指定的格式。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_2** — 第二个输入数据 标量 | 向量 | 矩阵

要串联的第二个输入，以数组形式提供，该数组遵循使用 **数据格式** 参数指定的格式。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_N** — 第 *N* 个输入数据 标量 | 向量 | 矩阵

要串联的第 *N* 个输入，以数组形式提供，该数组遵循使用 **数据格式** 参数指定的格式。模块的输入端口数等于使用 **层** 参数指定的对象的 `NumInputs` 属性值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 输出

### **Port\_1** — 串联后的输出数据数组

串联后的输出数据。输出数据具有与 **数据格式** 模块参数指定格式对应的维度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的**仿真**选项卡上的**准备**库中，选择**属性检查器**。

### 主要

### **层** — 对应的层对象 `layerObject`（默认）| `concatenationLayer` 对象

指定一个工作区变量的名称，该变量包含来自已训练网络的 `concatenationLayer` 对象。Concatenation Layer 模块使用该对象的属性自行配置。

#### 编程用法

|  |
| --- |
| **模块参数：** `Layer` |
| **类型：** 工作区变量 |
| **值：** `concatenationLayer` 对象 |
| **默认值：** `'layerObject'` |

### **数据格式** — 输入数据的格式 `SSC`（默认）| `C` | `CT` | `SC` | `SSSC`

输入数据的格式。这些选项使用与 `dlarray` 对象的 `fmt` 参数相同的表示法，但层模块不支持 Batch (`B`) 维度，而是假定观测编号为 `1`。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataFormat` |
| **类型：** 字符向量 |
| **值：** `'SSC'` | `'C'` | `'CT'` | `'SC'` | `'SSSC'` |
| **默认值：** `'SSC'` |

### 执行

### **采样时间** — 用于指定采样时间的选项 `-1`（默认）| 标量

指定采样时间点之间的离散间隔，或指定其他类型的采样时间，例如连续 (`0`) 或继承 (`-1`)。有关更多选项，请参阅采样时间的类型 (Simulink)。

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

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

### R2025a：**层** 参数的默认值为 `'layerObject'`

从 R2025a 开始，**层** 参数的默认值为 `'layerObject'`。在之前的版本中，默认值为 `'layer'`。如果你的代码以编程方式创建 Simulink 并依赖名为 `'layer'` 的变量，请更新代码，使该变量名为 `'layerObject'`。

## 描述

串联层

Concatenation Layer 模块接受输入，并沿指定维度将它们串联起来。除串联维度外，输入在所有维度上必须具有相同大小。此模块接受的数据具有与 **数据格式** 模块参数指定格式对应的维度。

`exportNetworkToSimulink` 函数生成此模块以表示 `concatenationLayer` 对象。
