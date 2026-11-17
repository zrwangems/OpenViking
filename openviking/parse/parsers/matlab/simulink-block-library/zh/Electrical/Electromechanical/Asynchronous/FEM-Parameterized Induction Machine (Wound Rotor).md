---
type: simulink-block
title: 'FEM-Parameterized Induction Machine (Wound Rotor)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Asynchronous'
documentation_page: 'femparameterizedinductionmachinewoundrotor'
documentation_source_path: 'ref/femparameterizedinductionmachinewoundrotor.html'
language: zh-CN
chinese_source: worker-translation
---

# FEM-Parameterized Induction Machine (Wound Rotor)

## 端口

### 守恒端口

### **~1** — 定子正端连接 电气

与定子正端连接相关联的复合三相端口。有关三相端口的详细信息，请参阅 Three-Phase Ports。

### **~2** — 定子负端连接 电气

与定子负端连接相关联的复合三相端口。

### **R** — 电机转子 机械旋转

与电机转子相关联的机械旋转守恒端口。

### **C** — 电机机壳 机械旋转

与电机机壳相关联的机械旋转守恒端口。

### **~1r'** — 转子正端连接 电气

与转子正端连接相关联的复合三相端口。有关三相端口的详细信息，请参阅 Three-Phase Ports。

### **~2r'** — 转子负端连接 电气

与转子负端连接相关联的复合三相端口。有关三相端口的详细信息，请参阅 Three-Phase Ports。

### **HA** — *a* 相端子 热

与 *a* 相端子相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HB** — *b* 相端子 热

与 *b* 相端子相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HC** — *c* 相端子 热

与 *c* 相端子相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HR** — 转子 热

与转子相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 启用热端口的选项 `No thermal port`（默认）| `Show thermal port`

用于启用模块热端口并建模生成热量和电机温度效应的选项。

### 电阻

### **Stator resistance, Rs** — 定子电阻 `0.25` `Ohm`（默认）| 正标量

定子电阻。

### **Tabulate rotor resistance with frequency** — 将转子电阻随频率制表的选项 `Off`（默认）| `On`

将转子电阻随频率制表的选项。

清除此参数以在额定温度下指定恒定转子电阻。

选择此参数以在额定温度下将电阻指定为频率的函数。

### **Referred rotor resistance, Rr\_d** — 折算转子电阻 `0.14` `Ohm`（默认）| 正标量

折算到定子的转子电阻。

#### 依赖关系

要启用此参数，请清除 **Tabulate rotor resistance with frequency** 参数。

### **Rotor AC frequency vector, fr** — 转子交流频率向量 `[0, 5, 10, 15]` `Hz`（默认）| 非负标量向量

转子交流频率向量。

#### 依赖关系

要启用此参数，请选择 **Tabulate rotor resistance with frequency** 参数。

### **Referred rotor resistance table, Rr\_d(fr)** — 折算转子电阻表 `[.14, .14, .14, .14]` `Ohm`（默认）| 正标量向量

折算到定子的转子电阻随转子交流频率向量变化的表。

#### 依赖关系

要启用此参数，请选择 **Tabulate rotor resistance with frequency** 参数。

### 磁通

### **Number of pole pairs** — 电机极对数 `1`（默认）| 正整数

电机极对数。

### **Stator d-axis current vector, iDS** — 定子 D 轴电流向量 `[0, 150, 350, 500]` `A`（默认）| 非负标量向量

定子 *D* 轴电流向量。

### **Stator q-axis current vector, iQS** — 定子 Q 轴电流向量 `[0, 250, 500]` `A`（默认）| 非负标量向量

定子 *Q* 轴电流向量。

### **Stator d-axis flux linkage table, λds(ids,iqs)** — 定子 D 轴磁链表 `4.4e-2 * repmat([0, 150, 350, 500]', 1, 3)` `Wb`（默认）| 标量矩阵

定子 *D* 轴磁链表。

默认值对应于线性磁通。使用线性磁通等效于 Induction Machine Squirrel Cage 模块的建模方法。

### **Stator q-axis flux linkage table, λqs(ids,iqs)** — 定子 Q 轴磁链表 `2.1e-3 * repmat([0, 250, 500], 4, 1)` `Wb`（默认）| 标量矩阵

定子 *Q* 轴磁链表。

默认值对应于线性磁通。使用线性磁通等效于 Induction Machine Squirrel Cage 模块的建模方法。

### **Interpolation method** — 插值方法 `Linear`（默认）| `Smooth`

当输入值位于网格点之间时用于逼近输出值的插值方法：

