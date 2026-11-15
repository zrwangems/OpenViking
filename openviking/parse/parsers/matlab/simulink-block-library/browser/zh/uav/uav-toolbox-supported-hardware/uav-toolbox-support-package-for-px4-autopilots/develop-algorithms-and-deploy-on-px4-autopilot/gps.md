---
type: simulink-block
title: 'GPS'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'gps'
documentation_source_path: 'px4/ref/gps.html'
language: zh-CN
chinese_source: worker-translation
---

# GPS

## 端口

### 输出

### **Status** — 接收到的 uORB 数据的状态 `0` | `1`

Status 输出指示在前一个时间步期间是否接收到 vehicle\_gps\_position uORB 消息。值 `0` 表示输出端的 uORB 数据是最新的，值 `1` 表示 uORB 数据在前一个时间步期间未更新。

此输出可用于触发子系统，以处理 uORB 网络中接收到的新消息。

**数据类型：** `Boolean`

### **Latitude** — PX4 Autopilot 的纬度 标量 | 1e-7 degrees

基于连接到 PX4 Autopilot 的 GPS 接收机当前位置的纬度坐标，从 vehicle\_gps\_position uORB 主题读取。

**数据类型：** `int32`

### **Longitude** — PX4 Autopilot 的经度 标量 | 1e-7 degrees

基于连接到 PX4 Autopilot 的 GPS 接收机当前位置的经度坐标，从 vehicle\_gps\_position uORB 主题读取。

**数据类型：** `int32`

### **Altitude(MSL)** — PX4 Autopilot 高于平均海平面 (MSL) 的高度 标量 | millimeters

基于 GPS 接收机当前位置高于平均海平面的高度坐标，从 vehicle\_gps\_position uORB 主题读取。

**数据类型：** `int32`

### **Speed** — PX4 Autopilot 的地速 标量 | meters/sec

来自连接到 PX4 Autopilot 的 GPS 接收机的地速坐标，从 vehicle\_gps\_position uORB 主题读取。

#### 依赖项

仅当选择了 **Ground speed (m/s)** 参数时，此输出才会出现。

**数据类型：** `float32`

### **Course** — PX4 Autopilot 的对地航向 标量 | radians

对地航向（不是航向，而是运动方向）值，范围为 (-π 到 π)，基于连接到 PX4 Autopilot 的 GPS 接收机的运动方向，从 vehicle\_gps\_position uORB 主题读取。

#### 依赖项

仅当选择了 **Course (rad)** 参数时，此输出才会出现。

**数据类型：** `float32`

### **Fix Type** — GPS 接收机的定位类型 标量

GPS 接收机用于确定位置所使用的信号或技术类型，从 vehicle\_gps\_position uORB 主题读取。下表表示此信号的值：

| 值 | 定位类型 |
| --- | --- |
| 0-1 | 无定位 |
| 2 | 2D 定位 |
| 3 | 3D 定位 |
| 4 | RTCM 码差分 |
| 5 | Real-Time Kinematic，float |
| 6 | Real-Time Kinematic，fixed |
| 8 | 外推。除非该字段值至少为 2，否则某些应用不会使用此字段的值，因此应始终正确填写定位类型。 |

#### 依赖项

仅当选择了 **GPS fix type** 参数时，此输出才会出现。

**数据类型：** `uint8`

### **Num Sats** — 用于全球定位的卫星数量 标量

GPS 接收机用于确定 GPS 坐标的卫星数量，从 vehicle\_gps\_position uORB 主题读取。

#### 依赖项

仅当选择了 **Number of satellites** 参数时，此输出才会出现。

**数据类型：** `uint8`

### **UTC Time** — 从 GPS 接收机获取的、采用 Unix 时间的 UTC 时间戳（以 microseconds 为单位）

从 GPS 接收机获取的、采用 Unix 时间的 UTC 时间戳（以 microseconds 为单位），从 vehicle\_gps\_position uORB 主题读取。值在冷启动后可能不可用，用值 0 表示。

#### 依赖项

仅当选择了 **Unix timestamp UTC (us)** 参数时，此输出才会出现。

**数据类型：** `uint64`

### **DOP** — GPS 接收机使用的水平和垂直精度因子 2-by-1 向量

GPS 接收机使用的水平和垂直精度因子 (DOP)，从 vehicle\_gps\_position uORB 主题读取。

#### 依赖项

仅当选择了 **Dilution of precision** 参数时，此输出才会出现。

**数据类型：** `float32`

### **NED velocity** — PX4 Autopilot 的北向、东向和地向速度 3-by-1 向量 | meters/sec

连接到 PX4 Autopilot 的 GPS 接收机测得的北向、东向和地向速度，从 vehicle\_gps\_position uORB 主题读取。

#### 依赖项

