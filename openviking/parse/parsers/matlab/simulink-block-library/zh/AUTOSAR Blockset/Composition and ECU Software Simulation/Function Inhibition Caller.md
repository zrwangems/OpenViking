---
type: simulink-block
title: 'Function Inhibition Caller'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Composition and ECU Software Simulation'
documentation_page: 'functioninhibitioncaller'
documentation_source_path: 'ref/functioninhibitioncaller.html'
language: zh-CN
chinese_source: official
---

# Function Inhibition Caller

## 端口

R2025b 官方文档未提供。

## 参数

### **客户端端口名称** — AUTOSAR 组件用于调用 FiM 服务接口 `FunctionInhibition` 的客户端端口的名称 `FunctionInhibition` (默认) | 字符向量

输入 AUTOSAR 软件组件用于调用 FiM 服务接口 `FunctionInhibition` 的客户端端口的名称。

#### 编程用法

|  |
| --- |
| **模块参数：**`PortName` |
| **类型：**字符向量 |
| **值：**`'FunctionInhibition'` |
| **默认值：**`'FunctionInhibition'` |

### **操作** — 指定在 FiM 服务接口 `FunctionInhibition` 中定义的操作 **GetFunctionPermission** (默认)

此模块支持 FiM 操作 **GetFunctionPermission** 并为此操作生成输入端口和输出端口。此操作查询 Function Inhibition Manager 以检查它是否有权限运行相关联的功能。权限基于使用 Diagnostic Service Component 模块创建的抑制配置。如果功能有权限，则操作返回 true；如果功能被禁止，则返回 false。

#### 编程用法

|  |
| --- |
| **模块参数：**`Operation` |
| **类型：**字符向量 |
| **值：**`'GetFunctionPermission'` |
| **默认值：**`'GetFunctionPermission'` |

### **采样时间** — 模块采样时间 -1 (默认) | 标量

模块采样时间。默认设置为模块从模型继承其采样时间。

#### 编程用法

|  |
| --- |
| **模块参数：**`st` |
| **类型：**字符向量 |
| **值：**`-1 |` 标量 |
| **默认值：**`-1` |

## 所属库

AUTOSAR Blockset / Classic Platform / Basic Software / Function Inhibition Manager (FiM)

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2020a 中推出**

### R2023a: 基础软件调用方模块支持所有 AUTOSAR 架构版本

从 23a 开始，基础软件调用方 (BSW) 模块支持 AUTOSAR Blockset 支持的所有 AUTOSAR 架构版本。BSW 模块继承模型指定的相同架构版本。从组件生成的代码和 ARXML 反映在模型上指定的架构版本。当您更改由模型指定的架构版本时，软件会自动将软件调用替换为正确的操作。

在某些情况下，在架构版本之间移动时，软件可能会提示您确认更改。当您更新到新架构版本时，软件也可能会显示警告，因为某些建模模式不再符合配置的 AUTOSAR 架构版本。

## 描述

调用 AUTOSAR Function Inhibition Manager (FiM) 服务接口 FunctionInhibition

对于 AUTOSAR Classic 平台，AUTOSAR 标准将重要服务定义为在 AUTOSAR 运行时环境 (RTE) 中运行的基础软件 (BSW) 的一部分。示例包括 Diagnostic Event Manager (Dem)、Function Inhibition Manager (FiM) 和 NVRAM Manager (NvM) 提供的服务。在 AUTOSAR RTE 中，AUTOSAR 软件组件通常使用客户端-服务器通信来访问 BSW 服务。

为了支持 AUTOSAR 组件和服务的系统级建模和仿真，AUTOSAR Blockset 提供了 AUTOSAR 基础软件模块库。该库包含预配置的模块，用于对组件调用 AUTOSAR BSW 服务进行建模，以及 BSW 服务的参考实现。

如 AUTOSAR 规范中所定义，Function Inhibition Manager 提供一种控制机制，用于根据具有抑制条件的函数标识符 (FID) 有选择地抑制（停用）软件组件可运行实体中的函数执行。

Function Inhibition Manager 与 Diagnostic Event Manager 密切相关，因为抑制条件可以基于诊断事件的状态。Function Inhibition Caller 模块调用 FiM 服务接口 `FunctionInhibition` 以启动 `GetFunctionPermission` 操作。
