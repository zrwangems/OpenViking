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
chinese_source: worker-translation
---

# Detector

## 端口

### 输入

### **Port\_1** — 指定为 boolean 的输入信号 boolean

Detector 模块的输入为 boolean 类型。

**数据类型：** `Boolean`
### 输出

### **Port\_1** — 返回为 boolean 的输出信号 boolean

Detector 模块的输出为 boolean 类型。

**数据类型：** `Boolean`

## 参数

### **External reset** — 模块是否可以被复位 off（默认）| on

指定模块是否可以通过外部 Boolean 复位信号复位到输入检测的开始处。

### **Output type** — 为输出指定固定的 true 持续时间长度 `Delayed fixed duration`（默认）| `Synchronized`

选择 `Delayed Fixed Duration`（默认），以在可选延迟之后为输出指定固定的 true 持续时间长度。
选择 `Synchronized`，以将输出的 true 持续时间与输入的 true 持续时间同步。

### **Time steps for input detection** — 输入检测的 true 持续时间长度 `2`（默认）| boolean

输入检测的 true 持续时间长度（最小为 `1`）。

### **Time steps for delay** — 指定延迟持续时间的长度 `1`（默认）| boolean

对于 `Delayed Fixed Duration`，可选地指定延迟持续时间的长度，在此之后输出变为 true。

### **Time steps for output durations** — 指定输出 true 持续时间的长度 `3`（默认）| boolean

对于 `Delayed Fixed Duration`，指定输出 true 持续时间的长度（最小为 `1`）。

## 所属库

Simulink Design Verifier / Temporal Operators

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2011a 中引入**

## 描述

检测输入上的 true 持续时间，并根据输出类型构造输出 true 持续时间

此模块检测输入信号为 true 的固定数量的连续时间步，并根据所选的输出类型构造输出信号。用于解释 detector 模块的术语如下：

- 信号的 *True duration* — 信号为 true 的连续时间步
- 信号 true 持续时间的 *Length* — 构成 true 持续时间的时间步数
- *Input detection* 阶段 — 在输入 true 持续时间预期长度的最后一个时间步完成的阶段
- *Output construction* 阶段 — 模块根据其输出类型在输出端构造 true 持续时间的阶段
- *Delay duration* — 输入检测之后的延迟时间步数，在此之后输出信号为 true

在输入检测时，Detector 模块根据您指定的两种输出类型之一构造输出信号：

- `Delayed Fixed Duration` — 在输入检测完成之后，并在可选延迟之后，输出信号在固定数量的时间步内变为 `true`。输出的 true 持续时间与输入无关。
- `Synchronized` — 在输入检测的最后一个时间步，输出变为 `true`，并且只要输入信号继续为 `true`，输出就保持 `true`。输出的 true 持续时间会变化，并与输入的 true 持续时间同步。
