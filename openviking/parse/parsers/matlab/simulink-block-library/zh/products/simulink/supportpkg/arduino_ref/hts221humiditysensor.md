---
type: simulink-block
title: 'HTS221 Humidity Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Environmental Sensors'
documentation_page: 'hts221humiditysensor'
documentation_source_path: 'supportpkg/arduino_ref/hts221humiditysensor.html'
language: zh-CN
chinese_source: worker-translation
---

# HTS221 Humidity Sensor

## 端口

### 输出

### **Humidity** — 由 HTS221 传感器测量的相对湿度，标量

该模块输出相对湿度，以百分比 (%) 为单位。

#### 依赖项

仅当选择 **Humidity
(%)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Temperature** — 由 HTS221 传感器测量的温度，标量

由连接到 Arduino 板的 HTS221 传感器测量的温度（单位为 ℃）。

#### 依赖项

仅当选择 **Temperature
(℃)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Status** — 压力和温度测量的状态 `0` | `1` | `-1`

压力和温度测量的状态，指定为 1×2 向量。
`0` 表示读取的数据是新数据，`1`
表示读取的数据不是新数据，`-1` 表示未选择相应输出。

#### 依赖项

仅当选择 **Status** 参数时，此输出端口才会出现。

**数据类型：** `int8`

## 参数

### **I2C module** — I2C 通信模块 `0`（默认）| 标量

指定 Arduino 硬件上用于与传感器外设通信的 I2C 模块。有关
Arduino 引脚映射以及硬件板支持的模块的详细信息，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

### **I2C address** — 用于与传感器通信的外设地址 `0x5F`（默认）| 标量

HTS221 传感器与 Arduino 硬件通信的外设地址。

### **Humidity (%)** — 设置用于读取湿度的输出端口 `on`（默认）| `off`

选择此参数可将 **Humidity** 设置为输出端口之一。

### **Temperature (℃)** — 设置用于读取温度的输出端口 `on`（默认）| `off`

选择此参数可将 **Temperature** 设置为输出端口之一。

### **Status** — 设置用于获取状态的输出端口 `off`（默认）| `on`

选择此参数可将 **Status** 设置为输出端口之一。

### **Output data rate (ODR)** — 湿度和温度数据的采样速率 `1 Hz`（默认）| `7 Hz` | `12.5 Hz`

选择对湿度数据进行采样的输出数据速率。

### **Sample time** — 读取数据的时间间隔 `-1`（默认）| 正整数

指定此模块从 HTS221 传感器读取数据的频率。将此参数设置为 -1 时，
Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Simulink Support Package for Arduino Hardware / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021a 中引入**

## 描述

测量来自 HTS221 传感器的相对湿度和温度

HTS221 Humidity Sensor 模块使用与 Arduino® 硬件连接的 HTS221 湿度传感器测量相对湿度和环境温度。该传感器包含一个传感元件，用于测量相对湿度和温度。

还可以在模块中为测量值选择输出数据速率。

**注意**

如果使用的是 Arduino Nano 33 BLE Sense 硬件（其始终包含一个嵌入式传感器），则不支持从包含 HTS221 传感器的分线板读取数据。
