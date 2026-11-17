---
type: simulink-block
title: 'OPC UA Write'
family: 'icomm'
product_id: 'icomm'
product_name: 'Industrial Communication Toolbox'
documentation_release: R2025b
official_category: 'OPC Unified Architecture'
documentation_page: 'opcuawrite'
documentation_source_path: 'ug/opcuawrite.html'
language: zh-CN
chinese_source: worker-translation
---

# OPC UA Write

## 端口
```yaml
ports:
- name: Value
  summary: 节点值向量 vector
  direction: input
  data_types: Boolean | single | double | datetime | duration | int8 | int16 | int32 | int64 | uint8 | uint8 vector | uint16
    | uint32 | uint64 | struct | char vector
```

### 输入

### **Value** — 节点值向量 vector

要写入 OPC UA 服务器节点的值。输入端口数量对应于您在 **Nodes** 参数中选择的节点数量。

有关 **Value** 端口支持的数据类型的详细信息，请参阅 OPC UA Server Data Types。

#### 依赖关系

要启用此端口，请在 **Nodes** 参数中指定一个或多个节点。

**数据类型：** `Boolean` | `single` | `double` | `datetime` | `duration` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint8 vector` | `uint16` | `uint32` | `uint64` | `struct` | `char vector`
## 参数
```yaml
parameters:
- name: Server
  summary: 为模块定义 OPC UA 服务器 下拉列表
  group: ''
  block_parameter: ServerList
  type: string | character vector
- name: Nodes
  summary: OPC UA 服务器节点列表 表格
  group: ''
  block_parameter: NodeList
  type: string | character vector
- name: Sample time
  summary: 写入操作的采样时间 -1（默认）| 非负标量
  group: ''
  block_parameter: SampleTime
  type: string | character vector
  values: 非负标量
```

### **Server** — 为模块定义 OPC UA 服务器 下拉列表

选择要与该模块关联的 OPC UA 客户端。

- 要使用 **OPC configuration** 窗格添加所需的客户端，请点击 **Configure servers**。有关详细信息，请参阅 Configure OPC UA Client in Simulink。
- 要将模块更新为最新的 OPC 配置，请点击 **Refresh**。

#### 编程用法

|  |
| --- |
| **模块参数：** `ServerList` |
| **类型：** `string` | `character vector` |

### **Nodes** — OPC UA 服务器节点列表 表格

选择要写入指定服务器的节点。

- 要添加变量类型节点，请点击 **Add**。此操作将打开所选 OPC UA 服务器的 Browse Namespace 对话框。使用此浏览器，您可以选择要添加到 **Nodes** 列表的节点。
- 要删除选定的节点，请点击 **Delete**。
- 要更改列表中选定节点的顺序，请点击 **Move Up** 或 **Move Down**。节点的序列号决定了模块在输入端口输入信号的顺序。

#### 编程用法

|  |
| --- |
| **模块参数：** `NodeList` |
| **类型：** `string` | `character vector` |

### **Sample time** — 写入操作的采样时间 -1（默认）| 非负标量

以秒为单位定义模块的采样时间。模块在指定的采样时间同步将数据写入服务器。您可以指定 `0` 表示连续模式，或指定 `-1` 以继承连接到 OPC UA Write 模块输入的模块的采样时间。有关详细信息，请参阅 Specify Sample Time (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** `string` | `character vector` |
| **值：** 非负标量 |
| **默认：** `'-1'` |
## 所属库

Industrial Communication Toolbox / OPC Unified Architecture

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

## 描述

将数据写入 OPC UA 服务器

OPC UA Write 模块将数据写入 OPC Unified Architecture (UA) 服务器上的一个或多个节点。写入操作在指定的采样时间同步进行。

每个输入端口将数据写入 OPC UA Write 模块 **Nodes** 列表中对应的节点。每个节点可以接受不同数据类型的数据。

**注意**

您需要 Industrial Communication Toolbox™ 和 Simulink® 许可证才能使用此模块。

**注意**

您必须连接至少一个 OPC UA 服务器才能使用 OPC UA Read 模块。您可以使用模型配置参数对话框中的 **OPC Configuration** 窗格创建 OPC UA 客户端。您必须在模型中添加至少一个 OPC UA Read 或 OPC UA Write 模块才能启用此窗格。有关详细信息，请参阅 Configure OPC UA Client in Simulink。
