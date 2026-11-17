---
type: simulink-block
title: 'SM ST2C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smst2c'
documentation_source_path: 'ref/smst2c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM ST2C

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
  summary: 接管点定子电流限制（OEL）标量
  direction: input
  data_types: single | double
- name: V_SCLuel
  summary: 接管点定子电流限制（UEL）标量
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

在求和点使用定子电流限制器时来自定子电流限制器的输入，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations
  (V\_SCL)** 设置为
  `Unused`。
- 要在求和点使用来自定子电流限制器的输入，请将 **Alternate SCL input
  locations (V\_SCL)** 设置为
  `Summation point`。

**数据类型：** `single` | `double`

### **V\_SCLoel** — 接管点定子电流限制（OEL）标量

在接管点使用时防止励磁过励的来自定子电流限制器的输入，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations
  (V\_SCL)** 设置为
  `Unused`。
- 要在接管点使用来自定子电流限制器的输入，请将 **Alternate SCL input
  locations (V\_SCL)** 设置为
  `Take-over`。

**数据类型：** `single` | `double`

### **V\_SCLuel** — 接管点定子电流限制（UEL）标量

在接管点使用时防止励磁欠励的来自定子电流限制器的输入，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations
  (V\_SCL)** 设置为
  `Unused`。
- 要在接管点使用来自定子电流限制器的输入，请将 **Alternate SCL input
  locations (V\_SCL)** 设置为
  `Take-over`。

**数据类型：** `single` | `double`

### **Ifd\_pu** — 测量的励磁电流标量

同步电机的测量标幺励磁电流。

**数据类型：** `single` | `double`
### 输出

### **Efd\_pu** — 励磁电压标量

要施加到同步电机励磁电路的标幺励磁电压，以标量形式返回。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Initial field voltage, Efd0 (pu)
  summary: 初始输出电压 1（默认）| 实数
  group: 常规
- name: Initial terminal voltage, Vt0 (pu)
  summary: 初始机端电压 1（默认）| 实数
  group: 常规
- name: Initial terminal current, It0 (pu)
  summary: 初始机端电流 1（默认）| 实数
  group: 常规
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 -1（默认）| 0 | 正标量
  group: 常规
- name: Resistive component of load compensation, R_C (pu)
  summary: 补偿电阻 0（默认）| 正数
  group: 预控制
- name: Reactance component of load compensation, X_C (pu)
  summary: 补偿电抗 0（默认）| 正数
  group: 预控制
- name: Regulator input filter time constant, T_R (s)
  summary: 调节器时间常数 0（默认）| 正数
  group: 预控制
- name: Voltage regulator proportional gain, K_PR (pu)
  summary: 调节器比例增益 1（默认）| 正数
  group: 控制
- name: Voltage regulator integral gain, K_IR (pu/s)
  summary: 调节器积分增益 0（默认）| 正数
  group: 控制
- name: Maximum voltage regulator output, V_PImax (pu)
  summary: PI 控制调节器输出的上限 99（默认）| 实数
  group: 控制
- name: Minimum voltage regulator output, V_PImin (pu)
  summary: PI 控制调节器输出的下限 -99（默认）| 实数
  group: 控制
- name: Voltage regulator gain, K_A (pu)
  summary: 调节器增益 120（默认）| 正数
  group: 控制
- name: Voltage regulator time constant, T_A (s)
  summary: 调节器时间常数 0.15（默认）| 正数
  group: 控制
- name: Rate feedback gain, K_F (pu)
  summary: 速率反馈增益 0.05（默认）| 正数
  group: 控制
- name: Rate feedback time constant, T_F (s)
  summary: 速率反馈时间常数 1（默认）| 正数
  group: 控制
- name: Maximum regulator output, V_Rmax (pu)
  summary: 调节器输出的上限 1（默认）| 实数
  group: 控制
- name: Minimum regulator output, V_Rmin (pu)
  summary: 调节器输出的下限 0（默认）| 实数
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
  summary: 整流器负载因数 0.1（默认）| 正数
  group: 励磁机
- name: Exciter field proportional constant, K_E (pu)
  summary: 励磁机磁场增益 1（默认）| 正数
  group: 励磁机
- name: Exciter field time constant, T_E (s)
  summary: 励磁机磁场时间常数 0.5（默认）| 正数
  group: 励磁机
- name: Maximum generator field voltage, E_FDmax (pu)
  summary: 发电机励磁电压上限 4.4（默认）| 正数
  group: 励磁机
- name: Potential circuit (voltage) gain coefficient, K_P (pu)
  summary: 电势电路电压增益系数 4.88（默认）| 正数
  group: 励磁机
- name: Compound circuit (current) gain coefficient, K_I (pu)
  summary: 电势电路电流增益系数 0（默认）| 正数
  group: 励磁机
- name: Reactance associated with potential source, X_L (pu)
  summary: 电势源电抗 0（默认）| 正数
  group: 励磁机
