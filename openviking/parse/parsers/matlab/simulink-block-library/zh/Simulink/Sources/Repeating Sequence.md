---
type: simulink-block
title: 'Repeating Sequence'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'repeatingsequence'
documentation_source_path: 'slref/repeatingsequence.html'
language: zh-CN
chinese_source: official
---

# Repeating Sequence

## 端口

### 输出

### **Port\_1** — 周期性输出信号 标量

输出由**时间值**和**输出值**参数指定的信号以创建周期性标量信号。

**数据类型:** `double`

## 参数

### **时间值** — 输出时间的向量 `[0 2]` (默认) | 向量

严格单调递增时间值的向量。生成的波形的周期是此参数的最后一个值和第一个值之差。

#### 编程用法

|  |
| --- |
| **模块参数**：`rep_seq_t` |
| **类型**：字符向量 |
| **值**：向量 |
| **默认值**：`[0 2]` |

### **输出值** — 输出值的向量 `[0 2]` (默认) | 向量

输出值的向量，用于指定输出波形。每个元素对应于**时间值**参数中的时间值。

#### 编程用法

|  |
| --- |
| **模块参数**：`rep_seq_y` |
| **类型**：字符向量 |
| **值**：向量 |
| **默认值**：`[0 2]` |

## 所属库

Simulink / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不建议用于生产代码。

考虑使用 Repeating Sequence Stair 或 Repeating Sequence Interpolated 模块进行代码生成。

## 版本历史

**在 R2006a 之前推出**

## 描述

生成任意形状的周期信号

Repeating Sequence 模块可以输出波形由**时间值**和**输出值**参数指定的周期性标量信号。**时间值**参数指定输出时间向量。**输出值**参数指定输出时间对应的信号振幅向量。这两个参数结合使用指定输出波形的重复间隔（信号周期）的各测量点确定的采样。

默认情况下，这两个参数都是 `[0 2]`。这些默认设置指定了从仿真开始每 `2` 秒重复一次，最大振幅为 `2` 的锯齿波形。
