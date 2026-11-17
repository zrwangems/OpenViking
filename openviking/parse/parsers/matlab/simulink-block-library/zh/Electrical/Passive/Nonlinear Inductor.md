---
type: simulink-block
title: 'Nonlinear Inductor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'nonlinearinductor'
documentation_source_path: 'ref/nonlinearinductor.html'
language: zh-CN
chinese_source: worker-translation
---

# Nonlinear Inductor

## 端口
```yaml
ports:
- name: +
  summary: 正极端子电气端口
  direction: conserving
- name: '-'
  summary: 负极端子电气端口
  direction: conserving
```

### 守恒端口

### **+** — 正极端子电气端口

与正极端子关联的电气守恒端口。

### **-** — 负极端子电气端口

与负极端子关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Parameterized by
  summary: 模块参数化方式 Single saturation point（默认）| Single inductance (linear) | Magnetic flux versus current characteristic |
    Magnetic flux density versus magnetic field strength characteristic | Magnetic flux density versus magnetic field strength
    characteristic with hysteresis
  group: 主设置
- name: Number of turns
  summary: 总匝数 10（默认）
  group: 主设置
- name: Unsaturated inductance
  summary: 非饱和电感 2e-4 H（默认）
  group: 主设置
- name: Saturated inductance
  summary: 饱和电感 1e-4 H（默认）
  group: 主设置
- name: Saturation magnetic flux
  summary: 饱和磁通 1.3e-05 Wb（默认）
  group: 主设置
- name: Current vector, i
  summary: 电流数据向量 [0, .64, 1.28, 1.92, 2.56, 3.2] A（默认）
  group: 主设置
- name: Magnetic flux vector, phi
  summary: 磁通数据 [0, 1.29, 2, 2.27, 2.36, 2.39] .* 1e-5 Wb（默认）
  group: 主设置
- name: Magnetic field strength vector, H
  summary: 磁场强度向量 [0, 200, 400, 600, 800, 1000] A/m（默认）| 向量
  group: 主设置
- name: Magnetic flux density vector, B
  summary: 磁通密度数据 [0, .81, 1.25, 1.42, 1.48, 1.49] T（默认）| 向量
  group: 主设置
- name: Effective length
  summary: 有效磁芯长度 0.032 m（默认）| 正有限标量
  group: 主设置
- name: Effective cross-sectional area
  summary: 有效磁芯横截面积 1.6e-5 m^2（默认）| 正有限标量
  group: 主设置
- name: Anhysteretic B-H gradient when H is zero
  summary: 零场强附近无磁滞 B-H 曲线的梯度 0.005 m*T/A（默认）| 标量
  group: 主设置
- name: Flux density point on anhysteretic B-H curve
  summary: 无磁滞 B-H 曲线上的磁通密度点 1.49 T（默认）| 标量
  group: 主设置
- name: Corresponding field strength
  summary: 对应场强 1000 A/m（默认）| 标量
  group: 主设置
- name: Coefficient for reversible magnetization, c
  summary: 可逆磁化系数 0.1（默认）| [0,1] 范围内的标量
  group: 主设置
- name: Bulk coupling coefficient, K
  summary: 体耦合系数 200 A/m（默认）| 有限正标量
  group: 主设置
- name: Inter-domain coupling factor, alpha
  summary: 域间耦合因子 1e-4（默认）| 标量
  group: 主设置
- name: Averaging period for power logging
  summary: 功率记录平均周期 0 s（默认）| 标量
  group: 主设置
- name: Parasitic parallel conductance
  summary: 寄生并联电导 1e-9 1/Ohm（默认）
  group: 主设置
- name: Interpolation option
  summary: 插值选项 Linear（默认）| Smooth
  group: 主设置
- name: Specify initial state by
  summary: 初始状态指定选项 Current（默认）| Magnetic flux
  group: 初始条件
- name: Initial current
  summary: 初始电流 0 A（默认）
  group: 初始条件
- name: Initial magnetic flux
  summary: 初始磁通 0 Wb（默认）
  group: 初始条件
- name: Initial magnetic flux density
  summary: 初始磁通密度 0 T（默认）
  group: 初始条件
- name: Initial field strength
  summary: 初始场强 0 A/m（默认）
  group: 初始条件
