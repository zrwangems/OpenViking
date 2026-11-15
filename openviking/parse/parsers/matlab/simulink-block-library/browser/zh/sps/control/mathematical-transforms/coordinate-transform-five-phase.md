---
type: simulink-block
title: 'Coordinate Transform (Five-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Mathematical Transforms'
documentation_page: 'coordinatetransformfivephase'
documentation_source_path: 'ref/coordinatetransformfivephase.html'
language: zh-CN
chinese_source: official
---

# Coordinate Transform (Five-Phase)

## 端口

### 输入

### **abcde** — *a* 相、*b* 相、*c* 相、*d* 相和 *e* 相分量 向量

*abcde* 参考系中五相系统的分量，指定为向量。

**数据类型:** `single` | `double`

### **θelec** — 旋转角度 标量

旋转参考系的角位置，指定为标量。

**数据类型:** `single` | `double`
### 输出

### **dqxy0** — 直轴、交轴、*x* 轴、*y* 轴和零轴分量 向量

系统在旋转参考系中的直轴、交轴、*x* 轴、*y* 轴以及零轴分量，以向量形式返回。

**数据类型:** `single` | `double`

## 参数

### **a 相轴对齐** — *dqxy0* 参考系对齐 **Q 轴** (默认) | **D 轴**

是将 *abcde* 参考系的 *a* 相向量与旋转参考系的 *d* 轴还是 *q* 轴对齐。

## 所属库

Simscape / Electrical / Control / Mathematical Transforms

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2021a 中推出**

## 描述

实现 abcde 到 dqxy0 的变换

Coordinate Transform (Five-Phase) 模块将 *abcde* 参考系中五相系统的时域分量转换为旋转参考系中的直轴、交轴、*x* 轴、*y* 轴和零轴分量。

您可以将此模块配置为在时间 *t* = 0 时，使五相系统的 *a* 相轴与旋转参考系的 *d* 轴或 *q* 轴对齐。

*θ = ωt + Offset* 是 *a* 轴与 *q* 轴之间的角度（对于 *q* 轴对齐），或是 *a* 轴与 *d* 轴之间的角度（对于 *d* 轴对齐），其中：

- *ω* 是旋转参考系的转速。
- *t* 是从初始对齐算起的时间，以秒为单位。
- Offset=π2,d−axis alignment0,q−axis alignment

### 方程

Coordinate Transform (Five-Phase) 模块按如下方程实现变换

[dqxy0]=25[sinθsin(θ−2π5)sin(θ−4π5)sin(θ+4π5)sin(θ+2π5)cosθcos(θ−2π5)cos(θ−4π5)cos(θ+4π5)cos(θ+2π5)sinθsin(θ+4π5)sin(θ−2π5)sin(θ+2π5)sin(θ−4π5)cosθcos(θ+4π5)cos(θ−2π5)cos(θ+2π5)cos(θ−4π5)1212121212][abcde]
