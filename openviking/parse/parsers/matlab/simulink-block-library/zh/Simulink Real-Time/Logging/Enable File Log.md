---
type: simulink-block
title: 'Enable File Log'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Logging'
documentation_page: 'enablefilelog'
documentation_source_path: 'io_ref/enablefilelog.html'
language: zh-CN
chinese_source: worker-translation
---

# Enable File Log

## 端口

### 输入

### **E** — 启用或禁用文件记录 布尔

提供对 File Log 模块操作的启用或禁用控制。当模型中的布尔信号触发使能输入时，目标计算机上会创建日志。这些日志的保留取决于 `FileLogMaxRuns` 设置。

## 参数

R2025b 中未记录。

## 所属库

Simulink Real-Time / Logging

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

启用或禁用目标计算机上信号的文件记录

Enable File Log 模块在 Speedgoat® 目标计算机上启用文件记录服务，以便当输入端口值为 true 时，模型中的 File Log 模块开始记录数据。当输入端口值为 false 时，该模块禁用目标计算机上的文件记录，File Log 模块不会记录数据。

如果模型包含 Enable File Log 模块，则 `startRecording` 函数和 `stopRecording` 函数仅控制信号流式传输，而不控制 File Log 记录。在这种情况下，当您使用 `stopRecording` 函数或点击 **Stop Recording** 按钮时，`start(tg)` 的 `AutoImportFileLog` 选项不会将数据导入 Simulation Data Inspector。

有关文件记录工作流的详细信息，请参阅 Real-Time Signal Logging and Streaming Basics。
