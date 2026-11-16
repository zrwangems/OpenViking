---
type: simulink-block
title: 'Detector'
family: 'sldv'
product_id: 'sldv'
product_name: 'Simulink Design Verifier'
documentation_release: R2025b
official_category: 'Temporal Operators'
documentation_page: 'detector'
documentation_source_path: 'ref/detector.html'
language: zh-CN
chinese_source: official
---

# Detector

## 端口

### 输入

### **Port\_1** — 输入信号指定为布尔值 布尔

Detector 模块的输入是布尔类型。

**数据类型:** `Boolean`
### 输出

### **Port\_1** — 输出信号以布尔值形式返回 布尔

Detector 模块的输出是布尔类型。

**数据类型:** `Boolean`

## 参数

### **外部重置** — 是否可以重置模块 off (默认) | on

指定是否可以通过外部布尔重置信号将模块重置为输入检测的起始状态。

### **输出类型** — 为输出指定固定的 true 持续期长度 `Delayed fixed duration` (默认) | `Synchronized`

选择**延迟固定持续期**（默认值）可在经过（可选）延迟后为输出指定固定 true 持续期长度。选择**同步**可将输出为 true 的持续期与输入为 true 的持续期同步。

### **输入检测时间步数** — 输入检测的 ture 持续期的长度 `2` (默认) | 布尔

输入检测的 ture 持续期的长度（最小值为 **1**）。

### **延迟时间步** — 指定延迟持续期的长度 `1` (默认) | 布尔

对于**延迟固定持续期**，可以选择指定延迟持续期的长度，此时间长度结束后输出将变为 true。

### **输出持续期时间步数** — 指定输出为 true 的持续期的长度 `3` (默认) | 布尔

对于**延迟固定持续期**，指定输出为 true 的持续期的长度（最小值为 **1**）。

## 所属库

Simulink Design Verifier / Temporal Operators

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2011a 中推出**

## 描述

检测输入为 true 的持续期并基于输出类型构造输出为 true 的持续期

此模块检测输入信号为 true 的固定数量的连续时间步，并基于所选输出类型构造输出信号。用于解释检测器模块的术语如下：

- 信号的 *true 持续期* - 信号为 true 的连续时间步
- 信号的 true 持续期的*长度* - 构成 true 持续期的时间步数
- *输入检测*阶段 - 在预期长度的输入为 true 的持续期的最终时间步完成的阶段
- *输出构造*阶段 - 模块基于模块的输出类型在输出端构造 true 持续期的阶段
- *延迟持续期* - 输入检测后的延迟时间步数，在此之后输出信号为 true

在输入检测时，Detector 模块会基于您指定的以下两种输出类型之一构造输出信号：

- **延迟固定持续期** - 在完成输入检测并在一定的（可选）延迟后，输出信号会变为 `true` 并持续固定数量的时间步。输出的 true 持续期与输入无关。
- **同步** - 在输入检测的最终时间步中，输出变为 `true`，并且只要输入信号继续为 `true`，输出就会保持为 `true`。输出的 true 持续期会发生变化，并与输入的 true 持续期同步。
