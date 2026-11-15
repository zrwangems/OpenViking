---
type: simulink-block
title: 'F28M35x/F28M36x UDP Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / Arm Cortex - M3/M4'
documentation_page: 'f28m35xf28m36xudpreceive'
documentation_source_path: 'ref/f28m35xf28m36xudpreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# F28M35x/F28M36x UDP Receive

## 端口

在 R2025b 中未记录。

## 参数

**Local IP Port**
:   输入本地 UDP 主机 IP 端口以接收 UDP 数据包。

**Remote IP address (0.0.0.0 for accepting all)**
:   输入远程 UDP 主机的 IP 地址，格式为 0.0.0.0，以接收 UDP 数据包。要从任何有效 IP 地址接收数据，请输入 ‘0.0.0.0’。

**Data type**
:   选择 UDP 数据包的数据类型。

**Data size (N)**
:   输入你在 **Data type** 参数中选择的数据类型的数据大小。

**Wait until data received**
:   选中此复选框，以仅在前一个数据包已接收后接收 UDP 数据包，从而避免数据重叠。

**Sample time**
:   指定此模块应读取端口缓冲区的频率。输入大于零的值。

    此值默认为 0.01 seconds 的采样时间。较小的值要求处理器在更短时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

在 R2025b 中未记录。

## 描述

从指定的 UDP 主机接收 UDP 数据包

从指定的远程主机接收 UDP 数据包。使用 UDP Receive 模块将接收到的 UDP 数据包输出为在 **Data size** 参数中定义大小的一维数组。使用 UDP Receive 模块进行无状态、无连接和面向字节的数据传输。

你可以在 **Remote IP address (0.0.0.0. for accepting all)** 参数中指定远程 UDP 主机，以将 UDP 数据包发送到在 **Local IP Port** 参数中指定的本地 UDP 主机。

模块上的 status 端口指示数据是否良好。

status 端口返回的不同值如下：

0 - 表示数据接收无错误

1 - 表示数据接收出错。
