---
type: simulink-block
title: 'BNO055 IMU Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Acceleration Sensors'
documentation_page: 'bno055imusensor'
documentation_source_path: 'supportpkg/arduino_ref/bno055imusensor.html'
language: zh-CN
chinese_source: worker-translation
---

# BNO055 IMU Sensor

## 端口

### 输出

### **Accel** — 沿传感器矩阵各轴的加速度（包括重力）

**Accel** 端口沿传感器的 *x*、*y* 和 *z* 轴输出加速度，形式为 3-by-`n` 向量，其中 `n` 是 Samples per frame 指定的值。在 Fusion 模式下，向量的元素表示校准值；而在 Non-Fusion 模式下，元素表示原始值。加速度以 m/s2 为单位测量，并且还包括重力加速度。

#### 依赖关系

仅当您选择 **Acceleration (m/s^2)** 参数时，**Accel** 端口才可用。

**数据类型：** `double`

### **Ang rate** — 绕传感器矩阵各轴的每秒旋转角度

**Ang rate** 端口绕传感器的 *x-*、*y-* 和 *z-* 轴输出每秒旋转角度，形式为 3-by-`n` 向量，其中 `n` 是 Samples per frame 指定的值。在 Fusion 模式下，向量的元素表示校准值；而在 Non-Fusion 模式下，元素表示原始值。角速率以 dps 为单位测量。

#### 依赖关系

仅当您选择 **Angular rate (dps)** 参数时，**Ang rate** 端口才可用。

**数据类型：** `double`

### **Mag field** — 沿传感器矩阵各轴的磁场强度

**Mag field** 端口沿传感器的 *x-*、*y-* 和 *z-* 轴输出磁场强度，形式为 3-by-`n` 向量，其中 `n` 是 Samples per frame 指定的值。在 Fusion 模式下，向量的元素表示校准值；而在 Non-Fusion 模式下，元素表示原始值。磁场强度以 μT 为单位测量。

#### 依赖关系

仅当您选择 **Magnetic field (μT)** 参数时，**Mag field** 端口才可用。

**数据类型：** `double`

### **Euler** — 以欧拉角矩阵形式给出的传感器方向

**Euler** 端口以 Azimuth-Pitch-Roll 表示法（*z*-*y*-*x* 顺序）沿传感器各轴输出方向，形式为 3-by-n 向量。这里 `n` 是 Samples per frame 指定的值

| 角度量 | 范围（度） |
| --- | --- |
| 方位角 | [0, 360] |
| 俯仰角 | [−180, 180] |
| 横滚角 | [−90, 90] |

#### 依赖关系

仅当您将 **Operation mode** 设置为 `Fusion` 并选择 **Euler angles (degrees)** 参数时，**Euler** 端口才可用。

**数据类型：** `double`

### **Quat** — 以四元数数组形式给出的传感器方向

**Quat** 端口沿传感器的 *w-*、*x-*、*y-* 和 *z-* 轴输出方向，形式为 4-by-`n` 向量，其中 `n` 是 Samples per frame 指定的值。方向以四元数为单位测量。

#### 依赖关系

仅当您将 **Operation mode** 设置为 `Fusion` 并选择 **Quaternion (quaternion)** 参数时，**Quat** 端口才可用。

**数据类型：** `double`

### **Lin accel** — 沿传感器矩阵各轴的排除重力的加速度

**Lin accel** 端口沿传感器的 *x-*、*y-* 和 *z-* 轴输出线性加速度，形式为 3-by-`n` 向量，其中 `n` 是 Samples per frame 指定的值。加速度以 m/s2 为单位测量，并且不包括重力加速度。

#### 依赖关系

仅当您将 **Operation mode** 设置为 `Fusion` 并选择 **Linear acceleration (m/s^2)** 参数时，**Lin accel** 端口才可用。

**数据类型：** `double`

### **Gravity** — 沿传感器矩阵各轴的重力加速度

