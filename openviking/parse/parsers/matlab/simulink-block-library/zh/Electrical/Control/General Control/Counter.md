---
type: simulink-block
title: 'Counter'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'counter'
documentation_source_path: 'ref/counter.html'
language: zh-CN
chinese_source: worker-translation
---

# Counter

## 端口
```yaml
ports:
- name: T
  summary: 计数器值 标量
  direction: output
  data_types: single | double
```

### 输出

### **T** — 计数器值 标量

计数器值。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Counter type
  summary: 计数器策略 Up（默认）| Down | Up-Down
  group: ''
- name: Output range
  summary: 范围 [0 1]（默认）| [-1 1]
  group: ''
- name: Timer period (s)
  summary: 周期 0.001（默认）| 正标量
  group: ''
- name: Phase delay (s)
  summary: 延迟 0（默认）| 0 或正标量
  group: ''
- name: Sample time
  summary: 模块采样时间 0.0001（默认）| 0 或正标量
  group: ''
```

### **Counter type** — 计数器策略 `Up`（默认）| `Down` | `Up-Down`

计数器类型。

### **Output range** — 范围 `[0 1]`（默认）| `[-1 1]`

输出的范围。

### **Timer period (s)** — 周期 `0.001`（默认）| 正标量

定时器周期，单位为 s。

### **Phase delay (s)** — 延迟 `0`（默认）| `0` 或正标量

相位延迟，单位为 s。添加相位延迟以更改计数器的初始状态。

### **Sample time** — 模块采样时间 `0.0001`（默认）| `0` 或正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于离散时间仿真，将采样时间设置为正标量。对于连续时间仿真，将采样时间设置为 `0`。
## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

离散或连续时间计数器

Counter 模块在离散或连续时间中实现增量计数器。计数器根据以下条件之一进行递增：

- Up — 输入上升。
- Down — 输入下降。
- Up-Down — 输入上升或下降。
