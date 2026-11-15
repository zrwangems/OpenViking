---
type: simulink-block
title: 'PID Controller (2DOF)'
family: continuous
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Continuous'
documentation_page: 'pidcontroller2dof'
---

# PID Controller (2DOF)

Continuous-time or discrete-time two-degree-of-freedom PID controller

## 中文

连续时间或离散时间二自由度 PID 控制器

### 所属库

Simulink / Continuous

### 描述

PID Controller (2DOF) 模块实现一个二自由度 PID 控制器（PID、PI 或 PD）。该模块与**时域**参数设置为**连续时间**的 Discrete PID Controller (2DOF) 模块相同。

该模块基于参考信号与测得的系统输出之间的差异来生成输出信号。此模块根据您指定的设定点权重（**b** 和 **c**）来计算比例和导数作用的加权差异信号。模块输出等于对各差异信号进行的比例、积分和导数作用的总和，其中的每个作用根据增益参数 **P**、**I** 和 **D** 进行加权。导数作用通过一阶极点进行滤波。

该模块支持多种控制器类型和结构体。此模块中可配置的选项包括：

- 控制器类型（PID、PI 或 PD）- 请参阅**控制器**参数。
- 控制器形式（Parallel 或 Ideal）- 请参阅**形式**参数。
- 时域（连续或离散）- 请参阅**时域**参数。
- 初始条件和重置触发器 - 请参阅**源**和**外部重置**参数。
- 输出饱和界限和内置抗积分饱和机制 - 请参阅**限制输出**参数。
- 无扰动切换和多环控制的信号跟踪 - 请参阅**启用跟踪模式**参数。

当您更改这些选项时，模块的内部结构体会通过激活不同的可变子系统而发生更改。（请参阅Implement Variations in Separate Hierarchy Using Variant Subsystems。）要检查模块及其可变子系统的内部结构体，请右键点击该模块，然后选择**封装** > **查看封装内部**。

#### 控制配置

在一个常见的实现中，PID Controller 模块在反馈环的前馈路径中运行。

有关接受误差信号（设定点与系统输出之间的差异）的单输入模块的信息，请参阅 PID Controller。

#### PID 增益调整

可手动或自动调整 PID 控制器系数和设定点权重。自动调整需要 Simulink® Control Design™ 软件。有关自动调整的详细信息，请参阅**选择调节方法**参数。

### 端口

#### 输入

#### **Ref** — 参考信号 标量 | 向量

被控对象要遵循的参考信号，如图所示。

当参考信号是向量时，该模块分别对每个信号起作用，从而向量化 PID 系数并产生相同维度的向量输出信号。您可以将 PID 系数和一些其他参数指定为与输入信号具有相同维度的向量。这样做相当于为输入信号中的每一项指定单独的 PID 控制器。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **Port\_1( y )** — 测得的系统输出 标量 | 向量

控制器接收的反馈信号，来自被控对象输出。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **ydot** — 外部源的导数 标量 | 向量

*自 R2024a 起*

将被控对象信号 *y* 的导数直接作为输入提供给模块。当您的模型中有可用的导数信号并且希望跳过模块内导数的计算时，这很有帮助。

##### 依赖关系

要启用此输入端口，请选择具有导数作用的控制器类型并启用**使用来自外部的导数**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **P** — 比例增益 标量 | 向量

比例增益，从模块外部的信源提供。外部增益输入非常有用，例如，当您希望将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部增益输入来实现增益调度 PID 控制。在增益调度控制中，您可以通过模型中的逻辑或其他计算确定 PID 系数，并将它们提供给模块。

##### 依赖关系

要启用此端口，请将**控制器参数源**设置为**外部**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **I** — 积分增益 标量 | 向量

积分增益，由模块外部的信源提供。外部增益输入非常有用，例如，当您希望将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部增益输入来实现增益调度 PID 控制。在增益调度控制中，您可以通过模型中的逻辑或其他计算确定 PID 系数，并将它们提供给模块。

当您从外部提供增益时，还会对积分增益中的时变进行积分。这是由于 PID 增益是在模块内实现而造成的。有关详细信息，请参阅**控制器参数源**参数。

##### 依赖关系

要启用此端口，请将**控制器参数源**设置为**外部**，并将**控制器**设置为具有积分作用的控制器类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **I\*Ts** — 积分增益乘以采样时间 标量 | 向量

对于离散时间控制器，积分增益乘以控制器采样时间，由模块外部的源提供。外部增益输入非常有用，例如，当您希望将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部增益输入来实现增益调度 PID 控制。在增益调度控制中，您可以通过模型中的逻辑或其他计算确定 PID 系数，并将它们提供给模块。

**注意**

PID 调节工具，如 PID 调节器和 Closed-Loop PID Autotuner 模块，可调节增益 **I**，但无法调节增益 **I\*T s**。因此，将从调节工具获得的积分增益值乘以采样时间，然后将其提供给此端口。

当您使用 **I\*Ts** 而不是 **I** 时，模块需要较少的计算来执行积分。这会改进生成代码的执行时间。

对于连续时间控制器，禁用**使用 I\*Ts** 并改用 **I** 端口。

##### 依赖关系

要启用此端口，请将**控制器参数源**设置为**外部**，将**控制器**设置为具有积分作用的控制器类型，并启用**使用 I\*Ts** 参数。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **D** — 导数增益 标量 | 向量

导数增益，由模块外部的信源提供。外部增益输入非常有用，例如，当您希望将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部增益输入来实现增益调度 PID 控制。在增益调度控制中，您可以通过模型中的逻辑或其他计算确定 PID 系数，并将它们提供给模块。

当您从外部提供增益时，还会对导数增益中的时变进行微分。这是由于 PID 增益是在模块内实现而造成的。有关详细信息，请参阅**控制器参数源**参数。

##### 依赖关系

要启用此端口，请将**控制器参数源**设置为**外部**，并将**控制器**设置为具有导数作用的控制器类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **N** — 滤波器系数 标量 | 向量

导数滤波器系数，由模块外部的信源提供。外部系数输入非常有用，例如，当您希望将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部输入来实现增益调度 PID 控制。在增益调度控制中，您可以通过模型中的逻辑或其他计算确定 PID 系数，并将它们提供给模块。

##### 依赖关系

要启用此端口，请将**控制器参数源**设置为**外部**，并将**控制器**设置为具有滤波后的导数的控制器类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **b** — 比例设定点权重 标量 | 向量

比例设定点权重，由模块外部的信源提供。外部输入非常有用，例如，当您希望将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部输入来实现增益调度 PID 控制。在增益调度控制中，您可以通过模型中的逻辑或其他计算确定 PID 系数，并将它们提供给模块。

##### 依赖关系

要启用此端口，请将**控制器参数源**设置为**外部**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **c** — 导数设定点权重 标量 | 向量

导数设定点权重，由模块外部的信源提供。外部输入非常有用，例如，当您希望将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部输入来实现增益调度 PID 控制。在增益调度控制中，您可以通过模型中的逻辑或其他计算确定 PID 系数，并将它们提供给模块。

##### 依赖关系

要启用此端口，请将**控制器参数源**设置为**外部**，并将**控制器**设置为具有导数作用的控制器类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **Reset** — 外部重置触发器 标量

用于将积分器和滤波器重置为其初始条件的触发器。使用**外部重置**参数指定触发重置的信号类型。端口图标指示该参数中指定的触发器类型。例如，下图显示**外部重置**设置为**上升沿**的连续时间 PID（二自由度）模块。

当触发事件发生时，模块将积分器和滤波器重置为由**积分器初始条件**和**滤波器初始条件**参数或 **I0** 和 **D0** 端口指定的初始条件。

**注意**

为了符合汽车行业软件可靠性协会 (MISRA™) 的软件标准，您的模型必须使用布尔值信号来驱动 PID controller 模块的外部重置端口。

##### 依赖关系

要启用此端口，请将**外部重置**设置为**无**以外的任何值。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `Boolean`

#### **I0** — 积分器初始条件 标量 | 向量

积分器初始条件，由模块外部的信源提供。

##### 依赖关系

要启用此端口，请将**初始条件源**设置为**外部**，并将**控制器**设置为具有积分作用的控制器类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **D0** — 滤波器初始条件 标量 | 向量

导数滤波器的初始条件，由模块外部的信源提供。

##### 依赖关系

要启用此端口，请将**初始条件源**设置为**外部**，并将**控制器**设置为具有导数作用的控制器类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **up** — 输出饱和上限 标量 | 向量

模块输出的上限，由模块外部的源提供。如果比例、积分和导数作用的加权总和超过此端口上提供的值，则模块输出保持在该值。

##### 依赖关系

要启用此端口，请选择**限制输出**，并将输出饱和**源**设置为**外部**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **lo** — 输出饱和下限 标量 | 向量

模块输出的下限，由模块外部的源提供。如果比例、积分和导数作用的加权总和低于此端口上提供的值，则模块输出保持在该值。

##### 依赖关系

要启用此端口，请选择**限制输出**，并将输出饱和**源**设置为**外部**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **TR** — 跟踪信号 标量 | 向量

控制器输出要跟踪的信号。激活信号跟踪后，跟踪信号与模块输出之间的差异将反馈给积分器输入。信号跟踪可用于实现系统在两个控制器之间的无扰动切换。它也可用于在多环控制系统中防止模块饱和。有关详细信息，请参阅**启用跟踪模式**参数。

##### 依赖关系

要启用此端口，请选择**启用跟踪模式**参数。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **TDTI** — 离散积分器时间 标量

离散积分器时间，作为标量提供给模块。您可以使用自己的离散时间积分器采样时间值来定义该模块在 Simulink 中或外部硬件上运行的速率。当在条件执行子系统中使用该模块时，离散时间积分器时间的值应与外部中断的平均采样率相匹配。

换句话说，您可以为以下任何积分器方法指定 `Ts`，使该值与外部中断的平均采样率相匹配。在离散时间内，控制器传递函数的导数项为：

D[N1+Nα(z)],

其中 *α*(*z*) 取决于您使用此参数指定的积分器方法。

**前向欧拉**
:   α(z)=Tsz−1.

**后向欧拉**
:   α(z)=Tszz−1.

**梯形**
:   α(z)=Ts2z+1z−1.

有关离散时间积分的详细信息，请参阅 Discrete-Time Integrator 模块参考页。有关条件执行子系统的详细信息，请参阅条件执行子系统概述。

##### 依赖关系

要启用此端口，请将**时域**设置为**离散时间**并选择 **PID 控制器位于条件执行子系统内**选项。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

#### **extAW** — 外部抗积分饱和算法 标量 | 向量

*自 R2024b 起*

在此端口上指定一个自定义抗积分饱和算法。该模块提供两个内置抗积分饱和方法，但为了防止积分器饱和，这些方法依赖超出指定模块输出限制的模块组件之和。如果您的应用在 PID Controller 模块的下游出现饱和或限制，您可以使用 **extAW** 输入端口来实现自定义抗积分饱和逻辑。该模块还在 **preInt** 输出端口提供积分器之前的信号，可用于实现自定义算法。

##### 依赖关系

要启用此端口，请在**饱和**选项卡上，选择**限制输出**，并将**抗积分饱和方法**设置为**外部**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
#### 输出

#### **Port\_1( u )** — 控制器输出 标量 | 向量

控制器输出，通常基于输入信号、输入信号的积分和输入信号的导数，经由设定点权重和比例、积分和导数增益参数加权求和。通过一阶极点过滤导数作用。控制器信号中存在哪些项取决于您为**控制器**参数选择的内容。当前设置的基本控制器传递函数显示在模块参数的**补偿器公式**部分中和封装下。其他参数修改模块输出，例如**上限**和**下限**饱和参数指定的饱和界限。

当任一输入为向量信号时，控制器输出是向量信号。在这种情况下，模块充当 *N* 个独立 PID 控制器，其中 *N* 是输入向量中的信号数。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **preInt** — 积分器之前的信号 标量 | 向量

*自 R2024b 起*

模块在积分器之前的此端口上输出信号。将此信号用作您在 **extAW** 端口上提供的自定义抗积分饱和算法的输入。

##### 依赖关系

要启用此端口，请在**饱和**选项卡上，选择**限制输出**，并将**抗积分饱和方法**设置为**外部**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 参数

#### **控制器** — 控制器类型 **PID** (默认) | **PI** | **PD**

指定在控制器中包含比例项、积分项和导数项中的哪些项。

**PID**
:   比例、积分和导数作用。

**PI**
:   仅比例和积分作用。

**PD**
:   仅比例和导数作用。

**提示**

当前设置的控制器输出显示在模块参数的**补偿器公式**部分中和封装下。

##### 编程用法

|  |
| --- |
| **模块参数**：`Controller` |
| **类型：**字符串、字符向量 |
| **值：**`"PID"`、`"PI"`、`"PD"` |
| **默认值：**`"PID"` |

#### **形式** — 控制器结构 **并行** (默认) | **理想**

指定控制器结构是“并行”还是“理想”。

**并行**
:   比例、积分和导数增益 **P**、**I** 和 **D** 的应用彼此独立。例如，对于并联型连续时间二自由度 PID 控制器，控制器输出 *u* 为：

    u=P(br−y)+I1s(r−y)+DN1+N1s(cr−y),

    其中 *r* 是参考信号，*y* 是测得的被控对象输出信号，*b* 和 *c* 是设定点权重。

    对于并联型离散时间二自由度控制器，控制器输出为：

    u=P(br−y)+Iα(z)(r−y)+DN1+Nβ(z)(cr−y),

    其中**积分器方法**和**滤波器方法**参数分别确定 *α*(*z*) 和 *β*(*z*)。

**理想**
:   比例增益 **P** 作用于所有作用的总和。例如，对于理想形式的连续时间二自由度 PID 控制器，控制器输出为：

    u=P[(br−y)+I1s(r−y)+DN1+N1s(cr−y)].

    对于理想形式的离散时间二自由度 PID 控制器，传递函数为：

    u=P[(br−y)+Iα(z)(r−y)+DN1+Nβ(z)(cr−y)],

    其中**积分器方法**和**滤波器方法**参数分别确定 *α*(*z*) 和 *β*(*z*)。

    **提示**

    当前设置的控制器输出显示在模块参数的**补偿器公式**部分中和封装下。

##### 编程用法

