---
type: simulink-block
title: 'SM AC3C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smac3c'
documentation_source_path: 'ref/smac3c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM AC3C

## 端口

### 输入

### **V\_REF** — 电压参考标量

电压调节器参考设定点，采用标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **V\_S** — 来自稳定器的输入标量

来自电力系统稳定器的输入，采用标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **V\_T** — 机端电压标量

机端电压幅值，采用标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **I\_T** — 机端电流标量

机端电流幅值，采用标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **V\_OEL** — 过励限制信号标量

来自过励限制器的输入，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自过励限制器的输入，将 **Alternate OEL input locations (V\_OEL)** 设置为 `Unused`。
- 要在求和点使用来自过励限制器的输入，将 **Alternate OEL input locations (V\_OEL)** 设置为 `Summation point`。
- 要在接管点使用来自过励限制器的输入，将 **Alternate OEL input locations (V\_OEL)** 设置为 `Take-over`。

**数据类型：** `single` | `double`

### **V\_UEL** — 欠励限制信号标量

来自欠励限制器的输入，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自欠励限制器的输入，将 **Alternate UEL input locations (V\_UEL)** 设置为 `Unused`。
- 要在求和点使用来自欠励限制器的输入，将 **Alternate UEL input locations (V\_UEL)** 设置为 `Summation point`。
- 要在接管点使用来自欠励限制器的输入，将 **Alternate UEL input locations (V\_UEL)** 设置为 `Take-over`。

**数据类型：** `single` | `double`

### **V\_SCLsum** — 求和点定子电流限制信号标量

使用求和点时来自定子电流限制器的输入，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，将 **Alternate SCL input locations (V\_SCL)** 设置为 `Unused`。
- 要在求和点使用来自定子电流限制器的输入，将 **Alternate SCL input locations (V\_SCL)** 设置为 `Summation point`。

**数据类型：** `single` | `double`

### **V\_SCLoel** — 用于过励限制器的接管点定子电流限制标量

使用接管点时来自定子电流限制器的输入，用于防止磁场过励，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，将 **Alternate SCL input locations (V\_SCL)** 设置为 `Unused`。
- 要在接管点使用来自定子电流限制器的输入，将 **Alternate SCL input locations (V\_SCL)** 设置为 `Take-over`。

**数据类型：** `single` | `double`

### **V\_SCLuel** — 用于欠励限制器的接管点定子电流限制标量

使用接管点时来自定子电流限制器的输入，用于防止磁场欠励，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，将 **Alternate SCL input locations (V\_SCL)** 设置为 `Unused`。
- 要在接管点使用来自定子电流限制器的输入，将 **Alternate SCL input locations (V\_SCL)** 设置为 `Take-over`。

**数据类型：** `single` | `double`

### **Ifd\_pu** — 测量的励磁电流标量

同步电机的测量标幺值励磁电流，指定为标量。

**数据类型：** `single` | `double`
### 输出

### **Efd\_pu** — 励磁电压标量

要施加到同步电机励磁电路的标幺值励磁电压，以标量形式返回。

**数据类型：** `single` | `double`

## 参数

### 常规

### **Initial field voltage, Efd0 (pu)** — 初始输出电压 `1`（默认）| 实数

要施加到同步电机励磁电路的初始标幺值电压。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，将此参数设置为 `-1`。对于离散时间操作，将此参数设置为正整数。对于连续时间操作，将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

### 预控制

### **Resistive component of load compensation, R\_C (pu)** — 补偿电阻 `0`（默认）| 正数

电流补偿系统中使用的电阻。将此参数和 **Reactance component of load compensation, X\_C (pu)** 设置为 `0` 以禁用电流补偿。

### **Reactance component of load compensation, X\_C (pu)** — 补偿电抗 `0`（默认）| 正数

电流补偿系统中使用的电抗。将此参数和 **Resistive component of load compensation, R\_C (pu)** 设置为 `0` 以禁用电流补偿。

