---
type: simulink-block
title: 'LSM6DS3H IMU Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sensors / IMU Sensors'
documentation_page: 'lsm6ds3himusensor'
documentation_source_path: 'supportpkg/raspberrypi_ref/lsm6ds3himusensor.html'
language: zh-CN
chinese_source: worker-translation
---

# LSM6DS3H IMU Sensor

## 端口

### 输出

您可以选择要激活的传感器，以测量角速度、加速度、温度或这些测量的组合。

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

### **Temperature** — 由 LSM6DS3H 传感器测量的温度标量

由连接到 Raspberry Pi 板的 LSM6DS3H 传感器测量的温度（以 ℃ 为单位）。

#### 依赖关系

此输出端口仅在您选择 **Temperature (℃)** 参数时出现。

**数据类型：** `double`

### **Status** — 加速度、角速度和温度测量的状态 `-1` | `0` | `1`

加速度、角速度和温度测量的状态，指定为 1×3 向量。`0` 表示读取的数据是新数据，`1` 表示读取的数据不是新数据，`-1` 表示未选择对应输出。

#### 依赖关系

此输出端口仅在您选择 **Status** 参数时出现。

**数据类型：** `int8`

## 参数

### 主要

### **I2C module** — 用于通信的模块 `1`（默认）

指定您用于 I2C 通信的板上的模块。

### **I2C address** — 用于与传感器通信的外设地址 `0x6A`（默认）| `0x6B`

用于与 LSM6DS3H 传感器上的加速度计和陀螺仪外设通信的外设地址由硬件板上 SDO/SA0 引脚的状态决定。下表提供了与该引脚及其状态对应的外设地址。

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

### **Status** — 设置用于获取所选输出状态的输出端口 `off`（默认）| `on`

选择此参数可将 **Status** 设置为输出端口之一。

### **Sample time** — 读取数据的时间间隔 `-1`（默认）| 正整数

指定此模块读取 LSM6DS3H 传感器数据的频率。将此参数设置为 -1 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

### 高级

#### 加速度计

### **Full scale range** — 用于测量线加速度的满量程 `±2g`（默认）| `±4g` | `±8g` | `±16g`

选择用于测量线加速度的满量程（传感器需要测量的加速度范围）。

### **Output data rate** — 加速度计数据采样的速率 `12.5 Hz`（默认）| `26 Hz` | `52 Hz` | `104 Hz` | `208 Hz` | `416 Hz` | `833 Hz` | `1666 Hz` | `3332 Hz` | `6664 Hz`

选择加速度计数据采样的输出数据速率，该速率也决定带宽。

### **Configure analog filter bandwidth** — 设置用于配置模拟滤波器带宽的选项 `off`（默认）| `on`

选择此参数可配置加速度计值滤波链中使用的模拟低通滤波器带宽。

### **Analog filter bandwidth** — 低通模拟滤波器的带宽 `400 Hz`（默认）| `50 Hz` | `100 Hz` | `200 Hz`

选择低通模拟滤波器所需的带宽。

#### 依赖关系

此参数仅在您选择 **Configure analog filter bandwidth** 参数时出现。

### **Select composite filter** — 滤波链中使用的复合滤波器 `No filter`（默认）| `High pass filter` | `Low pass filter`

选择用于读取加速度计值的滤波链中使用的复合滤波器类型。

### **High pass filter bandwidth** — 高通滤波器带宽 `ODR/100`（默认）| `ODR/9` | `ODR/400`

选择滤波链中使用的复合滤波器内高通滤波器所需的带宽。

#### 依赖关系

此参数仅在您在 **Select composite filter** 参数中选择 `High pass filter` 时出现。

### **Low pass filter bandwidth** — 低通滤波器带宽 `ODR/50`（默认）| `ODR/100` | `ODR/9` | `ODR/400`

选择滤波链中使用的复合滤波器内低通滤波器所需的带宽。

#### 依赖关系

此参数仅在您在 **Select composite filter** 参数中选择 `Low pass filter` 时出现。

#### 陀螺仪

### **Full scale range** — 用于测量角速度的满量程 `250 dps`（默认）| `125 dps` | `500 dps` | `1000 dps` | `2000 dps`

选择用于测量角速度的满量程（传感器需要测量的角速度范围）。

### **Output data rate** — 陀螺仪数据采样的速率 `12.5 Hz`（默认）| `26 Hz` | `52 Hz` | `104 Hz` | `208 Hz` | `416 Hz` | `833 Hz` | `1666 Hz`

选择陀螺仪数据采样的输出数据速率，该速率也决定带宽。

### **Enable high pass filter** — 为陀螺仪数据启用高通滤波器 `off`（默认）| `on`

启用高通滤波器以读取陀螺仪值。

### **High pass filter bandwidth** — 高通滤波器带宽 `0.0081 Hz`（默认）| `0.0324 Hz` | `2.07 Hz` | `16.32 Hz`

选择用于读取陀螺仪值的高通滤波器所需的带宽。

#### 依赖关系

此参数仅在您选择 **Enable high pass filter** 参数时出现。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Sensors / IMU Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

## 描述

从 LSM6DS3H 传感器测量线加速度、角速率和温度

LSM6DS3H IMU Sensor 模块使用与 Raspberry Pi® 板连接的 LSM6DS3H Inertial Measurement Unit (IMU) 传感器测量沿 X、Y 和 Z 轴的线加速度和角速率。这款 6 自由度 (DoF) IMU 传感器包含一个加速度计和一个陀螺仪，分别用于测量线加速度和角速率。该模块还测量来自 LSM6DS3H Sensor 中嵌入式温度传感器的温度。

您还可以在模块中使用模拟滤波器和复合滤波器选项处理加速度计值，并使用高通滤波器选项处理陀螺仪值。
