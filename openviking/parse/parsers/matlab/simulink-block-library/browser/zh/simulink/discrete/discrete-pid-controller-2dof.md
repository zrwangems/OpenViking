---
type: simulink-block
title: 'Discrete PID Controller (2DOF)'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Control System Design and Tuning / PID Controller Tuning / Model-Based PID Controller Tuning'
documentation_page: 'discretepidcontroller2dof'
documentation_source_path: '../simulink/slref/discretepidcontroller2dof.html'
language: zh-CN
chinese_source: worker-translation
---

# Discrete PID Controller (2DOF)

## 端口

### 输入

### **Ref** — 参考信号 标量 | 向量

被控对象要跟踪的参考信号，如下所示。

当参考信号是向量时，模块会分别对每个信号执行操作，将 PID 系数向量化，并产生维度相同的向量输出信号。您可以将 PID 系数和其他一些参数指定为与输入信号维度相同的向量。这样做等效于为输入信号中的每个条目指定一个单独的 PID 控制器。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_1( y )** — 测量的系统输出 标量 | 向量

来自被控对象输出的控制器反馈信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **ydot** — 外部提供的导数 标量 | 向量

*自 R2024a 起*

直接将被控对象信号 *y* 的导数作为模块输入提供。当您的模型中已有该导数信号，并且希望跳过模块内部的导数计算时，这很有帮助。

#### 依赖关系

要启用此输入端口，请选择一个具有微分作用的控制器类型，并启用 **Use externally sourced derivative**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **P** — 比例增益 标量 | 向量

比例增益，从模块外部源提供。外部增益输入很有用，例如，当您想将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部增益输入来实现增益调度 PID 控制。在增益调度控制中，您通过模型中的逻辑或其他计算确定 PID 系数，并将它们馈送到模块。

#### 依赖关系

要启用此端口，请将 **Controller parameters Source** 设置为 `external`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **I** — 积分增益 标量 | 向量

积分增益，从模块外部源提供。外部增益输入很有用，例如，当您想将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部增益输入来实现增益调度 PID 控制。在增益调度控制中，您通过模型中的逻辑或其他计算确定 PID 系数，并将它们馈送到模块。

当您从外部提供增益时，积分增益随时间的变化也会被积分。出现此结果是因为 PID 增益在模块内部的实现方式。有关详细信息，请参阅 **Controller parameters Source** 参数。

#### 依赖关系

要启用此端口，请将 **Controller parameters Source** 设置为 `external`，并将 **Controller** 设置为具有积分作用的控制器类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **I\*Ts** — 积分增益乘以采样时间 标量 | 向量

对于离散时间控制器，积分增益乘以控制器采样时间，从模块外部源提供。外部增益输入很有用，例如，当您想将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部增益输入来实现增益调度 PID 控制。在增益调度控制中，您通过模型中的逻辑或其他计算确定 PID 系数，并将它们馈送到模块。

**注意**

PID 整定工具（例如 PID Tuner app 和 Closed-Loop PID Autotuner block）整定增益 **I**，而不是 **I\*Ts**。因此，在将此端口提供的值写入之前，请将您从整定工具获得的积分增益值乘以采样时间。

当您使用 **I\*Ts** 而不是 **I** 时，模块执行积分所需的计算更少。这会改善生成代码的执行时间。

对于连续时间控制器，请禁用 **Use I\*Ts**，并改用 **I** 端口。

#### 依赖关系

要启用此端口，请将 **Controller parameters Source** 设置为 `external`，将 **Controller** 设置为具有积分作用的控制器类型，并启用 **Use I\*Ts** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **D** — 微分增益 标量 | 向量

微分增益，从模块外部源提供。外部增益输入很有用，例如，当您想将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部增益输入来实现增益调度 PID 控制。在增益调度控制中，您通过模型中的逻辑或其他计算确定 PID 系数，并将它们馈送到模块。

当您从外部提供增益时，微分增益随时间的变化也会被微分。出现此结果是因为 PID 增益在模块内部的实现方式。有关详细信息，请参阅 **Controller parameters Source** 参数。

#### 依赖关系

要启用此端口，请将 **Controller parameters Source** 设置为 `external`，并将 **Controller** 设置为具有微分作用的控制器类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **N** — 滤波器系数 标量 | 向量

微分滤波器系数，从模块外部源提供。外部系数输入很有用，例如，当您想将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部输入来实现增益调度 PID 控制。在增益调度控制中，您通过模型中的逻辑或其他计算确定 PID 系数，并将它们馈送到模块。

#### 依赖关系

要启用此端口，请将 **Controller parameters Source** 设置为 `external`，并将 **Controller** 设置为具有滤波微分作用的控制器类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **b** — 比例设定点权重 标量 | 向量

比例设定点权重，从模块外部源提供。外部输入很有用，例如，当您想将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部输入来实现增益调度 PID 控制。在增益调度控制中，您通过模型中的逻辑或其他计算确定 PID 系数，并将它们馈送到模块。

#### 依赖关系

要启用此端口，请将 **Controller parameters Source** 设置为 `external`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **c** — 微分设定点权重 标量 | 向量

微分设定点权重，从模块外部源提供。外部输入很有用，例如，当您想将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部输入来实现增益调度 PID 控制。在增益调度控制中，您通过模型中的逻辑或其他计算确定 PID 系数，并将它们馈送到模块。

#### 依赖关系

要启用此端口，请将 **Controller parameters Source** 设置为 `external`，并将 **Controller** 设置为具有微分作用的控制器类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Reset** — 外部复位触发 标量

用于将积分器和滤波器复位到初始条件的触发。使用 **External reset** 参数指定何种信号触发复位。端口图标指示该参数中指定的触发类型。例如，下图显示了一个连续时间 PID Controller (2DOF) 模块，其 **External reset** 设置为 `rising`。

当触发发生时，模块会将积分器和滤波器复位到由 **Integrator Initial condition** 和 **Filter Initial condition** 参数或 **I0** 和 **D0** 端口指定的初始条件。

**注意**

为了符合 Motor Industry Software Reliability Association (MISRA™) 软件标准，您的模型必须使用 Boolean 信号来驱动 PID 控制器模块的外部复位端口。

#### 依赖关系

要启用此端口，请将 **External reset** 设置为除 `none` 以外的任何值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `Boolean`

### **I0** — 积分器初始条件 标量 | 向量

积分器初始条件，从模块外部源提供。

#### 依赖关系

要启用此端口，请将 **Initial conditions Source** 设置为 `external`，并将 **Controller** 设置为具有积分作用的控制器类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **D0** — 滤波器初始条件 标量 | 向量

微分滤波器的初始条件，从模块外部源提供。

#### 依赖关系

要启用此端口，请将 **Initial conditions Source** 设置为 `external`，并将 **Controller** 设置为具有微分作用的控制器类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **up** — 输出饱和上限 标量 | 向量

模块输出的上限，从模块外部源提供。如果比例、积分和微分作用的加权和超过此端口提供的值，则模块输出保持在该值。

#### 依赖关系

要启用此端口，请选择 **Limit output**，并将输出饱和 **Source** 设置为 `external`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **lo** — 输出饱和下限 标量 | 向量

模块输出的下限，从模块外部源提供。如果比例、积分和微分作用的加权和低于此端口提供的值，则模块输出保持在该值。