|  |
| --- |
| **模块参数**：`Controller` |
| **类型：**字符串、字符向量 |
| **值：**`"Parallel"`、`"Ideal"` |
| **默认值**：`"Parallel"` |

#### **时域** — 指定连续时间或离散时间控制器 **连续时间** (默认) | **离散时间**

选择**离散时间**时，建议您为模块指定显式采样时间。请参阅**采样时间(-1 表示继承)** 参数。选择**离散时间**也会启用**积分器方法**和**滤波器方法**参数。

当 PID Controller 模块位于具有同步状态控件（请参阅 State Control (HDL Coder) 模块）的模型中时，您不能选择**连续时间**。

**注意**

PID Controller (2DOF) 和 Discrete PID Controller (2DOF) 模块是相同的，只是此参数的默认值不同。

##### 编程用法

|  |
| --- |
| **模块参数**：`TimeDomain` |
| **类型：**字符串、字符向量 |
| **值：**`"Continuous-time"`、`"Discrete-time"` |
| **默认值**：`"Continuous-time"` |

#### **PID 控制器位于条件执行子系统内** — 启用离散积分器时间端口 **off** (默认) | **on**

对于离散时间 PID 控制器，启用离散时间积分器端口以使用您自己的离散时间积分器采样时间值。为确保正确积分，请使用 `TDTI` 端口提供标量值 Δt，用于精确的离散时间积分。

##### 依赖关系

要启用此参数，请将**时域**设置为**离散时间**。

##### 编程用法

|  |
| --- |
| **模块参数**：`UseExternalTs` |
| **类型：**字符串、字符向量 |
| **值：**`"on"`、`"off"` |
| **默认值**：`"off"` |

#### **采样时间(-1 表示继承)** — 采样之间的离散间隔 -1 (默认) | 正标量

通过输入正标量值（例如 0.1）指定采样时间。默认的离散采样时间为 -1，表示该模块从上游模块继承其采样时间。但是，建议您显式设置控制器采样时间，尤其是在您预计上游模块的采样时间会发生变化时。控制器系数 P、I、D 和 N 的影响取决于采样时间。因此，对于给定的一组系数值，更改采样时间会更改控制器的性能。

有关详细信息，请参阅 指定采样时间。

要实现连续时间控制器，请将**时域**设置为**连续时间**。

**提示**

如果要使用外部指定的或可变的采样时间运行模块，请将此参数设置为 -1 并将模块放在 Triggered Subsystem 中。然后，在所需的采样时间触发该子系统。

##### 依赖关系

要启用此参数，请将**时域**设置为**离散时间**。

##### 编程用法

|  |
| --- |
| **模块参数：**`SampleTime` |
| **类型：**标量 |
| **值：** `-1`、正标量 |
| **默认值：**`-1` |

#### **积分器方法** — 离散时间控制器中积分的计算方法 **前向欧拉** (默认) | **后向欧拉** | **梯形**

在离散时间内，控制器传递函数的积分项为 *Ia*(*z*)，其中 *a*(*z*) 取决于您使用此参数指定的积分器方法。

**前向欧拉**
:   正向矩形（左手）逼近方法，

    α(z)=Tsz−1.

    这种方法最适合较小的采样时间，此时奈奎斯特限制与控制器带宽相比来说比较大。对于较大的采样时间，**前向欧拉**方法可能带来不稳定性，即使离散的是在连续时间下表现稳定的系统。

**后向欧拉**
:   反向矩形（右手）逼近方法，

    α(z)=Tszz−1.

    **后向欧拉**方法的一个优点是：使用这种方法离散稳定的连续时间系统始终会生成稳定的离散时间结果。

**梯形**
:   双线性逼近法。

    α(z)=Ts2z+1z−1.

    **梯形**方法的一个优点是：使用这种方法离散稳定的连续时间系统始终会生成稳定的离散时间结果。在所有可用的积分方法中，**梯形**方法可在离散化系统与对应的连续时间系统的频域属性之间生成最接近的匹配。

    **提示**

    当前设置的控制器公式显示在模块参数的**补偿器公式**部分中和封装下。

有关离散时间积分的详细信息，请参阅Discrete-Time Integrator模块参考页。

##### 依赖关系

要启用此参数，请将**时域**设置为**离散时间**，并将**控制器**设置为具有积分作用的控制器类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`IntegratorMethod` |
| **类型：**字符串、字符向量 |
| **值：**`"Forward Euler"`、`"Backward Euler"`、`"Trapezoidal"` |
| **默认值**：`"Forward Euler"` |

#### **滤波器方法** — 离散时间控制器中导数的计算方法 **前向欧拉** (默认) | **后向欧拉** | **梯形**

在离散时间内，控制器传递函数的导数项为：

D[N1+Nα(z)],

其中 *α*(*z*) 取决于您使用此参数指定的滤波器方法。

**前向欧拉**
:   正向矩形（左手）逼近方法，

    α(z)=Tsz−1.

    这种方法最适合较小的采样时间，此时奈奎斯特限制与控制器带宽相比来说比较大。对于较大的采样时间，**前向欧拉**方法可能带来不稳定性，即使离散的是在连续时间下表现稳定的系统。

**后向欧拉**
:   反向矩形（右手）逼近方法，

    α(z)=Tszz−1.

    **后向欧拉**方法的一个优点是：使用这种方法离散稳定的连续时间系统始终会生成稳定的离散时间结果。

**梯形**
:   双线性逼近法。

    α(z)=Ts2z+1z−1.

    **梯形**方法的一个优点是：使用这种方法离散稳定的连续时间系统始终会生成稳定的离散时间结果。在所有可用的积分方法中，**梯形**方法可在离散化系统与对应的连续时间系统的频域属性之间生成最接近的匹配。

    **提示**

    当前设置的控制器公式显示在模块参数的**补偿器公式**部分中和封装下。

有关离散时间积分的详细信息，请参阅Discrete-Time Integrator模块参考页。

##### 依赖关系

要启用此参数，请将**时域**设置为**离散时间**并启用**使用滤波导数**。

##### 编程用法

|  |
| --- |
| **模块参数**：`FilterMethod` |
| **类型：**字符串、字符向量 |
| **值：**`"Forward Euler"`、`"Backward Euler"`、`"Trapezoidal"` |
| **默认值**：`"Forward Euler"` |

#### 常设

#### **源** — 控制器增益和滤波器系数的信源 内部 (默认) | 外部

**内部**
:   使用模块参数 **P**、**I**、**D**、**N**、**b** 和 **c** 分别指定控制器增益、滤波器系数和设定点权重。

**外部**
:   使用模块输入在外部指定 PID 增益、滤波器系数和设定点权重。对于当前控制器类型需要的每个参数，模块上会出现一个额外的输入端口。

如果为参数启用外部输入，您可以在模块外部计算它们的值，并将它们作为信号输入提供给模块。

外部输入非常有用，例如，当您希望将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部增益输入来实现增益调度 PID 控制。在增益调度控制中，您可以通过模型中的逻辑或其他计算确定 PID 增益，并将它们提供给模块。

如果从外部提供增益，则会分别对积分和导数增益值的时变进行积分和微分。导数设定点权重 *c* 也被求导。出现这种结果是因为在连续时间和离散时间中，增益都会在积分或微分之前应用于信号。例如，对于采用外部输入的连续时间 PID 控制器，积分项的实现方式如下图所示。

在进行积分之前，系统会在模块内将输入信号 *u* 乘以外部提供的积分增益 *I*。此实现的结果为：

ui=∫(r−y)I dt.

因此，积分增益包含在积分中。类似地，在模块的导数项中，进行微分之前会乘以导数增益，从而导致导数增益 *D* 和导数设定点权重 *c* 被微分。

##### 编程用法

|  |
| --- |
| **模块参数**：`ControllerParametersSource` |
| **类型：**字符串、字符向量 |
| **值：**`"internal"`、`"external"` |
| **默认值**：`"internal"` |

#### **比例(P)** — 比例增益 1 (默认) | 标量 | 向量

为比例增益指定有限实数增益值。**控制器形式**可以是：

- **并行** - 比例作用独立于积分和导数作用。例如，对于并联型连续时间二自由度 PID 控制器，控制器输出 *u* 为：

  u=P(br−y)+I1s(r−y)+DN1+N1s(cr−y),

  其中 *r* 是参考信号，*y* 是测得的被控对象输出信号，*b* 和 *c* 是设定点权重。

  对于并联型离散时间二自由度控制器，控制器输出为：

  u=P(br−y)+Iα(z)(r−y)+DN1+Nβ(z)(cr−y),

  其中**积分器方法**和**滤波器方法**参数分别确定 *α*(*z*) 和 *β*(*z*)。
- **理想** - 比例增益乘以积分和导数项。例如，对于理想形式的连续时间二自由度 PID 控制器，控制器输出为：

  u=P[(br−y)+I1s(r−y)+DN1+N1s(cr−y)].

  对于理想形式的离散时间二自由度 PID 控制器，传递函数为：

  u=P[(br−y)+Iα(z)(r−y)+DN1+Nβ(z)(cr−y)],

  其中**积分器方法**和**滤波器方法**参数分别确定 *α*(*z*) 和 *β*(*z*)。

##### 依赖关系

要启用此参数，请将控制器参数**源**设置为**内部**。

##### 编程用法

|  |
| --- |
| **模块参数**：`P` |
| **类型：**标量、向量 |
| **默认值：**1 |

**可调:** Yes

#### **积分(I)** — 积分增益 1 (默认) | 标量 | 向量

为积分增益指定有限实数增益值。

**可调:** Yes

##### 依赖关系

要启用此参数，请在**常设**选项卡中将控制器参数**源**设置为**内部**，并将**控制器**设置为具有积分作用的类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`I` |
| **类型：**标量、向量 |
| **默认值：**1 |

#### **积分 (I\*Ts)** — 积分增益乘以采样时间 1 (默认) | 标量 | 向量

对于离散时间控制器，为积分增益乘以采样时间指定有限实数增益值。

**注意**

PID 调节工具，如 PID 调节器和 Closed-Loop PID Autotuner 模块，可调节增益 **I**，但无法调节增益 **I\*T s**。因此，将从调节工具获得的积分增益值乘以采样时间，然后将其写入此参数。

当您使用 **I\*Ts** 而不是 **I** 时，模块需要较少的计算来执行积分。这会改进生成代码的执行时间。

对于连续时间控制器，禁用**使用 I\*Ts** 并改用 **I** 参数。

**可调:** No

##### 依赖关系

要启用此参数，请在**常设**选项卡中将控制器参数**源**设置为**内部**，将**控制器**设置为具有积分作用的类型，并启用**使用 I\*Ts** 参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`I` |
| **类型：**标量、向量 |
| **默认值：**1 |

#### **使用 I\*Ts** — 使用积分增益乘以采样时间 `off` (默认) | `on`

对于具有积分作用的离散时间控制器，该模块将积分增益作为输入，并在内部将其乘以采样时间，作为执行积分的一部分。如果您启用此参数，您将显式指定积分增益乘以采样时间作为输入 (**I\*Ts**)，代替积分增益 (**I**)。这样做可以减少内部计算的次数，并且在您要改进所生成代码的执行时间时非常有用。

如果您启用信号跟踪或抗积分饱和模式反算，并且启用 **I\*Ts**，则还必须将跟踪增益参数 **Kt** 设置为 `Kt*Ts`，并将反算系数 **Kb** 设置为 `Kb*Ts`。

对于连续时间控制器，启用此参数对积分增益不起作用。

##### 依赖关系

要启用此参数，请将**控制器**设置为具有积分作用的控制器类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`UseKiTs` |
| **类型：**字符串、字符向量 |
| **值：**`"on"`、`"off"` |
| **默认值**：`"on"` |

#### **导数(D)** — 导数增益 0 (默认) | 标量 | 向量

为导数增益指定有限实数增益值。

**可调:** Yes

##### 依赖关系

要启用此参数，请在**常设**选项卡中将控制器参数**源**设置为**内部**，并将**控制器**设置为 **PID** 或 **PD**。

##### 编程用法

|  |
| --- |
| **模块参数**：`D` |
| **类型：**标量、向量 |
| **默认值：**0 |

#### **使用来自外部的导数** — 指定在模块输入端口上的导数 `off` (默认) | `on`

*自 R2024a 起*

选择此选项可将被控对象信号 *y* 的导数直接指定为模块的输入 **ydot**。当您的模型中有可用的导数信号并且希望跳过模块内导数的计算时，这很有帮助。

##### 依赖关系

要启用此选项，请选择具有导数作用的控制器类型。

#### **使用滤波导数** — 将滤波器应用于导数项 `on` (默认) | `off`

仅针对离散时间 PID 控制器，取消选中此选项以将滤波后的导数替换为未滤波的离散时间微分器。执行此操作时，控制器输出的导数项变为：

Dz−1zTs(cr−y).

对于连续时间 PID 控制器，始终对导数项进行滤波。

##### 依赖关系

要启用此参数，请将**时域**设置为**离散时间**，并将**控制器**设置为具有导数项的类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`UseFilter` |
| **类型：**字符串、字符向量 |
| **值：**`"on"`、`"off"` |
| **默认值**：`"on"` |

#### **滤波器系数(N)** — 导数滤波器系数 100 (默认) | 标量 | 向量

为滤波器系数指定有限实数增益值。滤波器系数确定滤波器在模块的导数作用中的极点位置。滤波器极点的位置取决于**时域**参数。

- 当**时域**为**连续时间**时，极点位置为 `s = -N`。
- 当**时域**为**离散时间**时，极点位置取决于**滤波器方法**参数。

  | 滤波器方法 | 滤波器极点的位置 |
  | --- | --- |
  | **前向欧拉** | zpole=1−NTs |
  | **后向欧拉** | zpole=11+NTs |
  | **梯形** | zpole=1−NTs/21+NTs/2 |

模块不支持 `N = Inf`（理想的未滤波导数）。当**时域**为**离散时间**时，可以清除**使用滤波导数**以删除导数滤波器。

##### 依赖关系

要启用此参数，请在**常设**选项卡中将控制器参数**源**设置为**内部**，并将**控制器**设置为 **PID** 或 **PD**。

##### 编程用法

|  |
| --- |
| **模块参数**：`N` |
| **类型：**标量、向量 |
| **默认值：**100 |

**可调:** Yes

#### **设定点权重(b)** — 比例设定点权重 1 (默认) | 标量 | 向量

