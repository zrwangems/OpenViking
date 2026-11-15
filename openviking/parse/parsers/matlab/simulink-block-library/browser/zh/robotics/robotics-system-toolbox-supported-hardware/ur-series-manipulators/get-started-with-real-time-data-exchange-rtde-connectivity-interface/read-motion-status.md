---
type: simulink-block
title: 'Read Motion Status'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robotics System Toolbox Supported Hardware / UR Series Manipulators / Get Started with Real-Time Data Exchange (RTDE) Connectivity Interface'
documentation_page: 'readmotionstatus'
documentation_source_path: 'urseries/ref/readmotionstatus.html'
language: zh-CN
chinese_source: worker-translation
---

# Read Motion Status

## 端口

### 输出

### **Port\_1** — 协作机器人运动状态（标量）

协作机器人的运动状态，指定为标量。该模块将结果输出为以下值之一：

- **2** – 协作机器人已完成运动
- **1** – 运动执行正在进行中
- **0** – 运动尚未开始

**数据类型：** `double`

## 参数

### **UR Controller IP address** — UR Controller 的 IP 地址 `192.168.1.10`（默认）| 标量

指定与您正在建立连接的 UR Series 协作机器人对应的 UR Controller 的 IP 地址。

### **Sample time** — 采样时间 `0.1`（默认）| 任何 0.1 的非负倍数 | `-1`

输入该模块从 UR RTDE Controller 读取值的时间间隔。

当您将此参数设置为 -1 时，Simulink 将根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Robotics System Toolbox Support Package for Universal Robots UR Series Manipulators / UR RTDE Blocks

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2025a 中引入**

## 描述

使用 RTDE 接口从 UR Controller 读取协作机器人的运动状态

Read Motion Status 模块读取协作机器人的运动状态，该状态通过 RTDE 接口从 UR Controller 读取。
