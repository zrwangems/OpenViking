---
type: simulink-block
title: 'SM ST7C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smst7c'
documentation_source_path: 'ref/smst7c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM ST7C

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
  summary: 用于过励限制器的接管定子电流限制标量
  direction: input
  data_types: single | double
- name: V_SCLuel
  summary: 用于欠励限制器的接管定子电流限制标量
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
  `Summation point at voltage
  reference`。
- 要在 Take-over Logic 子系统处使用来自过励限制器的输入，请将 **Alternate
  OEL input locations (V\_OEL)** 设置为
  `Take-over at voltage
  error`。
- 要在 Take-over Logic1 子系统处使用来自过励限制器的输入，请将 **Alternate
  OEL input locations (V\_OEL)** 设置为
  `Take-over at voltage regulator
  output`。

**数据类型：** `single` | `double`

### **V\_UEL** — 欠励限制信号标量

来自欠励限制器的输入，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自欠励限制器的输入，请将 **Alternate UEL input locations
  (V\_UEL)** 设置为
  `Unused`。
- 要在求和点使用来自欠励限制器的输入，请将 **Alternate UEL input
  locations (V\_UEL)** 设置为
  `Summation point at voltage
  reference`。
- 要在 Take-over Logic 子系统处使用来自欠励限制器的输入，请将 **Alternate
  UEL input locations (V\_UEL)** 设置为
  `Take-over at voltage
  error`。
- 要在 Take-over Logic1 子系统处使用来自欠励限制器的输入，请将 **Alternate
  UEL input locations (V\_UEL)** 设置为
  `Take-over at voltage regulator
  output`。

**数据类型：** `single` | `double`

### **V\_SCLsum** — 求和点定子电流限制信号标量

使用求和点时来自定子电流限制器的输入，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations
  (V\_SCL)** 设置为
  `Unused`。
- 要在求和点使用来自定子电流限制器的输入，请将 **Alternate SCL input
  locations (V\_SCL)** 设置为
  `Summation point at voltage
  reference`。

**数据类型：** `single` | `double`

### **V\_SCLoel** — 用于过励限制器的接管定子电流限制标量

使用接管点时来自定子电流限制器的输入，用于防止励磁过励，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations
  (V\_SCL)** 设置为
  `Unused`。
- 要在 Take-over Logic 子系统处使用来自定子电流限制器的输入，请将 **Alternate
  SCL input locations (V\_SCL)** 设置为
  `Take-over at voltage
  reference`。
- 要在 Take-over Logic1 子系统处使用来自定子电流限制器的输入，请将 **Alternate
  SCL input locations (V\_SCL)** 设置为
  `Take-over at voltage regulator
  output`。

**数据类型：** `single` | `double`

### **V\_SCLuel** — 用于欠励限制器的接管定子电流限制标量

使用接管点时来自定子电流限制器的输入，用于防止励磁欠励，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations
  (V\_SCL)** 设置为
  `Unused`。
- 要在 Take-over Logic 子系统处使用来自定子电流限制器的输入，请将 **Alternate
  SCL input locations (V\_SCL)** 设置为
  `Take-over at voltage
  error`。
- 要在 Take-over Logic1 子系统处使用来自定子电流限制器的输入，请将 **Alternate
  SCL input locations (V\_SCL)** 设置为
  `Take-over at voltage regulator
  output`。

**数据类型：** `single` | `double`
### 输出

### **Efd\_pu** — 励磁电压标量

要施加到同步电机励磁绕组的标幺值励磁电压，以标量形式返回。

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
  summary: 调节器时间常数 0（默认）| 正标量
  group: 预控制
- name: Regulator input filter time constant, T_G (s)
  summary: 电压滤波时间常数 1（默认）| 正标量
  group: 控制
- name: Voltage regulator denominator (lag) time constant, T_F (s)
  summary: 电压调节器的滞后时间常数 1（默认）| 正标量
  group: 控制
- name: Maximum voltage reference, V_max (pu)
  summary: 最大电压参考 1.1（默认）| 实数标量
  group: 控制
- name: Minimum voltage reference, V_min (pu)
  summary: 最小电压参考 0.9（默认）| 实数标量
  group: 控制
- name: Voltage regulator gain, K_PA (pu)
  summary: 电压调节器增益 40（默认）| 正标量
  group: 控制
- name: Voltage regulator denominator (lag) time constant, T_B (s)
  summary: 电压调节器滞后时间常数 1（默认）| 正标量
  group: 控制
- name: Voltage regulator numerator (lead) time constant, T_C (s)
  summary: 电压调节器超前时间常数 1（默认）| 正标量
  group: 控制
- name: Thyristor bridge firing control equivalent time constant, T_A (s)
  summary: 第一个超前-滞后环节的调节器滞后时间常数 0（默认）| 正标量
  group: 控制