控制器比例项的设定点权重。二自由度控制器输出的比例项为 *P* (*br* - *y*)，其中 *r* 是参考信号，*y* 是测得的被控对象输出。将 *b* 设置为 0 将去除对参考信号的比例作用，这样可以减少系统响应对设定点步长变化的过冲。更改 *b* 和 *c* 的相对值会改变抗扰和设定点跟踪之间的平衡。

**可调:** Yes

##### 依赖关系

要启用此参数，请在**常设**选项卡中将控制器参数**源**设置为**内部**。

##### 编程用法

|  |
| --- |
| **模块参数**：`b` |
| **类型：**标量、向量 |
| **默认值：**1 |

#### **设定点权重(c)** — 导数设定点权重 1 (默认) | 标量 | 向量

控制器导数项的设定点权重。二自由度控制器的导数项作用于 *cr* - *y*，其中 *r* 是参考信号，*y* 是测量的被控对象输出。因此，将 *c* 设置为 0 将去除对参考信号的导数作用，这样可以减少对设定点步长变化的瞬时响应。将 *c* 设置为 0 可产生一种既能实现有效的抗扰和顺利的设定点跟踪，又不会产生过多瞬时响应的控制器。更改 *b* 和 *c* 的相对值会改变抗扰和设定点跟踪之间的平衡。

**可调:** Yes

##### 依赖关系

要启用此参数，请在**常设**选项卡中将控制器参数**源**设置为**内部**并将**控制器**设置为具有导数作用的类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`c` |
| **类型：**标量、向量 |
| **默认值：**1 |

#### **选择调节方法** — 用来自动调整控制器系数的工具 **基于传递函数(PID 调节器)** (默认) | **基于频率响应**

如果您有 Simulink Control Design 软件，则可以自动调整在模块内部应用的 PID 系数。为此，请使用此参数选择调整工具，然后点击**调节**。

**基于传递函数(PID 调节器)**
:   使用 PID 调节器，您可以在检查相关系统响应以验证性能的同时交互调节 PID 系数。PID 调节器可以调节所有系数 **P**、**I**、**D** 和 **N** 以及设定点系数 **b** 和 **c**。默认情况下，这种 PID 调节器适合线性化被控对象模型。对于无法线性化的模型，您可以根据从仿真或测量的响应数据估算出的被控对象模型来调整 PID 系数。有关详细信息，请参阅 Design Two-Degree-of-Freedom PID Controllers (Simulink Control Design)。

**基于频率响应**
:   使用基于频率响应的 PID 调节器，它根据通过仿真获得的频率响应估计数据来调节 PID 控制器系数。这种调整方法特别适用于不可线性化或线性化为零的被控对象。基于频率响应的 PID 调节器调节系数 **P**、**I**、**D** 和 **N**，但不调节设定点系数 **b** 和 **c**。有关详细信息，请参阅Design PID Controller from Plant Frequency-Response Data (Simulink Control Design)。

这两种调整方法都采用单环路控制配置。Simulink Control Design 软件提供适合更复杂配置的其他调整方法。有关调整 PID Controller 模块的其他方法的信息，请参阅Choose a Control Design Approach (Simulink Control Design)。

##### 依赖关系

要启用此参数，请在**常设**选项卡中将控制器参数**源**设置为**内部**。

#### **启用过零检测** — 在重置时以及在进入或退出饱和状态时检测过零点 **on** (默认) | **off**

过零检测可以准确无误地确定信号的不连续性，而无需检测特别小的时间步，因为这样可能会大大延长仿真时间。如果在 PID Controller 模块中选择**限制输出**或者激活**外部重置**，激活过零检测可以缩短仿真时的计算时间。选择此参数可在以下时间激活过零检测：

- 在初始状态重置时
- 在进入上限或下限饱和状态时
- 在退出上限或下限饱和状态时

有关过零检测的详细信息，请参阅过零检测。

##### 编程用法

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型：**字符串、字符向量 |
| **值：**`"on"`、`"off"` |
| **默认值**：`"on"` |

#### 初始化

#### **源** — 积分器和导数初始条件的信源 **内部** (默认) | **外部**

Simulink 使用初始条件在仿真开始时或在指定的触发事件发生时初始化积分器和导数滤波器（或未滤波的导数）输出。（请参阅**外部重置**参数。）这些初始条件确定初始模块输出。使用此参数选择如何向模块提供初始条件值。

**内部**
:   使用**积分器初始条件**和**滤波器初始条件**参数指定初始条件。如果未选择**使用滤波导数**，请使用**微分器**参数指定未滤波的微分器的初始条件，而不是滤波器初始条件。

**外部**
:   使用模块输入从外部指定初始条件。额外的输入端口 **Io** 和 **Do** 出现在模块中。如果未选择**使用滤波导数**，请在 **Do** 处提供未滤波的微分器的初始条件，而不是滤波器初始条件。

##### 编程用法

|  |
| --- |
| **模块参数**：`InitialConditionSource` |
| **类型：**字符串、字符向量 |
| **值：**`"internal"`、`"external"` |
| **默认值**：`"internal"` |

#### **积分器** — 积分器初始条件 0 (默认) | 标量 | 向量

Simulink 在仿真一开始或在发生指定的触发事件时（请参阅**外部重置**）使用积分器初始条件来初始化积分器。积分器初始条件与滤波器初始条件一起确定 PID controller 模块的初始输出。

积分器初始条件不能是 `NaN` 或 `Inf`。

##### 依赖关系

要使用此参数，请在**初始化**选项卡中将**源**设置为**内部**，然后将**控制器**设置为具有积分作用的类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`InitialConditionForIntegrator` |
| **类型：**标量、向量 |
| **默认值：**0 |

#### **滤波器** — 滤波器初始条件 0 (默认) | 标量 | 向量

Simulink 在仿真一开始或在发生指定的触发事件时（请参阅**外部重置**）使用滤波器初始条件来初始化导数滤波器。积分器初始条件与滤波器初始条件一起确定 PID controller 模块的初始输出。

滤波器初始条件不能是 `NaN` 或 `Inf`。

##### 依赖关系

要使用此参数，请在**初始化**选项卡中将**源**设置为**内部**，并使用具有导数滤波器的控制器。

##### 编程用法

|  |
| --- |
| **模块参数**：`InitialConditionForFilter` |
| **类型：**标量、向量 |
| **默认值：**0 |

#### **微分器** — 未滤波的导数的初始条件 0 (默认) | 标量 | 向量

使用未滤波的导数时，Simulink 使用此参数在仿真一开始或在发生指定的触发事件时（请参阅**外部重置**）初始化微分器。积分器初始条件和导数初始条件一起确定 PID controller 模块的初始输出。

导数初始条件不能是 `NaN` 或 `Inf`。

##### 依赖关系

要使用此参数，请将**时域**设置为**离散时间**，清除**使用滤波导数**复选框，然后在**初始化**选项卡中，将**源**设置为**内部**。

##### 编程用法

|  |
| --- |
| **模块参数**：`DifferentiatorICPrevScaledInput` |
| **类型：**标量、向量 |
| **默认值：**0 |

#### **初始条件设置** — 应用初始条件的位置 **自动** (默认) | **输出**

使用此参数指定是否将**积分器初始条件**和**滤波器初始条件**参数应用于对应的模块状态或输出。您只能在命令行中使用 `set_param` 设置模块的 `InitialConditionSetting` 参数来更改此参数。

**自动**
:   除非模块在触发子系统或函数调用子系统中且启用了简化初始化模式，否则其他所有情况下均使用此选项。

**输出**
:   当模块在触发子系统或函数调用子系统中且启用了简化初始化模式时，使用此选项。

有关**初始条件设置**参数的详细信息，请参阅 Discrete-Time Integrator 模块。

此参数只能通过编程用法访问。

##### 编程用法

|  |
| --- |
| **模块参数**：`InitialConditionSetting` |
| **类型：**字符串、字符向量 |
| **值：**`"Auto"`、`"Output"` |
| **默认值：**`"Auto"` |

#### **外部重置** — 用于重置积分器和滤波器值的触发器 **无** (默认) | **上升沿** | **下降沿** | **任一沿** | **电平**

指定使模块将积分器和滤波器重置为初始条件的触发条件。（如果未选择**使用滤波导数**，则触发器会将积分器和微分器重置为初始条件。）选择**无**之外的任何选项都将在模块上启用**重置**端口以接收外部重置信号。

**无**
:   积分器和滤波器（或微分器）输出在仿真开始时设置为初始条件，在仿真期间不会重置。

**上升沿**
:   当重置信号具有上升沿时重置输出。

**下降沿**
:   当重置信号具有下降沿时重置输出。

**任一沿**
:   当重置信号上升或下降时重置输出。

**电平**
:   当重置信号具有以下情况之一时重置输出：

    - 在当前时间步为非零值时
    - 从上一时间步的非零更改为当前时间步的零时

    此选项在重置信号非零时使输出保持在初始条件。

##### 依赖关系

要启用此参数，请将**控制器**设置为具有导数或积分作用的类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`ExternalReset` |
| **类型：**字符串、字符向量 |
| **值：**`"none"`、`"rising"`、`"falling"`、`"either"`、`"level"` |
| **默认值**：`"none"` |

#### **线性化时忽略重置** — 强制线性化以忽略重置 **off** (默认) | **on**

选择此项可强制 Simulink 和 Simulink Control Design 线性化命令忽略在**外部重置**参数中指定的任何重置机制。忽略重置状态将允许您围绕某个工作点对模型进行线性化，即使该工作点会导致模块重置也一样。

##### 编程用法

|  |
| --- |
| **模块参数**：`IgnoreLimit` |
| **类型：**字符串、字符向量 |
| **值：**`"off"`、`"on"` |
| **默认值**：`"off"` |

#### **启用跟踪模式** — 激活信号跟踪 **off** (默认) | **on**

信号跟踪使模块输出能够跟随您在 **TR** 端口提供的跟踪信号。激活信号跟踪后，跟踪信号与模块输出之间的差异将反馈给由**跟踪增益 (Kt)** 参数指定的增益为 `Kt` 的积分器输入。跟踪信号具有多种应用，包括无扰动切换和避免多多环控制结构中的饱和。

##### 无扰动切换

使用信号跟踪可以实现系统在两个控制器之间切换时的无扰动切换。假设您要在 PID 控制器和另一个控制器之间转移控制权。为此，将控制器输出连接到 **TR** 输入，如下图所示。

有关详细信息，请参阅Bumpless Control Transfer with a Two-Degree-of-Freedom PID Controller。

##### 多环控制

使用信号跟踪来防止多环控制方法中的模块饱和。有关使用单自由度 PID 控制器说明此方法的示例，请参阅Prevent Block Windup in Multiloop Control。

##### 依赖关系

要启用此参数，请将**控制器**设置为具有积分作用的类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`TrackingMode` |
| **类型：**字符串、字符向量 |
| **值：**`"off"`、`"on"` |
| **默认值**：`"off"` |

#### **跟踪系数(Kt)** — 信号跟踪反馈环的增益 1 (默认) | 标量

选择**启用跟踪模式**时，信号 **TR** 与模块输出之间的差异将反馈到具有增益 `Kt` 的积分器输入。使用此参数指定该反馈环中的增益。

对于离散时间控制器，如果您选择模块的**使用 I\*Ts** 参数，则将此参数设置为值 `Kt*Ts`，其中 `Kt` 是所需增益，`Ts` 是采样时间。

##### 依赖关系

要启用此参数，请选择**启用跟踪模式**。

##### 编程用法

|  |
| --- |
| **模块参数：**`Kt` |
| **类型：**标量 |
| **默认值：**1 |

#### 饱和

##### 输出饱和

#### **限制输出** — 将模块输出限制为指定的饱和值 **off** (默认) | **on**

激活此选项可限制模块输出，因此无需在控制器后面另加 Saturation 模块。它还允许您激活模块内置的抗积分饱和机制（请参阅**抗积分饱和方法**参数）。使用**下限**和**上限**参数指定输出饱和界限。您也可以在外部指定饱和界限作为模块输入端口。

##### 编程用法

|  |
| --- |
| **模块参数**：`LimitOutput` |
| **类型：**字符串、字符向量 |
| **值：**`"off"`、`"on"` |
| **默认值**：`"off"` |

#### **源** — 输出饱和界限的源 内部 (默认) | 外部

使用此参数指定如何提供模块输出的饱和上限及饱和下限。

**内部**
:   使用**上限**和**下限**参数指定输出饱和界限。

**外部**
:   使用模块输入端口从外部指定输出饱和界限。额外的输入端口 **up** 和 **lo** 出现在该模块上。您可以使用输入端口来实现由 Simulink 模型中的逻辑或其他计算确定并传递给该模块的输出饱和上限和下限。

##### 编程用法

|  |
| --- |
| **模块参数**：`SatLimitsSource` |
| **类型：**字符串、字符向量 |
| **值：**`"internal"`、`"external"` |
| **默认值**：`"internal"` |

#### **上限** — 模块输出的饱和上限 `Inf` (默认) | 标量

指定模块输出的上限值。一旦比例、积分和导数作用的加权和高于**饱和上限**，模块输出将保持在该上限值。

##### 依赖关系

要启用此参数，请选择**限制输出**。

##### 编程用法

|  |
| --- |
| **模块参数：**`UpperSaturationLimit` |
| **类型：**标量 |
| **默认值**：`Inf` |

#### **下限** — 模块输出的饱和下限 `-Inf` (默认) | 标量

指定模块输出的下限。一旦比例、积分和微分作用的加权和低于**饱和下限**时，模块输出将保持在该下限值。

##### 依赖关系

要启用此参数，请选择**限制输出**。

##### 编程用法

|  |
| --- |
| **模块参数：**`LowerSaturationLimit` |
| **类型：**标量 |
| **默认值**：`-Inf` |

#### **线性化时忽略饱和界限** — 强制线性化以忽略输出限制 **off** (默认) | **on**

强制 Simulink 和 Simulink Control Design 线性化命令忽略在**上限**和**下限**参数中指定的模块输出限制。忽略输出限制允许您围绕某个工作点对模型进行线性化，即使该工作点会导致模块超出输出限制也一样。

##### 依赖关系

要启用此参数，请选择**限制输出**参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`LinearizeAsGain` |
| **类型：**字符串、字符向量 |
| **值：**`"off"`、`"on"` |
| **默认值**：`"off"` |

