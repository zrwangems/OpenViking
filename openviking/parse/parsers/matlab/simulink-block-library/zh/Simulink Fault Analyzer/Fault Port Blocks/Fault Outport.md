---
type: simulink-block
title: 'Fault Outport'
family: 'fault-analyzer'
product_id: 'fault-analyzer'
product_name: 'Simulink Fault Analyzer'
documentation_release: R2025b
official_category: 'Fault Port Blocks'
documentation_page: 'faultoutport'
documentation_source_path: 'ref/faultoutport.html'
language: zh-CN
chinese_source: worker-translation
---

# Fault Outport

## 端口
```yaml
ports:
- name: Port_1
  summary: 输出故障行为 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | string | fixed
    point | enumeration | bus
```

### 输入

### **Port\_1** — 输出故障行为 标量 | 向量 | 矩阵

从行为到模型的输出，指定为标量、向量或矩阵。连接到此模块以在另一个模型中表示所引入的行为。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumeration` | `bus`
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Simulink Fault Analyzer / Fault Port Blocks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

## 描述

从故障行为输出信号

Fault Outport 模块将故障行为模型中的信号链接到外部模型。您可以使用这些模块将信号数据输出到 Simulink® 和 System Composer™ 模型。

仅在 Fault Subsystem 模块中使用这些模块。每个 Fault Subsystem 模块只能包含一个 Fault Outport 模块。
