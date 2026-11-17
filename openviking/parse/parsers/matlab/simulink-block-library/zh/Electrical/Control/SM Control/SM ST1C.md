---
type: simulink-block
title: 'SM ST1C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smst1c'
documentation_source_path: 'ref/smst1c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM ST1C

## 端口

### 输入

### **V\_REF** — 电压参考值标量

电压调节器参考设定值，采用标幺值表示，指定为标量。

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
  `Summation point`。
- 要在接管点使用来自过励限制器的输入，请将 **Alternate OEL input
  locations (V\_OEL)** 设置为
  `Take-over`。

**数据类型：** `single` | `double`

### **V\_UEL** — 欠励限制信号标量

来自欠励限制器的输入，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自欠励限制器的输入，请将 **Alternate UEL input locations
  (V\_UEL)** 设置为
  `Unused`。
- 要在求和点使用来自欠励限制器的输入，请将 **Alternate UEL input
  locations (V\_UEL)** 设置为
  `Summation point`。
- 要在接管点使用来自欠励限制器的输入，请将 **Alternate UEL input
  locations (V\_UEL)** 设置为
  `Take-over`。

**数据类型：** `single` | `double`

### **V\_SCLsum** — 求和点定子电流限制信号标量

使用求和点时来自定子电流限制器的输入，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations
  (V\_SCL)** 设置为
  `Unused`。
- 要在求和点使用来自定子电流限制器的输入，请将 **Alternate SCL input
  locations** 设置为 `Summation
  point`。

**数据类型：** `single` | `double`

### **V\_SCLoel** — 接管定子电流限制（OEL）标量

使用接管点时来自定子电流限制器的输入，用于防止励磁过励，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations
  (V\_SCL)** 设置为
  `Unused`。
- 要在接管点使用来自定子电流限制器的输入，请将 **Alternate SCL input
  locations (V\_SCL)** 设置为
  `Take-over`。

**数据类型：** `single` | `double`

### **V\_SCLuel** — 接管定子电流限制（UEL）标量

使用接管点时来自定子电流限制器的输入，用于防止励磁欠励，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations
  (V\_SCL)** 设置为
  `Unused`。
- 要在接管点使用来自定子电流限制器的输入，请将 **Alternate SCL input
  locations (V\_SCL)** 设置为
  `Take-over`。

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

### **Initial field voltage, Efd0 (pu)** — 初始输出电压 `1`（默认）| 实数

施加到同步电机励磁绕组的初始标幺电压。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请将此参数设置为 `-1`。对于离散时间操作，请将此参数设置为正整数。对于连续时间操作，请将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保在模块的连续和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

### 预控制

### **Resistive component of load compensation, R\_C (pu)** — 补偿电阻 `0`（默认）| 正数

电流补偿系统中使用的电阻。将此参数和 **Reactance component of load compensation, X\_C
(pu)** 设置为 `0` 以禁用电流补偿。

### **Reactance component of load compensation, X\_C (pu)** — 补偿电抗 `0`（默认）| 正数

电流补偿系统中使用的电抗。将此参数和 **Resistive component of load compensation, R\_C
(pu)** 设置为 `0` 以禁用电流补偿。

### **Regulator input filter time constant, T\_R (s)** — 调节器时间常数 `0.02`（默认）| 正数

电压变送器滤波的等效时间常数。

### 控制

### **Regulator output gain, K\_A (pu)** — 调节器增益 `210`（默认）| 正数

与电压调节器相关的增益。

### **Regulator output time constant, T\_A (s)** — 调节器时间常数 `0`（默认）| 正数

电压调节器的主要时间常数。

### **Regulator denominator (lag) time constant, T\_B (s)** — 第一个超前-滞后环节的调节器滞后时间常数 `1`（默认）| 正数

电压调节器中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **Regulator numerator (lead) time constant, T\_C (s)** — 第一个超前-滞后环节的调节器超前时间常数 `1`（默认）| 正数

电压调节器中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **Regulator denominator (lag) time constant, T\_B 1(s)** — 第二个超前-滞后环节的调节器滞后时间常数 `0`（默认）| 正数

