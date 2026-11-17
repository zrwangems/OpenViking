---
type: simulink-block
title: 'Derating Function'
family: 'motor-control-blockset-hdl-support'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Controllers'
documentation_page: 'deratingfunction'
documentation_source_path: 'ref/deratingfunction.html'
language: zh-CN
chinese_source: official
---

# Derating Function

## 端口

### 输入

### **fmax** — 参考信号最大限值 标量

参考信号值的最大限值，如果超出该限值，降额因子将变为零。

**数据类型:** `single` | `double` | `fixed point`

### **ffeedback** — 参考反馈信号 标量

模块用于生成降额因子的参考信号，生成后您可以用该信号对控制信号进行降额处理。

**数据类型:** `single` | `double` | `fixed point`
### 输出

### **y** — 降额因子 标量

模块在信号超出**降额阈值**参数值时根据参考信号的反馈和最大限值生成的降额因子。

**数据类型:** `single` | `double` | `fixed point`

## 参数

### **降额阈值** — 降额阈值，超过该阈值必须发生降额 `0.9` (默认) | 范围 [0,1) 中的标量

参考信号值，超出该值则模块将生成降额因子。

## 所属库

Motor Control Blockset / Controls / Controllers Motor Control Blockset HDL Support / Controls / Controllers

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 要通过移动设计中的现有延迟来放置在输出端的寄存器的数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中推出**

## 描述

计算降额因子

Derating Function 模块根据输入参考信号的反馈 (*ffeedback*) 和最大限值 (*fmax*) 生成降额因子 (*y*)。

降额因子：

- 当 *ffeedback* 位于**降额阈值**的正值和负值之间时，保持等于 1。根据 *ffeedback*，降额因子在此范围之外呈线性变化。
- 当参考信号超出（正值或负值）*fmax* 时，保持等于零。

因此，在参考信号超出指定的**降额阈值**后，您可以使用生成的降额因子对控制信号进行降额处理。

下图显示使用正弦波作为 *ffeedback* 时的模块输出。

### 方程

**降额阈值**参数 x 表示参考信号峰值振幅的百分比。在所示的模块输出中，**降额阈值**为 0.5，因此阈值为 2（正弦参考信号的峰值振幅值为 4）。

x=[0,1)

此方程描述模块如何计算降额因子 (*y*)。

Derating factor (y)=1−ffeedback−xfmax(1−x)fmax
