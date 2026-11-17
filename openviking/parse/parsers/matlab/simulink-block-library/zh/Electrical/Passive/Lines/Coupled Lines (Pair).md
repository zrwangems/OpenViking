---
type: simulink-block
title: 'Coupled Lines (Pair)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Lines'
documentation_page: 'coupledlinespair'
documentation_source_path: 'ref/coupledlinespair.html'
language: zh-CN
chinese_source: worker-translation
---

# Coupled Lines (Pair)

## 端口

### 守恒端口

### **1+** — 线路 1 正极端子电气

与线路 1 正极端子关联的电气守恒端口。

### **1-** — 线路 1 负极端子电气

与线路 1 负极端子关联的电气守恒端口。

### **2+** — 线路 2 正极端子电气

与线路 2 正极端子关联的电气守恒端口。

### **2-** — 线路 2 负极端子电气

与线路 2 负极端子关联的电气守恒端口。

## 参数

#### 参数

### **Parameterization** — 线路阻抗参数化 `Balanced impedance`（默认）| `General impedance`

指定如何参数化两条线路的阻抗：

`Balanced impedance`
:   为两条线路指定相同的串联电阻、串联电感和并联泄漏电导。

`General impedance`
:   分别为每条线路指定串联电阻、串联电感和并联泄漏电导。

### **Line 1 inductance** — 线路 1 自感 `1e-3` `H`（默认）

线路 1 的自感。该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `General impedance`。

### **Line 2 inductance** — 线路 2 自感 `1e-3` `H`（默认）

线路 2 的自感。该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `General impedance`。

### **Line inductance** — 自感 `1e-3` `H`（默认）

线路 1 和线路 2 的自感。该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Balanced impedance`。

### **Mutual inductance** — 线路间互感 `3e-4` `H`（默认）

线路 1 和线路 2 之间的互感。如果已知耦合系数，请将此值设置为 kL1L2。要使互感在物理上可实现，该值必须满足：

−L1L2<Lm<L1L2。

### **Line 1 resistance** — 线路 1 串联电阻 `0.001` `Ohm`（默认）

线路 1 的串联电阻。该值必须大于或等于零。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `General impedance`。

### **Line 2 resistance** — 线路 2 串联电阻 `0.001` `Ohm`（默认）

线路 2 的串联电阻。该值必须大于或等于零。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `General impedance`。

### **Line resistance** — 串联电阻 `0.001` `Ohm`（默认）

线路 1 和线路 2 的串联电阻。该值必须大于或等于零。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Balanced impedance`。

### **Mutual resistance** — 线路间互阻 `0` `Ohm`（默认）

线路 1 和线路 2 之间的互阻。该值必须大于或等于零。使用此值可考虑公共返回路径中的损耗。

### **Line 1 leakage conductance** — 线路 1 并联泄漏电导 `1e-9` `1/Ohm`（默认）

线路 1 的并联泄漏电导。该值必须大于或等于零。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `General impedance`。

### **Line 2 leakage conductance** — 线路 2 并联泄漏电导 `1e-9` `1/Ohm`（默认）

线路 2 的并联泄漏电导。该值必须大于或等于零。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `General impedance`。

### **Line leakage conductance** — 并联泄漏电导 `1e-9` `1/Ohm`（默认）

线路 1 和线路 2 的并联泄漏电导。该值必须大于或等于零。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Balanced impedance`。

## 所属库

Simscape / Electrical / Passive / Lines

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

磁耦合两条线路

Coupled Lines (Pair) 模块对两条磁耦合线路进行建模。每条线路具有自感、串联电阻和并联电导。此外，两条线路之间还存在互感和互阻。

当两条线路之间的磁耦合不可忽略时，请使用此模块。这些效应在以下情况下最为显著：

- 线路平行且彼此靠近。
- 线路的自感较高。
- 网络的交流频率较高。

要对三相线路的磁耦合进行建模，请使用 Coupled Lines 模块。

### 等效电路

该图显示了一对耦合线路的等效电路。

其中：

- *R1* 和 *R2* 分别是线路 1 和线路 2 的串联电阻。
- *L1* 和 *L2* 分别是线路 1 和线路 2 的自感。
- *Rm* 是两条线路之间的互阻。您可以使用此参数来考虑公共返回路径中的损耗。
- *Lm* 是两条线路之间的互感。
- *G1* 和 *G2* 分别是线路 1 和线路 2 的泄漏电导。
- *V1* 和 *V2* 分别是线路 1 和线路 2 上的电压降。
- *I1* 和 *I2* 分别是流过电阻 *R1-Rm* 和 *R2-Rm* 的电流。

### 方程

此模块的定义方程为：

V=[R1RmRmR2]I+[L1LmLmL2]dIdt，

其中：

V=[V1V2]，

I=[I1I2]。

*I1* 和 *I2* 通常不等于线路 1 和线路 2 中的电流。这些端子电流构成向量：

Itotal=I+[G100G2]V。

### 电感耦合

要量化两条线路之间耦合的强度，可以使用耦合因子或耦合系数 *k*。耦合因子将互感与线路自感关联起来：

Lm=kL1L2。

该耦合因子必须落在 −1<k<1 范围内，其中负耦合因子表示其中一个线圈的取向反转。*k* 的大小表示：

- |k|=0 — 两条线路之间没有磁耦合。
- 0<|k|<0.5 — 两条线路为松耦合，互感磁效应较小。
- 0.5≤|k|<1 — 两条线路为强耦合，互感磁效应较大。

### 互阻

如果两条线路共享公共返回路径，您可以使用 **Mutual resistance** 参数对该返回路径的电阻进行建模。此工作流程等效于将 **Mutual resistance** 设置为零并显式建模返回路径电阻 *Rm*，如此图所示。

如果两条线路不共享公共返回路径，请将互阻参数设置为零，并显式建模每个返回电阻。
