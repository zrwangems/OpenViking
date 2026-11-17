---
type: simulink-block
title: 'Linear Second-Order Actuator'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Actuators'
documentation_page: 'linearsecondorderactuator'
documentation_source_path: 'linearsecondorderactuator.html'
language: zh-CN
chinese_source: worker-translation
---

# Linear Second-Order Actuator

## 端口

### 输入

### **Ademand** — 需求执行器位置 标量 | 数组

需求执行器位置，指定为标量或数组。

**数据类型：** `double`
### 输出

### **Aactual** — 实际执行器位置 标量 | 数组

实际执行器位置，以标量或数组形式返回。

**数据类型：** `double`

## 参数

### **Natural frequency** — 固有频率 `1`（默认）| 标量

执行器的固有频率，指定为标量双精度值，单位为弧度每秒。

#### 程序化使用

|  |
| --- |
| **模块参数**：`wn_fin` |
| **类型**：字符向量 |
| **值**：标量 | 双精度 |
| **默认**：`'1'` |

### **Damping ratio** — 阻尼比 `0.3`（默认）| 标量

执行器的阻尼比，指定为标量双精度值。

#### 程序化使用

|  |
| --- |
| **模块参数**：`z_fin` |
| **类型**：字符向量 |
| **值**：标量 | 双精度 |
| **默认**：`'0.3'` |

### **Initial position** — 初始位置 `0`（默认）| 标量

执行器的初始位置，指定为标量双精度值。初始位置的单位必须与
**Ademand** 输入相同。

#### 程序化使用

|  |
| --- |
| **模块参数**：`fin_act_0` |
| **类型**：字符向量 |
| **值**：标量 | 双精度 |
| **默认**：`'0'` |

### **Initial velocity** — 初始速度 `0`（默认）| 标量

执行器的初始速度，指定为标量双精度值。初始速度的单位必须与
**Ademand** 输入相同。

#### 程序化使用

|  |
| --- |
| **模块参数**：`fin_act_vel` |
| **类型**：字符向量 |
| **值**：标量 | 双精度 |
| **默认**：`'0'` |

## 所属库

Aerospace Blockset / Actuators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

## 描述

实现二阶线性执行器

Second Order Linear Actuator 模块使用输入的需求执行器位置和定义系统的其他参数，输出实际执行器位置。
