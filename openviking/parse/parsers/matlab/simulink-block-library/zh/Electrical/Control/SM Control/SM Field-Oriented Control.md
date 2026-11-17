---
type: simulink-block
title: 'SM Field-Oriented Control'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smfieldorientedcontrol'
documentation_source_path: 'ref/smfieldorientedcontrol.html'
language: zh-CN
chinese_source: worker-translation
---

# SM Field-Oriented Control

## 端口
```yaml
ports:
- name: Reference
  summary: 系统参考值标量
  direction: input
  data_types: single | double
- name: iabcSens
  summary: 测量的相电流向量
  direction: input
  data_types: single | double
- name: ifSens
  summary: 测量的励磁电流标量
  direction: input
  data_types: single | double
- name: wSens
  summary: 转子速度标量
  direction: input
  data_types: single | double
- name: thSens
  summary: 转子角度标量
  direction: input
  data_types: single | double
- name: vdcSens
  summary: 直流母线电压标量
  direction: input
  data_types: single | double
- name: G
  summary: 定子变换器门极脉冲向量
  direction: output
  data_types: single | double
- name: Gr
  summary: 励磁斩波器门极脉冲向量
  direction: output
  data_types: single | double
- name: Visualization
  summary: 可视化信号总线
  direction: output
  data_types: single | double
```

### 输入

### **Reference** — 系统参考值标量

系统参考值，根据所选控制模式指定为以 N\*m 为单位的转矩参考值或以 rad/s 为单位的速度参考值。

**数据类型：** `single` | `double`

### **iabcSens** — 测量的相电流向量

测量的定子相电流，单位为 A。

**数据类型：** `single` | `double`

### **ifSens** — 测量的励磁电流标量

测量的转子励磁电流，单位为 A。

**数据类型：** `single` | `double`

### **wSens** — 转子速度标量

测量的转子机械角速度，单位为 rad/s。

**数据类型：** `single` | `double`

### **thSens** — 转子角度标量

测量的转子机械角度，单位为 rad。

**数据类型：** `single` | `double`

### **vdcSens** — 直流母线电压标量

测量的直流母线电压，单位为 V。

**数据类型：** `single` | `double`
### 输出

### **G** — 定子变换器门极脉冲向量

六个脉冲波形，用于确定所连接功率变换器中的开关行为。

**数据类型：** `single` | `double`

### **Gr** — 励磁斩波器门极脉冲向量

用于确定所连接励磁斩波器中开关行为的波形。波形的大小取决于所选的斩波器类型。要指定斩波器类型，请使用 **Chopper type** 参数：

- `First and fourth quadrant
  chopper` — 输出波形有两个脉冲。
- `Four-quadrant chopper` — 输出波形有四个脉冲。

**数据类型：** `single` | `double`

### **Visualization** — 可视化信号总线

包含用于可视化的信号的总线，包括：

- `Reference`
- `wElectrical`
- `iabc`
- `theta`
- `Vdc`
- `PwmEnable`
- `TqRef`
- `TqLim`
- `idqRef`
- `idqf`
- `vdqRef`
- `modWave`
- `DCexcit`

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Control mode
  summary: 控制模式策略 Velocity control（默认）| Torque control
  group: 通用
- name: Nominal dc-link voltage (V)
  summary: 额定直流电压 300 V（默认）| 正数
  group: 通用
- name: Maximum power (W)
  summary: 最大功率 60000 W（默认）| 正数
  group: 通用
- name: Maximum torque (N\*m)
  summary: 最大转矩 250 N*m（默认）| 正数
  group: 通用
- name: Maximum field current (A)
  summary: 最大励磁电流 25 A（默认）| 正数
  group: 通用
- name: Inverter dc-link voltage threshold (V)
  summary: 直流母线电压阈值 100 V（默认）| 正数
  group: 通用
- name: Number of rotor pole pairs
  summary: 极对数 4（默认）| 正整数
  group: 通用
- name: Fundamental sample time (s)
  summary: 模块采样时间 5e-6（默认）| 正数
  group: 通用
- name: Control Type
  summary: 控制类型策略 PI control（默认）| P control | P-PI control
  group: 外环
- name: Controller proportional gain
  summary: PI 控制器比例增益 1（默认）| 正数
  group: 外环
- name: Controller integral gain
  summary: PI 控制器积分增益 1（默认）| 正数
  group: 外环
