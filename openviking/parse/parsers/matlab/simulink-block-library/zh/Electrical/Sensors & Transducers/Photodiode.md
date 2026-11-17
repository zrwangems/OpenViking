---
type: simulink-block
title: 'Photodiode'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'photodiode'
documentation_source_path: 'ref/photodiode.html'
language: zh-CN
chinese_source: worker-translation
---

# Photodiode

## 端口

### 输出

### **W** — 入射通量物理信号

与入射通量关联的物理信号端口。
### 守恒

### **+** — 正极端子电气

与阳极关联的电气守恒端口。

### **-** — 负极端子电气

与阴极关联的电气守恒端口。

### **H** — 热端口热

热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口并对产生的热量和设备温度的影响进行建模。

### 主

### **Sensitivity parameterization** — 灵敏度参数化 `Specify measured current for given flux density`（默认）| `Specify current per unit flux density`

选择以下灵敏度参数化方法之一：

- `Specify measured current for given flux density` —
  指定测得的电流及对应的通量密度。这是默认方法。
- `Specify current per unit flux density` — 直接指定
  器件灵敏度。

### **Measured current** — 测得电流 `25` `uA`（默认）

模块用于计算器件灵敏度的电流。

#### 依赖关系

仅当为 **Sensitivity
parameterization** 参数选择 `Specify measured current
for given flux density` 时，此参数才可见。

### **Flux density** — 通量密度 `5` `W/m^2`（默认）

模块用于计算器件灵敏度的通量密度。

#### 依赖关系

仅当为 **Sensitivity
parameterization** 参数选择 `Specify measured current
for given flux density` 时，此参数才可见。

### **Device sensitivity** — 器件灵敏度 `5e-06` `m^2*A/W`（默认）

单位通量密度对应的电流。

#### 依赖关系

仅当为 **Sensitivity parameterization**
参数选择 `Specify current per unit
flux density` 时，此参数才可见。

### **Diode parameterization** — 二极管参数化 `Use dark current plus a forward bias I-V data point`（默认）| `Use dark current and N`

选择以下二极管模型参数化方法之一：

- `Use dark current plus a forward bias I-V data point`
  — 指定暗电流和二极管 I-V 曲线上的一个点。这是默认方法。
- `Use dark current and N` — 指定暗电流和
  发射系数。

### **Current I1** — 正向偏置点处的电流 `0.1` `A`（默认）

二极管 I-V 曲线上正向偏置点处的电流，模块使用该值计算
*IS* 和 *N*。

#### 依赖关系

仅当为 **Diode
parameterization** 参数选择 `Use dark current plus a
forward bias I-V data point` 时，此参数才可见。

### **Voltage V1** — 正向偏置点处的电压 `1.3` `V`（默认）

二极管 I-V 曲线上正向偏置点处的对应电压，模块使用该值计算
*IS* 和 *N*。

#### 依赖关系

仅当为 **Diode
parameterization** 参数选择 `Use dark current plus a
forward bias I-V data point` 时，此参数才可见。

### **Dark current** — 暗电流 `5e-9` `A`（默认）

二极管未暴露于光照时通过二极管的电流。

### **Emission coefficient, N** — 发射系数 `3`（默认）

二极管发射系数或理想因子。

#### 依赖关系

仅当为 **Diode parameterization** 参数选择 `Use dark current and
N` 时，此参数才可见。

### **Ohmic resistance, RS** — 串联二极管连接电阻 `0.1` `Ohm`（默认）

串联二极管连接电阻。

### **Measurement temperature** — 测量温度 `25` `degC`（默认）

测量 I-V 曲线或暗电流时的温度。

### 结电容

### **Parameterization** — 结电容参数化 `Fixed or zero junction capacitance`（默认）| `Use C-V curve data points` | `Use parameters CJ0, VJ, M & FC`

选择以下结电容建模选项之一：

- `Fixed or zero junction capacitance` — 将
  结电容建模为固定值。
- `Use C-V curve data points` — 指定
  二极管 C-V 曲线上三个点的测量数据。
