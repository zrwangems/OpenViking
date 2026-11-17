---
type: simulink-block
title: 'Temperature Conversion'
family: 'aeroblks'
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
```yaml
ports:
- name: Port_1
  summary: 温度标量 | 数组
  direction: input
  data_types: double
- name: Port_1
  summary: 温度标量 | 数组
  direction: output
  data_types: double
```

### 输入

### **Port\_1** — 温度标量 | 数组

温度，指定为标量或数组，采用初始温度单位。

#### 依赖关系

输入端口标签取决于 **Initial unit** 设置。

**数据类型：** `double`
### 输出

### **Port\_1** — 温度标量 | 数组

温度，以标量或数组形式返回，采用最终温度单位。

#### 依赖关系

输出端口标签取决于 **Final unit** 设置。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Initial unit
  summary: 输入单位 R（默认）| F | C | K
  group: ''
  block_parameter: IU
  type: 字符向量
  values: '''K'' | ''F'' | ''C'' | ''R'''
  default: '''R'''
- name: Final unit
  summary: 输出单位 K（默认）| F | C | R
  group: ''
  block_parameter: OU
  type: 字符向量
  values: '''K'' | ''F'' | ''C'' | ''R'''
  default: '''K'''
```

### **Initial unit** — 输入单位 `R`（默认）| `F` | `C` | `K`

输入单位，指定为：

|  |  |
| --- | --- |
| `K` | 开尔文 |
| `F` | 华氏度 |
| `C` | 摄氏度 |
| `R` | 兰氏度 |

#### 依赖关系

输入端口标签取决于 **Initial unit** 设置。

#### 编程用法

|  |
| --- |
| **模块参数**：`IU` |
| **类型**：字符向量 |
| **值**：`'K'` | `'F'` | `'C'` | `'R'` |
| **默认值**：`'R'` |

### **Final unit** — 输出单位 `K`（默认）| `F` | `C` | `R`

输出单位，指定为：

|  |  |
| --- | --- |
| `K` | 开尔文 |
| `F` | 华氏度 |
| `C` | 摄氏度 |
| `R` | 兰氏度 |

#### 依赖关系

输出端口标签取决于 **Final unit** 设置。

#### 编程用法

|  |
| --- |
| **模块参数**：`OU` |
| **类型**：字符向量 |
| **值**：`'K'` | `'F'` | `'C'` | `'R'` |
| **默认值**：`'K'` |
## 所属库

Aerospace Blockset / Utilities / Unit Conversions

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

将温度单位转换为所需的温度单位

Temperature Conversion 模块计算从指定的输入温度单位到指定的输出温度单位的转换因子，并将该转换因子应用于输入信号。

Temperature Conversion 模块的端口标签根据从 **Initial unit** 和 **Final unit** 列表中选择的输入和输出单位而变化。
