---
type: simulink-block
title: 'Force Conversion'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Unit Conversions'
documentation_page: 'forceconversion'
documentation_source_path: 'forceconversion.html'
language: zh-CN
chinese_source: worker-translation
---

# Force Conversion

## 端口

### 输入

### **Port\_1** — 力 标量 | 数组

力，指定为标量或数组，以初始力单位表示。

#### 依赖关系

输入端口标签取决于 **Initial unit** 设置。

**数据类型：** `double`
### 输出

### **Port\_1** — 力 标量 | 数组

力，以标量或数组形式返回，以最终力单位表示。

#### 依赖关系

输出端口标签取决于 **Final unit** 设置。

**数据类型：** `double`

## 参数

### **Initial unit** — 输入单位 `lbf`（默认）| `N`

输入单位，指定为：

|  |  |
| --- | --- |
| `lbf` | 磅力 |
| `N` | 牛顿 |

#### 依赖关系

输入端口标签取决于 **Initial unit** 设置。

#### 编程用法

|  |
| --- |
| **模块参数**：`IU` |
| **类型**：字符向量 |
| **值**：`lbf` | `N` |
| **默认值**：`lbf` |

### **Final unit** — 输出单位 `N`（默认）| `lbf`

输出单位，指定为：

|  |  |
| --- | --- |
| `lbf` | 磅力 |
| `N` | 牛顿 |

#### 依赖关系

输出端口标签取决于 **Final unit** 设置。

#### 编程用法

|  |
| --- |
| **模块参数**：`OU` |
| **类型**：字符向量 |
| **值**：`lbf` | `N` |
| **默认值**：`N` |

## 所属库

Aerospace Blockset / Utilities / Unit Conversions

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

从力单位转换为所需的力单位

Force Conversion 模块计算从指定的输入力单位到指定的输出力单位的转换因子，并将该转换因子应用于输入信号。

Force Conversion 模块的端口标签会根据从 **Initial unit** 和 **Final unit** 列表中选择的输入和输出单位而变化。
