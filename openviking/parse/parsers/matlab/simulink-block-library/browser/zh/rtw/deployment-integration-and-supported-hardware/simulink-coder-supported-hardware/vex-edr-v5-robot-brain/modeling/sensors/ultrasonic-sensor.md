---
type: simulink-block
title: 'Ultrasonic Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Sensors'
documentation_page: 'ultrasonicsensor'
documentation_source_path: 'vexv5/ref/ultrasonicsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Ultrasonic Sensor

## 端口

### 输出

### **Port\_1** — 从 Ultrasonic sensor 的 Echo 端口读取的距离（centimeters）

从连接到 VEX V5 Robot Brain 的 Ultrasonic Sensor 的 Echo 端口读取的距离（以 cm 为单位）。

**数据类型：** `double`

## 参数

### **3-Wire Expander（智能端口）** — 选择 3-Wire Expander 使用的智能端口 `None`（默认） | `1` 到 `21`

如果使用 3-Wire Expander，请指定 VEX® EDR V5 Robot Brain 上该扩展器所连接的智能端口。

### **OUTPUT (Echo port)** — Optical Shaft Encoder 的 Output 端口所连接的 3-wire 端口 A（默认） | `C` | `E` | `G`

选择 VEX V5 Robot Brain 上 Ultrasonic sensor 的 Echo 端口（输出）所连接的 3-wire 端口。要了解输出端口，请点击 **What is INPUT and OUTPUT?** 按钮。

在模块中选择 **OUTPUT (Echo port)** 后，会假定相邻的 3-wire 端口连接到 ultrasonic sensor 的 INPUT（Ping 端口）。例如，如果选择 `A` 作为 **OUTPUT (Echo port)**，则假定 `B` 连接到 ultrasonic sensor 的 INPUT（Ping）端口。

### **采样时间** — 模块读取数值的时间间隔 `0.2`（默认） | 正标量 | -1

输入模块从 ultrasonic sensor 读取数值的时间间隔。

将此参数设置为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

表示已连接的 Ultrasonic sensor 并测量到物体的距离

Ultrasonic Sensor 模块表示连接到 VEX EDR V5 Robot Brain 的 3-wire 端口的 Ultrasonic Sensor，并测量机器人路径中物体的距离。当物体处于距离传感器 3 到 300 centimeters (cm) 的范围内时，该模块会启用物体检测。对于距离超过 300 cm 的物体，该模块输出值 0。