- name: Maximum regulator output, V_Rmax (pu)
  summary: 最大调节器输出 5（默认）| 实数标量
  group: 控制
- name: Minimum regulator output, V_Rmin (pu)
  summary: 最小调节器输出 -4.5（默认）| 实数标量
  group: 控制
- name: Alternate OEL input locations (V_OEL)
  summary: OEL 输入位置 Unused（默认）| Summation point at voltage reference | Take-over at voltage reference | Take-over at voltage
    regulator output
  group: 控制
- name: Alternate UEL input locations (V_UEL)
  summary: UEL 输入位置 Unused（默认）| Summation point at voltage reference | Take-over at voltage reference | Take-over at voltage
    regulator output
  group: 控制
- name: Alternate SCL input locations (V_SCL)
  summary: SCL 输入位置 Unused（默认）| Summation point at voltage reference | Take-over at voltage reference | Take-over at voltage
    regulator output
  group: 控制
- name: Minimum excitation limit gain, K_L (pu)
  summary: 最小励磁限制增益 1（默认）| 实数标量
  group: 励磁机
- name: Maximum excitation limit gain, K_H (pu)
  summary: 最大励磁限制增益 1（默认）| 实数标量
  group: 励磁机
- name: PI regulator feedback gain, K_IA (pu)
  summary: PI 调节器反馈增益 1（默认）| 实数标量
  group: 励磁机
- name: PI regulator feedback time constant, T_IA (s)
  summary: PI 调节器反馈时间常数 3（默认）| 正标量
  group: 励磁机
