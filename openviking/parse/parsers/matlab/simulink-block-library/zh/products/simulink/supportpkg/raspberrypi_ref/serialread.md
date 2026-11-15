---
type: simulink-block
title: 'Serial Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Communication'
documentation_page: 'serialread'
documentation_source_path: 'supportpkg/raspberrypi_ref/serialread.html'
language: zh-CN
chinese_source: worker-translation
---

# Serial Read

## 端口

### 输出

### **Data** — 用于读取数据的输出端口 [Nx1] 数组

该模块通过此数据端口从串行设备读取数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Status** — 用于发出数据读取状态的输出端口（标量）

输出端口，用于发出数据读取的状态。下表列出了可能的状态值及其描述。

| 状态值 | 状态描述 |
| --- | --- |
| `0` | `SUCCESS` |
| `1` | `RX_BUSY` |
| `2` | `TX_BUSY` |
| `4` | `PARITY_ERROR` |
| `8` | `FRAME_ERROR` |
| `16` | `BUS_ERROR` |
| `32` | `DATA_NOT_AVAILABLE` |

**数据类型：** `uint8`

## 参数

### **Board** — 用于串行通信的特定开发板 `Pi 3 Model B`（默认）| `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 2 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Pi 4 Model B` | `Pi 5 Model`

选择您正在使用的特定开发板。更改开发板会更新您可获得的引脚选项。

### **Port** — 要连接串行设备的端口 /dev/ttyAMA0（默认）

从所选 Raspberry Pi 开发板连接到串行设备的端口。对于 Pi 3 Model B 开发板，默认串行端口是 /dev/ttyS0。

### **Baudrate (in bits/s)** — 每秒位数 9600（默认）| 50 | 75 | 110 | 134 | 150 | 200 | 300 | 600 | 1200 | 1800 | 2400 | 4800 | 9600 | 19200 | 38400 | 57600 | 115200 | 230400

选择通过串行线路读取数据的速率。波特率以每秒读取的位数衡量。

### **Parity** — 添加到数据中用于错误检测的偶校验或奇校验 `None`（默认）| `Even` | `Odd`

选择添加到所传输数据中的奇偶校验。奇偶校验位用于检测数据传输中的错误。

- None – 此参数中的 None 值表示数据传输中不使用奇偶校验进行错误检测。
- Even parity – 如果值为 1 的位数为奇数，则校验位值为 1。如果值为 1 的位数为偶数，则校验位值为 0。
- Odd parity – 如果值为 1 的位数为偶数，则校验位值为 1。如果值为 1 的位数为奇数，则校验位值为 0。

### **Stop bits** — 用作停止位的位数 1（默认）| 2

选择数据传输中用作停止位的位。停止位标记一个传输单元的结束。

### **Data length (N)** — 用于传输的数据长度 1（默认）| scalar

输入您想要从串行设备读取的、用于所选数据类型的数据大小。

### **Data type** — 用于传输的数据类型 uint8（默认）| uint8 | uint16 | uint32 | int8 | int16 | int32 | single | double

选择您想要传输的数据类型。

### **Sample time** — 模块读取数据的时间频率 0.1（默认）| scalar

指定此模块读取串行数据的频率。输入一个大于零的值。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2017a 中引入**

## 描述

从串行设备读取数据

从连接到 Raspberry Pi® 硬件的串行设备读取数据。

有关信息，请参阅 Asynchronous Serial Communication。
要打开 Raspberry Pi 开发板的引脚映射，请点击 **View pin map** 按钮。
