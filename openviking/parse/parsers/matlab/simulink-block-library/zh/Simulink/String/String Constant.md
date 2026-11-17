---
type: simulink-block
title: 'String Constant'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'String'
documentation_page: 'stringconstant'
documentation_source_path: 'slref/stringconstant.html'
language: zh-CN
chinese_source: worker-translation
---

# String Constant

## 端口

### 输出

### **Port\_1** — 输出字符串标量

输出字符串，指定为标量。

**数据类型：** `string`

## 参数

### **String** — 输入字符串 "Hello!"（默认）| 标量

输入字符串，指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数：** `String` |
| **类型：** 字符向量 |
| **值：** `'"Hello!"'` | 标量 |
| **默认值：** `'"Hello!"'` |

### **Output data type** — 输出数据类型 `string`（默认）| `<data type expression>`

输出数据类型，使用 string 数据类型指定以表示没有最大长度的字符串。

要指定具有最大长度的字符串数据类型，请指定
`stringtype(N)`。例如，`stringtype(31)` 创建一个最大长度为 31 个字符的字符串数据类型。

点击 **Show data type assistant** 按钮以显示 **Data Type
Assistant**，它可以帮助您设置数据类型属性。有关更多信息，请参阅
使用数据类型助手指定数据类型。

#### 编程使用

|  |
| --- |
| **模块参数：** `OutDataTypeStr` |
| **类型：** 字符向量 |
| **值：** `'string'` | *`<data type expression>`* |
| **默认值：** `'string'` |

### **Mode** — 数据类别 `string`（默认）| `scalar`

使用 `stringtype` 函数，例如，
`stringtype(31)`。

#### 依赖关系

点击 **Show data type assistant** 按钮
可启用此参数。

## 所属库

Simulink / String

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `string` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL
实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2018a 中引入**

## 描述

输出指定的字符串

String Constant 模块输出由
**String** 参数指定的字符串。当您需要一个类型为 string 的常量时，请使用此模块。
