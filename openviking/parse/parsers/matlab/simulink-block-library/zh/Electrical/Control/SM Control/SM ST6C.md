---
type: simulink-block
title: 'SM ST6C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smst6c'
documentation_source_path: 'ref/smst6c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM ST6C

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
- 要在电压误差求和点使用来自过励限制器的输入，请将
  **Alternate OEL input locations
  (V\_OEL)** 设置为 `Summation point
  at voltage error`。
- 要在第一个接管点使用来自过励限制器的输入，请将 **Alternate OEL
  input locations (V\_OEL)** 设置为
  `Take-over at voltage
  error`。
- 要在 AVR 输入求和点使用来自过励限制器的输入，请将
  **Alternate OEL input locations
  (V\_OEL)** 设置为 `Summation point
  at AVR input`。
- 要在第二个接管点使用来自过励限制器的输入，请将 **Alternate OEL
  input locations (V\_OEL)** 设置为
  `Take-over at voltage regulator
  input`。

**数据类型：** `single` | `double`

### **V\_UEL** — 欠励限制信号标量

来自欠励限制器的输入，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自欠励限制器的输入，请将 **Alternate UEL input locations
  (V\_UEL)** 设置为
  `Unused`。
- 要在电压误差求和点使用来自欠励限制器的输入，请将
  **Alternate UEL input locations
  (V\_UEL)** 设置为 `Summation point
  at voltage error`。
- 要在第一个接管点使用来自欠励限制器的输入，请将 **Alternate UEL
  input locations (V\_UEL)** 设置为
  `Take-over at voltage
  error`。
- 要在 AVR 输入求和点使用来自欠励限制器的输入，请将
  **Alternate UEL input locations
  (V\_UEL)** 设置为 `Summation point
  at AVR input`。
- 要在第二个接管点使用来自欠励限制器的输入，请将 **Alternate UEL
  input locations (V\_UEL)** 设置为
  `Take-over at voltage regulator
  input`。

**数据类型：** `single` | `double`

### **V\_SCLsum** — 求和点定子电流限制信号标量

使用求和点时来自定子电流限制器的输入，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations
  (V\_SCL)** 设置为
  `Unused`。
- 要在求和点使用来自定子电流限制器的输入，请将 **Alternate SCL input
  locations** 设置为任意
  `Summation point`
  选项。

**数据类型：** `single` | `double`

### **V\_SCLoel** — 接管定子电流限制（OEL）标量

使用接管点时来自定子电流限制器的输入，用于防止励磁过励，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations
  (V\_SCL)** 设置为
  `Unused`。
- 要在接管点使用来自定子电流限制器的输入，请将 **Alternate SCL input
  locations (V\_SCL)** 设置为任意
  `Take-over` 选项。

**数据类型：** `single` | `double`

### **V\_SCLuel** — 接管定子电流限制（UEL）标量

使用接管点时来自定子电流限制器的输入，用于防止励磁欠励，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations
  (V\_SCL)** 设置为
  `Unused`。
- 要在接管点使用来自定子电流限制器的输入，请将 **Alternate SCL input
  locations (V\_SCL)** 设置为任意
  `Take-over` 选项。

**数据类型：** `single` | `double`

### **Ifd\_pu** — 测量的励磁电流标量

同步电机的测量标幺励磁电流，指定为标量。

**数据类型：** `single` | `double`
### 输出

### **Efd\_pu** — 励磁电压标量

施加到同步电机励磁绕组的标幺励磁电压，以标量形式返回。

**数据类型：** `single` | `double`

## 参数

### 通用

### **Initial field voltage, Efd0 (pu)** — 初始输出电压 `1`（默认）| 实数标量

施加到同步电机励磁绕组的初始标幺电压。

### **Initial terminal voltage, Vt0 (pu)** — 初始机端电压 `1`（默认）| 实数标量

施加到机端的初始标幺电压。

#### 依赖关系

要启用此参数，请在励磁器部分将
**Power source selector** 设置为
`Position A: power source derived from generator
terminal voltage`。

### **Initial terminal current, It0 (pu)** — 初始机端电流 `1`（默认）| 实数标量

