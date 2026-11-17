---
type: simulink-block
title: 'EtherCAT Get Scanbus Error Data'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'EtherCAT'
documentation_page: 'ethercatgetscanbuserrordata'
documentation_source_path: 'io_ref/ethercatgetscanbuserrordata.html'
language: zh-CN
chinese_source: worker-translation
---

# EtherCAT Get Scanbus Error Data

## 端口

### 输入

### **Values** — 来自 EtherCAT Get Notifications 模块的输入 [`Length` `20 * Notification`]

该模块扫描来自 EtherCAT Get Notifications 模块的输入。
### 输出

### **Error** — 指示 scanbus 错误 false（默认）| true

一个布尔输出，在收到 scanbus 错误通知后的一个周期内为 true。

## 参数

R2025b 中未记录。

## 所属库

Simulink Real-Time / EtherCAT

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

检测模型中的 EtherCAT 设备何时无响应

EtherCAT Get Scanbus Error Data 模块检测模型中的设备何时无响应，提供错误输出以停止模型，并生成日志输出以指示哪个设备无响应。日志消息提供有关 EtherCAT 网络与 ENI 文件不匹配位置的详细信息。日志消息指示在网络位置上存在缺失设备，或者在网络位置上发现的设备与该位置的 ENI 中指定的设备不同。仅报告发现的第一个不匹配。该模块的 `Error` 输出可用于触发 Stop Simulation 模块。
