---
type: simulink-block
title: 'SM ST10C'
family: 'control'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smst10c'
documentation_source_path: 'ref/smst10c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM ST10C

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

- 要忽略来自过励限制器的输入，将 **备用 OEL 输入位置 (V\_OEL)** 设置为 `Unused`。
- 要在求和点使用来自过励限制器的输入，将 **备用 OEL 输入位置 (V\_OEL)** 设置为 `Summation point at voltage error`。
- 要在 Take-over Logic 子系统使用来自过励限制器的输入，将 **备用 OEL 输入位置 (V\_OEL)** 设置为 `Take-over at voltage error`。
- 要在 Take-over Logic1 子系统使用来自过励限制器的输入，将 **备用 OEL 输入位置 (V\_OEL)** 设置为 `Take-over at voltage regulator output`。

**数据类型：** `single` | `double`

### **V\_UEL** — 欠励限制信号标量

来自欠励限制器的输入，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自欠励限制器的输入，将 **备用 UEL 输入位置 (V\_UEL)** 设置为 `Unused`。
- 要在求和点使用来自欠励限制器的输入，将 **备用 UEL 输入位置 (V\_UEL)** 设置为 `Summation point at voltage error`。
- 要在 Take-over Logic 子系统使用来自欠励限制器的输入，将 **备用 UEL 输入位置 (V\_UEL)** 设置为 `Take-over at voltage error`。
- 要在 Take-over Logic1 子系统使用来自欠励限制器的输入，将 **备用 UEL 输入位置 (V\_UEL)** 设置为 `Take-over at voltage regulator output`。

**数据类型：** `single` | `double`

### **V\_SCLsum** — 求和点定子电流限制信号标量

使用求和点时来自定子电流限制器的输入，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，将 **备用 SCL 输入位置 (V\_SCL)** 设置为 `Unused`。
- 要在求和点使用来自定子电流限制器的输入，将 **备用 SCL 输入位置 (V\_SCL)** 设置为 `Summation point at voltage error`。

**数据类型：** `single` | `double`

### **V\_SCLoel** — 用于过励限制器的接管定子电流限制标量

使用接管点时，来自定子电流限制器的输入，用于防止励磁过励，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，将 **备用 SCL 输入位置 (V\_SCL)** 设置为 `Unused`。
- 要在 Take-over Logic 子系统使用来自定子电流限制器的输入，将 **备用 SCL 输入位置 (V\_SCL)** 设置为 `Take-over at voltage error`。
- 要在 Take-over Logic1 子系统使用来自定子电流限制器的输入，将 **备用 SCL 输入位置 (V\_SCL)** 设置为 `Take-over at voltage regulator output`。

**数据类型：** `single` | `double`

### **V\_SCLuel** — 用于欠励限制器的接管定子电流限制标量

使用接管点时，来自定子电流限制器的输入，用于防止励磁欠励，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，将 **备用 SCL 输入位置 (V\_SCL)** 设置为 `Unused`。
- 要在 Take-over Logic 子系统使用来自定子电流限制器的输入，将 **备用 SCL 输入位置 (V\_SCL)** 设置为 `Take-over at voltage error`。
- 要在 Take-over Logic1 子系统使用来自定子电流限制器的输入，将 **备用 SCL 输入位置 (V\_SCL)** 设置为 `Take-over at voltage regulator output`。

**数据类型：** `single` | `double`

### **Ifd\_pu** — 测量的励磁电流标量

同步电机的测量标幺值励磁电流，指定为标量。

**数据类型：** `single` | `double`

### 输出

### **Efd\_pu** — 励磁电压标量

要施加到同步电机励磁电路的标幺值励磁电压，以标量形式返回。

**数据类型：** `single` | `double`

## 参数

### 常规

### **初始励磁电压，Efd0 (pu)** — 初始输出电压 `1`（默认）| real scalar

要施加到同步电机励磁电路的初始标幺值电压。

### **初始端电压，Vt0 (pu)** — 初始端电压 `1`（默认）| real scalar

要施加到端子的初始标幺值电压。

#### 依赖关系

要启用此参数，在励磁器节中，将 **电源选择器** 设置为 `Position A: power source derived from generator terminal voltage`。

### **初始端电流，It0 (pu)** — 初始端电流 `1`（默认）| real scalar

要施加到端子的初始标幺值电流。

#### 依赖关系

要启用此参数，在励磁器节中，将 **电源选择器** 设置为 `Position A: power source derived from generator terminal voltage`。

### **采样时间（-1 表示继承）** — 模块采样时间 `-1`（默认）| `0` | positive scalar

连续模块执行之间的时间。执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅“什么是采样时间？”和“指定采样时间”。

