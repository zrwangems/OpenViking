---
type: simulink-block
title: 'Length Conversion'
family: 'aeroblks'
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
```yaml
ports:
- name: Port_1
  summary: 长度标量 | 数组
  direction: input
  data_types: double
- name: Port_1
  summary: 长度标量 | 数组
  direction: output
  data_types: double
```

### 输入

### **Port\_1** — 长度标量 | 数组

长度，指定为标量或数组，采用初始长度单位。

#### 依赖关系

输入端口标签取决于 **Initial unit** 设置。

**数据类型：** `double`
### 输出

### **Port\_1** — 长度标量 | 数组

长度，以标量或数组形式返回，采用最终长度单位。

#### 依赖关系

输出端口标签取决于 **Final unit** 设置。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Initial unit
  summary: 输入单位 ft（默认）| m | km | in | mi | naut mi
  group: ''
  block_parameter: IU
  type: 字符向量
  values: '''m'' | ''ft'' | ''km'' | ''in'' | ''mi'' | ''naut mi'''
  default: '''ft'''
- name: Final unit
  summary: 输入单位 m（默认）| ft | km | in | mi | naut mi
  group: ''
  block_parameter: OU
  type: 字符向量
  values: '''m'' | ''ft'' | ''km'' | ''in'' | ''mi'' | ''naut mi'''
  default: '''m'''
```

### **Initial unit** — 输入单位 `ft`（默认）| `m` | `km` | `in` | `mi` | `naut mi`

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

输入端口标签取决于 **Initial unit** 设置。

#### 编程使用

|  |
| --- |
| **模块参数**：`IU` |
| **类型**：字符向量 |
| **值**：`'m'` | `'ft'` | `'km'` | `'in'` | `'mi'` | `'naut mi'` |
| **默认值**：`'ft'` |

### **Final unit** — 输入单位 `m`（默认）| `ft` | `km` | `in` | `mi` | `naut mi`

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

输出端口标签取决于 **Final unit** 设置。

#### 编程使用

|  |
| --- |
| **模块参数**：`OU` |
| **类型**：字符向量 |
| **值**：`'m'` | `'ft'` | `'km'` | `'in'` | `'mi'` | `'naut mi'` |
| **默认值**：`'m'` |
## 所属库

Aerospace Blockset / Utilities / Unit Conversions

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

从长度单位转换为所需的长度单位

Length Conversion 模块计算从指定的输入长度单位到指定的输出长度单位的转换因子，并将该转换因子应用于输入信号。

Length Conversion 模块的端口标签会根据从 **Initial unit** 和 **Final unit** 列表中选择的输入和输出单位而变化。
