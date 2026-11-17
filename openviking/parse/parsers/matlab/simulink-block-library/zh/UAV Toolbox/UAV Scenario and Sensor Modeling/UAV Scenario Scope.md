---
type: simulink-block
title: 'UAV Scenario Scope'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Scenario and Sensor Modeling'
documentation_page: 'uavscenarioscope'
documentation_source_path: 'ref/uavscenarioscope.html'
language: zh-CN
chinese_source: worker-translation
---

# UAV Scenario Scope

## 端口
```yaml
ports:
- name: In_1, In_2, ..., In_N
  summary: 激光雷达传感器的点云数据输入 *N*×*M*×3 双精度矩阵 | *N*×3 双精度矩阵
  direction: input
```

### 输入

### **In\_1, In\_2, ..., In\_N** — 激光雷达传感器的点云数据输入 *N*×*M*×3 双精度矩阵 | *N*×3 双精度矩阵

UAV Scenario 中传感器的输入点云数据。对于在 `Lidar Sensors` 表的 **Visualize** 列中勾选可视化的每个激光雷达传感器，都会创建一个输入端口。端口名称设置为传感器名称，其中包含传感器所属平台的名称。例如，名为 `EgoVehicle` 的平台上的激光雷达传感器的输入端口名称为 `EgoVehicle/Lidar`。

如果激光雷达传感器的 `Organized point cloud locations` 参数设置为 `'on'`，则输入端口期望一个 *N*×*M*×3 双精度矩阵，其中 *N* 是垂直扫描数，*M* 是水平扫描数。如果激光雷达传感器的 `Organized point cloud locations` 设置为 `'off'`，则输入端口期望一个 *N*×3 双精度矩阵，其中 *N* 是点云中的点数。
## 参数
```yaml
parameters:
- name: Lidar Sensors
  summary: 激光雷达传感器列表及其可视化表
  group: ''
- name: Sample time
  summary: 采样时间 0.1（默认）
  group: ''
```

### **Lidar Sensors** — 激光雷达传感器列表及其可视化表

`Lidar Sensors` 表列出了 UAV 场景中的所有激光雷达传感器。在第一列 **Sensor name** 中，所有传感器名称与其关联平台一起列出，格式为 *'平台名称/传感器名称'*。第二列 **Visualize** 包含表中每个激光雷达传感器的复选框。将激光雷达传感器的可视化设置为 `'on'` 会创建一个以该激光雷达传感器名称命名的输入端口。

在 **Filter table contents** 中输入字符串，可按表中 **Sensor Name** 列的传感器名称筛选传感器列表。

如果 UAV Scenario 中的激光雷达传感器列表已更改，请点击 **Refresh sensor table** 以更新 `Lidar Sensors` 表。

点击 **Show animation** 可显示或隐藏 UAV 场景的动画图窗。

### **Sample time** — 采样时间 `0.1`（默认）

指定可视化的采样时间。如果 `Sample time` 设置为 `-1`，则此模块使用 UAV Scenario Configuration 模块中指定的采样时间。
## 所属库

UAV Toolbox / UAV Scenario and Sensor Modeling

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

## 描述

可视化 UAV 场景和激光雷达点云

使用此模块可在动画图窗中可视化 UAV 场景和激光雷达点云。在模块参数中点击 **Show animation** 以可视化 UAV 场景。图窗中的可视化在模型运行时持续更新。

对于在 `Lidar Sensors` 表的 **Visualize** 列中勾选可视化的每个传感器，都会创建一个输入端口。

要使用此模块，请确保模型中有 UAV Scenario Configuration 模块。
