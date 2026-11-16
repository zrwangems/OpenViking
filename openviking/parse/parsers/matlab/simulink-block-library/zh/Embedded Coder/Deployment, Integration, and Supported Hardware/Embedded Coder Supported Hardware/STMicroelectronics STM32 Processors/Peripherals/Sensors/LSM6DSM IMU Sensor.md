---
type: simulink-block
title: 'LSM6DSM IMU Sensor'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Sensors'
documentation_page: 'lsm6dsmimusensor'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/lsm6dsmimusensor.html'
language: zh-CN
chinese_source: worker-translation
---

# LSM6DSM IMU Sensor

## 端口

### 输出

您可以选择要测量的活动传感器，以测量角速度、加速度、温度或这些测量的组合。

### **Acceleration** — 由加速度计测量的沿每个轴的加速度向量

模块输出加速度为一个 `n`×3 向量，其中 `n` 是每帧采样数的值。每个值表示沿 *X*、*Y* 和 *Z* 轴的加速度测量值，单位为 `m/s^2`。

#### 依赖关系

仅当选择 **Acceleration (m/s2)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Angular Velocity** — 由陀螺仪测量的沿每个轴的角速度向量

模块输出角速度为一个 `n`×3 向量，其中 `n` 是每帧采样数的值。每个值表示沿 *X*、*Y* 和 *Z* 轴的角速度测量值，单位为弧度每秒 (rad/s)。

#### 依赖关系

仅当选择 **Angular Velocity (rad/s)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Temperature** — LSM6DSM 传感器测量的温度标量

由连接到 STM32 Processors 的 LSM6DSM 传感器测量的温度（单位：℃）。

#### 依赖关系

仅当选择 **Temperature (℃)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Status** — 加速度、角速度和温度测量的状态 `-1` | `0` | `1`

加速度、角速度和温度测量的状态，指定为 1×3 向量。`0` 表示读取的数据是新的，`1` 表示读取的数据不是新的，`-1` 表示未选择对应的输出。

#### 依赖关系

仅当选择 **Status** 参数时，此输出端口才会出现。

**数据类型：** `int8`

### **Timestamp** — 读取数据时的时间戳 矩阵 | (`n`)×1

从传感器读取数据时的时间戳（单位：秒），返回为 `n`×1 矩阵，其中 `n` 是指定为 Samples per frame 的值。

#### 依赖关系

仅当选择 **Timestamp** 参数时，此输出端口才会出现。

**数据类型：** `double`

## 参数

### 主要

### **I2C 模块** — I2C 通信模块 `I2C1`（默认） | 标量

指定 STM32 Processors 上用于与传感器外设通信的 I2C 模块。

### **I2C 地址** — 用于与传感器通信的外设地址 `0x6A`（默认） | `0x6B`

用于与 LSM6DSM 传感器上的加速度计和陀螺仪外设通信的外设地址由硬件板上的 SDO/SA0 引脚状态决定。此表提供了与该引脚及其状态对应的外设地址。

| 引脚名称 | 引脚状态 | 外设地址 |
| --- | --- | --- |
| SDO/SA0 | 0 | 0x6A |
| 1 | 0x6B |

### **Acceleration (m/s2)** — 设置用于读取加速度的输出端口 `on`（默认） | `off`

选择此参数可将 **Acceleration** 设置为输出端口之一。

### **Angular Velocity (rad/s)** — 设置用于读取角速度的输出端口 `on`（默认） | `off`

选择此参数可将 **Angular Velocity** 设置为输出端口之一。

### **Temperature (℃)** — 设置用于读取温度的输出端口 `on`（默认） | `off`

选择此参数可将 **Temperature** 设置为输出端口之一。

### **Status** — 设置用于获取所选输出状态的输出端口 `off`（默认） | `on`

选择此参数可将 **Status** 设置为输出端口之一。

### **Timestamp** — 设置用于获取时间戳的输出端口 `off`（默认） | `on`

选择此参数可将 **Timestamp** 设置为输出端口之一。

### **采样时间** — 读取数据的时间间隔 `-1`（默认） | 正整数

