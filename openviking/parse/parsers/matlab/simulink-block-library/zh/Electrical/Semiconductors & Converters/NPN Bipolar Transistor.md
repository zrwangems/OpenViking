---
type: simulink-block
title: 'NPN Bipolar Transistor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'npnbipolartransistor'
documentation_source_path: 'ref/npnbipolartransistor.html'
language: zh-CN
chinese_source: worker-translation
---

# NPN Bipolar Transistor

## 端口

### 守恒

### **B** — 基极端子电气

与晶体管基极端子关联的电气守恒端口。

基极端子是控制端子，用于调制集电极与发射极之间的电流。

### **C** — 集电极端子电气

与晶体管集电极端子关联的电气守恒端口。

集电极端子是当晶体管导通时主电流从集电极流向发射极所经过的端子。集电极端子通常连接到相对于发射极为正的电压。

### **E** — 发射极端子电气

与晶体管发射极端子关联的电气守恒端口。

发射极端子是电流流出晶体管的端子。发射极通常连接到地或较低电压。

### **H** — 热端口热

热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口并对生成的热量和器件温度的影响进行建模。

### 主

### **Parameterization** — 模块参数化 `Specify from a datasheet`（默认）| `Specify using equation parameters directly`

选择以下方法之一进行模块参数化：

- `Specify from a datasheet`
  — 提供模块将其转换为描述晶体管的方程的参数。模块将正向厄利电压 *VAF* 计算为
  *Ic/h\_oe*，其中 *Ic*
  是 **Collector current at which h-parameters are
  defined** 参数值，
  *h\_oe* 是 **Output
  admittance h\_oe** 参数值 [1]。模块将 *BF* 设置为小信号
  **Forward current transfer ratio h\_fe**
  值。当 *Ic* 为零时，模块根据指定的
  **Voltage Vbe** 值和对应的 **Current Ib for voltage
  Vbe** 值计算饱和电流
  *IS*。
  这是默认方法。
- `Specify using equation parameters
  directly` — 提供方程
  参数 *IS*、*BF*
  和 *VAF*。

### **Forward current transfer ratio h\_fe** — 正向电流传输比 `100`（默认）

小信号电流增益。

#### 依赖关系

仅当为 **Parameterization** 参数选择
`Specify from a datasheet` 时，此参数才可见。

### **Output admittance h\_oe** — 输出导纳 `50e-6` `1/Ohm`（默认）

在固定基极电流下，集电极电流对集电极-发射极电压的导数。

#### 依赖关系

仅当为 **Parameterization** 参数选择
`Specify from a datasheet` 时，此参数才可见。

### **Collector current at which h-parameters are defined** — 定义 h 参数时的集电极电流 `1` `mA`（默认）

h 参数随工作点变化，并针对此集电极电流值进行定义。

#### 依赖关系

仅当为 **Parameterization** 参数选择
`Specify from a datasheet` 时，此参数才可见。

### **Collector-emitter voltage at which h-parameters are defined** — 定义 h 参数时的集电极-发射极电压 `5` `V`（默认）

h 参数随工作点变化，并针对此集电极-发射极电压值进行定义。

#### 依赖关系

仅当为 **Parameterization** 参数选择
`Specify from a datasheet` 时，此参数才可见。

### **Voltage Vbe** — 基极-发射极电压 `0.55` `V`（默认）

基极电流为 *Ib* 时的基极-发射极电压。
[ *Vbe*
*Ib* ] 数据对必须在晶体管处于正常有源区（即非饱和区）时引用。

#### 依赖关系

仅当为 **Parameterization** 参数选择
`Specify from a datasheet` 时，此参数才可见。

### **Current Ib for voltage Vbe** — 电压 Vbe 对应的电流 Ib `0.5` `mA`（默认）

基极-发射极电压为 *Vbe* 时的基极电流。
[ *Vbe*
*Ib* ] 数据对必须在晶体管处于正常有源区（即非饱和区）时引用。

#### 依赖关系

