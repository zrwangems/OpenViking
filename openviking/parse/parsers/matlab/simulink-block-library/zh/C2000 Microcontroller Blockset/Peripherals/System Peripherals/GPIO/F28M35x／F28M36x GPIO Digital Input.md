---
type: simulink-block
title: 'F28M35x/F28M36x GPIO Digital Input'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / System Peripherals / GPIO'
documentation_page: 'f28m35xf28m36xgpiodigitalinput'
documentation_source_path: 'ref/f28m35xf28m36xgpiodigitalinput.html'
language: zh-CN
chinese_source: worker-translation
---

# F28M35x/F28M36x GPIO Digital Input

## 端口

### 输出

### **Pin #** — GPIO 引脚状态标量 | 向量

此端口输出你在 **Pin number** 参数中选择的数字引脚的状态。

**数据类型：** `Boolean`

## 参数

### **GPIO port** — 用于读取 GPIO 引脚状态的端口 `GPIOA` (默认) | `GPIOB``GPIOC``…`

选择一个 GPIO 端口以获取 GPIO 引脚状态。

### **Pin number** — 你希望读取其状态的 GPIO 引脚 `Pin 0` (默认) | `Pin 1` | `Pin 2` | `...`

选择你希望读取其状态的 GPIO 引脚的引脚编号。

### **Sample time** — 模块读取输入引脚值的频率 `-1` (默认) | `0.1`

指定模块接收消息的频率，以秒为单位。将此参数指定为 -1 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M35x / M3 C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28M36x / M3 C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x C2000 Microcontroller Blockset / F29H85x Simulink Support Package for Arduino Hardware / Common

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2016a 中引入**

## 描述

读取配置为输入的 GPIO 引脚的逻辑值

读取已配置的 GPIO 引脚的逻辑值。

此模块配置通用 I/O (GPIO) MUX 寄存器，这些寄存器控制用于数字输入的 GPIO 共享引脚的操作。每个 I/O 端口都有一个 MUX 寄存器，用于选择外设操作或数字 I/O 操作（默认）。当某个引脚配置为数字输入时，不能将同一个引脚用于数字输出或外设操作。你可以为各个数字输入引脚配置上拉和开漏选项。要进行配置，请转到 **Configuration Parameters > Hardware Implementation > Target Hardware Resources**，并选择相应的 GPIO 组。
