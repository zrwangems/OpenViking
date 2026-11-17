---
type: simulink-block
title: 'SM AC5C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smac5c'
documentation_source_path: 'ref/smac5c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM AC5C

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
  summary: 过励限制器接管定子电流限制标量
  direction: input
  data_types: single | double
- name: V_SCLuel
  summary: 欠励限制器接管定子电流限制标量
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

使用求和点时来自定子电流限制器的输入，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations
  (V\_SCL)** 设置为
  `Unused`。
- 要在求和点使用来自定子电流限制器的输入，请将 **Alternate SCL input
  locations (V\_SCL)** 设置为
  `Summation point`。

**数据类型：** `single` | `double`

### **V\_SCLoel** — 过励限制器接管定子电流限制标量

使用接管点时来自定子电流限制器的输入，用于防止励磁过励，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations
  (V\_SCL)** 设置为
  `Unused`。
- 要在接管点使用来自定子电流限制器的输入，请将 **Alternate SCL input
  locations (V\_SCL)** 设置为
  `Take-over`。

**数据类型：** `single` | `double`

### **V\_SCLuel** — 欠励限制器接管定子电流限制标量

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

同步电机的测量标幺值励磁电流，指定为标量。

**数据类型：** `single` | `double`
### 输出

### **Efd\_pu** — 励磁电压标量

施加到同步电机励磁电路的标幺值励磁电压，以标量形式返回。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Initial field voltage, Efd0 (pu)
  summary: 初始输出电压 1（默认）| 实数
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
- name: Regulator output gain, K_A (pu)
  summary: 调节器增益 400（默认）| 正数
  group: 控制
- name: Regulator output time constant, T_A (s)
  summary: 调节器时间常数 0.02（默认）| 正数
  group: 控制
- name: Maximum regulator output, V_Amax (pu)
  summary: 调节器输出上限 7.3（默认）| 实数
  group: 控制
- name: Minimum regulator output, V_Amin (pu)
  summary: 调节器输出下限 -7.3（默认）| 实数
  group: 控制
- name: Rate feedback excitation system stabilizer gain, K_F (pu)
  summary: 速率反馈增益 0.03（默认）| 正数
  group: 控制
- name: Rate feedback excitation system stabilizer time constant, T_F1 (s)
  summary: 速率反馈时间常数 1（默认）| 正数
  group: 控制
- name: Rate feedback excitation system stabilizer time constant, T_F2 (s)
  summary: 速率反馈时间常数 0（默认）| 正数
  group: 控制
- name: Rate feedback excitation system stabilizer time constant, T_F3 (s)
  summary: 速率反馈时间常数 0（默认）| 正数
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
- name: Exciter field proportional constant, K_E (pu)
  summary: 励磁机磁场增益 1（默认）| 正数
  group: 励磁机
- name: Exciter field time constant, T_E (s)
  summary: 励磁机磁场时间常数 0.8（默认）| 正数
  group: 励磁机
- name: Rectifier loading factor proportional to commutating reactance, K_C (pu)
  summary: 整流器负载因数 0（默认）| 正数
  group: 励磁机
- name: Demagnetizing factor, function of exciter alternator reactances, K_D (pu)
  summary: 去磁因数 0（默认）| 正数
  group: 励磁机
- name: Exciter output voltage for saturation factor S_E(E_1), E_1 (pu)
  summary: 第一饱和输出电压 5.6（默认）| 正数
  group: 励磁机
- name: Exciter saturation factor at exciter output voltage E_1, S_E(E_1) (1)
  summary: 第一饱和查找电压 0.86（默认）| 正数
  group: 励磁机
- name: Exciter output voltage for saturation factor S_E(E_2), E_2 (pu)
  summary: 第二饱和输出电压 4.2（默认）| 正数
  group: 励磁机
- name: Exciter saturation factor at exciter output voltage E_2, S_E(E_2) (1)
  summary: 第二饱和查找电压 0.5（默认）| 正数
  group: 励磁机
- name: Maximum exciter field current limit reference, V_FEmax (pu)
  summary: 励磁机上限 99（默认）| 实数
  group: 励磁机
- name: Minimum exciter voltage output, V_Emin (pu)
  summary: 励磁机下限 0（默认）| 实数
  group: 励磁机
