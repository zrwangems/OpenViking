---
type: simulink-block
title: 'HTS221 Humidity Sensor'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32L475VG-Discovery (B-L475E-IOT01A) Board Blocks / Sensors'
documentation_page: 'hts221humiditysensor'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/hts221humiditysensor.html'
language: zh-CN
chinese_source: worker-translation
---

# HTS221 Humidity Sensor

## 端口

### 输出

### **Humidity** — 由 HTS221 传感器测得的相对湿度标量

该模块输出以百分比 (%) 表示的相对湿度。

#### 依赖关系

仅当选择 **Humidity (%)** 参数时，才会出现此输出端口。

**数据类型：** `double`

### **Temperature** — 由 HTS221 传感器测得的温度标量

#### 依赖关系

仅当选择 **Temperature (℃)** 参数时，才会出现此输出端口。

**数据类型：** `double`

### **Status** — 压力和温度测量状态 `0` | `1` | `-1`

压力和温度测量状态，指定为 1×2 向量。
`0` 表示读取的数据是新的，`1`
表示读取的数据不是新的，`-1` 表示未选择相应的输出。

#### 依赖关系

仅当选择 **Status** 参数时，才会出现此输出端口。

**数据类型：** `int8`

## 参数

### **Use onboard sensors** — 启用以使用板载传感器 `on`（默认） | `off`

选择此参数以使用板载传感器。

**注意**

此参数仅适用于 STM32L475VG-Discovery (B-L475E-IOT01A) 开发板。

### **I2C module** — 指定 I2C 模块 `2`（默认） | `positive integer`

指定开发板上的 I2C 模块。I2C 总线频率、串行时钟 (SCL) 引脚和串行数据 (SDA) 引脚根据配置参数中对应的 I2C 模块条目进行获取。

#### 依赖关系

要启用此参数，请取消选择 **Use onboard sensors** 参数。

### **Humidity (%)** — 设置用于读取湿度的输出端口 `on`（默认） | `off`

选择此参数以将 **Humidity** 设置为输出端口之一。

### **Temperature (℃)** — 设置用于读取温度的输出端口 `on`（默认） | `off`

选择此参数以将 **Temperature** 设置为输出端口之一。

### **Status** — 设置用于获取状态的输出端口 `off`（默认） | `on`

选择此参数以将 **Status** 设置为输出端口之一。

### **Output data rate (ODR)** — 湿度和温度数据的采样速率 `1 Hz`（默认） | `7 Hz` | `12.5 Hz`

选择对湿度数据进行采样的输出数据速率。

### **Sample time** — 读取数据的时间间隔 `-1`（默认） | positive integer

指定此模块从 HTS221 传感器读取数据的频率。将此参数设置为 -1 时，Simulink 将根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Embedded Coder Support Package for STMicroelectronics STM32 Processors / Sensors / Environmental Sensors Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Sensors Simulink Support Package for Arduino Hardware / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

测量来自 HTS221 传感器的相对湿度和温度

HTS221 Humidity Sensor 模块使用与 Nucleo/STM32L475-Discovery 开发板连接的 HTS221 湿度传感器测量相对湿度和环境温度。此传感器包含一个用于测量相对湿度和温度的传感元件。

您还可以在模块中为测量值选择输出数据速率。
