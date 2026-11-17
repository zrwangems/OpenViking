---
type: simulink-block
title: 'SM AC8C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smac8c'
documentation_source_path: 'ref/smac8c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM AC8C

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
- name: V_OELscl
  summary: 过励限制器的接管定子电流限制标量
  direction: input
  data_types: single | double
- name: V_UELscl
  summary: 欠励限制器的接管定子电流限制标量
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

电压调节器参考设定值，以标幺值表示，指定为标量。

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

- 要忽略来自过励限制器的输入，请将
  **备用 OEL 输入位置
  (V\_OEL)** 设置为
  `Unused`。
- 要在求和点使用来自过励限制器的输入，请将 **备用 OEL 输入位置
  (V\_OEL)** 设置为 `Summation
  point`。
- 要在接管点使用来自过励限制器的输入，请将
  **备用 OEL 输入位置
  (V\_OEL)** 设置为
  `Take-over`。

**数据类型：** `single` | `double`

### **V\_UEL** — 欠励限制信号标量

来自欠励限制器的输入，以标幺值表示，指定为标量。

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

使用求和点时来自定子电流限制器的输入，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将
  **备用 SCL 输入位置
  (V\_SCL)** 设置为
  `Unused`。
- 要在求和点使用来自定子电流限制器的输入，请将 **备用 SCL 输入位置
  (V\_SCL)** 设置为 `Summation
  point`。

**数据类型：** `single` | `double`

### **V\_OELscl** — 过励限制器的接管定子电流限制标量

使用接管点时来自定子电流限制器的输入，用于防止磁场过励，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将
  **备用 SCL 输入位置
  (V\_SCL)** 设置为
  `Unused`。
- 要在接管点使用来自定子电流限制器的输入，请将 **备用 SCL 输入位置
  (V\_SCL)** 设置为
  `Take-over`。

**数据类型：** `single` | `double`

### **V\_UELscl** — 欠励限制器的接管定子电流限制标量

使用接管点时来自定子电流限制器的输入，用于防止磁场欠励，以标幺值表示，指定为标量。

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

要施加到同步电机磁场电路的标幺磁场电压，以标量形式返回。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: 初始磁场电压，Efd0 (pu)
  summary: 初始输出电压 1（默认）| 实数
  group: 常规
- name: 初始端电压，Vt0 (pu)
  summary: 初始端电压 1（默认）| 实数
  group: 常规
- name: 初始端电流，It0 (pu)
  summary: 初始端电流 1（默认）| 实数
  group: 常规
- name: 采样时间（-1 表示继承）
  summary: 模块采样时间 -1（默认）| 0 | 正标量
  group: 常规
- name: 负载补偿的电阻分量，R_C (pu)
  summary: 补偿电阻 0（默认）| 正数
  group: 预控制
- name: 负载补偿的电抗分量，X_C (pu)
  summary: 补偿电抗 0（默认）| 正数
  group: 预控制
- name: 调节器输入滤波器时间常数，T_R (s)
  summary: 调节器时间常数 0（默认）| 正数
  group: 预控制
- name: 电压调节器比例增益，K_PR (pu)
  summary: 电压调节器的比例增益 80（默认）
  group: 控制
- name: 电压调节器积分增益，K_IR (pu/s)
  summary: 电压调节器的积分增益 5（默认）
  group: 控制
- name: 电压调节器微分增益，K_DR (pu.s)
  summary: 电压调节器的微分增益 10（默认）
  group: 控制
- name: PID 控制器微分通道的滞后时间常数，T_DR (s)
  summary: PID 微分通道的滞后时间常数 0.02（默认）| 正数
  group: 控制
- name: 电压调节器最大输出，V_PIDmax (pu)
  summary: PID 调节器的最大输出 99（默认）| 正数
  group: 控制
- name: 电压调节器最小输出，V_PIDmin (pu)
  summary: 调节器的最小输出 -99（默认）| 正数
  group: 控制
- name: 整流桥增益，K_A (pu)
  summary: 整流桥增益 1（默认）| 正数
  group: 控制
- name: 整流桥时间常数，T_A (s)
  summary: 整流桥时间常数 0.01（默认）| 正数
  group: 控制
- name: 调节器最大输出，V_Rmax (pu)
  summary: 调节器输出的上限 35（默认）| 实数
  group: 控制
- name: 调节器最小输出，V_Rmin (pu)
  summary: 调节器输出的下限 0（默认）| 实数
  group: 控制
- name: 备用 PSS 输入位置 (V_S)
  summary: PSS 输入位置 Voltage error calculation（默认）| After take-over UEL
  group: 控制
- name: 备用 OEL 输入位置 (V_OEL)
  summary: OEL 输入位置 Unused（默认）| Summation point at voltage error | Take-over at voltage error | Take-over at voltage regulator
    output
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
  summary: 整流器负载因子 0.55（默认）| 正数
  group: 励磁机
