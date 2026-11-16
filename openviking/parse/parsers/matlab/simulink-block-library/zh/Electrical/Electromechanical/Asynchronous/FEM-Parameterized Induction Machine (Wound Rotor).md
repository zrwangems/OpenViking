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

### 守恒

### **~1** — 定子正端连接 electrical

与定子正端连接关联的复合三相端口。有关三相端口的详细信息，请参阅 Three-Phase Ports。

### **~2** — 定子负端连接 electrical

与定子负端连接关联的复合三相端口。

### **R** — 电机转子 mechanical rotational

与电机转子关联的 mechanical rotational 守恒端口。

### **C** — 电机机壳 mechanical rotational

与电机机壳关联的 mechanical rotational 守恒端口。

### **~1r'** — 转子正端连接 electrical

与转子正端连接关联的复合三相端口。有关三相端口的详细信息，请参阅 Three-Phase Ports。

### **~2r'** — 转子负端连接 electrical

与转子负端连接关联的复合三相端口。有关三相端口的详细信息，请参阅 Three-Phase Ports。

### **HA** — *a* 相端子 thermal

与 *a* 相端子关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HB** — *b* 相端子 thermal

与 *b* 相端子关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HC** — *c* 相端子 thermal

与 *c* 相端子关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HR** — 转子 thermal

与转子关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 用于启用热端口的选项 `No thermal port`（默认） | `Show thermal port`

用于启用模块的热端口并模拟产生的热量和电机温度影响的选项。

### 电阻

### **Stator resistance, Rs** — 定子电阻 `0.25` `Ohm`（默认） | 正标量

定子电阻。

### **Tabulate rotor resistance with frequency** — 用于随频率将转子电阻制成表格的选项 `Off`（默认） | `On`

用于随频率将转子电阻制成表格的选项。

清除此参数可在额定温度下指定恒定转子电阻。

选择此参数可在额定温度下将电阻指定为频率的函数。

### **Referred rotor resistance, Rr\_d** — 折算后的转子电阻 `0.14` `Ohm`（默认） | 正标量

折算到定子的转子电阻。

#### 依赖关系

要启用此参数，请清除 **Tabulate rotor resistance with frequency** 参数。

### **Rotor AC frequency vector, fr** — 转子交流频率向量 `[0, 5, 10, 15]` `Hz`（默认） | 非负标量向量

转子交流频率向量。

#### 依赖关系

要启用此参数，请选择 **Tabulate rotor resistance with frequency** 参数。

### **Referred rotor resistance table, Rr\_d(fr)** — 折算后的转子电阻表 `[.14, .14, .14, .14]` `Ohm`（默认） | 正标量向量

作为转子交流频率向量的函数的、折算到定子的转子电阻表。

#### 依赖关系

要启用此参数，请选择 **Tabulate rotor resistance with frequency** 参数。

### 磁链

### **Number of pole pairs** — 电机极对数 `1`（默认） | 正整数

电机极对数。

### **Stator d-axis current vector, iDS** — 定子 D 轴电流向量 `[0, 150, 350, 500]` `A`（默认） | 非负标量向量

定子 *D* 轴电流向量。

### **Stator q-axis current vector, iQS** — 定子 Q 轴电流向量 `[0, 250, 500]` `A`（默认） | 非负标量向量

定子 *Q* 轴电流向量。

### **Stator d-axis flux linkage table, λds(ids,iqs)** — 定子 D 轴磁链表 `4.4e-2 * repmat([0, 150, 350, 500]', 1, 3)` `Wb`（默认） | 标量矩阵

定子 *D* 轴磁链表。

默认值对应于线性磁链。使用线性磁链等效于 Induction Machine Squirrel Cage 模块的建模方法。

### **Stator q-axis flux linkage table, λqs(ids,iqs)** — 定子 Q 轴磁链表 `2.1e-3 * repmat([0, 250, 500], 4, 1)` `Wb`（默认） | 标量矩阵

定子 *Q* 轴磁链表。

默认值对应于线性磁链。使用线性磁链等效于 Induction Machine Squirrel Cage 模块的建模方法。

### **Interpolation method** — 插值方法 `Linear`（默认） | `Smooth`

用于在输入值位于网格点之间时逼近输出值的插值方法：

- `Linear` — 使用多维插值的线性算法扩展。选择此选项可获得最佳性能。
- `Smooth` — 使用修改后的 Akima 插值算法。选择此选项可生成具有连续一阶导数的连续曲面。

