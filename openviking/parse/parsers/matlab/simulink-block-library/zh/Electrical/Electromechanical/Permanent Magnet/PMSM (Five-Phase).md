---
type: simulink-block
title: 'PMSM (Five-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Permanent Magnet'
documentation_page: 'pmsmfivephase'
documentation_source_path: 'ref/pmsmfivephase.html'
language: zh-CN
chinese_source: worker-translation
---

# PMSM (Five-Phase)

## 端口

### 守恒

### **a** — *a* 相电气

与 *a* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为
`Star-wound`、
`Pentacle-wound` 或
`Pentagram-wound`。

### **b** — *b* 相电气

与 *b* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为
`Star-wound`、
`Pentacle-wound` 或
`Pentagram-wound`。

### **c** — *c* 相电气

与 *c* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为
`Star-wound`、
`Pentacle-wound` 或
`Pentagram-wound`。

### **d** — *d* 相电气

与 *d* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为
`Star-wound`、
`Pentacle-wound` 或
`Pentagram-wound`。

### **e** — *e* 相电气

与 *e* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为
`Star-wound`、
`Pentacle-wound` 或
`Pentagram-wound`。

### **a1** — *a* 正端连接电气

*自 R2024a 起*

与 *a* 正端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为
`Open-end`。

### **b1** — *b* 正端连接电气

*自 R2024a 起*

与 *b* 正端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为
`Open-end`。

### **c1** — *c* 正端连接电气

*自 R2024a 起*

与 *c* 正端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为
`Open-end`。

### **d1** — *d* 正端连接电气

*自 R2024a 起*

与 *d* 正端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为
`Open-end`。

### **e1** — *e* 正端连接电气

*自 R2024a 起*

与 *e* 正端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为
`Open-end`。

### **a2** — *a* 负端连接电气

*自 R2024a 起*

与 *a* 负端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为
`Open-end`。

### **b2** — *b* 负端连接电气

*自 R2024a 起*

与 *b* 负端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为
`Open-end`。

### **c2** — *c* 负端连接电气

*自 R2024a 起*

与 *c* 负端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为
`Open-end`。

### **d2** — *d* 负端连接电气

*自 R2024a 起*

与 *d* 负端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为
`Open-end`。

### **e2** — *e* 负端连接电气

*自 R2024a 起*

与 *e* 负端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为
`Open-end`。

### **n** — 中性相电气

与中性相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding Type** 设置为
`Star-wound`，并将 **Zero
sequence** 设置为
`Include`。

### **R** — 电机转子机械

与电机转子相关联的机械旋转守恒端口。

### **C** — 电机壳体机械

与电机壳体相关联的机械旋转守恒端口。

### **HA** — *a* 相端子热端口热

与定子绕组 *a* 相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

### **HB** — *b* 相端子热端口热

与定子绕组 *b* 相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

### **HC** — *c* 相端子热端口热

与定子绕组 *c* 相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

### **HD** — *d* 相端子热端口热

与定子绕组 *d* 相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

### **HE** — *e* 相端子热端口热

与定子绕组 *e* 相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

### **HR** — 转子热端口热

与转子相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口，并对将功率转换为热量的损耗效应进行建模。

### 主

### **Winding type** — 绕组配置 `Star-wound`（默认）| `Pentagon-wound` | `Pentacle-wound` | `Open-end`

绕组的配置：

- `Star-wound` — 绕组为星形绕组。
- `Pentagon-wound` — 绕组为五边形绕组。*a* 相连接在端口 **a** 和 **b** 之间，*b* 相连接在端口 **b** 和 **c** 之间，*c* 相连接在端口 **c** 和 **d** 之间，*d* 相连接在端口 **d** 和 **e** 之间，*e* 相连接在端口 **e** 和 **a** 之间。
- `Pentacle-wound` — 绕组为五角星形绕组。*a* 相连接在端口 **a** 和 **d** 之间，*b* 相连接在端口 **b** 和 **e** 之间，*c* 相连接在端口 **c** 和 **a** 之间，*d* 相连接在端口 **d** 和 **b** 之间，*e* 相连接在端口 **e** 和 **c** 之间。
- `Open-end` — 绕组为开端配置。该模块将绕组的每一端作为电气连接暴露出来。

### **Number of pole pairs** — 极对数 `6`（默认）| 标量

转子上的永磁体极对数。

### **Permanent magnet flux linkage parameterization** — 永磁体磁链参数化 `Specify flux linkage`（默认）| `Specify torque constant` | `Specify back EMF constant`

