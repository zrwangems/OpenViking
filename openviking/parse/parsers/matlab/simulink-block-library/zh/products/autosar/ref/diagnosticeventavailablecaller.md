---
type: simulink-block
title: 'DiagnosticEventAvailableCaller'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Composition and ECU Software Simulation'
documentation_page: 'diagnosticeventavailablecaller'
documentation_source_path: 'ref/diagnosticeventavailablecaller.html'
language: zh-CN
chinese_source: worker-translation
---

# DiagnosticEventAvailableCaller

## 端口

R2025b 中未记录。

## 参数

### **客户端端口名称** — AUTOSAR 组件用于调用 Dem 服务接口 `EventAvailable` 的客户端端口名称 `EventAvailable`（默认）| character vector

输入 AUTOSAR 软件组件用于调用 Dem 服务接口 `EventAvailable` 的客户端端口名称。

#### 编程使用

|  |
| --- |
| **Block Parameter:** `PortName` |
| **Type:** character vector |
| **Values:** `'EventAvailable'` |
| **Default:** `'EventAvailable'` |

### **操作** — 指定 Dem 服务接口 `EventAvailable` 中定义的操作 `SetEventAvailable`（默认）

此模块支持 Dem 操作 `SetEventAvailable`，并为该操作生成输入端口和输出端口。您可以使用此操作将事件配置为不可用。不可用事件被视为如同未在系统中配置，并且当被其他操作访问时返回 E\_NOT\_OK。

#### 编程使用

|  |
| --- |
| **Block Parameter:** `Operation` |
| **Type:** character vector |
| **Values:** `'SetEventAvailable'` |
| **Default:** `'SetEventAvailable'` |

### **采样时间** — 模块采样时间 -1（默认）| scalar

模块采样时间。默认设置使模块从模型继承其采样时间。

#### 编程使用

|  |
| --- |
| **Block Parameter:** `st` |
| **Type:** character vector |
| **Values:** `-1 |` scalar |
| **Default:** `-1` |

## 所属库

AUTOSAR Blockset / Classic Platform / Basic Software / Diagnostic Event Manager (Dem)

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2023a：基础软件调用方模块支持所有 AUTOSAR schema 版本

从 23a 开始，基础软件调用方 (BSW) 模块支持 AUTOSAR Blockset 支持的所有 AUTOSAR schema 版本。BSW 模块继承模型指定的相同 schema 版本。从组件生成的代码和 ARXML 反映模型上指定的 schema 版本。当您更改模型指定的 schema 版本时，软件会自动将软件调用替换为正确的操作。

在某些情况下，当在 schema 版本之间移动时，软件可能会提示您确认更改。当您更新到新的 schema 版本时，软件还可能显示警告，因为某些建模模式不再符合所配置的 AUTOSAR schema 版本。

## 描述

调用 AUTOSAR Diagnostic Event Manager (Dem) 服务接口 EventAvailable

对于 AUTOSAR Classic Platform，AUTOSAR 标准将重要服务定义为在 AUTOSAR Runtime Environment (RTE) 中运行的基础软件 (BSW) 的一部分。示例包括由 Diagnostic Event Manager (Dem)、Function Inhibition Manager (FiM) 和 NVRAM Manager (NvM) 提供的服务。在 AUTOSAR RTE 中，AUTOSAR 软件组件通常使用客户端-服务器通信访问 BSW 服务。

为支持 AUTOSAR 组件和服务的系统级建模与仿真，AUTOSAR Blockset 提供 AUTOSAR Basic Software 模块库。该库包含预配置模块，用于对组件调用 AUTOSAR BSW 服务进行建模，以及 BSW 服务的参考实现。

DiagnosticEventAvailableCaller 模块调用 Dem 服务接口 `EventAvailable` 以启动 `SetEventAvailable` 操作。组件使用 `SetEventAvailable` 临时禁用和启用特定事件，例如，与现有 Dem `SetEventStatus` 调用方模块关联的同名事件。通常，您将 true/false Boolean 常量模块连接到 `SetEventAvailable` 输入，以便可以关闭（false）或打开（true）事件。禁用时，由 `SetEventStatus` 模块触发的事件没有效果。
