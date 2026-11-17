---
type: simulink-block
title: 'Tank (TL)'
family: 'hydro'
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
```yaml
ports:
- name: A
  summary: 液体端口 热液体
  direction: conserving
- name: B
  summary: 液体端口 热液体
  direction: conserving
- name: C
  summary: 液体端口 热液体
  direction: conserving
- name: D
  summary: 液体端口 热液体
  direction: conserving
- name: E
  summary: 液体端口 热液体
  direction: conserving
- name: F
  summary: 液体端口 热液体
  direction: conserving
- name: H
  summary: 流体温度 热液体
  direction: conserving
- name: P
  summary: 储罐压力，MPa 物理信号
  direction: input
- name: V
  summary: 液体体积，m^3 物理信号
  direction: output
- name: L
  summary: 液位，m 物理信号
  direction: output
- name: T
  summary: 流体温度，K 物理信号
  direction: output
```

### 守恒端口

### **A** — 液体端口 热液体

储罐入口。

### **B** — 液体端口 热液体

可选储罐入口。

#### 依赖关系

要启用此端口，请将 **Number of inlets** 设置为
`2`、`3`、
`4`、`5` 或
`6`。

### **C** — 液体端口 热液体

可选储罐入口。

#### 依赖关系

要启用此端口，请将 **Number of inlets** 设置为
`3`、`4`、
`5` 或
`6`。

### **D** — 液体端口 热液体

可选储罐入口。

#### 依赖关系

要启用此端口，请将 **Number of inlets** 设置为
`4`、`5` 或
`6`。

### **E** — 液体端口 热液体

可选储罐入口。

#### 依赖关系

要启用此端口，请将 **Number of inlets** 设置为
`5` 或
`6`。

### **F** — 液体端口 热液体

可选储罐入口。

#### 依赖关系

要启用此端口，请将 **Number of inlets** 设置为
`6`。

### **H** — 流体温度 热液体

储罐内的流体温度。
### 输入

### **P** — 储罐压力，`MPa` 物理信号

储罐压力，指定为物理信号输入，单位为 MPa。

#### 依赖关系

要启用此端口，请将 **Pressurization
specification** 设置为 `Variable
pressure`。
### 输出

### **V** — 液体体积，`m^3` 物理信号

储罐内的液体体积，单位为 `m^3`，指定为物理信号。

### **L** — 液位，`m` 物理信号

储罐内的液位，单位为 `m`，指定为物理信号。

### **T** — 流体温度，`K` 物理信号

储罐流体温度，单位为 `K`，指定为物理信号。
## 参数
```yaml
parameters:
- name: Number of inlets
  summary: 入口端口数量 1（默认）| 2 | 3 | 4 | 5 | 6
  group: ''
- name: Pressurization specification
  summary: 储罐压力指定方法 Atmospheric pressure（默认）| Specified pressure | Variable pressure
  group: ''
- name: Tank pressurization
  summary: 用户定义的储罐压力 0.101325 MPa（默认）| 正标量
  group: ''
- name: Tank volume parameterization
  summary: 储罐面积特性 Constant cross-section area（默认）| Tabulated data - volume vs. level
  group: ''
- name: Tank cross-sectional area
  summary: 储罐横截面积 1 m^2（默认）| 正标量
  group: ''
- name: Liquid level vector
  summary: 储罐流体液位向量 [0, 3, 5] m（默认）| 1×*n* 向量
  group: ''
- name: Liquid volume vector
  summary: 储罐流体液位向量 [0, 4, 6] m^3（默认）| 1×*n* 向量
  group: ''
- name: Inlet height
  summary: 入口端口高度 0.1 m（默认）| 正标量
  group: ''
- name: Inlet cross-sectional area
  summary: 端口入口的横截面积 0.01 m^2（默认）| 正标量
  group: ''
- name: Height vector for inlets A and B
  summary: 多个已启用端口的端口高度向量 [.1, .1] m（默认）| 1×*n* 向量
  group: ''
- name: Cross-sectional area vector for inlets A and B
  summary: 两个已启用端口的入口面积向量 [.01, .01] m^2（默认）| 1×*n* 向量
  group: ''
- name: Liquid level below inlet height
  summary: 是否通知低储罐液位 Error（默认）| Warning | None
  group: ''
- name: Liquid volume above max capacity
  summary: 是否通知高储罐体积 None（默认）| Warning | Error
  group: ''
- name: Maximum tank capacity
  summary: 储罐的填充限制 10 m^3（默认）| 正标量
  group: ''
- name: Gravitational acceleration
  summary: 重力加速度常数 9.81 m/s^2（默认）| 正标量
  group: ''
```

