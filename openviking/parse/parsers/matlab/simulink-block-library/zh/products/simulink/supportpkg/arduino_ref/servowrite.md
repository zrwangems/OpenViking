---
type: simulink-block
title: 'Servo Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Motors, Servo Motors, and Motor Drivers'
documentation_page: 'servowrite'
documentation_source_path: 'supportpkg/arduino_ref/servowrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Servo Write

## 端口

### 输入

### **Port\_1** — 轴的旋转角度值，介于 `0` 和 `180` 之间

输入信号是轴的旋转角度，单位为 degrees。
你指定的轴角度必须是
`0` degrees 到 `180` degrees 之间的任意值。模块输入端口处任何
超出范围的值，其效果与
最大或最小输入值相同。例如，`500`
被视为 180，`-500` 被视为 0。

模块输入继承上游模块的数据类型，并
在内部将输入转换为 `uint8`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **Motor port** — MKR Motor Carrier 上的端口号 `1` (default) | `2` | `3` | `4`

选择伺服电机所连接的 MKR Motor Carrier 上的端口号。

## 所属库

Simulink Support Package for Arduino Hardware / Arduino Motor Carrier

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019a 中引入**

## 描述

将伺服电机设置到指定角度

Servo Write 模块设置连接到 MKR Motor Carrier 的伺服电机的轴角度。要旋转电机轴，请提供介于
`0` degrees 和 `180` degrees 之间的输入值。

如果仿真包含 Servo Write 模块的模型而不连接硬件，则该模块不执行任何操作。有关详细信息，请参阅“模块在仿真中产生零值或不执行任何操作”。

### 支持的硬件

只能将 Servo Write 模块与 MKR 和 Nano 33 IoT
开发板配合使用。
