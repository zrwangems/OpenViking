---
type: simulink-block
title: 'Serial Transmit'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'serialtransmit'
documentation_source_path: 'px4/ref/serialtransmit.html'
language: zh-CN
chinese_source: worker-translation
---

# Serial Transmit

## 端口

### 输入

### **Data** — 要发送到 UART 或 USART 端口的数据向量

该端口接受 N-by-1 或 1-by-N 数组形式的值。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

## 参数

### **Port** — 用于串行通信的 UART 或 USART 端口 `/dev/ttyACM0` (default) | `/dev/ttyS1` | `/dev/ttyS2` | `/dev/ttyS3` | `/dev/ttyS5` | `/dev/ttyS6`

输入 PX4 飞控上 UART 或 USART 端口的名称，模块通过该端口发送接受的数据。要查看 UART/USART 端口与 Pixhawk 飞控上的标签之间的映射，请参阅 PX4 飞控板上的串口名称和对应标签。

## 所属库

UAV Toolbox Support Package for PX4 Autopilots / PX4 Utility Blocks

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

将串行数据发送到 UART 或 USART 端口

Serial Transmit 模块将串行数据发送到 PX4® 飞控上的通用异步收发器 (UART) 端口或通用同步和异步收发器 (USART) 端口。

该模块接受 N-by-1 或 1-by-N 数组形式的数据，并将其发送到指定的 UART 或 USART 端口。用于串行通信的每个端口的属性在 Simulink® 的 Configuration Parameters 对话框中说明（转到 **Configuration Parameters**  > **Hardware Implementation** > **/dev/tty**\* 窗格）。

在 Connected I/O 仿真期间，此模块将数据写入硬件的指定串口。

该模块从输入端口的信号继承数据类型。

**注意**

如果使用 Cube Orange 自动驾驶仪，则使用 `GPS2` 进行串行数据通信，因为使用 `TELEM1` 或 `TELEM2` 端口可能会出现问题。
