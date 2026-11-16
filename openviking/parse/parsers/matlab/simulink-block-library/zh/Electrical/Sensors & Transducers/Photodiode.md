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

### **+** — 正极端子 electrical

与阳极关联的电气守恒端口。

### **-** — 负极端子 electrical

与阴极关联的电气守恒端口。

### **H** — 热端口 thermal

热守恒端口。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

## 参数

### **建模选项** — 是否启用热端口 `No thermal port` (默认) | `Show thermal port`

是否启用模块的热端口并对生成的热量和器件温度的影响进行建模。

### 主要

### **灵敏度参数化** — 灵敏度参数化 `Specify measured current for given flux density` (默认) | `Specify current per unit flux density`

选择以下灵敏度参数化方法之一：

- `Specify measured current for given flux density` —
  指定测得的电流及对应的通量密度。这是默认方法。
- `Specify current per unit flux density` — 直接指定器件灵敏度。

### **测量电流** — 测量电流 `25` `uA` (默认)

模块用于计算器件灵敏度的电流。

#### 依赖关系

仅当您为 **灵敏度参数化** 参数选择 `Specify measured current for given flux density` 时，此参数才可见。

### **通量密度** — 通量密度 `5` `W/m^2` (默认)

模块用于计算器件灵敏度的通量密度。

#### 依赖关系

仅当您为 **灵敏度参数化** 参数选择 `Specify measured current for given flux density` 时，此参数才可见。

### **器件灵敏度** — 器件灵敏度 `5e-06` `m^2*A/W` (默认)

单位通量密度对应的电流。

#### 依赖关系

仅当您为 **灵敏度参数化** 参数选择 `Specify current per unit flux density` 时，此参数才可见。

### **二极管参数化** — 二极管参数化 `Use dark current plus a forward bias I-V data point` (默认) | `Use dark current and N`

选择以下二极管模型参数化方法之一：

- `Use dark current plus a forward bias I-V data point`
  — 指定暗电流和二极管 I-V 曲线上的一个点。这是默认方法。
- `Use dark current and N` — 指定暗电流和发射系数。

### **电流 I1** — 正向偏置点处的电流 `0.1` `A` (默认)

二极管 I-V 曲线上正向偏置点处的电流，模块用它计算 *IS* 和 *N*。

#### 依赖关系

仅当您为 **二极管参数化** 参数选择 `Use dark current plus a forward bias I-V data point` 时，此参数才可见。

### **电压 V1** — 正向偏置点处的电压 `1.3` `V` (默认)

二极管 I-V 曲线上正向偏置点处对应的电压，模块用它计算 *IS* 和 *N*。

#### 依赖关系

仅当您为 **二极管参数化** 参数选择 `Use dark current plus a forward bias I-V data point` 时，此参数才可见。

### **暗电流** — 暗电流 `5e-9` `A` (默认)

二极管未暴露于光中时通过它的电流。

### **发射系数, N** — 发射系数 `3` (默认)

二极管发射系数或理想因子。

#### 依赖关系

仅当您为 **二极管参数化** 参数选择 `Use dark current and N` 时，此参数才可见。

### **欧姆电阻, RS** — 二极管串联连接电阻 `0.1` `Ohm` (默认)

二极管串联连接电阻。

### **测量温度** — 测量温度 `25` `degC` (默认)

测量 I-V 曲线或暗电流时的温度。

### 结电容

### **参数化** — 结电容参数化 `Fixed or zero junction capacitance` (默认) | `Use C-V curve data points` | `Use parameters CJ0, VJ, M & FC`

选择以下用于对结电容建模的选项之一：

- `Fixed or zero junction capacitance` — 将结电容建模为固定值。
- `Use C-V curve data points` — 指定二极管 C-V 曲线上三个点的测量数据。
- `Use parameters CJ0, VJ, M & FC` — 指定零偏结电容、结电势、梯度系数和正向偏置耗尽电容系数。

### **结电容** — 结电容 `60` `pF` (默认)

结电容的固定值。

