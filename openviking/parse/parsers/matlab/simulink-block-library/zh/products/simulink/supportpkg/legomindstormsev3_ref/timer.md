---
type: simulink-block
title: 'Timer'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Control Blocks'
documentation_page: 'timer'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/timer.html'
language: zh-CN
chinese_source: worker-translation
---

# Timer

## 端口

### 输出

### **time** — 从运行 Simulink 模型起经过的时间（标量）

该模块输出 EV3 程序块开始运行 Simulink 模型后经过的时间，单位为毫秒。

**数据类型：** `uint32`

## 参数

### **采样时间** — 模块读取定时器值的时间间隔 `0.1`（默认）| 正整数

指定模块读取定时器值的频率。较短的采样时间（例如 `0.01`）可能会产生不可靠的测量结果。

较小的采样时间要求处理器在更短的时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2012a 中引入**

## 描述

测量 EV3 程序块中定时器经过的时间

使用 Timer 模块测量 EV3 程序块开始运行 Simulink® 模型后经过的时间，单位为毫秒。

通过观察 EV3 程序块上的 LCD，可以了解 EV3 程序块何时开始运行模型。对于不使用 Display 模块的 Simulink 模型，EV3 程序块上的 LCD 会显示 `I am running`，后跟模型名称。对于使用 Display 模块的模型，模型会显示发送给它的任何输出。

在没有硬件的情况下进行仿真时，此模块输出零。请参阅“模块在仿真中产生零或不执行任何操作”。
