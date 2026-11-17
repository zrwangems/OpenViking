---
type: simulink-block
title: 'Linear Second-Order Actuator'
family: 'actuators'
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

### **Ademand** — 所需作动器位置 标量 | 数组

所需作动器位置，指定为标量或数组。

**数据类型：** `double`
### 输出

### **Aactual** — 实际作动器位置 标量 | 数组

实际作动器位置，以标量或数组形式返回。

**数据类型：** `double`

## 参数

### **自然频率** — 自然频率 `1`（默认）| 标量

作动器的自然频率，指定为标量 double，以 radians per second 为单位。

#### 编程用法

|  |
| --- |
| **模块参数**：`wn_fin` |
| **类型**：character vector |
| **值**：标量 | double |
| **默认值**：`'1'` |

### **阻尼比** — 阻尼比 `0.3`（默认）| 标量

作动器的阻尼比，指定为标量 double。

#### 编程用法

|  |
| --- |
| **模块参数**：`z_fin` |
| **类型**：character vector |
| **值**：标量 | double |
| **默认值**：`'0.3'` |

### **初始位置** — 初始位置 `0`（默认）| 标量

作动器的初始位置，指定为标量 double。初始位置的单位必须与 **Ademand** 输入相同。

#### 编程用法

|  |
| --- |
| **模块参数**：`fin_act_0` |
| **类型**：character vector |
| **值**：标量 | double |
| **默认值**：`'0'` |

### **初始速度** — 初始速度 `0`（默认）| 标量

作动器的初始速度，指定为标量 double。初始速度的单位必须与 **Ademand** 输入相同。

#### 编程用法

|  |
| --- |
| **模块参数**：`fin_act_vel` |
| **类型**：character vector |
| **值**：标量 | double |
| **默认值**：`'0'` |

## 所属库

Aerospace Blockset / Actuators

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

## 描述

实现二阶线性作动器

Second Order Linear Actuator 模块使用输入的所需作动器位置和定义系统的其他参数，输出实际作动器位置。
