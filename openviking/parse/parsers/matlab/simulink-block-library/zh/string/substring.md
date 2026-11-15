---
type: simulink-block
title: 'Substring'
family: string
documentation_release: R2025b
official_category: 'String'
documentation_page: 'substring'
language: zh-CN
chinese_source: worker-translation
---

# Substring



从输入字符串信号中提取子字符串

## 库

Simulink / String

## 描述

Substring 模块从输入字符串信号中提取子字符串。该模块从与 **idx** 对应的字符开始提取子字符串，并包含从 **idx** 开始的 **len** 个字符。例如，如果输入字符串为 `"hello 123"`，输入 **idx** 为 `1`，输入 **len** 为 `5`，则输出为 `"hello"`。该模块从 `1` 开始提取子字符串，并提取接下来的 4 个字符，总共 5 个字符（`hello`）。

## 端口

### 输入

### **str** — 输入字符串信号标量

输入字符串信号，指定为字符串。

**数据类型：** `string`

### **idx** — 要提取的字符串起始位置标量

要提取的字符串起始位置，指定为正标量整数。

**数据类型：** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **len** — 要提取的字符串长度标量

要提取的字符串长度，指定为标量。如果 **len** 导致子字符串超出字符串末尾，则输出信号包含的字符数少于 **len**。

**数据类型：** `uint8` | `uint16` | `uint32`

### 输出

### **sub** — 提取的字符串标量

提取的字符串，指定为标量。

**数据类型：** `string`

## 参数

### **从输入继承最大长度** — 使用与输入字符串相同的最大长度 `on`（默认） | `off`

使用与输入字符串源模块相同的最大长度。

on
:   使用相同的最大长度。子字符串包含从 **idx** 处的字符开始到字符串末尾的字符。

off
:   不使用相同的最大长度。

#### 依赖关系

选中此复选框会启用 **输出数据类型** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `InheritMaximumLength` |
| **类型：** character vector |
| **值：** `'on'` | `'off'` |
| **默认：** `'on'` |

### **输出数据类型** — 输出数据类型 `string`（默认） | `<data type expression>`

输出数据类型，使用 string 数据类型来指定无最大长度的字符串。

要指定具有最大长度的 string 数据类型，请指定 `stringtype(N)`。例如，`stringtype(31)` 创建一个最大长度为 31 个字符的 string 数据类型。

单击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型。

#### 依赖关系

要启用此参数，请选中 **从输入继承最大长度**。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutDataTypeStr` |
| **类型：** character vector |
| **值：** `'string'` | *`<data type expression>`* |
| **默认：** `'string'` |

### **从 'idx' 到末尾输出字符串** — 从 `idx` 提取字符串到末尾 `off`（默认） | `on`

从 `idx` 提取字符串到输入字符串末尾。

on
:   从 `idx` 提取字符串到输入字符串末尾。

off
:   不从 `idx` 提取字符串到输入字符串末尾。

#### 依赖关系

选中此参数会移除第三个输入端口。

#### 编程用法

|  |
| --- |
| **模块参数：** `StringFromIdxToEnd` |
| **类型：** character vector |
| **值：** `'on'` | `'off'` |
| **默认：** `'off'` |

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `integer` | `string` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2018a 中引入**
