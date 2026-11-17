---
type: simulink-block
title: 'Velocity Conversion'
family: 'utilities'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Unit Conversions'
documentation_page: 'velocityconversion'
documentation_source_path: 'velocityconversion.html'
language: zh-CN
chinese_source: worker-translation
---

# Velocity Conversion

## 端口

### 输入

### **Port\_1** — 速度标量 | 数组

速度，指定为标量或数组，以初始速度单位表示。

#### 依赖项

输入端口标签取决于 **初始单位** 设置。

**数据类型：** `double`
### 输出

### **Port\_1** — 速度标量 | 数组

速度，以标量或数组形式返回，以最终速度单位表示。

#### 依赖项

输出端口标签取决于 **最终单位** 设置。

**数据类型：** `double`

## 参数

### **初始单位** — 输入单位 `ft/s`（默认） | `m/s` | `km/s` | `in/s` | `km/h` | `mph` | `kts` | `ft/min`

输入单位，指定为：

|  |  |
| --- | --- |
| `m/s` | Meters per second |
| `ft/s` | Feet per second |
| `km/s` | Kilometers per second |
| `in/s` | Inches per second |
| `km/h` | Kilometers per hour |
| `mph` | Miles per hour |
| `kts` | Nautical miles per hour |
| `ft/min` | Feet per minute |

#### 依赖项

输入端口标签取决于 **初始单位** 设置。

#### 编程使用

|  |
| --- |
| **模块参数**：`IU` |
| **类型**：character vector |
| **值**：`'m/s'` | `'ft/s'` | `'km/s'` | `'in/s'` | `'km/h'` | `'mph'` | `'kts'` | `'ft/min'` |
| **默认值**：`'ft/s'` |

### **最终单位** — 输出单位 `m/s`（默认） | `ft/s` | `km/s` | `in/s` | `km/h` | `mph` | `kts` | `ft/min`

输出单位，指定为：

|  |  |
| --- | --- |
| `m/s` | Meters per second |
| `ft/s` | Feet per second |
| `km/s` | Kilometers per second |
| `in/s` | Inches per second |
| `km/h` | Kilometers per hour |
| `mph` | Miles per hour |
| `kts` | Nautical miles per hour |
| `ft/min` | Feet per minute |

#### 依赖项

输出端口标签取决于 **最终单位** 设置。

#### 编程使用

|  |
| --- |
| **模块参数**：`OU` |
| **类型**：character vector |
| **值**：`'m/s'` | `'ft/s'` | `'km/s'` | `'in/s'` | `'km/h'` | `'mph'` | `'kts'` | `'ft/min'` |
| **默认值**：`'m/s'` |

## 所属库

Aerospace Blockset / Utilities / Unit Conversions

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

将速度单位转换为所需速度单位

Velocity Conversion 模块计算从指定输入速度单位到指定输出速度单位的转换因子，并将该转换因子应用于输入信号。

Velocity Conversion 模块的端口标签会根据从 **初始单位** 和 **最终单位** 列表中选择的输入和输出单位而变化。
