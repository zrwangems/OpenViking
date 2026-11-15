---
type: simulink-block
title: 'Mechanical to Electrical Position'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Control Algorithm Design / Sensor Decoders'
documentation_page: 'mechanicaltoelectricalposition'
documentation_source_path: 'ref/mechanicaltoelectricalposition.html'
language: zh-CN
chinese_source: official
---

# Mechanical to Electrical Position

## 端口

### 输入

### **θm** — 转子的机械位置 标量

转子的机械位置（作为转子位置传感器的输出），单位可以为弧度（0 至 2π）、角度（0 至 360）或标幺单位（0 至 1）。

**数据类型:** `single` | `double` | `fixed point`

### **Npp** — 电机中可用的极对数 标量

电机中可用的极对数。

#### 依赖关系

要启用此端口，请将**极对输入**参数设置为**输入端口**。

**数据类型:** `single` | `double` | `fixed point`

### **Offset** — 机械位置偏移量 标量

转子电气零点位置偏离机械零点位置的量。偏移量的单位与机械位置输入的单位相同。

#### 依赖关系

要启用此端口，请将**指定偏移量的方式**指定为**输入端口**。

**数据类型:** `single` | `double` | `fixed point`

**注意**

您在所有输入端口指定的值应具有相同的数据类型。
### 输出

### **θe** — 转子的电气位置 标量

转子的电气位置，其范围与机械位置输入的范围相同。电气位置的数据类型与输入的数据类型相同。

**数据类型:** `single` | `double` | `fixed point`

## 参数

### **极对输入** — 用于指定电机中可用极对数的方法 **通过对话框指定** (默认) | **输入端口**

您要用于指定电机中可用极对数的方法。选择**输入端口** 可启用并使用输入端口 **Npp**。选择**通过对话框指定**可使用对话框提供极对数。

### **极对数** — 电机中可用的极对数 `4` (默认) | 标量

电机中可用的极对数。

#### 依赖关系

要启用此参数，请将**极对输入**参数设置为**通过对话框指定**。

### **输入机械角度单位** — 转子机械位置的单位 **标幺** (默认) | **弧度** | **度**

转子机械位置的单位。

### **偏移量输入类型** — 用于指定偏移量的方法 **输入端口** (默认) | **通过对话框指定**

用于指定机械位置偏移量的方法。

- 选择**输入端口**可启用并使用输入端口**偏移量**。
- 选择**通过对话框指定**可启用**机械偏移量**参数并提供偏移值。

### **机械偏移量** — 机械位置的偏移值 `0` (默认) | 标量

在此参数中指定机械位置偏移值。偏移量的单位必须与机械位置输入的单位相同。

#### 依赖关系

要启用此参数，请将**偏移量输入类型**设置为**通过对话框指定**。

### **输入数据类型** — 输入端口的数据类型 **单精度** (默认) | **双精度** | **定点**

要用于输入端口的数据类型。

**注意**

如果您选择定点输入数据类型并向输入端口提供定点值，则当该模块部署到硬件上时运行速度会更快。

## 所属库

Motor Control Blockset / Sensor Decoders Motor Control Blockset HDL Support / Sensor Decoders

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

根据转子的机械位置计算其电气位置

Mechanical to Electrical Position 模块通过使用转子的机械位置、机械偏移值和极对数来计算转子的电气位置。
