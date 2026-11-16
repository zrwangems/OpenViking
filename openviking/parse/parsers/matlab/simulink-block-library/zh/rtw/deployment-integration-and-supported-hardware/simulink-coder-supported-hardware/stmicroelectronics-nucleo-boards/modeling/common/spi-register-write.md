---
type: simulink-block
title: 'SPI Register Write'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Common'
documentation_page: 'spiregisterwrite'
documentation_source_path: 'nucleo/ref/spiregisterwrite.html'
language: zh-CN
chinese_source: official
---

# SPI Register Write

## 端口

### 输入

### **SDO** — 要写入 SPI 外围设备寄存器的数据 向量

端口接受通过 SPI 接口写入外围设备寄存器的串行数据输出 (SDO)。

**数据类型:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

## 参数

### 主要

### **SPI 模块** — 用于写入数据的 SPI 模块 `0` (默认)

指定 SPI 外围设备连接到的 SPI 模块。

### **片选引脚** — 连接到 SPI 外围设备的引脚 `D7`

指定板上 SPI 外围设备连接到的引脚名称。SPI 控制器将选定外设的 SS 引脚拉至低 (0) 值以开始通信。外设是根据您在**片选引脚极性**参数中指定的引脚极性来选择的。控制器一次只能选择一个外设。

### **要传输的首位** — SPI 通信中要传输的首位 **最高有效位(MSB)** (默认) | **最低有效位(LSB)**

选择数据传输的顺序。

- 最高有效位 (MSB) - 选择 MSB 将首先发送最高有效位。
- 最低有效位 (LSB) - 选择 LSB 将首先发送最低有效位。

### **模式(时钟极性和相位)** — SPI 通信的模式 **0** (默认) | **1** | **2** | **3**

SPI 控制器设置时钟极性 (CPOL) 和时钟相位 (CPHA)。

极性和相位的组合称为 SPI 模式。SPI 模式 0-3 如下表所示。

| 模式 | 时钟极性 (CPOL) | 时钟相位 (CPHA) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 2 | 1 | 0 |
| 3 | 1 | 1 |

有关寄存器读/写的详细信息，请参阅 SPI 传输模式。

### **寄存器地址** — 要写入数据的 SPI 外设寄存器地址 `0` (默认)

使用 `hex2dec()` 将此地址指定为整数或十六进制格式，例如，hex2dec(‘20’)。

### 高级

### **片选引脚极性** — 建立 SPI 通信的逻辑电平 **低电平有效** (默认) | **高电平有效**

片选引脚支持的用于选择 SPI 外围设备的逻辑电平。

- 低电平有效 - 设备在逻辑低电平时启用。SPI 外围设备在其 SS 引脚设置为低电平时启用。
- 高电平有效 - 设备在逻辑高电平时启用。SPI 外围设备在其 SS 引脚设置为高电平时启用。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2018a 中推出**

## 描述

向 SPI 外围设备寄存器写入数据

SPI Register Write 模块通过串行外设接口 (SPI) 将数据写入外围设备的寄存器。使用此模块，您可以访问 SPI 设备以测量温度、压力等量或支持 EEPROM。

有关 SPI 通信的详细信息，请参阅支持 SPI 通信。
