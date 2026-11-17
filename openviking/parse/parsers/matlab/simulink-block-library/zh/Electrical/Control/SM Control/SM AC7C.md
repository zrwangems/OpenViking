---
type: simulink-block
title: 'SM AC7C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smac7c'
documentation_source_path: 'ref/smac7c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM AC7C

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
- name: V_OELscl
  summary: 过励限制器接管定子电流限制标量
  direction: input
  data_types: single | double
- name: V_UELscl
  summary: 欠励限制器接管定子电流限制标量
  direction: input
  data_types: single | double
- name: Ifd_pu
  summary: 测量的励磁电流标量
  direction: input
  data_types: single | double
- name: Efd_pu
  summary: 磁场电压标量
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

- 要忽略来自过励限制器的输入，请将
  **备用 OEL 输入位置
  (V\_OEL)** 设置为
  `Unused`。
- 要在求和点使用来自过励限制器的输入，请将 **备用 OEL 输入位置
  (V\_OEL)** 设置为 `Summation
  point`。
- 要在接管点使用来自过励限制器的输入，请将 **备用 OEL 输入位置
  (V\_OEL)** 设置为
  `Take-over`。

**数据类型：** `single` | `double`

### **V\_UEL** — 欠励限制信号标量

来自欠励限制器的输入，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自欠励限制器的输入，请将
  **备用 UEL 输入位置
  (V\_UEL)** 设置为
  `Unused`。
- 要在求和点使用来自欠励限制器的输入，请将 **备用 UEL 输入位置
  (V\_UEL)** 设置为 `Summation
  point`。
- 要在接管点使用来自欠励限制器的输入，请将 **备用 UEL 输入位置
  (V\_UEL)** 设置为
  `Take-over`。

**数据类型：** `single` | `double`

### **V\_SCLsum** — 求和点定子电流限制信号标量

使用求和点时来自定子电流限制器的输入，采用标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将
  **备用 SCL 输入位置
  (V\_SCL)** 设置为
  `Unused`。
- 要在求和点使用来自定子电流限制器的输入，请将 **备用 SCL 输入位置
  (V\_SCL)** 设置为 `Summation
  point`。

**数据类型：** `single` | `double`

### **V\_OELscl** — 过励限制器接管定子电流限制标量

使用接管点时来自定子电流限制器的输入，用于防止磁场过励，采用标幺值表示，指定为
标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将
  **备用 SCL 输入位置
  (V\_SCL)** 设置为
  `Unused`。
- 要在接管点使用来自定子电流限制器的输入，请将 **备用 SCL 输入位置
  (V\_SCL)** 设置为
  `Take-over`。

**数据类型：** `single` | `double`

### **V\_UELscl** — 欠励限制器接管定子电流限制标量

使用接管点时来自定子电流限制器的输入，用于防止磁场欠励，采用标幺值表示，指定为
标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将
  **备用 SCL 输入位置
  (V\_SCL)** 设置为
  `Unused`。
- 要在接管点使用来自定子电流限制器的输入，请将 **备用 SCL 输入位置
  (V\_SCL)** 设置为
  `Take-over`。

**数据类型：** `single` | `double`

### **Ifd\_pu** — 测量的励磁电流标量

同步电机的测量标幺励磁电流，指定为标量。

**数据类型：** `single` | `double`
### 输出

### **Efd\_pu** — 磁场电压标量

施加到同步电机磁场电路的标幺磁场电压，以标量形式返回。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: 初始磁场电压，Efd0 (pu)
  summary: 初始输出电压 1（默认）| 实数
  group: 常规
- name: 采样时间（-1 表示继承）
  summary: 模块采样时间 -1（默认）| 0 | 正标量
  group: 常规
- name: 负载补偿电阻分量，R_C (pu)
  summary: 补偿电阻 0（默认）| 正数
  group: 预控制
- name: 负载补偿电抗分量，X_C (pu)
  summary: 补偿电抗 0（默认）| 正数
  group: 预控制
- name: 调节器输入滤波器时间常数，T_R (s)
  summary: 调节器时间常数 0（默认）| 正数
  group: 预控制
