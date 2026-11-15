---
type: simulink-block
title: 'Angular Acceleration Conversion'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Unit Conversions'
documentation_page: 'angularaccelerationconversion'
documentation_source_path: 'angularaccelerationconversion.html'
language: zh-CN
chinese_source: worker-translation
---

# Angular Acceleration Conversion

## 端口

### 输入

### **Port\_1** — 角加速度输入 标量 | 数组

Angle，指定为标量，采用初始加速度单位。

#### 依赖项

输入端口标签取决于 **Initial unit** 设置。

**数据类型：** `double`
### 输出

### **Port\_1** — 角加速度输出 标量 | 数组

Angle，返回为标量，采用最终加速度单位。

#### 依赖项

输出端口标签取决于 **Final unit** 设置。

**数据类型：** `double`

## 参数

### **Initial unit** — 输入单位 `deg/s2`（默认） | `rad/s2` | `rpm/s`

指定输入单位，指定为：

|  |  |
| --- | --- |
| `deg/s`2 | 度每二次方秒 |
| `rad/s`2 | 弧度每二次方秒 |
| `rpm/s` | 每分钟转数每秒 |

#### 依赖项

输入端口标签取决于 **Initial unit** 设置。

#### 编程用法

|  |
| --- |
| **模块参数**：`IU` |
| **类型**：character vector |
| **值**：`'deg/s^2'` | `'rad/s^2'` | `'rpm/s'` |
| **默认值**：`'deg/s^2'` |

### **Final unit** — 输出单位 `rad/ss`（默认） | `deg/ss` | `rpm/s`

输出单位，指定为：

|  |  |
| --- | --- |
| `deg/s`2 | 度每二次方秒 |
| `rad/s`2 | 弧度每二次方秒 |
| `rpm/s` | 每分钟转数每秒 |

#### 依赖项

输出端口标签取决于 **Final unit** 设置。

#### 编程用法

|  |
| --- |
| **模块参数**：`OU` |
| **类型**：character vector |
| **值**：`'deg/s^2'` | `'rad/s^2'` | `'rpm/s'` |
| **默认值**：`'rad/s^2'` |

## 所属库

Aerospace Blockset / Utilities / Unit Conversions

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

将角加速度单位转换为所需的角加速度单位

Angular Acceleration Conversion 模块计算从指定输入角加速度单位到指定输出角加速度单位的转换因子，并将该转换因子应用于输入信号。

Angular Acceleration Conversion 模块的端口标签会根据从 **Initial unit** 和 **Final unit** 列表中选择的输入和输出单位而变化。
