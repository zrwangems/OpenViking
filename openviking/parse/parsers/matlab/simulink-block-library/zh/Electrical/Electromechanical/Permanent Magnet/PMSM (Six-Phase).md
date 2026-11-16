---
type: simulink-block
title: 'PMSM (Six-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Permanent Magnet'
documentation_page: 'pmsmsixphase'
documentation_source_path: 'ref/pmsmsixphase.html'
language: zh-CN
chinese_source: worker-translation
---

# PMSM (Six-Phase)

## 端口

### 守恒

### **~ABC** — 定子 ABC 绕组电气

与定子 ABC 绕组关联的三相电气端口。

### **~XYZ** — 定子 XYZ 绕组电气

与定子 XYZ 绕组关联的三相电气端口。

### **n1** — ABC 绕组中性点电气

与 ABC 绕组配置的中性点关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Zero sequence** 设置为 `Include`。

### **n2** — XYZ 绕组中性点电气

与 XYZ 绕组配置的中性点关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Zero sequence** 设置为 `Include`。

### **R** — 电机转子机械旋转

与电机转子关联的机械旋转守恒端口。

### **C** — 电机机壳机械旋转

与电机机壳关联的机械旋转守恒端口。

### **HA** — *a* 相端子热端口 热

与定子绕组 *a* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HB** — *b* 相端子热端口 热

与定子绕组 *b* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HC** — *c* 相端子热端口 热

与定子绕组 *c* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HX** — *x* 相端子热端口 热

与定子绕组 *x* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HY** — *y* 相端子热端口 热

与定子绕组 *y* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HZ** — *z* 相端子热端口 热

与定子绕组 *z* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HR** — 转子热端口 热

与转子关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认） | `Show thermal port`

是否启用模块的热端口，并对将功率转换为热量的损耗效应进行建模。

### 主要

### **Number of pole pairs** — 极对数 `6`（默认） | 标量

转子上的永磁体极对数。

### **Permanent magnet flux linkage parameterization** — 永磁磁链参数化 `Specify flux linkage`（默认） | `Specify torque constant` | `Specify back EMF constant`

永磁磁链，指定为 `Specify flux linkage`、`Specify torque constant` 或 `Specify back EMF constant`。

### **Permanent magnet flux linkage** — 永磁磁链 `0.03` `Wb`（默认） | 标量

任一定子绕组的峰值永磁磁链。

#### 依赖关系

要启用此参数，请将 **Permanent magnet flux linkage parameterization** 设置为 `Specify flux linkage`。

### **Torque constant** — 转矩常数 `0.18` `N*m/A`（默认） | 标量

任一定子绕组的转矩常数。

#### 依赖关系

要启用此参数，请将 **Permanent magnet flux linkage parameterization** 设置为 `Specify torque constant`。

### **Back EMF constant** — 反电动势常数 `0.18` `V/(rad/s)`（默认） | 标量

任一定子绕组的反电动势常数。

#### 依赖关系

要启用此参数，请将 **Permanent magnet flux linkage parameterization** 设置为 `Specify back EMF constant`。

### **Stator parameterization** — 定子参数化 `Specify Ld, Lq, and L0`（默认） | `Specify Ls, Lm, and Ms`

定子参数化，指定为 `Specify Ld, Lq, and L0` 或 `Specify Ls, Lm, and Ms`。

### **Stator d-axis inductance, Ld** — 定子 *d* 轴电感 `0.00019` `H`（默认） | 标量

*d* 轴电感。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ld, Lq, and L0`。

### **Stator q-axis inductance, Lq** — 定子 *q* 轴电感 `0.00025` `H`（默认） | 标量

*q* 轴电感。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ld, Lq, and L0`。

### **Stator zero-sequence inductance, L0** — 定子零序电感 `0.00016` `H`（默认） | 标量

零序电感。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ld, Lq, and L0`。

### **Stator self-inductance per phase, Ls** — 每相定子自感 `0.0002` `H`（默认） | 标量

五个定子绕组中每个绕组的平均自感。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ls, Lm, and Ms`。

### **Stator inductance fluctuation, Lm** — 定子电感波动 `-0.00002` `H`（默认） | 标量

定子绕组的自感和互感随转子角度波动的量。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ls, Lm, and Ms`。

### **Stator mutual inductance, Ms** — 定子互感 `0.00002` `H`（默认） | 标量

定子绕组之间的平均互感。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ls, Lm, and Ms`。

### **Stator resistance per phase, Rs** — 每相定子电阻 `0.013` `Ohm`（默认） | 标量

