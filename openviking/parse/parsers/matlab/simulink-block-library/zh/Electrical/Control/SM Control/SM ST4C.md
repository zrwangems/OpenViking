---
type: simulink-block
title: 'SM ST4C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smst4c'
documentation_source_path: 'ref/smst4c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM ST4C

## 端口

### 输入

### **V\_REF** — 电压参考标量

电压调节器参考设定值，采用标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **V\_S** — 来自稳定器的输入标量

来自电力系统稳定器的输入，采用标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **V\_T** — 端电压标量

端电压幅值，采用标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **I\_T** — 端电流标量

端电流幅值，采用标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **V\_OEL** — 过励限制信号标量

来自过励限制器的输入，采用标幺值表示，指定为标量。

#### 依赖项

- 要忽略来自过励限制器的输入，
  请将 **备用 OEL 输入位置 (V\_OEL)** 设置为 `Unused`。
- 要在求和点使用来自过励限制器的输入，
  请将 **备用 OEL 输入位置 (V\_OEL)** 设置为 `Summation point`。
- 要在接管点使用来自过励限制器的输入，
  请将 **备用 OEL 输入位置 (V\_OEL)** 设置为 `Take-over`。

**数据类型：** `single` | `double`

### **V\_UEL** — 欠励限制信号标量

来自欠励限制器的输入，采用标幺值表示，指定为标量。

#### 依赖项

- 要忽略来自欠励限制器的输入，
  请将 **备用 UEL 输入位置 (V\_UEL)** 设置为 `Unused`。
- 要在求和点使用来自欠励限制器的输入，
  请将 **备用 UEL 输入位置 (V\_UEL)** 设置为 `Summation point`。
- 要在接管点使用来自欠励限制器的输入，
  请将 **备用 UEL 输入位置 (V\_UEL)** 设置为 `Take-over`。

**数据类型：** `single` | `double`

### **V\_SCLsum** — 求和点定子电流限制信号标量

使用求和点时来自定子电流限制器的输入，采用标幺值表示，指定为标量。

#### 依赖项

- 要忽略来自定子电流限制器的输入，
  请将 **备用 SCL 输入位置 (V\_SCL)** 设置为 `Unused`。
- 要在求和点使用来自定子电流限制器的输入，
  请将 **备用 SCL 输入位置 (V\_SCL)** 设置为 `Summation point`。

**数据类型：** `single` | `double`

### **V\_SCLoel** — 接管定子电流限制 (OEL) 标量

使用接管点时来自定子电流限制器的输入，用于防止励磁过励，采用标幺值表示，指定为标量。

#### 依赖项

- 要忽略来自定子电流限制器的输入，
  请将 **备用 SCL 输入位置 (V\_SCL)** 设置为 `Unused`。
- 要在接管点使用来自定子电流限制器的输入，
  请将 **备用 SCL 输入位置 (V\_SCL)** 设置为 `Take-over`。

**数据类型：** `single` | `double`

### **V\_SCLuel** — 接管定子电流限制 (UEL) 标量

使用接管点时来自定子电流限制器的输入，用于防止励磁欠励，采用标幺值表示，指定为标量。

#### 依赖项

- 要忽略来自定子电流限制器的输入，
  请将 **备用 SCL 输入位置 (V\_SCL)** 设置为 `Unused`。
- 要在接管点使用来自定子电流限制器的输入，
  请将 **备用 SCL 输入位置 (V\_SCL)** 设置为 `Take-over`。

**数据类型：** `single` | `double`

### **Ifd\_pu** — 测量的励磁电流标量

同步电机的测量标幺励磁电流，指定为标量。

**数据类型：** `single` | `double`

### 输出

### **Efd\_pu** — 励磁电压标量

要施加到同步电机励磁电路的标幺励磁电压，以标量形式返回。

**数据类型：** `single` | `double`

## 参数

### 常规

### **初始励磁电压，Efd0 (pu)** — 初始输出电压 `1` (默认) | 实数

要施加到同步电机励磁电路的初始标幺电压。

