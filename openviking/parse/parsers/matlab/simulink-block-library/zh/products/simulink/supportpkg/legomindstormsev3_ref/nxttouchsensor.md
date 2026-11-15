---
type: simulink-block
title: 'NXT Touch Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Sensor Blocks'
documentation_page: 'nxttouchsensor'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/nxttouchsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# NXT Touch Sensor

## 端口

### 输出

### **Status** — NXT 触摸传感器的状态 `0` | `1`

该模块输出 LEGO
MINDSTORMS EV3 NXT 触摸传感器的状态。

- `0` — 表示 NXT 触摸传感器未按下。
- `1` — 表示 NXT 触摸传感器已按下。

**数据类型：** `uint8`

## 参数

### **EV3 brick input port number** — EV3 brick 的输入端口号 `1`（默认）| `2` | `3` | `4`

选择 NXT 触摸传感器连接到的 EV3 brick 输入端口。避免
将多个设备分配到同一输入端口。

### **Sample time** — 模块读取 EV3 brick 触摸传感器状态的时间间隔 `0.1`（默认）| 正整数

指定模块读取 NXT 触摸传感器状态的频率。
较短的采样时间（例如 `0.01`）可能会产生不可靠的
测量结果。

较小的采样时间要求处理器在更短时间内完成相同数量的
指令，这可能导致任务超限。

## 所属库

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware / NXT Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2012a 中引入**

## 描述

检测 EV3 brick NXT 触摸传感器的状态

使用 NXT Touch Sensor 模块检测连接到 LEGO®
MINDSTORMS® EV3 brick 的 NXT 触摸传感器是否按下。

在没有硬件的仿真期间，此模块输出零。请参阅 Block Produces Zeros or Does Nothing in Simulation。
