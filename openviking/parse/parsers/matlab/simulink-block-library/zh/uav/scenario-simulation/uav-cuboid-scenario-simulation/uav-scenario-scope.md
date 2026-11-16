---
type: simulink-block
title: 'UAV Scenario Scope'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / UAV Cuboid Scenario Simulation'
documentation_page: 'uavscenarioscope'
documentation_source_path: 'ref/uavscenarioscope.html'
language: zh-CN
chinese_source: worker-translation
---

# UAV Scenario Scope

## 端口

### 输入

### **In\_1, In\_2, ..., In\_N** — lidar 传感器的点云数据输入 *N*-by-*M*-by-3 double matrix | *N*-by-3 double matrix

输入 UAV 场景中传感器的点云数据。对于在 `Lidar Sensors` 表的 **Visualize** 列中勾选进行可视化的每个 lidar 传感器，都会创建一个输入端口。端口名称设置为传感器名称，其中包含该传感器所属平台的名称。例如，名为 `EgoVehicle` 的平台上的 lidar 传感器的输入端口将具有名称 `EgoVehicle/Lidar`。

如果 lidar 传感器的 `Organized point cloud locations` 参数设置为 `'on'`，则该输入端口期望 *N*-by-*M*-by-3 double matrix，其中 *N* 是垂直扫描的数量，*M* 是水平扫描的数量。如果 lidar 传感器的 `Organized point cloud locations` 设置为 `'off'`，则该输入端口期望 *N*-by-3 double matrix，其中 *N* 是点云中的点数。

## 参数

### **Lidar Sensors** — lidar 传感器列表及其可视化表

`Lidar Sensors` 表列出 UAV 场景中的所有 lidar 传感器。在第一列 **Sensor name** 中，所有传感器名称都与其关联平台一起列出，格式为 *'platform name/sensor name'*。第二列 **Visualize** 为表中的每个 lidar 传感器包含一个复选框。为 lidar 传感器将可视化设置为 `'on'` 会创建一个以该 lidar 传感器名称命名的输入端口。

在 **Filter table contents** 中输入字符串，以按传感器在表 **Sensor Name** 列中的名称筛选传感器列表。

如果 UAV 场景中的 lidar 传感器列表已更改，请点击 **Refresh sensor table** 以更新 `Lidar Sensors` 表。

点击 **Show animation** 以显示或隐藏 UAV 场景的动画图窗。

### **Sample time** — 采样时间 `0.1`（默认值）

指定可视化的采样时间。如果 `Sample time` 设置为 `-1`，则该模块使用 UAV Scenario Configuration 模块中指定的采样时间。

## 所属库

UAV Toolbox / UAV Scenario and Sensor Modeling

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

## 描述

可视化 UAV 场景和 lidar 点云

使用该模块可在动画图窗中可视化 UAV 场景和 lidar 点云。在模块参数中点击 **Show animation** 以可视化 UAV 场景。模型运行时，图窗中的可视化会持续更新。

对于在 `Lidar Sensors` 表的 **Visualize** 列中勾选进行可视化的每个传感器，都会创建一个输入端口。

要使用该模块，请确保模型中包含 UAV Scenario Configuration 模块。
