---
type: simulink-block
title: 'Color Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Sensor Blocks'
documentation_page: 'colorsensor'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/colorsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Color Sensor

## 端口

### 输出

### **Color** — 颜色数据、颜色模式、颜色强度

该模块输出传感器检测到的对象或其周围的颜色数据。

#### 依赖关系

该模块根据您选择的模式输出这些颜色值。

- `Color` — 该模块输出对象的颜色。
- `Reflected light intensity` — 该模块输出对象的颜色强度。
- `Ambient light intensity` — 该模块输出周围环境的光强度。

**数据类型：** `uint8`

## 参数

### **EV3 brick input port** — EV3 主机的输入端口号 `1`（默认） | `2` | `3` | `4`

选择颜色传感器连接的 EV3 主机输入端口。避免将多个设备分配到同一输入端口。

### **Mode** — 传感器的光检测模式 `Color`（默认） | `Reflected light intensity` | `Ambient light intensity`

选择连接到 EV3 主机的传感器的光检测模式。

- `Color` — 在此模式下，传感器评估对象的颜色，并在模块的输出端口上输出以下值之一。

  - `0` — 表示传感器未检测到颜色。
  - `1` — 表示传感器检测到黑色。
  - `2` — 表示传感器检测到蓝色。
  - `3` — 表示传感器检测到绿色。
  - `4` — 表示传感器检测到黄色。
  - `5` — 表示传感器检测到红色。
  - `6` — 表示传感器检测到白色。
  - `7` — 表示传感器检测到棕色。

  例如，您可以将此模式用于基于 EV3 的机器人来解魔方。
- `Reflected light intensity` — 在此模式下，传感器闪烁 LED 并测量附近表面反射的光量。该模块输出 `0` 到 `100` 的值，其中 `0` 表示深色表面，`100` 表示浅色表面。例如，您可以将此模式用于基于 EV3 的机器人，使其在障碍赛道中检测并沿黑线行进。
- `Ambient light intensity` — 在此模式下，传感器测量周围环境光。该模块输出 `0` 到 `100` 的值，其中 `0` 表示周围环境较暗，`100` 表示周围环境较亮。例如，您可以将此模式用于基于 EV3 的机器人来跟随光源。

### **Sample time** — 模块读取传感器值的时间间隔 `0.1`（默认） | 正整数

指定模块从连接到 EV3 主机的传感器读取值的频率。较短的采样时间（例如 `0.01`）可能会产生不可靠的测量结果。

较小的采样时间要求处理器在更短时间内完成相同数量的指令，这可能导致任务溢出。

## 所属库

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2012a 中引入**

## 描述

使用 EV3 主机检测颜色、反射光或环境光

使用 Color Sensor 模块，通过连接到 LEGO® MINDSTORMS® EV3 主机的颜色传感器来检测对象颜色、测量反射光或测量环境光。

在没有硬件的仿真期间，此模块输出零。请参阅“仿真中模块产生零或不执行任何操作”。
