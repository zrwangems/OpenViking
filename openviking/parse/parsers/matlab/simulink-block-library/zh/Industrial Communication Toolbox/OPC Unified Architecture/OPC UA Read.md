---
type: simulink-block
title: 'OPC UA Read'
family: 'icomm'
product_id: 'icomm'
product_name: 'Industrial Communication Toolbox'
documentation_release: R2025b
official_category: 'OPC Unified Architecture'
documentation_page: 'opcuaread'
documentation_source_path: 'ug/opcuaread.html'
language: zh-CN
chinese_source: worker-translation
---

# OPC UA Read

## 端口
```yaml
ports:
- name: Value
  summary: 所选节点的当前数据值 标量 | 总线
  direction: output
  data_types: Boolean | single | double | datetime | int8 | int16 | int32 | int64 | uint8 | uint8 vector | uint16 | uint32
    | uint64 | struct | char vector | bus
- name: Timestamp
  summary: 所选节点数据的时间戳 秒（默认）| 日期数字
  direction: output
  data_types: double
- name: Quality
  summary: 从所选节点读取的数据的质量 布尔值
  direction: output
  data_types: Boolean
```

### 输出

### **Value** — 所选节点的当前数据值 标量 | 总线

该模块将所选节点的值输出为以下之一：

- 当您选择单个节点时，输出为标量 Simulink 信号。该信号与所选节点具有相同的数据类型。
- 当您选择多个节点时，输出为 Simulink 总线信号。总线中的每个信号继承其对应节点的数据类型。使用 Bus Selector (Simulink) 模块从 Simulink 总线信号中提取节点的值。

有关 **Value** 端口支持的数据类型的详细信息，请参阅 OPC UA Server Data Types。

#### 依赖关系

要启用此端口，请在 **Nodes** 参数中指定一个或多个节点。

**数据类型：** `Boolean` | `single` | `double` | `datetime` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint8 vector` | `uint16` | `uint32` | `uint64` | `struct` | `char vector` | `bus`

### **Timestamp** — 所选节点数据的时间戳 秒（默认）| 日期数字

该模块将所选节点数据的时间戳输出为以下值之一：

- `Seconds since start`（默认）：表示 Simulink 客户端从服务器接收数据时的仿真时间。
- `Serial date number`：表示源向服务器提供数据时的实际时间。

#### 依赖关系

要启用此端口，请选择 **Show timestamp port** 参数。

**数据类型：** `double`

### **Quality** — 从所选节点读取的数据的质量 布尔值

该模块将从所选节点读取的数据的质量输出为布尔值。逻辑 `0` 输出表示 `'Bad'` 或 `'Uncertain'` 质量，逻辑 `1` 表示 `'Good'` 质量。有关质量格式的详细信息，请参阅 OPC UA Quality。

#### 依赖关系

要启用此端口，请选择 **Show quality port** 参数。

**数据类型：** `Boolean`
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
- name: Show quality port
  summary: 向模块添加质量输出 on（默认）| off
  group: ''
  block_parameter: ShowQualityPort
  type: string | character vector
  values: '''on'' | ''off'''
- name: Show timestamp port
  summary: 向模块添加时间戳输出 on（默认）| off
  group: ''
  block_parameter: ShowTimestampPort
  type: string | character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: 将时间戳端口显示为
  summary: 设置时间戳基准 Seconds since start（默认）| Serial date number
  group: ''
  block_parameter: ShowTimestampPortAs
  type: string | character vector
  values: '''Seconds since start'' | ''Serial date number'''
  default: '''Seconds since start'''
- name: 采样时间
  summary: 读取操作的采样时间 -1（默认）| 非负标量
  group: ''
  block_parameter: SampleTime
  type: string | character vector
  values: 非负标量
  default: '''-1'''
```

### **Server** — 为模块定义 OPC UA 服务器 下拉列表

选择要与该模块关联的 OPC UA 客户端。

- 要使用 **OPC configuration** 窗格添加所需的客户端，请点击 **Configure servers**。有关详细信息，请参阅 Configure OPC UA Client in Simulink。
- 要将模块更新到最新的 OPC 配置，请点击 **Refresh**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ServerList` |
| **类型：** `string` | `character vector` |

### **Nodes** — OPC UA 服务器节点列表 表格

选择要从指定服务器读取的节点。

- 要添加变量类型节点，请点击 **Add**。此操作会打开所选 OPC UA 服务器的 Browse Namespace 对话框。使用此浏览器，您可以选择要添加到 **Nodes** 列表的节点。
- 要删除所选节点，请点击 **Delete**。
- 要更改列表中所选节点的顺序，请点击 **Move Up** 或 **Move Down**。节点的序号决定了模块在 **Value** 端口输出总线中信号的顺序。

#### 程序化使用

|  |
| --- |
| **模块参数：** `NodeList` |
| **类型：** `string` | `character vector` |

### **Show quality port** — 向模块添加质量输出 on（默认）| off

当您选择此参数时，模块将在 **Quality** 端口输出读取数据的质量，为布尔值。质量值 `'good'` 由逻辑 `1` 表示，值 `'bad'` 或 `'uncertain'` 由逻辑 `0` 表示。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowQualityPort` |
| **类型：** `string` | `character vector` |
| **值：** `'on'` | `'off'` |
| **默认：** `'on'` |

### **Show timestamp port** — 向模块添加时间戳输出 on（默认）| off

当您选择此参数时，模块将在 **Timestamp** 端口输出所选节点数据的时间戳，为双精度值向量。您可以使用 Show timestamp port as 参数选择时间戳基准。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowTimestampPort` |
| **类型：** `string` | `character vector` |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **将时间戳端口显示为** — 设置时间戳基准 `Seconds since start`（默认）| `Serial date number`

将时间戳基准设置为 `Seconds since
start` 或 `Serial date
number`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowTimestampPortAs` |
| **类型：** `string` | `character vector` |
| **值：** `'Seconds since start'` | `'Serial date number'` |
| **默认值：** `'Seconds since start'` |

### **采样时间** — 读取操作的采样时间 -1（默认）| 非负标量

以秒为单位定义模块的采样时间。模块在指定的采样时间同步读取服务器中的数据。有关详细信息，请参阅 Specify Sample Time (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** `string` | `character vector` |
| **值：** 非负标量 |
| **默认值：** `'-1'` |
## 所属库

Industrial Communication Toolbox / OPC Unified Architecture

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

## 描述

从 OPC UA 服务器读取数据

OPC UA Read 模块从一个 OPC Unified Architecture (UA) 服务器上的一个或多个节点读取数据。读取操作在指定的采样时间同步进行。

该模块将所选节点的值输出为 Simulink® 总线信号。它可选地将与每个节点关联的时间戳和质量值输出到单独的输出端口。您在模块中选择的节点可以具有不同的数据类型，这些数据类型在 Simulink 总线信号中保持不变。该模块将时间戳输出为序列日期编号（实际时间），或输出为从您开始仿真模型起的秒数（仿真时间）。

**注意**

您需要 Industrial Communication Toolbox™ 和 Simulink 许可证才能使用此模块。

**注意**

您必须连接至少一个 OPC UA 服务器才能使用 OPC UA Read 模块。您可以使用模型配置参数对话框中的 **OPC Configuration** 窗格创建 OPC UA 客户端。您必须在模型中添加至少一个 OPC UA Read 或 OPC UA Write 模块才能启用此窗格。有关详细信息，请参阅 Configure OPC UA Client in Simulink。