```

### 常规

### **Initial field voltage, Efd0 (pu)** — 初始输出电压 `1`（默认）| 实数标量

要施加到同步电机励磁绕组的初始标幺值电压。

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

### **Regulator input filter time constant, T\_R (s)** — 调节器时间常数 `0`（默认）| 正标量

电压传感器滤波的等效时间常数。

### 控制

### **Regulator input filter time constant, T\_G (s)** — 电压滤波时间常数 `1`（默认）| 正标量

电压滤波的等效时间常数。

### **Voltage regulator denominator (lag) time constant, T\_F (s)** — 电压调节器的滞后时间常数 `1`（默认）| 正标量

电压调节器的等效滞后时间常数，以秒为单位。

### **Maximum voltage reference, V\_max (pu)** — 最大电压参考 `1.1`（默认）| 实数标量

电压调节器的最大标幺值电压参考。

### **Minimum voltage reference, V\_min (pu)** — 最小电压参考 `0.9`（默认）| 实数标量

电压调节器的最小标幺值电压参考。

### **Voltage regulator gain, K\_PA (pu)** — 电压调节器增益 `40`（默认）| 正标量

电压调节器的标幺值增益。

### **Voltage regulator denominator (lag) time constant, T\_B (s)** — 电压调节器滞后时间常数 `1`（默认）| 正标量

电压调节器的等效滞后时间常数。当附加滞后动态
可忽略时，请将此参数设置为 `0`。

### **Voltage regulator numerator (lead) time constant, T\_C (s)** — 电压调节器超前时间常数 `1`（默认）| 正标量

电压调节器的等效超前时间常数。当附加超前动态
可忽略时，请将此参数设置为 `0`。

### **Thyristor bridge firing control equivalent time constant, T\_A (s)** — 第一个超前-滞后环节的调节器滞后时间常数 `0`（默认）| 正标量

晶闸管桥触发控制中的等效时间常数。

### **Maximum regulator output, V\_Rmax (pu)** — 最大调节器输出 `5`（默认）| 实数标量

调节器的最大标幺值输出。

### **Minimum regulator output, V\_Rmin (pu)** — 最小调节器输出 `-4.5`（默认）| 实数标量

调节器的最小标幺值输出。

### **Alternate OEL input locations (V\_OEL)** — OEL 输入位置 `Unused`（默认）| `Summation point at voltage reference` | `Take-over at voltage reference` | `Take-over at voltage regulator output`

过励限制器输入位置，指定为以下选项之一：

- `Summation point at voltage
  reference` — **V\_OEL** 是
  Summation Point Logic 子系统的输入。
- `Take-over at voltage reference`
  — **V\_OEL** 是 Take-over
  Logic 子系统的输入。
- `Take-over at voltage regulator
  output` — **V\_OEL** 是
  Take-over Logic 1 子系统的输入。

### **Alternate UEL input locations (V\_UEL)** — UEL 输入位置 `Unused`（默认）| `Summation point at voltage reference` | `Take-over at voltage reference` | `Take-over at voltage regulator output`

欠励限制器输入位置，指定为以下选项之一：

- `Summation point at voltage
  reference` — **V\_UEL** 是
  Summation Point Logic 子系统的输入。
- `Take-over at voltage reference`
  — **V\_UEL** 是 Take-over
  Logic 子系统的输入。
- `Take-over at voltage regulator
  output` — **V\_UEL** 是
  Take-over Logic 1 子系统的输入。

### **Alternate SCL input locations (V\_SCL)** — SCL 输入位置 `Unused`（默认）| `Summation point at voltage reference` | `Take-over at voltage reference` | `Take-over at voltage regulator output`

定子电流限制器输入位置，指定为以下选项之一：

- `Summation point` — 使用
  **V\_SCLsum** 输入端口。
- 任意 `Take-over` 选项 —
  使用 **V\_SCLoel** 和
  **V\_SCLuel** 输入端口。

### 励磁机

### **Minimum excitation limit gain, K\_L (pu)** — 最小励磁限制增益 `1`（默认）| 实数标量

励磁机的最小标幺值增益。

### **Maximum excitation limit gain, K\_H (pu)** — 最大励磁限制增益 `1`（默认）| 实数标量

励磁机的最大标幺值增益。

### **PI regulator feedback gain, K\_IA (pu)** — PI 调节器反馈增益 `1`（默认）| 实数标量

PI 调节器的标幺值反馈增益。

### **PI regulator feedback time constant, T\_IA (s)** — PI 调节器反馈时间常数 `3`（默认）| 正标量

PI 调节器的反馈时间常数，以秒为单位。
## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

具有自动电压调节器的离散时间或连续时间同步电机 ST7C 静态励磁系统

SM ST7C 模块实现了一个符合 IEEE Std 421.5-2016 [1] 的同步电机型 ST7C 静态
励磁系统模型。

使用此模块对同步电机励磁电压的控制和调节进行建模。

通过使用 **Sample time (-1 for inherited)** 参数在模块的连续实现和离散实现之间
切换。要将积分器配置为连续时间，请将 **Sample time (-1 for
inherited)** 参数设置为 `0`。要将积分器配置
为离散时间，请将 **Sample time (-1 for inherited)** 参数
设置为正标量。要从上游模块继承采样时间，请将
**Sample time (-1 for inherited)** 参数设置为
`-1`。

SM ST7C 模块包含三个主要组件：

- Current Compensator 组件根据机端电流修改测量的机端电压。
- Voltage Measurement Transducer 组件使用低通滤波器模拟机端电压传感器的动态特性。
- Excitation Control Elements 组件将电压传感器输出与机端电压参考进行比较，以产生电压误差值。
  然后，该组件将此值通过电压调节器以产生励磁电压。

此图显示了 ST7C 励磁系统模型的结构：

在图中：

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
- *EFD* 是励磁电压。

### 电流补偿器和电压测量传感器

该模块使用以下方程对电流补偿器进行建模：

VC1=VT+ITRC2+XC2，

其中：

- *RC* 是负载补偿
  电阻。
- *XC* 是负载补偿
  电抗。

该模块将电压测量传感器实现为具有时间常数
*TR* 的 Low-Pass Filter 模块。有关精确的离散和连续
实现的信息，请参阅 Low-Pass Filter 模块的文档。

### 励磁控制元件

此图显示了励磁控制元件的结构：

在图中：

- Summation Point Logic 子系统对过励限制器 (OEL)、欠励限制器
  (UEL) 和定子电流限制器 (SCL) 电压的求和点输入
  位置进行建模。有关将限制器与此模块一起使用的更多信息，请参阅
  Field Current Limiters。
- 有两个 Take-over Logic 子系统。这些子系统对
  OEL、UEL 和 SCL 电压的接管点输入位置进行建模。有关
  将限制器与此模块一起使用的更多信息，请参阅 Field Current Limiters。
- 串联的 Lead-Lag 模块引入微分功能
  并将调节器转换为 PID。这通常仅用于
  无刷励磁系统。
- *KL* 和
  *KH* 对调节发电机
  励磁电流的高带宽调节器内环进行建模。

### 励磁电流限制器

您可以使用不同类型的励磁电流限制器在不安全的运行条件下修改电压
调节器的输出：

- 使用过励限制器防止因过大的励磁电流需求而导致励磁
  绕组过热。
- 使用欠励限制器在励磁过低时提升励磁，因为励磁过低
  存在失步风险。
- 使用定子电流限制器防止因电流过大而导致定子
  绕组过热。

将任何这些限制器的输出连接到以下点之一：

- 求和点 — 将限制器用作自动电压
  调节器 (AVR) 反馈回路的一部分。
- 接管点 — 覆盖 AVR 的常规行为。

如果您在求和点使用定子电流限制器，
请使用输入 *VSCLsum*。如果您
在接管点使用定子电流限制器，请使用过励输入
*VSCLoel* 和欠励
输入 *VSCLuel*。