```

### 主设置

### **Parameterized by** — 模块参数化方式 `Single saturation point`（默认）| `Single inductance (linear)` | `Magnetic flux versus current characteristic` | `Magnetic flux density versus magnetic field strength characteristic` | `Magnetic flux density versus magnetic field strength characteristic with hysteresis`

用于描述 *B*-*H* 曲线的参数化方法。选择以下选项之一：

- `Single inductance (linear)`
  — 提供匝数、非饱和电感和寄生并联电导的值。
- `Single saturation point`
  — 提供匝数、非饱和电感和饱和电感、饱和磁通以及寄生并联电导的值。
- `Magnetic flux versus current
  characteristic` — 除匝数和寄生并联电导值外，还需提供电流向量和磁通向量，以填充磁通对电流查找表。
- `Magnetic flux density versus magnetic field
  strength characteristic` — 除匝数和寄生并联电导值外，还需提供有效磁芯长度和横截面积的值，以及磁场强度向量和磁通密度向量，以填充磁通密度对磁场强度查找表。
- `Magnetic flux density versus magnetic field
  strength characteristic with hysteresis`
  — 除匝数、有效磁芯长度和横截面积外，还需提供初始无磁滞 *B*-*H* 曲线梯度、*B*-*H* 曲线上某点的磁通密度和场强，以及可逆磁化系数、体耦合系数和域间耦合因子的值，以将磁通密度定义为电流值和场强历史的函数。

### **Number of turns** — 总匝数 `10`（默认）

绕在电感磁芯上的导线总匝数。

### **Unsaturated inductance** — 非饱和电感 `2e-4` `H`（默认）

电感工作在线性区域时的电感值。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Single inductance (linear)` 或 `Single saturation point`。

### **Saturated inductance** — 饱和电感 `1e-4` `H`（默认）

电感工作超过饱和点时的电感值。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Single saturation point`。

### **Saturation magnetic flux** — 饱和磁通 `1.3e-05` `Wb`（默认）

电感饱和时的磁通值。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Single saturation point`。

### **Current vector, i** — 电流数据向量 `[0, .64, 1.28, 1.92, 2.56, 3.2]` `A`（默认）

模块用于填充磁通对电流查找表的电流数据。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Magnetic flux versus current characteristic`。

### **Magnetic flux vector, phi** — 磁通数据 `[0, 1.29, 2, 2.27, 2.36, 2.39] .* 1e-5` `Wb`（默认）

模块用于填充磁通对电流查找表的磁通数据。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Magnetic flux versus current characteristic`。

### **Magnetic field strength vector, H** — 磁场强度向量 `[0, 200, 400, 600, 800, 1000]` `A/m`（默认）| 向量

磁场强度 *H*，指定为与磁通密度向量 *B* 元素数量相同的向量。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Magnetic flux density versus magnetic field strength characteristic`。

### **Magnetic flux density vector, B** — 磁通密度数据 `[0, .81, 1.25, 1.42, 1.48, 1.49]` `T`（默认）| 向量

磁通密度 *B*，指定为与磁场强度向量 *H* 元素数量相同的向量。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Magnetic flux density versus magnetic field strength characteristic`。

### **Effective length** — 有效磁芯长度 `0.032` `m`（默认）| 正有限标量

有效磁芯长度。此参数表示磁芯周围磁路的平均长度。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Magnetic flux density versus magnetic field strength characteristic` 或 `Magnetic flux density versus magnetic field strength characteristic with hysteresis`。

### **Effective cross-sectional area** — 有效磁芯横截面积 `1.6e-5` `m^2`（默认）| 正有限标量

有效磁芯横截面积。此参数表示磁芯周围磁路的平均面积。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Magnetic flux density versus magnetic field strength characteristic` 或 `Magnetic flux density versus magnetic field strength characteristic with hysteresis`。

### **Anhysteretic B-H gradient when H is zero** — 零场强附近无磁滞 B-H 曲线的梯度 `0.005` `m*T/A`（默认）| 标量

零场强附近无磁滞 *B*-*H* 曲线的梯度。将此参数设置为上升和下降磁滞曲线的平均梯度。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Magnetic flux density versus magnetic field strength characteristic with hysteresis`。

### **Flux density point on anhysteretic B-H curve** — 无磁滞 B-H 曲线上的磁通密度点 `1.49` `T`（默认）| 标量

用于场强测量的点的磁通密度。您必须通过提供磁通密度值来指定无磁滞曲线上的一个点。为获得准确结果，请选择高场强处上升和下降磁滞曲线重合的点。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Magnetic flux density versus magnetic field strength characteristic with hysteresis`。

