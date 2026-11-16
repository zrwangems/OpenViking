---
type: simulink-block
title: 'Integrated Encoder Module'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Sensors'
documentation_page: 'integratedencodermodule'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/integratedencodermodule.html'
language: zh-CN
chinese_source: worker-translation
---

# Integrated Encoder Module

## 端口

R2025b 中未提供文档。

## 参数

**电机类型**
:   选择安装编码器的电机类型。电机类型决定每旋转一周的 tick 数。

**I2C 端口的序列顺序**
:   在菊花链中选择 Integrated Encoder Module 的序号。序号从 0 开始，0 分配给连接到
    I2C 端口的 Integrated Encoder Module，下一个模块的序号为 1，依此类推。

**复位模式**
:   选择用于将编码器测量值复位的复位模式。在下面所示的复位模式示例表中，
    假设该模块在时刻 T = 0 的 tick 计数为 0，采样时间为 1 sec。

    此模块支持的不同复位模式如下：

    - `No reset` – 测量值不复位，模块输出旋转的总 tick 数。

      例如，在下表中，T = 1 时，编码器沿逆时针方向转动了 20 个 tick，
      因此输出为 20。在 T = 1 和 T = 2 之间，编码器转动了 10 个 tick。

      因此，T = 2 时 tick 计数为 30（来自 T = 1 的 20 和来自 T = 2 的 10）。
      在此复位模式下，任意时刻的输出都是先前计数与当前计数的累积和。
    - `Reset at each sample time` – 对于每个采样周期，模块输出测量值，
      然后将其复位为 0。

      例如，在下表中，T = 1 时，编码器沿逆时针方向转动了 20 个 tick，
      因此输出为 20。在 T = 1 和 T = 2 之间，编码器转动了 10 个 tick，
      因此输出为 10。在此复位模式下，输出为特定时刻的 tick 计数。
    - `Reset by external signal` – 根据模块输入值将测量值复位为 0。
      当您向模块输入发送非 0 值时，测量值将复位为 0。对于每个采样周期，
      模块输出自上次复位以来的测量值。

      例如，在下表中，当外部信号为 0 时，输出基于 `No reset` 模式；
      当外部信号为非零值时，输出基于 `Reset at each sample time` 模式。

**输出旋转速度**
:   选中此复选框可输出内部编码器轮的旋转速度，单位为每分钟转数 (rpm)。

**添加用于仿真的输入端口**
:   如果您希望进行普通模式仿真，并由源模块提供输入值，请选中此复选框。

**采样时间**
:   指定此模块读取旋转量的时间间隔，单位为秒。如果选中**添加用于仿真的输入端口**
    复选框，或在**复位模式**参数中选择 `Reset by external signal` 选项，
    则隐藏**采样时间**参数，并继承其值（Sample time = -1）。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**于 R2017a 引入**

## 描述

以 ticks 为单位测量电机的旋转

测量安装了该传感器的电机的旋转，以 ticks 为单位。逆时针旋转时，tick 计数递增；
顺时针旋转时，tick 计数递减。模块根据电机类型输出 tick 计数。

在没有硬件的仿真过程中，如果没有 Source 模块连接到仿真输入端口，此模块会输出零。
请参阅“模块在仿真中输出零或不执行任何操作”。要实现仿真行为，请连接 VEX Microcontroller
库中 Utilities 库的 Source 模块。在代码生成过程中，连接到 Integrated Encoder Module
模块输入端口的任何仿真模块都会被忽略，且对生成的代码没有任何影响。
