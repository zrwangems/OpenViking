---
type: simulink-block
title: 'Enable File Log'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / I/O Connectivity / Logging and Profiling'
documentation_page: 'enablefilelog'
documentation_source_path: 'io_ref/enablefilelog.html'
language: zh-CN
chinese_source: official
---

# Enable File Log

## 端口

### 输入

### **E** — 启用或禁用文件日志记录 布尔值

提供对 File Log 模块操作的启用或禁用控制。当模型中的布尔信号触发使能输入时，目标计算机上会生成日志。这些日志的保留取决于 `FileLogMaxRuns` 设置。

## 参数

R2025b 官方文档未提供。

## 所属库

Simulink Real-Time / Logging

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2020b 中推出**

## 描述

启用或禁用目标计算机上信号的文件日志记录

Enable File Log 模块在 Speedgoat® 目标计算机上启用文件日志记录服务，使得模型中的 File Log 模块在输入端口值为真时开始记录数据。当输入端口值为 false 时，该模块将禁用目标计算机上的文件日志记录功能，且 File Log 模块不会记录数据。

若模型包含 Enable File Log 模块，则 `startRecording` 函数和 `stopRecording` 函数仅控制信号流传输，不影响文件日志记录。在此情况下，当您使用 `stopRecording` 函数或点击 **Stop Recording** 按钮时，`start(tg)` `AutoImportFileLog` 选项不会将数据导入仿真数据检查器。

有关文件日志记录工作流的更多信息，请参阅 Real-Time Signal Logging and Streaming Basics。