#### 依赖关系

仅当您为 **参数化** 参数选择 `Fixed or zero junction capacitance` 时，此参数才可见。

### **零偏结电容, CJ0** — 零偏结电容 `60` `pF` (默认)

与指数二极管项并联放置的电容值。

#### 依赖关系

仅当您为 **参数化** 参数选择 `Use parameters CJ0, VJ, M & FC` 时，此参数才可见。

### **反向偏置电压 [VR1 VR2 VR3]** — 反向偏置电压 `[ 0.1 10 100 ]` `V` (默认)

二极管 C-V 曲线上三个点处的反向偏置电压值向量，模块用它计算 *CJ0*、*VJ* 和 *M*。

#### 依赖关系

仅当您为 **参数化** 参数选择 `Use C-V curve data points` 时，此参数才可见。

### **对应电容 [C1 C2 C3]** — 对应电容 `[ 45 3 6 ]` `pF` (默认)

二极管 C-V 曲线上三个点处的电容值向量，模块用它计算 *CJ0*、*VJ* 和 *M*。

#### 依赖关系

仅当您为 **参数化** 参数选择 `Use C-V curve data points` 时，此参数才可见。

### **结电势, VJ** — 结电势 `1` `V` (默认)

结电势。

#### 依赖关系

仅当您为 **参数化** 参数选择 `Use parameters CJ0, VJ, M & FC` 时，此参数才可见。

### **梯度系数, M** — 梯度系数 `0.5` (默认)

梯度系数。

#### 依赖关系

仅当您为 **参数化** 参数选择 `Use parameters CJ0, VJ, M & FC` 时，此参数才可见。

### **电容系数, FC** — 电容系数 `0.5` (默认)

用于量化耗尽电容随施加电压而减小的拟合系数。

#### 依赖关系

仅当您为 **参数化** 参数选择 `Use C-V curve data points` 或 `Use parameters CJ0, VJ, M & FC` 时，此参数才可见。

### 温度依赖性

### **参数化** — 温度依赖性参数化 `None — Simulate at parameter measurement temperature` (默认) | `Use an I-V data point at second measurement temperature T2` | `Specify saturation current at second measurement temperature T2` | `Specify the energy gap EG`

选择以下温度依赖性参数化方法之一：

- `None — Simulate at parameter measurement temperature`
  — 不建模温度依赖性，或者在测量温度 *T*m1 下仿真模型（由 **主要** 选项卡上的 **测量温度** 参数指定）。这是默认方法。
- `Use an I-V data point at second measurement temperature T2`
  — 如果选择此选项，则指定第二个测量温度 *T*m2，以及此温度下的电流和电压值。模型使用这些值以及第一个测量温度 *T*m1 下的参数值来计算能隙值。
- `Specify saturation current at second measurement temperature
  T2` — 如果选择此选项，则指定第二个测量温度 *T*m2，以及此温度下的饱和电流值。模型使用这些值以及第一个测量温度 *T*m1 下的参数值来计算能隙值。
- `Specify the energy gap EG` — 直接指定能隙值。

### **第二个测量温度下的电流 I1** — 第二个测量温度下的电流 I1 `0.07` `A` (默认)

指定第二个测量温度下电压为 *V1* 时的二极管电流 *I1* 值。

#### 依赖关系

仅当您为 **参数化** 参数选择 `Use an I-V data point at second measurement temperature T2` 时，此参数才可见。

### **第二个测量温度下的电压 V1** — 第二个测量温度下的电压 V1 `1.3` `V` (默认)

指定第二个测量温度下电流为 *I1* 时的二极管电压 *V1* 值。

#### 依赖关系

仅当您为 **参数化** 参数选择 `Use an I-V data point at second measurement temperature T2` 时，此参数才可见。

### **第二个测量温度下的饱和电流, IS** — 第二个测量温度下的饱和电流, IS `2.5e-7` `A` (默认)

指定第二个测量温度下的饱和电流 *IS* 值。

#### 依赖关系

