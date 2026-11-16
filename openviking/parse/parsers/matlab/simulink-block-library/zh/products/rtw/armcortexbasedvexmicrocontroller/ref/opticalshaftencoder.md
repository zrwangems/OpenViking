---
type: simulink-block
title: 'Optical Shaft Encoder'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Sensors'
documentation_page: 'opticalshaftencoder'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/opticalshaftencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Optical Shaft Encoder

## 端口

R2025b 中未提供相关文档。

## 参数

**顶部端口**
:   选择顶部连接器所连接的数字端口号。可以选择 1 到 12 的端口号，但端口 10 除外。要确定顶部端口，请单击模块参数对话框窗口中的 **什么是顶部端口和底部端口？** 按钮。

**底部端口**
:   选择底部连接器所连接的数字端口号。可以选择 1 到 12 的端口号，但端口 10 除外。要确定底部端口，请单击模块参数对话框窗口中的 **什么是顶部端口和底部端口？** 按钮。

**复位模式**
:   选择用于复位编码器测量值的复位模式。在下面所示的复位模式示例表中，假设模块在时刻 T = 0 的 tick 计数为 0，采样时间为 1 sec。

    此模块支持的不同复位模式如下：

    - `No reset` – 测量值不复位，模块输出旋转的总 tick 数。

      例如，在下表中，在 T = 1 时，编码器沿逆时针方向转过 20 个 tick，因此输出为 20。在 T = 1 和 T = 2 之间，编码器转过 10 个 tick。

      因此，在 T = 2 时，tick 计数为 30（其中 20 来自 T = 1，10 来自 T = 2）。在此复位模式下，任意时刻的输出均为先前计数与当前计数的累积和。
    - `Reset at each sample time` – 对于每个采样周期，模块输出测量值，然后将其复位为 0。

      例如，在下表中，在 T = 1 时，编码器沿逆时针方向转过 20 个 tick，因此输出为 20。在 T = 1 和 T = 2 之间，编码器转过 10 个 tick，因此输出为 10。在此复位模式下，输出为特定时刻的 tick 计数。
    - `Reset by external signal` – 测量值根据模块输入值复位为 0。当向模块输入发送 0 以外的值时，测量值复位为 0。对于每个采样周期，模块输出自上次复位以来的测量值。

      例如，在下表中，当外部信号为 0 时，输出基于 ‘No reset’ 模式；当外部信号非零时，输出基于 ‘Reset at each sample time’ 模式。

**添加用于仿真的输入端口**
:   如果希望在正常模式仿真中由源模块提供输入值，请选中此复选框。

**采样时间**
:   指定此模块读取旋转量的时间间隔，单位为秒。如果选中 **添加用于仿真的输入端口** 复选框，或在 **复位模式** 参数中选择 `Reset by external signal` 选项，则会隐藏 **采样时间** 参数，并继承其值（Sample time = -1）。

## 所属库

R2025b 中未提供相关文档。

## 模块特性

R2025b 中未提供相关文档。

## 扩展功能

R2025b 中未提供相关文档。

## 版本历史

**在 R2017a 中推出**

## 描述

以 ticks 为单位测量电机的旋转量

测量通过传感器的电机轴的旋转量，以 ticks 表示。逆时针旋转时，tick 计数递增；顺时针旋转时，tick 计数递减。每旋转一圈，模块输出为 360 ticks。

在没有硬件的仿真过程中，如果没有任何 Source 模块连接到仿真输入端口，此模块会输出零。请参阅“模块在仿真中产生零或不执行任何操作”。从 VEX Microcontroller 库中的 Utilities 库连接一个 Source 模块，以实现仿真行为。在代码生成期间，连接到 Optical Shaft Encoder 模块输入端口的任何仿真模块都会被忽略，并且不会影响生成的代码。
