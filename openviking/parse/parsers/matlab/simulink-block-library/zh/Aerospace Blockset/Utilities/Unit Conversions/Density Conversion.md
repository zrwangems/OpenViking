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
```yaml
ports:
- name: Port_1
  summary: 密度 标量 | 数组
  direction: input
  data_types: double
- name: Port_1
  summary: 密度 标量 | 数组
  direction: output
  data_types: double
```

### 输入

### **Port\_1** — 密度 标量 | 数组

包含密度，指定为标量或数组，以初始密度单位表示。

#### 依赖关系

输入端口标签取决于 **Initial unit** 设置。

**数据类型：** `double`
### 输出

### **Port\_1** — 密度 标量 | 数组

包含密度，返回为标量或数组，以初始密度单位表示。

#### 依赖关系

输出端口标签取决于 **Final unit** 设置。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Initial unit
  summary: 输入单位 lbm/ft^3（默认）| kg/m^3 | slug/ft^3 | lbm/in^3
  group: ''
  block_parameter: IU
  type: 字符向量
  values: '''lbm/ft^3'' | ''kg/m^3'' | ''slug/ft^3'' | ''lbm/in^3'''
  default: '''lbm/ft^3'''
- name: Final unit
  summary: 输出单位 kg/m^3（默认）| lbm/ft^3 | slug/ft^3 | lbm/in^3
  group: ''
  block_parameter: OU
  type: 字符向量
  values: '''lbm/ft^3'' | ''kg/m^3'' | ''slug/ft^3'' | ''lbm/in^3'''
  default: '''kg/m^3'''
```

### **Initial unit** — 输入单位 `lbm/ft^3`（默认）| `kg/m^3` | `slug/ft^3` | `lbm/in^3`

输入单位，指定为：

|  |  |
| --- | --- |
| `lbm/ft^3` | 磅质量每立方英尺 |
| `kg/m^3` | 千克每立方米 |
| `slug/ft^3` | 斯勒格每立方英尺 |
| `lbm/in^3` | 磅质量每立方英寸 |

#### 依赖关系

输入端口标签取决于 **Initial unit** 设置。

#### 程序化使用

|  |
| --- |
| **模块参数**：`IU` |
| **类型**：字符向量 |
| **值**：`'lbm/ft^3'` | `'kg/m^3'` | `'slug/ft^3'` | `'lbm/in^3'` |
| **默认值**：`'lbm/ft^3'` |

### **Final unit** — 输出单位 `kg/m^3`（默认）| `lbm/ft^3` | `slug/ft^3` | `lbm/in^3`

输出单位，指定为：

|  |  |
| --- | --- |
| `lbm/ft^3` | 磅质量每立方英尺 |
| `kg/m^3` | 千克每立方米 |
| `slug/ft^3` | 斯勒格每立方英尺 |
| `lbm/in^3` | 磅质量每立方英寸 |

#### 依赖关系

输出端口标签取决于 **Final unit** 设置。

#### 程序化使用

|  |
| --- |
| **模块参数**：`OU` |
| **类型**：字符向量 |
| **值**：`'lbm/ft^3'` | `'kg/m^3'` | `'slug/ft^3'` | `'lbm/in^3'` |
| **默认值**：`'kg/m^3'` |
## 所属库

Aerospace Blockset / Utilities / Unit Conversions

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

从密度单位转换为所需的密度单位

Density Conversion 模块计算从指定的输入密度单位到指定的输出密度单位的转换因子，并将该转换因子应用于输入信号。

Density Conversion 模块的端口标签根据从 **Initial unit** 和 **Final unit** 列表中选择的输入和输出单位而变化。