施加到机端的初始标幺电流。

#### 依赖关系

要启用此参数，请在励磁器部分将
**Power source selector** 设置为
`Position A: power source derived from generator
terminal voltage`。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。
有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请将此参数设置为 `-1`。
对于离散时间操作，请将此参数设置为正整数。对于
连续时间操作，请将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保
模块的连续实现和离散实现之间正确切换。有关
详细信息，请参阅 Promote Block Parameters on a Mask。

### 预控制

### **Resistive component of load compensation, R\_C (pu)** — 补偿电阻 `0`（默认）| 正标量

电流补偿系统中使用的电阻。将此参数
和 **Reactance component of load compensation, X\_C
(pu)** 设置为 `0` 以禁用电流
补偿。

### **Reactance component of load compensation, X\_C (pu)** — 补偿电抗 `0`（默认）| 正标量

电流补偿系统中使用的电抗。将此参数
和 **Resistive component of load compensation, R\_C
(pu)** 设置为 `0` 以禁用电流
补偿。

### **Regulator input filter time constant, T\_R (s)** — 调节器时间常数 `0.012`（默认）| 正标量

电压传感器滤波的等效时间常数。

### 控制

### **Voltage regulator proportional gain, K\_PA (pu)** — 调节器比例增益 `18.038`（默认）| 正标量

电压调节器 PI 控制模块的比例增益。

### **Voltage regulator integral gain, K\_IA (pu/s)** — 调节器积分增益 `45.094`（默认）| 正标量

电压调节器 PI 控制模块的积分增益。

### **Pre-control gain constant of the inner loop field voltage regulator, K\_FF (pu)** — 内环励磁电压调节器的预控制增益常数 `1`（默认）

内环励磁电压调节器的标幺预控制增益常数。要禁用
内环励磁电压调节器，请将此参数和
**Feedback gain constant of the inner loop field voltage
regulator, K\_G** 参数设置为 `0`。

### **Forward gain of inner loop field regulator, K\_M (pu)** — 内环励磁调节器的前向增益 `1`（默认）

内环励磁电压
调节器的标幺前向增益。

### **Feedback gain constant of the inner loop field voltage regulator, K\_G (pu)** — 内环励磁电压调节器的反馈增益常数 `1`（默认）

内环励磁电压调节器的标幺反馈增益常数。要禁用
内环励磁电压调节器，请将此参数和
**Pre-control gain constant of the inner loop field voltage
regulator, K\_FF** 参数设置为 `0`。

### **Feedback time constant of inner loop field voltage regulator, T\_G (s)** — 内环励磁电压调节器的反馈时间常数 `0.02`（默认）

内环励磁电压调节器的反馈时间常数。

### **Maximum voltage regulator output, V\_Amax (pu)** — 电压调节器最大输出 `4.81`（默认）

电压调节器的最大标幺输出。

### **Minimum voltage regulator output, V\_Amin (pu)** — 电压调节器最小输出 `-3.85`（默认）

电压调节器的最小标幺输出。

### **Maximum regulator output limit, V\_Rmax (pu)** — 调节器最大输出 `4.81`（默认）

调节器的最大标幺输出。

### **Minimum regulator output limit, V\_Rmin (pu)** — 调节器最小输出 `-3.85`（默认）

调节器的最小标幺输出。

### **Maximum rectifier output limit, V\_Mmax (pu)** — 整流器最大输出 `4.81`（默认）

整流器的最大标幺输出。

### **Minimum rectifier output limit, V\_Mmin (pu)** — 整流器最小输出 `-3.85`（默认）

整流器的最小标幺输出。

### **Thyristor bridge firing control equivalent time constant, T\_A (s)** — 晶闸管桥触发控制等效时间常数 `0.02`（默认）

晶闸管桥触发控制的等效时间常数，以
秒为单位。

### **Alternate OEL input locations (V\_OEL)** — OEL 输入位置 `Unused`（默认）| `Summation point at voltage error` | `Take-over at voltage error` | `Summation point at AVR input` | `Take-over at voltage regulator input`

