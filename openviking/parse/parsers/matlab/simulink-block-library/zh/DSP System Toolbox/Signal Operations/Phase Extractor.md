---
type: simulink-block
title: 'Phase Extractor'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'phaseextractor'
documentation_source_path: 'ref/phaseextractor.html'
language: zh-CN
chinese_source: worker-translation
---

# Phase Extractor

## 端口

### 输入

### **Input 1** — 输入信号向量 | 矩阵

将输入信号指定为向量或矩阵。当输入为矩阵时，模块将信号的每一列视为一个独立通道。第一个维度是通道长度。第二个维度是通道数。模块将一维输入视为一个通道。

**数据类型：** `single` | `double`
**复数支持：** Yes
### 输出

### **Output 1** — 解缠相位向量 | 矩阵

模块返回信号的解缠相位。

模块保留输入的大小和维度，输出端口速率等于输入端口速率。

**数据类型：** `single` | `double`

## 参数

### **Unwrap phase only within the frame** — 仅在帧内解缠相位 `off`（默认） | `on`

当您清除此复选框时，模块忽略输入帧之间的边界。当您选中此复选框时，模块独立处理每个输入数据帧，并为每个新的输入帧重置初始相位值。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认） | `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` –– 使用
  MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` –– 使用
  生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码会复用于
  后续仿真。此选项需要额外的启动时间，但可提供更快的后续
  仿真。

## 所属库

DSP System Toolbox / Signal Operations

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

## 版本历史

**在 R2014b 中引入**

### R2024a：**Simulate using** 参数的默认值变更

**Simulate using** 参数的默认值现在为
`Interpreted execution`。通过此更改，模块默认使用
MATLAB 解释器进行仿真。

## 描述

提取复数输入的解缠相位

Phase Extractor 模块提取复数输入的解缠相位。
