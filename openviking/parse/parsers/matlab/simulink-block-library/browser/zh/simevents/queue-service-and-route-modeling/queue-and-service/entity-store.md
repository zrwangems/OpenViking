---
type: simulink-block
title: 'Entity Store'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: 'Queue, Service, and Route Modeling / Queue and Service'
documentation_page: 'entitystore'
documentation_source_path: 'ref/entitystore.html'
language: zh-CN
chinese_source: worker-translation
---

# Entity Store

## 端口

### 输入

### **Port\_1** — 输入实体 标量 | 向量 | 矩阵

用于进入存储区的实体的输入实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### 输出

### **Port\_1** — 输出实体 标量 | 向量 | 矩阵

用于离开存储区的实体的输出实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_d** — 已离开模块的实体数量 标量

已离开模块的实体数量。

#### 依赖项

要启用此端口，请点击 **统计信息** 选项卡，并选中标有 **已离开的实体数量，d** 的复选框。

**数据类型：** `double`

### **Port\_n** — 尚未离开模块的实体数量 标量

尚未离开模块的实体数量。

#### 依赖项

要启用此端口，请点击 **统计信息** 选项卡，并选中标有 **模块中的实体数量，n** 的复选框。

**数据类型：** `double`

### **Port\_w** — 模块中实体的平均等待时间 标量

模块中实体的平均等待时间。

#### 依赖项

要启用此端口，请点击 **统计信息** 选项卡，并选中标有 **平均等待时间，w** 的复选框。

**数据类型：** `double`

### **Port\_l** — 平均存储区大小 标量

存储区的平均大小。

#### 依赖项

要启用此端口，请点击 **统计信息** 选项卡，并选中标有 **平均存储区大小，l** 的复选框。

**数据类型：** `double`

### **Port\_ex** — 提取的实体数量 标量

从此模块中提取的实体数量。

#### 依赖项

要启用此端口，请点击 **统计信息** 选项卡，并选中标有 **提取的实体数量，ex** 的复选框。

**数据类型：** `double`

## 参数

### **Capacity** — 指定存储区的容量 `25`（默认）| scalar

指定存储区中包含的最大实体数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`Capacity` |
| **类型**：character vector |
| **值**：`'25'` | scalar |
| **默认值**：`'25'` |

### **Number of entities departed, d** — 输出已离开模块的实体数量 `off`（默认）| `on`

选中此复选框将输出已退出模块的实体数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberEntitiesDeparted` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Number of entities in block, n** — 输出模块中存在且尚未离开的实体数量 `off`（默认）| `on`

选中此复选框将输出模块中存在且尚未离开的实体数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberEntitiesInBlock` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Average wait, w** — 输出平均等待时间 `off`（默认）| `on`

离开模块的实体的等待时间总和除以其总数。*等待时间* 是实体进入和离开 Entity Store 模块之间的持续时间。有关详细信息，请参阅 Interpret SimEvents Models Using Statistical Analysis。

#### 编程使用

|  |
| --- |
| **模块参数**：`AverageWait` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Average store size, l** — 输出平均存储区大小 `off`（默认）| `on`

累积的时间加权平均存储区大小。*存储区大小* 是模块中存储的实体数量。该模块通过以下方式计算平均存储区大小：

1. 将存储区大小乘以其持续时间，以计算时间加权存储区大小
2. 将所有时间加权存储区大小相加，并在总时间上求平均

有关详细信息，请参阅 Interpret SimEvents Models Using Statistical Analysis。

#### 编程使用

|  |
| --- |
| **模块参数**：`AverageStoreSize` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Number of entities extracted, ex** — 从此模块提取的实体数量 `off`（默认）| `on`

输出由 Entity Find 模块从此模块中拉出的已提取实体数量。当实体被提取时，**已离开的实体数量，d**、**模块中的实体数量，n**、**平均等待时间，w** 和 **平均存储区大小，l** 统计信息会相应更新。有关查找和提取实体的详细信息，请参阅 Find and Extract Entities in SimEvents Models。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumEntitiesExtracted` |
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

**在 R2018a 中引入**

## 描述

存储实体

Entity Store 模块用作容器或存储箱，用于存储无序实体。这些实体一旦被下一个模块接受，就准备好立即离开该模块。Entity Store 模块会在实体到达时立即尝试转发该实体。如果尝试失败，该模块会将实体置于待处理状态。然后，当下一个模块可以开始接受该实体时，该实体即可离开。

要自定义实体进入、退出或被阻塞时的动作，请在 **事件动作** 选项卡的 `Entry action`、`Exit action` 或 `Blocked action` 字段中输入 MATLAB® 代码。