#### **抗积分饱和方法** — 积分器抗积分饱和方法 **无** (默认) | **反算** | **钳位** | **外部**

如果选中了**限制输出**且控制器组件的加权和超出了指定的输出限制，模块输出将保持在指定的限制值。但是，积分器输出可以继续增加（积分器饱和），从而加大了模块输出与模块组件之和之间的差距。换句话说，即使输出看起来在饱和界限范围内，模块中的内部信号也可以无限大。如果没有积分器抗积分饱和机制，可能会产生以下两种结果：

- 如果进入积分器的信号的符号始终不变，积分器将继续积分直到溢出。溢出值是积分器输出的数据类型的最大值或最小值。
- 如果进入积分器的信号的符号在加权和超出输出界限时发生改变，它将需要很长时间来防止积分器饱和，并返回位于模块饱和界限范围内的加权和。

无论哪种情况，控制器性能都会受到影响。要在没有抗积分饱和机制的情况下消除饱和效果，可能需要解调控制器（例如，通过减小控制器增益），从而导致控制器速度缓慢。要避免此问题，请使用此参数激活抗积分饱和机制。

**无**
:   不使用抗积分饱和机制。

**反算**
:   当模块输出饱和时，通过将饱和控制信号与非饱和控制信号之间的差异反馈给积分器来防止积分器饱和。下图表示连续时间控制器的反算反馈电路。要查看控制器配置的实际反馈电路，请右键点击该模块，然后选择**封装** > **查看封装内部**。

    使用**反算系数(Kb)** 参数指定抗积分饱和反馈电路的增益。通常，设置 `Kb = I`（对于具有导数作用的控制器，设置 `Kb = sqrt(I*D)`）是恰当的。对于饱和时间相对较长的被控对象，反算很有效。[1]

**钳位**
:   当模块组件之和超出输出限制且积分器输出与模块输入具有相同的符号时，积分停止。当模块组件之和超出输出限制且积分器输出与模块输入具有相反的符号时，积分恢复。钳位有时称为条件积分。

    对于饱和时间相对较小的被控对象，钳位可能很有用；但对于饱和时间较大的被控对象，它可能产生不良的瞬时响应。[1]

**外部** *(自 R2024b 起)*
:   两个内置抗积分饱和方法依赖超出指定模块输出限制的模块组件之和。如果您的应用在 PID Controller 模块的下游出现饱和或限制，您可以使用 **extAW** 输入端口来实现自定义抗积分饱和逻辑。该模块还在积分器之前的 **preInt** 输出端口上提供信号，您可以将该信号用作自定义算法的输入。

##### 依赖关系

要启用此参数，请选择**限制输出**参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`AntiWindupMode` |
| **类型：**字符串、字符向量 |
| **值：**`"none"`、`"back-calculation"`、`"clamping"`、`"external"` |
| **默认值**：`"none"` |

#### **反算系数(Kb)** — 抗积分饱和反馈环的增益系数 1 (默认) | 标量

当模块输出饱和时，`back-calculation` 抗积分饱和方法防止积分器饱和。它通过向积分器反馈饱和控制信号与非饱和控制信号之间的差异来实现此目的。使用**反算系数(Kb)** 参数指定抗积分饱和反馈电路的增益。有关详细信息，请参阅**抗积分饱和方法**参数。

对于离散时间控制器，如果选择模块的**使用 I\*Ts** 参数，则将此参数设置为值 `Kb*Ts`，其中 `Kb` 是所需的系数，`Ts` 是采样时间。

##### 依赖关系

要启用此参数，请选择**限制输出**参数，并将**抗积分饱和方法**参数设置为**反算**。

##### 编程用法

|  |
| --- |
| **模块参数：**`Kb` |
| **类型：**标量 |
| **默认值：**1 |

##### 积分器饱和

#### **限制输出** — 将积分器输出限制为指定的饱和界限 **off** (默认) | **on**

启用此参数可将积分器输出限制在指定范围内。当积分器输出达到界限时，积分作用将关闭以防止积分饱和。使用**下限**和**上限**参数指定饱和界限。

##### 依赖关系

要启用此参数，请将**控制器**设置为具有积分作用的控制器类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`LimitIntegratorOutput` |
| **类型：**字符串、字符向量 |
| **值：**`"off"`、`"on"` |
| **默认值**：`"off"` |

#### **上限** — 积分器的饱和上限 `Inf` (默认) | 标量

指定积分器输出的上限。一旦积分器输出超出此值，就会保持为该值。

##### 依赖关系

要启用此参数，请在**积分器饱和**下，选择**限制输出**。

##### 编程用法

|  |
| --- |
| **模块参数**：`UpperIntegratorSaturationLimit` |
| **类型：**标量 |
| **默认值**：`Inf` |

#### **下限** — 积分器的饱和下限 `-Inf` (默认) | 标量

指定积分器输出的下限。一旦积分器输出低于此值，就会保持为该值。

##### 依赖关系

要启用此参数，请在**积分器饱和**下，选择**限制输出**。

##### 编程用法

|  |
| --- |
| **模块参数**：`LowerIntegratorSaturationLimit` |
| **类型：**标量 |
| **默认值**：`-Inf` |

#### 数据类型

此选项卡中的参数主要用于使用 Fixed-Point Designer™ 生成定点代码。它们定义在生成代码时如何存储和处理与模块关联的数值量。

如果需要为定点代码生成配置数据类型，请点击**打开定点工具**并使用该工具配置选项卡中的其余参数。有关使用定点工具的信息，请参阅Autoscaling Data Objects Using the Fixed-Point Tool (Fixed-Point Designer)。

使用定点工具后，在必要时可以使用此选项卡中的参数调整定点数据类型设置。对于与模块关联的每个量，您可以指定：

- 浮点或定点数据类型，包括数据类型是否继承自模块中的上游值。
- 量的最小值和最大值，用于确定如何对量进行定标以使用定点表示。

要获取帮助以选择适当的值，请点击  以打开对应量的数据类型助手。有关详细信息，请参阅使用数据类型助手指定数据类型。

“数据类型”选项卡中具体列出的量取决于您配置 PID 控制器模块的方式。通常，您可以为以下类型的量配置数据类型：

- 乘积输出 - 存储在模块封装下执行的乘法的结果。例如，**P 乘积输出**存储增益模块的输出，该输出是模块输入与比例增益 **P** 的乘积。
- 参数 - 存储数值模块参数的值，例如 **P**、**I** 或 **D**。
- 模块输出 - 存储位于 PID 控制器模块封装下的模块的输出。例如，使用**积分器输出**指定名为 Integrator 的模块输出的数据类型。此模块位于 Integrator 子系统中的封装下，并计算控制器操作的积分项。
- 累加器 - 存储与求和模块关联的值。例如，**SumI2 累加器**设置与求和模块 SumI2 关联的累加器的数据类型。此模块位于 Anti-Windup 子系统的 Back Calculation 子系统中的封装下。

通常，您可以通过查看 PID Controller 模块封装并检查其子系统来查找与任何列出的参数关联的模块。您还可以使用模型资源管理器在封装下搜索列出的参数名称，例如 `SumI2`。（请参阅模型资源管理器。）

**匹配输入和内部数据类型**

默认情况下，模块中的所有数据类型都设置为**继承: 从内部规则继承**。使用此设置时，Simulink 在考虑嵌入式目标硬件的属性的同时，会选择相应的数据类型来平衡数值准确性、性能和生成的代码大小。

在某些情况下，模块内的数据类型之间可能会发生不兼容。例如，在连续时间下，封装下的 Integrator 模块只能接受 **double** 类型的信号。如果模块输入信号的类型不能转换为 **double**，例如 **uint16**，则生成代码时类型继承的内部规则会生成错误。

为了避免此类错误，可以使用“数据类型”设置强制进行数据类型转换。例如，您可以将 **P 乘积输出**、**I 乘积输出**和 **D 乘积输出**显式设置为 **double**，确保到达连续时间积分器的信号类型为 **double**。

通常，不建议在连续时间下将模块用于代码生成应用。但是，如果您将某些值显式设置为与模块中的下游信号约束不兼容的数据类型，则在离散时间下会发生类似的数据类型错误。在这种情况下，请使用“数据类型”设置确保所有数据类型在内部兼容。

##### 定点运算参数

#### **整数舍入模式** — 定点运算的舍入模式 **向下** (默认) | **向上** | **收敛** | **最邻近值** | **舍入** | **最简** | **零**

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最邻近的可表示值。要控制模块参数的舍入方法，请在封装字段中使用 MATLAB® 舍入函数输入表达式。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RndMeth` |
| **值:** | `'Floor'` (默认) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

#### **对整数溢出进行饱和处理** — 溢出操作的方法 `off` (默认) | `on`

指定对溢出是进行饱和处理还是绕回处理。

- `on` - 将溢出饱和处理为数据类型能够表示的最小值或最大值。
- `off` - 溢出将绕回到数据类型可以表示的合适值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。

- 选择此参数后，模块输出将在达到 127 时饱和。类似地，模块输出将在达到最小输出值 -128 时饱和。
- 清除此参数后，软件会将导致溢出的值解释为 `int8`，这可能产生意外结果。例如，以 `int8` 表示的模块结果 130（二进制 1000 0010）为 -126。

##### 提示

- 如果您的模型存在可能的溢出，而您希望在生成的代码中进行显式饱和保护，请考虑选中此参数。
- 如果您希望优化生成的代码的效率，请考虑清除此参数。清除此参数还可以帮助您避免过度地指定信号超出范围时模块的处理方式。有关详细信息，请参阅信号范围错误故障排除。
- 如果选中此参数，饱和将应用于模块中的每个内部操作，而不仅仅应用于输出或结果。
- 一般情况下，代码生成进程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SaturateOnIntegerOverflow` |
| **值:** | `'off'` (默认) | `'on'` |

#### **锁定数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您对此模块指定的数据类型。有关详细信息，请参阅Lock the Output Data Type Setting (Fixed-Point Designer)。

##### 编程用法

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### 状态属性

此选项卡中的参数主要用于代码生成。

#### **状态名称(例如，'position')** — 连续时间滤波器和积分器状态的名称 `''` (默认) | 字符向量

对于连续时间 PID 控制器，为与积分器或滤波器关联的状态分配唯一名称。（有关离散时间 PID 控制器中的状态名称的信息，请参阅**状态名称**参数。）状态名称的用途举例如下：

- 用于生成代码中的对应变量
- 作为在仿真期间记录状态时存储名称的一部分
- 用于通过线性化模块获得的线性模型中的对应状态

有效的状态名称以字母或下划线字符开始，后跟字母数字或下划线字符。

##### 依赖关系

要启用此参数，请将**时域**设置为**连续时间**。

##### 编程用法

|  |
| --- |
| **参数：**`IntegratorContinuousStateAttributes`、`FilterContinuousStateAttributes` |
| **类型：**字符向量 |
| **默认值：**`''` |

#### **状态名称** — 离散时间滤波器和积分器状态的名称 空字符串 (默认) | 字符串 | 字符向量

对于离散时间 PID 控制器，为与积分器或滤波器关联的状态分配唯一名称。（有关连续时间 PID 控制器中的状态名称的信息，请参阅**状态名称(例如，'position')** 参数。）

有效的状态名称以字母或下划线字符开始，后跟字母数字或下划线字符。状态名称的用途举例如下：

- 用于生成代码中的对应变量
- 作为在仿真期间记录状态时存储名称的一部分
- 用于通过线性化模块获得的线性模型中的对应状态

有关在代码生成中使用状态名称的详细信息，请参阅模型接口元素的 C 数据代码接口配置 (Simulink Coder)。

##### 依赖关系

要启用此参数，请将**时域**设置为**离散时间**。

##### 编程用法

|  |
| --- |
| **参数：**`IntegratorStateIdentifier`、`FilterStateIdentifier` |
| **类型：**字符串、字符向量 |
| **默认值：**`""` |

#### **状态名称必须解析为 Simulink 信号对象** — 要求将状态名称解析为信号对象 `off` (默认) | `on`

选择此参数会要求将离散时间积分器或滤波器状态名称解析为 Simulink 信号对象。

##### 依赖关系

要为离散时间积分器或滤波器状态启用此参数，请执行下列操作：

1. 将**时域**设置为**离散时间**。
2. 指定积分器或滤波器**状态名称**的值。
3. 将模型配置参数**信号解析**设置为**无**以外的值。

##### 编程用法

|  |
| --- |
| **模块参数：**`IntegratorStateMustResolveToSignalObject`、`FilterStateMustResolveToSignalObject` |
| **类型：**字符串、字符向量 |
| **值：**`"off"`、`"on"` |
| **默认值**：`"off"` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

对于连续时间 PID 控制器（**时域**设置为**连续时间**）：

- 考虑使用 模型离散化器 将连续时间模块映射到支持代码生成的离散等效值。要访问模型离散化器，请在 **App** 选项卡的**控制系统**下，点击**模型离散化器**。
- 不建议用于生产代码。

对于离散时间 PID 控制器（**时域**设置为**离散时间**）：

- 位于触发子系统层次结构中时取决于绝对时间。
- 生成的代码在特定条件下依赖于 `memcpy` 或 `memset` 函数 (`string.h`)。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

仅对离散时间 PID 控制器支持定点代码生成（**时域**设置为**离散时间**）。

### 版本历史记录

**在 R2009b 中推出**

#### R2024b: 使用新端口在外部指定抗积分饱和算法

模块现在允许您使用新输入端口 **extAW** 在外部指定抗积分饱和算法。该模块还在积分器之前的 **preInt** 输出端口上提供信号，您可以将该信号用作自定义算法的输入。PID Controller 模块提供两个内置抗积分饱和方法，但为了防止积分器饱和，这些方法依赖超出指定模块输出限制的模块组件之和。如果您的应用在 PID Controller 模块的下游出现饱和或限制，您可以使用新的 **extAW** 和 **preInt** 端口来实现自定义抗积分饱和逻辑。要启用新端口，请在**饱和**选项卡上，选择**限制输出**，并将**抗积分饱和方法**设置为**外部**。

#### R2024a: 使用来自外部源的导数信号

PID Controller 模块现在允许您将被控对象信号 *y* 的导数直接作为模块的输入。当您的模型中有可用的导数信号并且希望跳过模块内导数的计算时，这很有帮助。

