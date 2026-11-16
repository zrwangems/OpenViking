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

### **V\_OEL** — 过励磁限制信号标量

来自过励磁限制器的输入，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自过励磁限制器的输入，请将 **备用 OEL 输入位置 (V\_OEL)** 设置为 `Unused`。
- 要在求和点使用来自过励磁限制器的输入，请将 **备用 OEL 输入位置 (V\_OEL)** 设置为 `Summation point`。
- 要在接管点使用来自过励磁限制器的输入，请将 **备用 OEL 输入位置 (V\_OEL)** 设置为 `Take-over`。

**数据类型：** `single` | `double`

### **V\_UEL** — 欠励磁限制信号标量

来自欠励磁限制器的输入，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自欠励磁限制器的输入，请将 **备用 UEL 输入位置 (V\_UEL)** 设置为 `Unused`。
- 要在求和点使用来自欠励磁限制器的输入，请将 **备用 UEL 输入位置 (V\_UEL)** 设置为 `Summation point`。
- 要在接管点使用来自欠励磁限制器的输入，请将 **备用 UEL 输入位置 (V\_UEL)** 设置为 `Take-over`。

**数据类型：** `single` | `double`

### **V\_SCLsum** — 求和点定子电流限制信号标量

使用求和点时来自定子电流限制器的输入，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **备用 SCL 输入位置 (V\_SCL)** 设置为 `Unused`。
- 要在求和点使用来自定子电流限制器的输入，请将 **备用 SCL 输入位置 (V\_SCL)** 设置为 `Summation point`。

**数据类型：** `single` | `double`

### **V\_SCLoel** — 接管定子电流限制 (OEL) 标量

使用接管点时来自定子电流限制器的输入，该输入防止磁场过励磁，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **备用 SCL 输入位置 (V\_SCL)** 设置为 `Unused`。
- 要在接管点使用来自定子电流限制器的输入，请将 **备用 SCL 输入位置 (V\_SCL)** 设置为 `Take-over`。

**数据类型：** `single` | `double`

### **V\_SCLuel** — 接管定子电流限制 (UEL) 标量

使用接管点时来自定子电流限制器的输入，该输入防止磁场欠励磁，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **备用 SCL 输入位置 (V\_SCL)** 设置为 `Unused`。
- 要在接管点使用来自定子电流限制器的输入，请将 **备用 SCL 输入位置 (V\_SCL)** 设置为 `Take-over`。

**数据类型：** `single` | `double`

### **Ifd\_pu** — 测量励磁电流标量

同步电机的测量标幺值励磁电流，指定为标量。

**数据类型：** `single` | `double`

### 输出

### **Efd\_pu** — 励磁电压标量

要施加到同步电机励磁电路的标幺值励磁电压，以标量形式返回。

**数据类型：** `single` | `double`

## 参数

### 常规

### **初始励磁电压，Efd0 (pu)** — 初始输出电压 `1` (默认) | 实数标量

要施加到同步电机励磁电路的初始标幺值电压。

### **初始机端电压，Vt0 (pu)** — 初始机端电压 `1` (默认) | 实数标量

要施加到机端的初始标幺值电压。

#### 依赖关系

要启用此参数，在励磁器部分，将 **用于选择励磁器供电配置的开关** 设置为 `Position A: power source derived from generator terminal voltage`。

### **初始机端电流，It0 (pu)** — 初始机端电流 `1` (默认) | 实数标量

要施加到机端的初始标幺值电流。

#### 依赖关系

要启用此参数，在励磁器部分，将 **用于选择励磁器供电配置的开关** 设置为 `Position A: power source derived from generator terminal voltage`。

### **采样时间 (-1 表示继承)** — 模块采样时间 `-1` (默认) | `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承离散时间操作，将此参数设置为 `-1`。对于离散时间操作，将此参数设置为正整数。对于连续时间操作，将此参数设置为 `0`。

如果此模块位于掩码子系统或支持在连续操作和离散操作之间切换的变体子系统中，请提升此参数，以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

### 预控制

### **负载补偿的电阻分量，R\_C (pu)** — 补偿电阻 `0` (默认) | 正标量

用于电流补偿系统的电阻。将此参数和 **负载补偿的电抗分量，X\_C (pu)** 设置为 `0` 以禁用电流补偿。

### **负载补偿的电抗分量，X\_C (pu)** — 补偿电抗 `0` (默认) | 正标量

用于电流补偿系统的电抗。将此参数和 **负载补偿的电阻分量，R\_C (pu)** 设置为 `0` 以禁用电流补偿。

### **调节器输入滤波器时间常数，T\_R (s)** — 调节器时间常数 `0` (默认) | 正标量

电压变送器滤波的等效时间常数。

### 控制

### **AVR 微分部分的时间常数，T\_CD (s)** — AVR 微分部分的时间常数 `0.06` (默认) | 正标量

AVR 微分部分的 Filtered Derivative 模块的时间常数，以秒为单位。

