---
type: simulink-block
title: 'Sine HDL Optimized and Cosine HDL Optimized'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Code Generation from Simulink / Model and Architecture Design / Model Design / Basic HDL Algorithms / Lookup Tables'
documentation_page: 'sinehdloptimizedandcosinehdloptimized'
documentation_source_path: 'ref/sinehdloptimizedandcosinehdloptimized.html'
language: zh-CN
chinese_source: worker-translation
---

# Sine HDL Optimized and Cosine HDL Optimized

## 端口

### 输入

### **Input** — 用于实现正弦或余弦波的输入信号，实值信号

输入信号 u，指定为实值标量、向量或矩阵。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **sin(2\*pi\*u)** — 定点正弦波，实值定点信号

定点正弦波，使用查找表方法实现。

#### 依赖关系

当**输出公式**设置为
`sin(2*pi*u)` 或 `sin(2*pi*u) and
cos(2*pi*u)` 时，启用此端口。

**数据类型：** `fixed point`

### **cos(2\*pi\*u)** — 定点余弦波，实值定点信号

定点余弦波，使用查找表方法实现。

#### 依赖关系

当**输出公式**设置为
`cos(2*pi*u)` 或 `sin(2*pi*u) and
cos(2*pi*u)` 时，启用此端口。

**数据类型：** `fixed point`

### **exp(j\*2\*pi\*u)** — 复指数，复值定点信号

复指数，使用查找表方法实现。

#### 依赖关系

当**输出公式**设置为
`exp(j*2*pi*u)` 时，启用此端口。

**数据类型：** `fixed point`

## 参数

### **输出公式** — 选择要输出的信号 `cos(2*pi*u)` | `sin(2*pi*u)` | `exp(j*2*pi*u)` | `sin(2*pi*u) and cos(2*pi*u)`

选择要输出的信号。

### **数据点数** — 指定要从查找表中检索的数据点数 `64`（默认） | `integer, greater than or equal to 2`

指定要从查找表中检索的数据点数。当您将查找表数据点指定为
`(2^n)` 时，实现最高效，其中 *n* 是
整数。

### **表数据类型** — 指定表数据类型 `fixdt(0,16,15)`（默认） | `fixed point expression`

指定表数据类型。您可以指定一个求值为数据
类型的表达式，例如 `fixdt(1,16,0)`。

单击 **显示数据类型助手** 按钮
以显示 **数据类型
助手**，它可帮助您设置表数据类型。

### **数据类型助手** — 选择数据类型指定模式 `Fixed point`（默认） | `Expression`

选择数据类型指定模式。如果选择
`Expression`，请输入一个求值为数据
类型的表达式，例如 `fixdt(1,16,0)`。

如果选择 `Fixed point`，则可以使用
**数据类型助手** 中的选项来指定定点数据类型。在
`Fixed point` 模式下，您可以选择二进制小数点定标，并
指定符号性、字长、小数长度以及数据类型覆盖
设置。

### **模拟 RAM 延迟** — 插入单位延迟 `off`（默认） | `on`

选中此复选框会插入一个无复位的单位延迟。您可以在
Simulink® 建模环境中模拟此
延迟。生成 HDL 代码时，会在模块后插入一个
无复位寄存器。查找表与无复位寄存器的
组合会映射到目标硬件上的 RAM。

## 所属库

HDL Coder / Lookup Tables

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 生成用于 FPGA 和 ASIC 设计的 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

HDL 代码使用您在 Simulink 模块参数中指定的四分之一波查找表来实现 Sine HDL Optimized 或 Cosine HDL
Optimized 模块。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中的现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline。 |
| **MapToRAM** | 将查找表 (LUTs) 映射到 RAM。默认值为 `on`。另请参阅 MapToRAM。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline。 |

## 版本历史

**在 R2016b 中引入**

## 描述

使用针对 HDL 代码生成优化的查找表方法实现定点正弦和余弦波

Sine HDL Optimized 模块和 Cosine HDL Optimized 模块
使用利用四分之一波对称性的查找表方法实现定点正弦或余弦波。

为了实现最高效的 HDL 实现，请将模块的元素数量配置为精确的 2 的幂。在“模块参数”对话框中，对于**数据
点数**，指定一个为精确的 2 的幂的整数。也就是说，将
查找表数据点指定为 `(2^n)`，其中
*n* 是整数。默认情况下，**数据
点数**为 64。

当您为**数据
点数**指定 2 的幂时，在 HDL 代码生成后，查找表位于无复位寄存器之前。查找表
模块与无复位寄存器的组合可高效映射到目标
设备上的 RAM。

根据您对**输出公式**参数的选择，这些
模块可以输出输入信号的以下函数：

- sin(2π*u*)
- cos(2π*u*)
- exp(*i*2π*u*)
- sin(2π*u*) 和 cos(2π*u*)

使用**表数据类型**参数指定
定点输出数据类型的字长。输出的小数长度是输出字长
减 2。
