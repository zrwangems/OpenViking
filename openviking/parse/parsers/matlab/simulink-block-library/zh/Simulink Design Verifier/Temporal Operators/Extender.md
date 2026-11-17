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
chinese_source: worker-translation
---

# Extender

## 端口

### 输入

### **Port\_1** — 输入信号，指定为 boolean boolean

Extender 模块的输入为 boolean 类型。

**数据类型：** `Boolean`
### 输出

### **Port\_1** — 输出信号，返回为 boolean boolean

Extender 模块的输出为 boolean 类型。

**数据类型：** `Boolean`

## 参数

### **External reset** — 指定模块是否可以被复位 off（默认）| on

指定外部 Boolean 复位信号是否可以复位模块的扩展。该复位信号还会复位无限扩展。带外部复位的无限扩展是一种不定扩展，直到外部复位信号变为 `true`。

### **Extension Period** — 指定扩展的固定时间步数 `Finite`（默认）| `Infinite`

选择 `Finite`（默认）以指定扩展的固定时间步数。选择 `Infinite` 以指定不定扩展。

### **Time steps for extension** — 指定用于延长 true 持续时间的时间步数 3（默认）| boolean

对于有限扩展，指定用于延长 true 持续时间的时间步数（最小值为 `1`）。

## 所属库

Simulink Design Verifier / Temporal Operators

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2011a 中引入**

## 描述

延长输入的 true 持续时间

Extender 模块将输入信号的 true 持续时间延长固定步数（有限扩展模式）或无限延长。

信号的 *true 持续时间* 是指信号为 `true` 的连续时间步。
