---
type: simulink-block
title: 'Read Data'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS 2'
documentation_page: 'readdataros2'
documentation_source_path: 'ref/readdataros2.html'
language: zh-CN
chinese_source: worker-translation
---

# Read Data

## 端口

### 输出

### **IsNew** — 新消息指示符 逻辑标量

新消息指示符，以逻辑标量形式返回。如果输出为 `1`，则模块在对应时间从 ROS 2 bag 文件中加载了一条新消息。此输出可用于触发子系统以处理新消息。

**数据类型：** `Boolean`

### **Msg** — ROS 2 消息 非虚拟总线

ROS 2 消息，以非虚拟总线形式返回。消息按照其在 ROS 2 bag 文件中存储的顺序返回，并与仿真时间同步。

**数据类型：** `bus`

## 参数

### **Topic** — 要从日志文件中提取的话题名称 字符串标量 | 字符向量

指定要从日志文件中提取的话题名称。该话题必须存在于已加载的 ROS 2 bag 文件中。点击 **Select** 以查看可用话题并选择特定话题。

### **Sample time** — 输出之间的间隔 `-1`（默认）| 标量

指定输出之间的间隔。在仿真中，采样时间遵循仿真时间而非挂钟时间。

默认值表示模块采样时间为继承采样时间。有关继承采样时间类型的详细信息，请参阅 Specify Sample Time (Simulink)。

## 所属库

ROS Toolbox / ROS 2

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

### R2025a：读取未注册的消息类型

现在可以从 ROS 2 bag 文件中播放未注册的消息类型。

### R2024a：MCAP 存储格式支持

现在可以从包含一个或多个 MCAP 文件的 bag 文件夹中读取数据。

## 描述

播放 ROS 2 日志文件中的数据

Read Data 模块通过根据当前仿真时间输出日志文件中最新的消息来播放 ROS 2 bag 日志文件。您必须加载 DB3 或 MCAP 文件格式的 ROS 2 bag 文件，并使用 **Topic** 参数指定一个话题，以从文件中获取消息流。该模块从文件中输出该话题的消息，并与仿真时间同步。如果文件夹包含多个 ROS 2 bag 文件，您也可以通过加载扩展名为 `.yaml` 的 `metadata` 文件，使用 Read Data 模块读取它们。

在 Read Data 模块封装中，选择 **Load logfile data** 以指定要加载的 ROS 2 bag 文件。在 **Load Logfile** 对话框中，指定日志文件的完整路径，或选择 Browse 并导航到要加载的 bag 文件。要在文件中的某个点开始播放，请以秒为单位指定 **Start time offset**。要指定模块从指定的开始时间起播放此文件的时长，请以秒为单位指定 **Duration**。默认情况下，模块输出文件中指定话题的所有消息。
