---
type: simulink-block
title: 'PI Controller'
family: 'motor-control-blockset-hdl-support'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Controllers'
documentation_page: 'picontroller'
documentation_source_path: 'ref/picontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# PI Controller

## 端口

### 输入

### **Port\_1( u )** — 误差信号输入 标量 | 向量

参考信号与被控系统输出之间的差值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **ydot** — 外部提供的微分 标量 | 向量

*自 R2024a 起*

将对象信号 *y* 的微分直接作为模块的输入提供。当模型中已有微分信号并希望跳过模块内部的微分计算时，这非常有用。

#### 依赖

要启用此输入端口，请选择具有微分作用的控制器类型，并启用 **Use externally sourced derivative**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **P** — 比例增益 标量 | 向量

比例增益，由模块外部的源提供。外部增益输入非常有用，例如，当您希望将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部增益输入来实现增益调度 PID 控制。在增益调度控制中，您通过模型中的逻辑或其他计算确定 PID 系数，并将其馈送到模块。

#### 依赖

要启用此端口，请将 **Controller parameters Source** 设置为 `external`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **I\*Ts** — 积分增益乘以采样时间 标量 | 向量

积分增益乘以控制器采样时间，由模块外部的源提供。外部增益输入非常有用，例如，当您希望将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部增益输入来实现增益调度 PID 控制。在增益调度控制中，您通过模型中的逻辑或其他计算确定 PID 系数，并将其馈送到模块。

**注意**

PID 整定工具（如 PID Tuner 应用和 Closed-Loop PID Autotuner 模块）整定的是增益 **I**，而不是 **I\*Ts**。因此，在将整定工具获得的积分增益值提供给此端口之前，请将其乘以采样时间。

当您使用 **I\*Ts** 而不是 **I** 时，模块执行积分所需的计算更少。这改善了生成代码的执行时间。

#### 依赖

要启用此端口，请将 **Controller parameters Source** 设置为 `external`，将 **Controller** 设置为具有积分作用的控制器类型，并启用 **Use I\*Ts** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **I** — 积分增益 标量 | 向量

积分增益，由模块外部的源提供。外部增益输入非常有用，例如，当您希望将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部增益输入来实现增益调度 PID 控制。在增益调度控制中，您通过模型中的逻辑或其他计算确定 PID 系数，并将其馈送到模块。

当您从外部提供增益时，积分增益的时间变化也会被积分。这一结果是由于 PID 增益在模块内部的实现方式所致。有关详细信息，请参阅 **Controller parameters Source** 参数。

#### 依赖

要启用此端口，请将 **Controller parameters Source** 设置为 `external`，并将 **Controller** 设置为具有积分作用的控制器类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **D** — 微分增益 标量 | 向量

微分增益，由模块外部的源提供。
外部增益输入非常有用，例如，当您想要将不同的 PID 参数化映射到模块的 PID 增益时。
您还可以使用外部增益输入来实现增益调度 PID 控制。在
增益调度控制中，您通过模型中的逻辑或其他计算来确定 PID 系数，并将它们馈送到模块。

当您从外部提供增益时，微分增益的时间变化也会被微分。出现此结果是因为
PID 增益在模块内的实现方式。有关详细信息，请参阅
**控制器参数源** 参数。

#### 依赖关系

要启用此端口，请将 **控制器参数
源** 设置为 `external`，并将
**控制器** 设置为具有
微分作用的控制器类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **N** — 滤波器系数 标量 | 向量

微分滤波器系数，由模块外部的源提供。外部系数输入非常有用，例如，当您想要
将不同的 PID 参数化映射到模块的 PID 增益时。
您还可以使用外部输入来实现增益调度 PID
控制。在增益调度控制中，您通过模型中的逻辑或其他计算来确定 PID 系数，并将它们馈送到
模块。

#### 依赖关系

要启用此端口，请将 **控制器参数
源** 设置为 `external`，并将
**控制器** 设置为具有
滤波微分的控制器类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Reset** — 外部复位触发 标量

用于将积分器和滤波器复位到其初始
条件的触发。**外部复位**
参数的值决定复位是在上升信号、下降
信号还是电平信号上发生。端口图标指示所选的触发
类型。例如，下图显示了一个 **外部复位** 设置为
`level` 的 PID 模块。

当触发发生时，模块将积分器和滤波器复位到
**积分器初始
条件** 和 **滤波器初始
条件** 参数或
**I0** 和
**D0** 端口指定的初始条件。

**注意**

为了符合汽车工业软件可靠性
协会 (MISRA™) 软件标准，您的模型必须使用布尔
信号来驱动 PID
控制器模块的外部复位端口。

#### 依赖关系

要启用此端口，请将 **外部复位** 设置为
`none` 以外的任何值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `Boolean`

### **I0** — 积分器初始条件 标量 | 向量

积分器初始条件，由模块外部的源提供。

#### 依赖关系

要启用此端口，请将 **初始条件
源** 设置为 `external`，并将
**控制器** 设置为具有
积分作用的控制器类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **D0** — 滤波器初始条件 标量 | 向量

微分滤波器的初始条件，由模块外部的源
提供。

#### 依赖关系

要启用此端口，请将 **初始条件
源** 设置为 `external`，并将
**控制器** 设置为具有
微分作用的控制器类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **up** — 输出饱和上限 标量 | 向量

模块输出的上限，由模块外部的源提供。如果比例、积分和微分作用的加权和超过此端口提供的值，则模块输出保持在该值。

#### 依赖关系

要启用此端口，请选择 **Limit output** 并将输出饱和 **Source** 设置为 `external`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **lo** — 输出饱和下限 标量 | 向量

模块输出的下限，由模块外部的源提供。如果比例、积分和微分作用的加权和低于此端口提供的值，则模块输出保持在该值。

#### 依赖关系

要启用此端口，请选择 **Limit output** 并将输出饱和 **Source** 设置为 `external`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **TR** — 跟踪信号 标量 | 向量

控制器输出要跟踪的信号。当信号跟踪激活时，跟踪信号与模块输出之间的差值被反馈到积分器输入。信号跟踪对于在两个控制器之间切换的系统中实现无扰控制传递非常有用。它还可以用于防止多回路控制系统中的模块积分饱和。有关详细信息，请参阅 **Enable tracking mode** 参数。

#### 依赖关系

要启用此端口，请选择 **Enable tracking mode** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **TDTI** — 离散积分器时间 标量

离散积分器时间，以标量形式提供给模块。您可以使用自己的离散时间积分器采样时间值，该值定义了模块在 Simulink 中或外部硬件上运行时的速率。当模块在条件执行子系统内使用时，离散时间积分器时间的值应与外部中断的平均采样率匹配。