#### 依赖关系

要启用此端口，请选择 **Limit output**，并将输出饱和 **Source** 设置为 `external`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **TR** — 跟踪信号 标量 | 向量

控制器输出要跟踪的信号。当信号跟踪处于活动状态时，跟踪信号与模块输出之间的差值会以增益反馈到积分器输入。信号跟踪对于在在两个控制器之间切换的系统中实现无扰控制传递很有用。它还可用于防止多回路控制系统中的模块饱和。有关详细信息，请参阅 **Enable tracking mode** 参数。

#### 依赖关系

要启用此端口，请选择 **Enable tracking mode** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **TDTI** — 离散积分器时间 标量

离散积分器时间，作为标量提供给模块。您可以使用自己的离散时间积分器采样时间值，该值定义模块将在 Simulink 中或在外部硬件上运行时的速率。当模块用于条件执行子系统内部时，离散时间积分器时间的值应与外部中断的平均采样率匹配。

换句话说，您可以为下面任一积分器方法指定 `Ts`，使其值与外部中断的平均采样率匹配。在离散时间中，控制器传递函数的微分项为：

D[N1+Nα(z)]，

其中 *α*(*z*) 取决于您使用此参数指定的积分器方法。

`Forward Euler`
:   α(z)=Tsz−1。

`Backward Euler`
:   α(z)=Tszz−1。

`Trapezoidal`
:   α(z)=Ts2z+1z−1。

有关离散时间积分的详细信息，请参阅 Discrete-Time Integrator 模块参考页。有关条件执行子系统的详细信息，请参阅 Conditionally Executed Subsystems Overview。

#### 依赖关系

要启用此端口，请将 **Time Domain** 设置为 `Discrete-time`，并选择 **PID Controller is inside a conditionally executed subsystem** 选项。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **extAW** — 外部抗饱和算法 标量 | 向量

*自 R2024b 起*

在此端口指定自定义抗饱和算法。模块提供两种内置抗饱和方法，但是，为了解开积分器，这些方法依赖于模块分量之和超过指定的模块输出限值。如果您的应用在 PID 控制器模块下游具有饱和或限值，您可以使用 **extAW** 输入端口实现自定义抗饱和逻辑。模块还在 **preInt** 输出端口提供积分器之前的信号，您可以用它来实现自定义算法。

#### 依赖关系

要启用此端口，请在 **Saturation** 选项卡上，选择 **Limit output**，并将 **Anti-windup Method** 设置为 `external`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### 输出

### **Port\_1( u )** — 控制器输出 标量 | 向量

控制器输出，通常基于输入信号、输入信号的积分和输入信号的导数的总和，并由设定点权重以及比例、积分和微分增益参数加权。一阶极点对微分作用进行滤波。控制器信号中存在哪些项取决于您为 **Controller** 参数选择的内容。当前设置的基础控制器传递函数显示在模块参数的 **Compensator formula** 部分以及掩码下。其他参数会修改模块输出，例如由 **Upper Limit** 和 **Lower Limit** 饱和参数指定的饱和限值。

当任何输入是向量信号时，控制器输出是向量信号。在这种情况下，模块充当 *N* 个独立的 PID 控制器，其中 *N* 是输入向量中的信号数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **preInt** — 积分器前信号 标量 | 向量

*自 R2024b 起*

模块在此端口输出积分器之前的信号。将此信号用作您在 **extAW** 端口提供的自定义抗饱和算法的输入。

#### 依赖关系

要启用此端口，请在 **Saturation** 选项卡上，选择 **Limit output**，并将 **Anti-windup Method** 设置为 `external`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **Controller** — 控制器类型 `PID` (默认) | `PI` | `PD`

指定控制器中包含比例、积分和微分项中的哪些项。

`PID`
:   比例、积分和微分作用。

`PI`
:   仅比例和积分作用。

`PD`
:   仅比例和微分作用。

**提示**

当前设置的控制器输出显示在模块参数的 **Compensator formula** 部分以及掩码下。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Controller` |
| **类型：** string, character vector |
| **值：** `"PID"`, `"PI"`, `"PD"` |
| **默认：** `"PID"` |

### **Form** — 控制器结构 `Parallel` (默认) | `Ideal`

指定控制器结构是并联还是理想。

`Parallel`
:   比例、积分和微分增益 **P**、**I** 和 **D** 独立应用。例如，对于并联形式的连续时间 2-DOF PID 控制器，控制器输出 *u* 为：

    u=P(br−y)+I1s(r−y)+DN1+N1s(cr−y)，

    其中 *r* 是参考信号，*y* 是测量的被控对象输出信号，*b* 和 *c* 是设定点权重。

    对于并联形式的离散时间 2-DOF 控制器，控制器输出为：

    u=P(br−y)+Iα(z)(r−y)+DN1+Nβ(z)(cr−y)，

    其中 **Integrator method** 和 **Filter method** 参数分别确定 *α*(*z*) 和 *β*(*z*)。

`Ideal`
:   比例增益 **P** 作用于所有作用之和。例如，对于理想形式的连续时间 2-DOF PID 控制器，控制器输出为：

    u=P[(br−y)+I1s(r−y)+DN1+N1s(cr−y)]。

    对于理想形式的离散时间 2-DOF PID 控制器，传递函数为：

    u=P[(br−y)+Iα(z)(r−y)+DN1+Nβ(z)(cr−y)]，

    其中 **Integrator method** 和 **Filter method** 参数分别确定 *α*(*z*) 和 *β*(*z*)。

    **提示**

    当前设置的控制器输出显示在模块参数的 **Compensator formula** 部分以及掩码下。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Controller` |
| **类型：** string, character vector |
| **值：** `"Parallel"`, `"Ideal"` |
| **默认：** `"Parallel"` |

### **Time domain** — 指定离散时间或连续时间控制器 `Discrete-time` (默认) | `Continuous-time`

当您选择 `Discrete-time` 时，建议您为模块指定显式采样时间。请参阅 **Sample time (-1 for inherited)** 参数。选择 `Discrete-time` 还会启用 **Integrator method** 和 **Filter method** 参数。

当 PID Controller 模块位于具有同步状态控制的模型中时（请参阅 State Control (HDL Coder) 模块），您不能选择 `Continuous-time`。

**注意**