### **AVR 微分部分的 RegFilter 时间常数，T\_BD (s)** — AVR 微分部分的滤波器时间常数 `0.03` (默认) | 正标量

AVR 微分部分的 Filtered Derivative 模块的滤波器时间常数，以秒为单位。

### **AVR 微分部分影响的死区，Z\_A (1)** — AVR 微分部分影响的死区 `0.036` (默认) | 正标量

AVR 微分部分的死区。

### **AVR 增益，K\_A (1)** — AVR 增益 `12` (默认) | 实数标量

AVR 的增益。

### **与接管 UEL 激活相关的增益，K\_U (1)** — 与接管 UEL 激活相关的增益 `10000` (默认) | 实数标量

与接管 UEL 激活相关的增益。

### **AVR 时间常数，T\_A (s)** — AVR 时间常数 `2` (默认) | 正标量

AVR 的时间常数，以秒为单位。

### **欠励磁限制器时间常数，T\_AUEL (s)** — 欠励磁限制器时间常数 `2` (默认) | 正标量

UEL 的时间常数，以秒为单位。

### **调节器最大输出，V\_Rmax (pu)** — 调节器最大输出 `1` (默认) | 实数标量

调节器的最大标幺值输出。

### **调节器最小输出，V\_Rmin (pu)** — 调节器最小输出 `-0.866` (默认) | 实数标量

调节器的最小标幺值输出。

### **功率转换器增益（与供电电压成正比），K\_AS (pu)** — 功率转换器增益 `6.1` (默认) | 实数标量

功率转换器增益的标幺值增益，与供电电压成正比。

### **功率转换器触发控制的等效时间常数，T\_AS (s)** — 功率转换器触发控制的时间常数 `0.0018` (默认) | 正标量

功率转换器触发控制的等效时间常数，以秒为单位。

### **备用 OEL 输入位置 (V\_OEL)** — OEL 输入位置 `Unused` (默认) | `Summation point` | `Take-over`

过励磁限制器输入的位置，指定为以下选项之一：

- `Summation point` — **V\_OEL** 是 Summation Point Logic 子系统的输入。
- `Take-over` — **V\_OEL** 是 Take-over Logic 子系统的输入。

### **备用 UEL 输入位置 (V\_UEL)** — UEL 输入位置 `Unused` (默认) | `Summation point` | `Take-over`

欠励磁限制器输入的位置，指定为以下选项之一：

- `Summation point` — **V\_UEL** 是 Summation Point Logic 子系统的输入。
- `Take-over` — **V\_UEL** 是 Take-over Logic 子系统的输入。

### **备用 SCL 输入位置 (V\_SCL)** — SCL 输入位置 `Unused` (默认) | `Summation point` | `Take-over`

定子电流限制器输入的位置，指定为以下选项之一：

- `Summation point` — 使用 **V\_SCLsum** 输入端口。
- `Take-over` — 使用 **V\_SCLoel** 和 **V\_SCLuel** 输入端口。

### 励磁器

### **与换相电抗成正比的整流器负载系数，K\_C (pu)** — 整流器负载系数 `0` (默认) | 正标量

整流器负载系数。此值与换相电抗成正比。

### **电势电路（电压）增益系数，K\_P (pu)** — 电势电路电压增益系数 `1` (默认) | 正标量

电源电路中的标幺值电压增益系数。

### **电势电路（电流）增益系数，K\_I (pu)** — 电势电路电流增益系数 `0` (默认) | 正标量

电源电路中的标幺值电流增益系数。

#### 依赖关系

要启用此参数，请将 **用于选择励磁器供电配置的开关** 设置为 `Position A: power source derived from generator terminal voltage`。

### **与复合电源相关的电抗，X\_L (pu)** — 复合电源电抗 `0` (默认) | 正标量

复合电源中的标幺值电抗。

#### 依赖关系

要启用此参数，请将 **用于选择励磁器供电配置的开关** 设置为 `Position A: power source derived from generator terminal voltage`。

### **电势电路相位角 (degrees)** — 电势电路相位角 `0` (默认) | 正标量

电源电路的相位角，以度为单位。

#### 依赖关系

要启用此参数，请将 **用于选择励磁器供电配置的开关** 设置为 `Position A: power source derived from generator terminal voltage`。

### **基于供电条件的励磁器电压最大限制，V\_Bmax (pu)** — 励磁器电压上限 `11.63` (默认) | 正标量

基于供电条件的最大可用励磁器电压标幺值。

### **用于选择励磁器供电配置的开关** — 电源选择器 `Position A: power source derived from generator terminal voltage` (默认) | `Position B: power source independent of generator terminal conditions`

电源选择器的位置，指定为 `Position A: power source derived from generator terminal voltage` 或 `Position B: power source independent of generator terminal conditions`。

## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

离散时间或连续时间同步电机 ST9C 静态励磁系统，带有自动电压调节器

SM ST9C 模块实现符合 IEEE 421.5-2016 [1] 的同步电机型 ST9C 静态励磁系统模型。

使用此模块对同步电机的励磁电压进行控制和调节建模。

