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

### 守恒

### **~1** — 正三相复合端子电气

与定子绕组正端子关联的电气守恒三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`。

### **~2** — 负三相复合端子电气

与定子绕组负端子关联的电气守恒三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`。

### **a1** — 正 *a* 相端子电气

与定子绕组 *a* 正端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **a2** — 负 *a* 相端子电气

与定子绕组 *a* 负端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **b1** — 正 *b* 相端子电气

与定子绕组 *b* 正端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **b2** — 负 *b* 相端子电气

与定子绕组 *b* 负端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **c1** — 正 *c* 相端子电气

与定子绕组 *c* 正端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **c2** — 负 *c* 相端子电气

与定子绕组 *c* 负端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **R** — 转子机械

与转子关联的机械旋转守恒端口。

### **C** — 机壳机械

与定子或机壳关联的机械旋转守恒端口。

### **HA** — *a* 相端子热端口热

与定子绕组 *a* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HB** — *b* 相端子热端口热

与定子绕组 *b* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HC** — *c* 相端子热端口热

与定子绕组 *c* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HR** — 转子热端口热

与转子关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认） | `Show thermal port`

是否启用模块的热端口，并对将功率转换为热量的损耗效应进行建模。

### 主

### **Electrical connection** — 电气连接 `Composite three-phase ports`（默认） | `Expanded three-phase ports`

是使用复合三相端口还是扩展三相端口。

### **Number of rotor poles** — 转子极数 `4`（默认） | positive integer

转子极数。

### **Stator resistance per phase** — 电阻 `3` `Ohm`（默认） | positive scalar

每个定子绕组的每相电阻。

### **Stator parameterization** — 参数化方法 `Specify parametric data`（默认） | `Specify parametric and geometric data` | `Specify tabulated flux data`

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

### **Magnetizing resistance** — 磁损耗 `inf` `Ohm`（默认） | real scalar

每个相绕组的总磁化电阻。默认值 `inf` 表示没有铁损。

#### 依赖关系

当您将 **Stator parameterization** 设置为 `Specify parametric data` 或 `Specify parametric and geometric data` 时，此参数会显示。

### **Saturated flux linkage** — 磁链 `0.43` `Wb`（默认） | positive scalar

每相饱和磁链。

#### 依赖关系

当您将 **Stator parameterization** 设置为 `Specify parametric data` 或 `Specify parametric and geometric data` 时，此参数会显示。

### **Aligned inductance** — 电感 `0.0046` `H`（默认） | positive scalar

此参数的值必须大于 **Unaligned inductance** 参数的值。

#### 依赖关系

当您将 **Stator parameterization** 设置为 `Specify parametric data` 或 `Specify parametric and geometric data` 时，此参数会显示。

### **Unaligned inductance** — 电感 `6.7e-4` `H`（默认） | positive scalar

此参数的值必须小于 **Aligned inductance** 参数的值。

#### 依赖关系

当您将 **Stator parameterization** 设置为 `Specify parametric data` 或 `Specify parametric and geometric data` 时，此参数会显示。

### **Angle subtended by each stator pole** — 定子齿角度 `45` `deg`（默认） | positive scalar

每个定子齿跨过的角度。此值必须大于或等于 **Angle subtended by each rotor pole** 的值。

#### 依赖关系

当您将 **Stator parameterization** 设置为 `Specify parametric and geometric data` 时，此参数会显示。

### **Angle subtended by each rotor pole** — 转子齿角度 `42` `deg`（默认） | positive scalar

每个转子齿跨过的角度。

#### 依赖关系

当您将 **Stator parameterization** 设置为 `Specify parametric and geometric data` 时，此参数会显示。

### **Angle over which flux gradient changes are smoothed** — 拐点平滑 `0.5` `deg`（默认） | positive scalar

梯形电感曲线中尖锐边缘被平滑的角度。此值必须小于 **Angle subtended by each rotor pole** 的值。

#### 依赖关系

当您将 **Stator parameterization** 设置为 `Specify parametric and geometric data` 时，此参数会显示。

### **Current vector, i** — 电流 `[0, 50, 100]` `A`（默认） | vector

用于标识磁链曲线族的电流向量。

#### 依赖关系

当您将 **Stator parameterization** 设置为 `Specify tabulated flux data` 时，此参数会显示。

### **Angle vector, theta** — 角度 `[0, 45, 90]` `deg`（默认） | vector

用于标识磁链曲线族的角度向量。

#### 依赖关系

当您将 **Stator parameterization** 设置为 `Specify tabulated flux data` 时，此参数会显示。

### **Flux linkage matrix, Phi(i,theta)** — 磁链 `[0, 0, 0; .37, .06, .37; .43, .1, .43]` `Wb`（默认） | matrix

定义磁链曲线族的磁链矩阵。

#### 依赖关系

当您将 **Stator parameterization** 设置为 `Specify tabulated flux data` 时，此参数会显示。

### 铁损

有关计算铁损的更多信息，请参阅 Calculating Iron Losses。

### **Model** — 铁损建模选项 `None`（默认） | `Tabulate losses from current and speed` | `Tabulate losses from current, speed, and angle`

