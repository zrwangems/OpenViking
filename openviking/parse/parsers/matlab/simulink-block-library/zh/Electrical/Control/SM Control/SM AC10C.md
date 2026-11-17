---
type: simulink-block
title: 'SM AC10C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smac10c'
documentation_source_path: 'ref/smac10c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM AC10C

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
  summary: 过励限制器的接管定子电流限制标量
  direction: input
  data_types: single | double
- name: V_SCLuel
  summary: 欠励限制器的接管定子电流限制标量
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

来自欠励限制器的输入，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自欠励限制器的输入，请将 **Alternate UEL input locations
  (V\_UEL)** 设置为
  `Unused`。
- 要在求和点使用来自欠励限制器的输入，请将 **Alternate UEL input
  locations (V\_UEL)** 设置为
  `Summation point`。
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

使用求和点时来自定子电流限制器的输入，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations
  (V\_SCL)** 设置为
  `Unused`。
- 要在求和点使用来自定子电流限制器的输入，请将 **Alternate SCL input
  locations (V\_SCL)** 设置为
  `Summation point`。

**数据类型：** `single` | `double`

### **V\_SCLoel** — 过励限制器的接管定子电流限制标量

使用接管点时来自定子电流限制器的输入，用于防止励磁过励，采用标幺值表示，指定为标量。

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

### **V\_SCLuel** — 欠励限制器的接管定子电流限制标量

使用接管点时来自定子电流限制器的输入，用于防止励磁欠励，采用标幺值表示，指定为标量。

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
  summary: 调节器时间常数 0.01（默认）| 正标量
  group: 预控制
- name: Regulator gain, K_R (pu)
  summary: 调节器增益 600（默认）| 正标量
  group: 控制
- name: Voltage regulator denominator (lag) time constant 1, T_B1 (s)
  summary: 调节器滞后时间常数 1 22.5（默认）| 正标量
  group: 控制
- name: Voltage regulator numerator (lead) time constant 1, T_C1 (s)
  summary: 调节器超前时间常数 1 3（默认）| 正标量
  group: 控制
- name: Voltage regulator denominator (lag) time constant 2, T_B2 (s)
  summary: 调节器滞后时间常数 2 0.13（默认）| 正标量
  group: 控制
- name: Voltage regulator numerator (lead) time constant 2, T_C2 (s)
  summary: 调节器超前时间常数 2 0.9（默认）| 正标量
  group: 控制
- name: UEL regulator denominator (lag) time constant 1, T_UB1 (s)
  summary: UEL 调节器滞后时间常数 1 22.5（默认）
  group: 控制
- name: UEL regulator numerator (lead) time constant 1, T_UC1 (s)
  summary: UEL 调节器超前时间常数 1 3（默认）
  group: 控制
- name: UEL regulator denominator (lag) time constant 2, T_UB2 (s)
  summary: UEL 调节器滞后时间常数 2 0.13（默认）
  group: 控制
- name: UEL regulator numerator (lead) time constant 2, T_UC2 (s)
  summary: UEL 调节器超前时间常数 2 0.9（默认）
  group: 控制
- name: OEL regulator denominator (lag) time constant 1, T_OB1 (s)
  summary: OEL 调节器滞后时间常数 1 18（默认）
  group: 控制
- name: OEL regulator numerator (lead) time constant 1, T_OC1 (s)
  summary: OEL 调节器超前时间常数 1 0.9（默认）
  group: 控制
- name: OEL regulator denominator (lag) time constant 2, T_OB2 (s)
  summary: OEL 调节器滞后时间常数 2 0.1（默认）
  group: 控制
- name: OEL regulator numerator (lead) time constant 2, T_OC2 (s)
  summary: OEL 调节器超前时间常数 2 0.1（默认）
  group: 控制
- name: Maximum regulator output, V_Rmax (pu)
  summary: 最大调节器输出 40（默认）| 实数标量
  group: 控制
- name: Minimum regulator output, V_Rmin (pu)
  summary: 最小调节器输出 -35（默认）| 实数标量
  group: 控制
