---
type: simulink-block
title: 'PI Controller'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Controls / Controllers'
documentation_page: 'picontroller'
documentation_source_path: '../mcb/ref/picontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# PI Controller

## 端口

### 输入

### **Port\_1( u )** — 误差信号输入 标量 | 向量

参考信号与受控系统输出之间的差值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **ydot** — 外部提供的导数 标量 | 向量

*自 R2024a 起*

将对象信号 *y* 的导数直接作为输入提供给该模块。当模型中有可用的导数信号，并且希望跳过模块内部对该导数的计算时，这会很有帮助。

#### 依赖关系

要启用此输入端口，请选择具有微分作用的控制器类型，并启用 **Use externally sourced derivative**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **P** — 比例增益 标量 | 向量

比例增益，由模块外部的来源提供。外部增益输入很有用，例如，当你希望将不同的 PID 参数化映射到该模块的 PID 增益时。你还可以使用外部增益输入来实现增益调度 PID 控制。在增益调度控制中，你通过模型中的逻辑或其他计算确定 PID 系数，并将它们馈送到该模块。

#### 依赖关系

要启用此端口，请将 **Controller parameters Source** 设置为 `external`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **I\*Ts** — 积分增益乘以采样时间 标量 | 向量

积分增益乘以控制器采样时间，由模块外部的来源提供。外部增益输入很有用，例如，当你希望将不同的 PID 参数化映射到该模块的 PID 增益时。你还可以使用外部增益输入来实现增益调度 PID 控制。在增益调度控制中，你通过模型中的逻辑或其他计算确定 PID 系数，并将它们馈送到该模块。

**注意**

PID 整定工具，例如 PID Tuner app 和 Closed-Loop PID Autotuner block，整定的是增益 **I**，而不是 **I\*Ts**。因此，在将从整定工具获得的积分增益值提供给此端口之前，请将其乘以采样时间。

当你使用 **I\*Ts** 而不是 **I** 时，模块执行积分所需的计算更少。这可以改善生成代码的执行时间。

#### 依赖关系

要启用此端口，请将 **Controller parameters Source** 设置为 `external`，将 **Controller** 设置为具有积分作用的控制器类型，并启用 **Use I\*Ts** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **I** — 积分增益 标量 | 向量

积分增益，由模块外部的来源提供。外部增益输入很有用，例如，当你希望将不同的 PID 参数化映射到该模块的 PID 增益时。你还可以使用外部增益输入来实现增益调度 PID 控制。在增益调度控制中，你通过模型中的逻辑或其他计算确定 PID 系数，并将它们馈送到该模块。

当你从外部提供增益时，积分增益的时间变化也会被积分。出现这种结果是因为 PID 增益在该模块内部的实现方式。有关详细信息，请参阅 **Controller parameters Source** 参数。

#### 依赖关系

要启用此端口，请将 **Controller parameters Source** 设置为 `external`，并将 **Controller** 设置为具有积分作用的控制器类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **D** — 微分增益 标量 | 向量

微分增益，由模块外部的来源提供。外部增益输入很有用，例如，当你希望将不同的 PID 参数化映射到该模块的 PID 增益时。你还可以使用外部增益输入来实现增益调度 PID 控制。在增益调度控制中，你通过模型中的逻辑或其他计算确定 PID 系数，并将它们馈送到该模块。

当你从外部提供增益时，微分增益的时间变化也会被微分。出现这种结果是因为 PID 增益在该模块内部的实现方式。有关详细信息，请参阅 **Controller parameters Source** 参数。

#### 依赖关系

要启用此端口，请将 **Controller parameters Source** 设置为 `external`，并将 **Controller** 设置为具有微分作用的控制器类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **N** — 滤波器系数 标量 | 向量

微分滤波器系数，由模块外部的来源提供。外部系数输入很有用，例如，当你希望将不同的 PID 参数化映射到该模块的 PID 增益时。你还可以使用外部输入来实现增益调度 PID 控制。在增益调度控制中，你通过模型中的逻辑或其他计算确定 PID 系数，并将它们馈送到该模块。

#### 依赖关系

要启用此端口，请将 **Controller parameters Source** 设置为 `external`，并将 **Controller** 设置为具有滤波微分作用的控制器类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Reset** — 外部复位触发 标量

用于将积分器和滤波器复位到其初始条件的触发。 **External reset** 参数的值决定复位是在上升信号、下降信号还是电平信号上发生。端口图标指示所选的触发类型。例如，以下图示显示了一个 **External reset** 设置为 `level` 的 PID 模块。

当触发发生时，模块会将积分器和滤波器复位到由 **Integrator Initial condition** 和 **Filter Initial condition** 参数或 **I0** 和 **D0** 端口指定的初始条件。

**注意**

为了符合 Motor Industry Software Reliability Association (MISRA™) 软件标准，你的模型必须使用 Boolean 信号来驱动 PID controller block 的外部复位端口。

#### 依赖关系

要启用此端口，请将 **External reset** 设置为除 `none` 之外的任何值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `Boolean`

### **I0** — 积分器初始条件 标量 | 向量

积分器初始条件，由模块外部的来源提供。

#### 依赖关系

要启用此端口，请将 **Initial conditions Source** 设置为 `external`，并将 **Controller** 设置为具有积分作用的控制器类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **D0** — 滤波器初始条件 标量 | 向量

微分滤波器的初始条件，由模块外部的来源提供。

#### 依赖关系

要启用此端口，请将 **Initial conditions Source** 设置为 `external`，并将 **Controller** 设置为具有微分作用的控制器类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **up** — 输出饱和上限 标量 | 向量

模块输出的上限，由模块外部的来源提供。如果比例、积分和微分作用的加权和超过此端口提供的值，则模块输出保持在该值。

#### 依赖关系

要启用此端口，请选择 **Limit output**，并将输出饱和 **Source** 设置为 `external`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **lo** — 输出饱和下限 标量 | 向量

模块输出的下限，由模块外部的来源提供。如果比例、积分和微分作用的加权和低于此端口提供的值，则模块输出保持在该值。

#### 依赖关系

要启用此端口，请选择 **Limit output**，并将输出饱和 **Source** 设置为 `external`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **TR** — 跟踪信号 标量 | 向量

控制器输出要跟踪的信号。当信号跟踪激活时，跟踪信号与模块输出之间的差值会反馈到积分器输入。信号跟踪对于在两个控制器之间切换的系统中实现无扰控制切换很有用。它也可用于防止多回路控制系统中的模块积分饱和。有关详细信息，请参阅 **Enable tracking mode** 参数。

#### 依赖关系

