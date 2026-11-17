---
type: simulink-block
title: 'Detrend'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'detrend'
documentation_source_path: 'ref/detrend.html'
language: zh-CN
chinese_source: worker-translation
---

# Detrend

## 端口

### 输入

### **Input** — 输入数据向量

输入数据，指定为向量。该模块会去除在最小二乘意义上最佳拟合数据的直线。

**数据类型：** `single` | `double`
### 输出

### **Output** — 输出数据列向量

输出数据，以列向量形式返回。该模块在去除最小二乘意义上最佳拟合数据的直线后，返回剩余数据。

**数据类型：** `single` | `double`

## 参数

R2025b 中未记录。

## 所属库

DSP System Toolbox / Statistics

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `No` |
| **可变大小信号** | `No` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖 `memcpy` 或
`memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

从向量中去除线性趋势

Detrend 模块通过减去在最小二乘意义上最佳拟合数据的直线，从长度为 *M* 的输入向量 *u* 中去除线性趋势。

最小二乘直线 *û* = *ax* +
*b* 是具有参数 *a* 和
*b* 的直线，它使以下量最小化

∑i=1M(ui−u^i)2

其中 *x* 取 *M* 个等间距值，
*ui* 是输入向量中的第 *i* 个元素。输出 *y* =
*u*-*û* 始终是一个 *M*×1 列向量。
