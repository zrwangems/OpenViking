---
type: simulink-block
title: 'DiagnosticMonitorCaller'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Composition and ECU Software Simulation'
documentation_page: 'diagnosticmonitorcaller'
documentation_source_path: 'ref/diagnosticmonitorcaller.html'
language: zh-CN
chinese_source: official
---

# DiagnosticMonitorCaller

## 端口

R2025b 官方文档未提供。

## 参数

### **客户端端口名称** — AUTOSAR 组件用于调用 Dem 服务接口 `DiagnosticMonitor` 的客户端端口的名称 `DiagnosticMonitor` (默认) | 字符向量

输入 AUTOSAR 软件组件用于调用 Dem 服务接口 `DiagnosticMonitor` 的客户端端口的名称。

#### 编程用法

|  |
| --- |
| **模块参数：**`PortName` |
| **类型：**字符向量 |
| **值：**`'DiagnosticMonitor' |`  唯一名称 |
| **默认值：**`'DiagnosticMonitor'` |

### **操作** — 指定在 Dem 服务接口 `DiagnosticMonitor` 中定义的操作 `SetEventStatus` (默认) | `ResetMonitorStatus` | `ResetEventStatus` | `PrestoreFreezeFrame` | `ClearPrestoredFreezeFrame` | `SetEventDisabled`

选择 AUTOSAR 软件组件从 Dem 服务接口 `DiagnosticMonitor` 调用的操作。这些操作由 AUTOSAR 标准定义。在选择操作后，会生成模块的输入端口和输出端口以支持该操作。

#### 编程用法

|  |
| --- |
| **模块参数：**`Operation` |
| **类型：**字符向量 |
| **值：**`'SetEventStatus' | 'ResetMonitorStatus' | 'ResetEventStatus' | 'PrestoreFreezeFrame' | 'ClearPrestoredFreezeFrame' | 'SetEventDisabled'` |
| **默认值：**`'SetEventStatus'` |

### **EventStatus 的数据类型** — 指定表示 Dem 事件类型的数据类型 `Enum: Dem_EventStatusType` (默认)

指定一个枚举数据类型以表示某些操作所需的 Dem 事件类型。有关详细信息，请参阅 AUTOSAR 标准 *Diagnostic Event Manager 设定*。

#### 依赖关系

当**操作**设置为 `SetEventStatus` 时指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数：**`Datatype` |
| **类型：**字符向量 |
| **值：**`'Enum: Dem_EventStatusType' |` 枚举数据类型 |
| **默认值：**`'SetEventStatus'` |

### **采样时间** — 模块采样时间 `'-1'` (默认) | 标量

模块采样时间。默认设置为模块从模型继承其采样时间。

#### 编程用法

|  |
| --- |
| **模块参数：**`st` |
| **类型：**字符向量 |
| **值：**实数标量 |
| **默认值：**`'-1'` |

## 所属库

AUTOSAR Blockset / Classic Platform / Basic Software / Diagnostic Event Manager (Dem)

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2016b 中推出**

### R2025a: 使用任何受支持的架构版本进行操作

从 R2025a 开始，您可以使用与该模块关联的任何操作，无论模型和模型中其他模块的配置架构版本如何。

### R2024a: 使用操作 `ResetMonitorStatus`

从 R2024a 开始，使用 Diagnostic Event Manager (Dem) 操作 `ResetMonitorStatus`。要使用此操作，您的模型必须映射到 AUTOSAR 组件。

### R2023a: 基础软件调用方模块支持所有 AUTOSAR 架构版本

从 23a 开始，基础软件调用方 (BSW) 模块支持 AUTOSAR Blockset 支持的所有 AUTOSAR 架构版本。BSW 模块继承模型指定的相同架构版本。从组件生成的代码和 ARXML 反映在模型上指定的架构版本。当您更改由模型指定的架构版本时，软件会自动将软件调用替换为正确的操作。

在某些情况下，在架构版本之间移动时，软件可能会提示您确认更改。当您更新到新架构版本时，软件也可能显示警告，因为某些建模模式不再符合配置的 AUTOSAR 架构版本。

## 描述

调用 AUTOSAR Diagnostic Event Manager (Dem) 服务接口 DiagnosticMonitor

AUTOSAR 标准将 Diagnostic Event Manager (Dem) 服务定义为在 AUTOSAR 运行时环境 (RTE) 中运行的基础软件 (BSW) 的一部分。AUTOSAR 软件组件通过客户端-服务器调用访问 Dem 服务。DiagnosticMonitorCaller 模块调用 Dem 服务接口 `DiagnosticMonitor` 以启动指定操作。
