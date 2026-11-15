---
type: simulink-block
title: 'Permute Dimensions'
family: math-operations
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'permutedimensions'
language: zh-CN
chinese_source: worker-translation
---

# Permute Dimensions

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

此端口接受 Simulink® 支持的任何数据类型的标量、向量、矩阵和 N 维信号，包括 fixed-point、enumerated 和 nonvirtual bus 数据类型。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### 输出

### **Port\_1** — 输入信号的置换 标量 | 向量 | 矩阵 | N 维数组

模块根据 **Order** 参数的值输出输入信号的置换。输出与输入具有相同的数据类型。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **Order** — 置换向量 `[2,1]`（默认） | `N` 元素向量，其中 `N` 是输入信号的维数

指定要应用于输入信号维度的置换顺序。此参数的值必须是一个 `N` 元素向量，其中 `N` 是输入信号的维数。置换向量的元素必须是从 1 到 `N` 的值的重新排列。

例如，将置换向量 `[2 1]` 应用于 5×3 输入信号会得到一个 3×5 输出信号，换句话说，即输入信号的转置。

#### 编程使用

|  |
| --- |
| **模块参数**：`Order` |
| **类型**：character vector |
| **值**：`N` 元素向量 |
| **默认值**：`'[2 1]'` |

## 所属库

Simulink / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **零交叉检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2007a 中引入**

## 描述

重新排列多维数组的维度

Permute Dimensions 模块通过置换输入信号的维度来重新排列输入信号的元素。您使用 **Order** 参数指定要应用于输入信号的置换。

例如，要转置 3×5 输入信号，请为 **Order** 参数指定置换向量 `[2
1]`。这样做时，模块会重新排列输入信号的元素并输出一个 5×3 矩阵。

可以将总线数组用作 Permute Dimensions 模块的输入信号。有关定义和使用总线数组的详细信息，请参阅总线数组中的非虚拟总线分组。