- `Linear` — 使用多维插值线性算法的扩展。选择此选项以获得最佳性能。
- `Smooth` — 使用改进的 Akima 插值算法。选择此选项以生成具有连续一阶导数的连续曲面。

有关插值方法的详细信息，请参阅 `tablelookup`。

### 机械

### **Include rotor inertia** — 包含转子惯量的选项 `On`（默认）| `Off`

包含转子惯量的选项。

### **Rotor inertia** — 转子惯量 `1e-3` `kg*m^2`（默认）| 正标量

转子惯量。

#### 依赖关系

要启用此参数，请选择 **Include rotor inertia** 参数。

### **Rotor damping** — 转子阻尼 `0` `N*m*s/rad`（默认）| 非负标量

转子阻尼。

### 温度依赖性

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Measurement temperature** — 额定温度 `298.15` `K`（默认）| 实标量

您引用电机参数时的温度。

### **Stator resistance temperature coefficient** — 定子电阻温度系数 `3.93e-3` `1/K`（默认）| 非负标量

所有三个定子绕组的电阻与温度关系方程中的系数 α。有关详细信息，请参阅 Thermal Model for Actuator Blocks。默认值适用于铜。

### **Rotor resistance temperature coefficient** — 转子电阻温度系数 `3.93e-3` `1/K`（默认）| 非负标量

转子电阻与温度关系方程中的系数 α。有关详细信息，请参阅 Thermal Model for Actuator Blocks。默认值适用于铜。

### 热端口

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Include stator and rotor thermal masses** — 包含定子和转子热质量的选项 `On`（默认）| `Off`

包含定子和转子热质量的选项。

### **Thermal mass for each stator winding** — 绕组热质量 `100` `J/K`（默认）| 正标量

每个定子绕组的热质量值。热质量是使温度升高一度所需的能量。

#### 依赖关系

要启用此参数，请选择 **Include stator and rotor thermal masses** 参数。

### **Rotor thermal mass** — 转子热质量 `200` `J/K`（默认）| 正标量

转子的热质量。热质量是使转子温度升高一度所需的能量。

#### 依赖关系

要启用此参数，请选择 **Include stator and rotor thermal masses** 参数。

## 所属库

Simscape / Electrical / Electromechanical / Asynchronous

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

以磁链形式定义的绕线转子感应电机

FEM-Parameterized Induction Machine (Wound Rotor) 模块使用磁链表对绕线转子感应电机进行建模。

您可以使用有限元工具（如 ANSYS Motor-CAD 软件）生成磁链表。

绕线转子异步电机是一种感应电机。您可以访问模块上的所有定子和转子连接。因此，您可以使用星形和三角形配置之间的切换或通过增加转子电阻来建模软启动方案。如果您不需要访问转子绕组，可以改用 FEM-Parameterized Induction Machine (Squirrel Cage) 模块。

将端口 **~1** 连接到三相电路。要以三角形配置连接定子，请在端口 **~1** 和 **~2** 之间连接一个 Phase Permute 模块。要以星形配置连接定子，请将端口 **~2** 连接到 Grounded Neutral (Three-Phase) 或 Floating Neutral (Three-Phase) 模块。

如果您不需要改变转子电阻，请将转子端口 **~1r'** 连接到 Floating Neutral (Three-Phase) 模块，并将转子端口 **~2r'** 连接到 Grounded Neutral (Three-Phase) 模块。

转子电路折算到定子。因此，当您在电路中使用该模块时，请将任何附加电路参数折算到定子。

### 方程

三相绕线转子感应电机由带有三个铜绕组的铁定子叠片和带有三个铜绕组的转子叠片组成。

当三相交流电源为定子供电时，电流产生旋转磁场。该旋转磁场在转子绕组中感应出电流，从而在转子中产生磁场。这些磁场与电流之间的相互作用在转子中产生转矩，从而使其开始运动。

感应电机方程在定向于转子磁场的同步参考坐标系（SRFORF）中表示。该坐标系与定子和转子磁场同步，*D* 轴与转子磁场 *D* 轴对齐。在该坐标系中，转子磁链向量仅具有 *D* 轴分量。*Q* 轴分量为零。

λ′qr=0。

- λs→ 是定子磁场向量。
- λr→ 是转子磁场向量。
- is→ 是定子电流向量。

所有这些向量都以同步速度 *ωe* 旋转。同步角 *θe* 跟踪定子电流向量的方向。

转子电流向量以下式给出的速度旋转：

ωslip=ωe−Nppωr，

