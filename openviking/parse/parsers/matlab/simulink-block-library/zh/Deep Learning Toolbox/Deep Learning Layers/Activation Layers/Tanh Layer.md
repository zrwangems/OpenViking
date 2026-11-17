---
type: simulink-block
title: 'Tanh Layer'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning Layers / Activation Layers'
documentation_page: 'tanhlayer'
documentation_source_path: 'ref/tanhlayer.html'
language: zh-CN
chinese_source: worker-translation
---

# Tanh Layer

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入数据 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: 输出数据 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输入

### **Port\_1** — 输入数据 标量 | 向量 | 矩阵

要执行双曲正切运算的矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 输出数据 标量 | 向量 | 矩阵

对输入矩阵执行双曲正切运算的结果。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## 参数
```yaml
parameters:
- name: Approximation method
  summary: 用于计算层输出的近似方法 None（默认）| CORDIC | Lookup
  group: 数据类型
  block_parameter: ApproximationMethod
  type: character vector
  values: '''none'' | ''CORDIC'' | ''Lookup'''
  default: '''none'''
- name: Sample time
  summary: 用于指定采样时间的选项 -1（默认）| 标量
  group: 执行
  block_parameter: SampleTime
  values: '''-1''（默认）| 标量'
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### 数据类型

### **Approximation method** — 用于计算层输出的近似方法 `None`（默认）| `CORDIC` | `Lookup`

指定用于计算输出的近似方法类型。

| 近似方法 | 支持的数据类型 | 何时使用此方法 |
| --- | --- | --- |
| `None`（默认） | 浮点 | 仅处理浮点数据时。 |
| `CORDIC` | 浮点（double 和 single）以及 **Bias** 值为 `0` 且 **Slope** 值为 2 的幂的定点 | 处理定点数据并希望部署到 FPGA 硬件时。 |
| `Lookup` | 浮点和定点 | 处理定点数据并希望生成 C/C++ 代码时。 |

有关 CORDIC 近似方法的详细信息，请参阅 `cordictanh` (Fixed-Point Designer)。

#### 编程使用

|  |
| --- |
| **模块参数**：`ApproximationMethod` |
| **类型**：character vector |
| **值**：`'none'` | `'CORDIC'` | `'Lookup'` |
| **默认值**：`'none'` |

### 执行

### **Sample time** — 用于指定采样时间的选项 `-1`（默认）| 标量

指定采样时间命中之间的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`-1`）。有关更多选项，请参阅 Types of Sample Time (Simulink)。

默认情况下，模块根据其在模型中的上下文继承采样时间。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |
| --- |
| **Parameter:** `SampleTime` |
| **Data Types:** `char` |
| **值**：`'-1'`（默认）| 标量 |
## 所属库

Deep Learning Toolbox / Deep Learning Layers / Activation Layers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

双曲正切 (tanh) 层

Tanh Layer 模块对层输入应用 tanh 函数。

`exportNetworkToSimulink` 函数生成此模块以表示 `tanhLayer` 对象。由于它执行逐元素运算，此模块支持任意格式的输入数据，并输出与输入具有相同维度和格式的数据。