永磁体磁链，指定为 `Specify flux linkage`、`Specify torque constant` 或 `Specify back EMF constant`。

### **Permanent magnet flux linkage** — 永磁体磁链 `0.03` `Wb`（默认）| 标量

任一 stator 绕组的峰值永磁体磁链。

#### 依赖关系

要启用此参数，请将 **Permanent magnet flux linkage** 设置为
`Specify flux linkage`。

### **Torque constant** — 转矩常数 `0.18` `N*m/A`（默认）| 标量

任一 stator 绕组的转矩常数。

#### 依赖关系

要启用此参数，请将 **Permanent magnet flux linkage** 设置为
`Specify torque constant`。

### **Back EMF constant** — 反电动势常数 `0.18` `V/(rad/s)`（默认）| 标量

任一 stator 绕组的反电动势常数。

#### 依赖关系

要启用此参数，请将 **Permanent magnet flux linkage** 设置为
`Specify back EMF constant`。

### **Stator parameterization** — 定子参数化 `Specify Ld, Lq, and L0`（默认）| `Specify Ls, Lm, and Ms`

定子参数化，指定为 `Specify Ld, Lq, and L0`
或 `Specify Ls, Lm, and Ms`。

### **Stator d-axis inductance, Ld** — 定子 *d* 轴电感 `0.00019` `H`（默认）| 标量

*d* 轴电感。

#### 依赖关系

要启用此参数，请将 **Stator
parameterization** 设置为 `Specify Ld, Lq, and
L0`。

### **Stator q-axis inductance, Lq** — 定子 *q* 轴电感 `0.00025` `H`（默认）| 标量

*q* 轴电感。

#### 依赖关系

要启用此参数，请将 **Stator
parameterization** 设置为 `Specify Ld, Lq, and
L0`。

### **Stator zero-sequence inductance, L0** — 定子零序电感 `0.00016` `H`（默认）| 标量

零序电感。

#### 依赖关系

要启用此参数，请执行以下任一操作：

- 将 **Winding Type** 设置为
  `Star-wound`，
  **Zero sequence** 设置为
  `Include`，并将
  **Stator parameterization** 设置为
  `Specify Ld, Lq, and L0`。
- 将 **Winding Type** 设置为
  `Pentagon-wound`。
- 将 **Winding Type** 设置为
  `Pentacle-wound`。

### **Stator self-inductance per phase, Ls** — 每相定子自感 `0.0002` `H`（默认）| 标量

五个定子绕组中每个绕组的平均自感。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为
`Specify Ls, Lm, and Ms`。

### **Stator inductance fluctuation, Lm** — 定子电感波动 `-0.00002` `H`（默认）| 标量

定子绕组的自感和互感随转子角度波动的量。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为
`Specify Ls, Lm, and Ms`。

### **Stator mutual inductance, Ms** — 定子互感 `0.00002` `H`（默认）| 标量

定子绕组之间的平均互感。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为
`Specify Ls, Lm, and Ms`。

### **Stator resistance per phase, Rs** — 每相定子电阻 `0.013` `Ohm`（默认）| 标量

每个定子绕组的电阻。

### **Zero sequence** — 零序选项 `Include`（默认）| `Exclude`

是否包含或排除零序项。

- `Include` — 包含零序项。选择此选项可优先考虑模型保真度。使用此选项：

  - 对于使用 Partitioning 求解器的仿真会导致错误。有关详细信息，请参阅
    Increase Simulation Speed Using the Partitioning Solver。
  - 在 **Impedances** 设置中暴露一个零序参数。
- `Exclude` — 排除零序项。如果优先考虑桌面仿真或实时部署的仿真速度，请选择此选项。

#### 依赖关系

要启用此参数，请将 **Winding Type** 设置为
`Star-wound`。

### **Rotor angle definition** — 转子角度测量的参考点 `Angle between the a-phase magnetic axis and the d-axis`（默认）| `Angle between the a-phase magnetic axis and the q-axis`

转子角度测量的参考点。Motor Construction 图显示了默认值 `Angle between the a-phase magnetic axis and the d-axis`。当您选择此值时，转子磁通和 *a* 相磁通在转子角度为零时对齐。

当您选择 `Angle between the a-phase magnetic axis and the q-axis` 时，*a* 相电流在转子角度为零时产生最大转矩。

### 机械

### **Rotor inertia** — 转子惯量 `0.01` `kg*m^2`（默认）| 非负标量

连接到机械平移端口 **R** 的转子惯量。该值可以为零。

