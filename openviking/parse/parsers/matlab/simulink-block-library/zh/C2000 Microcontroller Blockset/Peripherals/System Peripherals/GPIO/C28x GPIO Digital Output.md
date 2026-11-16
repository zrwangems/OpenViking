---
type: simulink-block
title: 'C28x GPIO Digital Output'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / System Peripherals / GPIO'
documentation_page: 'gpiodigitaloutput'
documentation_source_path: 'ref/gpiodigitaloutput.html'
language: zh-CN
chinese_source: official
---

# C28x GPIO Digital Output

## 端口

### 输入

### **Input** — 设置 GPIO 引脚状态 标量 | 向量

用于设置 GPIO 引脚状态的输入端口。

## 参数

### **GPIO 组** — 您要配置的 GPIO 引脚 **GPIO0-GPIO7** (默认) | **GPIO8-GPIO15****GPIO16-GPIO23****…**

选择要查看或配置的 GPIO 引脚组。有关 GPIO 引脚和外设的表格，请参阅 Texas Instruments针对您特定目标的文档。

### **输出的 GPIO 引脚** — 您要配置的 GPIO 引脚 **GPIO0** (默认) | **GPIO8****GPIO16****…**

要将 GPIO 引脚配置为数字输出，请选中其旁边的复选框。请参考该模块，以获取每个引脚可用的所有外设的表。

当模块输入端的值为 True 时，选定的 GPIO 引脚将被驱动为高电平。当模块输入端的值为 False 时，选定的 GPIO 引脚将接地。

### **Toggle GPIO#** — 您要配置的 GPIO 引脚 **Toggle GPIO0** (默认) | **Toggle GPIO1****…**

对于选定的每个输出引脚，您可以选择切换该引脚的信号。在**切换**模式下，模块输入端的 `True` 值会切换 GPIO 引脚的输出电平。因此，如果 GPIO 引脚处于**切换**模式，输入值为 `True`，则引脚输出电平为低。如果 GPIO 引脚处于低电平（**切换**模式），且模块的输入值为 `True`，则该引脚的输出电平也会被拉高。如果模块的输入为 `False`，则 GPIO 引脚输出电平不受影响。

**注意**

该模块的输出可以向量化。

## 所属库

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M35x / M3 C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28M36x / M3 C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x C2000 Microcontroller Blockset / F29H85x Simulink Support Package for Arduino Hardware / Common

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2016a 中推出**

## 描述

将通用输入/输出引脚配置为数字输出

该模块配置通用 I/O (GPIO) MUX 寄存器，用于控制 GPIO 共享引脚的数字输入操作。每个 I/O 端口都有一个 MUX 寄存器，用于选择外设操作或数字 I/O 操作（默认）。当一个引脚配置为数字输入时，它将无法用于数字输出或外设操作。您可以为各个数字输入引脚配置 **Input qualification type**。要进行配置，请转到 **Configuration Parameters > Hardware Implementation > Target Hardware Resources** 并选择相应的 GPIO 组。

每个处理器可用的 GPIO 引脚数量都不同。

**注意**

为避免丢失新设置，请在更改 **GPIO Group** 参数之前点击**应用**。