是否启用铁损建模。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify tabulated flux data`。

### **Magnetizing resistance** — 铁损的磁化电阻 `inf` `Ohm`（默认）

磁化电阻。该值必须大于零。默认值为 `inf`，表示没有铁损。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify parametric data` 或 `Specify parametric and geometric data`。

### **Rotor speed vector, w** — 转子速度 `[500, 1000, 1500]` `rpm`（默认）

用于列出铁损的转子速度向量。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Tabulate losses from current and speed` 或 `Tabulate losses from current, speed, and angle`。

### **Iron loss table, Ploss(i,w)** — 按电流和速度列出的铁损表 `zeros(3, 3)` `W`（默认）

由于特定相中的铁损而损失在轴中的机械功率，表示为瞬时相电流和转子速度的函数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Tabulate losses from current and speed`。

### **Iron loss table, Ploss(i,w,theta)** — 按电流、速度和角度列出的铁损表 `zeros(3, 3, 2)` `W`（默认）

由于特定相中的铁损而损失在轴中的机械功率，表示为瞬时相电流、转子速度和转子角度的函数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Tabulate losses from current, speed, and angle`。

### 机械

### **Rotor inertia** — 惯性 `0.01` `kg*m^2`（默认） | zero or positive scalar

连接到机械平移端口 **R** 的转子惯性。

### **Rotor Damping** — 阻尼 `0` `N*m/(rad/s)`（默认） | positive scalar

旋转阻尼。

### 热

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Resistance temperature coefficient** — 温度系数 `3.93e-3` `1/K`（默认） | positive scalar

所有三个绕组的电阻与温度关系方程中的系数 α，如 Thermal Model for Actuator Blocks 中所述。默认值 `3.93e-3` 1/K 适用于铜。

### **Measurement temperature** — 额定温度 `25` `degC`（默认） | real scalar

电机参数所对应的温度。

### **Winding thermal mass** — 绕组热质量 `100` `J/K`（默认） | positive scalar

*a*、*b* 和 *c* 相绕组的热质量值。热质量是将温度升高一度所需的能量。

### **Rotor thermal mass** — 转子热质量 `50` `J/K`（默认） | positive scalar

转子的热质量。热质量是将转子温度升高一度所需的能量。

### **Percentage of total iron losses associated with the rotor** — 总铁损百分比 `50`（默认）

与转子相关的总铁损百分比。

## 所属库

Simscape / Electrical / Electromechanical / Reluctance & Stepper

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2021b：Electrical connection 端口更新

从 R2021b 起，要在复合端口和扩展端口之间切换，请将 **Electrical connection** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。

由于这些更改，在较早版本中保存的模型内，请检查此模块的 **Electrical connection** 参数。

## 描述

三相开关磁阻电机

Switched Reluctance Machine 模块表示三相开关磁阻电机（SRM）。定子有三个极对，承载三个电机绕组，转子有若干非磁性极。电机通过给一个定子极对通电来产生转矩，在最近的转子极上感应出力，并将其拉向对齐位置。该图显示了电机构造。

在您的应用中选择此电机以利用以下特性：

- 低成本
- 相对安全的故障电流
- 高温运行稳健性
- 高转矩惯性比

使用此模块利用易于测量或估计的参数对 SRM 建模。要使用 FEM 数据对 SRM 建模，请参阅 Switched Reluctance Motor Parameterized with FEM Data。

### 方程

**Switched Reluctance Machine Block**

三相电机的转子冲程角为

θst=2π3Nr,

其中：

- *θst* 是冲程角。
- *Nr* 是转子极数。

一个转子极的转矩产生能力 *β* 为

β=2πNr.

开关磁阻电机 (SRM) 的数学模型高度非线性，因为磁饱和会影响磁链-角度曲线 *λ*(*θph*)。SRM 的相电压方程为

vph=Rsiph+dλph(iph,θph)dt

其中：

- *vph* 是每相电压。
- *Rs* 是每相定子电阻。
- *iph* 是每相电流。
- *λph* 是每相磁链。
- *θph* 是每相角度。

将相电压方程改写为偏导数形式，得到以下方程：

vph=Rsiph+∂λph∂iphdiphdt+∂λph∂θphdθphdt.

瞬态电感定义为

Lt(iph,θph)=∂λph(iph,θph)∂iph,

或更简单地定义为

∂λph∂iph.

反电动势定义为

Eph=∂λph∂θphωr.

将这些项代入改写后的电压方程，得到以下电压方程：

vph=Rsiph+Lt(iph,θph)diphdt+Eph.

将共能公式应用于转矩方程，

Tph=∂W(θph)∂θr,

和能量方程，

W(iph,θph)=∫0iphλph(iph,θph)diph

得到定义每相瞬时转矩的积分方程，即

Tph (iph,θph)=∫0iph∂λph(iph,θph)∂θphdiph.

对各相积分，得到以下方程，该方程定义了三相 SRM 的总瞬时转矩：

T=∑j=13Tph(j).

运动方程为

Jdωdt=T−TL−Bmω

其中：

- *J* 是转子惯量。
- *ω* 是机械转速。
- *T* 是转子转矩。对于 Switched Reluctance Machine 模块，转矩从机壳（模块守恒端口 **C**）流向机器转子（模块守恒端口 **R**）。
- *TL* 是负载转矩。
- *J* 是转子惯量。
- *Bm* 是转子阻尼。

对于高保真建模和控制开发，使用经验数据和有限元计算来确定磁链随电流和角度变化的曲线，即

λph(iph,θph).

对于低保真建模，也可以使用解析技术近似该曲线。其中一种技术 [2] 使用以下指数函数：

λph(iph,θph)=λsat(1−e−iphf(θph)),

其中：

- *λsat* 是饱和磁链。
- *f*(*θr*) 通过傅里叶展开获得。

对于傅里叶展开，使用该方程的前两个偶次项：

f(θph)=a+bcos(Nrθph)

其中 *a* > *b*，

a= Lmin+Lmax2λsat,

以及

b= Lmax−Lmin2λsat.

**Switched Reluctance Motor Block**

磁链曲线基于参数和几何数据近似：

λph(iph,θph)=λsat(1−e−L0(θ)iph/λsat),

其中 *L0* 是未饱和电感。

当电流与未饱和电感的乘积接近饱和磁链值时，饱和效应更加显著。使用 **饱和磁链** 参数指定该值。

对磁链方程求导，得到绕组电感：

L(θph)=L0(θph)e(−L0(θph)iph/λsat)

未饱和电感在最小值和最大值之间变化。最小值出现在转子极正好位于两个定子极之间时。最大值出现在转子极与定子极对齐时。在这两点之间，模块将未饱和电感近似为转子角度的线性函数。下图展示了转子极经过定子极时的未饱和电感。

图中：

- *θR* 对应于转子极所张的角度。使用 **每个转子极所张的角度** 参数设置它。
- *θS* 对应于定子极所张的角度。使用 **每个定子极所张的角度** 参数设置它。
- *θC* 对应于该完整周期所张的角度，由 *2π/2n* 确定，其中 *n* 是定子极对数。

### 计算铁损

Switched Reluctance Machine (Multi-Phase) 模块将铁损实现为电磁转矩的减小。

如果将 **定子参数化** 参数设置为 `Specify parametric data` 或 `Specify parametric and geometric data`，则指定 **磁化电阻** 参数来对铁损建模。

如果将 **定子参数化** 参数设置为 `Specify tabulated flux data`，模块将损耗制表为每个定子相中损失的功率。每个定子的损耗仅取决于该相的定子电流、转子角度（几何上移位到该相）和转子速度。转子的铁损功率按总铁损功率的百分比计算，如 **与转子相关的总铁损百分比** 参数所指定。

如果按电流、速度和角度将损耗制表，铁损转矩会减小通用 “A” 相的电磁转矩：

τelecA=τ(iA,θA)−τloss(iA,w,θA)

其中 τloss(iA,w,θA)=sign(w)Ploss(abs(iA),abs(w),θA)abs(w)+wmin 是转矩损耗，按机械功率损耗除以转子速度计算。*wmin* 是最小转子速度，等于 `1` `rad/s`。当转子速度等于 `0` 时，该值可防止除以零。

如果仅按电流和速度的函数将损耗制表，铁损转矩会减小通用 “A” 相的电磁转矩：

τloss(iA,w)=sign(w)Ploss(abs(iA),abs(w))abs(w)+wmin.

铁损施加到机械侧，作为转矩的减小。如果根据 FEM 结果创建铁损表 *Ploss*，FEM 工具可能将损失功率表示为电功率而不是机械功率。

总电磁转矩等于每相电磁转矩之和：

τelec=τelecA+τelecB+τelecC.

总耗散功率等于铁损与铜损之和：

Pdissipated=(τlossA+τlossB+τlossC)w+Raia2+Rbib2+Rcic2.

**带热端口的铁损**

如果暴露模块的热端口，每相耗散的功率在电机和转子中充当热源：

PdissA=Raia2+PironAPdissB=Rbib2+PironBPdissC=Rcic2+PironCPdissR=PironR

转子中的铁损等于总铁损的百分比。该损耗保持恒定，不依赖于其他状态：

PironR=percentrotor100(τlossA+τlossB+τlossC)w.

然后，剩余铁损分配到不同的定子相中：

PironA=(1−percentrotor100)τlossA wPironB=(1−percentrotor100)τlossB wPironC=(1−percentrotor100)τlossC w

### 对热效应建模

可以暴露热端口来对将功率转换为热量的损耗效应建模。要暴露热端口，将 **建模选项** 参数设置为以下之一：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含多个热守恒端口。

有关在致动器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 数值平滑

在实践中，磁边缘效应会阻止电感在转子极经过定子极时呈现梯形形状。为了对这些效应建模，并避免妨碍求解器收敛的梯度不连续，模块在拐点处平滑梯度 *∂L0/∂θ*。要更改应用此平滑的角度，使用 **平滑磁链梯度变化的角度** 参数。

### 假设

模块假设零转子角度对应于与 *a* 相完全对齐的转子极。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。可以使用不同来源指定标称值，包括模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
