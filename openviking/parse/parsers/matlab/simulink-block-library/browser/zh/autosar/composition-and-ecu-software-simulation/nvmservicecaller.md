---
type: simulink-block
title: 'NvMServiceCaller'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Composition and ECU Software Simulation'
documentation_page: 'nvmservicecaller'
documentation_source_path: 'ref/nvmservicecaller.html'
language: zh-CN
chinese_source: official
---

# NvMServiceCaller

## 端口

R2025b 官方文档未提供。

## 参数

### **客户端端口名称** — AUTOSAR 组件用于调用 NvM 服务接口 `NvMService` 的客户端端口的名称 `NvMService` (默认) | 字符向量

输入 AUTOSAR 软件组件用于调用 NvM 服务接口 `NvMService` 的客户端端口的名称。

#### 编程用法

|  |
| --- |
| **模块参数：**`PortName` |
| **类型：**字符向量 |
| **值：**`'NvMService' |` 唯一名称 |
| **默认值：**`'NvMService'` |

### **操作** — 指定在 NvM 服务接口 `NvMService` 中定义的操作 **GetDataIndex** (默认) | **GetErrorStatus** | **EraseNvBlock** | **InvalidateNvBlock** | **ReadBlock** | **RestoreBlockDefaults** | **SetDataIndex** | **SetRamBlockStatus** | **WriteBlock**

选择 AUTOSAR 软件组件从 NvM 服务接口 `NvMService` 调用的操作。AUTOSAR 标准定义这些操作。在您选择操作后，将生成模块的输入端口和输出端口以支持该操作。

#### 编程用法

|  |
| --- |
| **模块参数：**`Operation` |
| **类型：**字符向量 |
| **值：**`'GetDataIndex' | 'GetErrorStatus' | 'EraseNvBlock' | 'InvalidateNvBlock' | 'ReadBlock' | 'RestoreBlockDefaults' | 'SetDataIndex' | 'SetRamBlockStatus' | 'WriteBlock'` |
| **默认值：**`'GetDataIndex'` |

### **参量设定** — 为操作读取或写入访问权限指定数据类型和维度 `uint8(1)` (默认) | 字符向量

MATLAB 表达式，指定操作要读取或写入的数据的数据类型和维度。

- 要指定多维数据类型，您可以使用数组语法，例如 `int8([1 1; 1 1])`。
- 要指定结构化数据类型，您可以创建一个 `Simulink.Parameter` 数据对象，使用 `Simulink.Bus` 对象为其指定类型，并引用参数名称。

有关示例，请参阅Argument Specification for Simulink Function Blocks。

#### 依赖关系

当**操作**设置为 `ReadBlock`、`RestoreBlockDefaults` 或 `WriteBlock` 时，指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数：**`ArgumentSpecification` |
| **类型：**字符向量 |
| **值：**`'uint8(1)' |` 字符向量 |
| **默认值：**`'uint8(1)'` |

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

在某些情况下，在架构版本之间移动时，软件可能会提示您确认更改。当您更新到新架构版本时，软件也可能显示警告，因为某些建模模式不再符合配置的 AUTOSAR 架构版本。

## 描述

调用 AUTOSAR NVRAM Manager (NvM) 服务接口 NvMService

AUTOSAR 标准将 NVRAM Manager (NvM) 服务定义为在 AUTOSAR 运行时环境 (RTE) 中运行的基础软件 (BSW) 的一部分。AUTOSAR 软件组件通过客户端-服务器调用访问 NvM 服务。NvMServiceCaller 模块调用 AUTOSAR NvM 服务接口 `NvMService` 以启动指定的操作。
