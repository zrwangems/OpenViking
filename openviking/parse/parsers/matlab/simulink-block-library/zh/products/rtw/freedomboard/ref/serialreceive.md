---
type: simulink-block
title: 'Serial Receive'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-KL25Z Board / Modeling'
documentation_page: 'serialreceive'
documentation_source_path: 'freedomboard/ref/serialreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# Serial Receive

## 端口

在 R2025b 中未提供文档。

## 参数

**UART**
:   选择用于串行通信接口的 UART。

**数据类型**
:   选择输出数据的数据类型。您可以从以下选项中选择：
    `double`, `single`,
    `int8`, `uint8`,
    `int16`, `uint16`,
    `int32`, `uint32` 和
    `boolean`。

**数据长度**
:   指定希望使用此模块接收的数据字节数。输入一个大于零的值。默认数据长度为
    `1` byte。

**采样时间**
:   指定模块读取 UART 上可用数据的时间间隔，单位为 seconds。
    默认采样时间为 `0.1` seconds。

## 所属库

在 R2025b 中未提供文档。

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

在 R2025b 中未提供文档。

## 版本历史

**在 R2014b 中推出**

## 描述

通过 UART 接收字节数据的 [Nx1] 数组

通过您选择的 UART 接收字节数据的 [Nx1] 数组。

Serial Receive 模块具有两个输出端口：**Data** 和
**Status**。

当接收到的数据长度大于或等于 **数据长度** 参数中指定的长度时：

- **Data** — 此输出端口输出串行接收缓冲区中的数据值。
- **Status** — 此输出端口输出 `1`。

当接收到的数据长度小于 **数据长度** 参数中指定的长度时：

- **Data** — 此输出端口输出 `0`。
- **Status** — 此输出端口输出 `0`。

**Data** 端口输出的值采用您在 **数据类型** 参数中选择的数据类型。

**Status** 端口输出 `uint8` 值。

在不使用硬件进行仿真时，此模块输出零值。此模块以“非阻塞模式”运行。

FRDM-KL25Z 硬件具有三个 UART：UART0、UART1 和 UART2。

您可以更改所选 UARTx 串行接口的 Tx 引脚、Rx 引脚和波特率，并可通过 **Configuration Parameters > Hardware Implementation pane > UARTx** 查看 FRDM-KL25Z 引脚映射图。
