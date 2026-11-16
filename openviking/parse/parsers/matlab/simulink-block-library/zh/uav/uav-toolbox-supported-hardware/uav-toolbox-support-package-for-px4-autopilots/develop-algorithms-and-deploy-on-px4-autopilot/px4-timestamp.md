---
type: simulink-block
title: 'PX4 Timestamp'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4timestamp'
documentation_source_path: 'px4/ref/px4timestamp.html'
language: zh-CN
chinese_source: worker-translation
---

# PX4 Timestamp

## 端口

### 输出

### **Timestamp** — 绝对时间戳 uint64

来自 PX4 Autopilot 的绝对时间戳，以 `uint64` 返回。

**数据类型：** `uint64`

## 参数

### **采样时间** — 模块读取值的时间间隔 `0.01`（默认）| 任何为 0.01 倍数的非负值 | -1

请输入模块从 Pixhawk Autopilot 读取值的时间间隔。

当您将此参数设置为 `-1` 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

UAV Toolbox Support Package for PX4 Autopilots / PX4 Utility Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

## 描述

将来自 PX4 Autopilot 的绝对时间戳输出到 Simulink 模型

PX4 Timestamp 模块从 PX4 Autopilot 获取自启动以来的时间（单位为 microseconds），并将其输入到 Simulink® 模型中。此时间戳信息是绝对的，确保它永远不会回绕或倒退。timestamp 的输出数据类型为 `uint64`。