换句话说，您可以为以下任何积分器方法指定 `Ts`，使其值与外部中断的平均采样率匹配。在离散时间中，控制器传递函数的微分项为：

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

要启用此端口，请将 **Time Domain** 设置为 `Discrete-time` 并选择 **PID Controller is inside a conditionally executed subsystem** 选项。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **extAW** — 外部抗积分饱和算法 标量 | 向量

*自 R2024b 起*

在此端口指定自定义抗积分饱和算法。该模块提供两种内置抗积分饱和方法，但是，为了退饱和积分器，这些方法依赖于模块分量之和超过指定的模块输出限值。如果您的应用在 PI Controller 模块下游存在饱和或限幅，您可以使用 **extAW** 输入端口来实现自定义抗积分饱和逻辑。该模块还在 **preInt** 输出端口提供积分器之前的信号，您可以使用该信号来实现自定义算法。

#### 依赖关系

要启用此端口，请在**饱和**选项卡上，选择**限制输出**，并将**抗积分饱和方法**设置为 `external`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1( y )** — 控制器输出 标量 | 向量

控制器输出，通常基于输入信号之和、输入信号的积分以及输入信号的导数，分别由比例、积分和微分增益参数加权。一阶极点对微分作用进行滤波。控制器信号中包含哪些项取决于**控制器**参数的选择。当前设置的基础控制器传递函数显示在模块参数的**补偿器公式**部分以及掩码下方。其他参数会修改模块输出，例如由**上限**和**下限**饱和参数指定的饱和限值。

当任一输入为向量信号时，控制器输出为向量信号。在这种情况下，模块作为 *N* 个独立的 PID 控制器运行，其中 *N* 是输入向量中信号的数量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **preInt** — 积分器前信号 标量 | 向量

*自 R2024b 起*

模块在此端口输出积分器之前的信号。将此信号用作您在 **extAW** 端口提供的自定义抗积分饱和算法的输入。

#### 依赖关系

要启用此端口，请在**饱和**选项卡上，选择**限制输出**，并将**抗积分饱和方法**设置为 `external`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **Controller** — 控制器类型 `PI`（默认）| `PID` | `PD` | `P` | `I`

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

当前设置的控制器传递函数显示在模块参数的**补偿器公式**部分以及掩码下方。

#### 编程用法

|  |
| --- |
| **模块参数：** `Controller` |
| **类型：** 字符串、字符向量 |
| **值：** `"PID"`、`"PI"`、`"PD"`、`"P"`、`"I"` |
| **默认值：** `"PI"` |

### **Form** — 控制器结构 `Parallel`（默认）| `Ideal`

指定控制器结构是并联型还是理想型。

`Parallel`
:   控制器输出是比例、积分和微分作用之和，分别由 **P**、**I** 和 **D** 独立加权。例如，对于连续时间并联型 PID 控制器，传递函数为：

    Cpar(s)=P+I(1s)+D(Nss+N)。

    对于离散时间并联型控制器，传递函数为：

    Cpar(z)=P+Iα(z)+D[N1+Nβ(z)]，

    其中**积分器方法**和**滤波器方法**参数分别确定 *α*(*z*) 和 *β*(*z*)。

`Ideal`
:   比例增益 **P** 作用于所有作用之和。例如，对于连续时间理想型 PID 控制器，传递函数为：

    Cid(s)=P[1+I(1s)+D(Nss+N)]。

    对于离散时间理想型控制器，传递函数为：

    Cid(z)=P[1+Iα(z)+DN1+Nβ(z)]，

    其中**积分器方法**和**滤波器方法**参数分别确定 *a*(*z*) 和 *b*(*z*)。

    **提示**

    当前设置的控制器传递函数显示在模块参数的**补偿器公式**部分以及掩码下方。

#### 编程用法

|  |
| --- |
| **模块参数：** `Controller` |
| **类型：** string, character vector |
| **值：** `"Parallel"`, `"Ideal"` |
| **默认值：** `"Parallel"` |

### **Time domain** — 指定离散时间或连续时间控制器 `Discrete-time`（默认）| `Continuous-time`

当您选择 `Discrete-time` 时，建议您为该模块指定显式采样时间。请参阅 **Sample time (-1 for inherited)** 参数。选择 `Discrete-time` 还会启用 **Integrator method** 和 **Filter method** 参数。

当 PID Controller 模块位于具有同步状态控制的模型中时（请参阅 State Control (HDL Coder) 模块），您不能选择 `Continuous-time`。

#### 编程用法

|  |
| --- |
| **模块参数：** `TimeDomain` |
| **类型：** string, character vector |
| **值：** `"Continuous-time"`, `"Discrete-time"` |
| **默认值：** `"Discrete-time"` |

### **PID Controller is inside a conditionally executed subsystem** — 启用离散积分器时间端口 `off`（默认）| `on`

对于离散时间 PID 控制器，启用离散时间积分器端口以使用您自己的离散时间积分器采样时间值。为确保正确积分，请使用 `TDTI` 端口提供 Δt 的标量值，以实现准确的离散时间积分。

#### 依赖关系

要启用此参数，请将 **Time Domain** 设置为 `Discrete-time`。

#### 编程用法

|  |
| --- |
| **模块参数：** `UseExternalTs` |
| **类型：** string, character vector |
| **值：** `"on"`, `"off"` |
| **默认值：** `"off"` |

### **Sample time (-1 for inherited)** — 采样之间的离散间隔 –1（默认）| 正标量

通过输入正标量值（例如 0.1）来指定采样时间。默认离散采样时间 –1 表示该模块从上游模块继承其采样时间。但是，建议您显式设置控制器采样时间，尤其是在您预计上游模块的采样时间会发生变化时。控制器系数 P、I、D 和 N 的效果取决于采样时间。因此，对于给定的一组系数值，更改采样时间会改变控制器的性能。

有关更多信息，请参阅 Specify Sample Time。

要实现连续时间控制器，请将 **Time domain** 设置为 `Continuous-time`。

**提示**

如果您希望以外部指定的采样时间或可变采样时间运行该模块，请将此参数设置为 –1，并将该模块放入 Triggered Subsystem 中。然后，以所需的采样时间触发该子系统。

#### 依赖关系

要启用此参数，请将 **Time domain** 设置为 `Discrete-time`。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** scalar |
| **值：** `-1`, positive scalar |
| **默认值：** `-1` |

### **Integrator method** — 离散时间控制器中积分的计算方法 `Forward Euler`（默认）| `Backward Euler` | `Trapezoidal`

在离散时间中，控制器传递函数的积分项为
*Iα*(*z*)，其中
*α*(*z*) 取决于你使用此参数指定的积分方法。

`Forward Euler`
:   前向矩形（左手）近似，

    α(z)=Tsz−1。

    此方法最适合小采样时间，此时奈奎斯特限制相对于控制器带宽较大。对于较大的采样时间，`Forward
    Euler` 方法可能导致不稳定，即使离散化一个连续时间下稳定的系统也是如此。

