---
type: simulink-block
title: 'SM AC8C'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control / Automatic Voltage Regulators — AC Type'
documentation_page: 'smac8c'
documentation_source_path: 'ref/smac8c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM AC8C

## 端口

### 输入

### **V\_REF** — 电压参考标量

电压调节器参考设定点，采用标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **V\_S** — 来自稳定器的输入标量

来自电力系统稳定器的输入，采用标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **V\_T** — 机端电压标量

以标幺值表示的机端电压幅值，指定为标量。

**数据类型：** `single` | `double`

### **I\_T** — 机端电流标量

以标幺值表示的机端电流幅值，指定为标量。

**数据类型：** `single` | `double`

### **V\_OEL** — 过励限制信号标量

来自过励限制器的输入，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自过励限制器的输入，请将 **Alternate OEL input locations (V\_OEL)** 设置为 `Unused`。
- 要在求和点使用来自过励限制器的输入，请将 **Alternate OEL input locations (V\_OEL)** 设置为 `Summation point`。
- 要在接管点使用来自过励限制器的输入，请将 **Alternate OEL input locations (V\_OEL)** 设置为 `Take-over`。

**数据类型：** `single` | `double`

### **V\_UEL** — 欠励限制信号标量

来自欠励限制器的输入，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自欠励限制器的输入，请将 **Alternate UEL input locations (V\_UEL)** 设置为 `Unused`。
- 要在求和点使用来自欠励限制器的输入，请将 **Alternate UEL input locations (V\_UEL)** 设置为 `Summation point`。
- 要在接管点使用来自欠励限制器的输入，请将 **Alternate UEL input locations (V\_UEL)** 设置为 `Take-over`。

**数据类型：** `single` | `double`

### **V\_SCLsum** — 求和点定子电流限制信号标量

在使用求和点时来自定子电流限制器的输入，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations (V\_SCL)** 设置为 `Unused`。
- 要在求和点使用来自定子电流限制器的输入，请将 **Alternate SCL input locations (V\_SCL)** 设置为 `Summation point`。

**数据类型：** `single` | `double`

### **V\_OELscl** — 过励限制器接管定子电流限制标量

在使用接管点时，来自定子电流限制器的输入，用于防止磁场过励，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations (V\_SCL)** 设置为 `Unused`。
- 要在接管点使用来自定子电流限制器的输入，请将 **Alternate SCL input locations (V\_SCL)** 设置为 `Take-over`。

**数据类型：** `single` | `double`

### **V\_UELscl** — 欠励限制器接管定子电流限制标量

在使用接管点时，来自定子电流限制器的输入，用于防止磁场欠励，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations (V\_SCL)** 设置为 `Unused`。
- 要在接管点使用来自定子电流限制器的输入，请将 **Alternate SCL input locations (V\_SCL)** 设置为 `Take-over`。

**数据类型：** `single` | `double`

### **Ifd\_pu** — 测量的励磁电流标量

同步电机的测量标幺励磁电流，指定为标量。

**数据类型：** `single` | `double`
### 输出

### **Efd\_pu** — 励磁电压标量

要施加到同步电机励磁电路的标幺励磁电压，以标量形式返回。

**数据类型：** `single` | `double`

## 参数

### 常规

### **Initial field voltage, Efd0 (pu)** — 初始输出电压 `1`（默认） | 实数

要施加到同步电机励磁电路的初始标幺电压。

### **Initial terminal voltage, Vt0 (pu)** — 初始机端电压 `1`（默认） | 实数

要施加到机端的初始标幺电压。

### **Initial terminal current, It0 (pu)** — 初始机端电流 `1`（默认） | 实数

要施加到机端的初始标幺电压。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认） | `0` | 正标量

连续块执行之间的时间。在执行期间，模块产生输出，并在适当情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，将此参数设置为 `-1`。对于离散时间操作，将此参数设置为正整数。对于连续时间操作，将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

### 预控制

### **Resistive component of load compensation, R\_C (pu)** — 补偿电阻 `0`（默认） | 正数

用于电流补偿系统的电阻。将此参数和 **Reactance component of load compensation, X\_C (pu)** 设置为 `0` 以禁用电流补偿。

