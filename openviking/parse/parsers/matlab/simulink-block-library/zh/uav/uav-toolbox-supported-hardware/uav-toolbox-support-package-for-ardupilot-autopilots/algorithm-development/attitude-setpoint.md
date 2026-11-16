---
type: simulink-block
title: 'Attitude Setpoint'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for ArduPilot Autopilots / Algorithm Development'
documentation_page: 'attitudesetpoint'
documentation_source_path: 'ardupilot/ref/attitudesetpoint.html'
language: zh-CN
chinese_source: worker-translation
---

# Attitude Setpoint

## 端口

### 输出

### **Port\_1** — 姿态设定点向量

来自 ArduPilot 的位置控制器的载具姿态设定点。

**数据类型：** `single`

## 参数

### **Output as** — 姿态设定点的输出格式 `Euler(ZYX)`（默认）| `Quaternion(ZYX)`

选择姿态设定点的输出格式。此参数允许您选择将姿态表示为欧拉角还是四元数。

- `Euler (ZYX)`：选择此选项以输出
  使用 ZYX 约定的欧拉角格式姿态设定点，
  该约定以横滚、俯仰和偏航角表示旋转。
- `Quaternion (WXYZ)`：选择此选项以
  输出四元数格式的姿态，该格式由
  四部分超复数（W、X、Y、Z）组成。

### **Sample time** — 模块读取值的时间间隔 `-1`（默认）

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

读取姿态设定点

此模块输出由 ArduPilot 的位置控制器确定的载具姿态设定点。
