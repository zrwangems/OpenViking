---
type: simulink-block
title: 'Edge Detector'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Management / Switches and Counters'
documentation_page: 'edgedetector'
documentation_source_path: 'ref/edgedetector.html'
language: zh-CN
chinese_source: worker-translation
---

# Edge Detector

## 端口
```yaml
ports:
- name: Input
  summary: 输入信号 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point | enumerated
- name: Output
  summary: 边沿检测器的输出 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point | enumerated
```

### 输入

### **Input** — 输入信号 向量 | 矩阵

将输入信号指定为向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`
### 输出

### **Output** — 边沿检测器的输出 向量 | 矩阵

该模块以向量或矩阵形式返回边沿检测器的输出。

根据输入数据类型以及布尔支持是启用还是禁用，该模块可能输出布尔值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`
## 参数
```yaml
parameters:
- name: Input processing
  summary: 输入处理 Columns as channels (frame based)（默认）| Elements as channels (sample based)
  group: ''
```

### **Input processing** — 输入处理 `Columns as channels (frame based)`（默认）| `Elements as channels (sample based)`

指定该模块应如何处理输入。您可以将此参数设置为以下选项之一：

- `Columns as channels (frame based)`（默认）— 选择此选项时，该模块将输入的每一列视为单独的信道。
- `Elements as channels (sample based)` — 选择此选项时，该模块将输入的每个元素视为单独的信道。
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

当输入的相应信道从零跳变到非零值时，Edge Detector 模块在给定输出信道中生成一个脉冲（值 1）。当输入未从零跳变到非零值时，该模块在相应输出信道中生成零。

该模块仅支持离散时间定步长信号。不支持连续信号。

输出的维度和采样率与输入相同。当您将 **Input processing** 参数设置为 `Columns as channels (frame based)` 时，该模块会在包含非零值的帧中计入跨两个连续帧分割的边沿。例如，如果第一帧的底部为零，第二帧的顶部为非零值，则该模块在第二帧中计入该边沿。