要启用此端口，请选择 **Enable tracking mode** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **TDTI** — 离散积分器时间 标量

离散积分器时间，作为标量提供给模块。你可以使用自己的离散时间积分器采样时间值，该值定义模块在 Simulink 中或外部硬件上运行时的速率。当该模块在条件执行子系统内使用时，离散时间积分器时间的值应与外部中断的平均采样率匹配。

换句话说，你可以为下面的任何积分器方法指定 `Ts`，使该值与外部中断的平均采样率匹配。在离散时间中，控制器传递函数的微分项为：

D[N1+Nα(z)],

其中 *α*(*z*) 取决于你使用此参数指定的积分器方法。

`Forward Euler`
:   α(z)=Tsz−1.

`Backward Euler`
:   α(z)=Tszz−1.

`Trapezoidal`
:   α(z)=Ts2z+1z−1.

有关离散时间积分的详细信息，请参阅 Discrete-Time Integrator block 参考页。有关条件执行子系统的详细信息，请参阅 Conditionally Executed Subsystems Overview。

#### 依赖关系

要启用此端口，请将 **Time Domain** 设置为 `Discrete-time`，并选择 **PID Controller is inside a conditionally executed subsystem** 选项。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **extAW** — 外部抗积分饱和算法 标量 | 向量

*自 R2024b 起*

在此端口指定自定义抗积分饱和算法。该模块提供两种内置抗积分饱和方法，但是，为了对积分器进行退饱和，这些方法依赖于模块各分量之和超过指定的模块输出限制。如果你的应用在 PI Controller 模块下游存在饱和或限制，你可以使用 **extAW** 输入端口来实现自定义抗积分饱和逻辑。该模块还在 **preInt** 输出端口提供积分器之前的信号，你可以使用它来实现自定义算法。

#### 依赖关系

要启用此端口，请在 **Saturation** 选项卡上，选择 **Limit output**，并将 **Anti-windup Method** 设置为 `external`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 输出

### **Port\_1( y )** — 控制器输出 标量 | 向量

控制器输出，通常基于输入信号、输入信号的积分和输入信号的导数的和，并由比例、积分和微分增益参数加权。一阶极点对微分作用进行滤波。控制器信号中出现哪些项取决于你为 **Controller** 参数选择的内容。当前设置的基本控制器传递函数显示在模块参数的 **Compensator formula** 部分以及掩码下。其他参数会修改模块输出，例如由 **Upper Limit** 和 **Lower Limit** 饱和参数指定的饱和限制。

当任何输入是向量信号时，控制器输出是向量信号。在这种情况下，该模块充当 *N* 个独立 PID 控制器，其中 *N* 是输入向量中的信号数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **preInt** — 积分器前信号 标量 | 向量

*自 R2024b 起*

该模块在此端口输出积分器之前的信号。将此信号用作你在 **extAW** 端口提供的自定义抗积分饱和算法的输入。

#### 依赖关系

要启用此端口，请在 **Saturation** 选项卡上，选择 **Limit output**，并将 **Anti-windup Method** 设置为 `external`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **Controller** — 控制器类型 `PI`（默认） | `PID` | `PD` | `P` | `I`

指定控制器中包含比例、积分和微分项中的哪些项。

`PID`
:   比例、积分和微分作用。

`PI`
:   仅比例和积分作用。

`PD`
:   仅比例和微分作用。

`P`
:   仅比例作用。

`I`
:   仅积分作用。

**提示**

当前设置的控制器传递函数显示在模块参数的 **Compensator formula** 部分以及掩码下。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Controller` |
| **类型：** string, character vector |
| **值：** `"PID"`, `"PI"`, `"PD"`, `"P"`, `"I"` |
| **默认值：** `"PI"` |

### **Form** — 控制器结构 `Parallel`（默认） | `Ideal`

指定控制器结构是并联还是理想。

`Parallel`
:   控制器输出是比例、积分和微分作用的和，分别由 **P**、**I** 和 **D** 独立加权。例如，对于连续时间并联形式 PID 控制器，传递函数为：

    Cpar(s)=P+I(1s)+D(Nss+N).

    对于离散时间并联形式控制器，传递函数为：

    Cpar(z)=P+Iα(z)+D[N1+Nβ(z)],

    其中 **Integrator method** 和 **Filter method** 参数分别确定 *α*(*z*) 和 *β*(*z*)。

`Ideal`
:   比例增益 **P** 作用于所有作用之和。例如，对于连续时间理想形式 PID 控制器，传递函数为：

    Cid(s)=P[1+I(1s)+D(Nss+N)].

    对于离散时间理想形式控制器，传递函数为：

    Cid(z)=P[1+Iα(z)+DN1+Nβ(z)],

    其中 **Integrator method** 和 **Filter method** 参数分别确定 *a*(*z*) 和 *b*(*z*)。

    **提示**

    当前设置的控制器传递函数显示在模块参数的 **Compensator formula** 部分以及掩码下。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Controller` |
| **类型：** string, character vector |
| **值：** `"Parallel"`, `"Ideal"` |
| **默认值：** `"Parallel"` |

### **时域** — 指定离散时间或连续时间控制器 `Discrete-time` (默认) | `Continuous-time`

当选择 `Discrete-time` 时，建议为模块指定显式采样时间。请参阅 **采样时间（继承时为 -1）** 参数。选择 `Discrete-time` 还会启用 **积分器方法** 和 **滤波器方法** 参数。

当 PID Controller 模块位于具有同步状态控制的模型中（请参阅 State Control (HDL Coder) 模块）时，不能选择 `Continuous-time`。

#### 编程用法

|  |
| --- |
| **模块参数：** `TimeDomain` |
| **类型：** string, character vector |
| **值：** `"Continuous-time"`, `"Discrete-time"` |
| **默认：** `"Discrete-time"` |

### **PID Controller 位于条件执行子系统内** — 启用离散积分器时间端口 `off` (默认) | `on`

对于离散时间 PID 控制器，启用离散时间积分器端口以使用您自己的离散时间积分器采样时间值。为确保正确积分，请使用 `TDTI` 端口提供 Δt 的标量值，以实现准确的离散时间积分。

#### 依赖关系

要启用此参数，请将 **时域** 设置为 `Discrete-time`。

#### 编程用法

|  |
| --- |
| **模块参数：** `UseExternalTs` |
| **类型：** string, character vector |
| **值：** `"on"`, `"off"` |
| **默认：** `"off"` |

### **采样时间（继承时为 -1）** — 采样之间的离散间隔 –1 (默认) | positive scalar

