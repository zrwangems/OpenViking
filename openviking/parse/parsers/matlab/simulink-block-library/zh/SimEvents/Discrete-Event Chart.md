---
type: simulink-block
title: 'Discrete-Event Chart'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'discreteeventchart'
documentation_source_path: 'ref/discreteeventchart.html'
language: zh-CN
chinese_source: worker-translation
---

# Discrete-Event Chart

## 端口

R2025b 中未记录。

## 参数

R2025b 中未记录。

## 所属库

SimEvents

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016a 中引入**

## 描述

离散事件图

Discrete-Event Chart 模块类似于 Stateflow® 图，但用于离散事件。该模块需要 Stateflow 许可证。

Discrete-Event Chart 模块的显著特征是它以基于事件而非基于时间的方式执行。Discrete-Event Chart 模块为离散事件建模提供了以下优势：

- 精确定时 — 事件发生的时间分辨率可以任意精确，并且不受模型采样时间的限制。
- 到达时触发 — Discrete-Event Chart 模块在消息到达时立即执行。它不会等待下一个采样时间命中。
- 可变执行顺序 — Discrete-Event Chart 模块没有固定的排序执行顺序。执行顺序取决于模型的运行时条件。
- 每个时间步多次执行 — Discrete-Event Chart 模块在单个时间步中可以执行零次或多次。

Discrete Event Chart 的使用方式与 Stateflow Chart (Stateflow) 类似。

要访问图属性，请右键点击图并选择 **Properties**。有关模块属性的详细信息，请参阅 Create Custom Queuing Systems Using Discrete-Event Stateflow Charts。

有关使用 Discrete-Event Chart 模块的 SimEvents® 常见设计模式的信息，请参阅 SimEvents Common Design Patterns。
