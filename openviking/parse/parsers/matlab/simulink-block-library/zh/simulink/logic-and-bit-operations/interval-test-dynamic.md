---
type: simulink-block
title: 'Interval Test Dynamic'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Logic and Bit Operations'
documentation_page: 'intervaltestdynamic'
documentation_source_path: 'slref/intervaltestdynamic.html'
language: zh-CN
chinese_source: official
---

# Interval Test Dynamic

## 端口

### 输入

### **up** — 区间的上限 标量 | 向量 | 矩阵 | N 维数组

区间的上限，指定为标量、向量、矩阵或 ND 数组。

#### 限制

当输入信号为枚举类型时，**up** 和 **lo** 信号必须是相同的枚举类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **u** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

输入信号，指定为标量、向量、矩阵或 N 维数组。

#### 限制

当输入信号为枚举类型时，**up** 和 **lo** 信号必须是相同的枚举类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **lo** — 区间的下限 标量 | 向量 | 矩阵 | N 维数组

区间的下限，指定为标量、向量、矩阵或 ND 数组。

#### 限制

当输入信号为枚举类型时，**up** 和 **lo** 信号必须是相同的枚举类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### 输出

### **y** — 输出信号 标量 | 向量 | 矩阵 | N 维数组

指示输入值是否在指定区间内的输出信号。您可以将**输出数据类型**指定为 **boolean** 或 **uint8**。

**数据类型:** `uint8` | `Boolean`

## 参数

### **右半闭区间** — 包含上限值 `on` (默认) | `off`

选中此复选框时，连接到 **up** 输入端口的信号的值将包含在模块输出 true (`1`) 的区间内。

#### 编程用法

|  |
| --- |
| **模块参数**： `IntervalClosedRight` |
| **类型：**字符向量 |
| **值：**`'on' | 'off'` |
| **默认值：**`'on'` |

### **左半闭区间** — 包含下限值 `on` (默认) | `off`

选中此复选框时，连接到 **lo** 输入端口的信号的值将包含在模块输出 true (`1`) 的区间内。

#### 编程用法

|  |
| --- |
| **模块参数**： `IntervalClosedLeft` |
| **类型：**字符向量 |
| **值：**`'on' | 'off'` |
| **默认值：**`'on'` |

### **输出数据类型** — 输出数据类型 **boolean** (默认) | **uint8**

将输出数据类型指定为 `boolean` 或 `uint8`。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'boolean' | 'uint8'` |
| **默认值：**`'boolean'` |

## 所属库

Simulink / Logic and Bit Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

确定信号是否在指定区间中

如果输入介于外部信号 **up** 和 **lo** 的值之间，则 Interval Test Dynamic 模块输出 true (`1`)。如果输入在这些值的范围之外，模块将输出 false (`0`)。要控制模块如何处理等于信号 **lo** 或信号 **up** 的输入值，请使用 **Interval closed on left** 和 **Interval closed on right** 复选框。
