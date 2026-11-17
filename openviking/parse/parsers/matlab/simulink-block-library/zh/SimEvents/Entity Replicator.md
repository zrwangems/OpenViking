---
type: simulink-block
title: 'Entity Replicator'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'entityreplicator'
documentation_source_path: 'ref/entityreplicator.html'
language: zh-CN
chinese_source: worker-translation
---

# Entity Replicator

## 端口

### 输入

### **Port\_1** — 输入实体 标量 | 向量 | 矩阵

进入模块的实体的输入端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`
### 输出

### **Port\_1** — 输出副本实体 标量 | 向量 | 矩阵

离开模块的副本实体的输出端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`

### **Port\_2** — 输出被复制的实体 标量 | 向量 | 矩阵

离开模块的原始实体的输出端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`

## 参数

### **Replicas depart from** — 选择副本离开的方式 `Separate output ports`（默认）| `Single output port`

选择副本是从单独的输出端口离开还是从单个输出端口离开。

- `Separate output ports` — 从每个输出端口输出一个副本实体
- `Single output port` — 从单个输出端口输出所有副本

#### 编程使用

|  |
| --- |
| **模块参数**：`ReplicasDepartFrom` |
| **类型**：character vector |
| **值**：`'Separate output ports'` | `'Single output port'` |
| **默认值**：`'Separate output ports'` |

### **Replication amount source** — 指定副本数量的来源 `Dialog`（默认）| `Attribute`

指定副本数量的来源。

- 选择 `Dialog` 在对话框中指定副本数量。
- 选择 `Attribute` 选择一个指定副本数量的属性。

#### 依赖关系

当您将 **Replicas depart from** 设置为 `Single output port` 时，此参数可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`ReplicationAmountSource` |
| **类型**：character vector |
| **值**：`'Dialog'` | `'Attribute'` |
| **默认值**：`'Dialog'` |

### **Number of replicas** — 指定副本数量 1（默认）| 标量

指定副本数量。如果您选择 `Single output port`，所有副本从该输出端口离开。如果您选择 `Separate output ports`，每个副本有自己的端口。

#### 依赖关系

当您将 **Replicas depart from** 设置为 `Separate output ports` 或 `Single output port`，并将 **Replication amount source** 设置为 `Dialog` 时，此参数可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberReplicas` |
| **类型**：character vector |
| **值**：`'1'` | scalar |
| **默认值**：`'1'` |

### **Replicate attribute name** — 指定确定副本数量的属性 `ReplicateAttribute`（默认）| character vector

#### 依赖关系

指定确定副本数量的属性。当您将 **Replicas depart from** 设置为 `Single output port`，并将 **Replication amount source** 设置为 `Attribute` 时，此参数可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`ReplicateAttributeName` |
| **类型**：character vector |
| **值**：`'ReplicateAttribute'` | character vector |
| **默认值**：`'ReplicateAttribute'` |

### **Hold original entity until all replicas depart** — 选择副本离开的方式 `off`（默认）| `on`

选中此复选框以保留原始实体，直到所有副本都已离开。模块会先尝试发送所有副本，然后再发送原始实体。选中此复选框可防止副本实体在原始实体之前未离开模块时被销毁。

#### 编程使用

|  |
| --- |
| **模块参数**：`HoldOriginalEntityUntilAllReplicasDepart` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

## 所属库

SimEvents

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016a 中引入**

## 描述

复制实体

Entity Replicator 模块复制实体。它输出副本实体，也可以输出原始实体。该模块为原始实体提供一个输出端口。

如果原始实体在副本之前离开模块，则其副本将被销毁。选中 **Hold original entity until all replicas depart** 复选框可确保副本在原始实体之前离开模块。

原始实体可以通过 Entity Find 模块从该模块中提取。如果正在 Entity Replicator 模块中等待的原始实体被提取，则所有副本将被销毁。只有原始实体可以被提取，因为副本无法在此模块中获取资源。有关查找和提取实体的详细信息，请参阅 Find and Extract Entities in SimEvents Models。
