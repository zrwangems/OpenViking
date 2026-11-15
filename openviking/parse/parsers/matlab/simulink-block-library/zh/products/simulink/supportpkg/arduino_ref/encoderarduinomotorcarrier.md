---
type: simulink-block
title: 'Encoder'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Motors, Servo Motors, and Motor Drivers'
documentation_page: 'encoderarduinomotorcarrier'
documentation_source_path: 'supportpkg/arduino_ref/encoderarduinomotorcarrier.html'
language: zh-CN
chinese_source: worker-translation
---

# Encoder

## 端口

### 输出

### **Position** — 旋转电机的位置 标量

**Position** 端口输出旋转电机位置的相对变化量，以 ticks 为单位。有关详细信息，请参阅 Calculate Position and Rotational Speed of the Motor。

**数据类型：** `int32`

### **Speed** — 旋转电机的速度 标量

**Speed** 端口输出电机的转速，以 ticks per second 为单位。有关详细信息，请参阅 Calculate Position and Rotational Speed of the Motor。

#### 依赖项

仅当选择 **Show Speed output port** 参数时，**Speed** 端口才可用。

**数据类型：** `int32`

## 参数

### **Encoder** — 编码器通道号 `1`（默认）| `2`

选择连接到 MKR 或 Nano Motor Carrier 的编码器的通道号。

### **Show Speed output port** — 旋转速度 off（默认）| on

选择 **Show Speed output port** 参数后，**Speed** 端口将变为可用。该端口输出电机的转速，以 ticks per second 为单位。

### **Reset count at initialization** — 每次模型开始运行时重置 tick 计数 `on`（默认）| `off`

选择 **Reset count at initialization** 参数后，每次 Simulink® 模型在硬件上运行时，该模块都会将 tick 计数重置为 0。

### **Sample time** — 从编码器读取值的时间间隔 `0.1`（默认）| `-1` | 非负实数值

指定该模块从编码器读取 tick 计数的频率，以秒为单位。当将此参数指定为 `-1` 时，Simulink 将根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Simulink Support Package for Arduino Hardware / Arduino Motor Carrier

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019a 中引入**

## 描述

以 ticks 为单位测量电机的旋转

Encoder 模块从连接到 MKR 或 Nano Motor Carrier 的编码器读取电机的位置和转速。位置以 ticks 为单位测量，速度以 ticks per second 为单位测量。tick 计数每增加一次表示顺时针旋转，每减少一次表示逆时针旋转。

如果在未连接硬件的情况下仿真包含 Encoder 模块的模型，该模块将输出零。有关详细信息，请参阅 Block Produces Zeros or Does Nothing in Simulation。
