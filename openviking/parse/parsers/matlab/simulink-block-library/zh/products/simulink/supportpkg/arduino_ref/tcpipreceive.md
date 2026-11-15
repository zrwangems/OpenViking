---
type: simulink-block
title: 'TCP/IP Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Internet'
documentation_page: 'tcpipreceive'
documentation_source_path: 'supportpkg/arduino_ref/tcpipreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# TCP/IP Receive

## 端口

### 输出

### **Data** — 用于发出所接收数据 [Nx1] 数组的输出端口

该模块以 [Nx1] 数组形式输出数据。

**数据类型：** `uint8`

### **Status** — 用于发出数据接收状态 1 | 0 的输出端口

此端口显示数据接收状态。状态值 1 表示成功接收数据。

**数据类型：** `int32`

## 参数

### **Server port** — 用于接收数据的服务器端口 `5896`（默认）| 标量

输入你希望 TCP/IP 服务器通过其发起消息接收的端口号。服务器端口号范围为 0 到 65535。

### **Sample time** — 模块接收数据的时间频率 1（默认）| 标量

指定此模块读取 TCP/IP 消息的频率，以 seconds 为单位。输入大于零的值。此值默认为采样时间 `1` second。

较小的值要求处理器在更短的时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

Simulink Support Package for Arduino Hardware / Ethernet Shield

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2013b 中引入**

## 描述

通过 TCP/IP 网络从远程主机接收数据

使用 TCP/IP Receive 模块通过网络从远程主机或其他目标硬件接收数据。
