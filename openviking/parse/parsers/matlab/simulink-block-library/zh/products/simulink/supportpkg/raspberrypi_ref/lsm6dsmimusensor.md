---
type: simulink-block
title: 'LSM6DSM IMU Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sensors / IMU Sensors'
documentation_page: 'lsm6dsmimusensor'
documentation_source_path: 'supportpkg/raspberrypi_ref/lsm6dsmimusensor.html'
language: zh-CN
chinese_source: worker-translation
---

# LSM6DSM IMU Sensor

## 端口

### 输出

您可以选择要启用的传感器来测量角速度、加速度、温度，或这些测量的组合。

### **Acceleration** — 由加速度计测得的沿各轴的加速度向量

该模块将加速度输出为 `1`-by-`3` 向量。每个值表示沿 X、Y 和 Z 轴的加速度测量值，单位为 `m/s^2`。

#### 依赖项

仅当选择 **Acceleration (m/s2)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Angular Velocity** — 由陀螺仪测得的沿各轴的角速度向量

该模块将角速度输出为 `1`-by-`3` 向量。每个值表示沿 X、Y 和 Z 轴的角速度测量值，单位为弧度每秒 (rad/s)。

#### 依赖项

仅当选择 **Angular Velocity (rad/s)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Temperature** — 由 LSM6DSM 传感器测得的温度标量

由连接到 Raspberry Pi 板的 LSM6DSM 传感器测得的温度（单位为 ℃）。

#### 依赖项

仅当选择 **Temperature (℃)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Status** — 加速度、角速度和温度测量的状态 `-1` | `0` | `1`

加速度、角速度和温度测量的状态，指定为 1-by-3 向量。`0` 表示读到的数据是新数据，`1` 表示读到的数据不是新数据，`-1` 表示未选择相应的输出。

#### 依赖项

仅当选择 **Status** 参数时，此输出端口才会出现。

**数据类型：** `int8`

## 参数

### 主要

### **I2C module** — 用于通信的模块 `1`（默认值）

指定板上用于 I2C 通信的模块。

### **I2C address** — 用于与传感器通信的外设地址 `0x6A`（默认值） | `0x6B`

用于与 LSM6DSM 传感器上的加速度计和陀螺仪外设通信的外设地址由硬件板上 SDO/SA0 引脚的状态决定。此表提供了与该引脚及其状态对应的外设地址。

| 引脚名称 | 引脚状态 | 外设地址 |
| --- | --- | --- |
| SDO/SA0 | 0 | 0x6A |
| 1 | 0x6B |

### **Acceleration (m/s2)** — 设置用于读取加速度的输出端口 `on`（默认值） | `off`

选择此参数可将 **Acceleration** 设置为输出端口之一。

### **Angular Velocity (rad/s)** — 设置用于读取角速度的输出端口 `on`（默认值） | `off`

选择此参数可将 **Angular Velocity** 设置为输出端口之一。

### **Temperature (℃)** — 设置用于读取温度的输出端口 `on`（默认值） | `off`

选择此参数可将 **Temperature** 设置为输出端口之一。

### **Status** — 设置用于获取所选输出状态的输出端口 `off`（默认值） | `on`

选择此参数可将 **Status** 设置为输出端口之一。

### **Sample time** — 读取数据的时间间隔 `-1`（默认值） | 正整数

指定此模块从 LSM6DSM 传感器读取数据的频率。将此参数设置为 -1 时，Simulink 会根据模块在模型中的上下文确定该模块的最佳采样时间。

### 高级

#### 加速度计

### **Full scale range** — 用于测量线性加速度的满量程 `±2g`（默认值） | `±4g` | `±8g` | `±16g`

选择用于测量线性加速度的满量程（传感器需要测量的加速度范围）。

### **Output data rate** — 加速度计数据的采样速率 `12.5 Hz`（默认值） | `26 Hz` | `52 Hz` | `104 Hz` | `208 Hz` | `416 Hz` | `833 Hz` | `1666 Hz` | `3332 Hz` | `6664 Hz`

选择加速度计数据的输出数据速率，这也决定了带宽。

### **Digital low pass filter bandwidth** — 低通数字滤波器的带宽 `ODR/2`（默认值） | `ODR/4`

选择低通数字滤波器所需的带宽。

### **Select composite filter** — 滤波链中使用的复合滤波器 `No filter`（默认值） | `High pass filter` | `Low pass filter`

选择用于读取加速度计值的滤波链中的复合滤波器类型。

### **High pass filter bandwidth** — 高通滤波器的带宽 `ODR/100`（默认值） | `ODR/9` | `ODR/400`

选择滤波链中使用的复合滤波器内高通滤波器所需的带宽。

#### 依赖项

仅当在 **Select composite filter** 参数中选择 `High pass filter` 时，此参数才会出现。

### **Low pass filter bandwidth** — 低通滤波器的带宽 `ODR/50`（默认值） | `ODR/100` | `ODR/9` | `ODR/400`

选择滤波链中使用的复合滤波器内低通滤波器所需的带宽。

#### 依赖项

仅当在 **Select composite filter** 参数中选择 `Low pass filter` 时，此参数才会出现。

#### 陀螺仪

### **Full scale range** — 用于测量角速度的满量程 `250 dps`（默认值） | `125 dps` | `500 dps` | `1000 dps` | `2000 dps`

选择用于测量角速度的满量程（传感器需要测量的角速度范围）。

### **Output data rate** — 陀螺仪数据的采样速率 `12.5 Hz`（默认值） | `26 Hz` | `52 Hz` | `104 Hz` | `208 Hz` | `416 Hz` | `833 Hz` | `1666 Hz` | `3332 Hz` | `6664 Hz`

选择陀螺仪数据的输出数据速率，这也决定了带宽。

### **Enable high pass filter** — 为陀螺仪数据启用高通滤波器 `off`（默认值） | `on`

启用用于读取陀螺仪值的高通滤波器。

### **High pass filter bandwidth** — 高通滤波器的带宽 `0.016 Hz`（默认值） | `0.065 Hz` | `0.260 Hz` | `1.04 Hz`

选择用于读取陀螺仪值的高通滤波器所需的带宽。

#### 依赖项

仅当选择 **Enable high pass filter** 参数时，此参数才会出现。

### **Enable low pass filter** — 为陀螺仪数据启用低通滤波器 `off`（默认值） | `on`

启用用于读取陀螺仪值的低通滤波器。

### **Low pass filter bandwidth mode** — 低通滤波器的带宽模式 `0`（默认值） | `1` | `2` | `3`

选择用于读取陀螺仪值的低通滤波器所需的带宽模式。

#### 依赖项

仅当选择 **Enable low pass filter** 参数时，此参数才会出现。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Sensors / IMU Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

## 描述

从 LSM6DSM 传感器测量线性加速度、角速率和温度

LSM6DSM IMU Sensor 模块使用与 Raspberry Pi® 硬件接口的 LSM6DSM 惯性测量单元 (IMU) 传感器，测量沿 X、Y 和 Z 轴的线性加速度和角速率。此 6 自由度 (DoF) IMU 传感器包含加速度计和陀螺仪，分别用于测量线性加速度和角速率。该模块还从 LSM6DSM Sensor 中的嵌入式温度传感器测量温度。

您还可以使用模块中的复合滤波器选项来处理加速度计值，并使用高通和低通滤波器选项来处理陀螺仪值。
