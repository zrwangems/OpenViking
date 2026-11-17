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

施加到同步电机励磁绕组的标幺值励磁电压，以标量形式返回。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Initial field voltage, Efd0 (pu)
  summary: 初始输出电压 1（默认值）| 实数
  group: 常规
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 -1（默认值）| 0 | 正标量
  group: 常规
- name: Resistive component of load compensation, R_C (pu)
  summary: 补偿电阻 0（默认值）| 正数
  group: 预控制
- name: Reactance component of load compensation, X_C (pu)
  summary: 补偿电抗 0（默认值）| 正数
  group: 预控制
- name: Regulator input filter time constant, T_R (s)
  summary: 调节器时间常数 0（默认值）| 正数
  group: 预控制
- name: Voltage regulator proportional gain, K_PR (pu)
  summary: 电压调节器的比例增益 1（默认值）
  group: 控制
- name: Voltage regulator integral gain, K_IR (pu/s)
  summary: 电压调节器的积分增益 0（默认值）
  group: 控制
- name: Voltage regulator derivative gain, K_DR (pu.s)
  summary: 电压调节器的微分增益 0（默认值）
  group: 控制
- name: Lag time constant for derivative channel of PID controller, T_DR (s)
  summary: PID 微分通道的滞后时间常数 1（默认值）| 正数
  group: 控制
- name: Maximum PID regulator output, V_PIDmax (pu)
  summary: PID 调节器的最大输出 3.2（默认值）| 正数
  group: 控制
- name: Minimum PID regulator output, V_PIDmin (pu)
  summary: PID 调节器的最小输出 -3.2（默认值）| 正数
  group: 控制
- name: Regulator denominator (lag) time constant, T_B (s)
  summary: 调节器滞后时间常数 0（默认值）| 正数
  group: 控制
- name: Regulator numerator (lead) time constant, T_C (s)
  summary: 调节器超前时间常数 0（默认值）| 正数
  group: 控制
- name: Regulator output gain, K_A (pu)
  summary: 调节器增益 45.62（默认值）| 正数
  group: 控制
- name: Regulator output time constant, T_A (s)
  summary: 调节器时间常数 0.013（默认值）| 正数
  group: 控制
- name: Maximum regulator output, V_Amax (pu)
  summary: 调节器输出的上限 1（默认值）| 实数
  group: 控制
- name: Minimum regulator output, V_Amin (pu)
  summary: 调节器输出的下限 -0.95（默认值）| 实数
  group: 控制
- name: Rate feedback time constant, T_F (s)
  summary: 速率反馈时间常数 1（默认值）| 正数
  group: 控制
- name: Value of EFD at which feedback gain changes, E_FDN (pu)
  summary: 反馈增益变化时的 EFD 值 2.36（默认值）| 正数
  group: 控制
- name: Rate feedback excitation system stabilizer gain, K_F (pu)
  summary: 速率反馈增益 0.143（默认值）| 正数
  group: 控制
- name: Rate feedback excitation system stabilizer gain, K_N (pu)
  summary: 速率反馈增益 0.05（默认值）| 正数
  group: 控制
- name: Alternate OEL input locations (V_OEL)
  summary: OEL 输入位置 Unused（默认值）| Summation point | Take-over
  group: 控制
- name: Alternate UEL input locations (V_UEL)
  summary: UEL 输入位置 Unused（默认值）| Summation point | Take-over
  group: 控制
- name: Alternate SCL input locations (V_SCL)
  summary: SCL 输入位置 Unused（默认值）| Summation point | Take-over
  group: 控制
- name: Exciter field proportional constant, K_E (pu)
  summary: 励磁机励磁增益 1（默认值）| 正数
  group: 励磁机
- name: Exciter field time constant, T_E (s)
  summary: 励磁机励磁时间常数 0.17（默认值）| 正数
  group: 励磁机
- name: Rectifier loading factor proportional to commutating reactance, K_C (pu)
  summary: 整流器负载因数 0.104（默认值）| 正数
  group: 励磁机
- name: Demagnetizing factor, function of exciter alternator reactances, K_D (pu)
  summary: 去磁因数 0.499（默认值）| 正数
  group: 励磁机
- name: Exciter output voltage for saturation factor S_E(E_1), E_1 (pu)
  summary: 第一饱和输出电压 6.24（默认值）| 正数
  group: 励磁机
- name: Exciter saturation factor at exciter output voltage E_1, S_E(E_1) (1)
  summary: 第一饱和查找电压 1.143（默认值）| 正数
  group: 励磁机
