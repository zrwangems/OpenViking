---
type: simulink-block
title: 'Concatenation Layer'
family: 'deeplearning'
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
```yaml
ports:
- name: Port_1
  summary: 第一个输入数据数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_2
  summary: 第二个输入数据 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_N
  summary: 第 *N* 个输入数据 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: 拼接后的输出数据数组
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输入

### **Port\_1** — 第一个输入数据数组

要拼接的第一个输入，以遵循通过 **Data format** 参数指定的格式的数组形式提供。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_2** — 第二个输入数据 标量 | 向量 | 矩阵

要拼接的第二个输入，以遵循通过 **Data format** 参数指定的格式的数组形式提供。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_N** — 第 *N* 个输入数据 标量 | 向量 | 矩阵

要拼接的第 *N* 个输入，以遵循通过 **Data format** 参数指定的格式的数组形式提供。该模块的输入端口数量等于通过 **Layer** 参数指定的对象的 `NumInputs` 属性值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 拼接后的输出数据数组

拼接后的输出数据。输出数据的维度对应于通过 **Data format** 模块参数指定的格式。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## 参数
```yaml
parameters:
- name: Layer
  summary: 对应的层对象 layerObject（默认）| concatenationLayer 对象
  group: 主要
  block_parameter: Layer
  type: workspace variable
  values: concatenationLayer object
  default: '''layerObject'''
- name: Data format
  summary: 输入数据的格式 SSC（默认）| C | CT | SC | SSSC
  group: 主要
  block_parameter: DataFormat
  type: character vector
  values: '''SSC'' | ''C'' | ''CT'' | ''SC'' | ''SSSC'''
  default: '''SSC'''
- name: Sample time
  summary: 用于指定采样时间的选项 -1（默认）| 标量
  group: 执行
  block_parameter: SampleTime
  values: '''-1'' (default) | scalar'
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### 主要

### **Layer** — 对应的层对象 `layerObject`（默认）| `concatenationLayer` 对象

指定包含来自训练网络的 `concatenationLayer` 对象的工作区变量名称。Concatenation Layer 模块通过使用该对象的属性来配置自身。

#### 编程使用

|  |
| --- |
| **模块参数**：`Layer` |
| **类型**：workspace variable |
| **值**：`concatenationLayer` object |
| **默认值**：`'layerObject'` |

### **Data format** — 输入数据的格式 `SSC`（默认）| `C` | `CT` | `SC` | `SSSC`

输入数据的格式。这些选项使用与 `dlarray` 对象的 `fmt` 参数相同的表示法，但层模块不支持 Batch（`B`）维度，而是假定观测数为 `1`。

#### 编程使用

|  |
| --- |
| **模块参数**：`DataFormat` |
| **类型**：character vector |
| **值**：`'SSC'` | `'C'` | `'CT'` | `'SC'` | `'SSSC'` |
| **默认值**：`'SSC'` |

### 执行

### **Sample time** — 用于指定采样时间的选项 `-1`（默认）| 标量

指定采样时间命中的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`-1`）。有关更多选项，请参阅 Types of Sample Time (Simulink)。

默认情况下，该模块根据其在模型中的上下文继承采样时间。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |
| --- |
| **Parameter:** `SampleTime` |
| **Data Types:** `char` |
| **值**：`'-1'` (default) | scalar |
## 所属库

Deep Learning Toolbox / Deep Learning Layers / Combination Layers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

### R2025a：**Layer** 参数默认值为 `'layerObject'`

从 R2025a 开始，**Layer** 参数的默认值为 `'layerObject'`。在以前的版本中，默认值为 `'layer'`。如果您有以编程方式创建 Simulink 并依赖于名称为 `'layer'` 的变量的代码，请更新代码，使该变量的名称为 `'layerObject'`。

## 描述

拼接层

Concatenation Layer 模块接收输入并沿指定维度将它们拼接。除拼接维度外，输入在所有维度上必须具有相同的大小。该模块接受具有对应于通过 **Data format** 模块参数指定的格式的维度的数据。

`exportNetworkToSimulink` 函数生成此模块以表示 `concatenationLayer` 对象。