对于继承的离散时间操作，将此参数设置为 `-1`。对于离散时间操作，将此参数设置为正整数。对于连续时间操作，将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的封装子系统或变体子系统中，请提升此参数，以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅“在封装上提升模块参数”。

### 预控制

### **负载补偿的电阻分量，R\_C (pu)** — 补偿电阻 `0`（默认）| positive scalar

电流补偿系统中使用的电阻。将此参数和 **负载补偿的电抗分量，X\_C (pu)** 设置为 `0` 以禁用电流补偿。

### **负载补偿的电抗分量，X\_C (pu)** — 补偿电抗 `0`（默认）| positive scalar

电流补偿系统中使用的电抗。将此参数和 **负载补偿的电阻分量，R\_C (pu)** 设置为 `0` 以禁用电流补偿。

### **调节器输入滤波器时间常数，T\_R (s)** — 调节器时间常数 `0.01`（默认）| positive scalar

电压变送器滤波的等效时间常数。

### 控制

### **调节器增益，K\_R (pu)** — 调节器增益 `500`（默认）| positive scalar

调节器的增益。

### **电压调节器分母（滞后）时间常数 1，T\_B1 (s)** — 调节器滞后时间常数 1 `12.5`（默认）| positive scalar

电压调节器的第二个 Lead-Lag (Discrete or Continuous) 模块中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **电压调节器分子（超前）时间常数 1，T\_C1 (s)** — 调节器超前时间常数 1 `1.5`（默认）| positive scalar

电压调节器的第二个 Lead-Lag (Discrete or Continuous) 模块中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **电压调节器分母（滞后）时间常数 2，T\_B2 (s)** — 调节器滞后时间常数 2 `0.1`（默认）| positive scalar

电压调节器的第一个 Lead-Lag (Discrete or Continuous) 模块中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **电压调节器分子（超前）时间常数 2，T\_C2 (s)** — 调节器超前时间常数 2 `0.1`（默认）| positive scalar

电压调节器的第一个 Lead-Lag (Discrete or Continuous) 模块中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **UEL 调节器分母（滞后）时间常数 1，T\_UB1 (s)** — UEL 调节器滞后时间常数 1 `12.5`（默认）

欠励限制器调节器的第二个 Lead-Lag (Discrete or Continuous) 模块中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **UEL 调节器分子（超前）时间常数 1，T\_UC1 (s)** — UEL 调节器超前时间常数 1 `1.5`（默认）

欠励限制器调节器的第二个 Lead-Lag (Discrete or Continuous) 模块中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **UEL 调节器分母（滞后）时间常数 2，T\_UB2 (s)** — UEL 调节器滞后时间常数 2 `0.1`（默认）

欠励限制器调节器的第一个 Lead-Lag (Discrete or Continuous) 模块中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **UEL 调节器分子（超前）时间常数 2，T\_UC2 (s)** — UEL 调节器超前时间常数 2 `0.1`（默认）

欠励限制器调节器的第一个 Lead-Lag (Discrete or Continuous) 模块中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **OEL 调节器分母（滞后）时间常数 1，T\_OB1 (s)** — OEL 调节器滞后时间常数 1 `12.5`（默认）

过励限制器调节器的第二个 Lead-Lag (Discrete or Continuous) 模块中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **OEL 调节器分子（超前）时间常数 1，T\_OC1 (s)** — OEL 调节器超前时间常数 1 `1.5`（默认）

过励限制器调节器的第二个 Lead-Lag (Discrete or Continuous) 模块中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **OEL 调节器分母（滞后）时间常数 2，T\_OB2 (s)** — OEL 调节器滞后时间常数 2 `0.1`（默认）

过励限制器调节器的第一个 Lead-Lag (Discrete or Continuous) 模块中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **OEL 调节器分子（超前）时间常数 2，T\_OC2 (s)** — OEL 调节器超前时间常数 2 `0.1`（默认）

过励限制器调节器的第一个 Lead-Lag (Discrete or Continuous) 模块中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **最大调节器输出，V\_Rmax (pu)** — 最大调节器输出 `10`（默认）| real scalar

最大标幺值调节器输出。

### **最小调节器输出，V\_Rmin (pu)** — 最小调节器输出 `-8.7`（默认）| real scalar

最小标幺值调节器输出。

### **最大 PSS 调节器输出，V\_RSmax (pu)** — 最大 PSS 调节器输出 `5`（默认）| real scalar

电力系统稳定器调节器的最大标幺值输出。

### **最小 PSS 调节器输出，V\_RSmin (pu)** — 最小 PSS 调节器输出 `-5`（默认）| real scalar

电力系统稳定器调节器的最小标幺值输出。