要启用提供导数的输入端口，请选择具有导数作用的控制器类型并启用**使用外部源的导数**参数。

#### R2022b: 积分器和滤波器的初始条件超出饱和界限时会发生错误

现在，当积分器或滤波器初始条件值超出输出饱和界限时，模块会出错。在以前的版本中，当这些初始条件具有这样的值时，模块不会出错。

如果此更改影响到您的模型，请更新 PID 积分器或滤波器初始条件值，使这些值在输出饱和界限范围内。

#### R2021b: `ReferenceBlock` 参数返回不同路径

从 R2021b 开始，`get_param` 函数为 `ReferenceBlock` 参数返回不同值。`ReferenceBlock` 参数是所有 Simulink 模块共有的属性，它给出模块链接到的库模块的路径。PID Controller (2DOF) 和 Discrete PID Controller (2DOF) 模块现在链接到 `'slpidlib/PID Controller (2DOF)'`。以前，这些模块链接到 `'pid_lib/PID Controller (2DOF)'`。

此更改不会影响任何其他功能或工作流。您仍可以将先前的路径与 `set_param` 函数结合使用。

#### R2020b: `ReferenceBlock` 参数返回不同路径

从 R2020b 开始，`get_param` 函数为 `ReferenceBlock` 参数返回不同值。`ReferenceBlock` 参数是所有 Simulink 模块共有的属性，它给出模块链接到的库模块的路径。PID Controller (2DOF) 和 Discrete PID Controller (2DOF) 模块现在链接到 `'pid_lib/PID Controller (2DOF)'`。以前，这些模块链接到 `'simulink/Continuous/PID Controller (2DOF)'`。

此更改不会影响任何其他功能或工作流。您仍可以将先前的路径与 `set_param` 函数结合使用。

## Libraries

Simulink / Continuous

## Description

The PID Controller (2DOF) block implements a two-degree-of-freedom PID
controller (PID, PI, or PD). The block is identical to the Discrete PID
Controller (2DOF) block with the **Time domain** parameter
set to `Continuous-time`.

The block generates an output signal based on the difference between a reference
signal and a measured system output. The block computes a weighted difference signal for
the proportional and derivative actions according to the setpoint weights
(**b** and **c**) that you specify. The block
output is the sum of the proportional, integral, and derivative actions on the
respective difference signals, where each action is weighted according to the gain
parameters **P**, **I**, and **D**. A
first-order pole filters the derivative action.

The block supports several controller types and structures. Configurable options in
the block include:

- Controller type (PID, PI, or PD) — See the **Controller**
  parameter.
- Controller form (Parallel or Ideal) — See the **Form**
  parameter.
- Time domain (continuous or discrete) — See the **Time
  domain** parameter.
- Initial conditions and reset trigger — See the **Source** and
  **External reset** parameters.
- Output saturation limits and built-in anti-windup mechanism — See the
  **Limit output** parameter.
- Signal tracking for bumpless control transfer and multiloop control — See the
  **Enable tracking mode** parameter.

As you change these options, the internal structure of the block changes by activating
different variant subsystems. (See Implement Variations in Separate Hierarchy Using Variant Subsystems.) To examine the internal structure of the block and its variant subsystems,
right-click the block and select **Mask** > **Look Under Mask**.

### Control Configuration

In one common implementation, the PID Controller block operates in
the feedforward path of a feedback loop.

For a single-input block that accepts an error signal (a difference between a
setpoint and a system output), see PID
Controller.

### PID Gain Tuning

The PID controller coefficients and the setpoint weights are tunable either
manually or automatically. Automatic tuning requires Simulink®
Control Design™ software. For more information about automatic tuning, see the
**Select tuning method** parameter.

## Ports

### Input

### **Ref** — Reference signal scalar | vector

Reference signal for plant to follow, as shown.

When the reference signal is a vector, the block acts separately on
each signal, vectorizing the PID coefficients and producing a vector
output signal of the same dimensions. You can specify the PID
coefficients and some other parameters as vectors of the same dimensions
as the input signal. Doing so is equivalent to specifying a separate PID
controller for each entry in the input signal.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_1( y )** — Measured system output scalar | vector

Feedback signal for the controller, from the plant output.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **ydot** — Externally sourced derivative scalar | vector

*Since R2024a*

Supply the derivative of the plant signal *y*
directly as an input to the block. This is helpful when you have the
derivative signal available in your model and want to skip the
computation of the derivative inside the block.

#### Dependencies

To enable this input port, select a controller type that has
derivative action and enable **Use externally sourced
derivative**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **P** — Proportional gain scalar | vector

Proportional gain, provided from a source external to the block. External gain input is
useful, for example, when you want to map a different PID
parameterization to the PID gains of the block. You can also use
external gain input to implement gain-scheduled PID control. In
gain-scheduled control, you determine the PID coefficients by
logic or other calculation in your model and feed them to the
block.

#### Dependencies

To enable this port, set **Controller parameters Source** to `external`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **I** — Integral gain scalar | vector

Integral gain, provided from a source external to the block. External gain input is useful,
for example, when you want to map a different PID
parameterization to the PID gains of the block. You can also use
external gain input to implement gain-scheduled PID control. In
gain-scheduled control, you determine the PID coefficients by
logic or other calculation in your model and feed them to the
block.

When you supply gains externally, time variations in the integral gain are also integrated. This result occurs because of the way the PID gains are implemented within the block. For details, see the **Controller parameters Source** parameter.

#### Dependencies

To enable this port, set **Controller parameters Source** to
`external`, and set **Controller** to
a controller type that has integral action.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **I\*Ts** — Integral gain multiplied by sample time scalar | vector

For discrete-time controllers, integral gain multiplied by the controller sample time,
provided from a source external to the block. External gain input is useful, for
example, when you want to map a different PID parameterization to the PID gains of the
block. You can also use external gain input to implement gain-scheduled PID control. In
gain-scheduled control, you determine the PID coefficients by logic or other
calculations in your model and feed them to the block.

**Note**

PID tuning tools, such as the PID Tuner app and Closed-Loop PID Autotuner block, tune the gain **I** but not **I\*Ts**. Therefore, multiply the integral gain value you obtain from a tuning tool by the sample time before you supply it to this port.

When you use **I\*Ts** instead of **I**, the block requires fewer calculations to perform integration. This improves the execution time of the generated code.

For continuous-time controllers, disable **Use I\*Ts** and use the
**I** port instead.

#### Dependencies

To enable this port, set **Controller parameters Source** to `external`, set **Controller** to a controller type that has integral action, and enable the **Use I\*Ts** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **D** — Derivative gain scalar | vector

Derivative gain, provided from a source external to the block. External gain input is useful,
for example, when you want to map a different PID
parameterization to the PID gains of the block. You can also use
external gain input to implement gain-scheduled PID control. In
gain-scheduled control, you determine the PID coefficients by
logic or other calculation in your model and feed them to the
block.

When you supply gains externally, time variations in the derivative gain are also differentiated. This result occurs because of the way the PID gains are implemented within the block. For details, see the **Controller parameters Source** parameter.

#### Dependencies

To enable this port, set **Controller parameters Source** to
`external`, and set **Controller** to
a controller type that has derivative action.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **N** — Filter coefficient scalar | vector

Derivative filter coefficient, provided from a source external to the block. External
coefficient input is useful, for example, when you want to map a different PID
parameterization to the PID gains of the block. You can also use the external input to
implement gain-scheduled PID control. In gain-scheduled control, you determine the PID
coefficients by logic or other calculation in your model and feed them to the
block.

#### Dependencies

To enable this port, set **Controller parameters Source** to
`external`, and set **Controller** to a
controller type that has a filtered derivative.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **b** — Proportional setpoint weight scalar | vector

Proportional setpoint weight, provided from a source external to the block. External input is useful, for example, when you want to map a different PID parameterization to the PID gains of the block. You can also use the external input to implement gain-scheduled PID control. In gain-scheduled control, you determine the PID coefficients by logic or other calculation in your model and feed them to the block.

#### Dependencies

To enable this port, set **Controller parameters Source** to
`external`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **c** — Derivative setpoint weight scalar | vector

Derivative setpoint weight, provided from a source external to the block. External input is useful, for example, when you want to map a different PID parameterization to the PID gains of the block. You can also use the external input to implement gain-scheduled PID control. In gain-scheduled control, you determine the PID coefficients by logic or other calculation in your model and feed them to the block.

#### Dependencies

To enable this port, set **Controller parameters Source** to
`external`, and set **Controller** to
a controller type that has derivative action.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Reset** — External reset trigger scalar

Trigger to reset the integrator and filter to their initial conditions. Use the
**External reset** parameter to specify what kind of signal
triggers a reset. The port icon indicates the trigger type specified in that parameter.
For example, the following illustration shows a continuous-time PID Controller (2DOF)
block with **External reset** set to
`rising`.

When the trigger occurs, the block resets the integrator and filter to the initial conditions specified by the  **Integrator Initial condition** and **Filter Initial condition** parameters or the **I0** and **D0** ports.

**Note**

To be compliant with the Motor Industry Software Reliability Association (MISRA™) software standard, your model must use Boolean signals to drive the external reset ports of the PID controller block.

#### Dependencies

To enable this port, set **External reset** to any value other than `none`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `Boolean`

### **I0** — Integrator initial condition scalar | vector

Integrator initial condition, provided from a source external to the block.

#### Dependencies

To enable this port, set **Initial conditions Source** to
`external`, and set **Controller** to
a controller type that has integral action.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **D0** — Filter initial condition scalar | vector

Initial condition of the derivative filter, provided from a source external to the
block.

#### Dependencies

To enable this port, set **Initial conditions Source** to
`external`, and set **Controller** to a
controller type that has derivative action.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **up** — Output saturation upper limit scalar | vector

Upper limit of the block output, provided from a source external to the block. If the weighted
sum of the proportional, integral, and derivative actions exceeds the value provided at
this port, the block output is held at that value.

#### Dependencies

To enable this port, select **Limit output** and set the output
saturation **Source** to
`external`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **lo** — Output saturation lower limit scalar | vector

Lower limit of the block output, provided from a source external to the block. If the weighted
sum of the proportional, integral, and derivative
actions goes below the value provided at this
port, the block output is held at that
value.

#### Dependencies

To enable this port, select **Limit output** and set the output saturation
**Source** to `external`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **TR** — Tracking signal scalar | vector

Signal for controller output to track. When signal tracking is active, the difference between
the tracking signal and the block output is fed back to the integrator input. Signal
tracking is useful for implementing bumpless control transfer in systems that switch
between two controllers. It can also be useful to prevent block windup in multiloop
control systems. For more information, see the **Enable tracking mode**
parameter.

#### Dependencies

To enable this port, select the **Enable tracking mode** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **TDTI** — Discrete-integrator time scalar

Discrete-integrator time, provided as a
scalar to the block. You can use your own value of
discrete-time integrator sample time that defines
the rate at which the block is going to be run
either in Simulink or on external hardware. The value
of the discrete-time integrator time should match
the average sampling rate of the external
interrupts, when the block is used inside a
conditionally-executed subsystem.

In other words, you can specify
`Ts` for any of the integrator
methods below such that the value matches the
average sampling rate of the external interrupts.
In discrete time, the derivative term of the
controller transfer function is:

D[N1+Nα(z)],

where *α*(*z*)
depends on the integrator method you specify with
this parameter.

`Forward Euler`
:   α(z)=Tsz−1.

`Backward Euler`
:   α(z)=Tszz−1.

`Trapezoidal`
:   α(z)=Ts2z+1z−1.

For more information about discrete-time
integration, see the Discrete-Time
Integrator block reference page. For more
information on conditionally executed subsystems,
see Conditionally Executed Subsystems Overview.

#### Dependencies

To enable this port, set **Time
Domain** to
`Discrete-time` and
select the **PID Controller is inside a
conditionally executed subsystem**
option.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **extAW** — External anti-windup algorithm scalar | vector

*Since R2024b*

Specify a custom anti-windup algorithm at this port. The block
provides two built-in anti-windup methods, however, to unwind the
integrator, these methods rely on the sum of the block components
exceeding the specified block output limits. If your application has
saturations or limits downstream of the PID controller blocks, you can
use the **extAW** input port to implement a
custom anti-windup logic. The block also provides the signal before the
integrator at the **preInt** output port that you can
use to implement a custom algorithm.

#### Dependencies

To enable this port, on the **Saturation** tab,
select **Limit output** and set
**Anti-windup Method** to
`external`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
### Output

### **Port\_1( u )** — Controller output scalar | vector

Controller output, generally based on a sum of the input signal, the integral of the input signal, and the derivative of the input signal, weighted by the setpoint weights and by the proportional, integral, and derivative gain parameters. A first-order pole filters the derivative action. Which terms are present in the controller signal depends on what you select for the **Controller** parameter. The base controller transfer function for the current settings is displayed in the **Compensator formula** section of the block parameters and under the mask. Other parameters modify the block output, such as saturation limits specified by the **Upper Limit** and **Lower Limit** saturation parameters.

The controller output is a vector signal when any of the inputs is a vector signal. In that case, the block acts as *N* independent PID controllers, where *N* is the number of signals in the input vector.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **preInt** — Pre-integrator signal scalar | vector

*Since R2024b*

The block outputs the signal before the integrator at this port. Use
this signal as an input for the custom anti-windup algorithm you provide
at the **extAW** port.

#### Dependencies

To enable this port, on the **Saturation** tab,
select **Limit output** and set
**Anti-windup Method** to
`external`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Controller** — Controller type `PID` (default) | `PI` | `PD`

Specify which of the proportional, integral, and derivative terms are in the controller.

`PID`
:   Proportional, integral, and derivative action.

`PI`
:   Proportional and integral action only.

`PD`
:   Proportional and derivative action only.

**Tip**

