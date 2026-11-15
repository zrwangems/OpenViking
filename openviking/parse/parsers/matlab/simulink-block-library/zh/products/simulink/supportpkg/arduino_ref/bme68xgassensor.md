---
type: simulink-block
title: 'BME68x Gas Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Environmental Sensors'
documentation_page: 'bme68xgassensor'
documentation_source_path: 'supportpkg/arduino_ref/bme68xgassensor.html'
language: zh-CN
chinese_source: worker-translation
---

# BME68x Gas Sensor

## 端口

### 输出

### **Pressure** — 气压标量

该模块输出气压，单位为 Pascal (Pa)。

#### 依赖关系

该输出端口仅在您选择 **Pressure (Pa)** 参数时出现。

**数据类型：** `single`

### **Temperature** — 环境温度标量

该模块输出环境温度，单位为 ℃。

#### 依赖关系

该输出端口仅在您选择 **Temperature (℃)** 参数时出现。

**数据类型：** `single`

### **Humidity** — 相对湿度标量

该模块输出相对湿度，单位为 `%`。

#### 依赖关系

该输出端口仅在您选择 **Humidity (%)** 参数时出现。

**数据类型：** `single`

### **IAQ** — 空气质量指数标量

该模块以 parts per million (ppm) 为单位输出室内空气质量指数。

#### 依赖关系

该输出端口仅在您选择 **IAQ** 参数时出现。

**数据类型：** `single`

### **IAQStatus** — IAQ 值的状态 `0` | `1`

该模块输出室内空气质量指数测量的状态。`0` 表示读取的 IAQ 数据是新的，`1` 表示读取的 IAQ 数据不是新的。

#### 依赖关系

该输出端口仅在您选择 **IAQ** 和 **IAQStatus** 参数时出现。

**数据类型：** `uint8`

### **eCO2** — 等效 CO2 标量

**eCO2** 端口以 parts per million (ppm) 为单位输出室内空气的等效 CO2 值。

#### 依赖关系

该输出端口仅在您选择 **eCO2** 参数时出现。

**数据类型：** `single`

### **bVOC** — 呼吸挥发性有机化合物浓度标量

**bVOC** 端口以 parts per million (ppm) 为单位输出室内空气的等效呼吸挥发性有机化合物浓度。

#### 依赖关系

该输出端口仅在您选择 **bVOC** 参数时出现。

**数据类型：** `single`

## 参数

### **I2C module** — I2C 通信模块 `0` (默认) | scalar

指定 Arduino 硬件上用于与传感器外设通信的 I2C 模块。有关 Arduino 引脚映射以及硬件板支持的模块的详细信息，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

### **I2C address** — 用于与传感器外设通信的 I2C 地址 `0x77` (默认) | `0x76`

与 BME68x 传感器上的外设通信的 I2C 地址由 Arduino Mega 2560 板上 SD0 引脚的状态决定。下表提供了与引脚及其状态对应的 I2C 地址。

| 引脚名称 | 引脚状态 | I2C 地址 |
| --- | --- | --- |
| SD0 | 0 | 0x76 |
| 1 | 0x77 |

### **Mode** — 传感器的功耗模式 `Low power (ODR = 0.33Hz)` (默认) | `Continuous (ODR = 1Hz)` | `Ultra low power (ODR = 3.3mHz)`

根据您使用的电源选择传感器的功耗模式。

### **Pressure (Pa)** — 设置用于读取气压的输出端口 `on` (默认) | `off`

选择此参数可将 **Pressure** 设置为输出端口之一。

### **Temperature (℃)** — 设置用于读取温度的输出端口 `on` (默认) | `off`

选择此参数可将 **Temperature** 设置为输出端口之一。

### **Humidity(%)** — 设置用于读取湿度的输出端口 `on` (默认) | `off`

选择此参数可将 **Humidity** 设置为输出端口之一。

### **IAQ** — 设置用于读取空气质量指数的输出端口 `on` (默认) | `off`

选择此参数可将 **IAQ** 设置为输出端口之一。

### **IAQStatus** — 设置用于读取 IAQ 状态的输出端口 `off` (默认) | `on`

选择此参数可将 **IAQStatus** 设置为输出端口之一。

### **eCO2** — 设置用于读取等效二氧化碳浓度的输出端口 `off` (默认) | `on`

选择此参数可将 **eCO2** 设置为输出端口之一。

### **bVOC** — 设置用于读取呼吸挥发性有机化合物浓度的输出端口 `off` (默认) | `on`

选择此参数可将 **bVOC** 设置为输出端口之一。

### **Sample time** — 读取数据的时间间隔 `-1` (默认) | positive integer

指定此模块从 BME68x 传感器读取数据的频率。将此参数设置为 -1 时，Simulink 会根据模型中的模块上下文确定此模块的最佳采样时间。

## 所属库

Simulink Support Package for Arduino Hardware / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2022b 中引入**

## 描述

从 BME68x 传感器测量气压、相对湿度、环境温度、IAQ、eCO2 和 bVOC

BME68x Gas Sensor 模块使用与 Arduino® Mega 2560 板连接的 BME68x Gas sensor，测量气压、相对湿度、环境温度、空气质量指数 (IAQ)、空气质量指数状态 (IAQStatus)、等效二氧化碳浓度 (eCO2) 和呼吸挥发性有机化合物浓度 (bVOC)。

**注意**

BME68x Gas sensor 仅支持从 Arduino Mega 2560 板读取数据。

**注意**

BME68x Gas Sensor 大约需要 `5` 分钟才能输出空气质量指数 (IAQ) 的值。
