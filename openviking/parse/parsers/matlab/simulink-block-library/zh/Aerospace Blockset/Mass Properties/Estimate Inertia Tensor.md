---
type: simulink-block
title: 'Estimate Inertia Tensor'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Mass Properties'
documentation_page: 'estimateinertiatensor'
documentation_source_path: 'estimateinertiatensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Estimate Inertia Tensor

## 端口
```yaml
ports:
- name: mass
  summary: 质量标量
  direction: input
  data_types: double
- name: dm/dt
  summary: 变化率标量
  direction: input
  data_types: double
- name: I
  summary: 惯性张量 3×3 矩阵
  direction: output
  data_types: double
- name: dI/dt
  summary: 变化率 3×3 矩阵
  direction: output
  data_types: double
```

### 输入

### **mass** — 质量标量

质量，指定为标量。

**数据类型：** `double`

### **dm/dt** — 变化率标量

质量变化率，指定为标量。

**数据类型：** `double`
### 输出

### **I** — 惯性张量 3×3 矩阵

惯性张量，以 3×3 矩阵形式返回。

**数据类型：** `double`

### **dI/dt** — 变化率 3×3 矩阵

惯性张量变化率，以 3×3 矩阵形式返回。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Full mass
  summary: 满载质量 2（默认）| 标量
  group: ''
  block_parameter: fmass
  type: character vector
  values: double scalar
  default: '''2'''
- name: Empty mass
  summary: 空载质量 1（默认）| 标量
  group: ''
  block_parameter: emass
  type: character vector
  values: double scalar
  default: '''1'''
- name: Full inertia matrix
  summary: 满载惯性矩阵 eye(3)（默认）| 3 元素矩阵
  group: ''
  block_parameter: fI
  type: character vector
  values: double scalar
  default: '''eye(3)'''
- name: Empty inertia matrix
  summary: 空载惯性矩阵 eye(3)/2（默认）| 标量
  group: ''
  block_parameter: eI
  type: character vector
  values: scalar
  default: '''eye(3)/2'''
```

### **Full mass** — 满载质量 `2`（默认）| 标量

飞行器的总质量，指定为双精度标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`fmass` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`'2'` |

### **Empty mass** — 空载质量 `1`（默认）| 标量

飞行器的空载质量，指定为双精度标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`emass` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`'1'` |

### **Full inertia matrix** — 满载惯性矩阵 `eye(3)`（默认）| 3 元素矩阵

飞行器满载质量下的惯性张量，指定为三元素矩阵。

#### 编程使用

|  |
| --- |
| **模块参数**：`fI` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`'eye(3)'` |

### **Empty inertia matrix** — 空载惯性矩阵 `eye(3)/2`（默认）| 标量

飞行器空载质量下的惯性张量，指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`eI` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'eye(3)/2'` |
## 所属库

Aerospace Blockset / Mass Properties

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算惯性张量

Estimate Inertia Tensor 模块计算惯性张量及惯性张量的变化率。

使用线性插值来估计惯性张量作为质量的函数。惯性张量的变化率是质量变化率的线性函数。
