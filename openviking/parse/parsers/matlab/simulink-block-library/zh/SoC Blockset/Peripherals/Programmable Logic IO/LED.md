---
type: simulink-block
title: 'LED'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Programmable Logic IO'
documentation_page: 'led'
documentation_source_path: 'ref/led.html'
language: zh-CN
chinese_source: worker-translation
---

# LED

## 端口

### 输入

### **LED*`x`*** — 输入信号 `Boolean` 标量

来自硬件逻辑的输入信号。每个 LED 都有一个端口，命名为
**LED1** 到 **LED*`x`***，
其中 *`x`* 是 **Number of LEDs**。

**数据类型：** `Boolean`

## 参数

### **Hardware board** — 查看所选硬件 `None`（默认） | 支持的 Xilinx® 或 Intel ® 板卡 | Custom boards

此参数为只读。要选择硬件板卡并配置板卡参数，请参阅 Hardware Implementation 窗格。

### **View LEDs location** — 查看 LED 按钮

要查看所选硬件板卡上 LED 位置的示意图，请点击
**View LEDs location** 按钮。

仅当选择特定的 Xilinx 或 Intel 板卡时，此按钮才启用。有关这些板卡的详细信息，请参阅支持的第三方工具和硬件。

### **IO logic** — IO 逻辑指示符 `None`（默认） | `Active High` | `Active Low`

此参数为只读。指示所选硬件板卡上的 IO 逻辑电平。

当 **IO logic** 参数显示为 **Active
Low** 时，LED 模块接受低电平有效信号，并表示端口名以字母 *n* 为前缀。例如，
**nLED1**。

### **Number of LEDs** — LED 端口数 `1`（默认） | [1, *n*] 范围内的整数列表

通过从此列表指定一个值，指定所需的 LED 端口数。
*`n`* 是指定硬件板卡上可用 LED 的数量。例如，如果将此参数设置为 `4`，则模块会显示四个 LED 端口。

要仅使用第 *`n`* 个 LED，请将 **Number of
LEDs** 参数设置为 *`n`*，并将未使用的 LED
端口保持未连接。

对于 Zynq®
UltraScale+™ RFSoC ZCU216 Evaluation Kit，前三个 LED 端口表示八组可用红色、绿色和蓝色（RGB）LED 中的第一组，接下来的三个
LED 端口表示第二组 RGB LED，依此类推。例如，如果将
**Number of LEDs** 参数设置为 `9`，则
**LED1**、**LED4** 和 **LED7**
端口连接到红色 LED，**LED2**、**LED5**
和 **LED8** 端口连接到绿色 LED，**LED3**、**LED6** 和 **LED9**
端口连接到 ZCU216 评估板上的蓝色 LED。

## 所属库

SoC Blockset / Hardware Logic I/O

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要为设计自动生成 HDL 代码，并在 SoC 器件上执行，请使用 **SoC Builder** 工具。请参阅使用 SoC Builder 生成 SoC 设计。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2019a 中引入**

## 描述

连接硬件板卡上 LED 所连接的信号

LED 模块指示信号的状态。连接到 LED 模块的硬件逻辑信号等效于连接到硬件板卡上发光二极管（LED）的信号。
