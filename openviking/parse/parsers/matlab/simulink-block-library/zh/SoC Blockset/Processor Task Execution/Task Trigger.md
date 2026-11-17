---
type: simulink-block
title: 'Task Trigger'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Processor Task Execution'
documentation_page: 'tasktrigger'
documentation_source_path: 'ref/tasktrigger.html'
language: zh-CN
chinese_source: worker-translation
---

# Task Trigger

## 端口

### 输出

### **Port\_1** — 输出触发标量

此端口发送任务信号，触发 Task Manager 模块执行关联的任务。

**数据类型：** `rteEvent`

## 参数

R2025b 中未记录。

## 所属库

SoC Blockset / Processor Task Execution

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

- 要为您的设计自动生成 C 代码，并在 SoC 设备上执行代码，请使用 SoC Builder 工具。
  有关为 SoC 设计生成代码的更多信息，请参阅 Use SoC Builder to Generate SoC Design。
- 要为您的 SoC 模型生成并执行 C 代码，此模块需要 Embedded Coder® 以及以下支持包之一：

  - SoC Blockset™ 对 AMD FPGA 和 SoC 设备的支持包
  - SoC Blockset Support Package for Intel® Devices
  - SoC Blockset Support Package for Embedded Linux® Devices
- 要使用此模块，您必须在配置参数中将 **Hardware Board** 设置为受支持的开发板。然后您可以按照说明配置开发板。有关更多信息，请参阅 Create an Embedded Linux Device Configuration。

当部署到受支持的硬件开发板时，此模块使用 POSIX 信号量 API 来实现任务触发。

## 版本历史

**在 R2023b 中引入**

## 描述

在您的应用程序中触发任务执行

Task Trigger 模块触发应用程序中事件驱动任务的执行。将此模块的输出连接到 Task Manager 模块中相应任务的事件端口。
将此模块放置在参考模型中的相应任务中。

您可以在同一任务中放置多个此模块。

使用此模块可实现高效的任务调度，并在任务之间实现显式同步。
