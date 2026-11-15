---
type: simulink-block
title: 'SPI Register Write'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Communication'
documentation_page: 'spiregisterwrite'
documentation_source_path: 'beagleboneblue/ref/spiregisterwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# SPI Register Write

## 端口

### 输入

### **Port\_1** — 用于接受 [Nx1] 或 [1xN] 数组数据的输入端口

用于接受要写入 SPI 外设寄存器的数据的输入端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### **SPI Select** — 连接到 SPI 外设设备的引脚 S1.1 (默认) | S1.2

选择 BeagleBone Blue 板上 SPI 外设设备所连接的引脚编号。

### **Mode (Clock polarity and phase)** — SPI 通信模式 0 (默认) | 1 | 2 | 3

选择 SPI 通信模式。

### **Register address** — 要写入数据的寄存器地址 0 (默认) | uint8 array

输入要写入数据的外设寄存器地址。

## 所属库

Simulink Coder Support Package for BeagleBone Blue Hardware / Communication

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

将数据写入 SPI 外设设备的寄存器

SPI Register Write 模块将模块输入数据写入指定的寄存器地址。要打开 BeagleBone® Blue 板的引脚映射，请点击 **View pin map** 按钮。
