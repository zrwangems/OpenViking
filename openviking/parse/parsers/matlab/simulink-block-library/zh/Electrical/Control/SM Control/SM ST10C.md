---
type: simulink-block
title: 'SM ST10C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smst10c'
documentation_source_path: 'ref/smst10c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM ST10C

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

- 要忽略来自过励限制器的输入，请将 **Alternate OEL input locations
  (V\_OEL)** 设置为
  `Unused`。
- 要在求和点使用来自过励限制器的输入，请将 **Alternate OEL input
  locations (V\_OEL)** 设置为
  `Summation point at voltage
  error`。
- 要在 Take-over Logic 子系统使用来自过励限制器的输入，请将 **Alternate
  OEL input locations (V\_OEL)** 设置为
  `Take-over at voltage
  error`。
- 要在 Take-over Logic1 子系统使用来自过励限制器的输入，请将 **Alternate
  OEL input locations (V\_OEL)** 设置为
  `Take-over at voltage regulator
  output`。

**数据类型：** `single` | `double`

### **V\_UEL** — 欠励限制信号标量

来自欠励限制器的输入，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自欠励限制器的输入，请将 **Alternate UEL input locations
  (V\_UEL)** 设置为
  `Unused`。
- 要在求和点使用来自欠励限制器的输入，请将 **Alternate UEL input
  locations (V\_UEL)** 设置为
  `Summation point at voltage
  error`。
- 要在 Take-over Logic 子系统使用来自欠励限制器的输入，请将 **Alternate
  UEL input locations (V\_UEL)** 设置为
  `Take-over at voltage
  error`。
- 要在 Take-over Logic1 子系统使用来自欠励限制器的输入，请将 **Alternate
  UEL input locations (V\_UEL)** 设置为
  `Take-over at voltage regulator
  output`。

**数据类型：** `single` | `double`

### **V\_SCLsum** — 求和点定子电流限制信号标量

使用求和点时来自定子电流限制器的输入，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations
  (V\_SCL)** 设置为
  `Unused`。
- 要在求和点使用来自定子电流限制器的输入，请将 **Alternate SCL input
  locations (V\_SCL)** 设置为
  `Summation point at voltage
  error`。

**数据类型：** `single` | `double`

### **V\_SCLoel** — 过励限制器接管定子电流限制标量

使用接管点时来自定子电流限制器的输入，用于防止励磁过励，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations
  (V\_SCL)** 设置为
  `Unused`。
- 要在 Take-over Logic 子系统使用来自定子电流限制器的输入，请将 **Alternate
  SCL input locations (V\_SCL)** 设置为
  `Take-over at voltage
  error`。
- 要在 Take-over Logic1 子系统使用来自定子电流限制器的输入，请将 **Alternate
  SCL input locations (V\_SCL)** 设置为
  `Take-over at voltage regulator
  output`。

**数据类型：** `single` | `double`

### **V\_SCLuel** — 欠励限制器接管定子电流限制标量

使用接管点时来自定子电流限制器的输入，用于防止励磁欠励，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations
  (V\_SCL)** 设置为
  `Unused`。
- 要在 Take-over Logic 子系统使用来自定子电流限制器的输入，请将 **Alternate
  SCL input locations (V\_SCL)** 设置为
  `Take-over at voltage
  error`。
- 要在 Take-over Logic1 子系统使用来自定子电流限制器的输入，请将 **Alternate
  SCL input locations (V\_SCL)** 设置为
  `Take-over at voltage regulator
  output`。

**数据类型：** `single` | `double`

### **Ifd\_pu** — 测量的励磁电流标量

同步电机的测量标幺励磁电流，指定为标量。

**数据类型：** `single` | `double`
### 输出

### **Efd\_pu** — 励磁电压标量

施加到同步电机励磁绕组的标幺励磁电压，以标量形式返回。

**数据类型：** `single` | `double`

## 参数

### 常规

### **Initial field voltage, Efd0 (pu)** — 初始输出电压 `1`（默认）| 实数标量

施加到同步电机励磁绕组的初始标幺电压。

### **Initial terminal voltage, Vt0 (pu)** — 初始机端电压 `1`（默认）| 实数标量

施加到机端的初始标幺电压。

#### 依赖关系

要启用此参数，请在 Exciter 部分将 **Power source selector** 设置为
`Position A: power source derived from generator
terminal voltage`。

### **Initial terminal current, It0 (pu)** — 初始机端电流 `1`（默认）| 实数标量

施加到机端的初始标幺电流。

#### 依赖关系

