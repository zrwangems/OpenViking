---
type: simulink-block
title: 'SPI Register Read'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Communication'
documentation_page: 'spiregisterread'
documentation_source_path: 'beagleboneblue/ref/spiregisterread.html'
language: zh-CN
chinese_source: worker-translation
---

# SPI Register Read

## 端口

### 输出

### **Port\_1** — 用于读取数据的输出端口 [Nx1] 数组

此端口是用于从 SPI 外设寄存器读取数据的输出端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

## 参数

### **Mode (Clock polarity and phase)** — SPI 通信模式 0（默认） | 1 | 2 | 3

选择 SPI 通信模式。

### **Register address** — 要读取数据的寄存器地址 0（默认） | uint8 array

输入要读取数据的 SPI 外设寄存器地址。

### **Output data type** — 输出的数据类型 int8（默认） | uint8 | int16 | uint16 | int32 | uint32 | int64 | uint64 | single | double

选择用于 SPI 通信的数据类型。

### **Output data length** — SPI 通信的数据长度 1（默认） | scalar

输入要从 SPI 外设寄存器读取的所选数据类型的输出数据长度。

### **SPI Select** — 连接到 SPI 外设设备的引脚 S1.1（默认） | S1.2

选择 BeagleBone Blue 板上连接 SPI 外设设备的引脚编号。

### **Sample time** — 从 SPI 外设设备读取数据的频率 `0.1`（默认）

指定模块从 SPI 外设设备读取数据的频率。当您将此参数指定为`-1`时，Simulink® 将根据模型中的模块上下文确定模块的最佳采样时间。

## 所属库

Simulink Coder Support Package for BeagleBone Blue Hardware / Communication

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2018b 中引入**

## 描述

从 SPI 外设设备寄存器读取数据

SPI Register Read 模块启动从 SPI 外设寄存器进行的 SPI 读取操作。您可以指定数据类型和数据长度，以从外设寄存器获取数据。要打开 BeagleBone® 板的引脚映射，请点击 **View pin map** 按钮。
