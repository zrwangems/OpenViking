---
type: simulink-block
title: 'SM AC7C'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control / Automatic Voltage Regulators — AC Type'
documentation_page: 'smac7c'
documentation_source_path: 'ref/smac7c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM AC7C

## 端口

### 输入

### **V\_REF** — 电压参考标量

电压调节器参考设定值，以标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **V\_S** — 来自稳定器的输入标量

来自电力系统稳定器的输入，以标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **V\_T** — 机端电压标量

以标幺值表示的机端电压幅值，指定为标量。

**数据类型：** `single` | `double`

### **I\_T** — 机端电流标量

以标幺值表示的机端电流幅值，指定为标量。

**数据类型：** `single` | `double`

### **V\_OEL** — 过励限制信号标量

来自过励限制器的输入，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自过励限制器的输入，请将 **Alternate OEL input locations (V\_OEL)** 设置为 `Unused`。
- 要在求和点使用来自过励限制器的输入，请将 **Alternate OEL input locations (V\_OEL)** 设置为 `Summation point`。
- 要在接管点使用来自过励限制器的输入，请将 **Alternate OEL input locations (V\_OEL)** 设置为 `Take-over`。

**数据类型：** `single` | `double`

### **V\_UEL** — 欠励限制信号标量

来自欠励限制器的输入，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自欠励限制器的输入，请将 **Alternate UEL input locations (V\_UEL)** 设置为 `Unused`。
- 要在求和点使用来自欠励限制器的输入，请将 **Alternate UEL input locations (V\_UEL)** 设置为 `Summation point`。
- 要在接管点使用来自欠励限制器的输入，请将 **Alternate UEL input locations (V\_UEL)** 设置为 `Take-over`。

**数据类型：** `single` | `double`

### **V\_SCLsum** — 求和点定子电流限制信号标量

使用求和点时来自定子电流限制器的输入，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations (V\_SCL)** 设置为 `Unused`。
- 要在求和点使用来自定子电流限制器的输入，请将 **Alternate SCL input locations (V\_SCL)** 设置为 `Summation point`。

**数据类型：** `single` | `double`

### **V\_OELscl** — 过励限制器的接管定子电流限制标量

使用接管点时来自定子电流限制器的输入，用于防止励磁过励，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations (V\_SCL)** 设置为 `Unused`。
- 要在接管点使用来自定子电流限制器的输入，请将 **Alternate SCL input locations (V\_SCL)** 设置为 `Take-over`。

**数据类型：** `single` | `double`

### **V\_UELscl** — 欠励限制器的接管定子电流限制标量

使用接管点时来自定子电流限制器的输入，用于防止励磁欠励，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations (V\_SCL)** 设置为 `Unused`。
- 要在接管点使用来自定子电流限制器的输入，请将 **Alternate SCL input locations (V\_SCL)** 设置为 `Take-over`。

**数据类型：** `single` | `double`

### **Ifd\_pu** — 测量的励磁电流标量

同步电机的测量标幺励磁电流，指定为标量。

**数据类型：** `single` | `double`
### 输出

### **Efd\_pu** — 励磁电压标量

要施加到同步电机励磁绕组的标幺励磁电压，以标量形式返回。

**数据类型：** `single` | `double`

## 参数

### 常规

### **Initial field voltage, Efd0 (pu)** — 初始输出电压 `1`（默认）| 实数

要施加到同步电机励磁绕组的初始标幺电压。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请将此参数设置为 `-1`。对于离散时间操作，请将此参数设置为正整数。对于连续时间操作，请将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的屏蔽子系统或变体子系统中，请提升此参数以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

### 预控制

### **Resistive component of load compensation, R\_C (pu)** — 补偿电阻 `0`（默认）| 正数

电流补偿系统中使用的电阻。将此参数和 **Reactance component of load compensation, X\_C (pu)** 设置为 `0` 以禁用电流补偿。

### **Reactance component of load compensation, X\_C (pu)** — 补偿电抗 `0`（默认）| 正数

电流补偿系统中使用的电抗。将此参数和 **Resistive component of load compensation, R\_C (pu)** 设置为 `0` 以禁用电流补偿。