### **Number of inlets** — 入口端口数量 `1`（默认）| `2` | `3` | `4` | `5` | `6`

入口端口数量。将此参数设置为
`2` 或更多将暴露额外的输入
端口。

### **Pressurization specification** — 储罐压力指定方法 `Atmospheric pressure`（默认）| `Specified pressure` | `Variable pressure`

指定储罐压力的方法。要定义非大气恒定
压力，请将此参数设置为 `Specified
pressure`，并使用 **Tank
pressurization** 参数指定值。要指定可变储罐
压力，请将此参数设置为 `Variable pressure`，
并在端口 **P** 处以物理信号形式提供储罐压力。

### **Tank pressurization** — 用户定义的储罐压力 `0.101325` MPa（默认）| 正标量

用户定义的储罐压力。

#### 依赖关系

要启用此参数，请将 **Pressurization
specification** 设置为 `Specified
pressure`。

### **Tank volume parameterization** — 储罐面积特性 `Constant cross-section area`（默认）| `Tabulated data - volume vs. level`

指定储罐面积特性。此参数用于确定
储罐中的液位。如果您想对具有
可变横截面积的储罐进行建模，可以使用 `Tabulated data - volume vs.
level` 选项提供储罐体积和
液位的数据。

### **Tank cross-sectional area** — 储罐横截面积 `1` m^2（默认）| 正标量

储罐横截面积。

#### 依赖关系

要启用此参数，请将 **Tank volume
parameterization** 设置为 `Constant cross-section
area`。

### **Liquid level vector** — 储罐流体液位向量 `[0, 3, 5]` m（默认）| 1×*n* 向量

用于非恒定储罐面积表格参数化的储罐流体液位
向量。此向量中的值与
**Volumetric flow rate vector** 参数中的值一一对应。
其元素按升序列出。元素必须为正，
且第一个元素必须为 0。

#### 依赖关系

要启用此参数，请将 **Tank volume
parameterization** 设置为 `Tabulated data - volume
vs. level`。

### **Liquid volume vector** — 储罐流体液位向量 `[0, 4, 6]` m^3（默认）| 1×*n* 向量

用于非恒定储罐面积表格参数化的储罐流体液位
向量。此向量中的值与
**Volumetric flow rate vector** 参数中的值一一对应。
其元素按升序列出。元素必须为正，
且第一个元素必须为 0。

#### 依赖关系

要启用此参数，请将 **Tank volume
parameterization** 设置为 `Tabulated data - volume
vs. level`。

### **Inlet height** — 入口端口高度 `0.1` m（默认）| 正标量

入口端口高度。该值必须大于或等于 0。

#### 依赖关系

要启用此参数，请将 **Number of inlets** 设置为
`1`。

### **Inlet cross-sectional area** — 端口入口的横截面积 `0.01` m^2（默认）| 正标量

端口入口的横截面积。该值必须大于
0。

### **Height vector for inlets A and B** — 多个已启用端口的端口高度向量 `[.1, .1]` m（默认）| 1×*n* 向量

多个已启用端口的端口高度向量。如果您启用了两个或更多
端口，**Inlet height** 参数将变为
一个值向量，对应于每个入口端口的高度，从端口
**A** 开始。参数名称和向量长度
取决于 **Number of inlets** 参数的值。
每个入口的默认高度为 `.1 m`。此向量的每个元素
必须大于或等于 0。

#### 依赖关系

要启用此参数，请将 **Number of inlets** 设置为
`2`、`3`、
`4`、`5` 或
`6`。

### **Cross-sectional area vector for inlets A and B** — 两个已启用端口的入口面积向量 `[.01, .01]` m^2（默认）| 1×*n* 向量

多个已启用端口的横截面积向量。如果您启用了
两个或更多端口，**Inlet cross-sectional
area** 参数将变为一个值向量，对应于
每个入口的横截面积，从端口
**A** 开始。参数名称将包含所有已启用
端口。此向量的每个元素必须大于 0。

#### 依赖关系

