---
type: simulink-block
title: 'Mass Conversion'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Unit Conversions'
documentation_page: 'massconversion'
documentation_source_path: 'massconversion.html'
language: zh-CN
chinese_source: worker-translation
---

# Mass Conversion

## 端口

### 输入

### **Port\_1** — 质量标量 | 数组

质量，指定为标量或数组，以初始质量单位表示。

#### 依赖关系

输入端口标签取决于 **Initial unit** 设置。

**数据类型：** `double`
### 输出

### **Port\_1** — 质量标量 | 数组

质量，返回为标量或数组，以最终质量单位表示。

#### 依赖关系

输出端口标签取决于 **Final unit** 设置。

**数据类型：** `double`

## 参数

### **Initial unit** — 输入单位 `lbm`（默认）| `kg` | `slug`

输入单位，指定为：

|  |  |
| --- | --- |
| `lbm` | 磅质量 |
| `kg` | 千克 |
| `slug` | 斯勒格 |

#### 依赖关系

输入端口标签取决于 **Initial unit** 设置。

#### 程序化使用

|  |
| --- |
| **模块参数**：`IU` |
| **类型**：字符向量 |
| **值**：`'lbm'` | `'kg'` | `'slug'` |
| **默认**：`'lbm'` |

### **Final unit** — 输出单位 `kg`（默认）| `lbm` | `slug`

输出单位，指定为：

|  |  |
| --- | --- |
| `lbm` | 磅质量 |
| `kg` | 千克 |
| `slug` | 斯勒格 |

#### 依赖关系

输出端口标签取决于 **Final unit** 设置。

#### 程序化使用

|  |
| --- |
| **模块参数**：`OU` |
| **类型**：字符向量 |
| **值**：`'lbm'` | `'kg'` | `'slug'` |
| **默认**：`'kg'` |

## 所属库

Aerospace Blockset / Utilities / Unit Conversions

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

从质量单位转换为所需的质量单位

Mass Conversion 模块计算从指定的输入质量单位到指定的输出质量单位的转换因子，并将该转换因子应用于输入信号。

Mass Conversion 端口模块标签根据从 **Initial unit** 和 **Final unit** 列表中选择的输入和输出单位而变化。
