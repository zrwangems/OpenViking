---
type: simulink-block
title: 'SPI Register Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Communication'
documentation_page: 'spiregisterwrite'
documentation_source_path: 'supportpkg/raspberrypi_ref/spiregisterwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# SPI Register Write

## 端口

### 输入

### **Port\_1** — 用于接受数据 [Nx1] 或 [1xN] 数组的输入端口

用于接受要写入 SPI 外设寄存器的数据的输入端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### **Board** — 用于通信的 SPI 模块 `Pi 2 Model B`（默认）| `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Pi 4 Model B` | `Pi Zero 2 W` | `Compute Module 4` | `Pi 5 Model`

选择您正在使用的特定板卡。更改板卡会更新您获得的引脚选项。

### **片选引脚** — 连接到 SPI 外设设备的引脚 `SPI0_CE0`（默认）| `SPI0_CE1` | `SPI1_CE0` | `SPI1_CE1` | `SPI1_CE2`

选择 Raspberry Pi 板上 SPI 外设设备所连接的引脚编号。

要在您的 Raspberry Pi® 硬件上启用辅助 SPI 总线，请按照“启用 Raspberry Pi 硬件的辅助 SPI 总线”中提到的步骤操作。

### **Mode（时钟极性和相位）** — SPI 通信模式 0（默认）| 1 | 2 | 3

选择 SPI 通信模式。

### **寄存器地址** — 要写入数据的寄存器地址 0（默认）| uint8 数组

输入要写入数据的外设寄存器地址。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Communication

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

未在 R2025b 中记录。

## 描述

将数据写入 SPI 外设设备的寄存器

SPI Register Write 模块将模块输入数据写入指定的寄存器地址。要打开 Raspberry Pi 板的引脚映射，请点击 **查看引脚映射** 按钮。

有关 SPI 通信的更多信息，请参阅支持 SPI 通信和 Raspberry Pi SPI 接口。
