---
type: simulink-block
title: 'Execution Time'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: 'Target Profiling'
documentation_page: 'executiontime'
documentation_source_path: 'ref/executiontime.html'
language: zh-CN
chinese_source: worker-translation
---

# Execution Time

## 端口

### 输出

### **Total Exec Time** — 上一个基础速率节拍的总执行时间 double

提供截至上一个采样时间的总执行时间。

### **Task Exec Time** — 各个采样率的任务执行时间（可选）vector of double

提供多任务模型中各个采样率截至上一个采样时间的任务执行时间。

#### 依赖关系

当选择 **测量任务执行时间** 时，此端口可见。

## 参数

### **测量任务执行时间** — 显示各个任务的执行时间 `‘off’` (默认) | `‘on’`

使端口 `Task Exec Time` 可见，该端口提供多任务模型中各个采样率截至上一个采样时间的任务执行时间。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowTaskTimes` |

## 所属库

Simulink Desktop Real-Time / Target Profiling

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2017a 中引入**

### R2024b: 对具有端口名称的模块的更新

在 R2024b 中，当启用可选端口（例如 **显示 "Missed Ticks" 端口**）时，这些 Simulink® Desktop Real-Time™ 模块端口会带标签显示。

## 描述

在 Run in Kernel 模式下输出总执行时间

Execution Time 模块在 **Run in Kernel** 模式下输出执行时间。

在 **Connected IO** 模式下，此模块不执行任何操作。它输出零。
