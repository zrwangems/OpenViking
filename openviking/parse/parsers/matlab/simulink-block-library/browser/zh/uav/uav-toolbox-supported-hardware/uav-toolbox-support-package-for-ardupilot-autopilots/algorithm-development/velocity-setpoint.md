---
type: simulink-block
title: 'Velocity Setpoint'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for ArduPilot Autopilots / Algorithm Development'
documentation_page: 'velocitysetpoint'
documentation_source_path: 'ardupilot/ref/velocitysetpoint.html'
language: zh-CN
chinese_source: worker-translation
---

# Velocity Setpoint

## 端口

### 输出

### **Port\_1** — 速度设定值向量

来自 ArduPilot 制导系统的 NED 坐标系下的飞行器速度设定值 (m/s)。

**数据类型：** `single`

## 参数

### **采样时间** — 模块读取值的时间间隔 `-1`（默认）

模块从 ArduPilot Autopilot 读取值的时间间隔。

## 所属库

UAV Toolbox Support Package for ArduPilot Autopilots / Controller Interface Blocks

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2025b 中引入**

## 描述

读取速度设定值

Velocity Setpoint 模块读取由 ArduPilot 制导系统基于当前飞行模式设置的、北-东-下 (NED) 坐标系下的飞行器速度设定值 (m/s)。

- 北 (N)：正方向指向北（地理北）。
- 东 (E)：正方向指向东（在水平面内垂直于北）。
- 下 (D)：正方向向下，指向地心（垂直分量）。