有关插值方法的详细信息，请参阅 `tablelookup`。

### 机械

### **Include rotor inertia** — 用于包含转子惯量的选项 `On`（默认） | `Off`

用于包含转子惯量的选项。

### **Rotor inertia** — 转子惯量 `1e-3` `kg*m^2`（默认） | 正标量

转子惯量。

#### 依赖关系

要启用此参数，请选择 **Include rotor inertia** 参数。

### **Rotor damping** — 转子阻尼 `0` `N*m*s/rad`（默认） | 非负标量

转子阻尼。

### 温度依赖性

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Measurement temperature** — 额定温度 `298.15` `K`（默认） | 实标量

引用电机参数时的温度。

### **Stator resistance temperature coefficient** — 定子电阻温度系数 `3.93e-3` `1/K`（默认） | 非负标量

用于所有三个定子绕组的电阻与温度关系方程中的系数 α。有关详细信息，请参阅 Thermal Model for Actuator Blocks。默认值适用于铜。

### **Rotor resistance temperature coefficient** — 转子电阻温度系数 `3.93e-3` `1/K`（默认） | 非负标量

用于转子的电阻与温度关系方程中的系数 α。有关详细信息，请参阅 Thermal Model for Actuator Blocks。默认值适用于铜。

### 热端口

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Include stator and rotor thermal masses** — 用于包含定子和转子热质量的选项 `On`（默认） | `Off`

用于包含定子和转子热质量的选项。

### **Thermal mass for each stator winding** — 绕组热质量 `100` `J/K`（默认） | 正标量

每个定子绕组的热质量值。热质量是将温度升高一度所需的能量。

#### 依赖关系

要启用此参数，请选择 **Include stator and rotor thermal masses** 参数。

### **Rotor thermal mass** — 转子热质量 `200` `J/K`（默认） | 正标量

转子的热质量。热质量是将转子温度升高一度所需的能量。

#### 依赖关系

要启用此参数，请选择 **Include stator and rotor thermal masses** 参数。

## 所属库

Simscape / Electrical / Electromechanical / Asynchronous

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

以磁链定义的绕线转子感应电机

FEM-Parameterized Induction Machine (Wound Rotor) 模块使用磁链表对绕线转子感应电机进行建模。

您可以使用有限元工具（例如 ANSYS Motor-CAD 软件）生成磁链表。

绕线转子异步电机是一种感应电机。您可以访问模块上的所有定子和转子连接。因此，您可以使用星形和三角形配置之间的切换，或通过增加转子电阻来模拟软启动工况。如果不需要访问转子绕组，可以改用 FEM-Parameterized Induction Machine (Squirrel Cage) 模块。

将端口 **~1** 连接到三相电路。要以三角形配置连接定子，请在端口 **~1** 和 **~2** 之间连接一个 Phase Permute 模块。要以星形配置连接定子，请将端口 **~2** 连接到 Grounded Neutral (Three-Phase) 或 Floating Neutral (Three-Phase) 模块。

如果不需要改变转子电阻，请将转子端口 **~1r'** 连接到 Floating Neutral (Three-Phase) 模块，并将转子端口 **~2r'** 连接到 Grounded Neutral (Three-Phase) 模块。

转子电路折算到定子。因此，在电路中使用该模块时，请将任何额外的电路参数折算到定子。

### 方程

三相绕线转子感应电机由带有三个铜绕组的铁定子叠片和带有三个铜绕组的转子叠片组成。

当三相交流电源为定子供电时，电流产生旋转磁场。该旋转磁场在转子绕组中感应出电流，从而在转子中产生磁场。这些磁场与电流之间的相互作用在转子中产生转矩，使转子开始运动。

感应电机方程在以转子磁场定向的同步参考坐标系 (SRFORF) 中表示。该坐标系与定子和转子磁场同步，并且 *D* 轴与转子磁场 *D* 轴对齐。在此坐标系中，转子磁链矢量仅具有 *D* 轴分量。*Q* 轴分量为零。

λ′qr=0.

- λs→ 是定子磁场矢量。
- λr→ 是转子磁场矢量。
- is→ 是定子电流矢量。

所有这些矢量均以同步速度 *ωe* 旋转。同步角 *θe* 跟踪定子电流矢量的方向。

转子电流矢量以下列方程给出的速度旋转：

ωslip=ωe−Nppωr,

