---
type: simulink-block
title: 'LPS22HB Pressure Sensor'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32L475VG-Discovery (B-L475E-IOT01A) Board Blocks / Sensors'
documentation_page: 'lps22hbpressuresensor'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/lps22hbpressuresensor.html'
language: zh-CN
chinese_source: worker-translation
---

# LPS22HB Pressure Sensor

## 端口

### 输出

### **Pressure** — 由 LPS22HB 传感器测量的大气压力标量

该模块输出大气压力，单位为 Pascals (Pa)。

#### 依赖项

仅当您选择 **Pressure (Pa)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Temperature** — 由 LPS22HB 传感器测量的温度标量

由连接到 Nucleo/STM32L475-Discovery 板的 LPS22HB 传感器测量的温度（单位为 ℃）。

#### 依赖项

仅当您选择 **Temperature (℃)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Status** — 压力和温度测量状态 `0` | `1` | `-1`

压力和温度测量状态，指定为 1×2 向量。
`0` 表示读取的数据是新数据，`1` 表示读取的数据不是新数据，`-1` 表示未选择对应输出。

#### 依赖项

仅当您选择 **Status** 参数时，此输出端口才会出现。

**数据类型：** `int8`

## 参数

### **Use onboard sensors** — 启用以使用板载传感器 `on`（默认）| `off`

选择此参数以使用板载传感器。

**注意**

此参数仅适用于 STM32L475VG-Discovery (B-L475E-IOT01A) 板。

### **I2C module** — 指定 I2C 模块 `2`（默认）| `positive integer`

指定板上的 I2C 模块。I2C 总线频率、串行时钟 (SCL) 引脚和串行数据 (SDA) 引脚根据配置参数中对应的 I2C 模块条目获取。

#### 依赖项

要启用此参数，请取消选择 **Use onboard sensors** 参数。

### **I2C address** — 用于与传感器外设通信的外设地址 `0x5C`（默认）| `0x5D`

用于与 LPS22HB 传感器通信的外设地址由硬件板上 SA0 引脚的状态决定。下表提供了与该引脚及其状态对应的外设地址。

| 引脚名称 | 引脚状态 | 外设地址 |
| --- | --- | --- |
| SA0 | 0 | 0x5C |
| 1 | 0x5D |

#### 依赖项

要启用此参数，请取消选择 **Use onboard sensors** 参数。

### **Pressure (Pa)** — 设置用于读取压力的输出端口 `on`（默认）| `off`

选择此参数以将 **Pressure** 设置为输出端口之一。

### **Temperature (℃)** — 设置用于读取温度的输出端口 `on`（默认）| `off`

选择此参数以将 **Temperature** 设置为输出端口之一。

### **Status** — 设置用于获取状态的输出端口 `off`（默认）| `on`

选择此参数以将 **Status** 设置为输出端口之一。

### **Output data rate (ODR)** — 压力数据采样速率 `1 Hz`（默认）| `10 Hz` | `25 Hz` | `50 Hz` | `75 Hz`

选择压力数据的输出数据速率，该速率也决定带宽。

### **Enable low pass filter** — 为压力数据启用低通滤波器 `off`（默认）| `on` |

启用低通滤波器以读取压力值。

### **Select the bandwidth** — 低通滤波器的带宽 `ODR/9`（默认）| `ODR/20`

选择低通滤波器所需的带宽。

#### 依赖项

仅当您选择 **Enable low pass filter** 参数时，此参数才会出现。

### **Sample time** — 读取数据的时间间隔 `-1`（默认）| positive integer

指定此模块从 LPS22HB 传感器读取数据的频率。将此参数设置为 -1 时，Simulink 根据模型中的模块上下文确定模块的最佳采样时间。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Embedded Coder Support Package for STMicroelectronics STM32 Processors / Sensors / Environmental Sensors Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Sensors Simulink Support Package for Arduino Hardware / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

测量来自 LPS22HB 传感器的大气压力和温度

LPS22HB Pressure Sensor 模块使用与 Nucleo/STM32L475-Discovery 板连接的 LPS22HB 压力传感器测量大气压力。此传感器包括一个用于测量绝对压力的传感元件。该模块还从 LPS22HB Sensor 中的嵌入式温度传感器测量温度。

您还可以在模块中选择输出数据速率，并使用低通滤波器选项对测得的压力值进行滤波。
