---
type: simulink-block
title: 'Signal Invalidation'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Classic Platform / Signal Routing'
documentation_page: 'signalinvalidation'
documentation_source_path: 'ref/signalinvalidation.html'
language: zh-CN
chinese_source: worker-translation
---

# Signal Invalidation

## 端口

### 输入

### **Port\_1** — 输入数据值 数值

如果有效，则要传递的输入数据值。

**示例：**  4

**数据类型：** `single` | `double` | `base integer` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Port\_2** — 失效控制标志 `true` | `false`

失效控制标志确定输入数据值是有效的并且可以传递（`false`），还是无效的并且必须根据失效策略进行处理（`true`）。

**示例：**
`false`

**数据类型：** `Boolean`
### 输出

### **Port\_1** — 输出数据值 数值

由输入数据值和失效控制标志组合产生的输出数据值。

**数据类型：** `single` | `double` | `base integer` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **Signal invalidation policy** — 失效策略 `Keep`（默认）| `Replace` | `DontInvalidate`

指定 AUTOSAR 数据元素失效策略，该策略确定如何处理无效数据元素。

#### 编程使用

|  |
| --- |
| **模块参数**：`InvalidationPolicy` |
| **类型**：character vector |
| **值**：`'Keep' | 'Replace' | 'DontInvalidate'` |
| **默认值**：`'Keep'` |

### **Initial value** — 数据元素初始值 0（默认）| double

指定数据元素初始值。如果输入数据值被标记为无效，并且 **Signal invalidation policy** 为 `Replace`，则软件将输入数据值替换为指定的初始值。

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialOutput` |
| **类型**：character vector |
| **值**：real finite values |
| **默认值**：`'0'` |

## 所属库

AUTOSAR Blockset / Classic Platform / Signal Routing

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

## 描述

控制 AUTOSAR 根输出端口数据元素失效

根据第二个输入（失效控制标志）的值，将第一个输入（数据值）传递到输出。

如果输入数据值有效（失效控制标志为 `false`），则软件将输入数据值传递到输出。

如果输入数据值无效（失效控制标志为 `true`），则结果操作由模块参数 **Signal invalidation policy** 的值决定：

- `Keep` - 将输入数据值替换为最后一个有效信号值。
- `Replace` - 将输入数据值替换为模块参数 **Initial value** 的值。
- `DontInvalidate` - 不替换输入数据值。

此模块必须直接连接到根输出端口模块。它不能在可重用子系统内使用。
