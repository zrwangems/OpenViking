---
type: simulink-block
title: 'UAV Scenario Motion Read'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / UAV Cuboid Scenario Simulation'
documentation_page: 'uavscenariomotionread'
documentation_source_path: 'ref/uavscenariomotionread.html'
language: zh-CN
chinese_source: worker-translation
---

# UAV Scenario Motion Read

## 端口

### 输出

### **Motion** — UAV 运动数据总线

输出来自平台或传感器的运动，该运动指定为具有以下属性的总线，名称在 Platform or sensor name 中指定：

- *PlatformID* – 平台 ID，基于平台在 `uavScenario.Platforms` 属性中的顺序。
- *Position* – NED 坐标系中的位置，指定为 1-by-3 向量。
- *Orientation* – NED 坐标系中的姿态，指定为 1-by-4 向量、四元数，即从 NED 坐标系到 UAV 机体坐标系的坐标系旋转。
- *Velocity* – NED 坐标系中的速度，指定为 1-by-3 向量。
- *Acceleration* – NED 坐标系中的加速度，指定为 1-by-3 向量。
- *AngularVelocity* – NED 坐标系中的角速度，指定为 1-by-3 向量。

如果在 `Platform or sensor name` 中指定了传感器名称，则会将 *SensorID* 字段添加到运动输出总线的总线字段中。

- *SensorID* – 传感器 ID，指定为标量，基于传感器在 `uavScenario.Platforms` 属性中的顺序。

平台和传感器运动总线的类型由模型中 UAV Scenario Configuration 模块的 `Sensor motion bus name` 和 `Sensor motion bus name` 属性命名。

### **SampledWind** — 合成风平移速度和角速度 1-by-6 向量

来自所有风模型对象的合成风平移速度和角速度，位于 UAV 平台机体坐标系中，返回为形式如 [uw vw ww pw qw rw] 的 1-by-6 向量。uw、vw 和 ww 表示 UAV 平台机体坐标系正 x、y 和 z 方向上的合成风平移速度，单位为 m/s。pw、qw 和 rw 表示 UAV 平台机体坐标系正 x、y 和 z 方向上的合成风角速度，单位为 rad/s。

#### 依赖项

仅当选中 **Generate wind velocity and angular velocity samples** 时，此端口才可见。

### **SampledWindByComponent** — 来自每个风模型对象的风平移速度和角速度 *N*-by-6 矩阵

来自每个风模型对象的风平移速度和角速度，位于 UAV 平台机体坐标系中，返回为 *N*-by-6 矩阵，其中 *N* 是添加到 UAV 平台的风模型对象数量。每行形式为 [uw vw ww pw qw rw]。uw、vw 和 ww 表示正 x、y 和 z 方向上的风平移速度，单位为 m/s。pw、qw 和 rw 表示正 x、y 和 z 方向上的风角速度，单位为 rad/s。

#### 依赖项

仅当选中 **Generate wind velocity and angular velocity samples** 时，此端口才可见。

## 参数

### **Platform or sensor name** — 平台或传感器名称 `'UAV'`（默认）| string

使用 **Select** 从 UAV Scenario 中选择一个平台或传感器以读取其运动。

此参数影响运动总线输出的字段。有关详细信息，请参阅 `Motion` 输出。

### **Coordinate frame of output motion** — 输出运动的坐标系 `'ENU'`（默认）| `'NED'` | string

将输出运动的坐标系指定为 East-North-Up (`'ENU'`) 或 North-East-Down (`'NED'`)。

### **Generate wind velocity and angular velocity samples** — 生成风速和角速度样本 `off`（默认）| `on`

从 **SampledWind** 和 **SampledWindByComponent** 端口输出风速。

#### 依赖项

仅当您已选择平台且 Aerospace Blockset™ 许可证可用时，此参数才启用。将此参数打开进行仿真会签出 Aerospace Blockset 许可证

## 所属库

UAV Toolbox / UAV Scenario and Sensor Modeling

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2021b 中引入**

### R2024a: **Generate wind velocity and angular velocity samples**

UAV Scenario Motion Read 模块现在具有 generate wind velocity and angular velocity samples 参数，您可以启用该参数以输出风平移速度和角速度

## 描述

从 UAV scenario 仿真中读取平台和传感器运动

使用此模块从 UAV scenario 仿真中的传感器或平台读取总线形式的运动。运动总线包含平台或传感器的位置、姿态、速度、角速度、加速度和 ID。

要使用此模块，请确保模型中存在 UAV Scenario Configuration 模块。

此模块使用 UAV Scenario Configuration 模块中指定的采样时间。
