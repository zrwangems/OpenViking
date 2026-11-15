---
type: simulink-block
title: 'Position Setpoint'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for ArduPilot Autopilots / Algorithm Development'
documentation_page: 'positionsetpoint'
documentation_source_path: 'ardupilot/ref/positionsetpoint.html'
language: zh-CN
chinese_source: worker-translation
---

# Position Setpoint

## 端口

### 输出

### **Port\_1** — 位置设定值向量

车辆相对于 NED（North-East-Down）坐标系原点的期望位置（以 meters 为单位）

**数据类型：** `single`

## 参数

### **采样时间** — 模块读取值的时间间隔 `-1`（默认）

模块从 ArduPilot Autopilot 读取值的时间间隔。

## 所属库

UAV Toolbox Support Package for ArduPilot Autopilots / Controller Interface Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2025b 中引入**

## 描述

读取位置设定值

Position Setpoint 模块输出车辆相对于 NED（North-East-Down）坐标系原点的期望位置（以 meters 为单位），NED 是导航中使用的一种坐标系。它用于描述相对于参考点的位置，该参考点通常是车辆的起始位置。

- 北 (N)：正方向指向北（地理北）。
- 东 (E)：正方向指向东（在水平面内，垂直于北）。
- 下 (D)：正方向向下，指向地心（垂直分量）。
