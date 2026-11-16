---
type: simulink-block
title: 'Discrete Varying Delay'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Linear Parameter Varying'
documentation_page: 'discretevaryingdelay'
documentation_source_path: 'ref/discretevaryingdelay.html'
language: zh-CN
chinese_source: worker-translation
---

# Discrete Varying Delay

## 端口

### 输入

### **u** — 数据输入信号 标量 | 向量

根据参数设置进行延迟的输入数据信号。

当你使用 **固定延迟（索引）** 参数将信号延迟指定为固定，并且为 **标称延迟** 参数指定值 `0` 时，此端口具有直接馈通。

### **d** — 延迟长度 标量 | 向量

瞬时延迟长度输入，指定为标量或向量。此值用于指定变化的延迟。模块将任何负输入值视为零。

当延迟长度输入为非整数值时，模块会将该值舍入到最接近的整数。

### 输出

### **Port\_1** — 输出信号 标量 | 向量

输出信号，指定为标量或向量。

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### **标称延迟（样本数）** — 延迟的标称值 `1`（默认） | 非负整数 | 非负整数值向量

以样本数指定延迟的标称值。

### **最大延迟** — 延迟长度输入的最大值 `10`（默认） | 非负整数 | 非负整数值向量

设置时间延迟输入的最大值。此值定义此模块允许的最大延迟长度输入。模块会裁剪超过此值的任何延迟。

### **固定延迟（索引）** — 具有固定延迟的信号索引 `[]`（默认） | 正标量 | 正值向量

指定延迟固定的输入信号通道的索引。例如，如果你有一个 4×1 输入信号，并且想要在第一个和第四个通道中指定固定延迟，请为此参数使用值 `[1 4]`。模块使用 **标称延迟** 参数对应索引处指定的值。

当你将所有通道都列出为固定时，模块会禁用第二个输入端口 **Port\_2**。

### **初始输出** — 初始输出 `0`（默认） | 标量 | 向量

对于每个输入通道，指定在仿真时间首次超过该通道的时间延迟之前的输出值。

### **采样时间（-1 表示继承）** — 采样时间 `-1`（默认） | 正标量

指定样本之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。此模块支持离散采样时间，但不支持连续采样时间。

### **使用最小延迟 1 防止直接馈通** — 防止直接馈通 `off`（默认） | `on`

选中此项可将最小延迟长度从零增加到 1。

选中此复选框可防止从输入端口 **u** 到输出端口的直接馈通。

## 所属库

Control System Toolbox / Linear Parameter Varying

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2024a 中引入**

## 描述

支持固定延迟和零延迟（直接馈通）的离散变化延迟

Discrete Varying Delay 模块通过提供对指定固定延迟和零延迟的额外支持，扩展了 `Simulink` / `Discrete` 库中 Variable Integer Delay (Simulink) 模块的功能。当你想要对零延迟、固定延迟和变化延迟的混合进行建模时（这可能出现在 LPV 模型中），此模块会很有用。
