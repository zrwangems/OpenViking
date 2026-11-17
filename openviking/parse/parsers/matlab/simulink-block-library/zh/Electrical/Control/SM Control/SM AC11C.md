---
type: simulink-block
title: 'SM AC11C'
family: 'control'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smac11c'
documentation_source_path: 'ref/smac11c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM AC11C

## 端口

### 输入

### **V\_REF** — 电压参考标量

电压调节器参考设定点，以标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **V\_S** — 来自稳定器的输入标量

来自电力系统稳定器的输入，以标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **V\_T** — 端电压标量

端电压幅值，以标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **I\_T** — 端电流标量

端电流幅值，以标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **V\_OEL** — 过励限制信号标量

来自过励限制器的输入，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自过励限制器的输入，
  将 **Alternate OEL input locations (V\_OEL)** 设置为
  `Unused`。
- 要在求和点使用来自过励限制器的输入，将 **Alternate OEL input locations (V\_OEL)** 设置为
  `Summation point`。
- 要在 Take-over Logic 子系统使用来自过励限制器的输入，将 **Alternate OEL input locations (V\_OEL)** 设置为
  `Take-over at voltage error`。
- 要在 Take-over Logic1 子系统使用来自过励限制器的输入，将 **Alternate OEL input locations (V\_OEL)** 设置为
  `Take-over at voltage regulator output`。

**数据类型：** `single` | `double`

### **V\_UEL** — 欠励限制信号标量

来自欠励限制器的输入，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自欠励限制器的输入，
  将 **Alternate UEL input locations (V\_UEL)** 设置为
  `Unused`。
- 要在求和点使用来自欠励限制器的输入，将 **Alternate UEL input locations (V\_UEL)** 设置为
  `Summation point`。
- 要在 Take-over Logic 子系统使用来自欠励限制器的输入，将 **Alternate UEL input locations (V\_UEL)** 设置为
  `Take-over at voltage error`。
- 要在 Take-over Logic1 子系统使用来自欠励限制器的输入，将 **Alternate UEL input locations (V\_UEL)** 设置为
  `Take-over at voltage regulator output`。

**数据类型：** `single` | `double`

### **V\_SCLsum** — 求和点定子电流限制信号标量

来自定子电流限制器的输入，在使用求和点时，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，
  将 **Alternate SCL input locations (V\_SCL)** 设置为
  `Unused`。
- 要在求和点使用来自定子电流限制器的输入，将 **Alternate SCL input locations (V\_SCL)** 设置为
  `Summation point`。

**数据类型：** `single` | `double`

### **V\_SCLoel** — 用于过励限制器的 Take-over 定子电流限制标量

来自定子电流限制器的输入，用于在使用 take-over 点时防止励磁过励，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，
  将 **Alternate SCL input locations (V\_SCL)** 设置为
  `Unused`。
- 要在 Take-over Logic 子系统使用来自定子电流限制器的输入，将 **Alternate SCL input locations (V\_SCL)** 设置为
  `Take-over at voltage error`。
- 要在 Take-over Logic1 子系统使用来自定子电流限制器的输入，将 **Alternate SCL input locations (V\_SCL)** 设置为
  `Take-over at voltage regulator output`。

**数据类型：** `single` | `double`

### **V\_SCLuel** — 用于欠励限制器的 Take-over 定子电流限制标量

来自定子电流限制器的输入，用于在使用 take-over 点时防止励磁欠励，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，
  将 **Alternate SCL input locations (V\_SCL)** 设置为
  `Unused`。
- 要在 Take-over Logic 子系统使用来自定子电流限制器的输入，将 **Alternate SCL input locations (V\_SCL)** 设置为
  `Take-over at voltage error`。
- 要在 Take-over Logic1 子系统使用来自定子电流限制器的输入，将 **Alternate SCL input locations (V\_SCL)** 设置为
  `Take-over at voltage regulator output`。

**数据类型：** `single` | `double`

### **Ifd\_pu** — 测量的励磁电流标量

同步电机的测量标幺励磁电流，指定为标量。

**数据类型：** `single` | `double`

### 输出

### **Efd\_pu** — 励磁电压标量

要施加到同步电机励磁电路的标幺励磁电压，以标量形式返回。

**数据类型：** `single` | `double`

## 参数

### 通用

### **Initial field voltage, Efd0 (pu)** — 初始输出电压 `1`（默认）| 实数标量

