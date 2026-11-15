---
type: simulink-block
title: 'Gyro Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Sensor Blocks'
documentation_page: 'gyrosensor'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/gyrosensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Gyro Sensor

## 端口

### 输出

### **Rotation** — 陀螺仪传感器的旋转速率（标量）

该模块输出连接到 EV3 brick 的陀螺仪传感器的旋转速率，单位为 degrees per second。

**数据类型：** `int32`

## 参数

### **EV3 brick 输入端口** — EV3 brick 的输入端口号 `1`（默认）| `2` | `3` | `4`

选择陀螺仪传感器连接到的 EV3 brick 输入端口。避免将多个设备分配到同一个输入端口。

### **采样时间** — 模块读取传感器值的时间间隔 `0.1`（默认）| 正整数

指定模块读取连接到 EV3 brick 的传感器值的频率。较短的采样时间（例如 `0.01`）可能会产生不可靠的测量结果。

更短的采样时间要求处理器在更短时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2013a 中引入**

## 描述

测量连接到 EV3 brick 的陀螺仪传感器的旋转速率

使用 Gyro Sensor 模块测量连接到 EV3 brick 的陀螺仪传感器的旋转速率，单位为 degrees per second。

在没有硬件的仿真中，此模块输出零。请参阅“模块在仿真中产生零值或不执行任何操作”。
