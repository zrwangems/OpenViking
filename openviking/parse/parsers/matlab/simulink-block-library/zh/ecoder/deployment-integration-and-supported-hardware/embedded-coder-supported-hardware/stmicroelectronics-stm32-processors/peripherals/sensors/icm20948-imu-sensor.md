---
type: simulink-block
title: 'ICM20948 IMU Sensor'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Sensors'
documentation_page: 'icm20948imusensor'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/icm20948imusensor.html'
language: zh-CN
chinese_source: worker-translation
---

# ICM20948 IMU Sensor

## 端口

### 输出

### **Acceleration** — 传感器测量的线性加速度 行向量

**Acceleration** 端口沿传感器的 *x-*、*y-* 和 *z-* 轴以 *n*-by-3 向量形式输出加速度，单位为 m/s2。

#### 依赖项

要启用此端口，请选择 **加速度 (m/s2)** 参数。

**数据类型：** `single (default)` | `double`

### **Angular Rate** — 传感器测量的角速度 行向量

**Angular Rate** 端口沿传感器的 *x-*、*y-* 和 *z-* 轴以 *n*-by-3 向量形式输出角速度，单位为弧度/秒 (rad/s)。

#### 依赖项

要启用此端口，请选择 **角速率 (rad/s)** 参数。

**数据类型：** `single (default)` | `double`

### **Magnetic Field** — ICM20948 IMU 传感器测量的磁场强度 行向量

**Magnetic Field** 端口沿传感器的 *x-*、*y-* 和 *z-* 轴以 *n*-by-3 向量形式输出磁场强度，单位为 µT。

#### 依赖项

要启用此端口，请选择 **磁场 (µT)** 参数。

**数据类型：** `single (default)` | `double`

### **Temperature** — 传感器测量的温度 标量

连接到 STM32 处理器的 ICM20948 IMU 传感器测量的温度（单位为 ℃）。

#### 依赖项

要启用此端口，请选择 **温度 (℃)** 参数。

**数据类型：** `single` | `double`

### **Status** — 加速度、角速率、磁力计和温度测量的状态 行向量

沿三个轴的加速度、角速率、磁力计和温度测量的状态，以 `uint8` 值的 1-by-2 向量形式返回。向量中的第一个元素表示加速度、角速率和温度测量的状态，第二个元素表示磁力计测量的状态。该模块将状态输出为 `0` 或 `1`。`0` 表示读取的数据是新的，`1` 表示读取的数据不是新的。

#### 依赖项

要启用此端口，请选择 **状态** 参数。

**注意**

如果选择 **生成数据就绪中断** 参数，则 **状态** 参数会被禁用。

**数据类型：** `uint8`

## 参数

### **I2C 模块** — I2C 通信模块 `I2C1`（默认） | 标量

指定 STM32 处理器上用于与传感器外设通信的 I2C 模块。

### **I2C 地址** — 传感器的 I2C 地址 `0x69`（默认） | `0x68`

该模块从中读取数据的 ICM20948 IMU 传感器的 I2C 地址。根据传感器 AD0 引脚上的逻辑电平，ICM20948 传感器可以有两个 I2C 地址。

| 引脚名称 | 引脚状态 | I2C 地址 |
| --- | --- | --- |
| AD0 | Low | 0x68 |
| AD0 | High | 0x69 |

### **生成数据就绪中断** — 数据就绪时生成中断 `off`（默认） | `on`

选择此参数可在数据就绪时在传感器的 INT1 引脚上生成中断。使用此选项，您可以触发其他子系统执行任何操作。

### **中断类型** — 中断类型 `Active high`（默认） | `Active low`

选择 INT1 引脚的逻辑电平为 `Active high` 或 `Active low`。

#### 依赖项

要启用此参数，请选择 **生成数据就绪中断** 参数。

### **加速度 (m/s2)** — 启用端口以输出加速度 `on`（默认） | `off`

选择此参数以启用 **Acceleration** 输出端口。

### **角速率 (rad/s)** — 启用端口以输出角速率 `on`（默认） | `off`

选择此参数以启用 **Angular Rate** 输出端口。

