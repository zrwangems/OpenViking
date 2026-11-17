---
type: simulink-block
title: 'Switched Reluctance Machine'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Reluctance & Stepper'
documentation_page: 'switchedreluctancemachine'
documentation_source_path: 'ref/switchedreluctancemachine.html'
language: zh-CN
chinese_source: worker-translation
---

# Switched Reluctance Machine

## 端口

### 守恒端口

### **~1** — 正三相复合端子 electrical

与定子绕组正极端子关联的电气守恒三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`。

### **~2** — 负三相复合端子 electrical

与定子绕组负极端子关联的电气守恒三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`。

### **a1** — 正 *a* 相端子 electrical

与定子绕组 *a* 正极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **a2** — 负 *a* 相端子 electrical

与定子绕组 *a* 负极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **b1** — 正 *b* 相端子 electrical

与定子绕组 *b* 正极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **b2** — 负 *b* 相端子 electrical

与定子绕组 *b* 负极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **c1** — 正 *c* 相端子 electrical

与定子绕组 *c* 正极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **c2** — 负 *c* 相端子 electrical

与定子绕组 *c* 负极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **R** — 转子 mechanical

与转子关联的机械旋转守恒端口。

### **C** — 机壳 mechanical

与定子或机壳关联的机械旋转守恒端口。

### **HA** — *a* 相端子热端口 thermal

与定子绕组 *a* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HB** — *b* 相端子热端口 thermal

与定子绕组 *b* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HC** — *c* 相端子热端口 thermal

与定子绕组 *c* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HR** — 转子热端口 thermal

与转子关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口并对将功率转换为热量的损耗效应进行建模。

### 主

### **Electrical connection** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

选择使用复合三相端口还是展开三相端口。

### **Number of rotor poles** — 转子极数 `4`（默认）| 正整数

转子极数。

### **Stator resistance per phase** — 电阻 `3` `Ohm`（默认）| 正标量

每个定子绕组的每相电阻。

### **Stator parameterization** — 参数化方法 `Specify parametric data`（默认）| `Specify parametric and geometric data` | `Specify tabulated flux data`

定子参数化的方法。

#### 依赖关系

选择 `Specify parametric data` 会启用以下参数：

- **Magnetizing resistance**
- **Saturated flux linkage**
- **Aligned inductance**
- **Unaligned inductance**

选择 `Specify parametric and geometric data` 会启用以下参数：

- **Magnetizing resistance**
- **Saturated flux linkage**
- **Aligned inductance**
- **Unaligned inductance**
- **Angle subtended by each stator pole**
- **Angle subtended by each rotor pole**
- **Angle over which flux gradient changes are smoothed**

选择 `Specify tabulated flux data` 会启用以下参数：

- **Current vector, i**
- **Angle vector, theta**
- **Flux linkage matrix, Phi(i,theta)**

### **Magnetizing resistance** — 磁损耗 `inf` `Ohm`（默认）| 实标量

每个相绕组的总磁化电阻。默认值 `inf` 表示没有铁损耗。

#### 依赖关系

当 **Stator parameterization** 设置为 `Specify parametric data` 或 `Specify parametric and geometric data` 时，会显示此参数。

### **Saturated flux linkage** — 磁链 `0.43` `Wb`（默认）| 正标量

每相饱和磁链。

#### 依赖关系

当 **Stator parameterization** 设置为 `Specify parametric data` 或 `Specify parametric and geometric data` 时，会显示此参数。

### **Aligned inductance** — 电感 `0.0046` `H`（默认）| 正标量

此参数的值必须大于 **Unaligned inductance** 参数的值。

#### 依赖关系

当 **Stator parameterization** 设置为 `Specify parametric data` 或 `Specify parametric and geometric data` 时，会显示此参数。

### **Unaligned inductance** — 电感 `6.7e-4` `H`（默认）| 正标量

此参数的值必须小于 **Aligned inductance** 参数的值。

#### 依赖关系

当 **Stator parameterization** 设置为 `Specify parametric data` 或 `Specify parametric and geometric data` 时，会显示此参数。

### **Angle subtended by each stator pole** — 定子齿角度 `45` `deg`（默认）| 正标量

