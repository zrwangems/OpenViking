---
type: simulink-block
title: 'SPI Register Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / Communication'
documentation_page: 'spiregisterwrite'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/spiregisterwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# SPI Register Write

## 端口

### 输入

### **SDO** — 要写入 SPI 外设设备寄存器中的数据向量

该端口接受串行数据输出（SDO），用于通过 SPI 接口将数据写入外设设备的寄存器。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

## 参数

### 主要

### **SPI 模块** — 要写入数据的 SPI 模块 `0`（默认）

指定 SPI 外设设备连接到的 SPI 模块。

### **片选引脚** — 连接到 SPI 外设设备的引脚 `D7`

指定板上 SPI 外设设备连接到的引脚名称。SPI 控制器将所选外设的 SS 引脚拉低 (0) 以启动通信。外设的选择取决于你在 **片选引脚极性** 参数中指定的引脚极性。控制器一次只能选择一个外设。

### **要传输的第一位** — 用于 SPI 通信的第一位 `Most significant bit (MSB)`（默认）| `Least significant bit (LSB)`

选择数据传输的顺序。

- Most significant bit (MSB) — 选择 MSB 以首先发送最高有效位（MSB）。
- Least significant bit (LSB) — 选择 LSB 以首先发送最低有效位（LSB）。

### **模式（时钟极性和相位）** — SPI 通信模式 `0`（默认）| `1` | `2` | `3`

SPI 控制器设置时钟极性 (CPOL) 和时钟相位 (CPHA)。

极性和相位的组合称为 SPI 模式。SPI 模式 0–3 如表所示。

| 模式 | 时钟极性 (CPOL) | 时钟相位 (CPHA) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 2 | 1 | 0 |
| 3 | 1 | 1 |

有关寄存器读/写的详细信息，请参阅 SPI 传输模式。

### **寄存器地址** — 要写入数据的 SPI 外设寄存器地址 `0`（默认）

指定此地址为整数，或通过使用 `hex2dec()` 以十六进制格式指定，例如，‘hex2dec(‘20’)’。

### 高级

### **片选引脚极性** — 用于建立 SPI 通信的逻辑电平 `Active low`（默认）| `Active high`

片选引脚支持用于选择 SPI 外设设备的逻辑电平。

- Active low — 设备在逻辑低电平时使能。当其 SS 引脚设置为低电平时，SPI 外设设备使能。
- Active high — 设备在逻辑高电平时使能。当其 SS 引脚设置为高电平时，SPI 外设设备使能。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

将数据写入 SPI 外设设备的寄存器

SPI Register Write 模块通过串行外设接口 (SPI) 将数据写入外设设备的寄存器。使用此模块，你可以访问 SPI 设备以测量温度、压力等量，或支持 EEPROM。

有关 SPI 通信的详细信息，请参阅支持 SPI 通信。