### **Reactance component of load compensation, X\_C (pu)** — 补偿电抗 `0`（默认） | 正数

用于电流补偿系统的电抗。将此参数和 **Resistive component of load compensation, R\_C (pu)** 设置为 `0` 以禁用电流补偿。

### **Regulator input filter time constant, T\_R (s)** — 调节器时间常数 `0`（默认） | 正数

电压传感器滤波的等效时间常数。

### 控制

### **Voltage regulator proportional gain, K\_PR (pu)** — 电压调节器比例增益 `80`（默认）

电压调节器的标幺比例增益。

### **Voltage regulator integral gain, K\_IR (pu/s)** — 电压调节器积分增益 `5`（默认）

电压调节器的标幺积分增益。

### **Voltage regulator derivative gain, K\_DR (pu.s)** — 电压调节器微分增益 `10`（默认）

电压调节器的微分增益。

### **Lag time constant for derivative channel of PID controller, T\_DR (s)** — PID 微分通道滞后时间常数 `0.02`（默认） | 正数

PID 控制器微分通道的等效滞后时间常数。

### **Maximum voltage regulator output, V\_PIDmax (pu)** — PID 调节器最大输出 `99`（默认） | 正数

PID 调节器允许的最大标幺输出。

### **Minimum voltage regulator output, V\_PIDmin (pu)** — 调节器最小输出 `-99`（默认） | 正数

PID 调节器允许的最小标幺输出。

### **Rectifier bridge gain, K\_A (pu)** — 整流桥增益 `1`（默认） | 正数

与整流器关联的增益。

### **Rectifier bridge time constant, T\_A (s)** — 整流桥时间常数 `0.01`（默认） | 正数

整流器的时间常数。

### **Maximum regulator output, V\_Rmax (pu)** — 调节器输出上限 `35`（默认） | 实数

调节器的最大标幺输出电压。

### **Minimum regulator output, V\_Rmin (pu)** — 调节器输出下限 `0`（默认） | 实数

调节器的最小标幺输出电压。

### **Alternate PSS input locations (V\_S)** — PSS 输入位置 `Voltage error calculation`（默认） | `After take-over UEL`

电力系统稳定器输入的位置。

### **Alternate OEL input locations (V\_OEL)** — OEL 输入位置 `Unused`（默认） | `Summation point at voltage error` | `Take-over at voltage error` | `Take-over at voltage regulator output`

过励限制器输入的位置。

### **Alternate UEL input locations (V\_UEL)** — UEL 输入位置 `Unused`（默认） | `Summation point at voltage error` | `Take-over at voltage error` | `Take-over at voltage regulator output`

欠励限制器输入的位置。

### **Alternate SCL input locations (V\_SCL)** — SCL 输入位置 `Unused`（默认） | `Summation point at voltage error` | `Take-over at voltage error` | `Take-over at voltage regulator output`

定子电流限制器输入的位置：

- 如果选择 `Summation point`，请使用 **V\_SCLsum** 输入端口。
- 如果选择任一 `Take-over` 选项，请使用 **V\_OELscl** 和 **V\_UELscl** 输入端口。

### 励磁机

### **Exciter field proportional constant, K\_E (pu)** — 励磁机磁场增益 `1`（默认） | 正数

励磁机磁场的比例常数。

### **Exciter field time constant, T\_E (s)** — 励磁机磁场时间常数 `1.2`（默认） | 正数

励磁机磁场的时间常数。

### **Rectifier loading factor proportional to commutating reactance, K\_C (pu)** — 整流器负载系数 `0.55`（默认） | 正数

与换相电抗成比例的整流器负载系数。

### **Demagnetizing factor, function of exciter alternator reactances, K\_D (pu)** — 去磁系数 `1.1`（默认） | 正数

与励磁机交流发电机各电抗有关的去磁系数。

### **Exciter output voltage for saturation factor S\_E(E\_1), E\_1 (pu)** — 第一饱和输出电压 `9`（默认） | 正数

第一饱和系数的励磁机输出电压。

