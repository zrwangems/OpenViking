---
type: simulink-block
title: 'SM ST8C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smst8c'
documentation_source_path: 'ref/smst8c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM ST8C

## 端口

### 输入

### **V\_REF** — 电压参考值标量

电压调节器参考设定值，以标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **V\_S** — 来自稳定器的输入标量

来自电力系统稳定器的输入，以标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **V\_T** — 机端电压标量

机端电压幅值，以标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **I\_T** — 机端电流标量

机端电流幅值，以标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **V\_OEL** — 过励限制信号标量

来自过励限制器的输入，以标幺值表示，指定为标量。

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

来自欠励限制器的输入，以标幺值表示，指定为标量。

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

使用求和点时来自定子电流限制器的输入，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations
  (V\_SCL)** 设置为
  `Unused`。
- 要在求和点使用来自定子电流限制器的输入，请将 **Alternate SCL input
  locations (V\_SCL)** 设置为
  `Summation point`。

**数据类型：** `single` | `double`

### **V\_SCLoel** — 接管定子电流限制（OEL）标量

使用接管点时来自定子电流限制器的输入，用于防止励磁过励，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations
  (V\_SCL)** 设置为
  `Unused`。
- 要在接管点使用来自定子电流限制器的输入，请将 **Alternate SCL input
  locations (V\_SCL)** 设置为
  `Take-over`。

**数据类型：** `single` | `double`

### **V\_SCLuel** — 接管定子电流限制（UEL）标量

使用接管点时来自定子电流限制器的输入，用于防止励磁欠励，以标幺值表示，指定为标量。

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

### **Initial field voltage, Efd0 (pu)** — 初始输出电压 `1`（默认）| 实数标量

施加到同步电机励磁绕组的初始标幺电压。

### **Initial terminal voltage, Vt0 (pu)** — 初始机端电压 `1`（默认）| 实数标量

施加到机端的初始标幺电压。

#### 依赖关系

要启用此参数，请在 Exciter 部分中，将 **Power source selector** 设置为
`Position A: power source derived from generator
terminal voltage`。

### **Initial terminal current, It0 (pu)** — 初始机端电流 `1`（默认）| 实数标量

施加到机端的初始标幺电流。

#### 依赖关系

要启用此参数，请在 Exciter 部分中，将 **Power source selector** 设置为
`Position A: power source derived from generator
terminal voltage`。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。
有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请将此参数设置为 `-1`。
对于离散时间操作，请将此参数设置为正整数。对于
连续时间操作，请将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保
在模块的连续实现和离散实现之间正确切换。有关
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

### **Regulator input filter time constant, T\_R (s)** — 调节器时间常数 `0.0226`（默认）| 正标量

电压变送器滤波的等效时间常数。

### 控制

### **Voltage regulator proportional gain, K\_PR (pu)** — 电压调节器比例增益 `6.6`（默认）

电压调节器的标幺比例增益。

### **Voltage regulator integral gain, K\_IR (pu/s)** — 电压调节器积分增益 `30`（默认）

电压调节器的标幺积分增益。

### **Maximum voltage regulator output, V\_PImax (pu)** — PI 调节器最大输出 `16`（默认）| 正标量

PI 调节器的最大允许标幺输出。

### **Minimum voltage regulator output, V\_PImin (pu)** — PI 调节器最小输出 `-16`（默认）| 正标量

PI 调节器的最小允许标幺输出。

### **Field current regulator proportional gain, K\_PA (pu)** — 励磁电流调节器比例增益 `2.38`（默认）

励磁电流调节器的标幺比例增益。

### **Field current regulator integral gain, K\_IA (pu/s)** — 励磁电流调节器积分增益 `0`（默认）

励磁电流调节器的标幺积分增益。

### **Maximum exciter output, V\_Amax (pu)** — 励磁机输出上限 `1`（默认）| 实数标量

励磁机的最大标幺输出电压。

### **Minimum exciter output, V\_Amin (pu)** — 励磁机输出下限 `-1`（默认）| 实数标量

励磁机的最小标幺输出电压。

### **Controlled rectifier bridge equivalent gain, K\_A (pu)** — 整流桥增益 `4.295`（默认）| 正标量

可控整流桥的增益。

### **Controlled rectifier bridge equivalent time constant, T\_A (s)** — 整流桥时间常数 `0.0017`（默认）| 正标量

可控整流桥的时间常数。

### **Maximum field current regulator output, V\_Rmax (pu)** — 励磁电流调节器最大输出 `4.27`（默认）| 正标量

励磁电流调节器的最大允许标幺输出。

### **Minimum field current regulator output, V\_Amin (pu)** — 励磁电流调节器最小输出 `-3.64`（默认）| 正标量

