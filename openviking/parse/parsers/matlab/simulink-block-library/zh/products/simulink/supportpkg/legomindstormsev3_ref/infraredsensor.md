---
type: simulink-block
title: 'Infrared Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Sensor Blocks'
documentation_page: 'infraredsensor'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/infraredsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Infrared Sensor

## 端口

### 输出

### **Button ID** — 按钮识别编号 正整数

模块输出在 LEGO® 遥控红外传感器上按下的按钮的识别编号。

Button ID 表

#### 依赖项

- 要启用此端口，请将 **Mode** 设置为 `Remote`。

**数据类型：** `int8`

### **Heading** — 信标接近角度 整数 [`-25`, `25`]

模块输出从红外传感器指向方向算起的角度。

#### 依赖项

- 要启用此端口，请将 **Mode** 设置为 `Beacon Proximity`。

**数据类型：** `int8`

### **Proximity** — 信标接近度百分比 正整数 [`0`, `100`]

模块以百分比形式输出红外传感器前方物体的接近度。

#### 依赖项

- 要启用此端口，请将 **Mode** 设置为 `Beacon Proximity` 或 `Proximity`。

**数据类型：** `uint8`

## 参数

### **EV3 主机输入端口号** — EV3 主机的输入端口号 `1`（默认） | `2` | `3` | `4`

选择红外传感器连接到的 EV3 主机输入端口。避免将多个设备分配到同一个输入端口。

### **Mode** — 红外传感器操作模式 `Remote`（默认） | `Beacon Proximity` | `Proximity`

### **Channel** — EV3 主机红外信标通道号 `1`（默认） | `2` | `3` | `4`

选择 EV3 主机上的红外信标通道号。

#### 依赖项

- 要启用此参数，请将 **Mode** 设置为 `Remote` 或 `Beacon Proximity`。

### **采样时间** — 模块读取传感器值的时间间隔 `0.1`（默认） | 正整数

指定模块读取连接到 EV3 主机的传感器值的频率。较短的采样时间（如 `0.01`）可能会产生不可靠的测量结果。

更短的采样时间要求处理器在更短时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2013a 中引入**

## 描述

检测 LEGO 遥控红外信标上的按钮状态，测量信标接近度和方向，并使用连接到 EV3 主机的红外传感器测量物体接近度

使用 Infrared Sensor 模块，通过连接到 EV3 主机的红外传感器测量和检测以下参数。

- 检测在遥控红外信标上按下的按钮
- 测量信标接近度和方向
- 使用红外传感器测量物体接近度

在没有硬件的仿真期间，此模块输出零。请参阅“在仿真中模块产生零或不执行任何操作”。
