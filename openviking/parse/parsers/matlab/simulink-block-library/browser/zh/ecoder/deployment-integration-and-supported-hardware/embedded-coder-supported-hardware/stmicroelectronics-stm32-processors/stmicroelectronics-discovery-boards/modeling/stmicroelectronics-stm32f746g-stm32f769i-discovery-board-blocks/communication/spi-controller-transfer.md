---
type: simulink-block
title: 'SPI Controller Transfer'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / Communication'
documentation_page: 'spicontrollertransferblock'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/spicontrollertransferblock.html'
language: zh-CN
chinese_source: worker-translation
---

# SPI Controller Transfer

## 端口

### 输入

### **SDO** — 要写入 SPI 外设寄存器的数据向量

该端口接受串行数据输出 (SDO)，以通过 SPI 接口写入外设的寄存器。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### 输出

### **SDI** — 从 SPI 外设寄存器读取的数据向量

该端口输出通过 SPI 接口从外设的寄存器读取的数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### 主要

### **SPI 模块** — 用于写入和读取数据的 SPI 模块 `0`（默认）

指定 SPI 外设所连接的 SPI 模块。

### **芯片选择引脚** — 连接到 SPI 外设的引脚

指定板卡上 SPI 外设所连接的引脚名称。SPI 控制器将所选外设的 SS 引脚拉低 (0) 以开始通信。根据您在 **芯片选择引脚极性** 参数中指定的引脚极性来选择外设。控制器一次只能选择一个外设。

### **要传输的第一个位** — SPI 通信中要传输的第一个位 `Most significant bit (MSB)`（默认） | `Least significant bit (LSB)`

选择数据传输的顺序。

- Most significant bit (MSB) — 选择 MSB 以先发送最高有效位 (MSB)。
- Least significant bit (LSB) — 选择 LSB 以先发送最低有效位 (LSB)。

### **模式（时钟极性和相位）** — SPI 通信模式 `0`（默认） | `1` | `2` | `3`

SPI 控制器设置时钟极性 (CPOL) 和时钟相位 (CPHA)。

极性和相位的组合称为 SPI 模式。SPI 模式 0–3 如下表所示。

| 模式 | 时钟极性 (CPOL) | 时钟相位 (CPHA) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 2 | 1 | 0 |
| 3 | 1 | 1 |

有关寄存器读/写的详细信息，请参阅 SPI 传输模式。

### 高级

### **芯片选择引脚极性** — 建立 SPI 通信的逻辑电平 `Active low`（默认） | `Active high`

芯片选择引脚支持用于选择 SPI 外设的逻辑电平。

- Active low — 设备在逻辑低电平时启用。当 SPI 外设的 SS 引脚设置为低电平时，该外设启用。
- Active high — 设备在逻辑高电平时启用。当 SPI 外设的 SS 引脚设置为高电平时，该外设启用。

## 所属库

Embedded Coder Support Package for STMicroelectronics Discovery Boards / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics Discovery Boards / STM32F746G-Discovery

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2018a 中引入**

## 描述

将数据写入 SPI 外设并从 SPI 外设读取数据

SPI controller Transfer 模块通过串行外设接口 (SPI) 接口将数据写入外设并从外设读取数据。该模块输出与输入值大小和数据类型相同的数组。您可以将此模块与 Byte Pack 和 Byte Unpack 模块一起使用，以支持异构数据类型传输。

使用此模块，您可以访问 SPI 设备以测量温度、压力等量。

有关 SPI 通信的详细信息，请参阅支持 SPI 通信。
