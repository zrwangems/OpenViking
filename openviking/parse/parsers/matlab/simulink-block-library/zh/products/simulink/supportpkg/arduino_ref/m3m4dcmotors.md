---
type: simulink-block
title: 'M3M4DCMotors'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Motors, Servo Motors, and Motor Drivers'
documentation_page: 'm3m4dcmotors'
documentation_source_path: 'supportpkg/arduino_ref/m3m4dcmotors.html'
language: zh-CN
chinese_source: worker-translation
---

# M3M4DCMotors

## 端口

### 输入

### **Port\_1** — 介于 `–255` 和 `255` 之间的输入信号值

输入信号的符号决定直流电机的旋转方向。正号表示正向旋转，而负号表示反向旋转。幅值决定提供给电机的功率。

- `1` 到 `255`：正向旋转，功率从最小到最大。
- `–1` 到 `–255`：反向旋转，功率从最小到最大。
- `0`：不提供功率。

在模块输入端口处，任何超出范围的值都具有与最大或最小输入值相同的效果。例如，值 `500` 会被解释为最大值 100。模块输入继承上游模块的数据类型，并在内部将输入转换为 `uint8`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **电机端口** — MKR 或 Nano Motor Carrier 上的端口号 `M3`（默认） | `M4`

选择 MKR 或 Nano Motor Carrier 上连接直流电机的端口号。

## 所属库

Simulink Support Package for Arduino Hardware / Arduino Motor Carrier

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019a 中引入**

## 描述

控制端口 M3 或 M4 上直流电机的功率和方向

M3 M4 DC Motors 模块控制连接到 MKR 或 Nano Motor Carrier 的直流电机的功率和方向。输入信号决定提供给电机的功率以及电机的旋转方向。

如果在未连接硬件的情况下仿真包含 M3 M4 DC Motors 模块的模型，该模块输出零。请参阅“模块在仿真中产生零值或不执行任何操作”。

### 支持的硬件

只能将 M3 M4 DC Motors 模块与 MKR 和 Nano 33 IoT 开发板配合使用。
