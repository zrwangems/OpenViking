---
type: simulink-block
title: 'Asynchronous Task Specification'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Architecture and Component Design / Timers and Scheduling / Event-Based Scheduling'
documentation_page: 'asynchronoustaskspecification'
documentation_source_path: 'ref/asynchronoustaskspecification.html'
language: zh-CN
chinese_source: official
---

# Asynchronous Task Specification

## 端口

### 输入

### **Port\_1** — 中断输入信号 标量

从根级 Inport 模块接收的中断输入信号。
### 输出

### **Port\_1** — 具有优先级的中断信号 标量

触发函数调用子系统的具有指定任务优先级的中断信号。

## 参数

### **任务优先级** — 调用函数调用子系统的异步任务的优先级 `10` (默认)

指定一个整数或 [] 作为调用所连接的函数调用子系统的异步任务的优先级。优先级必须为可产生相关速率转换行为的值。

- 如果指定一个整数，它必须与父模型中的中断信号发起方的优先级值匹配。
- 如果您指定 []，则优先级不必与顶层模型中的中断信号发起方的优先级匹配。速率转换算法是保守算法（未优化）。优先级未知，但为静态。

假定有以下模型。

引用模型具有以下内容。

如果**任务优先级**参数设置为 10，则父模型中的 Async Interrupt 模块的优先级也必须为 10。如果参数设置为 []，Async Interrupt 模块的优先级可以是 10 以外的值。

## 所属库

Simulink Coder / Asynchronous

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2011a 中推出**

## 描述

指定由异步中断触发的引用模型表示的异步任务的优先级

Asynchronous Task Specification 模块指定异步任务的参数，如任务优先级。异步任务由带异步中断触发器的函数调用子系统表示。此模块用于控制带异步事件触发器的函数调用子系统的调度。您可以通过为引用模型中的每个函数调用子系统分配优先级来控制调度。

要使用此模块，请按照Convert Asynchronous Subsystem to a Referenced Model中的过程进行操作。

通过观察下图可知：

- 该模块必须位于根级 Inport 模块和函数调用子系统之间的引用模型中。Asynchronous Task Specification 模块必须紧跟在 Inport 模块之后并直接连接到该模块。这两个模块的组合构成名为 JMAAB-B 的建模风格。
- Inport 模块必须从父模型中的 Async Interrupt 模块接收中断信号。
- Inport 模块必须配置为接收和发送函数调用触发信号。

How to use Asynchronous Task Specification block
