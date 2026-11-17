---
type: simulink-block
title: 'UAV Scenario Lidar'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Scenario and Sensor Modeling'
documentation_page: 'uavscenariolidar'
documentation_source_path: 'ref/uavscenariolidar.html'
language: zh-CN
chinese_source: worker-translation
---

# UAV Scenario Lidar

## 端口
```yaml
ports:
- name: Pointcloud
  summary: 点云数据 *N*-by-*M*-by-3 double 矩阵 | *N*-by-3 double 矩阵
  direction: output
```

### 输出

### **Pointcloud** — 点云数据 *N*-by-*M*-by-3 double 矩阵 | *N*-by-3 double 矩阵

在 Sensor Frame 中报告的点云数据。当勾选 `Output organized point cloud locations` 时，点云数据指定为 *N*-by-*M*-by-3 double 矩阵，其中 *N* 是垂直扫描数，*M* 是水平扫描数。当取消勾选 `Output organized point cloud locations` 时，点云数据指定为 *N*-by-3 double 矩阵，其中 *N* 是点云中的点数。
## 参数
```yaml
parameters:
- name: Sensor name
  summary: 激光雷达传感器名称 'UAV/Lidar'（默认）| string
  group: ''
- name: Max range
  summary: 激光雷达最大距离 120（默认）| double
  group: ''
- name: Range Accuracy
  summary: 激光雷达距离精度 0.002（默认）| double
  group: ''
- name: Azimuthal limits
  summary: 激光雷达方位角限制 [-180, 180]（默认）| 二元素向量
  group: ''
- name: Azimuthal resolution
  summary: 方位角分辨率 0.16（默认）| double
  group: ''
- name: Elevation limits
  summary: 激光雷达仰角限制 [-20, 20]（默认）| 二元素向量
  group: ''
- name: Elevation resolution
  summary: 仰角分辨率 1.25（默认）| double
  group: ''
- name: Add noise to measurement
  summary: 向测量添加噪声 'on'（默认）| 'off'
  group: ''
- name: Output organized point cloud locations
  summary: 输出组织化点云位置 'on'（默认）| 'off'
  group: ''
- name: Sample Time
  summary: 采样时间 0.1（默认）| double
  group: ''
```

### **Sensor name** — 激光雷达传感器名称 `'UAV/Lidar'`（默认）| string

将激光雷达传感器名称指定为字符串标量。

要从 MATLAB® 工作区中的 UAV Scenario 选择现有激光雷达传感器，请点击 **Select**。UAV Scenario Lidar 模块将使用指定激光雷达传感器属性的当前值来设置参数。

要将激光雷达传感器添加到 UAV Scenario，请创建 `uavSensor` 对象，并将 `uavLidarPointCloudGenerator` 作为指定的传感器模型，然后将 `uavSensor` 附加到 UAV Scenario 中的 `uavPlatform`。必须使用 UAV Scenario Configuration 模块将此场景导入 Simulink®。可用的传感器将列为 *'platform name/sensor name'*。

### **Max range** — 激光雷达最大距离 `120`（默认）| double

将激光雷达最大距离指定为以米为单位的 double 标量。

如果使用 **Select** 指定 **Sensor name** 参数，则 UAV Scenario Lidar 模块会将 **Max range** 参数的值设置为指定激光雷达传感器的 `MaxRange` 属性。

### **Range Accuracy** — 激光雷达距离精度 `0.002`（默认）| double

将激光雷达距离精度指定为以米为单位的 double 标量。

如果使用 **Select** 指定 **Sensor name** 参数，则 UAV Scenario Lidar 模块会将 **RangeAccuracy** 参数的值设置为指定激光雷达传感器的 `RangeAccuracy` 属性。

### **Azimuthal limits** — 激光雷达方位角限制 `[-180, 180]`（默认）| 二元素向量

将激光雷达方位角限制指定为以度为单位的二元素向量。

如果使用 **Select** 指定 **Sensor name** 参数，则 UAV Scenario Lidar 模块会将 **Azimuthal limits** 参数的值设置为指定激光雷达传感器的 `AzimuthLimits` 属性。

### **Azimuthal resolution** — 方位角分辨率 `0.16`（默认）| double

将激光雷达方位角分辨率指定为以度为单位的 double 标量。

如果使用 **Select** 指定 **Sensor name** 参数，则 UAV Scenario Lidar 模块会将 **Azimuthal resolution** 参数的值设置为指定激光雷达传感器的 `AzimuthResolution` 属性。

### **Elevation limits** — 激光雷达仰角限制 `[-20, 20]`（默认）| 二元素向量

将激光雷达仰角限制指定为以度为单位的二元素向量。

如果使用 **Select** 指定 **Sensor name** 参数，则 UAV Scenario Lidar 模块会将 **Elevation limits** 参数的值设置为指定激光雷达传感器的 `ElevationLimits` 属性。

### **Elevation resolution** — 仰角分辨率 `1.25`（默认）| double

将激光雷达仰角分辨率指定为以度为单位的 double 标量。

如果使用 **Select** 指定 **Sensor name** 参数，则 UAV Scenario Lidar 模块会将 **Elevation resolution resolution** 参数的值设置为指定激光雷达传感器的 `ElevationResolution` 属性。

### **Add noise to measurement** — 向测量添加噪声 `'on'`（默认）| `'off'`

勾选此框可向激光雷达测量添加噪声。此模块的噪声生成目前不允许用户指定种子。

如果使用 **Select** 指定 **Sensor name** 参数，则 UAV Scenario Lidar 模块会将 **Add noise to measurement** 参数的值设置为指定激光雷达传感器的 `HasNoise` 属性。

### **Output organized point cloud locations** — 输出组织化点云位置 `'on'`（默认）| `'off'`

选中此复选框可输出组织化点云位置，指定为 *N*×*M*×3，其中 *N* 是垂直扫描数，*M* 是水平扫描数。如果设置为 `'off'`，模块的输出为 *N*×3 双精度矩阵，其中 *N* 是点云中的点数。

如果使用 **Select** 指定 **Sensor name** 参数，UAV Scenario Lidar 模块将 **Output organized point cloud locations** 参数的值设置为指定激光雷达传感器的 `HasOrganizedOutput` 属性的值。

### **Sample Time** — 采样时间 `0.1`（默认）| double

以秒为单位将激光雷达的采样时间指定为双精度标量。采样时间必须是 UAV Scenario Configuration 模块中指定的采样时间的倍数。

如果使用 **Select** 指定 **Sensor name** 参数，UAV Scenario Lidar 模块将 **Sample Time** 参数的值设置为 `1/UpdateRate`。`UpdateRate` 是指定激光雷达传感器的 `UpdateRate` 属性。
## 所属库

UAV Toolbox / UAV Scenario and Sensor Modeling

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

## 描述

基于场景中的网格模拟激光雷达测量

使用此模块通过基于 UAV Scenario 中的网格输出点云数据来模拟激光雷达测量。要将网格添加到 UAV Scenario 中，请使用 `addMesh` 函数将其添加到 UAV Scenario Configuration 模块所包含的 `uavScenario` 对象中。有关添加网格的更多信息，请参阅 UAV Scenario Tutorial。

要使用此模块，请确保模型中包含 UAV Scenario Configuration 模块。