### **Regulator input filter time constant, T\_R (s)** — 调节器时间常数 `0`（默认）| 正数

电压变送器滤波的等效时间常数。

### 控制

### **Voltage regulator proportional gain, K\_PR (pu)** — 电压调节器的比例增益 `1`（默认）

电压调节器的标幺值比例增益。

### **Voltage regulator integral gain, K\_IR (pu/s)** — 电压调节器的积分增益 `0`（默认）

电压调节器的标幺值每秒积分增益。

### **Voltage regulator derivative gain, K\_DR (pu.s)** — 电压调节器的微分增益 `0`（默认）

电压调节器的微分增益。

### **Lag time constant for derivative channel of PID controller, T\_DR (s)** — PID 微分通道的滞后时间常数 `1`（默认）| 正数

PID 控制器微分通道的等效滞后时间常数。

### **Maximum PID regulator output, V\_PIDmax (pu)** — PID 调节器的最大输出 `3.2`（默认）| 正数

PID 调节器的最大允许标幺值输出。

### **Minimum PID regulator output, V\_PIDmin (pu)** — PID 调节器的最小输出 `-3.2`（默认）| 正数

PID 调节器的最小允许标幺值输出。

### **Regulator denominator (lag) time constant, T\_B (s)** — 调节器滞后时间常数 `0`（默认）| 正数

电压调节器中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **Regulator numerator (lead) time constant, T\_C (s)** — 调节器超前时间常数 `0`（默认）| 正数

电压调节器中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **Regulator output gain, K\_A (pu)** — 调节器增益 `45.62`（默认）| 正数

与电压调节器相关联的增益。

### **Regulator output time constant, T\_A (s)** — 调节器时间常数 `0.013`（默认）| 正数

电压调节器的主要时间常数。

### **Maximum regulator output, V\_Amax (pu)** — 调节器输出的上限 `1`（默认）| 实数

调节器的最大标幺值输出电压。

### **Minimum regulator output, V\_Amin (pu)** — 调节器输出的下限 `-0.95`（默认）| 实数

调节器的最小标幺值输出电压。

### **Rate feedback time constant, T\_F (s)** — 速率反馈时间常数 `1`（默认）| 正数

用于稳定励磁系统的速率反馈模块时间常数。

### **Value of EFD at which feedback gain changes, E\_FDN (pu)** — 反馈增益变化时的 EFD 值 `2.36`（默认）| 正数

反馈增益变化时的 EFD 标幺值。

### **Rate feedback excitation system stabilizer gain, K\_F (pu)** — 速率反馈增益 `0.143`（默认）| 正数

用于稳定励磁系统的速率反馈模块增益。

### **Rate feedback excitation system stabilizer gain, K\_N (pu)** — 速率反馈增益 `0.05`（默认）| 正数

用于稳定励磁系统的速率反馈模块增益。

### **Alternate OEL input locations (V\_OEL)** — OEL 输入位置 `Unused`（默认）| `Summation point` | `Take-over`

过励限制器输入的位置。

### **Alternate UEL input locations (V\_UEL)** — UEL 输入位置 `Unused`（默认）| `Summation point` | `Take-over`

欠励限制器输入的位置。

### **Alternate SCL input locations (V\_SCL)** — SCL 输入位置 `Unused`（默认）| `Summation point` | `Take-over`

定子电流限制器输入的位置：

- 如果选择 `Summation point`，使用 **V\_SCLsum** 输入端口。
- 如果选择 `Take-over`，使用 **V\_SCLoel** 和 **V\_SCLuel** 输入端口。

### 励磁机

### **Exciter field proportional constant, K\_E (pu)** — 励磁机磁场增益 `1`（默认）| 正数

励磁机磁场的比例常数。

### **Exciter field time constant, T\_E (s)** — 励磁机磁场时间常数 `0.17`（默认）| 正数