每个定子绕组的电阻。

### **Zero sequence** — 零序选项 `Include`（默认） | `Exclude`

是否包含或排除零序项。

- `Include` — 包含零序项。选择此选项可优先考虑模型保真度。对于使用 Partitioning 求解器的仿真，使用此选项会导致错误。有关更多信息，请参阅 Increase Simulation Speed Using the Partitioning Solver。
- `Exclude` — 排除零序项。如果优先考虑桌面仿真或实时部署的仿真速度，请选择此选项。

### **Rotor angle definition** — 转子角度测量的参考点 `Angle between the a-phase magnetic axis and the d-axis`（默认） | `Angle between the a-phase magnetic axis and the q-axis`

转子角度测量的参考点。Motor Construction 图显示了默认值 `Angle between the a-phase magnetic axis and the d-axis`。选择此值时，当转子角度为零时，转子和 *a* 相磁通对齐。

当选择 `Angle between the a-phase magnetic axis and the q-axis` 时，当转子角度为零时，*a* 相电流生成最大转矩。

### 机械

### **Rotor inertia** — 转子惯量 `0.01` `kg*m^2`（默认） | 非负标量

连接到机械平移端口 **R** 的转子的惯量。该值可以为零。

### **Rotor damping** — 转子阻尼 `0` `N*m/(rad/s)`（默认） | 非负标量

旋转阻尼。

### 热

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Measurement temperature** — 额定温度 `298.15` `k`（默认） | 实数标量

电机参数对应的温度。

### **Resistance temperature coefficient** — 温度系数 `3.93e-3` `1/K`（默认） | 正标量

方程中将电阻与温度关联的系数 α（适用于所有三个绕组），如 Thermal Model for Actuator Blocks 中所述。默认值 `3.93e-3` 1/K 适用于铜。

### **Permanent magnet flux temperature coefficient** — 永磁磁链温度系数 `-0.001` `1/K`（默认） | 标量

永磁磁通密度随温度变化的相对变化率。使用此参数可在温度升高时线性降低转矩和感生反电动势。

### **Thermal mass for each stator winding** — 绕组热质量 `100` `J/K`（默认） | 正标量

每个定子绕组的热质量值。热质量是将温度升高一度所需的能量。

### **Rotor thermal mass** — 转子热质量 `200` `J/K`（默认） | 正标量

转子的热质量。热质量是将转子温度升高一度所需的能量。

## 所属库

Simscape / Electrical / Electromechanical / Permanent Magnet

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

具有正弦磁通分布的六相永磁同步电机

PMSM (Six-Phase) 模块对具有六相星形绕组的定子的永磁同步电机 (PMSM) 进行建模。如果电机具有六个定子绕组：内置式永磁同步电机 (IPMSM)、表面式永磁同步电机 (SPMSM)、轴向磁通（盘式）电机或 PMSM 伺服电机，则可以使用此模块对这些类型的电机进行建模。

六相 PMSM 有两组三相定子绕组：ABC 组和 XYZ 组。这两组之间有 30 度的相位差。

该图显示了定子绕组的等效电路。

### 方程

定子绕组两端的电压为

[vavbvcvxvyvz]=[Rs000000Rs000000Rs000000Rs000000Rs000000Rs][iaibicixiyiz]+[dψadtdψbdtdψcdtdψxdtdψydtdψzdt],

其中：

- *va*、*vb* 和 *vc* 是从端口 **~ABC** 到中性点端口 **n1** 的各相电压。
- *vx*、*vy* 和 *vz* 是从端口 **~XYZ** 到中性点端口 **n2** 的各相电压。
- *Rs* 是每个定子绕组的等效电阻。
- *ia*、*ib* 和 *ic* 是从端口 **~ABC** 流向端口 **n1** 的电流。
- *ix*、*iy* 和 *iz* 是从端口 **~XYZ** 流向端口 **n2** 的电流。
- dψadt,dψbdt,dψcdt dψxdt, dψydt, and dψzdt 是每个定子绕组中磁通的变化率。

永磁体和六个绕组共同贡献于链接每个绕组的总磁通。总磁通为

[ψaψbψcψxψyψz]=[LaaLabLacLaxLayLazLbaLbbLbcLbxLbyLbzLcaLcbLccLcxLcyLczLxaLxbLxcLxxLxyLxzLyaLybLycLyxLyyLyzLzaLzbLzcLzxLzyLzz][iaibicixiyiz]+[ψamψbmψcmψxmψymψzm],

其中：