- name: 电压调节器比例增益，K_PR (pu)
  summary: 电压调节器的比例增益 40（默认）
  group: 控制
- name: 电压调节器积分增益，K_IR (pu/s)
  summary: 电压调节器的积分增益 5.6（默认）
  group: 控制
- name: 电压调节器微分增益，K_DR (pu.s)
  summary: 电压调节器的微分增益 0（默认）
  group: 控制
- name: PID 控制器微分通道的滞后时间常数，T_DR (s)
  summary: PID 微分通道的滞后时间常数 1（默认）| 正数
  group: 控制
- name: 调节器最大输出，V_Rmax (pu)
  summary: 调节器输出上限 3.2（默认）| 实数
  group: 控制
- name: 调节器最小输出，V_Rmin (pu)
  summary: 调节器输出下限 -3.2（默认）| 实数
  group: 控制
- name: 励磁电流调节器比例增益，K_PA (pu)
  summary: 励磁电流调节器的比例增益 112（默认）| 实数
  group: 控制
- name: 励磁电流调节器积分增益，K_IA (pu/s)
  summary: 励磁电流调节器的积分增益 0（默认）| 实数
  group: 控制
- name: 励磁电流调节器最大输出，V_Amax (pu)
  summary: 励磁电流调节器最大输出 65.2（默认）| 实数
  group: 控制
- name: 励磁电流调节器最小输出，V_Amin (pu)
  summary: 励磁电流调节器最小输出 -54（默认）| 实数
  group: 控制
- name: 发电机磁场电压反馈增益，K_F1 (pu)
  summary: 发电机磁场电压反馈增益 0（默认）| 实数
  group: 控制
- name: 励磁机磁场电流反馈增益，K_F2 (pu)
  summary: 励磁机磁场电流反馈增益 0.08（默认）| 实数
  group: 控制
- name: 速率反馈增益，K_F3 (pu)
  summary: 速率反馈增益 0.01（默认）| 实数
  group: 控制
- name: 速率反馈时间常数，T_F (s)
  summary: 速率反馈时间常数 1（默认）| 正数
  group: 控制
- name: 备用 PSS 输入位置 (V_S)
  summary: PSS 输入位置 Voltage error calculation（默认）| After take-over UEL
  group: 控制
- name: 备用 OEL 输入位置 (V_OEL)
  summary: OEL 输入位置 Unused（默认）| Summation point at voltage error | Take-over at voltage error | Take-over at voltage regulator
    output | Take-over at output of inner loop regulator
  group: 控制
- name: 备用 UEL 输入位置 (V_UEL)
  summary: UEL 输入位置 Unused（默认）| Summation point at voltage error | Take-over at voltage error | Take-over at voltage regulator
    output
  group: 控制
- name: 备用 SCL 输入位置 (V_SCL)
  summary: SCL 输入位置 Unused（默认）| Summation point at voltage error | Take-over at voltage error | Take-over at voltage regulator
    output
  group: 控制
- name: 励磁机磁场比例常数，K_E (pu)
  summary: 励磁机磁场增益 1（默认）| 正数
  group: 励磁机
- name: 励磁机磁场时间常数，T_E (s)
  summary: 励磁机磁场时间常数 1.2（默认）| 正数
  group: 励磁机
- name: 与换相电抗成比例的整流器负载因子，K_C (pu)
  summary: 整流器负载因子 0.12（默认）| 正数
  group: 励磁机
- name: 去磁因子，励磁机交流电机电抗的函数，K_D (pu)
  summary: 去磁因子 3.3（默认）| 正数
  group: 励磁机
- name: 饱和因子 S_E(E_1) 对应的励磁机输出电压，E_1 (pu)
  summary: 第一饱和输出电压 13.6（默认）| 正数
  group: 励磁机
- name: 励磁机输出电压 E_1 处的励磁机饱和因子，S_E(E_1) (1)
  summary: 第一饱和查找电压 3.74（默认）| 正数
  group: 励磁机
