---
type: simulink-block
title: 'Extender'
family: 'sldv'
product_id: 'sldv'
product_name: 'Simulink Design Verifier'
documentation_release: R2025b
official_category: 'Temporal Operators'
documentation_page: 'extender'
documentation_source_path: 'ref/extender.html'
language: zh-CN
chinese_source: official
---

# Extender

## 端口

### 输入

### **Port\_1** — 输入信号指定为布尔值 布尔

Extender 模块的输入是布尔类型。

**数据类型:** `Boolean`
### 输出

### **Port\_1** — 输出信号以布尔值形式返回 布尔

Extender 模块的输出是布尔类型。

**数据类型:** `Boolean`

## 参数

### **外部重置** — 指定是否可以重置模块 off (默认) | on

指定外部布尔重置信号是否可以重置模块延长。重置信号还会重置无限延长模式。带外部重置的无限延长是指延长到外部重置信号变为 `true` 的不定延长。

### **延长期** — 指定延长的固定时间步数 **有限** (默认) | **无限**

选择**有限**（默认值）可指定延长的固定时间步数。选择**无限**可指定不定延长。

### **延长时间步数** — 指定延长 true 持续期的时间步数 3 (默认) | 布尔

对于有限延长，指定延长 true 持续期的时间步数（最小值为 `1`）。

## 所属库

Simulink Design Verifier / Temporal Operators

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2011a 中推出**

## 描述

延长输入的 true 持续期

Extender 模块将输入信号为 true 的持续期延长固定步数（有限延长模式）或无限延长。

信号的 *true 持续期*是信号为 `true` 的连续时间步数。