通过输入正标量值（例如 0.1）来指定采样时间。默认离散采样时间 –1 表示模块从上游模块继承其采样时间。但是，建议显式设置控制器采样时间，特别是在您预期上游模块的采样时间会变化时。控制器系数 P、I、D 和 N 的效果取决于采样时间。因此，对于给定的一组系数值，更改采样时间会改变控制器的性能。

有关详细信息，请参阅 Specify Sample Time。

要实现连续时间控制器，请将 **时域** 设置为 `Continuous-time`。

**提示**

如果要使用外部指定的采样时间或可变采样时间运行模块，请将此参数设置为 –1，并将模块放入 Triggered Subsystem。然后，以所需的采样时间触发该子系统。

#### 依赖关系

要启用此参数，请将 **时域** 设置为 `Discrete-time`。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** scalar |
| **值：** `-1`, positive scalar |
| **默认：** `-1` |

### **积分器方法** — 在离散时间控制器中计算积分的方法 `Forward Euler` (默认) | `Backward Euler` | `Trapezoidal`

在离散时间中，控制器传递函数的积分项为 *Iα*(*z*)，其中 *α*(*z*) 取决于您用此参数指定的积分器方法。

`Forward Euler`
:   前向矩形（左侧）逼近，

    α(z)=Tsz−1.

    此方法最适合小采样时间，此时 Nyquist 极限相对于控制器带宽较大。对于较大的采样时间，`Forward Euler` 方法可能导致不稳定，即使离散化的是连续时间稳定的系统。

`Backward Euler`
:   后向矩形（右侧）逼近，

    α(z)=Tszz−1.

    `Backward Euler` 方法的一个优点是，使用此方法离散化稳定的连续时间系统总是产生稳定的离散时间结果。

`Trapezoidal`
:   双线性逼近，

    α(z)=Ts2z+1z−1.

    `Trapezoidal` 方法的一个优点是，使用此方法离散化稳定的连续时间系统总是产生稳定的离散时间结果。在所有可用的积分方法中，`Trapezoidal` 方法使离散化系统的频域特性与相应连续时间系统之间的匹配最接近。

    **提示**

    当前设置的控制器公式显示在模块参数的 **补偿器公式** 部分以及掩码下。

**注意**

对于 `BackwardEuler` 或 `Trapezoidal` 方法，如果满足以下任一条件，则不能为模块生成 HDL 代码：

- **限制输出** 已选择，并且 **抗饱和方法** 不是 `none`。
- **启用跟踪模式** 已选择。

有关离散时间积分的详细信息，请参阅 Discrete-Time Integrator 模块参考页。

#### 依赖关系

要启用此参数，请将 **时域** 设置为 `Discrete-time`，并将 **控制器** 设置为具有积分作用的控制器类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `IntegratorMethod` |
| **类型：** string, character vector |
| **值：** `"Forward Euler"`, `"Backward Euler"`, `"Trapezoidal"` |
| **默认：** `"Forward Euler"` |

### **滤波器方法** — 在离散时间控制器中计算微分的方法 `Forward Euler` (默认) | `Backward Euler` | `Trapezoidal`

在离散时间中，控制器传递函数的微分项为：

D[N1+Nα(z)],

其中 *α*(*z*) 取决于您用此参数指定的滤波器方法。

`Forward Euler`
:   前向矩形（左侧）逼近，

    α(z)=Tsz−1.

    此方法最适合小采样时间，此时 Nyquist 极限相对于控制器带宽较大。对于较大的采样时间，`Forward Euler` 方法可能导致不稳定，即使离散化的是连续时间稳定的系统。

`Backward Euler`
:   后向矩形（右侧）逼近，

    α(z)=Tszz−1.

    `Backward Euler` 方法的一个优点是，使用此方法离散化稳定的连续时间系统总是产生稳定的离散时间结果。

`Trapezoidal`
:   双线性逼近，

    α(z)=Ts2z+1z−1.

    `Trapezoidal` 方法的一个优点是，使用此方法离散化稳定的连续时间系统总是产生稳定的离散时间结果。在所有可用的积分方法中，`Trapezoidal` 方法使离散化系统的频域特性与相应连续时间系统之间的匹配最接近。

    **提示**

    当前设置的控制器公式显示在模块参数的 **补偿器公式** 部分以及掩码下。

有关离散时间积分的详细信息，请参阅 Discrete-Time Integrator 模块参考页。

#### 依赖关系

要启用此参数，请将 **时域** 设置为 `Discrete-time`，并启用 **使用滤波微分**。

#### 编程用法

|  |
| --- |
| **模块参数：** `FilterMethod` |
| **类型：** string, character vector |
| **值：** `"Forward Euler"`, `"Backward Euler"`, `"Trapezoidal"` |
| **默认：** `"Forward Euler"` |

### 主要

### **来源** — 控制器增益和滤波器系数的来源 `external` (默认) | `internal`

为参数启用外部输入允许您在模块外部计算 PID 增益和滤波器系数，并将它们作为信号输入提供给模块。

`internal`
:   使用模块参数 **P**、**I**（或 **I\*Ts**）、**D** 和 **N** 指定控制器增益和滤波器系数。

`external`
:   使用模块输入在外部指定 PID 增益和滤波器系数。对于当前控制器类型所需的每个参数，模块上都会出现一个附加输入端口。

    例如，当您想将不同的 PID 参数化映射到模块的 PID 增益时，外部增益输入很有用。您还可以使用外部增益输入来实现增益调度 PID 控制。在增益调度控制中，您通过模型中的逻辑或其他计算确定 PID 增益，并将它们馈送到模块。

    当您从外部提供增益时，积分增益值和微分增益值的时间变化将分别被积分和微分。出现此结果是因为在连续时间和离散时间中，增益都在积分或微分之前应用于信号。例如，对于具有外部输入的连续时间 PID 控制器，积分器项的实现如下图所示。

    在模块内部，输入信号 *u* 在积分之前乘以外部提供的积分器增益 *I*。此实现得到：

    yi=∫uI dt.

    因此，积分器增益包含在积分中。类似地，在模块的微分项中，乘以微分增益先于微分，这导致微分增益 *D* 被微分。

#### 编程用法

|  |
| --- |
| **模块参数：** `ControllerParametersSource` |
| **类型：** string, character vector |
| **值：** `"internal"`, `"external"` |
| **默认：** `"external"` |

### **比例 (P)** — 比例增益 1 (默认) | scalar | vector

为比例增益指定一个有限实增益值。当 **控制器形式** 为：