- `Use parameters CJ0, VJ, M & FC` —
  指定零偏结电容、结电势、梯度系数
  和正向偏置耗尽电容系数。

### **Junction capacitance** — 结电容 `60` `pF`（默认）

结电容的固定值。

#### 依赖关系

仅当为 **Parameterization**
参数选择 `Fixed or zero
junction capacitance` 时，此参数才可见。

### **Zero-bias junction capacitance, CJ0** — 零偏结电容 `60` `pF`（默认）

与指数二极管项并联的电容值。

#### 依赖关系

仅当为 **Parameterization**
参数选择 `Use parameters CJ0, VJ, M
& FC` 时，此参数才可见。

### **Reverse bias voltages [VR1 VR2 VR3]** — 反向偏置电压 `[ 0.1 10 100 ]` `V`（默认）

二极管 C-V 曲线上三个点处的反向偏置电压值向量，
模块使用该向量计算 *CJ0*、*VJ* 和
*M*。

#### 依赖关系

仅当为 **Parameterization**
参数选择 `Use C-V curve data
points` 时，此参数才可见。

### **Corresponding capacitances [C1 C2 C3]** — 对应电容 `[ 45 3 6 ]` `pF`（默认）

二极管 C-V 曲线上三个点处的电容值向量，
模块使用该向量计算 *CJ0*、*VJ* 和
*M*。

#### 依赖关系

仅当为 **Parameterization**
参数选择 `Use C-V curve data
points` 时，此参数才可见。

### **Junction potential, VJ** — 结电势 `1` `V`（默认）

结电势。

#### 依赖关系

仅当为 **Parameterization**
参数选择 `Use parameters CJ0, VJ, M
& FC` 时，此参数才可见。

### **Grading coefficient, M** — 梯度系数 `0.5`（默认）

梯度系数。

#### 依赖关系

仅当为 **Parameterization**
参数选择 `Use parameters CJ0, VJ, M
& FC` 时，此参数才可见。

### **Capacitance coefficient, FC** — 电容系数 `0.5`（默认）

拟合系数，用于量化耗尽电容随施加电压的减小。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Use C-V curve data
points` 或 `Use parameters CJ0, VJ, M &
FC` 时，此参数才可见。

### 温度依赖性

### **Parameterization** — 温度依赖性参数化 `None — Simulate at parameter measurement temperature`（默认）| `Use an I-V data point at second measurement temperature T2` | `Specify saturation current at second measurement temperature T2` | `Specify the energy gap EG`

选择以下温度依赖性参数化方法之一：

- `None — Simulate at parameter measurement temperature`
  — 不对温度依赖性建模，或在测量温度 *T*m1 下仿真模型
  （由 **Main** 选项卡上的
  **Measurement temperature** 参数指定）。这是默认方法。
- `Use an I-V data point at second measurement temperature T2`
  — 如果选择此选项，则指定第二个测量温度
  *T*m2，以及该温度下的电流和电压值。模型使用这些值
  以及第一个测量温度 *T*m1 下的参数值
  来计算能量间隙值。
- `Specify saturation current at second measurement temperature
  T2` — 如果选择此选项，则指定第二个测量
  温度 *T*m2，以及该温度下的饱和电流值。模型使用这些值
  以及第一个测量温度 *T*m1 下的参数值
  来计算能量间隙值。
- `Specify the energy gap EG` — 直接指定能量间隙
  值。

### **Current I1 at second measurement temperature** — 第二测量温度下的电流 I1 `0.07` `A`（默认）

指定在第二测量温度下电压为
*V1* 时的二极管电流 *I1* 值。

#### 依赖关系

仅当为
**Parameterization** 参数选择 `Use an I-V data point at
second measurement temperature T2` 时，此参数才可见。

### **Voltage V1 at second measurement temperature** — 第二测量温度下的电压 V1 `1.3` `V`（默认）

指定在第二测量温度下电流为
*I1* 时的二极管电压 *V1* 值。

#### 依赖关系

仅当为
**Parameterization** 参数选择 `Use an I-V data point at
second measurement temperature T2` 时，此参数才可见。

### **Saturation current, IS, at second measurement temperature** — 第二测量温度下的饱和电流 IS `2.5e-7` `A`（默认）

指定第二测量温度下的饱和电流 *IS* 值。

#### 依赖关系

仅当为
**Parameterization** 参数选择 `Specify saturation current
at second measurement temperature T2` 时，此参数才可见。

### **Second measurement temperature** — 第二测量温度 `125` `degC`（默认）

指定第二测量温度的值。

#### 依赖关系

仅当为
**Parameterization** 参数选择 `Use an I-V data point at
second measurement temperature T2` 或 `Specify saturation current
at second measurement temperature T2` 时，此参数才可见。

### **Energy gap parameterization** — 能量间隙参数化 `Use nominal value for silicon (EG=1.11eV)`（默认）| `Use nominal value for 4H-SiC silicon carbide (EG=3.23eV)` | `Use nominal value for 6H-SiC silicon carbide (EG=3.00eV)` | `Use nominal value for germanium (EG=0.67eV)` | `Use nominal value for gallium arsenide (EG=1.43eV)` | `Use nominal value for selenium (EG=1.74eV)` | `Use nominal value for Schottky barrier diodes (EG=0.69eV)` | `Specify a custom value`

从预定选项列表中选择能量间隙值，或指定自定义值：

- `Use nominal value for silicon (EG=1.11eV)` — 这是
  默认值。
- `Use nominal value for 4H-SiC silicon carbide (EG=3.23eV)`
- `Use nominal value for 6H-SiC silicon carbide (EG=3.00eV)`
- `Use nominal value for germanium (EG=0.67eV)`
- `Use nominal value for gallium arsenide (EG=1.43eV)`
- `Use nominal value for selenium (EG=1.74eV)`
- `Use nominal value for Schottky barrier diodes (EG=0.69eV)`
- `Specify a custom value` — 如果选择此选项，
  对话框中会出现 **Energy gap, EG** 参数，以便您
  为 *EG* 指定自定义值。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Specify the energy gap
EG` 时，此参数才可见。