```

### 常规

### **Initial field voltage, Efd0 (pu)** — 初始输出电压 `1`（默认）| 实数

施加到同步电机励磁电路的初始标幺值电压。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。
有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请将此参数设置为 `-1`。
对于离散时间操作，请将此参数设置为正整数。对于连续时间操作，请将此参数设置为 `0`。

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

### **Regulator output gain, K\_A (pu)** — 调节器增益 `400`（默认）| 正数

与电压调节器相关的增益。

### **Regulator output time constant, T\_A (s)** — 调节器时间常数 `0.02`（默认）| 正数

电压调节器的主要时间常数。

### **Maximum regulator output, V\_Amax (pu)** — 调节器输出上限 `7.3`（默认）| 实数

调节器的最大标幺值输出电压。

### **Minimum regulator output, V\_Amin (pu)** — 调节器输出下限 `-7.3`（默认）| 实数

调节器的最小标幺值输出电压。

### **Rate feedback excitation system stabilizer gain, K\_F (pu)** — 速率反馈增益 `0.03`（默认）| 正数

用于稳定励磁系统的速率反馈模块增益。

### **Rate feedback excitation system stabilizer time constant, T\_F1 (s)** — 速率反馈时间常数 `1`（默认）| 正数

用于稳定励磁系统的速率反馈模块时间常数。

### **Rate feedback excitation system stabilizer time constant, T\_F2 (s)** — 速率反馈时间常数 `0`（默认）| 正数

用于稳定励磁系统的速率反馈模块时间常数。

### **Rate feedback excitation system stabilizer time constant, T\_F3 (s)** — 速率反馈时间常数 `0`（默认）| 正数

用于稳定励磁系统的速率反馈模块时间常数。

### **Alternate OEL input locations (V\_OEL)** — OEL 输入位置 `Unused`（默认）| `Summation point` | `Take-over`

过励限制器输入的位置。

### **Alternate UEL input locations (V\_UEL)** — UEL 输入位置 `Unused`（默认）| `Summation point` | `Take-over`

欠励限制器输入的位置。

### **Alternate SCL input locations (V\_SCL)** — SCL 输入位置 `Unused`（默认）| `Summation point` | `Take-over`

定子电流限制器输入的位置：

- 如果选择 `Summation point`，
  请使用 **V\_SCLsum** 输入端口。
- 如果选择 `Take-over`，请使用
  **V\_SCLoel** 和
  **V\_SCLuel** 输入端口。

### 励磁机

### **Exciter field proportional constant, K\_E (pu)** — 励磁机磁场增益 `1`（默认）| 正数

励磁机磁场的比例常数。

### **Exciter field time constant, T\_E (s)** — 励磁机磁场时间常数 `0.8`（默认）| 正数

励磁机磁场的时间常数。

### **Rectifier loading factor proportional to commutating reactance, K\_C (pu)** — 整流器负载因数 `0`（默认）| 正数

与换相电抗成比例的整流器负载因数。

### **Demagnetizing factor, function of exciter alternator reactances, K\_D (pu)** — 去磁因数 `0`（默认）| 正数

与励磁机交流发电机电抗相关的去磁因数。

### **Exciter output voltage for saturation factor S\_E(E\_1), E\_1 (pu)** — 第一饱和输出电压 `5.6`（默认）| 正数

第一饱和因数的励磁机输出电压。

### **Exciter saturation factor at exciter output voltage E\_1, S\_E(E\_1) (1)** — 第一饱和查找电压 `0.86`（默认）| 正数

第一励磁机的饱和因数。

### **Exciter output voltage for saturation factor S\_E(E\_2), E\_2 (pu)** — 第二饱和输出电压 `4.2`（默认）| 正数

第二饱和因数的励磁机输出电压。

### **Exciter saturation factor at exciter output voltage E\_2, S\_E(E\_2) (1)** — 第二饱和查找电压 `0.5`（默认）| 正数

第二励磁机的饱和因数。

### **Maximum exciter field current limit reference, V\_FEmax (pu)** — 励磁机上限 `99`（默认）| 实数

最大标幺值励磁电流限制参考值。

### **Minimum exciter voltage output, V\_Emin (pu)** — 励磁机下限 `0`（默认）| 实数

最小标幺值励磁机电压输出。
## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

离散时间或连续时间同步电机 AC5C 励磁系统，包括自动电压调节器和励磁机

SM AC5C 模块实现了符合 IEEE 421.5-2016[1] 的同步电机 AC5C 型励磁系统模型。

使用此模块可对作为发电机运行并使用交流旋转励磁机的同步电机的励磁电压进行控制和调节建模。

您可以使用 **Sample time (-1 for inherited)** 参数在模块的连续实现和离散实现之间切换。要将积分器配置为连续时间，请将 **Sample time (-1 for
inherited)** 属性设置为 `0`。要将积分器配置为离散时间，请将 **Sample time (-1 for inherited)** 属性设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。

SM AC5C 模块由四个主要组件组成：

- 电流补偿器根据机端电流修改测量的机端电压。
- 电压测量传感器使用低通滤波器模拟机端电压传感器的动态特性。
- 励磁控制元件组件将电压传感器输出与机端电压参考值进行比较，以产生电压误差。该电压误差随后通过电压调节器产生励磁机磁场电压。
- 交流旋转励磁机对交流旋转励磁机进行建模，该励磁机产生施加到受控同步电机的励磁电压。该模块还将励磁机磁场电流（标准符号为 *VFE*）反馈到励磁系统。

下图显示了 AC5C 励磁系统模型的整体结构：

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
- *EFE* 和
  *VFE* 分别是励磁机磁场
  电压和电流。
- *EFD* 和
  *IFD* 分别是磁场电压
  和电流。

以下各节详细描述了模块的每个主要部分。

### 电流补偿器和电压测量传感器

电流补偿器建模为：

VC1=VT+ITRC2+XC2，

其中：

- *RC* 是负载补偿
  电阻。
- *XC* 是负载补偿
  电抗。

电压测量传感器实现为时间常数为
*TR* 的低通滤波器模块。有关离散和连续实现，请参阅此模块的文档。

### 励磁控制元件

下图说明了励磁控制元件的整体结构：

图中：

- Summation Point Logic 子系统对过励限制器 (OEL)、欠励限制器 (UEL) 和定子电流限制器 (SCL) 电压的求和点输入位置进行建模。有关在此模块中使用限制器的详细信息，请参阅励磁电流限制器。
- Low-Pass Filter 模块对电压调节器的主要动态特性进行建模。其中，*KA* 是
  调节器增益，*TA* 是
  调节器的主要时间常数。该模块的最小和最大
  抗积分饱和限制分别为
  *VAmin* 和
  *VAmax*。
- Filtered Derivative 和 Lead-Lag 模块对用于稳定励磁系统的速率反馈路径进行建模。其中，
  *KF* 是该系统的增益，
  *TF1*、
  *TF2* 和 *TF3* 是其时间
  常数。有关离散和连续实现，请参阅 Filtered Derivative 模块的文档。
- Take-over Logic 子系统对 OEL、UEL 和 SCL 电压的接管点输入位置进行建模。有关在此模块中使用限制器的详细信息，请参阅励磁电流限制器。
- **initialOffset** Constant 模块确保仿真可以从稳态开始。SM AC5C 模块通过使用饱和和励磁机参数（包括初始励磁电压和调节器输出增益）来计算此值。

### 励磁电流限制器

您可以使用各种励磁电流限制器在不安全运行条件下修改电压调节器的输出：

- 使用过励限制器防止因过大的励磁电流需求导致磁场绕组过热。
- 使用欠励限制器在励磁过低时提升励磁，因为励磁过低存在失步风险。
- 使用定子电流限制器防止因电流过大导致定子绕组过热。

将任何这些限制器的输出连接到以下位置之一：

- 求和点，作为自动电压调节器 (AVR) 反馈回路的一部分
- 接管点，以覆盖 AVR 的常规行为

如果在求和点使用定子电流限制器，请使用单个输入 *VSCLsum*。如果在接管点使用定子电流限制器，请同时使用过励输入 *VSCLoel* 和欠励输入 *VSCLuel*。

### AC Rotating Exciter

此图展示了交流旋转励磁机的结构：

图中：

- 励磁机励磁电流
  *VFE* 是三个信号之和：

  - 非线性函数
    *Vx*
    对励磁机输出电压的饱和进行建模。
  - 比例项
    *KE*
    对励磁机输出电压与励磁机励磁电流之间的线性关系进行建模。
  - 该子系统使用反馈回路中的去磁常数
    *KD* 对负载电流对励磁机输出电压的去磁效应进行建模。
- Integrator with variable limits
  子系统对
  *EFE* 与
  *VFE* 之间的差值进行积分，以生成励磁机交流发电机输出电压
  *VE*。
  *TE* 是该过程的时间常数。
- 非线性函数
  *FEX*
  对整流器调节引起的励磁机输出电压降进行建模。该函数取决于常数
  *KC*，
  而该常数本身是换相电抗的函数。
- 参数
  *VEmin*
  和
  *VFEmax*
  对旋转励磁机的下限和上限进行建模。
