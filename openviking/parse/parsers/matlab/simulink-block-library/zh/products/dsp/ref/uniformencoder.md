---
type: simulink-block
title: 'Uniform Encoder'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Fixed-Point Design / Quantizers'
documentation_page: 'uniformencoder'
documentation_source_path: 'ref/uniformencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Uniform Encoder

## 端口

### 输入

### **Input** — 输入信号向量 | 矩阵

指定浮点输入信号为向量或矩阵。
大于
(1−21−*B*)*V*
或小于 −*V* 的输入会在各自的值处饱和。
复数输入的实部和虚部独立饱和。

**数据类型：** `single` | `double`
**复数支持：** Yes

### 输出

### **Output** — 编码器输出向量 | 矩阵

编码器输出，返回为向量或矩阵。该模块对浮点输入中的每个样本进行量化，并将量化后的浮点值编码为整数值。有关该模块如何计算输出的更多信息，请参阅算法。

**数据类型：** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
**复数支持：** Yes

## 参数

### **Peak** — 要编码的最大输入幅度 `1`（默认） | 非负标量

将最大输入幅度 *V* 指定为非负标量。大于
(1−21−*B*)*V*
或小于 −*V* 的实部或虚部输入值会在这些限值处饱和（对于复数输入独立饱和）。

### **Bits** — 位数 `8`（默认） | 范围为 [`2`, `32`] 的整数

指定该模块表示整数输出所需的位数 *B*。位数 *B* 可以是 2 到 32（含）之间的任意整数值。该模块对浮点输入进行量化的级数为 2*B*。

### **Output type** — 模块输出的数据类型 `Unsigned integer`（默认） | `Signed integer`

将模块输出的数据类型指定为以下之一：

- `Unsigned integer` –– 该模块将最小的量化浮点值 −*V* 映射为整数 0，并将最大的量化浮点值 (1−21−*B*)*V* 映射为整数 2*B*−1。它线性（均匀）地将中间量化浮点值映射到范围 [0, 2*B*−1] 内的中间整数。为提高效率，该模块会自动选择一种 *unsigned* 输出数据类型（`uint8`、`uint16` 或 `uint32`），其位数等于或大于 *B* 且为最小位数。
- `Signed integer` –– 该模块将最小的量化浮点值 −*V* 映射为整数 −2*B*−1，并将最大的量化浮点值 (1−21−*B*)*V* 映射为整数 2*B*−1−1。它线性地将中间量化浮点值映射到范围 [−2*B*−1, 2*B*−1−1] 内的中间整数。该模块会自动选择一种 *signed* 输出数据类型（`int8`、`int16` 或 `int32`），其位数等于或大于 *B* 且为最小位数。

此表显示了该模块使用的输出数据类型。

| Bits | Unsigned Integer | Signed Integer |
| --- | --- | --- |
| `2` 到 `8` | `uint8` | `int8` |
| `9` 到 `16` | `uint16` | `int16` |
| `17` 到 `32` | `uint32` | `int32` |

## 所属库

DSP System Toolbox / Quantizers

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**于 R2006a 之前引入**

## 描述

将浮点输入量化和编码为整数输出

Uniform Encoder 模块对输入向量或矩阵中的每个浮点样本执行以下两个操作：

1. 使用相同精度对该值进行量化
2. 将量化后的浮点值编码为整数值

有关该模块如何计算输出的更多信息，请参阅算法。

Uniform Encoder 模块的操作遵循 ITU-T Recommendation G.701 中规定的均匀编码定义。
