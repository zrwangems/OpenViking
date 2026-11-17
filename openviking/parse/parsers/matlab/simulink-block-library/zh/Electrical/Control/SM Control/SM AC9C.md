---
type: simulink-block
title: 'SM AC9C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smac9c'
documentation_source_path: 'ref/smac9c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM AC9C

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
  group: 通用
- name: Initial terminal voltage, Vt0 (pu)
  summary: 初始机端电压 1（默认）| 实数标量
  group: 通用
- name: Initial terminal current, It0 (pu)
  summary: 初始机端电流 1（默认）| 实数标量
  group: 通用
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 -1（默认）| 0 | 正标量
  group: 通用
- name: Resistive component of load compensation, R_C (pu)
  summary: 补偿电阻 0（默认）| 正标量
  group: 预控制
- name: Reactance component of load compensation, X_C (pu)
  summary: 补偿电抗 0（默认）| 正标量
  group: 预控制
- name: Regulator input filter time constant, T_R (s)
  summary: 调节器时间常数 0.01（默认）| 正标量
  group: 预控制
- name: Voltage regulator proportional gain, K_PR (pu)
  summary: 电压调节器比例增益 10（默认）
  group: 控制
- name: Voltage regulator integral gain, K_IR (pu/s)
  summary: 电压调节器积分增益 10（默认）
  group: 控制
- name: Voltage regulator derivative gain, K_DR (pu.s)
  summary: 电压调节器微分增益 0（默认）
  group: 控制
- name: Lag time constant for derivative channel of PID controller, T_DR (s)
  summary: PID 微分通道滞后时间常数 0.01（默认）| 正标量
  group: 控制
- name: Maximum voltage regulator output, V_PIDmax (pu)
  summary: PID 调节器最大输出 1.6（默认）| 正标量
  group: 控制
- name: Minimum voltage regulator output, V_PIDmin (pu)
  summary: PID 调节器最小输出 0（默认）| 正标量
  group: 控制
- name: Field current regulator proportional gain, K_PA (pu)
  summary: 励磁电流调节器比例增益 4（默认）| 实数标量
  group: 控制
- name: Field current regulator integral gain, K_IA (pu/s)
  summary: 励磁电流调节器积分增益 0（默认）| 实数标量
  group: 控制
- name: Maximum current regulator output, V_Amax (pu)
  summary: 电流调节器最大输出 0.996（默认）| 实数标量
  group: 控制
- name: Minimum current regulator output, V_Amin (pu)
  summary: 电流调节器最小输出 -0.866（默认）| 实数标量
  group: 控制
- name: Controlled rectifier bridge equivalent gain, K_A (pu)
  summary: 整流桥增益 20（默认）| 正标量
  group: 控制
- name: Controlled rectifier bridge equivalent time constant, T_A (s)
  summary: 整流桥时间常数 0.0018（默认）| 正标量
  group: 控制
- name: Maximum rectifier bridge output, V_Rmax (pu)
  summary: 整流桥输出上限 19.92（默认）| 实数标量
  group: 控制
- name: Minimum rectifier bridge output, V_Rmin (pu)
  summary: 整流桥输出下限 -17.32（默认）| 实数标量
  group: 控制
- name: Exciter field current feedback gain, K_F (pu)
  summary: 励磁机励磁电流反馈增益 0.2（默认）| 实数标量
  group: 控制
- name: Field current feedback time constant, T_F (s)
  summary: 反馈时间常数 0.01（默认）| 正标量
  group: 控制
- name: Free wheel equivalent feedback gain, K_FW (pu)
  summary: 续流反馈增益 0（默认）| 实数标量
  group: 控制
- name: Maximum free wheel feedback, V_FWmax (pu)
  summary: 续流反馈上限 10（默认）| 实数标量
  group: 控制
- name: Minimum free wheel feedback, V_FWmin (pu)
  summary: 续流反馈下限 0（默认）| 实数标量
  group: 控制
- name: Power stage type selector, S_CT
  summary: 功率级类型选择选项 Thyristor bridge（默认）| Chopper converter
  group: 控制
- name: Voltage limit, V_lim1 (pu)
  summary: 第一自动电压调节器限值 0（默认）
  group: 控制
- name: Voltage limit, V_lim2 (pu)
  summary: 第二自动电压调节器限值 -0.1（默认）
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
  summary: 励磁机励磁增益 1（默认）| 正标量
  group: 励磁机
