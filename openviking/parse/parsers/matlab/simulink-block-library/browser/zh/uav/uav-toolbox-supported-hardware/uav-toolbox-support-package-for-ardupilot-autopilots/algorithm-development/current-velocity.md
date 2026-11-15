---
type: simulink-block
title: 'Current Velocity'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for ArduPilot Autopilots / Algorithm Development'
documentation_page: 'currentvelocity'
documentation_source_path: 'ardupilot/ref/currentvelocity.html'
language: zh-CN
chinese_source: worker-translation
---

# Current Velocity

## 端口

### 输出

### **Port\_1** — 当前速度向量

车辆在 NED（North-East-Down）坐标系中的当前速度，单位为 microseconds。

**数据类型：** `single`

## 参数

### **采样时间** — 模块读取值的时间间隔 `-1` (默认)

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

读取当前速度

Current Velocity 模块输出车辆在 NED（North-East-Down）坐标系中的当前速度（单位为 m/s），该坐标系是导航中使用的地理坐标系。

- 北（N）：正方向指向北（地理北方）。
- 东（E）：正方向指向东（在水平面内，垂直于北）。
- 下（D）：正方向指向下，朝向地球中心（垂直分量）。
