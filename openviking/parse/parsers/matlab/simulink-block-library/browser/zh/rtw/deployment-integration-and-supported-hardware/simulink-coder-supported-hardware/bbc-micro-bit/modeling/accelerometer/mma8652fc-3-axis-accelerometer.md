---
type: simulink-block
title: 'MMA8652FC 3-Axis Accelerometer'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BBC micro:bit / Modeling / Accelerometer'
documentation_page: 'mma8652fc3axisaccelerometer'
documentation_source_path: 'microbit/ref/mma8652fc3axisaccelerometer.html'
language: zh-CN
chinese_source: worker-translation
---

# MMA8652FC 3-Axis Accelerometer

## 端口

### 输出

该模块有一个输出端口。

### **Accel** — 沿芯片向量的每个轴施加到传感器的加速度

该模块将加速度输出为 `[1x3]` 向量。每个值表示沿 X、Y 和 Z 轴的加速度测量值，单位为 `g (9.8 m/s2)`。

**数据类型：** `double`

## 参数

### **Sensor output data rate (ODR)** — 数据采样速率 `800Hz`（默认） | `400Hz` | `200Hz` | `100Hz` | `50Hz` | `12.5Hz` | `6.25Hz` | `1.5625Hz`

指定您希望加速度计读取加速度测量值的速率。

### **Acceleration full scale range** — 加速度计可测量的加速度偏差范围 `-4g to +4g`（默认） | `-2g to +2g` | `-8g to +8g`

加速度计灵敏度在 `2 g` 模式下为 `256 counts/g`，在 `4 g` 模式下为 `128counts/g`，在 `8 g` 模式下为 `64counts/g`。较小的满量程范围意味着传感器灵敏度提高，从而使加速度计的读数更精确。

### **Sample time** — 指定模块从芯片上的加速度计读取数据的频率 `0.1`（默认）

当您将此参数指定为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Simulink Coder Support Package for BBC micro:bit/Accelerometer

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2018a 中引入**

## 描述

获取沿 MMA8652FC 3-Axis 芯片 X、Y 和 Z 轴的线性加速度测量值

MMA8652FC 3-Axis Accelerometer 模块测量沿 X、Y 和 Z 轴的线性加速度。该模块有一个输出端口 Accel。Accel 端口以 `[1x3]` 向量形式输出来自该芯片的加速度，单位为 `g (9.8 m/s2)`。

使用该模块的参数，您可以通过选择 `±2 g`、`±4 g` 或 `±8 g` 的满量程范围来更改加速度计灵敏度。

您还可以为两个传感器选择 Output Data Rates (ODR)。Output Data Rates (ODR) 范围从 `1.5625 Hz` 到 `800 Hz`。

### 芯片方向和相对于重力的轴方向

将板子保持为面向您，并使到 MMA8652FC 3-Axis 芯片顶部的线水平对齐桌面。在此位置，*X* 轴水平并指向左侧，*Y* 轴垂直并指向下方，*Z* 轴指向您。

箭头方向表示加速度计读数的正方向。

当您沿芯片的 X、Y 和 Z 轴倾斜板子时，此插图显示了加速度。

**X 方向的重力加速度**

将板子保持为面向您，并使到芯片右侧的线垂直对齐桌面。由于芯片静止，重力加速度是静态的。

在所得 `[1x3]` 向量中，表示 *X* 轴处加速度的第一个值 ≈ `1 g (9.81 m/s2)`。表示 Y 和 Z 轴处加速度（垂直于地球重力加速度）的后两个值 ≈ `0.00 g`。

以 `A m/s2` 的加速度向上推板子。重力加速度是动态的，等于板子的加速度减去重力 ≈ `(+A-9.81) m/s2`。在所得 `[1x3]` 向量中，*X* 轴的值在您在 **Acceleration full scale range** 参数中指定的满量程范围值之间变化。
