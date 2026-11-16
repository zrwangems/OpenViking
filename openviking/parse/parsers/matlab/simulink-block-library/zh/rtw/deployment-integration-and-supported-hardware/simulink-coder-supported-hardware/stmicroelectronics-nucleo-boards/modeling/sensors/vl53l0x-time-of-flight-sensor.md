---
type: simulink-block
title: 'VL53L0X Time of Flight Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Sensors'
documentation_page: 'vl53l0xtimeofflightsensor'
documentation_source_path: 'nucleo/ref/vl53l0xtimeofflightsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# VL53L0X Time of Flight Sensor

## 端口

### 输出

### **Distance** — 目标物体距离向量

**Distance** 端口输出目标物体的距离，单位为 millimeters

**数据类型：** `uint16`

## 参数

### **I2C module** — 用于通信的模块 `0`（默认值）

指定板上用于 I2C 通信的模块。

### **I2C address** — 传感器的 I2C 地址 `0x29`（默认值）

VL53L0X 传感器的 I2C 地址，模块从该地址读取值。您可以配置此值。I2C 地址范围为 `0x08` 到 `0x77`。

### **Ranging Mode** — VL53L0X 传感器的距离测量模式 `Default`（默认值） | `High accuracy` | `Long range` | `High speed`

选择用于测量到目标物体距离的测距模式。可用的四种测距模式如下表所示。

| 测距模式 | 时间预算 | 典型最大范围 | 典型应用 |
| --- | --- | --- | --- |
| Default | 30 ms | 1.2 m | 标准 |
| High accuracy | 200 ms | 2 m | 精确测量 |
| Long range | 33 ms | 1.2 m | 黑暗条件下的长距离测距 |
| High speed | 20 ms | 1.2 m | 精度不是优先考虑时的高速测量 |

时间预算是传感器执行一次距离测量所需的时间。

### **Sample time** — 读取数据的时间间隔 `-1`（默认值） | 正整数

指定此模块从 VL53L0X 传感器读取数据的频率。将此参数设置为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

测量到目标物体的距离

VL53L0X Time of Flight Sensor 模块测量完整视场（FOV = 25 degrees）内到目标物体的距离。此模块还提供根据您的需求选择四种测距模式之一的功能。

**注意**

VL53L0X 传感器需要 XSHUT 连接。将 XSHUT 引脚连接到 vcc。
