---
type: simulink-block
title: 'SM ST9C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smst9c'
documentation_source_path: 'ref/smst9c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM ST9C

## 端口
```yaml
ports:
- name: V_REF
  summary: 电压参考标量
  direction: input
  data_types: single | double
- name: V_S
  summary: 来自稳定器的输入标量
  direction: input
  data_types: single | double
- name: V_T
  summary: 机端电压标量
  direction: input
  data_types: single | double
- name: I_T
  summary: 机端电流标量
  direction: input
  data_types: single | double
- name: V_OEL
  summary: 过励限制信号标量
  direction: input
  data_types: single | double
- name: V_UEL
  summary: 欠励限制信号标量
  direction: input
  data_types: single | double
- name: V_SCLsum
  summary: 求和点定子电流限制信号标量
  direction: input
  data_types: single | double
- name: V_SCLoel
  summary: 接管定子电流限制（OEL）标量
  direction: input
  data_types: single | double
- name: V_SCLuel
  summary: 接管定子电流限制（UEL）标量
  direction: input
  data_types: single | double
- name: Ifd_pu
  summary: 测量的励磁电流标量
  direction: input
  data_types: single | double
- name: Efd_pu
  summary: 励磁电压标量
  direction: output
  data_types: single | double
```

### 输入

### **V\_REF** — 电压参考标量

电压调节器参考设定点，以标幺值表示，指定为标量。

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

要施加到同步电机励磁绕组的标幺励磁电压，以标量形式返回。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Initial field voltage, Efd0 (pu)
  summary: 初始输出电压 1（默认）| 实数标量
  group: 常规
- name: Initial terminal voltage, Vt0 (pu)
  summary: 初始机端电压 1（默认）| 实数标量
  group: 常规
- name: Initial terminal current, It0 (pu)
  summary: 初始机端电流 1（默认）| 实数标量
  group: 常规
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 -1（默认）| 0 | 正标量
  group: 常规
- name: Resistive component of load compensation, R_C (pu)
  summary: 补偿电阻 0（默认）| 正标量
  group: 预控制
- name: Reactance component of load compensation, X_C (pu)
  summary: 补偿电抗 0（默认）| 正标量
  group: 预控制
- name: Regulator input filter time constant, T_R (s)
  summary: 调节器时间常数 0（默认）| 正标量
  group: 预控制
- name: Time constant of differential part of AVR, T_CD (s)
  summary: AVR 微分部分时间常数 0.06（默认）| 正标量
  group: 控制
- name: RegFilter time constant of differential part of AVR, T_BD (s)
  summary: AVR 微分部分滤波时间常数 0.03（默认）| 正标量
  group: 控制
- name: Dead-band for differential part influence on AVR, Z_A (1)
  summary: AVR 微分部分影响死区 0.036（默认）| 正标量
  group: 控制
- name: AVR gain, K_A (1)
  summary: AVR 增益 12（默认）| 实数标量
  group: 控制
- name: Gain associated with activation of takeover UEL, K_U (1)
  summary: 与接管 UEL 激活相关的增益 10000（默认）| 实数标量
  group: 控制
- name: Time constant of AVR, T_A (s)
  summary: AVR 时间常数 2（默认）| 正标量
  group: 控制
- name: Time constant of underexcitation limiter, T_AUEL (s)
  summary: 欠励限制器时间常数 2（默认）| 正标量
  group: 控制
- name: Maximum regulator output, V_Rmax (pu)
  summary: 调节器最大输出 1（默认）| 实数标量
  group: 控制
- name: Minimum regulator output, V_Rmin (pu)
  summary: 调节器最小输出 -0.866（默认）| 实数标量
  group: 控制
- name: Power converter gain (proportional to supply voltage), K_AS (pu)
  summary: 功率变换器增益 6.1（默认）| 实数标量
  group: 控制
- name: Equivalent time constant of power converter firing control, T_AS (s)
  summary: 功率变换器触发控制时间常数 0.0018（默认）| 正标量
  group: 控制
- name: Alternate OEL input locations (V_OEL)
  summary: OEL 输入位置 Unused（默认）| Summation point | Take-over
  group: 控制
- name: Alternate UEL input locations (V_UEL)
  summary: UEL 输入位置 Unused（默认）| Summation point | Take-over
  group: 控制
- name: Alternate SCL input locations (V_SCL)
  summary: SCL 输入位置 Unused（默认）| Summation point | Take-over
  group: 控制
- name: Rectifier loading factor proportional to commutating reactance, K_C (pu)
  summary: 整流器负载系数 0（默认）| 正标量
  group: 励磁机
- name: Potential circuit (voltage) gain coefficient, K_P (pu)
  summary: 电势电路电压增益系数 1（默认）| 正标量
  group: 励磁机
- name: Potential circuit (current) gain coefficient, K_I (pu)
  summary: 电势电路电流增益系数 0（默认）| 正标量
  group: 励磁机
- name: Reactance associated with the compound source, X_L (pu)
  summary: 复励电源电抗 0（默认）| 正标量
  group: 励磁机
