---
type: simulink-block
title: 'Trigger-Based Operating Point Snapshot'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'triggerbasedoperatingpointsnapshot'
documentation_source_path: 'ug/triggerbasedoperatingpointsnapshot.html'
language: zh-CN
chinese_source: worker-translation
---

# Trigger-Based Operating Point Snapshot

## 端口

### 输入

### **Trigger** — 触发控制信号 标量

触发控制信号，指定为标量信号。

## 参数

### **Trigger type** — 控制信号类型 `rising`（默认）| `falling` | `either` | `function-call`

触发工作点快照的控制信号类型。

- `rising` — 当控制信号在增大时穿过零点时触发。
- `falling` — 当控制信号在减小时穿过零点时触发。
- `either` — 当控制信号在增大或减小时穿过零点时触发。
- `function-call`：当控制信号从 Stateflow® 图、Function-Call Generator 模块、S-Function 模块或 Hit Crossing 模块接收到函数调用事件时触发。

#### 编程使用

|  |
| --- |
| **模块参数**：`'TriggerType'` |
| **类型**：`character vector` |
| **值**：`'rising'``'falling'``'either'``'function-call'` |
| **默认值**：`'rising'` |

## 所属库

Simulink Control Design / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

### R2023b：库位置变更

Trigger-Based Operating Point Snapshot 模块现在位于 **Simulink Control Design/Utilities** 子库中。

在 R2023b 中，当您打开在之前版本中保存的模型时，Trigger-Based Operating Point Snapshot 模块的库链接会自动更新。

## 描述

在触发事件时生成工作点

Trigger-Based Operating Point Snapshot 模块在输入触发信号所指示的触发事件处获取 Simulink® 模型的快照工作点。例如，您可以将该模块配置为每当触发信号在增大时穿过零点时获取快照。

然后，您可以使用 `linearize` 函数或 Model Linearizer 应用在这些工作点处对模型进行线性化。
