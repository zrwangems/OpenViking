---
type: simulink-block
title: 'Modem Control'
family: 'rs232'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'RS232 / Mainboard'
documentation_page: 'modemcontrol'
documentation_source_path: 'io_ref/modemcontrol.html'
language: zh-CN
chinese_source: worker-translation
---

# Modem Control

## 端口

### 输入

### **RTS** — 用于设置请求发送线的电平敏感信号 `double`

模块的行为如下：

- `RTS > 0.5` — 模块将 RTS 控制位置为 `true`。输出变为正电压。
- `RTS ≤ 0.5` — 模块将 RTS 控制位置为 `false`。输出变为负电压。

#### 依赖关系

如果 **RTS** 参数为 `off`，则此输入不起作用。

### **DTR** — 用于设置数据终端就绪线的电平敏感信号 `double`

模块的行为如下：

- `DTR > 0.5` — 模块将 DTR 控制位置为 `true`。输出变为正电压。
- `DTR ≤ 0.5` — 模块将 DTR 控制位置为 `false`。输出变为负电压。

#### 依赖关系

如果 **DTR** 参数为 `off`，则此输入不起作用。

## 参数

### **RTS** — 启用对串行设备 RTS 线的控制 `on`（默认）| `off`

选中此复选框以控制此板的 RTS 线。

#### 程序化用法

`rts`

### **DTR** — 启用对串行设备 DTR 线的控制 `on`（默认）| `off`

选中此复选框以控制此板的 DTR 线。

#### 程序化用法

`dtr`

### **串行端口** — 正在访问的端口 `Legacy Serial Port 1`（默认）| .. | `Legacy Serial Port 8` | `USB Serial Port 1` | .. | `USB Serial Port 8`

指定用于通信的串行端口。

如果使用 USB 转串行适配器，目标计算机会按照适配器连接到串行设备的顺序，将这些适配器检测为 `serusb1`、`serusb2`，依此类推。

如果到端口的连接没有变化，则端口分配顺序在目标计算机或串行设备断电重启后仍会保留。

#### 程序化用法

|  |
| --- |
| **模块参数：** `port` |

## 所属库

Simulink Real-Time / RS232 / Mainboard

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

控制串行端口上 RTS 和 DTR 输出线的状态

Modem Control 模块控制 Speedgoat® 目标计算机上串行端口的 Request To Send (RTS) 和 Data Terminal Ready (DTR) 输出线中的一者或两者的状态。要选择要控制哪些输出线，请选择 **RTS** 和 **DTR** 参数。
