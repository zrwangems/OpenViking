---
type: simulink-block
title: 'Trigger-Based Operating Point Snapshot'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Operating Points'
documentation_page: 'triggerbasedoperatingpointsnapshot'
documentation_source_path: 'ug/triggerbasedoperatingpointsnapshot.html'
language: zh-CN
chinese_source: official
---

# Trigger-Based Operating Point Snapshot

## 端口

### 输入

### **Trigger** — 触发控制信号 标量

触发控制信号，指定为标量信号。

## 参数

### **触发器类型** — 控制信号的类型 `rising` (默认) | `falling` | `either` | `function-call`

触发工作点快照的控制信号类型。

- **上升沿** - 在控制信号上升到过零时触发。
- **下降沿** - 在控制信号下降到过零时触发。
- **任一沿** - 在控制信号上升或下降到过零时触发。
- **函数调用**：当控制信号接收到来自 Stateflow® 图、Function-Call Generator 模块、S-Function 模块或 Hit Crossing 模块的函数调用事件时触发。

#### 编程用法

|  |
| --- |
| **模块参数：**`'TriggerType'` |
| **类型：**`character vector` |
| **值：**`'rising'``'falling'``'either'``'function-call'` |
| **默认值：**`'rising'` |

## 所属库

Simulink Control Design / Utilities

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2006a 之前推出**

### R2023b: 库位置已更改

Trigger-Based Operating Point Snapshot 模块现在位于 **Simulink Control Design/Utilities** 子库中。

在 R2023b 中，当您打开使用上一版本保存的模型时，Trigger-Based Operating Point Snapshot 模块的库链接会自动更新。

## 描述

在发生触发事件时生成工作点

Trigger-Based Operating Point Snapshot 模块在发生由输入触发信号指示的触发事件时获取 Simulink® 模型的快照工作点。例如，您可以将模块配置为在触发信号上升到过零时拍摄快照。

然后，您可以使用 `linearize` 函数或模型线性化器在工作点处线性化您的模型。