励磁机磁场的时间常数。

### **Rectifier loading factor proportional to commutating reactance, K\_C (pu)** — 整流器负载因子 `0.104`（默认）| 正数

与换相电抗成比例的整流器负载因子。

### **Demagnetizing factor, function of exciter alternator reactances, K\_D (pu)** — 去磁因子 `0.499`（默认）| 正数

与励磁机交流发电机各电抗有关的去磁因子。

### **Exciter output voltage for saturation factor S\_E(E\_1), E\_1 (pu)** — 第一个饱和输出电压 `6.24`（默认）| 正数

第一个饱和因子的励磁机输出电压。

### **Exciter saturation factor at exciter output voltage E\_1, S\_E(E\_1) (1)** — 第一饱和查表电压 `1.143`（默认）| 正数

第一台励磁机的饱和因子。

### **Exciter output voltage for saturation factor S\_E(E\_2), E\_2 (pu)** — 第二个饱和输出电压 `4.68`（默认）| 正数

第二个饱和因子的励磁机输出电压。

### **Exciter saturation factor at exciter output voltage E\_2, S\_E(E\_2) (1)** — 第二饱和查表电压 `0.1`（默认）| 正数

第二台励磁机的饱和因子。

### **Gain associated with regulator and alternator field power supply, K\_R (pu)** — 调节器和交流发电机磁场电源增益 `3.77`（默认）| 实数

调节器和交流发电机磁场电源的标幺值增益。

### **Minimum exciter voltage output, V\_Emin (pu)** — 励磁机下限 `0.1`（默认）| 实数

最小标幺值励磁机电压输出。

### **Exciter field current limit, V\_FEmax (pu)** — 励磁机上限 `16`（默认）| 实数

励磁机磁场电流的标幺值上限。

## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

离散时间或连续时间同步电机 AC3C 励磁系统，包括自动电压调节器和励磁机

SM AC3C 模块实现符合 IEEE 421.5-2016[1] 的同步电机 AC3C 型励磁系统模型。

使用此模块对作为发电机运行且使用交流旋转励磁机的同步电机的励磁电压控制与调节进行建模。

你可以通过 **Sample time (-1 for inherited)** 参数在模块的连续和离散实现之间切换。要将积分器配置为连续时间，将 **Sample time (-1 for inherited)** 属性设置为 `0`。要将积分器配置为离散时间，将 **Sample time (-1 for inherited)** 属性设置为正的、非零值，或设置为 `-1` 以从上游模块继承采样时间。

SM AC3C 模块由四个主要组件组成：

- 电流补偿器根据机端电流修改测量的机端电压。
- 电压测量变送器使用低通滤波器模拟机端电压变送器的动态特性。
- 励磁控制元件组件将电压变送器输出与机端电压参考进行比较，以产生电压误差。然后，该电压误差经过电压调节器以产生励磁机磁场电压。
- 交流旋转励磁机组件对交流旋转励磁机建模，其产生施加于受控同步电机的励磁电压。该模块还将励磁机磁场电流（标准符号为 *VFE*）反馈到励磁系统。

此图显示 AC3C 励磁系统模型的总体结构：

图中：

- *VT* 和 *IT* 是同步电机的测量机端电压和电流。
- *VC1* 是电流补偿后的机端电压。
- *VC* 是滤波后的电流补偿机端电压。
- *VREF* 是参考机端电压。
- *VS* 是电力系统稳定器电压。
- *EFE* 和 *VFE* 分别是励磁机磁场电压和电流。
- *EFD* 和 *IFD* 分别是励磁电压和电流。

以下各节详细描述模块的每个主要部分。

### 电流补偿器和电压测量变送器

电流补偿器建模为：

VC1=VT+ITRC2+XC2,

其中：

- *RC* 是负载补偿电阻。
- *XC* 是负载补偿电抗。

电压测量变送器使用时间常数为 *TR* 的 Low-Pass Filter 模块实现。有关离散和连续实现，请参阅此模块的文档。

