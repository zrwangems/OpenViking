---
type: simulink-block
title: 'UAV Scenario Motion Write'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Scenario and Sensor Modeling'
documentation_page: 'uavscenariomotionwrite'
documentation_source_path: 'ref/uavscenariomotionwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# UAV Scenario Motion Write

## 端口

### 输入

### **Position** — 位置 1-by-3 向量

将平台在输入坐标系中的输入位置指定为 1-by-3 向量。

### **Orientation** — 姿态四元数 1-by-4 向量

将平台在输入坐标系中的输入姿态指定为 1-by-4 向量四元数。

### **Velocity** — 速度 1-by-3 向量

将平台在输入坐标系中的输入速度指定为 1-by-3 向量。

### **Acceleration** — 加速度 1-by-3 向量

将平台在输入坐标系中的输入加速度指定为 1-by-3 向量。

### **AngularVelocity** — 角速度 1-by-3 向量

将平台在输入坐标系中的输入角速度指定为 1-by-3 向量。

## 参数

### **Platform name** — 平台名称 `'UAV'`（默认）| string

使用 **Select** 从 UAV Scenario 中选择平台名称字符串。

### **Coordinate frame of input motion** — 输入运动的坐标系 `'NED'`（默认）| `ENU`

将输入运动的坐标系指定为 `'NED'`（North-East-Down，北-东-下）或 `'ENU'`（East-North-Up，东-北-上）。

## 所属库

UAV Toolbox / UAV Scenario and Sensor Modeling

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

## 描述

更新 UAV 场景仿真中的平台运动

使用此模块可在每个时间步使用输入信号更新 UAV 场景仿真中平台的运动状态。该模块将 position、orientation、velocity、acceleration 和 angular velocity 作为输入，以更新指定平台的运动状态 bus。但是，由于 UAV Scenario 中未仿真运动学模型，此模块不会基于 velocity 和 acceleration 输入移动平台。

要使用此模块，请确保模型中有 UAV Scenario Configuration 模块。

此模块使用 UAV Scenario Configuration 模块中指定的采样时间。