- name: 饱和因子 S_E(E_2) 对应的励磁机输出电压，E_2 (pu)
  summary: 第二饱和输出电压 10.2（默认）| 正数
  group: 励磁机
- name: 励磁机输出电压 E_2 处的励磁机饱和因子，S_E(E_2) (1)
  summary: 第二饱和查找电压 0.32（默认）| 正数
  group: 励磁机
- name: 最大励磁机磁场电流限制参考值，V_FEmax (pu)
  summary: 励磁机上限 23.2（默认）| 实数
  group: 励磁机
- name: 最小励磁机电压输出，V_Emin (pu)
  summary: 励磁机下限 0（默认）| 实数
  group: 励磁机
- name: 电势电路增益系数，K_P (pu)
  summary: 电势电路增益系数 1（默认）| 实数
  group: 励磁机
- name: 电势电路相位角（度）
  summary: 电势电路相位角 0（默认）| 实数
  group: 励磁机
- name: 电势电路（电流）增益系数，K_I (pu)
  summary: 电势电路电流增益系数 0（默认）| 实数
  group: 励磁机
- name: 与电势源相关的电抗，X_L (pu)
  summary: 与电势源相关的电抗 0（默认）| 实数
  group: 励磁机
- name: 与调节器和交流电机磁场电源相关的增益，K_R (pu)
  summary: 与调节器和交流电机磁场电源相关的增益 0（默认）| 实数
  group: 励磁机
- name: 与负励磁机磁场电流能力相关的增益，K_L (pu)
  summary: 与负励磁机磁场电流能力相关的增益 0（默认）| 实数
  group: 励磁机
- name: 与换相电抗成比例的整流器负载因子，K_C1 (pu)
  summary: 与换相电抗成比例的整流器负载因子 0（默认）| 实数
  group: 励磁机
- name: 最大可用励磁机磁场电压，V_Bmax (pu)
  summary: 励磁机最大可用磁场电压 999（默认）| 实数
  group: 励磁机
- name: 电源选择器 SW1
  summary: '电源选择器 Position A: power source derived from terminal voltage（默认）| Position B: power source independent of terminal
    conditions'
  group: 励磁机
- name: 电源选择器 SW2
  summary: '电源选择器 Position A: use variable V_B（默认）| 位置 B：不使用变量 V_B'
  group: 励磁机