- name: Exciter output voltage for saturation factor S_E(E_2), E_2 (pu)
  summary: 第二饱和输出电压 4.68（默认值）| 正数
  group: 励磁机
- name: Exciter saturation factor at exciter output voltage E_2, S_E(E_2) (1)
  summary: 第二饱和查找电压 0.1（默认值）| 正数
  group: 励磁机
- name: Gain associated with regulator and alternator field power supply, K_R (pu)
  summary: 调节器和交流发电机励磁电源增益 3.77（默认值）| 实数
  group: 励磁机
- name: Minimum exciter voltage output, V_Emin (pu)
  summary: 励磁机下限 0.1（默认值）| 实数
  group: 励磁机
- name: Exciter field current limit, V_FEmax (pu)
  summary: 励磁机上限 16（默认值）| 实数
  group: 励磁机
```

### 常规

### **Initial field voltage, Efd0 (pu)** — 初始输出电压 `1`（默认值）| 实数

施加到同步电机励磁绕组的初始标幺值电压。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认值）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。
有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请将此参数设置为 `-1`。
对于离散时间操作，请将此参数设置为正整数。对于连续时间操作，请将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

### 预控制

### **Resistive component of load compensation, R\_C (pu)** — 补偿电阻 `0`（默认值）| 正数

电流补偿系统中使用的电阻。将此参数和 **Reactance component of load compensation, X\_C
(pu)** 设置为 `0` 以禁用电流补偿。

### **Reactance component of load compensation, X\_C (pu)** — 补偿电抗 `0`（默认值）| 正数

电流补偿系统中使用的电抗。将此参数和 **Resistive component of load compensation, R\_C
(pu)** 设置为 `0` 以禁用电流补偿。

### **Regulator input filter time constant, T\_R (s)** — 调节器时间常数 `0`（默认值）| 正数

电压变送器滤波的等效时间常数。

### 控制

### **Voltage regulator proportional gain, K\_PR (pu)** — 电压调节器的比例增益 `1`（默认值）

电压调节器的标幺值比例增益。

### **Voltage regulator integral gain, K\_IR (pu/s)** — 电压调节器的积分增益 `0`（默认值）

电压调节器的标幺值每秒积分增益。

### **Voltage regulator derivative gain, K\_DR (pu.s)** — 电压调节器的微分增益 `0`（默认值）

电压调节器的微分增益。

### **Lag time constant for derivative channel of PID controller, T\_DR (s)** — PID 微分通道的滞后时间常数 `1`（默认值）| 正数

PID 控制器微分通道的等效滞后时间常数。

### **Maximum PID regulator output, V\_PIDmax (pu)** — PID 调节器的最大输出 `3.2`（默认值）| 正数

PID 调节器的最大允许标幺值输出。

### **Minimum PID regulator output, V\_PIDmin (pu)** — PID 调节器的最小输出 `-3.2`（默认值）| 正数

PID 调节器的最小允许标幺值输出。

### **Regulator denominator (lag) time constant, T\_B (s)** — 调节器滞后时间常数 `0`（默认值）| 正数

电压调节器中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **Regulator numerator (lead) time constant, T\_C (s)** — 调节器超前时间常数 `0`（默认值）| 正数

电压调节器中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **Regulator output gain, K\_A (pu)** — 调节器增益 `45.62`（默认值）| 正数

与电压调节器相关的增益。

### **Regulator output time constant, T\_A (s)** — 调节器时间常数 `0.013`（默认值）| 正数

电压调节器的主要时间常数。

### **Maximum regulator output, V\_Amax (pu)** — 调节器输出的上限 `1`（默认值）| 实数

调节器的最大标幺值输出电压。

### **Minimum regulator output, V\_Amin (pu)** — 调节器输出的下限 `-0.95`（默认值）| 实数

调节器的最小标幺值输出电压。

### **Rate feedback time constant, T\_F (s)** — 速率反馈时间常数 `1`（默认值）| 正数

用于励磁系统稳定的速率反馈模块时间常数。

### **Value of EFD at which feedback gain changes, E\_FDN (pu)** — 反馈增益变化时的 EFD 值 `2.36`（默认值）| 正数

反馈增益变化时的 EFD 标幺值。

### **Rate feedback excitation system stabilizer gain, K\_F (pu)** — 速率反馈增益 `0.143`（默认值）| 正数

用于励磁系统稳定的速率反馈模块增益。

### **Rate feedback excitation system stabilizer gain, K\_N (pu)** — 速率反馈增益 `0.05`（默认值）| 正数

用于励磁系统稳定的速率反馈模块增益。

### **Alternate OEL input locations (V\_OEL)** — OEL 输入位置 `Unused`（默认值）| `Summation point` | `Take-over`

过励限制器输入的位置。

### **Alternate UEL input locations (V\_UEL)** — UEL 输入位置 `Unused`（默认值）| `Summation point` | `Take-over`

欠励限制器输入的位置。

### **Alternate SCL input locations (V\_SCL)** — SCL 输入位置 `Unused`（默认值）| `Summation point` | `Take-over`

定子电流限制器输入的位置：

- 如果选择 `Summation point`，请使用 **V\_SCLsum** 输入端口。
- 如果选择 `Take-over`，请使用 **V\_SCLoel** 和 **V\_SCLuel** 输入端口。

### 励磁机

### **Exciter field proportional constant, K\_E (pu)** — 励磁机励磁增益 `1`（默认值）| 正数

励磁机励磁的比例常数。

### **Exciter field time constant, T\_E (s)** — 励磁机励磁时间常数 `0.17`（默认值）| 正数

励磁机励磁的时间常数。

### **Rectifier loading factor proportional to commutating reactance, K\_C (pu)** — 整流器负载因数 `0.104`（默认值）| 正数

与换相电抗成比例的整流器负载因数。

### **Demagnetizing factor, function of exciter alternator reactances, K\_D (pu)** — 去磁因数 `0.499`（默认值）| 正数

与励磁机交流发电机各电抗相关的去磁因数。

### **Exciter output voltage for saturation factor S\_E(E\_1), E\_1 (pu)** — 第一饱和输出电压 `6.24`（默认值）| 正数

第一饱和因数对应的励磁机输出电压。

### **Exciter saturation factor at exciter output voltage E\_1, S\_E(E\_1) (1)** — 第一饱和查找电压 `1.143`（默认值）| 正数

第一励磁机的饱和因数。

### **Exciter output voltage for saturation factor S\_E(E\_2), E\_2 (pu)** — 第二饱和输出电压 `4.68`（默认值）| 正数

第二饱和因数对应的励磁机输出电压。

### **Exciter saturation factor at exciter output voltage E\_2, S\_E(E\_2) (1)** — 第二饱和查找电压 `0.1`（默认值）| 正数

第二励磁机的饱和因数。

### **Gain associated with regulator and alternator field power supply, K\_R (pu)** — 调节器和交流发电机励磁电源增益 `3.77`（默认值）| 实数

调节器和交流发电机励磁电源的标幺值增益。

### **Minimum exciter voltage output, V\_Emin (pu)** — 励磁机下限 `0.1`（默认值）| 实数

励磁机的最小标幺值电压输出。

### **Exciter field current limit, V\_FEmax (pu)** — 励磁机上限 `16`（默认值）| 实数

励磁机励磁电流的标幺值上限。
## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

离散时间或连续时间同步电机 AC3C 励磁系统，包括自动电压调节器和励磁机

SM AC3C 模块实现符合 IEEE 421.5-2016[1] 的同步电机 AC3C 型励磁系统模型。

使用此模块可对作为发电机运行、使用交流旋转励磁机的同步电机的励磁电压进行控制和调节建模。

您可以使用 **Sample time (-1 for inherited)** 参数在模块的连续实现和离散实现之间切换。要将积分器配置为连续时间，请将 **Sample time (-1 for
inherited)** 属性设置为 `0`。要将积分器配置为离散时间，请将 **Sample time (-1 for inherited)** 属性设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。

SM AC3C 模块由四个主要组件组成：

- 电流补偿器根据机端电流修改测量的机端电压。
- 电压测量变送器使用低通滤波器模拟机端电压变送器的动态特性。
- 励磁控制元件组件将电压变送器输出与机端电压参考进行比较，产生电压误差。该电压误差随后通过电压调节器产生励磁机励磁电压。
- 交流旋转励磁机对交流旋转励磁机建模，其产生施加到受控同步电机的励磁电压。该模块还将励磁机励磁电流（标准符号为 *VFE*）反馈到励磁系统。

下图显示了 AC3C 励磁系统模型的整体结构：

图中：

- *VT* 和 *IT* 分别是同步电机的测量机端电压和电流。
- *VC1* 是电流补偿后的机端电压。
- *VC* 是滤波后的电流补偿机端电压。
- *VREF* 是参考机端电压。
- *VS* 是电力系统稳定器电压。
- *EFE* 和 *VFE* 分别是励磁机励磁电压和电流。
- *EFD* 和 *IFD* 分别是励磁电压和电流。

以下各节详细描述模块的每个主要部分。

### 电流补偿器和电压测量变送器

电流补偿器建模为：

VC1=VT+ITRC2+XC2，

其中：

- *RC* 是负载补偿电阻。
- *XC* 是负载补偿电抗。

电压测量变送器实现为时间常数为 *TR* 的低通滤波器模块。有关离散和连续实现，请参阅此模块的文档。

### Excitation Control Elements

此图展示了励磁控制元件的整体结构：

图中：

- Summation Point Logic 子系统为过励限制器（OEL）、欠励限制器（UEL）和定子电流限制器（SCL）电压建模了求和点输入位置。有关将此模块与限制器配合使用的详细信息，请参阅 Field Current Limiters。
- PID\_R 子系统为 PID 控制器建模，它允许表示改造项目，即在励磁机中添加现代数字励磁调节器。通过调节 PID 参数，可以建模 SM AC3A 励磁系统模型。
- Lead-Lag 模块为电压调节器的附加动态特性建模。此处，*TC* 为超前时间常数，*TB* 为滞后时间常数。有关 Lead-Lag 模块的离散和连续实现，请参阅其文档。
- Take-over Logic 子系统为 OEL、UEL 和 SCL 电压建模了接管点输入位置。有关将此模块与限制器配合使用的详细信息，请参阅 Field Current Limiters。
- Low-Pass Filter 模块为电压调节器的主要动态特性建模。此处，*KA* 为调节器增益，*TA* 为调节器的主要时间常数。该模块的最小和最大抗积分饱和限幅分别为 *VAmin* 和 *VAmax*。
- 电压调节器功率来自励磁机输出电压。电压调节器指令信号 *VA* 乘以励磁机输出电压 *EFD*，再乘以 *KR*。这为系统增加了一定程度的非线性。
- Filtered Derivative 模块为用于励磁系统稳定化的速率反馈路径建模。在这种情况下，稳定器具有非线性特性。如果励磁机输出电压 *EFD* 小于 **Value of EFD at which feedback gain changes, E\_FDN (pu)** 参数，则反馈增益为 *KF*。如果励磁机输出电压大于 **Value of EFD at which feedback gain changes, E\_FDN (pu)** 参数，则反馈增益为 *KN*。有关 Filtered Derivative 模块的确切离散和连续实现，请参阅其文档。
- *EFEmin* 和 *EFEmax* 分别为输出励磁机磁场电压 *EFE* 的最小和最大饱和限值。

### Field Current Limiters

您可以使用各种磁场电流限制器在不安全运行条件下修改电压调节器的输出：

- 使用过励限制器防止因过大的磁场电流需求导致磁场绕组过热。
- 使用欠励限制器在励磁过低时提升励磁，因为过低励磁存在失步风险。
- 使用定子电流限制器防止因过大电流导致定子绕组过热。

将上述任一限制器的输出连接到以下任一位置：

- 求和点，作为自动电压调节器（AVR）反馈回路的一部分
- 接管点，以覆盖 AVR 的常规行为

如果在求和点使用定子电流限制器，请使用单输入 *VSCLsum*。如果在接管点使用定子电流限制器，请同时使用过励输入 *VSCLoel* 和欠励输入 *VSCLuel*。

### AC Rotating Exciter

此图展示了交流旋转励磁机的结构：

图中：

- 励磁机磁场电流 *VFE* 是三个信号之和：

  - 非线性函数 *Vx* 为励磁机输出电压的饱和建模。
  - 比例项 *KE* 为励磁机输出电压与励磁机磁场电流之间的线性关系建模。
  - 该子系统使用反馈回路中的去磁常数 *KD* 为负载电流对励磁机输出电压的去磁效应建模。
- Integrator with variable limits 子系统对 *EFE* 与 *VFE* 之差进行积分，以生成励磁机交流发电机输出电压 *VE*。*TE* 为此过程的时间常数。
- 非线性函数 *FEX* 为整流器调节引起的励磁机输出电压降建模。此函数取决于常数 *KC*，而 *KC* 本身是换相电抗的函数。
- 参数 *VEmin* 和 *VFEmax* 为旋转励磁机的下限和上限建模。