要施加到同步电机励磁电路的初始标幺电压。

### **Initial terminal voltage, Vt0 (pu)** — 初始端电压 `1`（默认）| 实数标量

要施加到端子的初始标幺电压。

#### 依赖关系

要启用此参数，请在励磁机部分中，将 **Power source selector SW1** 设置为 `Position A: power source derived from terminal voltage`。

### **Initial terminal current, It0 (pu)** — 初始端电流 `1`（默认）| 实数标量

要施加到端子的初始标幺电流。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，将此参数设置为 `-1`。对于离散时间操作，将此参数设置为正整数。对于连续时间操作，将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

### 预控制

### **Resistive component of load compensation, R\_C (pu)** — 补偿电阻 `0`（默认）| 正标量

电流补偿系统中使用的电阻。将此参数和 **Reactance component of load compensation, X\_C (pu)** 设置为 `0` 以禁用电流补偿。

### **Reactance component of load compensation, X\_C (pu)** — 补偿电抗 `0`（默认）| 正标量

电流补偿系统中使用的电抗。将此参数和 **Resistive component of load compensation, R\_C (pu)** 设置为 `0` 以禁用电流补偿。

### **Regulator input filter time constant, T\_R (s)** — 调节器时间常数 `0.01`（默认）| 正标量

电压传感器滤波的等效时间常数。

### 控制

### **Voltage regulator proportional gain, K\_PA (pu)** — 电压调节器比例增益 `30`（默认）

电压调节器的标幺比例增益。

### **Voltage regulator integral time constant, T\_IA (s)** — 电压调节器积分时间常数 `2`（默认）

电压调节器的积分时间常数，以秒为单位。

### **UEL regulator proportional gain, K\_PU (pu)** — UEL 调节器比例增益 `30`（默认）

UEL 调节器的标幺比例增益。

### **UEL regulator integral time constant, T\_IU (s)** — UEL 调节器积分时间常数 `2`（默认）

UEL 调节器的积分时间常数，以秒为单位。

### **Voltage and UEL regulator derivative gain, K\_B (pu)** — 电压和 UEL 调节器微分增益 `3`（默认）

电压调节器和 UEL 调节器的标幺微分增益。

### **Time constant for derivative element, T\_B (s)** — 微分环节时间常数 `0.4`（默认）

微分环节的时间常数，以秒为单位。

### **OEL regulator proportional gain, K\_PO (pu)** — OEL 调节器比例增益 `30`（默认）

OEL 调节器的标幺比例增益。

### **OEL regulator integral time constant, T\_IO (s)** — OEL 调节器积分时间常数 `2`（默认）

OEL 调节器的积分时间常数，以秒为单位。

### **Maximum regulator output, V\_Rmax (pu)** — 最大调节器输出 `20`（默认）| 实数标量

最大标幺调节器输出。

### **Minimum regulator output, V\_Rmin (pu)** — 最小调节器输出 `-20`（默认）| 实数标量

最小标幺调节器输出。

### **Maximum PSS regulator output, V\_RSmax (pu)** — 最大 PSS 调节器输出 `3`（默认）| 实数标量

电力系统稳定器调节器的最大标幺输出。

### **Minimum PSS regulator output, V\_RSmin (pu)** — 最小 PSS 调节器输出 `-3`（默认）| 实数标量

电力系统稳定器调节器的最小标幺输出。

### **Maximum exciter output, V\_Amax (pu)** — 最大励磁机输出 `20`（默认）| 实数标量

励磁系统的最大标幺输出。

### **Minimum exciter output, V\_Amin (pu)** — 最小励磁机输出 `0`（默认）| 实数标量

励磁系统的最小标幺输出。

### **Alternate PSS input locations (V\_S)** — PSS 输入位置 `Output of AVR (after take-over limits)`（默认）| `Voltage error calculation` | `Voltage error or after take-over limits`

电力系统稳定器输入的位置。

### **Alternate OEL input locations (V\_OEL)** — OEL 输入位置 `Take-over at voltage error`（默认）| `Unused` | `Summation point at voltage error` | `Take-over at voltage regulator output`

过励限制器输入的位置，指定为下列选项之一：

- `Summation point at voltage error` — **V\_OEL** 是 **Summation Point Logic** 子系统的输入。
- `Take-over at voltage error` — **V\_OEL** 是 **Take-over Logic** 子系统的输入。
- `Take-over at voltage regulator output` — **V\_OEL** 是 **Take-over Logic 1** 子系统的输入。

