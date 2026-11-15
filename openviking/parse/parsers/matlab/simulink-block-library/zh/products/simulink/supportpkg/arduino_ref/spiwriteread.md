---
type: simulink-block
title: 'SPI WriteRead'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / SPI'
documentation_page: 'spiwriteread'
documentation_source_path: 'supportpkg/arduino_ref/spiwriteread.html'
language: zh-CN
chinese_source: worker-translation
---

# SPI WriteRead

## 端口

### 输入

### **Port\_1** — 用于将数据写入 SPI 外设的输入端口 [Nx1] 或 [1xN] 数组

该输入端口用于接收模块要向外部设备写入的一维值数组。

**数据类型：** `uint8` | `uint16` | `uint32`
### 输出

### **Port\_1** — 用于从 SPI 外设设备读取数据的输出端口 [Nx1] 数组

该输出端口用于从 SPI 外设设备接收数据。

**数据类型：** `uint8` | `uint16` | `uint32`

## 参数

### **SPI module** — SPI 通信模块 `0`（默认）| scalar

指定 Arduino 硬件上用于与 SPI 外设通信的 SPI 模块。有关 Arduino 引脚映射以及硬件板支持的模块的详细信息，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

### **Chip select (CS) pin** — SPI 外设设备连接到的片选引脚 10（默认）| 目标硬件引脚

输入 Arduino 板上 SPI 外设设备连接到的引脚编号。SPI 控制器将所选外设的 CS 引脚拉低（0）以启动通信。请参阅 Pin Mapping for Arduino Timer-Independent Blocks，了解不同 Arduino 板的 SS 引脚限制。

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

向 SPI 设备写入数据以及从 SPI 设备读取数据

向连接到 Arduino 板的 SPI 设备写入数据以及从 SPI 设备读取数据。使用此模块，您可以访问 SPI 设备以测量温度、压力等物理量。您还可以访问 SPI 设备以支持 Wi-Fi® 连接，并访问 SD 卡以存储数据。

单击 **查看引脚映射** 以打开 Arduino Pin Mapping 表。

要了解如何为该模块分配引脚，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。