- `Parallel` — 比例作用独立于积分作用和微分作用。例如，对于连续时间并联 PID 控制器，传递函数为：

  Cpar(s)=P+I(1s)+D(Nss+N).

  对于离散时间并联形式控制器，传递函数为：

  Cpar(z)=P+Iα(z)+D[N1+Nβ(z)],

  其中 **积分器方法** 和 **滤波器方法** 参数分别确定 *α*(*z*) 和 *β*(*z*)。
- `Ideal` — 比例增益乘以积分项和微分项。例如，对于连续时间理想 PID 控制器，传递函数为：

  Cid(s)=P[1+I(1s)+D(Nss+N)].

  对于离散时间理想形式控制器，传递函数为：

  Cid(z)=P[1+Iα(z)+DN1+Nβ(z)],

  其中 **积分器方法** 和 **滤波器方法** 参数分别确定 *α*(*z*) 和 *β*(*z*)。

#### 依赖关系

要启用此参数，请在 **主要** 选项卡中，将控制器参数 **来源** 设置为 `internal`，并将 **控制器** 设置为 `PID`、`PD`、`PI` 或 `P`。

#### 编程用法

|  |
| --- |
| **模块参数：** `P` |
| **类型：** scalar, vector |
| **默认：** 1 |

**可调：** Yes

### **积分 (I)** — 积分增益 1 (默认) | scalar | vector

为积分增益指定一个有限实增益值。

**可调：** Yes

#### 依赖关系

要启用此参数，请在 **主要** 选项卡中，将控制器参数 **来源** 设置为 `internal`，并将 **控制器** 设置为具有积分作用的类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `I` |
| **类型：** scalar, vector |
| **默认：** 1 |

### **积分 (I\*Ts)** — 积分增益乘以采样时间 1 (默认) | scalar | vector

为积分增益乘以采样时间指定一个有限实增益值。

**注意**

PID 整定工具（例如 PID Tuner app 和 Closed-Loop PID Autotuner 模块）整定增益 **I**，而不是 **I\*Ts**。因此，在将整定工具获得的积分增益值写入此参数之前，请将其乘以采样时间。

当您使用 **I\*Ts** 而不是 **I** 时，模块执行积分所需的计算更少。这会改善生成代码的执行时间。

**可调：** No

#### 依赖关系

要启用此参数，请在 **主要** 选项卡中，将控制器参数 **来源** 设置为 `internal`，将 **控制器** 设置为具有积分作用的类型，并启用 **使用 I\*Ts** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `I` |
| **类型：** scalar, vector |
| **默认：** 1 |

### **使用 I\*Ts** — 使用积分增益乘以采样时间 `on` (默认) | `off`

对于具有积分作用的离散时间控制器，模块将积分增益作为输入，并在内部将其乘以采样时间，作为执行积分的一部分。您可以启用此参数，以输入形式指定积分增益乘以采样时间（**I\*Ts**）来代替积分增益（**I**）。这样做可减少内部计算次数，并且当您想改善生成代码的执行时间时很有用。

#### 依赖关系

要启用此参数，请将 **控制器** 设置为具有积分作用的控制器类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `UseKiTs` |
| **类型：** string, character vector |
| **值：** `"on"`, `"off"` |
| **默认：** `"on"` |

### **微分 (D)** — 微分增益 0 (默认) | scalar | vector

为微分增益指定一个有限实增益值。

**可调：** Yes

#### 依赖关系

要启用此参数，请在 **主要** 选项卡中，将控制器参数 **来源** 设置为 `internal`，并将 **控制器** 设置为 `PID` 或 `PD`。

#### 编程用法

|  |
| --- |
| **模块参数：** `D` |
| **类型：** scalar, vector |
| **默认：** 0 |

### **使用外部提供的微分** — 在模块输入端口指定微分 `off` (默认) | `on`

*自 R2024a 起*

选择此选项可直接将被控对象信号 *y* 的微分指定为模块的输入 **ydot**。当您的模型中已有微分信号并希望跳过模块内部的微分计算时，这很有帮助。

#### 依赖关系

要启用此选项，请选择具有微分作用的控制器类型。

### **使用滤波微分** — 对微分项应用滤波器 `on` (默认) | `off`

仅对于离散时间 PID 控制器，清除此选项可将滤波微分替换为未滤波的离散时间微分器。这样做后，控制器传递函数的微分项变为：

Dz−1zTs.

对于连续时间 PID 控制器，微分项始终经过滤波。

#### 依赖关系

要启用此参数，请将 **时域** 设置为 `Discrete-time`，并将 **控制器** 设置为具有微分作用的类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `UseFilter` |
| **类型：** string, character vector |
| **值：** `"on"`, `"off"` |
| **默认：** `"on"` |

### **滤波器系数 (N)** — 微分滤波器系数 100 (默认) | scalar | vector

为滤波器系数指定一个有限实增益值。滤波器系数确定模块微分作用中滤波器的极点位置。滤波器极点的位置取决于 **时域** 参数。

- 当 **时域** 为 `Continuous-time` 时，极点位置为 `s = -N`。
- 当 **时域** 为 `Discrete-time` 时，极点位置取决于 **滤波器方法** 参数。

  | 滤波器方法 | 滤波器极点位置 |
  | --- | --- |
  | `Forward Euler` | zpole=1−NTs |
  | `Backward Euler` | zpole=11+NTs |
  | `Trapezoidal` | zpole=1−NTs/21+NTs/2 |

模块不支持 `N = Inf`（理想未滤波微分）。当 **时域** 为 `Discrete-time` 时，您可以清除 **使用滤波微分** 以移除微分滤波器。

#### 依赖关系

要启用此参数，请在 **主要** 选项卡中，将控制器参数 **来源** 设置为 `internal`，并将 **控制器** 设置为 `PID` 或 `PD`。

#### 编程用法

|  |
| --- |
| **模块参数：** `N` |
| **类型：** scalar, vector |
| **默认：** 100 |

**可调：** Yes

### **选择调参方法** — 用于自动调节控制器系数的工具 `Transfer Function Based (PID Tuner App)`（默认）| `Frequency Response Based`

如果您拥有 Simulink Control Design 软件，则可以自动调节 PID 系数。为此，使用此参数选择调参工具，然后点击 **Tune**。

`Transfer Function Based (PID Tuner App)`
:   使用 PID Tuner，它允许您在检查相关系统响应以验证性能的同时，交互式地调节 PID 系数。默认情况下，PID Tuner 使用被控对象模型的线性化。对于无法线性化的模型，您可以基于从仿真或测量响应数据估计出的被控对象模型来调节 PID 系数。有关详细信息，请参阅 Introduction to Model-Based PID Tuning in Simulink (Simulink Control Design)。

