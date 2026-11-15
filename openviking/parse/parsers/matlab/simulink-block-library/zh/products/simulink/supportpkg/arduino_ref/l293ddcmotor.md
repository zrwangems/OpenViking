---
type: simulink-block
title: 'L293D DC Motor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Motors, Servo Motors, and Motor Drivers'
documentation_page: 'l293ddcmotor'
documentation_source_path: 'supportpkg/arduino_ref/l293ddcmotor.html'
language: zh-CN
chinese_source: worker-translation
---

# L293D DC Motor

## 端口

### 输入

### **Port\_1** — 输入信号值，介于 `–100` 和 `100` 之间

输入信号的符号决定直流电机的旋转方向。正号表示正向旋转，负号表示反向旋转。幅值决定提供给电机的功率。

- `1` 到 `100`：正向旋转，功率从最小到最大。
- `–1` 到 `–100`：反向旋转，功率从最小到最大。
- `0`：不供电。

块输入端口上的任何超出范围的值都与最大或最小输入值具有相同效果。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **Enable pin** — 直流电机上的使能引脚 `5`（默认值）

指定电机驱动扩展板上连接到直流电机的使能引脚编号。

### **Input A pin** — 直流电机的 Input A 引脚编号 `8`（默认值）

指定电机驱动扩展板上连接到直流电机的 Input A 引脚编号。

不要将同一引脚编号分配给同一模型中的多个 DC Motor 模块。

### **Input B pin** — 直流电机的 Input B 引脚编号 `10`（默认值）

指定电机驱动扩展板上连接到直流电机的 Input B 引脚编号。

不要将同一引脚编号分配给同一模型中的多个 DC Motor 模块。

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2023a 中引入**

## 描述

控制直流电机的功率和方向

L293D DC Motor 模块控制连接到 L293D 和 L298N 等电机驱动扩展板的直流电机的功率和方向。

### 支持的硬件

L293D DC Motor 模块支持所有 Arduino 板。
