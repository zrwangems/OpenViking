---
type: simulink-block
title: 'Function Inhibition Caller'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Classic Platform / Basic Software / Function Inhibition Manager (FiM)'
documentation_page: 'functioninhibitioncaller'
documentation_source_path: 'ref/functioninhibitioncaller.html'
language: zh-CN
chinese_source: worker-translation
---

# Function Inhibition Caller

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Client port name
  summary: AUTOSAR 组件用于调用 FiM 服务接口 FunctionInhibition 的客户端端口名称 FunctionInhibition（默认）| 字符向量
  group: ''
  block_parameter: PortName
  type: character vector
  values: '''FunctionInhibition'''
  default: '''FunctionInhibition'''
- name: Operation
  summary: 指定 FiM 服务接口 FunctionInhibition 中定义的操作 GetFunctionPermission（默认）
  group: ''
  block_parameter: Operation
  type: character vector
  values: '''GetFunctionPermission'''
  default: '''GetFunctionPermission'''
- name: Sample time
  summary: 模块采样时间 -1（默认）| 标量
  group: ''
  block_parameter: st
  type: character vector
  values: -1 | scalar
  default: '-1'
```

### **Client port name** — AUTOSAR 组件用于调用 FiM 服务接口 `FunctionInhibition` 的客户端端口名称 `FunctionInhibition`（默认）| 字符向量

输入 AUTOSAR 软件组件用于调用 FiM 服务接口 `FunctionInhibition` 的客户端端口名称。

#### 编程使用

|  |
| --- |
| **模块参数**：`PortName` |
| **类型**：character vector |
| **值**：`'FunctionInhibition'` |
| **默认值**：`'FunctionInhibition'` |

### **Operation** — 指定 FiM 服务接口 `FunctionInhibition` 中定义的操作 `GetFunctionPermission`（默认）

此模块支持 FiM 操作 `GetFunctionPermission`，并为该操作生成输入端口和输出端口。此操作查询 Function Inhibition Manager，以检查其是否有权限运行关联的功能。权限基于使用 Diagnostic Service Component 模块创建的抑制配置。如果该功能有权限，操作返回 true；如果该功能被抑制，操作返回 false。

#### 编程使用

|  |
| --- |
| **模块参数**：`Operation` |
| **类型**：character vector |
| **值**：`'GetFunctionPermission'` |
| **默认值**：`'GetFunctionPermission'` |

### **Sample time** — 模块采样时间 -1（默认）| 标量

模块采样时间。默认设置使模块从模型继承其采样时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`st` |
| **类型**：character vector |
| **值**：`-1 |` scalar |
| **默认值**：`-1` |
## 所属库

AUTOSAR Blockset / Classic Platform / Basic Software / Function Inhibition Manager (FiM)

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2023a：Basic Software 调用方模块支持所有 AUTOSAR schema 版本

从 23a 开始，Basic Software 调用方（BSW）模块支持 AUTOSAR Blockset 支持的所有 AUTOSAR schema 版本。BSW 模块继承模型指定的相同 schema 版本。从组件生成的代码和 ARXML 反映模型上指定的 schema 版本。当您更改模型指定的 schema 版本时，软件会自动将软件调用替换为正确的操作。

在某些情况下，当在不同 schema 版本之间切换时，软件可能会提示您确认更改。当您更新到新的 schema 版本时，软件还可能显示警告，因为某些建模模式不再符合所配置的 AUTOSAR schema 版本。

## 描述

调用 AUTOSAR Function Inhibition Manager (FiM) 服务接口 FunctionInhibition

对于 AUTOSAR Classic Platform，AUTOSAR 标准将重要服务定义为在 AUTOSAR Runtime Environment (RTE) 中运行的 Basic Software (BSW) 的一部分。示例包括 Diagnostic Event Manager (Dem)、Function Inhibition Manager (FiM) 和 NVRAM Manager (NvM) 提供的服务。在 AUTOSAR RTE 中，AUTOSAR 软件组件通常使用客户端-服务器通信访问 BSW 服务。

为支持 AUTOSAR 组件和服务的系统级建模与仿真，AUTOSAR Blockset 提供了 AUTOSAR Basic Software 模块库。该库包含用于建模组件对 AUTOSAR BSW 服务的调用以及 BSW 服务的参考实现的预配置模块。

如 AUTOSAR 规范所定义，Function Inhibition Manager 提供了一种控制机制，用于基于带有抑制条件的函数标识符（FID）选择性地抑制（停用）软件组件可运行实体中的函数执行。

Function Inhibition Manager 与 Diagnostic Event Manager 密切相关，因为抑制条件可以基于诊断事件的状态。Function Inhibition Caller 模块调用 FiM 服务接口 `FunctionInhibition` 以启动 `GetFunctionPermission` 操作。
