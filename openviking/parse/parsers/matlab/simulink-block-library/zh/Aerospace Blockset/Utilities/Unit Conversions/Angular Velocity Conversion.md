---
type: simulink-block
title: 'Angular Velocity Conversion'
family: 'utilities'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Unit Conversions'
documentation_page: 'angularvelocityconversion'
documentation_source_path: 'angularvelocityconversion.html'
language: zh-CN
chinese_source: worker-translation
---

# Angular Velocity Conversion

## 端口

### 输入

### **Port\_1** — 角加速度 标量 | 数组

角加速度，以初始角加速度单位指定为标量。

#### 依赖关系

输入端口标签取决于 **初始单位** 设置。

**数据类型：** `double`

### 输出

### **Port\_1** — 角加速度 标量 | 数组

角加速度，以最终角加速度单位返回为标量。

#### 依赖关系

输出端口标签取决于 **最终单位** 设置。

**数据类型：** `double`

## 参数

### **初始单位** — 输入单位 `deg/s`（默认） | `rad/s` | `rpm`

输入单位，指定为：

|  |  |
| --- | --- |
| `deg`/s | 度每秒 |
| `rad`/s | 弧度每秒 |
| `rpm` | 转每分钟 |

#### 依赖关系

输入端口标签取决于 **初始单位** 设置。

#### 编程用法

|  |
| --- |
| **模块参数**: `IU` |
| **类型**: character vector |
| **值**: `'deg/s'` | `'rad/s'` | `'rpm/s'` |
| **默认值**: `'deg/s'` |

### **最终单位** — 输出单位 `rad/s`（默认） | `deg/s` | `rpm`

输出单位，指定为：

|  |  |
| --- | --- |
| `deg`/s | 度每秒 |
| `rad`/s | 弧度每秒 |
| `rpm` | 转每分钟 |

#### 依赖关系

输出端口标签取决于 **最终单位** 设置。

#### 编程用法

|  |
| --- |
| **模块参数**: `OU` |
| **类型**: character vector |
| **值**: `'deg/s'` | `'rad/s'` | `'rpm/s'` |
| **默认值**: `'deg/s'` |

## 所属库

Aerospace Blockset / Utilities / Unit Conversions

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

从角速度单位转换为所需角速度单位

Angular Velocity Conversion 模块计算从指定输入角速度单位到指定输出角速度单位的转换因子，并将该转换因子应用于输入信号。

Angular Velocity Conversion 模块的端口标签会根据从 **初始单位** 和 **最终单位** 列表中选择的输入和输出单位而变化。