**Gravity** 端口沿传感器的 *x-*、*y-* 和 *z-* 轴输出重力加速度，形式为 3-by-`n` 向量，其中 `n` 是 Samples per frame 指定的值。重力加速度以 m/s2 为单位测量。

#### 依赖关系

仅当您将 **Operation mode** 设置为 `Fusion` 并选择 **Gravity vector (m/s^2)** 参数时，**Gravity** 端口才可用。

**数据类型：** `double`

### **Status** — 整个系统以及陀螺仪、加速度计和磁力计的校准状态矩阵

**Status** 端口输出整个系统以及 BNO055 传感器内部传感器（陀螺仪、加速度计和磁力计）的校准状态，形式为 4-by-`n` 向量，其中 `n` 是 Samples per frame 指定的值。

下表说明了向量中每个元素值对传感器校准状态的含义。

| 值 | 校准状态 |
| --- | --- |
| `0` | 未校准 |
| `1` 和 `2` | 部分校准 |
| `3` | 完全校准 |

校准状态为 `2` 的部分校准传感器比校准状态为 `1` 的传感器提供更准确的读数。要完全校准这些传感器中的任何一个，请参阅 Calibrate Gyroscope、Calibrate Accelerometer 和 Calibrate Magnetometer。

**注意**

如果 **Status** 端口输出的数组中所有元素的值均为 `-1`，请确保传感器已正确连接到硬件，并且 **I2C address** 参数的值正确。

#### 依赖关系

仅当您将 **Operation mode** 设置为 `Fusion` 时，**Status** 端口才可用。

**数据类型：** `int8`

### **Timestamp** — 读取数据时的时间戳矩阵 | (`n`)-by-1

从传感器读取数据时的时间戳（以秒为单位），以 `n`-by-1 矩阵形式返回，其中 `n` 是 Samples per frame 指定的值。

#### 依赖关系

仅当您选择 **Timestamp** 参数时，此输出端口才会出现。

**数据类型：** `double`

## 参数

### **I2C module** — I2C 通信模块 `0`（默认）| 标量

指定 Arduino® 硬件上用于与传感器外设通信的 I2C 模块。有关 Arduino 引脚映射以及硬件板所支持模块的详细信息，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

### **I2C address** — 传感器的 I2C 外设地址 `0x28`（默认）| `0x29`

选择模块从中读取值的传感器的 I2C 地址。

### **Operation mode** — 输出校准值或原始值的选项 `Fusion`（默认）| `Non-Fusion`

- `Fusion` — 当您将 **Operation mode** 设置为 `Fusion` 时，传感器以 9 自由度（NDOF）模式运行。模块输出传感器的校准值。

  下表列出了模块输出、测量单位、维度以及测量每个输出时沿传感器的轴。

  | 输出 | 单位 | 维度a | 轴 |
  | --- | --- | --- | --- |
  | 加速度 | Meter per second squared (m/s2) | 3-by-n | *x*, *y*, and *z* |
  | 角速率 | Meter per second squared (m/s2) | 3-by-n | *x*, *y*, and *z* |
  | 磁场 | microtesla (μT) | 3-by-n | *x*, *y*, and *z* |
  | 欧拉角 | degrees per second (dps) | 3-by-n | *x*, *y*, and *z* |
  | 四元数 | Quaternion units | 4-by-n | *w*, *x*, *y*, and *z* |
  | 线性加速度 | Meter per second squared (m/s2) | 3-by-n | *x*, *y*, and *z* |
  | 重力向量 | Meter per second squared (m/s2) | 3-by-n | *x*, *y*, and *z* |
  | a `n` 是 Samples per frame 指定的值 | | | |

  **注意**

  在 Fusion 模式下，内部融合算法会使用某些值配置传感器的范围和带宽。这些值无法修改。
