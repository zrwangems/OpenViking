---
type: simulink-block
title: 'Entity Selector'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: 'Queue, Service, and Route Modeling / Route Entities and Simulink Messages'
documentation_page: 'entityselector'
documentation_source_path: 'ref/entityselector.html'
language: zh-CN
chinese_source: worker-translation
---

# Entity Selector

## 端口

### 输入

### **Key** — 传入参考实体 scalar | vector | matrix

进入模块的参考实体的输入实体端口。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_1** — 传入实体 scalar | vector | matrix

进入模块的匹配实体的输入实体端口。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### 输出

### **Port\_1** — 离开的参考实体 scalar | vector | matrix

离开模块的参考实体的输出实体端口。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_2** — 离开的匹配实体 scalar | vector | matrix

离开选择器的匹配实体的输出实体端口。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_d** — 已离开模块的实体数量 scalar

已离开模块的实体数量。

#### 依赖关系

要启用此端口，请点击 **Statistics**，然后选中 **Number of entities departed, d** 复选框。

**数据类型:** `double`

### **Port\_n** — 尚未离开模块的实体数量 scalar

尚未离开模块的实体数量。

#### 依赖关系

要启用此端口，请点击 **Statistics**，然后选中 **Number of entities in block, n** 复选框。

**数据类型:** `double`

### **Port\_ex** — 已提取的实体数量 scalar

从该模块中拉出的实体数量。

#### 依赖关系

要启用此端口，请点击 **Statistics** 选项卡，然后选中标记为 **Number of entities extracted, ex** 的框。

**数据类型:** `double`

## 参数

### **Number of matching streams** — 确定模块接受多少输入实体流 `1`（默认）| numerical

指定要与参考实体匹配的实体流数量。该模块最多可接受 `8` 个匹配流。

#### 程序化使用

|  |
| --- |
| **模块参数**: `mNumberOfStreams` |
| **类型**: character vector |
| **值**: `'1'` | scalar |
| **默认值**: `'1'` |

### **Key entity attribute Name** — 指定参考属性的名称 `{'ID'}`（默认）| character vector

用于评估匹配的参考属性名称。

#### 程序化使用

|  |
| --- |
| **模块参数**: `mKeyEntityAttributeName` |
| **类型**: character vector |
| **值**: `'{'ID'}'` | character vector |
| **默认值**: `'{'ID'}'` |

### **Matching entity attribute name(s)** — 指定选定属性名称的名称 `{'Type'}`（默认）| character vector

用于评估匹配的匹配实体属性名称。您可以指定一个属性名称，或指定一个属性名称数组，这些名称将与键值进行比较以评估匹配。

#### 程序化使用

|  |
| --- |
| **模块参数**: `mEntityAttributeName` |
| **类型**: character vector |
| **值**: `'{'Type'}'` | character vector |
| **默认值**: `'{'Type'}'` |

### **Number of entities source** — 用于确定要匹配的实体数量的来源 `Dialog`（默认）| `Attribute`

用于确定从每个流中选择的实体数量的来源。

#### 程序化使用

|  |
| --- |
| **模块参数**: `mMatchingNumberSource` |
| **类型**: character vector |
| **值**: `'Dialog'` | `'Attribute'` |
| **默认值**: `'Dialog'` |

### **Number of entities to select** — 要从每个传入实体流中选择的实体数量 `1`（默认）| scalar

要从每个匹配流中选择的实体数量。您可以指定 `0`、正整数或正整数数组，以确定从每个匹配实体流中选择的实体数量。

#### 依赖关系

要启用此参数，请将 **Number of entities source** 参数设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `mNumberOfMatches` |
| **类型**: character vector |
| **值**: `'1'` | scalar |
| **默认值**: `'1'` |

### **Key attribute for number of entities** — 确定要匹配的实体数量的 Key 属性名称 `Name`（默认）| character vector

用于确定要从每个匹配流中选择的实体数量的 Key 属性名称。属性值可以是整数，也可以是大小等于传入实体流数量的整数数组。

#### 依赖关系

要启用此参数，请将 **Number of entities source** 参数设置为 `Attribute`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `mNumberOfMatchesAttribute` |
| **类型**: character vector |
| **值**: `'Name'` | character vector |
| **默认值**: `'Name'` |

### **Number of entities departed, d** — 输出已离开模块的实体数量 `off`（默认）| `on`

已退出模块的实体数量。

#### 程序化使用

|  |
| --- |
| **模块参数**: `mNumEntitiesDepOpt` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

### **Number of entities in block, n** — 输出模块中存在的、尚未离开的实体数量 `off`（默认）| `on`

模块中存在的、尚未离开的实体数量。

#### 程序化使用

|  |
| --- |
| **模块参数**: `mNumEntitiesInBlockOpt` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

### **Number of entities extracted, ex** — 输出从模块中提取的实体数量 `off`（默认）| `on`

输出由 Entity Find 模块从该模块中拉出的已提取实体数量。如果提取的是键实体，则 Entity Selector 模块会等待所有匹配实体到达该模块。然后，匹配实体从对应输出端口离开。如果提取的是匹配实体，则该模块会查找另一个匹配实体。当实体被提取时，**Number of entities departed, d** 和 **Number of entities in block, n** 统计信息会相应更新。

#### 程序化使用

|  |
| --- |
| **模块参数**: `mNumEntitiesExtractedOpt` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

## 所属库

SimEvents

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2018a 中引入**

## 描述

选择实体

Entity Selector 模块从多个准备离开的实体流中选择实体，并将它们与参考实体匹配。您可以使用此模块对涉及基于输入进行匹配的项的场景建模。例如，您可以对生产零件并将这些零件与对应订单匹配的设施建模。

该模块首先接受一个带有其 **Key entity attribute name** 的参考实体。然后，该模块从其他每个接受传入实体的输入端口中选择一个具有 **Matching entity attribute name(s)** 的匹配实体。匹配基于指定属性值的相等性。当在所有实体流中找到匹配时，匹配实体集合和键实体变为准备离开。

Entity Store 模块可用作要由 Entity Selector 模块选择的实体的临时容器。有关示例，请参阅 Match Entities Based on Attributes。
