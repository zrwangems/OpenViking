---
type: simulink-block
title: 'SPI Controller Transfer'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2802x'
documentation_page: 'spicontrollertransfer'
documentation_source_path: '../simulink/supportpkg/raspberrypi_ref/spicontrollertransfer.html'
language: zh-CN
chinese_source: worker-translation
---

# SPI Controller Transfer

## 端口

### 输入

### **Port\_1** — 向 SPI 外设写入数据的输入端口 [Nx1] 或 [1xN] 数组

该输入端口用于接收模块向外设写入的一维数值数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### 输出

### **Port\_1** — 从 SPI 外设设备读取数据的输出端口 [Nx1] 数组

该输出端口用于接收模块从 SPI 外设设备读取的数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **Board** — 用于 SPI 通信的特定开发板 `Pi 2 Model B`（默认）| `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Pi 4 Model B` | `Pi Zero 2 W` | `Compute Module 4` | `Pi 5 Model`

选择您正在使用的特定开发板。更改开发板会更新可用的引脚选项。

### **Chip select pin** — SPI 外设设备所连接的片选引脚 `SPI0_CE0`（默认）| `SPI0_CE1` | `SPI1_CE0` | `SPI1_CE1` | `SPI1_CE2`

选择 Raspberry Pi® 开发板上 SPI 外设设备所连接的引脚编号。

要在 Raspberry Pi 硬件上启用辅助 SPI 总线，请按照启用 Raspberry Pi 硬件辅助 SPI 总线中所述的步骤操作。

### **Mode (Clock polarity and phase)** — SPI 通信模式 0（默认）| 1 | 2 | 3

选择 SPI 通信的模式。

有关模式的更多信息，请参阅 SPI 传输模式

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2017a 中引入**

## 描述

向 SPI 外设设备写入数据并从 SPI 外设设备读取数据

向 SPI 外设设备写入数据并从 SPI 外设设备读取数据。要打开 Raspberry Pi 开发板的引脚映射图，请点击 **View pin map** 按钮。

有关 SPI 通信的更多信息，请参阅支持 SPI 通信和 Raspberry Pi SPI 接口