- `Non-Fusion` — 当您将 **Operation mode** 设置为 `Non-Fusion` 时，传感器以 Accelerometer Magnetometer Gyroscope (AMG) 模式运行。模块输出传感器的原始值。

  下表列出了 Non-Fusion 模式下模块输出、测量单位、维度以及测量每个输出时沿传感器的轴。

  | 输出 | 单位 | 维度a | 轴 |
  | --- | --- | --- | --- |
  | 加速度 | Meter per second squared (m/s2) | 3-by-n | *x*, *y*, and *z* |
  | 角速率 | Meter per second squared (m/s2) | 3-by-n | *x*, *y*, and *z* |
  | 磁场 | microtesla (μT) | 3-by-n | *x*, *y*, and *z* |
  | a `n` 是 Samples per frame 指定的值 | | | |

### **Samples per frame** — 模块输出的样本数 `1`（默认）| 正整数

指定模块输出的样本数。

您在此处指定的值也用于计算输出采样时间：

输出采样时间 = `Samples per frame` \* `Sample time`。

### **Sample time** — 从传感器读取值的间隔 `–1`（默认）| `-1` | 任何非负值

指定模块从传感器读取值的频率，以秒为单位。当您将此参数指定为 `-1` 时，Simulink® 会根据模型中的模块上下文确定为该模块的最佳采样时间。输出采样时间是您指定的 `Samples per frame` 与 `Sample time` 的乘积。

### 选择输出

### **Acceleration (m/s^2)** — 沿传感器各轴的加速度（包括重力） `on`（默认）| `off`

当您选择 **Acceleration (m/s^2)** 参数时，**Accel** 端口变为可用。有关 **Accel** 端口的详细信息，请参阅 Accel。

### **Angular rate (dps)** — 绕传感器各轴的每秒旋转角度 `on`（默认）| `off`

当您选择 **Angular rate (dps)** 参数时，**Ang rate** 端口变为可用。有关 **Ang rate** 端口的详细信息，请参阅 Ang rate。

### **Magnetic field (μT)** — 沿传感器各轴的磁场强度 `on`（默认）| `off`

当您选择 **Magnetic field (μT)** 参数时，**Mag field** 端口变为可用。有关 **Mag field** 端口的详细信息，请参阅 Mag field。

**数据类型：** `double`

### **Euler angles (degrees)** — 沿传感器各轴的方向 `off`（默认）| `on`

当您选择 **Euler angles (degrees)** 参数时，**Euler** 端口变为可用。有关 **Euler** 端口的详细信息，请参阅 Euler。

#### 依赖关系

仅当您将 **Operation mode** 设置为 `Fusion` 时，**Euler angles (degrees)** 参数才可用。

### **Quaternion (quaternion)** — 沿传感器各轴的方向 `off`（默认）| `on`

当您选择 **Quaternion (quaternion)** 参数时，**Quat** 端口变为可用。有关 **Quat** 端口的详细信息，请参阅 Quat。

#### 依赖关系

仅当您将 **Operation mode** 设置为 `Fusion` 时，**Quaternion (quaternion)** 参数才可用。

**数据类型：** `double`

### **Linear acceleration (m/s^2)** — 沿传感器各轴的排除重力的加速度 `off`（默认）| `on`

当您选择 **Linear acceleration (m/s^2)** 参数时，**Lin accel** 端口变为可用。有关 **Lin accel** 端口的详细信息，请参阅 Lin accel。

#### 依赖关系

仅当您将 **Operation mode** 设置为 `Fusion` 时，**Linear acceleration (m/s^2)** 参数才可用。

### **Gravity vector (m/s^2)** — 沿传感器各轴的重力加速度 `off`（默认）| `on`

当您选择 **Gravity vector (m/s^2)** 参数时，**Gravity** 端口变为可用。有关 **Gravity** 端口的详细信息，请参阅 Gravity。

#### 依赖关系

仅当您将 **Operation mode** 设置为 `Fusion` 时，**Gravity vector (m/s^2)** 参数才可用。