### **Regulator input filter time constant, T\_R (s)** — 调节器时间常数 `0`（默认）| 正数

电压传感器滤波的等效时间常数。

### 控制

### **Voltage regulator proportional gain, K\_PR (pu)** — 电压调节器比例增益 `40`（默认）

电压调节器的标幺比例增益。

### **Voltage regulator integral gain, K\_IR (pu/s)** — 电压调节器积分增益 `5.6`（默认）

电压调节器的标幺积分增益。

### **Voltage regulator derivative gain, K\_DR (pu.s)** — 电压调节器微分增益 `0`（默认）

电压调节器的微分增益。

### **Lag time constant for derivative channel of PID controller, T\_DR (s)** — PID 微分通道的滞后时间常数 `1`（默认）| 正数

PID 控制器微分通道的等效滞后时间常数。

### **Maximum regulator output, V\_Rmax (pu)** — 调节器输出上限 `3.2`（默认）| 实数

调节器的最大标幺输出电压。

### **Minimum regulator output, V\_Rmin (pu)** — 调节器输出下限 `-3.2`（默认）| 实数

调节器的最小标幺输出电压。

### **Field current regulator proportional gain, K\_PA (pu)** — 励磁电流调节器比例增益 `112`（默认）| 实数

与励磁电流调节器相关的标幺比例增益。

### **Field current regulator integral gain, K\_IA (pu/s)** — 励磁电流调节器积分增益 `0`（默认）| 实数

与励磁电流调节器相关的标幺积分增益。

### **Maximum field current regulator output, V\_Amax (pu)** — 励磁电流调节器最大输出 `65.2`（默认）| 实数

励磁电流调节器的最大标幺输出。

### **Minimum field current regulator output, V\_Amin (pu)** — 励磁电流调节器最小输出 `-54`（默认）| 实数

励磁电流调节器的最小标幺输出。

### **Generator field voltage feedback gain, K\_F1 (pu)** — 发电机励磁电压反馈增益 `0`（默认）| 实数

与发电机相关的标幺励磁电压反馈增益。

### **Exciter field current feedback gain, K\_F2 (pu)** — 励磁机励磁电流反馈增益 `0.08`（默认）| 实数

与励磁机相关的标幺励磁电流反馈增益。

### **Rate feedback gain, K\_F3 (pu)** — 速率反馈增益 `0.01`（默认）| 实数

标幺速率反馈模块增益。

### **Rate feedback time constant, T\_F (s)** — 速率反馈时间常数 `1`（默认）| 正数

用于稳定励磁系统的速率反馈模块时间常数。

### **Alternate PSS input locations (V\_S)** — PSS 输入位置 `Voltage error calculation`（默认）| `After take-over UEL`

电力系统稳定器输入的位置。

### **Alternate OEL input locations (V\_OEL)** — OEL 输入位置 `Unused`（默认）| `Summation point at voltage error` | `Take-over at voltage error` | `Take-over at voltage regulator output` | `Take-over at output of inner loop regulator`

过励限制器输入的位置：

- 如果选择 `Summation point at voltage error`，则 **V\_OEL** 是 **Summation Point Logic** 子系统的输入。
- 如果选择 `Take-over at voltage error`，则 **V\_OEL** 是 **Take-over Logic** 子系统的输入。
- 如果选择 `Take-over at voltage regulator output`，则 **V\_OEL** 是 **Take-over Logic 1** 子系统的输入。
- 如果选择 `Take-over at output of inner loop regulator`，则 **V\_OEL** 是 **Take-over Logic 2** 子系统的输入。

### **Alternate UEL input locations (V\_UEL)** — UEL 输入位置 `Unused`（默认）| `Summation point at voltage error` | `Take-over at voltage error` | `Take-over at voltage regulator output`

欠励限制器输入的位置：

- 如果选择 `Summation point at voltage error`，则 **V\_UEL** 是 **Summation Point Logic** 子系统的输入。
- 如果选择 `Take-over at voltage error`，则 **V\_UEL** 是 **Take-over Logic** 子系统的输入。
- 如果选择 `Take-over at voltage regulator output`，则 **V\_UEL** 是 **Take-over Logic 1** 子系统的输入。