其中 *ωr* 是转子机械速度，*Npp* 是 **Number of pole pairs** 参数。

要将定子 *a*、*b* 和 *c* 相电压和电流表示在 SRFORF 参考坐标系中，您可以使用 Park 变换：

Ps=2/3[cosθecos(θe−2π/3)cos(θe+2π/3)−sinθe−sin(θe−2π/3)−sin(θe+2π/3)0.50.50.5]，

其中 *θe* 是同步速度的时间积分：

θe=∫ωe dt。

然后，您可以使用这些方程计算定子电压和电流的 *D* 轴和 *Q* 轴分量。

isdq0=Ps⋅isabcvsdq0=Ps⋅vsabc

转子 *a*、*b* 和 *c* 相电压和电流由于转差而不以同步速度旋转。转子电流以转差速度 *ωslip* 旋转。

要将转子 DQ 电流表示在静止坐标系（*a*、*b* 和 *c* 相）中，您可以使用 Park 变换：

Pr=2/3[cosθercos(θer−2π/3)cos(θer+2π/3)−sinθer−sin(θer−2π/3)−sin(θer+2π/3)0.50.50.5]，

其中 *θer* 是转子转差角，等于转差速度的时间积分：

θer=∫ωslip dt。

然后，您可以使用这些方程计算转子电压和电流的 *a*、*b* 和 *c* 分量。

irabc=Pr−1⋅irdq0vrabc=Pr−1⋅vrdq0

在 SRFORF 参考坐标系中，定子和转子电流、电压和磁通与以下基本感应电机方程相关：

- 定子电压方程

  vds=Rsids−ωeλqs+dλdsdtvqs=Rsiqs+ωeλds+dλqsdt
- 转子电压方程

  v′dr=R′ri′dr+dλ′drdtv′qr=R′ri′qr+ωslipλ′dr

  使用后一个转子电压方程计算转差速度，然后可以使用该速度计算参考坐标系变换的同步速度。

  ωslip  =  v′qr−R′ri′qrλ′dr。
- 绕线转子方程

  v′dr=Vrdv′qr=Vrq

  其中 *Vrd* 和 *Vrq* 分别是端口 **~1r'** 和 **~2r'** 两端的 *D* 轴和 *Q* 轴转子电压。
- 磁通-电流关系

  励磁 *D* 轴电流定义为

  id =  ids+  i′dr，

  磁通-电流关系为

  λ′dr=λds−Ltidsλ′qr=λqs−Ltiqs

  其中：

  - *λds* 是针对 *id* 和 *iqs* 的特定组合计算的 **Stator d-axis flux linkage table, λds(ids,iqs)** 参数的插值。
  - *λqs* 是针对 *id* 和 *iqs* 的特定组合计算的 **Stator q-axis flux linkage table, λqs(ids,iqs)** 参数的插值。
  - *Lt* 是从磁链表计算的瞬态电感的插值。

  转子磁通-电流关系的另一种形式使用 *Lϕ* 电感

  λ′dr=Lϕidλ′qr=Lϕiq

  其中 *Lϕ* 是从磁链表计算的励磁电感表的插值。

  当您将后一个 *Q* 轴转子磁通方程与 λ′qr=0 结合时，您得到 iq=0，这意味着折算转子 *Q* 轴电流与定子 *Q* 轴电流大小相等、方向相反：

  i′qr=−iqs。

  *Lϕ* 由下式定义。

  Lϕ=Ls−Lt，

  其中 *Lt* 是瞬态电感，定义为

  Lt=Ls−Lm2L′r。

  在这些方程中，*Ls*、*Lm* 和 L′r 分别是定子电感、励磁电感和折算转子电感。这些方程将这些电感关联起来：

  Ls=Lls+LmL′r=L′lr+Lm

  其中 *Lls* 和 L′lr 分别是定子漏感和折算转子漏感。
- 转矩方程

  T=32Npp(λdsiqs−λqsids)。

### 建模热效应

您可以暴露热端口以模拟生成热量和电机温度的效应。要暴露热端口并启用 **Temperature Dependence** 和 **Thermal Port** 参数，请将 **Modeling option** 参数设置为以下选项之一：

- `No thermal port` — 模块包含与定子绕组相关联的电气守恒端口，但不包含热端口。
- `Show thermal port` — 模块包含与定子绕组相关联的扩展电气守恒端口，以及每个绕组和转子的热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

额定值提供了一种在模型中指定变量预期幅值的方法。使用基于额定值的系统缩放可提高仿真鲁棒性。您可以使用不同的来源指定额定值，包括模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
