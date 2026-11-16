---
type: simulink-block
title: 'Squeeze'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Math Operations'
documentation_page: 'squeeze'
documentation_source_path: 'slref/squeeze.html'
language: zh-CN
chinese_source: official
---

# Squeeze

## 端口

### 输入

### **Port\_1** — 多维输入信号 多维信号

输入信号，其中的任何单一维度将在输出中删除。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 没有单一维度的输出信号 多维信号

没有单一维度的输出信号。例如，大小为 3×1×2 的多维数组会变为 3×2 信号。如果输入中没有单一维度，则输入信号会一直传递到输出而保持不变。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

R2025b 官方文档未提供。

## 所属库

Simulink / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2007b 中推出**

## 描述

从多维信号中删除单一维度

Squeeze 模块删除其多维输入信号中的单一维度。单一维度是其大小为 1 的任何维度。Squeeze 模块仅对维数大于 2 的信号进行操作。标量、向量和矩阵信号在通过 Squeeze 模块时保持不变。