### **Alternate SCL input locations (V\_SCL)** — SCL 输入位置 `Unused`（默认）| `Summation point at voltage error` | `Take-over at voltage error` | `Take-over at voltage regulator output`

定子电流限制器输入的位置：

- 如果选择 `Summation point`，请使用 **V\_SCLsum** 输入端口。
- 如果选择任何 `Take-over` 选项，请使用 **V\_OELscl** 和 **V\_UELscl** 输入端口。

### 励磁机

### **Exciter field proportional constant, K\_E (pu)** — 励磁机励磁增益 `1`（默认）| 正数

励磁机励磁的比例常数。

### **Exciter field time constant, T\_E (s)** — 励磁机励磁时间常数 `1.2`（默认）| 正数

励磁机励磁的时间常数。

### **Rectifier loading factor proportional to commutating reactance, K\_C (pu)** — 整流器负载因子 `0.12`（默认）| 正数

与换相电抗成比例的整流器负载因子。

### **Demagnetizing factor, function of exciter alternator reactances, K\_D (pu)** — 去磁因子 `3.3`（默认）| 正数

与励磁机交流发电机reactances(deleted)相关的去磁因子。

### **Exciter output voltage for saturation factor S\_E(E\_1), E\_1 (pu)** — 第一饱和输出电压 `13.6`（默认）| 正数

第一饱和因子的励磁机输出电压。

### **Exciter saturation factor at exciter output voltage E\_1, S\_E(E\_1) (1)** — 第一饱和查找电压 `3.74`（默认）| 正数

第一励磁机的饱和因子。

### **Exciter output voltage for saturation factor S\_E(E\_2), E\_2 (pu)** — 第二饱和输出电压 `10.2`（默认）| 正数

第二饱和因子的励磁机输出电压。

### **Exciter saturation factor at exciter output voltage E\_2, S\_E(E\_2) (1)** — 第二饱和查找电压 `0.32`（默认）| 正数

第二励磁机的饱和因子。

### **Maximum exciter field current limit reference, V\_FEmax (pu)** — 励磁机上限 `23.2`（默认）| 实数

最大标幺励磁电流限制参考值。

### **Minimum exciter voltage output, V\_Emin (pu)** — 励磁机下限 `0`（默认）| 实数

最小标幺励磁机电压输出。

### **Potential circuit gain coefficient, K\_P (pu)** — 电位电路增益系数 `1`（默认）| 实数

标幺电位电路增益系数。

#### 依赖关系

仅当您将 **Power source selector SW1** 参数设置为 `Position A: power source derived from terminal voltage` 且将 **Power source selector SW2** 参数设置为 `Position A: use variable V_B` 时，此参数才可见。

### **Potential circuit phase angle (degrees)** — 电位电路相位角 `0`（默认）| 实数

电位电路相位角，以度为单位。

#### 依赖关系

要启用此参数，请将 **Power source selector SW1** 设置为 `Position A: power source derived from terminal voltage`，并将 **Power source selector SW2** 设置为 `Position A: use variable V_B`。

### **Potential circuit (current) gain coefficient, K\_I (pu)** — 电位电路电流增益系数 `0`（默认）| 实数

标幺电位电路电流增益系数。

#### 依赖关系

要启用此参数，请将 **Power source selector SW1** 设置为 `Position A: power source derived from terminal voltage`，并将 **Power source selector SW2** 设置为 `Position A: use variable V_B`。

### **Reactance associated with potential source, X\_L (pu)** — 与电位源相关的电抗 `0`（默认）| 实数

与电位源相关的标幺电抗。

#### 依赖关系

要启用此参数，请将 **Power source selector SW1** 设置为 `Position A: power source derived from terminal voltage`，并将 **Power source selector SW2** 设置为 `Position A: use variable V_B`。

### **Gain related to regulator and alternator field power supply, K\_R (pu)** — 与调节器和交流发电机励磁电源相关的增益 `0`（默认）| 实数

与调节器和交流发电机励磁电源相关的标幺增益。

#### 依赖关系

要启用此参数，请将 **Power source selector SW2** 设置为 `Position B: do not use variable V_B`。

