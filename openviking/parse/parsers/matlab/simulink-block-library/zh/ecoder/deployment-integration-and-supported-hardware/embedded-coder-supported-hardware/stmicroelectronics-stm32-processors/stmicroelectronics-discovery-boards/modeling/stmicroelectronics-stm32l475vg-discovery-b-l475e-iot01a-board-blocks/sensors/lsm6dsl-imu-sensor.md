---
type: simulink-block
title: 'LSM6DSL IMU Sensor'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32L475VG-Discovery (B-L475E-IOT01A) Board Blocks / Sensors'
documentation_page: 'lsm6dslimusensor'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/lsm6dslimusensor.html'
language: zh-CN
chinese_source: worker-translation
---

# LSM6DSL IMU Sensor

## 端口

### 输出

您可以选择活动传感器来测量角速度、加速度、温度或这些测量的组合。

### **Acceleration** — 由加速度计测量的沿每个轴的加速度向量

模块将加速度输出为 `1`-by-`3` 向量。每个值表示沿 X、Y 和 Z 轴以 `m/s^2` 为单位的加速度测量值。

#### 依赖关系

此输出端口仅在您选择 **Acceleration (m/s2)** 参数时出现。

**数据类型：** `double`

### **Angular Velocity** — 由陀螺仪测量的沿每个轴的角速度向量

模块将角速度输出为 `1`-by-`3` 向量。每个值表示沿 X、Y 和 Z 轴以弧度每秒 (rad/s) 为单位的角速度测量值。

#### 依赖关系

此输出端口仅在您选择 **Angular Velocity (rad/s)** 参数时出现。

**数据类型：** `double`

### **Temperature** — 由 LSM6DSL 传感器测量的温度标量

由连接到 Nucleo/STM32L475-Discovery 板的 LSM6DSL 传感器测量的温度（单位为 ℃）。

#### 依赖关系

此输出端口仅在您选择 **Temperature (℃)** 参数时出现。

**数据类型：** `double`

### **Status** — 加速度、角速度和温度测量的状态 `-1` | `0` | `1`

加速度、角速度和温度测量的状态，指定为 1-by-3 向量。`0` 表示读取的数据是新数据，`1` 表示读取的数据不是新数据，`-1` 表示未选择对应输出。

#### 依赖关系

此输出端口仅在您选择 **Status** 参数时出现。

**数据类型：** `int8`

## 参数

### 主要

### **Use onboard sensors** — 启用后使用板载传感器 `on` (default) | `off`

选择此参数以使用板载传感器。

**注意**

此参数仅适用于 STM32L475VG-Discovery (B-L475E-IOT01A) 板。

### **I2C module** — 指定 I2C 模块 `2` (default) | `positive integer`

指定板上的 I2C 模块。I2C 总线频率、串行时钟 (SCL) 引脚和串行数据 (SDA) 引脚根据配置参数中对应的 I2C 模块条目确定。

#### 依赖关系

要启用此参数，请取消选择 **Use onboard sensors** 参数。

### **I2C address** — 用于与传感器外设通信的外设地址 `0x6A` (default) | `0x6B`

用于与 LSM6DSL 传感器上的加速度计和陀螺仪外设通信的外设地址由硬件板上 SDO/SA0 引脚的状态决定。下表提供了该引脚及其状态对应的外设地址。

| 引脚名称 | 引脚状态 | 外设地址 |
| --- | --- | --- |
| SDO/SA0 | 0 | 0x6A |
| 1 | 0x6B |

#### 依赖关系

要启用此参数，请取消选择 **Use onboard sensors** 参数。

### **Acceleration (m/s2)** — 设置用于读取加速度的输出端口 `on` (default) | `off`

选择此参数可将 **Acceleration** 设置为输出端口之一。

### **Angular Velocity (rad/s)** — 设置用于读取角速度的输出端口 `on` (default) | `off`

选择此参数可将 **Angular Velocity** 设置为输出端口之一。

### **Temperature (℃)** — 设置用于读取温度的输出端口 `on` (default) | `off`

选择此参数可将 **Temperature** 设置为输出端口之一。

### **Status** — 设置用于获取所选输出状态的输出端口 `off` (default) | `on`

选择此参数可将 **Status** 设置为输出端口之一。

