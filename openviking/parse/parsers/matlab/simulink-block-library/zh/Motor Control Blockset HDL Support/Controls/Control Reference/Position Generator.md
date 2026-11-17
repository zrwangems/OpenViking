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
chinese_source: worker-translation
---

# Position Generator

## 端口

### 输入

### **∆θ** — 位置增量值 标量

固定频率参考电压信号的位置增量值（以标幺值、弧度或度为单位）。以下方程描述了如何计算位置增量值：

- Δθ（标幺值）= Frequency × Sample Time
- Δθ（弧度）= 2π × Frequency × Sample Time
- Δθ（度）= 360 × Frequency × Sample Time

**注意**

如果上述 Δθ 计算导致模块输入产生精度损失，模块可能无法准确复现实际的 *Frequency*。

**数据类型：** `single` | `double` | `fixed point`

### **θ0** — 初始位置信号 标量

固定频率参考电压信号的初始位置值（以标幺值、弧度或度为单位）。

#### 依赖关系

要启用此端口，请将 **Initial state** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `fixed point`

### **Reset** — 外部复位信号 标量

外部脉冲，根据 **External reset** 参数的值复位位置斜坡输出。

#### 依赖关系

要启用此端口，请将 **External reset** 设置为 `active high resets to zero` 或 `active high resets to initial condition`。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **θe** — 参考电压位置 标量

参考电压信号的位置或相位值（以标幺值、弧度或度为单位）。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### **Theta Units** — *θ* 的单位 `Per-unit`（默认）| `Radians` | `Degrees`

输入位置增量值和输出参考电压位置的单位。

### **Initial state** — 指定如何提供 *θ* 的初始值 `Specify via dialog`（默认）| `Input port`

指定初始位置是作为模块参数提供还是作为输入端口提供。

将此参数设置为以下选项之一：

- `Specify via dialog` — 如果要使用模块参数对话框指定初始位置，请选择此选项。
- `Input port` — 如果要使用输入端口指定初始位置，请选择此选项。

### **Initial theta value** — `θe` 的初始值 `0`（默认）| 标量

初始时刻（0 秒）的输出位置斜坡值（以标幺值、弧度或度为单位）。

#### 依赖关系

要启用此参数，请将 **Initial state** 参数设置为 `Specify via dialog`。

### **External reset** — 复位时的输出值 `none`（默认）| `active high resets to zero` | `active high resets to initial condition`

当模块接收到高电平有效外部复位脉冲时的输出位置斜坡值（以标幺值、弧度或度为单位）。您可以将输出复位为零或复位为等于 **Initial theta output** 参数的值。

## 所属库

Motor Control Blockset / Controls / Control Reference Motor Control Blockset HDL Support / Controls / Control Reference

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅当您将 **External reset** 参数设置为 `none` 时，该模块才支持 HDL 代码生成。

### 使用 Fixed-Point Designer™ 进行定点转换设计与仿真定点系统。

## 版本历史

**在 R2020a 中引入**

### R2025a：新增输入端口和模块参数

“模块参数”对话框现在包含 **Initial state** 参数，供您从单独的输入端口 **θ0** 指定初始位置值。

## 描述

生成固定频率的位置斜坡

Position Generator 模块使用参考信号的位置增量值生成位置斜坡信号（其频率与参考电压信号的频率相同）。

我们建议您对此模块使用固定步长离散求解器，以支持代码生成并确保准确的仿真。