### **Gain related to negative exciter field current capability, K\_L (pu)** — 与负励磁机励磁电流能力相关的增益 `0`（默认）| 实数

与负励磁机励磁电流能力相关的标幺增益。

### **Rectifier loading factor proportional to commutating reactance, K\_C1 (pu)** — 与换相电抗成比例的整流器负载因子 `0`（默认）| 实数

*自 R2024b 起*

整流器的标幺负载因子，与换相电抗成比例。

#### 依赖关系

要启用此参数，请将 **Power source selector SW2** 设置为 `Position A: use variable V_B`。

### **Maximum available exciter field voltage, V\_Bmax (pu)** — 励磁机最大可用励磁电压 `999`（默认）| 实数

*自 R2024b 起*

励磁机的最大标幺可用励磁电压。

#### 依赖关系

要启用此参数，请将 **Power source selector SW2** 设置为 `Position A: use variable V_B`。

### **Power source selector SW1** — 电源选择器 `Position A: power source derived from terminal voltage`（默认）| `Position B: power source independent of terminal conditions`

电源选择器 SW1 的位置。

#### 依赖关系

要启用此参数，请将 **Power source selector SW2** 设置为 `Position A: use variable V_B`。

### **Power source selector SW2** — 电源选择器 `Position A: use variable V_B`（默认）| `Position B: do not use variable V_B`

电源选择器 SW2 的位置。

## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

离散时间或连续时间同步电机 AC7C 励磁系统，包括自动电压调节器和励磁机

SM AC7C 模块实现符合 IEEE 421.5-2016[1] 的同步电机 AC7C 型励磁系统模型。

使用此模块对作为发电机运行且采用交流旋转励磁机的同步电机的励磁电压控制和调节进行建模。

您可以使用 **Sample time (-1 for inherited)** 参数在模块的连续实现和离散实现之间切换。要将积分器配置为连续时间，请将 **Sample time (-1 for inherited)** 属性设置为 `0`。要将积分器配置为离散时间，请将 **Sample time (-1 for inherited)** 属性设置为正的非零值，或设置为 `-1` 以从上流模块继承采样时间。

SM AC7C 模块由五个主要组件组成：

- 电流补偿器根据机端电流修改测得的机端电压。
- 电压测量变送器使用低通滤波器模拟机端电压变送器的动态特性。
- 励磁控制元件组件将电压变送器输出与机端电压参考值进行比较，以产生电压误差。然后，此电压误差经过电压调节器，以产生励磁机磁场电压。
- 交流旋转励磁机对交流旋转励磁机进行建模，该励磁机产生施加到受控同步电机的励磁电压。该模块还将励磁机磁场电流（其标准符号为 *VFE*）反馈到励磁系统。
- 电源与自励对可控整流器的电源进行建模（当该电源独立于机端电压时）。它还允许表示励磁机的自励。

此图显示了 AC7C 励磁系统模型的总体结构：

图中：

- *VT* 和 *IT* 是同步电机的测得机端电压和机端电流。
- *VC1* 是电流补偿后的机端电压。
- *VC* 是滤波后的电流补偿机端电压。
- *VREF* 是参考机端电压。
- *VS* 是电力系统稳定器电压。
- *SW1* 和 *SW2* 是用户选择的可控整流器电源开关。
- *VB* 是励磁机磁场电压。
- *EFE* 和 *VFE* 分别是励磁机磁场电压和电流。
- *EFD* 和 *IFD* 分别是励磁电压和电流。

以下各节详细描述该模块的每个主要部分。

### 电流补偿器和电压测量变送器

电流补偿器建模为：

VC1=VT+ITRC2+XC2，

其中：

- *RC* 是负载补偿电阻。
- *XC* 是负载补偿电抗。

电压测量变送器实现为具有时间常数 *TR* 的 Low-Pass Filter 模块。有关离散和连续实现，请参阅此模块的文档。

### 励磁控制元件

此图说明了励磁控制元件的总体结构：

图中：

