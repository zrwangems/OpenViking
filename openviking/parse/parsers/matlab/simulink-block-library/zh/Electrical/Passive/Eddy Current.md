---
type: simulink-block
title: 'Eddy Current'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'eddycurrent'
documentation_source_path: 'ref/eddycurrent.html'
language: zh-CN
chinese_source: worker-translation
---

# Eddy Current

## 端口

### 守恒

### **N** — 北端子磁

与模块北端子关联的磁守恒端口。

### **S** — 南端子磁

与模块南端子关联的磁守恒端口。

### **H** — 热端口热

与模块热端口关联的热守恒端口。

#### 依赖

要启用此端口，请选择 **Show thermal port** 参数。

## 参数

### **Conductance of eddy current loop** — 涡流电导 `1` `1/Ohm`（默认）| 正数

涡流回路的电导，*Geddy*。该分量是电感在电气域中的磁域类比。

### **Parasitic series reluctance** — 串联磁阻 `1e-3` `1/H`（默认）| 非负数

涡流回路的寄生磁阻，R。

### **Parasitic parallel permeance** — 并联漏磁导 `1e-6` `H`（默认）| 非负数

并联漏磁路径的寄生磁导，P。为帮助某些电路拓扑中的仿真收敛，请将此参数设置为一个较小的值。

### **Show thermal port** — 热端口可见性 `Off`（默认）| `On`

是否启用模块的热端口。

### **Thermal mass** — 热质量 `0.1` `J/K`（默认）| 正数

模块的热质量。此参数对 Eddy Current 模块吸收和存储热能的能力进行建模。

#### 依赖

要启用此参数，请选择 **Show thermal port** 参数。

## 所属库

Simscape / Electrical / Passive

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

涡流损耗表示

Eddy Current 模块通过生成抵抗磁通变化的磁动势（MMF）来对涡流效应进行建模。此外，该模块使用串联磁阻和并联漏磁导对寄生效应进行建模，并使用可选的热端口 **H** 对热效应进行建模。

磁芯材料中的涡流由时变磁场引起。这些变化的场密度在材料内部感应出电压电势，使电流以闭合回路流动。此类电流通常是不期望的，并会导致磁性材料发热。

使用此模块可将磁域中的涡流损耗添加到自定义变压器或其他磁性组件中。

涡流分量有时被称为磁电感，因为它是电气域中电感器在磁域中的类比。

### 方程

这是该模块的等效磁路，包括涡流路径（底部）和并联漏磁路径（顶部）。

在图中：

- Φ 是端子处的总磁通。该磁通是涡流回路和并联漏磁路径的求和。
- Φ*L* 是通过涡流回路的磁通。

该模块计算端子 MMF，F，以及磁通，Φ，如下：

F=GeddydΦLdt+RΦLΦ=FP+ΦL

其中：

- *Geddy* 是涡流回路的电导。
- R 是涡流路径的寄生串联磁阻。
- P 是并联磁导。

由于寄生串联磁阻和并联磁导是无损的，模块上的总耗散功率为：

Pdiss=Geddy(dΦLdt)2

### 关联变压器电气模型和磁模型

在电气域中，涡流损耗使用跨初级绕组的并联电阻进行建模。这是非理想双绕组变压器的等效电路。

在图中：

- *Lp* 和 *Ls* 分别是初级绕组和次级绕组的自感。
- *Lm* 是两个绕组之间的互感。
- *Rm* 是两个绕组之间的互阻，由涡流损耗引起。

该双绕组变压器同样可以在磁域中表示。这是等效电路。

在图中：

- R*p* 和 R*s* 分别是与初级绕组和次级绕组关联的磁阻。
- R*g* 是与两个绕组的磁耦合关联的磁阻。
- *n* 是两个绕组之间的匝数比。

如果满足以下条件，则电气域和磁域电路等效：

Rg=n2Lm

Rp=n2Lp

Rs=1Ls

Geddy=n2Rm

您可以使用这些关系从一个域计算等效双绕组变压器在另一个域中的属性。
