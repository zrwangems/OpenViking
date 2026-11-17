---
type: simulink-block
title: 'String to ASCII'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'String'
documentation_page: 'stringtoascii'
documentation_source_path: 'slref/stringtoascii.html'
language: zh-CN
chinese_source: worker-translation
---

# String to ASCII

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入字符串信号 标量
  direction: input
  data_types: string
- name: Port_1
  summary: 转换后的 uint8 向量信号 向量 | 由 *N* 个元素组成的一维向量
  direction: output
  data_types: uint8
```

### 输入

### **Port\_1** — 输入字符串信号 标量

输入字符串信号，指定为标量。

**数据类型：** `string`
### 输出

### **Port\_1** — 转换后的 uint8 向量信号 向量 | 由 *N* 个元素组成的一维向量

从输入字符串信号转换而来的 ASCII 字符 `uint8` 向量信号，指定为向量。该模块将字符串中的每个元素转换为其对应的 ASCII 字符，并将 ASCII 等效值作为向量输出。如果字符数少于最大长度，该模块在仿真时用零填充剩余空间。在代码生成时，该模块用空字符填充剩余空间。

**数据类型：** `uint8`
## 参数
```yaml
parameters:
- name: Output vector size
  summary: 输出向量的大小 31 （默认） | 标量
  group: ''
  block_parameter: OutputVectorSize
  type: character vector
  values: scalar
  default: '''31'''
```

### **Output vector size** — 输出向量的大小 31 （默认） | 标量

输出字符串向量的大小，指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputVectorSize` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'31'` |
## 所属库

Simulink / String

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `integer` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2024b: String to ASCII 模块输出维度变更

String to
ASCII 模块的输出维度已从二维行向量（例如 2×*N* 向量）变为一维向量 *N*。
*N* 是元素个数。

## 描述

将字符串信号转换为 uint8 向量

String To ASCII 模块将字符串信号转换为 uint8 向量。该模块将字符串中的每个字符转换为其对应的 ASCII 值。例如，该模块将输入字符串 `"Hello"` 转换为 `[72
101 108 108 111]`。