- name: Maximum PSS regulator output, V_RSmax (pu)
  summary: 最大 PSS 调节器输出 20（默认）| 实数标量
  group: 控制
- name: Minimum PSS regulator output, V_RSmin (pu)
  summary: 最小 PSS 调节器输出 -20（默认）| 实数标量
  group: 控制
- name: Exciter field current regulator measurement time constant, T_EXC (s)
  summary: 励磁机励磁电流调节器测量时间常数 0（默认）| 正标量
  group: 控制
- name: Exciter field current regulator feedback gain, K_EXC (pu)
  summary: 励磁机励磁电流调节器反馈增益 1（默认）| 正标量
  group: 控制
- name: Exciter field current regulator proportional gain, K_CR (pu)
  summary: 励磁机励磁电流调节器比例增益 0（默认）| 正标量
  group: 控制
- name: Exciter field current regulator feedback selector SW_EXC
  summary: '励磁机励磁电流调节器反馈选择器 Position A: feedback from generator field voltage (E_FD)（默认）| Position B: feedback from exciter
    field current (V_FE)'
  group: 控制
- name: Exciter field current regulator numerator (lead) time constant, T_F1 (s)
  summary: 励磁机励磁电流调节器中的超前时间常数 0.1（默认）| 正标量
  group: 控制
- name: Exciter field current regulator denominator (lag) time constant, T_F2 (s)
  summary: 励磁机励磁电流调节器中的滞后时间常数 0.1（默认）| 正标量
  group: 控制
- name: Exciter field current limiter feedback gain, K_VFE (pu)
  summary: 励磁机励磁电流限制器增益 1（默认）| 正标量
  group: 控制
- name: Exciter field current limiter proportional gain, K_LIM (pu)
  summary: 励磁机励磁电流比例增益 0（默认）| 正标量
  group: 控制
- name: Exciter field current limiter reference, V_FELIM (pu)
  summary: 励磁系统励磁电流限制器参考值 20（默认）| 实数标量
  group: 控制
- name: Alternate PSS input locations (V_S)
  summary: PSS 输入位置 Voltage error or after take-over limits（默认）| Voltage error calculation | Output of AVR (after take-over
    limits)
  group: 控制
- name: Alternate OEL input locations (V_OEL)
  summary: OEL 输入位置 Take-over at voltage error（默认）| Summation point at voltage error | Unused | Take-over at voltage regulator
    output
  group: 控制
- name: Alternate UEL input locations (V_UEL)
  summary: UEL 输入位置 Take-over at voltage error（默认）| Summation point at voltage error | Unused | Take-over at voltage regulator
    output
  group: 控制
- name: Alternate SCL input locations (V_SCL)
  summary: SCL 输入位置 Take-over at voltage error（默认）| Summation point at voltage error | Unused | Take-over at voltage regulator
    output
  group: 控制
- name: Exciter field proportional constant, K_E (pu)
  summary: 励磁机磁场增益 1（默认）| 正标量
  group: Exciter
- name: Exciter field time constant, T_E (s)
  summary: 励磁机磁场时间常数 1.3（默认）| 正标量
  group: Exciter
- name: Rectifier loading factor proportional to commutating reactance, K_C (pu)
  summary: 整流器负载因子 0.13（默认）| 正标量
  group: Exciter
- name: Demagnetizing factor, function of exciter alternator reactances, K_D (pu)
  summary: 去磁因子 1.15（默认）| 正标量
  group: Exciter
- name: Exciter output voltage for saturation factor S_E(E_1), E_1 (pu)
  summary: 第一饱和输出电压 10（默认）| 正标量
  group: Exciter
- name: Exciter saturation factor at exciter output voltage E_1, S_E(E_1) (1)
  summary: 第一饱和查找电压 0.214（默认）| 正标量
  group: Exciter
- name: Exciter output voltage for saturation factor S_E(E_2), E_2 (pu)
  summary: 第二饱和输出电压 7.5（默认）| 正标量
  group: Exciter
