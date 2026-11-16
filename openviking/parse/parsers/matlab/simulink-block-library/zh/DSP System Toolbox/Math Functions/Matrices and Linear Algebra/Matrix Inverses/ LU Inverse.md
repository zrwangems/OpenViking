---
type: simulink-block
title: 'LU Inverse'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Inverses'
documentation_page: 'luinverse'
documentation_source_path: 'ref/luinverse.html'
language: zh-CN
chinese_source: worker-translation
---

# LU Inverse

## 端口

### 输入

### **Input** — 输入方阵 方阵

指定输入为 *M*-by-*M* 方阵。

**数据类型：** `single` | `double`
**复数支持：** Yes
### 输出

### **Output** — 矩阵的逆 方阵

矩阵的逆，以 *M*-by-*M* 方阵形式返回。

**数据类型：** `single` | `double`
**复数支持：** Yes

## 参数

R2025b 中未记录。

## 所属库

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Inverses

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

生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用 LU 分解计算方阵的逆

LU Inverse 模块通过对其行选主元变体 *A**p* 进行分解并求逆，计算方阵输入 *A* 的逆。

Ap−1=(LU)−1

*L* 是对角线元素为 1 的下三角方阵，*U* 是上三角方阵。该模块输出逆矩阵 *A*-1。
