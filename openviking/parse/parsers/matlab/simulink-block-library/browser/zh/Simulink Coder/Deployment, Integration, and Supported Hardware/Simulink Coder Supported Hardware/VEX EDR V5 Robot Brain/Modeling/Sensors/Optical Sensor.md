---
type: simulink-block
title: 'Optical Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Sensors'
documentation_page: 'opticalsensor'
documentation_source_path: 'vexv5/ref/opticalsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Optical Sensor

## 端口

### 输出

### **Proximity** — 反射红外标量的接近度

此端口传感器测量来自障碍物的反射红外能量的量。Proximity 的值范围为 0-255，值越高表示越靠近传感器。传感器的标称范围为 10cm。

**数据类型：** `double`

### **HSB** — 对象的色相、饱和度和亮度向量

此端口表示色相、饱和度、亮度/明度标度（HSB/HSV）。色相的值范围为 `0` 到 `360`，其中 `0` 对应红色。值 `120` 对应绿色，值 `240` 对应蓝色。饱和度和亮度的值范围为 `0` 到 `1`。

#### 依赖项

要启用此端口，请选择 **HSB (Hue, Saturation, Brightness)** 参数。

**数据类型：** `double`

### **RGB** — Red、Green、Blue 向量

此端口以 Red,Blue,Blue (RGB) 标度表示对象的颜色。

#### 依赖项

要启用此端口，请选择 **RGB (Red, Green, Blue)** 参数。

**数据类型：** `double`

## 参数

### **Smart Port** — VEX V5 Inertial Sensor 所连接的 Smart Port 1 (默认) | `1` 到 `21`

选择 V5 机器人上 VEX V5 inertial sensor 所连接的 smart port。V5 机器人上有 21 个 smart port。

### **LED Power (%)** — LED 灯的亮度 1 (默认) | `0` 到 `100`

值的范围为 0 到 100，LED 亮度随值的增加而增加。

### **Sample time** — 从传感器读取值的间隔 `0.2` (默认) | `-1` | positive scalar

以秒为单位指定采样时间，以确定模块从传感器读取值的频率。当您将此参数指定为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

### 附加输出

### **HSB (Hue, Saturation, Brightness)** — 对象的色相、饱和度和亮度 `on` (默认) | `off`

选择此参数以启用 **HSB** 端口。有关更多信息，请参阅 HSB。

### **RBG (Red, Blue, Green)** — 对象的颜色 `off` (默认) | `on`

选择此参数以启用 **RGB** 端口。有关 **RGB** 端口的更多信息，请参阅 RGB。

**数据类型：** `double`

## 所属库

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

读取接近度、颜色和亮度

Optical Sensor 模块读取连接到 VEX® V5 Brain 的光学传感器的数据。您可以在 Simulink 模型中使用此模块，通过光学传感器测量对象的颜色、亮度和接近度。
