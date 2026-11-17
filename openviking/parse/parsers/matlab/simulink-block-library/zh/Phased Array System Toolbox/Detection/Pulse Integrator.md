---
type: simulink-block
title: 'Pulse Integrator'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection'
documentation_page: 'pulseintegrator'
documentation_source_path: 'ref/pulseintegrator.html'
language: zh-CN
chinese_source: worker-translation
---

# Pulse Integrator

## 端口
```yaml
ports:
- name: x
  summary: 脉冲输入数据矩阵
  direction: input
  data_types: double
- name: ∑x
  summary: 积分脉冲列向量
  direction: output
  data_types: double
```

### 输入

### **x** — 脉冲输入数据矩阵

脉冲输入数据，指定为矩阵。`x` 的每一列为一个脉冲。

**数据类型：** `double`
### 输出

### **∑x** — 积分脉冲列向量

积分脉冲，返回为 *N*×1 列向量，其中 *N* 是输入 `x` 的行数。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Integration method
  summary: 积分方法 Coherent（默认）| Noncoherent
  group: ''
- name: Number of pulses to integrate
  summary: 要积分的脉冲数 10（默认）
  group: ''
- name: Integration overlap (in pulses)
  summary: 积分重叠 0（默认）
  group: ''
```

### **Integration method** — 积分方法 `Coherent`（默认）| `Noncoherent`

将积分方法指定为 `Coherent` 或 `Noncoherent`。

### **Number of pulses to integrate** — 要积分的脉冲数 `10`（默认）

将要积分的脉冲数指定为整数。

### **Integration overlap (in pulses)** — 积分重叠 `0`（默认）

将连续积分中重叠脉冲的数量指定为整数。此数值必须小于 **Number of pulses to integrate** 中指定的值。
## 所属库

Phased Array System Toolbox / Detection

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

相干或非相干脉冲积分

Pulse Integrator 模块对信号的连续脉冲执行相干或非相干积分，并输出积分结果。您可以指定要积分的脉冲数以及连续积分中重叠脉冲的数量。
