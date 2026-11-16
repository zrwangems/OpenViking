---
type: simulink-block
title: 'Create Diagonal Matrix'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'creatediagonalmatrix'
documentation_source_path: 'slref/creatediagonalmatrix.html'
language: zh-CN
chinese_source: official
---

# Create Diagonal Matrix

## 端口

### 输入

### **Port\_1** — 输入信号 向量

输入转换为对角矩阵，指定为 *M* 元素向量。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持:** 是
### 输出

### **Port\_1** — 输出信号 矩阵

输出指定为 *M*×*M* 矩阵，其中 *M* 是输入向量的长度。

输出相当于：

```
A = diag(D)		% Equivalent MATLAB code
```

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持:** 是

## 参数

R2025b 官方文档未提供。

## 所属库

Simulink / Matrix Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

生成的代码在特定条件下依赖于 `memcpy` 或 `memset` 函数(`string.h`)。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

### R2021b: Create Diagonal Matrix 模块移至 Simulink 矩阵运算库

Create Diagonal Matrix 模块已从 **DSP System Toolbox** > **数学函数** > **矩阵和线性代数** > **矩阵运算** 库移至 **Simulink** > **矩阵运算** 库。所有现有模型均继续发挥作用。

## 描述

根据对角元素创建方对角矩阵

Create Diagonal Matrix 模块使用长度为 *M* 的向量输入 `D` 中包含的元素填充 *M*×*M* 矩阵输出的对角线。对角线以外的元素为零。

等效的 MATLAB® 代码如下：

```
A = diag(D)
```