- name: P controller proportional gain
  summary: P 控制器比例增益 1（默认）| 正数
  group: 外环
- name: Integral anti-windup gain
  summary: 抗积分饱和增益 1（默认）| 正数
  group: 外环
- name: Current references
  summary: 电流参考策略 Zero d-axis control（默认）| Lookup-table based
  group: 外环
- name: Mechanical speed vector, wMechanical (rpm)
  summary: 转子速度查找向量 [0, 3000] rpm（默认）| 正单调递增向量
  group: 外环
- name: Torque reference vector, TqRef (N\*m)
  summary: 转矩参考查找向量 [-100, 0, 100] N*m（默认）| 正单调递增向量
  group: 外环
- name: DC-link voltage vector, Vdc (V)
  summary: 直流母线电压查找向量 [300, 350] V（默认）| 正单调递增向量
  group: 外环
- name: D-axis current reference matrix, id(wMechanical,TqRef,Vdc) (A)
  summary: 参考 d 轴电流值 zeros(2,3,2) A（默认）| 实数矩阵
  group: 外环
- name: Q-axis current reference matrix, iq(wMechanical,TqRef,Vdc) (A)
  summary: 参考 q 轴电流值 zeros(2,3,2) A（默认）| 实数矩阵
  group: 外环
- name: Field current reference matrix, if(wMechanical,TqRef,Vdc), (A)
  summary: 参考励磁电流值 zeros(2,3,2) A（默认）| 实数矩阵
  group: 外环
- name: Torque constant
  summary: 电机转矩常数 0.04 N*m/A（默认）| 正标量
  group: 外环
- name: D-axis current proportional gain
  summary: D 轴比例增益 1（默认）| 正数
  group: 内环
- name: D-axis current integral gain
  summary: D 轴积分增益 100（默认）| 正数
  group: 内环
- name: D-axis current anti-windup gain
  summary: D 轴抗积分饱和增益 1（默认）| 正数
  group: 内环
- name: Q-axis current proportional gain
  summary: Q 轴比例增益 1（默认）| 正数
  group: 内环
- name: Q-axis current integral gain
  summary: Q 轴积分增益 100（默认）| 正数
  group: 内环
- name: Q-axis current anti-windup gain
  summary: Q 轴抗积分饱和增益 1（默认）| 正数
  group: 内环
- name: Field current proportional gain
  summary: 励磁绕组比例增益 10（默认）| 正数
  group: 内环
- name: Field current integral gain
  summary: 励磁绕组积分增益 1000（默认）| 正数
  group: 内环
- name: Field current anti-windup gain
  summary: 励磁绕组抗积分饱和增益 1（默认）| 正数
  group: 内环
- name: Axis prioritization
  summary: 电压限制器的轴优先级 q-axis（默认）| d-axis | d-q equivalence
  group: 内环
- name: Enable zero cancellation
  summary: 前馈零点对消 off（默认）| on
  group: 内环
- name: Enable pre-control voltage
  summary: 预控制电压 on（默认）| off
  group: 内环
- name: Machine parameters
  summary: 电机参数化 Constant parameters（默认）| Lookup table based parameters
  group: 内环
- name: D-axis inductance (H)
  summary: 前馈 d 轴电感 0.00024（默认）| 正标量
  group: 内环
- name: Q-axis inductance (H)
  summary: 前馈 q 轴电感 0.00029（默认）| 正标量
  group: 内环
- name: Mutual field armature inductance (H)
  summary: 励磁绕组与电枢之间的互感 0.007（默认）
  group: 内环
- name: D-axis current vector, id (A)
  summary: D 轴电流断点向量 [-200,0,200] A（默认）| 单调递增向量
  group: 内环
- name: Q-axis current vector, iq (A)
  summary: Q 轴电流断点向量 [-200,0,200] A（默认）| 单调递增向量
  group: 内环
- name: Field current vector, if (A)
  summary: 励磁绕组电流向量 [0,20] A（默认）| 单调递增向量
  group: 内环
- name: Ld matrix, Ld(id,iq) (H)
  summary: D 轴电感查找数据 0.0002 * ones(3, 3) H（默认）| 正矩阵
  group: 内环
- name: Lq matrix, Lq(id,iq) (H)
  summary: Q 轴电感查找数据 0.0002 * ones(3, 3) H（默认）| 正矩阵
  group: 内环