`Frequency Response Based`
:   使用 Frequency Response Based PID Tuner，它基于通过仿真获得的频率响应估计数据来调节 PID 控制器系数。此调参方法对于不可线性化或线性化为零的被控对象特别有用。有关详细信息，请参阅 Design PID Controller from Plant Frequency-Response Data (Simulink Control Design)。

这两种调参方法都假定单回路控制配置。Simulink Control Design 软件还包含适用于更复杂配置的其他调参方法。有关调节 PID Controller 模块的其他方式的信息，请参阅 Choose a Control Design Approach (Simulink Control Design)。

### **启用过零检测** — 在复位时以及进入或离开饱和状态时检测过零 `on`（默认）| `off`

过零检测可以准确定位信号不连续点，而无需采用可能导致仿真时间过长的过小时间步长。如果您在 PID Controller 模块中选择 **限制输出** 或激活 **外部复位**，则激活过零检测可以减少仿真中的计算时间。选择此参数将在以下情况下激活过零检测：

- 在初始状态复位时
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

### **来源** — 积分器和导数初始条件的来源 `external`（默认）| `internal`

Simulink 使用初始条件在仿真开始时或指定的触发事件时初始化积分器和导数滤波器（或未滤波导数）输出。（请参阅 **外部复位** 参数。）这些初始条件决定模块的初始输出。使用此参数选择如何向模块提供初始条件值。

`internal`
:   使用 **积分器初始条件** 和 **滤波器初始条件** 参数指定初始条件。如果未选择 **使用滤波导数**，则使用 **微分器** 参数为未滤波微分器指定初始条件，而不是滤波器初始条件。

`external`
:   使用模块输入从外部指定初始条件。模块上会出现附加输入端口 **Io** 和 **Do**。如果未选择 **使用滤波导数**，则在 **Do** 处提供未滤波微分器的初始条件，而不是滤波器初始条件。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialConditionSource` |
| **类型：** string, character vector |
| **值：** `"internal"`, `"external"` |
| **默认：** `"external"` |

### **积分器** — 积分器初始条件 0（默认）| scalar | vector

Simulink 使用积分器初始条件在仿真开始时或指定的触发事件时初始化积分器（请参阅 **外部复位**）。积分器初始条件和滤波器初始条件决定 PID Controller 模块的初始输出。

积分器初始条件不能为 `NaN` 或 `Inf`。

#### 依赖关系

要使用此参数，请在 **初始化** 选项卡中，将 **来源** 设置为 `internal`，并将 **控制器** 设置为具有积分作用的类型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialConditionForIntegrator` |
| **类型：** scalar, vector |
| **默认：** 0 |

### **滤波器** — 滤波器初始条件 0（默认）| scalar | vector

Simulink 使用滤波器初始条件在仿真开始时或指定的触发事件时初始化导数滤波器（请参阅 **外部复位**）。积分器初始条件和滤波器初始条件决定 PID Controller 模块的初始输出。

滤波器初始条件不能为 `NaN` 或 `Inf`。

#### 依赖关系

要使用此参数，请在 **初始化** 选项卡中，将 **来源** 设置为 `internal`，并使用具有导数滤波器的控制器。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialConditionForFilter` |
| **类型：** scalar, vector |
| **默认：** 0 |

### **微分器** — 未滤波导数的初始条件 0（默认）| scalar | vector

当您使用未滤波导数时，Simulink 使用此参数在仿真开始时或指定的触发事件时初始化微分器（请参阅 **外部复位**）。积分器初始条件和导数初始条件决定 PID Controller 模块的初始输出。

导数初始条件不能为 `NaN` 或 `Inf`。

#### 依赖关系

要使用此参数，请将 **时间域** 设置为 `Discrete-time`，清除 **使用滤波导数** 复选框，并在 **初始化** 选项卡中将 **来源** 设置为 `internal`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DifferentiatorICPrevScaledInput` |
| **类型：** scalar, vector |
| **默认：** 0 |

### **初始条件设置** — 应用初始条件的位置 `Auto`（默认）| `Output`

使用此参数指定是将 **积分器初始条件** 和 **滤波器初始条件** 参数应用于相应的模块状态还是输出。您只能通过命令行更改此参数，使用 `set_param` 设置模块的 `InitialConditionSetting` 参数。

`Auto`
:   除模块位于触发子系统或函数调用子系统中且启用了简化初始化模式的情况外，在所有情况下使用此选项。

`Output`
:   当模块位于触发子系统或函数调用子系统中且启用了简化初始化模式时，使用此选项。

有关 **初始条件设置** 参数的详细信息，请参阅 Discrete-Time Integrator 模块。

此参数只能通过程序化使用访问。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialConditionSetting` |
| **类型：** string, character vector |
| **值：** `"Auto"`, `"Output"` |
| **默认：** `"Auto"` |

### **外部复位** — 用于复位积分器和滤波器值的触发 `level`（默认）| `none` | `rising` | `falling` | `either`

指定使模块将积分器和滤波器复位到初始条件的触发条件。（如果未选择 **使用滤波导数**，则该触发会将积分器和微分器复位到初始条件。）选择除 `none` 以外的任何选项都会启用模块上的 **Reset** 端口，用于外部复位信号。

`none`
:   积分器和滤波器（或微分器）输出在仿真开始时设置为初始条件，并且在仿真期间不复位。

`rising`
:   当复位信号具有上升沿时，复位输出。

`falling`
:   当复位信号具有下降沿时，复位输出。

`either`
:   当复位信号上升或下降时，复位输出。

`level`
:   当复位信号满足以下任一情况时，复位输出：

    - 在当前时间步非零
    - 在上一时间步非零，但在当前时间步变为零

    此选项在复位信号非零时将输出保持为初始条件。

#### 依赖关系

要启用此参数，请将 **控制器** 设置为具有导数或积分作用的类型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ExternalReset` |
| **类型：** string, character vector |
| **值：** `"none"`, `"rising"`, `"falling"`, `"either"`, `"level"` |
| **默认：** `"level"` |

### **线性化时忽略复位** — 强制线性化忽略复位 `off`（默认）| `on`

选择此项可强制 Simulink 和 Simulink Control Design 线性化命令忽略 **外部复位** 参数中指定的任何复位机制。忽略复位状态允许您围绕工作点对模型进行线性化，即使该工作点会导致模块复位。

#### 程序化使用

|  |
| --- |
| **模块参数：** `IgnoreLimit` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认：** `"off"` |

### **启用跟踪模式** — 激活信号跟踪 `off`（默认）| `on`

