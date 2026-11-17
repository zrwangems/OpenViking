---
type: simulink-block
title: 'Laminar Leakage (IL)'
family: 'isothermal-liquid'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Elements'
documentation_page: 'laminarleakageil'
documentation_source_path: 'ref/laminarleakageil.html'
language: zh-CN
chinese_source: worker-translation
---

# Laminar Leakage (IL)

## 端口

### 守恒

### **A** — 入口或出口等温液体

与层流泄漏的入口或出口关联的等温液体守恒端口。此模块没有固有方向性。

### **B** — 入口或出口等温液体

与层流泄漏的入口或出口关联的等温液体守恒端口。此模块没有固有方向性。

## 参数

### **横截面几何** — 选择泄漏横截面的形状 `Circular`（默认）| `Annular` | `Rectangular` | `Elliptical` | `Equilateral triangular` | `Custom`

选择横截面形状，然后根据所选选项指定其他参数值。

### **直径** — 圆形横截面的直径 `1e-3 m`（默认）| 正标量

圆形横截面的直径。

#### 依赖项

当 **横截面几何** 参数设置为 `Circular` 时启用。

### **内径** — 环形横截面的内径 `5e-4 m`（默认）| 正标量

环形横截面的内径。

#### 依赖项

当 **横截面几何** 参数设置为 `Annular` 时启用。

### **外径** — 环形横截面的外径 `1e-3 m`（默认）| 正标量

环形横截面的外径。

#### 依赖项

当 **横截面几何** 参数设置为 `Annular` 时启用。

### **宽度** — 矩形横截面的宽度 `1e-3 m`（默认）| 正标量

矩形横截面的宽度。

#### 依赖项

当 **横截面几何** 参数设置为 `Rectangular` 时启用。

### **高度** — 矩形横截面的高度 `0.1 m`（默认）| 正标量

矩形横截面的高度。

#### 依赖项

当 **横截面几何** 参数设置为 `Rectangular` 时启用。

### **长轴** — 椭圆形横截面的长轴 `1e-3 m`（默认）| 正标量

椭圆形横截面的长轴。

#### 依赖项

当 **横截面几何** 参数设置为 `Elliptical` 时启用。

### **短轴** — 椭圆形横截面的短轴 `5e-4 m`（默认）| 正标量

椭圆形横截面的短轴。

#### 依赖项

当 **横截面几何** 参数设置为 `Elliptical` 时启用。

### **边长** — 等边三角形横截面的三角形边长 `1e-3 m`（默认）| 正标量

等边三角形横截面的三角形边长。

#### 依赖项

当 **横截面几何** 参数设置为 `Equilateral triangular` 时启用。

### **纵向长度** — 流道的长度 `5 m`（默认）| 正标量

流道的长度。

### **线性压力-流量阻力** — 压力损失与质量流量之比 1e3 s\*MPa/m^3（默认）| 正标量

压力损失与质量流量之比。如果横截面几何未知，该模块用作线性液压阻力。

#### 依赖项

当 **横截面几何** 参数设置为 `Custom` 时启用。

## 所属库

Simscape / Foundation Library / Isothermal Liquid / Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体元件，用于对各种几何结构建模层流泄漏流动

Laminar Leakage (IL) 模块对等温液体网络中的层流进行建模。该模块包括若干常见的流道几何结构和自定义几何结构。选择一个 **横截面几何** 参数值，然后根据所选选项指定其他参数值：

- `Circular` — 提供直径和纵向长度。
- `Annular` — 提供内径、外径和纵向长度。
- `Rectangular` — 提供宽度、高度和纵向长度。
- `Elliptical` — 提供长轴、短轴和纵向长度。
- `Equilateral triangular` — 提供三角形边长和纵向长度。
- `Custom` — 提供流动阻力值，即压力损失与质量流量之比。在此配置中，该模块用作线性液压阻力。

流量计算基于 Hagen-Poiseuille 方程，该方程适用于充分发展的层流：

m˙A={KgeomνL(pA−pB),common geometriesρ¯R(pA−pB),custom

Kgeom={πd4128,circularπ128(do4−di4−(do2−di2)2log(do/di)),annularwh312(1−192hwπ5tanh(πw2h)),rectangularπ(ab)364(a2+b2),ellipticallside43320,triangular

ρ¯=ρA+ρB2

其中：

- m˙A 是通过端口 **A** 的质量流量。
- *p*A 和 *p*B 分别是端口 **A** 和 **B** 处的压力。
- *K*geom 是基于横截面几何计算得到的系数。
- *d* 是圆形横截面的直径。
- *d*o 是环形横截面的外径。
- *d*i 是环形横截面的内径。
- *w* 是矩形横截面的宽度。
- *h* 是矩形横截面的高度。
- *a* 是椭圆形横截面的长轴。
- *b* 是椭圆形横截面的短轴。
- *l*side 是三角形横截面的边长。
- *L* 是纵向长度。
- *R* 是自定义几何的线性液压阻力。
- *ν* 是大气压力下的液体运动黏度，它是由连接到回路的 Isothermal Liquid Properties (IL) 模块定义的全局参数。
- ρ¯ 是平均流体混合物密度。
- *ρ*A 和 *ρ*B 分别是端口 **A** 和 **B** 处的流体混合物密度值。用于计算流体混合物密度的方程取决于所选的等温液体模型。有关详细信息，请参阅 Isothermal Liquid Modeling Options。
