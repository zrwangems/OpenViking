---
type: simulink-block
title: 'Ultrasonic Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sensors / IMU Sensors'
documentation_page: 'ultrasonicsensor'
documentation_source_path: 'supportpkg/raspberrypi_ref/ultrasonicsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Ultrasonic Sensor

## 端口

### 输出

### **Distance** — 超声波传感器与传感器前方最近物体之间的距离，标量

该端口输出连接到硬件的超声波传感器与传感器前方最近物体之间的距离。该模块以 meters 为单位输出距离。如果物体放置在传感器检测范围之外，则该端口输出 `0`。

**数据类型：** `double`

## 参数

### **Board** — 用于连接超声波传感器的板 `Pi 4 Model B`（默认） | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 2 Model B` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Compute Module 4` | `Pi Zero 2 W` | `Pi 5 Model`

选择超声波传感器连接到的 Raspberry Pi® 硬件板。有关硬件上数字引脚编号的信息，请点击 **查看引脚映射**。

### **Number of signal pins** — 超声波传感器上的信号引脚数量 `2`（默认） | `1`

选择超声波传感器上用于发送和接收声波的信号引脚数量。

- `1` — 如果超声波传感器只有一个信号引脚 SIG，则选择 `1`。
- `2` — 如果超声波传感器有两个单独的信号引脚 Trig 和 Echo，则选择 `2`。

### **Trigger pin** — 连接到 Trig 引脚的数字引脚 `GPIO 23`（默认） | `GPIO 4` | `GPIO 17` | `GPIO 27` | `GPIO 22` | `GPIO 10` | `GPIO 9` | `GPIO 11` | `GPIO 14` | `GPIO 15` | `GPIO 18` | `GPIO 24` | `GPIO 25` | `GPIO 8` | `GPIO 7`

选择硬件上连接到超声波传感器 Trig 引脚的数字引脚。有关硬件上数字引脚编号的信息，请点击 **查看引脚映射**。

#### 依赖项

仅当您将 **Number of signal pins** 参数设置为 `2` 时，才会显示 **Trigger pin** 参数。

### **Echo pin** — 连接到 Echo 引脚的数字引脚 `GPIO 24`（默认） | `GPIO 4` | `GPIO 17` | `GPIO 27` | `GPIO 22` | `GPIO 10` | `GPIO 9` | `GPIO 11` | `GPIO 14` | `GPIO 15` | `GPIO 18` | `GPIO 23` | `GPIO 25` | `GPIO 8` | `GPIO 7`

选择硬件上连接到超声波传感器 Echo 引脚的数字引脚。有关硬件上数字引脚编号的信息，请点击 **查看引脚映射**。

#### 依赖项

仅当您将 **Number of signal pins** 参数设置为 `2` 时，才会显示 **Echo pin** 参数。

### **Signal pin** — 连接到 SIG 引脚的数字引脚 `GPIO 23`（默认） | `GPIO 4` | `GPIO 17` | `GPIO 27` | `GPIO 22` | `GPIO 10` | `GPIO 9` | `GPIO 11` | `GPIO 14` | `GPIO 15` | `GPIO 18` | `GPIO 24` | `GPIO 25` | `GPIO 8` | `GPIO 7`

选择硬件上连接到超声波传感器 SIG 引脚的数字引脚。有关硬件上数字引脚编号的信息，请点击 **查看引脚映射**。

#### 依赖项

仅当您将 **Number of signal pins** 参数设置为 `1` 时，才会显示 **Signal pin** 参数。

### **Sample time** — 使用超声波传感器读取距离的间隔 `0.1`（默认） | `-1` | 任意非负值

指定该模块使用超声波传感器读取距离的频率，以 seconds 为单位测量。

指定 **Sample time** 时，请验证以下设置以避免任务超限：

1. **Sample time** 参数必须等于模型基本速率。要查看模型基本速率，请在模型工具栏上选择 **显示** > **采样时间** > **全部**。在采样时间图例对话框中，红色框对应的值就是模型的基本速率。
2. **Sample time** 参数和模型基本速率必须大于传感器发送和接收声波所需的总时间。例如，如果物体放置在距传感器 0.1 meters 处，则指定的 **Sample time** 参数必须大于 `0.000301` seconds。

   有关如何计算声波传播时间的信息，请参阅计算声波的传播时间。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

## 描述

测量超声波传感器与物体之间的距离

Ultrasonic Sensor 模块输出连接到硬件的超声波传感器与传感器前方最近物体之间的距离。该模块以双精度值输出距离，单位为 meters。如果物体放置在传感器检测范围之外，则该模块输出 `0`。

如果在不连接硬件的情况下仿真包含 Ultrasonic Sensor 模块的模型，则该模块输出零。有关详细信息，请参阅模块在仿真中产生零值或不执行任何操作。
