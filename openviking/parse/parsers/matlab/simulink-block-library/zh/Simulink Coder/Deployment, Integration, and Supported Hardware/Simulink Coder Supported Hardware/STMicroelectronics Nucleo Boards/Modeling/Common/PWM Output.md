---
type: simulink-block
title: 'PWM Output'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Common'
documentation_page: 'pwmoutput'
documentation_source_path: 'nucleo/ref/pwmoutput.html'
language: zh-CN
chinese_source: official
---

# PWM Output

## 端口

### 输入

### **Port\_1** — 占空比值 标量

有效输入值的范围是 `0` - `–100`。输入控制方形波形的占空比（方波的宽度）。

输入值 `0` 产生 0% 占空比，输入值 `100` 产生 100% 占空比。任何超出范围的值，例如 `500` 或 `-500`，在模块输入端口上具有与最大或最小输入值相同的效果。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **引脚** — 模块在其上生成 PWM 信号的引脚

要查看板上的引脚映射，请点击**查看引脚映射**。

确保为模型中的不同模块分配不同引脚名称。

除了引脚映射表中提到的引脚名称外，还有其他备用引脚名称 `(Px_y_ALTz)`，可用于访问连接到同一引脚的其他硬件外围设备。要了解详细信息，请参考Usage of Alternate Pin Names。

备用引脚名称仅适用于 Simulink® Coder™ Support Package for STMicroelectronics® Nucleo Boards and Discovery boards。

### **初始频率(Hz)** — PWM 波形的初始频率 `2000` (默认)

指定 PWM 波形的初始频率。

### **初始占空比(0 - 100)** — PWM 引脚上方波的初始宽度 `50` (默认) | `integer between 0 and 100`

指定介于 `0` - `100` 之间的初始占空比。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2018a 中推出**

## 描述

在指定输出引脚上生成方波

PWM Output 模块在指定输出引脚上生成方形波形。模块输入控制方形波形的占空比。您可以提供介于 `0` - `100` 之间的值作为模块输入。输入值 0 产生 0% 占空比，输入值 100 产生 100% 占空比
