---
type: simulink-block
title: 'Task Trigger Merge'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Processor Task Execution'
documentation_page: 'tasktriggermerge'
documentation_source_path: 'ref/tasktriggermerge.html'
language: zh-CN
chinese_source: worker-translation
---

# Task Trigger Merge

## 端口

### 输入

### **Port\_1** — 输入触发标量

该端口接收多个任务触发并将它们合并为一个。

您通过指定 **输入任务触发数** 参数来定义 **Port\_*`N`*** 输入端口数量。

**数据类型：** `rteEvent`
### 输出

### **Port\_1** — 输出触发标量

该端口发送一个任务信号，该信号触发 Task Manager 模块执行关联任务。

**数据类型：** `rteEvent`

## 参数

### **输入任务触发数** — 要合并的触发数 2（默认）| 正整数

要合并为一个输出触发的任务触发数，指定为正整数。

## 所属库

SoC Blockset / Processor Task Execution

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

- 要自动为您的设计生成 C 代码，
  并在 SoC 设备上执行该代码，请使用 SoC Builder 工具。
  有关为 SoC 设计生成代码的详细信息，请参阅使用 SoC Builder 生成 SoC 设计。
- 要为您的 SoC 模型生成并执行 C 代码，该模块需要 Embedded Coder® 以及以下支持包之一：

  - SoC Blockset™ Support Package for AMD FPGA and SoC Devices
  - SoC Blockset Support Package for Intel® Devices
  - SoC Blockset Support Package for Embedded Linux® Devices
- 要使用该模块，您必须将配置参数中的 **硬件板** 设置为支持的板卡。然后，您可以按照说明配置板卡。有关详细信息，请参阅创建 Embedded Linux 设备配置。

当部署到支持的硬件板时，该模块使用 POSIX 信号量 API 实现任务触发。

## 版本历史

**在 R2023b 中引入**

## 描述

将多个任务触发合并为一个触发

Task Trigger Merge 模块从一组任务触发创建单个任务触发。将 Task Trigger 模块输出连接到该模块的输入端口，并将该模块的输出连接到 Task Manager 模块中相应事件驱动任务的事件端口。

将该模块放在顶层模型中。