`Backward Euler`
:   后向矩形（右手）近似，

    α(z)=Tszz−1。

    `Backward Euler`
    方法的一个优点是，使用此方法离散化一个稳定的连续时间系统始终会得到稳定的离散时间结果。

`Trapezoidal`
:   双线性近似，

    α(z)=Ts2z+1z−1。

    `Trapezoidal`
    方法的一个优点是，使用此方法离散化一个稳定的连续时间系统始终会得到稳定的离散时间结果。
    在所有可用的积分方法中，
    `Trapezoidal` 方法使离散化系统的频域特性与相应的连续时间系统之间的匹配最为接近。

    **提示**

    当前设置的控制器公式显示在模块参数的 **Compensator formula**
    部分以及掩码下方。

**注意**

对于 `BackwardEuler` 或
`Trapezoidal` 方法，如果满足以下任一条件，则无法为模块生成 HDL 代码：

- 选中了 **Limit output**，且
  **Anti-Windup Method** 不是 `none`。
- 选中了 **Enable tracking mode**。

有关离散时间积分的详细信息，请参阅 Discrete-Time Integrator
模块参考页。

#### 依赖关系

要启用此参数，请将 **Time Domain** 设置为
`Discrete-time`，并将
**Controller** 设置为具有积分作用的控制器类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`IntegratorMethod` |
| **类型**：string, character vector |
| **值**：`"Forward Euler"`, `"Backward Euler"`, `"Trapezoidal"` |
| **默认值**：`"Forward Euler"` |

### **Filter method** — 离散时间控制器中用于计算导数的方法 `Forward Euler`（默认）| `Backward Euler` | `Trapezoidal`

在离散时间中，控制器传递函数的导数项为：

D[N1+Nα(z)]，

其中 *α*(*z*) 取决于你使用此参数指定的滤波方法。

`Forward Euler`
:   前向矩形（左手）近似，

    α(z)=Tsz−1。

    此方法最适合小采样时间，此时奈奎斯特极限相对于控制器带宽较大。对于较大的采样时间，`Forward Euler` 方法可能导致不稳定，即使离散化的是一个连续时间下稳定的系统也是如此。

`Backward Euler`
:   后向矩形（右手）近似，

    α(z)=Tszz−1。

    `Backward Euler` 方法的一个优点是，使用此方法离散化一个稳定的连续时间系统总是会得到稳定的离散时间结果。

`Trapezoidal`
:   双线性近似，

    α(z)=Ts2z+1z−1。

    `Trapezoidal` 方法的一个优点是，使用此方法离散化一个稳定的连续时间系统总是会得到稳定的离散时间结果。在所有可用的积分方法中，`Trapezoidal` 方法使离散化系统的频域特性与相应连续时间系统之间的匹配最为接近。

    **提示**

    当前设置的控制器公式显示在模块参数的 **Compensator formula** 部分以及掩码下方。

有关离散时间积分的详细信息，请参阅 Discrete-Time Integrator 模块参考页。

#### 依赖关系

要启用此参数，请将 **Time Domain** 设置为 `Discrete-time`，并启用 **Use filtered derivative**。

#### 编程使用

|  |
| --- |
| **模块参数**：`FilterMethod` |
| **类型**：string, character vector |
| **值**：`"Forward Euler"`, `"Backward Euler"`, `"Trapezoidal"` |
| **默认值**：`"Forward Euler"` |

### 主要参数

### **Source** — 控制器增益和滤波器系数的来源 external（默认）| internal

为参数启用外部输入允许你在模块外部计算 PID 增益和滤波器系数，并将它们作为信号输入提供给模块。

`internal`
:   使用模块参数 **P**、**I**（或 **I\*Ts**）、**D** 和 **N** 指定控制器增益和滤波器系数。

`external`
:   使用模块输入在外部指定 PID 增益和滤波器系数。对于当前控制器类型所需的每个参数，模块上都会出现一个额外的输入端口。

    外部增益输入很有用，例如，当你想要将不同的 PID 参数化映射到模块的 PID 增益时。你还可以使用外部增益输入来实现增益调度 PID 控制。在增益调度控制中，你通过模型中的逻辑或其他计算来确定 PID 增益，并将它们馈送到模块中。

    当你从外部提供增益时，积分增益值和微分增益值的时间变化分别会被积分和微分。出现这种结果是因为在连续时间和离散时间中，增益都在积分或微分之前应用于信号。例如，对于具有外部输入的连续时间 PID 控制器，积分器项的实现如下图所示。

    在模块内部，输入信号 *u* 在积分之前先与外部提供的积分器增益 *I* 相乘。此实现得到：

    yi=∫uI dt。

    因此，积分器增益被包含在积分中。类似地，在模块的导数项中，与微分增益的乘法先于微分，这会导致微分增益 *D* 被微分。

#### 编程用法

|  |
| --- |
| **模块参数：** `ControllerParametersSource` |
| **类型：** string, character vector |
| **值：** `"internal"`, `"external"` |
| **默认值：** `"external"` |

### **Proportional (P)** — 比例增益 1（默认）| 标量 | 向量

为比例增益指定一个有限实数值。当**控制器形式**为：

- `Parallel` — 比例作用独立于积分作用和微分作用。例如，对于连续时间并联 PID 控制器，传递函数为：

  Cpar(s)=P+I(1s)+D(Nss+N)。

  对于离散时间并联形式控制器，传递函数为：

  Cpar(z)=P+Iα(z)+D[N1+Nβ(z)]，

  其中**积分器方法**和**滤波器方法**参数分别确定
  *α*(*z*) 和
  *β*(*z*)。
- `Ideal` — 比例增益乘以积分项和微分项。例如，对于连续时间理想 PID 控制器，传递函数为：

  Cid(s)=P[1+I(1s)+D(Nss+N)]。

  对于离散时间理想形式控制器，传递函数为：

  Cid(z)=P[1+Iα(z)+DN1+Nβ(z)]，

  其中**积分器方法**和**滤波器方法**参数分别确定
  *α*(*z*) 和
  *β*(*z*)。

#### 依赖关系

要启用此参数，请在**主**选项卡中将控制器参数**源**设置为
`internal`，并将**控制器**设置为
`PID`、`PD`、
`PI` 或
`P`。

#### 编程用法

|  |
| --- |
| **模块参数：** `P` |
| **类型：** scalar, vector |
| **默认值：** 1 |

**可调：** 是

### **Integral (I)** — 积分增益 1（默认）| 标量 | 向量

为积分增益指定一个有限实数值。

**可调：** 是

#### 依赖关系