励磁电流调节器的最小允许标幺输出。

### **Exciter field current feedback gain, K\_F (pu)** — 励磁机励磁电流反馈增益 `1`（默认）| 实数标量

励磁机的标幺励磁电流反馈增益。

### **Field current feedback time constant, T\_F (s)** — 反馈时间常数 `0.0226`（默认）| 正标量

用于励磁系统稳定的反馈时间常数。

### **Alternate OEL input locations (V\_OEL)** — OEL 输入位置 `Unused`（默认）| `Summation point` | `Take-over`

过励限制器输入的位置，指定为以下选项之一：

- `Summation point` —
  **V\_OEL** 是 Summation
  Point Logic 子系统的输入。
- `Take-over` —
  **V\_OEL** 是 Take-over
  Logic 子系统的输入。

### **Alternate UEL input locations (V\_UEL)** — UEL 输入位置 `Unused`（默认）| `Summation point` | `Take-over`

欠励限制器输入的位置，指定为以下选项之一：

- `Summation point` —
  **V\_UEL** 是 Summation
  Point Logic 子系统的输入。
- `Take-over` —
  **V\_UEL** 是 Take-over
  Logic 子系统的输入。

### **Alternate SCL input locations (V\_SCL)** — SCL 输入位置 `Unused`（默认）| `Summation point` | `Take-over`

定子电流限制器输入的位置，指定为以下选项之一：

- `Summation point` — 使用
  **V\_SCLsum** 输入端口。
- `Take-over` — 使用
  **V\_SCLoel** 和
  **V\_SCLuel** 输入端口。

### 励磁机

### **Rectifier loading factor proportional to commutating reactance, K\_C1 (pu)** — 整流器负载因数 `0.062`（默认）| 正标量

标幺整流器负载因数。此值与换相
电抗成正比。

### **Potential circuit (voltage) gain coefficient, K\_P (pu)** — 电势回路增益系数 `1`（默认）| 实数标量

标幺电势回路增益系数。

### **Compound circuit (current) gain coefficient, K\_I (pu)** — 电势回路电流增益系数 `0`（默认）| 实数标量

标幺电势回路电流增益系数。

#### 依赖关系

要启用此参数，请将 **Power source selector
SW1** 设置为 `Position A: power source derived
from generator terminal voltage`。

### **Reactance associated with potential source, X\_L (pu)** — 与电势源相关的电抗 `0`（默认）| 实数标量

与电势源相关的标幺电抗。

#### 依赖关系

要启用此参数，请将 **Power source
selector** 设置为 `Position A: power source
derived from generator terminal voltage`。

### **Potential circuit phase angle (degrees)** — 电势回路相位角 `0`（默认）| 实数标量

电势回路相位角，以度为单位。

#### 依赖关系

要启用此参数，请将 **Power source
selector** 设置为 `Position A: power source
derived from generator terminal voltage`。

### **Maximum available exciter voltage, V\_B1max (pu)** — 最大可用励磁机励磁电压 `2`（默认）| 实数标量

励磁机的最大可用标幺励磁电压。

### **Rectifier loading factor proportional to commutating reactance, K\_C2 (pu)** — 与换相电抗成正比的整流器负载因数 `0`（默认）| 实数标量

整流器的标幺负载因数。此值与换相
电抗成正比，通过单独的串联二极管桥从发电机机端电流
导出。

### **Compound circuit (current) gain coefficient, K\_I2 (pu)** — 复合回路电流增益系数 `0`（默认）| 实数标量

通过单独的串联二极管桥从发电机机端电流导出的标幺复合回路电流增益系数。将此参数设置为
`0` 以完全禁用单独的复合电源。

### **Maximum available exciter field voltage, V\_B2max (pu)** — 最大可用励磁机励磁电压 `0`（默认）| 实数标量

励磁机的最大可用标幺励磁电压，通过单独的串联二极管桥从发电机
机端电流导出。

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

具有自动电压调节器的离散时间或连续时间同步电机 ST8C 静态励磁系统

SM ST8C 模块实现符合 IEEE Std 421.5-2016 [1] 的同步电机型 ST8C 静态
励磁系统模型。

使用此模块对同步电机励磁电压的控制和调节进行建模。

通过使用 **Sample time (-1 for inherited)** 参数在模块的连续实现和离散实现之间
切换。要将积分器配置为连续时间，请将 **Sample time (-1 for
inherited)** 参数设置为 `0`。要将积分器配置
为离散时间，请将 **Sample time (-1 for inherited)** 参数
设置为正标量。要从上游模块继承采样时间，请将
**Sample time (-1 for inherited)** 参数设置为
`-1`。

SM ST8C 模块包含四个主要组件：

