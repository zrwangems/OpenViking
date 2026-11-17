---
type: simulink-block
title: 'Read UAV Trajectory'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'readuavtrajectory'
documentation_source_path: 'ref/readuavtrajectory.html'
language: zh-CN
chinese_source: worker-translation
---

# Read UAV Trajectory

## 端口
```yaml
ports:
- name: Time
  summary: 沿轨迹采样的时间点 标量
  direction: input
  data_types: double
- name: Translation
  summary: UAV 的位置 向量
  direction: output
  data_types: double
- name: Rotation
  summary: UAV 的欧拉角 向量
  direction: output
  data_types: double
```

### 输入

### **Time** — 沿轨迹采样的时间点 标量

沿轨迹采样的时间点，指定为标量。

为使平移和旋转采样与仿真对齐，请使用 Clock (Simulink) 模块作为此端口的输入。

**数据类型：** `double`
### 输出

### **Translation** — UAV 的位置 向量

UAV 的位置，以 `[X Y Z]` 形式的向量返回，其中 `X`、`Y` 和 `Z` 分别是 *x*、*y* 和 *z* 轴上的位置。单位为米。

如果启用 **Convert to ENU reference frame and Front-Left-Up body frame** 参数，此模块输出 ENU 参考坐标系中的位置。否则，该模块返回与轨迹源相同坐标系中的位置。

**示例：** `[1 1 1]`

**数据类型：** `double`

### **Rotation** — UAV 的欧拉角 向量

UAV 的欧拉角，以 `[Rz Ry Rx]` 形式的向量返回，其中 `Rz`、`Ry` 和 `Rx` 分别是绕 *z*、*y* 和 *x* 轴的旋转角度。单位为弧度。

如果启用 **Convert to ENU reference frame and Front-Left-Up body frame** 参数，此模块输出从 ENU 坐标系到 Front-Left-Up 机体坐标系的旋转。否则，此模块返回与轨迹源相同坐标系中的旋转。

**示例：** `[1 0 0]`

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Trajectory source
  summary: 轨迹源 From trajectory object in workspace（默认）| From UAV Scenario in workspace
  group: ''
- name: UAV scenario object
  summary: UAV 场景对象 singleUAVScenario（默认）| uavScenario 对象
  group: ''
- name: UAV platform name
  summary: UAV 平台名称 UAV（默认）| UAV 平台名称
  group: ''
- name: Trajectory object
  summary: 轨迹对象 waypointTrajectory()（默认）| multirotorFlightTrajectory 对象 | fixedwingFlightTrajectory 对象 | polynomialTrajectory
    对象 | waypointTrajectory 对象
  group: ''
- name: Convert to ENU reference frame and Front-Left-Up body frame
  summary: 平移和旋转坐标系 on（默认）| off
  group: ''
```

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### **Trajectory source** — 轨迹源 `From trajectory object in workspace`（默认）| `From UAV Scenario in workspace`

从以下选项中选择 UAV 轨迹的源：

- `From trajectory object in workspace` —

  使用工作区中的轨迹，该轨迹使用 `multirotorFlightTrajectory`、`fixedwingFlightTrajectory`、`polynomialTrajectory` 或 `waypointTrajectory` 对象创建。
- `From UAV Scenario in workspace` —

  使用已添加到 UAV 场景中平台的轨迹。

### **UAV scenario object** — UAV 场景对象 `singleUAVScenario`（默认）| `uavScenario` 对象

包含具有所需轨迹的 UAV 平台的 UAV 场景对象，指定为 `uavScenario` 对象。

#### 依赖关系

要启用此参数，请将 **Trajectory source** 设置为 `From UAV Scenario in workspace`。

### **UAV platform name** — UAV 平台名称 `UAV`（默认）| UAV 平台名称

具有所需轨迹的 UAV 的名称。

#### 依赖关系

要启用此参数，请将 **Trajectory source** 设置为 `From UAV Scenario in workspace`。

### **Trajectory object** — 轨迹对象 `waypointTrajectory()`（默认）| `multirotorFlightTrajectory` 对象 | `fixedwingFlightTrajectory` 对象 | `polynomialTrajectory` 对象 | `waypointTrajectory` 对象

使用工作区中的以下对象之一指定轨迹：`multirotorFlightTrajectory`、`fixedwingFlightTrajectory`、`polynomialTrajectory` 或 `waypointTrajectory`。

#### 依赖关系

要启用此参数，请将 **Trajectory source** 设置为 `From trajectory object in workspace`。

### **Convert to ENU reference frame and Front-Left-Up body frame** — 平移和旋转坐标系 `on`（默认）| `off`

选择此参数以输出 ENU 参考坐标系中的平移以及从 ENU 坐标系到 Front-Left-Up 机体坐标系的旋转。否则，该模块输出与轨迹源相同坐标系中的平移和旋转。如果要将此模块的输出用作 Simulation 3D UAV Vehicle 模块的 **Translation** 和 **Rotation** 输入，请选择此参数。
## 所属库

UAV Toolbox / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024b 中引入**

## 描述

从 UAV 轨迹生成平移和旋转样本，用于 3D 仿真

Read UAV Trajectory 模块从使用 `multirotorFlightTrajectory`、`fixedwingFlightTrajectory`、`polynomialTrajectory` 或 `waypointTrajectory` 对象创建的 UAV 轨迹中生成平移和旋转样本。

将此模块的输出用于 Simulation 3D UAV Vehicle 模块的 **Translation** 和 **Rotation** 输入端口，以在 3D 仿真环境中仿真 UAV 轨迹。