除此参数的默认值外，PID Controller (2DOF) 和 Discrete PID Controller (2DOF) 模块完全相同。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TimeDomain` |
| **类型：** string, character vector |
| **值：** `"Continuous-time"`, `"Discrete-time"` |
| **默认：** `"Discrete-time"` |

### **PID Controller is inside a conditionally executed subsystem** — 启用离散积分器时间端口 `off` (默认) | `on`

对于离散时间 PID 控制器，启用离散时间积分器端口以使用您自己的离散时间积分器采样时间值。为确保正确积分，请使用 `TDTI` 端口提供 Δt 的标量值，以实现准确的离散时间积分。

#### 依赖关系

要启用此参数，请将 **Time Domain** 设置为 `Discrete-time`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `UseExternalTs` |
| **类型：** string, character vector |
| **值：** `"on"`, `"off"` |
| **默认：** `"off"` |

### **Sample time (-1 for inherited)** — 样本之间的离散间隔 –1 (默认) | 正标量

通过输入正标量值（例如 0.1）来指定采样时间。默认离散采样时间 –1 表示模块从上游模块继承其采样时间。但是，建议您显式设置控制器采样时间，尤其是在您预期上游模块的采样时间会变化时。控制器系数 P、I、D 和 N 的效果取决于采样时间。因此，对于给定的一组系数值，更改采样时间会改变控制器的性能。

有关详细信息，请参阅 Specify Sample Time。

要实现连续时间控制器，请将 **Time domain** 设置为 `Continuous-time`。

**提示**

如果您想以外部指定或可变采样时间运行模块，请将此参数设置为 –1，并将模块放入 Triggered Subsystem 中。然后，以所需采样时间触发子系统。

#### 依赖关系

要启用此参数，请将 **Time domain** 设置为 `Discrete-time`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** scalar |
| **值：** `-1`, positive scalar |
| **默认：** `-1` |

### **Integrator method** — 离散时间控制器中计算积分的方法 `Forward Euler` (默认) | `Backward Euler` | `Trapezoidal`

在离散时间中，控制器传递函数的积分项为 *Ia*(*z*)，其中 *a*(*z*) 取决于您使用此参数指定的积分器方法。

`Forward Euler`
:   前向矩形（左手）近似，

    α(z)=Tsz−1。

    此方法最适合小采样时间，此时 Nyquist 限值相对于控制器带宽较大。对于较大的采样时间，`Forward Euler` 方法可能导致不稳定，即使离散化一个在连续时间中稳定的系统也是如此。

`Backward Euler`
:   后向矩形（右手）近似，

    α(z)=Tszz−1。

    `Backward Euler` 方法的一个优点是，使用此方法离散化稳定的连续时间系统总是产生稳定的离散时间结果。

`Trapezoidal`
:   双线性近似，

    α(z)=Ts2z+1z−1。

    `Trapezoidal` 方法的一个优点是，使用此方法离散化稳定的连续时间系统总是产生稳定的离散时间结果。在所有可用积分方法中，`Trapezoidal` 方法使离散化系统的频域属性与相应连续时间系统之间的匹配最接近。

    **提示**

    当前设置的控制器公式显示在模块参数的 **Compensator formula** 部分以及掩码下。

有关离散时间积分的详细信息，请参阅 Discrete-Time Integrator 模块参考页。

#### 依赖关系

要启用此参数，请将 **Time Domain** 设置为 `Discrete-time`，并将 **Controller** 设置为具有积分作用的控制器类型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `IntegratorMethod` |
| **类型：** string, character vector |
| **值：** `"Forward Euler"`, `"Backward Euler"`, `"Trapezoidal"` |
| **默认：** `"Forward Euler"` |

### **Filter method** — 离散时间控制器中计算导数的方法 `Forward Euler` (默认) | `Backward Euler` | `Trapezoidal`

在离散时间中，控制器传递函数的微分项为：

D[N1+Nα(z)]，

其中 *α*(*z*) 取决于您使用此参数指定的滤波器方法。

`Forward Euler`
:   前向矩形（左手）近似，

    α(z)=Tsz−1。

    此方法最适合小采样时间，此时 Nyquist 限值相对于控制器带宽较大。对于较大的采样时间，`Forward Euler` 方法可能导致不稳定，即使离散化一个在连续时间中稳定的系统也是如此。

`Backward Euler`
:   后向矩形（右手）近似，

    α(z)=Tszz−1。

    `Backward Euler` 方法的一个优点是，使用此方法离散化稳定的连续时间系统总是产生稳定的离散时间结果。

`Trapezoidal`
:   双线性近似，

    α(z)=Ts2z+1z−1。

    `Trapezoidal` 方法的一个优点是，使用此方法离散化稳定的连续时间系统总是产生稳定的离散时间结果。在所有可用积分方法中，`Trapezoidal` 方法使离散化系统的频域属性与相应连续时间系统之间的匹配最接近。

    **提示**

    当前设置的控制器公式显示在模块参数的 **Compensator formula** 部分以及掩码下。

有关离散时间积分的详细信息，请参阅 Discrete-Time Integrator 模块参考页。

#### 依赖关系

要启用此参数，请将 **Time Domain** 设置为 `Discrete-time`，并启用 **Use filtered derivative**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FilterMethod` |
| **类型：** string, character vector |
| **值：** `"Forward Euler"`, `"Backward Euler"`, `"Trapezoidal"` |
| **默认：** `"Forward Euler"` |

### 主要

### **Source** — 控制器增益和滤波器系数的来源 internal (默认) | external

`internal`
:   使用模块参数 **P**、**I**、**D**、**N**、**b** 和 **c** 分别指定控制器增益、滤波器系数和设定点权重。

`external`
:   使用模块输入从外部指定 PID 增益、滤波器系数和设定点权重。对于当前控制器类型所需的每个参数，模块上会出现一个额外的输入端口。

为参数启用外部输入允许您在模块外部计算它们的值，并将它们作为信号输入提供给模块。

外部输入很有用，例如，当您想将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部增益输入来实现增益调度 PID 控制。在增益调度控制中，您通过模型中的逻辑或其他计算确定 PID 增益，并将它们馈送到模块。

当您从外部提供增益时，积分和微分增益值的时间变化会分别被积分和微分。微分设定点权重 *c* 也会被微分。出现此结果是因为在连续时间和离散时间中，增益都应用于积分或微分之前的信号。例如，对于具有外部输入的连续时间 PID 控制器，积分器项的实现方式如下图所示。

在模块内部，输入信号 *u* 在积分之前乘以外部提供的积分器增益 *I*。此实现产生：

ui=∫(r−y)I dt。