- name: Potential circuit phase angle (degrees)
  summary: 电势电路相位角 0（默认）| 正标量
  group: 励磁机
- name: Maximum limit on exciter voltage based on supply condition, V_Bmax (pu)
  summary: 励磁机电压上限 11.63（默认）| 正标量
  group: 励磁机
- name: Switch to select exciter supply configuration
  summary: '电源选择器 Position A: power source derived from generator terminal voltage（默认）| Position B: power source independent
    of generator terminal conditions'
  group: 励磁机
```

### 常规

### **Initial field voltage, Efd0 (pu)** — 初始输出电压 `1`（默认）| 实数标量

要施加到同步电机励磁绕组的初始标幺电压。

### **Initial terminal voltage, Vt0 (pu)** — 初始机端电压 `1`（默认）| 实数标量

要施加到机端的初始标幺电压。

#### 依赖关系

要启用此参数，请在励磁机部分中，将
**Switch to select exciter supply
configuration** 设置为 `Position A: power
source derived from generator terminal
voltage`。

### **Initial terminal current, It0 (pu)** — 初始机端电流 `1`（默认）| 实数标量

要施加到机端的初始标幺电流。

#### 依赖关系

要启用此参数，请在励磁机部分中，将
**Switch to select exciter supply
configuration** 设置为 `Position A: power
source derived from generator terminal
voltage`。

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

### **Regulator input filter time constant, T\_R (s)** — 调节器时间常数 `0`（默认）| 正标量

电压变送器滤波的等效时间常数。

### 控制

### **Time constant of differential part of AVR, T\_CD (s)** — AVR 微分部分时间常数 `0.06`（默认）| 正标量

AVR 微分部分的 Filtered Derivative 模块的时间常数，以秒为单位。

### **RegFilter time constant of differential part of AVR, T\_BD (s)** — AVR 微分部分滤波时间常数 `0.03`（默认）| 正标量

AVR 微分部分的 Filtered Derivative 模块的滤波时间常数，以秒为单位。

### **Dead-band for differential part influence on AVR, Z\_A (1)** — AVR 微分部分影响死区 `0.036`（默认）| 正标量

AVR 微分部分的死区。

### **AVR gain, K\_A (1)** — AVR 增益 `12`（默认）| 实数标量

AVR 的增益。

### **Gain associated with activation of takeover UEL, K\_U (1)** — 与接管 UEL 激活相关的增益 `10000`（默认）| 实数标量

与接管 UEL 激活相关的增益。

### **Time constant of AVR, T\_A (s)** — AVR 时间常数 `2`（默认）| 正标量

AVR 的时间常数，以秒为单位。

### **Time constant of underexcitation limiter, T\_AUEL (s)** — 欠励限制器时间常数 `2`（默认）| 正标量

UEL 的时间常数，以秒为单位。

### **Maximum regulator output, V\_Rmax (pu)** — 调节器最大输出 `1`（默认）| 实数标量

调节器的最大标幺输出。

### **Minimum regulator output, V\_Rmin (pu)** — 调节器最小输出 `-0.866`（默认）| 实数标量

调节器的最小标幺输出。

### **Power converter gain (proportional to supply voltage), K\_AS (pu)** — 功率变换器增益 `6.1`（默认）| 实数标量

功率变换器增益的标幺值，与电源电压成正比。

### **Equivalent time constant of power converter firing control, T\_AS (s)** — 功率变换器触发控制时间常数 `0.0018`（默认）| 正标量

功率变换器触发控制的等效时间常数，以
秒为单位。

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

### **Rectifier loading factor proportional to commutating reactance, K\_C (pu)** — 整流器负载系数 `0`（默认）| 正标量

整流器负载系数。此值与换相
电抗成正比。

### **Potential circuit (voltage) gain coefficient, K\_P (pu)** — 电势电路电压增益系数 `1`（默认）| 正标量

电源电路中的标幺电压增益系数。

### **Potential circuit (current) gain coefficient, K\_I (pu)** — 电势电路电流增益系数 `0`（默认）| 正标量

电源电路中的标幺电流增益系数。

#### 依赖关系

要启用此参数，请将 **Switch to select exciter
supply configuration** 设置为 `Position A:
power source derived from generator terminal
voltage`。

### **Reactance associated with the compound source, X\_L (pu)** — 复励电源电抗 `0`（默认）| 正标量

复励电源中的标幺电抗。

#### 依赖关系

要启用此参数，请将 **Switch to select exciter
supply configuration** 设置为 `Position A:
power source derived from generator terminal
voltage`。

### **Potential circuit phase angle (degrees)** — 电势电路相位角 `0`（默认）| 正标量

电源电路的相位角，以度为单位。

#### 依赖关系

要启用此参数，请将 **Switch to select exciter
supply configuration** 设置为 `Position A:
power source derived from generator terminal
voltage`。

### **Maximum limit on exciter voltage based on supply condition, V\_Bmax (pu)** — 励磁机电压上限 `11.63`（默认）| 正标量

基于电源条件的最大可用励磁机电压标幺值。

### **Switch to select exciter supply configuration** — 电源选择器 `Position A: power source derived from generator terminal voltage`（默认）| `Position B: power source independent of generator terminal conditions`

电源选择器的位置，指定为
`Position A: power source derived from generator
terminal voltage` 或 `Position B: power
source independent of generator terminal
conditions`。
## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

具有自动电压调节器的离散时间或连续时间同步电机 ST9C 静态励磁系统

SM ST9C 模块实现符合 IEEE 421.5-2016 [1] 的同步电机型 ST9C 静态
励磁系统模型。

使用此模块对同步电机励磁电压的控制和调节进行建模。

使用 **Sample time (-1 for inherited)** 参数在模块的连续实现和离散实现之间
切换。要将积分器配置为连续时间，请将 **Sample time (-1 for
inherited)** 参数设置为 `0`。要将积分器
配置为离散时间，请将 **Sample time (-1 for inherited)** 参数
设置为正标量。要从上游模块继承采样时间，请将
**Sample time (-1 for inherited)** 参数设置为
`-1`。

SM ST9C 模块包含四个主要组件：

- Current Compensator 组件根据机端电流修改测量的机端电压。
- Voltage Measurement Transducer 组件使用低通滤波器模拟
  机端电压变送器的动态特性。
- Excitation Control Elements 组件将电压变送器
  输出与机端电压参考进行比较，以产生电压误差值。
  该组件随后将此值通过电压调节器以产生
  励磁电压。
- Power Source 组件对受控整流器的电源进行建模，当其独立于
  机端电压时。

此图显示了 ST9C 励磁系统
模型的结构：

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

该模块将电压测量变送器实现为 Low-Pass
Filter 模块，其时间常数为
*TR*。有关精确的离散和连续
实现的信息，请参阅 Low-Pass Filter 模块的文档。

### Excitation Control Elements

此图展示了励磁控制元件的结构：

图中：

- 补偿电压 *Vc* 路径中的微分环节使调节器在电压大幅变化时能够更快响应。Saturation 模块用于消除 *Vc* 小幅变化时微分环节的影响，其 **Upper limit** 和 **Lower limit** 参数等于 Z\_A，即 **Dead-band for differential part influence on AVR, Z\_A (1)** 参数的值。
- Summation Point Logic 子系统用于建模过励限制器（OEL）和欠励限制器（UEL）电压的求和点输入位置。有关将此模块与限制器配合使用的更多信息，请参阅 Field Current Limiters。
- 有两个 Take-over Logic 子系统。这些子系统用于建模 OEL、UEL 和 SCL 的接管点输入位置。有关将此模块与限制器配合使用的更多信息，请参阅 Field Current Limiters。
- Low-Pass Filter 模块用于建模功率变换器级，其中 **Power converter gain (proportional to supply voltage), K\_AS (pu)** 和 **Equivalent time constant of power converter firing control, T\_AS (s)** 分别为增益和时间常数。时间常数 *TAS* 表示门控单元和功率变换器的总延迟。增益 *KAS* 与为功率变换器供电的电力变压器二次电压成正比。
- UEL 是一个具有自身比例增益的 PI 调节器。该 PI 调节器与 AVR 共享积分路径。积分时间常数取决于 UEL 和 AVR 的误差信号。AVR 误差信号与来自 UEL 模型的 **V\_UEL** 信号之间差值的符号指示 UEL 或 AVR 哪个处于活动状态。
- **Power source selector** 参数控制受控整流器电源的来源。该子系统将电压调节器指令信号 *VR* 乘以励磁机励磁电压 *VB*。有关受控整流器电源逻辑开关的更多信息，请参阅 Power Source。

### Field Current Limiters

您可以使用不同类型的励磁电流限制器，在不安全运行条件下修改电压调节器的输出：

- 使用过励限制器防止因励磁电流需求过大而导致励磁绕组过热。
- 使用欠励限制器在励磁过低时提升励磁，因为过低会有失步风险。
- 使用定子电流限制器防止因电流过大而导致定子绕组过热。

将上述任一限制器的输出连接到以下任一位置：

- 求和点 — 将限制器用作自动电压调节器（AVR）反馈回路的一部分。
- 接管点 — 覆盖 AVR 的通常行为。

如果您在求和点使用定子电流限制器，请使用输入 *VSCLsum*。如果您在接管点使用定子电流限制器，请使用过励输入 *VSCLoel* 和欠励输入 *VSCLuel*。

### Power Source

您可以通过设置 **Switch to select exciter supply configuration** 参数值，为受控整流器使用不同的电源表示。若要从机端电压获得受控整流器的电源，请将 **Switch to select exciter supply configuration** 参数设置为 `Position A: power source derived from generator terminal voltage`。若要指定电源独立于机端电压，请将 **Switch to select exciter supply configuration** 参数设置为 `Position B: power source independent of generator terminal conditions`。

此图展示了一个利用机端电压 *VT* 和机端电流 *IT* 的相量组合来建模励磁电源的模型：
