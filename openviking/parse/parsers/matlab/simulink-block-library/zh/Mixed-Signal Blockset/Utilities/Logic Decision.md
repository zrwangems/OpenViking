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

### **wave** — 输入信号，固定步长采样 | 可变步长采样 | 标量

输入信号，指定为 floating point 标量。输入信号既可以继承，也可以由 Logic Decision 模块定义为固定步长离散采样时间。

**数据类型：** `double` | `Boolean`

### **vth** — 判决阈值，标量

判决阈值，指定为标量。**vth** 端口处的值决定输入信号何时被延迟一个固定量。

**数据类型：** `floating point`

### 输出

### **events** — 输出信号 `0` | `1`

输出信号，返回为 `0` 或 `1`。

**数据类型：** `double` | `Boolean`

## 参数

### **采样时间** — 采样时间的源 `Inherited`（默认） | `Fixed`

采样时间的源。

- 选择 `Inherited`，以从上一个模块继承采样时间。
- 选择 `Fixed`，以将离散采样时间设置为固定值。

#### 编程用法

- 使用 `get_param(gcb,'SampleTimeSource')` 查看 **采样时间** 的当前源。
- 使用 `set_param(gcb,'SampleTimeSource',value)` 将 **采样时间** 设置为特定值。

### **采样时间值** — 采样时间的实际值 `20e-12`（默认） | 非零实数标量

采样时间的实际值，指定为非零实数标量。

#### 依赖关系

要启用此参数，请在 **采样时间** 参数中选择 `Fixed`。

#### 编程用法

- 使用 `get_param(gcb,'SampleTimeIn')` 查看当前 **采样时间值**。
- 使用 `set_param(gcb,'SampleTimeIn',value)` 将 **采样时间值** 设置为特定值。

### **最小延迟值** — 最小传播延迟值 `1e-15`（默认） | 正标量

模块的最小传播延迟，指定为正标量。对于固定的离散输入采样时间，实际延迟是该参数值与固定步长的最大值。

#### 编程用法

- 使用 `get_param(gcb,'Delay')` 查看当前 **最小延迟值**。
- 使用 `set_param(gcb,'Delay',value)` 将 **最小延迟值** 设置为特定值。

### **缓冲区大小** — 要缓冲的阈值穿越次数 `1`（默认） | 正整数标量

可存储在模块中的待处理输出事件数，指定为正整数标量。

#### 编程用法

- 使用 `get_param(gcb,'BufferSizeIn')` 查看当前 **缓冲区大小**。
- 使用 `set_param(gcb,'BufferSizeIn',value)` 将 **缓冲区大小** 设置为特定值。

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

Logic Decision 模块会在输入信号穿越判决阈值几乎准确的时刻之后，以固定延迟产生输出事件。此模块有助于从均匀采样的输入波形过渡到事件驱动的数字逻辑子系统。
