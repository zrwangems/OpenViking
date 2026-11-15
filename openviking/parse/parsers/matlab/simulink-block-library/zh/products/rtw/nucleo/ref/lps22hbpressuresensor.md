---
type: simulink-block
title: 'LPS22HB Pressure Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Sensors'
documentation_page: 'lps22hbpressuresensor'
documentation_source_path: 'nucleo/ref/lps22hbpressuresensor.html'
language: zh-CN
chinese_source: worker-translation
---

# LPS22HB Pressure Sensor

## 端口

### 输出

### **Pressure** — 由 LPS22HB 传感器测量的大气压力（标量）

该模块输出以帕斯卡 (Pa) 为单位的大气压力。

#### 依赖关系

仅当选择 **Pressure
(Pa)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Temperature** — 由 LPS22HB 传感器测量的温度（标量）

由连接到 Nucleo/STM32L475-Discovery 板的 LPS22HB 传感器测量的温度（单位为 ℃）。

#### 依赖关系

仅当选择 **Temperature
(℃)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Status** — 压力和温度测量的状态 `0` | `1` | `-1`

压力和温度测量的状态，指定为 1×2 向量。
`0` 表示读取的数据是新数据，`1`
表示读取的数据不是新数据，`-1` 表示未选择对应的输出。

#### 依赖关系

仅当选择 **Status**
参数时，此输出端口才会出现。

**数据类型：** `int8`

## 参数

### **I2C module** — 指定 I2C 模块 `2`（默认） | `positive integer`

指定板上的 I2C 模块。I2C 总线频率、串行时钟 (SCL) 引脚和串行数据 (SDA) 引脚根据配置参数中对应的 I2C 模块条目确定。

### **I2C address** — 用于与传感器外设通信的外设地址 `0x5C`（默认） | `0x5D`

用于与 LPS22HB 传感器通信的外设地址由硬件板上 SA0 引脚的状态决定。此表提供与该引脚及其状态对应的外设地址。

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

选择压力数据的输出数据速率，该速率还决定带宽。

### **Enable low pass filter** — 为压力数据启用低通滤波器 `off`（默认） | `on` |

启用低通滤波器以读取压力值。

### **Select the bandwidth** — 低通滤波器的带宽 `ODR/9`（默认） | `ODR/20`

选择低通滤波器所需的带宽。

#### 依赖关系

仅当选择 **Enable low pass
filter** 参数时，此参数才会出现。

### **Sample time** — 读取数据的时间间隔 `-1`（默认） | positive integer

指定此模块从 LPS22HB 传感器读取数据的频率。将此参数设置为 -1 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

从 LPS22HB 传感器测量大气压力和温度

LPS22HB Pressure Sensor 模块使用与 Nucleo/STM32L475-Discovery 板连接的 LPS22HB 压力传感器测量大气压力。该传感器包含一个用于测量绝对压力的传感元件。该模块还通过 LPS22HB Sensor 中的嵌入式温度传感器测量温度。

还可以在模块中选择输出数据速率，并使用低通滤波器选项对测得的压力值进行滤波。
