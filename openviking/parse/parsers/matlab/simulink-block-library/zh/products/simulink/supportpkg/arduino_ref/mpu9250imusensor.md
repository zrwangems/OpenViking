---
type: simulink-block
title: 'MPU9250 IMU Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Acceleration Sensors'
documentation_page: 'mpu9250imusensor'
documentation_source_path: 'supportpkg/arduino_ref/mpu9250imusensor.html'
language: zh-CN
chinese_source: worker-translation
---

# MPU9250 IMU Sensor

## 端口

### 输出

### **Accel** — 沿传感器各轴的加速度，包括重力 vector

**Accel** 端口沿传感器的 *x-*、*y-* 和 *z-* 轴输出加速度，形式为 3-by-`n` 向量，其中 `n` 是指定为 Samples per frame 的值。加速度以 m/s2 为单位，并且还包括由重力引起的加速度。

#### 依赖关系

仅当选择 **Acceleration (m/s^2)** 参数时，**Accel** 端口才可用。

**数据类型：** `double`

### **Ang rate** — 沿传感器各轴每秒的旋转角度 vector

**Ang rate** 端口沿传感器的 *x-*、*y-* 和 *z-* 轴输出每秒的旋转角度，形式为 3-by-`n` 向量，其中 `n` 是指定为 Samples per frame 的值。角速度以 dps 为单位。

#### 依赖关系

仅当选择 **Angular rate (dps)** 参数时，**Ang rate** 端口才可用。

**数据类型：** `double`

### **Mag field** — 沿传感器各轴的磁场强度 vector

**Mag field** 端口沿传感器的 *x-*、*y-* 和 *z-* 轴输出磁场强度，形式为 3-by-`n` 向量，其中 `n` 是指定为 Samples per frame 的值。磁场强度以 μT 为单位。

#### 依赖关系

仅当选择 **Magnetic field (μT)** 参数时，**Mag field** 端口才可用。

**数据类型：** `double`

### **Temperature** — 沿传感器各轴的温度 vector

**Temperature** 端口沿传感器的 *x-*、*y-* 和 *z-* 轴输出温度。温度以 degree Celsius 为单位。

#### 依赖关系

仅当选择 **Temperature (deg C)** 参数时，**Temperature** 端口才可用。

**数据类型：** `double`

### **Status** — 读取操作的状态 scalar

**Status** 端口输出读取操作的状态。该端口将状态输出为 `uint8` 值。每个值对应一种数据传输状态。

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

### **Timestamp** — 读取数据时的时间戳 matrix | (`n`)-by-1

从传感器读取数据时的时间戳（以 seconds 为单位），以 `n`-by-1 矩阵形式返回，其中 `n` 是指定为 Samples per frame 的值。

#### 依赖关系

仅当选择 **Timestamp** 参数时，此输出端口才出现。

**数据类型：** `double`

## 参数

### **I2C module** — I2C 通信模块 `0`（默认）| scalar

指定 Arduino® 硬件上用于与传感器外设通信的 I2C 模块。有关 Arduino 引脚映射以及硬件板支持的模块的详细信息，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

### **I2C address** — 传感器的 I2C 外设地址 `0x68`（默认）| `0x69`

选择模块从中读取值的传感器的 I2C 地址。

### **Samples per frame** — 模块输出的样本数 `1`（默认）| positive integer

指定模块输出的样本数。

此处指定的值也用于计算输出采样时间：

输出采样时间 = `Samples per frame` \* `Sample time`。

### **Sample time** — 从传感器读取值的时间间隔 `-1`（默认）| 任意非负值

指定模块从传感器读取值的频率，以 seconds 为单位。将此参数指定为 `-1` 时，Simulink® 会根据模型中的模块上下文确定模块的最佳采样时间。输出采样时间是指定的 `Samples per frame` 与 `Sample time` 的乘积。

### 选择输出

### **Acceleration (m/s^2)** — 沿传感器各轴的加速度，包括重力 `on`（默认）| `off`

当选择 **Acceleration (m/s^2)** 参数时，**Accel** 端口变为可用。有关 **Accel** 端口的详细信息，请参阅 Accel。