要启用此参数，请在 Exciter 部分将 **Power source selector** 设置为
`Position A: power source derived from generator
terminal voltage`。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。
有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请将此参数设置为 `-1`。
对于离散时间操作，请将此参数设置为正整数。对于连续时间操作，请将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

### 预控制

### **Resistive component of load compensation, R\_C (pu)** — 补偿电阻 `0`（默认）| 正标量

电流补偿系统中使用的电阻。将此参数和 **Reactance component of load compensation, X\_C
(pu)** 设置为 `0` 以禁用电流补偿。

### **Reactance component of load compensation, X\_C (pu)** — 补偿电抗 `0`（默认）| 正标量

电流补偿系统中使用的电抗。将此参数和 **Resistive component of load compensation, R\_C
(pu)** 设置为 `0` 以禁用电流补偿。

### **Regulator input filter time constant, T\_R (s)** — 调节器时间常数 `0.01`（默认）| 正标量

电压传感器滤波的等效时间常数。

### 控制

### **Regulator gain, K\_R (pu)** — 调节器增益 `500`（默认）| 正标量

调节器的增益。

### **Voltage regulator denominator (lag) time constant 1, T\_B1 (s)** — 调节器滞后时间常数 1 `12.5`（默认）| 正标量

电压调节器第二个 Lead-Lag (Discrete or Continuous) 模块中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **Voltage regulator numerator (lead) time constant 1, T\_C1 (s)** — 调节器超前时间常数 1 `1.5`（默认）| 正标量

电压调节器第二个 Lead-Lag (Discrete or Continuous) 模块中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **Voltage regulator denominator (lag) time constant 2, T\_B2 (s)** — 调节器滞后时间常数 2 `0.1`（默认）| 正标量

电压调节器第一个 Lead-Lag (Discrete or Continuous) 模块中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **Voltage regulator numerator (lead) time constant 2, T\_C2 (s)** — 调节器超前时间常数 2 `0.1`（默认）| 正标量

电压调节器第一个 Lead-Lag (Discrete or Continuous) 模块中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **UEL regulator denominator (lag) time constant 1, T\_UB1 (s)** — UEL 调节器滞后时间常数 1 `12.5`（默认）

欠励限制器调节器第二个 Lead-Lag (Discrete or Continuous) 模块中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **UEL regulator numerator (lead) time constant 1, T\_UC1 (s)** — UEL 调节器超前时间常数 1 `1.5`（默认）

欠励限制器调节器第二个 Lead-Lag (Discrete or Continuous) 模块中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **UEL regulator denominator (lag) time constant 2, T\_UB2 (s)** — UEL 调节器滞后时间常数 2 `0.1`（默认）

欠励限制器调节器第一个 Lead-Lag (Discrete or Continuous) 模块中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **UEL regulator numerator (lead) time constant 2, T\_UC2 (s)** — UEL 调节器超前时间常数 2 `0.1`（默认）

欠励限制器调节器第一个 Lead-Lag (Discrete or Continuous) 模块中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **OEL regulator denominator (lag) time constant 1, T\_OB1 (s)** — OEL 调节器滞后时间常数 1 `12.5`（默认）

过励限制器调节器第二个 Lead-Lag (Discrete or Continuous) 模块中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **OEL regulator numerator (lead) time constant 1, T\_OC1 (s)** — OEL 调节器超前时间常数 1 `1.5`（默认）

过励限制器调节器第二个 Lead-Lag (Discrete or Continuous) 模块中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **OEL regulator denominator (lag) time constant 2, T\_OB2 (s)** — OEL 调节器滞后时间常数 2 `0.1`（默认）

过励限制器调节器第一个 Lead-Lag (Discrete or Continuous) 模块中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **OEL regulator numerator (lead) time constant 2, T\_OC2 (s)** — OEL 调节器超前时间常数 2 `0.1`（默认）

过励限制器调节器第一个 Lead-Lag (Discrete or Continuous) 模块中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **Maximum regulator output, V\_Rmax (pu)** — 最大调节器输出 `10`（默认）| 实数标量

最大标幺调节器输出。

### **Minimum regulator output, V\_Rmin (pu)** — 最小调节器输出 `-8.7`（默认）| 实数标量

最小标幺调节器输出。

### **Maximum PSS regulator output, V\_RSmax (pu)** — 最大 PSS 调节器输出 `5`（默认）| 实数标量

电力系统稳定器调节器的最大标幺输出。

### **Minimum PSS regulator output, V\_RSmin (pu)** — 最小 PSS 调节器输出 `-5`（默认）| 实数标量

电力系统稳定器调节器的最小标幺输出。

### **Alternate PSS input locations (V\_S)** — PSS 输入位置 `Summation point at output of AVR`（默认）| `Summation point at voltage error calculation` | `Summation point at voltage error or take-over limits`

