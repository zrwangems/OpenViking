---
type: simulink-block
title: 'Current Time'
family: 'ros-2'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS 2'
documentation_page: 'currenttimeros2'
documentation_source_path: 'ref/currenttimeros2.html'
language: zh-CN
chinese_source: worker-translation
---

# Current Time

## 端口

### 输出

### **Time** — ROS 2 时间 bus | scalar

ROS 2 时间，以 bus 信号或 scalar 返回。`Output format` 参数决定此输出端口的格式。该 bus 表示一条具有 `sec` 和 `nanosec` 元素的 `builtin_interfaces/Time` ROS 2 消息。该 scalar 是 ROS 2 时间，以 seconds 为单位。如果模块未从 `/clock` 主题接收到时间，则此输出为 `0`。

**数据类型：** `bus` | `double`

## 参数

### **Output format** — ROS 2 时间的格式 `bus`（默认） | `double`

ROS 2 `Time` 输出的格式，指定为 `bus` 或 `double`。

### **Sample time** — 输出之间的间隔 `-1`（默认） | numeric scalar

输出之间的间隔，指定为 numeric scalar。

有关详细信息，请参阅 Specify Sample Time (Simulink)。

## 所属库

ROS Toolbox / ROS 2

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

获取当前 ROS 2 时间或系统时间

Current Time 模块输出当前 ROS 2 时间。ROS 2 时间基于您的计算机的系统时钟或 ROS 2 网络上发布的 `/clock` 主题。

如果 `use_sim_time` ROS 2 参数设置为 `true`，则该模块返回 `/clock` 主题上发布的仿真时间。否则，该模块返回您的机器的系统时间。

Current Time 模块工作流。步骤 1。节点启动。步骤 2。检查 /use\_sim\_time ROS 参数是否为 true。步骤 3。如果为 true，则订阅 /clock 主题并等待接收时间。如果为 false，则获取系统时间。步骤 4。将接收到的时间输出为当前时间。