信号跟踪允许模块输出跟随您在 **TR** 端口提供的跟踪信号。当信号跟踪激活时，跟踪信号与模块输出之间的差值以增益 `Kt` 反馈到积分器输入端，增益 `Kt` 由 **跟踪增益 (Kt)** 参数指定。信号跟踪有多种应用，包括无扰控制切换和避免多回路控制结构中的积分饱和。

#### 无扰控制切换

使用信号跟踪在两个控制器之间切换的系统中实现无扰控制切换。假设您要在 PID 控制器和另一个控制器之间转移控制。为此，将控制器输出连接到 **TR** 输入，如下图所示。

有关详细信息，请参阅 Bumpless Control Transfer。

#### 多回路控制

使用信号跟踪在多回路控制方法中防止模块积分饱和，如下面的模型所示。

Inner Loop 子系统包含下图所示的模块。

由于 PID 控制器跟踪内回路的输出，其输出永远不会超过饱和的内回路输出。有关更多详细信息，请参阅 Prevent Block Windup in Multiloop Control。

#### 依赖关系

要启用此参数，请将 **控制器** 设置为具有积分作用的类型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TrackingMode` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认：** `"off"` |

### **跟踪系数 (Kt)** — 信号跟踪反馈环路的增益 1（默认）| scalar

当您选择 **启用跟踪模式** 时，信号 **TR** 与模块输出之间的差值以增益 `Kt` 反馈到积分器输入端。使用此参数指定该反馈环路中的增益。

#### 依赖关系

要启用此参数，请选择 **启用跟踪模式**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Kt` |
| **类型：** scalar |
| **默认：** 1 |

### 饱和

#### 输出饱和

### **限制输出** — 将模块输出限制为指定的饱和值 `on`（默认）| `off`

激活此选项会限制模块输出，因此您不需要在控制器之后使用单独的 Saturation 模块。它还允许您激活模块内置的抗积分饱和机制（请参阅 **抗积分饱和方法** 参数）。使用 **下限** 和 **上限** 参数指定输出饱和限值。您也可以将饱和限值作为模块输入端口从外部指定。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LimitOutput` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认：** `"on"` |

### **来源** — 输出饱和限值的来源 `internal`（默认）| `external`

使用此参数指定如何提供模块输出的上限和下限饱和限值。

`internal`
:   使用 **上限** 和 **下限** 参数指定输出饱和限值。

`external`
:   使用模块输入端口从外部指定输出饱和限值。模块上会出现附加输入端口 **up** 和 **lo**。您可以使用这些输入端口实现由 Simulink 模型中的逻辑或其他计算确定并传递给模块的输出上限和下限饱和限值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SatLimitsSource` |
| **类型：** string, character vector |
| **值：** `"internal"`, `"external"` |
| **默认：** `"internal"` |

### **上限** — 模块输出的上限饱和限值 1（默认）| scalar

指定模块输出的上限。每当比例、积分和微分作用的加权和超过该值时，模块输出保持在 **上限饱和限值**。

#### 依赖关系

要启用此参数，请选择 **限制输出**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `UpperSaturationLimit` |
| **类型：** scalar |
| **默认：** 1 |

### **下限** — 模块输出的下限饱和限值 –1（默认）| scalar

指定模块输出的下限。每当比例、积分和微分作用的加权和低于该值时，模块输出保持在 **下限饱和限值**。

#### 依赖关系

要启用此参数，请选择 **限制输出**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LowerSaturationLimit` |
| **类型：** scalar |
| **默认：** –1 |

### **线性化时忽略饱和** — 强制线性化忽略输出限值 `on`（默认）| `off`

强制 Simulink 和 Simulink Control Design 线性化命令忽略 **上限** 和 **下限** 参数中指定的模块输出限值。忽略输出限值允许您围绕工作点对模型进行线性化，即使该工作点会导致模块超出输出限值。

#### 依赖关系

要启用此参数，请选择 **限制输出** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LinearizeAsGain` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认：** `"on"` |

### **Anti-windup method** — 积分器抗积分饱和方法 `clamping`（默认） | `none` | `back-calculation` | `external`

当您选择 **Limit output** 且控制器各分量的加权和超过指定的输出限值时，模块输出保持在指定限值。然而，积分器输出可能继续增长（积分饱和），从而增大模块输出与模块各分量之和之间的差。换言之，即使输出看起来受饱和限值约束，模块内部信号也可能是无界的。如果没有防止积分饱和的机制，可能出现两种结果：

- 如果输入信号的符号从不改变，积分器继续积分直到溢出。溢出值是积分器输出数据类型的最大值或最小值。
- 如果输入信号在加权和已增长超过输出限值后改变符号，则可能需要很长时间才能使积分器退饱和，并使加权和回到模块饱和限值内。

在任一情况下，控制器性能都可能变差。若没有抗积分饱和机制来抵消饱和效应，可能必须对控制器进行去调谐（例如，通过降低控制器增益），导致控制器响应迟缓。为避免此问题，请使用此参数激活抗积分饱和机制。

`none`
:   不使用抗积分饱和机制。

`back-calculation`
:   当模块输出饱和时，通过将饱和与未饱和控制信号之差反馈到积分器，使积分器退饱和。下图表示连续时间控制器的反算反馈电路。要查看您的控制器配置的实际反馈电路，请右键单击模块并选择 **Mask** > **Look Under Mask**。

    使用 **Back-calculation coefficient (Kb)** 参数指定抗积分饱和反馈电路的增益。通常将 `Kb = I` 设为令人满意的值，或者对于带微分作用的控制器，设为 `Kb = sqrt(I*D)`。反算对于具有相对大死区时间的被控对象可能有效 [1]。

`clamping`
:   当模块各分量之和超过输出限值且积分器输出与模块输入具有相同符号时，积分停止。当模块各分量之和超过输出限值且积分器输出与模块输入符号相反时，积分恢复。Clamping 有时称为条件积分。

    Clamping 对于具有相对小死区时间的被控对象可能有用，但对于大死区时间可能产生较差的瞬态响应 [1]。

`external` *（自 R2024b 起）*
:   内置抗积分饱和方法依赖模块各分量之和超过指定的模块输出限值。如果您的应用在 PI Controller 模块下游存在饱和或限幅，您可以使用 **extAW** 输入端口实现自定义抗积分饱和逻辑。该模块还在 **preInt** 输出端口提供积分器之前的信号，您可以将其用作自定义算法的输入。

#### 依赖关系

