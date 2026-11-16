---
type: simulink-block
title: 'PNP Bipolar Transistor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'pnpbipolartransistor'
documentation_source_path: 'ref/pnpbipolartransistor.html'
language: zh-CN
chinese_source: worker-translation
---

# PNP Bipolar Transistor

## 端口

### 守恒

### **B** — 基极端子 电气

与晶体管基极端子关联的电气守恒端口。

基极端子是控制端子，用于调制发射极和集电极之间的电流。

### **C** — 集电极端子 电气

与晶体管集电极端子关联的电气守恒端口。

集电极端子是晶体管导通时主电流从发射极流向集电极所经过的端子。相对于发射极，集电极端子通常连接到较低的电压。

### **E** — 发射极端子 电气

与晶体管发射极端子关联的电气守恒端口。

发射极端子是电流进入晶体管的端子。发射极通常连接到正电压。

### **H** — 热端口 热

热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口，并对生成的热量和器件温度效应进行建模。

### 主要

### **Parameterization** — 模块参数化 `Specify from a datasheet`（默认）| `Specify using equation parameters directly`

选择以下模块参数化方法之一：

- `Specify from a datasheet` — 提供模块会转换为描述晶体管方程的参数。模块按下式计算正向 Early 电压 *VAF*：*Ic/h\_oe*，其中 *Ic* 是 **Collector current at which h-parameters are defined** 参数值，*h\_oe* 是 **Output admittance h\_oe** 参数值 [2]。模块将 *BF* 设置为小信号 **Forward current transfer ratio h\_fe** 值。当 *Ic* 为零时，模块根据指定的 **Voltage Vbe** 值和对应的 **Current Ib for voltage Vbe** 值计算饱和电流 *IS*。这是默认方法。
- `Specify using equation parameters directly` — 直接提供方程参数 *IS*、*BF* 和 *VAF*。

### **Forward current transfer ratio h\_fe** — 正向电流传输比 `100`（默认）

小信号电流增益。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Specify from a datasheet` 时，此参数才可见。

### **Output admittance h\_oe** — 输出导纳 `50e-6` `1/Ohm`（默认）

在固定基极电流下，集电极电流对集电极-发射极电压的导数。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Specify from a datasheet` 时，此参数才可见。

### **Collector current at which h-parameters are defined** — 定义 h 参数时的集电极电流 `-1` `mA`（默认）

h 参数随工作点变化，并针对此集电极电流值定义。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Specify from a datasheet` 时，此参数才可见。

### **Collector-emitter voltage at which h-parameters are defined** — 定义 h 参数时的集电极-发射极电压 `-5` `V`（默认）

h 参数随工作点变化，并针对此集电极-发射极电压值定义。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Specify from a datasheet` 时，此参数才可见。

### **Voltage Vbe** — 电压 Vbe `-0.55` `V`（默认）

基极电流为 *Ib* 时的基极-发射极电压。[ *Vbe* *Ib* ] 数据对应在晶体管处于正常有源区（即未处于饱和区）时给出。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Specify from a datasheet` 时，此参数才可见。

### **Current Ib for voltage Vbe** — 电压 Vbe 对应的电流 Ib `-0.5` `mA`（默认）

基极-发射极电压为 *Vbe* 时的基极电流。[ *Vbe* *Ib* ] 数据对应在晶体管处于正常有源区（即未处于饱和区）时给出。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Specify from a datasheet` 时，此参数才可见。

### **Forward current transfer ratio BF** — 正向电流传输比 `100`（默认）

理想最大正向电流增益。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Specify using equation parameters directly` 时，此参数才可见。

### **Saturation current IS** — 饱和电流 `1e-14` `A`（默认）

在非常大的反向偏置水平下，p-n 结渐近趋近的电流大小。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Specify using equation parameters directly` 时，此参数才可见。

### **Forward Early voltage VAF** — 正向 Early 电压 `200` `V`（默认）