### **Energy gap, EG** — 能量间隙 `1.11` `eV`（默认）

为能量间隙 *EG* 指定自定义值。

#### 依赖关系

仅当为 **Energy gap parameterization**
参数选择 `Specify a custom
value` 时，此参数才可见。

### **Saturation current temperature exponent parameterization** — 饱和电流温度指数参数化 `Use nominal value for pn-junction diode (XTI=3)`（默认）| `Use nominal value for Schottky barrier diode (XTI=2)` | `Specify a custom value`

选择以下选项之一来指定饱和电流温度指数值：

- `Use nominal value for pn-junction diode (XTI=3)` —
  这是默认值。
- `Use nominal value for Schottky barrier diode (XTI=2)`
- `Specify a custom value` — 如果选择此选项，
  对话框中会出现 **Saturation current temperature exponent, XTI** 参数，
  以便您为 *XTI* 指定自定义值。

### **Saturation current temperature exponent, XTI** — 饱和电流温度指数 `3`（默认）

为饱和电流温度指数
*XTI* 指定自定义值。

#### 依赖关系

仅当为 **Saturation current temperature exponent
parameterization** 参数选择 `Specify a custom
value` 时，此参数才可见。

### **Device simulation temperature** — 器件仿真温度 `25` `degC`（默认）

指定器件仿真温度 *T*s 的值。

## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

### R2024a：**Junction capacitance voltage** 变量已替换为 **Charge of junction capacitance** 变量

如果在 **Capacitance** 部分中，将
**Parameterization** 设置为 `Use C-V curve data
points` 或 `Use parameters Cj0, VJ, M & FC`，则
现在使用 **Charge of junction
capacitance** 变量为电容和电荷建模指定 **Initial Targets** 和 **Nominal Values**。
**Junction capacitance voltage**
变量不再启用。

如果在早期版本中创建的模型使用这些值进行
**Parameterization**，并为 **Junction capacitance
voltage** 变量指定了 **Initial Targets**
或 **Nominal Values**，则必须更新该模型。有关如何
计算结电容电荷的详细信息，请参阅描述。