电力系统稳定器输入的位置。

### **Alternate OEL input locations (V\_OEL)** — OEL 输入位置 `Summation point at voltage error`（默认）| `Unused` | `Take-over at voltage error` | `Take-over at voltage regulator output`

过励限制器输入的位置，指定为以下选项之一：

- `Summation point at voltage
  error` — **V\_OEL** 是 **Summation Point Logic**
  子系统的输入。
- `Take-over at voltage error` —
  **V\_OEL** 是 **Take-over Logic** 子系统的输入。
- `Take-over at voltage regulator
  output` — **V\_OEL** 是 **Take-over Logic 1**
  子系统的输入。

### **Alternate UEL input locations (V\_UEL)** — UEL 输入位置 `Summation point at voltage error`（默认）| `Unused` | `Take-over at voltage error` | `Take-over at voltage regulator output`

欠励限制器输入的位置，指定为以下选项之一：

- `Summation point at voltage
  error` — **V\_UEL** 是 **Summation Point Logic**
  子系统的输入。
- `Take-over at voltage error` —
  **V\_UEL** 是 **Take-over Logic** 子系统的输入。
- `Take-over at voltage regulator
  output` — **V\_UEL** 是 **Take-over Logic 1**
  子系统的输入。

### **Alternate SCL input locations (V\_SCL)** — SCL 输入位置 `Summation point at voltage error`（默认）| `Unused` | `Take-over at voltage error` | `Take-over at voltage regulator output`

定子电流限制器输入的位置，指定为以下选项之一：

- `Summation point` — 使用 **V\_SCLsum** 输入端口。
- 任意 `Take-over` 选项 —
  使用 **V\_OELscl** 和 **V\_UELscl** 输入端口。

### 励磁机

### **Rectifier loading factor proportional to commutating reactance, K\_C (pu)** — 整流器负载系数 `0.01`（默认）| 正标量

整流器负载系数。此值与换相电抗成正比。

### **Equivalent time constant for rectifier bridge, T\_1 (s)** — 整流器桥时间常数 `0.004`（默认）| 正标量

整流器桥的等效时间常数，以秒为单位。

### **Potential circuit (voltage) gain coefficient, K\_P (pu)** — 电位电路电压增益系数 `1`（默认）| 正标量

电源电路中每单位电压增益系数。

### **Potential circuit (current) gain coefficient, K\_I (pu)** — 电位电路电流增益系数 `0`（默认）| 正标量

电源电路中每单位电流增益系数。

#### 依赖关系

要启用此参数，请将 **Power source selector** 设置为 `Position A: power source
derived from generator terminal voltage`。

### **Reactance associated with the potential source, X\_L (pu)** — 电位源电抗 `0`（默认）| 正标量

电位源中的每单位电抗。

#### 依赖关系

要启用此参数，请将 **Power source selector** 设置为 `Position A: power source
derived from generator terminal voltage`。

### **Potential circuit phase angle (degrees)** — 电位电路相位角 `0`（默认）| 正标量

电源电路的相位角，以度为单位。

#### 依赖关系

要启用此参数，请将 **Power source selector** 设置为 `Position A: power source
derived from generator terminal voltage`。

### **Maximum available exciter voltage, V\_Bmax (pu)** — 励磁机电压上限 `1.5`（默认）| 正标量

最大每单位可用励磁机电压值。

### **Power source selector** — 电源选择器 `Position A: power source derived from generator terminal voltage`（默认）| `Position B: power source independent of generator terminal conditions`

电源选择器的位置。

## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

具有自动电压调节器的离散时间或连续时间同步电机 ST10C 静态励磁系统

SM ST10C 模块实现了符合 IEEE Std 421.5-2016 [1] 的同步电机型 ST10C 静态励磁系统模型。

使用此模块对同步电机励磁电压的控制和调节进行建模。

通过使用 **Sample time (-1 for inherited)** 参数在模块的连续和离散实现之间切换。要将积分器配置为连续时间，请将 **Sample time (-1 for inherited)** 参数设置为 `0`。要将积分器配置为离散时间，请将 **Sample time (-1 for inherited)** 参数设置为正标量。要从上游模块继承采样时间，请将 **Sample time (-1 for inherited)** 参数设置为 `-1`。

SM ST10C 模块包含四个主要组件：

- 电流补偿器组件根据端子电流修改测量的端子电压。
- 电压测量传感器组件使用低通滤波器模拟端子电压传感器的动态特性。
- 励磁控制元件组件将电压传感器输出与端子电压参考值进行比较，以产生电压误差值。该组件随后将此值通过电压调节器以产生励磁电压。
- 电源组件对受控整流器的电源进行建模，当该电源独立于端子电压时使用。