### **Rotor damping** — 转子阻尼 `0` `N*m/(rad/s)`（默认）| 非负标量

旋转阻尼。

### 热

要启用这些参数，请将 **Modeling option** 设置为
`Show thermal port`。

### **Measurement temperature** — 额定温度 `298.15` `k`（默认）| 实数标量

电机参数的标称温度。

### **Resistance temperature coefficient** — 温度系数 `3.93e-3` `1/K`（默认）| 正标量

所有三个绕组的电阻与温度关系方程中的系数 α，如 Thermal Model for Actuator Blocks 中所述。默认值 `3.93e-3` 1/K 适用于铜。

### **Permanent magnet flux temperature coefficient** — 永磁体磁通温度系数 `-0.001` `1/K`（默认）| 标量

永磁体磁通密度随温度变化的比例速率。使用此参数可随温度升高线性降低转矩和感应反电动势。

### **Thermal mass for each stator winding** — 绕组热质量 `100` `J/K`（默认）| 正标量

每个定子绕组的热质量值。热质量是将温度升高一度所需的能量。

### **Rotor thermal mass** — 转子热质量 `200` `J/K`（默认）| 正标量

转子的热质量。热质量是将转子温度升高一度所需的能量。

## 所属库

Simscape / Electrical / Electromechanical / Permanent Magnet

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a：定子绕组的开端配置

要以开端配置对电机的定子绕组进行建模，请将 **Winding type** 参数设置为
`Open-end`。然后，PMSM (Five-Phase) 模块通过启用相应的电气守恒端口来暴露绕组的每一端。

## 描述

具有正弦磁通分布的五相永磁同步电机

PMSM (Five-Phase) 模块对具有五相星形绕组、五边形绕组或五角星形绕组定子的永磁同步电机 (PMSM) 进行建模。如果电机具有五个定子绕组，请使用此模块对这些类型的电机进行建模：内置式永磁同步电机 (IPMSM)、表贴式永磁同步电机 (SPMSM)、轴向磁通（盘式）电机或 PMSM 伺服电机。该图显示了星形连接定子绕组的等效电路。

您还可以通过将 **Winding type** 设置为 `Pentagon-wound` 或 `Pentacle-wound`，以五边形绕组或五角星形绕组配置对永磁同步电机进行建模。

### 电机结构

此图显示了转子上具有单极对的电机结构。

永磁体产生转子磁场，该磁场基于转子角度产生正弦磁通变化率。

对于坐标轴约定，当您将 **Rotor angle definition** 参数设置为 `Angle between the a-phase magnetic axis and the d-axis` 时，*a* 相磁通和永磁体磁通在转子机械角度 *θr* 为零时对齐。当您将 **Rotor angle definition** 参数设置为 `Angle between the a-phase magnetic axis and the q-axis` 时，转子机械角度是 *a* 相磁轴与转子 *q* 轴之间的角度。

### 方程

定子绕组上的电压为

[vavbvcvdve]=[Rs00000Rs00000Rs00000Rs00000Rs][iaibicidie]+[dψadtdψbdtdψcdtdψddtdψedt],

其中：

- *va*、
  *vb*、
  *vc*、
  *vd* 和
  *ve* 是定子绕组上的各相电压。
- *Rs* 是每个定子绕组的等效电阻。
- *ia*、
  *ib*、
  *ic*、
  *id* 和
  *ie* 是流过定子绕组的电流。
- dψadt、dψbdt、dψcdt、
  dψddt 和 dψedt 是每个定子绕组中磁通的变化率。

永磁体和五个绕组共同贡献于链接每个绕组的总磁通。总磁通为

[ψaψbψcψdψe]=[LaaLabLacLadLaeLbaLbbLbcLbdLbeLcaLcbLccLcdLceLdaLdbLdcLddLdeLeaLebLecLedLee][iaibicidie]+[ψamψbmψcmψdmψem],

其中：

- *ψa*、
  *ψb*、
  *ψc*、
  *ψd* 和
  *ψe* 是链接每个定子绕组的总磁通。
- *Laa*、
  *Lbb*、
  *Lcc*、
  *Ldd* 和
  *Lee* 是定子绕组的自感。这些自感是转子电角度
  *θe* 的函数，并取决于定子每相自感
  *Ls* 和定子电感波动
  *Lm*。

  - θe=Nθr+rotor offset，其中 *θr*
    是转子机械角度。
  - *rotor offset* 为 `pi/2`（如果相对于
    *d* 轴定义转子电角度），或为 `0`（如果相对于
    *q* 轴定义转子电角度）。
  - *Ls* 是定子每相自感。该值是每个定子绕组的平均自感。
  - *Lm* 是定子电感波动。该值是自感和互感随转子角度变化而波动的量。
