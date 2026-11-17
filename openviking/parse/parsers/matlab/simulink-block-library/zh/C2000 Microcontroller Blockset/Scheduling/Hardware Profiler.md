---
type: simulink-block
title: 'Hardware Profiler'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Scheduling'
documentation_page: 'hardwareprofiler'
documentation_source_path: 'ref/hardwareprofiler.html'
language: zh-CN
chinese_source: worker-translation
---

# Hardware Profiler

## 端口

### 输出

### **f()** — 函数调用端口 标量

将函数调用子系统连接到此端口。当子系统执行时，将使用选定的测量技术对其进行性能分析。

### **cnt** — 计数端口 标量

以周期数显示执行时间。

#### 依赖关系

要启用此端口，请将 **Measurement mode** 参数设置为 `Embedded Real-time Analysis & Diagnostic (ERAD)` 或 `Timer`。

**数据类型：** `uint32`

## 参数

### **Measurement mode** — 选择硬件性能分析技术 `Embedded Real-time Analysis & Diagnostic (ERAD)`（默认）| `General Purpose Input Output (GPIO)` | `Timer`

选择用于对目标硬件上的函数调用子系统进行性能分析的测量技术。

- **ERAD**：测量并分析从起始到结束的下游函数调用子系统的执行时间。
- **GPIO**：利用 GPIO 引脚在执行下游函数调用子系统之前和之后设置和清除信号。
- **Timer Measurement**：使用定时器，通过计算执行前和执行后定时器计数之间的持续时间来测量执行时间。当您选择 Time Measurement 时，Timer 2 用于基于定时器的性能分析。

### **ERAD module** — 指定 ERAD 模块 `1`（默认）| `2` | `3` | `4`

指定 ERAD 模块。ERAD 模块由 ERAD 计数器和 2 个 ERAD 断点组成。当您选择 ERAD 模块时，该模块在函数开始和结束处放置断点，并测量两个断点之间执行的时钟周期数。

- `Module 1` - ERAD 计数器 1 以及 ERAD 断点 1 和 2。
- `Module 2` - ERAD 计数器 2 以及 ERAD 断点 3 和 4。
- `Module 3` - ERAD 计数器 3 以及 ERAD 断点 5 和 6。
- `Module 4` - ERAD 计数器 4 以及 ERAD 断点 7 和 8。

**注意**

ERAD 模块仅在选定的 TI 处理器中可用。

#### 依赖关系

要启用此参数，请将 **Measurement mode** 参数设置为 `Embedded Real-time Analysis & Diagnostic (ERAD)`。

### **GPIO number** — 指定 GPIO 编号 `0`（默认）

指定该模块的 GPIO 编号。

#### 依赖关系

要启用此参数，请将 **Measurement mode** 参数设置为 `General Purpose Input Output (GPIO)`。

### **Sample time** — 模块从硬件性能分析器读取数据的采样时间 `-1`（默认）

Hardware Profiler 模块触发下游函数调用子系统的采样时间。

使用此参数指定 2 次函数调用触发之间的时间间隔。计数数据也会在所述的采样时间更新。要继承采样时间，请将此参数设置为 -1。

## 所属库

C2000 Microcontroller Blockset / Scheduling

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024b 中引入**

## 描述

使用 GPIO、ERAD 或 Timer 测量模式对函数调用子系统进行性能分析

Hardware Profiler 模块使您能够使用通用输入输出（GPIO）、嵌入式实时分析与诊断（ERAD）以及定时器测量模式，对目标硬件上的函数调用子系统进行性能分析。

- **ERAD：** 测量并分析从起始到结束的下游函数调用子系统的执行时间。
- **GPIO：** 在执行下游函数调用子系统之前和之后设置和清除 GPIO 引脚。
- **Timer：** 通过计算执行前和执行后定时器计数之间的持续时间来测量事件的执行时间。

这些技术使您能够准确地对在 TI C2000 处理器上运行的代码进行性能分析和优化。

采用 Timer 和 ERAD 模式的 **Hardware Profiler** 模块以时钟周期为单位提供输出。要将其转换为秒，请使用以下公式：

**注意**

处于 ERAD 测量模式的 Hardware Profiler 模块始终提供最大执行时间。