- name: Potential circuit phase angle (degrees)
  summary: 电势电路相位角 0（默认）| 正数
  group: 励磁机
- name: Maximum available exciter voltage, V_Bmax (pu)
  summary: 励磁机电压上限 5.2（默认）| 正数
  group: 励磁机
```

### 常规

### **Initial field voltage, Efd0 (pu)** — 初始输出电压 `1`（默认）| 实数

要施加到同步电机励磁电路的初始标幺电压。

### **Initial terminal voltage, Vt0 (pu)** — 初始机端电压 `1`（默认）| 实数

初始标幺机端电压。

### **Initial terminal current, It0 (pu)** — 初始机端电流 `1`（默认）| 实数

初始标幺机端电流。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请将此参数设置为 `-1`。对于离散时间操作，请将此参数设置为正整数。对于连续时间操作，请将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

### 预控制

### **Resistive component of load compensation, R\_C (pu)** — 补偿电阻 `0`（默认）| 正数

电流补偿系统中使用的电阻。将此参数和 **Reactance component of load compensation, X\_C
(pu)** 设置为 `0` 以禁用电流补偿。

### **Reactance component of load compensation, X\_C (pu)** — 补偿电抗 `0`（默认）| 正数

电流补偿系统中使用的电抗。将此参数和 **Resistive component of load compensation, R\_C
(pu)** 设置为 `0` 以禁用电流补偿。

### **Regulator input filter time constant, T\_R (s)** — 调节器时间常数 `0`（默认）| 正数

电压传感器滤波的等效时间常数。

### 控制

### **Voltage regulator proportional gain, K\_PR (pu)** — 调节器比例增益 `1`（默认）| 正数

与电压调节器 PI 控制模块相关联的比例增益。

### **Voltage regulator integral gain, K\_IR (pu/s)** — 调节器积分增益 `0`（默认）| 正数

与电压调节器 PI 控制模块相关联的积分增益。

### **Maximum voltage regulator output, V\_PImax (pu)** — PI 控制调节器输出的上限 `99`（默认）| 实数

调节器 PI 控制模块的最大标幺输出电压。

### **Minimum voltage regulator output, V\_PImin (pu)** — PI 控制调节器输出的下限 `-99`（默认）| 实数

调节器 PI 控制模块的最小标幺输出电压。

### **Voltage regulator gain, K\_A (pu)** — 调节器增益 `120`（默认）| 正数

与电压调节器相关联的增益。

### **Voltage regulator time constant, T\_A (s)** — 调节器时间常数 `0.15`（默认）| 正数

电压调节器的主要时间常数。

### **Rate feedback gain, K\_F (pu)** — 速率反馈增益 `0.05`（默认）| 正数

速率反馈模块增益。

### **Rate feedback time constant, T\_F (s)** — 速率反馈时间常数 `1`（默认）| 正数

速率反馈模块时间常数。

### **Maximum regulator output, V\_Rmax (pu)** — 调节器输出的上限 `1`（默认）| 实数

调节器的最大标幺输出电压。

### **Minimum regulator output, V\_Rmin (pu)** — 调节器输出的下限 `0`（默认）| 实数

调节器的最小标幺输出电压。

### **Alternate OEL input locations (V\_OEL)** — OEL 输入位置 `Unused`（默认）| `Summation point` | `Take-over`

过励限制器输入位置。

### **Alternate UEL input locations (V\_UEL)** — UEL 输入位置 `Unused`（默认）| `Summation point` | `Take-over`

欠励限制器输入位置。

### **Alternate SCL input locations (V\_SCL)** — SCL 输入位置 `Unused`（默认）| `Summation point` | `Take-over`

定子电流限制器输入位置：

- 如果选择 `Summation point`，请使用 **V\_SCLsum** 输入端口。
- 如果选择 `Take-over`，请使用 **V\_SCLoel** 和 **V\_SCLuel** 输入端口。

### 励磁机

### **Rectifier loading factor proportional to commutating reactance, K\_C (pu)** — 整流器负载因数 `0.1`（默认）| 正数

与换相电抗成比例的整流器负载因数。

### **Exciter field proportional constant, K\_E (pu)** — 励磁机磁场增益 `1`（默认）| 正数

励磁机磁场的比例常数。

### **Exciter field time constant, T\_E (s)** — 励磁机磁场时间常数 `0.5`（默认）| 正数

励磁机磁场的时间常数。

### **Maximum generator field voltage, E\_FDmax (pu)** — 发电机励磁电压上限 `4.4`（默认）| 正数

最大标幺发电机励磁电压值。

### **Potential circuit (voltage) gain coefficient, K\_P (pu)** — 电势电路电压增益系数 `4.88`（默认）| 正数

电源电路中的标幺电压增益系数。

### **Compound circuit (current) gain coefficient, K\_I (pu)** — 电势电路电流增益系数 `0`（默认）| 正数

电源电路中的标幺电流增益系数。

### **Reactance associated with potential source, X\_L (pu)** — 电势源电抗 `0`（默认）| 正数

电源电路中的标幺电抗。

### **Potential circuit phase angle (degrees)** — 电势电路相位角 `0`（默认）| 正数

电源电路的相位角，以度为单位。

### **Maximum available exciter voltage, V\_Bmax (pu)** — 励磁机电压上限 `5.2`（默认）| 正数

最大可用标幺励磁机电压值。
## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

具有自动电压调节器的离散时间或连续时间同步电机 ST2C 静态励磁系统

SM ST2C 模块实现符合 IEEE 421.5-2016[1] 的同步电机型 ST2C 静态励磁系统模型。

使用此模块可对同步电机励磁电压的控制和调节进行建模。

您可以使用 **Sample time (-1 for inherited)** 参数在模块的连续实现和离散实现之间切换。要将积分器配置为连续时间，请将 **Sample time (-1 for
inherited)** 属性设置为 `0`。要将积分器配置为离散时间，请将 **Sample time (-1 for inherited)** 属性设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。

SM ST2C 模块包含四个主要组件：

- 电流补偿器根据机端电流修改测量的机端电压。
- 电压测量传感器使用低通滤波器模拟机端电压传感器的动态特性。
- 励磁控制元件组件将电压传感器输出与机端电压参考进行比较以产生电压误差。然后，该电压误差通过电压调节器以产生励磁电压。
- 电源对受控整流器的电源进行建模，当其独立于机端电压时。

此图显示了 ST2C 励磁系统模型的整体结构：

在图中：

- *VT* 和
  *IT* 是同步电机的测量机端电压和电流。
- *VC1* 是电流补偿后的机端电压。
- *VC* 是滤波后的电流补偿机端电压。
- *VREF* 是参考机端电压。
- *VS* 是电力系统稳定器电压。
- *VB* 是励磁机磁场电压。
- *EFD* 和
  *IFD* 分别是励磁电压和励磁电流。

以下各节详细描述了模块的每个主要部分。

### 电流补偿器和电压测量传感器

电流补偿器建模为：

VC1=VT+ITRC2+XC2，

其中：

- *RC* 是负载补偿电阻。
- *XC* 是负载补偿电抗。

电压测量传感器实现为具有时间常数 *TR* 的低通滤波器模块。有关离散和连续实现，请参阅低通滤波器模块的文档。

### 励磁控制元件

此图说明了励磁控制元件的整体结构：

在图中：

- 求和点逻辑子系统对过励限制器（OEL）、欠励限制器（UEL）、定子电流限制器（SCL）和电源开关选择器（V\_S）电压的求和点输入位置进行建模。有关在此模块中使用限制器的详细信息，请参阅励磁电流限制器。
- 接管逻辑子系统对 OEL、UEL 和 SCL 电压的接管点输入位置进行建模。有关在此模块中使用限制器的详细信息，请参阅励磁电流限制器。
- PI 子系统对用作自动电压调节器控制结构的 PI 控制器进行建模，并允许表示使用现代数字控制器的设备改造。该模块的最小和最大抗积分饱和限幅分别为 *VPImin* 和 *VPImax*。
- 低通滤波器模块对电压调节器的主要动态特性进行建模。此处，*KA* 是调节器增益，*TA* 是调节器的主要时间常数。该模块的最小和最大抗积分饱和限幅分别为 *VRmin* 和 *VRmax*。
- 滤波微分模块对用于稳定励磁系统的速率反馈路径进行建模。此处，*KF* 和 *TF* 分别是该系统的增益和时间常数。有关确切的离散和连续实现，请参阅滤波微分模块的文档。
- 积分器模块通过受控饱和控制励磁机输出。参数 *EFDmax* 表示励磁机电压的限制。时间常数 *TE* 与控制绕组的电感相关联。

### 励磁电流限制器

您可以使用各种励磁电流限制器在不安全运行条件下修改电压调节器的输出：

- 使用过励限制器防止因过大的励磁电流需求而导致励磁绕组过热。
- 使用欠励限制器在励磁过低时提升励磁，因为励磁过低存在失步风险。
- 使用定子电流限制器防止因过大电流而导致定子绕组过热。

将这些限制器中任何一个的输出连接到以下点之一：

- 求和点，作为自动电压调节器（AVR）反馈回路的一部分
- 接管点，以覆盖 AVR 的通常行为

如果在求和点使用定子电流限制器，请使用单个输入 *VSCLsum*。如果在接管点使用定子电流限制器，请同时使用过励输入 *VSCLoel* 和欠励输入 *VSCLuel*。

### 电源

某些静态系统同时利用电流源和电压源来生成电源。

此图显示了利用机端电压 *VT* 和机端电流 *IT* 的相量组合的励磁机电源模型：