此图显示了 ST10C 励磁系统模型的结构：

图中：

- *VT* 和 *IT* 分别是同步电机的测量端子电压和电流。
- *VC1* 是电流补偿后的端子电压。
- *VC* 是滤波后的电流补偿端子电压。
- *VREF* 是参考端子电压。
- *VS* 是电力系统稳定器电压。
- *VB* 是励磁机励磁电压。
- *EFD* 和 *IFD* 分别是励磁电压和电流。

### 电流补偿器和电压测量传感器

该模块使用以下方程对电流补偿器进行建模：

VC1=VT+ITRC2+XC2，

其中：

- *RC* 是负载补偿电阻。
- *XC* 是负载补偿电抗。

该模块将电压测量传感器实现为具有时间常数 *TR* 的低通滤波器模块。有关精确的离散和连续实现的信息，请参阅低通滤波器模块的文档。

### 励磁控制元件

此图显示了励磁控制元件的结构：

图中：

- 求和点逻辑子系统对过励限制器（OEL）、欠励限制器（UEL）和定子电流限制器（SCL）的求和点输入位置进行建模。有关在此模块中使用限制器的更多信息，请参阅励磁电流限制器。
- 有两个切换逻辑子系统。它们对 OEL、UEL 和 SCL 电压的切换点输入位置进行建模。有关在此模块中使用限制器的更多信息，请参阅励磁电流限制器。
- 超前-滞后（离散或连续）模块的并联配置在限制器激活时提供独立的控制设置。该模型提供一个公共增益因子 *KR* 和两个超前-滞后（离散或连续）模块，分别用于 AVR 以及欠励和过励限制器。当 *VUEL* 和/或 *VOEL* 信号连接到各自的备用位置时，SW\_UEL 和 SW\_OEL 开关模块激活相应的控制路径。当您将 **Alternate UEL input locations (V\_UEL)** 和 **Alternate OEL input locations (V\_OEL)** 参数设置为 `Take-over at voltage error` 时，SW\_UEL 和 SW\_OEL 开关模块处于位置 B。
- 每个控制路径中的两个超前-滞后模块对与电压调节器以及欠励和过励限制器相关的附加动态进行建模。每个相应路径中的第一个超前-滞后模块表示瞬态增益减小，其中 *TC2*（或 *TUC2* 和 *TOC2*）是超前时间常数，*TB2*（或 *TUB2* 和 *TOB2*）是滞后时间常数。第二个超前-滞后模块允许表示瞬态增益增加的可能性，其中 *TC1*（或 *TUC1* 和 *TOC1*）是超前时间常数，*TB1*（或 *TUB1* 和 *TOB1*）是滞后时间常数。有关离散和连续实现的信息，请参阅超前-滞后模块的文档。
- SM ST10C 模块还提供在第一个切换逻辑子系统之后的 AVR 求和点处或在门结构输出处通过单独路径（模型中的底部路径）施加 PSS 信号的选项。此单独路径包含与主求和点路径相同的控制元件。
- **Power source selector** 参数控制受控整流器电源的来源。该子系统将电压调节器指令信号 *VR* 乘以励磁机励磁电压 *VB*。有关受控整流器电源逻辑开关的更多信息，请参阅电源。

### 励磁电流限制器

您可以使用不同类型的励磁电流限制器在不安全运行条件下修改电压调节器的输出：

- 使用过励限制器防止因过大的励磁电流需求导致励磁绕组过热。
- 使用欠励限制器在励磁过低时提升励磁，否则存在失步风险。
- 使用定子电流限制器防止因过大电流导致定子绕组过热。

将任何这些限制器的输出连接到以下位置之一：

- 求和点 — 将限制器用作自动电压调节器（AVR）反馈回路的一部分。
- 切换点 — 覆盖 AVR 的常规行为。

如果您在求和点使用定子电流限制器，请使用输入 *VSCLsum*。如果您在切换点使用定子电流限制器，请使用过励输入 *VSCLoel* 和欠励输入 *VSCLuel*。

### 电源

您可以通过设置 **Power source selector** 参数值来使用不同的受控整流器电源表示。要从端子电压导出受控整流器的电源，请将 **Power source selector** 参数设置为 `Position A: power source derived from generator terminal voltage`。要指定电源独立于端子电压，请将 **Power source selector** 参数设置为 `Position B: power source independent of generator terminal conditions`。

此图显示了利用端子电压 *VT* 和端子电流 *IT* 的相量组合的励磁机电源模型：