电压调节器中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **Regulator numerator (lead) time constant, T\_C1 (s)** — 第二个超前-滞后环节的调节器超前时间常数 `0`（默认）| 正数

电压调节器中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **Rate feedback gain, K\_F (pu)** — 速率反馈增益 `0`（默认）| 正数

速率反馈环节增益。

### **Rate feedback time constant, T\_F (s)** — 速率反馈时间常数 `1`（默认）| 正数

速率反馈环节的时间常数。

### **Maximum regulator output, V\_Amax (pu)** — 调节器输出上限 `6.43`（默认）| 实数

调节器的最大标幺输出电压。

### **Minimum regulator output, V\_Amin (pu)** — 调节器输出下限 `-6`（默认）| 实数

调节器的最小标幺输出电压。

### **Maximum voltage error (regulator input), V\_Imax (pu)** — 电压上限 `99`（默认）| 实数

作为调节器输入的最大标幺电压。

### **Minimum voltage error (regulator input), V\_Imin (pu)** — 电压下限 `-99`（默认）| 实数

作为调节器输入的最小标幺电压。

### **Alternate PSS input locations (V\_S)** — PSS 输入位置 `Summation point at voltage error`（默认）| `Summation point at voltage regulator output`

电力系统稳定器输入位置。

### **Alternate OEL input locations (V\_OEL)** — OEL 输入位置 `Unused`（默认）| `Summation point at voltage error` | `Take-over at voltage error` | `Take-over at voltage regulator output`

过励限制器输入位置：

- 如果选择 `Summation point at voltage
  error`，则 **V\_OEL** 是 Summation Point Logic 子系统的输入。
- 如果选择 `Take-over at voltage
  error`，则 **V\_OEL** 是 Take-over Logic 子系统的输入。
- 如果选择 `Take-over at voltage regulator
  output`，则 **V\_OEL** 是 Take-over Logic 1 子系统的输入。

### **Alternate UEL input locations (V\_UEL)** — UEL 输入位置 `Unused`（默认）| `Summation point at voltage error` | `Take-over at voltage error` | `Take-over at voltage regulator output`

欠励限制器输入位置：

- 如果选择 `Summation point at voltage
  error`，则 **V\_UEL** 是 Summation Point Logic 子系统的输入。
- 如果选择 `Take-over at voltage
  error`，则 **V\_UEL** 是 Take-over Logic 子系统的输入。
- 如果选择 `Take-over at voltage regulator
  output`，则 **V\_UEL** 是 Take-over Logic 1 子系统的输入。

### **Alternate SCL input locations (V\_SCL)** — SCL 输入位置 `Unused`（默认）| `Summation point at voltage error` | `Take-over at voltage error` | `Take-over at voltage regulator output`

定子电流限制器输入位置：

- 如果选择 `Summation point`，请使用 **V\_SCLsum** 输入端口。
- 如果选择任何 `Take-over` 选项，请使用 **V\_SCLoel** 和 **V\_SCLuel** 输入端口。

### 励磁机

### **Rectifier loading factor proportional to commutating reactance, K\_C (pu)** — 整流器负载系数 `0.038`（默认）| 正数

与换相电抗成比例的整流器负载系数。

### **Exciter output current limiter gain, K\_LR (pu)** — 励磁机输出电流限制器增益 `4.54`（默认）| 实数

最大标幺励磁机电流限制器增益。

### **Exciter output current limit reference, I\_LR (pu)** — 励磁机输出电流限制参考值 `4.4`（默认）| 实数

标幺励磁机电流限制参考值。

### **Maximum exciter output, V\_Rmax (pu)** — 励磁机上限 `6.43`（默认）| 实数

最大标幺励磁机电压输出。

### **Minimum exciter output, V\_Rmin (pu)** — 励磁机下限 `-6`（默认）| 实数

最小标幺励磁机电压输出。

## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

具有自动电压调节器的离散时间或连续时间同步电机 ST1C 静态励磁系统

SM ST1C 模块实现了符合 IEEE 421.5-2016[1] 的同步电机型 ST1C 静态励磁系统模型。

使用此模块对同步电机励磁电压的控制和调节进行建模。

