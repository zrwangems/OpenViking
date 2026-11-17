---
type: simulink-block
title: 'Inverse Park Transform'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Mathematical Transforms'
documentation_page: 'inverseparktransform'
documentation_source_path: 'ref/inverseparktransform.html'
language: zh-CN
chinese_source: worker-translation
---

# Inverse Park Transform

## 端口
```yaml
ports:
- name: dq0
  summary: '*d*-*q* 轴和零分量向量'
  direction: input
  data_types: single | double
- name: θelec
  summary: 旋转角度，弧度标量
  direction: input
  data_types: single | double
- name: abc
  summary: '*a* 相、*b* 相和 *c* 相分量向量'
  direction: output
  data_types: single | double
```

### 输入

### **dq0** — *d*-*q* 轴和零分量向量

旋转参考系中系统的直轴分量、交轴分量和零分量。

**数据类型：** `single` | `double`

### **θelec** — 旋转角度，弧度标量

旋转参考系的角位置。此参数的值等于从 *abc* 参考系中 *a* 相向量到 *dq0* 参考系初始对齐轴的极距。

**数据类型：** `single` | `double`
### 输出

### **abc** — *a* 相、*b* 相和 *c* 相分量向量

*abc* 参考系中三相系统的分量。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Power Invariant
  summary: 功率不变变换 关（默认） | 开
  group: ''
- name: Phase-a axis alignment
  summary: '*dq0* 参考系对齐 Q-axis（默认） | D-axis'
  group: ''
```

### **Power Invariant** — 功率不变变换 关（默认） | 开

用于保持 *a**b**c* 参考系有功功率和无功功率的选项。

### **Phase-a axis alignment** — *dq0* 参考系对齐 `Q-axis`（默认） | `D-axis`

将 *abc* 参考系的 *a* 相向量对齐到旋转参考系的 *d* 轴或 *q* 轴。
## 所属库

Simscape / Electrical / Control / Mathematical Transforms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

实现 dq0 到 abc 变换

Inverse Park Transform 模块将旋转参考系中的时域直轴、交轴和零分量转换为 *a**b**c* 参考系中三相系统的分量。该模块可以通过实现 Park 变换的不变版本，保持有功功率和无功功率与旋转参考系中系统功率一致。对于平衡系统，零分量等于零。

您可以配置该模块，使三相系统的 *a* 轴在时间 *t* = 0 时对齐到旋转参考系的 *d* 轴或 *q* 轴。图中显示了 *a**b**c* 参考系和旋转 *d*-*q* 参考系中定子绕组磁轴的方向，其中：

- *a* 轴和 *q* 轴初始对齐。
- *a* 轴和 *d* 轴初始对齐。

在两种情况下，角度 *θ* = *ω**t*，其中

- *θ* 是 *q* 轴对齐时 *a* 轴与 *q* 轴之间的角度，或 *d* 轴对齐时 *a* 轴与 *d* 轴之间的角度。
- *ω* 是 *d*-*q* 参考系的旋转速度。
- *t* 是从初始对齐开始的时间，单位为 s。

图中显示了等效平衡 *dq0* 和 *abc* 各分量的时间响应，针对以下情况：

- *a* 相向量对齐到 *q* 轴
- *a* 相向量对齐到 *d* 轴

### 定义方程

Inverse Park Transform 模块实现 *a* 相到 *q* 轴对齐的变换为

[abc]=[sin(θ)cos(θ)1sin(θ−2π3)cos(θ−2π3)1sin(θ+2π3)cos(θ+2π3)1][dq0]，

其中：

- *d* 和 *q* 是旋转参考系中双轴系统的分量。
- *a*、*b* 和 *c* 是 *a**b**c* 参考系中三相系统的分量。
- *0* 是静止参考系中双轴系统的零分量。

对于功率不变的 *a* 相到 *q* 轴对齐，该模块使用以下方程实现变换：

[abc]=23[sin(θ)cos(θ)12sin(θ−2π3)cos(θ−2π3)12sin(θ+2π3)cos(θ+2π3)12][dq0]。

对于 *a* 相到 *d* 轴对齐，该模块使用以下方程实现变换：

[abc]=[cos(θ)−sin(θ)1cos(θ−2π3)−sin(θ−2π3)1cos(θ+2π3)−sin(θ+2π3)1][dq0]。

该模块实现功率不变的 *a* 相到 *d* 轴对齐为

[abc]=23[cos(θ)−sin(θ)12cos(θ−2π3)−sin(θ−2π3)12cos(θ+2π3)−sin(θ+2π3)12][dq0]。
