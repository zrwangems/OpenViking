---
type: simulink-block
title: 'Magnetometer X-Y-Z'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BBC micro:bit / Modeling / Magnetometer'
documentation_page: 'magnetometerxyz'
documentation_source_path: 'microbit/ref/magnetometerxyz.html'
language: zh-CN
chinese_source: worker-translation
---

# Magnetometer X-Y-Z

## 端口

### 输出

该模块有一个输出端口。

### **Magnet** — 沿芯片向量每个轴的地球磁场强度

该模块将磁场输出为 `[1x3]` 向量。
每个值表示沿 X、Y 和 Z 轴以 `μT` 为单位的磁场测量值。

**数据类型：** `double`

## 参数

### **传感器输出数据速率 (ODR)** — 数据采样速率 `80Hz`（默认） | `40Hz` | `20Hz` | `10Hz` | `5Hz` | `2.5Hz` | `1.25Hz` | `0.63Hz`

指定您希望磁力计读取磁场测量值的速率。

### **采样时间** — 指定模块从芯片上的磁力计读取数据的频率 `0.1`（默认）

当您将此参数指定为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Simulink Coder Support Package for BBC micro:bit/Magnetometer

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

## 描述

获取磁力计沿 X、Y 和 Z 轴的磁场测量值

Magnetometer X-Y-Z 模块测量沿 X、Y 和 Z 轴的磁场。该模块有三个输出端口。Magnet 端口将磁场输出为 `[1x3]` 向量，单位为 `uT`。

使用此模块的参数为磁力计选择输出数据速率 (ODR)。输出数据速率 (ODR) 范围为 `0.63 Hz` 到 `80 Hz`。

Magnetometer X-Y-Z 模块支持 BBC micro:bit 板版本 V1.3、V1.5 和 V2.2。

此模块由 MAG3110 3-Axis Magnetometer 和 LSM303 3-axes Magnetometer 传感器组成。

**注意**

LSM303 3-axes Magnetometer 传感器支持 V1.5 和 V2.2 板，MAG3110 3-Axis Magnetometer 传感器支持 V1.3 板。

### 芯片方向和相对于重力的轴方向

使板面向您，并使 MAG3110 3-Axis 芯片顶部的线水平对齐桌面。在此位置，X 轴水平并指向左侧，Y 轴竖直并指向下方，Z 轴指向您。

箭头方向表示磁力计读数的正方向。

当您沿芯片的 X、Y 和 Z 轴倾斜板时，此图示显示磁场的强度。

**X 方向上的磁场强度**

使板面向您，并使芯片右侧的线垂直对齐桌面。芯片上的磁力计测量沿每个传感器轴的地球磁场。在得到的 `[1x3]` 向量中，表示 X 轴处磁场强度的第一个值最小。