The controller output for the current setting is displayed in the **Compensator
formula** section of the block parameters and under the mask.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Controller` |
| **Type:** string, character vector |
| **Values:** `"PID"`, `"PI"`, `"PD"` |
| **Default:** `"PID"` |

### **Form** — Controller structure `Parallel` (default) | `Ideal`

Specify whether the controller structure is parallel or ideal.

`Parallel`
:   The proportional, integral, and derivative gains **P**, **I**, and **D**, are applied independently. For example, for a continuous-time 2-DOF PID controller in parallel form, the controller output *u* is:

    u=P(br−y)+I1s(r−y)+DN1+N1s(cr−y),

    where *r* is the reference signal, *y* is the measured plant output signal, and *b* and *c* are the setpoint weights.

    For a discrete-time 2-DOF controller in parallel form, the controller output is:

    u=P(br−y)+Iα(z)(r−y)+DN1+Nβ(z)(cr−y),

    where the **Integrator method** and **Filter method** parameters determine *α*(*z*) and *β*(*z*), respectively.

`Ideal`
:   The proportional gain **P** acts on the sum of all actions. For example, for a continuous-time 2-DOF PID controller in ideal form, the controller output is:

    u=P[(br−y)+I1s(r−y)+DN1+N1s(cr−y)].

    For a discrete-time 2-DOF PID controller in ideal form, the transfer function is:

    u=P[(br−y)+Iα(z)(r−y)+DN1+Nβ(z)(cr−y)],

    where the **Integrator method** and **Filter method** parameters determine *α*(*z*) and *β*(*z*), respectively.

    **Tip**

    The controller output for the current settings is displayed in the **Compensator formula** section of the block parameters and under the mask.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Controller` |
| **Type:** string, character vector |
| **Values:** `"Parallel"`, `"Ideal"` |
| **Default:** `"Parallel"` |

### **Time domain** — Specify continuous-time or discrete-time controller `Continuous-time` (default) | `Discrete-time`

When you select `Discrete-time`, it is
recommended that you specify an explicit sample time for the block. See the
**Sample time (-1 for inherited)** parameter. Selecting
`Discrete-time` also enables the
**Integrator method**, and **Filter
method** parameters.

When the PID Controller block is in a model with
synchronous state control (see the State Control (HDL Coder) block), you
cannot select `Continuous-time`.

**Note**

The PID Controller (2DOF) and Discrete PID
Controller (2DOF) blocks are identical except for the
default value of this parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TimeDomain` |
| **Type:** string, character vector |
| **Values:** `"Continuous-time"`, `"Discrete-time"` |
| **Default:** `"Continuous-time"` |

### **PID Controller is inside a conditionally executed subsystem** — Enable the discrete-integrator time port `off` (default) | `on`

For discrete-time PID controllers, enable the discrete-time integrator port to use
your own value of discrete-time integrator sample time. To ensure proper integration,
use the `TDTI` port to provide a scalar value
of Δt for accurate discrete-time integration.

#### Dependencies

To enable this parameter, set **Time Domain** to
`Discrete-time`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UseExternalTs` |
| **Type:** string, character vector |
| **Values:** `"on"`, `"off"` |
| **Default:** `"off"` |

### **Sample time (-1 for inherited)** — Discrete interval between samples –1 (default) | positive scalar

Specify a sample time by entering a positive scalar value, such as 0.1. The default discrete
sample time of –1 means that the block inherits its sample time from upstream blocks.
However, it is recommended that you set the controller sample time explicitly,
especially if you expect the sample time of upstream blocks to change. The effect of the
controller coefficients P, I, D, and N depend on the sample time. Thus, for a given set
of coefficient values, changing the sample time changes the performance of the
controller.

See
Specify Sample Time for more information.

To implement a continuous-time controller, set **Time domain** to `Continuous-time`.

**Tip**

If you want to run the block with an externally specified or variable sample time, set this parameter to –1 and put the block in a Triggered Subsystem. Then, trigger the subsystem at the desired sample time.

#### Dependencies

To enable this parameter, set **Time domain** to `Discrete-time`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** scalar |
| **Values:** `-1`, positive scalar |
| **Default:** `-1` |

### **Integrator method** — Method for computing integral in discrete-time controller `Forward Euler` (default) | `Backward Euler` | `Trapezoidal`

In discrete time, the integral term of the controller transfer function is *Ia*(*z*), where *a*(*z*) depends on the integrator method you specify with this parameter.

`Forward Euler`
:   Forward rectangular (left-hand) approximation,

    α(z)=Tsz−1.

    This method is best for small sampling times, where the Nyquist limit is large compared to the bandwidth of the controller. For larger sampling times, the `Forward Euler` method can result in instability, even when discretizing a system that is stable in continuous time.

`Backward Euler`
:   Backward rectangular (right-hand) approximation,

    α(z)=Tszz−1.

    An advantage of the `Backward Euler` method is that discretizing a stable continuous-time system using this method always yields a stable discrete-time result.

`Trapezoidal`
:   Bilinear approximation,

    α(z)=Ts2z+1z−1.

    An advantage of the `Trapezoidal` method is that discretizing a stable continuous-time system using this method always yields a stable discrete-time result. Of all available integration methods, the `Trapezoidal` method yields the closest match between frequency-domain properties of the discretized system and the corresponding continuous-time system.

    **Tip**

    The controller formula for the current setting is displayed in the
    **Compensator formula** section of the block parameters and
    under the mask.

For more information about discrete-time integration, see the Discrete-Time Integrator block reference page.

#### Dependencies

To enable this parameter, set **Time Domain** to `Discrete-time` and set **Controller** to a controller type with integral action.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IntegratorMethod` |
| **Type:** string, character vector |
| **Values:** `"Forward Euler"`, `"Backward Euler"`, `"Trapezoidal"` |
| **Default:** `"Forward Euler"` |

### **Filter method** — Method for computing derivative in discrete-time controller `Forward Euler` (default) | `Backward Euler` | `Trapezoidal`

In discrete time, the derivative term of the controller transfer function is:

D[N1+Nα(z)],

where *α*(*z*) depends on the filter method you specify
with this parameter.

`Forward Euler`
:   Forward rectangular (left-hand) approximation,

    α(z)=Tsz−1.

    This method is best for small sampling times, where the Nyquist limit is large compared to the bandwidth of the controller. For larger sampling times, the `Forward Euler` method can result in instability, even when discretizing a system that is stable in continuous time.

`Backward Euler`
:   Backward rectangular (right-hand) approximation,

    α(z)=Tszz−1.

    An advantage of the `Backward Euler` method is that discretizing a stable continuous-time system using this method always yields a stable discrete-time result.

`Trapezoidal`
:   Bilinear approximation,

    α(z)=Ts2z+1z−1.

    An advantage of the `Trapezoidal` method is that discretizing a stable continuous-time system using this method always yields a stable discrete-time result. Of all available integration methods, the `Trapezoidal` method yields the closest match between frequency-domain properties of the discretized system and the corresponding continuous-time system.

    **Tip**

    The controller formula for the current setting is displayed in the
    **Compensator formula** section of the block parameters and
    under the mask.

For more information about discrete-time integration, see the Discrete-Time Integrator block reference page.

#### Dependencies

To enable this parameter, set **Time Domain** to
`Discrete-time` and
enable **Use filtered
derivative**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FilterMethod` |
| **Type:** string, character vector |
| **Values:** `"Forward Euler"`, `"Backward Euler"`, `"Trapezoidal"` |
| **Default:** `"Forward Euler"` |

### Main

### **Source** — Source for controller gains and filter coefficient internal (default) | external

`internal`
:   Specify the controller gains, filter coefficient, and setpoint weights using the block parameters **P**, **I**, **D**, **N**, **b**, and **c** respectively.

`external`
:   Specify the PID gains, filter coefficient, and setpoint weights externally using block inputs. An additional input port appears on the block for each parameter that is required for the current controller type.

Enabling external inputs for the parameters allows you to compute their values externally to the block and provide them to the block as signal inputs.

External input is useful, for example, when you want to map a different PID parameterization to the PID gains of the block. You can also use external gain input to implement gain-scheduled PID control. In gain-scheduled control, you determine the PID gains by logic or other calculation in your model and feed them to the block.

When you supply gains externally, time variations in the integral and derivative gain values are integrated and differentiated, respectively. The derivative setpoint weight *c* is also differentiated. This result occurs because in both continuous time and discrete time, the gains are applied to the signal before integration or differentiation. For example, for a continuous-time PID controller with external inputs, the integrator term is implemented as shown in the following illustration.

Within the block, the input signal *u* is multiplied by the externally supplied integrator gain, *I*, before integration. This implementation yields:

ui=∫(r−y)I dt.

Thus, the integrator gain is included in the integral. Similarly, in the derivative term of the block, multiplication by the derivative gain precedes the differentiation, which causes the derivative gain *D* and the derivative setpoint weight *c* to be differentiated.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ControllerParametersSource` |
| **Type:** string, character vector |
| **Values:** `"internal"`, `"external"` |
| **Default:** `"internal"` |

### **Proportional (P)** — Proportional gain 1 (default) | scalar | vector

Specify a finite, real gain value for the proportional gain. When **Controller form** is:

- `Parallel` — Proportional action is independent of the integral and derivative actions. For example, for a continuous-time 2-DOF PID controller in parallel form, the controller output *u* is:

  u=P(br−y)+I1s(r−y)+DN1+N1s(cr−y),

  where *r* is the reference signal, *y* is the measured plant output signal, and *b* and *c* are the setpoint weights.

  For a discrete-time 2-DOF controller in parallel form, the controller output is:

  u=P(br−y)+Iα(z)(r−y)+DN1+Nβ(z)(cr−y),

  where the **Integrator method** and **Filter method** parameters determine *α*(*z*) and *β*(*z*), respectively.
- `Ideal` — The proportional gain multiples the integral and derivative terms. For example, for a continuous-time 2-DOF PID controller in ideal form, the controller output is:

  u=P[(br−y)+I1s(r−y)+DN1+N1s(cr−y)].

  For a discrete-time 2-DOF PID controller in ideal form, the transfer function is:

  u=P[(br−y)+Iα(z)(r−y)+DN1+Nβ(z)(cr−y)],

  where the **Integrator method** and **Filter method** parameters determine *α*(*z*) and *β*(*z*), respectively.

#### Dependencies

To enable this parameter, set the Controller parameters **Source** to `internal`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `P` |
| **Type:** scalar, vector |
| **Default:** 1 |

**Tunable:** Yes

### **Integral (I)** — Integral gain 1 (default) | scalar | vector

Specify a finite, real gain value for the integral gain.

**Tunable:** Yes

#### Dependencies

To enable this parameter, in the **Main** tab, set the controller-parameters
**Source** to `internal`, and set
**Controller** to a type that has integral action.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `I` |
| **Type:** scalar, vector |
| **Default:** 1 |

### **Integral (I\*Ts)** — Integral gain multiplied by sample time 1 (default) | scalar | vector

For discrete-time controllers, specify a finite, real gain value for the integral gain
multiplied by the sample time.

**Note**

PID tuning tools, such as the PID Tuner app and Closed-Loop PID Autotuner block, tune the gain **I** but not **I\*Ts**. Therefore, multiply the integral gain value you obtain from a tuning tool by the sample time before you write it to this parameter.

When you use **I\*Ts** instead of **I**, the block requires fewer calculations to perform integration. This improves the execution time of the generated code.

For continuous-time controllers, disable **Use I\*Ts** and use the
**I** parameter instead.

**Tunable:** No

#### Dependencies

To enable this parameter, in the **Main** tab, set the controller-parameters **Source** to `internal`, set **Controller** to a type that has integral action, and enable the **Use I\*Ts** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `I` |
| **Type:** scalar, vector |
| **Default:** 1 |

### **Use I\*Ts** — Use integral gain multiplied by sample time `off` (default) | `on`

For discrete-time controllers with integral action, the block takes the integral gain as an
input and multiplies it by the sample time internally as a part of performing the
integration. If you enable this parameter, you explicitly specify integral gain
multiplied by sample time as input (**I\*Ts**) in place of the integral
gain (**I**). Doing so reduces the number of internal calculations and
is useful when you want to improve the execution time of your generated code.

If you have enabled signal tracking or the anti-windup mode back-calculation and you
enable **I\*Ts**, then you must also set the tracking gain parameter
**Kt** to `Kt*Ts` and the back-calculation
coefficient **Kb** to `Kb*Ts`.

For continuous-time controllers, enabling this parameter has no effect on the integral
gain.

#### Dependencies

To enable this parameter, set **Controller** to a controller type that has integral action.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UseKiTs` |
| **Type:** string, character vector |
| **Values:** `"on"`, `"off"` |
| **Default:** `"on"` |

### **Derivative (D)** — Derivative gain 0 (default) | scalar | vector

Specify a finite, real gain value for the derivative gain.

**Tunable:** Yes

#### Dependencies

To enable this parameter, in the **Main** tab, set the controller-parameters
**Source** to `internal`, and set
**Controller** to `PID` or
`PD`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `D` |
| **Type:** scalar, vector |
| **Default:** 0 |

### **Use externally sourced derivative** — Specify derivative at block input port `off` (default) | `on`

*Since R2024a*

Select this option to specify the derivative of the plant signal
*y* directly as an input **ydot**
to the block. This is helpful when you have the derivative signal
available in your model and want to skip the computation of the
derivative inside the block.

#### Dependencies

To enable this option, select a controller type that has
derivative action.

### **Use filtered derivative** — Apply filter to derivative term `on` (default) | `off`

For discrete-time PID controllers only, clear this option to replace the filtered derivative with an unfiltered discrete-time differentiator. When you do so, the derivative term of the controller output becomes:

Dz−1zTs(cr−y).

For continuous-time PID controllers, the derivative term is always filtered.

#### Dependencies

