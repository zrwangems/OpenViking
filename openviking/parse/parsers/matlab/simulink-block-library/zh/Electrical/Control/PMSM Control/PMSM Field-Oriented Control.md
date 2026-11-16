---
type: simulink-block
title: 'PMSM Field-Oriented Control'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / PMSM Control'
documentation_page: 'pmsmfieldorientedcontrol'
documentation_source_path: 'ref/pmsmfieldorientedcontrol.html'
language: zh-CN
chinese_source: worker-translation
---

# PMSM Field-Oriented Control

## 端口

### 输入

### **Reference** — 系统参考标量

系统参考，根据所选控制模式指定为 N\*m 中的转矩参考或 rad/s 中的速度参考。

**数据类型：** `single` | `double`

### **iabcSens** — 测量的相电流向量

测量的定子相电流，单位为 A。

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

### **G** — 门极脉冲向量

六个脉冲波形，用于确定所连接功率变换器中的开关行为。

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
- `idq`
- `vdqRef`
- `modWave`

**数据类型：** `single` | `double`

## 参数

#### 常规

### **Winding Type** — 控制参数化 `Wye-wound` (默认) | `Delta-wound`

为控制器的参考值指定 wye-wound 或 delta-wound 参数化。

### **Control Mode** — 控制模式策略 `Torque control` (默认) | `Velocity control`

指定转矩控制或速度控制策略。

### **Nominal dc-link voltage (V)** — 额定直流电压 `300` (默认) | 正数

电源的标称直流母线电压，单位为 `V`。

### **Maximum power (W)** — 最大功率 `35000` (默认) | 正数

电机最大功率，单位为 `W`。

### **Maximum torque (N\*m)** — 最大转矩 `250` (默认) | 正数

电机最大转矩，单位为 `N*m`。

### **Number of rotor pole pairs** — 极对数 `8` (默认) | 正整数

转子上的永磁体极对数。

### **Inverter dc-link voltage threshold (V)** — 直流母线电压阈值 `100` (默认) | 正数

激活功率逆变器的电压阈值，单位为 `V`。

### **Fundamental sample time (s)** — 模块采样时间 `5e-6` (默认) | 正数

模块的基本采样时间，单位为 `s`。

### **Control sample time (s)** — 控制采样时间 `1e-4` (默认) | 正数

控制系统的采样时间，单位为 `s`。

#### 外环

### **Control Type** — 控制类型策略 `PI control` (默认) | `P control` | `P-PI control`

指定控制策略的类型。

### **Controller proportional gain** — PI 控制器的比例增益 `1` (默认) | 正数

PI 控制器的比例增益。

### **Controller integral gain** — PI 控制器的积分增益 `1` (默认) | 正数

PI 控制器的积分增益。

### **P controller proportional gain** — P 控制器的比例增益 `1` (默认) | 正数

P 控制器的比例增益。

### **Integral anti-windup gain** — 抗积分饱和增益 `1` (默认) | 正数

PI 控制器的抗积分饱和增益。

### **Current references** — 电流参考策略 `Zero d-axis control` (默认) | `Lookup-table based` | `Automatically generated lookup-table`

选择电流参考策略。

### **Mechanical speed vector, wMechanical (rpm)** — 转子速度查找向量 `[0, 3000]` (默认) | 正单调递增向量

用于确定电流参考的查找表中的速度向量，单位为 `rpm`。

### **Torque reference vector, TqRef (N\*m)** — 转矩参考查找向量 `[-100, 0, 100]` (默认) | 正单调递增向量

用于确定电流参考的查找表中的转矩向量，单位为 `N*m`。

### **DC-link voltage vector, Vdc (V)** — 直流母线电压查找向量 `[300, 350]` (默认) | 正单调递增向量

用于确定电流参考的查找表中的直流母线电压向量，单位为 `V`。

### **D-axis current reference matrix, id(wMechanical,TqRef,Vdc) (A)** — 参考 d 轴电流值 `zeros(2,3,2)` (默认) | 实数矩阵

直轴电流参考查找数据，单位为 `A`。

### **Q-axis current reference matrix, iq(wMechanical,TqRef,Vdc) (A)** — 参考 q 轴电流值 `zeros(2,3,2)` (默认) | 实数矩阵

交轴电流参考查找数据，单位为 `A`。

### **Modulation factor** — 调制因子 `1` (默认) | 正标量

用于在生成电流参考时计算最大允许相电压的安全因子。

#### 依赖关系

仅当 **Current references** 设置为 `Automatically generated lookup-table` 时，此参数才可见。

### **Permanent magnet flux linkage (Wb)** — PM 磁链 `0.04` (默认) | 正标量

峰值永磁磁链，单位为 `Wb`。

### **D-axis inductance (H)** — d 轴电感 `0.00024` (默认) | 正标量

直轴电感，单位为 `H`。

### **Q-axis inductance (H)** — q 轴电感 `0.00029` (默认) | 正标量

交轴电感，单位为 `H`。

### **Stator resistance (Ohm)** — 定子电阻 `0.01` (默认) | 正标量

每相定子电阻，单位为 `Ohm`。

#### 内环

### **D-axis current proportional gain** — d 轴比例增益 `1` (默认) | 正数

用于直轴电流控制的 PI 控制器的比例增益。

### **D-axis current integral gain** — d 轴积分增益 `100` (默认) | 正数

用于直轴电流控制的 PI 控制器的积分器增益。

