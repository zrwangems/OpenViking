---
type: simulink-block
title: 'C28x CLA Task'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / System Peripherals / CLA, Watchdog, Timer'
documentation_page: 'c28xclatask'
documentation_source_path: 'ref/c28xclatask.html'
language: zh-CN
chinese_source: official
---

# C28x CLA Task

## 端口

### 输出

### **Port\_1** — 向函数调用子系统或函数调用模型发送函数调用信号 标量

输出触发 CLA 任务，该任务在 CLA 核心上执行下游函数调用子系统。

## 参数

### **CLA 任务编号** — 在 CLA 核心上执行的 CLA 任务编号 `1` (默认) | [1, 8] 范围内的整数

要在 CLA 核心上执行的 CLA 任务编号。

### **CLA 任务触发器源** — CLA 任务触发器源 `Software` (默认) | 外设中断

触发 CLA 任务在 CLA 内核上执行的软件或外设中断源。

### **等到任务完成** — 阻止 C28x 执行，直到 CLA 任务完成。 `off` (默认) | on

选择参数 **Wait until completion of task**，作为触发 CLA 任务的软件源。

启用此功能将暂停 C28x 的执行，直到所有待处理的 CLA 任务完成。

#### 依赖关系

要启用此参数，请将 **CLA task trigger source** 参数设置为 `software`。

### **采样时间** — 函数调用子系统触发的频率 `0.2` (默认) | `-1` | 标量

设置 **CLA task trigger source** 触发函数调用子系统的频率。要异步执行此模块，请将此参数设置为 `-1`。

#### 依赖关系

要启用此参数，请在 **CLA task trigger source** 中选择**软件**选项。

## 所属库

C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2016b 中推出**

## 描述

创建 CLA 任务，该任务在 CLA 核心上执行下游函数调用子系统。

CLA Task 模块创建一个（控制律加速器）CLA 任务，该任务在 CLA 内核上执行下游函数调用子系统。CLA 是一种支持并行处理的协处理器。利用 CLA 处理时间紧迫的任务，可以释放主 CPU 以同时执行其他系统和通信功能。

您可以指定中断源来触发 CLA 任务。您可以创建最多八个 CLA 任务，在 CLA 核心上执行。

有关如何配置 CLA 模块以执行下游函数调用子系统的信息，请参阅 Overview of CLA Configuration for C2000 Processors Using Subsystem。

**注意**

并非所有 TI C2000 硬件板型号都支持 CLA。例如，在 TI Piccolo F2805x 处理器系列中，只有 F28055 和 F28053 处理器支持 CLA，而 F28054、F28052、F28051 和 F28050 处理器不支持 CLA。
