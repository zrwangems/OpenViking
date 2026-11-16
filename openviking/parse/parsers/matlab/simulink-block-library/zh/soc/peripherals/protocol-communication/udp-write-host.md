---
type: simulink-block
title: 'UDP Write (HOST)'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Protocol Communication'
documentation_page: 'udpwritehost'
documentation_source_path: 'ref/udpwritehost.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Write (HOST)

## 端口

### 输入

### **Port\_1** — 输入信号数值向量

输入信号，指定为数值向量。该模块将此数据作为 UDP 数据包发送到指定的远程 IP 地址和端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### **Remote IP address ('255.255.255.255' for broadcast)** — 远程主机的 IP 地址 `'255.255.255.255'`（默认）| 点分四段表达式

指定远程主机的 IP 地址。要广播 UDP 数据包，请使用默认值 `'255.255.255.255'`。

### **Remote IP port** — 远程主机的 IP 端口号 `25000`（默认）| 1 到 65,535 之间的整数

指定远程主机的 IP 端口号。

### **Local IP port source** — 本地 IP 端口源的来源 `Automatically determine`（默认）| `Specify via dialog`

通过选择以下值之一来设置模块的本地 IP 端口源：

- `Automatically determine` — 随机分配一个可用的本地 IP 端口号，
  UDP 数据包从该端口发送。
- `Specify via dialog` — 允许您使用 **Local IP port**
  参数指定本地 IP 端口号。

### **Local IP port** — 本地主机的 IP 端口号 `-1`（默认）| 1 到 65,535 之间的整数

指定本地主机的端口号。如果将此值设置为 `-1`（默认），该模块会将本地 IP 端口号设置为随机可用的端口号，并使用该端口发送 UDP 数据包。如果远程主机接受来自特定 IP 端口号的 UDP 数据包，请为此值指定该 IP 端口号。

## 所属库

SoC Blockset / Host I/O

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2019a 中引入**

## 描述

从主机计算机向远程主机发送 UDP 数据包

UDP Write (HOST) 模块将 UDP（用户数据报协议）数据包从本地主机发送到远程主机。本地主机是您希望从中发送 UDP 数据包的主机计算机。远程主机是您希望将 UDP 数据包发送到的主机计算机或硬件。远程主机通过主机计算机中的远程 IP 地址和远程 IP 端口参数进行标识。