仅当您为 **参数化** 参数选择 `Specify saturation current at second measurement temperature T2` 时，此参数才可见。

### **第二个测量温度** — 第二个测量温度 `125` `degC` (默认)

指定第二个测量温度的值。

#### 依赖关系

仅当您为 **参数化** 参数选择 `Use an I-V data point at second measurement temperature T2` 或 `Specify saturation current at second measurement temperature T2` 时，此参数才可见。

### **能隙参数化** — 能隙参数化 `Use nominal value for silicon (EG=1.11eV)` (默认) | `Use nominal value for 4H-SiC silicon carbide (EG=3.23eV)` | `Use nominal value for 6H-SiC silicon carbide (EG=3.00eV)` | `Use nominal value for germanium (EG=0.67eV)` | `Use nominal value for gallium arsenide (EG=1.43eV)` | `Use nominal value for selenium (EG=1.74eV)` | `Use nominal value for Schottky barrier diodes (EG=0.69eV)` | `Specify a custom value`

从预定义选项列表中选择能隙值，或指定自定义值：

- `Use nominal value for silicon (EG=1.11eV)` — 这是默认值。
- `Use nominal value for 4H-SiC silicon carbide (EG=3.23eV)`
- `Use nominal value for 6H-SiC silicon carbide (EG=3.00eV)`
- `Use nominal value for germanium (EG=0.67eV)`
- `Use nominal value for gallium arsenide (EG=1.43eV)`
- `Use nominal value for selenium (EG=1.74eV)`
- `Use nominal value for Schottky barrier diodes (EG=0.69eV)`
- `Specify a custom value` — 如果选择此选项，则对话框中将显示 **能隙, EG** 参数，以便为 *EG* 指定自定义值。

#### 依赖关系

仅当您为 **参数化** 参数选择 `Specify the energy gap EG` 时，此参数才可见。

### **能隙, EG** — 能隙 `1.11` `eV` (默认)

为能隙 *EG* 指定自定义值。

#### 依赖关系

仅当您为 **能隙参数化** 参数选择 `Specify a custom value` 时，此参数才可见。

### **饱和电流温度指数参数化** — 饱和电流温度指数参数化 `Use nominal value for pn-junction diode (XTI=3)` (默认) | `Use nominal value for Schottky barrier diode (XTI=2)` | `Specify a custom value`

选择以下选项之一来指定饱和电流温度指数值：

- `Use nominal value for pn-junction diode (XTI=3)` —
  这是默认值。
- `Use nominal value for Schottky barrier diode (XTI=2)`
- `Specify a custom value` — 如果选择此选项，则对话框中将显示 **饱和电流温度指数, XTI** 参数，以便为 *XTI* 指定自定义值。

### **饱和电流温度指数, XTI** — 饱和电流温度指数 `3` (默认)

为饱和电流温度指数 *XTI* 指定自定义值。

#### 依赖关系

仅当您为 **饱和电流温度指数参数化** 参数选择 `Specify a custom value` 时，此参数才可见。

### **器件仿真温度** — 器件仿真温度 `25` `degC` (默认)

指定器件要仿真时的温度 *T*s 值。

## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

### R2024a: **Junction capacitance voltage** 变量已替换为 **Charge of junction capacitance** 变量

如果，在 **电容** 部分中，您将 **参数化** 设置为 `Use C-V curve data points` 或 `Use parameters Cj0, VJ, M & FC`，那么现在您使用 **Charge of junction capacitance** 变量为电容和电荷建模指定 **初始目标** 和 **标称值**。**Junction capacitance voltage** 变量不再启用。

如果您在较早版本中创建的模型将这些值用于 **参数化**，并为 **Junction capacitance voltage** 变量指定了 **初始目标** 或 **标称值**，则必须更新该模型。有关如何计算结电容电荷的详细信息，请参阅描述。

## 描述

带入射通量输入端口的 Photodiode

Photodiode 模块将光电二极管表示为并联的受控电流源和指数二极管。受控电流源产生与辐射通量密度成正比的电流 *Ip*：

