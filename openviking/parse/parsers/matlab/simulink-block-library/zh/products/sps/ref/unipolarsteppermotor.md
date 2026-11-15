---
type: simulink-block
title: 'Unipolar Stepper Motor'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Reluctance and Stepper'
documentation_page: 'unipolarsteppermotor'
documentation_source_path: 'ref/unipolarsteppermotor.html'
language: zh-CN
chinese_source: worker-translation
---

# Unipolar Stepper Motor

## 端口

### 守恒

### **A+** — 顶部 A 相电气连接 electrical

与顶部 A 相电气连接关联的电气守恒端口。

### **A0** — A 相中心抽头连接 electrical

与 A 相中心抽头连接关联的电气守恒端口。

### **A-** — 下部 A 相电气连接 electrical

与下部 A 相电气连接关联的电气守恒端口。

### **B+** — 顶部 B 相电气连接 electrical

与顶部 B 相电气连接关联的电气守恒端口。

### **B0** — B 相中心抽头连接 electrical

与 B 相中心抽头连接关联的电气守恒端口。

### **B-** — 下部 B 相电气连接 electrical

与下部 B 相电气连接关联的电气守恒端口。

### **C** — 机壳 mechanical

与机壳关联的机械旋转守恒端口。

### **R** — 转子 mechanical

与转子关联的机械旋转守恒端口。

### **HA+** — 用于 **A+** 和 **A0** 之间绕组的热端口 thermal

用于 **A+** 和 **A0** 之间绕组的热端口。有关详细信息，请参阅 Model Thermal Effects。

### **HA-** — 用于 **A-** 和 **A0** 之间绕组的热端口 thermal

用于 **A-** 和 **A0** 之间绕组的热端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HB+** — 用于 **B+** 和 **B0** 之间绕组的热端口 thermal

用于 **B+** 和 **B0** 之间绕组的热端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HB-** — 用于 **B-** 和 **B0** 之间绕组的热端口 thermal

用于 **B-** 和 **B** 之间绕组的热端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HR** — 转子热端口 thermal

用于转子的热端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口，并对将功率转换为热量的损耗效应进行建模。

### 电气转矩

### **Simulation mode** — 仿真模式 `Stepping`（默认）| `Averaged`

选择 `Stepping` 或 `Averaged`。仅当该模块直接连接到同样以 Averaged 模式运行的 Unipolar Stepper Motor Driver 模块时，才使用 `Averaged`。

### **Vector of rotational speeds** — 转速向量 `[0, 1000, 3000]` `rpm`（默认）

用于定义最大转矩值以进行失步预测的转速向量。

#### 依赖关系

仅当将 **Simulation mode** 参数设置为 `Averaged` 时，此参数才可见。

### **Vector of maximum torque values** — 最大转矩值向量 `[2, 2, 1]` `N*m`（默认）

最大转矩值向量，与 **Vector of rotational speeds** 参数结合用于失步预测。最大转矩值通常由数据手册给出，并且应与驱动器中指定的电源电压和步进类型（半步或全步）相对应。

#### 依赖关系

仅当将 **Simulation mode** 参数设置为 `Averaged` 时，此参数才可见。

### **Action on slipping** — 检测到失步时的操作 `none`（默认）| `warn` | `error`

选择模块在仿真期间检测到失步时要执行的操作：

- `none` — 继续仿真，并根据 **Vector of maximum torque values** 限制负载转矩。
- `warn` — 继续仿真，并根据 **Vector of maximum torque values** 限制负载转矩，同时生成转子正在失步的警告。
- `error` — 停止仿真，并生成转子正在失步的错误消息。

请注意，如果您选择允许仿真继续的操作，仿真结果可能会不正确：发生失步时，电机产生的转矩通常不会是最大可用转矩；仅当步进控制器检测到失步并相应地调整步进速率命令时，才会达到最大转矩。

#### 依赖关系

仅当将 **Simulation mode** 参数设置为 `Averaged` 时，此参数才可见。

### **Approximate total load inertia** — 近似总负载惯量 `1e-4` `kg*m^2`（默认）

近似总负载惯量，包括转子惯量。此值用于帮助预测何时会因快速加速需求而发生失步。

#### 依赖关系

