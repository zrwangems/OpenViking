---
type: simulink-block
title: 'F28M35x/F28M36x TCP Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / Arm Cortex - M3/M4'
documentation_page: 'f28m35xf28m36xtcpreceive'
documentation_source_path: 'ref/f28m35xf28m36xtcpreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# F28M35x/F28M36x TCP Receive

## 端口

在 R2025b 中未记录。

## 参数

**Local IP Port**
:   输入本地主机的 IP 端口号以接收数据。

**Data type**
:   选择 TCP 数据包的数据类型。

**Data size (N)**
:   输入在 **Data type** 参数中所选数据类型的数据大小。

**Wait until data received**
:   选中此复选框，以仅在前一个数据包接收后接收 TCP 数据包，从而避免数据重叠。

**Sample time**
:   指定此模块读取端口缓冲区的频率。输入大于零的值。

    此值默认为采样时间 0.01 seconds。较小的值要求处理器在更短时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

在 R2025b 中未记录。

## 描述

从 TCP/IP 网络上的 TCP 主机接收 TCP 数据包

通过 TCP/IP 网络从另一台 TCP 主机接收 TCP 数据包。使用 TCP Receive 模块进行面向连接的、有状态的、基于流的数据传输。此外，TCP Receive 模块保证数据传输。

此模块将接收到的数据输出为在 **Data size** 参数中指定大小的数组。

模块上的 status 端口指示数据是否正常。

status 端口返回的不同值如下：

0 - 表示数据接收无错误

1 - 表示数据接收出错。