要启用此参数，请在**主**选项卡中将控制器参数**源**设置为
`internal`，并将**控制器**设置为具有积分作用的类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `I` |
| **类型：** scalar, vector |
| **默认值：** 1 |

### **Integral (I\*Ts)** — 积分增益乘以采样时间 1（默认）| 标量 | 向量

为积分增益乘以采样时间指定一个有限实数值。

**注意**

PID 整定工具（如 PID Tuner 应用和 Closed-Loop PID Autotuner 模块）整定的是增益
**I**，而不是
**I\*Ts**。因此，在将从整定工具获得的积分增益值写入此参数之前，请将其乘以采样时间。

当您使用 **I\*Ts** 而不是
**I** 时，模块执行积分所需的计算更少。这可以改善生成代码的执行时间。

**可调：** 否

#### 依赖关系

要启用此参数，请在**主**选项卡中将控制器参数**源**设置为
`internal`，将**控制器**设置为具有积分作用的类型，并启用 **Use I\*Ts**
参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `I` |
| **类型：** scalar, vector |
| **默认值：** 1 |

### **Use I\*Ts** — 使用积分增益乘以采样时间 `on`（默认）| `off`

对于具有积分作用的离散时间控制器，模块将积分增益作为输入，并在执行积分时在内部将其乘以采样时间。您可以启用此参数，以指定积分增益乘以采样时间作为输入
（**I\*Ts**），代替积分增益
（**I**）。这样做可以减少内部计算次数，当您希望改善生成代码的执行时间时非常有用。

#### 依赖关系

要启用此参数，请将**控制器**设置为具有积分作用的控制器类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `UseKiTs` |
| **类型：** string, character vector |
| **值：** `"on"`, `"off"` |
| **默认值：** `"on"` |

### **Derivative (D)** — 微分增益 0（默认）| 标量 | 向量

为微分增益指定一个有限实数值。

**可调：** 是

#### 依赖关系

要启用此参数，请在 **Main** 选项卡中，将控制器参数 **Source** 设置为 `internal`，并将 **Controller** 设置为 `PID` 或 `PD`。

#### 编程用法

|  |
| --- |
| **模块参数：** `D` |
| **类型：** 标量、向量 |
| **默认值：** 0 |

### **使用外部来源的微分** — 在模块输入端口指定微分 `off`（默认）| `on`

*自 R2024a 起*

选择此选项可直接将对象信号 *y* 的微分作为输入 **ydot** 指定给模块。当您的模型中已有微分信号并希望跳过模块内部的微分计算时，此选项非常有用。

#### 依赖关系

要启用此选项，请选择具有微分作用的控制器类型。

### **使用滤波微分** — 对微分项应用滤波器 `on`（默认）| `off`

仅适用于离散时间 PID 控制器，清除此选项可将滤波微分替换为未滤波的离散时间微分器。这样做后，控制器传递函数的微分项变为：

Dz−1zTs。

对于连续时间 PID 控制器，微分项始终经过滤波。

#### 依赖关系

要启用此参数，请将 **Time domain** 设置为 `Discrete-time`，并将 **Controller** 设置为具有微分作用的类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `UseFilter` |
| **类型：** 字符串、字符向量 |
| **值：** `"on"`、`"off"` |
| **默认值：** `"on"` |

### **滤波器系数 (N)** — 微分滤波器系数 100（默认）| 标量 | 向量

为滤波器系数指定一个有限的实增益值。滤波器系数决定了模块微分作用中滤波器的极点位置。滤波器极点的位置取决于 **Time domain** 参数。

- 当 **Time domain** 为 `Continuous-time` 时，极点位置为 `s = -N`。
- 当 **Time domain** 为 `Discrete-time` 时，极点位置取决于 **Filter method** 参数。

  | 滤波方法 | 滤波器极点位置 |
  | --- | --- |
  | `Forward Euler` | zpole=1−NTs |
  | `Backward Euler` | zpole=11+NTs |
  | `Trapezoidal` | zpole=1−NTs/21+NTs/2 |

该模块不支持 `N = Inf`（理想无滤波微分）。当 **Time domain** 为 `Discrete-time` 时，您可以清除 **Use filtered derivative** 以移除微分滤波器。

#### 依赖关系

要启用此参数，请在 **Main** 选项卡中，将控制器参数 **Source** 设置为 `internal`，并将 **Controller** 设置为 `PID` 或 `PD`。

#### 编程用法

|  |
| --- |
| **模块参数：** `N` |
| **类型：** 标量、向量 |
| **默认值：** 100 |

**可调：** 是

### **Select tuning method** — 控制器系数自动整定工具 `Transfer Function Based (PID Tuner App)`（默认）| `Frequency Response Based`

如果您有 Simulink
Control Design 软件，可以自动整定 PID 系数。
为此，请使用此参数选择整定工具，然后点击
**Tune**。

`Transfer Function Based (PID Tuner App)`
:   使用 PID Tuner，它允许您在检查相关系统
    响应的同时交互式地整定 PID 系数，以验证性能。默认情况下，PID
    Tuner 使用被控对象模型的线性化模型。对于无法线性化的模型，您可以
    根据从仿真或测量响应数据估计的被控对象模型来整定
    PID 系数。有关更多信息，
    请参阅
    Introduction to Model-Based PID Tuning in Simulink (Simulink Control Design)。

`Frequency Response Based`
:   使用 Frequency Response Based PID Tuner，它
    基于通过仿真获得的频率响应估计数据来
    整定 PID 控制器系数。
    此整定方法特别适用于无法线性化或线性化结果为零的被控对象。有关
    更多信息，请参阅
    Design PID Controller from Plant Frequency-Response Data (Simulink Control Design)。

这两种整定方法均假设单回路控制
配置。Simulink
Control Design 软件包含其他适用于更
复杂配置的整定方法。有关整定
PID Controller 模块的其他方式的信息，请参阅 Choose a Control Design Approach (Simulink Control Design)。

### **Enable zero-crossing detection** — 在复位时以及进入或离开饱和状态时检测过零点 `on`（默认）| `off`

过零检测可以精确定位信号不连续点，
而无需使用可能导致仿真时间过长的极小时间步长。如果您在 PID Controller 模块中选择 **Limit
output** 或激活 **External reset**，
激活过零检测可以减少仿真中的计算时间。选择此参数将在以下情况下激活
过零检测：

- 在初始状态复位时
- 进入上限或下限饱和状态时
- 离开上限或下限饱和状态时

有关过零检测的更多信息，请参阅 Zero-Crossing Detection。

#### 编程使用

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：string, character vector |
| **值**：`"on"`, `"off"` |
| **默认值**：`"on"` |

### Initialization

### **Source** — 积分器和微分器初始条件的来源 `external`（默认）| `internal`

