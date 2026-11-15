---
type: simulink-block
title: 'HTS221 Humidity Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Sensors'
documentation_page: 'hts221humiditysensor'
documentation_source_path: 'nucleo/ref/hts221humiditysensor.html'
language: zh-CN
chinese_source: worker-translation
---

# HTS221 Humidity Sensor

## 端口

### 输出

### **Humidity** — 由 HTS221 传感器测量的相对湿度 标量

此模块输出相对湿度，单位为百分比 (%)。

#### 依赖关系

仅当选择 **Humidity
(%)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Temperature** — 由 HTS221 传感器测量的温度 标量

#### 依赖关系

仅当选择 **Temperature
(℃)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Status** — 压力和温度测量的状态 `0` | `1` | `-1`

压力和温度测量的状态，指定为 1×2 向量。
`0` 表示读取的数据是新的，`1`
表示读取的数据不是新的，`-1` 表示未选择对应的输出。

#### 依赖关系

仅当选择 **Status**
参数时，此输出端口才会出现。

**数据类型：** `int8`

## 参数

### **I2C 模块** — 指定 I2C 模块 `2`（默认）| `positive integer`

指定板上的 I2C 模块。I2C 总线频率、串行时钟 (SCL) 引脚和串行数据 (SDA) 引脚根据配置参数中对应的 I2C 模块条目获取。

### **Humidity (%)** — 设置用于读取湿度的输出端口 `on`（默认）| `off`

选择此参数可将 **Humidity** 设置为其中一个输出端口。

### **Temperature (℃)** — 设置用于读取温度的输出端口 `on`（默认）| `off`

选择此参数可将 **Temperature** 设置为其中一个输出端口。

### **Status** — 设置用于获取状态的输出端口 `off`（默认）| `on`

选择此参数可将 **Status** 设置为其中一个输出端口。

### **输出数据速率 (ODR)** — 湿度和温度数据的采样速率 `1 Hz`（默认）| `7 Hz` | `12.5 Hz`

选择对湿度数据进行采样的输出数据速率。

### **采样时间** — 读取数据的时间间隔 `-1`（默认）| positive integer

指定此模块从 HTS221 传感器读取数据的频率。将此参数设置为 -1 时，Simulink 将根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

从 HTS221 传感器测量相对湿度和温度

HTS221 Humidity Sensor 模块使用与 Nucleo/STM32L475-Discovery 板连接的 HTS221 湿度传感器来测量相对湿度和环境温度。该传感器包含一个用于测量相对湿度和温度的传感元件。

您还可以在模块中为测量值选择输出数据速率。
