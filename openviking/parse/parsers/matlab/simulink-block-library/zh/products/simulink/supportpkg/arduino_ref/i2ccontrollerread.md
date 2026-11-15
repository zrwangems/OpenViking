---
type: simulink-block
title: 'I2C Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / I2C'
documentation_page: 'i2ccontrollerread'
documentation_source_path: 'supportpkg/arduino_ref/i2ccontrollerread.html'
language: zh-CN
chinese_source: worker-translation
---

# I2C Read

## 端口

### 输出

### **Data** — 用于从 I2C 外设设备读取数据的输出端口 [Nx1] 数组

用于从 I2C 外设设备读取数据的输出端口。该端口输出的数据大小基于 **数据大小 (N)** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Status** — 读取操作的状态，标量

用于显示错误状态的输出端口。有关详细信息，请参阅输出错误状态。

#### 依赖关系

仅当选择 **输出错误状态** 参数时，此端口才会出现。

**数据类型：** `uint8`

## 参数

### **I2C 模块** — I2C 通信模块 `0` (默认) | 标量

指定 Arduino® 硬件上用于与传感器外设通信的 I2C 模块。有关 Arduino 引脚映射以及硬件板支持的模块的详细信息，请参阅 Arduino 定时器无关模块的引脚映射。

### **外设地址** — I2C 外设设备地址 10 (默认) | 标量

输入要从中读取数据的 I2C 外设设备地址。可以使用十六进制格式 hex2dec() 指定此地址，例如 hex2dec(‘10')。

### **外设字节序** — I2C 外设设备支持的字节序 `BigEndian` (默认) | `LittleEndian`

选择 I2C 外设支持的字节序。

两种字节序选项为：

- `BigEndian` — 最高有效字节首先通过 I2C 总线读取。此选项为默认选项。
- `LittleEndian` — 最低有效字节首先通过 I2C 总线读取。

### **启用寄存器地址** — 用于启用从 I2C 外设寄存器读取的选项 `on` (默认) | `off`

选中此复选框以启用从 I2C 外设设备的特定寄存器读取数据。

清除此参数时，将显示 **数据传输结束时发送 NACK** 和 **数据传输结束时移除停止位** 参数。使用这些参数，可以根据需求修改读取操作。

### **外设寄存器地址** — 要读取数据的 I2C 外设设备寄存器地址 `0` (默认) | 标量

输入要从中读取数据的外设设备寄存器地址。

使用 `hex2dec()` 将此地址指定为整数或十六进制格式，例如 hex2dec(‘10’)。

#### 依赖关系

仅当选择 **启用寄存器访问** 参数时，此参数才启用。

### **数据类型** — 要从 I2C 外设设备读取的数据类型 `uint8` (默认) | `int8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

选择要从 I2C 外设设备读取的数据类型。

### **数据大小 (N)** — 要从 I2C 外设设备读取的数据大小 `1` (默认) | 标量

输入要针对所选数据类型从 I2C 外设设备读取的数据大小。

### **输出错误状态** — 在数据传输期间显示错误状态的选项 off (默认) | on

选中此选项以在数据传输期间显示错误状态。

当选择 **输出错误状态** 参数时，模块将配置一个输出端口。模块上的该端口标记为 `Status`，表示模块在输出端口处输出读取操作的状态。

模块将状态输出为 `uint8` 值。每个值对应一种数据传输状态。

| 状态值 | 状态描述 |
| --- | --- |
| `0` | `SUCCESS` |
| `1` | `BUSY` |
| `2` | `ARBITRATION_LOST` |
| `4` | `NO_ACKNOWLEDGE` |
| `8` | `BUS_ERROR` |
| `16` | `BUS_NOT_IN_USE` |

### **采样时间** — 模块读取数据的频率 0.1 (默认) | 标量

指定此模块从 I2C 外设读取数据的频率。输入大于零的值。

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2015a 中引入**

## 描述

从 I2C 外设设备或 I2C 外设设备寄存器读取数据

从 I2C 外设读取串行数据。使用此模块，还可以从 I2C 外设设备上的特定寄存器读取数据。

有关 I2C 通信的详细信息，请参阅 I2C 读取/写入。

单击 **查看引脚映射** 以打开 Arduino 引脚映射表。

要了解如何为该模块分配引脚，请参阅 Arduino 定时器无关模块的引脚映射。
