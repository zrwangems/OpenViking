---
type: simulink-block
title: 'Coordinate Transform (Five-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Mathematical Transforms'
documentation_page: 'coordinatetransformfivephase'
documentation_source_path: 'ref/coordinatetransformfivephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Coordinate Transform (Five-Phase)

## 端口

### 输入

### **abcde** — *a*、*b*、*c*、*d* 和 *e* 相分量向量

*abcde* 参考坐标系中五相系统的分量，指定为向量。

**数据类型：** `single` | `double`

### **θelec** — 旋转角度标量

旋转参考坐标系的角位置，指定为标量。

**数据类型：** `single` | `double`
### 输出

### **dqxy0** — 直轴、交轴、*x*、*y* 和零分量向量

旋转参考坐标系中系统的直轴、交轴、*x* 轴、*y* 轴和零分量，以向量形式返回。

**数据类型：** `single` | `double`

## 参数

### **Phase-a axis alignment** — *dqxy0* 参考坐标系对齐方式 `Q-axis`（默认）| `D-axis`

是否将 *abcde* 参考坐标系的 *a* 相向量对齐到旋转参考坐标系的 *d* 轴或 *q* 轴。

## 所属库

Simscape / Electrical / Control / Mathematical Transforms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

实现 abcde 到 dqxy0 变换

Coordinate Transform (Five-Phase) 模块将 *abcde* 参考坐标系中五相系统的时域分量转换为旋转参考坐标系中的直轴、交轴、*x*、*y* 和零分量。

您可以将该模块配置为在时间 *t* = 0 时将五相系统的 *a* 相轴对齐到旋转参考坐标系的 *d* 轴或 *q* 轴。

*θ = ωt + Offset* 是 *q* 轴对齐时 *a* 轴与 *q* 轴之间的角度，或 *d* 轴对齐时 *a* 轴与 *d* 轴之间的角度，其中：

- *ω* 是旋转参考坐标系的旋转速度。
- *t* 是距初始对齐的时间，单位为 s。
- Offset=π2,d−axis alignment0,q−axis alignment

### 方程

Coordinate Transform (Five-Phase) 模块将变换实现为

[dqxy0]=25[sinθsin(θ−2π5)sin(θ−4π5)sin(θ+4π5)sin(θ+2π5)cosθcos(θ−2π5)cos(θ−4π5)cos(θ+4π5)cos(θ+2π5)sinθsin(θ+4π5)sin(θ−2π5)sin(θ+2π5)sin(θ−4π5)cosθcos(θ+4π5)cos(θ−2π5)cos(θ+2π5)cos(θ−4π5)1212121212][abcde]