在标准 Ebers-Moll 方程中，*Ic* 对 *Vce* 曲线的梯度在正常有源区为零。附加的正向 Early 电压项会增大该梯度。当线性区域外推时，*Vce* 轴上的截距等于 –*VAF*。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Specify using equation parameters directly` 时，此参数才可见。

### **Reverse current transfer ratio BR** — 反向电流传输比 `1`（默认）

理想最大反向电流增益。该值通常未在制造商数据表中给出，因为当晶体管偏置在正常有源区工作时该值不重要。当该值未知且晶体管不会在反向区工作时，请使用默认值 `1`。

### **Measurement temperature** — 测量温度 `25` `degC`（默认）

测量 *Vbe* 和 *Ib*，或 *IS* 时的温度 *T*m1。

### 欧姆电阻

### **Collector resistance RC** — 集电极电阻 `0.01` `ohm`（默认）

集电极处的电阻。

### **Emitter resistance RE** — 发射极电阻 `1e-4` `Ohm`（默认）

发射极处的电阻。

### **Zero bias base resistance RB** — 零偏置基极电阻 `1` `Ohm`（默认）

零偏置时基极处的电阻。

### 电容

### **Base-collector junction capacitance** — 基极-集电极结电容 `5` `pF`（默认）

基极-集电极结两端的寄生电容。

### **Base-emitter junction capacitance** — 基极-发射极结电容 `5` `pF`（默认）

基极-发射极结两端的寄生电容。

### **Total forward transit time** — 总正向渡越时间 `0` `us`（默认）

表示少数载流子从发射极穿过基区到达集电极的平均时间，通常由参数 TF 表示 [1]。

### **Total reverse transit time** — 总反向渡越时间 `0` `us`（默认）

表示少数载流子从集电极穿过基区到达发射极的平均时间，通常由参数 TR 表示 [1]。

### 温度依赖性

### **Parameterization** — 温度依赖性参数化 `None — Simulate at parameter measurement temperature`（默认）| `Model temperature dependence`

选择以下温度依赖性参数化方法之一：

- `None — Simulate at parameter measurement temperature` — 不对温度依赖性建模，或者在测量温度 *T*m1（由 **主要** 选项卡上的 **Measurement temperature** 参数指定）下仿真模型。这是默认方法。
- `Model temperature dependence` — 提供仿真温度值，以对温度相关效应建模。还必须根据模块参数化方法提供一组附加参数。如果从数据表参数化模块，则必须提供第二个 [ *Vbe* *Ib* ] 数据对以及在第二测量温度下的 *h\_fe* 值。如果通过直接指定方程参数进行参数化，则必须提供 *XTI*、*EG* 和 *XTB* 的值。

### **Forward current transfer ratio, h\_fe, at second measurement temperature** — 第二测量温度下的正向电流传输比 h\_fe `125`（默认）

第二测量温度下的小信号电流增益。它必须在与 **主要** 选项卡上的 **Forward current transfer ratio h\_fe** 参数相同的集电极-发射极电压和集电极电流下给出。

#### 依赖关系

仅当在 **主要** 选项卡上为 **Parameterization** 参数选择 `Specify from a datasheet` 时，此参数才可见。

### **Voltage Vbe at second measurement temperature** — 第二测量温度下的电压 Vbe `-0.45` `V`（默认）

基极电流为 *Ib* 且温度设置为第二测量温度时的基极-发射极电压。[*Vbe* *Ib*] 数据对应在晶体管处于正常有源区（即未处于饱和区）时给出。

#### 依赖关系

仅当在 **主要** 选项卡上为 **Parameterization** 参数选择 `Specify from a datasheet` 时，此参数才可见。

### **Current Ib for voltage Vbe at second measurement temperature** — 第二测量温度下电压 Vbe 对应的电流 Ib `-0.5` `mA`（默认）

基极-发射极电压为 *Vbe* 且温度设置为第二测量温度时的基极电流。[ *Vbe* *Ib* ] 数据对应在晶体管处于正常有源区（即未处于饱和区）时给出。

#### 依赖关系

仅当在 **主要** 选项卡上为 **Parameterization** 参数选择 `Specify from a datasheet` 时，此参数才可见。

### **Second measurement temperature** — 第二测量温度 `125` `degC`（默认）

测量 *h\_fe*、*Vbe* 和 *Ib* 时的第二温度 *T*m2。

#### 依赖关系

仅当在 **主要** 选项卡上为 **Parameterization** 参数选择 `Specify from a datasheet` 时，此参数才可见。

### **Current gain temperature coefficient, XTB** — 电流增益温度系数 `0`（默认）

电流增益温度系数值。

#### 依赖关系

仅当在 **主要** 选项卡上为 **Parameterization** 参数选择 `Specify using equation parameters directly` 时，此参数才可见。

### **Energy gap, EG** — 能隙 `1.11` `eV`（默认）

能隙值。

#### 依赖关系

仅当在 **主要** 选项卡上为 **Parameterization** 参数选择 `Specify using equation parameters directly` 时，此参数才可见。

### **Saturation current temperature exponent, XTI** — 饱和电流温度指数 `3`（默认）

饱和电流温度系数值。

#### 依赖关系

仅当在 **主要** 选项卡上为 **Parameterization** 参数选择 `Specify using equation parameters directly` 时，此参数才可见。

### **Device simulation temperature** — 器件仿真温度 `25` `degC`（默认）

对器件进行仿真时的温度 *T*s。

## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

### R2024a: **Base-collector capacitance voltage** 和 **Base-emitter capacitance voltage** 变量已替换为 **Base-collector charge** 和 **Base-emitter charge** 变量

现在，您可以使用 **Base-collector charge** 和 **Base-emitter charge** 变量来指定用于电容和电荷建模的 **Initial Targets** 和 **Nominal Values**。**Base-collector capacitance voltage** 和 **Base-emitter capacitance voltage** 变量已被移除。

如果您在较早版本中创建的模型为 **Base-collector capacitance voltage** 或 **Base-emitter capacitance voltage** 变量指定了 **Initial Targets** 或 **Nominal Values**，则必须更新该模型。有关如何计算 base-collector charge 和 base-emitter charge 的详细信息，请参阅 Modeling Capacitance and Charge。

### R2019b: 热网络 simlog 路径

从 R2019b 开始，可以在内部或外部对该模块的热网络进行建模。

因此，与热网络对应的 simlog 路径已更改。如果您有以编程方式访问 simlog 的脚本，则必须手动更新它以反映这些更改。

## 描述

使用增强 Ebers-Moll 方程的 PNP 双极晶体管

PNP Bipolar Transistor 模块使用 Ebers-Moll 方程的一个变体来表示 PNP 双极晶体管。Ebers-Moll 方程基于两个指数二极管和两个电流控制电流源。PNP Bipolar Transistor 模块对模型提供以下增强：

- Early 电压效应
- 可选基极、集电极和发射极电阻
- 可选固定基极-发射极和基极-集电极电容

集电极和基极电流为 [1]：

IC=−IS[(e−qVBE/(kTm1)−e−qVBC/(kTm1))(1+VBCVA)−1βR(e−qVBC/(kTm1)−1)]IB=−IS[1βF(e−qVBE/(kTm1)−1)+1βR(e−qVBC/(kTm1)−1)]

在这些方程中：

- *IB* 和 *IC* 是基极和集电极电流，定义为流入器件为正。
- *IS* 是 **Saturation current IS** 参数的值。
- *VBE* 是基极-发射极电压，*VBC* 是基极-集电极电压。
- *βF* 是 **Forward current transfer ratio BF parameter** 参数的值。该项表示理想最大正向电流增益。
- *βR* 是 **Reverse current transfer ratio BR parameter** 参数的值。该项表示理想最大反向电流增益。
- *VA* 是 **Forward Early voltage VAF** 参数的值。
- *q* 是电子的基本电荷（1.602176e-19 Coulombs）。
- *k* 是玻尔兹曼常数（1.3806503e-23 J/K）。
- *T*m1 是晶体管温度，由 **Measurement temperature** 参数值定义。

您可以使用数据表参数指定晶体管行为，模块会使用这些参数计算这些方程的方程参数；也可以直接指定方程参数。

如果 –*q**V*BC / (*k**T*m1) > 40 或 –*q**V*BE / (*k**T*m1) > 40，则方程中相应的指数项分别替换为 (–*q**V*BC / (*k**T*m1) – 39)*e*40 和 (–*q**V*BE / (*k**T*m1) – 39)*e*40。这有助于防止与指数函数 *e*x 在大 *x* 值处陡峭梯度相关的数值问题。类似地，如果 –*q**V*BC / (*k**T*m1) < –39 或 –*q**V*BE / (*k**T*m1) < –39，则方程中相应的指数项分别替换为 (–*q**V*BC / (*k**T*m1) + 40)*e*–39 和 (–*q**V*BE / (*k**T*m1) + 40)*e*–39。

可选地，您可以指定基极-发射极和基极-集电极结两端的固定电容。您还可以选择指定基极、集电极和发射极连接电阻。

### 建模电容和电荷

您使用 **Base-collector junction capacitance** 和 **Base-emitter junction capacitance** 参数来建模电容和电荷。您还可以使用 **Total forward transit time** 和 **Total reverse transit time** 参数来表示反向恢复电荷和动态特性。此方程定义 base-collector 电荷，

QBC=tRICE+CBCVBC,

其中：

- *t*R 是 **Total reverse transit time** 参数值。
- *I*CE 是集电极-发射极电流。
- *C*BC 是 **Base-collector junction capacitance** 参数值。
- *V*BC 是基极-集电极电压。

此方程定义 base-collector 电荷和电容器电流，

IQBC=dQBCdt.

此方程定义 base-emitter 电荷，

QBE=tFIC+CBEVBE,

其中：

- *t*F 是 **Total forward transit time** 参数值。
- *I*C 是集电极电流。
- *C*BE 是 **Base-emitter junction capacitance** 参数值。
- *V*BE 是基极-发射极电压。

此方程定义 base-emitter 电荷和电容器电流，

IQBE=dQBEdt.

### 建模温度依赖性

默认行为是不建模对温度的依赖性，器件在您提供模块参数的温度下进行仿真。您可以选择在仿真期间对晶体管静态行为的温度依赖性进行建模。结点电容的温度依赖性不建模，因为其影响小得多。

当包括温度依赖性时，晶体管定义方程保持不变。测量温度值 *T*m1 替换为仿真温度 *T*s。饱和电流 *IS* 以及正向和反向增益（*βF* 和 *βR*）根据以下方程成为温度的函数：

ISTs=ISTm1⋅(Ts/Tm1)XTI⋅exp(−EGkTs(1−Ts/Tm1))

βFs=βFm1(TsTm1)XTB

βRs=βRm1(TsTm1)XTB

其中：

- *T*m1 是指定晶体管参数时的温度，由 **Measurement temperature** 参数值定义。
- *T*s 是仿真温度。
- *IS*Tm1 是测量温度下的饱和电流。
- *IS*Ts 是仿真温度下的饱和电流。当建模温度依赖性时，这是双极晶体管方程中使用的饱和电流值。
- *β*Fm1 和 *β*Rm1 是测量温度下的正向和反向增益。
- *β*Fs 和 *β*Rs 是仿真温度下的正向和反向增益。当建模温度依赖性时，这些是双极晶体管方程中使用的值。
- *EG* 是半导体类型的能隙，以 Joules 为单位。硅的值通常取为 1.11 eV，其中 1 eV 为 1.602e-19 Joules。
- *XTI* 是饱和电流温度指数。
- *XTB* 是正向和反向增益温度系数。
- *k* 是 Boltzmann 常数 (1.3806503e–23 J/K)。

*XTI* 和 *EG* 的合适值取决于晶体管类型和所用半导体材料。在实践中，需要调整 *XTI*、*EG* 和 *XTB* 的值，以建模特定晶体管的精确行为。一些制造商会在 SPICE Netlist 中给出这些经调整的值，您可以读取适当的值。否则，您可以使用较高温度 *T*m2 下的数据手册定义数据来确定 *XTI*、*EG* 和 *XTB* 的值。该模块为此提供了数据手册参数化选项。

您也可以自行调整 *XTI*、*EG* 和 *XTB* 的值，以匹配特定器件的实验室数据。您可以使用 Simulink® Design Optimization™ 软件来帮助调整这些值。

### 热端口

您可以公开热端口，以建模生成的热量和器件温度的影响。要公开热端口，将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 该模块不包含热端口，也不仿真器件中的热量生成。
- `Show thermal port` — 该模块包含一个热端口，允许您建模传导损耗生成的热量。为提高数值效率，热状态不影响模块的电气行为。

有关使用热端口和 **Thermal Port** 参数的详细信息，请参阅在半导体中仿真热效应。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

**注意**

为满足所有初始目标，不要将多于模块方程中微分变量总数的初始目标的优先级设置为 `High`。如果将 **Base-collector junction capacitance** 或 **Total reverse transit time** 参数设置为非零值，并将 **Base-emitter junction capacitance** 或 **Total forward transit time** 参数设置为非零值，则模块方程中的微分变量数为二。请选择以下选项之一：

- 要设置端子电流初始条件，请在 **Initial Targets** 部分中仅将 **Base current** 和 **Collector current** 变量的优先级设置为 `High`。
- 要设置端子电压初始条件，请在 **Initial Targets** 部分中仅将 **Collector-emitter voltage** 和 **Base-emitter voltage** 变量的优先级设置为 `High`。
- 要设置总电荷初始条件，请在 **Initial Targets** 部分中仅将 **Base-collector charge** 和 **Base-emitter charge** 变量的优先级设置为 `High`。*(since R2024a)*

使用标称值指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅通过标称值进行系统缩放。

### 绘制基本 I-V 特性

您可以在不构建完整模型的情况下绘制 PNP Bipolar Transistor 模块的基本 I-V 特性。使用这些图来探索参数选择对器件特性的影响。如果从数据手册参数化模块，可以将图与数据手册进行比较，以检查模块参数化是否正确。如果您有完整的工作模型，但不知道使用哪个制造器件，可以将图与数据手册进行比较，以帮助做出决定。

要启用此选项，请将 PNP Bipolar Transistor 模块的 **Modeling option** 参数设置为 `No thermal port`。要绘制基本特性，请右键单击模块，然后从上下文菜单中选择 **Electrical** > **Basic characteristics**。有关 **Basic characteristics** 选项的详细信息，请参阅绘制半导体模块的基本 I-V 特性。