过励限制器输入的位置，指定为以下选项之一：

- `Summation point at voltage
  error` — **V\_OEL** 是
  **Summation Point Logic**
  子系统的输入。
- `Take-over at voltage error` —
  **V\_OEL** 是
  **Take-over Logic** 子系统的输入。
- `Summation point at AVR input` —
  **V\_OEL** 是
  **Summation Point Logic1**
  子系统的输入。
- `Take-over at voltage regulator
  output` — **V\_OEL** 是
  **Take-over Logic 1**
  子系统的输入。

### **Alternate UEL input locations (V\_UEL)** — UEL 输入位置 `Unused`（默认）| `Summation point at voltage error` | `Take-over at voltage error` | `Summation point at AVR input` | `Take-over at voltage regulator input`

欠励限制器输入的位置，指定为以下选项之一：

- `Summation point at voltage
  error` — **V\_UEL** 是
  **Summation Point Logic**
  子系统的输入。
- `Take-over at voltage error` —
  **V\_UEL** 是
  **Take-over Logic** 子系统的输入。
- `Summation point at AVR input` —
  **V\_UEL** 是
  **Summation Point Logic1**
  子系统的输入。
- `Take-over at voltage regulator
  output` — **V\_UEL** 是
  **Take-over Logic 1**
  子系统的输入。

### **Alternate SCL input locations (V\_SCL)** — SCL 输入位置 `Unused`（默认）| `Summation point at voltage error` | `Take-over at voltage error` | `Summation point at AVR input` | `Take-over at voltage regulator input`

定子电流限制器输入位置，指定为以下选项之一：

- `Summation point at voltage
  error` — **V\_SCL** 是
  **Summation Point Logic**
  子系统的输入。
- `Take-over at voltage error` —
  **V\_SCL** 是
  **Take-over Logic** 子系统的输入。
- `Summation point at AVR input` —
  **V\_SCL** 是
  **Summation Point Logic1**
  子系统的输入。
- `Take-over at voltage regulator
  output` — **V\_SCL** 是
  **Take-over Logic 1**
  子系统的输入。

### 励磁器

### **Exciter output current limiter gain, K\_LR (pu)** — 励磁器输出电流限制器增益 `17.33`（默认）| 实数标量

最大标幺励磁器电流限制器增益。

### **Exciter output current limit reference, I\_LR (pu)** — 励磁器输出电流限制参考 `4.164`（默认）| 实数标量

标幺励磁器电流限制参考。

### **Exciter output current limit adjustment, K\_CI (pu)** — 励磁器输出电流限制调整 `1.0577`（默认）

标幺励磁器电流限制调整。

### **Rectifier loading factor proportional to commutating reactance, K\_C (pu)** — 整流器负载因子 `0`（默认）| 正标量

标幺整流器负载因子。此值与换相
电抗成正比。

### **Potential circuit (voltage) gain coefficient, K\_P (pu)** — 电位电路增益系数 `1`（默认）| 实数标量

标幺电位电路增益系数。

### **Compound circuit (current) gain coefficient, K\_I (pu)** — 电位电路电流增益系数 `0`（默认）| 实数标量

标幺电位电路电流增益系数。

#### 依赖关系

要启用此参数，请将 **Power source selector
SW1** 设置为 `Position A: power source derived
from generator terminal voltage`。

### **Reactance associated with potential source, X\_L (pu)** — 与电位源相关的电抗 `0`（默认）| 实数标量

与电位源相关的标幺电抗。

#### 依赖关系

要启用此参数，请将 **Power source
selector** 设置为 `Position A: power source
derived from generator terminal voltage`。

### **Potential circuit phase angle (degrees)** — 电位电路相位角 `0`（默认）| 实数标量

电位电路相位角，以度为单位。

#### 依赖关系

要启用此参数，请将 **Power source
selector** 设置为 `Position A: power source
derived from generator terminal voltage`。

### **Maximum available exciter voltage, V\_Bmax (pu)** — 最大可用励磁器励磁电压 `99`（默认）| 实数标量

励磁器的最大标幺可用励磁电压。

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

