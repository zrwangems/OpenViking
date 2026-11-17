---
type: simulink-block
title: 'Fault Inport'
family: 'fault-analyzer'
product_id: 'fault-analyzer'
product_name: 'Simulink Fault Analyzer'
documentation_release: R2025b
official_category: 'Fault Port Blocks'
documentation_page: 'faultinport'
documentation_source_path: 'ref/faultinport.html'
language: zh-CN
chinese_source: worker-translation
---

# Fault Inport

## 端口
```yaml
ports:
- name: Port_1
  summary: 来自所分配故障信号的输入 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | string | fixed
    point | enumeration | bus
```

### 输出

### **Port\_1** — 来自所分配故障信号的输入 标量 | 向量 | 矩阵

来自所分配故障信号到行为的输入，指定为标量、向量或矩阵。此端口表示模型中截获的信号。

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

捕获故障行为的入口信号

Fault Inport 模块将来自外部模型的信号链接到故障行为的模型。该模块直接从包含关联故障的信号中检索数据。您可以使用这些模块从 Simulink® 和 System Composer™ 模型中捕获信号数据。

仅在 Fault Subsystem 模块中使用这些模块。每个 Fault Subsystem 模块只能包含一个 Fault Inport 模块。