Simulink 使用初始条件在仿真开始时或在指定的触发事件时初始化积分器和
微分滤波器（或未滤波的微分器）输出。（请参阅
**External reset** 参数。）这些初始
条件决定模块的初始输出。使用此参数选择如何向模块提供初始条件值。

`internal`
:   使用
    **Integrator Initial condition** 和
    **Filter Initial condition**
    参数指定初始条件。如果未选择 **Use filtered derivative**，
    则使用 **Differentiator**
    参数来指定未滤波微分器的初始条件，
    而不是滤波器初始条件。

`external`
:   使用模块
    输入从外部指定初始条件。额外的输入端口
    **Io** 和
    **Do**
    会出现在模块上。如果未选择 **Use filtered
    derivative**，则在
    **Do**
    处提供未滤波微分器的
    初始条件，而不是滤波器初始条件。

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialConditionSource` |
| **类型**：string, character vector |
| **值**：`"internal"`, `"external"` |
| **默认值**：`"external"` |

### **Integrator** — 积分器初始条件 0（默认）| 标量 | 向量

Simulink 使用积分器初始条件在仿真开始时或在指定的触发事件时初始化积分器（参见**外部复位**）。积分器初始条件和滤波器初始条件决定 PID 控制器模块的初始输出。

积分器初始条件不能为 `NaN` 或 `Inf`。

#### 依赖关系

要使用此参数，请在**初始化**选项卡中，将**源**设置为 `internal`，并将**控制器**设置为具有积分作用的类型。

#### 编程使用

|  |
| --- |
| **模块参数：** `InitialConditionForIntegrator` |
| **类型：** 标量、向量 |
| **默认值：** 0 |

### **Filter** — 滤波器初始条件 0（默认）| 标量 | 向量

Simulink 使用滤波器初始条件在仿真开始时或在指定的触发事件时初始化微分滤波器（参见**外部复位**）。积分器初始条件和滤波器初始条件决定 PID 控制器模块的初始输出。

滤波器初始条件不能为 `NaN` 或 `Inf`。

#### 依赖关系

要使用此参数，请在**初始化**选项卡中，将**源**设置为 `internal`，并使用具有微分滤波器的控制器。

#### 编程使用

|  |
| --- |
| **模块参数：** `InitialConditionForFilter` |
| **类型：** 标量、向量 |
| **默认值：** 0 |

### **Differentiator** — 未滤波微分的初始条件 0（默认）| 标量 | 向量

当您使用未滤波微分时，Simulink 使用此参数在仿真开始时或在指定的触发事件时初始化微分器（参见**外部复位**）。积分器初始条件和微分初始条件决定 PID 控制器模块的初始输出。

微分初始条件不能为 `NaN` 或 `Inf`。

#### 依赖关系

要使用此参数，请将**时域**设置为 `Discrete-time`，清除**使用滤波微分**复选框，并在**初始化**选项卡中，将**源**设置为 `internal`。

#### 编程使用

|  |
| --- |
| **模块参数：** `DifferentiatorICPrevScaledInput` |
| **类型：** 标量、向量 |
| **默认值：** 0 |

### **Initial condition setting** — 应用初始条件的位置 `Auto`（默认）| `Output`

使用此参数指定是将**积分器初始条件**和**滤波器初始条件**参数应用于相应的模块状态还是输出。您只能在命令行更改此参数，使用 `set_param` 设置模块的 `InitialConditionSetting` 参数。

`Auto`
:   在所有情况下使用此选项，除非模块位于触发子系统或函数调用子系统中且启用了简化初始化模式。

`Output`
:   当模块位于触发子系统或函数调用子系统中且启用了简化初始化模式时，使用此选项。

有关**初始条件设置**参数的详细信息，请参见离散时间积分器模块。

此参数仅可通过编程使用访问。

#### 编程使用

|  |
| --- |
| **模块参数：** `InitialConditionSetting` |
| **类型：** 字符串、字符向量 |
| **值：** `"Auto"`、`"Output"` |
| **默认值：** `"Auto"` |

### **External reset** — 用于重置积分器和滤波器值的触发条件 `level`（默认）| `none` | `rising` | `falling` | `either`

指定使模块将积分器和滤波器重置为初始条件的触发条件。（如果未选中 **Use filtered derivative**，则该触发条件会将积分器和微分器重置为初始条件。）选择除 `none` 以外的任何选项都会启用模块上的 **Reset** 端口，用于外部重置信号。

`none`
:   积分器和滤波器（或微分器）输出在仿真开始时被设置为初始条件，并且在仿真期间不会被重置。

`rising`
:   当重置信号出现上升沿时，重置输出。

`falling`
:   当重置信号出现下降沿时，重置输出。

`either`
:   当重置信号出现上升沿或下降沿时，重置输出。

`level`
:   当重置信号满足以下任一条件时，重置输出：

    - 在当前时间步为非零
    - 从前一时间步的非零变为当前时间步的零

    当重置信号为非零时，此选项将输出保持为初始条件。

#### 依赖关系

要启用此参数，请将 **Controller** 设置为具有微分或积分作用的类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `ExternalReset` |
| **类型：** 字符串、字符向量 |
| **值：** `"none"`、`"rising"`、`"falling"`、`"either"`、`"level"` |
| **默认值：** `"level"` |

### **Ignore reset when linearizing** — 强制线性化忽略重置 `off`（默认）| `on`

选择此项可强制 Simulink 和 Simulink Control Design 线性化命令忽略 **External reset** 参数中指定的任何重置机制。忽略重置状态允许您在工作点附近对模型进行线性化，即使该工作点会导致模块重置。

#### 编程用法

|  |
| --- |
| **模块参数：** `IgnoreLimit` |
| **类型：** 字符串、字符向量 |
| **值：** `"off"`、`"on"` |
| **默认值：** `"off"` |

### **Enable tracking mode** — 激活信号跟踪 `off`（默认）| `on`

信号跟踪允许模块输出跟随您在 **TR** 端口提供的跟踪信号。当信号跟踪处于活动状态时，跟踪信号与模块输出之间的差值会以增益 `Kt` 反馈到积分器输入，该增益由 **Tracking gain (Kt)** 参数指定。信号跟踪有多种应用，包括无扰控制切换以及避免多回路控制结构中的积分饱和。

#### 无扰控制切换

使用信号跟踪可在两个控制器之间切换的系统中实现无扰控制切换。假设您要在 PID 控制器和另一个控制器之间切换控制。为此，将控制器输出连接到 **TR** 输入，如下图所示。

有关详细信息，请参阅 Bumpless Control Transfer。

#### 多回路控制

使用信号跟踪可防止多回路控制方法中的模块积分饱和，如下图所示模型。

Inner Loop 子系统包含下图所示的模块。

由于 PID 控制器跟踪内环的输出，其输出永远不会超过饱和的内环输出。有关更多详细信息，请参阅 Prevent Block Windup in Multiloop Control。

#### 依赖关系

要启用此参数，请将 **Controller** 设置为具有积分作用的类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `TrackingMode` |
| **类型：** 字符串、字符向量 |
| **值：** `"off"`、`"on"` |
| **默认值：** `"off"` |

### **Tracking coefficient (Kt)** — 信号跟踪反馈环路的增益 1（默认）| 标量

当您选择 **Enable tracking mode** 时，信号 **TR** 与模块输出之间的差值会以增益 `Kt` 反馈到积分器输入。使用此参数指定该反馈环路中的增益。

#### 依赖关系

要启用此参数，请选择 **Enable tracking mode**。

#### 编程用法

|  |
| --- |
| **模块参数：** `Kt` |
| **类型：** scalar |
| **默认值：** 1 |

### 饱和

#### 输出饱和

### **Limit Output** — 将模块输出限制为指定的饱和值 `on`（默认）| `off`

激活此选项会限制模块输出，因此您不需要在控制器之后单独添加 Saturation 模块。它还允许您激活模块内置的抗积分饱和机制（请参阅 **Anti-windup method** 参数）。使用 **Lower limit** 和 **Upper limit** 参数指定输出饱和限值。您也可以将饱和限值作为模块输入端口从外部指定。

#### 编程用法

|  |
| --- |
| **模块参数：** `LimitOutput` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"on"` |

