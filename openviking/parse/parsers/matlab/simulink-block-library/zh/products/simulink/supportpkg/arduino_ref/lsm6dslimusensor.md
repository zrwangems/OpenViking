---
type: simulink-block
title: 'LSM6DSL IMU Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Acceleration Sensors'
documentation_page: 'lsm6dslimusensor'
documentation_source_path: 'supportpkg/arduino_ref/lsm6dslimusensor.html'
language: zh-CN
chinese_source: worker-translation
---

# LSM6DSL IMU Sensor

## 端口

### 输出

您可以选择要激活的传感器来测量角速度、加速度、温度或这些测量的组合。

### **Acceleration** — 由加速度计测得的沿各轴的加速度向量

该模块将加速度输出为 `n`-by-3 向量，其中 `n` 是指定为 Samples per frame 的值。每个值表示沿 X、Y 和 Z 轴的加速度测量值，单位为 `m/s^2`。

#### 依赖关系

仅当选择 **Acceleration (m/s2)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Angular Velocity** — 由陀螺仪测得的沿各轴的角速度向量

该模块将角速度输出为 `n`-by-3 向量，其中 `n` 是指定为 Samples per frame 的值。每个值表示沿 X、Y 和 Z 轴的角速度测量值，单位为弧度每秒 (rad/s)。

#### 依赖关系

仅当选择 **Angular Velocity (rad/s)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Temperature** — 由 LSM6DSL 传感器测得的温度标量

由连接到 Arduino 板的 LSM6DSL 传感器测得的温度（单位：℃）。

#### 依赖关系

仅当选择 **Temperature (℃)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Status** — 加速度、角速度和温度测量的状态 `-1` | `0` | `1`

加速度、角速度和温度测量的状态，指定为 1-by-3 向量。`0` 表示读取的数据是新的，`1` 表示读取的数据不是新的，`-1` 表示未选择相应输出。

#### 依赖关系

仅当选择 **Status** 参数时，此输出端口才会出现。

**数据类型：** `int8`

### **Timestamp** — 读取数据时的时间戳矩阵 | (`n`)-by-1

从传感器读取数据时的时间戳（单位：秒），以 `n`-by-1 矩阵形式返回，其中 `n` 是指定为 Samples per frame 的值。

#### 依赖关系

仅当选择 **Timestamp** 参数时，此输出端口才会出现。

**数据类型：** `double`

## 参数

### 主要

### **I2C module** — I2C 通信模块 `0`（默认）| 标量

指定 Arduino 硬件上用于与传感器外设通信的 I2C 模块。有关 Arduino 引脚映射以及硬件板支持的模块的详细信息，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

### **I2C address** — 用于与传感器通信的外设地址 `0x6A`（默认）| `0x6B`

LSM6DSL 传感器上用于与加速度计和陀螺仪外设通信的外设地址由硬件板上 SDO/SA0 引脚的状态决定。下表提供了与该引脚及其状态对应的外设地址。

| 引脚名称 | 引脚状态 | 外设地址 |
| --- | --- | --- |
| SDO/SA0 | 0 | 0x6A |
| 1 | 0x6B |

### **Acceleration (m/s2)** — 设置用于读取加速度的输出端口 `on`（默认）| `off`

选择此参数可将 **Acceleration** 设置为输出端口之一。

### **Angular Velocity (rad/s)** — 设置用于读取角速度的输出端口 `on`（默认）| `off`

选择此参数可将 **Angular Velocity** 设置为输出端口之一。

### **Temperature (℃)** — 设置用于读取温度的输出端口 `on`（默认）| `off`

选择此参数可将 **Temperature** 设置为输出端口之一。

### **Status** — 设置用于获取所选输出状态的输出端口 `on`（默认）| `off`

选择此参数可将 **Status** 设置为输出端口之一。

### **Timestamp** — 设置用于获取时间戳的输出端口 `off`（默认）| `on`

选择此参数可将 **Timestamp** 设置为输出端口之一。

### **Samples per frame** — 模块输出的样本数 `1`（默认）| 正整数

指定模块输出的样本数。

此处指定的值还用于计算输出采样时间：

输出采样时间 = `Samples per frame` \* `Sample time`。

### **Sample time** — 读取数据的时间间隔 `-1`（默认）| 正整数

