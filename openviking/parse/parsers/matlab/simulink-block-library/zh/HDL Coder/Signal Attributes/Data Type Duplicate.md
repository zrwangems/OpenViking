---
type: simulink-block
title: 'Data Type Duplicate'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'datatypeduplicate'
documentation_source_path: '../simulink/slref/datatypeduplicate.html'
language: zh-CN
chinese_source: worker-translation
---

# Data Type Duplicate

## 端口
```yaml
ports:
- name: Port_1
  summary: 第一个输入信号 标量 | 向量 | 矩阵 | N 维数组
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | uint8 | uint16 | uint32 | string | Boolean | fixed point | enumerated
- name: Port_N
  summary: 第 N 个输入信号 标量 | 向量 | 矩阵 | N 维数组
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | uint8 | uint16 | uint32 | string | Boolean | fixed point | enumerated
```

### 输入

### **Port\_1** — 第一个输入信号 标量 | 向量 | 矩阵 | N 维数组

第一个输入信号，指定为标量、向量、矩阵或 N 维数组。如果所有信号的数据类型不相同，模块将返回错误消息。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `string` | `Boolean` | `fixed point` | `enumerated`

### **Port\_N** — 第 N 个输入信号 标量 | 向量 | 矩阵 | N 维数组

第 N 个输入信号，指定为标量、向量、矩阵或 N 维数组。如果所有信号的数据类型不相同，模块将返回错误消息。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `string` | `Boolean` | `fixed point` | `enumerated`
## 参数
```yaml
parameters:
- name: Number of input ports
  summary: 模块输入端口数 2（默认）| 实数值正整数
  group: ''
  block_parameter: NumInputPorts
  type: 字符向量
  values: 实数值正整数
  default: '''2'''
```

### **Number of input ports** — 模块输入端口数 `2`（默认）| 实数值正整数

将此模块的输入数目指定为实数值正整数。

#### 编程使用

|  |
| --- |
| **模块参数：** `NumInputPorts` |
| **类型：** 字符向量 |
| **值：** 实数值正整数 |
| **默认值：** `'2'` |
## 所属库

Simulink / Signal Attributes HDL Coder / Signal Attributes

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块可用于在生成代码的子系统中强制输入具有相同的数据类型，但不包含在硬件实现中。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

强制所有输入具有相同的数据类型

Data Type Duplicate 模块强制所有输入具有相同的数据类型。输入信号的其他属性（如维度、复杂度和采样时间）是独立的。

您可以使用 Data Type Duplicate 模块检查模块之间数据类型的一致性。如果所有信号的数据类型不相同，模块将返回错误消息。

Data Type Duplicate 模块的典型用法是：模块的一个信号控制所有其他模块的数据类型。其他模块通过反向传播设置为继承其数据类型。

该模块在用户创建的库中也很有用。这些库模块可以放置在任何模型中，所有库模块的数据类型根据模型中的用法进行配置。要创建具有比复制更复杂的数据类型规则的库模块，请使用 Data Type Propagation 模块。
