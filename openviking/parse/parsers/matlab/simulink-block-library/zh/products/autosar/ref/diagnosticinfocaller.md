---
type: simulink-block
title: 'DiagnosticInfoCaller'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Composition and ECU Software Simulation'
documentation_page: 'diagnosticinfocaller'
documentation_source_path: 'ref/diagnosticinfocaller.html'
language: zh-CN
chinese_source: worker-translation
---

# DiagnosticInfoCaller

## 端口

R2025b 中未提供文档。

## 参数

### **客户端端口名称** — AUTOSAR 组件用于调用 Dem 服务接口 `DiagnosticInfo` 的客户端端口名称 `DiagnosticInfo`（默认）| character vector

输入 AUTOSAR 软件组件用于调用 Dem 服务接口 `DiagnosticInfo` 的客户端端口名称。

#### 编程用法

|  |
| --- |
| **模块参数:** `PortName` |
| **类型:** character vector |
| **值:**`'DiagnosticInfo' |`唯一名称 |
| **默认值:** `'DiagnosticInfo'` |

### **操作** — 指定 Dem 服务接口 `DiagnosticInfo` 中定义的操作 `GetEventStatus`（默认）| `GetMonitorStatus` | `GetEventFailed` | `GetEventTested` | `GetDTCOfEvent` | `GetFaultDetectionCounter` | `GetEventExtendedDataRecord` | `GetEventFreezeFrameData`

选择 AUTOSAR 软件组件从 Dem 服务接口 `DiagnosticInfo` 调用的操作。AUTOSAR 标准定义了这些操作。选择操作后，将生成模块的输入端口和输出端口以支持该操作。

#### 编程用法

|  |
| --- |
| **模块参数:** `Operation` |
| **类型:** character vector |
| **值:** `'GetEventStatus' | 'GetMonitorStatus' | 'GetEventFailed' | 'GetEventTested' | 'GetDTCOfEvent' | 'GetFaultDetectionCounter' | 'GetEventExtendedDataRecord' | 'GetEventFreezeFrameData'` |
| **默认值:** `'GetEventStatus'` |

### **DTCFormat 的数据类型** — 指定用于表示 Dem 格式类型的数据类型 `Enum:Dem_DTCFormatType`（默认）

指定一个枚举数据类型，以表示某些操作所需的 Dem 格式类型。有关详细信息，请参阅 AUTOSAR 标准 *Specification of Diagnostic Event Manager*。

#### 依赖关系

当 **操作** 设置为 `GetDTCOfEvent` 时指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数:** `Datatype` |
| **类型:** character vector |
| **值:** `'Enum: Dem_DTCFormatType' |`enumerated data type |
| **默认值:** `'Enum: Dem_DTCFormatType'` |

### **采样时间** — 模块采样时间 `'-1'`（默认）| scalar

模块采样时间。默认设置使模块从模型继承其采样时间。

#### 编程用法

|  |
| --- |
| **模块参数:** `st` |
| **类型:** character vector |
| **值:** real scalar |
| **默认值:** `'-1'` |

## 所属库

AUTOSAR Blockset / Classic Platform / Basic Software / Diagnostic Event Manager (Dem)

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

### R2025a: 在任意受支持的架构版本中使用操作

从 R2025a 开始，无论模型和模型中其他模块配置的架构版本如何，都可以使用与该模块关联的任意操作。

### R2024a: 使用操作 `GetMonitorStatus`

从 R2024a 开始，使用 Diagnostic Event Manager (Dem) 操作 `GetMonitorStatus`。要使用此操作，您的模型必须映射到 AUTOSAR 组件。

### R2023a: 基础软件调用方模块支持所有 AUTOSAR 架构版本

从 23a 开始，基础软件调用方 (BSW) 模块支持 AUTOSAR Blockset 支持的所有 AUTOSAR 架构版本。BSW 模块继承模型指定的同一架构版本。从组件生成的代码和 ARXML 反映模型上指定的架构版本。当您更改模型指定的架构版本时，软件会自动将软件调用替换为正确的操作。

在某些情况下，当在架构版本之间移动时，软件可能会提示您确认更改。当您更新到新的架构版本时，软件还可能显示警告，因为某些建模模式不再符合配置的 AUTOSAR 架构版本。

## 描述

调用 AUTOSAR Diagnostic Event Manager (Dem) 服务接口 DiagnosticInfo

AUTOSAR 标准将 Diagnostic Event Manager (Dem) 服务定义为在 AUTOSAR Runtime Environment (RTE) 中运行的基础软件 (BSW) 的一部分。AUTOSAR 软件组件通过客户端-服务器调用访问 Dem 服务。DiagnosticInfoCaller 模块调用 Dem 服务接口 `DiagnosticInfo` 以启动指定的操作。
