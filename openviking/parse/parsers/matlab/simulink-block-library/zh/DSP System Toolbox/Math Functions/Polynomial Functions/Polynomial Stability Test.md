---
type: simulink-block
title: 'Polynomial Stability Test'
family: 'math-functions'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Polynomial Functions'
documentation_page: 'polynomialstabilitytest'
documentation_source_path: 'ref/polynomialstabilitytest.html'
language: zh-CN
chinese_source: worker-translation
---

# Polynomial Stability Test

## 端口

### 输入

### **Input** — 输入多项式向量 | 矩阵

指定输入多项式为大小为 *M* × *N* 的向量或矩阵。

输入矩阵 *u* 的每一列包含来自不同多项式的 *M* 个系数

f(x)=u1xM−1+u2xM−2+…+uM

按降幂顺序排列 *u*1、*u*2、...、*u*M。该多项式的阶数为 *M* − 1，并包含正整数指数。

该模块始终将长度为 *M* 的无方向向量输入视为 *M* × 1 矩阵。

**数据类型：** `single` | `double`
**复数支持：** Yes

### 输出

### **Output** — 多项式稳定性测试输出 标量 | 1 × *N* 矩阵

多项式稳定性测试输出，返回为标量或 1 × *N* 矩阵，每列包含值 `1` 或 `0`。

值 `1` 表示输入对应列中的多项式是稳定的，也就是说，*f(x)* = 0 的所有解的幅值都小于 1。值 `0` 表示输入对应列中的多项式可能不稳定，也就是说，*f*(*x*) = 0 的至少一个解的幅值大于或等于 1。

**数据类型：** `Boolean`

## 参数

### **Simulate using** — 要运行的仿真类型 `Interpreted execution` (默认) | `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` –– 使用
  MATLAB 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` –– 使用
  生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码会在后续仿真中重用。此选项
  需要额外的启动时间，但可提供更快的后续仿真。

## 所属库

DSP System Toolbox / Math Functions / Polynomial Functions

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `No` |
| **可变大小信号** | `No` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用 Schur-Cohn 算法确定输入多项式的所有根是否位于单位圆内

Polynomial Stability Test 模块使用 Schur-Cohn 算法确定多项式的所有根是否位于单位圆内。

下面是该模块的等效 MATLAB® 代码。

    y = all(abs(roots(u)) < 1)

此模块最常用于检查传递函数 *H*(*z*) 的分母多项式 *A*(*z*) 的极点位置。

H(z)=B(z)A(z)=b1+b2z−1+…+bmz−(m−1)a1+a2z−1+…+anz−(n−1)

极点是分母多项式 *A*(*z*) 的 *n* − 1 个根。当任何极点位于单位圆外时，传递函数 *H*(*z*) 不稳定。正如 DSP 应用中的典型情况，传递函数 *H*(*z*) 以 *z*−1 的降幂而不是 *z* 的降幂指定。
