---
type: simulink-block
title: 'LSF/LSP to LPC Conversion'
family: 'estimation'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Estimation / Linear Prediction'
documentation_page: 'lsflsptolpcconversion'
documentation_source_path: 'ref/lsflsptolpcconversion.html'
language: zh-CN
chinese_source: worker-translation
---

# LSF/LSP to LPC Conversion

## 端口

### 输入

### **LSP** — 线谱对 向量 | 矩阵

将线谱对指定为取值范围为 (−1 1) 的值的向量，按递减顺序。如果指定矩阵，模块将矩阵的每一列视为单独通道。当指定未定向向量时，模块将输入视为一个通道。这些值等于 0 到 π radians 之间的 LSF 值的余弦。不要包含保证的 LSP 值，−1 和 1。

**数据类型：** `single` | `double`

### **LSFn** — 归一化到范围 (0 0.5) 的线谱频率 向量 | 矩阵

将归一化到范围 (0 0.5) 的线谱频率指定为按递增顺序的向量或矩阵。如果指定矩阵，模块将矩阵的每一列视为单独通道。当指定未定向向量时，模块将输入视为一个通道。可以通过将 0 到 π radians 之间的 LSF 值除以 2π 来获得这些值。不要包含保证的 LSF 值，0 和 0.5。

**数据类型：** `single` | `double`

### **LSFr** — 范围 (0 π) 内的线谱频率 向量 | 矩阵

将范围 (0 π) 内的线谱频率指定为按递增顺序的向量或矩阵。如果指定矩阵，模块将矩阵的每一列视为单独通道。当指定未定向向量时，模块将输入视为一个通道。不要包含保证的 LSF 值，0 和 π。

**数据类型：** `single` | `double`
### 输出

### **A** — 线性预测系数 向量 | 矩阵

线性预测系数，以向量或矩阵形式返回。

**数据类型：** `single` | `double`

## 参数

### **Input** — 线谱对或线谱频率 `LSP in range (-1 1)` (default) | `LSF normalized in range (0 0.5)` | `LSF in range (0 pi)`

当将此参数选择为：

- `LSP in range (-1 1)` –– 模块将范围 (−1 1) 内的线谱对转换为线性预测系数。
- `LSF in range (0 pi)` –– 模块将范围 (0 π) 内的线谱频率转换为线性预测系数。
- `LSF normalized in range (0 0.5)` –– 模块将归一化到范围 (0 0.5) 的线谱频率转换为线性预测系数。

## 所属库

DSP System Toolbox / Estimation / Linear Prediction

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

**在 R2006a 之前引入**

## 描述

将线谱频率或线谱对转换为线性预测系数

LSF/LSP to LPC Conversion 模块将线谱对 (LSPs) 或线谱频率 (LSFs) 转换为线性预测多项式系数 (LPCs)。当将 LSFs 转换为 LPCs 时，模块输出与 `lsf2poly` 函数的输出一致。
