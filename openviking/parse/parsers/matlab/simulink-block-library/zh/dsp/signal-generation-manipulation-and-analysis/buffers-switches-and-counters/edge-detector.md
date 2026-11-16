---
type: simulink-block
title: 'Edge Detector'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Buffers, Switches, and Counters'
documentation_page: 'edgedetector'
documentation_source_path: 'ref/edgedetector.html'
language: zh-CN
chinese_source: worker-translation
---

# Edge Detector

## 端口

### 输入

### **Input** — 输入信号 向量 | 矩阵

将输入信号指定为向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`

### 输出

### **Output** — 边沿检测器的输出 向量 | 矩阵

该模块将边沿检测器的输出以向量或矩阵形式返回。

该模块可能根据输入数据类型以及启用还是禁用 Boolean 支持来输出 Boolean 值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`

## 参数

### **输入处理** — 输入处理 `Columns as channels (frame based)` (default) | `Elements as channels (sample based)`

指定模块应如何处理输入。您可以将此参数设置为以下选项之一：

- `Columns as channels (frame based)` (default) — 当
  您选择此选项时，模块将输入的每一列视为单独的通道。
- `Elements as channels (sample based)` — 当
  您选择此选项时，模块将输入的每个元素视为单独的通道。

## 所属库

DSP System Toolbox / Signal Management / Switches and Counters

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

在某些条件下，生成的代码依赖 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

检测从零到非零值的跳变

当输入的对应通道从零跳变到非零值时，Edge Detector 模块在给定输出通道中生成一个冲激（值 1）。当输入未从零跳变到非零值时，该模块在对应的输出通道中生成零。

此模块仅支持离散时间固定步长信号。不支持连续信号。

输出与输入具有相同的维度和采样率。当您将 **输入处理** 参数设置为 `Columns as channels (frame based)` 时，对于跨两个连续帧拆分的边沿，模块在包含非零值的帧中计数该边沿。例如，如果第一个帧的底部为零，第二个帧的顶部为非零值，则模块在第二个帧中计数该边沿。
