---
type: simulink-block
title: 'Rounding Function'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Math Operations'
documentation_page: 'roundingfunction'
documentation_source_path: 'slref/roundingfunction.html'
language: zh-CN
chinese_source: official
---

# Rounding Function

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

要应用舍入函数的输入信号。

**数据类型:** `single` | `double`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

对输入信号应用舍入函数后的输出信号。输出信号与输入信号具有相同的维度和数据类型。输出信号的每个元素是对输入信号的对应元素应用所选舍入函数后的结果。

**数据类型:** `single` | `double`

## 参数

### **函数** — 舍入函数 **向下** (默认) | **上半框括号** | **舍入** | **fix**

选择应用于输入信号的舍入函数。

| 舍入函数 | 舍入输入信号的每个元素 |
| --- | --- |
| **向下** | 朝负无穷方向舍入到最邻近的整数值 |
| **上半框括号** | 朝正无穷方向舍入到最邻近的整数 |
| **舍入** | 舍入到最邻近的整数 |
| **fix** | 朝零方向舍入到最邻近的整数 |

#### 编程用法

|  |
| --- |
| **模块参数**：`Operator` |
| **类型**：字符向量 |
| **值**：`'floor'` | `'ceil'` | `'round'` | `'fix'` |
| **默认值**：`'floor'` |

### **采样时间(-1 表示继承)** — 采样之间的时间间隔 `-1` (默认) | 标量 | 向量

指定采样时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

#### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时才可见。要了解详细信息，请参阅不建议设置采样时间的模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SampleTime` |
| **值:** | `"-1"` (默认) | scalar or vector in quotes |

## 所属库

Simulink / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 代码生成要求**

模块的 HDL 代码生成要求您使用单精度数据类型作为模块的输入，并启用原生浮点模式。在“配置参数”对话框的 **HDL 代码生成** > **浮点**窗格上，对于**库**，选择**原生浮点**。要了解有关使用原生浮点模式的详细信息，请参阅Getting Started with HDL Coder Native Floating-Point Support (HDL Coder) 和Generate Target-Independent HDL Code with Native Floating-Point (HDL Coder)。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

| 原生浮点 | |
| --- | --- |
| **LatencyStrategy** | 指定对于浮点运算符是否将设计中的模块映射到 `inherit`、`Max`、`Min`、`Zero` 或 `Custom`。默认值为 **inherit**。另请参阅LatencyStrategy (HDL Coder)。 |
| **NFPCustomLatency** | 要指定值，请将 **LatencyStrategy** 设置为 `Custom`。HDL Coder 会增加延迟，其值等于您为 **NFPCustomLatency** 设置指定的值。另请参阅NFPCustomLatency (HDL Coder)。 |

**复数数据支持**

此模块支持复信号的代码生成。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

对信号应用舍入函数

Rounding Function 模块对输入信号的每个元素进行舍入以产生输出信号。

您可以从**函数**参数列表中选择舍入类型。所选函数的名称显示在模块上。

**提示**

当您需要向量或矩阵输出时，请使用 Rounding Function 模块。