指定此模块从 LSM6DSL 传感器读取数据的频率。将此参数设置为 -1 时，Simulink 会根据模型中的模块上下文确定模块的最佳采样时间。输出采样时间是您指定的 `Samples per frame` 与 `Sample time` 的乘积。

### 高级

#### 加速度计

### **Full scale range** — 用于测量线性加速度的满量程 `±2g`（默认）| `±4g` | `±8g` | `±16g`

选择用于测量线性加速度的满量程（传感器需要测量的加速度范围）。

### **Output data rate** — 加速度计数据采样的速率 `12.5 Hz`（默认）| `26 Hz` | `52 Hz` | `104 Hz` | `208 Hz` | `416 Hz` | `833 Hz` | `1666 Hz` | `3332 Hz` | `6664 Hz`

选择加速度计数据采样的输出数据速率，这也决定了带宽。

### **Digital low pass filter bandwidth** — 低通数字滤波器的带宽 `ODR/2`（默认）| `ODR/4`

选择低通数字滤波器所需的带宽。

### **Select composite filter** — 滤波链中使用的复合滤波器 `No filter`（默认）| `High pass filter` | `Low pass filter`

选择用于读取加速度计值的滤波链中复合滤波器的类型。

### **High pass filter bandwidth** — 高通滤波器的带宽 `ODR/100`（默认）| `ODR/9` | `ODR/400`

选择滤波链中复合滤波器内高通滤波器所需的带宽。

#### 依赖关系

仅当在 **Select composite filter** 参数中选择 `High pass filter` 时，此参数才会出现。

### **Low pass filter bandwidth** — 低通滤波器的带宽 `ODR/50`（默认）| `ODR/100` | `ODR/9` | `ODR/400`

选择滤波链中复合滤波器内低通滤波器所需的带宽。

#### 依赖关系

仅当在 **Select composite filter** 参数中选择 `Low pass filter` 时，此参数才会出现。

#### 陀螺仪

### **Full scale range** — 用于测量角速度的满量程 `250 dps`（默认）| `125 dps` | `500 dps` | `1000 dps` | `2000 dps`

选择用于测量角速度的满量程（传感器需要测量的角速度范围）。

### **Output data rate** — 陀螺仪数据采样的速率 `12.5 Hz`（默认）| `26 Hz` | `52 Hz` | `104 Hz` | `208 Hz` | `416 Hz` | `833 Hz` | `1666 Hz` | `3332 Hz` | `6664 Hz`

选择陀螺仪数据采样的输出数据速率，这也决定了带宽。

### **Enable high pass filter** — 为陀螺仪数据启用高通滤波器 `off`（默认）| `on`

启用高通滤波器以读取陀螺仪值。

### **High pass filter bandwidth** — 高通滤波器的带宽 `0.016 Hz`（默认）| `0.065 Hz` | `0.260 Hz` | `1.04 Hz`

选择用于读取陀螺仪值的高通滤波器所需的带宽。

#### 依赖关系

仅当选择 **Enable high pass filter** 参数时，此参数才会出现。

### **Enable low pass filter** — 为陀螺仪数据启用低通滤波器 `off`（默认）| `on`

启用低通滤波器以读取陀螺仪值。

### **Low pass filter bandwidth mode** — 低通滤波器的带宽模式 `0`（默认）| `1` | `2` | `3`

选择用于读取陀螺仪值的低通滤波器所需的带宽模式。

#### 依赖关系

仅当选择 **Enable low pass filter** 参数时，此参数才会出现。

## 所属库

Simulink Support Package for Arduino Hardware / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2021a 中引入**

## 描述

测量来自 LSM6DSL 传感器的线性加速度、角速率和温度

LSM6DSL IMU Sensor 模块使用与 Arduino® 硬件连接的 LSM6DSL 惯性测量单元 (IMU) 传感器，测量沿 X、Y 和 Z 轴的线性加速度和角速率。这个 6 自由度 (DoF) IMU 传感器包含加速度计和陀螺仪，分别用于测量线性加速度和角速率。该模块还测量 LSM6DSL 传感器中嵌入式温度传感器的温度。

您还可以对加速度计值使用该模块中的复合滤波器选项，并对陀螺仪值使用高通和低通滤波器选项。
