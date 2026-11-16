---
type: simulink-block
title: 'XCP UDP Bypass'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'XCP / UDP'
documentation_page: 'xcpudpbypass'
documentation_source_path: 'io_ref/xcpudpbypass.html'
language: zh-CN
chinese_source: official
---

# XCP UDP Bypass

## 端口

### 输出

### **Function-call** — 绕过函数调用 函数调用

将函数调用输出端口连接到包含一个数据采集列表的函数调用子系统。

## 参数

### **Task Priority** — QNX Neutrino 调度器中的任务优先级 191 (默认) | 整数

为 QNX Neutrino 调度程序选择任务优先级。

### **Sample Time** — 采样时间 `-1` (默认) | 双精度

选择采样时间。有关详细信息，请参阅子系统中的采样时间。

## 所属库

Vehicle Network Toolbox / XCP Communication / UDP Simulink Real-Time / XCP / UDP

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

XCP 通信模块支持代码生成，但其部署可移植性有限，仅能在主机计算机或 Simulink Real-Time 目标设备上运行。

代码生成需要一个与代码生成目标兼容的 C++编译器。有关更多信息，请参阅支持和兼容的编译器。

## 版本历史

**在 R2020b 中推出**

## 描述

将函数调用输出端口连接到函数调用子系统

XCP UDP Bypass 模块将函数调用输出端口连接至包含一个数据采集列表的函数调用子系统。当下游数据采集列表中有新数据可用时，该模块会发出函数调用。

将下游函数调用子系统视为旁路任务：

在 Simulink® Real-Time™ 中，旁路任务以分配的任务优先级异步执行。

在 Simulink 中，该模块按指定采样率周期性地检查数据采集状态，并据此执行旁路任务。
