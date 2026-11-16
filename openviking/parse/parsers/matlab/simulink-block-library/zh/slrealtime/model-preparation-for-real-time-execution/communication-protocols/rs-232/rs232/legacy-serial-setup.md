---
type: simulink-block
title: 'Legacy Serial Setup'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / RS-232 / RS232'
documentation_page: 'legacyserialsetup'
documentation_source_path: 'io_ref/legacyserialsetup.html'
language: zh-CN
chinese_source: official
---

# Legacy Serial Setup

## 端口

R2025b 官方文档未提供。

## 参数

### **Serial port** — 正在访问的端口 **Legacy Serial Port 1** (默认) | .. | **Legacy Serial Port 8** | **USB Serial Port 1** | .. | **USB Serial Port 8**

指定用于通信的串行端口。

若使用 USB 转串口适配器，目标计算机将按适配器连接至串口设备的顺序，将这些适配器识别为 `serusb1`、`serusb2` 等名称。

端口分配顺序在目标计算机或串行设备断电重启后仍会保留，前提是端口连接状态未发生改变。

#### 编程用法

|  |
| --- |
| **模块参数：**`port` |

### **Baud rate** — 选择串口波特率 `115200` (默认) | `57600` | `38400` | `19200` | `9600` | `4800` | `2400` | `1200` | `600` | `300` | `110`

使用此值选择串行端口的波特率。

#### 编程用法

```
baud
```

### **Number of data bits** — 选择串行端口数据位 `8` (默认) | `7` | `6` | `5`

使用此值选择串行端口数据位的数量。

#### 编程用法

```
width
```

### **Number of stop bits** — 选择串行端口停止位 `1` (默认) | `2`

使用此值选择串行端口的停止位数量。

#### 编程用法

```
nstop
```

### **Parity** — 选择串口奇偶校验 `None` (默认) | `Even` | `Odd` | `Mark` | `Space`

使用此值选择串行端口的奇偶校验。

#### 编程用法

```
parity
```

### **Enable auto RTX/CTS** — 选择串口 RTX/CTS 模式 `off` (默认) | `on`

使用此值选择串行端口的 RTX/CTS 模式。

#### 编程用法

```
ctsmode
```

## 所属库

Simulink Real-Time / RS232 / Mainboard

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2020b 中推出**

### R2021b: USB 转 RS232 串口转换模块

RS232 主板模块支持连接 USB 串口适配器端口。**Serial port** 参数在 Legacy Serial Read 模块、Legacy Serial Write 模块、Legacy Serial Setup 模块、Legacy Serial Port 模块和 Legacy Serial Port F 模块中表示可选择 **USB Serial Port** 或 **Legacy Serial Port**。

## 描述

设置基座串行通信

Legacy Serial Setup 模块在 Speedgoat® 目标计算机上配置主板串行通信。

有关详细信息，请参阅RS-232 串行通信和RS-232 Legacy Drivers。
