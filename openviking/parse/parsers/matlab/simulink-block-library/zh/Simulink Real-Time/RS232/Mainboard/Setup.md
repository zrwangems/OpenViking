---
type: simulink-block
title: 'Legacy Serial Setup'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2023b
official_category: 'RS232 / Mainboard'
documentation_page: 'legacyserialsetup'
documentation_source_path: 'io_ref/legacyserialsetup.html'
language: zh-CN
chinese_source: worker-translation
---

# Legacy Serial Setup

## 端口

在 R2025b 中未记录。

## 参数

### **串行端口** — 选择串行端口 `Legacy Serial Port 1`（默认） | .. | `Legacy Serial Port 8` | `USB Serial Port 1` | .. | `USB Serial Port 8`

选择用于通信的 RS232 串行端口。如果使用 USB 转串口适配器，目标计算机按适配器连接到串行设备的顺序将这些适配器检测为 `serusb1`、`serusb2` 等。如果端口连接没有变化，则端口分配顺序在目标计算机或串行设备断电重启后仍会保留。

#### 编程用法

```
port
```

### **波特率** — 选择串行端口波特率 `115200`（默认） | `57600` | `38400` | `19200` | `9600` | `4800` | `2400` | `1200` | `600` | `300` | `110`

使用此值选择串行端口波特率。

#### 编程用法

```
baud
```

### **数据位数** — 选择串行端口数据位数 `8`（默认） | `7` | `6` | `5`

使用此值选择串行端口数据位数。

#### 编程用法

```
width
```

### **停止位数** — 选择串行端口停止位数 `1`（默认） | `2`

使用此值选择串行端口停止位数。

#### 编程用法

```
nstop
```

### **奇偶校验** — 选择串行端口奇偶校验 `None`（默认） | `Even` | `Odd` | `Mark` | `Space`

使用此值选择串行端口奇偶校验。

#### 编程用法

```
parity
```

### **启用自动 RTX/CTS** — 选择串行端口 RTX/CTS 模式 `off`（默认） | `on`

使用此值选择串行端口 RTX/CTS 模式。

#### 编程用法

```
ctsmode
```

## 所属库

Simulink Real-Time / RS232 / Mainboard

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

### R2021b：RS232 模块的 USB 转串口

RS232 主板模块支持连接 USB 串行适配器端口。Legacy Serial Read 模块、Legacy Serial Write 模块、Legacy Serial Setup 模块、Legacy Serial Port 模块和 Legacy Serial Port F 模块的 `Serial port` 参数意味着可以选择 `USB Serial Port` 或 `Legacy Serial Port`。

## 描述

设置基板串行通信

Legacy Serial Setup 模块用于设置基板串行通信。
