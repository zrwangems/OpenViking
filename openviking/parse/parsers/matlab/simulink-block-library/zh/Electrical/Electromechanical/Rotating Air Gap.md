---
type: simulink-block
title: 'Rotating Air Gap'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical'
documentation_page: 'rotatingairgap'
documentation_source_path: 'ref/rotatingairgap.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotating Air Gap

## 端口

### 守恒

### **N** — 定子磁连接 magnetic

与定子关联的磁守恒端口。

### **S** — 转子磁连接 magnetic

与转子关联的磁守恒端口。

### **C** — 电机外壳 mechanical

与电机外壳关联的机械旋转守恒端口。

### **R** — 电机转子 mechanical

与电机转子关联的机械旋转守恒端口。

## 参数

### 主

### **Number of rotor pole pairs** — 转子极对数 `5`（默认）| 正标量

转子的极对数。此参数必须大于或等于 `1`，且小于 **Number of stator teeth** 参数的值。

### **Number of stator teeth** — 定子齿数 `9`（默认）| 正标量

定子的齿数。此参数必须大于或等于 `2`。

### **Stator tooth reference index** — 定子齿参考索引 `1`（默认）| 正标量

电机定子齿的参考索引。此参数必须介于 `1` 和 **Number of stator teeth** 参数的值之间。

例如，如果要建模一个具有九个定子极的电机，请创建此模块的九个副本，并将每个 Rotating Air Gap 模块的 **Stator tooth reference index** 参数分别设置为 `1`、`2`、`3`、`4`、`5`、`6`、`7`、`8` 和 `9`。

### **Peak magnet flux density** — 磁体转子的峰值磁通密度 `0.4` `T`（默认）| 正标量

与永磁转子关联的峰值磁通密度。磁通密度随转子角度呈正弦变化。

### **Permanent magnet length (in direction of flux)** — 沿电机径向的磁体长度 `5` `mm`（默认）| 正标量

磁体沿电机径向的长度，或者等效地，沿磁通方向的长度。此参数必须小于 **Rotor radius** 参数的值。

### **Permanent magnet relative permeability** — 永磁体相对磁导率 `1.05`（默认）| 标量

永磁体的相对磁导率。通常，应将此值设置为略大于 `1`，以反映永磁体中磁偶极子已经对齐。

### **Air gap** — 径向气隙 `1` `mm`（默认）| 正标量

径向气隙的长度。

### **Rotor radius** — 转子半径 `65` `mm`（默认）| 正标量

转子的半径。

### **Tooth depth (in direction of shaft)** — 定子齿深度 `50` `mm`（默认）| 正标量

定子齿沿旋转轴方向的长度。

### 故障

### **Enable faults** — 故障选项 `off`（默认）| `on`

是否模拟转子磁体强度退化的影响。

### **Flux multipliers for faulted rotor poles** — 用于降低转子极磁通的乘数 `ones(1,10)`（默认）| 向量

用于在故障时降低转子极磁通密度的乘数。此参数的值必须是一个向量，其长度等于 **Number of rotor pole pairs** 参数值的两倍。向量的每个元素对应一个转子极。

默认值等于 `ones(1,10)`，其行为与无故障场景相同。

#### 依赖关系

要启用此参数，请选择 **Enable faults** 参数。

### **Duration of transition to faulted** — 模块完全故障所需的时间 `100` `s`（默认）| 正标量

模块对每个转子极的峰值磁体磁通密度施加故障乘数完整效果所需的时间。当模块进入故障状态时，每个转子极的峰值磁体磁通密度会使用故障乘数逐渐修改。

#### 依赖关系

要启用此参数，请选择 **Enable faults** 参数。

### **Simulation time for fault event** — 模块发生故障的仿真时间 `1` `s`（默认）| 正标量

模块开始对每个转子极的峰值磁体磁通密度施加故障乘数的仿真时间。

#### 依赖关系

要启用此参数，请选择 **Enable faults** 参数。

## 所属库

Simscape / Electrical / Electromechanical

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

定子齿与旋转永磁转子之间的气隙

Rotating Air Gap 模块对定子齿与旋转永磁转子之间的气隙进行建模。此模块假设转子磁体为表面安装式，并且相关的感应电压为正弦波。

下图显示了 Rotating Air Gap 模块的参数与其在永磁电机内部物理值之间的关系

其中：