### **Sample time** — 读取数据的时间间隔 `-1` (default) | positive integer

指定此模块从 LSM6DSL 传感器读取数据的频率。将此参数设置为 -1 时，Simulink 会根据模块在模型中的上下文确定模块的最佳采样时间。

### 高级

#### 加速度计

### **Full scale range** — 用于测量线性加速度的满量程 `±2g` (default) | `±4g` | `±8g` | `±16g`

选择用于测量线性加速度的满量程（传感器需要测量的加速度范围）。

### **Output data rate** — 加速度计数据的采样速率 `12.5 Hz` (default) | `26 Hz` | `52 Hz` | `104 Hz` | `208 Hz` | `416 Hz` | `833 Hz` | `1666 Hz` | `3332 Hz` | `6664 Hz`

选择加速度计数据采样的输出数据速率，这也决定带宽。

### **Digital low pass filter bandwidth** — 低通数字滤波器的带宽 `ODR/2` (default) | `ODR/4`

选择低通数字滤波器所需的带宽。

### **Select composite filter** — 滤波链中使用的复合滤波器 `No filter` (default) | `High pass filter` | `Low pass filter`

选择用于读取加速度计值的滤波链中使用的复合滤波器类型。

### **High pass filter bandwidth** — 高通滤波器的带宽 `ODR/100` (default) | `ODR/9` | `ODR/400`

选择滤波链中所用复合滤波器内高通滤波器所需的带宽。

#### 依赖关系

此参数仅在您在 **Select composite filter** 参数中选择 `High pass filter` 时出现。

### **Low pass filter bandwidth** — 低通滤波器的带宽 `ODR/50` (default) | `ODR/100` | `ODR/9` | `ODR/400`

选择滤波链中所用复合滤波器内低通滤波器所需的带宽。

#### 依赖关系

此参数仅在您在 **Select composite filter** 参数中选择 `Low pass filter` 时出现。

#### 陀螺仪

### **Full scale range** — 用于测量角速度的满量程 `250 dps` (default) | `125 dps` | `500 dps` | `1000 dps` | `2000 dps`

选择用于测量角速度的满量程（传感器需要测量的角速度范围）。

### **Output data rate** — 陀螺仪数据的采样速率 `12.5 Hz` (default) | `26 Hz` | `52 Hz` | `104 Hz` | `208 Hz` | `416 Hz` | `833 Hz` | `1666 Hz` | `3332 Hz` | `6664 Hz`

选择陀螺仪数据采样的输出数据速率，这也决定带宽。

### **Enable high pass filter** — 为陀螺仪数据启用高通滤波器 `off` (default) | `on` |

启用高通滤波器以读取陀螺仪值。

### **High pass filter bandwidth** — 高通滤波器的带宽 `0.016 Hz` (default) | `0.065 Hz` | `0.260 Hz` | `1.04 Hz`

选择用于读取陀螺仪值的高通滤波器所需的带宽。

#### 依赖关系

此参数仅在您选择 **Enable high pass filter** 参数时出现。

### **Enable low pass filter** — 为陀螺仪数据启用低通滤波器 `off` (default) | `on` |

启用低通滤波器以读取陀螺仪值。

### **Low pass filter bandwidth mode** — 低通滤波器的带宽模式 `0` (default) | `1` | `2` | `3`

选择用于读取陀螺仪值的低通滤波器所需的带宽模式。

#### 依赖关系

此参数仅在您选择 **Enable low pass filter** 参数时出现。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Embedded Coder Support Package for STMicroelectronics STM32 Processors / Sensors / IMU Sensors Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Sensors Simulink Support Package for Arduino Hardware / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

从 LSM6DSL 传感器测量线性加速度、角速率和温度

LSM6DSL IMU Sensor 模块使用与 Nucleo/STM32L475-Discovery 板连接的 LSM6DSL Inertial Measurement Unit (IMU) 传感器，测量沿 X、Y 和 Z 轴的线性加速度和角速率。此 6-Degree of Freedom (DoF) IMU 传感器包括加速度计和陀螺仪，分别用于测量线性加速度和角速率。该模块还测量 LSM6DSL Sensor 中嵌入式温度传感器的温度。

您还可以对加速度计值使用模块中的复合滤波器选项，并对陀螺仪值使用高通和低通滤波器选项。
