---
type: simulink-block
title: 'FXOS8700 6-Axes Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-K64F Board / Modeling'
documentation_page: 'fxos87006axessensor'
documentation_source_path: 'freescalefrdmk64fboard/ref/fxos87006axessensor.html'
language: zh-CN
chinese_source: worker-translation
---

# FXOS8700 6-Axes Sensor

## 端口

### 输出

该模块有两个输出端口。端口数量取决于你在 **活动传感器** 列表中选择的活动传感器。

### **Magnet** — 地球磁场沿芯片向量各轴的强度

该模块以 `[1x3]` 向量输出磁场。每个值表示沿 X、Y 和 Z 轴的磁场测量值，单位为 `μT`。

**数据类型：** `double`

### **Accel** — 施加到传感器上的、沿芯片向量各轴的加速度

该模块以 `[1x3]` 向量输出加速度。每个值表示沿 X、Y 和 Z 轴的加速度测量值，单位为 `g
(9.8 m/s2)`。

**数据类型：** `double`

## 参数

### **活动传感器** — 指定芯片上的活动传感器 `Accelerometer and Magnetometer` (默认) | `Accelerometer only` | `Magnetometer only`

- `Accelerometer only` —
  当你将 **活动传感器** 参数设置为 `Accelerometer
  only` 时，该模块会配置一个输出端口。该模块上的端口标记为 `Accel`，表示该模块输出加速度计测得的加速度。加速度沿芯片的 X、Y 和 Z 轴测量。

  ODR 的范围为 `1.5625 Hz` 到 `800
  Hz`。
- `Magnetometer only` —
  当你将 **活动传感器** 参数设置为 `Magnetometer
  only` 时，该模块会配置一个输出端口。该模块上的端口标记为 `Magnet`，表示该模块输出磁力计测得的地球磁场测量值。磁场沿芯片的 X、Y 和 Z 轴测量。

  ODR 的范围为 `1.5625 Hz` 到 `800
  Hz`。
- `Accelerometer and Magnetometer` —
  当你将 **活动传感器** 参数设置为 `Accelerometer
  and Magnetometer` 时，该模块会配置两个输出端口。该模块上的端口标记为 `Magnet` 和 `Accel`。`Magnet` 端口表示该模块输出磁力计测得的磁场测量值。`Accel` 端口表示该模块输出加速度计测得的加速度测量值。加速度和磁场沿芯片的 X、Y 和 Z 轴测量。

  ODR 的范围为 `0.7813 Hz` 到 `400
  Hz`。

### **传感器输出数据速率 (ODR)** — 数据采样速率 `400Hz` (默认) | `800Hz` | `200Hz` | `100Hz` | `50Hz` | `25Hz` | `12.5Hz` | `6.25Hz` | `3.125Hz` | `1.5625Hz` | `0.7813Hz`

指定你希望传感器读取加速度和磁场测量值的速率。此参数中显示的值取决于你在 **活动传感器** 列表中选择的活动传感器。

### **加速度满量程范围** — 加速度计可测量的加速度偏差范围 `-4g to +4g` (默认) | `-2g to +2g` | `-8g to +8g`

加速度计的灵敏度会随你在该参数中选择的满量程范围而变化。加速度计灵敏度在 `2 g` 模式下为 `0.244
mg/LSB`，在 `4
g` 模式下为 `0.488 mg/LSB`，在 `8
g` 模式下为 `0.976 mg/LSB`。较小的满量程范围意味着传感器灵敏度更高，从而使加速度计读数更精确。

#### 依赖关系

当你将 **活动传感器** 参数设置为 `Accelerometer only` 或 `Accelerometer
and Magnetometer` 时，将显示此参数。

### **采样时间** — 指定该模块从芯片上的传感器读取数据的频率 `-1` (默认)

默认情况下，该模块根据模型内该模块的上下文继承其采样时间。

## 所属库

Simulink Coder Support Package for NXP FRDM-K64F Board

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

获取沿 FXOS8700 6-Axes 芯片 X、Y 和 Z 轴的线加速度和磁场测量值

FXOS8700 6-Axes Sensor 模块测量沿 X、Y 和 Z 方向的线加速度和磁场。该模块有两个输出端口，Magnet 和 Accel。Magnet 端口以 `[1x3]` 向量（单位为 `uT`）输出 FXOS8700 6-Axes 芯片上磁力计测得的磁场。Accel 端口以 `[1x3]` 向量（单位为 `g
(9.8 m/s2)`）输出 FXOS8700 6-Axes 芯片上加速度计测得的加速度。输出端口的数量取决于你选择的活动传感器。

使用此模块的参数，你可以通过选择 `±2g`、`±4g`
或 `±8g` 的满量程范围来更改加速度计灵敏度。

你还可以选择两个传感器的输出数据速率 (ODR)。每个传感器的输出数据速率 (ODR) 范围为 `1.563
Hz` 到 `800 Hz`。在高达 400 Hz 的 ODR 下，可以获得交错的磁场和加速度数据。

### 芯片方向和相对于重力的轴方向

将板子正面朝上放在桌子上，使圆点位于 FXOS8700 6-Axes 芯片的右上角。在此位置，X 轴指向远离你的方向，Y 轴水平并指向左侧，Z 轴垂直并指向上方。

箭头方向表示加速度计和磁力计读数的正方向。

当你沿芯片的 X、Y 和 Z 轴倾斜板子时，此图示会显示加速度和磁场。

**X 方向上的重力加速度**

握住板子，使板子面向你，并且圆点位于芯片的右上角。由于芯片静止，重力加速度是静态的。

在所得的 `[1x3]` 向量中，表示 X 轴加速度的第一个值 ≈`1
g (9.81 m/s2)`。表示 Y 和 Z 轴（垂直于地球重力加速度）加速度的最后两个值 ≈ `0.00 g`。

以 `A m/s2` 的加速度向上推动板子。重力加速度是动态的，等于模块的加速度减去重力 ≈ `(+A-9.81)
m/s2`。在所得的 `[1x3]` 向量中，X 轴的值介于你在 **加速度满量程范围** 参数中指定的满量程范围值之间。

**X 方向上的磁场强度**

握住板子，使板子面向你，并且圆点位于芯片的右上角。芯片上的磁力计沿每个传感器轴测量地球磁场。在所得的 `[1x3]` 向量中，表示 X 轴磁场强度的第一个值最小。
