---
type: simulink-block
title: 'ADXL34x Accelerometer'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sensors / IMU Sensors'
documentation_page: 'adxl34xaccelerometer'
documentation_source_path: 'supportpkg/raspberrypi_ref/adxl34xaccelerometer.html'
language: zh-CN
chinese_source: worker-translation
---

# ADXL34x Accelerometer

## 端口

### 输出

### **Acceleration** — 由 ADXL34x 传感器测得的线性加速度向量

此端口将沿 *x*、*y* 和 *z* 轴的线性加速度（以 m/s2 为单位）输出为 1×3 数组。

**数据类型：** `double`

**注意**

据观察，市场上存在许多有故障的克隆 ADXL345 传感器，其 Z 轴原始输出会变得无响应。请从正规经销商处购买传感器以避免此问题。

## 参数

### **I2C 模块** — 用于通信的模块 `1`（默认值）

指定您用于 I2C 通信的板上的模块。

### **I2C 地址** — ADXL34x 传感器的 I2C 地址 `0x53`（默认值） | `0x1D`

模块从中读取值的 ADXL34x 传感器的 I2C 地址。

根据传感器 ALT 引脚上的逻辑电平，ADXL34x 传感器可以有两个 I2C 地址。

| 引脚名称 | 引脚状态 | I2C 地址 |
| --- | --- | --- |
| ALT | Low | 0x53 |
| High | 0x1D |

### **数据类型** — 来自 ADXL34x 传感器的值的输出数据类型 `single`（默认值） | `double`

选择模块从中读取值的传感器的数据类型。

指定从 ADXL34x 传感器读取的值的输出数据类型。Raspberry Pi 板的默认数据类型为 `single`。如果需要，可使用此参数将值更改为 `double`。

### **采样时间** — 读取数据的时间间隔 `-1`（默认值） | 正整数

指定此模块从 ADXL34x 传感器读取数据的频率。将此参数设置为 -1 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

### 高级设置

### **加速度计范围** — 测量线性加速度的满量程 `±4g`（默认值） | `±2g` | `±8g` | `±16g`

选择加速度计可以测量的加速度范围。

### **加速度计输出数据速率** — 加速度计数据采样的速率 `12.5 Hz`（默认值） | `0.1 Hz` | `0.2 Hz` | `0.39 Hz` | `0.78 Hz` | `1.56 Hz` | `3.13 Hz` | `6.25 Hz` | `25 Hz` | `50 Hz` | `100 Hz` | `200 Hz` | `400 Hz` | `800 Hz` | `1600 Hz`

选择加速度计数据采样的输出数据速率。

### **使能数据就绪中断** — 数据就绪时使能中断 `off`（默认值） | `on`

如果选择此选项，当数据就绪时，传感器会在引脚 INT1 或 INT2 上生成中断，从而允许您触发其他子系统执行任何操作。

### **中断生成引脚** — 用于生成数据就绪中断的引脚 `INT1`（默认值） | `INT2`

选择用于读取加速度计数据的中断生成引脚。

#### 依赖关系

要启用此参数，请选择 **使能数据就绪中断** 参数。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Sensors / IMU Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2022b 中引入**

## 描述

测量 ADXL34x 系列加速度计沿各轴的线性加速度

ADXL34x Accelerometer 模块使用 Raspberry Pi® 板从 ADXL34x 系列加速度计（ADXL343、ADXL344、ADXL345 和 ADXL346）读取数据。

您可以使用此模块测量沿 *X*、*Y* 和 *Z* 轴的线性加速度。该模块还提供使能数据就绪中断的选项。

该模块将加速度输出为 1×3 数组。