### **备用 PSS 输入位置 (V\_S)** — PSS 输入位置 `Summation point at output of AVR`（默认）| `Summation point at voltage error calculation` | `Summation point at voltage error or take-over limits`

电力系统稳定器输入的位置。

### **备用 OEL 输入位置 (V\_OEL)** — OEL 输入位置 `Summation point at voltage error`（默认）| `Unused` | `Take-over at voltage error` | `Take-over at voltage regulator output`

过励限制器输入的位置，指定为以下选项之一：

- `Summation point at voltage error` — **V\_OEL** 是 **Summation Point Logic** 子系统的一个输入。
- `Take-over at voltage error` — **V\_OEL** 是 **Take-over Logic** 子系统的一个输入。
- `Take-over at voltage regulator output` — **V\_OEL** 是 **Take-over Logic 1** 子系统的一个输入。

### **备用 UEL 输入位置 (V\_UEL)** — UEL 输入位置 `Summation point at voltage error`（默认）| `Unused` | `Take-over at voltage error` | `Take-over at voltage regulator output`

欠励限制器输入的位置，指定为以下选项之一：

- `Summation point at voltage error` — **V\_UEL** 是 **Summation Point Logic** 子系统的一个输入。
- `Take-over at voltage error` — **V\_UEL** 是 **Take-over Logic** 子系统的一个输入。
- `Take-over at voltage regulator output` — **V\_UEL** 是 **Take-over Logic 1** 子系统的一个输入。

### **备用 SCL 输入位置 (V\_SCL)** — SCL 输入位置 `Summation point at voltage error`（默认）| `Unused` | `Take-over at voltage error` | `Take-over at voltage regulator output`

定子电流限制器输入的位置，指定为以下选项之一：

- `Summation point` — 使用 **V\_SCLsum** 输入端口。
- 任何 `Take-over` 选项 — 使用 **V\_OELscl** 和 **V\_UELscl** 输入端口。

### 励磁器

### **与换相电抗成正比的整流器负载系数，K\_C (pu)** — 整流器负载系数 `0.01`（默认）| positive scalar

整流器负载系数。此值与换相电抗成正比。

### **整流器桥的等效时间常数，T\_1 (s)** — 整流器桥时间常数 `0.004`（默认）| positive scalar

整流器桥的等效时间常数，以秒为单位。

### **电势电路（电压）增益系数，K\_P (pu)** — 电势电路电压增益系数 `1`（默认）| positive scalar

电源电路中的标幺值电压增益系数。

### **电势电路（电流）增益系数，K\_I (pu)** — 电势电路电流增益系数 `0`（默认）| positive scalar

电源电路中的标幺值电流增益系数。

#### 依赖关系

要启用此参数，将 **电源选择器** 设置为 `Position A: power source derived from generator terminal voltage`。

### **与电势源相关的电抗，X\_L (pu)** — 电势源电抗 `0`（默认）| positive scalar

电势源中的标幺值电抗。

#### 依赖关系

要启用此参数，将 **电源选择器** 设置为 `Position A: power source derived from generator terminal voltage`。

### **电势电路相位角（degrees）** — 电势电路相位角 `0`（默认）| positive scalar

电源电路的相位角，单位为 degrees。

#### 依赖关系

要启用此参数，将 **电源选择器** 设置为 `Position A: power source derived from generator terminal voltage`。

### **最大可用励磁器电压，V\_Bmax (pu)** — 励磁器电压上限 `1.5`（默认）| positive scalar

最大可用标幺值励磁器电压值。

### **电源选择器** — 电源选择器 `Position A: power source derived from generator terminal voltage`（默认）| `Position B: power source independent of generator terminal conditions`

电源选择器的位置。

## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

离散时间或连续时间同步电机 ST10C 静态励磁系统，带自动电压调节器

SM ST10C 模块实现符合 IEEE Std 421.5-2016 [1] 的同步电机型 ST10C 静态励磁系统模型。

使用此模块对同步电机的励磁电压的控制和调节进行建模。

通过使用 **Sample time (-1 for inherited)** 参数在模块的连续和离散实现之间切换。要将积分器配置为连续时间，将 **Sample time (-1 for inherited)** 参数设置为 `0`。要将积分器配置为离散时间，将 **Sample time (-1 for inherited)** 参数设置为正标量。要从上游模块继承采样时间，将 **Sample time (-1 for inherited)** 参数设置为 `-1`。

SM ST10C 模块包含四个主要组件：

- Current Compensator 组件根据端子电流修改测得的端子电压。
- Voltage Measurement Transducer 组件使用低通滤波器模拟端子电压传感器的动态。
- Excitation Control Elements 组件将电压传感器输出与端子电压参考值进行比较，以产生电压误差值。然后该组件将此值通过电压调节器以产生励磁电压。
- Power Source 组件在电源独立于端子电压时，为受控整流器建模电源。