### **Alternate UEL input locations (V\_UEL)** — UEL 输入位置 `Take-over at voltage error`（默认）| `Unused` | `Summation point at voltage error` | `Take-over at voltage regulator output`

欠励限制器输入的位置，指定为下列选项之一：

- `Summation point at voltage error` — **V\_UEL** 是 **Summation Point Logic** 子系统的输入。
- `Take-over at voltage error` — **V\_UEL** 是 **Take-over Logic** 子系统的输入。
- `Take-over at voltage regulator output` — **V\_UEL** 是 **Take-over Logic 1** 子系统的输入。

### **Alternate SCL input locations (V\_SCL)** — SCL 输入位置 `Take-over at voltage error`（默认）| `Unused` | `Summation point at voltage error` | `Take-over at voltage regulator output`

定子电流限制器输入的位置，指定为下列选项之一：

- `Summation point` — 使用 **V\_SCLsum** 输入端口。
- 任意 `Take-over` 选项 — 使用 **V\_OELscl** 和 **V\_UELscl** 输入端口。

### 励磁机

### **Exciter field proportional constant, K\_E (pu)** — 励磁机励磁增益 `1`（默认）| 正标量

励磁机励磁的比例常数。

### **Exciter field time constant, T\_E (s)** — 励磁机励磁时间常数 `0.4`（默认）| 正标量

励磁机励磁的时间常数。

### **Rectifier loading factor proportional to commutating reactance, K\_C (pu)** — 整流器负载因子 `0.173`（默认）| 正标量

整流器负载因子。此值与换相电抗成比例。

### **Demagnetizing factor, function of exciter alternator reactances, K\_D (pu)** — 去磁因子 `1`（默认）| 正标量

与励磁机交流发电机电抗相关的去磁因子。

### **Exciter output voltage for saturation factor S\_E(E\_1), E\_1 (pu)** — 第一饱和输出电压 `7.4`（默认）| 正标量

第一饱和因子的励磁机输出电压。

### **Exciter saturation factor at exciter output voltage E\_1, S\_E(E\_1) (1)** — 第一饱和查找电压 `0.214`（默认）| 正标量

第一励磁机的饱和因子。

### **Exciter output voltage for saturation factor S\_E(E\_2), E\_2 (pu)** — 第二饱和输出电压 `5.55`（默认）| 正标量

第二饱和因子的励磁机输出电压。

### **Exciter saturation factor at exciter output voltage E\_2, S\_E(E\_2) (1)** — 第二饱和查找电压 `0.044`（默认）| 正标量

第二励磁机的饱和因子。

### **Maximum exciter field current, V\_FEmax (pu)** — 励磁机上限 `20`（默认）| 实数标量

最大标幺励磁电流限制参考值。

### **Minimum exciter output limit, V\_Emin (pu)** — 励磁机下限 `0`（默认）| 实数标量

最小标幺励磁机电压输出。

### **Potential circuit (voltage) gain coefficient, K\_P (pu)** — 电势电路增益系数 `1`（默认）| 实数标量

标幺电势电路增益系数。

#### 依赖关系

要启用此参数，请将 **Power source selector SW1** 设置为 `Position A: power source derived from terminal voltage`。

### **Potential circuit phase angle (degrees)** — 电势电路相位角 `0`（默认）| 实数标量

电势电路相位角，以度为单位。

#### 依赖关系

要启用此参数，请将 **Power source selector SW1** 设置为 `Position A: power source derived from terminal voltage`。

### **Potential circuit (current) gain coefficient, K\_I (pu)** — 电势电路电流增益系数 `0`（默认）| 实数标量

标幺电势电路电流增益系数。

#### 依赖关系

要启用此参数，请将 **Power source selector SW1** 设置为 `Position A: power source derived from terminal voltage`。

### **Reactance associated with potential source, X\_L (pu)** — 与电势源相关的电抗 `0`（默认）| 实数标量

与电势源相关的标幺电抗。

#### 依赖关系

要启用此参数，请将 **Power source selector SW1** 设置为 `Position A: power source derived from terminal voltage`。

### **Rectifier loading factor proportional to commutating reactance, K\_C1 (pu)** — 与换相电抗成比例的整流器负载因子 `0`（默认）| 实数标量