|  |  |
| --- | --- |
| *Ip* = *DeviceSensitivity* · *RadiantFluxDensity* | **(1)** |

其中：

- *DeviceSensitivity* 是产生的电流与入射辐射通量密度之比。

  - 如果为 **Sensitivity parameterization** 参数选择 `Specify measured current for given flux density`，则模块通过将 **Measured current** 参数值转换为 amps 单位并除以 **Flux density** 参数值来计算此变量。
  - 如果为 **Sensitivity parameterization** 参数选择 `Specify current per unit flux density`，则此变量由 **Device sensitivity** 参数值定义。
- *RadiantFluxDensity* 是入射辐射通量密度。

要建模动态响应时间，请使用 **Junction capacitance** 选项卡中的 **Parameterization** 参数，以在模型中包含二极管结电容。

指数二极管模型提供二极管电流 *I* 与二极管电压 *V* 之间的以下关系：

I=IS⋅(eqVNkTm1−1)

其中：

- *q* 是电子上的基本电荷（1.602176e–19 Coulombs）。
- *k* 是玻尔兹曼常数（1.3806503e–23 J/K）。
- *N* 是发射系数。
- *IS* 是饱和电流，等于 **Dark current** 参数值。
- *Tm1* 是指定二极管参数时的温度，由 **Measurement temperature** 参数值定义。

当 (*q**V* / *N**k**Tm1*) > 80 时，模块将 eqVNkTm1 替换为 (*q**V* / *N**k**Tm1* – 79)e80，这与 (*q**V* / *N**k**Tm1*) = 80 处二极管电流的梯度匹配，并进行线性外推。当 (*q**V* / *N**k**Tm1*) < –79 时，模块将 eqVNkTm1 替换为 (*q**V* / *N**k**Tm1* + 80)e–79，这同样匹配该梯度并进行线性外推。典型电路不会达到这些极端值。模块提供此线性外推，以在仿真期间求解约束时帮助收敛。

当为 **Diode parameterization** 参数选择 `Use dark current and N` 时，您用 **Dark current** 和 **Emission coefficient N** 参数指定二极管。当为 **Diode parameterization** 参数选择 `Use dark current plus a forward bias I-V data point` 时，您指定 **Dark current** 参数以及二极管 I-V 曲线上的一个电压和电流测量点。模块根据这些值按如下方式计算 *N*：

N=VF/(Vtlog(IF/IS+1))

其中：

- *VF* 是 **Forward voltage VF** 参数值。
- *Vt* = *k**Tm1* / *q*.
- *IF* 是 **Current IF at forward voltage VF** 参数值。

指数二极管模型提供包含结电容的选项：

- 当为 **Parameterization** 参数选择 `Fixed or zero junction capacitance` 时，电容是固定的。
- 当为 **Parameterization** 参数选择 `Use parameters CJO, VJ, M & FC` 时，模块使用系数 *CJO*、*VJ*、*M* 和 *FC* 来计算取决于结电压的结电容。
- 当为 **Parameterization** 参数选择 `Use C-V curve data points` 时，模块使用 C-V 电容曲线上的三个电容值来估计 *CJO*、*VJ* 和 *M*，并将这些值与指定的 *FC* 值一起使用来计算取决于结电压的结电容。模块按如下方式计算 *CJO*、*VJ* 和 *M*：

  - CJ0=C1((VR2−VR1)/(VR2−VR1(C2/C1)−1/M))M
  - VJ=−(−VR2(C1/C2)−1/M+VR1)/(1−(C1/C2)−1/M)
  - M=log(C3/C2)/log(VR2/VR3)

  其中：

  - *VR1*、*VR2* 和 *VR3* 是 **Reverse bias voltages [VR1 VR2 VR3]** 向量中的值。
  - *C1*、*C2* 和 *C3* 是 **Corresponding capacitances [C1 C2 C3]** 向量中的值。

  无法从表格数据可靠地估计 *FC*，因此必须使用 **Capacitance coefficient FC** 参数指定其值。如果没有适合此参数的数据，请使用典型值 0.5。

  反向偏置电压（定义为正值）应满足 *VR3* > *VR2* > *VR1*。这意味着电容应满足 *C1* > *C2* > *C3*，因为反向偏置会加宽耗尽区，从而降低电容。违反这些不等式会导致错误。电压 *VR2* 和 *VR3* 应远离结电势 *VJ*。电压 *VR1* 应小于结电势 *VJ*，*VR1* 的典型值为 0.1 V。

