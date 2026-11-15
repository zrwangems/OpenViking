---
type: simulink-block
title: 'Task'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Organizational Units'
documentation_page: 'task'
documentation_source_path: 'ref/task.html'
language: zh-CN
chinese_source: worker-translation
---

# Task

## 端口

R2025b 中未记录。

## 参数

R2025b 中未记录。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2019a 中引入**

## 描述

Task

Task 模块放置在 PLC 控制器内部。一个控制器内可以有多个任务。每个任务由一个程序或多个程序组成。

可以使用 `get_param` 和 `set_param` 函数控制 Task 模块的设置。

| 属性名称 | 描述 |
| --- | --- |
| `'Name'` | 任务名称 |
| `'SystemSampleTime'` | 任务速率 |
| `'PLCTaskWatchDog'` | 看门狗定时器值 |
| `'Priority'` | 任务优先级 |
| `'Description'` | 任务描述 |
