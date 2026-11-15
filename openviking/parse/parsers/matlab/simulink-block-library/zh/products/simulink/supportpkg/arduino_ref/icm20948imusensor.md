---
type: simulink-block
title: 'ICM20948 IMU Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Acceleration Sensors'
documentation_page: 'icm20948imusensor'
documentation_source_path: 'supportpkg/arduino_ref/icm20948imusensor.html'
language: zh-CN
chinese_source: worker-translation
---

# ICM20948 IMU Sensor

## 端口

### 输出

### **Acceleration** — 由 ICM20948 IMU 传感器测得的线性加速度行向量

**Acceleration** 端口输出沿传感器 x、y 和 z 轴的加速度，单位为 m/s2，形式为 `n`-by-3 向量，其中 `n` 是指定为 Samples per frame 的值。

#### 依赖关系

仅当选择 **Acceleration (m/s2)** 参数时，此输出端口才会出现。

**数据类型：** `single (default)` | `double`

### **Angular Rate** — 由陀螺仪测得的沿各轴的角速度行向量

**Angular Rate** 端口输出沿传感器 x、y 和 z 轴的角速度，单位为弧度/秒 (rad/s)，形式为 `n`-by-3 向量，其中 `n` 是指定为 Samples per frame 的值。

#### 依赖关系

仅当选择 **Angular Velocity (rad/s)** 参数时，此输出端口才会出现。

**数据类型：** `single (default)` | `double`

### **Magnetic Field** — 由 ICM20948 IMU 传感器测得的磁场强度行向量

**Magnetic Field** 端口输出沿传感器 x、y 和 z 轴的磁场强度，单位为 µT，形式为 `n`-by-3 向量，其中 `n` 是指定为 Samples per frame 的值。

#### 依赖关系

仅当选择 **Magnetic Field (µT)** 参数时，此输出端口才会出现。

**数据类型：** `single (default)` | `double`

### **Temperature** — 由 ICM20948 IMU 传感器测得的温度标量

由连接到 Arduino 板的 ICM20948 IMU 传感器测得的温度（单位为 ℃）。

#### 依赖关系

仅当选择 **Temperature (℃)** 参数时，此输出端口才会出现。

**数据类型：** `single` | `double`

### **Status** — 加速度值、角速度、磁力计测量值和温度的状态行向量

沿三个轴的加速度值、角速度、磁力计测量值和温度的状态，指定为 uint8 值的 [1X2] 向量。第一个元素表示加速度、角速度和温度测量的状态，第二个元素表示磁力计测量的状态。状态指示读取的数据是否为新值。`0` 表示读取的数据是新值，`1` 表示读取的数据不是新值。

#### 依赖关系

仅当选择 **Status** 参数时，此输出端口才会出现。

**注意**

如果选择 **Generate data ready interrupt** 参数，则 **Status** 参数将不可用。

**数据类型：** `uint8`

### **Timestamp** — 读取数据时的时间戳 矩阵 | (`n`)-by-1

从传感器读取数据时的时间戳（以秒为单位），以 `n`-by-1 矩阵返回，其中 `n` 是指定为 Samples per frame 的值。

#### 依赖关系

仅当选择 **Timestamp** 参数时，此输出端口才会出现。

Timestamp 输出的数据类型取决于为 **Output data type** 参数选择的值。

## 参数

### **I2C module** — I2C 通信模块 `0` (default) | 标量

指定 Arduino® 硬件上用于与传感器外设通信的 I2C 模块。有关 Arduino 引脚映射以及硬件板支持的模块的详细信息，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

### **I2C address** — ICM20948 IMU 传感器的 I2C 地址 `0x69` (default) | `0x68`

模块从中读取值的 ICM20948 IMU 传感器的 I2C 地址。根据传感器引脚 AD0 上的逻辑电平，ICM20948 传感器可以有两个 I2C 地址。

| 引脚名称 | 引脚状态 | I2C 地址 |
| --- | --- | --- |
| AD0 | Low | 0x68 |
| High | 0x69 |

### **Generate data ready interrupt** — 数据就绪时生成中断 `off` (default) | `on`

如果选择此选项，则当数据就绪时，会在传感器的引脚 INT1 上生成中断。使用此选项，您可以触发其他子系统执行任何操作。有关详细信息，请参阅 Estimate Orientation Using AHRS Filter and IMU Data in Simulink

### **Interrupt type** — 数据就绪时生成中断 `Active high` (default) | `Active low`

将 INT1 引脚的逻辑电平选择为 `Active high` 或 `Active low`。

#### 依赖关系

仅当选择 **Generate data ready interrupt** 参数时，此参数才会出现。

### **Acceleration (m/s2)** — 设置用于读取加速度的输出端口 `on` (default) | `off`