### **磁场 (µT)** — 启用端口以输出磁场 `on`（默认） | `off`

选择此参数以启用 **Magnetic Field** 输出端口。

### **温度 (℃)** — 启用端口以输出温度 `on`（默认） | `off`

选择此参数以启用 **Temperature** 输出端口。

### **状态** — 启用端口以输出加速度、角速率、磁力计测量和温度状态 `off`（默认） | `on`

选择此参数以将 **Status** 设置为输出端口之一。如果选择 **生成数据就绪中断** 参数，则此参数会被禁用。

### **输出数据类型** — 输出的数据类型 `double`（默认） | `single`

指定加速度、角速率、磁场和温度输出的数据类型。

### **采样时间** — 读取数据的时间间隔 `-1`（默认） | 正整数

指定该模块从 ICM20948 IMU 传感器读取数据的频率。将此参数设置为 -1 时，Simulink 会根据模块在模型中的上下文确定该模块的最佳采样时间。输出采样时间是您在 `Sample time` 参数中指定的值的乘积。

#### 加速度计设置

### **满量程范围** — 测量加速度的范围 `±2g`（默认） | `±4g` | `±8g` | `±16g`

选择用于测量加速度的范围。

### **输出数据速率** — 传感器输出加速度计数据的速率 `1125Hz`（默认）

指定输出数据速率为 `0.3` 到 `1125` Hz 范围内的标量。加速度计数据输出速率（以 Hz 为单位）由以下计算确定。

`1125/(1+ACCEL_SMPLRT_DIV)Hz`，其中 `ACCEL_SMPLRT_DIV` 为 `0,1,2,...4095`。

根据在模块掩码上指定的输出数据速率，在传感器上设置 `ACCEL_SMPLRT_DIV`。

### **带宽** — 加速度计的带宽 `23.9 Hz`（默认） | `5.7 Hz` | `11.5 Hz` | `50.4 Hz` | `111.4 Hz` | `246 Hz` | `473 Hz`

指定加速度计低通滤波器的 3 dB 带宽。

#### 陀螺仪设置

### **满量程范围** — 陀螺仪测量的最大角速度 `±250 dps`（默认） | `±500 dps` | `±1000 dps` | `±2000 dps`

指定陀螺仪每秒可以测量的最大角速度。

### **输出数据速率** — 传感器输出陀螺仪数据的速率 `1125Hz`（默认）

指定输出数据速率为 `4.4` Hz 到 `1125` Hz 范围内的标量。

陀螺仪数据输出速率（以 Hz 为单位）由以下计算确定。

`1125/(1+GYRO_SMPLRT_DIV)Hz`，其中 `GYRO_SMPLRT_DIV` 为 `0,1,2,...255`。

根据在模块掩码上指定的输出数据速率，将在传感器上设置 `GYRO_SMPLRT_DIV`。

### **带宽** — 陀螺仪的带宽 `23.9 Hz`（默认） | `5.7 Hz` | `11.6 Hz` | `51.2 Hz` | `119.5 Hz` | `151.8 Hz` | `196.6 Hz` | `361.4 Hz`

指定陀螺仪低通滤波器的 3 dB 带宽。

#### 磁力计设置

### **输出数据速率** — 传感器输出磁力计数据的速率 `100 Hz`（默认） | `10 Hz` | `20 Hz` | `50 Hz`

选择对磁力计数据进行采样的输出数据速率。

#### 温度传感器设置

### **带宽** — 温度的噪声带宽 `34.1 Hz`（默认） | `8.8 Hz` | `17.3 Hz` | `65.9 Hz` | `123.5 Hz` | `217.9 Hz` | `7932.0 Hz`

指定温度低通滤波器的噪声带宽 (NBW)，以 Hz 为单位。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / Sensors / IMU Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

从 ICM20948 IMU 传感器测量线性加速度、角速度、磁场和温度

ICM20948 IMU Sensor 模块输出连接到 STM32 处理器的 ICM20948 IMU 传感器沿 *x-*、*y-* 和 *z-* 轴测得的线性加速度、角速度和磁场强度值。该模块还输出 ICM20948 IMU 传感器读取的温度。
