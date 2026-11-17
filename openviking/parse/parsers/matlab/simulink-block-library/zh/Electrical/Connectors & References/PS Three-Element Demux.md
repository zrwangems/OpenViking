---
type: simulink-block
title: 'PS Three-Element Demux'
family: 'simscape'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Physical Signals / Nonlinear Operators'
documentation_page: 'psthreeelementdemux'
documentation_source_path: '../simscape/ref/psthreeelementdemux.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Three-Element Demux

## 端口
```yaml
ports:
- name: abc
  summary: 三元素物理信号，无量纲物理信号
  direction: input
- name: a
  summary: 标量物理信号，无量纲物理信号
  direction: output
- name: b
  summary: 标量物理信号，无量纲物理信号
  direction: output
- name: c
  summary: 标量物理信号，无量纲物理信号
  direction: output
```

### 输入

### **abc** — 三元素物理信号，无量纲物理信号

物理信号输入端口，信号为三元素行向量。

### 输出

### **a** — 标量物理信号，无量纲物理信号

标量物理信号输出端口。

### **b** — 标量物理信号，无量纲物理信号

标量物理信号输出端口。

### **c** — 标量物理信号，无量纲物理信号

标量物理信号输出端口。
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Simscape / Foundation Library / Physical Signals / Nonlinear Operators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2023b: 模块在 Foundation 库中可用

在 R2023b 之前，此模块是 Simscape™ Electrical™ 产品的一部分。它被称为 Three Element Demux，并且仅在 Simscape/Electrical/Connectors & References 库中可用。

此更改没有兼容性影响。模块功能未改变。如果您打开包含 Three Element Demux 模块的现有模型，它将自动更新为使用 Foundation 库中的 PS Three-Element Demux 模块。

## 描述

将三元素物理信号向量转换为标量物理信号

PS Three-Element Demux 模块将三元素物理信号向量拆分为三个标量物理信号。
