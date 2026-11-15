---
type: simulink-block
title: 'Read Data'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'Network Access / ROS Network Access / ROS Network Access in Simulink'
documentation_page: 'readdata'
documentation_source_path: 'ref/readdata.html'
language: zh-CN
chinese_source: worker-translation
---

# Read Data

## 端口

### 输出

### **IsNew** — 新消息指示符 `0` | `1`

新消息指示符，以 logical 形式返回。如果输出为 `1`，则表示此时从 rosbag 文件中加载了一条新消息。此输出可用于触发子系统以处理接收到的新消息。

### **Msg** — ROS 消息 nonvirtual bus

ROS 消息，以 nonvirtual bus 形式返回。消息按其在 rosbag 中存储的顺序输出，并与仿真时间同步。

**数据类型：** `bus`

## 参数

### **Topic** — 要从日志文件中提取的话题名称 string

要从日志文件中提取的话题名称，指定为 string。该话题必须存在于已加载的 rosbag 中。点击 **Load rosbag file**。使用 **Select ...** 检查可用话题并选择特定话题。

### **采样时间** — 输出之间的间隔 `–1`（默认）| scalar

输出之间的间隔，指定为 scalar。在仿真中，采样时间遵循仿真时间，而不是实际挂钟时间。

此默认值表示模块采样时间为 *inherited*。

有关 inherited 采样时间类型的详细信息，请参阅 Specify Sample Time (Simulink)。

## 所属库

ROS Toolbox / ROS

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019b 中引入**

## 描述

从日志文件回放数据

Read Data 模块通过基于当前仿真时间输出日志文件中的最新消息来回放 rosbag 日志文件。您必须加载 rosbag 日志文件（`.bag`），并在模块封装中指定 `Topic`，才能从该文件获取消息流。该话题上的消息会与仿真时间同步地从文件中输出。

在 Read Data 模块封装中，点击 **Load log file data** 以指定要加载的 rosbag 日志文件（`.bag`）。在 **Load Log File** 窗口中，指定 **Start time offset**（以秒为单位），以从文件中的某个点开始回放。**Duration** 指定模块应回放此文件的时长，以秒为单位。默认情况下，模块会输出文件中特定 `Topic` 的所有消息。
