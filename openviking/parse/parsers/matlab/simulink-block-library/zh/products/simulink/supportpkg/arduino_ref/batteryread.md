---
type: simulink-block
title: 'Battery Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Motors, Servo Motors, and Motor Drivers'
documentation_page: 'batteryread'
documentation_source_path: 'supportpkg/arduino_ref/batteryread.html'
language: zh-CN
chinese_source: worker-translation
---

# Battery Read

## 端口

### 输出

### **Port\_1** — 电池电压标量，范围为 [0, 4095]

该端口输出连接到 MKR 或 Nano Motor Carrier 的电池电压。该模块将电压输出为 `0` 到 `4095` 之间的 12-bit 数字值。输出 `0` 对应于连接到电池的模拟引脚上的最小 volts，输出 `4095` 对应于该引脚上的最大 volts。

**数据类型：** `uint16`

## 参数

### **采样时间** — 读取电池电压的时间间隔 `0.1`（默认） | `-1` | 非负实数值

指定该模块读取电池电压的频率，以 seconds 为单位。当将此参数指定为 `-1` 时，Simulink® 会根据模型中的模块上下文确定为该模块使用的最佳采样时间。

## 所属库

Simulink Support Package for Arduino Hardware / Arduino Motor Carrier

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019a 中引入**

## 描述

读取电池电压

Battery Read 模块读取连接到 MKR 或 Nano Motor Carrier 的电池电压。该模块将电压输出为 `0` 到 `4095` 之间的 12-bit 数字值。输出 `0` 对应于连接到电池的模拟引脚上的最小 volts，输出 `4095` 对应于该引脚上的最大 volts。

如果在未连接硬件的情况下仿真包含 Battery Read 模块的模型，则该模块输出零。有关详细信息，请参阅模块在仿真中产生零值或不执行任何操作。

### 支持的硬件

Battery Read 模块只能与 MKR 和 Nano 33 IoT 板配合使用。
