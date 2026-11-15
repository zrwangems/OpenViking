---
type: simulink-block
title: 'Serial Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Communications'
documentation_page: 'serialreceive'
documentation_source_path: 'supportpkg/android_ref/serialreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# Serial Receive

## 端口

R2025b 中未记录。

## 参数

### **数据类型** — 数据类型 `int32`（默认）

选择要在串行端口上接收的数据的数据类型。
可以在串行端口上接收 int8、uint8、int16、uint16、int32、uint32、double、single 或 boolean 数据类型。

### **数据长度** — 数据长度的值 `1`（默认）

输入要在串行端口上接收的数据元素数量。

### **采样时间** — 模块采样时间 `0.1`（默认）

指定此模块读取串行端口缓冲区的频率。输入一个大于零的值。此值默认为 `0.1` second 的采样时间。最小值为 `0.001` second。

较小的值要求处理器在更短的时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

Simulink Support Package for Android Devices / Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

## 描述

在串行端口上接收 [Nx1] 数据数组，并将其写入 Data 模块输出。当数据不可用时，将 0 写入 Data 模块输出

在指定的串行端口上获取 [Nx1] 数据数组，并写入 Data 模块输出。

Serial Receive 模块有两个输出：**Data** 和 **Status**。

当数据可用时：

- **Data** 模块输出发出串行接收缓冲区中的数据。
- **Status** 模块输出发出 `1`。

当数据不可用时：

- **Data** 模块输出发出 `0`。
- **Status** 模块输出发出 `0`。

**Data** 模块根据模块上选定的 **数据类型** 参数值输出数据类型：int8、uint8、int16、uint16、int32、uint32、double、single 或 boolean。默认数据类型为 int32。

**Status** 模块输出发出 int 值。你可以使用 Status 模块输出判断 **Data** 端口发出的 `0` 值是数据，还是表示未接收到数据的指示。

在仿真期间，此模块输出 `0`。

**注意**

一个模型中只允许有一个 Serial Transmit 和一个 Serial Receive 模块。
