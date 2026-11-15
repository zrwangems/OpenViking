---
type: simulink-block
title: 'SPI Controller Transfer'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Communication'
documentation_page: 'spicontrollertransfer'
documentation_source_path: 'supportpkg/raspberrypi_ref/spicontrollertransfer.html'
language: zh-CN
chinese_source: worker-translation
---

# SPI Controller Transfer

## 端口

### 输入

### **Port\_1** — 用于将数据写入 SPI 外设的输入端口 [Nx1] 或 [1xN] 数组

输入端口，模块通过该端口接受一维数值数组以写入外设设备。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### 输出

### **Port\_1** — 用于从 SPI 外设设备读取数据的输出端口 [Nx1] 数组

输出端口，模块通过该端口从 SPI 外设设备接收数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **Board** — 用于 SPI 通信的特定开发板 `Pi 2 Model B`（默认） | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Pi 4 Model B` | `Pi Zero 2 W` | `Compute Module 4` | `Pi 5 Model`

选择您正在使用的特定开发板。更改开发板会更新您获得的引脚选项。

### **Chip select pin** — SPI 外设设备连接到的片选引脚 `SPI0_CE0`（默认） | `SPI0_CE1` | `SPI1_CE0` | `SPI1_CE1` | `SPI1_CE2`

选择 SPI 外设设备连接到的 Raspberry Pi® 开发板上的引脚编号。

要启用 Raspberry Pi 硬件上的辅助 SPI 总线，请按照“启用 Raspberry Pi 硬件的辅助 SPI 总线”中提到的步骤操作。

### **Mode (Clock polarity and phase)** — SPI 通信模式 0（默认） | 1 | 2 | 3

选择 SPI 通信模式。

有关模式的详细信息，请参阅 SPI 传输模式

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

向 SPI 外设设备写入数据并从 SPI 外设设备读取数据。要打开 Raspberry Pi 开发板的引脚映射，请点击 **View pin map** 按钮。

有关 SPI 通信的详细信息，请参阅支持 SPI 通信和 Raspberry Pi SPI 接口
