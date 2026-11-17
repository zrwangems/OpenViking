---
type: simulink-block
title: 'Tank (TL)'
family: 'thermal-liquid'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Tanks & Accumulators'
documentation_page: 'tanktl'
documentation_source_path: 'ref/tanktl.html'
language: zh-CN
chinese_source: worker-translation
---

# Tank (TL)

## 端口

### 守恒

### **A** — 液体端口 thermal liquid

储罐入口。

### **B** — 液体端口 thermal liquid

可选储罐入口。

#### 依赖关系

要启用此端口，请将 **Number of inlets** 设置为 `2`、`3`、`4`、`5` 或 `6`。

### **C** — 液体端口 thermal liquid

可选储罐入口。

#### 依赖关系

要启用此端口，请将 **Number of inlets** 设置为 `3`、`4`、`5` 或 `6`。

### **D** — 液体端口 thermal liquid

可选储罐入口。

#### 依赖关系

要启用此端口，请将 **Number of inlets** 设置为 `4`、`5` 或 `6`。

### **E** — 液体端口 thermal liquid

可选储罐入口。

#### 依赖关系

要启用此端口，请将 **Number of inlets** 设置为 `5` 或 `6`。

### **F** — 液体端口 thermal liquid

可选储罐入口。

#### 依赖关系

要启用此端口，请将 **Number of inlets** 设置为 `6`。

### **H** — 流体温度 thermal liquid

储罐内部流体温度。
### 输入

### **P** — 储罐压力，`MPa` 物理信号

储罐压力，指定为物理信号输入，单位为 MPa。

#### 依赖关系

要启用此端口，请将 **Pressurization specification** 设置为 `Variable pressure`。
### 输出

### **V** — 液体体积，`m^3` 物理信号

储罐内部液体体积，单位为 `m^3`，指定为物理信号。

### **L** — 液位，`m` 物理信号

储罐内部液位，单位为 `m`，指定为物理信号。

### **T** — 流体温度，`K` 物理信号

储罐流体温度，单位为 `K`，指定为物理信号。

## 参数

### **Number of inlets** — 入口端口数量 `1` (默认) | `2` | `3` | `4` | `5` | `6`

入口端口数量。将此参数设置为 `2` 或更大值会显示额外的输入端口。

### **Pressurization specification** — 储罐压力指定方法 `Atmospheric pressure` (默认) | `Specified pressure` | `Variable pressure`

指定储罐压力的方法。要定义非大气压的恒定压力，请将此参数设置为 `Specified pressure`，并使用 **Tank pressurization** 参数指定该值。要指定可变储罐压力，请将此参数设置为 `Variable pressure`，并在端口 **P** 处将储罐压力作为物理信号提供。

### **Tank pressurization** — 用户定义的储罐压力 `0.101325` MPa (默认) | positive scalar

用户定义的储罐压力。

#### 依赖关系

要启用此参数，请将 **Pressurization specification** 设置为 `Specified pressure`。

### **Tank volume parameterization** — 储罐面积特性 `Constant cross-section area` (默认) | `Tabulated data - volume vs. level`

指定储罐面积特性。此参数用于确定储罐中的流体液位。如果要对具有可变横截面积的储罐建模，可以使用 `Tabulated data - volume vs. level` 选项提供储罐体积和流体液位数据。

### **Tank cross-sectional area** — 储罐横截面积 `1` m^2 (默认) | positive scalar

储罐横截面积。

#### 依赖关系

要启用此参数，请将 **Tank volume parameterization** 设置为 `Constant cross-section area`。

### **Liquid level vector** — 储罐流体液位向量 `[0, 3, 5]` m (默认) | 1-by-*n* vector

用于非常数储罐面积的表格化参数化的储罐流体液位向量。此向量中的值与 **Volumetric flow rate vector** 参数中的值一一对应。其元素按升序列出。元素必须为正，且第一个元素必须为 0。

#### 依赖关系

要启用此参数，请将 **Tank volume parameterization** 设置为 `Tabulated data - volume vs. level`。

### **Liquid volume vector** — 储罐流体液位向量 `[0, 4, 6]` m^3 (默认) | 1-by-*n* vector

用于非常数储罐面积的表格化参数化的储罐流体液位向量。此向量中的值与 **Volumetric flow rate vector** 参数中的值一一对应。其元素按升序列出。元素必须为正，且第一个元素必须为 0。

#### 依赖关系

要启用此参数，请将 **Tank volume parameterization** 设置为 `Tabulated data - volume vs. level`。

### **Inlet height** — 入口端口高度 `0.1` m (默认) | positive scalar

入口端口的高度。该值必须大于或等于 0。

#### 依赖关系

要启用此参数，请将 **Number of inlets** 设置为 `1`。

### **Inlet cross-sectional area** — 端口入口的横截面积 `0.01` m^2 (默认) | positive scalar

端口入口的横截面积。该值必须大于 0。

### **Height vector for inlets A and B** — 多个已启用端口的端口高度向量 `[.1, .1]` m (默认) | 1-by-*n* vector