离散时间或连续时间同步电机 ST6C 静态励磁系统，带自动电压调节器

SM ST6C 模块按照 IEEE Std 421.5-2016 [1] 实现了一个同步电机型 ST6C 静态励磁系统模型。

使用此模块可对同步电机励磁电压的控制和调节进行建模。

通过使用 **Sample time (-1 for inherited)** 参数，可在模块的连续和离散实现之间切换。要将积分器配置为连续时间，请将 **Sample time (-1 for inherited)** 参数设置为 `0`。要将积分器配置为离散时间，请将 **Sample time (-1 for inherited)** 参数设置为正标量。要从上游模块继承采样时间，请将 **Sample time (-1 for inherited)** 参数设置为 `-1`。

SM ST6C 模块包含四个主要组件：

- 电流补偿器组件根据端子电流修改测得的端子电压。
- 电压测量传感器组件使用低通滤波器模拟端子电压传感器的动态特性。
- 励磁控制元件组件将电压传感器输出与端子电压参考值进行比较，以产生电压误差值。该组件随后将此值通过电压调节器，以产生励磁电压。
- 电源组件对受控整流器的电源进行建模，适用于其独立于端子电压的情况。

此图显示了 ST6C 励磁系统模型的结构：

在图中：

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

该模块将电压测量传感器实现为具有时间常数 *TR* 的低通滤波器模块。有关精确的离散和连续实现信息，请参阅低通滤波器模块的文档。

### 励磁控制元件

此图显示了励磁控制元件的结构：

在图中：

- 有两个求和点逻辑子系统。这些子系统对过励限制器（OEL）、欠励限制器（UEL）、定子电流限制器（SCL）和电源开关选择器（V\_S）电压的求和点输入位置进行建模。有关将此模块与限制器配合使用的更多信息，请参阅励磁电流限制器。
- 有两个接管逻辑子系统。这些子系统对 OEL、UEL、SCL 和 PSS 电压的接管点输入位置进行建模。有关将此模块与限制器配合使用的更多信息，请参阅励磁电流限制器。
- PI 子系统对作为自动电压调节器控制结构的 PI 控制器进行建模，并允许表示采用现代数字控制器的设备改造。该模块的最小和最大抗积分饱和限幅为 *VAmin* 和 *VAmax*。
- 使用内部励磁电压控制环来提高动态响应，它由增益 *KM* 和 *KFF* 组成。该模块的最小和最大抗积分饱和限幅为 *VMmin* 和 *VMmax*。如果未实现励磁电压调节器，则相应参数 *KG* 和 *KFF* 设置为 0。
- **Power source selector** 参数控制受控整流器电源的来源。该子系统随后将整流桥输出 *VM* 与励磁机励磁电压 *VB* 相乘。有关受控整流器电源逻辑开关的更多信息，请参阅电源。

### 励磁电流限制器

您可以使用不同类型的励磁电流限制器，在不安全运行条件下修改电压调节器的输出：

- 使用过励限制器防止因励磁电流需求过大而导致励磁绕组过热。
- 使用欠励限制器在励磁过低时提升励磁，因为励磁过低存在失步风险。
- 使用定子电流限制器防止因电流过大而导致定子绕组过热。

将上述任一限制器的输出连接到以下任一位置：

- 求和点 — 将限制器用作自动电压调节器（AVR）反馈回路的一部分。
- 接管点 — 覆盖 AVR 的通常行为。

如果您在求和点使用定子电流限制器，请使用输入 *VSCLsum*。如果您在接管点使用定子电流限制器，请使用过励输入 *VSCLoel* 和欠励输入 *VSCLuel*。

### 电源

您可以通过设置 **Power source selector** 参数值，为受控整流器使用不同的电源表示。要从端子电压推导受控整流器的电源，请将 **Power source selector** 参数设置为 `Position A: power source derived from generator terminal voltage`。要指定电源独立于端子电压，请将 **Power source selector** 参数设置为 `Position B: power source independent of generator terminal conditions`。

此图显示了利用端子电压 *VT* 和端子电流 *IT* 的相量组合对励磁机电源进行建模的模型：
