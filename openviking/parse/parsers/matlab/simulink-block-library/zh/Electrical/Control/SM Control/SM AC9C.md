---
type: simulink-block
title: 'SM AC9C'
family: 'control'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smac9c'
documentation_source_path: 'ref/smac9c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM AC9C

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
  请将 **备选 OEL 输入位置 (V\_OEL)** 设置为
  `Unused`。
- 要在求和点使用来自过励限制器的输入，
  请将 **备选 OEL 输入位置 (V\_OEL)** 设置为
  `Summation point`。
- 要在接管点使用来自过励限制器的输入，
  请将 **备选 OEL 输入位置 (V\_OEL)** 设置为
  `Take-over`。

**数据类型：** `single` | `double`

### **V\_UEL** — 欠励限制信号标量

来自欠励限制器的输入，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自欠励限制器的输入，
  请将 **备选 UEL 输入位置 (V\_UEL)** 设置为
  `Unused`。
- 要在求和点使用来自欠励限制器的输入，
  请将 **备选 UEL 输入位置 (V\_UEL)** 设置为
  `Summation point`。
- 要在接管点使用来自欠励限制器的输入，
  请将 **备选 UEL 输入位置 (V\_UEL)** 设置为
  `Take-over`。

**数据类型：** `single` | `double`

### **V\_SCLsum** — 求和点定子电流限制信号标量

当使用求和点时，来自定子电流限制器的输入，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，
  请将 **备选 SCL 输入位置 (V\_SCL)** 设置为
  `Unused`。
- 要在求和点使用来自定子电流限制器的输入，
  请将 **备选 SCL 输入位置 (V\_SCL)** 设置为
  `Summation point`。

**数据类型：** `single` | `double`

### **V\_SCLoel** — 用于过励限制器的接管定子电流限制标量

当使用接管点时，来自定子电流限制器的输入，用于防止磁场过励，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，
  请将 **备选 SCL 输入位置 (V\_SCL)** 设置为
  `Unused`。
- 要在接管点使用来自定子电流限制器的输入，
  请将 **备选 SCL 输入位置 (V\_SCL)** 设置为
  `Take-over`。

**数据类型：** `single` | `double`

### **V\_SCLuel** — 用于欠励限制器的接管定子电流限制标量

当使用接管点时，来自定子电流限制器的输入，用于防止磁场欠励，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，
  请将 **备选 SCL 输入位置 (V\_SCL)** 设置为
  `Unused`。
- 要在接管点使用来自定子电流限制器的输入，
  请将 **备选 SCL 输入位置 (V\_SCL)** 设置为
  `Take-over`。

**数据类型：** `single` | `double`

### **Ifd\_pu** — 测量的励磁电流标量

同步电机的测量标幺值励磁电流，指定为标量。

**数据类型：** `single` | `double`

### 输出

### **Efd\_pu** — 励磁电压标量

要施加到同步机励磁电路的标幺值励磁电压，作为标量返回。

**数据类型：** `single` | `double`

## 参数

### 常规

### **初始励磁电压，Efd0 (pu)** — 初始输出电压 `1`（默认）| real scalar

初始施加到同步机励磁电路的标幺值电压。

### **初始端电压，Vt0 (pu)** — 初始端电压 `1`（默认）| real scalar

初始施加到端子的标幺值电压。

#### 依赖关系

要启用此参数，请在 Exciter 部分中，将
**电源选择器 SW1** 设置为
`Position A: power source derived from terminal
voltage`。

### **初始端电流，It0 (pu)** — 初始端电流 `1`（默认）| real scalar

初始施加到端子的标幺值电流。

### **采样时间 (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | positive scalar

连续模块执行之间的时间。执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，将此参数设置为 `-1`。
对于离散时间操作，将此参数设置为正整数。对于
连续时间操作，将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数，以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

### 预控制

### **负载补偿的电阻分量，R\_C (pu)** — 补偿电阻 `0`（默认）| positive scalar

用于电流补偿系统的电阻。将此参数
和 **负载补偿的电抗分量，X\_C
(pu)** 设置为 `0` 以禁用电流
补偿。

### **负载补偿的电抗分量，X\_C (pu)** — 补偿电抗 `0`（默认）| positive scalar

用于电流补偿系统的电抗。将此参数
和 **负载补偿的电阻分量，R\_C
(pu)** 设置为 `0` 以禁用电流
补偿。

