---
type: simulink-block
title: 'Temperature Conversion'
family: 'utilities'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Unit Conversions'
documentation_page: 'temperatureconversion'
documentation_source_path: 'temperatureconversion.html'
language: zh-CN
chinese_source: worker-translation
---

# Temperature Conversion

## 端口

### 输入

### **Port\_1** — 温度标量 | 数组

温度，指定为初始温度单位下的标量或数组。

#### 依赖项

输入端口标签取决于 **初始单位** 设置。

**数据类型：** `double`

### 输出

### **Port\_1** — 温度标量 | 数组

温度，返回为最终温度单位下的标量或数组。

#### 依赖项

输出端口标签取决于 **最终单位** 设置。

**数据类型：** `double`

## 参数

### **初始单位** — 输入单位 `R`（默认）| `F` | `C` | `K`

输入单位，指定为：

|  |  |
| --- | --- |
| `K` | Kelvin |
| `F` | Degrees Fahrenheit |
| `C` | Degrees Celsius |
| `R` | Degrees Rankine |

#### 依赖项

输入端口标签取决于 **初始单位** 设置。

#### 程序化使用

|  |
| --- |
| **模块参数**: `IU` |
| **类型**: character vector |
| **值**: `'K'` | `'F'` | `'C'` | `'R'` |
| **默认值**: `'R'` |

### **最终单位** — 输出单位 `K`（默认）| `F` | `C` | `R`

输出单位，指定为：

|  |  |
| --- | --- |
| `K` | Kelvin |
| `F` | Degrees Fahrenheit |
| `C` | Degrees Celsius |
| `R` | Degrees Rankine |

#### 依赖项

输出端口标签取决于 **最终单位** 设置。

#### 程序化使用

|  |
| --- |
| **模块参数**: `OU` |
| **类型**: character vector |
| **值**: `'K'` | `'F'` | `'C'` | `'R'` |
| **默认值**: `'K'` |

## 所属库

Aerospace Blockset / Utilities / Unit Conversions

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

从温度单位转换为所需温度单位

Temperature Conversion 模块计算从指定输入温度单位到指定输出温度单位的转换因子，并将该转换因子应用于输入信号。

Temperature Conversion 模块的端口标签会根据从 **初始单位** 和 **最终单位** 列表中选择的输入和输出单位而变化。