- name: 去磁因子，励磁机交流电机电抗的函数，K_D (pu)
  summary: 去磁因子 1.1（默认）| 正数
  group: 励磁机
- name: 饱和因子 S_E(E_1) 对应的励磁机输出电压，E_1 (pu)
  summary: 第一饱和输出电压 9（默认）| 正数
  group: 励磁机
- name: 励磁机输出电压 E_1 处的励磁机饱和因子，S_E(E_1) (1)
  summary: 第一饱和查找电压 3（默认）| 正数
  group: 励磁机
- name: 饱和因子 S_E(E_2) 对应的励磁机输出电压，E_2 (pu)
  summary: 第二饱和输出电压 6.5（默认）| 正数
  group: 励磁机
- name: 励磁机输出电压 E_2 处的励磁机饱和因子，S_E(E_2) (1)
  summary: 第二饱和查找电压 0.3（默认）| 正数
  group: 励磁机
- name: 最大励磁机磁场电流，V_FEmax (pu)
  summary: 励磁机上限 6（默认）| 实数
  group: 励磁机
- name: 最小励磁机电压输出限制，V_Emin (pu)
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
- name: 与换相电抗成比例的整流器负载因子，K_C1 (pu)
  summary: 与换相电抗成比例的整流器负载因子 0（默认）| 实数
  group: 励磁机
- name: 逻辑开关 1
  summary: '逻辑开关 Position A: power source derived from terminal voltage（默认）| Position B: power source independent of the terminal
    conditions'
  group: 励磁机
- name: 最大可用励磁机磁场电压，V_Bmax (pu)
  summary: 最大可用励磁机磁场电压 1.25（默认）| 实数
  group: 励磁机