### **Angular rate (dps)** — 沿传感器各轴每秒的旋转角度 `on`（默认）| `off`

当选择 **Angular rate (dps)** 参数时，**Ang rate** 端口变为可用。有关 **Ang rate** 端口的详细信息，请参阅 Ang rate。

### **Magnetic field (μT)** — 沿传感器各轴的磁场强度 `on`（默认）| `off`

当选择 **Magnetic field (μT)** 参数时，**Mag field** 端口变为可用。有关 **Mag field** 端口的详细信息，请参阅 Mag field。

**数据类型：** `double`

### **Temperature (deg C)** — 沿传感器各轴的温度 `on`（默认）| `off`

当选择 **Temperature (deg C)** 参数时，**Euler** 端口变为可用。有关 **Temperature (deg C)** 端口的详细信息，请参阅 Temperature。

### **Status** — 读取操作的状态 `off`（默认）| `on`

选择此参数以显示读取操作的状态。

当选择 **Status** 参数时，**Status** 端口变为可用。有关 **Status** 端口的详细信息，请参阅 Status。

### **Timestamp** — 设置用于获取时间戳的输出端口 `off`（默认）| `on`

选择此参数以将 **Timestamp** 设置为输出端口之一。

### 高级传感器设置（可选）

### **Accelerometer range** — 加速度计测量的加速度偏差范围 `2G`（默认）| `4G` | `8G` | `16G`

选择加速度计可测量的加速度偏差。加速度计范围越小，加速度计读数越灵敏。较小的范围可提供更详细的数据，从而使加速度计读数更精确。

#### 依赖关系

仅当选择 **Acceleration (m/s^2)** 参数时，**Accelerometer range** 参数才可用。

### **Accelerometer bandwidth** — 加速度计的频率响应 `218.1 Hz`（默认）| `1046 Hz` | `21.2 Hz` | `99 Hz` | `44.8 Hz` | `10.2 Hz` | `5.05 Hz` | `420 Hz`

指定加速度计对信号进行采样而不产生混叠的最高频率。

#### 依赖关系

仅当选择 **Acceleration (m/s^2)** 参数时，**Accelerometer bandwidth** 参数才可用。

### **Gyroscope range** — 陀螺仪测量的最大角速度 `250 dps`（默认）| `500 dps` | `1000 dps` | `2000 dps`

指定陀螺仪每秒可测量的最大角速度。

#### 依赖关系

仅当选择 **Angular rate (dps)** 参数时，**Gyroscope range** 参数才可用。

### **Gyroscope bandwidth** — 陀螺仪的频率响应 `250 Hz`（默认）| `8800 Hz` | `184 Hz` | `92 Hz` | `41 Hz` | `20 Hz` | `10 Hz` | `7 Hz` | `3600 Hz`

指定陀螺仪对信号进行采样而不产生混叠的最高频率。

#### 依赖关系

仅当选择 **Angular rate (dps)** 参数时，**Gyroscope bandwidth** 参数才可用。

## 所属库

Simulink Support Package for Arduino Hardware / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020a 中引入**

## 描述

测量沿 MPU-9250 传感器各轴的加速度、角速度、磁场和温度

MPU9250 IMU Sensor 模块从连接到硬件的 MPU-9250 传感器读取数据。

该模块输出沿传感器各轴的加速度、角速度、磁场强度和温度。除温度外，该模块将所有值输出为 3-by-`n` double-precision array，其中 `n` 是指定为 Samples per frame 的值。温度数据输出为 scalar double。

**注意**

除 `Temperature` 输出外，MPU-9250 传感器的输出可能具有有限但不可忽略的偏移值。对于此类情况，您可以考虑校正此偏移值。

下图显示了 MPU-9250 传感器的 *x-*、*y-* 和 *z-* 轴的默认方向。

如果仿真一个包含 MPU9250 模块的模型而未将其连接到硬件，则该模块输出零。有关详细信息，请参阅 Block Produces Zeros or Does Nothing in Simulation。
