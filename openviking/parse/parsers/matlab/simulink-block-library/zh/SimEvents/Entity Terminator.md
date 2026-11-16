---
type: simulink-block
title: 'Entity Terminator'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'entityterminator'
documentation_source_path: 'ref/entityterminator.html'
language: zh-CN
chinese_source: worker-translation
---

# Entity Terminator

## 端口

### 输入

### **Port\_1** — 输入实体 标量 | 向量 | 矩阵

用于进入 Entity Terminator 的实体的输入实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### 输出

### **Port\_a** — 已到达的实体数量 标量

已到达模块的实体数量。

#### 依赖关系

要启用此端口，请单击 **统计** 选项卡，然后选中标记为 **已到达的实体数量，a** 的框。

**数据类型：** `double`

## 参数

### **事件操作** — 指定实体在某些事件中的行为 `Entry`

指定实体在某些事件中的行为。在 **事件操作** 参数中定义行为。**Entry** 操作在实体进入模块之后立即被调用。

#### 编程用法

|  |
| --- |
| **模块参数**：`EntryAction` |
| **类型**：字符向量 |
| **值**：MATLAB 代码 |
| **默认值**：`''` |

### **已到达的实体数量，a** — 输出已到达模块的实体数量 `off` (默认) | `on`

已到达模块的实体数量。

#### 编程用法

|  |
| --- |
| **模块参数**：`NumberEntitiesArrived` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

## 所属库

SimEvents

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2016a 中引入**

## 描述

终止实体

Entity Terminator 模块接受并销毁实体。使用此模块表示实体离开模型。

要自定义实体进入时的操作，请在 **事件操作** 选项卡的 `Entry action` 字段中使用 MATLAB® 代码。有关详细信息，请参阅事件和事件操作。
