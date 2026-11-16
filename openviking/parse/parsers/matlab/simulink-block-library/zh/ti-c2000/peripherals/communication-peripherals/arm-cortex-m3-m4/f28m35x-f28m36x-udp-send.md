---
type: simulink-block
title: 'F28M35x/F28M36x UDP Send'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / Arm Cortex - M3/M4'
documentation_page: 'f28m35xf28m36xudpsend'
documentation_source_path: 'ref/f28m35xf28m36xudpsend.html'
language: zh-CN
chinese_source: worker-translation
---

# F28M35x/F28M36x UDP Send

## 端口

在 R2025b 中未记录。

## 参数

**远程 IP 地址（广播时为 255.255.255.255）**
:   指定用于数据传输的远程 UDP 主机的 IP 地址。若要广播到所有远程主机，请输入 ‘255.255.255.255’。

**远程 IP 端口**
:   指定用于数据传输的远程 UDP 主机的端口号。

**本地 IP 端口（-1 表示自动分配端口）**
:   输入用于数据传输的本地 UDP 主机的端口号。

**等待直到前一数据包传输完成**
:   选中此复选框可仅在上一数据包传输完成后传输 UDP 数据包，以避免数据重叠。保留默认值 ‘-1’ 以允许自动分配端口。

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

在 R2025b 中未记录。

## 描述

向 UDP 主机发送 UDP 数据包

向远程 UDP 主机发送 UDP 数据包。使用 UDP Send 模块进行无状态、无连接且面向字节的数据传输。

可以发送数据类型为 uint8、uint16、int16、uint32、int32、single 或 double 的一维数组。
