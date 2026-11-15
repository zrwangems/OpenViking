---
type: simulink-block
title: 'PX4 Write Parameter'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4writeparameter'
documentation_source_path: 'px4/ref/px4writeparameter.html'
language: zh-CN
chinese_source: worker-translation
---

# PX4 Write Parameter

## 端口

### 输入

### **Data** — 参数数据向量

指定要写入 PX4 参数的数据。

**数据类型：** `int32` | `float`

## 参数

### **参数名称** — PX4 参数的名称 `SL_FLOAT_PARAM`（默认）| 参数名称之一

从下拉列表中选择所需的 PX4 系统参数。在此字段中选择的 **参数名称** 必须是 PX4 参数之一；否则，`Status` 端口会输出值 `1`，表示参数句柄无效。此外，不支持需要系统重启的参数。

### **数据类型** — PX4 参数的数据类型 `FLOAT`（默认）

数据类型会根据您在 **参数名称** 字段中选择的参数自动填充。

**注意**

如果在此字段中选择的 **数据类型** 与 PX4 参数的实际数据类型不匹配，则写入的值可能会导致数据类型不匹配。

### **输出状态** — 数据传输状态 `off`（默认）| `on`

当您选择 **输出状态** 参数时，模块会配置一个输出端口。输出状态指示您指定的参数是否有效。值 `0` 表示参数句柄有效，值 `1` 表示参数句柄无效。

## 所属库

UAV Toolbox Support Package for PX4 Autopilots / PX4 Utility Blocks

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2025a 中引入**

## 描述

写入 PX4 系统参数

Write Parameter 模块写入您指定的 PX4 系统参数，从而轻松修改参数。

该模块支持 PX4 参数参考中列出的参数。您还可以使用符合 PX4 指南的自定义参数。有关详细信息，请参阅 PX4 指南。

在 Connected IO 仿真期间，此模块会将数据写入硬件的各外设。
