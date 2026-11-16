---
type: simulink-block
title: 'Serial Write'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Communication'
documentation_page: 'serialwrite'
documentation_source_path: 'nvidia/ref/serialwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Serial Write

## 端口

### 输入

### **Port\_1** — 接受 [Nx1] 或 [1xN] 数组数据的输入端口

模块通过该输入端口接受数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **Port** — 将板卡连接到串行设备的端口 `/dev/ttyTHS1` (default)

将 NVIDIA Jetson 板卡连接到串行设备的端口。

### **Baudrate (in bits/s)** — 每秒位数 `9600` (default) | `50` | `75` | `110` | `134` | `150` | `200` | `300` | `600` | `1200` | `1800` | `2400` | `4800` | `19200` | `38400` | `57600` | `115200` | `230400`

选择通过串行线读取数据的速率。波特率以每秒读取的位数衡量。

### **Parity** — 为检测错误而添加到数据中的奇偶校验 `None` (default) | `Even` | `Odd`

选择要添加到传输数据中的奇偶校验。奇偶校验位用于检测数据传输中的错误。

- **None** – 该值表示在数据传输中不使用奇偶校验进行错误检测。
- **Even** – 如果值为 1 的位数为奇数，则奇偶校验位值为 1。如果值为 1 的位数为偶数，则奇偶校验位值为 0。
- **Odd** – 如果值为 1 的位数为偶数，则奇偶校验位值为 1。如果值为 1 的位数为奇数，则奇偶校验位值为 0。

### **Stop bits** — 用于指示数据传输停止的位数 1 (default) | 2

选择用于指示数据传输停止的位数。

## 所属库

NVIDIA Jetson and NVIDIA DRIVE / Communication

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2020b 中引入**

## 描述

将数据写入串行端口

使用 Serial Write 模块将数据写入连接到 NVIDIA® Jetson™ 硬件的串行设备。要打开 NVIDIA Jetson 板卡的串行引脚映射，请点击 **View pin map** 按钮。有关详细信息，请参阅 NVIDIA Jetson 板卡的串行端口映射。