您可以使用 **Sample time (-1 for inherited)** 参数在模块的连续和离散实现之间切换。要将积分器配置为连续时间，请将 **Sample time (-1 for
inherited)** 属性设置为 `0`。要将积分器配置为离散时间，请将 **Sample time (-1 for inherited)** 属性设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。

SM ST1C 模块包含三个主要组件：

- 电流补偿器根据机端电流修改测量的机端电压。
- 电压测量变送器使用低通滤波器模拟机端电压变送器的动态特性。
- 励磁控制元件组件将电压变送器输出与机端电压参考值进行比较，以产生电压误差。该电压误差随后通过电压调节器产生励磁电压。

下图显示了 ST1C 励磁系统模型的整体结构：

图中：

- *VT* 和
  *IT* 是同步电机的测量
  机端电压和电流。
- *VC1* 是电流补偿后的
  机端电压。
- *VC* 是滤波后的、
  电流补偿后的机端电压。
- *VREF* 是参考机端
  电压。
- *VS* 是电力系统
  稳定器电压。
- *EFD* 和
  *IFD* 分别是励磁电压
  和电流。

以下各节详细描述了模块的每个主要部分。

### 电流补偿器和电压测量变送器

电流补偿器建模为：

VC1=VT+ITRC2+XC2，

其中：

- *RC* 是负载补偿
  电阻。
- *XC* 是负载补偿
  电抗。

电压测量变送器实现为具有时间常数
*TR* 的 Low-Pass
Filter 模块。有关离散和连续实现，请参阅 Low-Pass Filter 模块的文档。

### 励磁控制元件

下图说明了励磁控制元件的整体结构：

图中：

- Summation Point Logic 子系统对过励限制器（OEL）、欠励限制器（UEL）、定子电流限制器（SCL）和电源开关选择器（V\_S）电压的求和点输入位置进行建模。有关在此模块中使用限制器的详细信息，请参阅 Field Current Limiters。
- 有两个 Take-over Logic 子系统。这些子系统对 OEL、UEL、SCL 和 PSS 电压的接管点输入位置进行建模。有关在此模块中使用限制器的详细信息，请参阅 Field Current Limiters。
- 两个 Lead-Lag 模块对与电压调节器相关的附加动态进行建模。前者表示瞬态增益减小，其中 *TC* 是超前时间常数，*TB* 是滞后时间常数。后者允许表示瞬态增益增加的可能性，其中 *TC1* 是超前时间常数，*TB1* 是滞后时间常数。有关离散和连续实现，请参阅 Lead-Lag 模块的文档。
- Low-Pass Filter 模块对电压调节器的主要动态进行建模。此处，*KA* 是调节器增益，*TA* 是调节器的主要时间常数。模块的最小和最大抗积分饱和限幅分别为 *VAmin* 和 *VAmax*。
- Filtered Derivative 模块对用于励磁系统稳定的速率反馈路径进行建模。此处，*KF* 和 *TF* 分别是该系统的增益和时间常数。有关离散和连续实现，请参阅 Filtered Derivative 模块的文档。
- 由于具有非常高的强励能力，该模型采用励磁电流限制器来保护发电机转子和励磁机。初始阈值和增益分别由 *ILR* 和 *KLR* 定义。如果使用显式 OEL 模型，请通过将增益 *KLR* 设置为 `0` 来禁用此励磁电流限制器。

### Field Current Limiters

您可以使用各种励磁电流限制器，在不安全的运行条件下修改电压调节器的输出：

- 使用过励限制器，防止因励磁电流需求过大而导致励磁绕组过热。
- 使用欠励限制器，在励磁过低时提升励磁，因为励磁过低存在失步风险。
- 使用定子电流限制器，防止因电流过大而导致定子绕组过热。

将这些限制器中任意一个的输出连接到以下任一位置：

- 作为自动电压调节器 (AVR) 反馈回路一部分的求和点
- 用于覆盖 AVR 常规行为的接管点

如果您在求和点使用定子电流限制器，请使用单输入 *VSCLsum*。如果您在接管点使用定子电流限制器，请同时使用过励输入 *VSCLoel* 和欠励输入 *VSCLuel*。
