---
type: simulink-block
title: 'dB Gain'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Math Operations'
documentation_page: 'dbgain'
documentation_source_path: 'ref/dbgain.html'
language: zh-CN
chinese_source: worker-translation
---

# dB Gain

## 端口

### 输入

### **Input** — 输入信号 标量 | 向量 | 矩阵

将输入信号指定为标量、向量或大小为 *M*-by-*N* 的矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是
### 输出

### **Output** — 应用分贝增益后的输出 标量 | 向量 | 矩阵

应用分贝增益后的输出，返回为与输入信号具有相同大小、数据类型和复数特性的标量、向量或矩阵。

有关该模块如何应用分贝增益的更多信息，请参阅算法。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是

## 参数

**注意**

该模块在生成的代码中不支持可调性。

### **Gain, dB** — 增益 `-40`（默认）| 标量 | 矩阵

将应用于输入的分贝增益指定为标量或与输入矩阵大小相同的实数矩阵。

**可调：** 是

### **Input signal** — 输入信号 `Amplitude`（默认）| `Power`

将输入信号的类型指定为以下之一：

- `Power` –– 该模块将信号视为功率信号。
- `Amplitude` –– 该模块将信号视为电压信号。

**可调：** 是

## 所属库

DSP System Toolbox / Math Functions / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

该模块在生成的代码中不支持可调性。

## 版本历史

**在 R2006a 之前推出**

## 描述

应用分贝增益

dB Gain 模块将输入乘以 **Gain** 参数中指定的分贝值。您可以将输入指定为功率信号或电压信号。

有关该模块如何应用分贝增益的更多信息，请参阅算法。
