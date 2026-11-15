---
type: simulink-block
title: 'PCA9685 DC Motor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Motors, Servo Motors, and Motor Drivers'
documentation_page: 'pca9685dcmotor'
documentation_source_path: 'supportpkg/arduino_ref/pca9685dcmotor.html'
language: zh-CN
chinese_source: worker-translation
---

# PCA9685 DC Motor

## 端口

### 输入

### **Port\_1** — 输入信号值介于 `–100` 和 `100` 之间

输入信号的符号决定直流电机的旋转方向。正号表示正向旋转，而负号表示反向旋转。幅值决定提供给电机的功率。

- `1` 到 `100`：正向旋转，从最小到最大功率。
- `–1` 到 `–100`：反向旋转，从最小到最大功率。
- `0`：不提供功率。

模块输入端口上的任何超出范围的值，其效果与最大或最小输入值相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **I2C module** — I2C 通信模块 `0`（默认） | scalar

指定 Arduino® 硬件上用于与传感器外设通信的 I2C 模块。有关 Arduino 引脚映射以及硬件板支持的模块的详细信息，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

### **PCA9685 address** — 基于 PCA9685 PWM 芯片的扩展板上的地址 `0X60`（默认）

输入连接到直流电机的基于 PCA9685 PWM 芯片的扩展板上的 PCA9685 地址。

### **PWM frequency (Hz)** — 直流电机的 PWM 频率 `1200`（默认）

指定连接到直流电机的基于 PCA9685 PWM 芯片的扩展板上用于生成脉冲宽度调制信号的频率（以 hertz 为单位）。

### **Motor Channel** — 直流电机的电机通道 `1`（默认） | `1` 到 `4`

指定连接到直流电机的基于 PCA9685 PWM 芯片的扩展板上的电机通道。

不要在同一模型中的多个 DC Motor 模块中分配相同的通道号。

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023a 中引入**

## 描述

控制直流电机的功率和方向

PCA9685 DC Motor 模块控制连接到基于 PCA9685 PWM 芯片的扩展板（如 Adafruit Motor Shield V2）的直流电机的功率和方向。输入信号决定提供给电机的功率以及电机的旋转方向。

### 支持的硬件

PCA9685 DC Motor 模块支持所有 Arduino 板。
