---
type: simulink-block
title: 'DiagnosticOperationCycleCaller'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Composition and ECU Software Simulation'
documentation_page: 'diagnosticoperationcyclecaller'
documentation_source_path: 'ref/diagnosticoperationcyclecaller.html'
language: zh-CN
chinese_source: worker-translation
---

# DiagnosticOperationCycleCaller

## 端口

R2025b 中未记录。

## 参数

### **客户端端口名称** — AUTOSAR 组件用于调用 Dem 服务接口 `OperationCycle` 的客户端端口名称 `OperationCycle`（默认） | character vector

输入 AUTOSAR 软件组件用于调用 Dem 服务接口 `OperationCycle` 的客户端端口名称。

#### 编程用法

|  |
| --- |
| **模块参数：** `PortName` |
| **类型：** character vector |
| **值：** `'OperationCycle' |`唯一名称 |
| **默认值：** `'OperationCycle'` |

### **操作** — 指定 Dem 服务接口 `OperationCycle` 中定义的操作 `RestartOperationCycle`（默认） | `SetOperationCycleState` | `GetOperationCycleState`

选择 Dem 操作以控制或监视操作循环。要启动和停止操作循环，请选择 `SetOperationCycleState`。要查询操作循环的当前状态，请选择 `GetOperationCycleState`。选择操作后，将生成模块的输入端口和输出端口以支持该操作。

#### 依赖关系

仅当模块上没有输入端口时，操作 `RestartOperationCycle` 才可用。如果模块上有输入端口，则只有 `GetOperationCycle` 和 `SetOperationCycle` 可用。

#### 编程用法

|  |
| --- |
| **模块参数：** `Operation` |
| **类型：** character vector |
| **值：** `'RestartOperationCycle' | 'SetOperationCycleState' | 'GetOperationCycleState'` |
| **默认值：** `'RestartOperationCycle'` |

### **CycleState 的数据类型** — 指定用于启动或停止操作循环 `Enum:Dem_OperationCycleStateType`（默认）

指定一个枚举数据类型，以表示某些操作所需的 Dem 格式类型。

#### 依赖关系

当 **操作** 设置为 `SetOperationCycleState` 时指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `Datatype` |
| **类型：** character vector |
| **值：** `'Enum:Dem_OperationCycleStateType' |` 枚举数据类型 |
| **默认值：** `'Enum:Dem_OperationCycleStateType'` |

### **采样时间** — 模块采样时间 `'-1'`（默认） | scalar

模块采样时间。默认设置使模块从模型继承其采样时间。

#### 编程用法

|  |
| --- |
| **模块参数：** `st` |
| **类型：** character vector |
| **值：** real scalar |
| **默认值：** `'-1'` |

## 所属库

AUTOSAR Blockset / Classic Platform / Basic Software / Diagnostic Event Manager (Dem)

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2020a 中引入**

### R2025a：使用任何受支持架构版本的操作

从 R2025a 开始，无论模型及模型中其他模块配置的架构版本如何，都可以使用与该模块关联的任何操作。

### R2024a：使用操作 `RestartOperationCycle`

从 R2024a 开始，使用 Diagnostic Event Manager (Dem) 操作 `RestartOperationCycle`。要使用此操作，您的模型必须映射到 AUTOSAR 组件。

### R2023a：Basic Software 调用方模块支持所有 AUTOSAR 架构版本

从 23a 开始，Basic Software 调用方 (BSW) 模块支持 AUTOSAR Blockset 支持的所有 AUTOSAR 架构版本。BSW 模块继承模型指定的同一架构版本。从组件生成的代码和 ARXML 反映模型上指定的架构版本。更改模型指定的架构版本时，软件会自动将软件调用替换为正确的操作。在某些情况下，当在架构版本之间移动时，软件可能会提示您确认更改。当您更新到新的架构版本时，软件还可能显示警告，因为某些建模模式不再符合所配置的 AUTOSAR 架构版本。

## 描述

调用 AUTOSAR Diagnostic Event Manager (Dem) 服务接口 OperationCycle

对于 AUTOSAR Classic Platform，AUTOSAR 标准将重要服务定义为在 AUTOSAR Runtime Environment (RTE) 中运行的 Basic Software (BSW) 的一部分。示例包括由 Diagnostic Event Manager (Dem)、Function Inhibition Manager (FiM) 和 NVRAM Manager (NvM) 提供的服务。在 AUTOSAR RTE 中，AUTOSAR 软件组件通常通过客户端-服务器通信访问 BSW 服务。

为支持 AUTOSAR 组件和服务的系统级建模与仿真，AUTOSAR Blockset 提供 AUTOSAR Basic Software 模块库。该库包含用于对组件调用 AUTOSAR BSW 服务进行建模的预配置模块，以及 BSW 服务的参考实现。

如 AUTOSAR 规范所定义，Function Inhibition Manager 提供一种控制机制，用于基于带有抑制条件的函数标识符 (FIDs)，选择性地抑制（停用）软件组件可运行实体中的函数执行。

Function Inhibition Manager 与 Diagnostic Event Manager 密切相关，因为抑制条件可以基于诊断事件的状态。操作循环会影响共享同一 Diagnostic Service Component 的事件。DiagnosticOperationCycleCaller 模块调用 Dem 服务接口 `OperationCycle` 来控制操作循环。
