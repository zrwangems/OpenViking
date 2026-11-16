---
type: simulink-block
title: 'Density Conversion'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Unit Conversions'
documentation_page: 'densityconversion'
documentation_source_path: 'densityconversion.html'
language: zh-CN
chinese_source: worker-translation
---

# Density Conversion

## 端口

### 输入

### **Port\_1** — 密度标量 | 数组

包含密度，以初始密度单位指定为标量或数组。

#### 依赖关系

输入端口标签取决于 **初始单位** 设置。

**数据类型：** `double`
### 输出

### **Port\_1** — 密度标量 | 数组

包含密度，以初始密度单位返回为标量或数组。

#### 依赖关系

输出端口标签取决于 **最终单位** 设置。

**数据类型：** `double`

## 参数

### **初始单位** — 输入单位 `lbm/ft^3`（默认） | `kg/m^3` | `slug/ft^3` | `lbm/in^3`

输入单位，指定为：

|  |  |
| --- | --- |
| `lbm/ft^3` | 磅质量每立方英尺 |
| `kg/m^3` | 千克每立方米 |
| `slug/ft^3` | 斯勒格每立方英尺 |
| `lbm/in^3` | 磅质量每立方英寸 |

#### 依赖关系

输入端口标签取决于 **初始单位** 设置。

#### 编程用法

|  |
| --- |
| **模块参数**：`IU` |
| **类型**：character vector |
| **值**：`'lbm/ft^3'` | `'kg/m^3'` | `'slug/ft^3'` | `'lbm/in^3'` |
| **默认值**：`'lbm/ft^3'` |

### **最终单位** — 输出单位 `kg/m^3`（默认） | `lbm/ft^3` | `slug/ft^3` | `lbm/in^3`

输出单位，指定为：

|  |  |
| --- | --- |
| `lbm/ft^3` | 磅质量每立方英尺 |
| `kg/m^3` | 千克每立方米 |
| `slug/ft^3` | 斯勒格每立方英尺 |
| `lbm/in^3` | 磅质量每立方英寸 |

#### 依赖关系

输出端口标签取决于 **最终单位** 设置。

#### 编程用法

|  |
| --- |
| **模块参数**：`OU` |
| **类型**：character vector |
| **值**：`'lbm/ft^3'` | `'kg/m^3'` | `'slug/ft^3'` | `'lbm/in^3'` |
| **默认值**：`'kg/m^3'` |

## 所属库

Aerospace Blockset / Utilities / Unit Conversions

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2006a 之前引入**

## 描述

从密度单位转换为所需密度单位

Density Conversion 模块计算从指定输入密度单位到指定输出密度单位的转换因子，并将该转换因子应用于输入信号。

Density Conversion 模块端口标签根据从 **初始单位** 和 **最终单位** 列表中选择的输入和输出单位而变化。