仅当将 **Simulation mode** 参数设置为 `Averaged` 时，此参数才可见。

### **Maximum step rate command** — 最大步进速率命令 `10` `Hz`（默认）

系统将命令的最大步进速率。它用于确定为步进电机和驱动器确定二阶系统近似合适的带宽。

#### 依赖关系

仅当将 **Simulation mode** 参数设置为 `Averaged` 时，此参数才可见。

### **Half-winding resistance** — 半绕组电阻 `0.55` `Ohm`（默认）

A 相和 B 相绕组的电阻的一半，在 **A+** 和 **A-** 以及 **B+** 和 **B-** 端口之间测量。

#### 依赖关系

仅当将 **Simulation mode** 参数设置为 `Stepping` 时，此参数才可见。

### **Half-winding inductance** — 半绕组电感 `1.5e-3` `H`（默认）

A 相和 B 相绕组的电感的一半，在 **A+** 和 **A-** 以及 **B+** 和 **B-** 端口之间测量。

#### 依赖关系

仅当将 **Simulation mode** 参数设置为 `Stepping` 时，此参数才可见。

### **Motor torque constant** — 电机转矩常数 `0.19` `N*m/A`（默认）

电机转矩常数 *Km*。

#### 依赖关系

仅当将 **Simulation mode** 参数设置为 `Stepping` 时，此参数才可见。

### **Detent torque** — 定位转矩 `0` `N*m`（默认）

断电电机旋转轴时观察到的正弦转矩变化的幅值。

#### 依赖关系

仅当将 **Simulation mode** 参数设置为 `Stepping` 时，此参数才可见。

### **Magnetizing resistance** — 磁化电阻 `inf` `Ohm`（默认）| 正标量

从每个相绕组看进去的总磁化电阻，例如跨 **A+** 和 **A0**。该值必须大于零。默认值为 `Inf`，表示没有铁耗。

#### 依赖关系

仅当将 **Simulation mode** 参数设置为 `Stepping` 时，此参数才可见。

### **Full step size** — 全步长 `1.8` `deg`（默认）

改变 A 相或 B 相电流极性时的步长。

