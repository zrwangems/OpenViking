---
type: simulink-block
title: 'Composite Entity Creator'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: 'Resource Allocation Modeling'
documentation_page: 'compositeentitycreator'
documentation_source_path: 'ref/compositeentitycreator.html'
language: zh-CN
chinese_source: worker-translation
---

# Composite Entity Creator

## 端口

### 输入

### **port\_1** — 输入实体 标量 | 向量 | 矩阵

用于进入模块的实体的输入实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **port\_2** — 输入实体 标量 | 向量 | 矩阵

用于进入模块的实体的输入实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### 输出

### **port\_1** — 输出复合实体 标量 | 向量 | 矩阵

用于离开模块的复合实体的输出实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

## 参数

### **输入端口数** — 指定输入端口数 `2`（默认） | 标量

指定用于创建复合实体的输入端口数。

#### 编程用法

|  |
| --- |
| **模块参数**：`NumberInputPorts` |
| **类型**：character vector |
| **值**：`'2'` | 标量 |
| **默认**：`'2'` |

### **实体类型名称** — 指定复合实体的类型名称 `Combined`（默认） | character vector

指定组合传入实体后创建的复合实体的类型名称。

#### 编程用法

|  |
| --- |
| **模块参数**：`EntityTypeName` |
| **类型**：character vector |
| **值**：`'Combined'` | character vector |
| **默认**：`'Combined'` |

### **总线对象** — 指定输出 `off`（默认） | `on`

指定是否将复合实体输出为总线对象。

#### 编程用法

|  |
| --- |
| **模块参数**：`BusObject` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |

### **定义输入实体名称** — 指定用于生成复合实体的输入实体名称 `{E1, E2}`（默认） | character vector

复合实体中各实体的名称。

#### 编程用法

|  |
| --- |
| **模块参数**：`InputEntityName` |
| **类型**：character vector |
| **值**：`'E1|E2'` | character vector |
| **默认**：`'E1|E2'` |

## 所属库

SimEvents

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016a 中引入**

## 描述

创建复合实体

Composite Entity Creator 模块为同时到达所有输入端口的每组实体创建一个复合实体。新创建的实体可以包含有关到达实体的结构、属性和计时器的信息。

您可以使用此模块组合来自不同路径的实体。组合后的实体表示较大项中的不同部分，例如数据包中的头部、有效载荷和尾部。或者，您可以通过将表示资源的实体与表示部件或其他项的实体组合起来，对资源分配进行建模。

Composite Entity Creator 模块检测所有必需组件实体何时存在，以及组合操作产生的复合实体何时能够推进到下一个模块。您还可以配置 Composite Entity Creator 模块，使其能够通过 Composite Entity Splitter 模块逆转组合操作。