### **Source** — 输出饱和限值的来源 `internal`（默认）| `external`

使用此参数指定如何提供模块输出的上限和下限饱和限值。

`internal`
:   使用 **Upper limit** 和 **Lower limit** 参数指定输出饱和限值。

`external`
:   使用模块输入端口从外部指定输出饱和限值。模块上会出现额外的输入端口 **up** 和 **lo**。您可以使用这些输入端口来实现由 Simulink 模型中的逻辑或其他计算确定并传递给模块的输出饱和上限和下限。

#### 编程用法

|  |
| --- |
| **模块参数：** `SatLimitsSource` |
| **类型：** string, character vector |
| **值：** `"internal"`, `"external"` |
| **默认值：** `"internal"` |

### **Upper limit** — 模块输出的上限饱和限值 1（默认）| scalar

指定模块输出的上限。当比例、积分和微分作用的加权和超过该值时，模块输出将保持在 **Upper saturation limit**。

#### 依赖关系

要启用此参数，请选择 **Limit output**。

#### 编程用法

|  |
| --- |
| **模块参数：** `UpperSaturationLimit` |
| **类型：** scalar |
| **默认值：** 1 |

### **Lower limit** — 模块输出的下限饱和限值 –1（默认）| scalar

指定模块输出的下限。当比例、积分和微分作用的加权和低于该值时，模块输出将保持在 **Lower saturation limit**。

#### 依赖关系

要启用此参数，请选择 **Limit output**。

#### 编程用法

|  |
| --- |
| **模块参数：** `LowerSaturationLimit` |
| **类型：** scalar |
| **默认值：** –1 |

### **Ignore saturation when linearizing** — 强制线性化忽略输出限值 `on`（默认）| `off`

强制 Simulink 和 Simulink Control Design 线性化命令忽略在 **Upper limit** 和 **Lower limit** 参数中指定的模块输出限值。忽略输出限值允许您围绕某个工作点对模型进行线性化，即使该工作点导致模块超出输出限值。

#### 依赖关系

