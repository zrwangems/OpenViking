---
type: simulink-block
title: 'DIP Switch'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Programmable Logic IO'
documentation_page: 'dipswitch'
documentation_source_path: 'ref/dipswitch.html'
language: zh-CN
chinese_source: worker-translation
---

# DIP Switch

## 端口

### 输入

### **DSIn*`x`*** — 输入信号 `Boolean` 标量

用于控制硬件逻辑的输入信号。使用此端口，您可以在仿真期间运行时动态控制硬件逻辑。每个 DIP 开关都有一个端口，命名为 **DSIn1** 到 **DSIn*`x`***，其中 *`x`* 是 **Number of DIP switches**。

#### 依赖关系

要启用此端口，请将 **Specify DIP switches via** 参数设置为 `InputPort`。

**数据类型：** `Boolean`
### 输出

### **DS*`x`*** — 输出信号 `Boolean` 标量

返回开关状态的输出信号。每个 DIP 开关都有一个端口，命名为 **DS1** 到 **DS***`x`*，其中 *`x`* 是 **Number of DIP switches**。

**数据类型：** `Boolean`

## 参数

### **Hardware board** — 查看选定的硬件 `None`（默认） | 支持的 Xilinx® 或 Intel ® 板卡 | 自定义板卡

此参数是只读的。要选择硬件板并配置板参数，请参阅 Hardware Implementation Pane。

### **View DIP switches location** — 查看 DIP 开关按钮

要查看显示所选硬件板上 DIP 开关位置的图，请点击 **View DIP switches location** 按钮。

仅当您选择特定的 Xilinx 或 Intel 板卡时，此按钮才启用。有关这些板卡的详细信息，请参阅 Supported Third-Party Tools and Hardware。

### **IO logic** — IO 逻辑指示器 `None`（默认） | `Active High` | `Active Low`

此参数是只读的。指示所选硬件板上的 IO 逻辑电平。

当 **IO logic** 参数显示为 **Active Low** 时，如果将 **Specify DIP switches via** 参数设置为 `InputPort`，则 DIP Switch 模块接受并输出低电平有效信号；如果将 **Specify DIP switches via** 参数设置为 `Dialog`，则输出低电平有效信号。该模块将这些端口名称表示为以字母 *n* 为前缀。例如，**nDS1**。

### **Specify DIP switches via** — DIP 开关源 `Dialog`（默认） | `InputPort`

要使用模块参数控制硬件逻辑，请选择 `Dialog`。要从输入端口控制硬件逻辑，请选择 `InputPort`。

### **Number of DIP switches** — DIP 开关选择 `1`（默认） | 范围 [1, n] 内的整数列表

要指定所需的 DIP 开关端口数量，请从 **Number of DIP switches** 列表中选择一个值。*`n`* 表示指定硬件板上可用的 DIP 开关数量。例如，如果从列表中选择 `3`，则该模块显示三个 DIP 开关端口。

要仅使用第 *`n`* 个 DIP 开关，请将 **Number of DIP switches** 参数设置为 *`n`*，并终止未使用的 DIP 开关端口。

### **DS*`n`*** — 选定的 DIP 开关 `Off`（默认） | `On`

要启用第 *`n`* 个 DIP 开关端口，请为 DS*`n`* 参数选择 `On`。*`n`* 表示指定硬件板上可用的 DIP 开关数量。

#### 依赖关系

要启用此参数，请将 **Specify push buttons via** 参数设置为 `Dialog`。

### **Sample time** — 系统采样时间 `-1`（默认） | 正标量

指定 DIP 开关在 `On` 和 `Off` 之间切换的时间间隔。

## 所属库

SoC Blockset / Hardware Logic I/O

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要自动为您的设计生成 HDL 代码，并在 SoC 设备上执行，请使用 **SoC Builder** 工具。请参阅 Use SoC Builder to Generate SoC Design。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2019a 中引入**

## 描述

连接硬件板上连接到 DIP 开关的信号

DIP Switch 模块控制硬件逻辑。连接到 DIP Switch 模块的硬件逻辑信号等效于连接到硬件板上双列直插式封装 (DIP) 开关的信号。
