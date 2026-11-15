---
type: simulink-block
title: 'Touch Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Sensor Blocks'
documentation_page: 'touchsensor'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/touchsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Touch Sensor

## 端口

### 输出

### **Status** — EV3 主机触摸传感器的状态 `0` | `1`

该模块输出 LEGO
MINDSTORMS EV3 主机触摸传感器的状态。

- `0` — 表示触摸传感器未被按下。
- `1` — 表示触摸传感器被按下。

**数据类型：** `uint8`

## 参数

### **EV3 主机输入端口** — EV3 主机的输入端口编号 `1`（默认） | `2` | `3` | `4`

选择触摸传感器所连接的 EV3 主机输入端口。避免将多个设备分配到同一个输入端口。

### **采样时间** — 模块读取 EV3 主机触摸传感器状态的时间间隔 `0.1`（默认） | 正整数

指定模块读取触摸传感器状态的频率。较短的采样时间（例如 `0.01`）可能会产生不可靠的测量结果。

较小的采样时间要求处理器在更短时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2012a 中引入**

## 描述

检测 EV3 主机触摸传感器的状态

使用 Touch Sensor 模块检测连接到
LEGO®
MINDSTORMS® EV3 主机的触摸传感器是否被按下。

在没有硬件的仿真期间，此模块输出零。请参阅“模块在仿真中产生零或不执行任何操作”。