### **Corresponding field strength** — 对应场强 `1000` `A/m`（默认）| 标量

与通过 **Flux density point on anhysteretic B-H curve** 参数定义的点相对应的场强。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Magnetic flux density versus magnetic field strength characteristic with hysteresis`。

### **Coefficient for reversible magnetization, c** — 可逆磁化系数 `0.1`（默认）| [0,1] 范围内的标量

Jiles-Atherton 方程中的可逆磁化系数 *c*。此参数表示可逆磁化的比例。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Magnetic flux density versus magnetic field strength characteristic with hysteresis`。

### **Bulk coupling coefficient, K** — 体耦合系数 `200` `A/m`（默认）| 有限正标量

Jiles-Atherton 方程中的体耦合系数 *K*。此参数主要控制 *B*-*H* 曲线穿过零磁通密度线时的场强幅值。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Magnetic flux density versus magnetic field strength characteristic with hysteresis`。

### **Inter-domain coupling factor, alpha** — 域间耦合因子 `1e-4`（默认）| 标量

Jiles-Atherton 方程中的域间耦合因子 *α*。此参数主要影响 *B*-*H* 曲线与零场强线的交点。典型值在 `1e-4` 到 `1e-3` 范围内。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Magnetic flux density versus magnetic field strength characteristic with hysteresis`。

### **Averaging period for power logging** — 功率记录平均周期 `0` `s`（默认）| 标量

磁滞损耗计算的平均周期。这些损耗与 *B*-*H* 轨迹所包围的面积成正比。如果您以已知的固定频率激励模块，可以将此值设置为相应的激励周期以计算磁滞损耗。模块在每个 AC 周期将磁滞损耗记录到仿真数据日志中的 `power_dissipated` 变量中。如果您使用定步长求解器，此值必须是仿真步长的整数倍。

如果您不以已知的固定频率激励模块，请将此参数设置为 `0`。模块将仿真数据日志中的 `power_dissipated` 变量设置为 `0`。您可以通过后处理仿真数据日志中的 `power_instantaneous` 变量来计算实际的磁滞损耗。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Magnetic flux density versus magnetic field strength characteristic with hysteresis`。

### **Parasitic parallel conductance** — 寄生并联电导 `1e-9` `1/Ohm`（默认）

寄生并联电导。使用此参数表示小的寄生效应。对于某些电路拓扑，您需要一个小值的并联电导。

### **Interpolation option** — 插值选项 `Linear`（默认）| `Smooth`

查找表插值选项。选择以下插值方法之一：

- `Linear` — 选择此选项以获得最佳性能。
- `Smooth` — 选择此选项以生成具有连续一阶导数的连续曲线。

有关插值算法的更多信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Magnetic flux versus current characteristic` 或 `Magnetic flux density versus magnetic field strength characteristic`。

### 初始条件

### **Specify initial state by** — 初始状态指定选项 `Current`（默认）| `Magnetic flux`

初始状态指定方式。选择以下选项之一：

- `Current` — 通过电感初始电流 *i*L 指定电感的初始状态。
- `Magnetic flux` — 通过磁通指定电感的初始状态。

#### 依赖关系

要启用此参数，请在 **Main** 设置中将 **Parameterized by** 参数设置为以下选项之一：

- `Single inductance
  (linear)`
- `Single saturation
  point`
- `Magnetic flux versus current
  characteristic`
- `Magnetic flux density versus magnetic field
  strength characteristic`

### **Initial current** — 初始电流 `0` `A`（默认）

模块用于计算零时刻磁通值的初始电流值。此参数为流过电感的电流。元件电流由流过电感的电流和流过寄生并联电导的电流组成。

#### 依赖关系

要启用此参数，请将 **Specify initial state by** 设置为 `Current`。

### **Initial magnetic flux** — 初始磁通 `0` `Wb`（默认）

零时刻的磁通。

#### 依赖关系

要启用此参数，请将 **Specify initial state by** 设置为 `Magnetic flux`。

### **Initial magnetic flux density** — 初始磁通密度 `0` `T`（默认）

零时刻的磁通密度。

#### 依赖关系