因此，积分器增益包含在积分中。类似地，在模块的微分项中，乘以微分增益先于微分，这导致微分增益 *D* 和微分设定点权重 *c* 被微分。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ControllerParametersSource` |
| **类型：** string, character vector |
| **值：** `"internal"`, `"external"` |
| **默认：** `"internal"` |

### **Proportional (P)** — 比例增益 1 (默认) | 标量 | 向量

为比例增益指定一个有限实增益值。当 **Controller form** 为：

- `Parallel` — 比例作用独立于积分和微分作用。例如，对于并联形式的连续时间 2-DOF PID 控制器，控制器输出 *u* 为：

  u=P(br−y)+I1s(r−y)+DN1+N1s(cr−y)，

  其中 *r* 是参考信号，*y* 是测量的被控对象输出信号，*b* 和 *c* 是设定点权重。

  对于并联形式的离散时间 2-DOF 控制器，控制器输出为：

  u=P(br−y)+Iα(z)(r−y)+DN1+Nβ(z)(cr−y)，

  其中 **Integrator method** 和 **Filter method** 参数分别确定 *α*(*z*) 和 *β*(*z*)。
- `Ideal` — 比例增益乘以积分项和微分项。例如，对于理想形式的连续时间 2-DOF PID 控制器，控制器输出为：

  u=P[(br−y)+I1s(r−y)+DN1+N1s(cr−y)]。

  对于理想形式的离散时间 2-DOF PID 控制器，传递函数为：

  u=P[(br−y)+Iα(z)(r−y)+DN1+Nβ(z)(cr−y)]，

  其中 **Integrator method** 和 **Filter method** 参数分别确定 *α*(*z*) 和 *β*(*z*)。

#### 依赖关系

要启用此参数，请将控制器参数 **Source** 设置为 `internal`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `P` |
| **类型：** scalar, vector |
| **默认：** 1 |

**可调：** 是

### **Integral (I)** — 积分增益 1 (默认) | 标量 | 向量

为积分增益指定一个有限实增益值。

**可调：** 是

#### 依赖关系

要启用此参数，请在 **Main** 选项卡中，将控制器参数 **Source** 设置为 `internal`，并将 **Controller** 设置为具有积分作用的类型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `I` |
| **类型：** scalar, vector |
| **默认：** 1 |

### **Integral (I\*Ts)** — 积分增益乘以采样时间 1 (默认) | 标量 | 向量

对于离散时间控制器，为积分增益乘以采样时间指定一个有限实增益值。

**注意**

PID 整定工具（例如 PID Tuner app 和 Closed-Loop PID Autotuner block）整定增益 **I**，而不是 **I\*Ts**。因此，在将此参数写入之前，请将您从整定工具获得的积分增益值乘以采样时间。

当您使用 **I\*Ts** 而不是 **I** 时，模块执行积分所需的计算更少。这会改善生成代码的执行时间。

对于连续时间控制器，请禁用 **Use I\*Ts**，并改用 **I** 参数。

**可调：** 否

#### 依赖关系

要启用此参数，请在 **Main** 选项卡中，将控制器参数 **Source** 设置为 `internal`，将 **Controller** 设置为具有积分作用的类型，并启用 **Use I\*Ts** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `I` |
| **类型：** scalar, vector |
| **默认：** 1 |

### **Use I\*Ts** — 使用积分增益乘以采样时间 `off` (默认) | `on`

对于具有积分作用的离散时间控制器，模块将积分增益作为输入，并在执行积分时在内部将其乘以采样时间。如果您启用此参数，则您显式指定积分增益乘以采样时间作为输入（**I\*Ts**），以代替积分增益（**I**）。这样做会减少内部计算次数，并且当您想改善生成代码的执行时间时很有用。

如果您已启用信号跟踪或抗饱和模式 back-calculation，并启用 **I\*Ts**，则还必须将跟踪增益参数 **Kt** 设置为 `Kt*Ts`，并将 back-calculation 系数 **Kb** 设置为 `Kb*Ts`。

对于连续时间控制器，启用此参数对积分增益没有影响。

#### 依赖关系

要启用此参数，请将 **Controller** 设置为具有积分作用的控制器类型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `UseKiTs` |
| **类型：** string, character vector |
| **值：** `"on"`, `"off"` |
| **默认：** `"on"` |

### **Derivative (D)** — 微分增益 0 (默认) | 标量 | 向量

为微分增益指定一个有限实增益值。

**可调：** 是

#### 依赖关系

要启用此参数，请在 **Main** 选项卡中，将控制器参数 **Source** 设置为 `internal`，并将 **Controller** 设置为 `PID` 或 `PD`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `D` |
| **类型：** scalar, vector |
| **默认：** 0 |

### **Use externally sourced derivative** — 在模块输入端口指定导数 `off` (默认) | `on`

*自 R2024a 起*

选择此选项以直接将被控对象信号 *y* 的导数作为输入 **ydot** 提供给模块。当您的模型中已有该导数信号，并且希望跳过模块内部的导数计算时，这很有帮助。

#### 依赖关系

要启用此选项，请选择具有微分作用的控制器类型。

### **Use filtered derivative** — 对微分项应用滤波器 `on` (默认) | `off`

仅对于离散时间 PID 控制器，清除此选项以将滤波微分替换为未滤波的离散时间微分器。这样做时，控制器输出的微分项变为：

Dz−1zTs(cr−y)。

对于连续时间 PID 控制器，微分项始终经过滤波。

#### 依赖关系

要启用此参数，请将 **Time domain** 设置为 `Discrete-time`，并将 **Controller** 设置为具有微分项的类型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `UseFilter` |
| **类型：** string, character vector |
| **值：** `"on"`, `"off"` |
| **默认：** `"on"` |

### **Filter coefficient (N)** — 微分滤波器系数 100 (默认) | 标量 | 向量

为滤波器系数指定一个有限实增益值。滤波器系数确定模块微分作用中滤波器的极点位置。滤波器极点的位置取决于 **Time domain** 参数。

- 当 **Time domain** 为 `Continuous-time` 时，极点位置为 `s = -N`。
- 当 **Time domain** 为 `Discrete-time` 时，极点位置取决于 **Filter method** 参数。

  | 滤波器方法 | 滤波器极点位置 |
  | --- | --- |
  | `Forward Euler` | zpole=1−NTs |
  | `Backward Euler` | zpole=11+NTs |
  | `Trapezoidal` | zpole=1−NTs/21+NTs/2 |

模块不支持 `N = Inf`（理想未滤波微分）。当 **Time domain** 为 `Discrete-time` 时，您可以清除 **Use filtered derivative** 以移除微分滤波器。

#### 依赖关系

要启用此参数，请在 **Main** 选项卡中，将控制器参数 **Source** 设置为 `internal`，并将 **Controller** 设置为 `PID` 或 `PD`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `N` |
| **类型：** scalar, vector |
| **默认：** 100 |

**可调：** 是

### **Setpoint weight (b)** — 比例设定点权重 1 (默认) | 标量 | 向量

控制器比例项上的设定点权重。2-DOF 控制器输出的比例项为
*P*(*br*–*y*)，
其中 *r* 是参考信号，*y* 是测量的被控对象输出。将 *b* 设置为 0 可消除参考信号上的比例作用，这可以减少系统对设定点阶跃变化的响应中的超调。更改 *b* 和 *c* 的相对值会改变扰动抑制与设定点跟踪之间的平衡。

**可调：** 是

#### 依赖关系

要启用此参数，请在 **Main** 选项卡中，将控制器参数 **Source** 设置为 `internal`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `b` |
| **类型：** scalar, vector |
| **默认：** 1 |

### **Setpoint weight (c)** — 微分设定点权重 1 (默认) | 标量 | 向量

控制器微分项上的设定点权重。2-DOF 控制器的微分项作用于 *cr*–*y*，其中 *r* 是参考信号，*y* 是测量的被控对象输出。因此，将 *c* 设置为 0 可消除参考信号上的微分作用，这可以减少对设定点阶跃变化的瞬态响应。将 *c* 设置为 0 可产生一个控制器，该控制器既能实现有效的扰动抑制，又能实现平滑的设定点跟踪，而不会产生过大的瞬态响应。更改 *b* 和 *c* 的相对值会改变扰动抑制与设定点跟踪之间的平衡。

**可调：** 是

#### 依赖关系

要启用此参数，请在 **Main** 选项卡中，将控制器参数 **Source** 设置为 `internal`，并将 **Controller** 设置为具有微分作用的类型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `c` |
| **类型：** scalar, vector |
| **默认：** 1 |

### **Select tuning method** — 控制器系数自动整定工具 `Transfer Function Based (PID Tuner App)` (默认) | `Frequency Response Based`

如果您有 Simulink Control Design 软件，则当 PID 系数在模块内部时，您可以自动整定它们。为此，请使用此参数选择整定工具，然后单击 **Tune**。

`Transfer Function Based (PID Tuner App)`
:   使用 PID Tuner，它允许您交互式整定 PID 系数，同时检查相关系统响应以验证性能。PID Tuner 可以整定所有系数 **P**、**I**、**D** 和 **N**，以及设定点系数 **b** 和 **c**。默认情况下，PID Tuner 使用您被控对象模型的线性化。对于无法线性化的模型，您可以针对根据仿真或测量响应数据估计的被控对象模型来整定 PID 系数。有关详细信息，请参阅 Design Two-Degree-of-Freedom PID Controllers (Simulink Control Design)。

`Frequency Response Based`
:   使用 Frequency Response Based PID Tuner，它基于通过仿真获得的频率响应估计数据来整定 PID 控制器系数。此整定方法对于无法线性化或线性化为零的被控对象特别有用。Frequency Response Based PID Tuner 整定系数 **P**、**I**、**D** 和 **N**，但不整定设定点系数 **b** 和 **c**。有关详细信息，请参阅 Design PID Controller from Plant Frequency-Response Data (Simulink Control Design)。

这两种整定方法都假设单回路控制配置。Simulink Control Design 软件包含其他适合更复杂配置的整定方法。有关整定 PID Controller 模块的其他方式的信息，请参阅 Choose a Control Design Approach (Simulink Control Design)。

#### 依赖关系

要启用此参数，请在 **Main** 选项卡中，将控制器参数 **Source** 设置为 `internal`。

### **Enable zero-crossing detection** — 在复位时以及进入或离开饱和状态时检测过零 `on` (默认) | `off`

过零检测可以准确定位信号不连续点，而无需诉诸可能导致漫长仿真时间的极小时间步。如果您在 PID Controller 模块中选择 **Limit output** 或激活 **External reset**，则激活过零检测可以减少仿真中的计算时间。选择此参数会在以下情况下激活过零检测：

- 初始状态复位时
- 进入上限或下限饱和状态时
- 离开上限或下限饱和状态时

有关过零检测的详细信息，请参阅 Zero-Crossing Detection。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ZeroCross` |
| **类型：** string, character vector |
| **值：** `"on"`, `"off"` |
| **默认：** `"on"` |