选择此参数可将 **Acceleration** 设置为输出端口之一。

### **Angular rate (rad/s)** — 设置用于读取角速度的输出端口 `on` (default) | `off`

选择此参数可将 **Angular Rate** 设置为输出端口之一。

### **Magnetic Field (µT)** — 设置用于读取磁场的输出端口 `on` (default) | `off`

选择此参数可将 **Magnetic Field** 设置为输出端口之一。

### **Temperature (℃)** — 设置用于读取温度的输出端口 `on` (default) | `off`

选择此参数可将 **Temperature** 设置为输出端口之一。

### **Status** — 设置用于获取加速度、角速度、磁力计测量值和温度状态的输出端口 `off` (default) | `on`

选择此参数可将 **Status** 设置为输出端口之一。如果选择了 **Generate data ready interrupt** 参数，则此参数将不可用。

### **Timestamp** — 设置用于获取时间戳的输出端口 `off` (default) | `on`

选择此参数可将 **Timestamp** 设置为输出端口之一。

### **Output data type** — 输出数据的类型 `double` (default) | `single`

指定加速度、角速度、磁场和温度输出的数据类型。

### **Samples per frame** — 模块输出的样本数 `1` (default) | 正整数

指定模块输出的样本数。此处指定的值还用于计算输出采样时间：

输出采样时间 = `Samples per frame` \*
`Sample time`

### **Sample time** — 读取数据的时间间隔 `-1` (default) | 正整数

指定此模块从 ICM20948 IMU 传感器读取数据的频率。将此参数设置为 -1 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。输出采样时间是指定的 `Samples per frame` 与 `Sample time` 的乘积。

#### 加速度计设置

### **Full scale range** — 加速度计可测量的加速度范围 `±2g` (default) | `±4g` | `±8g` | `±16g`

选择加速度计可以测量的加速度范围。

### **Output data rate** — 加速度计数据的采样速率 `1125Hz` (default)

输入加速度计数据采样的输出数据速率，范围为 `0.3` Hz 到 `1125` Hz。

加速度计数据输出速率（以 Hz 为单位）由以下计算确定。

`1125/(1+ACCEL_SMPLRT_DIV)Hz`，其中 `ACCEL_SMPLRT_DIV` 为 `0,1,2,...4095`。

根据模块掩码上指定的输出数据速率，`ACCEL_SMPLRT_DIV` 将在传感器上设置。

### **Bandwidth** — 加速度计带宽 `23.9 Hz` (default) | `5.7 Hz` | `11.5 Hz` | `50.4 Hz` | `111.4 Hz` | `246 Hz` | `473 Hz`

指定加速度计低通滤波器的 3 dB 带宽。

#### 陀螺仪设置

### **Full scale range** — 陀螺仪可测量的最大角速度 `±250 dps` (default) | `±500 dps` | `±1000 dps` | `±2000 dps`

指定陀螺仪可以测量的最大角速度。

### **Output data rate** — 陀螺仪数据的采样速率 `1125Hz` (default)

输入陀螺仪数据采样的输出数据速率，范围为 `4.4` Hz 到 `1125` Hz。

陀螺仪数据输出速率（以 Hz 为单位）由以下计算确定。

`1125/(1+GYRO_SMPLRT_DIV)Hz`，其中 `GYRO_SMPLRT_DIV` 为 `0,1,2,...255`。

根据模块掩码上指定的输出数据速率，`GYRO_SMPLRT_DIV` 将在传感器上设置。

### **Bandwidth** — 陀螺仪带宽 `23.9 Hz` (default) | `5.7 Hz` | `11.6 Hz` | `51.2 Hz` | `119.5 Hz` | `151.8 Hz` | `196.6 Hz` | `361.4 Hz`

指定陀螺仪低通滤波器的 3 dB 带宽。

#### 磁力计设置

### **Output data rate** — 磁力计数据的采样速率 `100 Hz` (default) | `10 Hz` | `20 Hz` | `50 Hz`

选择磁力计数据采样的输出数据速率。

#### 温度传感器设置

### **Bandwidth** — 温度的噪声带宽 `34.1 Hz` (default) | `8.8 Hz` | `17.3 Hz` | `65.9 Hz` | `123.5 Hz` | `217.9 Hz` | `7932.0 Hz`

指定温度低通滤波器的噪声带宽 (NBW)，以 Hz 为单位。

## 所属库

Simulink Support Package for Arduino Hardware / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022a 中引入**

## 描述

测量来自 ICM20948 IMU 传感器的线性加速度、角速度、磁场和温度

ICM20948 IMU Sensor 模块输出由连接到 Arduino 板的 ICM20948 IMU 传感器测得的沿 x、y 和 z 轴的线性加速度、角速度和磁场强度值。该模块还输出由 ICM20948 IMU 传感器读取的温度。