要启用此参数，请选择 **Limit output** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `LinearizeAsGain` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"on"` |

### **Anti-windup method** — 积分器抗饱和方法 `clamping`（默认）| `none` | `back-calculation` | `external`

当您选择 **Limit output** 且控制器分量的加权和超过指定的输出限值时，模块输出保持在指定限值。然而，积分器输出可以继续增长（积分器饱和），增大模块输出与模块分量之和之间的差异。换句话说，即使输出看起来受饱和限值约束，模块内部的信号也可能是无界的。如果没有防止积分器饱和的机制，可能会出现两种结果：

- 如果输入信号的符号从不改变，积分器会持续积分直到溢出。溢出值是积分器输出数据类型的最大值或最小值。
- 如果输入信号的符号在加权和超出输出限值后发生变化，则可能需要很长时间才能解除积分器的饱和并将加权和恢复到模块饱和限值以内。

在任一情况下，控制器性能都可能受到影响。为了在没有抗饱和机制的情况下对抗饱和效应，可能需要降低控制器的灵敏度（例如，通过减小控制器增益），从而导致控制器响应迟缓。为避免此问题，请使用此参数启用抗饱和机制。

`none`
:   不使用抗饱和机制。

`back-calculation`
:   当模块输出饱和时，通过将饱和与未饱和控制信号之间的差值反馈给积分器来解除积分器的饱和。下图表示连续时间控制器的反算反馈电路。要查看您控制器配置的实际反馈电路，请右键单击模块并选择 **Mask** > **Look Under Mask**。

    使用 **Back-calculation coefficient (Kb)** 参数指定抗饱和反馈电路的增益。通常将 `Kb = I` 设为满意值，或者对于具有微分作用的控制器，设置 `Kb = sqrt(I*D)`。反算对于具有相对较大死区时间的被控对象可能有效 [1]。

`clamping`
:   当模块分量之和超过输出限值且积分器输出与模块输入具有相同符号时，积分停止。当模块分量之和超过输出限值且积分器输出与模块输入具有相反符号时，积分恢复。钳位有时称为条件积分。

    钳位对于具有相对较小死区时间的被控对象可能有用，但对于大死区时间可能产生较差的瞬态响应 [1]。

`external` *(自 R2024b 起)*
:   内置抗饱和方法依赖于模块分量之和超过指定的模块输出限值。如果您的应用在 PI Controller 模块下游存在饱和或限值，您可以使用 **extAW** 输入端口来实现自定义抗饱和逻辑。该模块还在 **preInt** 输出端口提供积分器之前的信号，您可以将其用作自定义算法的输入。

#### 依赖关系

要启用此参数，请选择 **Limit output** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`AntiWindupMode` |
| **类型**：string, character vector |
| **值**：`"none"`, `"back-calculation"`, `"clamping"` |
| **默认值**：`"clamping"` |

### **Back-calculation coefficient (Kb)** — 抗积分饱和反馈环路的增益系数 1（默认）| 标量

`back-calculation` 抗积分饱和方法在模块输出饱和时对积分器进行退饱和。它通过将饱和控制信号与非饱和控制信号之间的差值反馈到积分器来实现这一点。使用 **Back-calculation coefficient (Kb)** 参数指定抗积分饱和反馈电路的增益。有关详细信息，请参阅 **Anti-windup method** 参数。

#### 依赖关系

要启用此参数，请选择 **Limit output** 参数，并将 **Anti-windup method** 参数设置为 `back-calculation`。

#### 编程用法

|  |
| --- |
| **模块参数：** `Kb` |
| **类型：** 标量 |
| **默认值：** 1 |

#### 积分器饱和

### **Limit Output** — 将积分器输出限制在指定的饱和限值内 `off`（默认）| `on`

启用此参数可将积分器输出限制在指定范围内。当积分器输出达到限值时，积分作用关闭以防止积分饱和。使用 **Lower limit** 和 **Upper limit** 参数指定饱和限值。

#### 依赖关系

要启用此参数，请将 **Controller** 设置为具有积分作用的控制器类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `LimitIntegratorOutput` |
| **类型：** 字符串、字符向量 |
| **值：** `"off"`、`"on"` |
| **默认值：** `"off"` |

### **Upper limit** — 积分器上限饱和值 `Inf`（默认）| 标量

指定积分器输出的上限。当积分器输出将超过此值时，输出将保持在此值。

#### 依赖关系

要启用此参数，请在 **Integrator saturation** 下选择 **Limit output**。

#### 编程用法

|  |
| --- |
| **模块参数：** `UpperIntegratorSaturationLimit` |
| **类型：** 标量 |
| **默认值：** `Inf` |

### **Lower limit** — 积分器下限饱和值 `-Inf`（默认）| 标量

指定积分器输出的下限。当积分器输出将低于此值时，输出将保持在此值。

#### 依赖关系

要启用此参数，请在 **Integrator saturation** 下选择 **Limit output**。

#### 编程用法

|  |
| --- |
| **模块参数：** `LowerIntegratorSaturationLimit` |
| **类型：** 标量 |
| **默认值：** `-Inf` |

### 数据类型

此选项卡中的参数主要用于使用 Fixed-Point Designer™ 进行定点代码生成。它们定义了在生成代码时，与模块相关的数值量的存储和处理方式。

如果需要为定点代码生成配置数据类型，请点击 **Open Fixed-Point Tool** 并使用该工具配置选项卡中的其余参数。有关使用 Fixed-Point Tool 的信息，请参阅 Autoscaling Data Objects Using the Fixed-Point Tool (Fixed-Point Designer)。

使用 Fixed-Point Tool 后，如有必要，可以使用此选项卡中的参数对定点数据类型设置进行调整。对于与模块相关的每个量，可以指定：

- 浮点或定点数据类型，包括数据类型是否从模块中的上游值继承。
- 该量的最小值和最大值，这些值决定了该量在定点表示中如何缩放。

如需帮助选择适当的值，请点击 以打开相应量的 Data Type Assistant。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

Data Types 选项卡中列出的具体量因 PID 控制器模块的配置方式而异。通常，可以为以下类型的量配置数据类型：

- Product output — 存储模块掩码下执行的乘法结果。例如，**P product output** 存储将模块输入与比例增益 **P** 相乘的增益模块的输出。
- Parameter — 存储数值模块参数的值，例如 **P**、**I** 或 **D**。
- Block output — 存储位于 PID 控制器模块掩码下的模块的输出。例如，使用 **Integrator output** 指定名为 Integrator 的模块输出的数据类型。此模块位于 Integrator 子系统中的掩码下，并计算控制器作用的积分项。
- Accumulator — 存储与求和模块相关的值。例如，**SumI2 Accumulator** 设置与求和模块 SumI2 相关的累加器的数据类型。此模块位于 Anti-Windup 子系统的 Back Calculation 子系统中的掩码下。

通常，可以通过查看 PID Controller 模块掩码下并检查其子系统来找到与任何列出的参数相关的模块。还可以使用 Model Explorer 在掩码下搜索列出的参数名称，例如 `SumI2`。（请参阅 Model Explorer。）

**匹配输入和内部数据类型**

默认情况下，product output 和 block output 的数据类型设置为 `Inherit: Same as first input`。使用此设置时，模块将这些信号的第一个输入信号的数据类型用作其数据类型。

当数据类型设置为 `Inherit: Inherit via internal rule` 时，Simulink 会选择数据类型以平衡数值精度、性能和生成的代码大小，同时考虑嵌入式目标硬件的属性。

在某些条件下，模块内部的数据类型之间可能会发生不兼容。例如，在连续时间中，掩码下的 Integrator 模块只能接受 `double` 类型的信号。如果模块输入信号是无法转换为 `double` 的类型，例如 `uint16`，则类型继承的内部规则会在生成代码时生成错误。

为避免此类错误，可以使用 Data Types 设置强制进行数据类型转换。例如，可以显式将 **P product output**、**I product output** 和 **D product output** 设置为 `double`，确保到达连续时间积分器的信号为 `double` 类型。

通常，不建议在代码生成应用中将该模块用于连续时间。但是，如果在离散时间中显式地将某些值设置为与模块内下游信号约束不兼容的数据类型，也可能出现类似的数据类型错误。在这种情况下，使用数据类型设置来确保所有数据类型在内部兼容。

#### 定点运算参数

### **整数舍入模式** — 定点运算的舍入模式 `Simplest`（默认）| `Floor` | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

指定定点运算的舍入模式。有关更多信息，请参阅舍入模式（Fixed-Point Designer）。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `'Ceiling'` | `'Convergent'` | `'Floor'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |
| **默认：** `'Simplest'` |

### **整数溢出时饱和** — 溢出操作的方法 `off`（默认）| `on`

指定溢出时是饱和还是回绕。

- `off` — 溢出回绕到数据类型可以表示的适当值。

  例如，数字 130 不适合有符号 8 位整数，会回绕到 -126。
- `on` — 溢出饱和到数据类型可以表示的最小值或最大值。

  例如，与有符号 8 位整数相关的溢出可以饱和到 -128 或 127。

**提示**

- 当您的模型可能存在溢出并且您希望在生成的代码中具有显式饱和保护时，考虑选中此复选框。
- 当您希望优化生成代码的效率时，考虑清除此复选框。

  清除此复选框还有助于避免过度指定模块如何处理超出范围的信号。有关更多信息，请参阅信号范围错误疑难解答。
