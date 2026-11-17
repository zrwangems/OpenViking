---
type: simulink-block
title: 'Park Transform'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Mathematical Transforms'
documentation_page: 'parktransform'
documentation_source_path: 'ref/parktransform.html'
language: zh-CN
chinese_source: worker-translation
---

# Park Transform

## 端口

### 输入

### **abc** — *a*、*b* 和 *c* 相分量向量

*abc* 参考坐标系中三相系统的分量。

**数据类型：** `single` | `double`

### **θelec** — 旋转角度，弧度标量

旋转参考坐标系的角位置。该参数的值等于 *abc* 参考坐标系中 a 相向量到 *dq0* 参考坐标系初始对齐轴的极距。

**数据类型：** `single` | `double`
### 输出

### **dq0** — *d*-*q* 轴和零分量向量

旋转参考坐标系中系统的直轴分量、交轴分量和零分量。

**数据类型：** `single` | `double`

## 参数

### **Power Invariant** — 功率不变变换 off（默认）| on

用于保持 *abc* 参考坐标系有功功率和无功功率的选项。

### **Phase-a axis alignment** — *dq0* 参考坐标系对齐 `Q-axis`（默认）| `D-axis`

将 *abc* 参考坐标系的 *a* 相向量对齐到旋转参考坐标系的 *d* 轴或 *q* 轴。

## 所属库

Simscape / Electrical / Control / Mathematical Transforms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

实现 abc 到 dq0 变换

Park Transform 模块将 *abc* 参考坐标系中三相系统的时域分量转换为旋转参考坐标系中的直轴、交轴和零分量。该模块可以通过实现 Park 变换的不变版本，保持有功功率和无功功率与 *abc* 参考坐标系中系统功率一致。对于平衡系统，零分量等于零。

您可以将该模块配置为在时间 *t* = 0 时将三相系统的 *a* 轴对齐到旋转参考坐标系的 *d* 轴或 *q* 轴。图中显示了 *abc* 参考坐标系和旋转 *dq0* 参考坐标系中定子绕组磁轴的方向，其中：

- *a* 轴和 *q* 轴初始对齐。
- *a* 轴和 *d* 轴初始对齐。

在两种情况下，角度 *θ* = *ω**t*，其中：

- *θ* 对于 *q* 轴对齐是 *a* 轴和 *q* 轴之间的角度，对于 *d* 轴对齐是 *a* 轴和 *d* 轴之间的角度。
- *ω* 是 *d*-*q* 参考坐标系的旋转速度。
- *t* 是从初始对齐开始的时间，单位为 s。

图中显示了等效平衡 *abc* 和 *dq0* 各分量的时间响应，针对：

- *a* 相向量对齐到 *q* 轴
- *a* 相向量对齐到 *d* 轴

### 方程

Park Transform 模块实现 *a* 相到 *q* 轴对齐的变换为

[dq0]=23[sin(θ)sin(θ−2π3)sin(θ+2π3)cos(θ)cos(θ−2π3)cos(θ+2π3)121212][abc]，

其中：

- *a*、*b* 和 *c* 是 *abc* 参考坐标系中三相系统的分量。
- *d* 和 *q* 是旋转参考坐标系中两轴系统的分量。
- *0* 是静止参考坐标系中两轴系统的零分量。

对于功率不变的 *a* 相到 *q* 轴对齐，该模块使用以下方程实现变换：

[dq0]=23[sin(θ)sin(θ−2π3)sin(θ+2π3)cos(θ)cos(θ−2π3)cos(θ+2π3)121212][abc]。

对于 *a* 相到 *d* 轴对齐，该模块使用以下方程实现变换：

[dq0]=23[cos(θ)cos(θ−2π3)cos(θ+2π3)−sin(θ)−sin(θ−2π3)−sin(θ+2π3)121212][abc]。

该模块实现功率不变的 *a* 相到 *d* 轴对齐为

[dq0]=23[cos(θ)cos(θ−2π3)cos(θ+2π3)−sin(θ)−sin(θ−2π3)−sin(θ+2π3)121212][abc]。
