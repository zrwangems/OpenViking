---
type: simulink-block
title: 'HTS221 Humidity Sensor'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Sensors'
documentation_page: 'hts221humiditysensorblock'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/hts221humiditysensorblock.html'
language: zh-CN
chinese_source: worker-translation
---

# HTS221 Humidity Sensor

## 端口

### 输出

### **Humidity** — 由 HTS221 传感器测得的相对湿度标量

该模块输出相对湿度，单位为百分比 (%)。

#### 依赖关系

仅当您选择 **Humidity
(%)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Temperature** — 由 HTS221 传感器测得的温度标量

由连接到 STM32
Processors 的 HTS221 传感器测得的温度（单位为 ℃）。

#### 依赖关系

仅当您选择 **Temperature
(℃)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Status** — 压力和温度测量状态 `0` | `1` | `-1`

压力和温度测量状态，指定为 1×2 向量。`0` 表示读取的数据是新的，`1` 表示读取的数据不是新的，`-1` 表示未选择相应输出。

#### 依赖关系

仅当您选择
**Status** 参数时，此输出端口才会出现。

**数据类型：** `int8`

## 参数

### **I2C module** — I2C 通信模块 `0`（默认）| 标量

指定 STM32 Processors 上用于与传感器外设通信的 I2C 模块。

### **I2C address** — 用于与传感器通信的外设地址 `0x5F`（默认）| 标量

HTS221 传感器与 STM32
Processors 通信的外设地址。

### **Humidity (%)** — 设置用于读取湿度的输出端口 `on`（默认）| `off`

选择此参数以将 **Humidity** 设置为输出端口之一。

### **Temperature (℃)** — 设置用于读取温度的输出端口 `on`（默认）| `off`

选择此参数以将 **Temperature** 设置为输出端口之一。

### **Status** — 设置用于获取状态的输出端口 `off`（默认）| `on`

选择此参数以将 **Status** 设置为输出端口之一。

### **Output data rate (ODR)** — 湿度和温度数据的采样速率 `1 Hz`（默认）| `7 Hz` | `12.5 Hz`

选择对湿度数据进行采样的输出数据速率。

### **Sample time** — 读取数据的时间间隔 `-1`（默认）| 正整数

指定此模块从 HTS221 传感器读取数据的频率。将此参数设置为 -1 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Embedded Coder Support Package for STMicroelectronics STM32 Processors / Sensors / Environmental Sensors Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Sensors Simulink Support Package for Arduino Hardware / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

测量来自 HTS221 传感器的相对湿度和温度

HTS221 Humidity Sensor 模块使用与 STM32 Processors 接口的 HTS221 湿度传感器测量相对湿度和环境温度。该传感器包含一个用于测量相对湿度和温度的传感元件。

您还可以在模块中为测量值选择输出数据速率。
