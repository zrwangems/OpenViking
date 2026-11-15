---
type: simulink-block
title: 'ADXL34x Accelerometer'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Acceleration Sensors'
documentation_page: 'adxl34xaccelerometer'
documentation_source_path: 'supportpkg/arduino_ref/adxl34xaccelerometer.html'
language: zh-CN
chinese_source: worker-translation
---

# ADXL34x Accelerometer

## 端口

### 输出

### **Acceleration** — 由 ADXL34x 传感器向量测量的线性加速度

此端口输出沿 *x*-、*y*- 和 *z*- 轴的线性加速度（单位为
m/s2），以 `n`-by-3
数组形式返回，其中 `n` 是指定为
Samples per frame 的值。

**数据类型：** `double`

### **Timestamp** — 读取数据时的时间戳 matrix | (`n`)-by-1

从传感器读取数据时的时间戳（单位为秒），以 `n`-by-1 矩阵形式返回，其中
`n` 是指定为 Samples per frame 的值。

#### 依赖关系

仅当选择 **Enable timestamp output** 参数时，此输出端口才会出现。

Timestamp 输出的数据类型取决于为 **Data type** 参数选择的值。

**注意**

据观察，市场上有许多有故障的克隆 ADXL345 传感器，其 *Z* 轴原始输出变得无响应。
请从正规经销商处购买传感器以避免此问题。

## 参数

### **I2C module** — I2C 通信模块 `0`（默认） | scalar

指定 Arduino® 硬件上用于与传感器外设通信的 I2C 模块。有关 Arduino 引脚映射以及硬件板支持的模块的详细信息，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

### **I2C address** — ADXL34x 传感器的 I2C 地址 `0x53`（默认） | `0x1D`

ADXL34x 传感器的 I2C 地址，模块从该地址读取值。

ADXL34x 传感器可以有两个 I2C 地址，具体取决于传感器 ALT 引脚上的逻辑电平。

| 引脚名称 | 引脚状态 | I2C 地址 |
| --- | --- | --- |
| ALT | Low | 0x53 |
| ALT | High | 0x1D |

### **Enable timestamp output** — 设置用于获取时间戳的输出端口 `off`（默认） | `on`

选择此参数可将 **Timestamp** 设置为输出端口之一。

### **Data type** — ADXL34x 传感器值的输出数据类型 `single`（默认） | `double`

选择模块从中读取值的传感器的数据类型。

指定从 ADXL34x 传感器读取的值的输出数据类型。Arduino 硬件的默认数据类型为 `single`。如果需要，可使用此参数将值更改为 `double`。

### **Samples per frame** — 模块输出的样本数 `1`（默认） | 正整数

指定模块输出的样本数。此处指定的值也用于计算输出采样时间：

输出采样时间 = `Samples per frame` \* `Sample time`

### **Sample time** — 读取数据的时间间隔 `-1`（默认） | 正整数

指定此模块从 ADXL34x 传感器读取数据的频率。将此参数设置为 -1 时，Simulink® 会根据模型中的模块上下文为该模块确定最佳采样时间。输出采样时间是所指定的 `Samples per frame` 与 `Sample time` 的乘积。

### 高级设置

### **Accelerometer range** — 测量线性加速度的满量程 `±4g`（默认） | `±2g` | `±8g` | `±16g`

选择加速度计可测量的加速度范围。

### **Accelerometer output data rate** — 加速度计数据采样的速率 `12.5 Hz`（默认） | `0.1 Hz` | `0.2 Hz` | `0.39 Hz` | `0.78 Hz` | `1.56 Hz` | `3.13 Hz` | `6.25 Hz` | `25 Hz` | `50 Hz` | `100 Hz` | `200 Hz` | `400 Hz` | `800 Hz` | `1600 Hz`

选择加速度计数据采样的输出数据速率。

### **Enable data ready interrupt** — 数据就绪时启用中断 `off`（默认） | `on`

如果选择此选项，则当数据就绪时，会在传感器的 INT1 或 INT2 引脚上生成中断，从而使您能够触发其他子系统执行任意操作。

### **Interrupt generate pin** — 用于生成数据就绪中断的引脚 `INT1`（默认） | `INT2`

选择中断生成引脚以读取加速度计数据。

#### 依赖关系

要启用此参数，请选择 **Enable data ready interrupt** 参数。

## 所属库

Simulink Support Package for Arduino Hardware / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022a 中引入**

## 描述

测量 ADXL34x 系列加速度计沿各轴的线性加速度

ADXL34x Accelerometer 模块使用 Arduino 硬件从 ADXL34x 系列加速度计（ADXL343、ADXL344、ADXL345 和 ADXL346）读取数据。

您可以使用此模块测量沿 *X*、*Y* 和 *Z* 轴的线性加速度。该模块还提供启用数据就绪中断的选项。