### **初始端电压，Vt0 (pu)** — 初始端电压 `1` (默认) | 实数

初始标幺端电压。

### **初始端电流，It0 (pu)** — 初始端电流 `1` (默认) | 实数

初始标幺端电流。

### **采样时间（-1 表示继承）** — 模块采样时间 `-1` (默认) | `0` | 正标量

连续模块执行之间的时间。在执行期间，模块生成输出，并在适当时更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

对于继承的离散时间操作，请将此参数设置为 `-1`。对于离散时间操作，请将此参数设置为正整数。对于连续时间操作，请将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数，以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

### 预控制

### **负载补偿的电阻分量，R\_C (pu)** — 补偿电阻 `0` (默认) | 正数

电流补偿系统中使用的电阻。将此参数和 **负载补偿的电抗分量，X\_C (pu)** 设置为 `0` 以禁用电流补偿。

### **负载补偿的电抗分量，X\_C (pu)** — 补偿电抗 `0` (默认) | 正数

电流补偿系统中使用的电抗。将此参数和 **负载补偿的电阻分量，R\_C (pu)** 设置为 `0` 以禁用电流补偿。

### **调节器输入滤波器时间常数，T\_R (s)** — 调节器时间常数 `0` (默认) | 正数

电压传感器滤波的等效时间常数。

### 控制

### **电压调节器比例增益，K\_PR (pu)** — 调节器比例增益 `10.75` (默认) | 正数

与电压调节器 PI 控制模块相关的比例增益。

### **电压调节器积分增益，K\_IR (pu/s)** — 调节器积分增益 `10.75` (默认) | 正数

与电压调节器 PI 控制模块相关的积分增益。

### **晶闸管桥触发控制等效时间常数，T\_A (s)** — 第一个超前-滞后模块的调节器滞后时间常数 `0.02` (默认) | 正数

晶闸管桥触发控制中的等效时间常数。

### **调节器最大输出，V\_Rmax (pu)** — 调节器输出上限 `1` (默认) | 实数

调节器的最大标幺输出电压。

### **调节器最小输出，V\_Rmin (pu)** — 调节器输出下限 `-0.87` (默认) | 实数

调节器的最小标幺输出电压。

### **内环励磁调节器的正向比例增益，K\_PM (pu)** — 内环正向比例增益 `1` (默认) | 正数

内环励磁调节器中 PI 控制模块的标幺正向比例增益。

### **内环励磁调节器的正向积分增益，K\_IM (pu/s)** — 内环正向积分增益 `0` (默认) | 正数

内环励磁调节器中 PI 控制模块的正向积分增益。

### **励磁电流调节器最大输出，V\_Mmax (pu)** — 励磁电流调节器输出上限 `99` (默认) | 实数

励磁电流调节器的最大标幺输出电压。

### **励磁电流调节器最小输出，V\_Mmin (pu)** — 励磁电流调节器输出下限 `-99` (默认) | 实数

励磁电流调节器的最小标幺输出电压。

### **励磁机最大输出，V\_Amax (pu)** — 励磁机输出上限 `99` (默认) | 实数

励磁机的最大标幺输出电压。

### **励磁机最小输出，V\_Amin (pu)** — 励磁机输出下限 `-99` (默认) | 实数

励磁机的最小标幺输出电压。

### **励磁电流调节器反馈增益，K\_G (pu)** — 励磁电流调节器反馈增益 `0` (默认) | 正数

励磁电流调节器的标幺反馈增益。

### **励磁电流调节器反馈时间常数，T\_G (s)** — 励磁电流调节器反馈时间常数 `0` (默认) | 正数

励磁电流调节器的标幺反馈时间常数。

### **励磁电流调节器最大反馈电压，V\_Gmax (pu)** — 励磁电流调节器最大反馈电压 `99` (默认) | 正数

励磁电流调节器的最大标幺反馈电压。

### **备用 PSS 输入位置 (V\_S)** — PSS 输入位置 `Summation point before take-over UEL` (默认) | `Summation point after take-over UEL`

电力系统稳定器输入。

