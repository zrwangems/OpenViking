---
type: simulink-block
title: 'Permanent Magnet'
family: 'magnetic'
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

### 守恒

### **N** — 北端子磁性

与北端子关联的磁性守恒端口。

### **S** — 南端子磁性

与南端子关联的磁性守恒端口。

## 参数

### **横截面积** — 磁体的横截面积 `25 mm^2`（默认） | positive scalar

磁体的横截面积。

### **磁体长度** — 磁体长度 `0.02 m`（默认） | positive scalar

磁体的长度。

### **剩余磁场参数化** — 剩余磁场参数化的方法 `Remanent flux density and relative permeability`（默认） | `Remanent flux density and coercivity` | `Relative permeability and coercivity`

用于参数化线性 *B*-*H* 关系的方法。

### **材料相对磁导率** — 相对磁导率 `1.05`（默认） | positive scalar

材料的相对磁导率。

#### 依赖关系

要启用此参数，请将 **剩余磁场参数化** 设置为 `Remanent flux density and relative permeability` 或 `Relative permeability and coercivity`。

### **磁体剩余磁通密度** — 剩余磁通密度 `1.2 T`（默认） | positive scalar

移除外部磁场后磁体的磁通密度。

#### 依赖关系

要启用此参数，请将 **剩余磁场参数化** 设置为 `Remanent flux density and relative permeability` 或 `Remanent flux density and coercivity`。

### **磁体矫顽力** — 磁体矫顽力 `1.2 / 1.05 / (4*pi*1e-7) A/m`（默认） | positive scalar

磁体的矫顽力。

#### 依赖关系

要启用此参数，请将 **剩余磁场参数化** 设置为 `Remanent flux density and coercivity` 或 `Relative permeability and coercivity`。

## 所属库

Simscape / Foundation Library / Magnetic / Magnetic Elements

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

被动生成磁场的永磁体

Permanent Magnet 模块对被动生成磁场的组件进行建模。使用此模块对不会磁化或退磁的磁体进行建模。永磁体的磁场具有随外部磁场强度增加而线性增加的磁通密度。

Permanent Magnet 模块等效于并联的 Flux Source 模块和 Reluctance 模块，或者串联的 MMF Source 模块和 Reluctance 模块。要根据制造商的剩余磁通密度、磁导率或矫顽力规格来参数化磁体，请使用 Permanent Magnet 模块。

### 方程

当将 Permanent Magnet 模块置于外部磁场中时，该模块使用以下线性关系之一来近似合成磁场的磁通密度 *B*：

B=Br+μmμ0H

B=BrHc(Hc+H)

B=μmμ0(Hc+H)

其中：

- *B*r 是 **磁体剩余磁通密度** 参数。
- *μ*m 是 **材料相对磁导率** 参数。
- μ0 是真空中的磁导率。
- *H* 是外部磁场的强度。
- *H*c 是 **磁体矫顽力** 参数。

使用 **剩余磁场参数化** 参数指定模块使用哪些参数来定义线性方程。

仅当磁体不磁化或退磁时，该线性关系才有效。该模块在 *B*-*H* 曲线的第二象限中运行：

- *B* ≥ 0
- *H* ≤ 0

流过磁体的磁通量 *φ* 定义为：

*φ* = *A**B*,

其中 *A* 是 **横截面积** 参数。

模块两端的磁动势 (mmf) 定义为：

*MMF* = *H**l*,

其中 *l* 是 **磁体长度** 参数。

模块两端的 mmf 定义为：

*MMF* = *MMF(N)* - *MMF(S)*,

其中 *N* 和 *S* 分别是永磁体的北端子和南端子。当磁通从北端子通过器件流向南端子时，磁通为正。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **初始目标** 部分。有关详细信息，请参阅“设置模块变量的优先级和初始目标”。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **标称值** 部分。有关详细信息，请参阅“修改模块变量的标称值”。
