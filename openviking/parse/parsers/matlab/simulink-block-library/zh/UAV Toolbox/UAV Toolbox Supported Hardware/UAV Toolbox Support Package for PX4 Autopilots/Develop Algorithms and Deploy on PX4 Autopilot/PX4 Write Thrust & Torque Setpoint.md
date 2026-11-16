---
type: simulink-block
title: 'PX4 Write Thrust & Torque Setpoint'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4writethrusttorquesetpoint'
documentation_source_path: 'px4/ref/px4writethrusttorquesetpoint.html'
language: zh-CN
chinese_source: worker-translation
---

# PX4 Write Thrust & Torque Setpoint

## 端口

### 输入

### **Thrust** — 推力设定点向量

指定沿载具机体 *x-*、*y-* 和 *z-* 轴所需的推力设定点。指定的输入在载具机体 FRD 坐标系中归一化到范围 `[-1,1]`。

**数据类型：** `single`

### **Torque** — 扭矩设定点向量

指定绕载具机体 *x-*、*y-* 和 *z-* 轴所需的扭矩设定点。指定的输入在载具机体 FRD 坐标系中归一化到范围 `[-1,1]`。

**数据类型：** `single`

## 参数

在 R2025b 中未提供文档。

## 所属库

UAV Toolbox Support Package for PX4 Autopilots / PX4 Utility Blocks

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

在 R2025b 中未提供文档。

## 版本历史

**在 R2025a 中引入**

## 描述

将推力和扭矩设定点发布到 uORB 主题

此模块通过直接将推力和扭矩设定点发布到 `vehicle_thrust_setpoint` 和 `vehicle_torque_setpoint` uORB 主题，来写入电机和舵机执行器值。此模块接受两个输入，thrust 和 torque，每个均为 1-by-3 向量。推力设定点沿机体 *x-*、*y-* 和 *z-* 轴，扭矩设定点绕机体 *x-*、*y-* 和 *z-* 轴。两个输入均在载具机体 FRD 坐标系中归一化到范围 `[-1,1]`。