### **调节器输入滤波器时间常数，T\_R (s)** — 调节器时间常数 `0.01`（默认）| positive scalar

用于电压变送器滤波的等效时间常数。

### 控制

### **电压调节器比例增益，K\_PR (pu)** — 电压调节器的比例增益 `10`（默认）

电压调节器的标幺值比例增益。

### **电压调节器积分增益，K\_IR (pu/s)** — 电压调节器的积分增益 `10`（默认）

电压调节器的标幺值积分增益。

### **电压调节器微分增益，K\_DR (pu.s)** — 电压调节器的微分增益 `0`（默认）

电压调节器的微分增益。

### **PID 控制器微分通道的滞后时间常数，T\_DR (s)** — PID 微分通道的滞后时间常数 `0.01`（默认）| positive scalar

PID 控制器微分通道的等效滞后时间常数。

### **电压调节器最大输出，V\_PIDmax (pu)** — PID 调节器的最大输出 `1.6`（默认）| positive scalar

PID 调节器的最大允许标幺值输出。

### **电压调节器最小输出，V\_PIDmin (pu)** — PID 调节器的最小输出 `0`（默认）| positive scalar

PID 调节器的最小允许标幺值输出。

### **励磁电流调节器比例增益，K\_PA (pu)** — 励磁电流调节器的比例增益 `4`（默认）| real scalar

励磁电流调节器的标幺值比例增益。

### **励磁电流调节器积分增益，K\_IA (pu/s)** — 励磁电流调节器的积分增益 `0`（默认）| real scalar

励磁电流调节器的标幺值积分增益。

### **电流调节器最大输出，V\_Amax (pu)** — 电流调节器最大输出 `0.996`（默认）| real scalar

最大标幺值电流调节器输出。

### **电流调节器最小输出，V\_Amin (pu)** — 电流调节器最小输出 `-0.866`（默认）| real scalar

最小标幺值电流调节器输出。

### **可控整流桥等效增益，K\_A (pu)** — 整流桥增益 `20`（默认）| positive scalar

可控整流桥的增益。

### **可控整流桥等效时间常数，T\_A (s)** — 整流桥时间常数 `0.0018`（默认）| positive scalar

可控整流桥的时间常数。

### **整流桥最大输出，V\_Rmax (pu)** — 整流桥输出的上限 `19.92`（默认）| real scalar

整流桥的最大标幺值输出。

### **整流桥最小输出，V\_Rmin (pu)** — 整流桥输出的下限 `-17.32`（默认）| real scalar

整流桥的最小标幺值输出。

### **励磁器励磁电流反馈增益，K\_F (pu)** — 励磁器励磁电流反馈增益 `0.2`（默认）| real scalar

励磁器的标幺值励磁电流反馈增益。

### **励磁电流反馈时间常数，T\_F (s)** — 反馈时间常数 `0.01`（默认）| positive scalar

用于励磁系统稳定的反馈时间常数。

### **续流等效反馈增益，K\_FW (pu)** — 续流反馈增益 `0`（默认）| real scalar

励磁器的标幺值续流反馈增益。

### **最大续流反馈，V\_FWmax (pu)** — 续流反馈的上限 `10`（默认）| real scalar

最大标幺值续流反馈。

### **最小续流反馈，V\_FWmin (pu)** — 续流反馈的下限 `0`（默认）| real scalar

最小标幺值续流反馈。

### **功率级类型选择器，S\_CT** — 用于选择功率级类型的选项 `Thyristor bridge`（默认）| `Chopper converter`

用于选择功率级类型的选项。如果将 **功率级类型选择器，S\_CT** 参数设置为
`Thyristor bridge`，则功率级
表示晶闸管换流器。如果将 **功率级
类型选择器，S\_CT** 参数设置为 `Chopper
converter`，则功率级表示斩波
换流器。

### **电压限值，V\_lim1 (pu)** — 第一自动电压调节器限值 `0`（默认）

用于计算电压调节器指令信号的第一自动电压调节器限值。

### **电压限值，V\_lim2 (pu)** — 第二自动电压调节器限值 `-0.1`（默认）

用于计算电压调节器指令信号的第二自动电压调节器限值。

### **备选 OEL 输入位置 (V\_OEL)** — OEL 输入位置 `Unused`（默认）| `Summation point` | `Take-over`

过励限制器输入的位置，指定为以下选项之一：