- name: Exciter saturation factor at exciter output voltage E_2, S_E(E_2) (1)
  summary: 第二饱和查找电压 0.044（默认）| 正标量
  group: Exciter
- name: Maximum exciter field current, V_FEmax (pu)
  summary: 励磁机上限 44（默认）| 实标量
  group: Exciter
- name: Minimum exciter voltage output limit, V_Emin (pu)
  summary: 励磁机下限 0（默认）| 实标量
  group: Exciter
- name: Potential circuit gain coefficient, K_P (pu)
  summary: 电位电路增益系数 1（默认）| 实标量
  group: Exciter
- name: Potential circuit phase angle (degrees)
  summary: 电位电路相位角 0（默认）| 实标量
  group: Exciter
- name: Potential circuit (current) gain coefficient, K_I (pu)
  summary: 电位电路电流增益系数 0（默认）| 实标量
  group: Exciter
- name: Reactance associated with potential source, X_L (pu)
  summary: 与电位源相关的reactance 0（默认）| 实标量
  group: Exciter
- name: Rectifier loading factor proportional to commutating reactance, K_C1 (pu)
  summary: 与换相电抗成正比的整流器负载因子 0（默认）| 实标量
  group: Exciter
- name: Power source selector SW1
  summary: '电源选择器 Position B: power source independent of the terminal conditions（默认）| Position A: power source derived from
    terminal voltage'
  group: Exciter
- name: Maximum available exciter voltage, V_B1max (pu)
  summary: 最大可用励磁机磁场电压 1.5（默认）| 实标量
  group: Exciter
- name: Rectifier loading factor proportional to commutating reactance, K_C2 (pu)
  summary: 与换相电抗成正比的整流器负载因子 0（默认）| 实标量
  group: Exciter
- name: Additive potential circuit (current) gain coefficient, K_I2 (pu)
  summary: 附加电路电流增益系数 0（默认）| 实标量
  group: Exciter
- name: Maximum available exciter voltage, V_B2max (pu)
  summary: 最大可用励磁机电压 0（默认）| 实标量
  group: Exciter
