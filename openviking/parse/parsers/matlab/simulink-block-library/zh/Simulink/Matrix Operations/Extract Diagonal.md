---
type: simulink-block
title: 'Extract Diagonal'
family: 'matrix-operations'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'extractdiagonal'
documentation_source_path: 'slref/extractdiagonal.html'
language: zh-CN
chinese_source: worker-translation
---

# Extract Diagonal

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

要从其提取对角线的输入矩阵，指定为标量、向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** Yes

### 输出

### **Port\_1** — 输出信号 向量

每个对角线元素的输出向量。

输出与输入具有相同的数据类型和复数性。输出向量的长度为 `min(M,N)`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** Yes

## 参数

未在 R2025b 中记录。

## 所属库

Simulink / Matrix Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖于 `memcpy` 或
`memset` 函数（`string.h`）。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**R2006a 之前引入**

### R2021b：Extract Diagonal 模块已移至 Simulink Matrix Operations 库

Extract Diagonal 模块已从 **DSP System Toolbox** > **Math Functions** > **Matrices and Linear Algebra** > **Matrix Operations** 库移至 **Simulink** > **Matrix Operations** 库。所有现有模型继续正常工作。

## 描述

提取输入矩阵的主对角线

Extract Diagonal 模块使用 *M*×*N* 输入矩阵 `A` 主对角线上的元素填充未定向的输出向量。

等效的 MATLAB® 代码如下：

```
D = diag(A)
```