仅当为 **Parameterization** 参数选择
`Specify from a datasheet` 时，此参数才可见。

### **Forward current transfer ratio BF** — 正向电流传输比 `100`（默认）

理想最大正向电流增益。

#### 依赖关系

仅当为 **Parameterization** 参数选择
`Specify using equation parameters
directly` 时，此参数才可见。

### **Saturation current IS** — 饱和电流 `1e-14` `A`（默认）

p-n 结在非常大的反向偏置水平下渐近趋近的电流大小。

#### 依赖关系

仅当为 **Parameterization** 参数选择
`Specify using equation parameters
directly` 时，此参数才可见。

### **Forward Early voltage VAF** — 正向厄利电压 `200` `V`（默认）

在标准 Ebers-Moll 方程中，*Ic* 对 *Vce* 曲线的梯度在正常有源区为零。附加的正向厄利电压项增加了该梯度。当线性区域外推时，*Vce* 轴上的截距等于 –*VAF*。

#### 依赖关系

仅当为 **Parameterization** 参数选择
`Specify using equation parameters
directly` 时，此参数才可见。

### **Reverse current transfer ratio BR** — 反向电流传输比 `1`（默认）

理想最大反向电流增益。制造商数据表中通常不引用此值，因为当晶体管偏置在正常有源区工作时该值不显著。当该值未知且晶体管不在反向区工作时，使用默认值 `1`。

### **Measurement temperature** — 测量温度 `25` `degC`（默认）

测量 *Vbe* 和 *Ib*，或 *IS* 时的温度 *Tm1*。默认值为 `25` °C。

### 欧姆电阻

### **Collector resistance RC** — 集电极电阻 `0.01` `Ohm`（默认）

集电极处的电阻。

### **Emitter resistance RE** — 发射极电阻 `1e-4` `Ohm`（默认）

发射极处的电阻。

### **Zero bias base resistance RB** — 零偏置基极电阻 RB `1` `Ohm`（默认）

零偏置时基极处的电阻。

### 电容

### **Base-collector junction capacitance** — 基极-集电极结电容 `5` `pF`（默认）

基极-集电极结两端的寄生电容。

### **Base-emitter junction capacitance** — 基极-发射极结电容 `5` `pF`（默认）

基极-发射极结两端的寄生电容。

### **Total forward transit time** — 总正向渡越时间 `0` `us`（默认）

表示少数载流子从发射极穿过基区到达集电极的平均时间，通常用参数 TF 表示 [1]。

### **Total reverse transit time** — 总反向渡越时间 `0` `us`（默认）

表示少数载流子从集电极穿过基区到达发射极的平均时间，通常用参数 TR 表示 [1]。

### 温度依赖性

### **Parameterization** — 温度依赖性参数化 `None — Simulate at parameter measurement temperature`（默认）| `Model temperature dependence`

选择以下方法之一进行温度依赖性参数化：

- `None — Simulate at parameter
  measurement temperature` —
  不对温度依赖性建模，或在测量温度
  *Tm1*（由 **Main** 选项卡上的 **Measurement
  temperature** 参数指定）下仿真模型。这是默认方法。
- `Model temperature dependence`
  — 提供仿真温度值，以对温度相关效应进行建模。您还必须根据模块参数化方法提供一组附加参数。如果从数据表对模块进行参数化，则必须提供第二个 [
  *Vbe*
  *Ib* ] 数据对以及第二个测量温度下的
  *h\_fe*。如果通过直接指定方程参数进行参数化，则必须提供
  *XTI*、*EG* 和
  *XTB* 的值。

### **Forward current transfer ratio, h\_fe, at second measurement temperature** — 第二测量温度下的正向电流传输比 h\_fe `125`（默认）

第二测量温度下的小信号电流增益。必须在与 **Main** 选项卡上的 **Forward current transfer ratio
h\_fe** 参数相同的集电极-发射极电压和集电极电流下引用。

#### 依赖关系