To enable this parameter, set **Time domain** to `Discrete-time`, and set **Controller** to a type that has a derivative term.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UseFilter` |
| **Type:** string, character vector |
| **Values:** `"on"`, `"off"` |
| **Default:** `"on"` |

### **Filter coefficient (N)** — Derivative filter coefficient 100 (default) | scalar | vector

Specify a finite, real gain value for the filter coefficient. The filter coefficient
determines the pole location of the filter in the derivative action of the
block. The location of the filter pole depends on the **Time
domain** parameter.

- When **Time domain** is
  `Continuous-time`, the pole
  location is `s = -N`.
- When **Time domain** is
  `Discrete-time`, the pole
  location depends on the **Filter method**
  parameter.

  | Filter Method | Location of Filter Pole |
  | --- | --- |
  | `Forward Euler` | zpole=1−NTs |
  | `Backward Euler` | zpole=11+NTs |
  | `Trapezoidal` | zpole=1−NTs/21+NTs/2 |

The block does not support `N = Inf` (ideal unfiltered derivative). When the **Time domain** is `Discrete-time`, you can clear **Use filtered derivative** to remove the derivative filter.

#### Dependencies

To enable this parameter, in the **Main** tab, set the controller-parameters
**Source** to
`internal` and set
**Controller** to
`PID` or
`PD`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `N` |
| **Type:** scalar, vector |
| **Default:** 100 |

**Tunable:** Yes

### **Setpoint weight (b)** — Proportional setpoint weight 1 (default) | scalar | vector

Setpoint weight on the proportional term of the controller. The proportional term of a 2-DOF
controller output is
*P*(*br*–*y*),
where *r* is the reference signal
and *y* is the measured plant
output. Setting *b* to 0
eliminates proportional action on the reference
signal, which can reduce overshoot in the system
response to step changes in the setpoint. Changing
the relative values of *b* and
*c* changes the balance between
disturbance rejection and setpoint
tracking.

**Tunable:** Yes

#### Dependencies

To enable this parameter, in the **Main** tab, set the controller-parameters
**Source** to `internal`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `b` |
| **Type:** scalar, vector |
| **Default:** 1 |

### **Setpoint weight (c)** — Derivative setpoint weight 1 (default) | scalar | vector

Setpoint weight on the derivative term of the controller. The derivative term of a 2-DOF
controller acts on *cr*–*y*, where
*r* is the reference signal and *y* is the
measured plant output. Thus, setting *c* to 0 eliminates derivative
action on the reference signal, which can reduce transient response to step changes in
the setpoint. Setting *c* to 0 can yield a controller that achieves
both effective disturbance rejection and smooth setpoint tracking without excessive
transient response. Changing the relative values of *b* and
*c* changes the balance between disturbance rejection and setpoint
tracking.

**Tunable:** Yes

#### Dependencies

To enable this parameter, in the **Main** tab, set the controller-parameters
**Source** to `internal` and set
**Controller** to a type that has derivative action.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `c` |
| **Type:** scalar, vector |
| **Default:** 1 |

### **Select tuning method** — Tool for automatic tuning of controller coefficients `Transfer Function Based (PID Tuner App)` (default) | `Frequency Response Based`

If you have Simulink
Control Design software, you can automatically tune the PID coefficients when they are
internal to the block. To do so, use this parameter to select a tuning tool, and click
**Tune**.

`Transfer Function Based (PID Tuner App)`
:   Use PID Tuner, which lets you interactively tune PID coefficients while examining relevant system responses to validate performance. PID Tuner can tune all the coefficients **P**, **I**, **D**, and **N**, and the setpoint coefficients **b** and **c**. By default, PID Tuner works with a linearization of your plant model. For models that cannot be linearized, you can tune PID coefficients against a plant model estimated from simulated or measured response data. For more information, see Design Two-Degree-of-Freedom PID Controllers (Simulink Control Design).

`Frequency Response Based`
:   Use Frequency Response Based PID Tuner, which tunes PID controller coefficients based on frequency-response estimation data obtained by simulation. This tuning approach is especially useful for plants that are not linearizable or that linearize to zero. Frequency Response Based PID Tuner tunes the coefficients **P**, **I**, **D**, and **N**, but does not tune the setpoint coefficients **b** and **c**. For more information, see Design PID Controller from Plant Frequency-Response Data (Simulink Control Design).

Both of these tuning methods assume a single-loop control configuration. Simulink
Control Design software includes other tuning approaches that suit more complex configurations. For information about other ways to tune a PID Controller block, see Choose a Control Design Approach (Simulink Control Design).

#### Dependencies

To enable this parameter, in the **Main** tab, set the
controller-parameters **Source** to
`internal`.

### **Enable zero-crossing detection** — Detect zero crossings on reset and on entering or leaving a saturation state `on` (default) | `off`

Zero-crossing detection can accurately locate signal discontinuities without resorting to excessively small time steps that can lead to lengthy simulation times. If you select **Limit output** or activate **External reset** in your PID Controller block, activating zero-crossing detection can reduce computation time in your simulation. Selecting this parameter activates zero-crossing detection:

- At initial-state reset
- When entering an upper or lower saturation state
- When leaving an upper or lower saturation state

For more information about zero-crossing detection, see Zero-Crossing Detection.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ZeroCross` |
| **Type:** string, character vector |
| **Values:** `"on"`, `"off"` |
| **Default:** `"on"` |

### Initialization

### **Source** — Source for integrator and derivative initial conditions `internal` (default) | `external`

Simulink uses initial conditions to initialize the integrator and derivative-filter
(or the unfiltered derivative) output at the start of a simulation or at a specified
trigger event. (See the **External reset** parameter.) These initial
conditions determine the initial block output. Use this parameter to select how to
supply the initial condition values to the block.

`internal`
:   Specify the initial conditions using the **Integrator Initial
    condition** and **Filter Initial condition**
    parameters. If **Use filtered derivative** is not selected,
    use the **Differentiator** parameter to specify the initial
    condition for the unfiltered differentiator instead of a filter initial
    condition.

`external`
:   Specify the initial conditions externally using block inputs. Additional
    input ports **Io** and
    **Do** appear on the block.
    If **Use filtered derivative** is not selected, supply the
    initial condition for the unfiltered differentiator at
    **Do** instead of a filter
    initial condition.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialConditionSource` |
| **Type:** string, character vector |
| **Values:** `"internal"`, `"external"` |
| **Default:** `"internal"` |

### **Integrator** — Integrator initial condition 0 (default) | scalar | vector

Simulink uses the integrator initial condition to initialize the integrator at the start of a simulation or at a specified trigger event (see **External reset**). The integrator initial condition and the filter initial condition determine the initial output of the PID controller block.

The integrator initial condition cannot be `NaN` or `Inf`.

#### Dependencies

To use this parameter, in the **Initialization** tab, set
**Source** to `internal`, and set
**Controller** to a type that has integral action.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialConditionForIntegrator` |
| **Type:** scalar, vector |
| **Default:** 0 |

### **Filter** — Filter initial condition 0 (default) | scalar | vector

Simulink uses the filter initial condition to initialize the derivative filter at the start of a simulation or at a specified trigger event (see **External reset**). The integrator initial condition and the filter initial condition determine the initial output of the PID controller block.

The filter initial condition cannot be `NaN` or `Inf`.

#### Dependencies

To use this parameter, in the **Initialization** tab, set
**Source** to `internal`, and use a
controller that has a derivative filter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialConditionForFilter` |
| **Type:** scalar, vector |
| **Default:** 0 |

### **Differentiator** — Initial condition for unfiltered derivative 0 (default) | scalar | vector

When you use an unfiltered derivative, Simulink uses this parameter to initialize the differentiator at the start of a simulation or at a specified trigger event (see **External reset**). The integrator initial condition and the derivative initial condition determine the initial output of the PID controller block.

The derivative initial condition cannot be `NaN` or `Inf`.

#### Dependencies

To use this parameter, set **Time domain** to `Discrete-time`, clear the **Use filtered derivative** check box, and in the **Initialization** tab, set **Source** to `internal`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DifferentiatorICPrevScaledInput` |
| **Type:** scalar, vector |
| **Default:** 0 |

### **Initial condition setting** — Location at which initial condition is applied `Auto` (default) | `Output`

Use this parameter to specify whether to apply the **Integrator Initial condition** and **Filter Initial condition** parameter to the corresponding block state or output. You can change this parameter at the command line only, using `set_param` to set the `InitialConditionSetting` parameter of the block.

`Auto`
:   Use this option in all situations except when the block is in a triggered subsystem or a function-call subsystem and simplified initialization mode is enabled.

`Output`
:   Use this option when the block is in a triggered subsystem or a function-call subsystem and simplified initialization mode is enabled.

For more information about the **Initial condition setting** parameter, see the Discrete-Time Integrator block.

This parameter is only accessible through programmatic use.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialConditionSetting` |
| **Type:** string, character vector |
| **Values:** `"Auto"`, `"Output"` |
| **Default:** `"Auto"` |

### **External reset** — Trigger for resetting integrator and filter values `none` (default) | `rising` | `falling` | `either` | `level`

Specify the trigger condition that causes the block to reset the integrator and filter to initial conditions. (If **Use filtered derivative** is not selected, the trigger resets the integrator and differentiator to initial conditions.) Selecting any option other than `none` enables the **Reset** port on the block for the external reset signal.

`none`
:   The integrator and filter (or differentiator) outputs are set to initial conditions at the beginning of simulation, and are not reset during simulation.

`rising`
:   Reset the outputs when the reset signal has a rising edge.

`falling`
:   Reset the outputs when the reset signal has a falling edge.

`either`
:   Reset the outputs when the reset signal either rises or falls.

`level`
:   Reset the outputs when the reset signal either:

    - Is nonzero at the current time step
    - Changes from nonzero at the previous time step to zero at the current time step

    This option holds the outputs to the initial conditions while the reset signal is nonzero.

#### Dependencies

To enable this parameter, set **Controller** to a type that has derivative or
integral action.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ExternalReset` |
| **Type:** string, character vector |
| **Values:** `"none"`, `"rising"`, `"falling"`, `"either"`,`"level"` |
| **Default:** `"none"` |

### **Ignore reset when linearizing** — Force linearization to ignore reset `off` (default) | `on`

Select to force Simulink and Simulink
Control Design linearization commands to ignore any reset mechanism specified in the **External reset** parameter. Ignoring reset states allows you to linearize a model around an operating point even if that operating point causes the block to reset.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IgnoreLimit` |
| **Type:** string, character vector |
| **Values:** `"off"`, `"on"` |
| **Default:** `"off"` |

### **Enable tracking mode** — Activate signal tracking `off` (default) | `on`

Signal tracking lets the block output follow a tracking signal that you provide at the **TR** port. When signal tracking is active, the difference between the tracking signal and the block output is fed back to the integrator input with a gain `Kt`, specified by the **Tracking gain (Kt)** parameter. Signal tracking has several applications, including bumpless control transfer and avoiding windup in multiloop control structures.

#### Bumpless control transfer

Use signal tracking to achieve bumpless control transfer in systems that switch between two controllers. Suppose you want to transfer control between a PID controller and another controller. To do so, connecting the controller output to the **TR** input as shown in the following illustration.

For more information, see Bumpless Control Transfer with a Two-Degree-of-Freedom PID Controller.

#### Multiloop control

Use signal tracking to prevent block windup in multiloop control approaches. For an example illustrating this approach with a 1DOF PID controller, see Prevent Block Windup in Multiloop Control.

#### Dependencies

To enable this parameter, set **Controller** to a type that has
integral action.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TrackingMode` |
| **Type:** string, character vector |
| **Values:** `"off"`, `"on"` |
| **Default:** `"off"` |

### **Tracking coefficient (Kt)** — Gain of signal-tracking feedback loop 1 (default) | scalar

When you select **Enable tracking mode**, the difference between the signal **TR** and the block output is fed back to the integrator input with a gain `Kt`. Use this parameter to specify the gain in that feedback loop.

For discrete-time controllers, if you select the **Use I\*Ts**
parameter of the block, then set this parameter to the value `Kt*Ts`,
where `Kt` is the desired gain and `Ts` is the sample
time.

#### Dependencies

To enable this parameter, select **Enable tracking mode**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Kt` |
| **Type:** scalar |
| **Default:** 1 |

### Saturation

#### Output saturation

### **Limit Output** — Limit block output to specified saturation values `off` (default) | `on`

Activating this option limits the block output, so that you do not need a separate Saturation block after the controller. It also allows you
to activate the anti-windup mechanism built into the block (see the
**Anti-windup method** parameter). Specify the output saturation
limits using the **Lower limit** and **Upper limit**
parameters. You can also specify the saturation limits externally as block input
ports.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LimitOutput` |
| **Type:** string, character vector |
| **Values:** `"off"`, `"on"` |
| **Default:** `"off"` |

### **Source** — Source for output saturation limits internal (default) | external

Use this parameter to specify how to supply the upper and lower saturation limits of
the block output.

`internal`
:   Specify the output saturation limits using the **Upper
    limit** and **Lower limit** parameters.

`external`
:   Specify the output saturation limits externally using block input ports.
    The additional input ports **up** and
    **lo** appear on the block. You can use the input ports
    to implement the upper and lower output saturation limits determined by
    logic or other calculations in the Simulink model and passed to the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SatLimitsSource` |
| **Type:** string, character vector |
| **Values:** `"internal"`, `"external"` |
| **Default:** `"internal"` |

### **Upper limit** — Upper saturation limit for block output `Inf` (default) | scalar

Specify the upper limit for the block output. The block output is held at the **Upper saturation limit** whenever the weighted sum of the proportional, integral, and derivative actions exceeds that value.

#### Dependencies

To enable this parameter, select **Limit output**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UpperSaturationLimit` |
| **Type:** scalar |
| **Default:** `Inf` |

### **Lower limit** — Lower saturation limit for block output `-Inf` (default) | scalar

Specify the lower limit for the block output. The block output is held at the **Lower saturation limit** whenever the weighted sum of the proportional, integral, and derivative actions goes below that value.

#### Dependencies

To enable this parameter, select **Limit output**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LowerSaturationLimit` |
| **Type:** scalar |
| **Default:** `-Inf` |

### **Ignore saturation when linearizing** — Force linearization to ignore output limits `off` (default) | `on`

Force Simulink and Simulink
Control Design linearization commands to ignore block output limits specified in the **Upper limit** and **Lower limit** parameters. Ignoring output limits allows you to linearize a model around an operating point even if that operating point causes the block to exceed the output limits.

#### Dependencies

To enable this parameter, select the **Limit output**
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LinearizeAsGain` |
| **Type:** string, character vector |
| **Values:** `"off"`, `"on"` |
| **Default:** `"off"` |

### **Anti-windup method** — Integrator anti-windup method `none` (default) | `back-calculation` | `clamping` | `external`

When you select **Limit output** and the weighted sum of the
controller components exceeds the specified output limits, the block output holds at the
specified limit. However, the integrator output can continue to grow (integrator
windup), increasing the difference between the block output and the sum of the block
components. In other words, the internal signals in the block can be unbounded even if
the output appears bounded by saturation limits. Without a mechanism to prevent
integrator windup, two results are possible:

- If the sign of the signal entering the integrator never changes, the
  integrator continues to integrate until it overflows. The overflow value is
  the maximum or minimum value for the data type of the integrator
  output.
