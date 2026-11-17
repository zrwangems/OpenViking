---
type: simulink-block
title: 'Unipolar Stepper Motor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Reluctance & Stepper'
documentation_page: 'unipolarsteppermotor'
documentation_source_path: 'ref/unipolarsteppermotor.html'
language: zh-CN
chinese_source: worker-translation
---

# Unipolar Stepper Motor

## 端口

### 守恒端口

### **A+** — A 相顶部电气连接 electrical

与 A 相顶部电气连接相关联的电气守恒端口。

### **A0** — A 相中心抽头连接 electrical

与 A 相中心抽头连接相关联的电气守恒端口。

### **A-** — A 相下部电气连接 electrical

与 A 相下部电气连接相关联的电气守恒端口。

### **B+** — B 相顶部电气连接 electrical

与 B 相顶部电气连接相关联的电气守恒端口。

### **B0** — B 相中心抽头连接 electrical

与 B 相中心抽头连接相关联的电气守恒端口。

### **B-** — B 相下部电气连接 electrical

与 B 相下部电气连接相关联的电气守恒端口。

### **C** — 外壳 mechanical

与外壳相关联的机械旋转守恒端口。

### **R** — 转子 mechanical

与转子相关联的机械旋转守恒端口。

### **HA+** — A+ 与 A0 之间绕组的热端口 thermal

**A+** 与 **A0** 之间绕组的热端口。有关详细信息，请参阅 Model Thermal Effects。

### **HA-** — A- 与 A0 之间绕组的热端口 thermal

**A-** 与 **A0** 之间绕组的热端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HB+** — B+ 与 B0 之间绕组的热端口 thermal

**B+** 与 **B0** 之间绕组的热端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HB-** — B- 与 B0 之间绕组的热端口 thermal

**B-** 与 **B** 之间绕组的热端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HR** — 转子热端口 thermal

转子的热端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口，并对将功率转换为热量的损耗效应进行建模。

### Electrical Torque

### **Simulation mode** — 仿真模式 `Stepping`（默认）| `Averaged`

选择 `Stepping` 或 `Averaged`。仅当模块直接连接到同样以 Averaged 模式运行的 Unipolar Stepper Motor Driver 模块时，才使用 `Averaged`。

### **Vector of rotational speeds** — 转速向量 `[0, 1000, 3000]` `rpm`（默认）

用于定义最大转矩值以进行失步预测的转速向量。

#### 依赖关系

仅当将 **Simulation mode** 参数设置为 `Averaged` 时，此参数才可见。

### **Vector of maximum torque values** — 最大转矩值向量 `[2, 2, 1]` `N*m`（默认）

用于结合 **Vector of rotational speeds** 参数进行失步预测的最大转矩值向量。最大转矩值通常由数据手册给出，并且应与驱动器中指定的电源电压和步进类型（半步或整步）相对应。

#### 依赖关系

仅当将 **Simulation mode** 参数设置为 `Averaged` 时，此参数才可见。

### **Action on slipping** — 检测到失步时的操作 `none`（默认）| `warn` | `error`

选择模块在仿真期间检测到失步时要执行的操作：

- `none` — 继续仿真，根据 **Vector of maximum torque values** 限制负载转矩。
- `warn` — 继续仿真，根据 **Vector of maximum torque values** 限制负载转矩，并生成转子正在失步的警告。
- `error` — 停止仿真，并生成转子正在失步的错误消息。

请注意，如果选择允许仿真继续的操作，仿真结果可能不正确：发生失步时，电机产生的转矩通常不是最大可用转矩；只有在步进控制器检测到失步并相应调整步进速率命令时，才能达到最大转矩。

#### 依赖关系

仅当将 **Simulation mode** 参数设置为 `Averaged` 时，此参数才可见。

### **Approximate total load inertia** — 近似总负载惯量 `1e-4` `kg*m^2`（默认）

近似总负载惯量，包括转子惯量。此值用于帮助预测由于快速加速需求而何时会发生失步。

#### 依赖关系

仅当将 **Simulation mode** 参数设置为 `Averaged` 时，此参数才可见。

### **Maximum step rate command** — 最大步进速率命令 `10` `Hz`（默认）

系统将命令的最大步进速率。它用于确定为步进电机和驱动器建立合适的二阶系统近似带宽。

#### 依赖关系

仅当将 **Simulation mode** 参数设置为 `Averaged` 时，此参数才可见。

### **Half-winding resistance** — 半绕组电阻 `0.55` `Ohm`（默认）

在 **A+** 与 **A-** 以及 **B+** 与 **B-** 端口之间测得的 A 相和 B 相绕组电阻的一半。

#### 依赖关系

仅当将 **Simulation mode** 参数设置为 `Stepping` 时，此参数才可见。

### **Half-winding inductance** — 半绕组电感 `1.5e-3` `H`（默认）

在 **A+** 与 **A-** 以及 **B+** 与 **B-** 端口之间测得的 A 相和 B 相绕组电感的一半。

#### 依赖关系

仅当将 **Simulation mode** 参数设置为 `Stepping` 时，此参数才可见。

### **Motor torque constant** — 电机转矩常数 `0.19` `N*m/A`（默认）

