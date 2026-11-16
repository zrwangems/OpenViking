---
type: simulink-block
title: 'Floating Reference'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Elements'
documentation_page: 'floatingreference'
documentation_source_path: 'ref/floatingreference.html'
language: zh-CN
chinese_source: worker-translation
---

# Floating Reference

## 端口

### 守恒

### **n** — 直流电流为零的电气端口

直流电流为零的电气守恒端口。使用此端口可测量浮置电气网络中其他节点的电压。

## 参数

### **电容** — 阻断直流电流的电容 `1 uF`（默认值）| 正标量

表示浮置网络与电气接地之间的物理电容。该电容会阻断直流电流。

### **寄生并联电导** — 微小寄生效应 `0 1/Ohm`（默认值）| 非负标量

表示微小的寄生效应。对于某些电路拓扑，仿真时需要使用非零值。

## 所属库

Simscape / Foundation Library / Electrical / Electrical Elements Simscape / Electrical / Connectors & References

## 模块特性

R2025b 中未提供相关文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中推出**

## 描述

用于测量浮置电气网络中其他节点电压的参考

Floating Reference 模块提供了一个电气参考，可用于测量浮置电气网络中其他节点的电压。

与提供接地连接的 Electrical Reference 模块不同，此模块使用电容来阻断直流电流。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅“设置模块变量的优先级和初始目标”。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真的鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅“修改模块变量的标称值”。
