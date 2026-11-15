---
type: simulink-block
title: 'Distance Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Sensors'
documentation_page: 'distancesensor'
documentation_source_path: 'vexv5/ref/distancesensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Distance Sensor

## 端口

### 输出

### **Distance** — 障碍物距离标量

**Distance** 端口输出以 meters 为单位的距离。
标称范围约为 2 meters。

**数据类型：** `double`

### **Velocity** — 接近速度标量

**Velocity** 端口输出障碍物的相对速度，单位为 meters per second。

#### 依赖关系

要启用此端口，请选择 **Velocity (m/s)** 参数。

**数据类型：** `double`

### **Size** — 障碍物大小标量

**Size** 输出指示障碍物大小。它的范围为 0 到 400，值越大表示障碍物越大。

#### 依赖关系

要启用此端口，请选择 **Size** 参数。

**数据类型：** `double`

### **Confidence** — 距离测量置信度标量

**Confidence** 指示是否在传感器范围内检测到对象，其值范围为 0 到 63。当对象超出传感器范围时，置信度值降至 0；对于低于 0.2 meters 的距离，该值为 10。

#### 依赖关系

要启用此端口，请选择 **Confidence** 参数。

**数据类型：** `double`

## 参数

### **Smart Port** — VEX V5 Distance Sensor 所连接的智能端口 1 (默认) | `1` 到 `21`

选择 V5 机器人上 VEX V5 Distance sensor 所连接的智能端口。V5 机器人上有 21 个智能端口。

### **Sample time** — 从传感器读取值的时间间隔 `0.2` (默认) | 正标量 | `-1`

指定采样时间（以 seconds 为单位），以确定该模块从传感器读取值的频率。当将此参数指定为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

### 附加输出

### **Velocity (m/s)** — 接近速度 `off` (默认) | `on`

选择此参数以启用 **Velocity** 端口。
有关 **Velocity** 端口的详细信息，请参阅
Velocity，

### **Size** — 障碍物大小 `off` (默认) | `on`

选择此参数以启用 **Size** 端口。有关
**Size** 端口的详细信息，请参阅 Size，

### **Confidence** — 距离置信度 `on` (默认) | `off`

选择此参数以启用 **Confidence** 端口。
有关 **Confidence** 端口的详细信息，请参阅
Confidence。

## 所属库

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

读取障碍物的距离、速度和相对大小

Distance Sensor 模块从连接到 VEX® V5 Brain 的 Distance sensor 读取数据。您可以在 Simulink 模型中使用此模块来获取距离、速度、障碍物相对大小和置信度。此外，该传感器还输出距离测量中的置信度。
