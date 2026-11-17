---
type: simulink-block
title: 'SM AC11C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smac11c'
documentation_source_path: 'ref/smac11c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM AC11C

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
  summary: 端电压标量
  direction: input
  data_types: single | double
- name: I_T
  summary: 端电流标量
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

### **V\_T** — 端电压标量

端电压幅值，采用标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **I\_T** — 端电流标量

端电流幅值，采用标幺值表示，指定为标量。

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
- 要在 Take-over Logic 子系统使用来自过励限制器的输入，请将 **Alternate
  OEL input locations (V\_OEL)** 设置为
  `Take-over at voltage
  error`。
- 要在 Take-over Logic1 子系统使用来自过励限制器的输入，请将 **Alternate
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
- 要在 Take-over Logic 子系统使用来自欠励限制器的输入，请将 **Alternate
  UEL input locations (V\_UEL)** 设置为
  `Take-over at voltage
  error`。
- 要在 Take-over Logic1 子系统使用来自欠励限制器的输入，请将 **Alternate
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

### **V\_SCLoel** — 过励限制器接管定子电流限制标量

使用接管点时来自定子电流限制器的输入，用于防止励磁过励，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations
  (V\_SCL)** 设置为
  `Unused`。
- 要在 Take-over Logic 子系统使用来自定子电流限制器的输入，请将 **Alternate
  SCL input locations (V\_SCL)** 设置为
  `Take-over at voltage
  error`。
- 要在 Take-over Logic1 子系统使用来自定子电流限制器的输入，请将 **Alternate
  SCL input locations (V\_SCL)** 设置为
  `Take-over at voltage regulator
  output`。

**数据类型：** `single` | `double`

### **V\_SCLuel** — 欠励限制器接管定子电流限制标量

使用接管点时来自定子电流限制器的输入，用于防止励磁欠励，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **Alternate SCL input locations
  (V\_SCL)** 设置为
  `Unused`。
- 要在 Take-over Logic 子系统使用来自定子电流限制器的输入，请将 **Alternate
  SCL input locations (V\_SCL)** 设置为
  `Take-over at voltage
  error`。
- 要在 Take-over Logic1 子系统使用来自定子电流限制器的输入，请将 **Alternate
  SCL input locations (V\_SCL)** 设置为
  `Take-over at voltage regulator
  output`。

**数据类型：** `single` | `double`

### **Ifd\_pu** — 测量的励磁电流标量

同步电机的测量标幺励磁电流，指定为标量。

**数据类型：** `single` | `double`
### 输出

### **Efd\_pu** — 励磁电压标量

施加到同步电机励磁电路的标幺励磁电压，以标量形式返回。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Initial field voltage, Efd0 (pu)
  summary: 初始输出电压 1（默认）| 实数标量
  group: 常规
- name: Initial terminal voltage, Vt0 (pu)
  summary: 初始端电压 1（默认）| 实数标量
  group: 常规
- name: Initial terminal current, It0 (pu)
  summary: 初始端电流 1（默认）| 实数标量
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
- name: Voltage regulator proportional gain, K_PA (pu)
  summary: 电压调节器比例增益 30（默认）
  group: 控制
- name: Voltage regulator integral time constant, T_IA (s)
  summary: 电压调节器积分时间常数 2（默认）
  group: 控制
- name: UEL regulator proportional gain, K_PU (pu)
  summary: UEL 调节器比例增益 30（默认）
  group: 控制
- name: UEL regulator integral time constant, T_IU (s)
  summary: UEL 调节器积分时间常数 2（默认）
  group: 控制
- name: Voltage and UEL regulator derivative gain, K_B (pu)
  summary: 电压和 UEL 调节器微分增益 3（默认）
  group: 控制
- name: Time constant for derivative element, T_B (s)
  summary: 微分环节时间常数 0.4（默认）
  group: 控制
- name: OEL regulator proportional gain, K_PO (pu)
  summary: OEL 调节器比例增益 30（默认）
  group: 控制
- name: OEL regulator integral time constant, T_IO (s)
  summary: OEL 调节器积分时间常数 2（默认）
  group: 控制