要启用此参数，请选择 **Limit output** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `AntiWindupMode` |
| **类型：** string, character vector |
| **值：** `"none"`, `"back-calculation"`, `"clamping"` |
| **默认：** `"clamping"` |

### **Back-calculation coefficient (Kb)** — 抗积分饱和反馈环路的增益系数 1（默认） | scalar

`back-calculation` 抗积分饱和方法在模块输出饱和时使积分器退饱和。它通过将饱和与未饱和控制信号之差反馈到积分器来实现。使用 **Back-calculation coefficient (Kb)** 参数指定抗积分饱和反馈电路的增益。有关详细信息，请参阅 **Anti-windup method** 参数。

#### 依赖关系

要启用此参数，请选择 **Limit output** 参数，并将 **Anti-windup method** 参数设置为 `back-calculation`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Kb` |
| **类型：** scalar |
| **默认：** 1 |

#### 积分器饱和

### **Limit Output** — 将积分器输出限制在指定的饱和限值内 `off`（默认） | `on`

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

### **Upper limit** — 积分器的上限饱和限值 `Inf`（默认） | scalar

指定积分器输出的上限。当积分器输出否则将超过此值时，它保持在该值。

#### 依赖关系

要启用此参数，请在 **Integrator saturation** 下选择 **Limit output**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `UpperIntegratorSaturationLimit` |
| **类型：** scalar |
| **默认：** `Inf` |

### **Lower limit** — 积分器的下限饱和限值 `-Inf`（默认） | scalar

指定积分器输出的下限。当积分器输出否则将低于此值时，它保持在该值。

#### 依赖关系

要启用此参数，请在 **Integrator saturation** 下选择 **Limit output**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LowerIntegratorSaturationLimit` |
| **类型：** scalar |
| **默认：** `-Inf` |

### 数据类型

此选项卡中的参数主要用于使用 Fixed-Point Designer™ 进行定点代码生成。它们定义生成代码时与模块关联的数值量如何存储和处理。

如果您需要为定点代码生成配置数据类型，请单击 **Open Fixed-Point Tool** 并使用该工具配置此选项卡中的其余参数。有关使用 Fixed-Point Tool 的信息，请参阅 Autoscaling Data Objects Using the Fixed-Point Tool (Fixed-Point Designer)。

使用 Fixed-Point Tool 后，如有必要，您可以使用此选项卡中的参数调整定点数据类型设置。对于与模块关联的每个量，您可以指定：

- 浮点或定点数据类型，包括数据类型是否从模块中的上游值继承。
- 该量的最小值和最大值，它们确定该量如何缩放以用于定点表示。

如需帮助选择适当的值，请单击  打开相应量的 Data Type Assistant。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

Data Types 选项卡中列出的具体量取决于您如何配置 PID controller 模块。通常，您可以为以下类型的量配置数据类型：

- Product output — 存储模块掩码下执行的乘法结果。例如，**P product output** 存储增益模块的输出，该模块将模块输入与比例增益 **P** 相乘。
- Parameter — 存储数值模块参数的值，例如 **P**、**I** 或 **D**。
- Block output — 存储位于 PID controller 模块掩码下的模块的输出。例如，使用 **Integrator output** 指定名为 Integrator 的模块输出的数据类型。此模块位于 Integrator 子系统中的掩码下，并计算控制器作用的积分项。
- Accumulator — 存储与求和模块关联的值。例如，**SumI2 Accumulator** 设置与求和模块 SumI2 关联的累加器的数据类型。此模块位于 Anti-Windup 子系统的 Back Calculation 子系统中的掩码下。

通常，您可以通过查看 PID Controller 模块掩码下并检查其子系统，找到与任何列出的参数关联的模块。您还可以使用 Model Explorer 在掩码下搜索列出的参数名称，例如 `SumI2`。（请参阅 Model Explorer。）

**匹配输入和内部数据类型**

默认情况下，乘积输出和模块输出的数据类型设置为 `Inherit: Same as first input`。使用此设置，模块将这些信号的数据类型设置为其第一个输入信号的数据类型。

当数据类型设置为 `Inherit: Inherit via internal rule` 时，Simulink 会选择数据类型以平衡数值精度、性能和生成的代码大小，同时考虑嵌入式目标硬件的属性。

在某些条件下，模块内的数据类型之间可能发生不兼容。例如，在连续时间中，掩码下的 Integrator 模块只能接受 `double` 类型的信号。如果模块输入信号是无法转换为 `double` 的类型，例如 `uint16`，则类型继承的内部规则会在您生成代码时生成错误。

为避免此类错误，您可以使用 Data Types 设置强制进行数据类型转换。例如，您可以显式将 **P product output**、**I product output** 和 **D product output** 设置为 `double`，确保到达连续时间积分器的信号为 `double` 类型。

通常，不建议在代码生成应用中将该模块用于连续时间。但是，如果您将某些值显式设置为与模块内下游信号约束不兼容的数据类型，离散时间中也可能发生类似的数据类型错误。在这种情况下，使用 Data Types 设置确保所有数据类型在内部兼容。

#### 定点运算参数

### **Integer rounding mode** — 定点运算的舍入模式 `Simplest`（默认） | `Floor` | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** character vector |
| **值：** `'Ceiling'` | `'Convergent'` | `'Floor'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |
| **默认：** `'Simplest'` |

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认） | `on`

指定溢出是饱和还是回绕。

- `off` — 溢出回绕到该数据类型可以表示的相应值。

  例如，数字 130 无法容纳在 signed 8-bit integer 中，并回绕为 -126。
- `on` — 溢出饱和到该数据类型可以表示的最小值或最大值。

  例如，与 signed 8-bit integer 相关的溢出可以饱和为 -128 或 127。

**提示**

- 当您的模型可能溢出并且您希望在生成的代码中显式提供饱和保护时，考虑选中此复选框。
- 当您希望优化生成的代码效率时，考虑清除此复选框。

  清除此复选框还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors。
- 选中此复选框时，饱和应用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SaturateOnIntegerOverflow` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认） | `on`

选择此参数以防止定点工具覆盖您在此模块上指定的数据类型。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### 状态属性

此选项卡中的参数主要用于代码生成。

### **State name (e.g., 'position')** — 连续时间滤波器和积分器状态的名称 `''`（默认） | character vector

为连续时间 PID 控制器，为与积分器或滤波器关联的状态分配唯一名称。（有关离散时间 PID 控制器中状态名称的信息，请参阅 **State name** 参数。）状态名称用于，例如：

- 用于生成代码中的对应变量
- 作为仿真期间记录状态时的存储名称的一部分
- 用于通过线性化模块获得的线性模型中的对应状态

