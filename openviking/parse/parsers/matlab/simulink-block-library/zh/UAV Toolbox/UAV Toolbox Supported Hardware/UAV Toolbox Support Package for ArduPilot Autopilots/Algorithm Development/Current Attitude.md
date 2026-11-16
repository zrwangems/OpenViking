---
type: simulink-block
title: 'Current Attitude'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for ArduPilot Autopilots / Algorithm Development'
documentation_page: 'currentattitude'
documentation_source_path: 'ardupilot/ref/currentattitude.html'
language: zh-CN
chinese_source: worker-translation
---

# Current Attitude

## 端口

### 输出

### **Port\_1** — 当前姿态向量

由 ArduPilot 的姿态航向参考系统 (AHRS) 确定的飞行器当前姿态（横滚角、俯仰角和偏航角）。

**数据类型：** `single`

## 参数

### **输出为** — 当前姿态的输出格式 `Euler(ZYX)`（默认） | `Quaternion(ZYX)`

选择当前姿态的输出格式。此参数允许您在将当前姿态表示为欧拉角或四元数之间进行选择。

- `Euler (ZYX)`：选择此选项以使用 ZYX 约定输出欧拉角格式的当前姿态，该约定以横滚角、俯仰角和偏航角表示旋转。
- `Quaternion (WXYZ)`：选择此选项以输出四元数格式的当前姿态，该格式由四部分超复数（W、X、Y、Z）组成。

### **采样时间** — 读取数据的时间间隔 `-1`（默认）

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

读取当前姿态

Current Attitude 模块输出由 ArduPilot 的姿态航向参考系统 (AHRS) 确定的飞行器当前姿态（横滚角、俯仰角和偏航角）。
