---
type: simulink-block
title: 'LDL Solver'
family: 'math-functions'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Linear System Solvers'
documentation_page: 'ldlsolver'
documentation_source_path: 'ref/ldlsolver.html'
language: zh-CN
chinese_source: worker-translation
---

# LDL Solver

## 端口

### 输入

### **S** — 系统矩阵 方阵

将系统矩阵 S 指定为大小为 *M*-by-*M* 的 Hermitian 正定方阵。仅使用矩阵的对角线和下三角部分，并且忽略对角线元素的任何虚部。当输入不是正定时，模块将按照 **非正定输入** 参数指定的行为进行响应。有关详细信息，请参阅 **非正定输入** 参数的描述。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **B** — 系统方程右侧矩阵 向量 | 矩阵

将系统方程 S*X* = B 的右侧矩阵 B 指定为 *M*-by-*N* 矩阵。

右侧 B 的长度为 *M* 的无方向向量输入将被视为 *M*-by-1 矩阵。

**数据类型：** `single` | `double`
**复数支持：** Yes
### 输出

### **X** — 方程组的解 向量 | 矩阵

方程组 S*X* = B 的唯一解，以 *M*-by-*N* 矩阵 *X* 形式返回。

有关模块如何确定此解的详细信息，请参阅算法。

**数据类型：** `single` | `double`
**复数支持：** Yes

## 参数

### **非正定输入** — 非正定输入 `Ignore`（默认） | `Warning` | `Error`

将针对非正定矩阵输入的响应指定为 `Ignore`、`Warning` 或 `Error`。

该算法要求输入为 Hermitian 正定。当输入不是正定时，模块将按照 **非正定输入** 参数指定的行为进行响应。将此参数设置为：

- `Ignore` — 模块继续计算，并且不发出警报。输出不是有效解。
- `Warning` — 模块继续计算，并在 MATLAB® 命令窗口中显示警告消息。输出不是有效解。
- `Error` — 模块显示错误对话框并终止仿真。

**注意**

**非正定输入** 参数是诊断参数。与配置参数对话框上的所有诊断参数一样，在 Simulink® Coder™ 代码生成软件为此模块生成的代码中，它被设置为 `Ignore`。

## 所属库

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Linear System Solvers

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

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

当 S 是方阵 Hermitian 正定矩阵时，求解 S X = B

LDL Solver 模块通过对 **S** 端口处的 Hermitian 正定方阵应用 LDL 分解来求解线性方程组 S*X* = B。有关详细信息，请参阅算法。
