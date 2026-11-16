---
type: simulink-block
title: 'MAVLink Bridge Sink'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'mavlinkbridgesink'
documentation_source_path: 'px4/ref/mavlinkbridgesink.html'
language: zh-CN
chinese_source: worker-translation
---

# MAVLink Bridge Sink

## 端口

### 输入

### **Data** — MAVLink 数据流向量

此端口将 MAVLink 数据流（uint8）作为输入。

**数据类型：** `unit8`

## 参数

### **串行端口** — 用于连接 Pixhawk 板的端口 `Select a port`（默认） | `COM1` | `COM3` | `Specify manually`

选择用于连接到 Pixhawk 板的串行端口。如果列表中所需端口不可用，请选择 `Specify manually`，然后在 **串行端口（手动指定）** 字段中输入串行端口。

**注意**

必须在 MAVLink Bridge Source 和 MAVLink Bridge Sink 模块中选择/指定相同的串行端口。

### **源端口** — 用于启用数据路由的端口 `'UDP','127.0.0.1','14550'`（默认）

点击 **添加** 以添加用于数据路由的源 UDP/TCP 连接。现有连接（`'UDP','127.0.0.1','14550'`）用于连接到 QGC。

**注意**

MAVLink 桥接模块使用以下本地端口设置：

- 地面控制站的本地端口：
  `14570`
- 机载连接的本地端口：`14580`

## 所属库

px4MAVLinkBridgelib

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022a 中引入**

## 描述

将 MAVLink 数据写入 Pixhawk 板

MAVLink Bridge Sink 模块从源 UDP/TCP 端口读取 MAVLink 数据，将其与输入数据合并，并写入连接到串行端口的 Pixhawk® 硬件。

要访问该模块，请在 MATLAB® 命令窗口中输入以下命令以打开模块库。

```
px4MAVLinkBridgelib
```

MAVLink Bridge Sink 和 MAVLink Bridge Source 模块提供了一种在 HITL 工作流中将 MAVLink 数据流从 Pixhawk 硬件路由到任务规划软件 QGroundControl(QGC)、机载计算机硬件、Simulink Plant，以及反向路由的方法。有关详细信息，请参阅 MAVLink Connectivity for QGC, On-board Computer and Simulink Plant。
