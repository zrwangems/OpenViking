---
type: simulink-block
title: 'SM ST5C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smst5c'
documentation_source_path: 'ref/smst5c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM ST5C

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
  locations** 设置为 `Summation
  point`。

**数据类型：** `single` | `double`

### **V\_SCLoel** — 接管点定子电流限制（OEL）标量

使用接管点时来自定子电流限制器的输入，用于防止励磁过励，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations
  (V\_SCL)** 设置为
  `Unused`。
- 要在接管点使用来自定子电流限制器的输入，请将 **Alternate SCL input
  locations (V\_SCL)** 设置为
  `Take-over`。

**数据类型：** `single` | `double`

### **V\_SCLuel** — 接管点定子电流限制（UEL）标量

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
```yaml
parameters:
- name: Initial field voltage, Efd0 (pu)
  summary: 初始输出电压 1（默认）| 实数标量
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
  summary: 调节器时间常数 0.02（默认）| 正标量
  group: 预控制
- name: Regulator gain, K_R (pu)
  summary: 调节器增益 200（默认）| 正标量
  group: 控制
- name: Voltage regulator denominator (lag) time constant (first block), T_B1 (s)
  summary: 调节器滞后时间常数 1 6（默认）| 正标量
  group: 控制
- name: Voltage regulator numerator (lead) time constant (first block), T_C1 (s)
  summary: 调节器超前时间常数 1 0.8（默认）| 正标量
  group: 控制
- name: Voltage regulator denominator (lag) time constant (second block), T_B2 (s)
  summary: 调节器滞后时间常数 2 0.01（默认）| 正标量
  group: 控制
- name: Voltage regulator numerator (lead) time constant (second block), T_C2 (s)
  summary: 调节器超前时间常数 2 0.08（默认）| 正标量
  group: 控制
- name: UEL regulator denominator (lag) time constant (first block), T_UB1 (s)
  summary: UEL 调节器滞后时间常数 1 10（默认）
  group: 控制
- name: UEL regulator numerator (lead) time constant (first block), T_UC1 (s)
  summary: UEL 调节器超前时间常数 1 2（默认）
  group: 控制
- name: UEL regulator denominator (lag) time constant (second block), T_UB2 (s)
  summary: UEL 调节器滞后时间常数 2 0.05（默认）
  group: 控制
- name: UEL regulator numerator (lead) time constant (second block), T_UC2 (s)
  summary: UEL 调节器超前时间常数 2 0.1（默认）
  group: 控制
- name: OEL regulator denominator (lag) time constant (first block), T_OB1 (s)
  summary: OEL 调节器滞后时间常数 1 2（默认）
  group: 控制
- name: OEL regulator numerator (lead) time constant (first block), T_OC1 (s)
  summary: OEL 调节器超前时间常数 1 0.1（默认）
  group: 控制
- name: OEL regulator denominator (lag) time constant (second block), T_OB2 (s)
  summary: OEL 调节器滞后时间常数 2 0.08（默认）
  group: 控制
- name: OEL regulator numerator (lead) time constant (second block), T_OC2 (s)
  summary: OEL 调节器超前时间常数 2 0.08（默认）
  group: 控制
- name: Maximum regulator output, V_Rmax (pu)
  summary: 调节器最大输出 5（默认）| 实数标量
  group: 控制
- name: Minimum regulator output, V_Rmin (pu)
  summary: 调节器最小输出 -4（默认）| 实数标量
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
  summary: 整流器负载因数 0.004（默认）| 正标量
  group: 励磁机
- name: Thyristor bridge firing control equivalent time constant, T_1 (s)
  summary: 晶闸管桥触发控制时间常数 0.004（默认）| 正标量
  group: 励磁机
```

### 常规

### **Initial field voltage, Efd0 (pu)** — 初始输出电压 `1`（默认）| 实数标量

施加到同步电机励磁绕组的初始标幺电压。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请将此参数设置为 `-1`。对于离散时间操作，请将此参数设置为正整数。对于连续时间操作，请将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

### 预控制

### **Resistive component of load compensation, R\_C (pu)** — 补偿电阻 `0`（默认）| 正标量

电流补偿系统中使用的电阻。将此参数和 **Reactance component of load compensation, X\_C
(pu)** 设置为 `0` 以禁用电流补偿。

### **Reactance component of load compensation, X\_C (pu)** — 补偿电抗 `0`（默认）| 正标量

电流补偿系统中使用的电抗。将此参数和 **Resistive component of load compensation, R\_C
(pu)** 设置为 `0` 以禁用电流补偿。