电压相关结以结电容电荷 *Qj* 的形式定义如下：

- 对于 *V* < *FC*·*VJ*：

  Qj=CJ0⋅(VJ/(M−1))⋅((1−V/VJ)1−M−1)
- 对于 *V* ≥ *FC*·*VJ*：

  Qj=CJ0⋅F1+(CJ0/F2)⋅(F3⋅(V−FC⋅VJ)+0.5(M/VJ)⋅(V2−(FC⋅VJ)2))

其中：

- F1=(VJ/(1−M))⋅(1−(1−FC)1−M))
- F2=(1−FC)1+M))
- F3=1−FC⋅(1+M)
- *V* 是结电容电压。

这些方程与 [2] 中使用的相同，不同之处在于未对 *VJ* 和 *FC* 的温度依赖性建模。此模型不包含扩散电容项，该项会影响高频开关应用的性能。

Photodiode 模块包含若干选项，用于在仿真期间对二极管电流-电压关系对温度的依赖性进行建模。未对结电容的温度依赖性建模，因为这一影响小得多。有关详细信息，请参阅 Diode 参考页。

### 热端口

您可以显示热端口，以对生成的热和器件温度的影响进行建模。要显示热端口，请将 **Modeling option** 参数设置为以下任一项：

- `No thermal port` — 模块不包含热端口，也不仿真器件中的热生成。
- `Show thermal port` — 模块包含热端口，允许您对传导损耗生成的热进行建模。出于数值效率考虑，热状态不影响模块的电气行为。

有关使用热端口以及 **Thermal Port** 参数的详细信息，请参阅模拟半导体中的热效应。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

**注意**

要满足所有初始目标，请不要为超过模块方程中微分变量总数的初始目标将优先级设置为 `High`。

- 如果在 **Capacitance** 部分，将 **Parameterization** 设置为 `Fixed or zero junction capacitance`，并将 **Junction capacitance** 设置为 `0`，则模块方程中微分变量的总数为零。请不要将 **Initial Targets** 部分中任何变量的优先级设置为 `High`。
- 如果在 **Capacitance** 部分，将 **Parameterization** 设置为 `Fixed or zero junction capacitance`，并将 **Junction capacitance** 参数设置为非零值，则模块方程中微分变量的总数为 1。请将 **Initial Targets** 部分中不超过一个变量的优先级设置为 `High`。
- 如果在 **Capacitance** 部分，将 **Parameterization** 设置为 `Use C-V curve data points` 或 `Use parameters Cj0, VJ, M & FC`，则模块方程中微分变量的总数为 1。请将 **Initial Targets** 部分中不超过一个变量的优先级设置为 `High`。

使用标称值来指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源。其中一个来源是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅按标称值进行系统缩放。

### 绘制基本 I-V 特性

无需构建完整模型，即可绘制 Photodiode 模块的基本 I-V 特性。使用绘图来探究参数选择对器件特性的影响。如果根据数据表参数化模块，则可以将绘图与数据表进行比较，以检查是否正确参数化了模块。如果您有一个完整可用的模型，但不知道要使用哪个制造部件，则可以将绘图与数据表进行比较以帮助决定。

要启用此选项，请将 Photodiode 模块的 **Modeling option** 参数设置为 `No thermal port`。要绘制基本特性，请右键单击模块，然后从上下文菜单中选择 **Electrical** > **Basic characteristics**。有关 **Basic characteristics** 选项的详细信息，请参阅绘制半导体模块的基本 I-V 特性。
