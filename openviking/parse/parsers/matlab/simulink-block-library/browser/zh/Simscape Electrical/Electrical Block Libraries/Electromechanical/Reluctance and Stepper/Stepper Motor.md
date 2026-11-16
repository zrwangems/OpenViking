---
type: simulink-block
title: 'Stepper Motor'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Reluctance and Stepper'
documentation_page: 'steppermotor'
documentation_source_path: 'ref/steppermotor.html'
language: zh-CN
chinese_source: worker-translation
---

# Stepper Motor

## 端口

### 守恒

### **A+** — A 相正极端子电气

与 A 相正极端子关联的电气守恒端口。

### **A-** — A 相负极端子电气

与 A 相负极端子关联的电气守恒端口。

### **B+** — B 相正极端子电气

与 B 相正极端子关联的电气守恒端口。

### **B-** — B 相负极端子电气

与 B 相负极端子关联的电气守恒端口。

### **C** — 电机机壳机械旋转

连接到电机机壳的机械旋转守恒端口。

### **R** — 电机转子机械旋转

连接到转子的机械旋转守恒端口。

### **HA** — 绕组 A 热质量热

与绕组 A 的热质量关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HB** — 绕组 B 热质量热

与绕组 B 的热质量关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HR** — 转子热质量热

与转子的热质量关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Selected part** — 预定义参数化选项 `<click to select>`（默认）

用于将模块参数化以表示特定供应商组件的选项。点击 **<click to select>** 超链接以打开 Block Parameterization Manager 窗口。有关 Block Parameterization Manager 的详细信息，请参阅 Load Predefined Parameterizations。

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口并对将功率转换为热量的损耗效应建模。

### 电气转矩

### **Simulation mode** — 仿真模式 `Stepping`（默认）| `Averaged`

仅当该模块直接连接到同样以 `Averaged` 模式运行的 Stepper Motor Driver 模块时，才使用 `Averaged`。

### **Vector of rotational speeds** — 转子转速 `[0, 1000, 3000]` `rpm`（默认）| 正向量

用于定义最大转矩值以进行失步预测的转速向量。

#### 依赖关系

要启用此参数，请将 **Simulation mode** 设置为 `Averaged`。

### **Vector of maximum torque values** — 最大转矩 `[2, 2, 1]` `N*m`（默认）| 正向量

最大转矩值向量，用于结合 **Vector of rotational speeds** 参数进行失步预测。这些值通常在数据手册中给出，并对应于驱动器中指定的电源电压和步进类型（半步或整步）。

#### 依赖关系

要启用此参数，请将 **Simulation mode** 设置为 `Averaged`。

### **Action on slipping** — 失步响应 `none`（默认）| `warn` | `error`

选择模块在仿真期间检测到失步时要执行的操作：

- `none` — 继续仿真，根据 **Vector of maximum torque values** 限制负载转矩。
- `warn` — 继续仿真，根据 **Vector of maximum torque values** 限制负载转矩，并生成转子正在失步的警告。
- `error` — 停止仿真，并生成转子正在失步的错误消息。

如果选择允许仿真继续的操作，仿真结果可能不正确。发生失步时，电机并不总是产生最大转矩。仅当步进控制器检测到失步并相应调整步速率命令时，才会达到最大转矩。

#### 依赖关系

要启用此参数，请将 **Simulation mode** 设置为 `Averaged`。

### **Approximate total load inertia** — 总负载惯量 `1e-4` `kg*m^2`（默认）| 正数

近似总负载惯量，包括转子惯量。该值用于帮助预测由快速加速需求引起的失步。

#### 依赖关系

要启用此参数，请将 **Simulation mode** 设置为 `Averaged`。

### **Maximum step rate command** — 最大命令频率 `10` `Hz`（默认）| 正数

系统的最大命令步速率。它用于确定为步进电机和驱动器近似的二阶系统合适的带宽。

#### 依赖关系

要启用此参数，请将 **Simulation mode** 设置为 `Averaged`。

### **Phase winding resistance** — 相电阻 `0.55` `Ohm`（默认）| 正数

A 相和 B 相绕组的电阻。

#### 依赖关系

要启用此参数，请将 **Simulation mode** 设置为 `Stepping`。

### **Phase winding inductance** — 相电感 `1.5e-3` `Ohm`（默认）| 正数

A 相和 B 相绕组的电感。

#### 依赖关系

要启用此参数，请将 **Simulation mode** 设置为 `Stepping`。

### **Motor torque constant** — 转矩常数 `0.19` `N*m/A`（默认）| 正数

电机转矩常数 *Km*。

#### 依赖关系

要启用此参数，请将 **Simulation mode** 设置为 `Stepping`。

### **Detent torque** — 转矩变化幅值 `0` `N*m`（默认）| 正数

在未通电电机轴旋转时观察到的正弦转矩变化幅值。

