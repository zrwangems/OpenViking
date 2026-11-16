---
type: simulink-block
title: 'PX4 uORB Message'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4uorbmessage'
documentation_source_path: 'px4/ref/px4uorbmessage.html'
language: zh-CN
chinese_source: worker-translation
---

# PX4 uORB Message

## 端口

R2025b 中未记录。

## 参数

### **Topic** — 用于创建空白 uORB 消息的 uORB 主题名称 vehicle\_gps\_position（默认）| uORB 主题之一

选择供该模块创建空白消息的 uORB 主题名称。点击 **Select** 浏览已下载的 `px4/Firmware/msg` 目录中可用的主题名称。

### **Sample time** — 输出之间的间隔 `Inf`（默认）| 数值标量

输入该模块提供空白 uORB 消息的时间间隔。

默认值表示模块输出永不变化。使用此值可加快仿真和代码生成，因为无需重新计算模块输出。否则，模块会在 **Sample time** 的每个间隔输出一条新的空白消息。

## 所属库

UAV Toolbox Support Package for PX4 Autopilots / PX4 uORB Read and Write Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

使用指定的 uORB 主题创建空白消息

PX4 uORB Message 模块创建一个 Simulink® 非虚拟总线，其中包含与所选 uORB 主题对应的空白消息。
该模块创建可与 `PX4 uORB Write`
模块配合使用的 uORB 消息总线。

### 输出

### **Msg** — 空白 uORB 消息非虚拟总线

空白 uORB 消息，以非虚拟总线形式返回。uORB 消息的类型使用参数 `Topic` 指定。总线的所有元素都初始化为 0。连接 Bus Assignment 模块以修改消息中的特定字段。

**数据类型：** `bus`
