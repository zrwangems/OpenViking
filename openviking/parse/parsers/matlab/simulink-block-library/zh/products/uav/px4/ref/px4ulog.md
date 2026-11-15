---
type: simulink-block
title: 'PX4 ULog'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4ulog'
documentation_source_path: 'px4/ref/px4ulog.html'
language: zh-CN
chinese_source: worker-translation
---

# PX4 ULog

## 端口

### 输入

### **double\_a** — 第一个输入信号，指定为 double 标量

由该模块记录的输入信号，指定为 double。

**数据类型：** `double`

### **double\_b** — 第二个输入信号，指定为 double 标量

由该模块记录的输入信号，指定为 double。

**数据类型：** `double`

### **single\_a** — 第一个输入信号，指定为 single 标量

由该模块记录的输入信号，指定为 single。

**数据类型：** `single`

### **single\_b** — 第二个输入信号，指定为 single 标量

由该模块记录的输入信号，指定为 single。

**数据类型：** `single`

## 参数

### **Topic** — 要将 Simulink 信号记录到的 uORB 主题的名称 SL\_CustomPX4uORB（默认） | 其中一个 uORB 主题

选择该模块需要记录 Simulink 信号的 uORB 主题的名称。
单击 **Select** 浏览你下载的 `px4` 目录的 `Firmware/msg` 文件夹中可用的主题名称。

## 所属库

UAV Toolbox Support Package for PX4 Autopilots / PX4 Utility Blocks

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

## 描述

将 Simulink 信号以 ULog 格式记录到 SD 卡

PX4 ULog 模块将 Simulink® 信号以 ULog 格式记录到 SD 卡。

在 PX4 Autopilots 中，系统架构使用记录器模块，以 ULog 文件格式记录主题。PX4 使用 ULog 文件格式进行 uORB 记录消息。这些消息通常称为 micro-ORB（Object Request Broker），并构成 PX4 中订阅、发布架构的基础。

ULog 格式对于飞行后分析很高效。使用 ulogreader、飞行日志记录器应用或在线工具，你可以分析、可视化和转换 ULog 文件，以获得见解并提高基于 PX4 的自主系统的性能。

模块中的端口数量根据所选的 uORB 主题更新。要创建自己的主题，请使用 `createPX4uORBMessage` API。该模块当前配置为默认 uORB 主题 `SL_CustomPX4uORB`，该主题在设置屏幕期间构建。

**注意**

该模块不支持 PX4 Host target 和 Connected I/O Simulation。
