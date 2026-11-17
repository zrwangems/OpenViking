---
type: simulink-block
title: 'Current Time'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS'
documentation_page: 'currenttime'
documentation_source_path: 'ref/currenttime.html'
language: zh-CN
chinese_source: worker-translation
---

# Current Time

## 端口

### 输出

### **Time** — ROS 时间总线 | 标量

ROS 时间，以总线信号或标量形式返回。总线表示一个 `rosgraph_msgs/Clock` ROS 消息，包含 `Sec` 和 `NSec` 元素。标量是以秒为单位的 ROS 时间。如果未在 `/clock` 主题上接收到时间，该模块输出 `0`。

**数据类型：** `bus` | `double`

## 参数

### **Output format** — ROS 时间的格式 `bus`（默认）| `double`

ROS `Time` 输出的格式，指定为 `bus` 或 `double`。

### **Sample time** — 输出之间的间隔 `-1`（默认）| 数值标量

输出之间的间隔，指定为数值标量。

有关详细信息，请参阅 Specify Sample Time (Simulink)。

## 所属库

ROS Toolbox / ROS

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

检索当前 ROS 时间或系统时间

Current Time 模块输出当前 ROS 或系统时间。ROS 时间基于您计算机的系统时钟或 ROS 节点上发布的 `/clock` 主题。

使用此模块将您的仿真时间与所连接的 ROS 节点同步。

如果 `use_sim_time` ROS 参数设置为 `true`，该模块返回在 `/clock` 主题上发布的仿真时间。否则，该模块返回您机器的系统时间。

当前时间模块工作流程。步骤 1. 节点启动。步骤 2. 检查 `/use_sim_time` ROS 参数是否为 true。步骤 3. 如果为 true，订阅 `/clock` 主题并等待接收时间。如果为 false，获取系统时间。步骤 4. 将接收到的时间作为当前时间输出。