要启用此参数，请在 **Main** 设置中将 **Parameterized by** 参数设置为 `Magnetic flux density versus magnetic field strength characteristic with hysteresis`。

### **Initial field strength** — 初始场强 `0` `A/m`（默认）

零时刻的磁场强度。

#### 依赖关系

要启用此参数，请在 **Main** 设置中将 **Parameterized by** 参数设置为 `Magnetic flux density versus magnetic field strength characteristic with hysteresis`。
## 所属库

Simscape / Electrical / Passive

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

## 描述

具有非理想磁芯的电感

Nonlinear Inductor 模块表示具有非理想磁芯的电感。磁芯可能因其磁特性和尺寸而非理想。要在这些参数化选项之间进行选择，请使用 **Parameterized by** 参数：

- Single inductance
  (linear)
- Single saturation
  point
- Magnetic flux versus
  current characteristic
- Magnetic flux density
  versus magnetic field strength characteristic
- Magnetic flux density
  versus magnetic field strength characteristic with hysteresis

### 单一电感（线性）

以下方程定义了电压、电流和磁通之间的关系，

i=iL+vGp

v=NwdΦdt

Φ=LNwiL

其中：

- *v* 是端子电压。
- *i* 是端子电流。
- *i*L 是流过电感的电流。
- *G*p 是寄生并联电导。
- *N*w 是绕组匝数。
- *Φ* 是磁通。
- *L* 是非饱和电感。

### 单一饱和点

以下方程定义了电压、电流和磁通之间的关系，

i=iL+vGp

v=NwdΦdt

Φ=LNwiL（非饱和时）

Φ=LsatNwiL±Φoffset（饱和时）

其中：

- *v* 是端子电压。
- *i* 是端子电流。
- *i*L 是流过电感的电流。
- *G*p 是寄生并联电导。
- *N*w 是绕组匝数。
- *Φ* 是磁通。
- *Φ*offset 是磁通饱和偏移量。
- *L* 是非饱和电感。
- *L*sat 是饱和电感。

### 磁通对电流特性

以下方程定义了电压、电流和磁通之间的关系，

i=iL+vGp

v=NwdΦdt

Φ=f(iL)

其中：

- *v* 是端子电压。
- *i* 是端子电流。
- *i*L 是流过电感的电流。
- *G*p 是寄生并联电导。
- *N*w 是绕组匝数。
- *Φ* 是磁通。

模块通过基于您提供的电流值向量和对应磁通值向量的一维查找表来确定磁通。您可以使用负值和正值数据，或仅使用正值数据来构造这些向量。如果仅使用正值数据，向量的第一个元素必须为 0。模块通过将正值数据绕 (0,0) 旋转 180° 来计算负值。

### Magnetic Flux Density Versus Magnetic Field Strength Characteristic

这些方程定义了电压、电流和磁通之间的关系，

i=iL+vGp

v=NwdΦdt

Φ=B⋅Ae

B=f(H)

H=NwleiL

其中：

- *v* 是端电压。
- *i* 是端电流。
- *i*L 是通过电感的电流。
- *G*p 是寄生并联电导。
- *N*w 是绕组匝数。
- *Φ* 是磁通。
- *B* 是磁通密度。
- *H* 是磁场强度。
- *l*e 是有效磁芯长度。
- *A*e 是有效磁芯横截面积。

该模块通过一维查表确定磁通密度，基于您提供的磁场强度值向量和对应的磁通密度值向量。您可以使用负值和正值数据，或仅使用正值数据来构造这些向量。如果仅使用正值数据，向量的第一个元素必须为 0。该模块通过将正值数据绕 (0,0) 旋转 180° 来计算负值。

### Magnetic Flux Density Versus Magnetic Field Strength Characteristic with Hysteresis

这些方程定义了电压、电流和磁通之间的关系，

i=iL+vGp

v=NwdΦdt

Φ=B⋅Ae

B=μ0(H+M)

H=NwleiL

其中：

- *v* 是端电压。
- *i* 是端电流。
- *i*L 是通过电感的电流。
- *G*p 是寄生并联电导。
- *N*w 是绕组匝数。
- *Φ* 是磁通。
- *B* 是磁通密度。
- *μ*0 是真空磁导率。
- *H* 是磁场强度。
- *M* 是电感磁芯的磁化强度。
- *l*e 是有效磁芯长度。
- *A*e 是有效磁芯横截面积。

