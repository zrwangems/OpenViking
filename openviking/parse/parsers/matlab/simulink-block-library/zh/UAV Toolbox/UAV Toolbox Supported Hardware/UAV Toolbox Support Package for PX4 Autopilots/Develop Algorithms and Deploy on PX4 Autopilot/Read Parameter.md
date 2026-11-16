---
type: simulink-block
title: 'Read Parameter'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'readparameter'
documentation_source_path: 'px4/ref/readparameter.html'
language: zh-CN
chinese_source: worker-translation
---

# Read Parameter

## 端口

### 输出

### **Data** — 参数的标量值

指定的 PX4 系统参数的值

**数据类型：** `int32` | `float`

### **Status** — 接收到的参数值的状态 `0` | `1`

Status 输出指示您指定的参数是否有效。值 `0` 表示参数句柄有效，值 `1` 表示参数句柄无效。

**数据类型：** `Boolean`

## 参数

### **参数名称** — PX4 参数的名称 `ATT_BIAS_MAX`（默认） | 参数之一

输入 PX4 系统参数的名称。

**注意**

您在此字段中输入的 **参数名称** 必须与其中一个 PX4 参数匹配；否则，`Status` 端口会输出 `1`，表示参数句柄无效。

### **数据类型** — PX4 参数的数据类型 `FLOAT`（默认） | int32

选择您在 `Parameter Name` 字段中输入的参数的数据类型。

**注意**

如果您在此字段中选择的 **数据类型** 与 PX4 参数的实际数据类型不匹配，则读取的值可能导致数据类型不匹配。

### **采样时间** — 模块读取值的时间间隔 `0.5`（默认） | 任何非负且为 0.5 的倍数的值 | -1

输入模块从 uORB 网络读取值的时间间隔。

当您将此参数设置为 `-1` 时，Simulink® 会根据模型中的模块上下文确定模块的最佳采样时间。

## 所属库

UAV Toolbox Support Package for PX4 Autopilots

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

读取 PX4 系统参数

Read Parameter 模块读取指定的 PX4 系统参数，并将其值作为输出提供。

该模块支持 PX4 Parameter Reference 页面中列出的所有参数。您还可以使用按照指南开发的自定义参数。

在普通模式仿真期间，该模块输出零。

在 Connected I/O 仿真期间，此模块从硬件的外设读取数据。
