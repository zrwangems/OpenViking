---
type: simulink-block
title: 'Deinterlacer'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Sequence Operations'
documentation_page: 'deinterlacer'
documentation_source_path: 'ref/deinterlacer.html'
language: zh-CN
chinese_source: worker-translation
---

# Deinterlacer

## 端口
```yaml
ports:
- name: In
  summary: 输入信号列向量
  direction: input
  data_types: double | single
- name: O
  summary: 奇数编号元素向量
  direction: output
- name: E
  summary: 偶数编号元素向量
  direction: output
```

### 输入

### **In** — 输入信号列向量

输入信号，指定为偶数长度的列向量。

**数据类型：** `double` | `single`
**复数支持：** 是
### 输出

### **O** — 奇数编号元素向量

输入向量的奇数编号元素，以向量形式返回。如果输入是长度为 *N* 的向量，则输出长度为 *N*/2。

### **E** — 偶数编号元素向量

输入向量的偶数编号元素，以向量形式返回。如果输入是长度为 *N* 的向量，则输出长度为 *N*/2。
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Communications Toolbox / Sequence Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

将输入向量的元素交替分配到两个输出向量中

Deinterlacer 模块接受偶数长度的列向量输入信号。该模块将元素交替放入两个输出向量中。因此，每个输出向量的大小是输入向量大小的一半。输出从输入模块的 **Sample time** 参数继承采样时间。