#### 依赖关系

要启用此参数，请将 **Simulation mode** 设置为 `Stepping`。

### **Magnetizing resistance** — 相励磁电阻 `inf`（默认）| 严格正数

从每个相绕组看进去的总励磁电阻。该值必须大于零。默认值为 `Inf`，表示没有铁耗。

#### 依赖关系

要启用此参数，请将 **Simulation mode** 设置为 `Stepping`。

### **Full step size** — 步长 `1.8` `deg`（默认）| 正数

改变 A 相或 B 相电流极性时的步长。

该值等于 (π/2)/*Nr*，其中 *Nr* 是两个转子磁极中每个磁极上的齿数。

### 机械

### **Rotor inertia** — 转动惯量 `4.5e-5` `kg*m^2`（默认）| 零或正数

阻碍转子加速度的保守力。

### **Rotor damping** — 转动阻尼 `8.0e-4` `N*m/(rad/s)`（默认）| 零或正数

阻碍转子速度的耗散力。

### **Initial rotor speed** — 初始速度 `0` `rpm`（默认）| 实数

仿真开始时转子的速度。

### **Initial rotor angle** — 初始角度 `0` `rad`（默认）| 实数

仿真开始时转子的角度。

### 温度依赖性

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Resistance temperature coefficients, [alpha\_A alpha\_B]** — 温度系数 `[.00393, .00393]` `1/K`（默认）| 正向量

二元行向量，定义将电阻与温度关联的方程中的系数 α，如 Model Thermal Effects 中所述。第一个元素对应绕组 A，第二个对应绕组 B。默认值适用于铜。

### **Measurement temperature** — 参考温度 `25` `degC`（默认）| 实数

定义电机参数所用的温度。

### 热端口

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Winding thermal masses, [M\_A M\_B]** — 绕组热质量 `[100, 100]` `J/K`（默认）| 正向量

二元行向量，定义 A 和 B 绕组的热质量。热质量是将温度升高一度所需的能量。

### **Winding initial temperatures, [T\_A T\_B]** — 初始绕组温度 `[25, 25]` `degC`（默认）| 实数

二元行向量，定义仿真开始时 A 和 B 热端口的温度。

### **Rotor thermal mass** — 转子热质量 `50` `J/K`（默认）| 正数

转子的热质量，即将转子温度升高一度所需的能量。

### **Rotor initial temperature** — 初始转子温度 `25` `degC`（默认）| 实数

仿真开始时转子的温度。

### **Percentage of magnetizing resistance associated with the rotor** — 励磁电阻转子百分比 `90`（默认）| `0` 到 `100` 之间的正数

与通过转子的磁路关联的励磁电阻百分比。它确定有多少铁耗加热归因于转子热端口 **HR**，以及绕组热端口 **HA** 和 **HB**。

## 所属库

Simscape / Electrical / Electromechanical / Reluctance & Stepper

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

适用于整步、半步和微步进的永磁步进电机

Stepper Motor 模块对步进电机进行建模。步进电机具有永磁转子和两个绕线定子绕组。如果您的步进电机在每个定子绕组上都有中心抽头，请改用 Unipolar Stepper Motor 模块。

小步距的步进电机通常具有带齿的北极和南极转子。大步距的步进电机通常具有沿转子圆周分布的多个磁体。您可以使用 Stepper Motor 模块对两种类型的电机建模，并使用 Stepper Motor Driver 模块驱动电机。

您可以使用步进电机来避免位置测量的需求。您可以将步进电机用于打印机等设备以及机器人和工厂自动化等应用。

Stepper Motor 模块使用输入脉冲序列 `A` 和 `B`，根据以下方程控制机械输出，

eA=−Kmωsin(Nrθ)

eB=Kmωcos(Nrθ)

diAdt=(vA−RiA−eA)/L

diBdt=(vB−RiB−eB)/L

Jdωdt+Bω=Te

Te=−Km(iA−eARm)sin(Nrθ)+Km(iB−eBRm)cos(Nrθ)−Tdsin(4Nrθ)

dθdt=ω

其中：

- *eA* 和 *eB* 分别是 *A* 相和 *B* 相绕组中感应的反电动势（EMF）。
- *iA* 和 *iB* 是 *A* 相和 *B* 相绕组电流。
- *vA* 和 *vB* 是 *A* 相和 *B* 相绕组电压。
- *Km* 是电机转矩常数。
- *Nr* 是两个转子磁极中每个磁极上的齿数。
- *R* 是绕组电阻。
- *L* 是绕组电感。
- *Rm* 是励磁电阻。
- *B* 是转动阻尼。
- *J* 是惯量。
- *ω* 是转子速度。
- *Θ* 是转子角度。
- *Td* 是定位转矩幅值。
- *Te* 是电气转矩。

如果初始转子角度为零或为 (π/2)/*N*r 的倍数，则转子与脉冲 A 的相绕组对齐。当存在从 **A+** 流向 **A-** 端口的正电流，且没有从 **B+** 流向 **B-** 端口的电流时，会发生这种对齐。

使用 Stepper Motor Driver 模块为 Stepper Motor 模块创建脉冲序列。

当脉冲 `A` 的相位超前脉冲 `B` 的相位时，Stepper Motor 模块产生从机械 **C** 端口到 **R** 端口的正转矩。

### Averaged 模式

如果将 **Simulation mode** 参数设置为 `Averaged`，且同时用于 Stepper Motor 模块和控制它的 Stepper Motor Driver 模块，则不会仿真各个步进。这可能是加快仿真的好方法。在 Averaged 模式下，在非失步条件下，电机和驱动器由跟踪指定步速率的二阶线性系统表示。所需步速率直接根据 **A+** 和 **A-** 两端的电压确定。因此，例如，**A+** 和 **A-** 端子两端 +10 V 的电压被解释为每秒 10 步的步速率需求。有关如何将驱动器模块连接到步进角控制器的详细信息，请参阅 Stepper Motor Driver 模块参考页。

Averaged 模式包含失步估计器，用于预测如果以 Stepping 仿真模式运行，步进电机是否会失步。如果电机转矩超过 **Vector of maximum torque values** 参数值的时间长于一个步进周期，则预测为失步，该步进周期根据当前步速率需求确定。检测到失步后，仿真将根据 **Action on slipping** 参数值继续或停止并报错。如果选择允许仿真继续的操作，请注意仿真结果可能不正确。发生失步时，电机产生的转矩通常不是最大可用转矩；仅当步进控制器检测到失步并相应调整步速率命令时，才会达到最大转矩。

等效二阶系统的动态由您为 **Approximate total load inertia** 和 **Maximum step rate command** 参数指定的值确定。将这些参数设置为尽可能准确的值很重要，以便跟踪步速率命令，并且模块不会生成错误的失步警告或错误。

如果在暴露可选热端口的情况下以 Averaged 模式运行电机（请参阅 Model Thermal Effects），则会向热端口添加热量，假设即使步速率命令为零，绕组也始终通电。模块会针对半步进以及较高速度下转矩（和绕组电流）降低进行调整。为了使这些调整正确，**Vector of maximum torque** 参数值必须正确。对于半步进，在零速度下，模块产生的热量是在半步和整步停止时产生的热量的平均值。

要验证预测会发生失步的 Averaged 模式模型配置，请将结果与以 stepping 模式执行的相同仿真进行比较。

### 热效应建模

您可以暴露热端口，以对将功率转换为热量的损耗效应建模。要暴露热端口，请将 **Modeling option** 参数设置为以下任一值：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含多个热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

如果暴露这些端口，则假定绕组电阻与温度线性相关，并由下式给出：

*R* = *R0* (1 +
α (*T* – *T0*
))

其中：

- *R* 是温度 *T* 下的电阻。
- *R0* 是在测量（或参考）温度 *T0* 下的电阻。使用 **Measurement temperature** 参数指定参考温度。
- α 是电阻温度系数，您可以使用 **Resistance temperature coefficients, [alpha\_A alpha\_B]** 参数指定。铜的典型值为 0.00393/K。

模块通过下式计算每个绕组和转子的温度：

MdTdt=Q

其中

- *M* 是热质量。对于绕组，使用 **Winding thermal masses, [M\_A M\_B]** 参数指定该值；对于转子，使用 **Rotor thermal mass** 参数指定。
- *T* 是温度。对于绕组，使用 **Winding initial temperatures, [T\_A T\_B]** 参数指定初始值；对于转子，使用 **Rotor initial temperature** 参数指定。
- *Q* 是热流，根据绕组的铁耗计算：

QA=ia2RA(1−ρm/100)QB=iB2RB(1−ρm/100)QR=QA(ρm/100)+QB(ρm/100)

其中 *ρm* 是与转子关联的励磁电阻百分比。使用 **Percentage of magnetizing resistance associated with the rotor** 参数指定该百分比。

### 预定义参数化

Stepper Motor 模块有多种可用的内置参数化。

这些预参数化数据允许您设置该模块以表示特定的供应商组件。要加载预定义参数化，请双击 Stepper Motor 模块，点击 **Selected part** 参数的 **<click to select>** 超链接，然后在 Block Parameterization Manager 窗口中，从可用组件列表中选择要使用的部件。

**注意**

Simscape™ 组件的预定义参数化使用可用的数据源来获取参数值。对于缺失数据，使用工程判断和简化假设进行补充。因此，预期仿真行为与实际物理行为之间会存在偏差。为确保准确性，请根据实验数据验证仿真行为，并按需细化组件模型。

有关预参数化的更多信息以及可用组件列表，请参阅 List of Pre-Parameterized Components。
