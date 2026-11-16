---
type: simulink-block
title: 'Ang Velocity Setpoint'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for ArduPilot Autopilots / Algorithm Development'
documentation_page: 'angvelocitysetpoint'
documentation_source_path: 'ardupilot/ref/angvelocitysetpoint.html'
language: zh-CN
chinese_source: worker-translation
---

# Ang Velocity Setpoint

## 端口

### 输出

### **Port\_1** — 角速度设定点向量

来自 ArduPilot 位置控制器的沿 *x-*、*y-* 和 *z-* 轴的角速度设定点 (rad/s)。

**数据类型：** `single`

## 参数

### **采样时间** — 模块读取值的时间间隔 `-1`（默认）

模块从 ArduPilot 自动驾驶仪读取值的时间间隔。

## 所属库

UAV Toolbox Support Package for ArduPilot Autopilots / Controller Interface Blocks

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2025b 中引入**

## 描述

读取角速度设定点

Ang Velocity Setpoint 模块输出由 ArduPilot 位置控制器设置的沿 *x-*、*y-* 和 *z-* 轴的角速度设定点的值 (rad/s)。
