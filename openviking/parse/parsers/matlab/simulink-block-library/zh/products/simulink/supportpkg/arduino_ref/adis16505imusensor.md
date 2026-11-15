---
type: simulink-block
title: 'ADIS16505 IMU Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Acceleration Sensors'
documentation_page: 'adis16505imusensor'
documentation_source_path: 'supportpkg/arduino_ref/adis16505imusensor.html'
language: zh-CN
chinese_source: worker-translation
---

# ADIS16505 IMU Sensor

## 端口

### 输出

### **Acceleration** — 沿传感器轴的线性加速度行向量

**Acceleration** 端口输出沿传感器 x、y 和 z 轴的加速度，单位为 m/s2，形式为 `n`-by-3 向量，其中 `n` 是指定为 Samples per frame 的值。

#### 依赖项

仅当选择 **Acceleration (m/s^2)** 参数时，此输出端口才会出现。

**数据类型：** `double` | `single` | `int32`

### **Angular Rate** — 沿传感器轴每秒的旋转角度行向量

**Angular Rate** 端口输出沿传感器 x、y 和 z 轴的角速度，单位为 radians per second (rad/s)，形式为 `n`-by-3 向量，其中 `n` 是指定为 Samples per frame 的值。

#### 依赖项

仅当选择 **Angular Velocity (rad/s)** 参数时，此输出端口才会出现。

**数据类型：** `double` | `single` | `int32`

### **Temperature** — 沿传感器轴的温度标量

连接到 Arduino 板的 ADIS16505 IMU 传感器测得的温度（单位为 ℃）。

#### 依赖项

仅当选择 **Temperature (℃)** 参数时，此输出端口才会出现。

**数据类型：** `double` | `single` | `int32`

### **Status** — 加速度、角速度和温度测量的状态 `0` | `1`

加速度、角速度和温度测量的状态，指定为标量。`0` 表示读取的数据是新的，`1` 表示读取的数据不是新的。

**注意**

要观察状态变化，请将模块采样时间设置为小于 `0.5` milliseconds。这是因为 ADIS16505 传感器以 `2000` Hz 的时钟频率运行。

#### 依赖项

仅当选择 **Status** 参数时，**Status** 端口才可用。

**数据类型：** `uint8`

### **Timestamp** — 读取数据时的时间戳 矩阵 | (`n`)-by-1

从传感器读取数据时的时间戳（单位为 seconds），以 `n`-by-1 矩阵返回，其中 `n` 是指定为 Samples per frame 的值。

#### 依赖项

仅当选择 **Timestamp (s)** 参数时，此输出端口才会出现。

**数据类型：** `double`

## 参数

### **SPI chip select pin** — 将 SPI 外设连接到的片选引脚 `10`（默认）| 目标硬件引脚

输入 Arduino® 板上连接传感器片选引脚的引脚编号。有关不同 Arduino 板的 SS 引脚限制，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

### **Interrupt type** — 当数据就绪时生成中断 `Active high`（默认）| `Active low`

选择 INT1 引脚的逻辑电平为 `Active high` 或 `Active low`。

### **Desired output data rate (1 Hz - 2000 Hz)** — 加速度计数据采样的速率 `1`（默认）

输入所需的输出数据速率，介于 `1` Hz 到 `2000` Hz 之间，加速度计数据必须以此速率采样。

加速度计数据输出速率（以 Hz 为单位）由以下计算确定。

`Achieved output data rate = 2000/(1+DEC_RATE)`，其中 `DEC_RATE` 为 `0,1,2,...1999`。

根据模块掩码上指定的所需输出数据速率，将在传感器上设置 `Achieved output data rate (Hz)`。

### **No of taps for Bartlett window filter** — 抽头数 `1`（默认）| `2` | `4` | `8` | `16` | `32` | `64`

选择 Bartlett 窗滤波器的抽头数。

单击 **Frequency response based on number of taps** 以查看 Bartlett 滤波器的频率响应。下面显示了一个示例屏幕。

Bartlett 窗滤波器

### **Data type** — 输出数据的类型 `double`（默认）| `single` | `int32`

指定加速度、角速度和温度输出的数据类型。

### **Samples per frame** — 模块输出的样本数 `1`（默认）| 正整数

指定模块输出的样本数。

此处指定的值也用于计算输出采样时间：

输出采样时间 = `Samples per frame` \* `Sample time`。

### **Sample time** — 从传感器读取值的间隔 `–1`（默认）| 任意非负值

指定模块从传感器读取值的间隔，单位为 seconds。将此参数指定为 `-1` 时，Simulink® 会根据模型中的模块上下文确定模块的最佳采样时间。输出采样时间是所指定的 `Samples per frame` 和 `Sample time` 的乘积。

### 选择输出

### **Acceleration (m/s^2)** — 沿传感器轴的加速度，包括重力 `on`（默认）| `off`

选择 **Acceleration (m/s^2)** 参数时，**Acceleration** 端口将变为可用。有关 **Acceleration** 端口的详细信息，请参阅 Acceleration。

### **Angular velociy (rad/s)** — 沿传感器轴的每秒旋转角度 `on`（默认）| `off`

选择 **Angular velocity (rad/s)** 参数时，**Angular Rate** 端口将变为可用。有关 **Angular Rate** 端口的详细信息，请参阅 Angular Rate。

### **Temperature (deg C)** — 沿传感器轴的温度 `on`（默认）| `off`

选择 **Temperature (deg C)** 参数时，**Temperature** 端口将变为可用。有关 **Temperature (deg C)** 端口的详细信息，请参阅 Temperature。

### **Status** — 读取操作的状态 `on`（默认）| `off`

选择此参数以显示读取操作的状态。

选择 **Status** 参数时，**Status** 端口将变为可用。有关 **Status** 端口的详细信息，请参阅 Status。

### **Timestamp (s)** — 设置输出端口以获取时间戳 `on`（默认）| `off`

选择此参数可将 **Timestamp** 设置为输出端口之一。有关 **Timestamp** 端口的详细信息，请参阅 Timestamp。

## 所属库

Simulink Support Package for Arduino Hardware / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

## 描述

测量 ADIS16505 传感器轴上的加速度、角速度和温度

ADIS16505 IMU Sensor 模块输出连接到 Arduino 板的 ADIS16505 IMU Sensor 测得的沿 x、y 和 z 轴的加速度、角速度和温度值。

**注意**

除 `Temperature` 输出外，ADIS16505 传感器的输出可能存在有限的不可忽略的偏移值。对于此类情况，您可以考虑校正此偏移值。

如果仿真包含 ADIS16505 IMU Sensor 模块的模型而未将其连接到硬件，则该模块输出零。有关详细信息，请参阅 Block Produces Zeros or Does Nothing in Simulation。
