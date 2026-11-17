---
type: simulink-block
title: 'Sine'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Lookup Tables'
documentation_page: 'sine'
documentation_source_path: 'slref/sine.html'
language: zh-CN
chinese_source: worker-translation
---

# Sine

## 端口

### 输入

### **u** — 作为定点正弦或余弦波实现的输入信号 实值信号

输入信号 u，指定为实值标量、向量或矩阵。

为获得有意义的模块输出，模块输入值应落在范围 [0, 1) 内。对于超出此范围的输入值，这些值会被转换为无符号数据类型，其中溢出会回绕。对于这些超出范围的输入，模块输出可能没有意义。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **sin(2\*pi\*u)** — 定点正弦波 实值定点信号

定点正弦波，使用查找表方法实现。

#### 依赖关系

当 **Output formula** 设置为 `sin(2*pi*u)` 或 `sin(2*pi*u) and cos(2*pi*u)` 时，启用此端口。

**数据类型：** `fixed point`

### **cos(2\*pi\*u)** — 定点余弦波 实值定点信号

定点余弦波，使用查找表方法实现。

#### 依赖关系

当 **Output formula** 设置为 `cos(2*pi*u)` 或 `sin(2*pi*u) and cos(2*pi*u)` 时，启用此端口。

**数据类型：** `fixed point`

### **exp(j\*2\*pi\*u)** — exp(j\*2\*pi\*u) 复值定点信号

`exp(j*2*pi*u)`，使用查找表方法实现。

#### 依赖关系

当 **Output formula** 设置为 `exp(j*2*pi*u)` 时，启用此端口。

**数据类型：** `fixed point`

## 参数

### **Output formula** — 选择要输出的信号 `cos(2*pi*u)` | `sin(2*pi*u)` | `exp(j*2*pi*u)` | `sin(2*pi*u) and cos(2*pi*u)`

选择要输出的信号。

对于 Sine 模块，此参数的默认值为 `sin(2*pi*u)`。

对于 Cosine 模块，此参数的默认值为 `cos(2*pi*u)`。

#### 编程用法

|  |
| --- |
| **模块参数：** `Formula` |
| **值：** `'sin(2*pi*u)' | 'cos(2*pi*u)' | 'exp(j*2*pi*u)' | 'sin(2*pi*u) and cos(2*pi*u)'` |

### **Number of data points for lookup table** — 指定要从查找表中检索的数据点数量 `(2^5)+1`（默认值） | 大于或等于 2 的整数

当您将查找表数据点指定为 `(2^n)+1`（其中 *n* 为整数）时，实现效率最高。为与 **Output word length** 参数兼容，**Number of data points for lookup table** 必须小于或等于 (2^(**Output word length**-2)+1)。

#### 编程用法

|  |
| --- |
| **模块参数：** `NumDataPoints` |
| **类型：** 标量 |
| **值：** 大于或等于 2 的整数 |
| **默认值：** `'(2^5)+1'` |

### **Output word length** — 指定输出信号定点数据类型的字长 `16`（默认值） | 从 2 到 53 的整数

输出的小数长度为输出字长减 2。为与 **Number of data points for lookup table** 参数兼容，(2^(**Output word length** - 2) +1) 必须大于或等于 **Number of data points for lookup table**。

**注意**

该模块使用双精度浮点值来构造查找表。因此，您可以在输出中实现的最大精度为 53 位。将字长设置为大于 53 位的值不会提高输出的精度。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutputWordLength` |
| **类型：** 标量 |
| **值：** 从 2 到 53 的整数 |
| **默认值：** `'16'` |

### **Internal rule priority for lookup table** — 指定中间计算的内部规则 `Speed`（默认值） | `Precision`

选择 `Speed` 可加快计算速度。如果这样做，可能会出现精度损失，通常最多 2 位。

#### 编程用法

|  |
| --- |
| **模块参数：** `InternalRulePriority` |
| **值：** `'Speed' | 'Precision'` |
| **默认值：** `'Speed'` |

## 所属库

Simulink / Lookup Tables

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

HDL 代码通过使用您在 Simulink 模块参数中指定的四分之一波查找表来实现 Cosine 和 Sine 模块。

为避免在 HDL 代码中生成除法运算符 (`/`)，对于 **Number of data points for lookup table**，请输入 `(2^n)+1`。*`n`* 为整数。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

如果您使用 Intel® MAX 10 器件，要将查找表映射到 RAM，请在 Quartus 工具中创建工程时添加以下 Tcl 命令：

`set_global_assignment -name INTERNAL_FLASH_UPDATE_MODE "SINGLE IMAGE
WITH ERAM"`

**注意**

基于查找表的 sine 和 cosine 模块不会生成硬件优化的 HDL 代码。为获得更好的综合结果，请使用 Sine HDL Optimized 和 Cosine HDL Optimized (HDL Coder) 模块。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

使用利用四分之一波对称性的查找表方法实现定点正弦或余弦波

Sine 和 Cosine 模块使用利用四分之一波对称性的查找表方法以定点实现正弦波、余弦波或两者。该模块可以输出输入信号的以下函数，具体取决于您为 **Output formula** 参数选择的内容：

- sin(2π*u*)
- cos(2π*u*)
- exp(*j*2π*u*)
- sin(2π*u*) 和 cos(2π*u*)

您在 **Number of data points for lookup table** 参数中定义查找表点的数量。当您将查找表数据点指定为 `(2^n)+1`（其中 *n* 为整数）时，模块实现效率最高。

使用 **Output word length** 参数指定定点输出数据类型的字长。输出的小数长度为输出字长减 2。