要启用此参数，请将 **Number of inlets** 设置为
`2`、`3`、
`4`、`5` 或
`6`。

### **Liquid level below inlet height** — 是否通知低储罐液位 `Error`（默认）| `Warning` | `None`

是否在仿真期间储罐流体液位降至端口入口
高度以下时发出通知。如果您希望在仿真期间发生此情况时
收到警告，请将此参数设置为
`Warning`。如果您希望在发生此情况时
停止仿真，请将此参数设置为
`Error`。

### **Liquid volume above max capacity** — 是否通知高储罐体积 `None`（默认）| `Warning` | `Error`

是否在仿真期间储罐流体体积升至储罐
最大容量以上时发出通知。如果您希望在仿真期间发生此情况时
收到警告，请将此参数设置为
`Warning`。如果您希望在发生此情况时
停止仿真，请将此参数设置为
`Error`。

### **Maximum tank capacity** — 储罐的填充限制 `10` m^3（默认）| 正标量

储罐的填充限制。

#### 依赖关系

要启用此参数，请将 **Liquid volume above max
capacity** 设置为以下之一：

- `Warning`
- `Error`

### **Gravitational acceleration** — 重力加速度常数 `9.81` m/s^2（默认）| 正标量

重力加速度常数。
## 所属库

Simscape / Fluids / Thermal Liquid / Tanks & Accumulators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2023b：指定可变压力

您现在可以为 Tank
(TL) 模块指定可变储罐加压。当您将 **Pressurization
specification** 设置为 `Variable pressure` 时，
该模块在动态压力方程中使用端口 **P** 处物理信号的值。

## 描述

具有可变流体体积的热液体容器

Tank (TL) 模块对具有可变流体体积的热液体容器进行建模。假设罐内流体体积的绝对压力恒定，并等于模块对话框中指定的值。在罐加压等于大气压的特殊情况下，该模块表示通风罐。

该罐可以与其周围环境交换能量，从而使内部温度和压力随时间演变。将端口 **H** 连接到其他热模块，以对与环境的热传递或通过罐壁的热传导进行建模。

**罐示意图**

该罐最多可以有六个输入端口，**A** 到 **F**。罐入口处的压力是模块对话框中指定的恒定罐加压与由入口高度引起的静水压力之和。端口 **H** 处的温度是罐内流体体积的温度。

### 罐体积

罐内流体体积根据每个时间步的总流体质量计算：

V=Mρ，

其中：

- *V* 是罐内流体体积。
- *M* 是罐内流体质量。
- *ρ* 是罐内流体密度。

### 质量平衡

罐内流体体积中的质量守恒方程为

M˙=m˙A+m˙B+m˙C+m˙D+m˙E+m˙F，

其中：

- M˙ 是流体质量的变化。
- m˙η 表示通过端口 **η** 进入罐内流体体积的质量流量。

### 动量平衡

对于端口 **η**，其中 η=A,B,C,D,E,F，罐内流体体积中的动量守恒方程为

pη+pdyn=pRef+ρg(y−yη)，

其中：

- *pη* 是入口 **η** 处的流体压力。
- *pRef* 是恒定罐加压。
- *pdyn* 是动压：

  pdyn={0,m˙η≥0m˙η22ρηSIA2,m˙η<0

  当流动方向为进入罐内时，进入的射流耗散到大的流体体积中，失去动量，并使 *pdyn* 为 `0`。当流体流出罐时，体积中的流体加速进入端口，并使 *pdyn* 大于 `0`。
- *ρη* 是端口 **η** 处的液体密度。
- *SIA* 是罐入口面积。
- *g* 是重力常数。
- *y* 是相对于罐底的罐液位，即高度。
- *yη* 是相对于罐底的罐入口高度。

### 能量平衡

罐内流体体积中的能量守恒方程为

M(Cp−hα)T˙=ϕA+ϕB+ϕC+ϕD+ϕE+ϕF−(m˙A+m˙B+m˙C+m˙D+m˙E+m˙F+MαT˙)h+Q，

其中：

- *Cp* 是流体热容量。
- *α* 是流体等压体积模量。
- *T* 是流体温度。
- *Φη* 表示通过端口 **η** 进入罐的能量流率。
- *h* 是流体焓。
- *Q* 是通过端口 **H** 进入罐的热能流率。
