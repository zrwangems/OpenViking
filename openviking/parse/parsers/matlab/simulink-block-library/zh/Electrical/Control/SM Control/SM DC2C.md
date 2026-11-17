---
type: simulink-block
title: 'SM DC2C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smdc2c'
documentation_source_path: 'ref/smdc2c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM DC2C

## 端口

### 输入

### **V\_REF** — 电压参考标量

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
  locations (V\_SCL)** 设置为
  `Summation point`。

**数据类型：** `single` | `double`

### **V\_OELscl** — 接管点定子电流限制（OEL）标量

使用接管点时来自定子电流限制器的输入，用于防止励磁过励，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations
  (V\_SCL)** 设置为
  `Unused`。
- 要在接管点使用来自定子电流限制器的输入，请将 **Alternate SCL input
  locations (V\_SCL)** 设置为
  `Take-over`。

**数据类型：** `single` | `double`

### **V\_UELscl** — 接管点定子电流限制（UEL）标量

使用接管点时来自定子电流限制器的输入，用于防止励磁欠励，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations
  (V\_SCL)** 设置为
  `Unused`。
- 要在接管点使用来自定子电流限制器的输入，请将 **Alternate SCL input
  locations (V\_SCL)** 设置为
  `Take-over`。

**数据类型：** `single` | `double`
### 输出

### **Efd\_pu** — 励磁电压标量

要施加到同步电机励磁绕组的标幺值励磁电压，以标量形式返回。

**数据类型：** `single` | `double`

## 参数

### 常规

### **Initial field voltage, Efd0 (pu)** — 初始输出电压 `1`（默认）| 实数

要施加到同步电机励磁绕组的初始标幺值电压。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请将此参数设置为 `-1`。对于离散时间操作，请将此参数设置为正整数。对于连续时间操作，请将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

### 预控制

### **Resistive component of load compensation, R\_C (pu)** — 补偿电阻 `0`（默认）| 正数

电流补偿系统中使用的电阻。将此参数和 **Reactance component of load compensation, X\_C
(pu)** 设置为 `0` 可禁用电流补偿。

### **Reactance component of load compensation, X\_C (pu)** — 补偿电抗 `0`（默认）| 正数

电流补偿系统中使用的电抗。将此参数和 **Resistive component of load compensation, R\_C
(pu)** 设置为 `0` 可禁用电流补偿。

### **Regulator input filter time constant, T\_R (s)** — 调节器时间常数 `0`（默认）| 正数

电压传感器滤波的等效时间常数。

### 控制

### **Regulator output gain, K\_A (pu)** — 调节器增益 `300`（默认）| 正数

与电压调节器相关的增益。

### **Regulator time constant, T\_A (s)** — 调节器时间常数 `0.01`（默认）| 正数

电压调节器的主要时间常数。

### **Regulator denominator (lag) time constant, T\_B (s)** — 调节器滞后时间常数 `0`（默认）| 正数

电压调节器中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **Regulator numerator (lead) time constant, T\_C (s)** — 调节器超前时间常数 `0`（默认）| 正数

电压调节器中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **Rate feedback gain, K\_F (pu)** — 速率反馈增益 `0.02`（默认）| 正数

用于稳定励磁系统的速率反馈模块增益。

### **Rate feedback time constant, T\_F (s)** — 速率反馈时间常数 `0.675`（默认）| 正数

用于稳定励磁系统的速率反馈模块时间常数。

### **Maximum controller output, V\_Rmax (pu)** — 控制器输出上限 `4.95`（默认）| 实数

控制器的最大标幺值输出电压。

### **Minimum controller output, V\_Rmin (pu)** — 控制器输出下限 `-4.90`（默认）| 实数

控制器的最小标幺值输出电压。

### **Alternate OEL input locations (V\_OEL)** — 过励限制器输入位置 `Unused`（默认）| `Summation point` | `Take-over`

选择过励限制器输入位置。

### **Alternate UEL input locations (V\_UEL)** — 欠励限制器输入位置 `Unused`（默认）| `Summation point` | `Take-over`

选择欠励限制器输入位置。

### **Alternate SCL input locations (V\_SCL)** — 定子电流限制器输入位置 `Unused`（默认）| `Summation point` | `Take-over`

选择定子电流限制器输入位置。要指定 SCL 输入：

- 如果选择 `Summation point`，请使用 **V\_SCLsum** 输入端口。
- 如果选择 `Take-over`，请使用 **V\_OELscl** 和 **V\_UELscl** 输入端口。

### 励磁机

### **Exciter field proportional constant, K\_E (pu)** — 励磁机励磁增益 `1`（默认）| 正数

励磁机励磁的比例常数。

### **Exciter field time constant, T\_E (s)** — 励磁机励磁时间常数 `1.33`（默认）| 正数

励磁机励磁的时间常数。

### **Lower limit, E\_FDmin (pu)** — 励磁电压下限 `-99`（默认）| 正数

励磁电压的下限。

### **Exciter output voltage for saturation factor S\_E(E\_1), E\_1 (pu)** — 第一饱和输出电压 `3.05`（默认）| 正数

第一饱和系数的励磁机输出电压。

