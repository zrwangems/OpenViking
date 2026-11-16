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

该模块从 EtherCAT Get Notifications 模块扫描输入。
### 输出

### **Error** — 指示扫描总线错误 false (默认) | true

一个 boolean 输出，在收到扫描总线错误通知后的一个周期内为 true。

## 参数

在 R2025b 中未记录。

## 所属库

Simulink Real-Time / EtherCAT

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

检测模型中的 EtherCAT 设备何时未响应

EtherCAT Get Scanbus Error Data 模块检测模型中的设备何时未响应，提供错误输出以停止模型，并生成日志输出，指示哪个设备未响应。该日志消息提供详细信息，说明 EtherCAT 网络在何处与 ENI 文件不匹配。该日志消息指示以下任一种情况：某个网络位置缺少设备，或者在某个网络位置发现的设备与该位置的 ENI 中指定的设备不同。仅报告发现的第一个不匹配项。该模块的 `Error` 输出可用于触发 Stop Simulation 模块。
