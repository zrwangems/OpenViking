---
type: simulink-block
title: 'Floating Reference'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Electrical Models / Electrical Elements'
documentation_page: 'floatingreference'
documentation_source_path: 'ref/floatingreference.html'
language: zh-CN
chinese_source: worker-translation
---

# Floating Reference

## 端口

### 守恒

### **n** — 直流电流为零的电气端口

直流电流为零的电气守恒端口。使用此端口可测量浮动电气网络中其他节点的电压。

## 参数

### **Capacitance** — 阻断直流电流的电容 `1 uF`（默认）| positive scalar

表示浮动网络与电气地之间的物理电容。该电容阻断直流电流。

### **Parasitic parallel conductance** — 小寄生效应 `0 1/Ohm`（默认）| nonnegative scalar

表示小寄生效应。对于某些电路拓扑的仿真，需要非零值。

## 所属库

Simscape / Foundation Library / Electrical / Electrical Elements Simscape / Electrical / Connectors & References

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

用于测量浮动电气网络中其他节点电压的参考

Floating Reference 模块提供电气参考，可用于测量浮动电气网络中其他节点的电压。

与提供接地连接的 Electrical Reference 模块不同，此模块使用电容来阻断直流电流。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