- 当您选中此复选框时，饱和适用于模块上的每个内部操作，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SaturateOnIntegerOverflow` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **锁定数据类型设置以防止定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选中此参数可防止定点工具覆盖您在此模块上指定的数据类型。有关更多信息，请参阅锁定输出数据类型设置（Fixed-Point Designer）。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### 状态属性

此选项卡中的参数主要用于代码生成。

### **状态名称（例如 'position'）** — 连续时间滤波器和积分器状态的名称 `''`（默认）| 字符向量

为连续时间 PID 控制器的积分器或滤波器关联的状态分配唯一名称。（有关离散时间 PID 控制器中状态名称的信息，请参阅**状态名称**参数。）状态名称用于，例如：

- 生成的代码中的对应变量
- 仿真期间记录状态时作为存储名称的一部分
- 通过线性化模块获得的线性模型中的对应状态

有效的状态名称以字母或下划线字符开头，后跟字母数字或下划线字符。

#### 依赖关系

要启用此参数，请将**时间域**设置为 `Continuous-time`。

#### 程序化使用

|  |
| --- |
| **参数：**  `IntegratorContinuousStateAttributes`, `FilterContinuousStateAttributes` |
| **类型：** 字符向量 |
| **默认值：**  `''` |

### **状态名称** — 离散时间滤波器和积分器状态的名称 空字符串（默认）| 字符串 | 字符向量

为离散时间 PID 控制器的积分器或滤波器关联的状态分配唯一名称。（有关连续时间 PID 控制器中状态名称的信息，请参阅 **状态名称（例如 'position'）** 参数。）

有效的状态名称以字母或下划线字符开头，后跟字母数字或下划线字符。状态名称用于，例如：

- 生成代码中对应的变量
- 仿真期间记录状态时作为存储名称的一部分
- 通过线性化模块获得的线性模型中对应的状态

有关状态名称在代码生成中使用的更多信息，请参阅
用于模型接口元素的 C 数据代码接口配置（Simulink Coder）。

#### 依赖关系

要启用此参数，请将 **时间域** 设置为
`Discrete-time`。

#### 程序化使用

|  |
| --- |
| **参数：**  `IntegratorStateIdentifier`, `FilterStateIdentifier` |
| **类型：** 字符串、字符向量 |
| **默认值：**  `""` |

### **状态名称必须解析为 Simulink 信号对象** — 要求状态名称解析为信号对象 `off`（默认）| `on`

选择此参数以要求离散时间积分器或滤波器状态名称解析为 Simulink 信号对象。

#### 依赖关系

要为离散时间积分器或滤波器状态启用此参数：

1. 将 **时间域** 设置为
   `Discrete-time`。
2. 为积分器或滤波器 **状态名称** 指定一个值。
3. 将模型配置参数 **信号解析** 设置为
   `None` 以外的值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `IntegratorStateMustResolveToSignalObject`, `FilterStateMustResolveToSignalObject` |
| **类型：** 字符串、字符向量 |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

## 所属库

Motor Control Blockset / Controls / Controllers Motor Control Blockset HDL Support / Controls / Controllers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

对于离散时间 PID 控制器（**时间域** 设置为
`Discrete-time`）：

- 放置在触发子系统层次结构中时依赖于绝对时间。
- 生成的代码在某些条件下依赖于 `memcpy` 或
  `memset` 函数（`string.h`）。

对于连续时间 PID 控制器（**时间域** 设置为
`Continuous-time`）：

- 考虑使用 Model Discretizer 将连续时间模块映射到支持代码生成的离散等效模块。要访问 Model Discretizer，请在模型中，于 **Apps** 选项卡下，在
  **Control Systems** 下，点击 **Model
  Discretizer**。
- 不建议用于生产代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有单一的默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

- HDL 代码生成仅支持离散时间 PID 控制器（**Time domain** 设置为 `Discrete-time`）。
- 如果 **Integrator method** 设置为 `BackwardEuler` 或 `Trapezoidal`，则在以下任一条件下无法为该模块生成 HDL 代码：

  - 选中了 **Limit output** 且 **Anti-Windup Method** 为 `none` 以外的任何值。
  - 选中了 **Enable tracking mode**。
- 要生成 HDL 代码：

  - 使用离散时间 PID 控制器。在 **Time domain** 部分，指定 **Discrete-time**。
  - 保持选中 **Use filtered derivative** 复选框。
  - 在内部指定滤波器和积分器的初始条件。在 **Initialization** 选项卡上，将 **Source** 指定为 `internal`。

    对于 HDL 代码生成，您可以在内部和外部指定滤波器系数。在 **Main** 选项卡上，对于 **Source**，您可以使用 `internal` 或 `external`。
  - 将 **External reset** 设置为 `none`。
  - 当使用 double 输入时，不要将 **Anti-windup Method** 设置为 `clamping`。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

定点代码生成仅支持离散时间 PID 控制器（**Time domain** 设置为 `Discrete-time`）。

## 版本历史

**在 R2022a 中引入**

### R2024b：使用新端口在外部指定自定义抗积分饱和算法

该模块现在允许您使用新的输入端口 **extAW** 在外部指定抗积分饱和算法。该模块还在 **preInt** 输出端口提供积分器之前的信号，您可以将其用作自定义算法的输入。PI Controller 模块提供两种内置抗积分饱和方法，但是，为了退饱和积分器，这些方法依赖于模块组件之和超过指定的模块输出限值。如果您的应用在 PI Controller 模块下游存在饱和或限幅，您可以使用新的 **extAW** 和 **preInt** 端口来实现自定义抗积分饱和逻辑。要启用新端口，请在 **Saturation** 选项卡上，选中 **Limit Output** 并将 **Anti-windup Method** 设置为 `external`。

### R2024a：使用来自外部源的导数信号

该模块现在允许您将对象信号 *y* 的导数直接作为模块的输入提供。当您的模型中已有导数信号并且希望跳过模块内部的导数计算时，这很有帮助。

要启用用于提供导数的输入端口，请选择具有微分作用的控制器类型，并启用 **Use externally sourced derivative** 参数。

## 描述

离散时间 PID 控制器

PI Controller 模块实现离散时间 PID 控制器（PID、PI、PD、仅 P 或仅 I）。该模块与 Discrete PID Controller Simulink® 模块相同。

模块输出是输入信号、输入信号的积分和输入信号的导数的加权和。权重为比例、积分和微分增益参数。一阶极点对微分作用进行滤波。

- 控制器类型（PID、PI、PD、仅 P 或仅 I）— 请参阅 **Controller** 参数。
- 控制器形式（Parallel 或 Ideal）— 请参阅 **Form** 参数。
- 时域（连续或离散）— 请参阅 **Time domain** 参数。
- 初始条件和复位触发 — 请参阅 **Source** 和 **External reset** 参数。
- 输出饱和限幅和内建抗积分饱和机制 — 请参阅 **Limit output** 参数。
- 用于无扰控制切换和多回路控制的信号跟踪 — 请参阅 **Enable tracking mode** 参数。

当您更改这些选项时，模块的内部结构会通过激活不同的变体子系统而发生变化。（有关详细信息，请参阅 ）。要检查模块及其变体子系统的内部结构，请右键点击模块并选择 **Mask** > **Look Under Mask**。

### PID 增益整定

PID 控制器增益可手动或自动整定。自动整定需要 Simulink Control Design™ 软件。有关自动整定的详细信息，请参阅 **Select tuning method** 参数。
