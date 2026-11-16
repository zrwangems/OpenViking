---
type: simulink-block
title: 'LIS3MDL Magnetometer Sensor'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Sensors'
documentation_page: 'lis3mdlmagnetometersensorblock'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/lis3mdlmagnetometersensorblock.html'
language: zh-CN
chinese_source: worker-translation
---

# LIS3MDL Magnetometer Sensor

## 端口

### 输出

### **Magnetic Field** — 由 LIS3MDL 传感器测得的磁场强度 行向量

由连接到STM32
Processor 的 LIS3MDL 传感器沿 x-、y- 和 z- 轴测得的磁场强度（单位：µT），指定为行向量
[x,y,z]。

#### 依赖项

仅当选择 **Magnetic Field
(µT)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Temperature** — 由 LIS3MDL 传感器测得的温度 标量

由连接到 STM32
Processor 的 LIS3MDL 传感器测得的温度（单位：℃）。

#### 依赖项

仅当选择 **Temperature
(℃)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Status** — 磁场和温度测量的状态 `-1` | `0` | `1`

磁场和温度测量的状态，指定为 1-by-2
向量。`0` 表示读取的数据是新的，
`1` 表示读取的数据不是新的，
`-1` 表示未选择相应的输出。

#### 依赖项

仅当选择
**Status** 参数时，此输出端口才会出现。

**数据类型：** `int8`

## 参数

**主选项卡**

### **I2C module** — 指定 I2C 模块 `2`（默认） | `positive integer`

指定板上的 I2C 模块。I2C 总线频率、串行时钟 (SCL)
引脚和串行数据 (SDA) 引脚根据配置参数中对应的 I2C 模块
条目获取。

### **Magnetic Field (µT)** — 设置用于读取磁场的输出端口 `on`（默认） | `off`

选择此参数以将 **Magnetic Field** 设置为
输出端口之一。

### **Temperature (℃)** — 设置用于读取温度的输出端口 `on`（默认） | `off`

选择此参数以将 **Temperature** 设置为
输出端口之一。

### **Magnetic Field Status** — 设置用于获取磁场状态的输出端口 `off`（默认） | `on`

选择此参数以将 **Magnetic Field Status** 设置为
输出端口之一。

### **Sample time** — 读取数据的时间间隔 `-1`（默认） | positive integer

指定此模块从 LIS3MDL 传感器读取数据的频率。当您
将此参数设置为 -1 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

#### 高级选项卡

### **Magnetometer range** — 用于测量磁范围的全量程 `±2g`（默认） | `±4g` | `±8g`

选择用于测量线性加速度的全量程（传感器需要测量的
加速度范围）。

### **Magnetometer output data rate** — 磁力计数据被采样的速率 `0.625 Hz`（默认） | `1.25 Hz` | `2.5 Hz` | `5 Hz` | `10 Hz` | `20 Hz` | `40 Hz` | `80 Hz`

选择磁力计数据被采样的输出数据速率。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Embedded Coder Support Package for STMicroelectronics STM32 Processors / Sensors / IMU Sensors Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

测量来自 LIS3MDL Magnetometer sensor 的磁场强度和温度

LIS3MDL Magnetometer Sensor 模块输出由连接到 STM32 processor 的 LIS3MDL Magnetometer sensor
沿 x-、y- 和 z- 轴测得的磁场强度值。该模块还输出由 LIS3MDL
Magnetometer sensor 读取的温度。