### **Exciter saturation factor at exciter output voltage E\_1, S\_E(E\_1) (1)** — 第一饱和查找电压 `0.279`（默认）| 正数

第一励磁机饱和系数。

### **Exciter output voltage for saturation factor S\_E(E\_2), E\_2 (pu)** — 第二饱和输出电压 `2.29`（默认）| 正数

第二饱和系数的励磁机输出电压。

### **Exciter saturation factor at exciter output voltage E\_2, S\_E(E\_2) (1)** — 第二饱和查找电压 `0.117`（默认）| 正数

第二励磁机饱和系数。

## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

离散时间或连续时间同步电机 DC2C 励磁系统，包括自动电压调节器和励磁机

SM DC2C 模块对符合 IEEE 421.5-2016[1] 的同步电机 DC2C 型励磁系统进行建模。

使用此模块可对作为发电机运行并使用直流换向旋转励磁机的同步电机的励磁电压进行控制和调节建模。

您可以使用 **Sample time (-1 for inherited)** 参数在模块的连续实现和离散实现之间切换。要将积分器配置为连续时间，请将 **Sample time (-1 for
inherited)** 属性设置为 `0`。要将积分器配置为离散时间，请将 **Sample time (-1 for inherited)** 属性设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。

SM DC2C 模块由四个主要组件组成：

- 电流补偿器根据机端电流修改测量的机端电压。
- 电压测量传感器通过使用低通滤波器模拟机端电压传感器的动态特性。
- 励磁控制元件组件将电压传感器输出与机端电压参考进行比较以产生电压误差。然后，该电压误差通过电压调节器以产生励磁机励磁电压。
- 直流旋转励磁机对直流换向旋转励磁机进行建模，并产生施加到受控同步电机的励磁电压。该模块还将励磁电压反馈回励磁系统。

此图显示了 DC2C 励磁系统模型的整体结构：

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
- *EFE* 是励磁机励磁
  电压。
- *EFD* 是励磁电压。

以下各节详细描述了模块的每个主要部分。

### 电流补偿器和电压测量传感器

电流补偿器建模为：

VC1=VT+ITRC2+XC2，

其中：

- *RC* 是负载补偿
  电阻。
- *XC* 是负载补偿
  电抗。

电压测量传感器实现为具有时间常数
*TR* 的低通滤波器模块。有关确切的离散和连续实现，请参阅该模块的文档。

### 励磁控制元件

此图说明了励磁控制元件的整体结构：

图中：

- Summation Point Logic 子系统对过励限制器（OEL）、欠励限制器（UEL）和定子电流限制器（SCL）电压的求和点输入位置进行建模。有关在此模块中使用限制器的详细信息，请参阅励磁电流限制器。
- Lead-Lag 模块对与电压调节器相关的附加动态进行建模。此处，
  *TC* 是超前时间
  常数，*TB* 是滞后
  时间常数。有关确切的离散和连续实现，请参阅 Lead-Lag 模块文档。
- Low-Pass Filter 模块对电压调节器的主要动态进行建模。此处，*KA* 是
  调节器增益，*TA* 是
  调节器的主要时间常数。该模块的最小和最大抗积分饱和限幅为
  *VRmin* 和
  *VRmax*。
- Take-over Logic 子系统对 OEL、UEL 和 SCL 电压的接管点输入位置进行建模。有关在此模块中使用限制器的详细信息，请参阅励磁电流限制器。
- Filtered Derivative 模块对用于稳定励磁系统的速率反馈路径进行建模。此处，
  *KF* 和
  *TF* 分别是该系统的增益和
  时间常数。有关确切的离散和连续实现，请参阅 Filtered Derivative 模块的文档。
- *VT\*VRmax*
  和
  *VT\*VRmin*
  是输出励磁机励磁电压 *EFE* 的最小和最大饱和限幅。

### 励磁电流限制器

您可以使用各种励磁电流限制器在不安全运行条件下修改电压调节器的输出：

- 使用过励限制器防止因过大的励磁电流需求导致励磁绕组过热。
- 使用欠励限制器在励磁过低时提升励磁，否则可能导致失步。
- 使用定子电流限制器防止因过大电流导致定子绕组过热。

将这些限制器中任何一个的输出连接到以下点之一：

- 求和点，作为自动电压调节器（AVR）反馈回路的一部分
- 接管点，以覆盖 AVR 的常规行为

如果在求和点使用定子电流限制器，请使用单个输入 *VSCLsum*。如果在接管点使用定子电流限制器，请同时使用过励输入 *VOELscl* 和欠励输入 *VUELscl*。

### 直流旋转励磁机

此图说明了直流换向旋转励磁机的整体结构：

图中：

- 励磁机励磁电流 *VFE* 建模为两个信号之和：

  - 非线性函数 *Vx* 对励磁机输出电压的饱和进行建模。
  - 比例项 *KE* 对励磁机输出电压与励磁机励磁电流之间的线性关系进行建模。
- **Integrator** 子系统对 *EFE* 与 *VFE* 之间的差值进行积分，以生成输出励磁电压 *Efd*。*TE* 是此过程的时间常数。
