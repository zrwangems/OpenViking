---
type: simulink-block
title: 'SPI Register Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / Communication'
documentation_page: 'spiregisterread'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/spiregisterread.html'
language: zh-CN
chinese_source: worker-translation
---

# SPI Register Read

## 端口

### 输出

### **SDI** — 从 SPI 外设设备寄存器读取的数据向量

该端口输出通过 SPI 接口从外设设备寄存器读取的数据。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

## 参数

### 主要

### **SPI 模块** — 用于读取数据的 SPI 模块 `0` (default)

指定 SPI 外设设备连接到的 SPI 模块。

### **片选引脚** — 连接到 SPI 外设设备的引脚 `D7`

指定板上连接到 SPI 外设设备的引脚名称。SPI 控制器将所选外设的 SS 引脚拉低 (0) 以开始通信。根据您在 **片选引脚极性** 参数中指定的引脚极性来选择外设。控制器一次只能选择一个外设。

### **要传输的第一位** — SPI 通信要传输的第一位 `Most significant bit (MSB)` (default) | `Least significant bit (LSB)`

选择数据传输的顺序。

- Most significant bit (MSB) — 选择 MSB 以先发送最高有效位 (MSB)。
- Least significant bit (LSB) — 选择 LSB 以先发送最低有效位 (LSB)。

### **模式（时钟极性和相位）** — SPI 通信模式 `0` (default) | `1` | `2` | `3`

SPI 控制器设置时钟极性 (CPOL) 和时钟相位 (CPHA)。

极性和相位的组合称为 SPI 模式。SPI 模式 0–3 如表所示。

| 模式 | 时钟极性 (CPOL) | 时钟相位 (CPHA) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 2 | 1 | 0 |
| 3 | 1 | 1 |

有关寄存器读/写的更多信息，请参阅 SPI Transfer Modes。

### **寄存器地址** — 要读取数据的 SPI 外设寄存器地址 `0` (default)

使用整数或通过 `hex2dec()` 以十六进制格式指定此地址，例如，‘hex2dec(‘20’)’。

### **输出数据类型** — 从 SPI 外设设备读取的数据的数据类型 `int8` (default) | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

指定从 SPI 外设设备寄存器读取的数据类型。

### **输出数据长度** — 要从 SPI 外设设备读取的数据大小 `1` (default) | `integer greater than or equal to 0`

指定从 SPI 外设设备寄存器读取的数据长度。

### **采样时间** — 从 SPI 外设设备读取数据的频率 `0.1` (default)

指定该模块从 SPI 外设设备读取数据的频率。当您将此参数指定为`-1`时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

### 高级

### **片选引脚极性** — 建立 SPI 通信的逻辑电平 `Active low` (default) | `Active high`

片选引脚支持用于选择 SPI 外设设备的逻辑电平。

- Active low — 器件在逻辑低电平时启用。当 SPI 外设设备的 SS 引脚设为低电平时，该外设设备启用。
- Active high — 器件在逻辑高电平时启用。当 SPI 外设设备的 SS 引脚设为高电平时，该外设设备启用。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

从 SPI 外设设备寄存器读取数据

SPI Register Read 模块通过串行外设接口 (SPI) 接口从外设设备的寄存器读取数据。使用此模块，您可以访问 SPI 设备以测量温度、压力等量，或支持 EEPROM。

有关 SPI 通信的更多信息，请参阅 Support SPI Communication。