### 初始化

### **Source** — 积分器和微分初始条件的来源 `internal` (默认) | `external`

Simulink 使用初始条件在仿真开始时或指定触发事件时初始化积分器和微分滤波器（或未滤波微分）输出。（请参阅 **External reset** 参数。）这些初始条件确定初始模块输出。使用此参数选择如何向模块提供初始条件值。

`internal`
:   使用 **Integrator Initial condition** 和 **Filter Initial condition** 参数指定初始条件。如果未选择 **Use filtered derivative**，请使用 **Differentiator** 参数为未滤波微分器指定初始条件，而不是滤波器初始条件。

`external`
:   使用模块输入从外部指定初始条件。模块上会出现额外的输入端口 **Io** 和 **Do**。如果未选择 **Use filtered derivative**，请在 **Do** 处为未滤波微分器提供初始条件，而不是滤波器初始条件。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialConditionSource` |
| **类型：** string, character vector |
| **值：** `"internal"`, `"external"` |
| **默认：** `"internal"` |

### **Integrator** — 积分器初始条件 0 (默认) | 标量 | 向量

Simulink 使用积分器初始条件在仿真开始时或指定触发事件时初始化积分器（请参阅 **External reset**）。积分器初始条件和滤波器初始条件确定 PID 控制器模块的初始输出。

积分器初始条件不能为 `NaN` 或 `Inf`。

#### 依赖关系

要使用此参数，请在 **Initialization** 选项卡中，将 **Source** 设置为 `internal`，并将 **Controller** 设置为具有积分作用的类型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialConditionForIntegrator` |
| **类型：** scalar, vector |
| **默认：** 0 |

### **Filter** — 滤波器初始条件 0 (默认) | 标量 | 向量

Simulink 使用滤波器初始条件在仿真开始时或指定触发事件时初始化微分滤波器（请参阅 **External reset**）。积分器初始条件和滤波器初始条件确定 PID 控制器模块的初始输出。

滤波器初始条件不能为 `NaN` 或 `Inf`。

#### 依赖关系

要使用此参数，请在 **Initialization** 选项卡中，将 **Source** 设置为 `internal`，并使用具有微分滤波器的控制器。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialConditionForFilter` |
| **类型：** scalar, vector |
| **默认：** 0 |

### **Differentiator** — 未滤波微分的初始条件 0 (默认) | 标量 | 向量

当您使用未滤波微分时，Simulink 使用此参数在仿真开始时或指定触发事件时初始化微分器（请参阅 **External reset**）。积分器初始条件和微分初始条件确定 PID 控制器模块的初始输出。

微分初始条件不能为 `NaN` 或 `Inf`。

#### 依赖关系

要使用此参数，请将 **Time domain** 设置为 `Discrete-time`，清除 **Use filtered derivative** 复选框，并在 **Initialization** 选项卡中，将 **Source** 设置为 `internal`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DifferentiatorICPrevScaledInput` |
| **类型：** scalar, vector |
| **默认：** 0 |

### **Initial condition setting** — 应用初始条件的位置 `Auto` (默认) | `Output`

使用此参数指定是将 **Integrator Initial condition** 和 **Filter Initial condition** 参数应用于相应模块状态还是输出。您只能在命令行更改此参数，使用 `set_param` 设置模块的 `InitialConditionSetting` 参数。

`Auto`
:   除模块位于触发子系统或函数调用子系统中且启用了简化初始化模式外，在所有情况下都使用此选项。

`Output`
:   当模块位于触发子系统或函数调用子系统中且启用了简化初始化模式时，使用此选项。

有关 **Initial condition setting** 参数的详细信息，请参阅 Discrete-Time Integrator 模块。

此参数只能通过程序化使用访问。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialConditionSetting` |
| **类型：** string, character vector |
| **值：** `"Auto"`, `"Output"` |
| **默认：** `"Auto"` |

### **External reset** — 用于复位积分器和滤波器值的触发 `none` (默认) | `rising` | `falling` | `either` | `level`

指定导致模块将积分器和滤波器复位到初始条件的触发条件。（如果未选择 **Use filtered derivative**，则触发会将积分器和微分器复位到初始条件。）选择除 `none` 以外的任何选项都会启用模块上的 **Reset** 端口，用于外部复位信号。

`none`
:   积分器和滤波器（或微分器）输出在仿真开始时设置为初始条件，并且在仿真期间不会复位。

`rising`
:   当复位信号具有上升沿时，复位输出。

`falling`
:   当复位信号具有下降沿时，复位输出。

`either`
:   当复位信号上升或下降时，复位输出。

`level`
:   当复位信号满足以下任一情况时，复位输出：

    - 在当前时间步非零
    - 从上一时间步的非零变为当前时间步的零

    当复位信号非零时，此选项将输出保持为初始条件。

#### 依赖关系

要启用此参数，请将 **Controller** 设置为具有微分或积分作用的类型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ExternalReset` |
| **类型：** string, character vector |
| **值：** `"none"`, `"rising"`, `"falling"`, `"either"`,`"level"` |
| **默认：** `"none"` |

