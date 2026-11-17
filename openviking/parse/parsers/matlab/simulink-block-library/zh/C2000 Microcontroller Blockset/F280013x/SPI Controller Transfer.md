---
type: simulink-block
title: 'SPI Controller Transfer'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2833x'
documentation_page: 'spicontrollertransferblock'
documentation_source_path: '../ecoder/stmicroelectronicsstm32f4discovery/ref/spicontrollertransferblock.html'
language: zh-CN
chinese_source: worker-translation
---

# SPI Controller Transfer

## 端口
```yaml
ports:
- name: SDO
  summary: 要写入 SPI 外设设备寄存器向量的数据
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: SDI
  summary: 从 SPI 外设设备寄存器向量读取的数据
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
```

### 输入

### **SDO** — 要写入 SPI 外设设备寄存器向量的数据

该端口接受串行数据输出（SDO），用于通过 SPI 接口写入外设设备的寄存器。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### 输出

### **SDI** — 从 SPI 外设设备寄存器向量读取的数据

该端口输出通过 SPI 接口从外设设备寄存器读取的数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
## 参数
```yaml
parameters:
- name: SPI module
  summary: 用于写入和读取数据的 SPI 模块 0（默认值）
  group: 主要
- name: Chip select pin
  summary: 连接到 SPI 外设设备的引脚
  group: 主要
- name: First bit to transfer
  summary: SPI 通信中首先传输的位 Most significant bit (MSB)（默认值） | Least significant bit (LSB)
  group: 主要
- name: Mode (Clock polarity and phase)
  summary: SPI 通信模式 0（默认值） | 1 | 2 | 3
  group: 主要
- name: Chip select pin polarity
  summary: 建立 SPI 通信的逻辑电平 Active low（默认值） | Active high
  group: 高级
```

### 主要

### **SPI module** — 用于写入和读取数据的 SPI 模块 `0`（默认值）

指定 SPI 外设设备所连接的 SPI 模块。

### **Chip select pin** — 连接到 SPI 外设设备的引脚

指定板上 SPI 外设设备所连接的引脚名称。SPI 控制器将所选外设设备的 SS 引脚拉低（0）以开始通信。外设设备的选择取决于您在 **Chip select pin polarity** 参数中指定的引脚极性。控制器一次只能选择一个外设设备。

### **First bit to transfer** — SPI 通信中首先传输的位 `Most significant bit (MSB)`（默认值） | `Least significant bit (LSB)`

选择数据传输的顺序。

- Most significant bit (MSB) — 选择 MSB 以首先发送最高有效位（MSB）。
- Least significant bit (LSB) — 选择 LSB 以首先发送最低有效位（LSB）。

### **Mode (Clock polarity and phase)** — SPI 通信模式 `0`（默认值） | `1` | `2` | `3`

SPI 控制器设置时钟极性（CPOL）和时钟相位（CPHA）。

极性和相位的组合称为 SPI 模式。SPI 模式 0–3 如下表所示。

| 模式 | 时钟极性（CPOL） | 时钟相位（CPHA） |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 2 | 1 | 0 |
| 3 | 1 | 1 |

有关寄存器读/写的更多信息，请参阅 SPI Transfer Modes。

### 高级

### **Chip select pin polarity** — 建立 SPI 通信的逻辑电平 `Active low`（默认值） | `Active high`

Chip select pin 支持用于选择 SPI 外设设备的逻辑电平。

- Active low — 设备在逻辑低电平时使能。当 SPI 外设设备的 SS 引脚设置为低电平时，该设备被使能。
- Active high — 设备在逻辑高电平时使能。当 SPI 外设设备的 SS 引脚设置为高电平时，该设备被使能。
## 所属库

Embedded Coder Support Package for STMicroelectronics Discovery Boards / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics Discovery Boards / STM32F746G-Discovery

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018a 中引入**

## 描述

向 SPI 外设设备写入数据并从其读取数据

SPI Controller Transfer 模块通过串行外设接口（SPI）接口向外设设备写入数据并从其读取数据。该模块输出的数组大小和数据类型与输入值相同。您可以将此模块与 Byte Pack 和 Byte Unpack 模块配合使用，以支持异构数据类型传输。

使用此模块，您可以访问 SPI 设备以测量温度、压力等物理量。

有关 SPI 通信的更多信息，请参阅 Support SPI Communication。
