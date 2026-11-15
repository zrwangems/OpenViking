---
type: simulink-block
title: 'XCP UDP Bypass'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'XCP Communication / Communication in Simulink'
documentation_page: 'xcpudpbypass'
documentation_source_path: 'ug/xcpudpbypass.html'
language: zh-CN
chinese_source: official
---

# XCP UDP Bypass

## 端口

### 输出

### **Function-call** — 旁路的函数调用 函数调用

将函数调用输出端口连接到包含一个数据采集列表的函数调用子系统。

## 参数

### **任务优先级** — QNX Neutrino 调度器中的任务优先级 191 (默认) | 整数

为 QNX Neutrino 调度器选择任务优先级。

### **采样时间** — 采样时间 `-1` (默认) | 双精度值

选择采样时间。有关详细信息，请参阅子系统中的采样时间 (Simulink)。

## 所属库

Vehicle Network Toolbox / XCP Communication / UDP Simulink Real-Time / XCP / UDP

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

XCP 通信模块支持仅在主机或 Simulink Real-Time 目标上运行的具有有限部署可移植性的代码生成。

代码生成需要与代码生成目标兼容的 C++ 编译器。有关详细信息，请参阅支持和兼容的编译器。

## 版本历史

**在 R2020b 中推出**

## 描述

将函数调用输出端口连接到函数调用子系统

XCP UDP Bypass 模块将函数调用输出端口连接到包含一个数据采集列表的函数调用子系统。当下游数据采集列表有新数据可用时，该模块发出函数调用。

将下游函数调用子系统视为旁路任务：

在 Simulink® Real-Time™ 中，旁路任务以指定的任务优先级异步执行。

在 Simulink 中，模块以指定的采样率定期检查数据采集数据，并相应地执行旁路任务。
