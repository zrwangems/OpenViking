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

此端口接收多个任务触发并将它们合并为一个。

通过指定 **Number of input task triggers** 参数来定义 **Port\_*`N`*** 输入端口数量。

**数据类型：** `rteEvent`
### 输出

### **Port\_1** — 输出触发标量

此端口发送一个任务信号，触发 Task Manager 模块执行关联的任务。

**数据类型：** `rteEvent`

## 参数

### **Number of input task triggers** — 要合并的触发数量 2（默认）| 正整数

要合并为一个输出触发的任务触发数量，指定为正整数。

## 所属库

SoC Blockset / Processor Task Execution

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

- 要为您的设计自动生成 C 代码，并在 SoC 设备上执行代码，请使用 SoC Builder 工具。有关为 SoC 设计生成代码的详细信息，请参阅 Use SoC Builder to Generate SoC Design。
- 要为您的 SoC 模型生成并执行 C 代码，此模块需要 Embedded Coder® 以及以下支持包之一：

  - 适用于 AMD FPGA 和 SoC 设备的 SoC Blockset™ 支持包
  - SoC Blockset Support Package for Intel® Devices
  - SoC Blockset Support Package for Embedded Linux® Devices
- 要使用此模块，您必须在配置参数中将 **Hardware Board** 设置为受支持的开发板。然后您可以按照说明配置开发板。有关详细信息，请参阅 Create an Embedded Linux Device Configuration。

部署到受支持的硬件开发板时，此模块使用 POSIX 信号量 API 来实现任务触发。

## 版本历史

**在 R2023b 中引入**

## 描述

将多个任务触发合并为一个触发

Task Trigger Merge 模块从一组任务触发中创建一个单一任务触发。将 Task Trigger 模块的输出连接到此模块的输入端口，并将此模块的输出连接到 Task Manager 模块中相应事件驱动任务的事件端口。

将此模块放置在顶层模型中。
