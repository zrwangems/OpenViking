---
type: simulink-block
title: 'Hardware Interrupt'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / ARM Cortex-M Processors / Modeling'
documentation_page: 'hardwareinterrupt'
documentation_source_path: 'armcortexm/ref/hardwareinterrupt.html'
language: zh-CN
chinese_source: worker-translation
---

# Hardware Interrupt

## 端口

R2025b 中未记录。

## 参数

R2025b 中未记录。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

**在 R2014b 中引入**

## 描述

从中断服务例程触发下游函数调用子系统。

# Hardware Interrupt

从中断服务例程触发下游函数调用子系统。

****需要附加功能：** 此功能需要 Embedded Coder Support Package for ARM Cortex-M Processors 附加组件。**

在模型生成的代码中自动创建中断服务例程 (ISR)。该 ISR 执行与模块关联的下游函数调用子系统。

您可以将此模块用于以下目的：

- 使用此模块构建特定于处理器的、基于 ARM®
  Cortex®-M 内核的硬件中断模块。

  您可以通过提供基于 XML 的中断描述文件，将模块自定义为特定于处理器的中断。请参阅《使用中断描述文件为基于 ARM Cortex-M 的处理器创建 Hardware Interrupt 模块》。

  在代码生成中按原样使用此模块，以响应 Fault 和 NMI
  中断服务例程，并触发下游函数调用子系统。请确保 FaultISR 和 NmiISR
  在您的中断向量表中可用。

使用此模块，您可以：

- 在基于 ARM Cortex-M 的处理器上创建 ISR。
- 设置 ISR 优先级。
- 启用或禁用中断抢占。
- 使用仿真输入模拟中断和下游子系统的触发。

对于硬件支持包，处理器特定的模块随中断描述文件一起提供。在中断描述文件中，掩码参数会更新为与处理器特性匹配的中断组、名称和中断编号。

此模块仅为指定的 ISR 生成代码。启用中断和特定触发选项的配置应在外设设置中完成。

- Hardware Interrupt 模块
