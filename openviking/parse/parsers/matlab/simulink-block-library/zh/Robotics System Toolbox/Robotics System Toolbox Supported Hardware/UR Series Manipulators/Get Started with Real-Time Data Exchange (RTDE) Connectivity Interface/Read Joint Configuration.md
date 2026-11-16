---
type: simulink-block
title: 'Read Joint Configuration'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robotics System Toolbox Supported Hardware / UR Series Manipulators / Get Started with Real-Time Data Exchange (RTDE) Connectivity Interface'
documentation_page: 'readjointconfiguration'
documentation_source_path: 'urseries/ref/readjointconfiguration.html'
language: zh-CN
chinese_source: worker-translation
---

# Read Joint Configuration

## 端口

### 输出

### **q** — 当前关节构型 数值向量

协作机器人的当前关节构型（以弧度为单位），范围为 [-2π, 2π]，指定为 1×6 向量。

**数据类型：** `double`

### **Status** — 读取操作的状态 数值标量

读取操作的状态，指定为数值标量。该模块将结果输出为以下值之一：

- **0** – 读取操作成功
- **1** – 读取操作失败

**数据类型：** `double`

## 参数

### **UR Controller IP address** — UR Controller 的 IP 地址 `192.168.1.10`（默认）| 标量

指定与您要建立连接的 UR Series 协作机器人对应的 UR Controller 的 IP 地址。

### **Sample time** — 采样时间 `0.1`（默认）| 任何为 0.1 倍数的非负值 | `-1`

输入该模块从 UR RTDE Controller 读取值的时间间隔。

当您将此参数设置为 -1 时，Simulink 会根据模型中的模块上下文为该模块确定最佳采样时间。

## 所属库

Robotics System Toolbox Support Package for Universal Robots UR Series Manipulators / UR RTDE Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2025a 中引入**

## 描述

使用 RTDE 接口从 UR Controller 读取当前关节构型

Read Joint Configuration 模块使用 RTDE 接口从 UR Controller 读取协作机器人的当前关节构型。
