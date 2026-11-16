---
type: simulink-block
title: 'Fault Subsystem'
family: 'fault-analyzer'
product_id: 'fault-analyzer'
product_name: 'Simulink Fault Analyzer'
documentation_release: R2025b
official_category: ''
documentation_page: 'faultsubsystem'
documentation_source_path: 'ref/faultsubsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# Fault Subsystem

## 端口

R2025b 中未记录。

## 参数

R2025b 中未记录。

## 所属库

Simulink Fault Analyzer

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `imagea` | `integera` | `singlea` | `stringa` |
| **直接馈通** | `no` |
| **多维信号** | `yesa` |
| **可变大小信号** | `yesa` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 实际的数据类型或能力支持取决于模块实现。 | |

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

## 描述

为故障注入建模行为

使用这些模块对故障行为进行建模。Fault Subsystem 模块包含一个 Fault Inport 模块，用于获取要修改的信号；还包含一个 Fault Outport 模块，用于输出该信号。在这两个模块之间连接行为。

当您向故障添加故障行为时，Simulink® Fault Analyzer™ 会从库中复制故障行为，并将模型存储在此模块中。您可以从内置行为中选择，也可以创建并注册自定义行为。请参阅创建预定义和自定义故障行为。

每个 Fault Subsystem 模块只能包含一个 Fault Input 模块和一个 Fault Outport 模块。若要检索供 Fault Subsystem 模块使用的其他模型信号数据，请使用 Fault Data Inport 模块。
