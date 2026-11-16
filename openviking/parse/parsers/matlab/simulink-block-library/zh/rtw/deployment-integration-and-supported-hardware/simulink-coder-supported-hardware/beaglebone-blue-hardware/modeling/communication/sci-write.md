---
type: simulink-block
title: 'SCI Write'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Communication'
documentation_page: 'sciwrite'
documentation_source_path: 'beagleboneblue/ref/sciwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# SCI Write

## 端口

### 输入

### **Port\_1** — 发送到 UART 的数据向量

从您的模型发送到 UART 端口的数据。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

## 参数

### **Port** — 硬件上的串行端口 `/dev/ttyO1`（默认）| 有效路径和文件名

指定硬件上连接到串行设备的串行端口。例如，如果端口 UT0 连接到串行设备，请将此参数指定为 `/dev/ttyO0`。要查看 BeagleBone® 引脚布局，请单击 **查看引脚映射** 按钮。

### **Baudrate (in bits/s)** — 串行波特率 `9600`（默认）| `50` | `75` | `110` | `134` | `150` | `200` | `300` | `600` | `1200` | `1800` | `2400` | `4800` | `19200` | `38400` | `57600` | `115200` | `230400`

选择每秒传输的位数。传输的位包括起始位、数据位、奇偶校验位（如果定义）和停止位。

### **Parity** — 用于所传输数据的错误校验类型 `None`（默认）| `Even` | `Odd`

选择一种奇偶校验，以为所传输的数据提供简单的错误检查。下表显示了奇偶校验的类型。

| 奇偶校验类型 | 描述 |
| --- | --- |
| `None` | 无奇偶校验。 |
| `Even` | 数据位加上奇偶校验位后，1 的总数为偶数。 |
| `Odd` | 数据位加上奇偶校验位后，1 的总数为奇数。 |

奇偶校验过程遵循以下步骤：

1. 发送设备根据数据位值以及所选的奇偶校验类型，将奇偶校验位设置为 0 或 1。
2. 接收设备检查奇偶校验位是否与所传输的数据一致。如果一致，则接受数据位。如果不一致，则返回错误。

例如，假设数据位 01110001 被传输到您的计算机。如果选择 `Even`，则发送设备将奇偶校验位设置为 0，以产生偶数个 1。如果选择 `Odd`，则发送设备将奇偶校验位设置为 1，以产生奇数个 1。

**注意**

奇偶校验只能检测 1 位错误。多位错误可能会显示为有效数据。

### **Stop bits** — 用于指示字节结束的位数 `1`（默认）| `2`

选择用于指示一个字节结束的停止位数。

- `1` — 传输一个停止位以指示一个字节的结束。
- `2` — 传输两个停止位以指示一个字节的结束。

## 所属库

Simulink Coder Support Package for BeagleBone Blue Hardware / Communication

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

将串行数据发送到 UART 端口

SCI Write 模块将数据发送到硬件的选定通用异步收发器（UART）端口。数据必须是 *N*×1 或 1×*N* 数组，其中 *N* 是要写入的数据长度。该模块从输入端口处的信号继承数据类型。

如果在未连接硬件的情况下仿真包含 SCI Write 模块的模型，则该模块不执行任何操作。有关详细信息，请参阅“模块在仿真中产生零值或不执行任何操作”。
