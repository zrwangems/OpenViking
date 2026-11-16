---
type: simulink-block
title: 'Execution Profiler'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Utilities'
documentation_page: 'executionprofiler'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/executionprofiler.html'
language: zh-CN
chinese_source: worker-translation
---

# Execution Profiler

## 端口

### 输出

### **f()** — 函数调用端口标量

将函数调用子系统连接到此端口。当该子系统执行时，将使用所选的测量技术对其进行分析。

### **cnt** — 计数端口标量

显示以周期数表示的执行时间。

#### 依赖关系

要启用此端口，请将 **测量模式** 参数设置为 `Data Watchpoint Trace (DWT) Timer` 或 `Timer`。

**数据类型：** `uint32`

## 参数

### **测量模式** — 选择执行分析技术 `Data Watchpoint Trace (DWT) Timer`（默认） | `Digital Port Write (GPIO)` | `Timer`

选择用于在目标硬件上分析函数调用子系统的测量技术。

- **Data Watchpoint Trace (DWT) Timer**：
  测量并分析从起始到结束的下游函数调用子系统的执行时间。
- **Digital Port Write (GPIO)**：利用 GPIO 引脚在执行下游函数调用子系统之前和之后设置和清除信号。
- **Timer**：使用定时器，通过计算执行前与执行后定时器计数之间的持续时间来测量执行时间。选择 **Timer** 测量时，使用 `Timer 2` 进行基于定时器的分析。

### **GPIO 端口名称** — 指定 GPIO 端口名称 `GPIOC`（默认） | `GPIOA` | `GPIOB` | `…`

指定模块的 GPIO 端口名称。

#### 依赖关系

要启用此参数，请将 **测量模式** 参数设置为 `Digital Port Write (GPIO)`。

### **GPIO 引脚编号** — 指定 GPIO 引脚编号 `0`（默认）

指定模块的 GPIO 引脚编号。

#### 依赖关系

要启用此参数，请将 **测量模式** 参数设置为 `Digital Port Write (GPIO)`。

### **定时器模块** — 选择定时器模块 `TIM2`（默认） | `TIM1` | `TIM3` | `...`

选择模块的定时器模块。

#### 依赖关系

要启用此参数，请将 **测量模式** 参数设置为 `Timer`。

### **采样时间** — 模块从执行分析器读取数据的采样时间 `1`（默认）

**Execution Profiler** 模块触发下游函数调用子系统时的采样时间。

使用此参数指定 2 次函数调用触发之间的时间间隔。计数数据也会在上述采样时间更新。要继承采样时间，请将此参数设置为 -1。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2025a 中引入**

## 描述

使用 DWT Timer、GPIO 或 Timer 测量模式分析函数的执行时间

**Execution Profile** 模块使您能够使用 Data Watchpoint Trace (DWT) Timer、GPIO 或 Timer 测量模式来分析函数的执行时间。

- **DWT Timer：** 通过在函数的开始和结束处记录周期计数来测量任务时序。
- **GPIO：** 在执行下游函数调用子系统之前和之后设置和清除 GPIO 引脚。
- **Timer：** 通过计算执行前与执行后定时器计数之间的持续时间来测量事件的执行时间。

这些技术使您能够准确分析并优化在 STM32 处理器上运行的代码性能。