### **备用 OEL 输入位置 (V\_OEL)** — OEL 输入位置 `Unused` (默认) | `Summation point at voltage error` | `Take-over at voltage regulator input` | `Take-over at inner-loop output`

过励限制器输入位置：

- 如果选择 `Summation point at voltage error`，则 **V\_OEL** 是 Summation Point Logic 子系统的输入。
- 如果选择 `Take-over at voltage regulator input`，则 **V\_OEL** 是 Take-over Logic 子系统的输入。
- 如果选择 `Take-over at inner-loop output`，则 **V\_OEL** 是 Take-over Logic 1 子系统的输入。

### **备用 UEL 输入位置 (V\_UEL)** — UEL 输入位置 `Unused` (默认) | `Summation point at voltage error` | `Take-over at voltage regulator input` | `Take-over at inner-loop output`

欠励限制器输入位置：

- 如果选择 `Summation point at voltage error`，则 **V\_UEL** 是 Summation Point Logic 子系统的输入。
- 如果选择 `Take-over at voltage regulator input`，则 **V\_UEL** 是 Take-over Logic 子系统的输入。
- 如果选择 `Take-over at inner-loop output`，则 **V\_UEL** 是 Take-over Logic 1 子系统的输入。

### **备用 SCL 输入位置 (V\_SCL)** — SCL 输入位置 `Unused` (默认) | `Summation point at voltage error` | `Take-over at voltage regulator input` | `Take-over at inner-loop output`

定子电流限制器输入位置：

- 如果选择 `Summation point`，请使用 **V\_SCLsum** 输入端口。
- 如果选择任何 `Take-over` 选项，请使用 **V\_SCLoel** 和 **V\_SCLuel** 输入端口。

### 励磁机

### **与换相电抗成比例的整流器负载因数，K\_C (pu)** — 整流器负载因数 `0.113` (默认) | 正数

与换相电抗成比例的整流器负载因数。

### **电势电路（电压）增益系数，K\_P (pu)** — 电势电路电压增益系数 `9.3` (默认) | 正数

电源电路中的标幺电压增益系数。

#### 依赖项

要启用此参数，请将 **电源选择器** 设置为 `Position A: power source derived from generator terminal voltage`。

### **复合电路（电流）增益系数，K\_I (pu)** — 电势电路电流增益系数 `0` (默认) | 正数

电源电路中的标幺电流增益系数。

#### 依赖项

要启用此参数，请将 **电源选择器** 设置为 `Position A: power source derived from generator terminal voltage`。

### **与电势源相关的电抗，X\_L (pu)** — 电势源电抗 `0.124` (默认) | 正数

电源电路中的标幺电抗。

#### 依赖项

要启用此参数，请将 **电源选择器** 设置为 `Position A: power source derived from generator terminal voltage`。

### **电势电路相角 (degrees)** — 电势电路相角 `0` (默认) | 正数

电源电路的相角，以度为单位。

#### 依赖项

要启用此参数，请将 **电源选择器** 设置为 `Position A: power source derived from generator terminal voltage`。

### **最大可用励磁机电压，V\_Bmax (pu)** — 励磁机电压上限 `11.63` (默认) | 正数

最大可用标幺励磁机电压值。

### **电源选择器** — 电源选择器 `Position A: power source derived from generator terminal voltage` (默认) | `Position B: power source independent of generator terminal conditions`

电源选择器的位置，指定为 `Position A: power source derived from generator terminal voltage` 或 `Position B: power source independent of generator terminal conditions`。

## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

具有自动电压调节器的离散时间或连续时间同步电机 ST4C 静态励磁系统

SM ST4C 模块实现符合 IEEE 421.5-2016[1] 的同步电机型 ST4C 静态励磁系统模型。

使用此模块对同步电机的励磁电压的控制和调节进行建模。

您可以使用 **采样时间（-1 表示继承）** 参数在模块的连续实现和离散实现之间切换。要将积分器配置为连续时间，请将 **采样时间（-1 表示继承）** 属性设置为 `0`。要将积分器配置为离散时间，请将 **采样时间（-1 表示继承）** 属性设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。

