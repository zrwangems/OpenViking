---
type: simulink-block
title: 'NvMAdminCaller'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Classic Platform / Basic Software / NVRAM Manager (NvM)'
documentation_page: 'nvmadmincaller'
documentation_source_path: 'ref/nvmadmincaller.html'
language: zh-CN
chinese_source: official
---

# NvMAdminCaller

## 端口

R2025b 官方文档未提供。

## 参数

### **客户端端口名称** — AUTOSAR 组件用于调用 NvM 服务接口 `NvMAdmin` 的客户端端口的名称 `NvMAdmin` (默认) | 字符向量

输入 AUTOSAR 软件组件用于调用 NvM 服务接口 `NvMAdmin` 的客户端端口的名称。

#### 编程用法

|  |
| --- |
| **模块参数：**`PortName` |
| **类型：**字符向量 |
| **值：**`'NvMAdmin' |` 唯一名称 |
| **默认值：**`'NvMAdmin'` |

### **操作** — 在 NvM 服务接口 `NvMAdmin` 中定义的操作 **SetBlockProtection** (默认)

选择 AUTOSAR 软件组件从 NvM 服务接口 `NvMAdmin` 调用的操作。AUTOSAR 标准定义这些操作。在您选择操作后，将生成模块的输入端口和输出端口以支持该操作。支持一项操作：**SetBlockProtection**。

#### 编程用法

|  |
| --- |
| **模块参数：**`Operation` |
| **类型：**字符向量 |
| **值：**`'SetBlockProtection'` |
| **默认值：**`'SetBlockProtection'` |

### **采样时间** — 模块采样时间 -1 (默认) | 标量

模块采样时间。默认设置为模块从模型继承其采样时间。

#### 编程用法

|  |
| --- |
| **模块参数：**`st` |
| **类型：**标量 |
| **值：**`'-1' |` 标量 |
| **默认值：**`'-1'` |

## 所属库

AUTOSAR Blockset / Classic Platform / Basic Software / NVRAM Manager (NvM)

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2016b 中推出**

### R2023a: 基础软件调用方模块支持所有 AUTOSAR 架构版本

从 23a 开始，基础软件调用方 (BSW) 模块支持 AUTOSAR Blockset 支持的所有 AUTOSAR 架构版本。BSW 模块继承模型指定的相同架构版本。从组件生成的代码和 ARXML 反映在模型上指定的架构版本。当您更改由模型指定的架构版本时，软件会自动将软件调用替换为正确的操作。

在某些情况下，在架构版本之间移动时，软件可能会提示您确认更改。当您更新到新架构版本时，软件也可能会显示警告，因为某些建模模式不再符合配置的 AUTOSAR 架构版本。

## 描述

调用 AUTOSAR NVRAM Manager (NvM) 服务接口 NvMadmin

AUTOSAR 标准将 NVRAM Manager (NvM) 服务定义为在 AUTOSAR 运行时环境 (RTE) 中运行的基础软件 (BSW) 的一部分。AUTOSAR 软件组件通过客户端-服务器调用访问 NvM 服务。NvMAdminCaller 模块调用 AUTOSAR NvM 服务接口 `NvMAdmin` 以启动指定的操作。