整流器的标幺负载因子。此值与换相电抗成比例。

### **Power source selector SW1** — 电源选择器 `Position B: power source independent of the terminal conditions`（默认）| `Position A: power source derived from terminal voltage`

电源选择器 SW1 的位置。

### **Maximum available exciter voltage, V\_B1max (pu)** — 最大可用励磁机磁场电压 `1.5`（默认）| 实数标量

励磁机最大可用标幺磁场电压。

### **Rectifier loading factor proportional to commutating reactance, K\_C2 (pu)** — 与换相电抗成比例的整流器负载因子 `0`（默认）| 实数标量

整流器的标幺负载因子。此值与换相电抗成比例，通过单独串联二极管桥从发电机端电流导出。

### **Additive potential circuit (current) gain coefficient, K\_I2 (pu)** — 附加电路电流增益系数 `0`（默认）| 实数标量

从发电机端电流通过单独串联二极管桥导出的标幺附加电路电流增益系数。将此参数设置为 `0` 可完全禁用单独的附加电源。

### **最大可用励磁机电压，V\_B2max (pu)** — 最大可用励磁机电压 `0` (默认) | real scalar

用于励磁机的最大标幺可用励磁电压，通过单独的串联二极管桥从发电机
端子电流导出。

### **附加独立源，K\_BOOST (pu)** — 附加独立源 `0` (默认)

用于升压电路的标幺附加独立源。

### **用于投入附加（升压）电路的参考值，V\_BOOST (pu)** — 用于投入升压电路的参考值 `0` (默认)

用于在励磁系统中激活附加升压电路的标幺参考值。

## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

离散时间或连续时间同步电机 AC11C 励磁系统，包括自动电压调节器和励磁机

SM AC11C 模块实现了一个符合 IEEE Std 421.5-2016 [1] 的同步电机 AC11C 型励磁系统模型。

使用此模块对作为发电机运行且使用交流旋转励磁机的同步电机的励磁电压的控制和调节进行建模。

通过使用 **采样时间（-1 表示继承）** 参数，可在模块的连续实现和离散实现之间切换。要将积分器配置为连续时间，请将 **采样时间（-1 表示继承）** 参数设置为 `0`。要将积分器配置为离散时间，请将 **采样时间（-1 表示继承）** 参数设置为正标量。要从上游模块继承采样时间，请将 **采样时间（-1 表示继承）** 参数设置为 `-1`。

SM AC11C 模块包含五个主要组件：

- 电流补偿器组件根据端子电流修改测得的端子电压。
- 电压测量变送器组件使用低通滤波器模拟端子电压变送器的动态特性。
- 励磁控制元件组件将电压变送器输出与端子电压参考进行比较，以产生电压误差值。然后该组件将此值通过电压调节器以产生励磁机励磁电压。
- 交流旋转励磁机组件对交流旋转励磁机进行建模，该励磁机产生施加到受控同步电机的励磁电压。该模块还会将励磁机励磁电流 (*VFE*) 反馈到励磁系统。
- 电源组件对受控整流器电源对端子电压的依赖性进行建模。电源包含多个复合电路。您可以选择此附加电路作为升压电路，当系统中的故障条件导致发电机端子电压下降时投入该电路。然后，当发电机电压恢复时，SM AC11C 模块会释放该电路。

此图显示了 AC11C 励磁系统模型的结构：

图中：

- *VT* 和 *IT* 分别是同步电机的测得端子电压和电流。
- *VC1* 是经过电流补偿的端子电压。
- *VC* 是经过滤波、电流补偿后的端子电压。
- *VREF* 是参考端子电压。
- *VS* 是电力系统稳定器电压。
- *SW1* 是您为受控整流器指定的电源开关。
- *VB* 是励磁机励磁电压。
- *EFE* 和 *VFE* 分别是励磁机励磁电压和电流。
- *EFD* 和 *IFD* 分别是励磁电压和电流。

### 电流补偿器和电压测量变送器

该模块使用以下方程对电流补偿器进行建模：

VC1=VT+ITRC2+XC2,

其中：

- *RC* 是负载补偿电阻。
- *XC* 是负载补偿电抗。

该模块使用时间常数为 *TR* 的 Low-Pass Filter 模块实现电压测量变送器。有关精确的离散和连续实现的信息，请参阅 Low-Pass Filter 模块的文档。

