---
type: simulink-block
title: 'SPI Register Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Communication'
documentation_page: 'spiregisterread'
documentation_source_path: 'supportpkg/raspberrypi_ref/spiregisterread.html'
language: zh-CN
chinese_source: worker-translation
---

# SPI Register Read

## 端口

### 输出

### **Port\_1** — 用于读取数据的输出端口 [Nx1] 数组

此端口是用于从 SPI 外设寄存器读取数据的输出端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **Board** — 用于 SPI 通信的特定板卡 `Pi 2 Model B` (默认) | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Pi 4 Model B` | `Pi Zero 2 W` | `Compute Module 4` | `Pi 5 Model`

选择您正在使用的特定板卡。更改板卡会更新您可以获得的引脚选项。

### **Chip select pin** — 连接到 SPI 外设设备的引脚 `SPI0_CE0` (默认) | `SPI0_CE1` | `SPI1_CE0` | `SPI1_CE1` | `SPI1_CE2`

选择 Raspberry Pi 板上 SPI 外设设备所连接的引脚编号。

要在您的 Raspberry Pi® 硬件上启用次级 SPI 总线，请按照 Enable Secondary SPI Bus of Raspberry Pi Hardware 中提到的步骤操作。

### **Mode (Clock polarity and phase)** — SPI 通信模式 0 (默认) | 1 | 2 | 3

选择 SPI 通信模式。

### **Register address** — 用于读取数据的寄存器地址 0 (默认) | uint8 数组

输入要读取数据的 SPI 外设寄存器地址。

### **Output data type** — 输出的数据类型 int8 (默认) | uint8 | int16 | uint16 | int32 | uint32 | single | double

选择用于 SPI 通信的数据类型。

### **Output data length** — SPI 通信的数据长度 1 (默认) | 标量

输入要从 SPI 外设寄存器读取的所选数据类型的输出数据长度。

### **Sample time** — 模块从 SPI 外设设备读取数据的时间间隔 `0.1` (默认) | `-1` | 任意非负值

指定此模块从 SPI 外设设备读取数据的时间间隔，以 seconds 为单位。当您将此参数设置为 `-1` 时，Simulink® 将根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Communication

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2017a 中引入**

## 描述

从 SPI 外设设备寄存器读取数据

SPI Register Read 模块发起从 SPI 外设寄存器读取的 SPI 读操作。您可以指定数据类型和数据长度，以从外设寄存器获取数据。要打开 Raspberry Pi 板的引脚映射，请点击 **View pin map** 按钮。

有关 SPI 通信的更多信息，请参阅 Support SPI Communication 和 Raspberry Pi SPI Interface
