---
type: simulink-block
title: 'Actuate Gripper'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robotics System Toolbox Supported Hardware / UR Series Manipulators / Get Started with Real-Time Data Exchange (RTDE) Connectivity Interface'
documentation_page: 'actuategripper'
documentation_source_path: 'urseries/ref/actuategripper.html'
language: zh-CN
chinese_source: worker-translation
---

# Actuate Gripper

## 端口

### 输入

### **Actuation** — 关闭或打开夹爪 `1` | `0`

Actuation 端口用于传递逻辑值以驱动夹爪。
`1` 关闭夹爪，`0` 打开夹爪。

**数据类型：** `Boolean`

### **Enable** — 启用或禁用夹爪驱动 `1` | `0`

Enable 端口用于传递逻辑值，以启用或禁用模块执行夹爪驱动。`1` 启用模块以在 **Actuation** 输入端口接受值，而 `0` 禁用模块。

**数据类型：** `Boolean`

## 参数

### **UR Controller IP address** — UR Controller 的 IP 地址 `192.168.1.10` (默认) | scalar

指定与你要建立连接的 UR 系列协作机器人对应的 UR Controller 的 IP 地址。

## 所属库

Robotics System Toolbox Support Package for Universal Robots UR Series Manipulators / UR RTDE Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2025a 中引入**

## 描述

驱动连接到协作机器人的夹爪

Actuate Gripper 模块驱动连接到 UR 系列协作机器人的夹爪。你可以使用此模块驱动 Robotiq Vacuum Gripper 或 Robotiq 2-Finger Adaptive Robot Gripper。

**注意**

使用此模块进行的仿真和部署仅适用于连接到实际的 UR 系列协作机器人，而不适用于使用 URSim 的仿真协作机器人。

默认情况下，即使你成功连接到协作机器人，夹爪连接也是禁用的。要使夹爪连接能够接收驱动命令，你需要修改支持包中提供的 `URServerScript.script`（更多详细信息，请参阅在硬件上加载并播放 UR 程序）。