- name: Exciter field time constant, T_E (s)
  summary: 励磁机励磁时间常数 1（默认）| 正标量
  group: 励磁机
- name: Diode bridge loading factor proportional to commutating reactance, K_C (pu)
  summary: 二极管桥负载因子 0（默认）| 正标量
  group: 励磁机
- name: Demagnetizing factor, function of exciter alternator reactances, K_D (pu)
  summary: 去磁因子 1（默认）| 正标量
  group: 励磁机
- name: Exciter output voltage for saturation factor S_E(E_1), E_1 (pu)
  summary: 第一饱和输出电压 4.167（默认）| 正标量
  group: 励磁机
- name: Exciter saturation factor at exciter output voltage E_1, S_E(E_1) (1)
  summary: 第一饱和查找电压 0.001（默认）| 正标量
  group: 励磁机
- name: Exciter output voltage for saturation factor S_E(E_2), E_2 (pu)
  summary: 第二饱和输出电压 3.125（默认）| 正标量
  group: 励磁机
- name: Exciter saturation factor at exciter output voltage E_2, S_E(E_2) (1)
  summary: 第二饱和查找电压 0.01（默认）| 正标量
  group: 励磁机
- name: Exciter field current limit , V_FEmax (pu)
  summary: 励磁机上限 16（默认）| 实数标量
  group: 励磁机
- name: Minimum exciter output limit, V_Emin (pu)
  summary: 励磁机下限 0（默认）| 实数标量
  group: 励磁机
- name: Potential circuit gain coefficient, K_P (pu)
  summary: 电位电路增益系数 1（默认）| 实数标量
  group: 励磁机
- name: Potential circuit phase angle (degrees)
  summary: 电位电路相位角 0（默认）| 实数标量
  group: 励磁机
- name: Compound circuit (current) gain coefficient, K_I (pu)
  summary: 复合电路电流增益系数 0（默认）| 实数标量
  group: 励磁机
- name: Reactance associated with potential source, X_L (pu)
  summary: 与电位源相关的电抗 0（默认）| 实数标量
  group: 励磁机
- name: Rectifier loading factor proportional to commutating reactance, K_C1 (pu)
  summary: 与换相电抗成正比的整流器负载因子 0（默认）| 实数标量
  group: 励磁机
- name: Power source selector SW1
  summary: '电源选择器 Position A: power source derived from terminal voltage（默认）| Position B: power source independent of the
    terminal conditions'
  group: 励磁机
- name: Maximum available exciter field voltage, V_B1max (pu)
  summary: 最大可用励磁机励磁电压 100（默认）| 实数标量
  group: 励磁机
- name: Rectifier loading factor proportional to commutating reactance, K_C2 (pu)
  summary: 与换相电抗成正比的整流器负载因子 0（默认）| 实数标量
  group: 励磁机
- name: Compound circuit (current) gain coefficient, K_I2 (pu)
  summary: 复合电路电流增益系数 0（默认）| 实数标量
  group: 励磁机
- name: 最大可用励磁机磁场电压，V_B2max (pu)
  summary: 最大可用励磁机磁场电压 0（默认）| 实数标量
  group: 励磁机