## 描述

具有入射通量输入端的光电二极管

光电二极管模块将光电二极管表示为一个受控电流源和一个指数二极管并联连接。受控电流源产生一个与辐射通量密度成正比的电流 *Ip*：

|  |  |
| --- | --- |
| *Ip* = *DeviceSensitivity* · *RadiantFluxDensity* | **(1)** |

其中：

- *DeviceSensitivity* 是产生的电流与入射辐射通量密度之比。

  - 如果为 **Sensitivity parameterization** 参数选择 `Specify measured current for given flux density`，则该模块通过将 **Measured current** 参数值转换为安培单位并除以 **Flux density** 参数值来计算此变量。
  - 如果为 **Sensitivity parameterization** 参数选择 `Specify current per unit flux density`，则该变量由 **Device sensitivity** 参数值定义。
- *RadiantFluxDensity* 是入射辐射通量密度。

要对动态响应时间进行建模，请使用 **Junction capacitance** 选项卡中的 **Parameterization** 参数将二极管结电容包含在模型中。

指数二极管模型提供二极管电流 *I* 与二极管电压 *V* 之间的以下关系：

I=IS⋅(eqVNkTm1−1)

其中：

- *q* 是电子的基本电荷（1.602176e–19 库仑）。
- *k* 是玻尔兹曼常数（1.3806503e–23 J/K）。
- *N* 是发射系数。
- *IS* 是饱和电流，等于 **Dark current** 参数值。
- *Tm1* 是指定二极管参数时的温度，由 **Measurement temperature** 参数值定义。

当 (*q**V* / *N**k**Tm1*) > 80 时，模块将 eqVNkTm1 替换为 (*q**V* / *N**k**Tm1* – 79)e80，这与 (*q**V* / *N**k**Tm1*) = 80 处二极管电流的梯度相匹配并进行线性外推。当 (*q**V* / *N**k**Tm1*) < –79 时，模块将 eqVNkTm1 替换为 (*q**V* / *N**k**Tm1* + 80)e–79，这也与梯度相匹配并进行线性外推。典型电路不会达到这些极端值。模块提供此线性外推以帮助在仿真期间求解约束时收敛。

当为 **Diode parameterization** 参数选择 `Use dark current and N` 时，您通过 **Dark current** 和 **Emission coefficient N** 参数来指定二极管。当为 **Diode parameterization** 参数选择 `Use dark current plus a forward bias I-V data point` 时，您指定 **Dark current** 参数以及二极管 I-V 曲线上的一个电压和电流测量点。模块根据这些值计算 *N* 如下：

N=VF/(Vtlog(IF/IS+1))

其中：

- *VF* 是 **Forward voltage VF** 参数值。
- *Vt* = *k**Tm1* / *q*。
- *IF* 是 **Current IF at forward voltage VF** 参数值。

指数二极管模型提供包含结电容的选项：

- 当为 **Parameterization** 参数选择 `Fixed or zero junction capacitance` 时，电容是固定的。
- 当为 **Parameterization** 参数选择 `Use parameters CJO, VJ, M & FC` 时，模块使用系数 *CJO*、*VJ*、*M* 和 *FC* 来计算取决于结电压的结电容。
- 当为 **Parameterization** 参数选择 `Use C-V curve data points` 时，模块使用 C-V 电容曲线上的三个电容值来估算 *CJO*、*VJ* 和 *M*，并将这些值与指定的 *FC* 值一起使用来计算取决于结电压的结电容。模块计算 *CJO*、*VJ* 和 *M* 如下：

  - CJ0=C1((VR2−VR1)/(VR2−VR1(C2/C1)−1/M))M
  - VJ=−(−VR2(C1/C2)−1/M+VR1)/(1−(C1/C2)−1/M)
  - M=log(C3/C2)/log(VR2/VR3)

  其中：

  - *VR1*、*VR2* 和 *VR3* 是 **Reverse bias voltages [VR1 VR2 VR3]** 向量中的值。
  - *C1*、*C2* 和 *C3* 是 **Corresponding capacitances [C1 C2 C3]** 向量中的值。

  无法从表格数据可靠地估算 *FC*，因此必须使用 **Capacitance coefficient FC** 参数指定其值。如果缺少此参数的合适数据，请使用典型值 0.5。

  反向偏置电压（定义为正值）应满足 *VR3* > *VR2* > *VR1*。这意味着电容应满足 *C1* > *C2* > *C3*，因为反向偏置会加宽耗尽区从而降低电容。违反这些不等式会导致错误。电压 *VR2* 和 *VR3* 应远离结电势 *VJ*。电压 *VR1* 应小于结电势 *VJ*，*VR1* 的典型值为 0.1 V。