SM ST4C 模块包含四个主要组件：

- Current Compensator 根据端电流修改测得的端电压。
- Voltage Measurement Transducer 使用低通滤波器模拟端电压传感器的动态特性。
- Excitation Control Elements 组件将电压传感器输出与端电压参考进行比较，以产生电压误差。然后，该电压误差通过电压调节器以产生励磁电压。
- 当电源独立于端电压时，Power Source 组件对受控整流器的电源进行建模。

此图显示了 ST4C 励磁系统模型的整体结构：

图中：

- *VT* 和 *IT* 是同步电机的测量端电压和端电流。
- *VC1* 是电流补偿后的端电压。
- *VC* 是经过滤波的电流补偿后端电压。
- *VREF* 是参考端电压。
- *VS* 是电力系统稳定器电压。
- *VB* 是励磁机励磁电压。
- *EFD* 和 *IFD* 分别是励磁电压和励磁电流。

以下各节详细描述模块的每个主要部分。

### 电流补偿器和电压测量传感器

电流补偿器建模为：

VC1=VT+ITRC2+XC2,

其中：

- *RC* 是负载补偿电阻。
- *XC* 是负载补偿电抗。

电压测量传感器使用具有时间常数 *TR* 的 Low-Pass Filter 模块实现。有关确切的离散和连续实现，请参阅 Low-Pass Filter 模块的文档。

### Excitation Control Elements

此图说明了励磁控制元件的总体结构：

图中：

- Summation Point Logic 子系统对过励限制器 (OEL)、欠励限制器 (UEL)、定子电流限制器 (SCL) 以及功率开关选择器 (V\_S) 电压的求和点输入位置进行建模。有关将此模块与限制器一起使用的详细信息，请参阅励磁电流限制器。
- 有两个 Take-over Logic 子系统。这些子系统对 OEL、UEL、SCL 和 PSS 电压的接管点输入位置进行建模。有关将此模块与限制器一起使用的详细信息，请参阅励磁电流限制器。
- PI\_R 子系统对 PI 控制器进行建模，该控制器用作自动电压调节器的控制结构，并允许表示采用现代数字控制器的设备改造。该模块的抗积分饱和最小和最大饱和限值分别为 *VPImin* 和 *VPImax*。
- PI\_M 子系统对 PI 控制器进行建模，并替代 SM ST3C 中的 Lead-Lag 模块。该模块的抗积分饱和最小和最大饱和限值分别为 *VMmin* 和 *VMmax*。
- 使用内励磁电压控制环来线性化励磁机控制特性，它由增益 *KM* 和 *KG* 以及时间常数 *TM* 和 *TG* 组成。Low-Pass Filter 模块的抗积分饱和最小和最大饱和限值分别为 *VAmin* 和 *VAmax*。

### 励磁电流限制器

您可以使用各种励磁电流限制器在不安全运行条件下修改电压调节器的输出：

- 使用过励限制器防止因励磁电流需求过大而导致励磁绕组过热。
- 使用欠励限制器在励磁过低时提升励磁，因为励磁过低存在失步风险。
- 使用定子电流限制器防止因电流过大而导致定子绕组过热。

将任何这些限制器的输出连接到以下点之一：

- 求和点，作为自动电压调节器 (AVR) 反馈回路的一部分
- 接管点，用于覆盖 AVR 的通常行为

如果在求和点使用定子电流限制器，请使用单个输入 *VSCLsum*。如果在接管点使用定子电流限制器，请同时使用过励输入 *VSCLoel* 和欠励输入 *VSCLuel*。

### 电源

通过选择 **Power source selector** 参数中的相关选项，可以采用可控整流器电源的不同表示形式。可控整流器的电源既可以来自机端电压 (`Position A: power source
derived from generator terminal voltage`)，也可以独立于机端电压 (`Position B: power source independent of
generator terminal conditions`)。

此图显示了利用机端电压 *VT* 和机端电流 *IT* 的相量组合的励磁机电源模型：