- *Lab*、
  *Lac*、
  *Lba* 等是定子绕组的互感。这些互感是转子电角度
  *θe* 的函数，并取决于定子互感
  *Ms* 和定子每相自感
  *Ls*。

  - *Ms* 是定子互感。该值是定子绕组之间的平均互感。
- *ψam*、
  *ψbm*、
  *ψcm*、
  *ψdm* 和
  *ψem* 是链接定子绕组的永磁体磁通。

链接绕组 *a-a'* 的永磁体磁通在
*θe* = 0° 时最大，在
*θe* = 90° 时为零。因此，链接的电机磁通定义为：

[ψamψbmψcmψdmψem]=[ψmcosθeψmcos(θr−2π/5)ψmcos(θr−4π/5)ψmcos(θr+4π/5)ψmcos(θr+2π/5)],

其中 *ψm* 是永磁体磁链。

### 简化电气方程

为了消除电感项对转子角度的依赖性，对电机方程执行变换
*T*。

*T* 变换定义为：

T(θe)=25[sinθesin(θe−2π/5)sin(θe−4π/5)sin(θe+4π/5)sin(θe+2π/5)cosθecos(θe−2π/5)cos(θe−4π/5)cos(θe+4π/5)cos(θe+2π/5)sinθesin(θe+4π/5)sin(θe−2π/5)sin(θe+2π/5)sin(θe−4π/5)cosθecos(θe+4π/5)cos(θe−2π/5)cos(θe+2π/5)cos(θe−4π/5)1/21/21/21/21/2],

其中 *θe* 是定义为
*Nθr* 的电角度。*N* 是极对数。

变换矩阵具有以下伪正交性质：

T−1(θe)=52Tt(θe).

对定子绕组电压和电流使用 *T* 变换，将其变换到 dq0 和 xy 坐标系，这些坐标系与转子角度无关：

[vdsvqsvxvyv0]=T[vavbvcvdve]

[idsiqsixiyi0]=T[iaibicidie]

将此变换应用于前两个电气方程，得到以下方程

vds=Rsids+Lddidsdt−NωiqsLq

vqs=Rsiqs+Lqdiqsdt+Nω(idsLd+ψm)

vx=Rsix+Lddixdt

vy=Rsiy+Lqdiydt

v0=Rsi0+L0di0dt

T=52N(iqs(idsLd+ψm)−idsiqsLq)

其中：

- *Ld* =
  *Ls* +
  *Ms* + 5/2
  *Lm*。
  *Ld* 是定子
  *d* 轴电感。
- *Lq* =
  *Ls* +
  *Ms* − 5/2
  *Lm*。
  *Lq* 是定子
  *q* 轴电感。
- *L0* =
  *Ls* –
  4*Ms*。
  *L0* 是定子零序电感。
- *ω* 是转子机械转速。
- *N* 是转子永磁体极对数。

### 替代磁链参数化

您可以通过使用 **Permanent magnet flux linkage** 参数，使用反电动势或转矩常数来参数化电机，这些常数在电机数据表中更常见。

反电动势常数是永磁体在每单位转速下每相感应的峰值电压。峰值永磁体磁链与反电动势之间的关系为：

ke=Nψm.

一相的反电动势 *eph* 为：

eph=keω.

转矩常数是每相每单位电流感应的峰值转矩。当两者均以 SI 单位表示时，其数值与反电动势常数相同：

kt=Nψm.

当 *Ld* =
*Lq* 且所有五相中的电流平衡时，合成转矩 *T* 为：

T=52ktiq=52ktIpk,

其中 *Ipk* 是任一三相绕组中的峰值电流。

因子 5/2 由所有相的稳态转矩之和计算得出。因此，转矩常数 *kt* 也可以为：

kt=25(TIpk),

其中 *T* 是在使用峰值线电压为
*Ipk* 的平衡三相电流进行测试时测得的总转矩。RMS 线电压为：

kt=25(Tiline,rms).

### 模型热效应

您可以暴露热端口来建模将功率转换为热量的损耗效应。要暴露热端口，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 该模块包含与定子绕组相关的扩展电气守恒端口，但不包含热端口。
- `Show thermal port` — 该模块包含与定子绕组相关的扩展电气守恒端口，以及每个绕组和转子的热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。您可以使用不同来源指定标称值，包括模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
