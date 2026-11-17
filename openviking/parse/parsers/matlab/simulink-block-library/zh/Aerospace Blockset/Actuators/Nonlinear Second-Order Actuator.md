---
type: simulink-block
title: 'Nonlinear Second-Order Actuator'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Actuators'
documentation_page: 'nonlinearsecondorderactuator'
documentation_source_path: 'nonlinearsecondorderactuator.html'
language: zh-CN
chinese_source: worker-translation
---

# Nonlinear Second-Order Actuator

## 端口

### 输入

### **Ademand** — 需求作动器位置 标量 | 数组

需求作动器位置，指定为标量或数组。

**数据类型：** `double`
### 输出

### **Aactual** — 实际作动器位置 标量 | 数组

实际作动器位置，返回为标量或数组。

**数据类型：** `double`

## 参数

### **Natural frequency** — 固有频率 `1`（默认）| 标量

作动器的固有频率，指定为标量 double，单位为弧度每秒。

#### 程序化使用

|  |
| --- |
| **模块参数**：`wn_fin` |
| **类型**：字符向量 |
| **值**：标量 | double |
| **默认**：`'1'` |

### **Damping ratio** — 阻尼比 `0.3`（默认）| 标量

作动器的阻尼比，指定为标量 double。

#### 程序化使用

|  |
| --- |
| **模块参数**：`z_fin` |
| **类型**：字符向量 |
| **值**：标量 | double |
| **默认**：`'0.3'` |

### **Maximum deflection** — 允许的最大作动器位置 `20*pi/180`（默认）| 标量

允许的最大作动器位置，指定为标量 double，单位与需求作动器位置相同。

#### 程序化使用

|  |
| --- |
| **模块参数**：`fin_max` |
| **类型**：字符向量 |
| **值**：标量 | double |
| **默认**：`'20*pi/180'` |

### **Minimum deflection** — 允许的最小作动器位置 `-20*pi/180`（默认）| 标量

允许的最小作动器位置，指定为标量 double，单位与需求作动器位置相同。

#### 程序化使用

|  |
| --- |
| **模块参数**：`fin_min` |
| **类型**：字符向量 |
| **值**：标量 | double |
| **默认**：`'-20*pi/180'` |

### **Rate limit** — 允许的最快速度 `500*pi/180`（默认）| 标量

作动器运动允许的最快速度，指定为标量 double，单位为需求作动器位置每秒。

#### 程序化使用

|  |
| --- |
| **模块参数**：`fin_maxrate` |
| **类型**：字符向量 |
| **值**：标量 | double |
| **默认**：`'500*pi/180'` |

### **Initial position** — 初始位置 `0`（默认）| 标量

作动器的初始位置，指定为标量 double，单位与需求作动器位置相同。

- 如果指定值小于 **Minimum deflection** 的值，模块将 **Minimum deflection** 的值设置为初始位置值。
- 如果指定值大于 **Maximum deflection** 的值，模块将 **Maximum deflection** 的值设置为初始位置值。

#### 程序化使用

|  |
| --- |
| **模块参数**：`fin_act_0` |
| **类型**：字符向量 |
| **值**：标量 | double |
| **默认**：`'0'` |

### **Initial velocity** — 初始速度 `0`（默认）| 标量

作动器的初始速度，指定为标量 double，单位为需求作动器位置每秒。

如果指定值的绝对值大于 **Rate Limit** 的绝对值，此模块将 **Rate Limit** 的值设置为初始速度值。

#### 程序化使用

|  |
| --- |
| **模块参数**：`fin_act_vel` |
| **类型**：字符向量 |
| **值**：标量 | double |
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

实现具有速率和偏转限制的二阶作动器

Second Order Nonlinear Actuator 模块使用输入的需求作动器位置以及定义系统的其他对话框参数，输出实际作动器位置。