有效状态名称以字母或下划线字符开头，后跟字母数字或下划线字符。

#### 依赖关系

要启用此参数，请将 **Time domain** 设置为 `Continuous-time`。

#### 程序化使用

|  |
| --- |
| **参数：**  `IntegratorContinuousStateAttributes`, `FilterContinuousStateAttributes` |
| **类型：**  character vector |
| **默认：**  `''` |

### **State name** — 离散时间滤波器和积分器状态的名称 空字符串（默认） | string | character vector

为离散时间 PID 控制器，为与积分器或滤波器关联的状态分配唯一名称。（有关连续时间 PID 控制器中状态名称的信息，请参阅 **State name (e.g., 'position')** 参数。）

有效状态名称以字母或下划线字符开头，后跟字母数字或下划线字符。状态名称用于，例如：

- 用于生成代码中的对应变量
- 作为仿真期间记录状态时的存储名称的一部分
- 用于通过线性化模块获得的线性模型中的对应状态

有关在代码生成中使用状态名称的详细信息，请参阅 C Data Code Interface Configuration for Model Interface Elements (Simulink Coder)。

#### 依赖关系

要启用此参数，请将 **Time domain** 设置为 `Discrete-time`。

#### 程序化使用

|  |
| --- |
| **参数：**  `IntegratorStateIdentifier`, `FilterStateIdentifier` |
| **类型：**  string, character vector |
| **默认：**  `""` |

### **State name must resolve to Simulink signal object** — 要求状态名称解析为信号对象 `off`（默认） | `on`

选择此参数以要求离散时间积分器或滤波器状态名称解析为 Simulink 信号对象。

#### 依赖关系

要为离散时间积分器或滤波器状态启用此参数：

1. 将 **Time domain** 设置为 `Discrete-time`。
2. 为积分器或滤波器 **State name** 指定值。
3. 将模型配置参数 **Signal resolution** 设置为 `None` 以外的值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `IntegratorStateMustResolveToSignalObject`, `FilterStateMustResolveToSignalObject` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认：** `"off"` |

## 所属库

Motor Control Blockset / Controls / Controllers Motor Control Blockset HDL Support / Controls / Controllers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

对于离散时间 PID 控制器（**Time domain** 设置为 `Discrete-time`）：

- 当置于触发子系统层次结构内时，取决于绝对时间。
- 在某些条件下，生成的代码依赖 `memcpy` 或 `memset` 函数（`string.h`）。

对于连续时间 PID 控制器（**Time domain** 设置为 `Continuous-time`）：

- 考虑使用 Model Discretizer 将连续时间模块映射到支持代码生成的离散等效模块。要访问 Model Discretizer，请在您的模型中，在 **Apps** 选项卡的 **Control Systems** 下，点击 **Model Discretizer**。
- 不建议用于生产代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

该模块具有单一的默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

- 仅支持对离散时间 PID 控制器进行 HDL 代码生成（**Time domain** 设置为 `Discrete-time`）。
- 如果 **Integrator method** 设置为 `BackwardEuler` 或 `Trapezoidal`，则在以下任一条件下，您无法为该模块生成 HDL 代码：

  - 已选择 **Limit output**，并且 **Anti-Windup Method** 不是 `none`。
  - 已选择 **Enable tracking mode**。
- 要生成 HDL 代码：

  - 使用离散时间 PID 控制器。在 **Time domain** 部分中，指定 **Discrete-time**。
  - 保持选中 **Use filtered derivative** 复选框。
  - 在内部指定滤波器和积分器的初始条件。在 **Initialization** 选项卡上，将 **Source** 指定为 `internal`。

    对于 HDL 代码生成，您可以在内部和外部指定滤波器系数。在 **Main** 选项卡上，对于 **Source**，您可以使用 `internal` 或 `external`。
  - 将 **External reset** 设置为 `none`。
  - 当您使用 double 输入时，不要将 **Anti-windup Method** 设置为 `clamping`。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

仅支持对离散时间 PID 控制器进行定点代码生成（**Time domain** 设置为 `Discrete-time`）。

## 版本历史

**在 R2022a 中引入**

### R2024b：使用新端口从外部指定自定义抗饱和算法

该模块现在允许您使用新输入端口 **extAW** 从外部指定抗饱和算法。该模块还在 **preInt** 输出端口提供积分器之前的信号，您可以将该信号用作自定义算法的输入。PI Controller 模块提供两种内置抗饱和方法；但是，为了对积分器退饱和，这些方法依赖于模块分量之和超过指定的模块输出限值。如果您的应用在 PI Controller 模块下游具有饱和或限值，您可以使用新的 **extAW** 和 **preInt** 端口来实现自定义抗饱和逻辑。要启用新端口，请在 **Saturation** 选项卡上选择 **Limit Output**，并将 **Anti-windup Method** 设置为 `external`。

### R2024a：使用来自外部源的导数信号

该模块现在允许您将被控对象信号 *y* 的导数直接作为模块的输入提供。当您的模型中已有可用的导数信号，并且希望跳过模块内部的导数计算时，这会很有帮助。

要启用用于提供导数的输入端口，请选择具有微分作用的控制器类型，并启用 **Use externally sourced derivative** 参数。

## 描述

离散时间 PID 控制器

PI Controller 模块实现离散时间 PID 控制器（PID、PI、PD、仅 P 或仅 I）。该模块与 Discrete PID Controller Simulink® 模块相同。

模块输出是输入信号、输入信号的积分和输入信号的导数的加权和。权重为比例、积分和微分增益参数。一阶极点对微分作用进行滤波。

- 控制器类型（PID、PI、PD、仅 P 或仅 I）— 请参阅 **Controller** 参数。
- 控制器形式（Parallel 或 Ideal）— 请参阅 **Form** 参数。
- 时域（continuous 或 discrete）— 请参阅 **Time domain** 参数。
- 初始条件和复位触发 — 请参阅 **Source** 和 **External reset** 参数。
- 输出饱和限值和内置抗饱和机制 — 请参阅 **Limit output** 参数。
- 用于无扰动控制切换和多回路控制的信号跟踪 — 请参阅 **Enable tracking mode** 参数。

当您更改这些选项时，模块的内部结构会通过激活不同的变体子系统而发生变化。（有关详细信息，请参阅 ）。要查看模块及其变体子系统的内部结构，请右键单击该模块，然后选择 **Mask** > **Look Under Mask**。

### PID 增益整定

PID 控制器增益可以手动或自动整定。自动整定需要 Simulink Control Design™ 软件。有关自动整定的详细信息，请参阅 **Select tuning method** 参数。
