---
type: simulink-block
title: 'NXT Gyro Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Sensor Blocks'
documentation_page: 'nxtgyrosensor'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/nxtgyrosensor.html'
language: zh-CN
chinese_source: worker-translation
---

# NXT Gyro Sensor

## 端口

### 输出

### **Rotation** — 陀螺仪传感器的旋转速率标量

该模块输出连接到 EV3 brick 的陀螺仪传感器的旋转速率，单位为度每秒。

**数据类型：** `int32`

## 参数

### **EV3 brick input port number** — EV3 brick 的输入端口号 `1`（默认） | `2` | `3` | `4`

选择 NXT 陀螺仪传感器连接到的 EV3 brick 输入端口。避免将多个设备分配到同一输入端口。

### **Output mode** — 传感器旋转数据输出 `Rotation rate (-360 to 360)`（默认） | `Raw A/D (1023 to 0)`

- `Rotation rate (-360 to 360)` — 该模块输出旋转速率，单位为度每秒。
- `Raw A/D (1023 to 0)` — 该模块输出旋转速率，单位为原始模数转换值每秒。

### **Offset** — 传感器偏置偏移值 `600`（默认） | 正或负整数

输入正或负的传感器偏置偏移值。使用此参数中的值，直到传感器偏置接近零。

#### 依赖关系

- 要启用此参数，请将 **Output mode** 设置为
  `Rotation rate (-360 to 360)`。

### **Sample time** — 模块读取传感器值的时间间隔 `0.1`（默认） | 正整数

指定模块读取连接到 EV3 brick 的传感器值的频率。较短的采样时间（例如 `0.01`）可能会产生不可靠的测量结果。

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

测量连接到 EV3 brick 的 NXT 陀螺仪传感器的旋转速率

使用 NXT Gyro Sensor 模块测量沿连接到 LEGO® MINDSTORMS® EV3 brick 的 HiTechnic NXT Gyro Sensor (NGY1044) 的单轴旋转速率（yaw）。此 yaw 由左图中垂直轴上方的圆圈表示，并由右图中的双箭头表示。在将此传感器用于精确测量之前，请使用偏移值消除输出值中的微小正偏置或负偏置，如下面的示例所述。有关 NXT Gyro Sensor NGY1044 的详细信息，请参阅其数据表。

在无硬件仿真期间，此模块输出零。请参阅“模块在仿真中产生零或不执行任何操作”。

Lego NXT Gyro Sensor