多个已启用端口的端口高度向量。如果启用了两个或更多端口，**Inlet height** 参数将变为值向量，这些值对应于每个入口端口的高度，从端口 **A** 开始。参数名称和向量长度取决于 **Number of inlets** 参数的值。每个入口的默认高度为 `.1 m`。此向量的每个元素必须大于或等于 0。

#### 依赖关系

要启用此参数，请将 **Number of inlets** 设置为 `2`、`3`、`4`、`5` 或 `6`。

### **Cross-sectional area vector for inlets A and B** — 两个已启用端口的入口面积向量 `[.01, .01]` m^2 (默认) | 1-by-*n* vector

多个已启用端口的横截面积向量。如果启用了两个或更多端口，**Inlet cross-sectional area** 参数将变为值向量，这些值对应于每个入口的横截面积，从端口 **A** 开始。参数名称将包含所有已启用端口。此向量的每个元素必须大于 0。

#### 依赖关系

要启用此参数，请将 **Number of inlets** 设置为 `2`、`3`、`4`、`5` 或 `6`。

### **Liquid level below inlet height** — 是否在储罐液位过低时收到通知 `Error` (默认) | `Warning` | `None`

是否在仿真期间储罐流体液位降至端口入口高度以下时收到通知。如果希望在此仿真期间发生此情况时收到警告，请将此参数设置为 `Warning`。如果希望在此情况发生时停止仿真，请将此参数设置为 `Error`。

### **Liquid volume above max capacity** — 是否在储罐体积过高时收到通知 `None` (默认) | `Warning` | `Error`

是否在仿真期间储罐流体体积升至储罐最大容量以上时收到通知。如果希望在此仿真期间发生此情况时收到警告，请将此参数设置为 `Warning`。如果希望在此情况发生时停止仿真，请将此参数设置为 `Error`。

### **Maximum tank capacity** — 储罐的填充限制 `10` m^3 (默认) | positive scalar

储罐的填充限制。

#### 依赖关系

要启用此参数，请将 **Liquid volume above max capacity** 设置为以下之一：

- `Warning`
- `Error`

### **Gravitational acceleration** — 重力加速度常数 `9.81` m/s^2 (默认) | positive scalar

重力加速度常数。

## 所属库

Simscape / Fluids / Thermal Liquid / Tanks & Accumulators

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2023b：指定可变压力

现在可以为 Tank (TL) 模块指定可变储罐加压。将 **Pressurization specification** 设置为 `Variable pressure` 时，模块将在动态压力方程中使用端口 **P** 的物理信号值。

## 描述

具有可变流体体积的热液体容器

Tank (TL) 模块对具有可变流体体积的热液体容器进行建模。假定储罐流体体积的绝对压力恒定，并等于模块对话框中指定的值。在储罐加压等于大气压的特殊情况下，该模块表示通气储罐。

储罐可以与其周围环境交换能量，从而使内部温度和压力随时间变化。将端口 **H** 连接到其他热模块，以对与环境的热传递或通过储罐壁的热传导进行建模。

**储罐示意图**

储罐最多可具有六个输入端口，**A** 到 **F**。储罐入口处的压力是模块对话框中指定的恒定储罐加压与由入口高度引起的静水压力之和。端口 **H** 处的温度是储罐流体体积的温度。

### 储罐体积

储罐流体体积根据每个时间步的总流体质量计算：

V=Mρ,

其中：

- *V* 是储罐流体体积。
- *M* 是储罐流体质量。
- *ρ* 是储罐流体密度。

### 质量平衡

储罐流体体积中的质量守恒方程为

M˙=m˙A+m˙B+m˙C+m˙D+m˙E+m˙F,

其中：

- M˙ 是流体质量的变化。
- m˙η 表示通过端口 **η** 进入储罐流体体积的质量流量。

### 动量平衡

对于端口 **η**，其中 η=A,B,C,D,E,F，储罐流体体积中的动量守恒方程为

pη+pdyn=pRef+ρg(y−yη),

其中：

- *pη* 是入口 **η** 处的流体压力。
- *pRef* 是恒定储罐加压。
- *pdyn* 是动态压力：

  pdyn={0,m˙η≥0m˙η22ρηSIA2,m˙η<0

  当流动方向为流入储罐时，进入的射流耗散到大的流体体积中，失去动量，并使 *pdyn* 为 `0`。当流体流出储罐时，体积中的流体加速进入端口，并使 *pdyn* 大于 `0`。
- *ρη* 是端口 **η** 处的液体密度。
- *SIA* 是储罐入口面积。
- *g* 是重力常数。
- *y* 是相对于储罐底部的储罐液位或高度。
- *yη* 是相对于储罐底部的储罐入口高度。

### 能量平衡

储罐流体体积中的能量守恒方程为

M(Cp−hα)T˙=ϕA+ϕB+ϕC+ϕD+ϕE+ϕF−(m˙A+m˙B+m˙C+m˙D+m˙E+m˙F+MαT˙)h+Q,

其中：

- *Cp* 是流体热容量。
- *α* 是流体等压体积模量。
- *T* 是流体温度。
- *Φη* 表示通过端口 **η** 进入储罐的能量流率。
- *h* 是流体焓。
- *Q* 是通过端口 **H** 进入储罐的热能流率。