### **Status** — 读取操作的状态 `on`（默认）| `off`

选择此参数以显示读取操作的状态。

当您选择 **Status** 参数时，**Status** 端口变为可用。有关 **Status** 端口的详细信息，请参阅 Status。

### **Timestamp (s)** — 设置用于获取时间戳的输出端口 `off`（默认）| `on`

选择此参数以将 **Timestamp** 设置为输出端口之一。

### 高级传感器设置

### **Accelerometer range** — 加速度计测量的加速度偏差范围 `4G`（默认）| `2G` | `8G` | `16G`

指定加速度计可以测量的加速度偏差。加速度计范围越小，加速度计的读数越灵敏。小范围可提供更详细的数据，从而使加速度计的读数更精确。

#### 依赖关系

仅当您将 **Operation mode** 设置为 `Non-Fusion` 时，**Accelerometer range** 参数才可用。

### **Accelerometer bandwidth** — 加速度计的频率响应 `62.5 Hz`（默认）| `7.81 Hz` | `15.63 Hz` | `31.25 Hz` | `125 Hz` | `250 Hz` | `500 Hz` | `1000 Hz`

指定加速度计测量加速度的频率。

#### 依赖关系

仅当您将 **Operation mode** 设置为 `Non-Fusion` 时，**Accelerometer bandwidth** 参数才可用。

### **Gyroscope range** — 陀螺仪测量的最大角速度 `2000 dps`（默认）| `125 dps` | `250 dps` | `500 dps` | `1000 dps`

指定陀螺仪每秒可以测量的最大角速度。

#### 依赖关系

仅当您将 **Operation mode** 设置为 `Non-Fusion` 时，**Gyroscope range** 参数才可用。

### **Gyroscope bandwidth** — 陀螺仪的频率响应 `32 Hz`（默认）| `12 Hz` | `23 Hz` | `47 Hz` | `64 Hz` | `116 Hz` | `230 Hz` | `523 Hz`

指定陀螺仪测量角速度的频率。

#### 依赖关系

仅当您将 **Operation mode** 设置为 `Non-Fusion` 时，**Gyroscope bandwidth** 参数才可用。

### **Magnetometer output data range** — 数据采样速率 `15 Hz`（默认）| `2 Hz` | `6 Hz` | `8 Hz` | `10 Hz` | `20 Hz` | `25 Hz` | `30 Hz`

指定磁力计可以读取的磁场范围。

#### 依赖关系

仅当您将 **Operation mode** 设置为 `Fusion` 时，**Magnetometer output data range** 参数才可用。

**数据类型：** `double`

## 所属库

Simulink Support Package for Arduino Hardware / Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

测量沿 BNO055 传感器各轴的加速度、角速率和磁场，并计算融合值，例如欧拉角、四元数、线性加速度和重力向量

BNO055 IMU Sensor 模块从连接到硬件的 BNO055 IMU 传感器读取数据。该模块有两种操作模式：Non-Fusion 和 Fusion。

该模块在 Non-Fusion 和 Fusion 模式下输出沿传感器各轴的加速度、角速率和磁场强度。在 Fusion 模式下，该模块还输出传感器的方向（以欧拉角或四元数表示），以及线性加速度、重力向量和传感器的校准状态。在 Non-Fusion 模式下输出的值是原始值，而在 Fusion 模式下输出的值是校准值。该模块将除四元数和校准状态之外的所有值输出为 `double` 数据类型的 3-by-n 数组。四元数是 `double` 数据类型的 4-by-n 数组，校准状态是 `int8` 数据类型的 4-by-n 数组。这里，`n` 是 Samples per frame 指定的值

如果在未连接硬件的情况下仿真包含 BNO055 IMU Sensor 模块的模型，该模块输出零。有关详细信息，请参阅 Block Produces Zeros or Does Nothing in Simulation。
