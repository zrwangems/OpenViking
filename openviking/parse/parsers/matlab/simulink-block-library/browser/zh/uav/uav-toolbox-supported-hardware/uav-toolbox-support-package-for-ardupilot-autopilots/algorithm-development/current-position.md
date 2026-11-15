---
type: simulink-block
title: 'Current Position'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for ArduPilot Autopilots / Algorithm Development'
documentation_page: 'currentposition'
documentation_source_path: 'ardupilot/ref/currentposition.html'
language: zh-CN
chinese_source: worker-translation
---

# Current Position

## 端口

### 输出

### **Port\_1** — 当前位置向量

车辆相对于 NED (North-East-Down) 坐标系原点的当前位置（以 meters 为单位）。

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

读取当前位置

Current Position 模块输出车辆相对于 NED (North-East-Down) 坐标系原点的当前位置（以 meters 为单位），NED (North-East-Down) 是一种常用于导航的地理坐标系。

- North (N)：正方向指向北（地理北）。
- East (E)：正方向指向东（垂直于北，在水平面内）。
- Down (D)：正方向指向下，朝向地球中心（垂直分量）。
