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
```yaml
ports:
- name: u
  summary: 数据输入信号 标量 | 向量
  direction: input
- name: d
  summary: 延迟长度 标量 | 向量
  direction: input
- name: Port_1
  summary: 输出信号 标量 | 向量
  direction: output
```

### 输入

### **u** — 数据输入信号 标量 | 向量

根据参数设置进行延迟的输入数据信号。

当您使用 **Fixed delays (indices)** 参数将信号延迟指定为固定延迟，并为 **Nominal delay** 参数指定值 `0` 时，此端口具有直接馈通。

### **d** — 延迟长度 标量 | 向量

指定为标量或向量的瞬时延迟长度输入。此值用于指定变化的延迟。该模块将任何负输入值视为零。

当延迟长度输入为非整数值时，该模块将该值舍入为最接近的整数。
### 输出

### **Port\_1** — 输出信号 标量 | 向量

指定为标量或向量的输出信号。
## 参数
```yaml
parameters:
- name: Nominal delay (number of samples)
  summary: 延迟的标称值 1 （默认） | 非负整数 | 非负整数值向量
  group: ''
- name: Maximum delay
  summary: 延迟长度输入的最大值 10 （默认） | 非负整数 | 非负整数值向量
  group: ''
- name: Fixed delays (indices)
  summary: 具有固定延迟的信号索引 [] （默认） | 正标量 | 正值向量
  group: ''
- name: Initial output
  summary: 初始输出 0 （默认） | 标量 | 向量
  group: ''
- name: Sample time (-1 for inherited)
  summary: 采样时间 -1 （默认） | 正标量
  group: ''
- name: Prevent direct feedthrough with minimum delay of 1
  summary: 防止直接馈通 off （默认） | on
  group: ''
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Nominal delay (number of samples)** — 延迟的标称值 1 （默认） | 非负整数 | 非负整数值向量

将延迟的标称值指定为采样数。

### **Maximum delay** — 延迟长度输入的最大值 `10` （默认） | 非负整数 | 非负整数值向量

设置时间延迟输入的最大值。此值定义该模块允许的最大延迟长度输入。该模块会裁剪任何超过此值的延迟。

### **Fixed delays (indices)** — 具有固定延迟的信号索引 `[]` （默认） | 正标量 | 正值向量

指定延迟固定的输入信号通道的索引。例如，如果您有一个 4×1 输入信号，并且想要在第一和第四通道中指定固定延迟，请为此参数使用值 `[1 4]`。该模块使用 **Nominal delay** 参数对应索引处指定的值。

当您将所有通道都列为固定通道时，该模块会禁用第二个输入端口 **Port\_2**。

### **Initial output** — 初始输出 `0` （默认） | 标量 | 向量

对于每个输入通道，指定在仿真时间首次超过该通道的时间延迟之前的输出值。

### **Sample time (-1 for inherited)** — 采样时间 `-1` （默认） | 正标量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。该模块支持离散采样时间，但不支持连续采样时间。

### **Prevent direct feedthrough with minimum delay of 1** — 防止直接馈通 `off` （默认） | `on`

选择此项可将最小延迟长度从零增加到 1。

选中此复选框可防止从输入端口 **u** 到输出端口的直接馈通。
## 所属库

Control System Toolbox / Linear Parameter Varying

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

支持固定延迟和零延迟（直接馈通）的离散变化延迟

Discrete Varying Delay 模块扩展了 `Simulink` / `Discrete` 库中 Variable Integer Delay (Simulink) 模块的功能，提供了对指定固定延迟和零延迟的额外支持。当您想要对零延迟、固定延迟和变化延迟的混合进行建模时，此模块非常有用，这种情况可能出现在 LPV 模型中。
