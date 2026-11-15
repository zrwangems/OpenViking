---
type: simulink-block
title: 'MPU6050 IMU Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Acceleration Sensors'
documentation_page: 'mpu6050imusensor'
documentation_source_path: 'supportpkg/arduino_ref/mpu6050imusensor.html'
language: zh-CN
chinese_source: worker-translation
---

# MPU6050 IMU Sensor

## 端口

### 输出

### **Accel** — 沿传感器轴包含重力的加速度 向量

**Accel** 端口将沿传感器 *x-*、*y-* 和 *z-* 轴的加速度输出为 3-by-`n` 向量，其中 `n` 是指定为 Samples per frame 的值。加速度以 m/s2 为单位测量，并且还包括重力加速度。

#### 依赖关系

仅当选择 **Acceleration (m/s^2)** 参数时，**Accel** 端口才可用。

**数据类型：** `double`

### **Ang rate** — 沿传感器轴每秒旋转的角度 向量

**Ang rate** 端口将沿传感器 *x-*、*y-* 和 *z-* 轴的每秒旋转角度输出为 3-by-`n` 向量，其中 `n` 是指定为 Samples per frame 的值。角速度以 dps 为单位测量。

#### 依赖关系

仅当选择 **Angular rate (dps)** 参数时，**Ang rate** 端口才可用。

**数据类型：** `double`

### **Temperature** — 沿传感器轴的温度 向量

**Temperature** 端口输出沿传感器 *x-*、*y-* 和 *z-* 轴的温度。温度以 degree Celsius 为单位测量。

#### 依赖关系

仅当选择 **Temperature (deg C)** 参数时，**Temperature** 端口才可用。

**数据类型：** `double`

### **Status** — 读取操作的状态 标量

**Status** 端口输出读取操作的状态。该端口将状态输出为 `uint8` 值。每个值对应数据传输状态。

| 状态值 | 状态描述 |
| --- | --- |
| `0` | `SUCCESS` |
| `1` | `BUSY` |
| `2` | `ARBITRATION_LOST` |
| `4` | `NO_ACKNOWLEDGE` |
| `8` | `BUS_ERROR` |
| `16` | `BUS_NOT_IN_USE` |
| `32` | `SENSOR_INIT_ERROR` |

#### 依赖关系

仅当选择 **Status** 参数时，**Status** 端口才可用。

**数据类型：** `uint8`

### **Timestamp** — 读取数据时的时间戳 矩阵 | (`n`)-by-1

从传感器读取数据时的时间戳（以 seconds 为单位），以 `n`-by-1 矩阵返回，其中 `n` 是指定为 Samples per frame 的值。

#### 依赖关系

仅当选择 **Timestamp** 参数时，此输出端口才会出现。

**数据类型：** `double`

## 参数

### **I2C module** — I2C 通信模块 `0`（默认）| 标量

指定 Arduino® 硬件上与传感器外设通信的 I2C 模块。有关 Arduino 引脚映射以及硬件板支持的模块的更多信息，请参见 Pin Mapping for Arduino Timer-Independent Blocks。

### **I2C address** — 传感器的 I2C 外设地址 `0x68`（默认）| `0x69`

选择模块从中读取值的传感器的 I2C 地址。

### **Samples per frame** — 模块输出的样本数 `1`（默认）| 正整数

指定模块输出的样本数。

此处指定的值也用于计算输出采样时间：

输出采样时间 = `Samples per frame` \* `Sample time`。

### **Sample time** — 从传感器读取值的时间间隔 `–1`（默认）| 任意非负值

指定模块从传感器读取值的频率，以 seconds 为单位。将此参数指定为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。输出采样时间是指定的 `Samples per frame` 与 `Sample time` 的乘积。

### 选择输出

### **Acceleration (m/s^2)** — 沿传感器轴包含重力的加速度 `on`（默认）| `off`

选择 **Acceleration (m/s^2)** 参数后，**Accel** 端口将变为可用。有关 **Accel** 端口的更多信息，请参见 Accel。

### **Angular rate (dps)** — 沿传感器轴每秒旋转的角度 `on`（默认）| `off`

选择 **Angular rate (dps)** 参数后，**Ang rate** 端口将变为可用。有关 **Ang rate** 端口的更多信息，请参见 Ang rate。

### **Temperature (deg C)** — 沿传感器轴的温度 `on`（默认）| `off`

选择 **Temperature (deg C)** 参数后，**Temperature** 端口将变为可用。有关 **Temperature (deg C)** 端口的更多信息，请参见 Temperature。

### **Status** — 读取操作的状态 `on`（默认）| `off`

选择此参数以显示读取操作的状态。

选择 **Status** 参数后，**Status** 端口将变为可用。有关 **Status** 端口的更多信息，请参见 Status。

### **Timestamp (s)** — 设置用于获取时间戳的输出端口 `off`（默认）| `on`

选择此参数可将 **Timestamp** 设置为输出端口之一。

### 高级传感器设置（可选）

### **Accelerometer range** — 加速度计测量的加速度偏差范围 `2G`（默认）| `4G` | `8G` | `16G`

选择加速度计可以测量的加速度偏差。加速度计范围越小，加速度计的读数越灵敏。较小的范围可提供更详细的数据，从而使加速度计的读数更精确。

#### 依赖关系

仅当选择 **Acceleration (m/s^2)** 参数时，**Accelerometer range** 参数才可用。

### **Gyroscope range** — 陀螺仪测量的最大角速度 `250 dps`（默认）| `500 dps` | `1000 dps` | `2000 dps`

指定陀螺仪每秒可以测量的最大角速度。

#### 依赖关系

仅当选择 **Angular rate (dps)** 参数时，**Gyroscope range** 参数才可用。

### **Accelerometer and Gyroscope bandwidth** — 加速度计和陀螺仪的频率响应 `Accelerometer: 184Hz, Gyroscope: 188Hz`（默认）| `Accelerometer: 260Hz, Gyroscope: 256Hz` | `Accelerometer: 94Hz, Gyroscope: 98Hz` | `Accelerometer: 44Hz, Gyroscope: 42Hz` | `Accelerometer: 21Hz, Gyroscope: 20Hz` | `Accelerometer: 10Hz, Gyroscope: 10Hz` | `Accelerometer: 5Hz, Gyroscope: 5Hz`

指定加速度计和陀螺仪在不产生混叠的情况下对信号采样的最高频率。

#### 依赖关系

仅当选择 **Acceleration (m/s^2)** 或 **Angular rate (dps)** 参数时，**Accelerometer and Gyroscope bandwidth** 参数才可用。

## 所属库

Simulink Support Package for Arduino Hardware / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020a 中引入**

## 描述

测量沿 MPU-6050 传感器轴的加速度、角速度和温度

MPU6050 IMU Sensor 模块从连接到硬件的 MPU-6050 传感器读取数据。

该模块输出沿传感器轴的加速度、角速度和温度。该模块将加速度和角速度输出为 3-by-`n` double-precision 数组，其中 `n` 是指定为 Samples per frame 的值。温度数据输出为标量 double。

**注意**

除 `Temperature` 输出外，MPU-6050 传感器的输出可能具有有限的、不可忽略的偏移值。对于此类情况，您可以考虑校正此偏移值。

此图显示了 MPU-6050 传感器的 *x-*、*y-* 和 *z-* 轴的默认方向。

如果仿真包含 MPU6050 IMU Sensor 模块的模型而未将其连接到硬件，则该模块输出零。有关更多信息，请参见 Block Produces Zeros or Does Nothing in Simulation。
