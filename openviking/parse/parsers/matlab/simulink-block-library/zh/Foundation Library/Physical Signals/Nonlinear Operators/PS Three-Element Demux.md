---
type: simulink-block
title: 'PS Three-Element Demux'
family: 'physical-signals'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Nonlinear Operators'
documentation_page: 'psthreeelementdemux'
documentation_source_path: 'ref/psthreeelementdemux.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Three-Element Demux

## 端口

### 输入

### **abc** — 三元素物理信号，无单位物理信号

物理信号输入端口，该信号为三元素行向量。

### 输出

### **a** — 标量物理信号，无单位物理信号

标量物理信号输出端口。

### **b** — 标量物理信号，无单位物理信号

标量物理信号输出端口。

### **c** — 标量物理信号，无单位物理信号

标量物理信号输出端口。

## 参数

在 R2025b 中未提供文档。

## 所属库

Simscape / Foundation Library / Physical Signals / Nonlinear Operators

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中推出**

### R2023b: 模块在 Foundation 库中可用

在 R2023b 之前，此模块属于 Simscape™ Electrical™ 产品。它称为 Three Element Demux，并且仅在 Simscape/Electrical/Connectors & References 库中提供。

此更改对兼容性没有影响。模块功能保持不变。如果打开包含 Three Element Demux 模块的现有模型，该模块将自动更新为使用 Foundation 库中的 PS Three-Element Demux 模块。

## 描述

将三元素物理信号向量转换为标量物理信号

PS Three-Element Demux 模块将三元素物理信号向量拆分为三个标量物理信号。
