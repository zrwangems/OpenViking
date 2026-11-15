---
type: simulink-block
title: 'Serial Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Communication'
documentation_page: 'serialwrite'
documentation_source_path: 'supportpkg/raspberrypi_ref/serialwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Serial Write

## 端口

### 输入

### **Port\_1** — 用于接受数据 [Nx1] 或 [1xN] 数组的输入端口

模块通过该输入端口接受数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **Board** — 用于串行通信的特定开发板 `Pi 3 Model B` (默认) | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 2 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Pi 4 Model B` | `Pi 5 Model`

选择您正在使用的特定开发板。更改开发板会更新您可获得的引脚选项。

### **Port** — 您要连接到串行设备的端口 /dev/ttyAMA0 (默认)

您要从所选 Raspberry Pi 开发板连接到串行设备的端口。对于 Pi 3 Model B 开发板，默认串行端口为 /dev/ttyS0。

### **Baudrate (in bits/s)** — 每秒位数 9600 (默认) | 50 | 75 | 110 | 134 | 150 | 200 | 300 | 600 | 1200 | 1800 | 2400 | 4800 | 9600 | 19200 | 38400 | 57600 | 115200 | 230400

选择通过串行线路读取数据的速率。波特率以每秒读取的位数来衡量。

### **Parity** — 添加到数据中的偶校验或奇校验 `None` (默认) | `Even` | `Odd`

选择添加到所传输数据中的校验。校验位用于检测数据传输中的错误。

- None – 此参数中的 None 值表示数据传输中不使用校验进行错误检测。
- 偶校验 – 如果值为 1 的位数为奇数，则校验位值为 1。如果值为 1 的位数为偶数，则校验位值为 0。
- 奇校验 – 如果值为 1 的位数为偶数，则校验位值为 1。如果值为 1 的位数为奇数，则校验位值为 0。

### **Stop bits** — 用作停止位的位数 1 (默认) | 2

选择数据传输中用作停止位的位数。停止位标记一个传输单元的结束。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Communication

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2017a 中引入**

## 描述

将数据写入串行设备

将数据写入连接到 Raspberry Pi® 硬件的串行设备。要打开 Raspberry Pi 开发板的引脚图，请点击 **查看引脚图**。

有关信息，请参阅异步串行通信。
