---
type: simulink-block
title: 'Position Generator'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'positiongenerator'
documentation_source_path: '../mcb/ref/positiongenerator.html'
language: zh-CN
chinese_source: official
---

# Position Generator

## 端口

### 输入

### **∆θ** — 位置增量值 标量

固定频率参考电压信号的位置增量值（以标幺、弧度或度为单位）。下列方程描述如何计算位置增量值：

- Δθ (per unit) = Frequency × Sample Time
- Δθ (radians) = 2π × Frequency × Sample Time
- Δθ (degrees) = 360 × Frequency × Sample Time

**注意**

如果前面的 Δθ 计算导致模块输入中出现精度损失，则模块可能无法准确复制实际的 *Frequency*。

**数据类型:** `single` | `double` | `fixed point`

### **θ0** — 初始位置信号 标量

固定频率参考电压信号的初始位置值（以标幺、弧度或度为单位）。

#### 依赖关系

要启用此端口，请将**初始状态**参数设置为**输入端口**。

**数据类型:** `single` | `double` | `fixed point`

### **Reset** — 外部重置信号 标量

根据**外部重置**参数值重置位置斜坡输出的外部脉冲。

#### 依赖关系

要启用此端口，请将**外部重置**设置为**高电平重置为零**或**高电平重置为初始条件**。

**数据类型:** `single` | `double` | `fixed point`
### 输出

### **θe** — 参考电压位置 标量

参考电压信号的位置或相位值（以标幺、弧度或度为单位）。

**数据类型:** `single` | `double` | `fixed point`

## 参数

### **Theta 单位** — *θ* 的单位 **标幺** (默认) | **弧度** | **度**

输入位置增量值和输出参考电压位置的单位。

### **初始状态** — 指定如何提供 *θ* 的初始值 **通过对话框指定** (默认) | **输入端口**

指定是否将初始位置作为模块参数或输入端口提供。

将此参数设置为以下选项之一：

- **通过对话框指定** - 如果您要使用“模块参数”对话框指定初始位置，请选择此选项。
- **输入端口** - 如果您要使用输入端口指定初始位置，请选择此选项。

### **初始 theta 值** — `θe` 的初始值 `0` (默认) | 标量

初始时间（0 秒）时的输出位置斜坡值（以标幺、弧度或度为单位）。

#### 依赖关系

要启用此参数，请将**初始状态**参数设置为**通过对话框指定**。

### **外部重置** — 重置时的输出值 **无** (默认) | **高电平重置为零** | **高电平重置为初始条件**

模块接收到有效的高电平外部重置脉冲时的输出位置斜坡值（以标幺、弧度或度为单位）。您可以将输出重置为零或等于**初始 theta 输出**参数的值。

## 所属库

Motor Control Blockset / Controls / Control Reference Motor Control Blockset HDL Support / Controls / Control Reference

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

**限制**

仅当**外部重置**参数设置为**无**时，该模块才支持 HDL 代码生成。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中推出**

### R2025a: 增加了新的输入端口和模块参数

“模块参数”对话框现在包含**初始状态**参数，可让您从单独的输入端口 **θ0** 指定初始位置值。

## 描述

生成固定频率的位置斜坡

Position Generator 模块使用参考信号的位置增量值生成位置斜坡信号（其频率与参考电压信号的频率相同）。

我们建议您对该模块使用定步长离散求解器，以实现代码生成并确保精确仿真。
