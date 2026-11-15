---
type: simulink-block
title: 'TCP/IP Send'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Internet'
documentation_page: 'tcpipsend'
documentation_source_path: 'supportpkg/arduino_ref/tcpipsend.html'
language: zh-CN
chinese_source: worker-translation
---

# TCP/IP Send

## 端口

### 输入

### **Port\_1** — 用于接收数据的输入端口 [Nx1] 数组

该模块输入要从模块发送到远程主机的数据值。

**数据类型：** `uint8`

## 参数

### **服务器端口** — 服务器端口号 `50000`（默认值）| 1 到 65,535 的整数

输入你希望 TCP/IP 服务器通过其发送消息的端口号。服务器端口号范围为 0 到 65535。

## 所属库

Simulink Support Package for Arduino Hardware / Ethernet Shield

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**R2013b 中引入**

## 描述

通过 TCP/IP 网络向另一台远程主机发送数据

使用 TCP/IP Send 模块通过网络向远程主机或另一块硬件板发送数据。
