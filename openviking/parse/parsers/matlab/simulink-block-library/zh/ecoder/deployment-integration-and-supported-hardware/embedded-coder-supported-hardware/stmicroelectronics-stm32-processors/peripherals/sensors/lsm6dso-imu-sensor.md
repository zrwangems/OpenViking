---
type: simulink-block
title: 'LSM6DSO IMU Sensor'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Sensors'
documentation_page: 'lsm6dsoimusensor'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/lsm6dsoimusensor.html'
language: zh-CN
chinese_source: worker-translation
---

# LSM6DSO IMU Sensor

## 端口

### 输出

您可以选择激活的传感器，以测量角速度、加速度、温度或这些测量的组合。

### **Acceleration** — 由加速度计测得的沿各轴的加速度向量

该模块将加速度输出为 *n*×3 向量，其中 *n* 是每帧样本数的值。每个值表示沿 *X-*、*Y-* 和 *Z-* 轴测得的加速度，单位为 `m/s^2`。

#### 依赖项

要启用此端口，请选择 **Acceleration (m/s2)** 参数。

**数据类型：** `double`

### **Angular Velocity** — 由陀螺仪测得的沿各轴的角速度向量

该模块将角速度输出为 *n*×3 向量，其中 *n* 是每帧样本数的值。每个值表示沿 *X-*、*Y-* 和 *Z-* 轴测得的角速度，单位为弧度每秒 (rad/s)。

#### 依赖项

要启用此端口，请选择 **Angular Velocity (rad/s)** 参数。

**数据类型：** `double`

### **Temperature** — 由 LSM6DSO 传感器测得的温度标量

由连接到 STM32 处理器的 LSM6DSO 传感器测得的温度（单位：℃）。

#### 依赖项

要启用此端口，请选择 **Temperature (℃)** 参数。

**数据类型：** `double`

### **Status** — 加速度、角速度和温度测量的状态 `-1` | `0` | `1`

加速度、角速度和温度测量的状态，以 1×3 向量返回。

- `0` - 读取的数据是新数据
- `1` - 读取的数据不是新数据
- `-1` - 未选择对应输出

#### 依赖项

要启用此端口，请选择 **Status** 参数。

**数据类型：** `int8`

## 参数

### 主要

### **I2C module** — I2C 通信模块 `I2C1` (默认) | 标量

指定 STM32 处理器上用于与传感器外设通信的 I2C 模块。

### **I2C address** — 用于与传感器通信的外设地址 `0x6A` (默认) | `0x6B`

用于与 LSM6DSO 传感器上的加速度计和陀螺仪外设通信的外设地址由 STM32 处理器上 SDO/SA0 引脚的状态决定。下表提供与该引脚及其状态对应的外设地址。

| 引脚名称 | 引脚状态 | 外设地址 |
| --- | --- | --- |
| SDO/SA0 | 0 | 0x6A |
| 1 | 0x6B |

### **Acceleration (m/s2)** — 启用端口以输出加速度 `on` (默认) | `off`

选择此参数以启用 **Acceleration** 输出端口。

### **Angular Velocity (rad/s)** — 启用端口以输出角速度 `on` (默认) | `off`

选择此参数以启用 **Angular Velocity** 输出端口。

### **Temperature (℃)** — 启用端口以输出温度 `on` (默认) | `off`

选择此参数以启用 **Temperature** 输出端口。

### **Status** — 启用端口以输出所选输出的状态 `on` (默认) | `off`

选择此参数以启用 **Status** 输出端口。

### **Sample time** — 读取数据的时间间隔 `-1` (默认) | 正整数

指定模块从 LSM6DSO 传感器读取数据的频率。当您将此参数设置为 -1 时，Simulink 会根据模块在模型中的上下文确定为该模块的最佳采样时间。输出采样时间是您指定的 `Sample time` 的乘积。

### 高级

#### 加速度计

### **Full scale range** — 用于测量线性加速度的范围 `±2g` (默认) | `±4g` | `±8g` | `±16g`

