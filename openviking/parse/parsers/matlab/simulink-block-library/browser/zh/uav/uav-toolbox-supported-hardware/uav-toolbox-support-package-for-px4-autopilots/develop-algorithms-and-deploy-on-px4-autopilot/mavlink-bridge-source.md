---
type: simulink-block
title: 'MAVLink Bridge Source'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'mavlinkbridgesource'
documentation_source_path: 'px4/ref/mavlinkbridgesource.html'
language: zh-CN
chinese_source: worker-translation
---

# MAVLink Bridge Source

## 端口

### 输出

### **Data** — MAVLink 数据流向量

此端口输出 MAVLink 数据流。

**数据类型：** `uint8`

### **Length** — 数据流长度标量

此端口输出当前时间设置下数据流的长度。

**数据类型：** `uint16`

## 参数

### **串行端口** — 用于连接 Pixhawk 板的端口 `Select a port`（默认） | `COM1` | `COM3` | `Specify manually`

选择用于连接 Pixhawk 板的串行端口。如果列表中所需端口不可用，请选择 `Specify manually`，然后在 **串行端口（手动指定）** 字段中输入串行端口。

### **最大数据长度** — 最大输出数据流长度 `1024`（默认） | `any non-negative value`

输入最大输出数据流长度。

### **目标端口** — 用于启用数据路由的端口 `'UDP','127.0.0.1','14550'`（默认）

点击 **Add** 以添加用于数据路由的目标 UDP/TCP 连接。现有连接 (`'UDP','127.0.0.1','14550'`) 用于连接到 QGC。

**注意**

MAVLink Bridge 模块使用以下本地端口设置：

- 地面控制站本地端口：`14570`
- 板载连接本地端口：`14580`

### **采样时间** — 输出之间的间隔 `0.01`（默认） | 任何非负整数，且为 0,001 的倍数 | `-1`

指定模块从串行连接读取值并将其路由到已添加的 UDP/TCP 连接的时间间隔。

## 所属库

px4MAVLinkBridgelib

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022a 中引入**

## 描述

从 Pixhawk 板读取 MAVLink 数据

MAVLink Bridge Source 模块从连接到串行端口的 Pixhawk® 板读取 MAVLink 数据流，并将其路由到 Simulink® 被控对象模型和已配置的 UDP/TCP 对象。此模块允许您配置串行、UDP 和 TCP 连接。

要访问该模块，请在 MATLAB® 命令窗口中输入以下命令以打开模块库。

    px4MAVLinkBridgelib

MAVLink Bridge Source 和 MAVLink Bridge Sink 模块提供了一种在 HITL 工作流中从 Pixhawk 硬件将 MAVLink 数据流路由到任务规划软件 QGroundControl(QGC)、板载计算机硬件、Simulink Plant，以及反向路由的方法。有关详细信息，请参阅 MAVLink Connectivity for QGC, On-board Computer and Simulink Plant。