### 励磁控制元件

此图展示了励磁控制元件的总体结构：

在图中：

- Summation Point Logic 子系统对过励限制器（OEL）、欠励限制器（UEL）和定子电流限制器（SCL）电压的求和点输入位置进行建模。有关将限制器与此模块一起使用的更多信息，请参阅励磁电流限制器。
- PID\_R 子系统对 PID 控制器进行建模，并允许表示改造项目，即在励磁机中添加现代数字励磁机。通过调整 PID 参数，可以对 SM AC3A 励磁系统模型进行建模。
- Lead-Lag 模块对与电压调节器相关的附加动态进行建模。这里，*TC* 是超前时间常数，*TB* 是滞后时间常数。有关离散和连续实现，请参阅 Lead-Lag 模块的文档。
- Take-over Logic 子系统对 OEL、UEL 和 SCL 电压的接管点输入位置进行建模。有关将限制器与此模块一起使用的更多信息，请参阅励磁电流限制器。
- Low-Pass Filter 模块对电压调节器的主要动态进行建模。这里，*KA* 是调节器增益，*TA* 是调节器的主要时间常数。该模块的最小和最大抗积分饱和饱和限值分别为 *VAmin* 和 *VAmax*。
- 电压调节器功率来自励磁机输出电压。电压调节器指令信号 *VA* 乘以励磁机输出电压 *EFD*，再乘以 *KR*。这给系统增加了一定程度的非线性。
- Filtered Derivative 模块对用于稳定励磁系统的速率反馈路径进行建模。在这种情况下，稳定器具有非线性特性。如果励磁机输出电压 *EFD* 小于 **Value of EFD at which feedback gain changes, E\_FDN (pu)** 参数，则反馈增益为 *KF*。如果励磁机输出电压大于 **Value of EFD at which feedback gain changes, E\_FDN (pu)** 参数，则反馈增益为 *KN*。有关确切的离散和连续实现，请参阅 Filtered Derivative 模块的文档。
- *EFEmin* 和 *EFEmax* 是输出励磁机励磁电压 *EFE* 的最小和最大饱和限值。

### 励磁电流限制器

在不安全运行条件下，可以使用各种励磁电流限制器来修改电压调节器的输出：

- 使用过励限制器防止因过大的励磁电流需求而导致励磁绕组过热。
- 使用欠励限制器在励磁过低时提升励磁，否则存在失步风险。
- 使用定子电流限制器防止因电流过大而导致定子绕组过热。

将任何这些限制器的输出连接到以下点之一：

- 作为自动电压调节器（AVR）反馈回路一部分的求和点
- 用于覆盖 AVR 通常行为的接管点

如果在求和点使用定子电流限制器，请使用单输入 *VSCLsum*。如果在接管点使用定子电流限制器，请同时使用过励输入 *VSCLoel* 和欠励输入 *VSCLuel*。

### 交流旋转励磁机

此图展示了交流旋转励磁机的结构：

在图中：

- 励磁机励磁电流 *VFE* 是三个信号之和：

  - 非线性函数 *Vx* 对励磁机输出电压的饱和进行建模。
  - 比例项 *KE* 对励磁机输出电压与励磁机励磁电流之间的线性关系进行建模。
  - 该子系统使用反馈回路中的去磁常数 *KD* 对负载电流对励磁机输出电压的去磁效应进行建模。
- Integrator with variable limits 子系统对 *EFE* 与 *VFE* 之间的差进行积分，以生成励磁机交流发电机输出电压 *VE*。*TE* 是该过程的时间常数。
- 非线性函数 *FEX* 对由整流器调节引起的励磁机输出电压降进行建模。此函数取决于常数 *KC*，而 *KC* 本身是换相电抗的函数。
- 参数 *VEmin* 和 *VFEmax* 对旋转励磁机的下限和上限进行建模。
