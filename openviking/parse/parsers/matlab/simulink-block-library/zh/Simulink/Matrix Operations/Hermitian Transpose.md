---
type: simulink-block
title: 'Hermitian Transpose'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'hermitiantranspose'
documentation_source_path: 'slref/hermitiantranspose.html'
language: zh-CN
chinese_source: worker-translation
---

# Hermitian Transpose

## 端口
```yaml
ports:
- name: Port_1
  summary: 矩阵 *M*×*N* 矩阵
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: 转置矩阵 *N*×*M* 矩阵
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输入

### **Port\_1** — 矩阵 *M*×*N* 矩阵

矩阵，指定为 *M*×*N* 矩阵。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 转置矩阵 *N*×*M* 矩阵

转置矩阵，返回为 *N*×*M* 矩阵。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Simulink / Matrix Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

计算矩阵的埃尔米特转置

Hermitian Transpose 模块计算 *M*×*N* 矩阵的埃尔米特转置。
