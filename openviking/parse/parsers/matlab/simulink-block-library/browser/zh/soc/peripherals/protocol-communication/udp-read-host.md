---
type: simulink-block
title: 'UDP Read (HOST)'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Protocol Communication'
documentation_page: 'udpreadhost'
documentation_source_path: 'ref/udpreadhost.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Read (HOST)

## 端口

### 输出

### **data** — 从远程主机接收的 UDP 数据包 数值向量

在本地主机计算机上接收的 UDP 数据包，以数值向量形式返回。**消息的数据类型** 和 **长度** 参数分别设置此输出数据类型和数据包长度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **length** — UDP 数据包的长度 非负标量

在 **data** 端口上返回的 UDP 数据包长度。

在清除 **输出可变大小信号** 参数之前，此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### **本地 IP 端口** — 本地主机的 IP 端口号 `25000`（默认值）| 1 到 65,535 的整数

指定本地主机的 IP 端口号。

**注意**

在 Linux® 上，要将本地 IP 端口号设置为小于 1024 的值，请以 root 权限运行 MATLAB®。例如，在 Linux 命令行中，输入：

    sudo matlab

### **远程 IP 地址 ('0.0.0.0' 表示接受所有)** — 远程主机的 IP 地址 `'0.0.0.0'`（默认值）| 点分四段表达式

指定远程主机的 IP 地址。将此值设置为特定 IP 地址，以阻止来自所有其他 IP 地址的 UDP 数据包。要接受来自所有 IP 地址的 UDP 数据包，请使用默认值 `'0.0.0.0'`。

### **接收缓冲区大小 (bytes)** — 接收数据中的最大数据 bytes 数 `8192`（默认值）| 正整数

指定要存储在本地缓冲区中的 UDP 数据包的最大数据 bytes 数。将此值设置得足够大，以避免缓冲区溢出导致的数据丢失。

### **消息的最大长度** — 数据的最大长度 `255`（默认值）| 正整数标量

指定输出 UDP 数据包的最大长度。将此参数设置为等于或大于 UDP 数据包数据大小的值。模块会截断超过此长度的任何数据。

UDP 数据包的最大有效负载大小为 65,507 bytes。**消息的最大长度** 等于 UDP 数据包的最大有效负载大小（以 bytes 为单位）除以 UDP 数据包的数据类型大小。例如，如果输出数据类型为 `double`，则将 **消息的最大长度** 值设置为 65507/8 = 8118。

### **消息的数据类型** — 输出 UDP 数据包的数据类型 `uint8`（默认值）| `single` | `double` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

选择输出 UDP 数据包向量元素的数据类型。将此数据类型与远程主机发送的 UDP 数据包的数据类型匹配。

### **阻塞时间 (seconds)** — 等待 UDP 数据包的时间 `0`（默认值）| 非负标量

指定每个采样中在将控制权返回给调度器之前等待 UDP 数据包的持续时间。

### **采样时间 (seconds)** — 采样时间 `0.01`（默认值）| 非负标量

指定调度器运行此模块的频率。

## 所属库

SoC Blockset / Host I/O

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

在本地主机计算机上从远程主机接收 UDP 数据包

UDP Read (HOST) 模块在本地主机上从远程主机接收 UDP（用户数据报协议）数据包。本地主机是您要在其上接收 UDP 数据包的主机计算机。远程主机是您要从中接收 UDP 数据包的主机计算机或硬件。