### **Ignore reset when linearizing** — 强制线性化忽略复位 `off` (默认) | `on`

选择此项以强制 Simulink 和 Simulink Control Design 线性化命令忽略 **External reset** 参数中指定的任何复位机制。忽略复位状态允许您围绕工作点对模型进行线性化，即使该工作点导致模块复位。

#### 程序化使用

|  |
| --- |
| **模块参数：** `IgnoreLimit` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认：** `"off"` |

### **Enable tracking mode** — 激活信号跟踪 `off` (默认) | `on`

信号跟踪允许模块输出跟随您在 **TR** 端口提供的跟踪信号。当信号跟踪处于活动状态时，跟踪信号与模块输出之间的差值会以增益 `Kt` 反馈到积分器输入，该增益由 **Tracking gain (Kt)** 参数指定。信号跟踪有多种应用，包括无扰控制传递和避免多回路控制结构中的饱和。

#### 无扰控制传递

使用信号跟踪在在两个控制器之间切换的系统中实现无扰控制传递。假设您想在 PID 控制器和另一个控制器之间传递控制。为此，将控制器输出连接到 **TR** 输入，如下图所示。

有关详细信息，请参阅 Bumpless Control Transfer with a Two-Degree-of-Freedom PID Controller。

#### 多回路控制

使用信号跟踪防止多回路控制方法中的模块饱和。有关使用 1DOF PID 控制器说明此方法的示例，请参阅 Prevent Block Windup in Multiloop Control。

#### 依赖关系

要启用此参数，请将 **Controller** 设置为具有积分作用的类型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TrackingMode` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认：** `"off"` |

### **Tracking coefficient (Kt)** — 信号跟踪反馈环路的增益 1 (默认) | 标量

当您选择 **Enable tracking mode** 时，信号 **TR** 与模块输出之间的差值会以增益 `Kt` 反馈到积分器输入。使用此参数指定该反馈环路中的增益。

对于离散时间控制器，如果您选择模块的 **Use I\*Ts** 参数，则将此参数设置为值 `Kt*Ts`，其中 `Kt` 是所需增益，`Ts` 是采样时间。

#### 依赖关系

要启用此参数，请选择 **Enable tracking mode**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Kt` |
| **类型：** scalar |
| **默认：** 1 |

### 饱和

#### 输出饱和

### **Limit Output** — 将模块输出限制到指定的饱和值 `off` (默认) | `on`

激活此选项会限制模块输出，因此您不需要在控制器之后使用单独的 Saturation 模块。它还允许您激活模块内置的抗饱和机制（请参阅 **Anti-windup method** 参数）。使用 **Lower limit** 和 **Upper limit** 参数指定输出饱和限值。您还可以将饱和限值作为模块输入端口从外部指定。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LimitOutput` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认：** `"off"` |

### **Source** — 输出饱和限值的来源 internal (默认) | external

使用此参数指定如何提供模块输出的上限和下限饱和限值。

`internal`
:   使用 **Upper limit** 和 **Lower limit** 参数指定输出饱和限值。

`external`
:   使用模块输入端口从外部指定输出饱和限值。模块上会出现额外的输入端口 **up** 和 **lo**。您可以使用这些输入端口实现由 Simulink 模型中的逻辑或其他计算确定并传递给模块的输出饱和上限和下限。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SatLimitsSource` |
| **类型：** string, character vector |
| **值：** `"internal"`, `"external"` |
| **默认：** `"internal"` |

### **Upper limit** — 模块输出的上限饱和限值 `Inf` (默认) | 标量

指定模块输出的上限。当比例、积分和微分作用的加权和超过该值时，模块输出保持在 **Upper saturation limit**。

#### 依赖关系

要启用此参数，请选择 **Limit output**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `UpperSaturationLimit` |
| **类型：** scalar |
| **默认：** `Inf` |

### **Lower limit** — 模块输出的下限饱和限值 `-Inf` (默认) | 标量

指定模块输出的下限。当比例、积分和微分作用的加权和低于该值时，模块输出保持在 **Lower saturation limit**。

#### 依赖关系

要启用此参数，请选择 **Limit output**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LowerSaturationLimit` |
| **类型：** scalar |
| **默认：** `-Inf` |

### **Ignore saturation when linearizing** — 强制线性化忽略输出限值 `off` (默认) | `on`

强制 Simulink 和 Simulink Control Design 线性化命令忽略 **Upper limit** 和 **Lower limit** 参数中指定的模块输出限值。忽略输出限值允许您围绕工作点对模型进行线性化，即使该工作点导致模块超过输出限值。

#### 依赖关系

要启用此参数，请选择 **Limit output** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LinearizeAsGain` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认：** `"off"` |

### **Anti-windup method** — 积分器抗饱和方法 `none` (默认) | `back-calculation` | `clamping` | `external`

当您选择 **Limit output** 且控制器分量的加权和超过指定的输出限值时，模块输出保持在指定限值。但是，积分器输出可能继续增长（积分器饱和），从而增大模块输出与模块分量之和之间的差值。换句话说，即使输出看起来受饱和限值约束，模块内部信号也可能是无界的。如果没有防止积分器饱和的机制，可能会出现两种结果：

- 如果进入积分器的信号符号从不改变，积分器会继续积分直到溢出。溢出值是积分器输出数据类型的最大值或最小值。
- 如果进入积分器的信号在加权和增长到超过输出限值后改变符号，则可能需要很长时间才能解开积分器并使加权和回到模块饱和限值内。

在任一情况下，控制器性能都可能变差。为了在没有抗饱和机制的情况下对抗饱和影响，可能需要降低控制器整定程度（例如，通过减小控制器增益），从而导致控制器响应迟缓。为避免此问题，请使用此参数激活抗饱和机制。

`none`
:   不使用抗饱和机制。

`back-calculation`
:   当模块输出饱和时，通过将饱和与未饱和控制信号之间的差值反馈到积分器来解开积分器。下图表示连续时间控制器的 back-calculation 反馈电路。要查看您的控制器配置的实际反馈电路，请右键单击模块并选择 **Mask** > **Look Under Mask**。

    使用 **Back-calculation coefficient (Kb)** 参数指定抗饱和反馈电路的增益。通常设置 `Kb = I` 就足够，或者对于具有微分作用的控制器，`Kb = sqrt(I*D)`。Back-calculation 对于具有相对较大死区的被控对象可能有效 [1]。

`clamping`
:   Clamping 有时称为条件积分。

    当以下两个条件都成立时，积分停止：

    - 模块分量之和超过输出限值。
    - 积分器输入和饱和模块输入具有相同符号。

    当任一条件不再成立时，积分恢复。

    Clamping 对于具有相对较小死区的被控对象可能有用，但对于大死区可能产生较差的瞬态响应 [1]。

`external` *（自 R2024b 起）*
:   内置抗饱和方法依赖于模块分量之和超过指定的模块输出限值。如果您的应用在 PID 控制器模块下游具有饱和或限值，您可以使用 **extAW** 输入端口实现自定义抗饱和逻辑。模块还在 **preInt** 输出端口提供积分器之前的信号，您可以将其用作自定义算法的输入。

#### 依赖关系