每个定子齿所跨的角度。此值必须大于或等于 **Angle subtended by each rotor pole** 的值。

#### 依赖关系

当 **Stator parameterization** 设置为 `Specify parametric and geometric data` 时，会显示此参数。

### **Angle subtended by each rotor pole** — 转子齿角度 `42` `deg`（默认）| 正标量

每个转子齿所跨的角度。

#### 依赖关系

当 **Stator parameterization** 设置为 `Specify parametric and geometric data` 时，会显示此参数。

### **Angle over which flux gradient changes are smoothed** — 拐点平滑 `0.5` `deg`（默认）| 正标量

梯形电感曲线中尖锐边缘被平滑的角度范围。此值必须小于 **Angle subtended by each rotor pole** 的值。

#### 依赖关系

当 **Stator parameterization** 设置为 `Specify parametric and geometric data` 时，会显示此参数。

### **Current vector, i** — 电流 `[0, 50, 100]` `A`（默认）| 向量

用于标识磁链曲线族的电流向量。

#### 依赖关系

当 **Stator parameterization** 设置为 `Specify tabulated flux data` 时，会显示此参数。

### **Angle vector, theta** — 角度 `[0, 45, 90]` `deg`（默认）| 向量

用于标识磁链曲线族的角度向量。

#### 依赖关系

当 **Stator parameterization** 设置为 `Specify tabulated flux data` 时，会显示此参数。

### **Flux linkage matrix, Phi(i,theta)** — 磁链 `[0, 0, 0; .37, .06, .37; .43, .1, .43]` `Wb`（默认）| 矩阵

定义磁链曲线族的磁链矩阵。

#### 依赖关系

当 **Stator parameterization** 设置为 `Specify tabulated flux data` 时，会显示此参数。

### 铁损耗

有关计算铁损耗的更多信息，请参阅 Calculating Iron Losses。

### **Model** — 铁损耗建模选项 `None`（默认）| `Tabulate losses from current and speed` | `Tabulate losses from current, speed, and angle`

是否启用铁损耗建模。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify tabulated flux data`。

### **Magnetizing resistance** — 铁损耗的磁化电阻 `inf` `Ohm`（默认）

磁化电阻。该值必须大于零。默认值为 `inf`，表示没有铁损耗。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify parametric data` 或 `Specify parametric and geometric data`。

### **Rotor speed vector, w** — 转子速度 `[500, 1000, 1500]` `rpm`（默认）

用于制表铁损耗的转子速度向量。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Tabulate losses from current and speed` 或 `Tabulate losses from current, speed, and angle`。

### **Iron loss table, Ploss(i,w)** — 基于电流和速度制表的铁损耗表 `zeros(3, 3)` `W`（默认）

特定相中由于铁损耗而在轴上损失的机械功率，作为瞬时相电流和转子速度的函数制表。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Tabulate losses from current and speed`。

### **Iron loss table, Ploss(i,w,theta)** — 基于电流、速度和角度制表的铁损耗表 `zeros(3, 3, 2)` `W`（默认）

