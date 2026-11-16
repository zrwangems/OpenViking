---
type: simulink-block
title: 'Push Button'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Programmable Logic IO'
documentation_page: 'pushbutton'
documentation_source_path: 'ref/pushbutton.html'
language: zh-CN
chinese_source: worker-translation
---

# Push Button

## 端口

### 输入

### **PBIn*`x`*** — 输入信号 `Boolean` 标量

用于控制硬件逻辑的输入信号。使用这些端口，您可以在仿真期间运行时动态控制硬件逻辑。每个按键都有一个端口，命名为 **PBIn1** 到 **PBIn*`x`***，其中 *`x`* 是 **Number of push buttons**。

#### 依赖项

要启用此端口，请将 **Specify push buttons via** 参数设置为 `InputPort`。

**数据类型：** `Boolean`
### 输出

### **PB*`x`*** — 输出信号 `Boolean` 标量

返回按键状态的输出信号。每个按键都有一个端口，命名为 **PB1** 到 **PB*`x`***，其中 *`x`* 是 **Number of push buttons**。

**数据类型：** `Boolean`

## 参数

### **Hardware board** — 查看所选硬件 `None` (默认) | 支持的 Xilinx® 或 Intel ® 板卡 | 自定义板卡

此参数为只读。要选择硬件板并配置板参数，请参阅硬件实现窗格。

### **View push buttons location** — 查看按键按钮

要查看所选硬件板上按键位置的示意图，请点击 **View push buttons location** 按钮。

仅当您选择特定的 Xilinx 或 Intel 板卡时，此按钮才启用。有关这些板卡的详细信息，请参阅支持的第三方工具和硬件。

### **IO logic** — IO 逻辑指示符 `None` (默认) | `Active High` | `Active Low`

此参数为只读。指示所选硬件板上的 IO 逻辑电平。

当 **IO logic** 参数显示为 **Active Low** 时，Push Button 模块在您将 **Specify push buttons via** 参数设置为 `InputPort` 时接受并输出低电平有效信号，并在您将 **Specify push buttons via** 参数设置为 `Dialog` 时输出低电平有效信号。该模块表示这些端口名以字母 *n* 为前缀。例如，**nPB1**。

### **Specify push buttons via** — 按键来源 `Dialog` (默认) | `InputPort`

要通过使用模块参数控制硬件逻辑，请选择 `Dialog`。要从输入端口控制硬件逻辑，请选择 `InputPort`。

### **Number of push buttons** — 按键选择 `1` (默认) | 范围 [1, n] 内的整数列表

要指定所需的按键端口数量，请从 **Number of push buttons** 列表中选择一个值。*`n`* 表示指定硬件板上可用按键的数量。例如，如果您从列表中选择 `3`，则该模块会显示三个按键端口。

要仅使用第 *`n`* 个按键，请将 **Number of push buttons** 参数设置为 *`n`*，并终止未使用的按键端口。

### **PB*`n`*** — 选中的按键 `Off` (默认) | `On`

要启用第 *`n`* 个按键端口，请为 PB*`n`* 参数选择 `On`。*`n`* 表示指定硬件板上可用按键的数量。

#### 依赖项

要启用此参数，请将 **Specify push buttons via** 参数设置为 `Dialog`。

### **Sample time** — 采样间隔 -1 (默认) | 正标量

指定按键在 `On` 和 `Off` 之间切换的时间间隔。

## 所属库

SoC Blockset / Hardware Logic I/O

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要为您的设计自动生成 HDL 代码，并在 SoC 设备上执行，请使用 **SoC Builder** 工具。请参阅使用 SoC Builder 生成 SoC 设计。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2019a 中引入**

## 描述

连接与硬件板上按键相连的信号

Push Button 模块控制硬件机制。连接到 Push Button 模块的硬件逻辑信号等效于连接到硬件板上的按键的信号。
