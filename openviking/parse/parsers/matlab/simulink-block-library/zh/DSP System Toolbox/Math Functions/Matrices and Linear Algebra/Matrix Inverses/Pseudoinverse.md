---
type: simulink-block
title: 'Pseudoinverse'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Inverses'
documentation_page: 'pseudoinverse'
documentation_source_path: 'ref/pseudoinverse.html'
language: zh-CN
chinese_source: worker-translation
---

# Pseudoinverse

## 端口

### 输入

### **A** — 输入向量 | 矩阵

将输入指定为向量或矩阵。

**数据类型：** `single` | `double`
**复数支持：** Yes
### 输出

### **X** — 伪逆输出向量 | 矩阵

伪逆输出，以向量或矩阵形式返回。如果伪逆计算无法收敛，此端口上的输出为正确大小的未定义矩阵。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **E** — 错误状态 `0` | `1`

此端口可接收的错误状态的可能值为：

- `0` — 伪逆计算收敛。
- `1` — 伪逆计算不收敛。

如果伪逆计算无法收敛，端口 **X** 处的输出为正确大小的未定义矩阵。

**数据类型：** `Boolean`

## 参数

### **Show error status port (E)** — Show error status port `off`（默认） | `on`

选择此项以启用 **E** 输出端口，该端口报告收敛失败。有关更多详细信息，请参阅 **E** 输出端口的描述。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认） | `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` —— 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。对于此模块，此模式下的仿真速度快于 `Code generation`。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不更改，后续仿真会重用该 C 代码。此选项需要额外的启动时间，但仿真速度会随着后续仿真而提高。

## 所属库

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Inverses

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算矩阵的 Moore-Penrose 伪逆

Pseudoinverse 模块计算输入矩阵 *A* 的 Moore-Penrose 伪逆。

等价的 MATLAB® 代码为：

    [U,S,V] = svd(A,0)
