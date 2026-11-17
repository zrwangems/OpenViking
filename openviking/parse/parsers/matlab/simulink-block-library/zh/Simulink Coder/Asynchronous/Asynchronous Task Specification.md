---
type: simulink-block
title: 'Asynchronous Task Specification'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Asynchronous'
documentation_page: 'asynchronoustaskspecification'
documentation_source_path: 'ref/asynchronoustaskspecification.html'
language: zh-CN
chinese_source: worker-translation
---

# Asynchronous Task Specification

## 端口

### 输入

### **Port\_1** — 中断输入信号 标量

从根级 Inport 模块接收的中断输入信号。
### 输出

### **Port\_1** — 带优先级的中断信号 标量

具有指定任务优先级的信号，用于触发函数调用子系统。

## 参数

### **Task priority** — 调用函数调用子系统的异步任务的优先级 `10`（默认值）

指定一个整数或 [] 作为调用所连接函数调用子系统的异步任务的优先级。该优先级必须是一个能够生成相关速率转换行为的值。

- 如果指定一个整数，它必须与父模型中中断信号发起者的优先级值匹配。
- 如果指定 []，则优先级不必与顶层模型中中断信号发起者的优先级匹配。速率转换算法是保守的（未优化）。优先级未知但为静态。

考虑以下模型。

被引用模型包含以下内容。

如果 **Task priority** 参数设置为 10，则父模型中的 Async Interrupt 模块也必须具有优先级 10。如果该参数设置为 []，则 Async Interrupt 模块的优先级可以是 10 以外的值。

## 所属库

Simulink Coder / Asynchronous

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2011a 中引入**

## 描述

指定由异步中断触发的被引用模型所表示的异步任务的优先级

Asynchronous Task Specification 模块指定由异步中断触发的函数调用子系统所表示的异步任务的参数（例如任务优先级）。使用此模块可以控制由异步事件触发的函数调用子系统的调度。您可以通过为被引用模型中的每个函数调用子系统分配优先级来控制调度。

要使用此模块，请按照 Convert Asynchronous Subsystem to a Referenced Model 中的过程操作。

观察图中：

- 该模块必须位于被引用模型中，介于根级 Inport 模块和函数调用子系统之间。Asynchronous Task Specification 模块必须紧跟在 Inport 模块之后并直接连接到该 Inport 模块。这两个模块的组合构成了称为 JMAAB-B 的建模风格。
- Inport 模块必须从父模型中的 Async Interrupt 模块接收中断信号。
- Inport 模块必须配置为接收和发送函数调用触发信号。

如何使用 Asynchronous Task Specification 模块
