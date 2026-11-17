---
type: simulink-block
title: 'Coulomb and Viscous Friction'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Discontinuities'
documentation_page: 'coulombandviscousfriction'
documentation_source_path: 'slref/coulombandviscousfriction.html'
language: zh-CN
chinese_source: official
---

# Coulomb and Viscous Friction

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

库仑和粘性摩擦模型的输入信号。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

通过将摩擦模型应用于输入来计算输出信号。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

要编辑 Coulomb and Viscous Friction 模块的参数，请双击模块图标。

### **库仑摩擦值** — 静态摩擦偏移量 `[1320]` (默认) | 实数值

指定应用于所有输入值的偏移量。

#### 编程用法

|  |
| --- |
| **模块参数**：`offset` |
| **类型**：字符向量 |
| **值**：实数值 |
| **默认值**：`'[1 3 2 0]'` |

### **粘性摩擦系数** — 动态摩擦系数 `1` (默认) | 实数值

指定非零输入值的信号增益。

#### 编程用法

|  |
| --- |
| **模块参数**：`gain` |
| **类型**：字符向量 |
| **值**：实数值 |
| **默认值**：`'1'` |

## 所属库

Simulink / Discontinuities HDL Coder / Discontinuities

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
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

**限制**

HDL 代码生成不支持复数输入。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

对值为零时的不连续性以及非零时的线性增益建模

Coulomb and Viscous Friction 模块用于对库仑（静态）摩擦和粘性（动态）摩擦进行建模。此模块可以对值为零时的不连续性以及非零时的线性增益进行建模。

模块输出匹配以下公式的 MATLAB® 结果：

```
y = sign(x) .* (Gain .* abs(x) + Offset)
```

其中 `y` 是输出，`x` 是输入，`Gain` 是非零输入值的信号增益，`Offset` 是库仑摩擦。

此模块接受一个输入并生成一个输出。输入可以是标量、向量或包含实数和复数元素的矩阵。

- 对于标量输入，`Gain` 和 `Offset` 的维度可以不同于输入。输出是标量、向量或矩阵，具体取决于 `Gain` 和 `Offset` 的维度。
- 对于向量或矩阵输入，`Gain` 和 `Offset` 必须为标量或与输入具有相同的维度。输出是向量或与输入具有相同维度的矩阵。
