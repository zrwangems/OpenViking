---
type: simulink-block
title: 'Event-Count Comparator'
family: 'signal-management'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Management / Switches and Counters'
documentation_page: 'eventcountcomparator'
documentation_source_path: 'ref/eventcountcomparator.html'
language: zh-CN
chinese_source: worker-translation
---

# Event-Count Comparator

## 端口

### 输入

### **Data** — 数据输入标量

将数据输入指定为离散时间标量。

Event-Count Comparator 模块接受实数和复数浮点及定点输入。然而，由于该模块具有离散状态，因此不支持常量或连续采样时间。因此，必须将 Event-Count Comparator 模块的至少一个输入端口或输出端口连接到 **Sample time** 参数为离散的模块。Event-Count Comparator 模块继承此非无限离散采样时间。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`
**复数支持：** Yes

### **Int** — 区间使能信号标量

将区间使能信号指定为标量。此端口处的非零输入使模块开始计数并重置输出。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`
### 输出

### **Out** — 检测所需数量的非零输入 `true` 或 `1` | `false` 或 `0`

如果随时间累积的非零输入数量等于或超过您在 **Event threshold** 参数中指定的值，则该模块返回逻辑 `1`。

**数据类型：** `Boolean`

## 参数

### **Event threshold** — 事件阈值 `10`（默认） | 非负整数

将事件阈值指定为非负整数。该模块将非零输入的数量与此值进行比较。如果随时间累积的非零输入数量等于或超过您在此参数中指定的值，则该模块返回逻辑 `1`。

**可调：** Yes

## 所属库

DSP System Toolbox / Signal Management / Switches and Counters

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

检测累积非零输入的阈值穿越

Event-Count Comparator 模块在 **Int** 端口的高信号（值为 `1`）使能该模块的期间，检测 **Data** 端口处非零输入的数量。两个输入都必须为标量。

当累积非零输入的数量首次等于 **Event threshold** 参数中的值时，该模块额外等待一个采样区间，然后将 **Out** 端口设置为 `1`。该模块将 **Out** 端口保持为 `1`，直到 **Int** 端口的信号从低值（`0`）跳变到高值（`1`）。
