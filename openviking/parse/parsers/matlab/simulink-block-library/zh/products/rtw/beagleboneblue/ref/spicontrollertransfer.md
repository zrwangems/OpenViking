---
type: simulink-block
title: 'SPI Master Transfer'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Communication'
documentation_page: 'spicontrollertransfer'
documentation_source_path: 'beagleboneblue/ref/spicontrollertransfer.html'
language: zh-CN
chinese_source: worker-translation
---

# SPI Master Transfer

## 端口

### 输入

### **Port\_1** — 用于将数据写入 SPI 外设的输入端口 [Nx1] 或 [1xN] 数组

该输入端口用于让模块接收一维值数组，以写入外设设备。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### 输出

### **Port\_1** — 用于从 SPI 外设设备读取数据的输出端口 [Nx1] 数组

模块通过该输出端口从 SPI 外设设备接收数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **SPI select** — SPI 外设设备所连接的外设选择引脚 S1.1（默认）| S1.2

选择 SPI 外设设备所连接的 BeagleBoneBlue 板上的引脚编号。

### **Mode (Clock polarity and phase)** — SPI 通信模式 0（默认）| 1 | 2 | 3

选择 SPI 通信模式。

有关模式的详细信息，请参阅 SPI 传输模式。

## 所属库

Simulink Coder Support Package for BeagleBone Blue Hardware / Communication

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

向 SPI 外设设备写入数据并从 SPI 外设设备读取数据

向 SPI 外设设备写入数据并从 SPI 外设设备读取数据。要打开 BeagleBone® Blue 板的引脚图，请点击 **View pin map** 按钮。

有关 SPI 通信的详细信息，请参阅支持 SPI 通信。

该模块可与 Byte Pack 或 Byte Unpack 模块一起使用，以支持异构数据类型传输。