仅当选择了 **NED velocity** 参数时，此输出才会出现。

**数据类型：** `float32`

### **Altitude(Ellipsoid)** — PX4 Autopilot 高于椭球面的高度 标量 | millimeters

基于椭球模型（高于椭球面 1e-3 meters）的 GPS 接收机当前位置的高度坐标，从 vehicle\_gps\_position uORB 主题读取。

#### 依赖项

仅当选择了 **Altitude above Ellipsoid** 参数时，此输出才会出现。

**数据类型：** `int32`

### **Jamming ind** — GPS 接收机的干扰指示 标量

GPS 接收机的干扰指示值，用于指示是否正在发生信号干扰，从 vehicle\_gps\_position uORB 主题读取。

#### 依赖项

仅当选择了 **Jamming indicator** 参数时，此输出才会出现。

**数据类型：** `int32`

### **Timestamp** — 自系统启动以来接收到的 uORB 数据的时间戳 microseconds

表示自 PX4 系统启动以来，vehicle\_gps\_position uORB 主题最后一次更新所经过的时间。

#### 依赖项

仅当选择了 **PX4 timestamp (us)** 参数时，此输出才会出现。

**数据类型：** `uint64`

## 参数

#### 主选项卡

### **Latitude (1e-7 degrees)** — 启用纬度值作为输出之一 `on` (默认) | `off`

### **Longitude (1e-7 degrees)** — 启用经度值作为输出之一 `on` (默认) | `off`

### **Alititude above MSL (mm)** — 启用高度（高于 MSL）作为输出之一 `off` (默认) | `on`

### **Ground speed (m/s)** — 启用地速值作为输出之一 `off` (默认) | `on`

### **Course (rad)** — 启用对地航向值作为输出之一 `off` (默认) | `on`

### **GPS fix type** — 启用 GPS 定位类型值作为输出之一 `off` (默认) | `on`

### **Number of satellites** — 启用卫星数量作为输出之一 `off` (默认) | `on`

### **Unix timestamp UTC (us)** — 启用 UTC 时间戳值作为输出之一 `off` (默认) | `on`

### **Sample time** — 模块读取值的时间间隔 `1/250` (默认) | 任何为 1/250 倍数的非负值 | -1

输入模块从 uORB 网络读取值的时间间隔。

当将此参数设置为 `-1` 时，Simulink® 根据模型中的模块上下文确定该模块的最佳采样时间。

#### 高级选项卡

### **Wait until data received** — 等待直到请求的数据可用 off (默认) | on

- 选择此选项时，读取操作在 Blocking Mode 下运行。读取操作会被阻塞，直到请求的数据可用。当数据可用时，模块输出所选值，并且 **Status** 端口设置为 `0`。

  板卡在 Blocking Mode 下等待消息，时间为 `Timeout in seconds` 中提到的时长。如果在超时之前未收到数据，则 Status 端口输出 1，并且模块输出最后接收到的值。

  如果在计划开始下一次读取操作时，目标硬件仍在等待数据可用，则会发生任务超限。

  要解决超限，请使用 **Sample time** 参数增大时间步长。
- 清除此选项时，读取操作在 Non-Blocking Mode 下运行。在此模式下，模块不会等待请求的数据可用。

### **Dilution of precision** — 启用精度因子值作为输出之一 `off` (默认) | `on`

### **NED velocity** — 启用 NED velocity 值作为输出之一 `off` (默认) | `on`

### **Altitude above Ellipsoid** — 启用高于椭球面的高度值作为输出之一 `off` (默认) | `on`

### **Jamming indicator** — 启用干扰指示值作为输出之一 `off` (默认) | `on`

### **PX4 timestamp (us)** — 启用 PX4 时间戳值作为输出之一 `off` (默认) | `on`

## 所属库

UAV Toolbox Support Package for PX4 Autopilots / PX4 Sensor Blocks

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2020a 中引入**

## 描述

读取 vehicle\_gps\_position uORB 主题并获取 GPS 坐标

GPS 模块读取 vehicle\_gps\_position uORB 主题，并输出连接到 PX4 Autopilot 的 GPS 接收机的 GPS 坐标。默认情况下，该模块输出 latitude、longitude 和 altitude，并且还提供添加更多基于 GPS 坐标的输出的选项。

在每个仿真步中，模块检查 vehicle\_gps\_position 主题上是否有新消息可用。如果有新消息可用，模块会检索该消息并输出它，同时更新时间戳。如果没有新消息可用，模块输出最后更新的 uORB 消息，并且时间戳不更新。如果自仿真开始以来尚未收到任何消息，则输出为 0。

在 Normal mode 仿真期间，模块输出 0。

在 Connected I/O 仿真期间，此模块从硬件的 peripherals 读取数据。
