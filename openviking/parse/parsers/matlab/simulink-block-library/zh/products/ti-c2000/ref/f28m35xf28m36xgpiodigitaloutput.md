---
type: simulink-block
title: 'F28M35x/F28M36x GPIO Digital Output'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / System Peripherals / GPIO'
documentation_page: 'f28m35xf28m36xgpiodigitaloutput'
documentation_source_path: 'ref/f28m35xf28m36xgpiodigitaloutput.html'
language: zh-CN
chinese_source: worker-translation
---

# F28M35x/F28M36x GPIO Digital Output

## 端口

### 输入

### **Pin #** — GPIO 引脚状态 标量 | 向量

在此端口指定一个值，以设置 GPIO 引脚的状态。

**数据类型：** `Boolean`

## 参数

### **GPIO port** — 要写入 GPIO 引脚状态的端口 `GPIOA`（默认）| `GPIOB``GPIOC``…`

选择要将 GPIO 引脚状态写入的 GPIO 端口之一。

### **Pin number** — 要写入状态的 GPIO 引脚 `Pin 0`（默认）| `Pin 1` | `Pin 2` | `...`

选择要写入其状态的 GPIO 引脚的引脚编号。

### **Initially set GPIO pin** — 模型初始化期间的 GPIO 引脚状态 `on`（默认）| `off`

选择此选项以在模型初始化期间设置 GPIO 引脚状态。

## 所属库

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M35x / M3 C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28M36x / M3 C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x C2000 Microcontroller Blockset / F29H85x Simulink Support Package for Arduino Hardware / Common

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2016a 中引入**

## 描述

设置配置为输出的 GPIO 引脚的逻辑值

设置已配置的 GPIO 引脚的逻辑值。

配置各个通用输入/输出 (GPIO) 引脚以作为数字输出工作。当引脚配置为数字输出时，它不能作为数字输入工作，也不能连接到外设 I/O 信号。