仅当为 **Main** 选项卡上的 **Parameterization** 参数选择
`Specify from a datasheet` 时，此参数才可见。

### **Voltage Vbe at second measurement temperature** — 第二测量温度下的电压 Vbe `0.45` `V`（默认）

基极电流为 *Ib* 且温度设置为第二测量温度时的基极-发射极电压。
[*Vbe*
*Ib*] 数据对必须在晶体管处于正常有源区（即非饱和区）时引用。

#### 依赖关系

仅当为 **Main** 选项卡上的 **Parameterization** 参数选择
`Specify from a datasheet` 时，此参数才可见。

### **Current Ib for voltage Vbe at second measurement temperature** — 第二测量温度下电压 Vbe 对应的电流 Ib `0.5` `mA`（默认）

基极-发射极电压为 *Vbe* 且温度设置为第二测量温度时的基极电流。[
*Vbe*
*Ib* ] 数据对必须在晶体管处于正常有源区（即非饱和区）时引用。

#### 依赖关系

仅当为 **Main** 选项卡上的 **Parameterization** 参数选择
`Specify from a datasheet` 时，此参数才可见。

### **Second measurement temperature** — 第二测量温度 `125` `degC`（默认）

测量 *h\_fe*、*Vbe* 和 *Ib* 时的第二温度 *Tm2*。

#### 依赖关系

仅当为 **Main** 选项卡上的 **Parameterization** 参数选择
`Specify from a datasheet` 时，此参数才可见。

### **Current gain temperature coefficient, XTB** — 电流增益温度系数 `0`（默认）

电流增益温度系数值。

#### 依赖关系

仅当为 **Main** 选项卡上的 **Parameterization** 参数选择
`Specify using equation parameters
directly` 时，此参数才可见。

### **Energy gap, EG** — 能隙 `1.11` `eV`（默认）

能隙值。

#### 依赖关系

仅当为 **Main** 选项卡上的 **Parameterization** 参数选择
`Specify using equation parameters
directly` 时，此参数才可见。

### **Saturation current temperature exponent, XTI** — 饱和电流温度指数 `3`（默认）

饱和电流温度系数值。

#### 依赖关系

仅当为 **Main** 选项卡上的 **Parameterization** 参数选择
`Specify using equation parameters
directly` 时，此参数才可见。

### **Device simulation temperature** — 器件仿真温度 `25` `degC`（默认）

仿真器件时的温度 *Ts*。

## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

### R2024a：**Base-collector capacitance voltage** 和 **Base-emitter capacitance voltage** 变量替换为 **Base-collector charge** 和 **Base-emitter charge** 变量

现在您使用 **Base-collector charge** 和 **Base-emitter
charge** 变量为电容和电荷建模指定 **Initial Targets** 和 **Nominal
Values**。**Base-collector capacitance
voltage** 和 **Base-emitter capacitance voltage**
变量已被移除。

如果您在早期版本中创建的模型为
**Base-collector capacitance voltage** 或
**Base-emitter capacitance voltage** 变量指定了 **Initial
Targets** 或 **Nominal Values**，则必须更新该模型。有关如何计算基极-集电极电荷和基极-发射极电荷的详细信息，请参阅 Modeling Capacitance and Charge。

### R2019b：热网络 simlog 路径

从 R2019b 起，可以在内部或外部对此模块的热网络进行建模。

因此，与热网络对应的 simlog 路径已更改。如果您有以编程方式访问 simlog 的脚本，则必须手动更新它以反映这些更改。

## 描述

使用增强 Ebers-Moll 方程的 NPN 双极晶体管

NPN Bipolar Transistor 模块使用 Ebers-Moll 方程的变体来表示 NPN 双极晶体管。Ebers-Moll 方程基于两个指数二极管加两个电流控制电流源。NPN Bipolar Transistor 模块对该模型提供以下增强：

- 厄利电压效应
- 可选的基极、集电极和发射极电阻
- 可选的固定基极-发射极和基极-集电极电容

集电极和基极电流为：

