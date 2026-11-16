---
type: simulink-block
title: 'C28x GPIO Digital Input'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / System Peripherals / GPIO'
documentation_page: 'gpiodigitalinput'
documentation_source_path: 'ref/gpiodigitalinput.html'
language: zh-CN
chinese_source: official
---

# C28x GPIO Digital Input

## 端口

### 输出

### **Pin #** — GPIO 引脚状态 标量 | 向量

该端口输出您在 **GPIO Group** 参数中选择的数字引脚的状态。

## 参数

### **GPIO 组** — 您要配置的 GPIO 引脚 **GPIO0-GPIO7** (默认) | **GPIO8-GPIO15****GPIO16-GPIO23****…**

选择要查看或配置的 GPIO 引脚组。有关 GPIO 引脚和外设的表格，请参阅 Texas Instruments针对您特定目标的文档。

### **采样时间** — 模块读取输入引脚值的频率 `-1` (默认) | `0.1`

指定模块接收消息的频率（以秒为单位）。当您将此参数指定为 -1 时，Simulink 将根据模型中的模块上下文确定块的最佳采样时间。

有关更多信息，请参阅 指定采样时间 部分。

### **数据类型** — GPIO 输入的数据类型 **auto** (默认) | **unit8** | **双精度** | **单精度** | **int8** | **int16** | **uint16** | **int32** | **uint32** | **布尔**

指定输入数据的数据类型。输入被读取为 16 位整数，然后转换为选定的数据类型。

## 所属库

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M35x / M3 C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28M36x / M3 C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x C2000 Microcontroller Blockset / F29H85x Simulink Support Package for Arduino Hardware / Common

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2016a 中推出**

## 描述

将通用输入/输出引脚配置为数字输入

该模块配置通用 I/O (GPIO) MUX 寄存器，用于控制 GPIO 共享引脚的数字输入操作。每个 I/O 端口都有一个 MUX 寄存器，用于选择外设操作或数字 I/O 操作（默认）。当一个引脚配置为数字输入时，它将无法用于数字输出或外设操作。您可以为各个数字输入引脚配置 **Input qualification type**。要进行配置，请转到 **Configuration Parameters > Hardware Implementation > Target Hardware Resources** 并选择相应的 GPIO 组。

每个处理器可用的 GPIO 引脚数量都不同。

**注意**

为避免丢失新设置，请在更改 **GPIO Group** 参数之前点击**应用**。
