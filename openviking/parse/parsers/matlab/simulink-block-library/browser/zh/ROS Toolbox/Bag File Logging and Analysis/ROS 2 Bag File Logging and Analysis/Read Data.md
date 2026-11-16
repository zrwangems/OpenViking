---
type: simulink-block
title: 'Read Data'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'Network Access / ROS 2 Network Access / ROS 2 Network Access in Simulink'
documentation_page: 'readdataros2'
documentation_source_path: 'ref/readdataros2.html'
language: zh-CN
chinese_source: worker-translation
---

# Read Data

## 端口

### 输出

### **IsNew** — 新消息指示符 logical scalar

新消息指示符，以 logical scalar 形式返回。如果输出为
`1`，则该模块在对应时间从 ROS 2 bag 文件中加载了一条新消息。此输出可用于触发子系统以处理
新消息。

**数据类型：** `Boolean`

### **Msg** — ROS 2 消息 nonvirtual bus

ROS 2 消息，以 nonvirtual bus 形式返回。消息按其在 ROS 2 bag 文件中存储的顺序返回，并与仿真时间同步。

**数据类型：** `bus`

## 参数

### **Topic** — 要从日志文件中提取的主题名称 string scalar | character vector

指定要从日志文件中提取的主题名称。该主题必须存在于已加载的 ROS 2 bag 文件中。点击 **Select** 以检查可用主题并选择特定主题。

### **Sample time** — 输出之间的间隔 `-1` (default) | scalar

指定输出之间的间隔。在仿真中，采样时间遵循仿真时间，而不是挂钟时间。

默认值表示模块采样时间是继承的。有关继承采样时间类型的详细信息，请参阅 Specify Sample Time (Simulink)。

## 所属库

ROS Toolbox / ROS 2

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

### R2025a: Read unregistered message types

现在可以从 ROS 2 bag 文件中回放未注册的消息类型。

### R2024a: MCAP Storage Format Support

现在可以从包含一个或多个 MCAP 文件的 bag 文件夹中读取数据。

## 描述

从 ROS 2 日志文件回放数据

Read Data 模块通过基于当前仿真时间输出日志文件中的最新消息，来回放 ROS 2 bag 日志文件。您必须加载 DB3 或 MCAP 文件格式的 ROS 2 bag 文件，并使用 **Topic** 参数指定主题，以从文件中获取消息流。该模块输出文件中此主题的消息，并与仿真时间同步。如果文件夹包含多个 ROS 2 bag 文件，您也可以通过加载扩展名为 `.yaml` 的 `metadata` 文件，使用 Read Data 模块读取它们。

在 Read Data 模块封装中，选择 **Load logfile data** 以指定要加载的 ROS 2 bag 文件。在 **Load Logfile** 对话框中，指定日志文件的完整路径，或选择 Browse 并导航到要加载的 bag 文件。要在文件中的某个点开始回放，请指定 **Start time offset**，单位为 seconds。要指定模块从指定的开始时间回放此文件的时长，请指定 **Duration**，单位为 seconds。默认情况下，该模块输出文件中指定主题的所有消息。