### **Exciter saturation factor at exciter output voltage E\_1, S\_E(E\_1) (1)** — 第一饱和查找电压 `3`（默认） | 正数

第一励磁机的饱和系数。

### **Exciter output voltage for saturation factor S\_E(E\_2), E\_2 (pu)** — 第二饱和输出电压 `6.5`（默认） | 正数

第二饱和系数的励磁机输出电压。

### **Exciter saturation factor at exciter output voltage E\_2, S\_E(E\_2) (1)** — 第二饱和查找电压 `0.3`（默认） | 正数

第二励磁机的饱和系数。

### **Maximum exciter field current, V\_FEmax (pu)** — 励磁机上限 `6`（默认） | 实数

最大标幺励磁电流限值参考。

### **Minimum exciter voltage output limit, V\_Emin (pu)** — 励磁机下限 `0`（默认） | 实数

最小标幺励磁机电压输出。

### **Potential circuit gain coefficient, K\_P (pu)** — 电势电路增益系数 `1`（默认） | 实数

标幺电势电路增益系数。

#### 依赖关系

要启用此参数，请将 **Logical switch 1** 设置为 `Position A: power source derived from terminal voltage`。

### **Potential circuit phase angle (degrees)** — 电势电路相位角 `0`（默认） | 实数

电势电路相位角，以 degrees 为单位。

#### 依赖关系

要启用此参数，请将 **Logical switch 1** 设置为 `Position A: power source derived from terminal voltage`。

### **Potential circuit (current) gain coefficient, K\_I (pu)** — 电势电路电流增益系数 `0`（默认） | 实数

标幺电势电路电流增益系数。

#### 依赖关系

要启用此参数，请将 **Logical switch 1** 设置为 `Position A: power source derived from terminal voltage`。

### **Reactance associated with potential source, X\_L (pu)** — 与电势源关联的电抗 `0`（默认） | 实数

与电势源关联的标幺电抗。

#### 依赖关系

要启用此参数，请将 **Logical switch 1** 设置为 `Position A: power source derived from terminal voltage`。

### **Rectifier loading factor proportional to commutating reactance, K\_C1 (pu)** — 与换相电抗成比例的整流器负载系数 `0`（默认） | 实数

与换相电抗成比例的整流器标幺负载系数。

### **Logical switch 1** — 逻辑开关 `Position A: power source derived from terminal voltage`（默认） | `Position B: power source independent of the terminal conditions`

逻辑开关 1 的位置。

### **Maximum available exciter field voltage, V\_Bmax (pu)** — 最大可用励磁机磁场电压 `1.25`（默认） | 实数

励磁机的最大可用标幺磁场电压。

## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

离散时间或连续时间同步电机 AC8C 励磁系统，包括自动电压调节器和励磁机

SM AC8C 模块实现符合 IEEE 421.5-2016[1] 的同步电机 AC8C 励磁系统模型。

使用此模块对作为发电机运行、使用交流旋转励磁机的同步电机的励磁电压的控制和调节进行建模。

可以通过 **Sample time (-1 for inherited)** 参数在模块的连续实现和离散实现之间切换。要将积分器配置为连续时间，请将 **Sample time (-1 for inherited)** 属性设置为 `0`。要将积分器配置为离散时间，请将 **Sample time (-1 for inherited)** 属性设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。

SM AC8C 模块由五个主要组件组成：

- 电流补偿器根据机端电流修改测得的机端电压。
- 电压测量传感器使用低通滤波器模拟机端电压传感器的动态特性。
- 励磁控制元件组件将电压传感器输出与机端电压参考进行比较以产生电压误差。然后，该电压误差经过电压调节器以产生励磁机磁场电压。
- 交流旋转励磁机对交流旋转励磁机建模，该励磁机产生施加到受控同步电机的磁场电压。该模块还将励磁机磁场电流（标准符号为 *VFE*）反馈到励磁系统。
- 电源对受控整流器的电源与机端电压的依赖关系进行建模。

此图显示了 AC8C 励磁系统模型的总体结构：

在图中：