使用 **采样时间 (-1 表示继承)** 参数在模块的连续实现和离散实现之间切换。要将积分器配置为连续时间，请将 **采样时间 (-1 表示继承)** 参数设置为 `0`。要将积分器配置为离散时间，请将 **采样时间 (-1 表示继承)** 参数设置为正标量。要从上游模块继承采样时间，请将 **采样时间 (-1 表示继承)** 参数设置为 `-1`。

SM ST9C 模块包含四个主要组件：

- Current Compensator 组件根据机端电流修改测量的机端电压。
- Voltage Measurement Transducer 组件使用低通滤波器模拟机端电压变送器的动态特性。
- Excitation Control Elements 组件将电压变送器输出与机端电压参考进行比较，以产生电压误差值。然后，该组件将此值通过电压调节器以产生励磁电压。
- Power Source 组件在受控整流器的电源独立于机端电压时，对该电源进行建模。

此图显示了 ST9C 励磁系统模型的结构：

图中：

- *VT* 和 *IT* 分别是同步电机测量的机端电压和电流。
- *VC1* 是电流补偿后的机端电压。
- *VC* 是滤波后的电流补偿机端电压。
- *VREF* 是参考机端电压。
- *VS* 是电力系统稳定器电压。
- *VB* 是励磁器励磁电压。
- *EFD* 和 *IFD* 分别是励磁电压和励磁电流。

### 电流补偿器和电压测量变送器

该模块使用以下方程对电流补偿器进行建模：

VC1=VT+ITRC2+XC2,

其中：

- *RC* 是负载补偿电阻。
- *XC* 是负载补偿电抗。

该模块将电压测量变送器实现为具有时间常数 *TR* 的 Low-Pass Filter 模块。有关精确的离散和连续实现的信息，请参阅 Low-Pass Filter 模块的文档。

### 励磁控制元件

此图展示了励磁控制元件的结构：

图中：

- 补偿电压 *Vc* 路径中的微分环节使调节器在电压变化较大时具有更快的响应。Saturation 模块消除微分环节对 *Vc* 小变化的影响，其中 **Upper limit** 和 **Lower limit** 参数等于 Z\_A，即 **Dead-band for differential part influence on AVR, Z\_A (1)** 参数的值。
- Summation Point Logic 子系统对过励限制器 (OEL) 和欠励限制器 (UEL) 电压的求和点输入位置进行建模。有关将限制器与此模块配合使用的更多信息，请参阅励磁电流限制器。
- 有两个 Take-over Logic 子系统。这些子系统对 OEL、UEL 和 SCL 的接管点输入位置进行建模。有关将限制器与此模块配合使用的更多信息，请参阅励磁电流限制器。
- Low-Pass Filter 模块对功率变换器级进行建模，其中 **Power converter gain (proportional to supply voltage), K\_AS (pu)** 和 **Equivalent time constant of power converter firing control, T\_AS (s)** 分别为增益和时间常数。时间常数 *TAS* 表示门极控制单元和功率变换器的总延迟。增益 *KAS* 与为功率变换器供电的 power potential transformer 的二次电压成正比。
- UEL 是一个具有自身比例增益的 PI 调节器。该 PI 调节器与 AVR 共享积分路径。积分时间常数取决于 UEL 和 AVR 的误差信号。AVR 误差信号与来自 UEL 模型的 **V\_UEL** 信号之间的差值的符号指示 UEL 还是 AVR 处于活动状态。
- **Power source selector** 参数控制可控整流器电源的来源。该子系统将电压调节器指令信号 *VR* 与励磁机励磁电压 *VB* 相乘。有关可控整流器电源的逻辑开关的更多信息，请参阅电源。

### 励磁电流限制器

在不安全的运行工况下，您可以使用不同类型的励磁电流限制器来修改电压调节器的输出：

- 使用过励限制器防止因励磁电流需求过大而导致励磁绕组过热。
- 使用欠励限制器在励磁过低时提升励磁，因为励磁过低存在失步风险。
- 使用定子电流限制器防止因电流过大而导致定子绕组过热。

将任一这些限制器的输出连接到以下点之一：

- 求和点 — 将限制器用作自动电压调节器 (AVR) 反馈回路的一部分。
- 接管点 — 覆盖 AVR 的通常行为。

如果您在求和点使用定子电流限制器，请使用输入 *VSCLsum*。如果您在接管点使用定子电流限制器，请使用过励输入 *VSCLoel* 和欠励输入 *VSCLuel*。

### 电源

您可以通过设置 **Switch to select exciter supply configuration** 参数值，为可控整流器使用不同的电源表示。要从机端电压获得可控整流器的电源，请将 **Switch to select exciter supply configuration** 参数设置为 `Position A: power source derived from generator terminal voltage`。要指定电源与机端电压无关，请将 **Switch to select exciter supply configuration** 参数设置为 `Position B: power source independent of generator terminal conditions`。

此图展示了利用机端电压 *VT* 和机端电流 *IT* 的相量组合的励磁机电源模型：
