---
type: simulink-block
title: 'Tachometer'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Motor and Vehicle Sensors'
documentation_page: 'tachometer'
documentation_source_path: 'supportpkg/arduino_ref/tachometer.html'
language: zh-CN
chinese_source: worker-translation
---

# Tachometer

## 端口

### 输出

### **Port\_1** — 轴的转速（标量）

该端口输出连接到硬件的轴的转速。

**数据类型：** `uint32`

## 参数

### **引脚编号** — 硬件上的引脚编号 `2`（默认值）

指定转速计所连接硬件上的引脚编号。

单击 **查看引脚映射** 以打开 Arduino 引脚映射表。

要了解如何为该模块分配引脚，请参阅 Arduino 定时器无关模块的引脚映射。

有关硬件上支持来自转速计的中断的引脚的详细信息，请参阅具有中断的引脚。

### **中断模式** — 转速计信号的计数方式 `RISING`（默认值） | `FALLING` | `CHANGE` | `LOW` | `HIGH`

中断模式指定转速计如何对其输出信号进行计数。不同中断模式的计数方式不同：

- `RISING` – 对信号的每个上升沿进行计数。
- `FALLING` – 对信号的每个下降沿进行计数。
- `CHANGE` – 对信号的每个上升沿和下降沿进行计数。
- `LOW` – 对每个低信号进行计数。
- `HIGH` – 对每个高信号进行计数。

此图显示了转速计在不同中断模式下如何对其输出信号进行计数。

### **每转脉冲计数** — 每转的中断数 `1`（默认值） | 任意正整数

指定该模块每转接收的中断数。

### **采样时间** — 从转速计读取值的时间间隔 `0.1`（默认值）

指定该模块从转速计读取转速的时间间隔，以秒为单位。

## 所属库

Simulink Support Package for Arduino Hardware / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2018b 中引入**

## 描述

读取轴的转速

Tachometer 模块从连接到硬件的转速计读取轴的转速。该模块将旋转速度输出为 `uint32` 值。

如果在未连接硬件的情况下仿真包含 Tachometer 模块的模型，该模块输出零。有关详细信息，请参阅模块在仿真中产生零或不执行任何操作。
