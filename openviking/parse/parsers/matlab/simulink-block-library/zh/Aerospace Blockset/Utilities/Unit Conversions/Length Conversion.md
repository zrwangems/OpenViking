---
type: simulink-block
title: 'Length Conversion'
family: 'utilities'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Unit Conversions'
documentation_page: 'lengthconversion'
documentation_source_path: 'lengthconversion.html'
language: zh-CN
chinese_source: worker-translation
---

# Length Conversion

## 端口

### 输入

### **Port\_1** — 长度标量 | 数组

长度，指定为初始长度单位下的标量或数组。

#### 依赖关系

输入端口标签取决于 **初始单位** 设置。

**数据类型：** `double`
### 输出

### **Port\_1** — 长度标量 | 数组

长度，以最终长度单位返回为标量或数组。

#### 依赖关系

输出端口标签取决于 **最终单位** 设置。

**数据类型：** `double`

## 参数

### **初始单位** — 输入单位 `ft`（默认） | `m` | `km` | `in` | `mi` | `naut mi`

输入单位，指定为：

|  |  |
| --- | --- |
| `m` | 米 |
| `ft` | 英尺 |
| `km` | 千米 |
| `in` | 英寸 |
| `mi` | 英里 |
| `naut mi` | 海里 |

#### 依赖关系

输入端口标签取决于 **初始单位** 设置。

#### 编程用法

|  |
| --- |
| **模块参数**: `IU` |
| **类型**: character vector |
| **值**: `'m'` | `'ft'` | `'km'` | `'in'` | `'mi'` | `'naut mi'` |
| **默认值**: `'ft'` |

### **最终单位** — 输入单位 `m`（默认） | `ft` | `km` | `in` | `mi` | `naut mi`

输出单位，指定为：

|  |  |
| --- | --- |
| `m` | 米 |
| `ft` | 英尺 |
| `km` | 千米 |
| `in` | 英寸 |
| `mi` | 英里 |
| `naut mi` | 海里 |

#### 依赖关系

输出端口标签取决于 **最终单位** 设置。

#### 编程用法

|  |
| --- |
| **模块参数**: `OU` |
| **类型**: character vector |
| **值**: `'m'` | `'ft'` | `'km'` | `'in'` | `'mi'` | `'naut mi'` |
| **默认值**: `'m'` |

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

从长度单位转换为所需长度单位

Length Conversion 模块计算从指定输入长度单位到指定输出长度单位的转换因子，并将转换因子应用于输入信号。

Length Conversion 模块端口标签会根据从 **初始单位** 和 **最终单位** 列表中选择的输入和输出单位而变化。
