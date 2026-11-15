---
type: simulink-block
title: 'SCI Read'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Communication'
documentation_page: 'sciread'
documentation_source_path: 'beagleboneblue/ref/sciread.html'
language: zh-CN
chinese_source: worker-translation
---

# SCI Read

## 端口

### 输出

### **Data** — 从 UART 读取的数据向量

**Data** 端口输出从所选 UART 读取的数据。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

### **Status** — 读取操作状态标量

当接收到的数据长度大于或等于 **Data length (N)** 参数中指定的长度时，模块输出 `0`。值 `0` 表示读取操作成功。当接收到的数据长度小于 **Data length (N)** 参数中指定的长度时，模块输出非零值。

例如，当接收到的数据长度为 9 且 *N* = 8 时，**Status** 端口输出 `0`，表示读取操作成功。当接收到的数据长度为 9 且 *N* = 10 时，**Status** 端口输出 `32`，表示数据不可用。

| 接收到的数据长度 = 9 | | | | |
| --- | --- | --- | --- | --- |
| **端口** | **数据类型** | **数据长度** | | |
| *N* = 8 | *N* = 9 | *N* = 10 |
| **Data** | `uint8` | `8` | `9` | `9` |
| **Status** | `uint8` | `0` | `0` | `32` |

**数据类型：** `uint8`

## 参数

### **Port** — 硬件连接到的串行端口 `/dev/ttyO1` (default) | 有效的路径和文件名

指定硬件上连接到串行设备的串行端口。例如，如果端口 UT0 连接到串行设备，请将此参数指定为 `/dev/ttyO0`。要查看 BeagleBone® Blue 引脚排列，请点击 **View pin map** 按钮。

### **Baudrate (in bits/s)** — 串行波特率 `9600` (default) | `50` | `75` | `110` | `134` | `150` | `200` | `300` | `600` | `1200` | `1800` | `2400` | `4800` | `19200` | `38400` | `57600` | `115200` | `230400`

选择每秒要接收的位数。接收的位包括起始位、数据位、奇偶校验位（如果已定义）和停止位。

### **Parity** — 接收数据的差错校验类型 `None` (default) | `Even` | `Odd`

选择奇偶校验以便为接收的数据提供简单的差错校验。下表显示了奇偶校验的类型。

| 奇偶校验类型 | 描述 |
| --- | --- |
| `None` | 不进行奇偶校验。 |
| `Even` | 数据位加上奇偶校验位会得到偶数个 1。 |
| `Odd` | 数据位加上奇偶校验位会得到奇数个 1。 |

奇偶校验过程遵循以下步骤：

1. 发送设备根据数据位值和所选的奇偶校验类型，将奇偶校验位设置为 0 或 1。
2. 接收设备检查奇偶校验位是否与发送的数据一致。如果一致，则接受数据位。如果不一致，则返回错误。

例如，假设数据位 01110001 被发送到您的计算机。如果选择 even parity，发送设备将奇偶校验位设置为 0，以产生偶数个 1。如果选择 odd parity，发送设备将奇偶校验位设置为 1，以产生奇数个 1。

**注意**

奇偶校验只能检测 1 位错误。多位错误可能表现为有效数据。

### **Stop bits** — 用于表示字节结束的位数 `1` (default) | `2`

选择用于表示字节结束的停止位数。

- `1` — 发送一个停止位以表示字节结束。
- `2` — 发送两个停止位以表示字节结束。

### **Data type** — 来自 UART 端口的数据类型 `uint8` (default) | `int8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

选择要从 UART 端口读取的数据类型。

### **Data length (N)** — 要从 UART 端口读取的数据值数量 `1` (default) | 非负整数

指定要为所选数据类型从 UART 端口读取的值的数量。

### **Sample time** — 从 UART 端口读取数据的频率 `0.1` (default) | `-1` | 非负整数

指定从 UART 端口读取数据的时间间隔，以秒为单位。将此参数设置为 `-1` 时，Simulink® 会根据模型中的模块上下文为该模块确定最佳采样时间。

## 所属库

Simulink Coder Support Package for BeagleBone Blue Hardware / Communication

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

从 UART 端口读取串行数据

SCI Read 模块从硬件上的通用异步收发器 (UART) 读取一个 *N*×1 数据数组，其中 *N* 是要读取的数据长度。

如果在未连接硬件的情况下仿真包含 SCI Read 模块的模型，该模块输出零。请参阅 Block Produces Zeros or Does Nothing in Simulation。

此模块以非阻塞模式运行。
