---
type: simulink-block
title: 'Control Function Available Caller'
family: 'classic-platform'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Classic Platform / Basic Software / Function Inhibition Manager (FiM)'
documentation_page: 'controlfunctionavailablecaller'
documentation_source_path: 'ref/controlfunctionavailablecaller.html'
language: zh-CN
chinese_source: worker-translation
---

# Control Function Available Caller

## 端口

在 R2025b 中未记录。

## 参数

### **客户端端口名称** — AUTOSAR 组件用于调用 FiM 服务接口 `ControlFunctionAvailable` 的客户端端口名称 `ControlFunctionAvailable`（默认）| character vector

输入 AUTOSAR 软件组件用于调用 FiM 服务接口 `ControlFunctionAvailable` 的客户端端口名称。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PortName` |
| **类型：** character vector |
| **取值：** `'ControlFunctionAvailable' |` 唯一名称 |
| **默认值：** `'ControlFunctionAvailable'` |

### **操作** — 指定 FiM 服务接口 `ControlFunctionAvailable` 中定义的操作 `SetFunctionAvailable`（默认）

此模块支持 FiM 操作 `SetFunctionAvailable`，并为该操作生成输入端口和输出端口。传递 true 值会将与客户端端口关联的功能标记为可用，传递 false 值会将该功能标记为不可用。与不可用功能关联的 `GetPermission` 操作（Function Inhibition Caller 模块）返回 false。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Operation` |
| **类型：** character vector |
| **取值：** `'SetFunctionAvailable'` |
| **默认值：** `'SetFunctionAvailable'` |

### **采样时间** — 模块采样时间 -1（默认）| scalar

模块采样时间。默认值将模块设置为从模型继承其采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `st` |
| **类型：** scalar |
| **取值：** `-1 |` scalar |
| **默认值：** `-1` |

## 所属库

AUTOSAR Blockset / Classic Platform / Basic Software / Function Inhibition Manager (FiM)

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2023a：基础软件调用方模块支持所有 AUTOSAR schema 版本

从 23a 开始，基础软件调用方 (BSW) 模块支持 AUTOSAR Blockset 支持的所有 AUTOSAR schema 版本。BSW 模块继承模型指定的同一 schema 版本。从组件生成的代码和 ARXML 反映模型上指定的 schema 版本。当更改模型指定的 schema 版本时，软件会自动将软件调用替换为正确的操作。

在某些情况下，当在不同 schema 版本之间切换时，软件可能会提示您确认更改。当更新到新的 schema 版本时，软件还可能显示警告，因为某些建模模式不再符合所配置的 AUTOSAR schema 版本。

## 描述

调用 AUTOSAR Function Inhibition Manager (FiM) 服务接口 ControlFunctionAvailable

对于 AUTOSAR Classic Platform，AUTOSAR 标准将重要服务定义为基础软件 (BSW) 的一部分，这些服务在 AUTOSAR 运行时环境 (RTE) 中运行。示例包括由 Diagnostic Event Manager (Dem)、Function Inhibition Manager (FiM) 和 NVRAM Manager (NvM) 提供的服务。在 AUTOSAR RTE 中，AUTOSAR 软件组件通常使用客户端-服务器通信访问 BSW 服务。

为了支持 AUTOSAR 组件和服务的系统级建模与仿真，AUTOSAR Blockset 提供了 AUTOSAR 基础软件模块库。该库包含预配置的模块，用于对组件调用 AUTOSAR BSW 服务进行建模，以及 BSW 服务的参考实现。

如 AUTOSAR 规范所定义，Function Inhibition Manager 提供了一种控制机制，用于基于功能标识符 (FIDs) 和抑制条件，选择性地抑制（停用）软件组件可运行实体 (runnables) 中的功能执行。

Function Inhibition Manager 与 Diagnostic Event Manager 密切相关，因为抑制条件可以基于诊断事件的状态。Control Function Available Caller 模块调用 FiM 服务接口 `ControlFunctionAvailable` 以启动 `SetFunctionAvailable` 操作。