此值等于 (π/2)/*Nr*，其中 *Nr* 是两个转子磁极各自的齿数。

### **Coefficient of coupling** — 互感耦合系数 `0`（默认）

绕组用于互感的耦合系数。

### 机械

### **Rotor inertia** — 转子惯量 `4.5e-5` `kg*m^2`（默认）

转子对电机运动变化的阻力。该值可以为零。

### **Rotor damping** — 转子阻尼 `8.0e-4` `N*m/(rad/s)`（默认）

转子耗散的能量。该值可以为零。

### **Initial rotor speed** — 初始转子速度 `0` `rpm`（默认）

仿真开始时转子的速度。

### **Initial rotor angle** — 初始转子角度 `0` `deg`（默认）

仿真开始时转子的角度。

### 温度依赖性

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Resistance temperature coefficient** — 电阻温度系数 `3.93e-3` `1/K`（默认）

将电阻定义为温度函数的方程中的参数 α，如 Thermal Model for Actuator Blocks 中所述。假定所有绕组由相同材料制成，因此具有相同的电阻温度系数。

#### 依赖关系

仅当将 **电气转矩** 设置中的 **Simulation mode** 参数设置为 `Stepping` 时，此参数才可见。

### **Measurement temperature** — 测量温度 `25` `degC`（默认）

定义电机参数时的温度。

### **Vector of maximum torque values at second measurement temperature** — 第二测量温度下的最大转矩值向量 `[1.7, 1.7, .85]` `N*m`（默认）

第二测量温度下的最大转矩值向量。

#### 依赖关系

仅当将 **电气转矩** 设置中的 **Simulation mode** 参数设置为 `Averaged` 时，此参数才可见。

### **Second measurement temperature** — 第二测量温度 `125` `degC`（默认）

第二测量温度。

#### 依赖关系

仅当将 **电气转矩** 设置中的 **Simulation mode** 参数设置为 `Averaged` 时，此参数才可见。

### **Stepping mode** — 步进模式 `Full stepping`（默认）| `Half stepping`

指定步进模式。

#### 依赖关系

仅当将 **电气转矩** 设置中的 **Simulation mode** 参数设置为 `Averaged` 时，此参数才可见。

### 热端口

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Half-winding thermal mass** — 半绕组热质量 `100` `J/K`（默认）

半 A 绕组或半 B 绕组的热质量。热质量是将温度升高一度所需的能量。假定所有四个半绕组具有相同的热质量。

### **Half-winding initial temperatures, [T\_A+ T\_A- T\_B+ T\_B-]** — 半绕组初始温度 `[25, 25, 25, 25]` `degC`（默认）

定义仿真开始时四个半绕组温度的 1×4 行向量。

### **Rotor thermal mass** — 转子热质量 `50` `J/K`（默认）

转子的热质量，即将转子温度升高一度所需的能量。

### **Rotor initial temperature** — 转子初始温度 `25` `degC`（默认）

仿真开始时转子的温度。

### **Percentage of magnetizing resistance associated with the rotor** — 与转子相关联的磁化电阻百分比 `90`（默认）

与通过转子的磁路相关联的磁化电阻百分比。它决定了铁耗发热中有多少归属于转子热端口 HR，以及有多少归属于四个绕组热端口。

## 所属库

Simscape / Electrical / Electromechanical / Reluctance & Stepper

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

## 描述

每个绕组上均带有中心抽头的永磁步进电机

Unipolar Stepper Motor 模块对单极步进电机进行建模。单极步进电机具有永磁转子和两个带中心抽头的绕线定子绕组。中心抽头简化了步进驱动器设计，因为驱动器输出的极性不需要改变。如果您的电机在每个定子绕组上没有中心抽头，请改用 Stepper Motor 模块。

小步距的步进电机通常具有带齿的北极和南极转子。大步距的步进电机通常在转子圆周上分布有多个磁体。您可以使用 Unipolar Stepper Motor 模块对这两种类型的电机进行建模，并使用 Unipolar Stepper Motor Driver 模块驱动电机。

您可以使用步进电机来避免进行位置测量。您可以在打印机等设备以及机器人和工厂自动化等应用中使用步进电机。

以下方程定义绕组电流和机械输出，

eA+=−Kmωsin(Nrθ)

eA−=Kmωsin(Nrθ)

eB+=Kmωcos(Nrθ)

eB−=−Kmωcos(Nrθ)

diA+dt=(vA+−RiA+−eA+)/L

diA−dt=(vA−−RiA−−eA−)/L

diB+dt=(vB+−RiB+−eB+)/L

diB−dt=(vB−−RiB−−eB−)/L

Jdωdt+Bω=Te

Te=−Km(iA+−iA−−eA+−eA−Rm)sin(Nrθ)+Km(iB+−iB−−eB+−eB−Rm)cos(Nrθ)−Tdsin(4Nrθ)

dθdt=ω

其中：

- *eA+* 是在 **A+** 到 **A0** 半绕组上感应的反电动势 (EMF)。
- *eA-* 是在 **A-** 到 **A0** 半绕组上感应的反电动势 (EMF)。
- *eB+* 是在 **B+** 到 **B0** 半绕组上感应的反电动势 (EMF)。
- *eB-* 是在 **B-** 到 **B0** 半绕组上感应的反电动势 (EMF)。
- *iA+* 是从 **A+** 端口流向 **A0** 中心抽头端口的电流。
- *iA-* 是从 **A-** 端口流向 **A0** 中心抽头端口的电流。
- *iB+* 是从 **B+** 端口流向 **B0** 中心抽头端口的电流。
- *iB-* 是从 **B-** 端口流向 **B0** 中心抽头端口的电流。
- *vA+* 是 **A+** 端口相对于 **A0** 中心抽头端口的电压。
- *vA-* 是 **A-** 端口相对于 **A0** 中心抽头端口的电压。
- *vB+* 是 **B+** 端口相对于 **B0** 中心抽头端口的电压。
- *vB-* 是 **B-** 端口相对于 **B0** 中心抽头端口的电压。
- *Km* 是电机转矩常数。
- *Nr* 是两个转子磁极各自的齿数。
- *R* 是半绕组电阻。例如，它是 **A+** 和 **A0** 端口之间的电阻。
- *L* 是半绕组电感。例如，它是 **A+** 和 **A0** 端口之间的电感。
- *R*m 是磁化电阻。
- *B* 是旋转阻尼。
- *J* 是惯性。
- *ω* 是转子速度。
- *Θ* 是转子角度。
- *Td* 是定位转矩幅值。
- *Te* 是电气转矩。

如果初始转子角度为零或 (π/2)/*N*r 的倍数，则转子与 A 相绕组对齐。如果正电流从 **A+** 端口流向 **A0** 中心抽头端口，则步进电机的作用是保持与 A 相对齐。等效地，正电流从 **A0** 中心抽头端口流向 **A-** 端口也会作用于转子以保持与 A 相对齐。

对于此表中列出的四个序列，Unipolar Stepper Motor 模块会产生从机械 **C** 端口作用到 **R** 端口的正转矩。这些序列假定转子初始角度为零或 (π/2)/*N*r 的倍数。

| 序列 | 中心抽头连接到地 | 中心抽头连接到正电源 |
| --- | --- | --- |
| 1 | 从 **A+** 到 **A0** 的正电流 | 从 **A0** 到 **A-** 的正电流 |
| 2 | 从 **B+** 到 **B0** 的正电流 | 从 **B0** 到 **B-** 的正电流 |
| 3 | 从 **A-** 到 **A0** 的正电流 | 从 **A0** 到 **A-** 的正电流 |
| 4 | 从 **B-** 到 **B0** 的正电流 | 从 **B0** 到 **B-** 的正电流 |

### Averaged 模式

如果将 **Simulation mode** 参数设置为 `Averaged`，并且对 Unipolar Stepper Motor 模块以及控制它的 Unipolar Stepper Motor Driver 模块都如此设置，则不会仿真各个步。这可能是加快仿真速度的好方法。在 Averaged 模式下，在非失步条件下，电机和驱动器由跟踪指定步进速率的二阶线性系统表示。所需步进速率直接根据 **A+** 和 **A-** 两端的电压确定。因此，例如，**A+** 和 **A-** 端子两端的 +10V 电压会被解释为 ten steps per second 的步进速率需求。有关如何将 Unipolar Stepper Motor Driver 连接到步进角控制器的更多信息，请参见 Unipolar Stepper Motor Driver 参考页。

Averaged 模式包含一个失步估计器，用于预测步进电机如果在 Stepping 仿真模式下运行是否会失步。如果电机转矩超过 **Vector of maximum torque values** 参数值的时间长于一个步进周期，则预测为失步；该步进周期根据当前步进速率需求确定。检测到失步后，根据 **Action on slipping** 参数值，仿真将继续进行或因错误而停止。如果选择让仿真继续的操作，请注意仿真结果可能不正确：发生失步时，电机产生的转矩通常不会是最大可用转矩；只有在步进控制器检测到失步并相应地调整步进速率命令时，才会达到最大转矩。

等效二阶系统的动态特性由您为 **Approximate total load inertia** 和 **Maximum step rate command** 参数指定的值确定。请务必为这些参数设置尽可能准确的值，以便跟踪步进速率命令，并且该模块不会生成错误的失步警告或错误。

如果在暴露可选热端口的情况下以 Averaged 模式运行电机（参见热效应建模），则会向热端口添加热量，并假定绕组始终通电，即使步进速率命令为零。该模块会针对半步进以及较高速度下转矩（和绕组电流）减小的情况进行调整。为使这些调整正确，**Vector of maximum torque** 参数值必须正确。对于半步进，在零速时，该模块生成的热量是在半步位置和整步位置停止时生成热量的平均值。

如果要仿真或预测失步，请在使用平均模型表示进行仿真研究之前，先进行一些验证运行，比较 Stepping 和 Averaged 模式。

### 热效应建模

您可以暴露热端口，以对将功率转换为热量的损耗效应建模。要暴露热端口，请将 **Modeling option** 参数设置为以下任一项：

- `No thermal port` — 该模块不包含热端口。
- `Show thermal port` — 该模块包含多个热守恒端口。

有关在致动器模块中使用热端口的详细信息，请参见 Simulating Thermal Effects in Rotational and Translational Actuators。
