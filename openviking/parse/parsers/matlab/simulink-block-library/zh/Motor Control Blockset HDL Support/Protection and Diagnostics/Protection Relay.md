---
type: simulink-block
title: 'Protection Relay'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Protection and Diagnostics'
documentation_page: 'protectionrelay'
documentation_source_path: '../mcb/ref/protectionrelay.html'
language: zh-CN
chinese_source: worker-translation
---

# Protection Relay

## 端口

### 输入

### **Imax** — 电流上限标量

反馈回路中电流的上限（单位为安培），用于提供过流保护。当反馈回路中的电流（`Ifb`）超过此值时，该模块会生成一个锁存的故障信号。

#### 依赖

要启用此端口，请将 **Select Protection** 设置为 `Overcurrent`。

**数据类型：** `single` | `double` | `fixed point`

### **Ifb** — 反馈回路中的实际电流标量

给定时刻反馈回路中的实际电流（单位为安培）。

#### 依赖

要启用此端口，请将 **Select Protection** 设置为 `Overcurrent`。

**数据类型：** `single` | `double` | `fixed point`

### **⍵m max** — 用于超速保护的转子速度限值标量

转子的速度限值（单位为 RPM）。当转子速度（`⍵m fb`）超过此值时，该模块会生成一个锁存的故障信号。

#### 依赖

要启用此端口，请将 **Select Protection** 设置为 `Overspeed`。

**数据类型：** `single` | `double` | `fixed point`

### **⍵m fb** — 实际转子速度标量

给定时刻的实际转子速度（单位为 RPM）。

#### 依赖

要启用此端口，请将 **Select Protection** 设置为 `Overspeed`。

**数据类型：** `single` | `double` | `fixed point`

### **Vmax** — 用于过压保护的电压上限标量

反馈回路两端电压的上限（单位为伏特）。当反馈回路两端的电压（`Vfb`）超过此值时，该模块会生成一个锁存的故障信号。

#### 依赖

要启用此端口，请将 **Select Protection** 设置为 `Overvoltage`。

**数据类型：** `single` | `double` | `fixed point`

### **Vmin** — 用于欠压保护的电压下限标量

反馈回路两端电压的下限（单位为伏特）。当反馈回路两端的电压（`Vfb`）低于此值时，该模块会生成一个锁存的故障信号。

#### 依赖

要启用此端口，请将 **Select Protection** 设置为 `Undervoltage`。

**数据类型：** `single` | `double` | `fixed point`

### **Vfb** — 反馈回路两端的实际电压标量

给定时刻反馈回路两端的实际电压（单位为伏特）。

#### 依赖

要启用此端口，请将 **Select Protection** 设置为 `Overvoltage` 或 `Undervoltage`。

**数据类型：** `single` | `double` | `fixed point`

### **Reset** — 外部复位脉冲标量

用于复位故障锁存器的外部脉冲。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **y** — 锁存的故障信号标量

该模块在过流、超速、过压和欠压条件下生成的锁存故障信号，用于保护硬件和电机。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### **Select Protection** — 保护继电器类型 `Overcurrent`（默认）| `Overspeed` | `Overvoltage` | `Undervoltage`

可用的保护类型，用于配置模块在过流、超速、过压和欠压条件下的行为。

### **Maximum count input type** — 最大计数的输入方法 `Specify via dialog`（默认）| `Input port`

使用以下方法之一指定计数器限值：

- `Specify via dialog` — 使用 **Maximum count** 参数指定计数器限值。
- `Input port` — 使用输入端口 **Cntmax** 指定计数器限值。

### **Maximum count** — 计数器限值 `100`（默认）| 标量

该模块用于评估反馈信号是否违反阈值时所使用的计数器支持的最大计数。

### **Samples for debounce filter** — 去抖滤波器采样数 `3`（默认）| 标量

去抖算法用于测试每次阈值违反是否停止所使用的模块采样数。此值决定去抖周期。

## 所属库

Motor Control Blockset HDL Support / Protection and Diagnostics Motor Control Blockset / Protection and Diagnostics

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中引入**

## 描述

使用定时限（DMT）跳闸特性实现保护继电器

Protection Relay 模块使用参考限值、反馈和复位输入信号，为硬件和电机实现具有定时限（DMT）跳闸特性的保护继电器。在发生故障时，该模块会生成一个锁存的故障信号，您可以使用该信号来保护硬件和电机。您可以使用外部复位信号来复位故障锁存。

有关该模块所用算法的更多详细信息，请参阅算法。