- If the sign of the signal entering the integrator changes once the
  weighted sum has grown beyond the output limits, it can take a long time to
  unwind the integrator and return the weighted sum within the block
  saturation limit.

In either case, controller performance can suffer. To combat the effects of windup
without an anti-windup mechanism, it may be necessary to detune the controller (for
example, by reducing the controller gains), resulting in a sluggish controller. To avoid
this problem, activate an anti-windup mechanism using this parameter.

`none`
:   Do not use an anti-windup mechanism.

`back-calculation`
:   Unwind the integrator when the block output saturates by feeding back to
    the integrator the difference between the saturated and unsaturated control
    signal. The following diagram represents the back-calculation feedback
    circuit for a continuous-time controller. To see the actual feedback circuit
    for your controller configuration, right-click the block and select **Mask** > **Look Under Mask**.

    Use the **Back-calculation coefficient (Kb)** parameter
    to specify the gain of the anti-windup feedback circuit. It is usually
    satisfactory to set `Kb = I`, or for controllers with
    derivative action, `Kb = sqrt(I*D)`. Back-calculation can
    be effective for plants with relatively large dead time
    [1].

`clamping`
:   Clamping is sometimes referred to as conditional integration.

    Integration stops when both of the following conditions are true:

    - The sum of the block components exceeds the output limits.
    - The integrator input and saturation block input have the same
      sign.

    Integration resumes when either of these conditions is no longer
    true.

    Clamping can be useful for plants with relatively small dead times, but
    can yield a poor transient response for large dead times
    [1].

`external` *(since R2024b)*
:   The built-in anti-windup methods rely on the sum of the block components
    exceeding the specified block output limits. If your application has
    saturations or limits downstream of the PID controller blocks, you can use
    the **extAW** input port to implement a custom
    anti-windup logic. The block also provides the signal before the integrator
    at the **preInt** output port that you can use as input to
    your custom algorithm.

#### Dependencies

To enable this parameter, select the **Limit output**
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AntiWindupMode` |
| **Type:** string, character vector |
| **Values:** `"none"`, `"back-calculation"`,`"clamping"`, `"external"` |
| **Default:** `"none"` |

### **Back-calculation coefficient (Kb)** — Gain coefficient of anti-windup feedback loop 1 (default) | scalar

The `back-calculation` anti-windup method unwinds the integrator when the
block output saturates. It does so by feeding back to the integrator the difference
between the saturated and unsaturated control signal. Use the **Back-calculation
coefficient (Kb)** parameter to specify the gain of the anti-windup
feedback circuit. For more information, see the **Anti-windup method**
parameter.

For discrete-time controllers, if you select the **Use I\*Ts**
parameter of the block, then set this parameter to the value `Kb*Ts`,
where `Kb` is the desired coefficient and `Ts` is the
sample time.

#### Dependencies

To enable this parameter, select the **Limit output** parameter, and set the
**Anti-windup method** parameter to
`back-calculation`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Kb` |
| **Type:** scalar |
| **Default:** 1 |

#### Integrator saturation

### **Limit Output** — Limit integrator output to specified saturation limits `off` (default) | `on`

Enable this parameter to limit the integrator output to be within a specified range. When the
integrator output reaches the limits, the integral action turns off to prevent integral
windup. Specify the saturation limits using the **Lower limit** and
**Upper limit** parameters.

#### Dependencies

To enable this parameter, set **Controller** to a controller type
that has integral action.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LimitIntegratorOutput` |
| **Type:** string, character vector |
| **Values:** `"off"`, `"on"` |
| **Default:** `"off"` |

### **Upper limit** — Upper saturation limit for integrator `Inf` (default) | scalar

Specify the upper limit for the integrator output. The integrator output is held at this value whenever it would otherwise exceed this value.

#### Dependencies

To enable this parameter, under **Integrator saturation**, select **Limit output**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UpperIntegratorSaturationLimit` |
| **Type:** scalar |
| **Default:** `Inf` |

### **Lower limit** — Lower saturation limit for integrator `-Inf` (default) | scalar

Specify the lower limit for the integrator output. The integrator output is held at this value whenever it would otherwise go below this value.

#### Dependencies

To enable this parameter, under **Integrator saturation**, select **Limit output**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LowerIntegratorSaturationLimit` |
| **Type:** scalar |
| **Default:** `-Inf` |

### Data Types

The parameters in this tab are primarily of use in fixed-point code generation using Fixed-Point Designer™. They define how numeric quantities associated with the block are stored and processed when you generate code.

If you need to configure data types for fixed-point code generation, click **Open Fixed-Point Tool** and use that tool to configure the rest of the parameters in the tab. For information about using Fixed-Point Tool, see Autoscaling Data Objects Using the Fixed-Point Tool (Fixed-Point Designer).

After you use Fixed-Point Tool, you can use the parameters in this tab to make adjustments to fixed-point data-type settings if necessary. For each quantity associated with the block, you can specify:

- Floating-point or fixed-point data type, including whether the data type is inherited from upstream values in the block.
- The minimum and maximum values for the quantity, which determine how the quantity is scaled for fixed-point representation.

For assistance in selecting appropriate values, click  to open the Data Type Assistant for the corresponding quantity. For more information, see Specify Data Types Using Data Type Assistant.

The specific quantities listed in the Data Types tab vary depending on how you configure the PID controller block. In general, you can configure data types for the following types of quantities:

- Product output — Stores the result of a multiplication carried out under the block mask. For example, **P product output** stores the output of the gain block that multiplies the block input with the proportional gain **P**.
- Parameter — Stores the value of a numeric block parameter, such as **P**, **I**, or **D**.
- Block output — Stores the output of a block that resides under the PID controller block mask. For example, use **Integrator output** to specify the data type of the output of the block called Integrator. This block resides under the mask in the Integrator subsystem, and computes integrator term of the controller action.
- Accumulator — Stores values associated with a sum block. For example,
  **SumI2 Accumulator** sets the data type of the accumulator
  associated with the sum block SumI2. This block resides under the mask in the Back
  Calculation subsystem of the Anti-Windup subsystem.

In general, you can find the block associated with any listed parameter by looking under the
PID Controller block mask and examining its subsystems. You can also use the Model Explorer
to search under the mask for the listed parameter name, such as `SumI2`.
(See Model
Explorer.)

**Matching Input and Internal Data Types**

By default, all data types in the block are set to `Inherit: Inherit via internal rule`. With this setting, Simulink chooses data types to balance numerical accuracy, performance, and generated code size, while accounting for the properties of the embedded target hardware.

Under some conditions, incompatibility can occur between data types within the block. For
instance, in continuous time, the Integrator block under the mask can accept only signals of
type `double`. If the block input signal is a type that cannot be
converted to `double`, such as `uint16`,
the internal rules for type inheritance generate an error when you generate code.

To avoid such errors, you can use the Data Types settings to force a data type conversion. For
instance, you can explicitly set **P product output**, **I product
output**, and **D product output** to
`double`, ensuring that the signals reaching the
continuous-time integrators are of type `double`.

In general, it is not recommended to use the block in continuous time for code generation
applications. However, similar data type errors can occur in discrete time, if you
explicitly set some values to data types that are incompatible with downstream signal
constraints within the block. In such cases, use the Data Types settings to ensure that all
data types are internally compatible.

#### Fixed-Point Operational Parameters

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations. For more information, see Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To control the
rounding of a block parameter, enter an expression using a MATLAB® rounding function into the mask field.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RndMeth` |
| **Values:** | `'Floor'` (default) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Saturate on integer overflow** — Method of overflow action `off` (default) | `on`

Specify whether overflows saturate or wrap.

- `on` — Overflows saturate to either the minimum or maximum
  value that the data type can represent.
- `off` — Overflows wrap to the appropriate value that the data
  type can represent.

For example, the maximum value that the signed 8-bit integer `int8`
can represent is 127. Any block operation result greater than this maximum value causes
overflow of the 8-bit integer.

- With this parameter selected, the block output saturates at 127.
  Similarly, the block output saturates at a minimum output value of
  -128.
- With this parameter cleared, the software interprets the overflow-causing
  value as `int8`, which can produce an unintended result.
  For example, a block result of 130 (binary 1000 0010) expressed as
  `int8` is -126.

#### Tips

- Consider selecting this parameter when your model has a possible overflow
  and you want explicit saturation protection in the generated code.
- Consider clearing this parameter when you want to optimize efficiency of
  your generated code. Clearing this parameter also helps you to avoid
  overspecifying how a block handles out-of-range signals. For more
  information, see Troubleshoot Signal Range Errors.
- When you select this parameter, saturation applies to every internal
  operation on the block, not just the output or result.
- In general, the code generation process can detect when overflow is not
  possible. In this case, the code generator does not produce saturation
  code.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **Values:** | `'off'` (default) | `'on'` |

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types you specify on this block. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LockScale` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### State Attributes

The parameters in this tab are primarily of use in code generation.

### **State name (e.g., 'position')** — Name for continuous-time filter and integrator states `''` (default) | character vector

Assign a unique name to the state associated with the integrator or the filter, for continuous-time PID controllers. (For information about state names in a discrete-time PID controller, see the **State name** parameter.) The state name is used, for example:

- For the corresponding variable in generated code
- As part of the storage name when logging states during simulation
- For the corresponding state in a linear model obtain by linearizing the block

A valid state name begins with an alphabetic or underscore character, followed by alphanumeric or underscore characters.

#### Dependencies

To enable this parameter, set **Time domain** to `Continuous-time`.

#### Programmatic Use

|  |
| --- |
| **Parameter:**  `IntegratorContinuousStateAttributes`, `FilterContinuousStateAttributes` |
| **Type:**  character vector |
| **Default:**  `''` |

### **State name** — Names for discrete-time filter and integrator states empty string (default) | string | character vector

Assign a unique name to the state associated with the integrator or the filter, for discrete-time PID controllers. (For information about state names in a continuous-time PID controller, see the **State name (e.g., 'position')** parameter.)

A valid state name begins with an alphabetic or underscore character, followed by alphanumeric or underscore characters. The state name is used, for example:

- For the corresponding variable in generated code
- As part of the storage name when logging states during simulation
- For the corresponding state in a linear model obtain by linearizing the block

For more information about the use of state names in code generation, see C Data Code Interface Configuration for Model Interface Elements (Simulink Coder).

#### Dependencies

To enable this parameter, set **Time domain** to `Discrete-time`.

#### Programmatic Use

|  |
| --- |
| **Parameter:**  `IntegratorStateIdentifier`, `FilterStateIdentifier` |
| **Type:**  string, character vector |
| **Default:**  `""` |

### **State name must resolve to Simulink signal object** — Require that state name resolve to a signal object `off` (default) | `on`

Select this parameter to require that the discrete-time integrator or filter state name resolves to a Simulink signal object.

#### Dependencies

To enable this parameter for the discrete-time integrator or filter state:

1. Set **Time domain** to `Discrete-time`.
2. Specify a value for the integrator or filter **State name**.
3. Set the model configuration parameter **Signal resolution** to a value other than `None`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IntegratorStateMustResolveToSignalObject`, `FilterStateMustResolveToSignalObject` |
| **Type:** string, character vector |
| **Values:** `"off"`, `"on"` |
| **Default:** `"off"` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

For continuous-time PID controllers (**Time domain** set to `Continuous-time`):

- Consider using Model Discretizer to map
  continuous-time blocks to discrete equivalents that support
  code generation. To access Model Discretizer, in the
  **Apps** tab, under
  **Control Systems**, click
  **Model Discretizer**.
- Not recommended for production code.

For discrete-time PID controllers (**Time domain** set to `Discrete-time`):

- Depends on absolute time when placed inside a triggered subsystem hierarchy.
- Generated code relies on `memcpy` or `memset` functions (`string.h`) under certain conditions.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Fixed-point code generation is supported for discrete-time PID controllers only (**Time domain** set to `Discrete-time`).

## Version History

**Introduced in R2009b**

### R2024b: Specify anti-windup algorithm externally using new ports

The block now allows you to specify an anti-windup algorithm externally using a new
input port **extAW**. The block also provides the signal before the
integrator at the **preInt** output port that you can use as input for
the custom algorithm. The PID controller blocks provide two built-in anti-windup
methods, however, to unwind the integrator, these methods rely on the sum of the block
components exceeding the specified block output limits. If your application has
saturations or limits downstream of the PID controller blocks, you can use the new
**extAW** and **preInt** ports to implement a
custom anti-windup logic. To enable the new ports, on the
**Saturation** tab, select **Limit Output** and
set **Anti-windup Method** to
`external`.

### R2024a: Use derivative signal from external source

The PID controller blocks now allow you to supply the derivative of the plant signal
*y* directly as an input to the block. This is helpful when you
have the derivative signal available in your model and want to skip the computation of
the derivative inside the block.

To enable the input port for supplying the derivative, select a controller type that
has derivative action and enable the **Use externally sourced
derivative** parameter.

### R2022b: Issues error when integrator and filter initial conditions lie outside saturation limits

The block now issues an error when the integrator or filter initial condition value
lies outside the output saturation limits. In previous releases, the block did not issue
an error when these initial conditions had such values.

If this change impacts your model, update the PID integrator or filter initial
condition values such that they are within the output saturation limits.

### R2021b: `ReferenceBlock` parameter returns different path

Starting in R2021b, the `get_param` function returns a different
value for the `ReferenceBlock` parameter. The
`ReferenceBlock` parameter is a property common to all Simulink blocks and gives the path of the library block to which a block links. The
PID Controller (2DOF) and Discrete PID Controller
(2DOF) blocks now link to `'slpidlib/PID Controller
(2DOF)'`. Previously, the blocks linked to `'pid_lib/PID Controller
(2DOF)'`.

This change does not affect any other functionality or workflows. You can still use
the previous path with the `set_param` function.

### R2020b: `ReferenceBlock` parameter returns different path

Starting in R2020b, the `get_param` function returns a different
value for the `ReferenceBlock` parameter. The
`ReferenceBlock` parameter is a property common to all Simulink blocks and gives the path of the library block to which a block links. The
PID Controller (2DOF) and Discrete PID Controller
(2DOF) blocks now link to `'pid_lib/PID Controller
(2DOF)'`. Previously, the blocks linked to `'simulink/Continuous/PID
Controller (2DOF)'`.

This change does not affect any other functionality or workflows. You can still use the previous path with the `set_param` function.