### 励磁控制元件

此图显示了励磁控制元件的结构：

图中：

- Summation Point Logic 子系统对过励限制器 (OEL)、欠励限制器 (UEL) 和定子电流限制器 (SCL) 的求和点输入位置进行建模。有关将限制器与此模块一起使用的详细信息，请参阅励磁电流限制器。
- 有两个 Take-over Logic 子系统。它们对 OEL、UEL 和 SCL 电压的接管点输入位置进行建模。有关将限制器与此模块一起使用的详细信息，请参阅励磁电流限制器。
- SM AC11C 模块使用三种不同的 PID 控制对自动电压调节器的控制器进行建模。特定限制器（UEL 或 OEL）的激活会立即将自动电压调节器的传递函数更改为与已激活限制器相对应的控制器路径。当 *VUEL* 和/或 *VOEL* 信号连接到各自的备用位置时，SW\_UEL 和 SW\_OEL Switch 模块会激活相应的控制路径。当您将 **备用 UEL 输入位置 (V\_UEL)** 和 **备用 OEL 输入位置 (V\_OEL)** 参数设置为 `Take-over at voltage error` 时，SW\_UEL 和 SW\_OEL Switch 模块位于位置 B。
- **电源选择器 SW1** 参数控制受控整流器电源的来源。电源包含一个升压电路，当系统中的故障条件导致发电机端子电压下降时，您可以投入该电路。然后，电压调节器指令信号 *VR* 与励磁机励磁电压 *VB1* 和 *VB2* 相加和/或相乘。有关受控整流器电源的逻辑开关的详细信息，请参阅电源和升压电路。

### 励磁电流限制器

您可以使用不同类型的励磁电流限制器，在不安全的运行条件下修改电压调节器的输出：

- 使用过励限制器防止因励磁电流需求过大而导致励磁绕组过热。
- 使用欠励限制器在励磁过低时提升励磁，过低会有失步风险。
- 使用定子电流限制器防止因电流过大而导致定子绕组过热。

将这些限制器中任意一个的输出连接到以下点之一：

- 求和点 — 将限制器用作自动电压调节器 (AVR) 反馈回路的一部分。
- 接管点 — 覆盖 AVR 的通常行为。

如果在求和点使用定子电流限制器，请使用输入 *VSCLsum*。如果在接管点使用定子电流限制器，请使用过励输入 *VOELscl* 和欠励输入 *VUELscl*。

### 交流旋转励磁机

此图显示了交流旋转励磁机的结构：

图中：

- 励磁机励磁电流 *VFE* 是三个信号之和：

  - 非线性函数 *Vx* 对励磁机输出电压的饱和进行建模。
  - 比例项 *KE* 对励磁机输出电压与励磁机励磁电流之间的线性关系进行建模。
  - 该子系统使用反馈回路中的去磁常数 *KD* 对负载电流对励磁机输出电压的去磁效应进行建模。
- Integrator with variable limits 子系统对 *EFE* 和 *VFE* 之间的差值进行积分，以生成励磁机交流发电机输出电压 *VE*。*TE* 是此过程的时间常数。
- 非线性函数 *FEX* 对由整流器调节引起的励磁机输出电压降进行建模。此函数取决于常数 *KC*，而 *KC* 本身是换向电抗的函数。
- 参数 *VEmin* 和 *VFEmax* 对旋转励磁机的下限和上限进行建模。

### 电源和升压电路

您可以通过设置 **电源选择器 SW1** 参数值，为受控整流器使用不同的电源表示。要从端子电压导出受控整流器的电源，请将 **电源选择器 SW1** 参数设置为 `Position A: power source derived from terminal voltage`。要指定电源独立于端子电压，请将 **电源选择器 SW1** 参数设置为 `Position B: power source independent from the terminal conditions`。

电源部分还包含一个附加电路，您可以将其用作升压电路。当系统中的故障条件导致发电机端子电压下降时，会投入此附加电路。SW\_Boost Switch 模块控制与升压电路相关的逻辑。如果端子电压 *VT* 大于 **用于投入附加（升压）电路的参考值，V\_BOOST (pu)** 参数的值，则开关位于位置 “A”，否则开关位于位置 “B”。

如果您将 **用于投入附加（升压）电路的参考值，V\_BOOST (pu)** 参数设置为高值，则附加组件始终处于有效状态。
