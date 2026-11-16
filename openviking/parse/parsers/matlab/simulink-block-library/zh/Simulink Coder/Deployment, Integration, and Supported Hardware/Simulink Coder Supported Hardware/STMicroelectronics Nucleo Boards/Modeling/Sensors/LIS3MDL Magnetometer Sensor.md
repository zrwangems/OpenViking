---
type: simulink-block
title: 'LIS3MDL Magnetometer Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Sensors'
documentation_page: 'lis3mdlmagnetometersensor'
documentation_source_path: 'nucleo/ref/lis3mdlmagnetometersensor.html'
language: zh-CN
chinese_source: worker-translation
---

# LIS3MDL Magnetometer Sensor

## 端口

### 输出

### **Magnetic Field** — 由 LIS3MDL 传感器测量的磁场强度行向量

由连接到 Nucleo/STM32L475-Discovery 板的 LIS3MDL 传感器测量的磁场强度（以 µT 为单位），沿 x、y 和 z 轴，指定为行向量 [x,y,z]。

#### 依赖关系

此输出端口仅在您选择 **Magnetic Field (µT)** 参数时出现。

**数据类型：** `double`

### **Temperature** — 由 LIS3MDL 传感器测量的温度标量

由连接到 Nucleo/STM32L475-Discovery 板的 LIS3MDL 传感器测量的温度（以 ℃ 为单位）。

#### 依赖关系

此输出端口仅在您选择 **Temperature (℃)** 参数时出现。

**数据类型：** `double`

### **Status** — 磁场和温度测量的状态 `-1` | `0` | `1`

磁场和温度测量的状态，指定为 1×2 向量。`0` 表示读取的数据是新数据，`1` 表示读取的数据不是新数据，`-1` 表示未选择相应的输出。

#### 依赖关系

此输出端口仅在您选择 **Status** 参数时出现。

**数据类型：** `int8`

## 参数

**主选项卡**

### **I2C module** — 指定 I2C 模块 `2`（默认）| `positive integer`

指定板上的 I2C 模块。I2C 总线频率、串行时钟（SCL）引脚和串行数据（SDA）引脚根据配置参数中相应的 I2C module 条目获取。

### **Magnetic Field (µT)** — 设置用于读取磁场的输出端口 `on`（默认）| `off`

选择此参数可将 **Magnetic Field** 设置为输出端口之一。

### **Temperature (℃)** — 设置用于读取温度的输出端口 `on`（默认）| `off`

选择此参数可将 **Temperature** 设置为输出端口之一。

### **Magnetic Field Status** — 设置用于获取磁场状态的输出端口 `off`（默认）| `on`

选择此参数可将 **Magnetic Field Status** 设置为输出端口之一。

### **Sample time** — 读取数据的时间间隔 `-1`（默认）| positive integer

指定此模块读取 LIS3MDL 传感器数据的频率。当您将此参数设置为 -1 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

#### 高级选项卡

### **Magnetometer range** — 用于测量磁范围的满量程 `±2g`（默认）| `±4g` | `±8g`

选择用于测量线性加速度的满量程（传感器需要测量的加速度范围）。

### **Magnetometer output data rate** — 采样磁力计数据的速率 `0.625 Hz`（默认）| `1.25 Hz` | `2.5 Hz` | `5 Hz` | `10 Hz` | `20 Hz` | `40 Hz` | `80 Hz`

选择采样磁力计数据时的输出数据速率。

## 所属库

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

从 LIS3MDL Magnetometer sensor 测量磁场强度和温度

LIS3MDL Magnetometer Sensor 模块输出由连接到 Nucleo/STM32L475-Discovery 板的 LIS3MDL Magnetometer sensor 测量的沿 x、y 和 z 轴的磁场强度值。该模块还输出由 LIS3MDL Magnetometer sensor 读取的温度。
