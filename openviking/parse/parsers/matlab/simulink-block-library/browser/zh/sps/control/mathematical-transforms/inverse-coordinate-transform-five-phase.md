---
type: simulink-block
title: 'Inverse Coordinate Transform (Five-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Mathematical Transforms'
documentation_page: 'inversecoordinatetransformfivephase'
documentation_source_path: 'ref/inversecoordinatetransformfivephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Inverse Coordinate Transform (Five-Phase)

## 端口

### 输入

### **dqxy0** — 直轴、交轴、*x*、*y* 和零分量向量

旋转参考坐标系中系统的直轴、交轴、*x* 轴、*y* 轴和零分量，指定为向量。

**数据类型：** `single` | `double`

### **θelec** — 旋转角度标量

旋转参考坐标系的角度位置，指定为标量。

**数据类型：** `single` | `double`

### 输出

### **abcde** — *a*、*b*、*c*、*d* 和 *e* 相分量向量

五相系统在 *abcde* 参考坐标系中的分量，以向量形式返回。

**数据类型：** `single` | `double`

## 参数

### **Phase-a axis alignment** — *dqxy0* 参考坐标系对齐 `Q-axis` (default) | `D-axis`

是否将 *abcde* 参考坐标系的 *a* 相向量对齐到旋转参考坐标系的 *d*-axis 或 *q*-axis。

## 所属库

Simscape / Electrical / Control / Mathematical Transforms

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

实现 dqxy0 到 abcde 变换

Inverse Coordinate Transform (Five-Phase) 模块将旋转参考坐标系中的时域直轴、交轴、*x*、*y* 和零分量转换为 *abcde* 参考坐标系中五相系统的分量。

您可以配置该模块，以在时间 *t* = 0 时将五相系统的 *a*-axis 对齐到旋转参考坐标系的 *d*-axis 或 *q*-axis。

*θ = ωt + Offset* 是 *q*-axis alignment 时 *a* 与 *q* 轴之间的角度，或 *d*-axis alignment 时 *a* 与 *d* 轴之间的角度，其中：

- *ω* 是旋转参考坐标系的旋转速度。
- *t* 是从初始对齐开始的时间，单位为 s。
- Offset=​π2,      d−axis alignment 0,        q−axis alignment

### 方程

Inverse Coordinate Transform (Five-Phase) 模块将变换实现为

[abcde]=[sinθcosθsinθcosθ12sin(θ−2π5)cos(θ−2π5)sin(θ+4π5)cos(θ+4π5)12sin(θ−4π5)cos(θ−4π5)sin(θ−2π5)cos(θ−2π5)12sin(θ+4π5)cos(θ+4π5)sin(θ+2π5)cos(θ+2π5)12sin(θ+2π5)cos(θ+2π5)sin(θ−4π5)cos(θ−4π5)12][dqxy0]
