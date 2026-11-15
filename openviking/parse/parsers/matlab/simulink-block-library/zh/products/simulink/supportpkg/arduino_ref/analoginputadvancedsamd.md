---
type: simulink-block
title: 'Analog Input SAMD'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / System Peripherals'
documentation_page: 'analoginputadvancedsamd'
documentation_source_path: 'supportpkg/arduino_ref/analoginputadvancedsamd.html'
language: zh-CN
chinese_source: worker-translation
---

# Analog Input SAMD

## 端口

### 输出

### **ADC\_Ch1(A0)** — ADC 输出数据标量

该模块输出从 Arduino 板的模拟输入引脚接收到的、经数字转换后的电压数据。输出端口数量取决于您在 **模拟输入引脚数** 参数中指定的模拟输入引脚数量。
例如，如果您将 **模拟输入引脚数** 参数设置为 `3`，该模块将启用三个输出端口，端口名称为 **ADC\_Ch1(A0)**、**ADC\_Ch2(A1)** 和 **ADC\_Ch3(A2)**。

**数据类型：** `double`

## 参数

### **模拟输入引脚数** — 选择模拟输入数量 `1`（默认） | `2` | `3`

选择用于模数转换的输入数量。

### **引脚编号 1** — Arduino 引脚编号 `0`（默认） | Arduino 板引脚编号

输入 Arduino 板的模拟输入引脚编号。要打开 Arduino 引脚映射表，请点击 **查看引脚映射**。要了解如何为 Analog Input 模块分配引脚，请参阅 Arduino 定时器独立模块的引脚映射。

**引脚编号** 参数的数量取决于您在 **模拟输入引脚数** 参数中指定的模拟输入引脚数量。例如，如果您将 **模拟输入引脚数** 参数设置为 `3`，该模块将启用 **引脚编号 2** 和 **引脚编号 3** 参数。您可以相应地输入 Arduino 板的模拟引脚编号。

### **启用转换结束中断** — 在 ADC 转换完成后使能中断 `on`（默认） | `off`

选择此选项以在 Arduino 硬件引脚处的模拟电压转换为等效数字电压之后生成中断。

## 所属库

Simulink Support Package for Arduino Hardware / Advanced / SAMD

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

## 描述

在 Arduino SAMD21 内核的模拟引脚上完成 ADC 转换后读取 ADC 寄存器值

使用 Analog Input 模块在 Arduino® SAMD21 模拟引脚上完成模数转换后，从 ADC 寄存器读取值。您可以使用该模块同时读取最多三个模拟电压输出。

在基于中断服务例程 (ISR) 触发执行 ADC 转换操作的下游函数调用子系统中使用该模块。您可以使用 Hardware Interrupt 模块指定 ISR 触发。

**注意**

Analog Input 模块支持 C/C++ 代码生成。此功能允许您使用 Embedded Coder® 生成 C 和 C++ 代码。

### 支持的 Arduino 板

- Arduino MKR 1000
- Arduino MKR ZERO
- Arduino MKR Wi-Fi® 1010
- Arduino Nano 33 IoT