### **Regulator input filter time constant, T\_R (s)** — 调节器时间常数 `0.02`（默认）| 正标量

电压变送器滤波的等效时间常数。

### 控制

### **Regulator gain, K\_R (pu)** — 调节器增益 `200`（默认）| 正标量

调节器的增益。

### **Voltage regulator denominator (lag) time constant (first block), T\_B1 (s)** — 调节器滞后时间常数 1 `6`（默认）| 正标量

电压调节器第一个超前-滞后（离散或连续）模块中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **Voltage regulator numerator (lead) time constant (first block), T\_C1 (s)** — 调节器超前时间常数 1 `0.8`（默认）| 正标量

电压调节器第一个超前-滞后（离散或连续）模块中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **Voltage regulator denominator (lag) time constant (second block), T\_B2 (s)** — 调节器滞后时间常数 2 `0.01`（默认）| 正标量

电压调节器第二个超前-滞后（离散或连续）模块中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **Voltage regulator numerator (lead) time constant (second block), T\_C2 (s)** — 调节器超前时间常数 2 `0.08`（默认）| 正标量

电压调节器第二个超前-滞后（离散或连续）模块中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **UEL regulator denominator (lag) time constant (first block), T\_UB1 (s)** — UEL 调节器滞后时间常数 1 `10`（默认）

欠励限制器调节器第一个超前-滞后（离散或连续）模块中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **UEL regulator numerator (lead) time constant (first block), T\_UC1 (s)** — UEL 调节器超前时间常数 1 `2`（默认）

欠励限制器调节器第一个超前-滞后（离散或连续）模块中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **UEL regulator denominator (lag) time constant (second block), T\_UB2 (s)** — UEL 调节器滞后时间常数 2 `0.05`（默认）

欠励限制器调节器第二个超前-滞后（离散或连续）模块中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **UEL regulator numerator (lead) time constant (second block), T\_UC2 (s)** — UEL 调节器超前时间常数 2 `0.1`（默认）

欠励限制器调节器第二个超前-滞后（离散或连续）模块中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **OEL regulator denominator (lag) time constant (first block), T\_OB1 (s)** — OEL 调节器滞后时间常数 1 `2`（默认）

过励限制器调节器第一个超前-滞后（离散或连续）模块中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **OEL regulator numerator (lead) time constant (first block), T\_OC1 (s)** — OEL 调节器超前时间常数 1 `0.1`（默认）

过励限制器调节器第一个超前-滞后（离散或连续）模块中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **OEL regulator denominator (lag) time constant (second block), T\_OB2 (s)** — OEL 调节器滞后时间常数 2 `0.08`（默认）

过励限制器调节器第二个超前-滞后（离散或连续）模块中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **OEL regulator numerator (lead) time constant (second block), T\_OC2 (s)** — OEL 调节器超前时间常数 2 `0.08`（默认）

过励限制器调节器第二个超前-滞后（离散或连续）模块中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **Maximum regulator output, V\_Rmax (pu)** — 调节器最大输出 `5`（默认）| 实数标量

调节器最大标幺输出。

### **Minimum regulator output, V\_Rmin (pu)** — 调节器最小输出 `-4`（默认）| 实数标量

调节器最小标幺输出。

### **Alternate OEL input locations (V\_OEL)** — OEL 输入位置 `Unused`（默认）| `Summation point` | `Take-over`

过励限制器输入位置。

### **Alternate UEL input locations (V\_UEL)** — UEL 输入位置 `Unused`（默认）| `Summation point` | `Take-over`

欠励限制器输入位置。

### **Alternate SCL input locations (V\_SCL)** — SCL 输入位置 `Unused`（默认）| `Summation point` | `Take-over`

定子电流限制器输入位置，指定为以下选项之一：

- `Summation point` — 使用
  **V\_SCLsum** 输入端口。
- `Take-over` — 使用
  **V\_SCLoel** 和
  **V\_SCLuel** 输入端口。

### 励磁机

### **Rectifier loading factor proportional to commutating reactance, K\_C (pu)** — 整流器负载因数 `0.004`（默认）| 正标量

标幺整流器负载因数。该值与换相电抗成正比。

### **Thyristor bridge firing control equivalent time constant, T\_1 (s)** — 晶闸管桥触发控制时间常数 `0.004`（默认）| 正标量

晶闸管桥触发控制的等效时间常数，以秒为单位。
## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

