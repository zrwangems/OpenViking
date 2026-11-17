---
type: simulink-block
title: 'Autocorrelation LPC'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Estimation / Linear Prediction'
documentation_page: 'autocorrelationlpc'
documentation_source_path: 'ref/autocorrelationlpc.html'
language: zh-CN
chinese_source: worker-translation
---

# Autocorrelation LPC

## 端口

### 输入

### **Input 1** — 输入数组 无向向量 | 列向量 | 矩阵

将输入 *u* 指定为无向向量、列向量或矩阵。行向量不是有效输入。该模块将所有 *M*×*N* 矩阵输入视为 *N* 个长度为 *M* 的通道。

**数据类型：** `single` | `double`
### 输出

### **A** — 多项式系数 列向量 | 矩阵

当您将 **Output(s)** 参数设置为 `A` 或 `A and K` 时生成的多项式系数。对于每个输入通道，端口 A 输出一个 (*N*+1)×1 列向量 *a* = [1 *a2**a3* ... *aN+1*]T，其中包含一个 *N* 阶滑动平均（MA）线性过程的系数，该过程预测输入时间序列中的下一个值 *ûM+1*。

u^M+1=−(a2uM)−(a3uM−1)−...−(aN+1uM−N+1)

#### 依赖关系

要启用端口 A，请将 **Output(s)** 设置为 `A` 或 `A and K`。

**数据类型：** `single` | `double`

### **K** — 反射系数 列向量 | 矩阵

当 **Output(s)** 设置为 `K` 或 `A and K` 时生成的反射系数。对于每个输入通道，端口 K 输出一个长度为 *N* 的列向量，其元素为预测误差反射系数。

#### 依赖关系

要启用端口 K，请将 **Output(s)** 设置为 `A` 或 `A and K`。

**数据类型：** `single` | `double`

### **P** — 预测误差功率 向量

端口 P 输出的预测误差功率，其长度等于输入通道数。

#### 依赖关系

要启用端口 P，请选中 **Output prediction error power (P)** 参数。

**数据类型：** `single` | `double`

## 参数

### **Output(s)** — 预测系数类型 `A`（默认）| `A and K` | `K`

指定该模块输出的预测系数类型。该模块可以输出多项式系数（`A`）、反射系数（`K`）或两者（`A and K`）。

当您将 **Output(s)** 设置为 `A and K` 时，该模块启用端口 A 和 K，每个端口为每个通道输出其各自的预测系数集。

### **Output prediction error power (P)** — 输出预测误差功率 `off`（默认）| `on`

选中此参数以启用输出端口 `P`，该端口输出预测误差功率。

### **Inherit prediction order from input dimensions** — 从输入维度继承预测阶数 `off`（默认）| `on`

选中此参数以从输入维度继承预测阶数 *N*。

### **Prediction order (N)** — 预测阶数 `1`（默认）| 标量

指定预测阶数 *N*。请注意，*N* 必须是一个标量，其值小于输入通道的长度，否则该模块将产生错误。

#### 依赖关系

此参数仅在您未选中 **Inherit prediction order from input dimensions** 参数时显示。

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

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

确定 N 阶前向线性预测器的系数

Autocorrelation LPC 模块通过最小化最小二乘意义上的预测误差，为每个长度为 *M* 的输入通道 *u* 中的时间序列确定 *N* 步前向线性预测器的系数。线性预测器是一种 FIR 滤波器，它根据当前和过去的输入预测序列中的下一个值。该技术应用于滤波器设计、语音编码、频谱分析和系统辨识。

Autocorrelation LPC 模块可以将每个通道的预测误差输出为多项式系数、反射系数或两者。该模块还可以输出每个通道的预测误差功率。
