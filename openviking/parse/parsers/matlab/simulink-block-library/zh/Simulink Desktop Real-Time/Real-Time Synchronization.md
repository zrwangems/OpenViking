---
type: simulink-block
title: 'Real-Time Sync'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: ''
documentation_page: 'realtimesync'
documentation_source_path: 'ref/realtimesync.html'
language: zh-CN
chinese_source: worker-translation
---

# Real-Time Sync

## 端口

### 输出

### **Missed Ticks** — 错过的节拍计数（可选）double

在 **Connected IO** 模式下，返回模型落后于实时内核的定时器节拍数。当模型落后超过 **Maximum missed ticks** 时，软件报告错误并停止仿真。

#### 依赖

当您选中 **Show “Missed Ticks” port** 时，此端口可见。

**数据类型：** `double`

## 参数

### **Sample time** — 模块的采样时间 `0.1`（默认）| double

输入一个以秒为单位的值，表示您希望模块执行并与 I/O 硬件交互的频率。模块以此采样率将您的模型与实时时钟同步。

如果您使用的是固定步长求解器，请输入您在 **Fixed step size** 配置参数中输入的值或该值的整数倍。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |

### **Maximum missed ticks** — 模型可以落后于内核的定时器节拍数 `10`（默认）| integer

在 **Connected IO** 模式下，输入模型可以落后于实时内核的定时器节拍数。当模型落后此数量或更少的定时器节拍时，软件假定该滞后是暂时的。它允许模型追赶，即使模型错过了一些节拍。当模型落后超过此数量时，软件报告错误并停止仿真。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 编程使用

|  |
| --- |
| **模块参数**：`MaxMissedTicks` |

### **Show “Missed Ticks” port** — 将错过的节拍数发送到端口 `Missed Ticks` `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框以将错过的节拍数发送到输出端口 `Missed Ticks`。

在 **Run in Kernel** 模式下，`Missed Ticks` 端口为零。

#### 编程使用

|  |
| --- |
| **模块参数**：`ShowMissedTicks` |

### **Yield CPU when waiting** — 在内核等待硬件时让出 CPU `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框以在内核等待硬件响应时授予其他程序更多 CPU 时间。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 编程使用

|  |
| --- |
| **模块参数**：`YieldWhenWaiting` |

## 所属库

Simulink Desktop Real-Time

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2012a 中引入**

### R2024b：更新了带端口名称的模块

在 R2024b 中，当您启用可选端口（例如 **Show "Missed Ticks" port**）时，这些 Simulink Desktop Real-Time 模块端口会显示标签。

## 描述

在 Connected IO 模式下将模型执行同步到实时

Real-Time Sync 模块在 Real-Time Sync 模块采样命中时将您的 Simulink® 模型与实时内核时钟同步。参数仅指定采样时间和错过的节拍值。没有输入端口。

Real-Time Sync 模块仅在 **Connected IO** 模式下运行。它在 **Run in Kernel** 模式下没有功能。

如果 **Connected IO** 模式模型包含另一个 Simulink Desktop Real-Time™ 模块，则该另一个模块将 Simulink 模型与实时时钟同步。请勿在此类模型中包含 Real-Time Sync 模块。