要启用此参数，请选择 **Limit output** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `AntiWindupMode` |
| **类型：** string, character vector |
| **值：** `"none"`, `"back-calculation"`,`"clamping"`, `"external"` |
| **默认：** `"none"` |

### **Back-calculation coefficient (Kb)** — 抗饱和反馈环路的增益系数 1 (默认) | 标量

`back-calculation` 抗饱和方法在模块输出饱和时解开积分器。它通过将饱和与未饱和控制信号之间的差值反馈到积分器来实现。使用 **Back-calculation coefficient (Kb)** 参数指定抗饱和反馈电路的增益。有关详细信息，请参阅 **Anti-windup method** 参数。

对于离散时间控制器，如果您选择模块的 **Use I\*Ts** 参数，则将此参数设置为值 `Kb*Ts`，其中 `Kb` 是所需系数，`Ts` 是采样时间。

#### 依赖关系

要启用此参数，请选择 **Limit output** 参数，并将 **Anti-windup method** 参数设置为 `back-calculation`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Kb` |
| **类型：** scalar |
| **默认：** 1 |

#### 积分器饱和

### **Limit Output** — 将积分器输出限制到指定的饱和限值 `off` (默认) | `on`

启用此参数以将积分器输出限制在指定范围内。当积分器输出达到限值时，积分作用关闭以防止积分饱和。使用 **Lower limit** 和 **Upper limit** 参数指定饱和限值。

#### 依赖关系

要启用此参数，请将 **Controller** 设置为具有积分作用的控制器类型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LimitIntegratorOutput` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认：** `"off"` |

### **Upper limit** — 积分器的上限饱和限值 `Inf` (默认) | 标量

指定积分器输出的上限。只要积分器输出本来会超过此值，它就会保持在此值。

#### 依赖关系

要启用此参数，请在 **Integrator saturation** 下选择 **Limit output**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `UpperIntegratorSaturationLimit` |
| **类型：** scalar |
| **默认：** `Inf` |

### **Lower limit** — 积分器的下限饱和限值 `-Inf` (默认) | 标量

指定积分器输出的下限。只要积分器输出本来会低于此值，它就会保持在此值。

#### 依赖关系

要启用此参数，请在 **Integrator saturation** 下选择 **Limit output**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LowerIntegratorSaturationLimit` |
| **类型：** scalar |
| **默认：** `-Inf` |

### 数据类型

此选项卡中的参数主要用于使用 Fixed-Point Designer™ 进行定点代码生成。它们定义当您生成代码时，与模块关联的数值量如何存储和处理。

如果您需要为定点代码生成配置数据类型，请单击 **Open Fixed-Point Tool** 并使用该工具配置选项卡中的其余参数。有关使用 Fixed-Point Tool 的信息，请参阅 Autoscaling Data Objects Using the Fixed-Point Tool (Fixed-Point Designer)。

使用 Fixed-Point Tool 后，如有必要，您可以使用此选项卡中的参数调整定点数据类型设置。对于与模块关联的每个量，您可以指定：

- 浮点或定点数据类型，包括数据类型是否从模块中的上游值继承。
- 量的最小值和最大值，它们决定该量如何缩放以进行定点表示。

如需帮助选择适当的值，请单击  以打开相应量的 Data Type Assistant。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

Data Types 选项卡中列出的具体量取决于您如何配置 PID controller 模块。通常，您可以为以下类型的量配置数据类型：

- Product output — 存储模块掩码下执行的乘法结果。例如，**P product output** 存储将模块输入与比例增益 **P** 相乘的增益模块的输出。
- Parameter — 存储数值模块参数的值，例如 **P**、**I** 或 **D**。
- Block output — 存储位于 PID controller 模块掩码下的模块输出。例如，使用 **Integrator output** 指定名为 Integrator 的模块输出的数据类型。此模块位于 Integrator 子系统中的掩码下，并计算控制器作用的积分项。
- Accumulator — 存储与求和模块关联的值。例如，**SumI2 Accumulator** 设置与求和模块 SumI2 关联的累加器的数据类型。此模块位于 Anti-Windup 子系统的 Back Calculation 子系统中的掩码下。

通常，您可以通过查看 PID Controller 模块掩码下并检查其子系统，找到与任何列出的参数关联的模块。您还可以使用 Model Explorer 在掩码下搜索列出的参数名称，例如 `SumI2`。（请参阅 Model Explorer。）

**匹配输入和内部数据类型**

默认情况下，模块中的所有数据类型都设置为 `Inherit: Inherit via internal rule`。使用此设置，Simulink 会选择数据类型以平衡数值精度、性能和生成代码大小，同时考虑嵌入式目标硬件的属性。

在某些条件下，模块内部的数据类型之间可能发生不兼容。例如，在连续时间中，掩码下的 Integrator 模块只能接受 `double` 类型的信号。如果模块输入信号是无法转换为 `double` 的类型，例如 `uint16`，则类型继承的内部规则会在您生成代码时产生错误。

为避免此类错误，您可以使用 Data Types 设置强制进行数据类型转换。例如，您可以显式将 **P product output**、**I product output** 和 **D product output** 设置为 `double`，确保到达连续时间积分器的信号为 `double` 类型。

通常，不建议在代码生成应用中将该模块用于连续时间。但是，如果您显式将某些值设置为与模块内下游信号约束不兼容的数据类型，则离散时间中也可能发生类似的数据类型错误。在这种情况下，请使用 Data Types 设置确保所有数据类型在内部兼容。

#### 定点运算参数

### **Integer rounding mode** — 定点运算的舍入模式 `Floor` (默认) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RndMeth` |
| **值：** | `'Floor'` (默认) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Saturate on integer overflow** — 溢出操作的方法 `off` (默认) | `on`

指定溢出是饱和还是回绕。

- `on` — 溢出饱和到数据类型可以表示的最小值或最大值。
- `off` — 溢出回绕到数据类型可以表示的适当值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。

- 选择此参数后，模块输出在 127 处饱和。类似地，模块输出在最小输出值 -128 处饱和。
- 清除此参数后，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 是 -126。

#### 提示

- 当您的模型可能发生溢出，并且您希望在生成代码中具有显式饱和保护时，请考虑选择此参数。
- 当您想优化生成代码的效率时，请考虑清除此参数。清除此参数还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors。
- 当您选择此参数时，饱和适用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `'off'` (默认) | `'on'` |

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选择此参数以防止定点工具覆盖您在此模块上指定的数据类型。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** character vector |
| **值：** `'off' | 'on'` |
| **默认：** `'off'` |

### 状态属性

此选项卡中的参数主要用于代码生成。

### **State name (e.g., 'position')** — 连续时间滤波器和积分器状态的名称 `''` (默认) | character vector

为与积分器或滤波器关联的状态指定唯一名称，用于连续时间 PID 控制器。（有关离散时间 PID 控制器中的状态名称的信息，请参阅 **State name** 参数。）状态名称用于，例如：

- 生成代码中的相应变量
- 仿真期间记录状态时作为存储名称的一部分
- 通过线性化模块获得的线性模型中的相应状态

有效状态名称以字母或下划线字符开头，后跟字母数字或下划线字符。

#### 依赖关系

要启用此参数，请将 **Time domain** 设置为 `Continuous-time`。

#### 程序化使用