磁化作用会增加磁通密度，其值取决于当前值和磁场强度的历史。该模块使用 Jiles-Atherton 1, 2] 方程来确定任意给定时刻的 *M*。下图显示了 *B* 和 *H* 之间所得关系的典型曲线。

当磁场强度从 *H* = 0 增加时，曲线最初沿上升磁滞曲线变化。在饱和点，磁场强度的进一步增加不再导致磁通的显著增加。

当您从饱和点降低磁场强度时，曲线沿下降磁滞曲线变化。上升曲线和下降曲线之间的差异是由于 *M* 对轨迹历史的依赖性。从物理上讲，这种行为对应于磁芯中的磁偶极子随着磁场强度的增加而排列，但当磁场强度减小时并未完全恢复到其原始位置。

Jiles-Atherton 方程的起点是将磁化效应分为两部分，一部分是有效磁场强度 *Heff* 的纯函数，另一部分是不可逆部分，取决于历史。该方程定义了非磁滞磁化 *Man* 和不可逆磁化 *Mirr* 对总磁化 *M* 的相对贡献，

M=cMan+(1−c)Mirr,

其中 *c* 是可逆磁化系数。

该方程将 *Man* 与等效磁化 *Heff* 关联起来：

Man=Ms(coth(Heffa)−aHeff).

该函数定义了具有极限值 ±*Ms* 的饱和曲线，其中：

- *M*s 是*饱和磁化强度*。
- *a* 是*非磁滞磁化系数*，它决定了饱和点。它近似描述了两条磁滞曲线的平均值。

在 Nonlinear Inductor 模块掩膜中，您需要提供当 *H*eff = 0 时的 dMan/dHeff 值以及非磁滞 *B*-*H* 曲线上的一个点 [*H*1, *B*1]。该模块使用这些值来确定 *a* 和 *M*s 的值。

Jiles-Atherton 模型通过关于磁场强度的偏导数来定义不可逆项，

dMirrdH=Man−MirrKδ−α(Man−Mirr)δ={1if dHdt≥0−1if dHdt<0

其中：

- *K* 是*体耦合系数*，它决定了不可逆特性的形状。
- *α* 是*域间耦合因子*。

将该方程与标准一阶微分方程进行比较可以发现，当您改变总磁场强度 *H* 时，不可逆项 *Mirr* 试图跟踪可逆项 *Man*，但具有可变跟踪增益 1/(Kδ−α(Man−Mirr))。跟踪误差在 *δ* 改变符号的点处产生磁滞。

该方程定义了非磁滞曲线的有效磁场强度，

Heff=H+αM.

*α* 的值影响磁滞曲线的形状。较大的值会增加 *B* 轴截距。然而，稳定性项 Kδ−α(Man−Mirr) 对于 *δ* > 0 必须为正，对于 *δ* < 0 必须为负。因此，您可以提供的 *α* 值存在限制。典型的最大值约为 1e-3 量级。

**寻找 Jiles-Atherton (JA) 方程系数近似值的步骤**

您可以使用以下步骤确定方程系数的代表性值：

1. 为 **Anhysteretic B-H gradient when H is zero** 参数（当 *Heff* = 0 时的 dMan/dHeff）提供一个值，以及非磁滞 *B*-*H* 曲线上的一个数据点 [*H*1, *B1*]。根据这些值，模块初始化确定 *α* 和 *M*s 的值。
2. 设置 **Coefficient for reversible magnetization, c** 参数，以在从 [*H* *B*] = [0 0] 开始仿真时获得正确的初始 *B*-*H* 梯度。*c* 的值大约是该初始梯度与 **Anhysteretic B-H gradient when H is zero** 的比值。*c* 的值必须大于 0 且小于 1。
3. 将 **Bulk coupling coefficient, K** 参数设置为上升磁滞曲线上 *B* = 0 时 *H* 的近似幅值。
4. 从 **Inter-domain coupling factor, alpha** 参数的一个非常小的值开始，然后逐渐增大它以调整穿过 *H* = 0 线时的 *B* 值。典型值在 1e-4 到 1e-3 的范围内。过大的值会导致 *B*-*H* 曲线的梯度趋于无穷大，这是非物理的，并会产生运行时断言错误。

要获得与预定义 *B*-*H* 曲线的良好匹配，请对这四步进行迭代。
