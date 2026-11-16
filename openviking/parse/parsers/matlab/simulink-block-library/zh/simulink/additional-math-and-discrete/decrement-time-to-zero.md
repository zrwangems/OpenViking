---
type: simulink-block
title: 'Decrement Time To Zero'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Additional Math and Discrete'
documentation_page: 'decrementtimetozero'
documentation_source_path: 'slref/decrementtimetozero.html'
language: zh-CN
chinese_source: worker-translation
---

# Decrement Time To Zero

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

输出是输入信号的实际值减去采样时间 `Ts` 后的结果。输出永远不会低于零。输出具有与输入相同的数据类型和维度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

R2025b 中未记录。

## 所属库

Simulink / Additional Math & Discrete / Additional Math: Increment - Decrement

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

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

将信号的实际值按采样时间递减，但仅递减到零

Decrement Time To Zero 模块将信号的实际值按采样时间 `Ts` 递减。输出永远不会低于零。
