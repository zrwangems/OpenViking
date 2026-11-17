---
type: simulink-block
title: 'Derepeat'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Sequence Operations'
documentation_page: 'derepeat'
documentation_source_path: 'ref/derepeat.html'
language: zh-CN
chinese_source: worker-translation
---

# Derepeat

## 端口
```yaml
ports:
- name: In
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: double
- name: Out
  summary: 输出信号 标量 | 向量 | 矩阵
  direction: output
  data_types: double
```

### 输入

### **In** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。

**数据类型：** `double`
**复数支持：** 是
### 输出

### **Out** — 输出信号 标量 | 向量 | 矩阵

输出信号，返回为标量或列向量。

**数据类型：** `double`
**复数支持：** 是

有关处理速率的详细信息，请参阅单速率处理和多速率处理。
## 参数
```yaml
parameters:
- name: Derepeat factor, N
  summary: 去重复因子 5（默认）| 整数
  group: ''
- name: Input processing
  summary: 输入处理控制 Columns as channels (frame based)（默认）| Elements as channels (sample based)
  group: ''
- name: Rate options
  summary: 模块处理速率 Allow multirate processing（默认）| Enforce single-rate processing
  group: ''
- name: Initial condition
  summary: 初始条件 0（默认）| 标量 | 向量 | 矩阵
  group: ''
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的**仿真**选项卡中，在**准备**库中选择**属性检查器**。

### **Derepeat factor, N** — 去重复因子 5（默认）| 整数

去重复因子，指定为整数。去重复因子是产生每个输出样本时进行平均的连续输入样本的数量。

### **Input processing** — 输入处理控制 `Columns as channels (frame based)`（默认）| `Elements as channels (sample based)`

输入处理控制，指定为以下选项之一：

- `Columns as channels (frame based)` — 模块将输入的每一列视为单独的通道。
- `Elements as channels (sample based)` — 模块将输入的每个元素视为单独的通道。

### **Rate options** — 模块处理速率 `Allow multirate processing`（默认）| `Enforce single-rate processing`

模块处理速率，指定为以下选项之一：

- `Allow multirate processing` — 模块对信号进行下采样，使输出采样率比输入采样率慢 `Derepeat factor, N` 倍。有关详细信息，请参阅多速率处理。
- `Enforce single-rate processing` — 模块通过将输出帧大小减小等于 `Derepeat factor, N` 参数值的因子来保持输入采样率。此外，在单速率处理模式下，您可以在触发子系统使用此模块。有关详细信息，请参阅单速率处理

### **Initial condition** — 初始条件 0（默认）| 标量 | 向量 | 矩阵

初始条件，指定为标量、向量或矩阵。此参数指定当输入数据过早无法在输出中显示时输出的值。如果**Initial condition**参数的维度与输出维度匹配，则该参数表示初始输出值。如果**Initial condition**是标量，则它表示输出中每个元素的初始值。该模块不支持初始条件的空矩阵。
## 所属库

Communications Toolbox / Sequence Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

通过对连续样本求平均值来降低采样率

Derepeat 模块通过对 *N* 个连续样本求平均值，以输入采样率的 1/*N* 倍速率对离散输入进行重采样。*N* 表示 `Derepeat factor, N` 参数。
