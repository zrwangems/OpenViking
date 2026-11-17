---
type: simulink-block
title: 'String Find'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'String'
documentation_page: 'stringfind'
documentation_source_path: 'slref/stringfind.html'
language: zh-CN
chinese_source: worker-translation
---

# String Find

## 端口

### 输入

### **str** — 要在其中查找模式的字符串标量

要在其中查找模式（`sub`）的字符串，指定为标量。

**数据类型：** `string`

### **sub** — 模式标量

要在字符串（`str`）中查找的模式，指定为标量。

**数据类型：** `string`
### 输出

### **idx** — 找到的模式标量的位置索引

找到的模式的位置索引，指定为正整数标量。

- 如果模块未找到该模式，则返回 `-1`。
- 如果 **sub** 参数为空（`""`），则模块返回 `1`，表示它匹配了被搜索字符串的开头。

**数据类型：** `int8` | `int16` | `int32`

## 参数

### **Output data type** — 输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Inherit via back propagation` | `int8` | `int16` | `int32` | `<data type expression>`

输出数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择继承选项时，模块将表现出以下行为：

- `Inherit: Inherit via internal rule` — Simulink® 选择一种数据类型，以平衡数值精度、性能和生成代码大小，同时考虑嵌入式目标硬件的属性。
- `Inherit: Inherit via back propagation` — 使用驱动模块的数据类型。

点击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule'` | `'Inherit: Inherit via back propagation'` | `'int8'` | `'int16'` | `'int32'` | *`<data type expression>`* |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Mode** — 数据类型类别 `Inherit`（默认）| `Built in` | `Expression`

数据类型类别，指定为 `Inherit`、`Built in` 或 `Expression`。有关使用此参数的详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

点击 **Show data type assistant** 按钮可启用此参数。

## 所属库

Simulink / String

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `integer` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

返回模式字符串首次出现位置的索引

String Find 模块返回文本字符串 **str** 中模式字符串 **sub** 首次出现位置的索引。
