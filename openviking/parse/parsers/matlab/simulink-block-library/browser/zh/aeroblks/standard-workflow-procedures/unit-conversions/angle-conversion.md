---
type: simulink-block
title: 'Angle Conversion'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Unit Conversions'
documentation_page: 'angleconversion'
documentation_source_path: 'angleconversion.html'
language: zh-CN
chinese_source: worker-translation
---

# Angle Conversion

## 端口

### 输入

### **Port\_1** — Angle 标量 | 数组

Angle，指定为标量或数组，以初始加速度单位表示。

#### 依赖关系

输入端口标签取决于 **Initial unit** 设置。

**数据类型：** `double`
### 输出

### **Port\_1** — Angle 标量 | 数组

Angle，以标量形式返回，以最终加速度单位表示。

#### 依赖关系

输出端口标签取决于 **Final unit** 设置。

**数据类型：** `double`

## 参数

### **Initial unit** — 输入单位 `deg`（默认） | `rad` | `rev`

输入单位，指定为：

|  |  |
| --- | --- |
| `deg` | 度 |
| `rad` | 弧度 |
| `rev` | 转 |

#### 依赖关系

输入端口标签取决于 **Initial unit** 设置。

#### 编程用法

|  |
| --- |
| **模块参数**：`IU` |
| **类型**：character vector |
| **值**：`'deg'` | `'rad'` | `'rev'` |
| **默认值**：`'deg'` |

### **Final unit** — 输出单位 `rad`（默认） | `deg` | `rev`

输出单位，指定为：

|  |  |
| --- | --- |
| `deg` | 度 |
| `rad` | 弧度 |
| `rev` | 转 |

#### 依赖关系

输出端口标签取决于 **Final unit** 设置。

#### 编程用法

|  |
| --- |
| **模块参数**：`OU` |
| **类型**：character vector |
| **值**：`'deg'` | `'rad'` | `'rev'` |
| **默认值**：`'rad'` |

## 所属库

Aerospace Blockset / Utilities / Unit Conversions

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

将角度单位转换为所需角度单位

Angle Conversion 模块计算从指定的输入角度单位到指定的输出角度单位的转换因子，并将该转换因子应用于输入信号。

Angle Conversion 模块的端口标签会根据从 **Initial unit** 和 **Final unit** 列表中选择的输入和输出单位而变化。