- `Summation point` —
  **V\_OEL** 是 Summation
  Point Logic 子系统的输入。
- `Take-over` —
  **V\_OEL** 是 Take-over
  Logic 子系统的输入。

### **备选 UEL 输入位置 (V\_UEL)** — UEL 输入位置 `Unused`（默认）| `Summation point` | `Take-over`

欠励限制器输入的位置，指定为以下选项之一：

- `Summation point` —
  **V\_UEL** 是 Summation
  Point Logic 子系统的输入。
- `Take-over` —
  **V\_UEL** 是 Take-over
  Logic 子系统的输入。

### **备选 SCL 输入位置 (V\_SCL)** — SCL 输入位置 `Unused`（默认）| `Summation point` | `Take-over`

定子电流限制器输入的位置，指定为以下选项之一：

- `Summation point` — 使用
  **V\_SCLsum** 输入端口。
- `Take-over` — 使用
  **V\_SCLoel** 和
  **V\_SCLuel** 输入端口。

### 励磁器

### **励磁器磁场比例常数，K\_E (pu)** — 励磁器磁场增益 `1`（默认）| positive scalar

励磁器磁场的比例常数。

### **励磁器磁场时间常数，T\_E (s)** — 励磁器磁场时间常数 `1`（默认）| positive scalar

励磁器磁场的时间常数。

### **与换向电抗成正比的二极管桥负载系数，K\_C (pu)** — 二极管桥负载系数 `0`（默认）| positive scalar

二极管桥负载系数。此值与换向电抗成正比。

### **去磁系数，励磁器交流发电机电抗的函数，K\_D (pu)** — 去磁系数 `1`（默认）| positive scalar

与励磁器交流发电机电抗相关的去磁系数。

### **饱和系数 S\_E(E\_1) 对应的励磁器输出电压，E\_1 (pu)** — 第一饱和输出电压 `4.167`（默认）| positive scalar

用于第一饱和系数的励磁器输出电压。

### **励磁器输出电压 E\_1 处的励磁器饱和系数，S\_E(E\_1) (1)** — 第一饱和查找电压 `0.001`（默认）| positive scalar

第一励磁器的饱和系数。

### **饱和系数 S\_E(E\_2) 对应的励磁器输出电压，E\_2 (pu)** — 第二饱和输出电压 `3.125`（默认）| positive scalar

用于第二饱和系数的励磁器输出电压。

### **励磁器输出电压 E\_2 处的励磁器饱和系数，S\_E(E\_2) (1)** — 第二饱和查找电压 `0.01`（默认）| positive scalar

第二励磁器的饱和系数。

### **励磁器磁场电流限值，V\_FEmax (pu)** — 励磁器上限 `16`（默认）| real scalar

最大标幺值磁场电流限值参考。

### **最小励磁器输出限值，V\_Emin (pu)** — 励磁器下限 `0`（默认）| real scalar

最小标幺值励磁器电压输出。

### **电压源电路增益系数，K\_P (pu)** — 电压源电路增益系数 `1`（默认）| real scalar

标幺值电压源电路增益系数。

### **电压源电路相角 (degrees)** — 电压源电路相角 `0`（默认）| real scalar

电压源电路相角，以度为单位。

#### 依赖关系

要启用此参数，请将 **电源选择器
SW1** 设置为 `Position A: power source derived
from terminal voltage`。

### **复合电路（电流）增益系数，K\_I (pu)** — 复合电路电流增益系数 `0`（默认）| real scalar

标幺值复合电路电流增益系数。

#### 依赖关系

要启用此参数，请将 **电源选择器
SW1** 设置为 `Position A: power source derived
from terminal voltage`。

### **与电压源相关的电抗，X\_L (pu)** — 与电压源相关的电抗 `0`（默认）| real scalar

与电压源相关的标幺值电抗。

#### 依赖关系

要启用此参数，请将 **电源选择器
SW1** 设置为 `Position A: power source derived
from terminal voltage`。

### **与换向电抗成正比的整流器负载系数，K\_C1 (pu)** — 与换向电抗成正比的整流器负载系数 `0`（默认）| real scalar

整流器的标幺值负载系数。此值与换向电抗成正比。

### **电源选择器 SW1** — 电源选择器 `Position A: power source derived from terminal voltage`（默认）| `Position B: power source independent of the terminal conditions`

电源选择器 SW1 的位置。

