---
type: simulink-block
title: 'BMP280 Pressure Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sensors / Environmental Sensors'
documentation_page: 'bmp280pressuresensor'
documentation_source_path: 'supportpkg/raspberrypi_ref/bmp280pressuresensor.html'
language: zh-CN
chinese_source: worker-translation
---

# BMP280 Pressure Sensor

## 端口

### 输出

### **Pressure** — 大气压标量

该模块输出以 Pascal (Pa) 为单位的大气压。

#### 依赖关系

仅当您选择 **Pressure
(Pa)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Temperature** — 环境温度标量

该模块输出以 ℃ 为单位的环境温度。

#### 依赖关系

仅当您选择 **Temperature
(℃)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Status** — 压力和温度读取值的状态 `0` | `1`

该模块输出大气压和环境温度测量的状态。`0` 表示读取的数据是新数据，
`1` 表示读取的数据不是新数据。

#### 依赖关系

仅当您选择 **Status**
参数时，此输出端口才会出现。

**数据类型：** `uint8`

## 参数

### **I2C Module** — 用于 I2C 通信的特定模块 `1` (默认)

指定板上用于 I2C 通信的模块。

### **I2C address** — 用于与 BMP280 传感器通信的 I2C 地址 `0x76` (默认) | `0x77`

用于与 BMP280 传感器上的加速度计外设通信的 I2C 地址由硬件板上的 SDO 引脚状态决定。此表提供了对应引脚及其状态的 I2C 地址。

| 引脚名称 | 引脚状态 | I2C address |
| --- | --- | --- |
| SDO | 0 | 0x76 |
| 1 | 0x77 |

### **Pressure (Pa)** — 设置用于读取压力的输出端口 `on` (默认) | `off`

选择此参数可将 **Pressure** 设置为输出端口之一。

### **Temperature (℃)** — 设置用于读取温度的输出端口 `on` (默认) | `off`

选择此参数可将 **Temperature** 设置为输出端口之一。

### **Status** — 设置用于获取所选输出状态的输出端口 `on` (默认) | `off`

选择此参数可将 **Status** 设置为输出端口之一。

### **Data type** — 来自 BMP280 传感器值的输出数据类型 `double` (默认) | `single` | `uint32`

选择模块从中读取值的传感器的输出数据类型。Raspberry Pi 硬件的默认数据类型为 `double`。如果需要，可使用此参数将这些值更改为 `double` 或 `uint32`。

### **Sample time** — 读取数据的时间间隔 `-1` (默认) | 正整数

指定此模块从 BMP280 传感器读取数据的频率。将此参数设置为 -1 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

### IIR 滤波器设置

### **Filter coeffiecient** — 滤波器系数值 `0` (默认) | `2` | `4` | `8` | `16`

选择传感器的滤波器系数值，这有助于降低输出信号的带宽。

Raspberry Pi 硬件的默认滤波器系数值为 `0`。如果需要，可使用此参数更改这些值。

启用滤波器后，传感器使用以下公式进行最新测量计算。

`dt = (dadc / f) +
dt-1 (1 - 1 / f)`，其中
`dt` 是当前数据，
`dt-1` 是前一数据，
`dadc` 是预滤波数据，并且
`f` 是滤波器系数。

### 灵敏度

### **Pressure sensitivity factor (Pa)** — 压力灵敏度因子 `2.62` (默认) | `1.31` | `0.66` | `0.33` | `0.16`

选择压力灵敏度因子，传感器在气压变化时使用该因子读取值。

Raspberry Pi 硬件的默认数据类型为 `2.62`。如果需要，可使用此参数更改这些值。

### **Temperature sensitivity factor (℃)** — 温度灵敏度因子 `0.005` (默认) | `0.0025`

选择温度灵敏度因子，传感器在温度条件变化时使用该因子读取值。

Raspberry Pi 硬件的默认数据类型为 `0.005`。如果需要，可使用此参数更改这些值。

## 所属库

Simulink Support Package for Arduino Hardware / Sensors Simulink Support Package for Raspberry Pi Hardware / Sensors / Environmental Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2022b 中引入**

## 描述

从 BMP280 传感器测量大气压和环境温度

BMP280 Pressure Sensor 模块使用与 Raspberry Pi® 板连接的 BMP280 压力传感器测量大气压和环境温度。
