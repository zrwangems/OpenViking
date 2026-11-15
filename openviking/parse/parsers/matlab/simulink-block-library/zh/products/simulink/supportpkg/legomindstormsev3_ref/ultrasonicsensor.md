---
type: simulink-block
title: 'Ultrasonic Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Sensor Blocks'
documentation_page: 'ultrasonicsensor'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/ultrasonicsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Ultrasonic Sensor

## 端口

### 输出

### **Distance** — 超声波传感器与其前方最近物体之间的距离 标量

该模块输出连接到 EV3 brick 的超声波传感器与该传感器前方最近物体之间的距离。该模块以 centimeters 为单位输出该距离。

当最近物体超出超声波传感器的最大范围时，该模块输出最大值 255。当物体放置在传感器检测范围之外时，该端口输出 0。

**数据类型：** `uint8`

## 参数

### **EV3 brick 输入端口** — EV3 brick 的输入端口号 `1`（默认）| `2` | `3` | `4`

选择超声波传感器连接到的 EV3 brick 输入端口。避免将多个设备分配到同一个输入端口。

### **采样时间** — 模块读取传感器值的时间间隔 `0.1`（默认）| 正整数

指定模块读取连接到 EV3 brick 的传感器值的频率。较短的采样时间（例如 `0.01`）可能会产生不可靠的测量结果。

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

测量连接到 EV3 brick 的超声波传感器与最近物体之间的距离

使用 Ultrasonic Sensor 模块测量连接到 EV3 brick 的超声波传感器与该传感器前方最近物体之间的距离。该传感器可以检测大约 5 到 255 centimeters 远的物体。该模块测量与物体之间的近似距离。为获得更高精度，请根据物理测量结果校准传感器输出值。

传感器首次检测到接近物体的距离取决于以下因素。

- 物体的超声波反射率，它是物体大小和组成的函数。与小型柔软物体相比，传感器从更远距离检测大型坚硬物体。例如，传感器可能在 255 cm 处检测到一块玻璃，在 150 cm 处检测到手偶。
- 物体相对于传感器的入射角。与位于侧面的物体相比，传感器从更远距离检测正前方的物体。

在没有硬件的仿真过程中，该模块输出零。请参阅 Block Produces Zeros or Does Nothing in Simulation。
