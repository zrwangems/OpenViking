---
type: simulink-block
title: 'M1M2DCMotors'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Motors, Servo Motors, and Motor Drivers'
documentation_page: 'm1m2dcmotors'
documentation_source_path: 'supportpkg/arduino_ref/m1m2dcmotors.html'
language: zh-CN
chinese_source: worker-translation
---

# M1M2DCMotors

## 端口

### 输入

### **Port\_1** — `–100` 到 `100` 之间的输入信号值

输入信号的符号决定直流电机的旋转方向。正号表示正向旋转，负号表示反向旋转。幅值决定提供给电机的功率。

- `1` 到 `100`：正向
  旋转，从最小功率到最大功率。
- `–1` 到 `–100`：反向
  旋转，从最小功率到最大功率。
- `0`：不提供功率。

模块输入端口处任何超出范围的值，其效果与最大或最小输入值相同。例如，值 `500` 会被解释为最大值 100。模块输入继承上游模块的数据类型，并在内部将输入转换为 `uint8`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **电机端口** — MKR 或 Nano Motor Carrier 上的端口号 `M1`（默认）| `M2`

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

控制端口 M1 或 M2 上直流电机的功率和方向

M1 M2 DC Motors 模块控制连接到 MKR 或 Nano Motor Carrier 的直流电机的功率和方向。输入信号决定提供给电机的功率以及电机的旋转方向。

如果仿真包含 M1 M2 DC Motors 模块的模型而不连接硬件，则该模块输出零。请参阅“模块在仿真中输出零或不执行任何操作”。

### 支持的硬件

只能将 M1 M2 DC Motors 模块与 MKR 和 Nano 33 IoT 板配合使用。
