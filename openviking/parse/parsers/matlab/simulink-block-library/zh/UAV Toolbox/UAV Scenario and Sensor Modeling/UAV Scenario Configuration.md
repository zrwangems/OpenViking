---
type: simulink-block
title: 'UAV Scenario Configuration'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Scenario and Sensor Modeling'
documentation_page: 'uavscenarioconfiguration'
documentation_source_path: 'ref/uavscenarioconfiguration.html'
language: zh-CN
chinese_source: worker-translation
---

# UAV Scenario Configuration

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: MATLAB or model workspace variable name
  summary: MATLAB 或模型工作区变量名称 'singleUAVScenario'（默认）| 字符串
  group: 主
- name: Sample time
  summary: 采样时间 0.1（默认）| 正双精度值
  group: 主
- name: Sensor motion bus name
  summary: 传感器运动总线名称 'SensorMotionBus'（默认）| 字符串
  group: 场景总线和信号名称
- name: Platform motion bus name
  summary: 平台运动总线名称 'PlatformMotionBus'（默认）| 字符串
  group: 场景总线和信号名称
- name: Scenario motion bus name
  summary: 场景运动总线名称 'SensorMotionBus'（默认）| 字符串
  group: 场景总线和信号名称
- name: Scenario motion signal name
  summary: 场景运动信号名称 'ScenarioMotions'（默认）| 字符串
  group: 场景总线和信号名称
```

### 主

### **MATLAB or model workspace variable name** — MATLAB 或模型工作区变量名称 `'singleUAVScenario'`（默认）| 字符串

指定要从 MATLAB 或模型工作区导入的 `uavScenario`
对象，以字符串形式的变量名称指定。点击
**Refresh** 以从
`uavScenario` 对象重新加载场景。

### **Sample time** — 采样时间 `0.1`（默认）| 正双精度值

以秒为单位指定 UAV 场景的采样时间。此模块仅支持
离散采样时间。

### 场景总线和信号名称

### **Sensor motion bus name** — 传感器运动总线名称 `'SensorMotionBus'`（默认）| 字符串

以字符串形式指定传感器运动总线类型的名称。由
UAV Scenario Motion
Read 读取的传感器运动使用具有指定名称的总线对象。

### **Platform motion bus name** — 平台运动总线名称 `'PlatformMotionBus'`（默认）| 字符串

以字符串形式指定平台运动总线类型的名称。分别由 UAV Scenario Motion
Read 和 UAV Scenario Motion
Write 读取和写入的平台运动将使用具有指定名称的总线对象。

### **Scenario motion bus name** — 场景运动总线名称 `'SensorMotionBus'`（默认）| 字符串

以字符串形式指定场景运动总线类型的名称。此总线类型
由 UAV Scenario Configuration 模块用于存储 UAV 场景中所有平台和传感器的运动数据。

### **Scenario motion signal name** — 场景运动信号名称 `'ScenarioMotions'`（默认）| 字符串

以字符串形式指定场景运动总线信号的名称。这是
用于存储 UAV 场景数据的 Data Store Read 模块所使用的名称。
## 所属库

UAV Toolbox / UAV Scenario and Sensor Modeling

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

## 描述

配置并仿真 UAV 场景

此模块允许您导入 `uavScenario` 对象并
仿真该场景。此模块必须位于包含 UAV Scenario Lidar 和
Motion 模块的模型中，以便使用来自
`uavScenario`
环境的数据测试感知、控制和规划算法。包含 UAV Scenario 的模型一次只能使用一个 UAV Scenario
Configuration 模块，且不适用于跨模型
工作流。在 UAV 场景中，此模块必须先于其他 UAV Scenario 模块执行。
使用 **Refresh** 按钮更新 UAV Scenario Configuration 模块，然后点击 **Apply** 以反映在
MATLAB® 中对导入的 `uavScenario` 所做的任何更改。

此模块在内部将来自平台和传感器的运动状态存储在全局数据
存储内存模块中，作为总线中的总线，其名称由 **Scenario
motion bus name** 参数指定。该总线包含以下字段：

- *NumPlatforms* — 场景中 UAV 平台的数量，存储为
  标量。
- *Time* — 与运动状态关联的仿真时间，存储为
  标量。
- *Platforms* — 名称由
  **Platform motion bus name** 参数指定的总线数组，包含 UAV 场景中的所有平台，每个平台具有以下字段：

  - *PlatformID* — 基于 `uavScenario.Platforms` 属性中平台顺序的平台 ID。
  - *Position* — NED 坐标系中的位置，指定为 1×3
    向量。
  - *Orientation* — NED 坐标系中的姿态，指定为
    1×4 向量，四元数，从 NED 坐标系到 UAV 机体坐标系的坐标系旋转。
  - *Velocity* — NED 坐标系中的速度，指定为 1×3
    向量。
  - *Acceleration* — NED 坐标系中的加速度，指定为
    1×3 向量。
  - *AngularVelocity* — NED 坐标系中的角速度，指定
    为 1×3 向量。
