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
chinese_source: official
---

# Signal Invalidation

## 端口

### 输入

### **Port\_1** — 输入数据值 数值

要中继的输入数据值（如果有效）。

**示例:**  4

**数据类型:** `single` | `double` | `base integer` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Port\_2** — 失效控制标志 `true` | `false`

失效控制标志确定输入数据值是有效的并且可以中继 (`false`)，还是无效的并且必须基于失效策略来处理 (`true`)。

**示例:**  `false`

**数据类型:** `Boolean`
### 输出

### **Port\_1** — 输出数据值 数值

由输入数据值和失效控制标志的组合生成的输出数据值。

**数据类型:** `single` | `double` | `base integer` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **信号失效策略** — 失效策略 **保持** (默认) | **替换** | **DontInvalidate**

指定 AUTOSAR 数据元素失效策略，该策略确定如何处理无效的数据元素。

#### 编程用法

|  |
| --- |
| **模块参数：**`InvalidationPolicy` |
| **类型：**字符向量 |
| **值：**`'Keep' | 'Replace' | 'DontInvalidate'` |
| **默认值：**`'Keep'` |

### **初始值** — 数据元素初始值 0 (默认) | 双精度

指定数据元素初始值。如果输入数据值标记为无效，并且**信号失效策略**是**替换**，则软件会用指定的初始值替换输入数据值。

#### 编程用法

|  |
| --- |
| **模块参数：**`InitialOutput` |
| **类型：**字符向量 |
| **值：**有限实数值 |
| **默认值：**`'0'` |

## 所属库

AUTOSAR Blockset / Classic Platform / Signal Routing

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2015b 中推出**

## 描述

控制 AUTOSAR 根输出端口数据元素失效

基于第二个输入（失效控制标志）的值，将第一个输入（数据值）中继到输出。

如果输入数据值有效（失效控制标志为 `false`），软件将输入数据值中继到输出。

如果输入数据值无效（失效控制标志为 `true`），则产生的动作由模块参数**信号失效策略**的值确定：

- **保持** - 用最后一个有效信号值替换输入数据值。
- **替换** - 用模块参数**初始值**的值替换输入数据值。
- **DontInvalidate** - 不要替换输入数据值。

此模块必须直接连接到根 Outport 模块。它无法在可重用子系统中使用。
