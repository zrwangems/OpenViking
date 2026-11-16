---
type: simulink-block
title: '2-D Correlation'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: '2dcorrelation'
documentation_source_path: 'ref/2dcorrelation.html'
language: zh-CN
chinese_source: worker-translation
---

# 2-D Correlation

## 端口

### 输入

### **I1** — 第一输入矩阵矩阵

第一输入矩阵，指定为 *M*×*N* 矩阵。两个输入矩阵必须具有相同类别的数据类型，例如 `double`、`single`、无符号整数（`uint8`、`uint16`、`uint32`、`uint64`）或整数（`int8`、`int16`、`int32`、`int64`）。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** Yes

### **I2** — 第二输入矩阵矩阵

第二输入矩阵，指定为 *P*×*Q* 矩阵。两个输入矩阵必须具有相同类别的数据类型，例如 `double`、`single`、无符号整数（`uint8`、`uint16`、`uint32`、`uint64`）或整数（`int8`、`int16`、`int32`、`int64`）。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** Yes

### 输出

### **Port\_1** — 计算得到的互相关标量 | 向量 | 矩阵

计算得到的互相关，以标量、向量或矩阵形式返回。互相关输出的尺寸取决于 **Output size** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** Yes

## 参数

### 主

### **Output size** — 互相关输出的大小 `Full`（默认） | `Same as input port I1` | `Valid`

互相关输出的大小。

- 如果选择 `Full`，输出维度为 (*M*+*P*-1)×(*N*+*Q*-1)。
- 如果选择 `Same as input port I1`，输出维度与端口 **I1** 处的输入相同。该模块返回互相关矩阵的中心部分，其大小与端口 **I1** 处的输入相同。
- 如果选择 `Valid`，输出维度为 (*M*-*P*+1)×(*N*-*Q*+1)。该模块仅返回未使用零填充边缘计算的互相关矩阵部分。

### **Normalized output** — 归一化互相关输出 `off`（默认） | `on`

如果输入的数据类型为浮点，请选择此参数。互相关输出的值归一化到 [0, 1]。

### 数据类型

有关定点模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

### **Lock data type settings against change by the fixed-point tools** — 阻止定点工具覆盖数据类型 `off`（默认） | `on`

选择此参数可阻止定点工具覆盖您在此模块上指定的数据类型。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

## 所属库

Computer Vision Toolbox / Statistics

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算两个输入矩阵的二维相关性

2-D Correlation 模块计算两个输入矩阵之间的二维互相关。