电压相关结以结电容电荷 *Qj* 的形式定义为：

- 对于 *V* < *FC*·*VJ*：

  Qj=CJ0⋅(VJ/(M−1))⋅((1−V/VJ)1−M−1)
- 对于 *V* ≥ *FC*·*VJ*：

  Qj=CJ0⋅F1+(CJ0/F2)⋅(F3⋅(V−FC⋅VJ)+0.5(M/VJ)⋅(V2−(FC⋅VJ)2))

其中：

- F1=(VJ/(1−M))⋅(1−(1−FC)1−M))
- F2=(1−FC)1+M))
- F3=1−FC⋅(1+M)
- *V* 是结电容电压。

这些方程与 [2] 中使用的相同，但不建模 *VJ* 和 *FC* 的温度依赖性。此模型不包括影响高频开关应用性能的扩散电容项。

光电二极管模块包含若干选项，用于在仿真期间对二极管电流-电压关系对温度的依赖性进行建模。不建模结电容的温度依赖性，因为其影响要小得多。有关详细信息，请参阅 Diode 参考页。

### 热端口

您可以暴露热端口以对产生的热量和设备温度的影响进行建模。要暴露热端口，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 模块不包含热端口，也不模拟设备中的热量产生。
- `Show thermal port` — 模块包含一个热端口，允许您对传导损耗产生的热量进行建模。为了提高数值效率，热状态不影响模块的电气行为。

有关使用热端口以及 **Thermal Port** 参数的详细信息，请参阅 Simulating Thermal Effects in Semiconductors。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

**注意**

要满足所有初始目标，请勿将优先级设置为 `High` 的初始目标数量超过模块方程中微分变量的总数。

- 如果在 **Capacitance** 部分中，将 **Parameterization** 设置为 `Fixed or zero junction capacitance`，并将 **Junction capacitance** 设置为 `0`，则模块方程中微分变量的总数为零。请勿将 **Initial Targets** 部分中任何变量的优先级设置为 `High`。
- 如果在 **Capacitance** 部分中，将 **Parameterization** 设置为 `Fixed or zero junction capacitance`，并将 **Junction capacitance** 参数设置为非零值，则模块方程中微分变量的总数为 1。将 **Initial Targets** 部分中不超过一个变量的优先级设置为 `High`。
- 如果在 **Capacitance** 部分中，将 **Parameterization** 设置为 `Use C-V curve data points` 或 `Use parameters Cj0, VJ, M & FC`，则模块方程中微分变量的总数为 1。将 **Initial Targets** 部分中不超过一个变量的优先级设置为 `High`。

使用标称值来指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。

### 绘制基本 I-V 特性

您可以在不构建完整模型的情况下绘制光电二极管模块的基本 I-V 特性。使用这些图来探索参数选择对设备特性的影响。如果您从数据手册对模块进行参数化，可以将图与数据手册进行比较，以检查是否正确地对模块进行了参数化。如果您有一个完整的可用模型但不知道使用哪个制造部件，可以将图与数据手册进行比较以帮助您做出决定。

要启用此选项，请将光电二极管模块的 **Modeling option** 参数设置为 `No thermal port`。要绘制基本特性，请右键单击模块并从上下文菜单中选择 **Electrical** > **Basic characteristics**。有关 **Basic characteristics** 选项的详细信息，请参阅 Plot Basic I-V Characteristics of Semiconductor Blocks。