```

### 通用

### **Initial field voltage, Efd0 (pu)** — 初始输出电压 `1`（默认）| 实数标量

施加到同步电机励磁绕组的初始标幺电压。

### **Initial terminal voltage, Vt0 (pu)** — 初始机端电压 `1`（默认）| 实数标量

施加到机端的初始标幺电压。

#### 依赖关系

要启用此参数，请在励磁机部分将 **Power source selector SW1** 设置为
`Position A: power source derived from terminal
voltage`。

### **Initial terminal current, It0 (pu)** — 初始机端电流 `1`（默认）| 实数标量

施加到机端的初始标幺电流。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。
有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请将此参数设置为 `-1`。
对于离散时间操作，请将此参数设置为正整数。对于连续时间操作，请将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

### 预控制

### **Resistive component of load compensation, R\_C (pu)** — 补偿电阻 `0`（默认）| 正标量

电流补偿系统中使用的电阻。将此参数和 **Reactance component of load compensation, X\_C
(pu)** 设置为 `0` 以禁用电流补偿。

### **Reactance component of load compensation, X\_C (pu)** — 补偿电抗 `0`（默认）| 正标量

电流补偿系统中使用的电抗。将此参数和 **Resistive component of load compensation, R\_C
(pu)** 设置为 `0` 以禁用电流补偿。

### **Regulator input filter time constant, T\_R (s)** — 调节器时间常数 `0.01`（默认）| 正标量

电压变送器滤波的等效时间常数。

### 控制

### **Voltage regulator proportional gain, K\_PR (pu)** — 电压调节器比例增益 `10`（默认）

电压调节器的标幺比例增益。

### **Voltage regulator integral gain, K\_IR (pu/s)** — 电压调节器积分增益 `10`（默认）

电压调节器的标幺积分增益。

### **Voltage regulator derivative gain, K\_DR (pu.s)** — 电压调节器微分增益 `0`（默认）

电压调节器的微分增益。

### **Lag time constant for derivative channel of PID controller, T\_DR (s)** — PID 微分通道滞后时间常数 `0.01`（默认）| 正标量

PID 控制器微分通道的等效滞后时间常数。

### **Maximum voltage regulator output, V\_PIDmax (pu)** — PID 调节器最大输出 `1.6`（默认）| 正标量

PID 调节器的最大允许标幺输出。

### **Minimum voltage regulator output, V\_PIDmin (pu)** — PID 调节器最小输出 `0`（默认）| 正标量

PID 调节器的最小允许标幺输出。

### **Field current regulator proportional gain, K\_PA (pu)** — 励磁电流调节器比例增益 `4`（默认）| 实数标量

励磁电流调节器的标幺比例增益。

### **Field current regulator integral gain, K\_IA (pu/s)** — 励磁电流调节器积分增益 `0`（默认）| 实数标量

励磁电流调节器的标幺积分增益。

### **Maximum current regulator output, V\_Amax (pu)** — 电流调节器最大输出 `0.996`（默认）| 实数标量

电流调节器的最大标幺输出。

### **Minimum current regulator output, V\_Amin (pu)** — 电流调节器最小输出 `-0.866`（默认）| 实数标量

电流调节器的最小标幺输出。

### **Controlled rectifier bridge equivalent gain, K\_A (pu)** — 整流桥增益 `20`（默认）| 正标量

可控整流桥的增益。

### **Controlled rectifier bridge equivalent time constant, T\_A (s)** — 整流桥时间常数 `0.0018`（默认）| 正标量

可控整流桥的时间常数。

### **Maximum rectifier bridge output, V\_Rmax (pu)** — 整流桥输出上限 `19.92`（默认）| 实数标量

整流桥的最大标幺输出。

### **Minimum rectifier bridge output, V\_Rmin (pu)** — 整流桥输出下限 `-17.32`（默认）| 实数标量

整流桥的最小标幺输出。

### **Exciter field current feedback gain, K\_F (pu)** — 励磁机励磁电流反馈增益 `0.2`（默认）| 实数标量

励磁机的标幺励磁电流反馈增益。

### **Field current feedback time constant, T\_F (s)** — 反馈时间常数 `0.01`（默认）| 正标量

用于励磁系统稳定的反馈时间常数。

### **Free wheel equivalent feedback gain, K\_FW (pu)** — 续流反馈增益 `0`（默认）| 实数标量

励磁机的标幺续流反馈增益。

### **Maximum free wheel feedback, V\_FWmax (pu)** — 续流反馈上限 `10`（默认）| 实数标量

最大标幺续流反馈。

### **Minimum free wheel feedback, V\_FWmin (pu)** — 续流反馈下限 `0`（默认）| 实数标量

最小标幺续流反馈。

### **Power stage type selector, S\_CT** — 功率级类型选择选项 `Thyristor bridge`（默认）| `Chopper converter`

选择功率级类型的选项。如果将 **Power stage type selector, S\_CT** 参数设置为
`Thyristor bridge`，则功率级表示晶闸管换流器。如果将 **Power stage
type selector, S\_CT** 参数设置为 `Chopper
converter`，则功率级表示斩波换流器。

### **Voltage limit, V\_lim1 (pu)** — 第一自动电压调节器限值 `0`（默认）

用于计算电压调节器指令信号的第一自动电压调节器限值。

### **Voltage limit, V\_lim2 (pu)** — 第二自动电压调节器限值 `-0.1`（默认）

用于计算电压调节器指令信号的第二自动电压调节器限值。

### **Alternate OEL input locations (V\_OEL)** — OEL 输入位置 `Unused`（默认）| `Summation point` | `Take-over`

过励限制器输入的位置，指定为以下选项之一：

- `Summation point` —
  **V\_OEL** 是 Summation
  Point Logic 子系统的输入。
- `Take-over` —
  **V\_OEL** 是 Take-over
  Logic 子系统的输入。

### **Alternate UEL input locations (V\_UEL)** — UEL 输入位置 `Unused`（默认）| `Summation point` | `Take-over`

欠励限制器输入的位置，指定为以下选项之一：

- `Summation point` —
  **V\_UEL** 是 Summation
  Point Logic 子系统的输入。
- `Take-over` —
  **V\_UEL** 是 Take-over
  Logic 子系统的输入。

### **Alternate SCL input locations (V\_SCL)** — SCL 输入位置 `Unused`（默认）| `Summation point` | `Take-over`

定子电流限制器输入的位置，指定为以下选项之一：

- `Summation point` — 使用
  **V\_SCLsum** 输入端口。
- `Take-over` — 使用
  **V\_SCLoel** 和
  **V\_SCLuel** 输入端口。

### 励磁机

### **Exciter field proportional constant, K\_E (pu)** — 励磁机励磁增益 `1`（默认）| 正标量

励磁机励磁的比例常数。

### **Exciter field time constant, T\_E (s)** — 励磁机励磁时间常数 `1`（默认）| 正标量

励磁机励磁的时间常数。

### **Diode bridge loading factor proportional to commutating reactance, K\_C (pu)** — 二极管桥负载因子 `0`（默认）| 正标量

二极管桥负载因子。此值与换相电抗成正比。

### **Demagnetizing factor, function of exciter alternator reactances, K\_D (pu)** — 去磁因子 `1`（默认）| 正标量

与励磁机交流发电机reactance相关的去磁因子。

### **Exciter output voltage for saturation factor S\_E(E\_1), E\_1 (pu)** — 第一饱和输出电压 `4.167`（默认）| 正标量

第一饱和因子的励磁机输出电压。

### **Exciter saturation factor at exciter output voltage E\_1, S\_E(E\_1) (1)** — 第一饱和查找电压 `0.001`（默认）| 正标量

第一励磁机的饱和因子。

### **Exciter output voltage for saturation factor S\_E(E\_2), E\_2 (pu)** — 第二饱和输出电压 `3.125`（默认）| 正标量

第二饱和因子的励磁机输出电压。

### **Exciter saturation factor at exciter output voltage E\_2, S\_E(E\_2) (1)** — 第二饱和查找电压 `0.01`（默认）| 正标量

第二励磁机的饱和因子。

### **Exciter field current limit , V\_FEmax (pu)** — 励磁机上限 `16`（默认）| 实数标量

最大标幺励磁电流限制参考值。

### **Minimum exciter output limit, V\_Emin (pu)** — 励磁机下限 `0`（默认）| 实数标量

最小标幺励磁机电压输出。

### **Potential circuit gain coefficient, K\_P (pu)** — 电位电路增益系数 `1`（默认）| 实数标量

标幺电位电路增益系数。

### **Potential circuit phase angle (degrees)** — 电位电路相位角 `0`（默认）| 实数标量

电位电路相位角，以度为单位。

#### 依赖关系

要启用此参数，请将 **Power source selector
SW1** 设置为 `Position A: power source derived
from terminal voltage`。

### **Compound circuit (current) gain coefficient, K\_I (pu)** — 复合电路电流增益系数 `0`（默认）| 实数标量

标幺复合电路电流增益系数。

#### 依赖关系

要启用此参数，请将 **Power source selector
SW1** 设置为 `Position A: power source derived
from terminal voltage`。

### **Reactance associated with potential source, X\_L (pu)** — 与电位源相关的电抗 `0`（默认）| 实数标量

与电位源相关的标幺电抗。

#### 依赖关系

要启用此参数，请将 **Power source selector
SW1** 设置为 `Position A: power source derived
from terminal voltage`。

### **Rectifier loading factor proportional to commutating reactance, K\_C1 (pu)** — 与换相电抗成正比的整流器负载因子 `0`（默认）| 实数标量

整流器的标幺负载因子。此值与换相电抗成正比。

### **Power source selector SW1** — 电源选择器 `Position A: power source derived from terminal voltage`（默认）| `Position B: power source independent of the terminal conditions`

电源选择器 SW1 的位置。

### **Maximum available exciter field voltage, V\_B1max (pu)** — 最大可用励磁机励磁电压 `100`（默认）| 实数标量

励磁机的最大可用标幺励磁电压。

### **Rectifier loading factor proportional to commutating reactance, K\_C2 (pu)** — 与换相电抗成正比的整流器负载因子 `0`（默认）| 实数标量

整流器的标幺负载因子。此值与换相电抗成正比，通过单独的串联二极管桥从发电机机端电流导出。

### **Compound circuit (current) gain coefficient, K\_I2 (pu)** — 复合电路电流增益系数 `0`（默认）| 实数标量

通过单独的串联二极管桥从发电机机端电流导出的标幺复合电路电流增益系数。将此参数设置为
`0` 以完全禁用单独的复合电源。

### **最大可用励磁机磁场电压，V\_B2max (pu)** — 最大可用励磁机磁场电压 `0`（默认）| 实数标量

励磁机的最大每单位可用磁场电压，通过单独的串联二极管桥从发电机
端子电流导出。
## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

离散时间或连续时间同步电机 AC9C 励磁系统，包括自动电压调节器和励磁机

SM AC9C 模块实现符合 Std IEEE 421.5-2016 [1] 的同步电机 AC9C 型励磁
系统模型。

使用此模块对作为发电机运行并使用交流旋转励磁机的同步电机的磁场电压
进行控制和调节建模。

通过使用 **采样时间（-1 表示继承）** 参数在模块的连续和离散实现之间
切换。要将积分器配置为连续时间，请将 **采样时间（-1 表示继承）** 参数设置为 `0`。要将积分器
配置为离散时间，请将 **采样时间（-1 表示继承）** 参数
设置为正标量。要从上游模块继承采样时间，请将
**采样时间（-1 表示继承）** 参数设置为
`-1`。

SM AC9C 模块包含五个主要组件：

- 电流补偿器组件根据端子电流修改测量的端子电压。
- 电压测量传感器组件使用低通滤波器模拟端子电压传感器的动态特性。
- 励磁控制元件组件将电压传感器输出与端子电压参考值进行比较，以产生电压误差值。
  该组件然后将此值通过电压调节器以产生励磁机磁场电压。
- 交流旋转励磁机组件模拟交流旋转励磁机，它产生施加到受控同步
  电机的磁场电压。该模块还将励磁机磁场电流
  (*VFE*) 反馈到
  励磁系统。
- 电源组件模拟受控整流器的电源对端子电压的依赖性。

此图显示了 AC9C 励磁系统模型的结构：

图中：

- *VT* 和
  *IT* 分别是同步电机的测量
  端子电压和电流。
- *VC1* 是电流补偿后的
  端子电压。
- *VC* 是滤波后的、
  电流补偿后的端子电压。
- *VREF* 是参考端子
  电压。
- *VS* 是电力系统
  稳定器电压。
- *SW1* 是为受控整流器指定的电源
  开关。
- *VB* 是励磁机磁场
  电压。
- *EFE* 和
  *VFE* 分别是励磁机磁场
  电压和电流。
- *EFD* 和
  *IFD* 分别是磁场电压
  和电流。

### 电流补偿器和电压测量传感器

该模块使用以下方程对电流补偿器建模：

VC1=VT+ITRC2+XC2,

其中：

- *RC* 是负载补偿
  电阻。
- *XC* 是负载补偿
  电抗。

该模块将电压测量传感器实现为具有时间常数
*TR* 的低通滤波器模块。有关精确的离散和连续
实现信息，请参阅低通滤波器模块的文档。

### 励磁控制元件

此图显示了励磁控制元件的结构：

图中：

- 求和点逻辑子系统为过励限制器 (OEL)、欠励限制器
  (UEL) 和定子电流限制器 (SCL) 建模求和点输入
  位置。有关将此模块与限制器一起使用的更多信息，请参阅
  磁场电流限制器。
- PID 子系统建模一个 PID 控制器，用作自动电压调节器的控制
  结构。该模块的最小和最大
  抗积分饱和限制分别为
  *VPIDmin* 和
  *VPIDmax*。
- 接管逻辑子系统为 OEL、UEL、SCL 和 PSS 电压建模接管点输入
  位置。有关将此模块与限制器一起使用的更多信息，请参阅
  磁场电流限制器。
- PI\_R 子系统建模一个 PI 控制器，用作
  磁场电流调节器的控制结构。该模块的最小和最大抗
  积分饱和限制分别为
  *VAmin* 和
  *VAmax*。
- 顶部低通滤波器模块建模受控整流桥的
  主要动态特性。
  *KA* 是受控
  整流桥等效增益，
  *TA* 是受控整流桥的主要时间
  常数。该模块的最小和最大
  抗积分饱和限制分别为
  *VRmin* 和
  *VRmax*。
- 底部低通滤波器模块建模用于励磁系统稳定化的
  速率反馈路径。
  *KF* 和
  *TF* 分别是该系统的时间常数和
  增益。有关离散和连续实现的信息，请参阅
  低通滤波器模块的文档。
- 功率状态逻辑子系统支持选择功率级类型，可以是晶闸管或斩波器换流器。如果将
  **功率级类型选择器，S\_CT** 参数设置为
  `Thyristor bridge`，它表示
  晶闸管换流器。如果将 **功率级类型选择器，
  S\_CT** 参数设置为 `Chopper
  converter`，它表示斩波器换流器。该
  子系统将电压调节器指令信号
  *VR* 与励磁机
  磁场电压 *VB* 相加。有关
  受控整流器电源的逻辑开关以及功率状态逻辑子系统的更多
  信息，请参阅电源和功率状态逻辑。
- **initialOffset** 常量模块确保
  仿真可以从稳态开始。SM AC9C 模块
  使用饱和和励磁机参数计算此值，
  包括初始磁场电压和励磁机磁场电流
  反馈增益。

### 磁场电流限制器

您可以使用不同类型的磁场电流限制器在不安全的运行条件下修改电压
调节器的输出：

- 使用过励限制器防止因过大的磁场电流需求导致磁场
  绕组过热。
- 使用欠励限制器在磁场励磁过低时提升励磁，过低
  存在失步风险。
- 使用定子电流限制器防止因过大电流导致定子
  绕组过热。

将任何这些限制器的输出连接到以下位置之一：

- 求和点 — 将限制器用作自动电压
  调节器 (AVR) 反馈回路的一部分。
- 接管点 — 覆盖 AVR 的常规行为。

如果在求和点使用定子电流限制器，
请使用输入 *VSCLsum*。如果在
接管点使用定子电流限制器，请使用过励输入
*VOELscl* 和欠励
输入 *VUELscl*。

### 交流旋转励磁机

此图显示了交流旋转励磁机的结构：

图中：

- 励磁机磁场电流
  *VFE* 是
  三个信号之和：

  - 非线性函数
    *Vx*
    建模励磁机输出电压的
    饱和。
  - 比例项
    *KE*
    建模励磁机
    输出电压与励磁机磁场
    电流之间的线性关系。
  - 该子系统使用反馈回路中的
    去磁常数
    *KD* 建模负载电流对励磁机输出
    电压的去磁效应。
- 可变限制积分器
  子系统对
  *EFE* 和
  *VFE* 之间的差值进行积分
  以生成励磁机交流发电机输出电压
  *VE*。
  *TE* 是
  此过程的时间常数。
- 非线性函数
  *FEX*
  建模整流器调节引起的励磁机输出电压降。此函数取决于
  常数
  *KC*，
  它本身是换相
  电抗的函数。
- 参数
  *VEmin*
  和
  *VFEmax*
  建模旋转
  励磁机的下限和上限。

### 电源和功率状态逻辑

您可以通过设置 **电源选择器 SW1** 参数值来使用受控整流器的不同电源表示。要从端子电压
导出受控整流器的电源，请将
**电源选择器 SW1** 参数设置为
`Position A: power source derived from terminal
voltage`。要指定电源独立于
端子电压，请将 **电源选择器 SW1** 参数
设置为 `Position B: power source independent from the terminal
conditions`。

功率状态逻辑子系统支持选择功率级类型，可以是
晶闸管或斩波器换流器。如果将 **功率级类型
选择器，S\_CT** 参数设置为 `Thyristor
bridge`，功率状态逻辑子系统表示晶闸管
换流器。如果将 **功率级类型选择器，S\_CT**
参数设置为 `Chopper converter`，功率状态逻辑
子系统表示斩波器换流器。电压调节器指令
信号 *VR* 的值取决于 **电压
限制，V\_lim1 (pu)** 和 **电压限制，V\_lim2
(pu)** 参数以及
*VCT*、
*VFW* 和
*VAVR* 信号，根据以下逻辑：

```
if S_CT ~= 0 % Thyristor bridge
	V_R = V_CT
else  	% Chopper converter
	if V_AVR > V_lim1
		V_R = C_T
	else
		if V_AVR > V_lim2
			V_R = 0
		else
			V_R = -V_FW
		end
	end
end
```
