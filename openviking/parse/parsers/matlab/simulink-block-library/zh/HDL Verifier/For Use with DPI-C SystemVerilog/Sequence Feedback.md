---
type: simulink-block
title: 'Sequence Feedback'
family: 'hdlverifier'
product_id: 'hdlverifier'
product_name: 'HDL Verifier'
documentation_release: R2025b
official_category: 'For Use with DPI-C SystemVerilog'
documentation_page: 'sequencefeedback'
documentation_source_path: 'ref/sequencefeedback.html'
language: zh-CN
chinese_source: worker-translation
---

# Sequence Feedback

## 端口
```yaml
ports:
- name: Port_1
  summary: 来自记分板的反馈信号 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: 发送至序列子系统的反馈信号 标量
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### 输入

### **Port\_1** — 来自记分板的反馈信号 标量

Sequence Feedback 模块直接接收来自记分板子系统的输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 发送至序列子系统的反馈信号 标量

Sequence Feedback 模块直接向序列子系统输出信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

HDL Verifier / For Use with DPI-C SystemVerilog

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023a 中引入**

## 描述

连接 UVM 测试平台模型中记分板与序列之间的反馈

Sequence Feedback 模块将反馈信号从 UVM 测试平台模型中的记分板传递到序列。该模块实现了一个 Unit Delay (Simulink) 模块，其 **Initial condition** 参数设置为 `0`。
