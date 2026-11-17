---
type: simulink-block
title: 'NvMServiceCaller'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Classic Platform / Basic Software / NVRAM Manager (NvM)'
documentation_page: 'nvmservicecaller'
documentation_source_path: 'ref/nvmservicecaller.html'
language: zh-CN
chinese_source: worker-translation
---

# NvMServiceCaller

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Client port name
  summary: AUTOSAR 组件用于调用 NvM 服务接口 NvMService 的客户端端口名称 NvMService（默认）| 字符向量
  group: ''
  block_parameter: PortName
  type: 字符向量
  values: '''NvMService'' | 唯一名称'
- name: Operation
  summary: 指定 NvM 服务接口 NvMService 中定义的操作 GetDataIndex（默认）| GetErrorStatus | EraseNvBlock | InvalidateNvBlock | ReadBlock |
    RestoreBlockDefaults | SetDataIndex | SetRamBlockStatus | WriteBlock
  group: ''
  block_parameter: Operation
  type: 字符向量
  values: '''GetDataIndex'' | ''GetErrorStatus'' | ''EraseNvBlock'' | ''InvalidateNvBlock'' | ''ReadBlock'' | ''RestoreBlockDefaults''
    | ''SetDataIndex'' | ''SetRamBlockStatus'' | ''WriteBlock'''
- name: Argument specification
  summary: 为操作读或写访问指定数据类型和维度 uint8(1)（默认）| 字符向量
  group: ''
  block_parameter: ArgumentSpecification
  type: 字符向量
  values: '''uint8(1)'' | 字符向量'
- name: Sample time
  summary: 模块采样时间 -1（默认）| 标量
  group: ''
  block_parameter: st
  type: 标量
  values: '''-1'' | 标量'
```

### **Client port name** — AUTOSAR 组件用于调用 NvM 服务接口 `NvMService` 的客户端端口名称 `NvMService`（默认）| 字符向量

输入 AUTOSAR 软件组件用于调用 NvM 服务接口 `NvMService` 的客户端端口名称。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PortName` |
| **类型：** 字符向量 |
| **值：** `'NvMService' |` 唯一名称 |
| **默认：** `'NvMService'` |

### **Operation** — 指定 NvM 服务接口 `NvMService` 中定义的操作 `GetDataIndex`（默认）| `GetErrorStatus` | `EraseNvBlock` | `InvalidateNvBlock` | `ReadBlock` | `RestoreBlockDefaults` | `SetDataIndex` | `SetRamBlockStatus` | `WriteBlock`

选择 AUTOSAR 软件组件从 NvM 服务接口 `NvMService` 中调用的操作。AUTOSAR 标准定义了这些操作。选择操作后，模块的输入端口和输出端口将自动生成以支持该操作。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Operation` |
| **类型：** 字符向量 |
| **值：** `'GetDataIndex' | 'GetErrorStatus' | 'EraseNvBlock' | 'InvalidateNvBlock' | 'ReadBlock' | 'RestoreBlockDefaults' | 'SetDataIndex' | 'SetRamBlockStatus' | 'WriteBlock'` |
| **默认：** `'GetDataIndex'` |

### **Argument specification** — 为操作读或写访问指定数据类型和维度 `uint8(1)`（默认）| 字符向量

一个 MATLAB 表达式，用于指定操作要读取或写入的数据的数据类型和维度。

- 要指定多维数据类型，可以使用数组语法，例如 `int8([1 1;
  1 1])`。
- 要指定结构化数据类型，可以创建一个 `Simulink.Parameter` 数据对象，使用 `Simulink.Bus` 对象为其指定类型，并引用该参数名称。

有关示例，请参阅 Argument Specification for Simulink Function Blocks。

#### 依赖关系

当 **Operation** 设置为 `ReadBlock`、`RestoreBlockDefaults` 或 `WriteBlock` 时，指定此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ArgumentSpecification` |
| **类型：** 字符向量 |
| **值：** `'uint8(1)' |` 字符向量 |
| **默认：** `'uint8(1)'` |

### **Sample time** — 模块采样时间 -1（默认）| 标量

模块采样时间。默认值将模块设置为从模型继承采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `st` |
| **类型：** 标量 |
| **值：** `'-1' |` 标量 |
| **默认：** `'-1'` |
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

在某些情况下，在 schema 版本之间切换时，软件可能会提示您确认更改。在更新到新的 schema 版本时，软件还可能显示警告，因为某些建模模式不再符合所配置的 AUTOSAR schema 版本。

## 描述

调用 AUTOSAR NVRAM Manager (NvM) 服务接口 NvMService

AUTOSAR 标准将 NVRAM Manager (NvM) 服务定义为在 AUTOSAR 运行时环境（RTE）中运行的基础软件（BSW）的一部分。AUTOSAR 软件组件通过客户端-服务器调用访问 NvM 服务。NvMServiceCaller 模块通过调用 AUTOSAR NvM 服务接口 `NvMService` 来发起指定的操作。