### **D-axis current anti-windup gain** — d 轴抗积分饱和增益 `1` (默认) | 正数

用于直轴电流控制的 PI 控制器的抗积分饱和增益。

### **Q-axis current proportional gain** — q 轴比例增益 `1` (默认) | 正数

用于交轴电流控制的 PI 控制器的比例增益。

### **Q-axis current integral gain** — q 轴积分增益 `100` (默认) | 正数

用于交轴电流控制的 PI 控制器的积分器增益。

### **Q-axis current anti-windup gain** — q 轴抗积分饱和增益 `1` (默认) | 正数

用于交轴电流控制的 PI 控制器的抗积分饱和增益。

### **Axis prioritization** — 电压限制器的轴优先级 `q-axis` (默认) | `d-axis` | `d-q equivalence`

当模块限制电压时，优先考虑或保持 *d* 轴与 *q* 轴之间的比例。

### **Enable zero cancellation** — 前馈零点对消 `off` (默认) | `on`

启用或禁用前馈路径上的零点对消。

### **Enable pre-control voltage** — 预控制电压 `on` (默认) | `off`

启用或禁用预控制电压。

### **Machine parameters** — 电机参数化 `Constant parameters` (默认) | `Lookup table based parameters`

指定如何参数化电机。

- `Constant parameters` — 指定在仿真过程中保持恒定的电机参数。
- `Lookup table based parameters` — 指定依赖于电流的查找表形式的电机参数。

### **D-axis inductance for feed-forward pre-control (H)** — 前馈 d 轴电感 `0.00024` (默认) | 正标量

用于前馈预控制的直轴电感，单位为 `H`。

### **Q-axis inductance for feed-forward pre-control (H)** — 前馈 q 轴电感 `0.00029` (默认) | 正标量

用于前馈预控制的交轴电感，单位为 `H`。

### **Permanent magnet flux linkage for feed-forward pre-control (H)** — 前馈磁链 `0.04` (默认) | 标量

用于前馈预控制的永磁磁链，单位为 `H`。

### **D-axis current vector, id (A)** — d 轴电流断点向量 `[-200,0,200]` (默认) | 单调递增向量

用于参数确定的查找表中的直轴电流向量，单位为 `A`。对于恒定电机参数，请勿更改默认值。

### **Q-axis current vector, iq (A)** — q 轴电流断点向量 `[-200,0,200]` (默认) | 单调递增向量

用于参数确定的查找表中的交轴电流向量，单位为 `A`。对于恒定电机参数，请勿更改默认值。

### **Ld matrix, Ld(id,iq) (H)** — d 轴电感查找数据 `0.0002 * ones(3, 3)` (默认) | 正矩阵

用作查找表数据的 *Ld* 矩阵，单位为 `H`。对于恒定电机参数，仅更改常数因子，例如 *Ld* \* `ones(3, 3)`。

### **Lq matrix, Lq(id,iq) (H)** — q 轴电感查找数据 `0.0002 * ones(3, 3)` (默认) | 正矩阵

用作查找表数据的 *Lq* 矩阵，单位为 `H`。对于恒定电机参数，仅更改常数因子，例如 *Lq* \* `ones(3, 3)`。

### **Permanent magnet flux linkage matrix, PM(id,iq) (Wb)** — 磁链查找数据 `0.04 * ones(3, 3)` (默认) | 实数矩阵

用于查找表的永磁磁链矩阵，单位为 `Wb`。对于恒定电机参数，仅更改常数因子，例如 *psim* \* `ones(3, 3)`。

#### PWM

### **PWM method** — 脉宽调制方法 `SVM: space vector modulation` (默认) | `SPWM: sinusoidal PWM`

指定波形技术。

### **Sampling mode** — 波采样方法 `Natural` (默认) | `Asymmetric` | `Symmetric`

指定模块是在波相交时采样调制波形，还是在载波处于其一个或两个边界条件时采样。

### **Switching frequency (Hz)** — 开关频率 `1000` (默认) | 正整数

指定您希望功率变换器中的开关进行开关的速率。

## 所属库

Simscape / Electrical / Control / PMSM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

永磁同步电机磁场定向控制

PMSM Field-Oriented Control 模块为永磁同步电机 (PMSM) 实现磁场定向控制结构。磁场定向控制 (FOC) 是一种高性能的交流电机控制策略，它通过将静止相电流变换到旋转坐标系来解耦转矩和磁链。当已知转子速度和位置，并且您的应用需要以下条件时，请使用 FOC：

- 启动时高转矩和低电流。
- 高效率。

### 方程

PMSM FOC 结构通过使用转子 d-q 参考坐标系来解耦转矩和磁链。下图显示了该模块的整体架构。

图中：

- *ω* 和 *ωref* 分别是测量的和参考的角速度。
- *Tref* 是参考电磁转矩。
- *i* 和 *v* 是定子电流和电压，下标 *d* 和 *q* 表示 *d* 轴和 *q* 轴，下标 *a*、*b* 和 *c* 表示三个定子绕组。
- *θe* 是转子电角度。
- *G* 是门极脉冲，下标 *H* 和 *L* 表示高电平和低电平，下标 *a*、*b* 和 *c* 表示三个定子绕组。

您可以使用 `Control mode` 参数选择实现速度控制或转矩控制。该模块完全按照图中所示实现速度控制。该模块通过移除 Velocity Controller 模块并直接接受参考转矩来实现转矩控制。

### 假设

电机参数已知。

### 限制

该控制结构以单一采样率实现。
