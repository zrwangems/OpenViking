---
type: simulink-block
title: 'Composite Entity Creator'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'compositeentitycreator'
documentation_source_path: 'ref/compositeentitycreator.html'
language: zh-CN
chinese_source: worker-translation
---

# Composite Entity Creator

## 端口

### 输入

### **port\_1** — 输入实体 标量 | 向量 | 矩阵

进入模块的实体的输入实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **port\_2** — 输入实体 标量 | 向量 | 矩阵

进入模块的实体的输入实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### 输出

### **port\_1** — 输出复合实体 标量 | 向量 | 矩阵

离开模块的复合实体的输出实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

## 参数

### **Number of input ports** — 指定输入端口数量 `2`（默认）| 标量

指定用于创建复合实体的输入端口数量。

#### 程序化使用

|  |
| --- |
| **模块参数**：`NumberInputPorts` |
| **类型**：字符向量 |
| **值**：`'2'` | 标量 |
| **默认值**：`'2'` |

### **Entity type name** — 指定复合实体的类型名称 `Combined`（默认）| 字符向量

指定合并传入实体后所创建的复合实体的类型名称。

#### 程序化使用

|  |
| --- |
| **模块参数**：`EntityTypeName` |
| **类型**：字符向量 |
| **值**：`'Combined'` | 字符向量 |
| **默认值**：`'Combined'` |

### **Bus object** — 指定输出 `off`（默认）| `on`

指定是否将复合实体输出为总线对象。

#### 程序化使用

|  |
| --- |
| **模块参数**：`BusObject` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Define input entity names** — 指定用于生成复合实体的输入实体名称 `{E1, E2}`（默认）| 字符向量

复合实体中各实体的名称。

#### 程序化使用

|  |
| --- |
| **模块参数**：`InputEntityName` |
| **类型**：字符向量 |
| **值**：`'E1|E2'` | 字符向量 |
| **默认值**：`'E1|E2'` |

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

Composite Entity Creator 模块为同时到达所有输入端口的每一组实体创建一个复合实体。新创建的实体可以包含有关到达实体的结构、属性和计时器的信息。

您可以使用此模块组合来自不同路径的实体。组合后的实体表示较大项中的不同部分，例如数据包中的头部、有效载荷和尾部。或者，您可以通过将一个表示资源的实体与一个表示零件或其他项的实体组合来对资源分配进行建模。

Composite Entity Creator 模块检测所有必要的组件实体何时存在，以及组合操作产生的复合实体何时能够推进到下一个模块。您还可以配置 Composite Entity Creator 模块，通过 Composite Entity Splitter 模块使组合操作可逆。