```

### 常规

### **Initial field voltage, Efd0 (pu)** — 初始输出电压 `1`（默认）| 实数标量

施加到同步电机励磁绕组的初始标幺电压。

### **Initial terminal voltage, Vt0 (pu)** — 初始机端电压 `1`（默认）| 实数标量

施加到机端的初始标幺电压。

#### 依赖关系

要启用此参数，请在 Exciter 部分中，将
**Power source selector SW1** 设置为
`Position A: power source derived from terminal
voltage`。

### **Initial terminal current, It0 (pu)** — 初始机端电流 `1`（默认）| 实数标量

施加到机端的初始标幺电流。

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

### **Regulator input filter time constant, T\_R (s)** — 调节器时间常数 `0.01`（默认）| 正标量

电压传感器滤波的等效时间常数。

### 控制

### **Regulator gain, K\_R (pu)** — 调节器增益 `600`（默认）| 正标量

调节器的增益。

### **Voltage regulator denominator (lag) time constant 1, T\_B1 (s)** — 调节器滞后时间常数 1 `22.5`（默认）| 正标量

电压调节器第二个 Lead-Lag (Discrete
or Continuous) 模块中的等效滞后时间常数。当附加滞后
动态可忽略时，将此参数设置为 `0`。

### **Voltage regulator numerator (lead) time constant 1, T\_C1 (s)** — 调节器超前时间常数 1 `3`（默认）| 正标量

电压调节器第二个 Lead-Lag (Discrete
or Continuous) 模块中的等效超前时间常数。当附加超前
动态可忽略时，将此参数设置为 `0`。

### **Voltage regulator denominator (lag) time constant 2, T\_B2 (s)** — 调节器滞后时间常数 2 `0.13`（默认）| 正标量

电压调节器第一个 Lead-Lag (Discrete or
Continuous) 模块中的等效滞后时间常数。当附加滞后
动态可忽略时，将此参数设置为 `0`。

### **Voltage regulator numerator (lead) time constant 2, T\_C2 (s)** — 调节器超前时间常数 2 `0.9`（默认）| 正标量

电压调节器第一个 Lead-Lag (Discrete
or Continuous) 模块中的等效超前时间常数。当附加超前
动态可忽略时，将此参数设置为 `0`。

### **UEL regulator denominator (lag) time constant 1, T\_UB1 (s)** — UEL 调节器滞后时间常数 1 `22.5`（默认）

欠励限制器调节器第二个 Lead-Lag (Discrete
or Continuous) 模块中的等效滞后时间常数。当附加滞后
动态可忽略时，将此参数设置为 `0`。

### **UEL regulator numerator (lead) time constant 1, T\_UC1 (s)** — UEL 调节器超前时间常数 1 `3`（默认）

欠励限制器调节器第二个 Lead-Lag (Discrete
or Continuous) 模块中的等效超前时间常数。当附加超前
动态可忽略时，将此参数设置为 `0`。

### **UEL regulator denominator (lag) time constant 2, T\_UB2 (s)** — UEL 调节器滞后时间常数 2 `0.13`（默认）

欠励限制器调节器第一个 Lead-Lag (Discrete or
Continuous) 模块中的等效滞后时间常数。
当附加滞后动态可忽略时，将此参数设置为 `0`。

### **UEL regulator numerator (lead) time constant 2, T\_UC2 (s)** — UEL 调节器超前时间常数 2 `0.9`（默认）

欠励限制器调节器第一个 Lead-Lag (Discrete
or Continuous) 模块中的等效超前时间常数。当附加超前
动态可忽略时，将此参数设置为 `0`。

### **OEL regulator denominator (lag) time constant 1, T\_OB1 (s)** — OEL 调节器滞后时间常数 1 `18`（默认）

过励限制器调节器第二个 Lead-Lag (Discrete
or Continuous) 模块中的等效滞后时间常数。当附加滞后
动态可忽略时，将此参数设置为 `0`。

### **OEL regulator numerator (lead) time constant 1, T\_OC1 (s)** — OEL 调节器超前时间常数 1 `0.9`（默认）

过励限制器调节器第二个 Lead-Lag (Discrete
or Continuous) 模块中的等效超前时间常数。当附加超前
动态可忽略时，将此参数设置为 `0`。

### **OEL regulator denominator (lag) time constant 2, T\_OB2 (s)** — OEL 调节器滞后时间常数 2 `0.1`（默认）

过励限制器调节器第一个 Lead-Lag (Discrete or
Continuous) 模块中的等效滞后时间常数。
当附加滞后动态可忽略时，将此参数设置为 `0`。

### **OEL regulator numerator (lead) time constant 2, T\_OC2 (s)** — OEL 调节器超前时间常数 2 `0.1`（默认）

过励限制器调节器第一个 Lead-Lag (Discrete
or Continuous) 模块中的等效超前时间常数。当附加超前
动态可忽略时，将此参数设置为 `0`。

### **Maximum regulator output, V\_Rmax (pu)** — 最大调节器输出 `40`（默认）| 实数标量

最大标幺调节器输出。

### **Minimum regulator output, V\_Rmin (pu)** — 最小调节器输出 `-35`（默认）| 实数标量

最小标幺调节器输出。

### **Maximum PSS regulator output, V\_RSmax (pu)** — 最大 PSS 调节器输出 `20`（默认）| 实数标量

电力系统稳定器调节器的最大标幺输出。

### **Minimum PSS regulator output, V\_RSmin (pu)** — 最小 PSS 调节器输出 `-20`（默认）| 实数标量

电力系统稳定器调节器的最小标幺输出。

### **Exciter field current regulator measurement time constant, T\_EXC (s)** — 励磁机励磁电流调节器测量时间常数 `0`（默认）| 正标量

励磁机励磁电流调节器的测量时间常数，以秒为单位。

### **Exciter field current regulator feedback gain, K\_EXC (pu)** — 励磁机励磁电流调节器反馈增益 `1`（默认）| 正标量

励磁机励磁电流调节器的标幺反馈增益。

### **Exciter field current regulator proportional gain, K\_CR (pu)** — 励磁机励磁电流调节器比例增益 `0`（默认）| 正标量

励磁机励磁电流调节器的标幺比例增益。

### **Exciter field current regulator feedback selector SW\_EXC** — 励磁机励磁电流调节器反馈选择器 `Position A: feedback from generator field voltage (E_FD)`（默认）| `Position B: feedback from exciter field current (V_FE)`

用于选择励磁机励磁电流调节器电路中反馈变量的选项。

### **Exciter field current regulator numerator (lead) time constant, T\_F1 (s)** — 励磁机励磁电流调节器中的超前时间常数 `0.1`（默认）| 正标量

励磁机励磁电流调节器中的等效超前时间常数。
当附加滞后动态可忽略时，将此参数设置为 `0`。

### **Exciter field current regulator denominator (lag) time constant, T\_F2 (s)** — 励磁机励磁电流调节器中的滞后时间常数 `0.1`（默认）| 正标量

励磁机励磁电流调节器中的等效滞后时间常数。
当附加滞后动态可忽略时，将此参数设置为 `0`。

### **Exciter field current limiter feedback gain, K\_VFE (pu)** — 励磁机励磁电流限制器增益 `1`（默认）| 正标量

励磁系统励磁电流限制器的标幺反馈增益。

### **Exciter field current limiter proportional gain, K\_LIM (pu)** — 励磁机励磁电流比例增益 `0`（默认）| 正标量

励磁系统励磁电流限制器的标幺比例增益。

如果将此参数设置为大于
`0` 的值，则 SW\_LIM Switch 模块位于位置 "A"，并且
励磁机励磁电流限制器处于活动状态。

如果将此参数和 **Exciter field current
regulator proportional gain, K\_CR (pu)** 参数都设置为
`0`，则 SW\_SS Switch 模块位于位置 "A"，并且
Current control 子系统不活动。

### **Exciter field current limiter reference, V\_FELIM (pu)** — 励磁系统励磁电流限制器参考值 `20`（默认）| 实数标量

励磁系统励磁电流限制器的标幺参考值。

### **Alternate PSS input locations (V\_S)** — PSS 输入位置 `Voltage error or after take-over limits`（默认）| `Voltage error calculation` | `Output of AVR (after take-over limits)`

电力系统稳定器输入的位置。

### **Alternate OEL input locations (V\_OEL)** — OEL 输入位置 `Take-over at voltage error`（默认）| `Summation point at voltage error` | `Unused` | `Take-over at voltage regulator output`

过励限制器输入的位置，指定为以下选项之一：

- `Summation point at voltage
  error` — **V\_OEL** 是
  **Summation Point Logic**
  子系统的输入。
- `Take-over at voltage error` —
  **V\_OEL** 是
  **Take-over Logic** 子系统的输入。
- `Take-over at voltage regulator
  output` — **V\_OEL** 是
  **Take-over Logic 1**
  子系统的输入。

### **Alternate UEL input locations (V\_UEL)** — UEL 输入位置 `Take-over at voltage error`（默认）| `Summation point at voltage error` | `Unused` | `Take-over at voltage regulator output`

欠励限制器输入的位置，指定为以下选项之一：

- `Summation point at voltage
  error` — **V\_UEL** 是
  **Summation Point Logic**
  子系统的输入。
- `Take-over at voltage error` —
  **V\_UEL** 是
  **Take-over Logic** 子系统的输入。
- `Take-over at voltage regulator
  output` — **V\_UEL** 是
  **Take-over Logic 1**
  子系统的输入。

### **Alternate SCL input locations (V\_SCL)** — SCL 输入位置 `Take-over at voltage error`（默认）| `Summation point at voltage error` | `Unused` | `Take-over at voltage regulator output`

定子电流限制器输入的位置，指定为以下选项之一：

- `Summation point` — 使用
  **V\_SCLsum** 输入端口。
- 任意 `Take-over` 选项 —
  使用 **V\_OELscl** 和
  **V\_UELscl** 输入端口。

### Exciter

### **Exciter field proportional constant, K\_E (pu)** — 励磁机磁场增益 `1`（默认）| 正标量

励磁机磁场的比例常数。

### **Exciter field time constant, T\_E (s)** — 励磁机磁场时间常数 `1.3`（默认）| 正标量

励磁机磁场的时间常数。

### **Rectifier loading factor proportional to commutating reactance, K\_C (pu)** — 整流器负载因子 `0.13`（默认）| 正标量

整流器负载因子。该值与换相电抗成正比。

### **Demagnetizing factor, function of exciter alternator reactances, K\_D (pu)** — 去磁因子 `1.15`（默认）| 正标量

与励磁机交流发电机reactance相关的去磁因子。

### **Exciter output voltage for saturation factor S\_E(E\_1), E\_1 (pu)** — 第一饱和输出电压 `10`（默认）| 正标量

第一饱和因子对应的励磁机输出电压。

### **Exciter saturation factor at exciter output voltage E\_1, S\_E(E\_1) (1)** — 第一饱和查找电压 `0.214`（默认）| 正标量

第一励磁机的饱和因子。

### **Exciter output voltage for saturation factor S\_E(E\_2), E\_2 (pu)** — 第二饱和输出电压 `7.5`（默认）| 正标量

第二饱和因子对应的励磁机输出电压。

### **Exciter saturation factor at exciter output voltage E\_2, S\_E(E\_2) (1)** — 第二饱和查找电压 `0.044`（默认）| 正标量

第二励磁机的饱和因子。

### **Maximum exciter field current, V\_FEmax (pu)** — 励磁机上限 `44`（默认）| 实标量

最大标幺磁场电流限值参考。

### **Minimum exciter voltage output limit, V\_Emin (pu)** — 励磁机下限 `0`（默认）| 实标量

最小标幺励磁机电压输出。

### **Potential circuit gain coefficient, K\_P (pu)** — 电位电路增益系数 `1`（默认）| 实标量

标幺电位电路增益系数。

#### 依赖关系

要启用此参数，请将 **Power source selector
SW1** 设置为 `Position A: power source derived
from terminal voltage`。

### **Potential circuit phase angle (degrees)** — 电位电路相位角 `0`（默认）| 实标量

电位电路相位角，以度为单位。

#### 依赖关系

要启用此参数，请将 **Power source selector
SW1** 设置为 `Position A: power source derived
from terminal voltage`。

### **Potential circuit (current) gain coefficient, K\_I (pu)** — 电位电路电流增益系数 `0`（默认）| 实标量

标幺电位电路电流增益系数。

#### 依赖关系

要启用此参数，请将 **Power source selector
SW1** 设置为 `Position A: power source derived
from terminal voltage`。

### **Reactance associated with potential source, X\_L (pu)** — 与电位源相关的reactance `0`（默认）| 实标量

与电位源相关的标幺reactance。

#### 依赖关系

要启用此参数，请将 **Power source selector
SW1** 设置为 `Position A: power source derived
from terminal voltage`。

### **Rectifier loading factor proportional to commutating reactance, K\_C1 (pu)** — 与换相电抗成正比的整流器负载因子 `0`（默认）| 实标量

整流器的标幺负载因子。该值与换相电抗成正比。

### **Power source selector SW1** — 电源选择器 `Position B: power source independent of the terminal conditions`（默认）| `Position A: power source derived from terminal voltage`

电源选择器 SW1 的位置。

### **Maximum available exciter voltage, V\_B1max (pu)** — 最大可用励磁机磁场电压 `1.5`（默认）| 实标量

励磁机的最大标幺可用磁场电压。

### **Rectifier loading factor proportional to commutating reactance, K\_C2 (pu)** — 与换相电抗成正比的整流器负载因子 `0`（默认）| 实标量

整流器的标幺负载因子。该值与换相电抗成正比，通过单独的串联二极管桥从发电机端子电流导出。

### **Additive potential circuit (current) gain coefficient, K\_I2 (pu)** — 附加电路电流增益系数 `0`（默认）| 实标量

通过单独的串联二极管桥从发电机端子电流导出的标幺附加电路电流增益系数。将此参数设置为
`0` 可完全禁用单独的附加电源。

### **Maximum available exciter voltage, V\_B2max (pu)** — 最大可用励磁机电压 `0`（默认）| 实标量

励磁机的最大标幺可用磁场电压，通过单独的串联二极管桥从发电机端子电流导出。
## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

离散时间或连续时间同步电机 AC10C 励磁系统，包括自动电压调节器和励磁机

SM AC10C 模块实现符合 IEEE Std 421.5-2016 [1] 的同步电机 AC10C 型励磁系统模型。

使用此模块可对作为发电机运行并使用交流旋转励磁机的同步电机的磁场电压进行建模和控制与调节。

通过使用 **Sample time (-1 for inherited)** 参数在模块的连续和离散实现之间切换。要将积分器配置为连续时间，请将 **Sample time (-1 for
inherited)** 参数设置为 `0`。要将积分器配置为离散时间，请将 **Sample time (-1 for inherited)** 参数设置为正标量。要从上游模块继承采样时间，请将
**Sample time (-1 for inherited)** 参数设置为
`-1`。

SM AC10C 模块包含五个主要组件：

- Current Compensator 组件根据端子电流修改测得的端子电压。
- Voltage Measurement Transducer 组件使用低通滤波器模拟端子电压传感器的动态特性。
- Excitation Control Elements 组件将电压传感器输出与端子电压参考进行比较以产生电压误差。然后，该电压误差通过电压调节器以产生励磁机磁场电压。
- AC Rotating Exciter 组件对交流旋转励磁机建模，该励磁机产生施加到受控同步电机的磁场电压。该模块还将励磁机磁场电流
  (*VFE*) 反馈回励磁系统。
- Power Source 组件对受控整流器电源与端子电压的依赖性进行建模。

此图显示了 AC10C 励磁系统模型的结构：

图中：

- *VT* 和
  *IT* 分别是同步电机的测得端子电压和电流。
- *VC1* 是电流补偿后的端子电压。
- *VC* 是滤波后的电流补偿端子电压。
- *VREF* 是参考端子电压。
- *VS* 是电力系统稳定器电压。
- *SW1* 是为受控整流器指定的电源开关。
- *VB* 是励磁机磁场电压。
- *EFE* 和
  *VFE* 分别是励磁机磁场电压和电流。
- *EFD* 和
  *IFD* 分别是磁场电压和电流。

### Current Compensator and Voltage Measurement Transducer

该模块使用以下方程对电流补偿器建模：

VC1=VT+ITRC2+XC2，

其中：

- *RC* 是负载补偿电阻。
- *XC* 是负载补偿reactance。

该模块将电压测量传感器实现为具有时间常数
*TR* 的 Low-Pass Filter 模块。有关精确的离散和连续实现信息，请参阅 Low-Pass Filter 模块的文档。

### Excitation Control Elements

此图显示了励磁控制元件的结构：

图中：

- Summation Point Logic 子系统对过励限制器 (OEL)、欠励限制器 (UEL) 和定子电流限制器 (SCL) 的求和点输入位置进行建模。有关将此模块与限制器一起使用的更多信息，请参阅 Field Current Limiters。
- 有两个 Take-over Logic 子系统。它们对 OEL、UEL 和 SCL 电压的接管点输入位置进行建模。有关将此模块与限制器一起使用的更多信息，请参阅 Field Current Limiters。
- Lead-Lag (Discrete or Continuous) 模块的并联配置在限制器激活时提供独立控制设置。该模型为 AVR 以及欠励和过励限制器提供一个公共增益因子 *KR* 和两个 Lead-Lag (Discrete or Continuous) 模块。当 *VUEL* 和/或 *VOEL* 信号连接到各自的备用位置时，SW\_UEL 和 SW\_OEL Switch 模块激活适当的控制路径。当您将 **Alternate UEL input locations (V\_UEL)** 和 **Alternate OEL input locations (V\_OEL)** 参数设置为 `Take-over at voltage error` 时，SW\_UEL 和 SW\_OEL Switch 模块位于位置 B。
- 每个控制路径中的两个 Lead-Lag 模块对与电压调节器以及与欠励和过励限制器相关的附加动态进行建模。每个相应路径中的第一个 Lead-Lag 模块表示瞬态增益降低，其中 *TC2*（或 *TUC2* 和 *TOC2*）是超前时间常数，*TB2*（或 *TUB2* 和 *TOB2*）是滞后时间常数。第二个 Lead-Lag 模块允许表示瞬态增益增加的可能性，其中 *TC1*（或 *TUC1* 和 *TOC1*）是超前时间常数，*TB1*（或 *TUB1* 和 *TOB1*）是滞后时间常数。有关离散和连续实现的信息，请参阅 Lead-Lag 模块的文档。
- 控制信号 *VR1* 要么直接控制功率级，要么用作级联励磁机磁场电流控制环路的参考。有关 Current control 子系统的更多信息，请参阅 Current Control Subsystem。

### Current Control Subsystem

当 SW\_SS Switch 模块位于位置 “A” 时，即当您将 **Exciter field current regulator proportional gain, K\_CR (pu)** 和 **Exciter field current limiter proportional gain, K\_LIM (pu)** 参数设置为 `0` 时，SM AC10C 模块绕过 Current control 子系统。当 SW\_SS Switch 模块位于位置 “B” 时，Current control 子系统处于活动状态。Current control 子系统还提供一个限制器，以避免励磁机过载并将励磁机电流限制为 **Exciter field current limiter reference, V\_FELIM (pu)** 参数的值。

当 SW\_LIM Switch 模块位于位置 “B” 时，即当 **Exciter field current limiter proportional gain, K\_LIM (pu)** 参数大于零时，励磁机磁场电流限制器处于活动状态。当 SW\_LIM Switch 模块位于位置 “A” 时，限制器被绕过。SW\_EXC Switch 模块允许您选择反馈变量。

### Field Current Limiters

您可以使用不同类型的磁场电流限制器在不安全运行条件下修改电压调节器的输出：

- 使用过励限制器防止因过大的磁场电流需求而导致磁场绕组过热。
- 使用欠励限制器在磁场励磁过低时提升磁场励磁，过低会有失步风险。
- 使用定子电流限制器防止因过大电流而导致定子绕组过热。

将任何这些限制器的输出连接到以下点之一：

- Summation point — 将限制器用作自动电压调节器 (AVR) 反馈环路的一部分。
- Take-over point — 覆盖 AVR 的通常行为。

如果在求和点使用定子电流限制器，请使用输入 *VSCLsum*。如果在接管点使用定子电流限制器，请使用过励输入 *VOELscl* 和欠励输入 *VUELscl*。

### AC Rotating Exciter

此图显示了交流旋转励磁机的结构：

图中：

- 励磁机磁场电流 *VFE* 是三个信号之和：

  - 非线性函数 *Vx* 对励磁机输出电压的饱和进行建模。
  - 比例项 *KE* 对励磁机输出电压与励磁机磁场电流之间的线性关系进行建模。
  - 该子系统使用反馈环路中的去磁常数 *KD* 对负载电流对励磁机输出电压的去磁效应进行建模。
- Integrator with variable limits 子系统对 *EFE* 与 *VFE* 之间的差值进行积分，以生成励磁机交流发电机输出电压 *VE*。*TE* 是此过程的时间常数。
- 非线性函数 *FEX* 对来自整流器调节的励磁机输出电压降进行建模。此函数取决于常数 *KC*，而 *KC* 本身是换相电抗的函数。
- 参数 *VEmin* 和 *VFEmax* 对旋转励磁机的下限和上限进行建模。

### Power Source

通过设置 **Power source selector SW1** 参数值，可以为受控整流器使用不同的电源表示。要从端子电压导出受控整流器的电源，请将 **Power source selector SW1** 参数设置为 `Position A: power source derived from terminal voltage`。要指定电源独立于端子电压，请将 **Power source selector SW1** 参数设置为 `Position B: power source independent from the terminal conditions`。