- name: Maximum regulator output, V_Rmax (pu)
  summary: 最大调节器输出 20（默认）| 实数标量
  group: 控制
- name: Minimum regulator output, V_Rmin (pu)
  summary: 最小调节器输出 -20（默认）| 实数标量
  group: 控制
- name: Maximum PSS regulator output, V_RSmax (pu)
  summary: 最大 PSS 调节器输出 3（默认）| 实数标量
  group: 控制
- name: Minimum PSS regulator output, V_RSmin (pu)
  summary: 最小 PSS 调节器输出 -3（默认）| 实数标量
  group: 控制
- name: Maximum exciter output, V_Amax (pu)
  summary: 最大励磁机输出 20（默认）| 实数标量
  group: 控制
- name: Minimum exciter output, V_Amin (pu)
  summary: 最小励磁机输出 0（默认）| 实数标量
  group: 控制
- name: Alternate PSS input locations (V_S)
  summary: PSS 输入位置 Output of AVR (after take-over limits)（默认）| Voltage error calculation | Voltage error or after take-over
    limits
  group: 控制
- name: Alternate OEL input locations (V_OEL)
  summary: OEL 输入位置 Take-over at voltage error（默认）| Unused | Summation point at voltage error | Take-over at voltage regulator
    output
  group: 控制
- name: Alternate UEL input locations (V_UEL)
  summary: UEL 输入位置 Take-over at voltage error（默认）| Unused | Summation point at voltage error | Take-over at voltage regulator
    output
  group: 控制
- name: Alternate SCL input locations (V_SCL)
  summary: SCL 输入位置 Take-over at voltage error（默认）| Unused | Summation point at voltage error | Take-over at voltage regulator
    output
  group: 控制
- name: Exciter field proportional constant, K_E (pu)
  summary: 励磁机磁场增益 1（默认）| 正标量
  group: 励磁机
- name: Exciter field time constant, T_E (s)
  summary: 励磁机磁场时间常数 0.4（默认）| 正标量
  group: 励磁机
- name: Rectifier loading factor proportional to commutating reactance, K_C (pu)
  summary: 整流器负载因子 0.173（默认）| 正标量
  group: 励磁机
- name: Demagnetizing factor, function of exciter alternator reactances, K_D (pu)
  summary: 去磁因子 1（默认）| 正标量
  group: 励磁机
- name: Exciter output voltage for saturation factor S_E(E_1), E_1 (pu)
  summary: 第一饱和输出电压 7.4（默认）| 正标量
  group: 励磁机
- name: Exciter saturation factor at exciter output voltage E_1, S_E(E_1) (1)
  summary: 第一饱和查找电压 0.214（默认）| 正标量
  group: 励磁机
- name: Exciter output voltage for saturation factor S_E(E_2), E_2 (pu)
  summary: 第二饱和输出电压 5.55（默认）| 正标量
  group: 励磁机
- name: Exciter saturation factor at exciter output voltage E_2, S_E(E_2) (1)
  summary: 第二饱和查找电压 0.044（默认）| 正标量
  group: 励磁机
- name: Maximum exciter field current, V_FEmax (pu)
  summary: 励磁机上限 20（默认）| 实数标量
  group: 励磁机
- name: Minimum exciter output limit, V_Emin (pu)
  summary: 励磁机下限 0（默认）| 实数标量
  group: 励磁机
- name: Potential circuit (voltage) gain coefficient, K_P (pu)
  summary: 电位电路增益系数 1（默认）| 实数标量
  group: 励磁机
- name: Potential circuit phase angle (degrees)
  summary: 电位电路相位角 0（默认）| 实数标量
  group: 励磁机
- name: Potential circuit (current) gain coefficient, K_I (pu)
  summary: 电位电路电流增益系数 0（默认）| 实数标量
  group: 励磁机
- name: Reactance associated with potential source, X_L (pu)
  summary: 与电位源相关的电抗 0（默认）| 实数标量
  group: 励磁机
- name: Rectifier loading factor proportional to commutating reactance, K_C1 (pu)
  summary: 与换向电抗成正比的整流器负载因子 0（默认）| 实数标量
  group: 励磁机