- Summation Point Logic 子系统对过励限制器 (OEL)、欠励限制器 (UEL)、定子电流限制器 (SCL) 和电源开关选择器 (V\_S) 电压的求和点输入位置进行建模。有关将此模块与限制器一起使用的详细信息，请参阅励磁电流限制器。
- 有三个 Take-over Logic 子系统。它们对 OEL、UEL、SCL 和 PSS 电压的接管点输入位置进行建模。有关将此模块与限制器一起使用的详细信息，请参阅励磁电流限制器。
- PID\_R 子系统对 PID 控制器进行建模，该控制器用作自动电压调节器的控制结构。该模块的最小和最大抗饱和饱和限值分别为 *VRmin* 和 *VRmax*。
- PI\_R 子系统对 PI 控制器进行建模，该控制器用作励磁电流调节器的控制结构。该模块的最小和最大抗饱和饱和限值分别为 *VAmin* 和 *VAmax*。
- 在自励情况下，当 *KR* 非零且 **Power source selector SW2** 参数设置为 `Position B: do not use variable V_B` 时，电压调节器的电源来自励磁机输出电压。电压调节器指令信号乘以励磁机输出电压 *EFD*，再乘以 *KR*。有关可控整流器电源的用户选择逻辑开关的详细信息，请参阅电源与自励。
- *KF1* 和 *KF2* 对高带宽调节器内环进行建模，该内环调节发电机磁场电流或励磁电流。
- Filtered Derivative 模块对速率反馈路径进行建模，用于在自动电压调节器没有微分项时稳定励磁系统。这里，*KF3* 和 *TF* 分别是该系统的增益和时间常数。有关离散和连续实现，请参阅 Filtered Derivative 模块的文档。
- *-K\_L\*VFE* 和 *inf* 是输出励磁机磁场电压 *EFE* 的最小和最大饱和限值。
- **initialOffset1** Constant 模块确保仿真可从稳态启动。SM AC7C 模块使用饱和参数和励磁机参数计算此值，包括励磁机磁场电流反馈增益、发电机励磁电压反馈增益和初始励磁电压。

### 励磁电流限制器

在各种不安全运行工况下，可使用多种励磁电流限制器修改电压调节器的输出：

- 使用过励限制器防止因励磁电流需求过大而导致励磁绕组过热。
- 使用欠励限制器在励磁过低时提升励磁，因为励磁过低有失步风险。
- 使用定子电流限制器防止因电流过大而导致定子绕组过热。

将这些限制器中任意一个的输出连接到以下任一位置：

- 作为自动电压调节器 (AVR) 反馈回路一部分的求和点
- 用于覆盖 AVR 通常行为的接管点

如果在求和点使用定子电流限制器，请使用单输入 *VSCLsum*。如果在接管点使用定子电流限制器，请同时使用过励输入 *VOELscl* 和欠励输入 *VUELscl*。

### 交流旋转励磁机

此图显示了交流旋转励磁机的结构：

图中：

- 励磁机磁场电流 *VFE* 是三个信号之和：

  - 非线性函数 *Vx* 对励磁机输出电压的饱和进行建模。
  - 比例项 *KE* 对励磁机输出电压与励磁机磁场电流之间的线性关系进行建模。
  - 该子系统使用反馈回路中的去磁常数 *KD* 对负载电流对励磁机输出电压的去磁效应进行建模。
- Integrator with variable limits 子系统对 *EFE* 和 *VFE* 之间的差值进行积分，以生成励磁机交流发电机输出电压 *VE*。*TE* 是此过程的时间常数。
- 非线性函数 *FEX* 对整流器调节引起的励磁机输出电压降进行建模。该函数取决于常数 *KC*，而 *KC* 本身是换向电抗的函数。
- 参数 *VEmin* 和 *VFEmax* 对旋转励磁机的下限和上限进行建模。

### 电源与自励

通过在 **Power source selector SW1** 参数中选择相关选项，可以对可控整流器使用不同的电源表示。可控整流器的电源既可以取自机端电压 (`Position A: power source derived from terminal voltage`)，也可以独立于机端电压 (`Position B: power source independent from the terminal conditions`)。注意，此开关取决于第二个逻辑开关的状态。

第二个逻辑开关 **Power source selector SW2** 确定励磁机是否采用自励。如果 **Power source selector SW2** 参数设置为 `Position B: do not use variable V_B`，则励磁机为自励，因为与变量 *VB* 关联的模型参数不影响仿真。
