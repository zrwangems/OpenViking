---
type: simulink-block
title: 'MAG3110 3-Axis Magnetometer'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BBC micro:bit / Modeling / Magnetometer'
documentation_page: 'mag31103axismagnetometer'
documentation_source_path: 'microbit/ref/mag31103axismagnetometer.html'
language: zh-CN
chinese_source: worker-translation
---

# MAG3110 3-Axis Magnetometer

## 端口

### 输出

该模块有一个输出端口。

### **Magnet** — 沿芯片向量的每个轴的地球磁场强度

该模块将磁场输出为 `[1x3]` 向量。每个值表示沿 X、Y 和 Z 轴的磁场测量值，单位为 `μT`。

**数据类型：** `double`

## 参数

### **传感器输出数据速率 (ODR)** — 数据采样速率 `80Hz`（默认） | `40Hz` | `20Hz` | `10Hz` | `5Hz` | `2.5Hz` | `1.25Hz` | `0.63Hz`

指定您希望磁力计读取磁场测量值的速率。

### **采样时间** — 指定模块从芯片上的磁力计读取数据的频率 `0.1`（默认）

当您将此参数指定为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Simulink Coder Support Package for BBC micro:bit/Magnetometer

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2018a 中引入**

## 描述

获取沿 MAG3110 3-Axis 芯片的 X、Y 和 Z 轴的磁场测量值

MAG3110 3-Axis Magnetometer 模块测量沿 X、Y 和 Z 轴的磁场。该模块有一个输出端口，Magnet。Magnet 端口将磁场输出为 `[1x3]` 向量，单位为 `uT`。

使用此模块的参数，您可以为磁力计选择输出数据速率 (ODR)。输出数据速率 (ODR) 范围为 `0.63 Hz` 到 `80 Hz`。

### 芯片朝向和轴朝向相对于重力

使开发板面向您，并使 MAG3110 3-Axis 芯片顶部的线相对于桌面水平对齐。在此位置，X 轴水平并指向左侧，Y 轴垂直并指向下方，Z 轴指向您。

箭头方向表示磁力计读数的正方向。

当您沿芯片的 X、Y 和 Z 轴倾斜开发板时，此图显示了磁场强度。

**X 方向上的磁场强度**

使开发板面向您，并使芯片右侧的线相对于桌面垂直对齐。芯片上的磁力计测量沿每个传感器轴的地球磁场。在得到的 `[1x3]` 向量中，表示 X 轴处磁场强度的第一个值最小。