- *ψa*、*ψb*、*ψc*、*ψx*、*ψy* 和 *ψz* 是链接每个定子绕组的总磁通。
- *Laa*、*Lbb*、*Lcc*、*Lxx*、*Lyy* 和 *Lzz* 是定子绕组的自感。这些自感是转子电角度 *θe* 的函数，并且取决于定子每相自感 *Ls* 和定子电感波动 *Lm*。

  - θe=Nθr+rotor offset，其中 *θr* 是转子机械角度。
  - 如果相对于 *d* 轴定义转子电角度，则 *rotor offset* 为 `0`；如果相对于 *q* 轴定义转子电角度，则为 `-pi/2`。
  - *Ls* 是定子每相自感。该值是每个定子绕组的平均自感。
  - *Lm* 是定子电感波动。该值是自感和互感随转子角度变化的波动量。
- *Lab*、*Lac*、*Lba* 等是定子绕组的互感。这些互感是转子电角度 *θe* 的函数，并且取决于定子互感 *Ms* 和定子每相自感 *Ls*。

  - *Ms* 是定子互感。该值是定子绕组之间的平均互感。
- *ψam*、*ψbm*、*ψcm*、*ψxm*、*ψym* 和 *ψzm* 是链接定子绕组的永磁体磁通。

链接绕组 *a-a'* 的永磁磁通在 *θe* = 0° 时最大，在 *θe* = 90° 时为零。因此，链接的电机磁通定义为：

[ψamψbmψcmψxmψymψzm]=[ψmcosθeψmcos(θe−2π/3)ψmcos(θe+2π/3)ψmcos(θe−π/6)ψmcos(θe−5π/6)ψmcos(θe+π/2)],

其中 *ψm* 是永磁磁链。

### 简化电气方程

对模块电气方程应用解耦变换，可得到与转子角度无关的转矩表达式。

解耦变换定义为：

P(θe)=13[cosθecos(θe−2π3)cos(θe+2π3)cos(θe−π6)cos(θe−5π6)cos(θe+π2)−sinθe−sin(θe−2π3)−sin(θe+2π3)−sin(θe−π6)−sin(θe−5π6)−sin(θe+π2)1−12−12−323200−32321212−1111000000111].

变换矩阵 *P* 具有以下伪正交性质：

P−1(θe)=3PT(θe).

对定子绕组电压和电流使用解耦变换，可将它们变换到 *dq0* 坐标系，该坐标系与转子角度无关。

为获得 ABC 和 XYZ 组的 *d* 轴、*q* 轴和零序定子电压与磁链，将变换应用于电压和磁链方程：

[vdvqvz1vz2v01v02]=[Rs000000Rs000000Rs000000Rs000000Rs000000Rs][idiqiz1iz2i01i02]+[−ψqψd0000]Nω+ddt[ψdψqψz1ψz2ψ01ψ02]

[ψdψqψz1ψz2ψ01ψ02]=[Ld000000Lq000000L0000000L0000000L0000000L0][idiqiz1iz2i01i02]+[ψm00000]

其中：

- *vd*、*vq*、*vz1*、*vz2*、*v01* 和 *v02* 是 ABC 和 XYZ 组的 *d*、*q*、*z1* 和 *z2* 分量以及零序定子电压，定义为：

  [vdvqvz1vz2v01v02]=P[vavbvcvxvyvz].
- *id*、*iq*、*iz1*、*iz2*、*i01* 和 *i02* 是 ABC 和 XYZ 组的 *d* 轴、*q* 轴和零序定子电流，定义为：

  [idiqiz1iz2i01i02]=P[iaibicixiyiz].
- Ld=Ls+4Ms+3Lm 是定子 *d* 轴电感。
- Lq=Ls+4Ms−3Lm 是定子 *q* 轴电感。
- L0=Ls−2Ms 是定子零序电感。
- *ω* 是转子机械转速。
- *N* 是转子永磁体极对数。

转矩方程定义为：

T=3N[iq(idLd+ψm)−idiqLq].

### 热效应建模

可以公开热端口，以对将功率转换为热量的损耗效应进行建模。要公开热端口，请将 **Modeling option** 参数设置为以下任一项：

- `No thermal port` — 模块包含与定子绕组关联的扩展电气守恒端口，但不包含热端口。
- `Show thermal port` — 模块包含与定子绕组关联的扩展电气守恒端口，以及每个绕组和转子的热守恒端口。

有关在执行机构模块中使用热端口的更多信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期量值的方法。使用基于标称值的系统缩放可提高仿真稳健性。可以使用不同来源指定标称值，包括模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关更多信息，请参阅 System Scaling by Nominal Values。