- *VT* 和 *IT* 是同步电机的测量机端电压和电流。
- *VC1* 是电流补偿后的机端电压。
- *VC* 是滤波后的电流补偿机端电压。
- *VREF* 是参考机端电压。
- *VS* 是电力系统稳定器电压。
- *SW1* 是用户选择的受控整流器电源开关。
- *VB* 是励磁机磁场电压。
- *EFE* 和 *VFE* 分别是励磁机磁场电压和电流。
- *EFD* 和 *IFD* 分别是磁场电压和电流。

以下各节详细描述模块的每个主要部分。

### 电流补偿器和电压测量传感器

电流补偿器建模为：

VC1=VT+ITRC2+XC2,

其中：

- *RC* 是负载补偿电阻。
- *XC* 是负载补偿电抗。

电压测量传感器使用 Low-Pass Filter 模块实现，时间常数为 *TR*。有关该模块的离散和连续实现，请参阅该模块的文档。

### 励磁控制元件

此图展示了励磁控制元件的整体结构：

图中：

- Summation Point Logic 子系统对过励限制器 (OEL)、欠励限制器 (UEL)、定子电流限制器 (SCL) 和功率开关选择器 (V\_S) 电压的求和点输入位置进行建模。有关将此模块与限制器配合使用的详细信息，请参阅励磁电流限制器。
- 有两个 Take-over Logic 子系统。它们对 OEL、UEL、SCL 和 PSS 电压的接管点输入位置进行建模。有关将此模块与限制器配合使用的详细信息，请参阅励磁电流限制器。
- PID\_R 子系统对用作自动电压调节器控制结构的 PID 控制器进行建模。该模块的最小和最大抗积分饱和饱和限值分别为 *VPIDmin* 和 *VPIDmax*。
- Low-Pass Filter 模块对电压调节器的主要动态特性进行建模。其中，*KA* 是调节器增益，*TA* 是调节器的主要时间常数。该模块的最小和最大抗积分饱和饱和限值分别为 *VRmin* 和 *VRmax*。
- **Logical switch 1** 参数控制可控整流器电源的来源。电压调节器指令信号 *VR* 乘以励磁机励磁电压 *VB*。有关用于可控整流器电源的用户所选逻辑开关的详细信息，请参阅电源。

### 励磁电流限制器

您可以使用各种励磁电流限制器在不安全运行条件下修改电压调节器的输出：

- 使用过励限制器防止因励磁电流需求过大而导致励磁绕组过热。
- 使用欠励限制器在励磁过低时提升励磁，因为过低会有失步风险。
- 使用定子电流限制器防止因电流过大而导致定子绕组过热。

将上述任一种限制器的输出连接到以下某个点：

- 求和点，作为自动电压调节器 (AVR) 反馈回路的一部分
- 接管点，用于覆盖 AVR 的通常行为

如果您在求和点使用定子电流限制器，请使用单个输入 *VSCLsum*。如果您在接管点使用定子电流限制器，请同时使用过励输入 *VOELscl* 和欠励输入 *VUELscl*。

### 交流旋转励磁机

此图展示了交流旋转励磁机的结构：

图中：

- 励磁机励磁电流 *VFE* 是三个信号之和：

  - 非线性函数 *Vx* 对励磁机输出电压的饱和进行建模。
  - 比例项 *KE* 对励磁机输出电压与励磁机励磁电流之间的线性关系进行建模。
  - 该子系统使用反馈回路中的去磁常数 *KD* 对负载电流对励磁机输出电压的去磁效应进行建模。
- Integrator with variable limits 子系统对 *EFE* 与 *VFE* 之间的差值进行积分，以生成励磁机交流发电机输出电压 *VE*。*TE* 是此过程的时间常数。
- 非线性函数 *FEX* 对由整流器调节引起的励磁机输出电压降进行建模。此函数取决于常数 *KC*，而 *KC* 本身是换相电抗的函数。
- 参数 *VEmin* 和 *VFEmax* 对旋转励磁机的下限和上限进行建模。

### 电源

通过在 **Logical switch 1** 参数中选择相关选项，可以对可控整流器使用不同的电源表示。可控整流器的电源既可以从端电压获得（`Position A: power source derived from terminal
voltage`），也可以独立于端电压（`Position B: power source independent from the terminal
conditions`）。
