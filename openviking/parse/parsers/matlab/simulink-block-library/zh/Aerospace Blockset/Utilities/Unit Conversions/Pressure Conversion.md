---
type: simulink-block
title: 'Pressure Conversion'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Unit Conversions'
documentation_page: 'pressureconversion'
documentation_source_path: 'pressureconversion.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure Conversion

## 端口

### 输入

### **Port\_1** — 压力标量 | 数组

压力，指定为标量或数组，采用初始压力单位。

#### 依赖关系

输入端口标签取决于 **Initial unit** 设置。

**数据类型：** `double`
### 输出

### **Port\_1** — 压力标量 | 数组

压力，以标量或数组形式返回，采用最终压力单位。

#### 依赖关系

输出端口标签取决于 **Final unit** 设置。

**数据类型：** `double`

## 参数

### **Initial unit** — 输入单位 `psi`（默认）| `Pa` | `psf` | `atm`

输入单位，指定为：

|  |  |
| --- | --- |
| `psi` | 磅质量每平方英寸 |
| `Pa` | 帕斯卡 |
| `psf` | 磅质量每平方英尺 |
| `atm` | 标准大气压 |

#### 依赖关系

输入端口标签取决于 **Initial unit** 设置。

#### 程序化使用

|  |
| --- |
| **模块参数**：`IU` |
| **类型**：字符向量 |
| **值**：`'psi'` | `'Pa'` | `'psf'` | `'atm'` |
| **默认值**：`'psi'` |

### **Final unit** — 输出单位 `Pa`（默认）| `psi` | `psf` | `atm`

输出单位，指定为：

|  |  |
| --- | --- |
| `psi` | 磅质量每平方英寸 |
| `Pa` | 帕斯卡 |
| `psf` | 磅质量每平方英尺 |
| `atm` | 标准大气压 |

#### 依赖关系

输出端口标签取决于 **Final unit** 设置。

#### 程序化使用

|  |
| --- |
| **模块参数**：`OU` |
| **类型**：字符向量 |
| **值**：`'psi'` | `'Pa'` | `'psf'` | `'atm'` |
| **默认值**：`'Pa'` |

## 所属库

Aerospace Blockset / Utilities / Unit Conversions

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

将压力单位转换为所需的压力单位

Pressure Conversion 模块计算从指定的输入压力单位到指定的输出压力单位的转换因子，并将该转换因子应用于输入信号。

Pressure Conversion 模块的端口标签根据从 **Initial unit** 和 **Final unit** 列表中选择的输入和输出单位而变化。
