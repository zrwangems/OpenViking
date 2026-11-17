---
type: simulink-block
title: 'Variant End'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'variantend'
documentation_source_path: 'slref/variantend.html'
language: zh-CN
chinese_source: worker-translation
---

# Variant End

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入分支 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | image
- name: Port_N
  summary: 与第 *N* 个分支关联的输入端口 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | image
- name: Port_1
  summary: 输出信号 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | image
```

### 输入

### **Port\_1** — 输入分支 标量 | 向量 | 矩阵

输入分支，与对应的 Variant Start 模块一起定义有界区域的结束。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### **Port\_N** — 与第 *N* 个分支关联的输入端口 标量 | 向量 | 矩阵

与第 *N* 个分支关联的输入端口，与对应的 Variant Start 模块一起定义有界区域的结束。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

来自活动变体的输出信号。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
## 参数
```yaml
parameters:
- name: Variant Start End Tag
  summary: 有界区域的唯一标识符 A（默认）| 有效的 MATLAB® 标识符
  group: ''
  block_parameter: VariantStartEndTag
  type: 字符向量
  values: '''A'' | 有效的 MATLAB 标识符'
- name: Variant Paired Block
  summary: 用于高亮显示配对的 Variant Start 模块的选项 off（默认）| on
  group: ''
  block_parameter: VariantPairedBlock
  type: 字符向量
  values: '''off'' | ''on'''
```

### **Variant Start End Tag** — 有界区域的唯一标识符 `A`（默认）| 有效的 MATLAB® 标识符

用于标识构成有界区域的正确 Variant Start 和 Variant End 配对的唯一标识符，指定为有效的 MATLAB 标识符。有效的 MATLAB 标识符是由字母数字（A–Z、a–z、0–9）和下划线组成的字符向量，其中第一个字符为字母，且字符向量的长度小于或等于 `namelengthmax`。

#### 编程使用

|  |
| --- |
| **模块参数：** `VariantStartEndTag` |
| **类型：** 字符向量 |
| **值：** `'A'` | 有效的 MATLAB 标识符 |
| **默认：** `'A'` |

### **Variant Paired Block** — 用于高亮显示配对的 Variant Start 模块的选项 `off`（默认）| `on`

选择此参数可高亮显示与 Variant End 具有相同 **Variant Start End Tag** 的 Variant Start。如果存在多个具有相同 **Variant Start End Tag** 的 Variant Start 模块，则高亮显示找到的第一个模块。

#### 编程使用

|  |
| --- |
| **模块参数：** `VariantPairedBlock` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |
## 所属库

Simulink / Signal Routing

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2024a 中引入**

## 描述

定义有界区域的结束

Variant End 模块定义有界区域的结束，允许您限制变体条件传播而不引入层级。使用 Variant Start 模块定义有界区域的开始。每个 Variant Start 模块都有一个对应的 Variant End 模块。当您在 Variant Start 模块上指定变体条件时，对应的 Variant End 模块会在编译时根据唯一的 **Variant Start End Tag** 继承条件和其他参数。
