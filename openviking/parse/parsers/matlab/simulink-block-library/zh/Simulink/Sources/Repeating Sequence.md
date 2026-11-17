---
type: simulink-block
title: 'Repeating Sequence'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'repeatingsequence'
documentation_source_path: 'slref/repeatingsequence.html'
language: zh-CN
chinese_source: worker-translation
---

# Repeating Sequence

## 端口
```yaml
ports:
- name: Port_1
  summary: 周期输出信号 标量
  direction: output
  data_types: double
```

### 输出

### **Port\_1** — 周期输出信号 标量

由 **Time values** 和 **Output values** 参数指定的输出信号，用于生成周期标量信号。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Time values
  summary: 输出时间向量 [0 2]（默认）| 向量
  group: ''
  block_parameter: rep_seq_t
  type: 字符向量
  values: 向量
  default: '[0 2]'
- name: Output values
  summary: 输出值向量 [0 2]（默认）| 向量
  group: ''
  block_parameter: rep_seq_y
  type: 字符向量
  values: 向量
  default: '[0 2]'
```

### **Time values** — 输出时间向量 `[0 2]`（默认）| 向量

严格单调递增的时间值向量。生成波形的周期是该参数最后一个值与第一个值之差。

#### 编程使用

|  |
| --- |
| **模块参数**：`rep_seq_t` |
| **类型**：字符向量 |
| **值**：向量 |
| **默认值**：`[0 2]` |

### **Output values** — 输出值向量 `[0 2]`（默认）| 向量

指定输出波形的输出值向量。每个元素对应于 **Time values** 参数中的时间值。

#### 编程使用

|  |
| --- |
| **模块参数**：`rep_seq_y` |
| **类型**：字符向量 |
| **值**：向量 |
| **默认值**：`[0 2]` |
## 所属库

Simulink / Sources

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不推荐用于生产代码。

考虑使用 Repeating Sequence Stair 或 Repeating Sequence Interpolated 模块进行代码生成。

## 版本历史

**在 R2006a 之前引入**

## 描述

生成任意形状的周期信号

Repeating Sequence 模块输出一个周期标量信号，其波形由 **Time values** 和 **Output values** 参数指定。**Time values** 参数指定一个输出时间向量。**Output values** 参数指定在对应输出时间处的信号幅值向量。这两个参数共同指定了输出波形在从波形重复区间（信号周期）起点开始测量的各点处的采样值。

默认情况下，两个参数均为 `[0 2]`。这些默认设置指定了一个锯齿波形，从仿真开始每 `2` 秒重复一次，最大幅值为 `2`。