选择用于测量线性加速度的范围。

### **Output data rate** — 传感器输出加速度计数据的速率 `12.5 Hz` (默认) | `26 Hz` | `52 Hz` | `104 Hz` | `208 Hz` | `416 Hz` | `833 Hz` | `1666 Hz` | `3332 Hz` | `6664 Hz`

选择传感器采样并输出加速度计数据的速率。此速率还决定传感器的带宽。

### **Select composite filter** — 要在滤波链中使用的复合滤波器 `No filter` (默认) | `High pass filter` | `Low pass filter`

选择用于读取加速度计值的滤波链中要使用的复合滤波器类型。

### **High pass filter bandwidth** — 高通滤波器的带宽 `ODR/4` (默认) | `ODR/10` | `ODR/20` | `ODR/45` | `ODR/100` | `ODR/200` | `ODR/400` | `ODR/800`

选择滤波链中使用的复合滤波器内高通滤波器的带宽。

#### 依赖项

要启用此参数，请在 **Select composite filter** 参数中选择 `High pass filter`。

### **Low pass filter bandwidth** — 低通滤波器的带宽 `ODR/4` (默认) | `ODR/10` | `ODR/20` | `ODR/45` | `ODR/100` | `ODR/200` | `ODR/400` | `ODR/800`

选择滤波链中使用的复合滤波器内低通滤波器所需的带宽。

#### 依赖项

要启用此参数，请在 **Select composite filter** 参数中选择 `Low pass filter`。

#### 陀螺仪

### **Full scale range** — 用于测量角速度的范围 `125 dps` (默认) | `250 dps` | `500 dps` | `1000 dps` | `2000 dps`

选择用于测量角速度的范围（传感器需要测量的角速度范围）。

### **Output data rate** — 传感器输出陀螺仪数据的速率 `12.5 Hz` (默认) | `26 Hz` | `52 Hz` | `104 Hz` | `208 Hz` | `416 Hz` | `833 Hz` | `1666 Hz` | `3332 Hz` | `6664 Hz`

选择传感器采样并输出陀螺仪数据的速率。此速率还决定传感器的带宽。

### **Enable high pass filter** — 为陀螺仪数据启用高通滤波器 `off` (默认) | `on`

启用高通滤波器以读取陀螺仪值。

### **High pass filter bandwidth** — 高通滤波器的带宽 `0.016 Hz` (默认) | `0.065 Hz` | `0.260 Hz` | `1.04 Hz`

选择用于读取陀螺仪值的高通滤波器所需带宽。

#### 依赖项

要启用此参数，请选择 **Enable high pass filter** 参数。

### **Enable low pass filter** — 为陀螺仪数据启用低通滤波器 `off` (默认) | `on`

启用低通滤波器以读取陀螺仪值。

### **Low pass filter bandwidth mode** — 低通滤波器的带宽模式 `0` (默认) | `1` | `2` | `3` | `4` | `5` | `6` | `7`

选择用于读取陀螺仪值的低通滤波器所需带宽模式。

对于陀螺仪 ODR > 1666 Hz，只有以下值适用于低通滤波器带宽模式：`0`、`1`、`2`、`3`。

#### 依赖项

要启用此参数，请选择 **Enable low pass filter** 参数。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / Sensors / IMU Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

从 LSM6DSO 传感器测量线性加速度、角速率和温度

LSM6DSO IMU Sensor 模块使用与 STM32 处理器连接的 LSM6DSO 惯性测量单元 (IMU) 传感器，测量沿 *X-*、*Y-* 和 *Z-* 轴的线性加速度和角速率。这个六自由度 (DoF) IMU 传感器由加速度计和陀螺仪组成，您可分别使用它们测量线性加速度和角速率。该模块还测量 LSM6DSO 传感器中嵌入式温度传感器的温度。

您还可以对加速度计值使用模块中的复合滤波器选项，并对陀螺仪值使用高通和低通滤波器选项。
