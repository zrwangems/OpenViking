---
type: simulink-block
title: 'Current Ang Velocity'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for ArduPilot Autopilots / Algorithm Development'
documentation_page: 'currentangvelocity'
documentation_source_path: 'ardupilot/ref/currentangvelocity.html'
language: zh-CN
chinese_source: worker-translation
---

# Current Ang Velocity

## 端口

### 输出

### **Port\_1** — 当前角速度向量

由载具的陀螺仪测量得到的沿 *-x*、*-y* 和 *-z* 轴的当前角速度。

**数据类型：** `single`

## 参数

### **采样时间** — 模块读取数值的时间间隔 `-1`（默认值）

模块从 ArduPilot Autopilot 读取数值的时间间隔。

## 所属库

UAV Toolbox Support Package for ArduPilot Autopilots / Controller Interface Blocks

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2025b 中引入**

## 描述

读取当前角速度

Current Ang Velocity 模块输出由载具的陀螺仪测量得到的沿 *x-*、*y-* 和 *z-* 轴的角速度（单位为 rad/s）。
