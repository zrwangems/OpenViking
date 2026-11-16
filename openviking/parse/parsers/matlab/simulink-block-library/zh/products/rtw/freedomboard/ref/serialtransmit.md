---
type: simulink-block
title: 'Serial Transmit'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-KL25Z Board / Modeling'
documentation_page: 'serialtransmit'
documentation_source_path: 'freedomboard/ref/serialtransmit.html'
language: zh-CN
chinese_source: worker-translation
---

# Serial Transmit

## 端口

R2025b 中未提供文档。

## 参数

**UART**
:   选择用于串行通信接口的 UART。

    使用外部模式时，请确保不要选择 UART0，因为外部模式使用 UART0 进行目标机到主机的通信。

**Send mode**
:   要向 UART 传输字节数据数组，请将 Send mode 参数设置为 putc。

    选择 printf 值以进行调试。您可以将任意数据类型的数组发送到终端。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**在 R2014b 中引入**

## 描述

将 [MxN] 数据数组发送到 UART

将 [MXN] 数据数组发送到所选的 UART。

您可以在 **配置参数** > **硬件实现窗格** > **UARTx** 中更改波特率，并为 UARTx 串行接口选择 Tx 引脚。

在没有硬件的情况下进行仿真时，此模块不执行任何操作。
