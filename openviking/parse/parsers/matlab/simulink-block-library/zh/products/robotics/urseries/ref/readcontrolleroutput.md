---
type: simulink-block
title: 'Read Controller Output'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robotics System Toolbox Supported Hardware / UR Series Manipulators / Get Started with Real-Time Data Exchange (RTDE) Connectivity Interface'
documentation_page: 'readcontrolleroutput'
documentation_source_path: 'urseries/ref/readcontrolleroutput.html'
language: zh-CN
chinese_source: worker-translation
---

# Read Controller Output

## 端口

### 输出

### **q** — 当前关节构型数值向量

协作机器人的当前关节构型（以 radians 为单位），范围为 [-2π, 2π]，指定为 1×6 向量。

**数据类型：** `double`

### **qd** — 当前关节速度数值向量

协作机器人的当前关节速度（以 radians per second 为单位），指定为 1×6 向量。

#### 依赖项

要启用此端口，请选择 **Enable joint velocity output** 参数。

**数据类型：** `double`

### **qdd** — 当前关节加速度数值向量

协作机器人的当前关节加速度（以 radians per second squared 为单位），指定为 1×6 向量。

#### 依赖项

要启用此端口，请选择 **Enable joint acceleration output** 参数。

**数据类型：** `double`

## 参数

### **UR Controller IP address** — UR Controller 的 IP 地址 `192.168.1.10`（默认）| 标量

指定与您正在建立连接的 UR 系列协作机器人相对应的 UR Controller 的 IP 地址。

### **Enable joint velocity output** — 通过输出端口获取关节速度 `off`（默认）| on

启用输出端口 **qd** 以获取关节速度。

### **Enable joint acceleration output** — 通过输出端口获取关节加速度 `off`（默认）| on

启用输出端口 **qdd** 以获取关节加速度。

### **Sample time** — 采样时间 `0.1`（默认）| 任何为 0.1 倍数的非负值 | `-1`

输入模块从 UR RTDE Controller 读取值的时间间隔。

当您将此参数设置为 -1 时，Simulink 会根据模型中的模块上下文确定模块的最佳采样时间。

## 所属库

Robotics System Toolbox Support Package for Universal Robots UR Series Manipulators / UR RTDE Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2025a 中引入**

## 描述

使用 RTDE 接口从 UR Controller 读取指定信号

Read Controller Output 模块使用 RTDE 接口读取由 UR 系列协作机器人的 UR Controller 生成的指定输出信号。对于协作机器人的梯形或非梯形运动，均可读取这些值。