IC=IS[(eqVBE/(kTm1)−eqVBC/(kTm1))(1−VBCVA)−1βR(eqVBC/(kTm1)−1)]IB=IS[1βF(eqVBE/(kTm1)−1)+1βR(eqVBC/(kTm1)−1)]

在这些方程中：

- *IB* 和
  *IC* 是基极和集电极电流，定义为流入器件为正。
- *IS* 是 **Saturation current
  IS** 参数的值。
- *VBE* 是基极-发射极电压，*VBC* 是基极-集电极电压。
- *βF* 是 **Forward current transfer ratio BF parameter**
  参数的值。该项表示理想最大正向电流增益。
- *βR* 是 **Reverse current transfer ratio BR parameter**
  参数的值。该项表示理想最大反向电流增益。
- *VA* 是 **Forward Early voltage VAF** 参数的值。
- *q* 是电子的基本电荷（1.602176e–19 库仑）。
- *k* 是玻尔兹曼常数（1.3806503e–23 J/K）。
- *T*m1 是晶体管温度，由 **Measurement temperature**
  参数值定义。

您可以使用数据表参数指定晶体管行为，模块使用这些参数计算这些方程的参数，也可以直接指定方程参数。

如果 *q**VBC* /
(*k**Tm1*) >
40 或 *q**VBE* /
(*k**Tm1*) >
40，则方程中相应的指数项分别替换为
(*q**VBC* /
(*k**Tm1*) –
39)*e*40 和 (*q**VBE* /
(*k**Tm1*) –
39)*e*40。这有助于防止与指数函数 *e*x 在大 *x* 值处的陡峭梯度相关的数值问题。类似地，如果 *q**VBC* /
(*k**Tm1*) <
–39 或 *q**VBE* /
(*k**Tm1*) <
–39，则方程中相应的指数项分别替换为
(*q**VBC* /
(*k**Tm1*) +
40)*e*–39 和 (*q**VBE* /
(*k**Tm1*) +
40)*e*–39。

可选地，您可以指定基极-发射极和基极-集电极结两端的固定电容。您还可以指定基极、集电极和发射极连接电阻。

### 对电容和电荷建模

您使用 **Base-collector junction capacitance** 和 **Base-emitter junction capacitance** 参数对电容和电荷建模。您还可以使用 **Total forward transit time** 和 **Total reverse transit time** 参数来表示反向恢复电荷和动态特性。此方程定义了基极-集电极电荷，

QBC=tRICE+CBCVBC，

其中：

- *t*R 是 **Total reverse transit time** 参数值。
- *I*CE 是集电极-发射极电流。
- *C*BC 是 **Base-collector junction capacitance** 参数值。
- *V*BC 是基极-集电极电压。

此方程定义了基极-集电极电荷和电容器电流，

IQBC=dQBCdt。

此方程定义了基极-发射极电荷，

QBE=tFIC+CBEVBE，

其中：

- *t*F 是 **Total forward transit time** 参数值。
- *I*C 是集电极电流。
- *C*BE 是 **Base-emitter junction capacitance** 参数值。
- *V*BE 是基极-发射极电压。

此方程定义了基极-发射极电荷和电容器电流，

IQBE=dQBEdt。

### 对温度依赖性建模

默认行为是不对温度依赖性建模，器件在您提供模块参数时所处的温度下进行仿真。您可以选择性地在仿真期间包含对晶体管静态行为温度依赖性的建模。不对结电容的温度依赖性建模，因为其影响要小得多。

当包含温度依赖性时，定义晶体管的方程保持不变。测量温度值 *Tm1* 替换为仿真温度 *Ts*。饱和电流 *IS* 以及正向和反向增益（*βF* 和 *βR*）根据以下方程变为温度的函数：

ISTs=ISTm1⋅(Ts/Tm1)XTI⋅exp(−EGkTs(1−Ts/Tm1))

βFs=βFm1(TsTm1)XTB

βRs=βRm1(TsTm1)XTB

其中：

