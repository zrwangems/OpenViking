---
type: simulink-block
title: 'Squeeze'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'squeeze'
documentation_source_path: 'slref/squeeze.html'
language: zh-CN
chinese_source: worker-translation
---

# Squeeze

## 端口

### 输入

### **Port\_1** — 多维输入信号 多维信号

在输出中移除任意单一维度的输入信号。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 无单一维度的输出信号 多维信号

无单一维度的输出信号。例如，大小为 3×1×2 的多维数组变为 3×2 的信号。如果输入中没有单一维度，则输入信号原样传递到输出。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

R2025b 中未记录。

## 所属库

Simulink / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2007b 中引入**

## 描述

从多维信号中移除单一维度

Squeeze 模块从其多维输入信号中移除单一维度。单一维度是大小为 1 的任意维度。Squeeze 模块仅对维度数大于二的信号进行操作。标量、向量和矩阵信号原样通过 Squeeze 模块。
