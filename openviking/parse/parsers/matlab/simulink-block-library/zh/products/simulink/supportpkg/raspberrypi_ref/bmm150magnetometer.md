---
type: simulink-block
title: 'BMM150 Magnetometer'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sensors / IMU Sensors'
documentation_page: 'bmm150magnetometer'
documentation_source_path: 'supportpkg/raspberrypi_ref/bmm150magnetometer.html'
language: zh-CN
chinese_source: worker-translation
---

# BMM150 Magnetometer

## 端口

### 输出

### **Magnetic Field** — 由 BMM150 传感器测得的磁场强度行向量

由连接到 Raspberry Pi 板的 BMM150 传感器测得的磁场强度（单位为 µT），沿 x-、y- 和 z- 轴，指定为行向量 [x,y,z]。

**数据类型：** `double`

### **Magnetic Field Status** — 磁场值的状态 `0` | `1`

磁场状态 `0` 表示读取的数据是新的，`1` 表示读取的数据不是新的。

#### 依赖关系

仅当选择 **状态** 参数时，此输出端口才会出现。

**数据类型：** `int8`

## 参数

### **I2C 模块** — 用于通信的模块 `1`（默认）

指定板上用于 I2C 通信的模块。

### **I2C 地址** — BMM150 传感器的 I2C 地址 `0x13`（默认） | `0x10` | `0x11` | `0x12`

BMM150 传感器与 Raspberry Pi 处理器通信时使用的 I2C 地址。默认参数值（`0x13`）对应于 BOOSTXL-SENSORS BoosterPackTM Plug-in Module User's Guide 的 `Schematics` 部分中提到的值。

### **状态** — 设置用于获取磁场状态的输出端口 `on`（默认） | `off`

选择此参数以将 **Magnetic Field Status** 设置为输出端口之一。

### **预设值** — BMM150 传感器工作条件的预设值 `Low power`（默认） | `Regular` | `Enhanced` | `High accuracy`

指定读取值时 BMM150 传感器工作条件的预设值。选择四个预设值之一会影响电气特性（如供电电流）以及相对于 ODR 和输出噪声所需的输出精度。

### **数据类型** — BMM150 传感器值的输出数据类型 `single`（默认） | `double`

指定从 BMM150 传感器读取的值的输出数据类型。Raspberry Pi 处理器的默认数据类型为 `single`。如果需要，可使用此参数将值更改为 `double`。

### **采样时间** — 读取数据的时间间隔 `-1`（默认） | 正整数

指定此模块从 BMM150 传感器读取数据的频率。将此参数设置为 -1 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Sensors / IMU Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

## 描述

测量来自 BMM150 传感器的磁场

BMM150 模块输出由连接到 Raspberry Pi® 板的 BMM150 传感器测得的沿 x-、y- 和 z- 轴的磁场值。
