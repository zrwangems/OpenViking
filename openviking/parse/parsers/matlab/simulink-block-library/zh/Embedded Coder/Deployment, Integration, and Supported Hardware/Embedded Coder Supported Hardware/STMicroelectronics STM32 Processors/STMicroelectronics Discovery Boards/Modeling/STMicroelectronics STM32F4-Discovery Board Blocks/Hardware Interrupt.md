---
type: simulink-block
title: 'Hardware Interrupt'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F4-Discovery Board Blocks'
documentation_page: 'hardwareinterrupt'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/hardwareinterrupt.html'
language: zh-CN
chinese_source: worker-translation
---

# Hardware Interrupt

## 端口

在 R2025b 中未记录。

## 参数

**Interrupt group**
:   选择中断组。

    **Interrupt group** 列出中断描述文件中的所有中断
    组。选择某个中断组会更改 **Interrupt name** 参数中的值列表。

**Interrupt name**
:   选择要生成的中断服务例程 (ISR)。

    **Interrupt name** 对应于处理器中断向量表中的特定
    条目。

**Interrupt number**
:   此只读参数指示所选
    ISR 在目标硬件中断向量表中的位置。

**Simulink task priority**
:   要设置下游函数调用子系统的优先级，
    请使用此参数。默认模型基础采样率优先级
    设置为 40，优先级值越低表示优先级越高的
    任务。这些设置可以在 Configuration
    Parameter 的 Solver 窗格中调整。所选中断的 Simulink task priority
    相对于模型基础速率优先级。选中 **Disable
    interrupt pre-emption** 参数，以在执行所选中断服务例程时阻止所有其他中断。

**Disable interrupt pre-emption**
:   默认情况下，中断可被更高优先级
    中断抢占。选择此选项允许低优先级中断
    完成其执行，而不会被其他中断抢占。

**Add simulation input port**
:   选择此选项以启用 SimIRQ 模块输入。当 SimIRQ 输入
    为 true 时，中断模块在仿真中发起函数调用。但是，SimIRQ 在生成代码中会被忽略。

**Interrupt group**
:   选择中断组。

    **Interrupt group** 列出中断描述文件中的所有中断
    组。选择某个中断组会更改 **Interrupt name** 参数中的值列表。

**Interrupt name**
:   选择要生成的中断服务例程 (ISR)。

    **Interrupt name** 对应于处理器中断向量表中的特定
    条目。

**Interrupt number**
:   此只读参数指示所选
    ISR 在目标硬件中断向量表中的位置。

**Simulink task priority**
:   要设置下游函数调用子系统的优先级，
    请使用此参数。默认模型基础采样率优先级
    设置为 40，优先级值越低表示优先级越高的
    任务。这些设置可以在 Configuration
    Parameter 的 Solver 窗格中调整。所选中断的 Simulink task priority
    相对于模型基础速率优先级。选中 **Disable
    interrupt pre-emption** 参数，以在执行所选中断服务例程时阻止所有其他中断。

**Disable interrupt pre-emption**
:   默认情况下，中断可被更高优先级
    中断抢占。选择此选项允许低优先级中断
    完成其执行，而不会被其他中断抢占。

**Add simulation input port**
:   选择此选项以启用 SimIRQ 模块输入。当 SimIRQ 输入
    为 true 时，中断模块在仿真中发起函数调用。但是，SimIRQ 在生成代码中会被忽略。

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

在 R2025b 中未记录。

## 描述

从中断服务例程触发下游函数调用子系统。

# Hardware Interrupt

从
中断服务例程触发下游函数调用子系统。

在模型的生成代码中自动创建中断服务例程 (ISR)。该 ISR 执行与该模块关联的下游函数调用
子系统。

您可以将此模块用于以下目的：

- 使用此模块构建处理器特定的、基于 ARM
  Cortex-M 内核的硬件中断模块。

  您可以通过提供基于 XML 的中断描述文件，将模块自定义为处理器特定的中断。请参阅 Create Hardware Interrupt Block for an ARM Cortex-M Based Processor using an Interrupt Description File。
- 在代码生成中按原样使用此模块，以响应
  Fault 和 NMI 中断服务例程，并触发下游
  函数调用子系统。确保 FaultISR 和 NmiISR 在您的中断向量表中可用。

使用此模块，您可以：

- 在基于 ARM Cortex-M 的处理器上创建 ISR。
- 设置 ISR 优先级。
- 启用或禁用中断抢占。
- 使用仿真输入模拟中断和下游
  子系统的触发。

对于硬件支持包，处理器特定的模块随附
中断描述文件提供。在中断描述
文件中，封装参数会更新为与处理器特性匹配的中断组、名称
和中断号。

此模块仅为指定的 ISR 生成代码。启用中断和特定触发选项的配置
应在外设设置中完成。

- Hardware Interrupt block
