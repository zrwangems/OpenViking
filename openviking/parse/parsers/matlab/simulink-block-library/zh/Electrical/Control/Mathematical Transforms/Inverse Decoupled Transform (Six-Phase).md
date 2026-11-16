---
type: simulink-block
title: 'Inverse Decoupled Transform (Six-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Mathematical Transforms'
documentation_page: 'inversedecoupledtransformsixphase'
documentation_source_path: 'ref/inversedecoupledtransformsixphase.html'
language: zh-CN
chinese_source: worker-translation
---

# Inverse Decoupled Transform (Six-Phase)

## 端口

### 输入

### **dqz1z2o1o2** — 直轴、交轴、*z1*、*z2*、*o1* 和 *o2* 分量向量

旋转参考坐标系中系统的直轴、交轴、*z1* 轴、*z2* 轴、*o1* 轴和 *o2* 轴分量，指定为向量。

**数据类型：** `single` | `double`

### **θelec** — 旋转角度标量

旋转参考坐标系的角度位置，指定为标量。

**数据类型：** `single` | `double`
### 输出

### **abc** — *a*、*b* 和 *c* 相分量向量

三相系统在 *abc* 参考坐标系中的分量，返回为向量。

**数据类型：** `single` | `double`

### **xyz** — *x*、*y* 和 *z* 相分量向量

三相系统在 *xyz* 参考坐标系中的分量，返回为向量。

**数据类型：** `single` | `double`

## 参数

### **a 相轴对齐** — *dqz1z2o1o2* 参考坐标系对齐 `Q-axis`（默认）| `D-axis`

是否将 *abc* 参考坐标系的 *a* 相向量与旋转参考坐标系的 *d* 轴或 *q* 轴对齐。

## 所属库

Simscape / Electrical / Control / Mathematical Transforms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

实现 dqz 1 z 2 o 1 o 2 到 abc 和 xyz 变换

Inverse Decoupled Transform (Six-Phase) 模块将旋转参考坐标系中的直轴、交轴、*z1*、*z2*、*o1* 和 *o2* 分量转换为 *abc* 和 *xyz* 参考坐标系中的六相系统分量。三相系统 *abc* 和 *xyz* 在空间上偏移 30 electrical degrees。

您可以配置该模块，以在时间 *t* = 0 时使五相系统的 a 相轴与旋转参考坐标系的 *d* 轴或 *q* 轴对齐。

*θ = ωt + Offset* 是 *q* 轴对齐时 *a* 轴与 *q* 轴之间的角度，或 *d* 轴对齐时 *a* 轴与 *d* 轴之间的角度，其中：

- *ω* 是旋转参考坐标系的旋转速度。
- *t* 是自初始对齐起的时间，单位为 s。
- Offset=0,     d−axis alignment−π2,     q−axis alignment

### 方程

Inverse Decoupled Transform (Six-Phase) 模块按如下方式实现该变换

[abcxyz]=[cosθ−sinθ1010cos(θ−2π3)−sin(θ−2π3)−12−3210cos(θ+2π3)−sin(θ+2π3)−123210cos(θ−π6)−sin(θ−π6)−321201cos(θ−5π6)−sin(θ−5π6)321201cos(θ+π2)−sin(θ+π2)0−101][dqz1z2o1o2]

*z1*–*z2* 和 *o1*–*o2* 对不形成旋转磁势。它们为广义零序分量。
