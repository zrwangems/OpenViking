---
type: simulink-block
title: 'NXT Sound Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Sensor Blocks'
documentation_page: 'nxtsoundsensor'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/nxtsoundsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# NXT Sound Sensor

## 端口

### 输出

### **Sound level** — 周围声音级别标量

该模块以归一化或原始模数转换格式输出周围声音级别。

**数据类型：** `uint16`

## 参数

### **EV3 程序块输入端口号** — EV3 程序块的输入端口号 `1`（默认） | `2` | `3` | `4`

选择超声波传感器所连接的 EV3 程序块输入端口。避免将多个设备分配到同一输入端口。

### **输出模式** — Sound level 输出格式 `Normalised (0-100)`（默认） | `Raw A/D (1023-0)`

选择该模块输出的声音数据类型。

- `Normalised (0-100)` — 以 0 到 100 的刻度输出声音强度，其中 0 表示最弱强度的声音，100 表示最强强度的声音。
- `Raw A/D (1023-0)` — 以 1023 到 0 的刻度输出声音强度，其中 1023 表示最弱强度的声音，0 表示最强强度的声音。

### **采样时间** — 模块读取传感器值的时间间隔 `0.1`（默认） | 正整数

指定模块读取连接到 EV3 程序块的传感器值的频率。较短的采样时间（例如 `0.01`）可能会产生不可靠的测量结果。

较小的采样时间要求处理器在更短时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware / NXT Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2012a 中引入**

## 描述

使用连接到 EV3 程序块的 NXT 声音传感器测量周围声音级别

使用 NXT Sound Sensor 模块，通过连接到 LEGO® MINDSTORMS® EV3 程序块的 NXT 声音传感器测量周围声音级别。

在没有硬件的仿真中，此模块输出零。请参阅“模块在仿真中产生零或不执行任何操作”。
