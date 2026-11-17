---
type: simulink-block
title: 'Implies'
family: 'sldv'
product_id: 'sldv'
product_name: 'Simulink Design Verifier'
documentation_release: R2025b
official_category: 'Verification Utilities'
documentation_page: 'implies'
documentation_source_path: 'ref/implies.html'
language: zh-CN
chinese_source: worker-translation
---

# Implies

## 端口
```yaml
ports:
- name: Values
  summary: 输入信号 标量 | 元胞数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus
```

### 输入

### **Values** — 输入信号 标量 | 元胞数组

Implies 模块接受 Simulink 软件支持的所有数值数据类型的信号。有关 Simulink 软件支持的数据类型的讨论，请参阅 Data Types Supported by Simulink。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Simulink Design Verifier / Verification Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2009a 中引入**

## 描述

指定产生特定响应的条件

Implies 模块允许您指定一个条件以产生给定的响应；例如，当您踩下汽车刹车踏板时，巡航控制机制被禁用。如果输入 A 为 true 且输入 B 为 false，则输出为 false；对于所有其他输入对，输出为 true。

您可以在任何模型中使用 Implies 模块，而不仅仅是在运行 Simulink® Design Verifier™ 软件时。
