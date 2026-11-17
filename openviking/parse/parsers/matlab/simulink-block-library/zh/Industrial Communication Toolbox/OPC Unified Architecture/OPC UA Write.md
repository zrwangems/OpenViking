---
type: simulink-block
title: 'OPC UA Write'
family: 'opc-unified-architecture'
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

### 输入

### **Value** — 节点值向量

要写入 OPC UA 服务器节点的值。输入端口数对应于你在 **Nodes** 参数中选择的节点数。

有关 **Value** 端口支持的数据类型的详细信息，请参阅 OPC UA 服务器数据类型。

#### 依赖关系

要启用此端口，请在 **Nodes** 参数中指定一个或多个节点。

**数据类型：** `Boolean` | `single` | `double` | `datetime` | `duration` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint8 vector` | `uint16` | `uint32` | `uint64` | `struct` | `char vector`

## 参数

### **Server** — 为模块下拉列表定义 OPC UA 服务器

选择要与该模块关联的 OPC UA 客户端。

- 要使用 **OPC 配置**窗格添加所需客户端，请点击 **配置服务器**。有关详细信息，请参阅在 Simulink 中配置 OPC UA 客户端。
- 要将模块更新到最新的 OPC 配置，请点击 **刷新**。

#### 编程用法

|  |
| --- |
| **模块参数：** `ServerList` |
| **类型：** `string` | `character vector` |

### **Nodes** — OPC UA 服务器节点列表表

选择要写入指定服务器的节点。

- 要添加变量类型节点，请点击 **添加**。此操作会为选定的 OPC UA 服务器打开浏览命名空间对话框。使用此浏览器，你可以选择要添加到 **Nodes** 列表的节点。
- 要删除选定的节点，请点击 **删除**。
- 要更改列表中选定节点的顺序，请点击 **上移** 或 **下移**。节点的序列号决定模块在输入端口输入信号的顺序。

#### 编程用法

|  |
| --- |
| **模块参数：** `NodeList` |
| **类型：** `string` | `character vector` |

### **Sample time** — 写操作的采样时间 -1 (默认) | 非负标量

以秒为单位定义模块的采样时间。模块在指定的采样时间将数据同步写入服务器。你可以指定 `0` 表示连续模式，或指定 `-1` 以继承连接到 OPC UA Write 模块输入的模块的采样时间。有关详细信息，请参阅指定采样时间 (Simulink)。

#### 编程用法

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

将数据写入 OPC UA 服务器

OPC UA Write 模块将数据写入 OPC Unified Architecture (UA) 服务器上的一个或多个节点。写操作在指定的采样时间同步进行。

每个输入端口将数据写入 OPC UA Write 模块的 **Nodes** 列表中对应的节点。每个节点可以接受不同数据类型的数据。

**注意**

使用此模块需要 Industrial Communication Toolbox™ 和 Simulink® 许可证。

**注意**

你必须连接至少一个 OPC UA 服务器才能使用 OPC UA Read 模块。你可以使用模型“配置参数”对话框中的 **OPC 配置**窗格创建 OPC UA 客户端。你必须在模型中添加至少一个 OPC UA Read 或 OPC UA Write 模块才能启用此窗格。有关详细信息，请参阅在 Simulink 中配置 OPC UA 客户端。