此图显示 ST10C 励磁系统模型的结构：

在图中：

- *VT* 和 *IT* 分别是同步电机的测量端子电压和电流。
- *VC1* 是电流补偿后的端子电压。
- *VC* 是滤波后的电流补偿端子电压。
- *VREF* 是参考端子电压。
- *VS* 是电力系统稳定器电压。
- *VB* 是励磁机励磁电压。
- *EFD* 和 *IFD* 分别是励磁电压和电流。

### 电流补偿器和电压测量传感器

该模块使用以下方程对电流补偿器建模：

VC1=VT+ITRC2+XC2,

其中：

- *RC* 是负载补偿电阻。
- *XC* 是负载补偿电抗。

该模块将电压测量传感器实现为具有时间常数 *TR* 的 Low-Pass Filter 模块。有关精确的离散和连续实现信息，请参阅 Low-Pass Filter 模块的文档。

### 励磁控制元件

此图显示励磁控制元件的结构：

在图中：

- Summation Point Logic 子系统为过励限制器 (OEL)、欠励限制器 (UEL) 和定子电流限制器 (SCL) 建模求和点输入位置。有关将此模块与限制器一起使用的更多信息，请参阅励磁电流限制器。
- 有两个 Take-over Logic 子系统。它们为 OEL、UEL 和 SCL 电压建模接管点输入位置。有关将此模块与限制器一起使用的更多信息，请参阅励磁电流限制器。
- Lead-Lag (Discrete or Continuous) 模块的并联配置在限制器激活时提供独立控制设置。该模型提供一个公共增益因子 *KR*，以及用于 AVR 和用于欠励和过励限制器的两个 Lead-Lag (Discrete or Continuous) 模块。当 *VUEL* 和/或 *VOEL* 信号连接到其各自的备用位置时，SW\_UEL 和 SW\_OEL Switch 模块激活适当的控制路径。当您将 **Alternate UEL input locations (V\_UEL)** 和 **Alternate OEL input locations (V\_OEL)** 参数设置为 `Take-over at voltage error` 时，SW\_UEL 和 SW\_OEL Switch 模块处于位置 B。
- 每个控制路径中的两个 Lead-Lag 模块为电压调节器以及欠励和过励限制器建模附加动态。每个相应路径中的第一个 Lead-Lag 模块表示瞬态增益降低，其中 *TC2*（或 *TUC2* 和 *TOC2*）是超前时间常数，*TB2*（或 *TUB2* 和 *TOB2*）是滞后时间常数。第二个 Lead-Lag 模块允许表示瞬态增益增加的可能性，其中 *TC1*（或 *TUC1* 和 *TOC1*）是超前时间常数，*TB1*（或 *TUB1* 和 *TOB1*）是滞后时间常数。有关离散和连续实现信息，请参阅 Lead-Lag 模块的文档。
- SM ST10C 模块还提供选项，可在第一个 Take-over Logic 子系统之后的 AVR 求和点处，或在门结构输出处，通过单独路径（模型中的底部路径）施加 PSS 信号。此单独路径包含与主求和点路径相同的控制元件。
- **Power source selector** 参数控制受控整流器的电源来源。该子系统将电压调节器命令信号 *VR* 乘以励磁机励磁电压 *VB*。有关受控整流器电源的逻辑开关的更多信息，请参阅 Power Source。

### 励磁电流限制器

您可以使用不同类型的励磁电流限制器在不安全运行条件下修改电压调节器的输出：

- 使用过励限制器防止由于过大的励磁电流需求而导致励磁绕组过热。
- 使用欠励限制器在励磁过低时提升励磁，过低会有失步风险。
- 使用定子电流限制器防止由于过大电流而导致定子绕组过热。

将这些限制器中任意一个的输出连接到以下点之一：

- Summation point — 将限制器用作自动电压调节器 (AVR) 反馈回路的一部分。
- Take-over points — 覆盖 AVR 的通常行为。

如果您在求和点使用定子电流限制器，请使用输入 *VSCLsum*。如果您在接管点使用定子电流限制器，请使用过励输入 *VSCLoel*，以及欠励输入 *VSCLuel*。

### Power Source

您可以通过设置 **Power source selector** 参数值，为受控整流器使用不同的电源表示。要从端子电压导出受控整流器的电源，将 **Power source selector** 参数设置为 `Position A: power source derived from generator terminal voltage`。要指定电源独立于端子电压，将 **Power source selector** 参数设置为 `Position B: power source independent of generator terminal conditions`。

此图显示利用端子电压 *VT* 和端子电流 *IT* 的相量组合的励磁机电源模型：