电机转矩常数 *Km*。

#### 依赖关系

仅当将 **Simulation mode** 参数设置为 `Stepping` 时，此参数才可见。

### **Detent torque** — 定位转矩 `0` `N*m`（默认）

旋转未通电电机轴时观察到的正弦转矩变化的幅值。

#### 依赖关系

仅当将 **Simulation mode** 参数设置为 `Stepping` 时，此参数才可见。

### **Magnetizing resistance** — 磁化电阻 `inf` `Ohm`（默认）| 正标量

从每个相绕组看到的磁化电阻总和，例如跨 **A+** 和 **A0**。该值必须大于零。默认值为 `Inf`，表示没有铁损。

#### 依赖关系

仅当将 **Simulation mode** 参数设置为 `Stepping` 时，此参数才可见。

### **Full step size** — 整步步长 `1.8` `deg`（默认）

改变 A 相或 B 相电流极性时的步长。

此值等于 (π/2)/*Nr*，其中 *Nr* 是两个转子磁极中每个磁极上的齿数。

### **Coefficient of coupling** — 互感耦合系数 `0`（默认）

用于互感的绕组耦合系数。

### Mechanical

### **Rotor inertia** — 转子惯量 `4.5e-5` `kg*m^2`（默认）

转子对电机运动变化的阻力。该值可以为零。

### **Rotor damping** — 转子阻尼 `8.0e-4` `N*m/(rad/s)`（默认）

转子耗散的能量。该值可以为零。

### **Initial rotor speed** — 初始转子速度 `0` `rpm`（默认）

仿真开始时转子的速度。

### **Initial rotor angle** — 初始转子角度 `0` `deg`（默认）

仿真开始时转子的角度。

### Temperature Dependence

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Resistance temperature coefficient** — 电阻温度系数 `3.93e-3` `1/K`（默认）

将电阻定义为温度函数的方程中的参数 α，如 Thermal Model for Actuator Blocks 中所述。假设所有绕组由相同材料制成，因此具有相同的电阻温度系数。

#### 依赖关系

仅当将 **Electrical Torque** 设置中的 **Simulation mode** 参数设置为 `Stepping` 时，此参数才可见。

### **Measurement temperature** — 测量温度 `25` `degC`（默认）

定义电机参数时的温度。

### **Vector of maximum torque values at second measurement temperature** — 第二测量温度下的最大转矩值向量 `[1.7, 1.7, .85]` `N*m`（默认）

第二测量温度下的最大转矩值向量。

#### 依赖关系

仅当将 **Electrical Torque** 设置中的 **Simulation mode** 参数设置为 `Averaged` 时，此参数才可见。

### **Second measurement temperature** — 第二测量温度 `125` `degC`（默认）

第二测量温度。

#### 依赖关系

仅当将 **Electrical Torque** 设置中的 **Simulation mode** 参数设置为 `Averaged` 时，此参数才可见。

### **Stepping mode** — 步进模式 `Full stepping`（默认）| `Half stepping`

指定步进模式。

#### 依赖关系

仅当将 **Electrical Torque** 设置中的 **Simulation mode** 参数设置为 `Averaged` 时，此参数才可见。

### Thermal Port

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Half-winding thermal mass** — 半绕组热质量 `100` `J/K`（默认）

A 绕组或 B 绕组一半的热质量。热质量是将温度升高一度所需的能量。假设所有四个半绕组具有相同的热质量。

### **Half-winding initial temperatures, [T\_A+ T\_A- T\_B+ T\_B-]** — 半绕组初始温度 `[25, 25, 25, 25]` `degC`（默认）

一个 1×4 行向量，定义仿真开始时四个半绕组的温度。

### **Rotor thermal mass** — 转子热质量 `50` `J/K`（默认）

转子的热质量，即将转子温度升高一度所需的能量。

### **Rotor initial temperature** — 转子初始温度 `25` `degC`（默认）

仿真开始时转子的温度。

### **Percentage of magnetizing resistance associated with the rotor** — 与转子相关联的磁化电阻百分比 `90`（默认）

与通过转子的磁路相关联的磁化电阻百分比。它决定了铁损发热中有多少归因于转子热端口 HR，以及多少归因于四个绕组热端口。

## 所属库

Simscape / Electrical / Electromechanical / Reluctance & Stepper

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

## 描述

永磁步进电机，两个绕组各带中心抽头

Unipolar Stepper Motor 模块对单极步进电机进行建模。单极步进电机具有永磁转子和两个带中心抽头的绕线定子绕组。中心抽头简化了步进驱动器设计，因为驱动器输出的极性无需改变。如果您的电机在每个定子绕组上没有中心抽头，请改用 Stepper Motor 模块。

步长较小的步进电机通常具有带齿的北极和南极转子。步长较大的步进电机通常具有沿转子圆周分布的多个磁体。您可以使用 Unipolar Stepper Motor 模块对这两种类型的电机进行建模，并使用 Unipolar Stepper Motor Driver 模块驱动电机。

您可以使用步进电机来避免进行位置测量的需要。您可以在打印机等设备以及机器人和工厂自动化等应用中使用步进电机。

这些方程定义了绕组电流和机械输出，

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
- *eA-* 是在 **A-** 到 **A0** 半绕组上感应的反电动势。
- *eB+* 是在 **B+** 到 **B0** 半绕组上感应的反电动势。
- *eB-* 是在 **B-** 到 **B0** 半绕组上感应的反电动势。
- *iA+* 是从 **A+** 端口流向 **A0** 中心抽头端口的电流。
- *iA-* 是从 **A-** 端口流向 **A0** 中心抽头端口的电流。
- *iB+* 是从 **B+** 端口流向 **B0** 中心抽头端口的电流。
- *iB-* 是从 **B-** 端口流向 **B0** 中心抽头端口的电流。
- *vA+* 是 **A+** 端口相对于 **A0** 中心抽头端口的电压。
- *vA-* 是 **A-** 端口相对于 **A0** 中心抽头端口的电压。
- *vB+* 是 **B+** 端口相对于 **B0** 中心抽头端口的电压。
- *vB-* 是 **B-** 端口相对于 **B0** 中心抽头端口的电压。
- *Km* 是电机转矩常数。
- *Nr* 是两个转子磁极中每个磁极上的齿数。
- *R* 是半绕组电阻。例如，它是 **A+** 与 **A0** 端口之间的电阻。
- *L* 是半绕组电感。例如，它是 **A+** 与 **A0** 端口之间的电感。
- *R*m 是磁化电阻。
- *B* 是旋转阻尼。
- *J* 是惯量。
- *ω* 是转子速度。
- *Θ* 是转子角度。
- *Td* 是定位转矩幅值。
- *Te* 是电磁转矩。

如果初始转子角度为零或为 (π/2)/*N*r 的倍数，则转子与 A 相绕组对齐。如果正电流从 **A+** 端口流向 **A0** 中心抽头端口，则步进电机的作用是保持与 A 相对齐。等效地，正电流从 **A0** 中心抽头端口流向 **A-** 端口也会作用于转子以保持与 A 相对齐。

对于下表列出的四种序列，Unipolar Stepper Motor 模块产生从机械 **C** 端口到 **R** 端口的正转矩。这些序列假设转子初始角度为零或为 (π/2)/*N*r 的倍数。

| 序列 | 中心抽头接地 | 中心抽头接正电源 |
| --- | --- | --- |
| 1 | 正电流从 **A+** 流向 **A0** | 正电流从 **A0** 流向 **A-** |
| 2 | 正电流从 **B+** 流向 **B0** | 正电流从 **B0** 流向 **B-** |
| 3 | 正电流从 **A-** 流向 **A0** | 正电流从 **A0** 流向 **A-** |
| 4 | 正电流从 **B-** 流向 **B0** | 正电流从 **B0** 流向 **B-** |

### 平均模式

如果将 **Simulation mode** 参数设置为 `Averaged`，无论是对于单极性步进电机模块还是控制它的单极性步进电机驱动器模块，都不会模拟各个步进。这可能是加速仿真的一种好方法。在平均模式下，在非滑移条件下，电机和驱动器由跟踪指定步进速率的二阶线性系统表示。所需步进速率直接由 **A+** 和 **A-** 两端的电压确定。因此，例如，**A+** 和 **A-** 端子两端的 +10V 电压被解释为每秒十步的步进速率需求。有关如何将单极性步进电机驱动器连接到您的步进角控制器的更多信息，请参阅单极性步进电机驱动器参考页。

平均模式包含一个滑移估计器，用于预测步进电机如果在步进仿真模式下运行是否会发生滑移。如果电机转矩超过 **Vector of maximum torque values** 参数值的时间超过一个步进周期，则预测发生滑移，步进周期由当前步进速率需求确定。检测到滑移后，仿真将根据 **Action on slipping** 参数值继续运行或停止并报错。如果选择让仿真继续的操作，请注意仿真结果可能不正确：发生滑移时，电机产生的转矩通常不是最大可用转矩；只有在步进控制器检测到滑移并相应调整步进速率命令时，才能达到最大转矩。

等效二阶系统的动态特性由您为 **Approximate total load inertia** 和 **Maximum step rate command** 参数指定的值确定。将这些参数设置为尽可能准确的值非常重要，以便跟踪步进速率命令，并且模块不会生成错误的滑移警告或错误。

如果在暴露可选热端口的情况下以平均模式运行电机（请参阅建模热效应），则假设绕组始终通电，即使步进速率命令为零，也会向热端口添加热量。模块会针对半步进以及较高速度下转矩（和绕组电流）降低进行调整。为了使这些调整正确，**Vector of maximum torque** 参数值必须正确。对于半步进，在零速度下，模块产生的热量是在半步和整步停止时产生热量的平均值。

如果您模拟或预测滑移，请在使用平均模型表示进行仿真研究之前，进行一些验证运行，比较步进模式和平均模式。

### 建模热效应

您可以暴露热端口来建模将功率转换为热量的损耗效应。要暴露热端口，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含多个热守恒端口。

有关在执行器模块中使用热端口的更多信息，请参阅模拟旋转和平移执行器中的热效应。
