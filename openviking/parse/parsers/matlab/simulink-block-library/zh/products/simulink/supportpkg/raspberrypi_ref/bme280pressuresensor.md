---
type: simulink-block
title: 'BME280 Pressure Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sensors / Environmental Sensors'
documentation_page: 'bme280pressuresensor'
documentation_source_path: 'supportpkg/raspberrypi_ref/bme280pressuresensor.html'
language: zh-CN
chinese_source: worker-translation
---

# BME280 Pressure Sensor

## 端口

### 输出

### **Pressure** — 由 BME280 传感器测得的气压标量

由连接到 Raspberry Pi 板的 BME280 传感器测得的气压（单位：Pascal (Pa)）。

#### 依赖关系

仅当选择 **Pressure (Pa)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Temperature** — 由 BME280 传感器测得的温度标量

由连接到 Raspberry Pi 板的 BME280 传感器测得的温度（单位：℃）。

#### 依赖关系

仅当选择 **Temperature (℃)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Humidity** — 由 BME280 传感器测得的相对湿度标量

由连接到 Raspberry Pi 板的 BME280 传感器测得的相对湿度（单位：%）。

#### 依赖关系

仅当选择 **Humidity (%)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Status** — 读取值的状态 `0` | `1`

从 BME280 传感器读取的值的状态，用于指示读取的数据是否为新值。**Status** 值 `0` 表示读取的数据是新值，`1` 表示读取的数据不是新值。

#### 依赖关系

仅当选择 **Status** 参数时，此输出端口才会出现。

**数据类型：** `uint8`

## 参数

### **I2C module** — 用于通信的模块 `1`（默认）

指定板上用于 I2C 通信的模块。

### **I2C address** — BME280 传感器的 I2C 地址 `0x76`（默认） | `0x77`

BME280 传感器与 Raspberry Pi 板通信时使用的 I2C 地址。

### **Pressure (Pa)** — 设置用于读取压力的输出端口 `on`（默认） | `off`

选择此参数可将 **Pressure** 设置为输出端口之一。

### **Temperature (℃)** — 设置用于读取温度的输出端口 `on`（默认） | `off`

选择此参数可将 **Temperature** 设置为输出端口之一。

### **Humidity (%)** — 设置用于读取湿度的输出端口 `on`（默认） | `off`

选择此参数可将 **Humidity** 设置为输出端口之一。

### **Status** — 设置用于获取读取值状态的输出端口 `off`（默认） | `on`

选择此参数可将 **Status** 设置为输出端口之一。

### **Filter coefficient** — IIR 滤波器的滤波系数 `0`（默认） | `2` | `4` | `8` | `16`

指定从 BME280 传感器读取压力和温度值时 IIR 滤波器的滤波系数。为滤波系数选择非零值有助于改善阶跃响应并消除测量值中的短期波动。

### **Stand by time** — 读取值的待机时间 `0.5`（默认） | `10` | `20` | `62.5` | `125` | `250` | `500` | `1000`

指定从 BME280 传感器读取值时处理器保持空闲（非活动持续时间）的待机时间（单位：ms）。此值的选择会影响总循环时间。

### **Pressure oversampling factor** — 测得压力值的过采样因子 `1`（默认） | `2` | `4` | `8` | `16`

指定过采样因子以降低从 BME280 传感器读取的压力值的噪声。此值是一个乘法因子，会影响测量速率和电流消耗。

### **Humidity oversampling factor** — 测得湿度值的过采样因子 `1`（默认） | `2` | `4` | `8` | `16`

指定过采样因子以降低从 BME280 传感器读取的湿度值的噪声。此值是一个乘法因子，会影响测量速率和电流消耗。

### **Temperature oversampling factor** — 测得湿度值的过采样因子 `1`（默认） | `2` | `4` | `8` | `16`

指定过采样因子以降低从 BME280 传感器读取的温度值的噪声。此值是一个乘法因子，会影响测量速率和电流消耗。

### **Data type** — BME280 传感器值的输出数据类型 `single`（默认） | `double`

指定从 BME280 传感器读取的值的输出数据类型。Raspberry Pi 板的默认数据类型是 `single`。如果需要，可使用此参数将值更改为 `double`。

### **Sample time** — 读取数据的时间间隔 `-1`（默认） | 正整数

指定此模块从 BME280 传感器读取数据的频率。将此参数设置为 -1 时，Simulink 会根据模块在模型中的上下文确定该模块的最佳采样时间。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Sensors / Environmental Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

## 描述

从 BME280 传感器测量气压、相对湿度和温度

BME280 模块输出由连接到 Raspberry Pi® 板的 BME280 传感器测得的气压和相对湿度值。该模块还输出由 BME280 传感器读取的温度。