```

### 常规

### **初始磁场电压，Efd0 (pu)** — 初始输出电压 `1`（默认）| 实数

施加到同步电机磁场电路的初始标幺电压。

### **采样时间（-1 表示继承）** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在
执行期间，模块产生输出，并在适当时更新其内部状态。
有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请将此参数设置为 `-1`。
对于离散时间操作，请将此参数设置为正整数。对于
连续时间操作，请将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保
模块的连续实现和离散实现之间正确切换。有关
详细信息，请参阅 Promote Block Parameters on a Mask。

### 预控制

### **负载补偿电阻分量，R\_C (pu)** — 补偿电阻 `0`（默认）| 正数

电流补偿系统中使用的电阻。将此参数
和 **负载补偿电抗分量，X\_C
(pu)** 设置为 `0` 以禁用电流
补偿。

### **负载补偿电抗分量，X\_C (pu)** — 补偿电抗 `0`（默认）| 正数

电流补偿系统中使用的电抗。将此参数
和 **负载补偿电阻分量，R\_C
(pu)** 设置为 `0` 以禁用电流
补偿。

### **调节器输入滤波器时间常数，T\_R (s)** — 调节器时间常数 `0`（默认）| 正数

电压传感器滤波的等效时间常数。

### 控制

### **电压调节器比例增益，K\_PR (pu)** — 电压调节器的比例增益 `40`（默认）

电压调节器的标幺比例增益。

### **电压调节器积分增益，K\_IR (pu/s)** — 电压调节器的积分增益 `5.6`（默认）

电压调节器的标幺积分增益。

### **电压调节器微分增益，K\_DR (pu.s)** — 电压调节器的微分增益 `0`（默认）

电压调节器的微分增益。

### **PID 控制器微分通道的滞后时间常数，T\_DR (s)** — PID 微分通道的滞后时间常数 `1`（默认）| 正数

PID 控制器微分通道的等效滞后时间常数。

### **调节器最大输出，V\_Rmax (pu)** — 调节器输出上限 `3.2`（默认）| 实数

调节器的最大标幺输出电压。

### **调节器最小输出，V\_Rmin (pu)** — 调节器输出下限 `-3.2`（默认）| 实数

调节器的最小标幺输出电压。

### **励磁电流调节器比例增益，K\_PA (pu)** — 励磁电流调节器的比例增益 `112`（默认）| 实数

与励磁电流调节器相关的标幺比例增益。

### **励磁电流调节器积分增益，K\_IA (pu/s)** — 励磁电流调节器的积分增益 `0`（默认）| 实数

与励磁电流调节器相关的标幺积分增益。

### **励磁电流调节器最大输出，V\_Amax (pu)** — 励磁电流调节器最大输出 `65.2`（默认）| 实数

最大标幺励磁电流调节器输出。

### **励磁电流调节器最小输出，V\_Amin (pu)** — 励磁电流调节器最小输出 `-54`（默认）| 实数

最小标幺励磁电流调节器输出。

### **发电机磁场电压反馈增益，K\_F1 (pu)** — 发电机磁场电压反馈增益 `0`（默认）| 实数

与发电机相关的标幺磁场电压反馈增益。

### **励磁机磁场电流反馈增益，K\_F2 (pu)** — 励磁机磁场电流反馈增益 `0.08`（默认）| 实数

与励磁机相关的标幺磁场电流反馈增益。

### **速率反馈增益，K\_F3 (pu)** — 速率反馈增益 `0.01`（默认）| 实数

标幺速率反馈模块增益。

### **速率反馈时间常数，T\_F (s)** — 速率反馈时间常数 `1`（默认）| 正数

用于励磁系统稳定的速率反馈模块时间常数。

### **备用 PSS 输入位置 (V\_S)** — PSS 输入位置 `Voltage error calculation`（默认）| `After take-over UEL`

电力系统稳定器输入的位置。

### **备用 OEL 输入位置 (V\_OEL)** — OEL 输入位置 `Unused`（默认）| `Summation point at voltage error` | `Take-over at voltage error` | `Take-over at voltage regulator output` | `Take-over at output of inner loop regulator`

过励限制器输入的位置：

- 如果选择 `Summation point at voltage
  error`，则 **V\_OEL** 是
  **Summation Point Logic**
  子系统的输入。
- 如果选择 `Take-over at voltage
  error`，则 **V\_OEL** 是
  **Take-over Logic**
  子系统的输入。
- 如果选择 `Take-over at voltage regulator
  output`，则 **V\_OEL** 是
  **Take-over Logic 1**
  子系统的输入。
- 如果选择 `Take-over at output of inner
  loop regulator`，则 **V\_OEL**
  是 **Take-over Logic 2**
  子系统的输入。

### **备用 UEL 输入位置 (V\_UEL)** — UEL 输入位置 `Unused`（默认）| `Summation point at voltage error` | `Take-over at voltage error` | `Take-over at voltage regulator output`

欠励限制器输入的位置：

- 如果选择 `Summation point at voltage
  error`，则 **V\_UEL** 是
  **Summation Point Logic**
  子系统的输入。
- 如果选择 `Take-over at voltage
  error`，则 **V\_UEL** 是
  **Take-over Logic**
  子系统的输入。
- 如果选择 `Take-over at voltage regulator
  output`，则 **V\_UEL** 是
  **Take-over Logic 1**
  子系统的输入。

### **备用 SCL 输入位置 (V\_SCL)** — SCL 输入位置 `Unused`（默认）| `Summation point at voltage error` | `Take-over at voltage error` | `Take-over at voltage regulator output`

定子电流限制器输入的位置：

- 如果选择 `Summation point`，
  请使用 **V\_SCLsum** 输入端口。
- 如果选择任何
  `Take-over` 选项，请使用
  **V\_OELscl** 和
  **V\_UELscl** 输入端口。

### 励磁机

### **励磁机磁场比例常数，K\_E (pu)** — 励磁机磁场增益 `1`（默认）| 正数

励磁机磁场的比例常数。

### **励磁机磁场时间常数，T\_E (s)** — 励磁机磁场时间常数 `1.2`（默认）| 正数

励磁机磁场的时间常数。

### **与换相电抗成比例的整流器负载因子，K\_C (pu)** — 整流器负载因子 `0.12`（默认）| 正数

与换相电抗成比例的整流器负载因子。

### **去磁因子，励磁机交流电机电抗的函数，K\_D (pu)** — 去磁因子 `3.3`（默认）| 正数

与励磁机交流电机电抗相关的去磁因子。

### **饱和因子 S\_E(E\_1) 对应的励磁机输出电压，E\_1 (pu)** — 第一饱和输出电压 `13.6`（默认）| 正数

第一饱和因子对应的励磁机输出电压。

### **励磁机输出电压 E\_1 处的励磁机饱和因子，S\_E(E\_1) (1)** — 第一饱和查找电压 `3.74`（默认）| 正数

第一励磁机的饱和因子。

### **饱和因子 S\_E(E\_2) 对应的励磁机输出电压，E\_2 (pu)** — 第二饱和输出电压 `10.2`（默认）| 正数

第二饱和因子对应的励磁机输出电压。

### **励磁机输出电压 E\_2 处的励磁机饱和因子，S\_E(E\_2) (1)** — 第二饱和查找电压 `0.32`（默认）| 正数

第二励磁机的饱和因子。

### **最大励磁机磁场电流限制参考值，V\_FEmax (pu)** — 励磁机上限 `23.2`（默认）| 实数

最大标幺磁场电流限制参考值。

### **最小励磁机电压输出，V\_Emin (pu)** — 励磁机下限 `0`（默认）| 实数

最小标幺励磁机电压输出。

### **电势电路增益系数，K\_P (pu)** — 电势电路增益系数 `1`（默认）| 实数

标幺电势电路增益系数。

#### 依赖关系

仅当将 **电源选择器 SW1** 参数设置为
`Position A: power source derived from terminal
voltage` 且将 **电源选择器
SW2** 参数设置为 `Position A: use
variable V_B` 时，此参数才可见。

### **电势电路相位角（度）** — 电势电路相位角 `0`（默认）| 实数

电势电路相位角，以度为单位。

#### 依赖关系

要启用此参数，请将 **电源选择器 SW1** 设置为
`Position A: power source derived from terminal
voltage`，并将 **电源选择器
SW2** 设置为 `Position A: use variable
V_B`。

### **电势电路（电流）增益系数，K\_I (pu)** — 电势电路电流增益系数 `0`（默认）| 实数

标幺电势电路电流增益系数。

#### 依赖关系

要启用此参数，请将 **电源选择器
SW1** 设置为 `Position A: power source derived
from terminal voltage`，并将 **电源
选择器 SW2** 设置为 `Position A: use variable
V_B`。

### **与电势源相关的电抗，X\_L (pu)** — 与电势源相关的电抗 `0`（默认）| 实数

与电势源相关的标幺电抗。

#### 依赖关系

要启用此参数，请将 **电源选择器
SW1** 设置为 `Position A: power source derived
from terminal voltage`，并将 **电源
选择器 SW2** 设置为 `Position A: use variable
V_B`。

### **与调节器和交流电机磁场电源相关的增益，K\_R (pu)** — 与调节器和交流电机磁场电源相关的增益 `0`（默认）| 实数

与调节器和交流电机磁场电源相关的标幺增益。

#### 依赖关系

要启用此参数，请将 **电源选择器 SW2** 设置为
`位置 B：不使用变量
V_B`。

### **与负励磁机磁场电流能力相关的增益，K\_L (pu)** — 与负励磁机磁场电流能力相关的增益 `0`（默认）| 实数

与负励磁机磁场电流能力相关的标幺增益。

### **与换相电抗成比例的整流器负载因子，K\_C1 (pu)** — 与换相电抗成比例的整流器负载因子 `0`（默认）| 实数

*自 R2024b 起*

整流器的标幺负载因子，与
换相电抗成比例。

#### 依赖关系

要启用此参数，请将 **电源选择器
SW2** 设置为 `Position A: use variable
V_B`。

### **最大可用励磁机磁场电压，V\_Bmax (pu)** — 励磁机最大可用磁场电压 `999`（默认）| 实数

*自 R2024b 起*

励磁机的最大标幺可用磁场电压。

#### 依赖关系

要启用此参数，请将 **电源选择器
SW2** 设置为 `Position A: use variable
V_B`。

### **电源选择器 SW1** — 电源选择器 `Position A: power source derived from terminal voltage`（默认）| `Position B: power source independent of terminal conditions`

电源选择器 SW1 的位置。

#### 依赖关系

要启用此参数，请将 **电源选择器 SW2** 设置为
`Position A: use variable V_B`。

### **电源选择器 SW2** — 电源选择器 `Position A: use variable V_B`（默认）| `位置 B：不使用变量 V_B`

电源选择器 SW2 的位置。
## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

离散时间或连续时间同步电机 AC7C 励磁系统，包括自动电压调节器和励磁机

SM AC7C 模块按照 IEEE 421.5-2016[1] 实现同步电机 AC7C 型励磁系统模型。

使用此模块可对作为发电机运行、使用交流旋转励磁机的同步电机的励磁电压进行建模和控制调节。

您可以通过使用 **Sample time (-1 for inherited)** 参数在模块的连续和离散实现之间切换。要将积分器配置为连续时间，请将 **Sample time (-1 for inherited)** 属性设置为 `0`。要将积分器配置为离散时间，请将 **Sample time (-1 for inherited)** 属性设置为正的非零值，或设置为 `-1` 以从上流模块继承采样时间。

SM AC7C 模块由五个主要组件组成：

- 电流补偿器根据终端电流修改测量的终端电压。
- 电压测量传感器使用低通滤波器模拟终端电压传感器的动态特性。
- 励磁控制元件组件将电压传感器输出与终端电压参考值进行比较，以产生电压误差。然后，该电压误差通过电压调节器产生励磁机励磁电压。
- 交流旋转励磁机模拟交流旋转励磁机，其产生施加到受控同步电机的励磁电压。该模块还将励磁机励磁电流（标准符号为 *VFE*）反馈到励磁系统。
- 电源和自励磁模拟受控整流器的电源，当该电源独立于终端电压时。它还允许表示励磁机的自励磁。

此图显示了 AC7C 励磁系统模型的整体结构：

图中：

- *VT* 和 *IT* 分别是同步电机的测量终端电压和电流。
- *VC1* 是电流补偿后的终端电压。
- *VC* 是滤波后的电流补偿终端电压。
- *VREF* 是参考终端电压。
- *VS* 是电力系统稳定器电压。
- *SW1* 和 *SW2* 是用户选择的受控整流器电源开关。
- *VB* 是励磁机励磁电压。
- *EFE* 和 *VFE* 分别是励磁机励磁电压和电流。
- *EFD* 和 *IFD* 分别是励磁电压和电流。

以下各节详细描述了模块的每个主要部分。

### 电流补偿器和电压测量传感器

电流补偿器建模为：

VC1=VT+ITRC2+XC2，

其中：

- *RC* 是负载补偿电阻。
- *XC* 是负载补偿电抗。

电压测量传感器实现为具有时间常数 *TR* 的低通滤波器模块。有关离散和连续实现，请参阅该模块的文档。

### 励磁控制元件

此图说明了励磁控制元件的整体结构：

图中：

- Summation Point Logic 子系统为过励限制器（OEL）、欠励限制器（UEL）、定子电流限制器（SCL）和电源开关选择器（V\_S）电压建模求和点输入位置。有关将此模块与限制器一起使用的更多信息，请参阅励磁电流限制器。
- 有三个 Take-over Logic 子系统。它们为 OEL、UEL、SCL 和 PSS 电压建模接管点输入位置。有关将此模块与限制器一起使用的更多信息，请参阅励磁电流限制器。
- PID\_R 子系统建模一个 PID 控制器，用作自动电压调节器的控制结构。该模块的最小和最大抗积分饱和限幅值为 *VRmin* 和 *VRmax*。
- PI\_R 子系统建模一个 PI 控制器，用作励磁电流调节器的控制结构。该模块的最小和最大抗积分饱和限幅值为 *VAmin* 和 *VAmax*。
- 在自励磁情况下，当 *KR* 非零且 **Power source selector SW2** 参数设置为 `位置 B：不使用变量 V_B` 时，电压调节器功率来自励磁机输出电压。电压调节器指令信号乘以励磁机输出电压 *EFD* 再乘以 *KR*。有关受控整流器电源的用户选择逻辑开关的更多信息，请参阅电源和自励磁。
- *KF1* 和 *KF2* 建模一个高带宽调节器内环，用于调节发电机励磁或励磁电流。
- Filtered Derivative 模块建模用于励磁系统稳定的速率反馈路径，当自动电压调节器没有微分项时。此处，*KF3* 和 *TF* 分别是该系统的增益和时间常数。有关离散和连续实现，请参阅 Filtered Derivative 模块的文档。
- *-K\_L\*VFE* 和 *inf* 是输出励磁机励磁电压 *EFE* 的最小和最大饱和限幅值。
- **initialOffset1** Constant 模块确保仿真可以从稳态开始。SM AC7C 模块使用饱和和励磁机参数计算此值，包括励磁机励磁电流反馈增益、发电机励磁电压反馈增益和初始励磁电压。

### 励磁电流限制器

您可以使用各种励磁电流限制器在不安全运行条件下修改电压调节器的输出：

- 使用过励限制器防止因过大的励磁电流需求导致励磁绕组过热。
- 使用欠励限制器在励磁过低时提升励磁，因为励磁过低存在失步风险。
- 使用定子电流限制器防止因过大电流导致定子绕组过热。

将任何这些限制器的输出连接到以下点之一：

- 作为自动电压调节器（AVR）反馈回路一部分的求和点
- 接管点，用于覆盖 AVR 的通常行为

如果您在求和点使用定子电流限制器，请使用单输入 *VSCLsum*。如果您在接管点使用定子电流限制器，请同时使用过励输入 *VOELscl* 和欠励输入 *VUELscl*。

### 交流旋转励磁机

此图显示了交流旋转励磁机的结构：

图中：

- 励磁机励磁电流 *VFE* 是三个信号之和：

  - 非线性函数 *Vx* 建模励磁机输出电压的饱和。
  - 比例项 *KE* 建模励磁机输出电压与励磁机励磁电流之间的线性关系。
  - 该子系统使用反馈回路中的去磁常数 *KD* 建模负载电流对励磁机输出电压的去磁效应。
- Integrator with variable limits 子系统对 *EFE* 和 *VFE* 之间的差值进行积分，以生成励磁机交流发电机输出电压 *VE*。*TE* 是该过程的时间常数。
- 非线性函数 *FEX* 建模整流器调节引起的励磁机输出电压降。该函数取决于常数 *KC*，而 *KC* 本身是换相电抗的函数。
- 参数 *VEmin* 和 *VFEmax* 建模旋转励磁机的下限和上限。

### 电源和自励磁

通过在 **Power source selector SW1** 参数中选择相关选项，可以为受控整流器使用不同的电源表示。受控整流器的电源可以来自终端电压（`Position A: power source derived from terminal voltage`），也可以独立于终端电压（`Position B: power source independent from the terminal conditions`）。请注意，此开关取决于第二个逻辑开关的状态。

第二个逻辑开关 **Power source selector SW2** 决定励磁机是否采用自励磁。如果 **Power source selector SW2** 参数设置为 `位置 B：不使用变量 V_B`，则励磁机为自励磁，因为与变量 *VB* 相关的模型参数不会影响仿真。
