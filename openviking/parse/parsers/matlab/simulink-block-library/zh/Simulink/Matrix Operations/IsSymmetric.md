---
type: simulink-block
title: 'IsSymmetric'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'issymmetric'
documentation_source_path: 'slref/issymmetric.html'
language: zh-CN
chinese_source: worker-translation
---

# IsSymmetric

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入矩阵 matrix
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: 对称或反对称矩阵 real scalar boolean
  direction: output
  data_types: Boolean
```

### 输入

### **Port\_1** — 输入矩阵 matrix

输入，指定为矩阵。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 对称或反对称矩阵 real scalar boolean

对称或反对称矩阵，返回为实数标量布尔值。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Mode
  summary: 矩阵是对称还是反对称 Symmetric (默认) | Skew-Symmetric
  group: ''
  block_parameter: Mode
  type: character vector
  values: '''Symmetric'' | ''Skew-Symmetric'''
  default: '''Symmetric'''
```

### **Mode** — 矩阵是对称还是反对称 `Symmetric` (默认) | `Skew-Symmetric`

将矩阵标识为 `Symmetric` 或
`Skew-Symmetric`。

#### 编程使用

|  |
| --- |
| **模块参数**：`Mode` |
| **类型**：character vector |
| **值**：`'Symmetric'` | `'Skew-Symmetric'` |
| **默认值**：`'Symmetric'` |
## 所属库

Simulink / Matrix Operations

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `half` | `integera` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a 此模块在反对称模式下仅支持有符号整数类型。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

检查矩阵是对称还是反对称

IsSymmetric 模块确定输入是对称矩阵还是反对称矩阵。