### **最大可用励磁器磁场电压，V\_B1max (pu)** — 最大可用励磁器磁场电压 `100`（默认）| real scalar

励磁器的最大可用标幺值磁场电压。

### **与换向电抗成正比的整流器负载系数，K\_C2 (pu)** — 与换向电抗成正比的整流器负载系数 `0`（默认）| real scalar

整流器的标幺值负载系数。此值与换向电抗成正比，通过单独的串联二极管桥从发电机端电流导出。

### **复合电路（电流）增益系数，K\_I2 (pu)** — 复合电路电流增益系数 `0`（默认）| real scalar

标幺值复合电路电流增益系数，通过单独的串联二极管桥从发电机端电流导出。将此参数设置为
`0` 可完全禁用单独的复合电源。

### **Maximum available exciter field voltage, V\_B2max (pu)** — Maximum available exciter field voltage `0` (default) | real scalar

励磁机的最大每单位可用磁场电压，通过单独的串联二极管桥从发电机端电流获得。

## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

离散时间或连续时间同步电机 AC9C 励磁系统，包括自动电压调节器和励磁机

SM AC9C 模块实现符合 Std IEEE 421.5-2016 [1] 的同步电机类型 AC9C 励磁系统模型。

使用此模块对作为发电机运行并使用交流旋转励磁机的同步电机的磁场电压进行控制和调节建模。

通过 **Sample time (-1 for inherited)** 参数在模块的连续实现和离散实现之间切换。要将积分器配置为连续时间，请将 **Sample time (-1 for inherited)** 参数设置为 `0`。要将积分器配置为离散时间，请将 **Sample time (-1 for inherited)** 参数设置为正标量。要从上游模块继承采样时间，请将 **Sample time (-1 for inherited)** 参数设置为 `-1`。

SM AC9C 模块包含五个主要组件：

- Current Compensator 组件根据端电流修改测量的端电压。
- Voltage Measurement Transducer 组件使用低通滤波器模拟端电压传感器的动态特性。
- Excitation Control Elements 组件将电压传感器输出与端电压参考进行比较，以产生电压误差值。然后该组件将此值通过电压调节器以产生励磁机磁场电压。
- AC Rotating Exciter 组件对交流旋转励磁机建模，该励磁机产生施加到受控同步电机的磁场电压。该模块还将励磁机磁场电流 (*VFE*) 反馈回励磁系统。
- Power Source 组件对受控整流器电源与端电压的依赖性进行建模。

此图显示 AC9C 励磁系统模型的结构：

图中：

- *VT* 和 *IT* 分别是同步电机的测量端电压和电流。
- *VC1* 是电流补偿后的端电压。
- *VC* 是滤波后的、电流补偿后的端电压。
- *VREF* 是参考端电压。
- *VS* 是电力系统稳定器电压。
- *SW1* 是为受控整流器指定的电源开关。
- *VB* 是励磁机磁场电压。
- *EFE* 和 *VFE* 分别是励磁机磁场电压和电流。
- *EFD* 和 *IFD* 分别是磁场电压和电流。

### Current Compensator and Voltage Measurement Transducer

该模块使用以下方程对电流补偿器建模：

VC1=VT+ITRC2+XC2,

其中：

- *RC* 是负载补偿电阻。
- *XC* 是负载补偿电抗。

该模块使用时间常数为 *TR* 的 Low-Pass Filter 模块实现电压测量传感器。有关精确的离散和连续实现的信息，请参阅 Low-Pass Filter 模块的文档。

### Excitation Control Elements

此图显示励磁控制元件的结构：

图中：