离散时间或连续时间同步电机 ST5C 静态励磁系统，带自动电压调节器

SM ST5C 模块实现了符合 IEEE Std 421.5-2016 [1] 的同步电机型 ST5C 静态励磁系统模型。

使用此模块对同步电机励磁电压的控制和调节进行建模。

使用 **Sample time (-1 for inherited)** 参数在模块的连续实现和离散实现之间切换。要将积分器配置为连续时间，请将 **Sample time (-1 for
inherited)** 参数设置为 `0`。要将积分器配置为离散时间，请将 **Sample time (-1 for inherited)** 参数设置为正标量。要从上游模块继承采样时间，请将 **Sample time (-1 for inherited)** 参数设置为 `-1`。

SM ST5C 模块包含三个主要组件：

- 电流补偿器组件根据机端电流修改测量的机端电压。
- 电压测量变送器组件使用低通滤波器模拟机端电压变送器的动态特性。
- 励磁控制元件组件将电压变送器输出与机端电压参考进行比较，以产生电压误差值。该组件随后将此值通过电压调节器以产生励磁电压。

此图显示了 ST5C 励磁系统模型的结构：

图中：

- *VT* 和
  *IT* 分别为同步电机的测量机端电压和电流。
- *VC1* 为电流补偿后的机端电压。
- *VC* 为滤波后的电流补偿机端电压。
- *VREF* 为参考机端电压。
- *VS* 为电力系统稳定器电压。
- *EFD* 和
  *IFD* 分别为励磁电压和励磁电流。

### 电流补偿器和电压测量变送器

该模块使用以下方程对电流补偿器进行建模：

VC1=VT+ITRC2+XC2，

其中：

- *RC* 为负载补偿电阻。
- *XC* 为负载补偿电抗。

该模块将电压测量变送器实现为具有时间常数 *TR* 的低通滤波器模块。有关精确的离散和连续实现的信息，请参阅低通滤波器模块的文档。

### 励磁控制元件

此图显示了励磁控制元件的结构：

图中：

- 求和点逻辑子系统对过励限制器（OEL）、欠励限制器（UEL）、定子电流限制器（SCL）和电源开关选择器（V\_S）电压的求和点输入位置进行建模。有关在此模块中使用限制器的详细信息，请参阅 Field Current Limiters。
- 接管逻辑子系统对 OEL、UEL、SCL 和 PSS 电压的接管点输入位置进行建模。有关在此模块中使用限制器的详细信息，请参阅 Field Current Limiters。
- 超前-滞后（离散或连续）模块的并联配置在限制器激活时提供独立控制设置。该模型为 AVR 以及欠励和过励限制器提供一个公共增益因子 *KR* 和两个超前-滞后（离散或连续）模块。当 *VUEL* 和/或 *VOEL* 信号连接到各自的备用位置时，SW\_UEL 和 SW\_OEL 开关模块激活相应的控制路径。当您将 **Alternate UEL input locations (V\_UEL)** 和 **Alternate OEL input locations (V\_OEL)** 参数设置为 `Take-over at voltage error` 时，SW\_UEL 和 SW\_OEL 开关模块处于位置 B。
- 每个控制路径中的两个超前-滞后模块对与电压调节器以及与欠励和过励限制器相关的附加动态进行建模。每个相应路径中的第一个超前-滞后模块表示瞬态增益降低，其中 *TC*（或 *TC2* 和 *TUC2*）为超前时间常数，*TB*（或 *TB2* 和 *TUB2*）为滞后时间常数。第二个超前-滞后模块允许表示瞬态增益增加的可能性，其中 *TC1* 为超前时间常数，*TB1* 为滞后时间常数。有关离散和连续实现的信息，请参阅超前-滞后模块的文档。

### Field Current Limiters

您可以使用不同类型的励磁电流限制器，在不安全运行条件下修改电压调节器的输出：

- 使用过励限制器，防止因励磁电流需求过大而导致励磁绕组过热。
- 使用欠励限制器，在励磁过低时提升励磁，否则会有失步风险。
- 使用定子电流限制器，防止因电流过大而导致定子绕组过热。

将这些限制器中任意一个的输出连接到以下任一位置：

- 求和点 — 将限制器用作自动电压调节器（AVR）反馈回路的一部分。
- 接管点 — 覆盖 AVR 的通常行为。

如果在求和点使用定子电流限制器，请使用输入 *VSCLsum*。如果在接管点使用定子电流限制器，请使用过励输入 *VSCLoel*，以及欠励输入 *VSCLuel*。
