---
type: simulink-block
title: 'Extract Triangular Matrix'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics and Linear Algebra / Array and Matrix Mathematics / Matrix Operations'
documentation_page: 'extracttriangularmatrix'
documentation_source_path: 'ref/extracttriangularmatrix.html'
language: zh-CN
chinese_source: worker-translation
---

# Extract Triangular Matrix

## 端口

### 输入

### **A** — 输入向量 | 矩阵

将输入指定为大小为 *M*-by-*N* 的向量或矩阵。该模块将长度为 *M* 的无向向量输入视为 *M*-by-1 矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** Yes

### 输出

### **U** — 下三角或上三角输出向量 | 矩阵

提取输入矩阵的下三角或上三角。当您将 **Extract** 参数设置为：

- `Upper` — 该模块将输入矩阵主对角线上及以上的元素复制到相同大小的输出矩阵。输出矩阵的第一行与输入矩阵的第一行相同。输出矩阵主对角线以下的元素为零。
- `Lower` — 该模块将输入矩阵主对角线上及以下的元素复制到相同大小的输出矩阵。输出矩阵的第一列与输入矩阵的第一列相同。输出矩阵主对角线以上的元素为零。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** Yes

## 参数

### **Extract** — 要提取的矩阵分量 `Upper`（默认）| `Lower`

指定要复制到输出的矩阵分量：

- `Upper` — 该模块将输入矩阵主对角线上及以上的元素复制到相同大小的输出矩阵。输出矩阵的第一行与输入矩阵的第一行相同。输出矩阵主对角线以下的元素为零。
- `Lower` — 该模块将输入矩阵主对角线上及以下的元素复制到相同大小的输出矩阵。输出矩阵的第一列与输入矩阵的第一列相同。输出矩阵主对角线以上的元素为零。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项缩短启动时间。
- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不更改，后续仿真会重用该 C 代码。此选项需要额外的启动时间，但可提供更快的后续仿真。

## 所属库

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Operations

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

生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

### R2024a：**Simulate using** 参数默认值的更改

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此更改，该模块默认使用 MATLAB 解释器进行仿真。

## 描述

从输入矩阵中提取下三角或上三角

Extract Triangular Matrix 模块根据 *M*-by-*N* 输入矩阵的上三角或下三角元素创建三角矩阵输出。该模块将长度为 *M* 的无向向量输入视为 *M*-by-1 矩阵。