```

### 常规

### **初始磁场电压，Efd0 (pu)** — 初始输出电压 `1`（默认）| 实数

要施加到同步电机磁场电路的初始标幺电压。

### **初始端电压，Vt0 (pu)** — 初始端电压 `1`（默认）| 实数

要施加到端子的初始标幺电压。

### **初始端电流，It0 (pu)** — 初始端电流 `1`（默认）| 实数

要施加到端子的初始标幺电压。

### **采样时间（-1 表示继承）** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。
有关详细信息，请参阅什么是采样时间？和指定采样时间。

对于继承的离散时间操作，请将此参数设置为 `-1`。
对于离散时间操作，请将此参数设置为正整数。对于连续时间操作，请将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅提升掩码上的模块参数。

### 预控制

### **负载补偿的电阻分量，R\_C (pu)** — 补偿电阻 `0`（默认）| 正数

电流补偿系统中使用的电阻。将此参数和
**负载补偿的电抗分量，X\_C
(pu)** 设置为 `0` 以禁用电流补偿。

### **负载补偿的电抗分量，X\_C (pu)** — 补偿电抗 `0`（默认）| 正数

电流补偿系统中使用的电抗。将此参数和
**负载补偿的电阻分量，R\_C
(pu)** 设置为 `0` 以禁用电流补偿。

### **调节器输入滤波器时间常数，T\_R (s)** — 调节器时间常数 `0`（默认）| 正数

电压传感器滤波的等效时间常数。

### 控制

### **电压调节器比例增益，K\_PR (pu)** — 电压调节器的比例增益 `80`（默认）

电压调节器的标幺比例增益。

### **电压调节器积分增益，K\_IR (pu/s)** — 电压调节器的积分增益 `5`（默认）

电压调节器的标幺积分增益。

### **电压调节器微分增益，K\_DR (pu.s)** — 电压调节器的微分增益 `10`（默认）

电压调节器的微分增益。

### **PID 控制器微分通道的滞后时间常数，T\_DR (s)** — PID 微分通道的滞后时间常数 `0.02`（默认）| 正数

PID 控制器微分通道的等效滞后时间常数。

### **电压调节器最大输出，V\_PIDmax (pu)** — PID 调节器的最大输出 `99`（默认）| 正数

PID 调节器的最大允许标幺输出。

### **电压调节器最小输出，V\_PIDmin (pu)** — 调节器的最小输出 `-99`（默认）| 正数

PID 调节器的最小允许标幺输出。

### **整流桥增益，K\_A (pu)** — 整流桥增益 `1`（默认）| 正数

与整流器相关的增益。

### **整流桥时间常数，T\_A (s)** — 整流桥时间常数 `0.01`（默认）| 正数

整流器的时间常数。

### **调节器最大输出，V\_Rmax (pu)** — 调节器输出的上限 `35`（默认）| 实数

调节器的最大标幺输出电压。

### **调节器最小输出，V\_Rmin (pu)** — 调节器输出的下限 `0`（默认）| 实数

调节器的最小标幺输出电压。

### **备用 PSS 输入位置 (V\_S)** — PSS 输入位置 `Voltage error calculation`（默认）| `After take-over UEL`

电力系统稳定器输入的位置。

### **备用 OEL 输入位置 (V\_OEL)** — OEL 输入位置 `Unused`（默认）| `Summation point at voltage error` | `Take-over at voltage error` | `Take-over at voltage regulator output`

过励限制器输入的位置。

### **备用 UEL 输入位置 (V\_UEL)** — UEL 输入位置 `Unused`（默认）| `Summation point at voltage error` | `Take-over at voltage error` | `Take-over at voltage regulator output`

欠励限制器输入的位置。

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

### **与换相电抗成比例的整流器负载因子，K\_C (pu)** — 整流器负载因子 `0.55`（默认）| 正数

与换相电抗成比例的整流器负载因子。

### **去磁因子，励磁机交流电机电抗的函数，K\_D (pu)** — 去磁因子 `1.1`（默认）| 正数

与励磁机交流电机电抗相关的去磁因子。

### **饱和因子 S\_E(E\_1) 对应的励磁机输出电压，E\_1 (pu)** — 第一饱和输出电压 `9`（默认）| 正数

第一饱和因子对应的励磁机输出电压。

### **励磁机输出电压 E\_1 处的励磁机饱和因子，S\_E(E\_1) (1)** — 第一饱和查找电压 `3`（默认）| 正数

第一励磁机的饱和因子。

### **饱和因子 S\_E(E\_2) 对应的励磁机输出电压，E\_2 (pu)** — 第二饱和输出电压 `6.5`（默认）| 正数

第二饱和因子对应的励磁机输出电压。

### **励磁机输出电压 E\_2 处的励磁机饱和因子，S\_E(E\_2) (1)** — 第二饱和查找电压 `0.3`（默认）| 正数

第二励磁机的饱和因子。

### **最大励磁机磁场电流，V\_FEmax (pu)** — 励磁机上限 `6`（默认）| 实数

最大标幺磁场电流限制参考值。

### **最小励磁机电压输出限制，V\_Emin (pu)** — 励磁机下限 `0`（默认）| 实数

最小标幺励磁机电压输出。

### **电势电路增益系数，K\_P (pu)** — 电势电路增益系数 `1`（默认）| 实数

标幺电势电路增益系数。

#### 依赖关系

要启用此参数，请将 **逻辑开关 1** 设置为
`Position A: power source derived from terminal
voltage`。

### **电势电路相位角（度）** — 电势电路相位角 `0`（默认）| 实数

电势电路相位角，以度为单位。

#### 依赖关系

要启用此参数，请将 **逻辑开关
1** 设置为 `Position A: power source derived
from terminal voltage`。

### **电势电路（电流）增益系数，K\_I (pu)** — 电势电路电流增益系数 `0`（默认）| 实数

标幺电势电路电流增益系数。

#### 依赖关系

要启用此参数，请将 **逻辑开关
1** 设置为 `Position A: power source derived
from terminal voltage`。

### **与电势源相关的电抗，X\_L (pu)** — 与电势源相关的电抗 `0`（默认）| 实数

与电势源相关的标幺电抗。

#### 依赖关系

要启用此参数，请将 **逻辑开关
1** 设置为 `Position A: power source derived
from terminal voltage`。

### **与换相电抗成比例的整流器负载因子，K\_C1 (pu)** — 与换相电抗成比例的整流器负载因子 `0`（默认）| 实数

与换相电抗成比例的整流器标幺负载因子。

### **逻辑开关 1** — 逻辑开关 `Position A: power source derived from terminal voltage`（默认）| `Position B: power source independent of the terminal conditions`

逻辑开关 1 的位置。

### **最大可用励磁机磁场电压，V\_Bmax (pu)** — 最大可用励磁机磁场电压 `1.25`（默认）| 实数

励磁机的最大标幺可用磁场电压。
## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

离散时间或连续时间同步电机 AC8C 励磁系统，包括自动电压调节器和励磁机

SM AC8C 模块实现符合 IEEE 421.5-2016[1] 的同步电机 AC8C 型励磁系统模型。

使用此模块可对作为发电机运行并使用交流旋转励磁机的同步电机的磁场电压进行控制和调节建模。

您可以使用
**采样时间（-1 表示继承）** 参数在模块的连续实现和离散实现之间切换。要将积分器配置为连续时间，请将 **采样时间（-1 表示继承）** 属性设置为 `0`。要将积分器配置为离散时间，请将 **采样时间（-1 表示继承）** 属性设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。

SM AC8C 模块由五个主要组件组成：

- 电流补偿器根据端电流修改测量的端电压。
- 电压测量传感器使用低通滤波器模拟端电压传感器的动态特性。
- 励磁控制元件组件将电压传感器输出与端电压参考值进行比较，以产生电压误差。然后，该电压误差通过电压调节器以产生励磁机磁场电压。
- 交流旋转励磁机对交流旋转励磁机进行建模，该励磁机产生施加到受控同步电机的磁场电压。该模块还将励磁机磁场电流（标准符号为 *VFE*）反馈到励磁系统。
- 电源对受控整流器电源与端电压的依赖关系进行建模。

此图显示了 AC8C 励磁系统模型的整体结构：

图中：

- *VT* 和
  *IT* 是同步电机的测量端电压和电流。
- *VC1* 是电流补偿后的端电压。
- *VC* 是滤波后的电流补偿端电压。
- *VREF* 是参考端电压。
- *VS* 是电力系统稳定器电压。
- *SW1* 是用户选择的受控整流器电源开关。
- *VB* 是励磁机磁场电压。
- *EFE* 和
  *VFE* 分别是励磁机磁场电压和电流。
- *EFD* 和
  *IFD* 分别是磁场电压和电流。

以下各节详细描述了模块的每个主要部分。

### 电流补偿器和电压测量传感器

电流补偿器建模为：

VC1=VT+ITRC2+XC2，

其中：

- *RC* 是负载补偿电阻。
- *XC* 是负载补偿电抗。

电压测量传感器实现为时间常数为
*TR* 的低通滤波器模块。有关离散和连续实现，请参阅此模块的文档。

### Excitation Control Elements

此图展示了励磁控制元件的整体结构：

图中：

- Summation Point Logic 子系统为过励限制器（OEL）、欠励限制器（UEL）、定子电流限制器（SCL）和电源开关选择器（V\_S）电压建模了求和点输入位置。有关将此模块与限制器配合使用的详细信息，请参阅 Field Current Limiters。
- 有两个 Take-over Logic 子系统。它们为 OEL、UEL、SCL 和 PSS 电压建模了接管点输入位置。有关将此模块与限制器配合使用的详细信息，请参阅 Field Current Limiters。
- PID\_R 子系统为作为自动电压调节器控制结构的 PID 控制器建模。该模块的最小和最大抗积分饱和限幅分别为 *VPIDmin* 和 *VPIDmax*。
- Low-Pass Filter 模块为电压调节器的主要动态特性建模。其中，*KA* 是调节器增益，*TA* 是调节器的主要时间常数。该模块的最小和最大抗积分饱和限幅分别为 *VRmin* 和 *VRmax*。
- **Logical switch 1** 参数控制受控整流器电源的来源。电压调节器指令信号 *VR* 乘以励磁机磁场电压 *VB*。有关用户为受控整流器电源选择的逻辑开关的详细信息，请参阅 Power Source。

### Field Current Limiters

您可以使用各种磁场电流限制器在不安全运行条件下修改电压调节器的输出：

- 使用过励限制器防止因过大的磁场电流需求导致磁场绕组过热。
- 当励磁过低时，使用欠励限制器提升磁场励磁，因为过低会有失步风险。
- 使用定子电流限制器防止因电流过大导致定子绕组过热。

将上述任一限制器的输出连接到以下任一位置：

- 求和点，作为自动电压调节器（AVR）反馈回路的一部分
- 接管点，以覆盖 AVR 的通常行为

如果在求和点使用定子电流限制器，请使用单输入 *VSCLsum*。如果在接管点使用定子电流限制器，请同时使用过励输入 *VOELscl* 和欠励输入 *VUELscl*。

### AC Rotating Exciter

此图展示了交流旋转励磁机的结构：

图中：

- 励磁机磁场电流 *VFE* 是三个信号之和：

  - 非线性函数 *Vx* 为励磁机输出电压的饱和建模。
  - 比例项 *KE* 为励磁机输出电压与励磁机磁场电流之间的线性关系建模。
  - 该子系统使用反馈回路中的去磁常数 *KD* 为负载电流对励磁机输出电压的去磁效应建模。
- Integrator with variable limits 子系统对 *EFE* 与 *VFE* 之差进行积分，以生成励磁机交流发电机输出电压 *VE*。*TE* 是此过程的时间常数。
- 非线性函数 *FEX* 为整流器调节引起的励磁机输出电压降建模。此函数取决于常数 *KC*，而 *KC* 本身是换相电抗的函数。
- 参数 *VEmin* 和 *VFEmax* 为旋转励磁机的下限和上限建模。

### Power Source

通过在 **Logical switch 1** 参数中选择相关选项，可以为受控整流器使用不同的电源表示。受控整流器的电源既可以来自机端电压（`Position A: power source derived from terminal voltage`），也可以独立于机端电压（`Position B: power source independent from the terminal conditions`）。