- *r* 是 **Rotor radius** 参数的值。
- *g* 是 **Air gap** 参数的值。
- *lm* 是 **Permanent magnet length (in direction of flux)** 参数的值。
- *l* 是 **Tooth depth (in direction of shaft)** 参数的值。

转子周长等于 2πr。那么，转子上一个永磁体的宽度等于 2πr2N，其中 *N* 是 **Number of rotor pole pairs**。

如果转子角度为零（由 **Variables** 部分中的 **Rotor angle** 变量指定），则转子磁体与第一个定子齿的中间完全对齐。此时永磁体的方向设置为阻碍磁通从端口 **N** 流向端口 **S**。

使用此模块可以创建永磁同步电机（PMSM）的磁表示。例如，如果要建模一个具有九个定子极的电机，请创建此模块的九个副本，并将每个 **Stator tooth reference index** 参数分别设置为 `1`、`2`、`3`、`4`、`5`、`6`、`7`、`8` 和 `9`。

### 方程

下图显示了气隙和相邻永磁体的等效电路

其中：

- *ϕg* 是从外部磁路流向端口 **N** 的磁通。
- *Rg* 是气隙磁阻。
- *mmf* 是旋转气隙组件两端的磁动势。
- *Rm* 是永磁体磁阻。
- *ϕr* 是由转子永磁体在定子齿所张角度范围内产生的磁通。

此方程定义了 *ϕg*、*mmf* 和 *ϕr* 之间的关系：

ϕg=mmf−RmϕrRm+Rg。

如果反电动势为正弦波，则永磁转子的磁通密度由以下方程定义

Br=B0cos(Nθs−Nθr)

其中：

- *N* 是 **Number of rotor pole pairs**。
- *θr* 是转子角度。
- *θs* 是定子角度。
- *B0* 是 **Peak magnet flux density**，单位为 Tesla。

然后，要获得永磁体磁链，请对定子齿所张的定子角度进行积分

ϕr(θr)=rl∫−θtooth2θtooth2[B0cos(Nθs−Nθr)]dθs

其中：

- *r* 是 **Rotor radius**。
- *l* 是 **Tooth depth (in direction of shaft)**。

对于理想 PMSM，*θtooth* 必须等于 *2π/Ns*，其中 *Ns* 是 **Number of stator teeth** 参数的值。然后，通过求解积分可获得流过等效电路的磁通方程：

ϕr(θr)=2B0lr/Nsin(πNNs)cos(Nθr)。

要获得气隙中产生的转矩，首先计算组件存储的总能量：

E=12ϕg2Rg+12(ϕr(θr))2Rm。

然后，要获得转矩，请对转子角度求导：

τ=∂E∂θr=−2B0Rmlrsin(πNNs)sin(Nθr)(ϕg+ϕr(θr))/N。

最后，根据几何结构计算 *Rg* 和 *Rm*：

Rg=gμ0AgRm=lmμrμ0Ag

其中：

- *μ0* 是自由空间的介电常数。
- *μr* 是永磁体的相对介电常数。
- *g* 是 **Air gap**。
- *lm* 是磁体长度。

### 故障

您可以对 Rotating Air Gap 模块设置故障。要启用故障，请在 **Faults** 部分中选择 **Enable faults** 参数。

**注意**

Rotating Air Gap 模块不支持非侵入式故障建模。要对非侵入式故障建模，请使用 Magnetic Rotor。

故障定义为峰值磁体磁通密度的降低。与每个转子磁体关联的磁通密度在形状上保持正弦。当 Rotating Air Gap 模块处于故障状态时，您可以通过指定 **Flux multipliers for faulted rotor poles** 参数，对任何转子极的磁通密度施加降低因子。

具有正弦反电动势的理想 PMSM 气隙中的无故障磁通密度等于：

Br=B0cos(Nθs−Nθr)

当故障磁体与齿相互作用时，模块使用以下方程定义磁通密度

Br=λB0cos(Nθs−Nθr)，

其中 *λ* 是将峰值 *B0* 映射到故障 *B0* 的因子，并在 **Flux multipliers for faulted rotor poles** 参数中定义。

向故障值的过渡在 **Duration of transition to faulted** 参数中指定的时间段内线性混合。使用此参数可以模拟过热永磁体如何随时间逐渐失去其磁化强度。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值来指定模型中变量的预期幅值。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