- name: Power source selector SW1
  summary: '电源选择器 Position B: power source independent of the terminal conditions（默认）| Position A: power source derived from
    terminal voltage'
  group: 励磁机
- name: Maximum available exciter voltage, V_B1max (pu)
  summary: 最大可用励磁机磁场电压 1.5（默认）| 实数标量
  group: 励磁机
- name: Rectifier loading factor proportional to commutating reactance, K_C2 (pu)
  summary: 与换向电抗成正比的整流器负载因子 0（默认）| 实数标量
  group: 励磁机
- name: Additive potential circuit (current) gain coefficient, K_I2 (pu)
  summary: 附加电路电流增益系数 0（默认）| 实数标量
  group: 励磁机
- name: 最大可用励磁机电压，V_B2max (pu)
  summary: 最大可用励磁机电压 0（默认）| 实数标量
  group: 励磁机
- name: 附加独立源，K_BOOST (pu)
  summary: 附加独立源 0（默认）
  group: 励磁机
- name: 施加附加（升压）电路的参考值，V_BOOST (pu)
  summary: 施加升压电路的参考值 0（默认）
  group: 励磁机
```

### 常规

### **Initial field voltage, Efd0 (pu)** — 初始输出电压 `1`（默认）| 实数标量

施加到同步电机励磁电路的初始标幺电压。

### **Initial terminal voltage, Vt0 (pu)** — 初始端电压 `1`（默认）| 实数标量

施加到端口的初始标幺电压。

#### 依赖关系

要启用此参数，请在 Exciter 部分将
**Power source selector SW1** 设置为
`Position A: power source derived from terminal
voltage`。

### **Initial terminal current, It0 (pu)** — 初始端电流 `1`（默认）| 实数标量

施加到端口的初始标幺电流。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。
有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请将此参数设置为 `-1`。
对于离散时间操作，请将此参数设置为正整数。对于
连续时间操作，请将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保
模块的连续实现和离散实现之间正确切换。有关
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

### **Voltage regulator proportional gain, K\_PA (pu)** — 电压调节器比例增益 `30`（默认）

电压调节器的标幺比例增益。

### **Voltage regulator integral time constant, T\_IA (s)** — 电压调节器积分时间常数 `2`（默认）

电压调节器的积分时间常数，以秒为单位。

### **UEL regulator proportional gain, K\_PU (pu)** — UEL 调节器比例增益 `30`（默认）

UEL 调节器的标幺比例增益。

### **UEL regulator integral time constant, T\_IU (s)** — UEL 调节器积分时间常数 `2`（默认）

UEL 调节器的积分时间常数，以秒为单位。

### **Voltage and UEL regulator derivative gain, K\_B (pu)** — 电压和 UEL 调节器微分增益 `3`（默认）

电压调节器和 UEL 调节器的标幺微分增益。

### **Time constant for derivative element, T\_B (s)** — 微分环节时间常数 `0.4`（默认）

微分环节的时间常数，以秒为单位。

### **OEL regulator proportional gain, K\_PO (pu)** — OEL 调节器比例增益 `30`（默认）

OEL 调节器的标幺比例增益。

### **OEL regulator integral time constant, T\_IO (s)** — OEL 调节器积分时间常数 `2`（默认）

OEL 调节器的积分时间常数，以秒为单位。

### **Maximum regulator output, V\_Rmax (pu)** — 最大调节器输出 `20`（默认）| 实数标量

最大标幺调节器输出。

### **Minimum regulator output, V\_Rmin (pu)** — 最小调节器输出 `-20`（默认）| 实数标量

最小标幺调节器输出。

### **Maximum PSS regulator output, V\_RSmax (pu)** — 最大 PSS 调节器输出 `3`（默认）| 实数标量

电力系统稳定器调节器的最大标幺输出。

### **Minimum PSS regulator output, V\_RSmin (pu)** — 最小 PSS 调节器输出 `-3`（默认）| 实数标量

电力系统稳定器调节器的最小标幺输出。

### **Maximum exciter output, V\_Amax (pu)** — 最大励磁机输出 `20`（默认）| 实数标量

励磁系统的最大标幺输出。

### **Minimum exciter output, V\_Amin (pu)** — 最小励磁机输出 `0`（默认）| 实数标量

励磁系统的最小标幺输出。

### **Alternate PSS input locations (V\_S)** — PSS 输入位置 `Output of AVR (after take-over limits)`（默认）| `Voltage error calculation` | `Voltage error or after take-over limits`

电力系统稳定器输入的位置。

### **Alternate OEL input locations (V\_OEL)** — OEL 输入位置 `Take-over at voltage error`（默认）| `Unused` | `Summation point at voltage error` | `Take-over at voltage regulator output`

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

### **Alternate UEL input locations (V\_UEL)** — UEL 输入位置 `Take-over at voltage error`（默认）| `Unused` | `Summation point at voltage error` | `Take-over at voltage regulator output`

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

### **Alternate SCL input locations (V\_SCL)** — SCL 输入位置 `Take-over at voltage error`（默认）| `Unused` | `Summation point at voltage error` | `Take-over at voltage regulator output`

定子电流限制器输入的位置，指定为以下选项之一：

- `Summation point` — 使用
  **V\_SCLsum** 输入端口。
- 任意 `Take-over` 选项 —
  使用 **V\_OELscl** 和
  **V\_UELscl** 输入端口。

### 励磁机

### **Exciter field proportional constant, K\_E (pu)** — 励磁机磁场增益 `1`（默认）| 正标量

励磁机磁场的比例常数。

### **Exciter field time constant, T\_E (s)** — 励磁机磁场时间常数 `0.4`（默认）| 正标量

励磁机磁场的时间常数。

### **Rectifier loading factor proportional to commutating reactance, K\_C (pu)** — 整流器负载因子 `0.173`（默认）| 正标量

整流器负载因子。此值与换向电抗成正比。

### **Demagnetizing factor, function of exciter alternator reactances, K\_D (pu)** — 去磁因子 `1`（默认）| 正标量

与励磁机交流发电机reactance相关的去磁因子。

### **Exciter output voltage for saturation factor S\_E(E\_1), E\_1 (pu)** — 第一饱和输出电压 `7.4`（默认）| 正标量

第一饱和因子的励磁机输出电压。

### **Exciter saturation factor at exciter output voltage E\_1, S\_E(E\_1) (1)** — 第一饱和查找电压 `0.214`（默认）| 正标量

第一励磁机的饱和因子。

### **Exciter output voltage for saturation factor S\_E(E\_2), E\_2 (pu)** — 第二饱和输出电压 `5.55`（默认）| 正标量

第二饱和因子的励磁机输出电压。

### **Exciter saturation factor at exciter output voltage E\_2, S\_E(E\_2) (1)** — 第二饱和查找电压 `0.044`（默认）| 正标量

第二励磁机的饱和因子。

### **Maximum exciter field current, V\_FEmax (pu)** — 励磁机上限 `20`（默认）| 实数标量

最大标幺励磁电流限制参考值。

### **Minimum exciter output limit, V\_Emin (pu)** — 励磁机下限 `0`（默认）| 实数标量

最小标幺励磁机电压输出。

### **Potential circuit (voltage) gain coefficient, K\_P (pu)** — 电位电路增益系数 `1`（默认）| 实数标量

标幺电位电路增益系数。

#### 依赖关系

要启用此参数，请将 **Power source selector
SW1** 设置为 `Position A: power source derived
from terminal voltage`。

### **Potential circuit phase angle (degrees)** — 电位电路相位角 `0`（默认）| 实数标量

电位电路相位角，以度为单位。

#### 依赖关系

要启用此参数，请将 **Power source selector
SW1** 设置为 `Position A: power source derived
from terminal voltage`。

### **Potential circuit (current) gain coefficient, K\_I (pu)** — 电位电路电流增益系数 `0`（默认）| 实数标量

标幺电位电路电流增益系数。

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

### **Rectifier loading factor proportional to commutating reactance, K\_C1 (pu)** — 与换向电抗成正比的整流器负载因子 `0`（默认）| 实数标量

整流器的标幺负载因子。此值与换向
电抗成正比。

### **Power source selector SW1** — 电源选择器 `Position B: power source independent of the terminal conditions`（默认）| `Position A: power source derived from terminal voltage`

电源选择器 SW1 的位置。

### **Maximum available exciter voltage, V\_B1max (pu)** — 最大可用励磁机磁场电压 `1.5`（默认）| 实数标量

励磁机的最大标幺可用磁场电压。

### **Rectifier loading factor proportional to commutating reactance, K\_C2 (pu)** — 与换向电抗成正比的整流器负载因子 `0`（默认）| 实数标量

整流器的标幺负载因子。此值与换向
电抗成正比，通过单独的串联二极管桥从发电机端电流导出。

### **Additive potential circuit (current) gain coefficient, K\_I2 (pu)** — 附加电路电流增益系数 `0`（默认）| 实数标量

通过单独的串联二极管桥从发电机端电流导出的标幺附加电路电流增益
系数。将此参数设置为
`0` 以完全禁用单独的附加电源。

### **最大可用励磁机电压，V\_B2max (pu)** — 最大可用励磁机电压 `0`（默认）| 实数标量

励磁机的最大标幺可用磁场电压，通过单独的串联二极管桥从发电机端子电流导出。

### **附加独立源，K\_BOOST (pu)** — 附加独立源 `0`（默认）

升压电路的标幺附加独立源。

### **施加附加（升压）电路的参考值，V\_BOOST (pu)** — 施加升压电路的参考值 `0`（默认）

用于激活励磁系统中附加升压电路的标幺参考值。
## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

离散时间或连续时间同步电机 AC11C 励磁系统，包括自动电压调节器和励磁机

SM AC11C 模块实现符合 IEEE Std 421.5-2016 [1] 的同步电机 AC11C 型励磁系统模型。

使用此模块对作为发电机运行、使用交流旋转励磁机的同步电机的磁场电压进行控制和调节建模。

使用 **Sample time (-1 for inherited)** 参数在模块的连续和离散实现之间切换。要将积分器配置为连续时间，请将 **Sample time (-1 for inherited)** 参数设置为 `0`。要将积分器配置为离散时间，请将 **Sample time (-1 for inherited)** 参数设置为正标量。要从上游模块继承采样时间，请将 **Sample time (-1 for inherited)** 参数设置为 `-1`。

SM AC11C 模块包含五个主要组件：

- 电流补偿器组件根据端子电流修改测得的端子电压。
- 电压测量传感器组件使用低通滤波器模拟端子电压传感器的动态特性。
- 励磁控制元件组件将电压传感器输出与端子电压参考值进行比较，以产生电压误差值。该组件随后将此值通过电压调节器传递，以产生励磁机磁场电压。
- 交流旋转励磁机组件对交流旋转励磁机建模，该励磁机产生施加到受控同步电机的磁场电压。该模块还将励磁机磁场电流（*VFE*）反馈到励磁系统。
- 电源组件对受控整流器电源与端子电压的依赖性进行建模。电源包含多个复合电路。您可以将此附加电路选择为升压电路，当系统中的故障条件导致发电机端子电压下降时施加该电路。SM AC11C 模块随后在发电机电压恢复时释放该电路。

此图显示了 AC11C 励磁系统模型的结构：

图中：

- *VT* 和 *IT* 分别是同步电机的测量端子电压和电流。
- *VC1* 是电流补偿后的端子电压。
- *VC* 是滤波后的电流补偿端子电压。
- *VREF* 是参考端子电压。
- *VS* 是电力系统稳定器电压。
- *SW1* 是您为受控整流器指定的电源开关。
- *VB* 是励磁机磁场电压。
- *EFE* 和 *VFE* 分别是励磁机磁场电压和电流。
- *EFD* 和 *IFD* 分别是磁场电压和电流。

### 电流补偿器和电压测量传感器

该模块使用以下方程对电流补偿器建模：

VC1=VT+ITRC2+XC2，

其中：

- *RC* 是负载补偿电阻。
- *XC* 是负载补偿电抗。

该模块将电压测量传感器实现为具有时间常数 *TR* 的低通滤波器模块。有关精确的离散和连续实现信息，请参阅低通滤波器模块的文档。

### 励磁控制元件

此图显示了励磁控制元件的结构：

图中：

- 求和点逻辑子系统对过励限制器（OEL）、欠励限制器（UEL）和定子电流限制器（SCL）的求和点输入位置进行建模。有关将此模块与限制器一起使用的更多信息，请参阅磁场电流限制器。
- 有两个接管逻辑子系统。它们对 OEL、UEL 和 SCL 电压的接管点输入位置进行建模。有关将此模块与限制器一起使用的更多信息，请参阅磁场电流限制器。
- SM AC11C 模块使用三种不同的 PID 控制对自动电压调节器的控制器进行建模。特定限制器（UEL 或 OEL）的激活会立即将自动电压调节器的传递函数更改为与激活的限制器相对应的控制器路径。当 *VUEL* 和/或 *VOEL* 信号连接到各自的备用位置时，SW\_UEL 和 SW\_OEL Switch 模块激活相应的控制路径。当您将 **Alternate UEL input locations (V\_UEL)** 和 **Alternate OEL input locations (V\_OEL)** 参数设置为 `Take-over at voltage error` 时，SW\_UEL 和 SW\_OEL Switch 模块处于位置 B。
- **Power source selector SW1** 参数控制受控整流器电源的来源。电源包含一个升压电路，当系统中的故障条件导致发电机端子电压下降时，您可以施加该电路。电压调节器指令信号 *VR* 随后与励磁机磁场电压 *VB1* 和 *VB2* 相加和/或相乘。有关受控整流器电源逻辑开关的更多信息，请参阅电源和升压电路。

### 磁场电流限制器

您可以使用不同类型的磁场电流限制器在不安全运行条件下修改电压调节器的输出：

- 使用过励限制器防止因过大的磁场电流需求导致磁场绕组过热。
- 使用欠励限制器在励磁过低时提升励磁，因为励磁过低存在失步风险。
- 使用定子电流限制器防止因过大电流导致定子绕组过热。

将任何这些限制器的输出连接到以下位置之一：

- 求和点 — 将限制器用作自动电压调节器（AVR）反馈回路的一部分。
- 接管点 — 覆盖 AVR 的常规行为。

如果您在求和点使用定子电流限制器，请使用输入 *VSCLsum*。如果您在接管点使用定子电流限制器，请使用过励输入 *VOELscl* 和欠励输入 *VUELscl*。

### 交流旋转励磁机

此图显示了交流旋转励磁机的结构：

图中：

- 励磁机磁场电流 *VFE* 是三个信号之和：

  - 非线性函数 *Vx* 对励磁机输出电压的饱和进行建模。
  - 比例项 *KE* 对励磁机输出电压与励磁机磁场电流之间的线性关系进行建模。
  - 该子系统使用反馈回路中的去磁常数 *KD* 对负载电流对励磁机输出电压的去磁效应进行建模。
- 可变限幅积分器子系统对 *EFE* 和 *VFE* 之间的差值进行积分，以生成励磁机交流发电机输出电压 *VE*。*TE* 是此过程的时间常数。
- 非线性函数 *FEX* 对整流器调节引起的励磁机输出电压降进行建模。此函数取决于常数 *KC*，而 *KC* 本身是换相电抗的函数。
- 参数 *VEmin* 和 *VFEmax* 对旋转励磁机的下限和上限进行建模。

### 电源和升压电路

您可以通过设置 **Power source selector SW1** 参数值来使用受控整流器的不同电源表示。要从端子电压导出受控整流器的电源，请将 **Power source selector SW1** 参数设置为 `Position A: power source derived from terminal voltage`。要指定电源独立于端子电压，请将 **Power source selector SW1** 参数设置为 `Position B: power source independent from the terminal conditions`。

电源部分还包含一个附加电路，您可以将其用作升压电路。当系统中的故障条件导致发电机端子电压下降时，施加此附加电路。SW\_Boost Switch 模块控制与升压电路相关的逻辑。如果端子电压 *VT* 大于 **Reference value for applying additive (boost) circuit, V\_BOOST (pu)** 参数的值，则开关处于位置“A”，否则开关处于位置“B”。

如果您将 **Reference value for applying additive (boost) circuit, V\_BOOST (pu)** 参数设置为高值，则附加组件始终处于激活状态。