- *Tm1* 是指定晶体管参数时所处的温度，由 **Measurement temperature** 参数值定义。
- *Ts* 是仿真温度。
- *ISTm1* 是测量温度下的饱和电流。
- *ISTs* 是仿真温度下的饱和电流。这是当对温度依赖性建模时，双极晶体管方程中使用的饱和电流值。
- *βFm1* 和 *βRm1* 是测量温度下的正向和反向增益。
- *βFs* 和 *βRs* 是仿真温度下的正向和反向增益。这些是当对温度依赖性建模时，双极晶体管方程中使用的值。
- *EG* 是半导体类型的能隙，以焦耳为单位。硅的值通常取为 1.11 eV，其中 1 eV 为 1.602e-19 焦耳。
- *XTI* 是饱和电流温度指数。
- *XTB* 是正向和反向增益温度系数。
- *k* 是玻尔兹曼常数（1.3806503e–23 J/K）。

*XTI* 和 *EG* 的合适值取决于晶体管的类型和所使用的半导体材料。在实践中，需要调整 *XTI*、*EG* 和 *XTB* 的值，以对特定晶体管的确切行为建模。一些制造商在 SPICE 网表中给出了这些调整后的值，您可以读取相应的值。否则，您可以使用数据手册定义的更高温度 *Tm2* 下的数据来确定 *XTI*、*EG* 和 *XTB* 的值。该模块为此提供了数据手册参数化选项。

您也可以自行调整 *XTI*、*EG* 和 *XTB* 的值，以匹配您特定器件的实验室数据。您可以使用 Simulink® Design Optimization™ 软件来帮助调整这些值。

### 热端口

您可以暴露热端口，以对产生的热量和器件温度的影响进行建模。要暴露热端口，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 该模块不包含热端口，也不对器件中的热量产生进行仿真。
- `Show thermal port` — 该模块包含一个热端口，允许您对传导损耗产生的热量进行建模。为了提高数值效率，热状态不影响模块的电气行为。

有关使用热端口以及 **Thermal Port** 参数的详细信息，请参阅 Simulating Thermal Effects in Semiconductors。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

**注意**

为满足您的所有初始目标，请勿将超过模块方程中微分变量总数的更多初始目标的优先级设置为 `High`。如果您将 **Base-collector junction capacitance** 或 **Total reverse transit time** 参数设置为非零值，并将 **Base-emitter junction capacitance** 或 **Total forward transit time** 参数设置为非零值，则模块方程中的微分变量数量为两个。请选择以下选项之一：

- 要设置端子电流初始条件，请在 **Initial Targets** 部分中，仅将 **Base current** 和 **Collector current** 变量的优先级设置为 `High`。
- 要设置端子电压初始条件，请在 **Initial Targets** 部分中，仅将 **Collector-emitter voltage** 和 **Base-emitter voltage** 变量的优先级设置为 `High`。
- 要设置总电荷初始条件，请在 **Initial Targets** 部分中，仅将 **Base-collector charge** 和 **Base-emitter charge** 变量的优先级设置为 `High`。*（自 R2024a 起）*

使用标称值来指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。

### 绘制基本 I-V 特性

您可以在不构建完整模型的情况下绘制 NPN Bipolar Transistor 模块的基本 I-V 特性。使用这些图来探究您的参数选择对器件特性的影响。如果您从数据手册对模块进行参数化，可以将您的图与数据手册进行比较，以检查您是否正确地对模块进行了参数化。如果您有一个完整的工作模型但不知道使用哪个制造部件，可以将您的图与数据手册进行比较，以帮助您做出决定。

要启用此选项，请将 NPN Bipolar Transistor 模块的 **Modeling option** 参数设置为 `No thermal port`。要绘制基本特性，请右键单击该模块，然后从上下文菜单中选择 **Electrical** > **Basic characteristics**。有关 **Basic characteristics** 选项的详细信息，请参阅 Plot Basic I-V Characteristics of Semiconductor Blocks。