- Current Compensator 组件根据机端电流修改测量的机端电压。
- Voltage Measurement Transducer 组件使用低通滤波器模拟机端电压变送器的动态特性。
- Excitation Control Elements 组件将电压变送器输出与机端电压参考值进行比较，以产生电压误差值。
  该组件随后将此值通过电压调节器以产生励磁电压。
- Power Source 组件在受控整流器的电源独立于机端电压时，对受控整流器的电源进行建模。

此图显示了 ST8C 励磁系统模型的结构：

图中：

- *VT* 和
  *IT* 分别是同步电机的测量
  机端电压和电流。
- *VC1* 是电流补偿后的
  机端电压。
- *VC* 是滤波后的、
  电流补偿后的机端电压。
- *VREF* 是参考机端
  电压。
- *VS* 是电力系统
  稳定器电压。
- *VB* 是励磁机励磁
  电压。
- *EFD* 和
  *IFD* 分别是励磁电压
  和电流。

### 电流补偿器和电压测量变送器

该模块使用以下方程对电流补偿器进行建模：

VC1=VT+ITRC2+XC2，

其中：

- *RC* 是负载补偿
  电阻。
- *XC* 是负载补偿
  电抗。

该模块将电压测量变送器实现为具有时间常数
*TR* 的 Low-Pass
Filter 模块。有关精确的离散和连续实现的信息，请参阅
Low-Pass Filter 模块的文档。

### Excitation Control Elements

此图展示了励磁控制元件的结构：

图中：

- Summation Point Logic 子系统为过励限制器（OEL）、欠励限制器（UEL）和定子电流限制器（SCL）电压建模了求和点输入位置。有关将此模块与限制器配合使用的详细信息，请参阅 Field Current Limiters。
- Take-over Logic 子系统为 OEL、UEL 和 SCL 电压建模了接管点输入位置。有关将此模块与限制器配合使用的详细信息，请参阅 Field Current Limiters。
- PI 子系统为作为自动电压调节器控制结构的 PI 控制器建模，并允许表示采用现代数字控制器的设备改造。该模块的最小和最大抗积分饱和限幅分别为 *VPImin* 和 *VPImax*。电流 PI 调节器以级联方式跟随电压 PI 调节器。
- PI1 子系统为作为励磁电流调节器控制结构的 PI 控制器建模。该模块的最小和最大抗积分饱和限幅分别为 *VAmin* 和 *VAmax*。
- 顶部 Low-Pass Filter 模块为受控整流桥的主要动态特性建模。*KA* 是受控整流桥等效增益，*TA* 是受控整流桥的主要时间常数。该模块的最小和最大抗积分饱和限幅分别为 *VRmin* 和 *VRmax*。
- **Power source selector** 参数控制受控整流器电源的来源。贡献因子被求和和/或乘到功率级输出。求和分量 *VB2* 对应于由发电机端电流导出的复合电源。如果将 **Potential circuit (current) gain coefficient, K\_I2 (pu)** 和 **Rectifier loading factor proportional to commutating reactance, K\_C2 (pu)** 参数设置为 `0`，则该求和分量被禁用。有关受控整流器电源逻辑开关的详细信息，请参阅 Power Source。

### Field Current Limiters

您可以使用不同类型的励磁电流限制器，在不安全运行条件下修改电压调节器的输出：

- 使用过励限制器防止因过大的励磁电流需求导致励磁绕组过热。
- 使用欠励限制器在励磁过低时提升励磁，因为励磁过低存在失步风险。
- 使用定子电流限制器防止因电流过大导致定子绕组过热。

将上述任一限制器的输出连接到以下任一位置：

- 求和点 — 将限制器用作自动电压调节器（AVR）反馈回路的一部分。
- 接管点 — 覆盖 AVR 的常规行为。

如果在求和点使用定子电流限制器，请使用输入 *VSCLsum*。如果在接管点使用定子电流限制器，请使用过励输入 *VSCLoel* 和欠励输入 *VSCLuel*。

### Power Source

您可以通过设置 **Power source selector** 参数值，为受控整流器使用不同的电源表示。若要从端电压导出受控整流器的电源，请将 **Power source selector** 参数设置为 `Position A: power source derived from generator terminal voltage`。若要指定电源独立于端电压，请将 **Power source selector** 参数设置为 `Position B: power source independent of generator terminal conditions`。

此图展示了利用端电压 *VT* 和端电流 *IT* 的相量组合的励磁机电源模型：

求和分量 *VB2* 对应于由发电机端电流导出的复合电源。如果将 **Potential circuit (current) gain coefficient, K\_I2 (pu)** 和 **Rectifier loading factor proportional to commutating reactance, K\_C2 (pu)** 参数设置为 `0`，则该求和分量被禁用。
