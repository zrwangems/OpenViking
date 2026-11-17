---
type: simulink-block
title: 'Entity Store'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'entitystore'
documentation_source_path: 'ref/entitystore.html'
language: zh-CN
chinese_source: worker-translation
---

# Entity Store

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入实体 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated | bus
    | fixed point
- name: Port_1
  summary: 输出实体 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated | bus
    | fixed point
- name: Port_d
  summary: 已离开模块的实体数量 标量
  direction: output
  data_types: double
- name: Port_n
  summary: 尚未离开模块的实体数量 标量
  direction: output
  data_types: double
- name: Port_w
  summary: 模块中实体的平均等待时间 标量
  direction: output
  data_types: double
- name: Port_l
  summary: 平均存储大小 标量
  direction: output
  data_types: double
- name: Port_ex
  summary: 提取的实体数量 标量
  direction: output
  data_types: double
```

### 输入

### **Port\_1** — 输入实体 标量 | 向量 | 矩阵

用于进入存储的实体的输入实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### 输出

### **Port\_1** — 输出实体 标量 | 向量 | 矩阵

用于离开存储的实体的输出实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_d** — 已离开模块的实体数量 标量

已离开模块的实体数量。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，然后选中标记为 **Number of entities departed, d** 的复选框。

**数据类型：** `double`

### **Port\_n** — 尚未离开模块的实体数量 标量

尚未离开模块的实体数量。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，然后选中标记为 **Number of entities in block, n** 的复选框。

**数据类型：** `double`

### **Port\_w** — 模块中实体的平均等待时间 标量

模块中实体的平均等待时间。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，然后选中标记为 **Average wait, w** 的复选框。

**数据类型：** `double`

### **Port\_l** — 平均存储大小 标量

存储的平均大小。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，然后选中标记为 **Average store size, l** 的复选框。

**数据类型：** `double`

### **Port\_ex** — 提取的实体数量 标量

从此模块中取出的实体数量。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，然后选中标记为 **Number of entities extracted, ex** 的复选框。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Capacity
  summary: 指定存储的容量 25（默认）| 标量
  group: ''
  block_parameter: Capacity
  type: 字符向量
  values: '''25'' | 标量'
- name: Number of entities departed, d
  summary: 输出已离开模块的实体数量 off（默认）| on
  group: ''
  block_parameter: NumberEntitiesDeparted
  type: 字符向量
  values: '''on'' | ''off'''
- name: Number of entities in block, n
  summary: 输出模块中存在的、尚未离开的实体数量 off（默认）| on
  group: ''
  block_parameter: NumberEntitiesInBlock
  type: 字符向量
  values: '''on'' | ''off'''
- name: Average wait, w
  summary: 输出平均等待时间 off（默认）| on
  group: ''
  block_parameter: AverageWait
  type: 字符向量
  values: '''on'' | ''off'''
- name: Average store size, l
  summary: 输出平均存储大小 off（默认）| on
  group: ''
  block_parameter: AverageStoreSize
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Number of entities extracted, ex
  summary: 从该模块提取的实体数量 off（默认）| on
  group: ''
  block_parameter: NumEntitiesExtracted
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
```

### **Capacity** — 指定存储的容量 `25`（默认）| 标量

指定存储中包含的实体的最大数量。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Capacity` |
| **类型**：字符向量 |
| **值**：`'25'` | 标量 |
| **默认**：`'25'` |

### **Number of entities departed, d** — 输出已离开模块的实体数量 `off`（默认）| `on`

选中此复选框将输出已离开模块的实体数量。

#### 程序化使用

|  |
| --- |
| **模块参数**：`NumberEntitiesDeparted` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |

### **Number of entities in block, n** — 输出模块中存在的、尚未离开的实体数量 `off`（默认）| `on`

选中此复选框将输出模块中存在的、尚未离开的实体数量。

#### 程序化使用

|  |
| --- |
| **模块参数**：`NumberEntitiesInBlock` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |

### **Average wait, w** — 输出平均等待时间 `off`（默认）| `on`

离开模块的实体的等待时间之和除以其总数。*等待时间* 是实体进入和离开 Entity Store 模块之间的持续时间。有关更多信息，请参阅 Interpret SimEvents Models Using Statistical Analysis。

#### 程序化使用

|  |
| --- |
| **模块参数**：`AverageWait` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |

### **Average store size, l** — 输出平均存储大小 `off`（默认）| `on`

累积的时间加权平均存储大小。*存储大小*是模块中存储的实体数量。该模块通过以下方式计算平均存储大小：

1. 将存储大小乘以其持续时间，以计算时间加权存储大小
2. 将所有时间加权存储大小求和，并在总时间上取平均值

有关详细信息，请参阅 Interpret SimEvents Models Using Statistical Analysis。

#### 编程使用

|  |
| --- |
| **模块参数**：`AverageStoreSize` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Number of entities extracted, ex** — 从该模块提取的实体数量 `off`（默认）| `on`

输出由 Entity Find 模块从该模块中拉出的已提取实体数量。当实体被提取时，**Number of entities departed, d**、**Number of entities in block, n**、**Average wait, w** 和 **Average store size, l** 统计量会相应更新。有关查找和提取实体的详细信息，请参阅 Find and Extract Entities in SimEvents Models。

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

Entity Store 模块用作存储无序实体的容器或箱。只要下一个模块接受这些实体，它们就可以立即离开该模块。Entity Store 模块会在实体到达时立即尝试将其转发。如果尝试失败，该模块会将实体置于待处理状态。当下一个模块可以开始接受它时，该实体便可以离开。

若要自定义实体进入、退出或被阻塞时的操作，请在 **Event actions** 选项卡的 `Entry action`、`Exit action` 或 `Blocked action` 字段中输入 MATLAB® 代码。