- Summation Point Logic 子系统为过励限制器 (OEL)、欠励限制器 (UEL) 和定子电流限制器 (SCL) 建模求和点输入位置。有关将此模块与限制器一起使用的更多信息，请参阅磁场电流限制器。
- PID 子系统对用作自动电压调节器控制结构的 PID 控制器进行建模。该模块的最小和最大抗积分饱和饱和限值分别为 *VPIDmin* 和 *VPIDmax*。
- Take-over Logic 子系统为 OEL、UEL、SCL 和 PSS 电压建模接管点输入位置。有关将此模块与限制器一起使用的更多信息，请参阅磁场电流限制器。
- PI\_R 子系统对用作磁场电流调节器控制结构的 PI 控制器进行建模。该模块的最小和最大抗积分饱和饱和限值分别为 *VAmin* 和 *VAmax*。
- 顶部 Low-Pass Filter 模块对受控整流桥的主要动态特性进行建模。*KA* 是受控整流桥等效增益，*TA* 是受控整流桥的主要时间常数。该模块的最小和最大抗积分饱和饱和限值分别为 *VRmin* 和 *VRmax*。
- 底部 Low-Pass Filter 模块对用于稳定励磁系统的速率反馈路径进行建模。*KF* 和 *TF* 分别是该系统的增益和时间常数。有关离散和连续实现的信息，请参阅 Low-Pass Filter 模块的文档。
- Power state logic 子系统支持选择功率级类型，该类型可以是晶闸管或斩波转换器。如果将 **Power stage type selector, S\_CT** 参数设置为 `Thyristor bridge`，它表示晶闸管转换器。如果将 **Power stage type selector, S\_CT** 参数设置为 `Chopper converter`，它表示斩波转换器。该子系统将电压调节器命令信号 *VR* 与励磁机磁场电压 *VB* 相加。有关受控整流器电源的逻辑开关以及 Power state logic 子系统的更多信息，请参阅 Power Source and Power State Logic。
- **initialOffset** Constant 模块确保仿真可以从稳态开始。SM AC9C 模块使用饱和和励磁机参数计算此值，包括初始磁场电压和励磁机磁场电流反馈增益。

### 磁场电流限制器

您可以使用不同类型的磁场电流限制器在不安全运行条件下修改电压调节器的输出：

- 使用过励限制器防止因磁场电流需求过大而导致磁场绕组过热。
- 使用欠励限制器在磁场励磁过低时提升励磁，过低会导致失步风险。
- 使用定子电流限制器防止因电流过大而导致定子绕组过热。

将上述任一限制器的输出连接至以下任一位置：

- 求和点 — 将限制器用作自动电压调节器 (AVR) 反馈回路的一部分。
- 接管点 — 覆盖 AVR 的通常行为。

如果在求和点使用定子电流限制器，请使用输入 *VSCLsum*。如果在接管点使用定子电流限制器，请使用过励输入 *VOELscl* 和欠励输入 *VUELscl*。

### AC Rotating Exciter

此图显示交流旋转励磁机的结构：

图中：

- 励磁机磁场电流 *VFE* 是三个信号之和：

  - 非线性函数 *Vx* 对励磁机输出电压的饱和进行建模。
  - 比例项 *KE* 对励磁机输出电压与励磁机磁场电流之间的线性关系进行建模。
  - 该子系统使用反馈回路中的去磁常数 *KD* 对负载电流对励磁机输出电压的去磁效应进行建模。
- Integrator with variable limits 子系统对 *EFE* 与 *VFE* 之间的差值进行积分，以生成励磁机交流发电机输出电压 *VE*。*TE* 是此过程的时间常数。
- 非线性函数 *FEX* 对整流器调节引起的励磁机输出电压降进行建模。此函数取决于常数 *KC*，而 *KC* 本身是换向电抗的函数。
- 参数 *VEmin* 和 *VFEmax* 对旋转励磁机的下限和上限进行建模。

### Power Source and Power State Logic

您可以通过设置 **Power source selector SW1** 参数值来为受控整流器使用不同的电源表示。要从端电压获得受控整流器的电源，请将 **Power source selector SW1** 参数设置为 `Position A: power source derived from terminal voltage`。要指定电源独立于端电压，请将 **Power source selector SW1** 参数设置为 `Position B: power source independent from the terminal conditions`。

Power state logic 子系统支持选择功率级类型，该类型可以是晶闸管或斩波转换器。如果将 **Power stage type selector, S\_CT** 参数设置为 `Thyristor bridge`，则 Power state logic 子系统表示晶闸管转换器。如果将 **Power stage type selector, S\_CT** 参数设置为 `Chopper converter`，则 Power state logic 子系统表示斩波转换器。电压调节器命令信号 *VR* 的值取决于 **Voltage limit, V\_lim1 (pu)** 和 **Voltage limit, V\_lim2 (pu)** 参数以及 *VCT*、*VFW* 和 *VAVR* 信号，具体逻辑如下：

```
if S_CT ~= 0 % Thyristor bridge
	V_R = V_CT
else  	% Chopper converter
	if V_AVR > V_lim1
		V_R = C_T
	else
		if V_AVR > V_lim2
			V_R = 0
		else
			V_R = -V_FW
		end
	end
end
```