指定此模块从 LSM6DSM 传感器读取数据的频率。当您将此参数设置为 -1 时，Simulink® 会根据模型中的模块上下文确定模块的最佳采样时间。输出采样时间是您指定的 `Sample time` 的乘积。

### 高级

#### 加速度计

### **满量程范围** — 测量线性加速度的满量程 `±2g`（默认） | `±4g` | `±8g` | `±16g`

选择用于测量线性加速度的满量程（传感器需要测量的加速度范围）。

### **输出数据速率** — 加速度计数据的采样速率 `12.5 Hz`（默认） | `26 Hz` | `52 Hz` | `104 Hz` | `208 Hz` | `416 Hz` | `833 Hz` | `1666 Hz` | `3332 Hz` | `6664 Hz`

选择加速度计数据的采样输出数据速率，这也决定了带宽。

### **数字低通滤波器带宽** — 低通数字滤波器的带宽 `ODR/2`（默认） | `ODR/4`

选择低通数字滤波器所需的带宽。

### **选择复合滤波器** — 滤波链中使用的复合滤波器 `No filter`（默认） | `High pass filter` | `Low pass filter`

选择用于读取加速度计值的滤波链中使用的复合滤波器类型。

### **高通滤波器带宽** — 高通滤波器的带宽 `ODR/100`（默认） | `ODR/9` | `ODR/400`

选择滤波链中使用的复合滤波器内高通滤波器所需的带宽。

#### 依赖关系

仅当在 **选择复合滤波器** 参数中选择 `High pass filter` 时，此参数才会出现。

### **低通滤波器带宽** — 低通滤波器的带宽 `ODR/50`（默认） | `ODR/100` | `ODR/9` | `ODR/400`

选择滤波链中使用的复合滤波器内低通滤波器所需的带宽。

#### 依赖关系

仅当在 **选择复合滤波器** 参数中选择 `Low pass filter` 时，此参数才会出现。

#### 陀螺仪

### **满量程范围** — 测量角速度的满量程 `250 dps`（默认） | `125 dps` | `500 dps` | `1000 dps` | `2000 dps`

选择用于测量角速度的满量程（传感器需要测量的角速度范围）。

### **输出数据速率** — 陀螺仪数据的采样速率 `12.5 Hz`（默认） | `26 Hz` | `52 Hz` | `104 Hz` | `208 Hz` | `416 Hz` | `833 Hz` | `1666 Hz` | `3332 Hz` | `6664 Hz`

选择陀螺仪数据的采样输出数据速率，这也决定了带宽。

### **启用高通滤波器** — 为陀螺仪数据启用高通滤波器 `off`（默认） | `on`

启用用于读取陀螺仪值的高通滤波器。

### **高通滤波器带宽** — 高通滤波器的带宽 `0.016 Hz`（默认） | `0.065 Hz` | `0.260 Hz` | `1.04 Hz`

选择用于读取陀螺仪值的高通滤波器所需的带宽。

#### 依赖关系

仅当选择 **启用高通滤波器** 参数时，此参数才会出现。

### **启用低通滤波器** — 为陀螺仪数据启用低通滤波器 `off`（默认） | `on`

启用用于读取陀螺仪值的低通滤波器。

### **低通滤波器带宽模式** — 低通滤波器的带宽模式 `0`（默认） | `1` | `2` | `3`

选择用于读取陀螺仪值的低通滤波器所需的带宽模式。

#### 依赖关系

仅当选择 **启用低通滤波器** 参数时，此参数才会出现。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / Sensors / IMU Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

从 LSM6DSM 传感器测量线性加速度、角速率和温度

LSM6DSM IMU Sensor 模块使用与 STM32 Processors 连接的 LSM6DSM 惯性测量单元 (IMU) 传感器，测量沿 *X*、*Y* 和 *Z* 轴的线性加速度和角速率。此 6 自由度 (DoF) IMU 传感器包含加速度计和陀螺仪，分别用于测量线性加速度和角速率。该模块还测量 LSM6DSM Sensor 中嵌入式温度传感器的温度。

您还可以在模块中对加速度计值使用复合滤波器选项，并对陀螺仪值使用高通和低通滤波器选项。
