---
type: simulink-block
title: 'Legacy Serial Read'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'RS232 / Mainboard'
documentation_page: 'legacyserialread'
documentation_source_path: 'io_ref/legacyserialread.html'
language: zh-CN
chinese_source: worker-translation
---

# Legacy Serial Read

## 端口

### 输出

### **Output** — 从串口读取的数据 串行数据

Output 端口提供从串口读取的数据。

## 参数

### **Serial port** — 正在访问的端口 `Legacy Serial Port 1`（默认）| .. | `Legacy Serial Port 8` | `USB Serial Port 1` | .. | `USB Serial Port 8`

指定用于通信的串口。

如果使用 USB 转串口适配器，目标计算机会按照适配器连接到串行设备的顺序将这些适配器检测为 `serusb1`、`serusb2` 等。

如果端口连接没有变化，则端口分配的顺序在目标计算机或串行设备的电源循环期间保持不变。

#### 编程使用

|  |
| --- |
| **模块参数**：`port` |

### **Max Read Count** — 选择最大字读取计数 `51`（默认）| int

使用此值选择最大字读取计数。

#### 编程使用

```
count
```

### **Output Datatype** — 选择输出数据类型 `8 bit uint null terminated`（默认）| `8 bit int null terminated` | `count+16 bit uint` | `count+16 bit int` | `count+32 bit uint` | `count+32 bit int`

使用此值选择输出数据类型。

#### 编程使用

```
dtype
```

### **SampleTime** — 选择采样时间（以秒为单位） `.01`（默认）| double

使用此值选择采样时间（以秒为单位）。

#### 编程使用

```
sampletime
```

## 所属库

Simulink Real-Time / RS232 / Mainboard

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

### R2021b：RS232 模块的 USB 转串口

RS232 主板模块支持连接 USB 串口适配器端口。Legacy Serial Read 模块、Legacy Serial Write 模块、Legacy Serial Setup 模块、Legacy Serial Port 模块和 Legacy Serial Port F 模块的 `Serial port` 参数意味着您可以选择 `USB Serial Port` 或 `Legacy Serial Port`。

## 描述

读取底板串行通信的输入数据

Legacy Serial Read 模块在 Speedgoat® 目标计算机上读取底板串行通信的输入数据。

有关详细信息，请参阅 RS-232 Serial Communication 和 RS-232 Legacy Drivers。
