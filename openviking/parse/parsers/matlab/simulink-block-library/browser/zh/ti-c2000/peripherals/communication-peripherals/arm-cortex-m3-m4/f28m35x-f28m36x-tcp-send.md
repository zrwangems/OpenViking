---
type: simulink-block
title: 'F28M35x/F28M36x TCP Send'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / Arm Cortex - M3/M4'
documentation_page: 'f28m35xf28m36xtcpsend'
documentation_source_path: 'ref/f28m35xf28m36xtcpsend.html'
language: zh-CN
chinese_source: worker-translation
---

# F28M35x/F28M36x TCP Send

## 端口

R2025b 中未记录。

## 参数

**本地 IP 端口**
:   输入用于数据传输的本地主机的 IP 端口。

**等待上一数据包传输完成**
:   选中此复选框以仅在上一数据包传输完成后发送 TCP/IP 数据包。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

向 TCP/IP 网络上的 TCP 主机发送 TCP 数据包

通过 TCP/IP 网络向另一个 TCP 主机发送 TCP 数据包。使用 TCP Send 模块进行面向连接、有状态且基于流的数据传输。此外，TCP Send 模块保证数据传输。

使用此模块，您可以发送数据类型为 uint8、uint16、int16、uint32、int32、single 或 double 的一维数组。