|  |
| --- |
| **参数：**  `IntegratorContinuousStateAttributes`, `FilterContinuousStateAttributes` |
| **类型：**  character vector |
| **默认：**  `''` |

### **State name** — 离散时间滤波器和积分器状态的名称 空字符串 (默认) | string | character vector

为与积分器或滤波器关联的状态指定唯一名称，用于离散时间 PID 控制器。（有关连续时间 PID 控制器中的状态名称的信息，请参阅 **State name (e.g., 'position')** 参数。）

有效状态名称以字母或下划线字符开头，后跟字母数字或下划线字符。状态名称用于，例如：

- 生成代码中的相应变量
- 仿真期间记录状态时作为存储名称的一部分
- 通过线性化模块获得的线性模型中的相应状态

有关代码生成中状态名称使用的详细信息，请参阅 C Data Code Interface Configuration for Model Interface Elements (Simulink Coder)。

#### 依赖关系

要启用此参数，请将 **Time domain** 设置为 `Discrete-time`。

#### 程序化使用

|  |
| --- |
| **参数：**  `IntegratorStateIdentifier`, `FilterStateIdentifier` |
| **类型：**  string, character vector |
| **默认：**  `""` |

### **State name must resolve to Simulink signal object** — 要求状态名称解析为信号对象 `off` (默认) | `on`

选择此参数以要求离散时间积分器或滤波器状态名称解析为 Simulink signal object。

#### 依赖关系

要为离散时间积分器或滤波器状态启用此参数：

1. 将 **Time domain** 设置为 `Discrete-time`。
2. 为积分器或滤波器 **State name** 指定值。
3. 将模型配置参数 **Signal resolution** 设置为除 `None` 以外的值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `IntegratorStateMustResolveToSignalObject`, `FilterStateMustResolveToSignalObject` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认：** `"off"` |

## 所属库

Simulink / Discrete

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

对于连续时间 PID 控制器（**Time domain** 设置为 `Continuous-time`）：

- 考虑使用 Model Discretizer 将连续时间模块映射到支持代码生成的离散等效模块。要访问 Model Discretizer，请在 **Apps** 选项卡中，在 **Control Systems** 下，单击 **Model Discretizer**。
- 不建议用于生产代码。

对于离散时间 PID 控制器（**Time domain** 设置为 `Discrete-time`）：

- 当放置在触发子系统层次结构内时，取决于绝对时间。
- 在某些条件下，生成代码依赖 `memcpy` 或 `memset` 函数（`string.h`）。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

仅支持离散时间 PID 控制器的定点代码生成（**Time domain** 设置为 `Discrete-time`）。

## 版本历史

**在 R2009b 中引入**

### R2024b：使用新端口从外部指定抗饱和算法

此模块现在允许您使用新的输入端口 **extAW** 从外部指定抗饱和算法。模块还在 **preInt** 输出端口提供积分器之前的信号，您可以将其用作自定义算法的输入。PID controller 模块提供两种内置抗饱和方法，但是，为了解开积分器，这些方法依赖于模块分量之和超过指定的模块输出限值。如果您的应用在 PID controller 模块下游具有饱和或限值，您可以使用新的 **extAW** 和 **preInt** 端口实现自定义抗饱和逻辑。要启用新端口，请在 **Saturation** 选项卡上，选择 **Limit Output**，并将 **Anti-windup Method** 设置为 `external`。

### R2024a：使用来自外部源的导数信号

PID controller 模块现在允许您直接将被控对象信号 *y* 的导数作为模块输入提供。当您的模型中已有该导数信号，并且希望跳过模块内部的导数计算时，这很有帮助。

要启用用于提供导数的输入端口，请选择具有微分作用的控制器类型，并启用 **Use externally sourced derivative** 参数。

### R2022b：当积分器和滤波器初始条件位于饱和限值之外时发出错误

当积分器或滤波器初始条件值位于输出饱和限值之外时，模块现在会发出错误。在以前的版本中，当这些初始条件具有此类值时，模块不会发出错误。

如果此更改影响您的模型，请更新 PID 积分器或滤波器初始条件值，使其位于输出饱和限值内。

### R2021b：`ReferenceBlock` 参数返回不同的路径

从 R2021b 开始，`get_param` 函数为 `ReferenceBlock` 参数返回不同的值。`ReferenceBlock` 参数是所有 Simulink 模块共有的属性，它给出模块链接到的库模块的路径。PID Controller (2DOF) 和 Discrete PID Controller (2DOF) 模块现在链接到 `'slpidlib/PID Controller (2DOF)'`。以前，这些模块链接到 `'pid_lib/PID Controller (2DOF)'`。

此更改不影响任何其他功能或工作流。您仍然可以将以前的路径与 `set_param` 函数一起使用。

### R2020b：`ReferenceBlock` 参数返回不同的路径

从 R2020b 开始，`get_param` 函数为 `ReferenceBlock` 参数返回不同的值。`ReferenceBlock` 参数是所有 Simulink 模块共有的属性，它给出模块链接到的库模块的路径。PID Controller (2DOF) 和 Discrete PID Controller (2DOF) 模块现在链接到 `'pid_lib/PID Controller (2DOF)'`。以前，这些模块链接到 `'simulink/Continuous/PID Controller (2DOF)'`。

此更改不影响任何其他功能或工作流。您仍然可以将以前的路径与 `set_param` 函数一起使用。

## 描述

离散时间或连续时间二自由度 PID 控制器

Discrete PID Controller (2DOF) 模块实现二自由度 PID 控制器（PID、PI 或 PD）。该模块与 **Time domain** 参数设置为 `Discrete-time` 的 PID Controller (2DOF) 模块相同。

该模块基于参考信号与测量的系统输出之间的差值生成输出信号。该模块根据您指定的设定点权重（**b** 和 **c**）为比例和微分作用计算加权差值信号。模块输出是比例、积分和微分作用在相应差值信号上的总和，其中每个作用根据增益参数 **P**、**I** 和 **D** 加权。一阶极点对微分作用进行滤波。

该模块支持多种控制器类型和结构。模块中的可配置选项包括：

- 控制器类型（PID、PI 或 PD）— 请参阅 **Controller** 参数。
- 控制器形式（Parallel 或 Ideal）— 请参阅 **Form** 参数。
- 时间域（离散或连续）— 请参阅 **Time domain** 参数。
- 初始条件和复位触发 — 请参阅 **Source** 和 **External reset** 参数。
- 输出饱和限值和内置抗饱和机制 — 请参阅 **Limit output** 参数。
- 用于无扰控制传递和多回路控制的信号跟踪 — 请参阅 **Enable tracking mode** 参数。

当您更改这些选项时，模块的内部结构会通过激活不同的变体子系统而变化。（请参阅 Implement Variations in Separate Hierarchy Using Variant Subsystems。）要检查模块及其变体子系统的内部结构，请右键单击模块并选择 **Mask** > **Look Under Mask**。

### 控制配置

在一种常见实现中，PID Controller 模块在反馈回路的前馈路径中运行。

对于接受误差信号（设定点与系统输出之间的差值）的单输入模块，请参阅 Discrete PID Controller。

### PID 增益整定

PID 控制器系数和设定点权重可以手动或自动整定。自动整定需要 Simulink® Control Design™ 软件。有关自动整定的详细信息，请参阅 **Select tuning method** 参数。
