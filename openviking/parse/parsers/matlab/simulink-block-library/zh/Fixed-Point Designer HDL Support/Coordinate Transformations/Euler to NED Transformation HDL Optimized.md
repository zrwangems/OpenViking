---
type: simulink-block
title: 'Euler to NED Transformation HDL Optimized'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Coordinate Transformations'
documentation_page: 'eulertonedtransformationhdloptimized'
documentation_source_path: '../fixedpoint/ref/eulertonedtransformationhdloptimized.html'
language: zh-CN
chinese_source: worker-translation
---

# Euler to NED Transformation HDL Optimized

## 端口

### 输入

### **U In** — 输入数组 3×1 向量

输入数组，指定为 3×1 向量。

定点输入必须使用二进制小数点定标。

**示例：**
`UIn = [0;0;1]`

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** 是

### **Angle In** — 旋转角度 3×1 向量

旋转角度，指定为包含角度 phi、theta 和 psi（以弧度为单位）的 3×1 实值向量。

**示例：**
`AngleIn = [phi;theta;psi]`

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Valid In** — 输入是否有效 `Boolean` 标量

输入是否有效，指定为布尔标量。此控制信号指示来自 **U In** 和 **Angle In** 输入端口的数据何时有效。当此值为 `1`（`true`）时，模块捕获 **U In** 和 **Angle In** 输入端口的值。当此值为 `0`（`false`）时，模块忽略输入采样。

**数据类型：** `Boolean`

### **Restart** — 是否清除内部状态 `Boolean` 标量

是否清除内部状态，指定为布尔标量。当此值为 1（`true`）时，模块停止当前计算并清除所有内部状态。当此值为 0（`false`）且 **Valid In** 值为 1（`true`）时，模块开始新的子帧。

**数据类型：** `Boolean`
### 输出

### **U Out** — 旋转后的数组 3×1 向量

旋转后的数组，以 3×1 向量形式返回。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Valid Out** — 输出数据是否有效 布尔标量

输出数据是否有效，以布尔标量形式返回。当此控制信号的值为 `1`（`true`）时，模块已成功计算输出 **U Out**。当此值为 `0`（`false`）时，输出数据无效。

**数据类型：** `Boolean`

### **Ready** — 模块是否准备好接收输入 `Boolean` 标量

模块是否准备好接收输入，以布尔标量形式返回。此控制信号指示模块何时准备好接收新的输入数据。当此值为 1（`true`）且 **Valid In** 值为 1（`true`）时，模块在下一个时间步接受输入数据。当此值为 0（`false`）时，模块在下一个时间步忽略输入数据。

**数据类型：** `Boolean`

## 参数

### **Architecture** — 架构类型 `Pipelined`（默认）| `Burst`

此参数指定架构类型。

- `Pipelined` — 选择此值以指定低延迟架构。
- `Burst` — 选择此值以指定最小资源架构。

#### 编程使用

|  |
| --- |
| **模块参数**：`Architecture` |
| **类型**：character vector |
| **值**：`'Pipelined'` | `'Burst'` |
| **默认值**：`'Pipelined'` |

## 所属库

Fixed-Point Designer HDL Support / Coordinate Transformations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

仅支持定点数据类型。定点数据类型必须使用二进制小数点定标。

生成的 C/C++ 代码将具有 HDL 模块的时序。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持定点数据类型。定点数据类型必须使用二进制小数点定标。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2022b 中引入**

## 描述

使用流水线或突发架构计算 Euler 到 North-East-Down 变换，并生成优化的 HDL 代码

Euler to NED Transformation HDL Optimized 模块提供两种架构，使用 CORDIC 旋转内核为 FPGA 和 ASIC 应用实现 Euler 到 North-East-Down (NED) 变换。

您可以选择针对吞吐量或面积进行优化的架构。

- `Pipelined` — 将此架构用于高吞吐量应用。
- `Burst` — 将此架构用于最小资源实现。

Euler to NED Transformation HDL Optimized 模块提供硬件友好的控制信号。
