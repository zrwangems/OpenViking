---
type: simulink-block
title: 'Dropout Layer'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning with Simulink / Utility Layers'
documentation_page: 'dropoutlayer'
documentation_source_path: 'ref/dropoutlayer.html'
language: zh-CN
chinese_source: worker-translation
---

# Dropout Layer

## 端口

### 输入

### **In** — 输入矩阵 标量 | 向量 | 矩阵

输入数据。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 输出

### **Out** — 输出矩阵 标量 | 向量 | 矩阵

与输入数据相等的输出数据。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### 执行

### **采样时间** — 用于指定采样时间的选项 `-1`（默认）| 标量

指定采样时间命中之间的离散间隔，或指定另一种采样时间类型，例如连续 (`0`) 或继承 (`-1`)。有关更多选项，请参阅 Types of Sample Time (Simulink)。

默认情况下，该模块根据其在模型中的上下文继承其采样时间。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |
| --- |
| **参数:** `SampleTime` |
| **数据类型:** `char` |
| **值:** `'-1'`（默认）| 标量 |

## 所属库

Deep Learning Toolbox / Deep Learning Layers / Utility Layers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

Dropout 层

Dropout Layer 模块表示深度学习网络中的 dropout 层。在训练时，dropout 层按给定概率随机将输入元素设置为零。在预测时，dropout 层的输出等于其输入。

`exportNetworkToSimulink` 函数生成此模块以表示 `dropoutLayer` 对象。由于深度学习层模块只能用于预测，因此此模块没有效果。
