---
type: simulink-block
title: 'LPS22HB Pressure Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sensors / Environmental Sensors'
documentation_page: 'lps22hbpressuresensor'
documentation_source_path: 'supportpkg/raspberrypi_ref/lps22hbpressuresensor.html'
language: zh-CN
chinese_source: worker-translation
---

# LPS22HB Pressure Sensor

## 端口

### 输出

### **Pressure** — 由 LPS22HB 传感器测量的大气压力，标量

该模块输出以 Pascals (Pa) 为单位的大气压力。

#### 依赖关系

仅当您选择 **Pressure (Pa)** 参数时，才会显示此输出端口。

**数据类型：** `double`

### **Temperature** — 由 LPS22HB 传感器测量的温度，标量

由连接到 Raspberry Pi 板的 LPS22HB 传感器测量的温度（单位：℃）。

#### 依赖关系

仅当您选择 **Temperature (℃)** 参数时，才会显示此输出端口。

**数据类型：** `double`

### **Status** — 压力和温度测量的状态 `0` | `1` | `-1`

压力和温度测量的状态，指定为 1×2 向量。
`0` 表示读取的数据是新数据，`1` 表示读取的数据不是新数据，`-1` 表示未选择相应的输出。

#### 依赖关系

仅当您选择 **Status** 参数时，才会显示此输出端口。

**数据类型：** `int8`

## 参数

### **I2C module** — 用于通信的模块 `1`（默认）

指定板上用于 I2C 通信的模块。

### **I2C address** — 用于与传感器通信的外设地址 `0x5C`（默认） | `0x5D`

用于与 LPS22HB 传感器通信的外设地址由硬件板上 SA0 引脚的状态决定。下表提供了该引脚及其状态对应的外设地址。

| 引脚名称 | 引脚状态 | 外设地址 |
| --- | --- | --- |
| SA0 | 0 | 0x5C |
| 1 | 0x5D |

### **Pressure (Pa)** — 设置用于读取压力的输出端口 `on`（默认） | `off`

选择此参数可将 **Pressure** 设置为输出端口之一。

### **Temperature (℃)** — 设置用于读取温度的输出端口 `on`（默认） | `off`

选择此参数可将 **Temperature** 设置为输出端口之一。

### **Status** — 设置用于获取状态的输出端口 `off`（默认） | `on`

选择此参数可将 **Status** 设置为输出端口之一。

### **Output data rate (ODR)** — 压力数据的采样速率 `1 Hz`（默认） | `10 Hz` | `25 Hz` | `50 Hz` | `75 Hz`

选择压力数据的采样输出数据速率，这也决定了带宽。

### **Enable low pass filter** — 为压力数据启用低通滤波器 `off`（默认） | `on`

启用低通滤波器以读取压力值。

### **Select the bandwidth** — 低通滤波器的带宽 `ODR/9`（默认） | `ODR/20`

选择低通滤波器所需的带宽。

#### 依赖关系

仅当您选择 **Enable low pass filter** 参数时，才会显示此参数。

### **Sample time** — 读取数据的时间间隔 `-1`（默认） | 正整数

指定此模块从 LPS22HB 传感器读取数据的频率。当您将此参数设置为 -1 时，Simulink 将根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Sensors / Environmental Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2022b 中引入**

## 描述

测量来自 LPS22HB 传感器的大气压力和温度

LPS22HB Pressure Sensor 模块使用与 Raspberry Pi® 板连接的 LPS22HB 压力传感器测量大气压力。该传感器包含一个用于测量绝对压力的感测元件。该模块还测量 LPS22HB Sensor 中嵌入式温度传感器的温度。

您还可以在该模块中选择输出数据速率，并使用低通滤波器选项对测得的压力值进行滤波。