- name: Lmf matrix, Lmf(id,iq,if), (H)
  summary: 励磁-电枢互感查找 0.007 * ones(2,2,2) H（默认）| 正矩阵
  group: 内环
- name: PWM method
  summary: '脉宽调制方法 SVM: space vector modulation（默认）| SPWM: sinusoidal PWM'
  group: PWM
- name: Sampling mode
  summary: 波形采样方法 Natural（默认）| Asymmetric | Symmetric
  group: PWM
- name: Switching frequency (Hz)
  summary: 开关频率 1000 Hz（默认）| 正整数
  group: PWM
- name: Chopper type
  summary: DC-DC 斩波器类型 First and fourth quadrant chopper（默认）| Four-quadrant chopper
  group: PWM
- name: Switching frequency excitation (Hz)
  summary: 励磁系统开关频率 1000 Hz（默认）| 正整数
  group: PWM
```

### 通用

### **Control mode** — 控制模式策略 `Velocity control`（默认）| `Torque control`

指定转矩控制或速度控制策略。

### **Nominal dc-link voltage (V)** — 额定直流电压 `300` `V`（默认）| 正数

电源的额定直流母线电压。

### **Maximum power (W)** — 最大功率 `60000` `W`（默认）| 正数

最大电机功率。

### **Maximum torque (N\*m)** — 最大转矩 `250` `N*m`（默认）| 正数

最大电机转矩。

### **Maximum field current (A)** — 最大励磁电流 `25` `A`（默认）| 正数

励磁绕组中的最大电流。

### **Inverter dc-link voltage threshold (V)** — 直流母线电压阈值 `100` `V`（默认）| 正数

激活功率逆变器的电压阈值。

### **Number of rotor pole pairs** — 极对数 `4`（默认）| 正整数

转子上的极对数。

### **Fundamental sample time (s)** — 模块采样时间 `5e-6`（默认）| 正数

模块的基本采样时间。

### 外环

### **Control Type** — 控制类型策略 `PI control`（默认）| `P control` | `P-PI control`

指定控制策略的类型。

### **Controller proportional gain** — PI 控制器比例增益 `1`（默认）| 正数

PI 控制器的比例增益。

### **Controller integral gain** — PI 控制器积分增益 `1`（默认）| 正数

PI 控制器的积分增益。

### **P controller proportional gain** — P 控制器比例增益 `1`（默认）| 正数

P 控制器的比例增益。

### **Integral anti-windup gain** — 抗积分饱和增益 `1`（默认）| 正数

PI 控制器的抗积分饱和增益。

### **Current references** — 电流参考策略 `Zero d-axis control`（默认）| `Lookup-table based`

选择电流参考策略。

### **Mechanical speed vector, wMechanical (rpm)** — 转子速度查找向量 `[0, 3000]` `rpm`（默认）| 正单调递增向量

用于确定电流参考的查找表中的速度向量。

### **Torque reference vector, TqRef (N\*m)** — 转矩参考查找向量 `[-100, 0, 100]` `N*m`（默认）| 正单调递增向量

用于确定电流参考的查找表中的转矩向量。

### **DC-link voltage vector, Vdc (V)** — 直流母线电压查找向量 `[300, 350]` `V`（默认）| 正单调递增向量

用于确定电流参考的查找表中的直流母线电压向量。

### **D-axis current reference matrix, id(wMechanical,TqRef,Vdc) (A)** — 参考 d 轴电流值 `zeros(2,3,2)` `A`（默认）| 实数矩阵

直轴电流参考查找数据。

### **Q-axis current reference matrix, iq(wMechanical,TqRef,Vdc) (A)** — 参考 q 轴电流值 `zeros(2,3,2)` `A`（默认）| 实数矩阵

交轴电流参考查找数据。

### **Field current reference matrix, if(wMechanical,TqRef,Vdc), (A)** — 参考励磁电流值 `zeros(2,3,2)` `A`（默认）| 实数矩阵

励磁电流参考查找数据。

### **Torque constant** — 电机转矩常数 `0.04` `N*m/A`（默认）| 正标量

同步电机转矩常数。该值在数值上等同于以 `V/(rad/s)` 表示的反电动势常数。

### 内环

### **D-axis current proportional gain** — D 轴比例增益 `1`（默认）| 正数

用于直轴电流控制的 PI 控制器的比例增益。

### **D-axis current integral gain** — D 轴积分增益 `100`（默认）| 正数

用于直轴电流控制的 PI 控制器的积分增益。

### **D-axis current anti-windup gain** — D 轴抗积分饱和增益 `1`（默认）| 正数

用于直轴电流控制的 PI 控制器的抗积分饱和增益。

### **Q-axis current proportional gain** — Q 轴比例增益 `1`（默认）| 正数

用于交轴电流控制的 PI 控制器的比例增益。

### **Q-axis current integral gain** — Q 轴积分增益 `100`（默认）| 正数

用于交轴电流控制的 PI 控制器的积分增益。

### **Q-axis current anti-windup gain** — Q 轴抗积分饱和增益 `1`（默认）| 正数

用于交轴电流控制的 PI 控制器的抗积分饱和增益。

### **Field current proportional gain** — 励磁绕组比例增益 `10`（默认）| 正数

用于励磁电流控制的 PI 控制器的比例增益。

### **Field current integral gain** — 励磁绕组积分增益 `1000`（默认）| 正数

用于励磁电流控制的 PI 控制器的积分增益。

### **Field current anti-windup gain** — 励磁绕组抗积分饱和增益 `1`（默认）| 正数

用于励磁电流控制的 PI 控制器的抗积分饱和增益。

### **Axis prioritization** — 电压限制器的轴优先级 `q-axis`（默认）| `d-axis` | `d-q equivalence`

当模块限制电压时，优先处理或维持 *d* 轴和 *q* 轴之间的比例。

### **Enable zero cancellation** — 前馈零点对消 `off`（默认）| `on`

启用或禁用前馈路径上的零点对消。

### **Enable pre-control voltage** — 预控制电压 `on`（默认）| `off`

启用或禁用预控制电压。

### **Machine parameters** — 电机参数化 `Constant parameters`（默认）| `Lookup table based parameters`

指定如何参数化电机。

- `Constant parameters` — 指定在整个仿真过程中保持恒定的电机参数。
- `Lookup table based parameters` — 将电机参数指定为依赖于电流的查找表。

#### 依赖关系

当选中 **Enable pre-control voltage** 参数时启用。

### **D-axis inductance (H)** — 前馈 d 轴电感 `0.00024`（默认）| 正标量

用于前馈预控制的直轴电感。

#### 依赖关系

当 **Machine parameters** 参数设置为 `Constant parameters` 时启用。

### **Q-axis inductance (H)** — 前馈 q 轴电感 `0.00029`（默认）| 正标量

用于前馈预控制的交轴电感。

#### 依赖关系

当 **Machine parameters** 参数设置为 `Constant parameters` 时启用。

### **Mutual field armature inductance (H)** — 励磁绕组与电枢之间的互感 `0.007`（默认）

励磁绕组与电枢绕组之间的互感。

#### 依赖关系

当 **Machine parameters** 参数设置为 `Constant parameters` 时启用。

### **D-axis current vector, id (A)** — D 轴电流断点向量 `[-200,0,200]` `A`（默认）| 单调递增向量

用于参数确定查找表的直轴电流向量。

#### 依赖关系

当 **Machine parameters** 参数设置为 `Lookup table based
parameters` 时启用。

### **Q-axis current vector, iq (A)** — Q 轴电流断点向量 `[-200,0,200]` `A`（默认）| 单调递增向量

用于参数确定查找表的交轴电流向量。

#### 依赖关系

当 **Machine parameters** 参数设置为 `Lookup table based
parameters` 时启用。

### **Field current vector, if (A)** — 励磁绕组电流向量 `[0,20]` `A`（默认）| 单调递增向量

用于参数确定查找表的励磁电流向量。

#### 依赖关系

当 **Machine parameters** 参数设置为 `Lookup table based
parameters` 时启用。

### **Ld matrix, Ld(id,iq) (H)** — D 轴电感查找数据 `0.0002 * ones(3, 3)` `H`（默认）| 正矩阵

用作查找表数据的 *Ld* 矩阵。

#### 依赖关系

当 **Machine parameters** 参数设置为 `Lookup table based
parameters` 时启用。

### **Lq matrix, Lq(id,iq) (H)** — Q 轴电感查找数据 `0.0002 * ones(3, 3)` `H`（默认）| 正矩阵

用作查找表数据的 *Lq* 矩阵。

#### 依赖关系

当 **Machine parameters** 参数设置为 `Lookup table based
parameters` 时启用。

### **Lmf matrix, Lmf(id,iq,if), (H)** — 励磁-电枢互感查找 `0.007 * ones(2,2,2)` `H`（默认）| 正矩阵

用作查找表数据的 *Lmf* 矩阵。

#### 依赖关系

当 **Machine parameters** 参数设置为 `Lookup table based
parameters` 时启用。

### PWM

### **PWM method** — 脉宽调制方法 `SVM: space vector modulation`（默认）| `SPWM: sinusoidal PWM`

指定波形技术。

### **Sampling mode** — 波形采样方法 `Natural`（默认）| `Asymmetric` | `Symmetric`

指定模块在波形相交时或在载波处于其一个或两个边界条件时对调制波形进行采样的方式。

### **Switching frequency (Hz)** — 开关频率 `1000` `Hz`（默认）| 正整数

指定功率变换器中开关的切换速率。

### **Chopper type** — DC-DC 斩波器类型 `First and fourth quadrant chopper`（默认）| `Four-quadrant chopper`

指定 DC-DC 斩波器类型。

### **Switching frequency excitation (Hz)** — 励磁系统开关频率 `1000` `Hz`（默认）| 正整数

指定励磁系统的 PWM 开关频率。
## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

同步电机磁场定向控制

SM Field-Oriented Control 模块实现同步电机（SM）磁场定向控制结构。磁场定向控制（FOC）是一种高性能的交流电机控制策略，通过将静止相电流变换到旋转坐标系来解耦转矩和磁通。当转子速度和位置已知且您的应用需要以下条件时，请使用 FOC：

- 启动时高转矩和低电流
- 高效率

### 方程

SM FOC 由 Control 库中的若干控制模块组成。要查看和修改这些模块以及 FOC 的内部结构，请在 Simulink 中右键单击该模块，然后选择 **Mask** > **Look Under Mask**。整体控制结构由若干部分组成：

- 外环控制器将您提供的参考信号转换为参考 *d* 轴、*q* 轴和励磁电流。

  您可以使用 `Control mode` 参数选择所提供的参考信号类型：

  - `Velocity control` — 控制或调节同步电机的旋转速度。内部 Velocity Controller 模块根据转子速度误差生成参考转矩。
  - `Torque control` — 控制或调节 SM 的机械转矩。

  内部 SM Current Reference Generator 模块使用比例积分（PI）控制器生成参考电流，从而最小化转矩误差。
- 内环控制器将电流参考转换为电压参考。内部 SM Current Controller 使用 PI 控制器生成电压参考，从而最小化电流误差，并使用前馈项：

  vd\_FF=−ωeLqiqvq\_FF=ωe(Ldid+Lmfif)vf\_FF=0

  其中：

  - *ωe* 是转子电角速度。
  - *Ld* 和 *Lq* 分别是 *d* 轴和 *q* 轴定子电感。
  - *Lmf* 是励磁-电枢互感。
  - *id*、*iq* 和 *if* 分别是定子 *d*-*q* 轴电流和励磁电流。
- PWM Generator 将参考定子电压转换为门极脉冲，以传递给为同步电机定子绕组供电的 Power Converter。
- Excitation PWM Generator 将参考励磁电压转换为门极脉冲，以传递给为 SM 励磁绕组供电的 DC-DC Chopper。

下图显示了该模块的整体架构。

图中：

- *ω* 和 *ωref* 分别是测量的和参考的角速度。
- *Tref* 是参考电磁转矩。如果您将模块配置为速度控制，Velocity Controller 会生成此参考转矩。
- *i* 和 *v* 是定子电流和电压。下标 *d*、*q* 和 *f* 分别表示 *d* 轴、*q* 轴和励磁绕组。下标 *a*、*b* 和 *c* 表示三个定子绕组。
- *θe* 是转子电角度。
- *G* 是门极脉冲，下标 *H* 和 *L* 分别表示高电平和低电平，下标 *a*、*b* 和 *c* 表示三个定子绕组。下标 *ex* 表示励磁脉冲。

您可以使用 `Control mode` 参数选择实现速度控制或转矩控制。该模块完全按照图中所示实现速度控制。该模块通过移除 Velocity Controller 模块并直接接受参考转矩来实现转矩控制。

### 假设

电机参数已知。

### 限制

控制结构以单一采样率实现。
