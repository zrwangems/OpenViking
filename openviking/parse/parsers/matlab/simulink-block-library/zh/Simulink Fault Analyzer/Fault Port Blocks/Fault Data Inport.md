---
type: simulink-block
title: 'Fault Data Inport'
family: 'fault-analyzer'
product_id: 'fault-analyzer'
product_name: 'Simulink Fault Analyzer'
documentation_release: R2025b
official_category: 'Fault Port Blocks'
documentation_page: 'faultdatainport'
documentation_source_path: 'ref/faultdatainport.html'
language: zh-CN
chinese_source: worker-translation
---

# Fault Data Inport

## 端口
```yaml
ports:
- name: Port_1
  summary: 来自模型信号的数据 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | string | fixed
    point | enumeration | bus
```

### 输出

### **Port\_1** — 来自模型信号的数据 标量 | 向量 | 矩阵

Fault Data Inport 模块输出实值标量、向量或矩阵数据。将该模块映射到模型中的模块或组件输出信号。模型必须包含分配给该行为的故障。映射到该模块的信号决定输出数据类型。

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

**在 R2024b 中引入**

## 描述

将 Simulink 模型数据导入故障行为

Fault Data Inport 模块从模型中检索信号数据，并将数据馈送到分配给故障的行为。您可以使用这些模块从 Simulink® 和 System Composer™ 模型中捕获信号数据。

仅在 Fault Subsystem 模块的顶层使用这些模块。

有关详细信息，请参阅 Access Data from Model Outputs in Fault Behaviors。
