---
type: simulink-block
title: 'Timestamp'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for ArduPilot Autopilots / Algorithm Development'
documentation_page: 'timestamp'
documentation_source_path: 'ardupilot/ref/timestamp.html'
language: zh-CN
chinese_source: worker-translation
---

# Timestamp

## 端口

### 输出

### **Timestamp** — 绝对时间戳向量

来自 ArduPilot 板的绝对时间戳，以 microseconds 为单位。

**数据类型：** `uint64`

## 参数

### **采样时间** — 模块读取值的时间间隔 `-1`（默认）

模块从 ArduPilot Autopilots 读取值的时间间隔。

## 所属库

UAV Toolbox Support Package for ArduPilot Autopilots / Utility Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2025b 中引入**

## 描述

读取绝对时间戳

Timestamp 模块将来自 ArduPilot 板的绝对时间戳（以 microseconds 为单位）读入 Simulink® 模型。此时间戳信息是绝对的，确保其永不回绕或倒退。
