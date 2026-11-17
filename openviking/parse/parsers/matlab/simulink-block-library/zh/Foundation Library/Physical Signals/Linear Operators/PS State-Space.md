---
type: simulink-block
title: 'PS State-Space'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Linear Operators'
documentation_page: 'psstatespace'
documentation_source_path: 'ref/psstatespace.html'
language: zh-CN
chinese_source: worker-translation
---

# PS State-Space

## 端口
```yaml
ports:
- name: U
  summary: 输入物理信号向量，*u*，无类型物理信号
  direction: input
- name: Y
  summary: 输出物理信号向量，*y*，无类型物理信号
  direction: output
```

### 输入

### **U** — 输入物理信号向量，*u*，无类型物理信号

输入物理信号。
### 输出

### **Y** — 输出物理信号向量，*y*，无类型物理信号

输出物理信号。
## 参数
```yaml
parameters:
- name: A
  summary: 状态矩阵 [0, 1; -1, -2]（默认）| 标量 | 矩阵
  group: ''
- name: B
  summary: 输入矩阵 [0, 1]（默认）| 标量 | 向量 | 矩阵
  group: ''
- name: C
  summary: 输出矩阵 [1, 0]（默认）| 标量 | 向量 | 矩阵
  group: ''
- name: D
  summary: 前馈矩阵或直接传输矩阵 0（默认）| 标量 | 向量 | 矩阵
  group: ''
- name: E
  summary: 描述符矩阵 [1, 0; 0, 1]（默认）| 标量 | 矩阵
  group: ''
- name: Initial state vector
  summary: 状态向量的初始条件 [0; 0]（默认）| 标量 | 向量 | 矩阵
  group: ''
```

### **A** — 状态矩阵 `[0, 1; -1, -2]`（默认）| 标量 | 矩阵

状态矩阵，指定为 *n*×*n* 矩阵，
其中 *n* 是状态数。

### **B** — 输入矩阵 `[0, 1]`（默认）| 标量 | 向量 | 矩阵

输入矩阵，指定为 *n*×*m* 矩阵，
其中 *n* 是状态数，*m* 是
输入向量中的元素数。

### **C** — 输出矩阵 `[1, 0]`（默认）| 标量 | 向量 | 矩阵

输出矩阵，指定为 *r*×*n* 矩阵，
其中 *r* 是输出向量中的元素数，
*n* 是状态数。

### **D** — 前馈矩阵或直接传输矩阵 `0`（默认）| 标量 | 向量 | 矩阵

前馈矩阵或直接传输矩阵，指定为
*r*×*m* 矩阵，其中 *r* 是
输出向量中的元素数，*m* 是
输入向量中的元素数。

### **E** — 描述符矩阵 `[1, 0; 0, 1]`（默认）| 标量 | 矩阵

系统的质量矩阵。质量矩阵可以是奇异或非奇异的，并且必须
与状态矩阵 **A** 具有相同的维度。

### **Initial state vector** — 状态向量的初始条件 `[0; 0]`（默认）| 标量 | 向量 | 矩阵

无量纲向量，表示状态向量在
时间 *t*=0 时的初始条件。
## 所属库

Simscape / Foundation Library / Physical Signals / Linear Operators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

实现线性状态空间系统

PS State-Space 模块实现线性时不变系统的状态空间
表示，由以下方程定义：

Ex˙=Ax+Bu,y=Cx+Du,

其中：

- *x* 是无量纲状态向量。
- *u* 是输入向量。
- *y* 是输出向量。
- *E* 是描述符矩阵。
- *A* 是状态矩阵。
- *B* 是输入矩阵。
- *C* 是输出矩阵。
- *D* 是前馈矩阵或直接传输矩阵。

状态空间模型提供了一种紧凑且高效的方式来表示和分析
具有多输入和多输出的系统。该模型对于控制设计和
动态系统仿真特别有用。

您可以在工作区中定义矩阵，然后将这些工作区变量用作模块
参数。
