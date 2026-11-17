---
type: simulink-block
title: 'Decoupled Transform (Six-Phase)'
family: 'control'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Mathematical Transforms'
documentation_page: 'decoupledtransformsixphase'
documentation_source_path: 'ref/decoupledtransformsixphase.html'
language: zh-CN
chinese_source: worker-translation
---

# Decoupled Transform (Six-Phase)

## 端口

### 输入

### **abc** — *a*-、*b*- 和 *c*-相分量向量

三相系统在 *abc* 参考坐标系中的分量，指定为向量。

**数据类型：** `single` | `double`

### **xyz** — *x*-、*y*- 和 *z*-相分量向量

三相系统在 *xyz* 参考坐标系中的分量，指定为向量。

**数据类型：** `single` | `double`

### **θelec** — 旋转角标量

旋转参考坐标系的角位置，指定为标量。

**数据类型：** `single` | `double`

### 输出

### **dqz1z2o1o2** — 直轴、交轴、*z1*、*z2*、*o1* 和 *o2* 分量向量

系统在旋转参考坐标系中的直轴、交轴、*z1*-、*z2*-、*o1*- 和 *o2*-轴分量，以向量形式返回。

**数据类型：** `single` | `double`

## 参数

### **Phase-a axis alignment** — *dqz1z2o1o2* 参考坐标系对齐 `Q-axis`（默认）| `D-axis`

是否将 *abc* 参考坐标系的 *a* 相向量对齐到旋转参考坐标系的 *d* 轴或 *q* 轴。

## 所属库

Simscape / Electrical / Control / Mathematical Transforms

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

实现 abc 和 xyz 到 dqz 1 z 2 o 1 o 2 变换

Decoupled Transform (Six-Phase) 模块将 *abc* 和 *xyz* 参考坐标系中的六相系统的时域分量转换为旋转参考坐标系中的直轴、交轴、*z1*、*z2*、*o1* 和 *o2* 分量。三相系统 *abc* 和 *xyz* 在空间上偏移 30 电角度。

您可以配置该模块，以在时间 *t* = 0 时将六相系统的 *a* 相轴对齐到旋转参考坐标系的 *d* 轴或 *q* 轴。

*θ = ωt + Offset* 是对于 *q* 轴对齐而言 *a* 轴与 *q* 轴之间的角度，或对于 *d* 轴对齐而言 *a* 轴与 *d* 轴之间的角度，其中：

- *ω* 是旋转参考坐标系的旋转速度。
- *t* 是距初始对齐的时间，单位为 s。
- Offset=0,     d−axis  alignment−π2,    q−axis  alignment

### 方程

Decoupled Transform (Six-Phase) 模块按如下方式实现该变换

[dqz1z2o1o2]=13[cosθcos(θ−2π3)cos(θ+2π3)cos(θ−π6)cos(θ−5π6)cos(θ+π2)−sinθ−sin(θ−2π3)−sin(θ+2π3)−sin(θ−π6)−sin(θ−5π6)−sin(θ+π2)1−12−12−323200−32321212−1111000000111][abcxyz]
