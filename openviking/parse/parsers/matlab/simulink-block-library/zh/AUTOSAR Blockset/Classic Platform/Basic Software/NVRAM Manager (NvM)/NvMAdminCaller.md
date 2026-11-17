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
chinese_source: worker-translation
---

# NvMAdminCaller

## 端口

R2025b 中未记录。

## 参数

### **Client port name** — AUTOSAR 组件用于调用 NvM 服务接口 `NvMAdmin` 的客户端端口名称 `NvMAdmin`（默认）| 字符向量

输入 AUTOSAR 软件组件用于调用 NvM 服务接口 `NvMAdmin` 的客户端端口名称。

#### 编程使用

|  |
| --- |
| **模块参数**：`PortName` |
| **类型**：character vector |
| **值**：`'NvMAdmin' |` unique name |
| **默认值**：`'NvMAdmin'` |

### **Operation** — 在 NvM 服务接口 `NvMAdmin` 中定义的操作 `SetBlockProtection`（默认）

选择 AUTOSAR 软件组件从 NvM 服务接口 `NvMAdmin` 调用的操作。AUTOSAR 标准定义了这些操作。选择操作后，模块的输入端口和输出端口将生成以支持该操作。支持一个操作：`SetBlockProtection`。

#### 编程使用

|  |
| --- |
| **模块参数**：`Operation` |
| **类型**：character vector |
| **值**：`'SetBlockProtection'` |
| **默认值**：`'SetBlockProtection'` |

### **Sample time** — 模块采样时间 -1（默认）| 标量

模块采样时间。默认设置使模块从模型继承其采样时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`st` |
| **类型**：scalar |
| **值**：`'-1' |` scalar |
| **默认值**：`'-1'` |

## 所属库

AUTOSAR Blockset / Classic Platform / Basic Software / NVRAM Manager (NvM)

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

### R2023a：基础软件调用方模块支持所有 AUTOSAR schema 版本

从 23a 开始，基础软件调用方（BSW）模块支持 AUTOSAR Blockset 支持的所有 AUTOSAR schema 版本。BSW 模块继承模型指定的相同 schema 版本。从组件生成的代码和 ARXML 反映模型上指定的 schema 版本。当您更改模型指定的 schema 版本时，软件会自动将软件调用替换为正确的操作。

在某些情况下，当在 schema 版本之间切换时，软件可能会提示您确认更改。当您更新到新的 schema 版本时，软件还可能显示警告，因为某些建模模式不再符合所配置的 AUTOSAR schema 版本。

## 描述

调用 AUTOSAR NVRAM Manager (NvM) 服务接口 NvMadmin

AUTOSAR 标准将 NVRAM Manager (NvM) 服务定义为在 AUTOSAR 运行时环境（RTE）中运行的基础软件（BSW）的一部分。AUTOSAR 软件组件通过客户端-服务器调用访问 NvM 服务。NvMAdminCaller 模块调用 AUTOSAR NvM 服务接口 `NvMAdmin` 以启动指定的操作。
