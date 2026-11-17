---
type: simulink-block
title: 'Logic Decision'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'logicdecision'
documentation_source_path: 'ref/logicdecision.html'
language: zh-CN
chinese_source: worker-translation
---

# Logic Decision

## 端口

### 输入

### **wave** — 输入信号 固定步长采样 | 可变步长采样 | 标量

输入信号，指定为浮点标量。输入信号可以继承，也可以由 Logic Decision 模块定义为固定步长离散采样时间。

**数据类型：** `double` | `Boolean`

### **vth** — 判决阈值 标量

判决阈值，指定为标量。**vth** 端口的值决定输入信号何时被延迟固定量。

**数据类型：** `floating point`
### 输出

### **events** — 输出信号 `0` | `1`

输出信号，返回为 `0` 或 `1`。

**数据类型：** `double` | `Boolean`

## 参数

### **Sample time** — 采样时间来源 `Inherited`（默认）| `Fixed`

采样时间来源。

- 选择 `Inherited` 以从上一个模块继承采样时间。
- 选择 `Fixed` 以将离散采样时间设置为固定值。

#### 编程使用

- 使用 `get_param(gcb,'SampleTimeSource')` 查看当前的 **Sample time** 来源。
- 使用 `set_param(gcb,'SampleTimeSource',value)` 将 **Sample time** 设置为特定值。

### **Sample time value** — 采样时间的实际值 `20e-12`（默认）| 非零实数标量

采样时间的实际值，指定为非零实数标量。

#### 依赖关系

要启用此参数，请在 **Sample time** 参数中选择 `Fixed`。

#### 编程使用

- 使用 `get_param(gcb,'SampleTimeIn')` 查看当前的 **Sample time value**。
- 使用 `set_param(gcb,'SampleTimeIn',value)` 将 **Sample time value** 设置为特定值。

### **Minimum delay value** — 最小传播延迟值 `1e-15`（默认）| 正标量

模块的最小传播延迟，指定为正标量。对于固定离散输入采样时间，实际延迟为此参数值与固定步长的最大值。

#### 编程使用

- 使用 `get_param(gcb,'Delay')` 查看当前的 **Minimum delay value**。
- 使用 `set_param(gcb,'Delay',value)` 将 **Minimum delay value** 设置为特定值。

### **Buffer size** — 要缓冲的阈值穿越次数 `1`（默认）| 正整数标量

可存储在模块中的待处理输出事件数，指定为正整数标量。

#### 编程使用

- 使用 `get_param(gcb,'BufferSizeIn')` 查看当前的 **Buffer size**。
- 使用 `set_param(gcb,'BufferSizeIn',value)` 将 **Buffer size** 设置为特定值。

## 所属库

Mixed-Signal Blockset / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

二进制过程输入端的阈值穿越检测器

Logic Decision 模块在输入信号穿越判决阈值几乎精确时刻起，经过固定延迟后产生输出事件。此模块有助于从均匀采样输入波形过渡到事件驱动数字逻辑子系统。