特定相中由于铁损耗而在轴上损失的机械功率，作为瞬时相电流、转子速度和转子角度的函数制表。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Tabulate losses from current, speed, and angle`。

### 机械

### **Rotor inertia** — 惯量 `0.01` `kg*m^2`（默认）| 零或正标量

连接到机械平移端口 **R** 的转子的惯量。

### **Rotor Damping** — 阻尼 `0` `N*m/(rad/s)`（默认）| 正标量

旋转阻尼。

### 热

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Resistance temperature coefficient** — 温度系数 `3.93e-3` `1/K`（默认）| 正标量

所有三个绕组的电阻与温度关系方程中的系数 α，如 Thermal Model for Actuator Blocks 中所述。默认值 `3.93e-3` 1/K 适用于铜。

### **Measurement temperature** — 额定温度 `25` `degC`（默认）| 实标量

电机参数所对应的温度。

### **Winding thermal mass** — 绕组热质量 `100` `J/K`（默认）| 正标量

*a*、*b* 和 *c* 绕组的热质量值。热质量是将温度升高一度所需的能量。

### **Rotor thermal mass** — 转子热质量 `50` `J/K`（默认）| 正标量

转子的热质量。热质量是将转子温度升高一度所需的能量。

### **Percentage of total iron losses associated with the rotor** — 总铁损耗百分比 `50`（默认）

与转子关联的总铁损耗百分比。

## 所属库

Simscape / Electrical / Electromechanical / Reluctance & Stepper

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2021b：电气连接端口更新

从 R2021b 起，要在复合端口和展开端口之间切换，请将 **Electrical connection** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。

由于这些更改，在早期版本中保存的模型内，请检查此模块的 **Electrical connection** 参数。

## 描述

三相开关磁阻电机

Switched Reluctance Machine 模块表示三相开关磁阻电机（SRM）。定子具有三个极对，承载三个电机绕组，转子具有多个非磁性极。电机通过激励一个定子极对产生转矩，在最近的转子极上感应力并将其拉向对齐位置。该图显示了电机构造。

在您的应用中选择此电机可利用以下特性：

- 低成本
- 相对安全的故障电流
- 对高温运行的鲁棒性
- 高转矩惯量比

使用此模块可通过易于测量或估计的参数对 SRM 进行建模。要使用 FEM 数据对 SRM 进行建模，请参阅 Switched Reluctance Motor Parameterized with FEM Data。

### 方程

**开关磁阻电机模块**

三相电机的转子行程角为

θst=2π3Nr，

其中：

- *θst* 是行程角。
- *Nr* 是转子极数。

一个转子极的转矩产生能力 *β* 为

β=2πNr。

开关磁阻电机（SRM）的数学模型高度非线性，因为磁饱和会影响磁链-角度曲线 *λ*(*θph*)。SRM 的相电压方程为

vph=Rsiph+dλph(iph,θph)dt

其中：

- *vph* 是每相电压。
- *Rs* 是每相定子电阻。
- *iph* 是每相电流。
- *λph* 是每相磁链。
- *θph* 是每相角度。

将相电压方程用偏导数重写后得到以下方程：

vph=Rsiph+∂λph∂iphdiphdt+∂λph∂θphdθphdt。

瞬态电感定义为

Lt(iph,θph)=∂λph(iph,θph)∂iph，

或更简单地表示为

∂λph∂iph。

反电动势定义为

Eph=∂λph∂θphωr。

将这些项代入重写后的电压方程，得到以下电压方程：

vph=Rsiph+Lt(iph,θph)diphdt+Eph。

将共能公式应用于转矩方程

Tph=∂W(θph)∂θr

和能量方程

W(iph,θph)=∫0iphλph(iph,θph)diph

可得到一个积分方程，用于定义每相瞬时转矩，即

Tph (iph,θph)=∫0iph∂λph(iph,θph)∂θphdiph。

对各相积分后得到以下方程，用于定义三相 SRM 的总瞬时转矩：

T=∑j=13Tph(j)。

运动方程为

Jdωdt=T−TL−Bmω

其中：

- *J* 是转子惯量。
- *ω* 是机械转速。
- *T* 是转子转矩。对于开关磁阻电机模块，转矩从电机壳体（模块守恒端口 **C**）流向电机转子（模块守恒端口 **R**）。
- *TL* 是负载转矩。
- *J* 是转子惯量。
- *Bm* 是转子阻尼。

对于高保真建模和控制开发，请使用经验数据和有限元计算来确定磁链随电流和角度变化的曲线，即

λph(iph,θph)。

对于低保真建模，也可以使用解析技术来近似该曲线。其中一种技术 [2] 使用以下指数函数：

λph(iph,θph)=λsat(1−e−iphf(θph))，

其中：

- *λsat* 是饱和磁链。
- *f*(*θr*) 通过傅里叶展开获得。

对于傅里叶展开，使用该方程的前两个偶次项：

f(θph)=a+bcos(Nrθph)

其中 *a* > *b*，

a= Lmin+Lmax2λsat，

并且

b= Lmax−Lmin2λsat。

**开关磁阻电动机模块**

磁链曲线基于参数和几何数据近似为：

λph(iph,θph)=λsat(1−e−L0(θ)iph/λsat)，

其中 *L0* 是未饱和电感。

当电流与未饱和电感的乘积接近饱和磁链值时，饱和效应会更加显著。使用 **Saturated flux linkage** 参数指定该值。

对磁链方程求导后得到绕组电感：

L(θph)=L0(θph)e(−L0(θph)iph/λsat)

未饱和电感在最小值和最大值之间变化。最小值出现在转子极正好位于两个定子极之间时。最大值出现在转子极与定子极对齐时。在这两点之间，模块将未饱和电感近似为转子角度的线性函数。下图显示了转子极经过定子极时的未饱和电感。

图中：

- *θR* 对应于转子极所张的角度。使用 **Angle subtended by each rotor pole** 参数设置。
- *θS* 对应于定子极所张的角度。使用 **Angle subtended by each stator pole** 参数设置。
- *θC* 对应于该完整周期所张的角度，由 *2π/2n* 确定，其中 *n* 是定子极对数。

### 计算铁耗

开关磁阻电机（多相）模块将铁耗实现为电转矩的减少。

如果将 **Stator parameterization** 参数设置为 `Specify parametric data` 或 `Specify parametric and geometric data`，请指定 **Magnetizing resistance** 参数来建模铁耗。

如果将 **Stator parameterization** 参数设置为 `Specify tabulated flux data`，模块会将损耗制表为每个定子相中损失的功率。每个定子的损耗仅取决于该相中的定子电流、转子角度（按几何关系偏移到该相）和转子速度。转子铁耗功率按总铁耗功率的百分比计算，该百分比由 **Percentage of total iron losses associated with the rotor** 参数指定。

如果按电流、速度和角度对损耗进行制表，则铁耗转矩会减少通用“A”相的电转矩：

τelecA=τ(iA,θA)−τloss(iA,w,θA)

其中 τloss(iA,w,θA)=sign(w)Ploss(abs(iA),abs(w),θA)abs(w)+wmin 是转矩损耗，按机械功率损耗除以转子速度计算。*wmin* 是最小转子速度，等于 `1` `rad/s`。该值可防止转子速度等于 `0` 时发生除零。

如果仅按电流和速度的函数对损耗进行制表，则铁耗转矩会减少通用“A”相的电转矩：

τloss(iA,w)=sign(w)Ploss(abs(iA),abs(w))abs(w)+wmin。

铁耗作为转矩减少施加到机械侧。如果根据 FEM 结果创建铁耗表 *Ploss*，FEM 工具可能会将损耗功率表示为电功率而不是机械功率。

总电转矩等于各相电转矩之和：

τelec=τelecA+τelecB+τelecC。

总耗散功率等于铁耗与铜耗之和：

Pdissipated=(τlossA+τlossB+τlossC)w+Raia2+Rbib2+Rcic2。

**带热端口的铁耗**

如果暴露模块的热端口，则每相耗散的功率会作为电机和转子中的热源：

PdissA=Raia2+PironAPdissB=Rbib2+PironBPdissC=Rcic2+PironCPdissR=PironR

转子中的铁耗等于总铁耗的某一百分比。该损耗保持恒定，不依赖于其他状态：

PironR=percentrotor100(τlossA+τlossB+τlossC)w。

然后，剩余的铁耗在不同定子相之间分配：

PironA=(1−percentrotor100)τlossA wPironB=(1−percentrotor100)τlossB wPironC=(1−percentrotor100)τlossC w

### 建模热效应

可以暴露热端口来建模将功率转换为热量的损耗效应。要暴露热端口，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含多个热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 数值平滑

在实践中，磁边缘效应会阻止电感在转子极经过定子极时呈现梯形形状。为了对这些效应建模，并避免阻碍求解器收敛的梯度不连续，模块在拐点处对梯度 *∂L0/∂θ* 进行平滑。要更改应用此平滑的角度，请使用 **Angle over which flux gradient changes are smoothed** 参数。

### 假设

模块假设零转子角度对应于与 *a* 相完全对齐的转子极。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。可以使用不同来源指定标称值，包括模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
