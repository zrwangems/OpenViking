---
type: simulink-block
title: 'Signal Sample and Hold'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'signalsampleandhold'
documentation_source_path: 'ref/signalsampleandhold.html'
language: zh-CN
chinese_source: worker-translation
---

# Signal Sample and Hold

## 端口
```yaml
ports:
- name: u
  summary: 输入信号 标量 | 向量
  direction: input
  data_types: single | double
- name: S
  summary: 控制信号 0 | 1
  direction: input
  data_types: Boolean
- name: y
  summary: 输出信号 标量 | 向量
  direction: output
  data_types: single | double
```

### 输入

### **u** — 输入信号 标量 | 向量

输入信号。

**数据类型：** `single` | `double`

### **S** — 控制信号 `0` | `1`

采样脉冲，`0` 表示 `false`，`1` 表示 `true`。

**数据类型：** `Boolean`
### 输出

### **y** — 输出信号 标量 | 向量

输出信号。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Initial condition
  summary: 初始输出值 标量 | 向量
  group: ''
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 -1（默认）| 0 | 正标量
  group: ''
```

### **Initial condition** — 初始输出值 标量 | 向量

指定初始条件。该值必须为标量或与输入信号大小相同的向量。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，将此参数设置为 `-1`。对于离散时间操作，将此参数设置为正整数。对于连续时间操作，将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。
## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

离散时间或连续时间输入信号采样和保持

Signal Sample and Hold 模块在离散时间或连续时间中实现信号采样和保持。

当输入 *S* 为 `true` 时，输出 *y* 等于输入 *u*。当输入 *S* 为 `false` 时，模块保持输出，直到 *S* 再次变为 `true`。