其中 *ωr* 是转子机械速度，*Npp* 是 **Number of pole pairs** 参数。

为了在 SRFORF 参考坐标系中表示定子 *a*、*b* 和 *c* 相电压和电流，可以使用 Park 变换：

Ps=2/3[cosθecos(θe−2π/3)cos(θe+2π/3)−sinθe−sin(θe−2π/3)−sin(θe+2π/3)0.50.50.5],

其中 *θe* 是同步速度的时间积分：

θe=∫ωe dt.

然后可以使用以下方程计算定子电压和电流的 *D* 轴和 *Q* 轴分量。

isdq0=Ps⋅isabcvsdq0=Ps⋅vsabc

由于转差，转子 *a*、*b* 和 *c* 相电压和电流不以同步速度旋转。转子电流以转差速度 *ωslip* 旋转。

为了在静止坐标系（*a*、*b* 和 *c* 相）中表示转子 DQ 电流，可以使用 Park 变换：

Pr=2/3[cosθercos(θer−2π/3)cos(θer+2π/3)−sinθer−sin(θer−2π/3)−sin(θer+2π/3)0.50.50.5],

其中 *θer* 是转子转差角，等于转差速度的时间积分：

θer=∫ωslip dt.

然后，可以使用以下方程计算转子电压和电流的 *a*、*b* 和 *c* 分量。

irabc=Pr−1⋅irdq0vrabc=Pr−1⋅vrdq0

在 SRFORF 参考坐标系中，定子和转子电流、电压和磁链与以下基本感应电机方程相关：

- 定子电压方程

  vds=Rsids−ωeλqs+dλdsdtvqs=Rsiqs+ωeλds+dλqsdt
- 转子电压方程

  v′dr=R′ri′dr+dλ′drdtv′qr=R′ri′qr+ωslipλ′dr

  使用后一个转子电压方程计算转差速度，然后可使用该速度计算用于参考坐标系变换的同步速度。

  ωslip  =  v′qr−R′ri′qrλ′dr.
- 绕线转子方程

  v′dr=Vrdv′qr=Vrq

  其中 *Vrd* 和 *Vrq* 分别是端口 **~1r'** 和 **~2r'** 两端的 *D* 轴和 *Q* 轴转子电压。
- 磁链-电流关系

  励磁 *D* 轴电流定义为

  id =  ids+  i′dr,

  并且磁链-电流关系为

  λ′dr=λds−Ltidsλ′qr=λqs−Ltiqs

  其中：

  - *λds* 是针对 *id* 和 *iqs* 的特定组合计算得到的 **Stator d-axis flux linkage table, λds(ids,iqs)**  参数的插值。
  - *λqs* 是针对 *id* 和 *iqs* 的特定组合计算得到的 **Stator q-axis flux linkage table, λqs(ids,iqs)**  参数的插值。
  - *Lt* 是根据磁链表计算得到的瞬态电感的插值。

  转子磁链-电流关系的另一种形式使用 *Lϕ* 电感

  λ′dr=Lϕidλ′qr=Lϕiq

  其中 *Lϕ* 是根据磁链表计算得到的励磁电感表的插值。

  当将后一个关于 *Q* 轴转子磁链的方程与 λ′qr=0 结合时，得到 iq=0，这意味着折算后的转子 *Q* 轴电流与定子 *Q* 轴电流大小相等、方向相反：

  i′qr=−iqs.

  *Lϕ* 由以下方程定义。

  Lϕ=Ls−Lt,

  其中 *Lt* 是瞬态电感，定义为

  Lt=Ls−Lm2L′r.

  在这些方程中，*Ls*、*Lm* 和 L′r 分别是定子电感、励磁电感和折算后的转子电感。这些方程将这些电感关联起来：

  Ls=Lls+LmL′r=L′lr+Lm

  其中 *Lls* 和 L′lr 分别是定子漏感和折算后的转子漏感。
- 转矩方程

  T=32Npp(λdsiqs−λqsids).

### 对热效应建模

您可以公开热端口，以模拟产生的热量和电机温度的影响。要公开热端口并启用 **Temperature Dependence** 和 **Thermal Port** 参数，请将 **Modeling option** 参数设置为以下选项之一：

- `No thermal port` — 该模块包含与定子绕组关联的电气守恒端口，但不包含热端口。
- `Show thermal port` — 该模块包含与定子绕组关联的扩展电气守恒端口，以及每个绕组和转子的热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。您可以使用不同来源指定标称值，包括模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
