---
type: simulink-block
title: 'Rotation Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Sensors'
documentation_page: 'rotationsensor'
documentation_source_path: 'vexv5/ref/rotationsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotation Sensor

## 端口

### 输出

### **Position** — 轴旋转位置向量

此端口表示轴的旋转位置，以 degrees 为单位。
旋转位置值的范围从 `-inf` 到
`inf`。

**数据类型：** `double`

### **Velocity** — 轴速度向量

**Velocity** 端口输出轴速度，以
degrees per second 为单位。

**数据类型：** `double`

## 参数

### **Smart Port** — VEX V5 Rotation Sensor 连接到的 Smart Port 1（默认）| `1` 到 `21`

选择 V5 robot 上 VEX V5 Rotation sensor 所连接的 smart port。V5 robot 上有 21 个 smart ports。

### **Reset mode** — 重置 Rotation Sensor 读数的选项 `No reset`（默认）| `Reset by each sample time` | `Reset by external signal`

指定重置 rotation sensor 读数的选项。

- `No reset` – 模块不重置
  Rotation sensor 读数，并输出总旋转角度。

  例如，在表中 T = 1 时，Rotation sensor 逆时针旋转 20
  degrees，因此输出为 20。
- `Reset at each sample time`  – 对于每个
  采样周期，模块输出 rotation sensor 读数，然后
  将其重置为 0。

  例如，在表中，T = 1 时，rotation sensor 逆时针旋转
  20 degrees，因此输出为 20。

  在 T = 1 和 T = 2 之间，rotation sensor 逆时针旋转 10 degrees，
  因此输出为 10。

  如果以这种方式重置 rotation sensor，它会保留当前程序执行的
  偏移量。重启程序后可能需要重置。如果要保留零
  偏移，请在 VEX V5 Brain’s User
  Interface 上选择 **Set Zero**。有关详细信息，请参阅 Using VEX V5 Rotation Sensor。
- `Reset by external signal`  – 根据
  `Rst` 端口的输入值，Rotation sensor 读数重置为 0。当您向模块输入发送非 0
  值时，Rotation sensor 读数重置为 0。对于
  每个采样周期，模块输出自上次重置以来的 Rotation sensor 读数。

  Reset mode

### **Sample time** — 从传感器读取值的间隔 `0.2`（默认）| 正标量 | `-1`

指定采样时间（以 seconds 为单位），以确定模块从传感器读取
值的频率。当您将此参数指定为
`-1` 时，Simulink® 会根据模型中的模块上下文确定模块的最佳采样时间。

## 所属库

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

读取轴位置和速度

Rotation Sensor 模块从连接到 VEX® V5 Brain 的
Rotation sensor 读取轴的位置和速度。VEX V5 Rotation sensor 是一种绝对编码器，它在电源循环期间保留
轴方向。
