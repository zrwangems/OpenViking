---
type: simulink-block
title: 'Float Typecast'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Floating Point Operations'
documentation_page: 'floattypecast'
documentation_source_path: 'ref/floattypecast.html'
language: zh-CN
chinese_source: worker-translation
---

# Float Typecast

## 端口
```yaml
ports:
- name: Port_1(u)
  summary: 输入信号 scalar | vector
  direction: input
  data_types: singledouble | uint32 | fixed point
- name: Port_1(y)
  summary: 输出信号 scalar | vector
  direction: output
  data_types: single | double | uint32 | fixed point
```

### 输入

### **Port\_1(u)** — 输入信号 `scalar` | `vector`

用于向模块提供输入的端口。

**数据类型：** `singledouble` | `uint32` | `fixed point`
### 输出

### **Port\_1(y)** — 输出信号 `scalar` | `vector`

用于从模块获取计算输出的端口。

**数据类型：** `single` | `double` | `uint32` | `fixed point`
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

HDL Coder / HDL Floating Point Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

该模块支持在 `Native Floating
Point` 模式下生成 HDL 代码。要使用此模式，请将 `single` 或
`uint32` 数据类型指定为模块的输入。借助 HDL Code
Advisor，您可以替换使用
`Stored Integer (SI)` 模式并在浮点与定点数据类型之间转换的 Data Type Conversion 模块。

该模块支持复数信号的代码生成。

## 版本历史

**在 R2017b 中引入**

## 描述

将浮点类型转换为无符号整数，或反之

该模块将输入的底层位转换为相应的定点或浮点表示。模块的输入和输出包含相同的位数。

| 输入数据类型 | 输出数据类型 |
| --- | --- |
| `half` | `uint16` |
| `single` | `uint32` |
| `double` | `uint64` |
| `uint32` | `single` |
| `uint64` | `double` |
| `uint16` | `half` |

下图展示了模块掩码、行为和输出数据类型如何根据您指定的输入数据类型动态变化。

展示了输出数据类型如何随输入数据类型的变化而变化。
