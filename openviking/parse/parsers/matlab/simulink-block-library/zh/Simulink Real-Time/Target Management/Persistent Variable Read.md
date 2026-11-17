---
type: simulink-block
title: 'Persistent Variable Read'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Target Management'
documentation_page: 'persistentvariableread'
documentation_source_path: 'io_ref/persistentvariableread.html'
language: zh-CN
chinese_source: worker-translation
---

# Persistent Variable Read

## 端口
```yaml
ports:
- name: Data
  summary: 持久变量输出数据 变量数据
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean
```

### 输出

### **Data** — 持久变量输出数据 变量数据

Persistent Variable Read 模块输出端口的数据类型和维度由 `Default value` 参数设置。如果这些属性与目标计算机上存储的变量不匹配，则在实时应用程序加载期间发生错误。

该模块可以接受复数。Persistent Variable Read 模块输出端口的复数性由 `Default value` 参数设置。如果此属性与目标计算机上存储的变量的复数性不匹配，则在实时应用程序加载期间发生错误。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`
## 参数
```yaml
parameters:
- name: Variable name
  summary: 持久变量的名称 Variable1（默认）| 字符向量 | 字符串
  group: ''
  block_parameter: varName
- name: Default value
  summary: 当目标计算机上不存在变量时持久变量的起始值 0（默认）| 支持与 Data 端口相同的数据类型
  group: ''
  block_parameter: defaultValue
```

### **Variable name** — 持久变量的名称 `Variable1`（默认）| 字符向量 | 字符串

**Variable name** 参数提供持久变量的名称。使用此名称可通过 `getPersistentVariables` 函数从目标计算机检索的变量值结构中访问该变量。

#### 编程使用

|  |
| --- |
| **模块参数**：`varName` |

### **Default value** — 当目标计算机上不存在变量时持久变量的起始值 `0`（默认）| 支持与 Data 端口相同的数据类型

**Default value** 参数在目标计算机上不存在变量时为持久变量提供起始值。此参数设置 Persistent Variable Read 模块输出端口的数据类型和维度。

#### 编程使用

|  |
| --- |
| **模块参数**：`defaultValue` |
## 所属库

Simulink Real-Time / Target Management

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

从目标计算机读取持久变量值

Persistent Variable Read 模块在加载实时应用程序时从 Speedgoat® 目标计算机读取所选的持久变量。如果该模块找不到所选变量，则输出所选的默认值。目标计算机关闭后，变量值仍然保留。

使用 `getPersistentVariables` 函数和 `setPersistentVariables` 函数访问目标计算机上的持久变量值。
