---
type: simulink-block
title: 'Permanent Magnet'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Magnetic / Magnetic Elements'
documentation_page: 'permanentmagnet'
documentation_source_path: 'ref/permanentmagnet.html'
language: zh-CN
chinese_source: worker-translation
---

# Permanent Magnet

## 端口

### 守恒端口

### **N** — 北极端子磁端口

与北极端子关联的磁守恒端口。

### **S** — 南极端子磁端口

与南极端子关联的磁守恒端口。

## 参数

### **Cross-sectional area** — 磁体横截面积 `25 mm^2`（默认）| 正标量

磁体的横截面积。

### **Length of magnet** — 磁体长度 `0.02 m`（默认）| 正标量

磁体的长度。

### **Remanent field parameterization** — 剩磁参数化方法 `Remanent flux density and relative permeability`（默认）| `Remanent flux density and coercivity` | `Relative permeability and coercivity`

用于参数化线性 *B*-*H* 关系的方法。

### **Relative magnetic permeability of material** — 相对磁导率 `1.05`（默认）| 正标量

材料的相对磁导率。

#### 依赖关系

要启用此参数，请将 **Remanent field parameterization** 设置为 `Remanent flux density and relative permeability` 或 `Relative permeability and coercivity`。

### **Remanent flux density of magnet** — 剩磁通密度 `1.2 T`（默认）| 正标量

移除外部磁场后磁体的磁通密度。

#### 依赖关系

要启用此参数，请将 **Remanent field parameterization** 设置为 `Remanent flux density and relative permeability` 或 `Remanent flux density and coercivity`。

### **Coercivity of magnet** — 磁体矫顽力 `1.2 / 1.05 / (4*pi*1e-7) A/m`（默认）| 正标量

磁体的矫顽力。

#### 依赖关系

要启用此参数，请将 **Remanent field parameterization** 设置为 `Remanent flux density and coercivity` 或 `Relative permeability and coercivity`。

## 所属库

Simscape / Foundation Library / Magnetic / Magnetic Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

被动生成磁场的永磁体

Permanent Magnet 模块对被动生成磁场的组件进行建模。使用此模块对不会磁化或退磁的磁体进行建模。永磁体的磁场具有磁通密度，该磁通密度随外部磁场强度的增加而线性增加。

Permanent Magnet 模块等效于并联的 Flux Source 模块和 Reluctance 模块，或串联的 MMF Source 模块和 Reluctance 模块。要根据制造商规格中的剩磁通密度、磁导率或矫顽力来参数化磁体，请使用 Permanent Magnet 模块。

### 方程

当 Permanent Magnet 模块受到外部磁场作用时，该模块使用以下线性关系之一来近似合成磁场的磁通密度 *B*：

B=Br+μmμ0H

B=BrHc(Hc+H)

B=μmμ0(Hc+H)

其中：

- *B*r 是 **Remanent flux density of magnet** 参数。
- *μ*m 是 **Relative magnetic permeability of material** 参数。
- μ0 是真空中的磁导率。
- *H* 是外部磁场的强度。
- *H*c 是 **Coercivity of magnet** 参数。

使用 **Remanent field parametrization** 参数指定模块使用哪些参数来定义线性方程。

该线性关系仅在磁体不发生磁化或退磁时有效。该模块工作在 *B*-*H* 曲线的第二象限：

- *B* ≥ 0
- *H* ≤ 0

流过磁体的磁通量 *φ* 定义为：

*φ* = *A**B*，

其中 *A* 是 **Cross-sectional area** 参数。

模块两端的磁动势（mmf）定义为：

*MMF* = *H**l*，

其中 *l* 是 **Length of magnet** 参数。

模块两端的 mmf 定义为：

*MMF* = *MMF(N)* - *MMF(S)*，

其中 *N* 和 *S* 分别是永磁体的北极端子和南极端子。当磁通从北极端子通过器件流向南极端子时，磁通为正。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
