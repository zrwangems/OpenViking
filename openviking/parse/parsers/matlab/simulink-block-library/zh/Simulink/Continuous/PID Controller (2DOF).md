---
type: simulink-block
title: 'PID Controller (2DOF)'
family: 'control'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Linear Parameter Varying'
documentation_page: 'pidcontroller2dof'
documentation_source_path: 'slref/pidcontroller2dof.html'
language: zh-CN
chinese_source: worker-translation
---

# PID Controller (2DOF)

## 端口
```yaml
ports:
- name: Ref
  summary: 参考信号 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1( y )
  summary: 测量的系统输出 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: ydot
  summary: 外部来源的微分 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: P
  summary: 比例增益 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: I
  summary: 积分增益 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: I\*Ts
  summary: 积分增益乘以采样时间 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: D
  summary: 微分增益 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: N
  summary: 滤波器系数 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: b
  summary: 比例设定点权重 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: c
  summary: 微分设定点权重 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Reset
  summary: 外部复位触发 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point | Boolean
- name: I0
  summary: 积分器初始条件 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: D0
  summary: 滤波器初始条件 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: up
  summary: 输出饱和上限 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: lo
  summary: 输出饱和下限 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: TR
  summary: 跟踪信号 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: TDTI
  summary: 离散积分器时间 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64
- name: extAW
  summary: 外部抗积分饱和算法 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64
- name: Port_1( u )
  summary: 控制器输出 标量 | 向量
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: preInt
  summary: 积分器前信号 标量 | 向量
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输入

### **Ref** — 参考信号 标量 | 向量

被控对象要跟踪的参考信号，如图所示。

当参考信号为向量时，该模块对每个信号分别作用，将 PID 系数向量化，并产生相同维度的向量输出信号。您可以将 PID 系数和其他一些参数指定为与输入信号维度相同的向量。这样做等效于为输入信号中的每个条目指定一个单独的 PID 控制器。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_1( y )** — 测量的系统输出 标量 | 向量

来自被控对象输出的控制器反馈信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **ydot** — 外部来源的微分 标量 | 向量

*自 R2024a 起*

将被控对象信号 *y* 的微分直接作为输入提供给该模块。当您的模型中已有微分信号并希望跳过模块内部的微分计算时，这非常有用。

#### 依赖关系

要启用此输入端口，请选择具有微分作用的控制器类型，并启用 **Use externally sourced derivative**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **P** — 比例增益 标量 | 向量

比例增益，由模块外部的来源提供。外部增益输入非常有用，例如，当您想将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部增益输入来实现增益调度 PID 控制。在增益调度控制中，您通过模型中的逻辑或其他计算确定 PID 系数，并将它们馈送到模块。

#### 依赖关系

要启用此端口，请将 **Controller parameters Source** 设置为 `external`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **I** — 积分增益 标量 | 向量

积分增益，由模块外部的来源提供。外部增益输入非常有用，例如，当您想将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部增益输入来实现增益调度 PID 控制。在增益调度控制中，您通过模型中的逻辑或其他计算确定 PID 系数，并将它们馈送到模块。

当您从外部提供增益时，积分增益的时间变化也会被积分。这一结果是由于 PID 增益在模块内部的实现方式所致。有关详细信息，请参阅 **Controller parameters Source** 参数。

#### 依赖关系

要启用此端口，请将 **Controller parameters Source** 设置为 `external`，并将 **Controller** 设置为具有积分作用的控制器类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **I\*Ts** — 积分增益乘以采样时间 标量 | 向量

对于离散时间控制器，积分增益乘以控制器采样时间，由模块外部的来源提供。外部增益输入非常有用，例如，当您想将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部增益输入来实现增益调度 PID 控制。在增益调度控制中，您通过模型中的逻辑或其他计算确定 PID 系数，并将它们馈送到模块。

**注意**

PID 整定工具（如 PID Tuner 应用和 Closed-Loop PID Autotuner 模块）整定的是增益 **I** 而非 **I\*Ts**。因此，在将整定工具获得的积分增益值提供给此端口之前，请先将其乘以采样时间。

当您使用 **I\*Ts** 而非 **I** 时，模块执行积分所需的计算更少。这改善了生成代码的执行时间。

对于连续时间控制器，请禁用 **Use I\*Ts** 并使用 **I** 端口。

#### 依赖关系

要启用此端口，请将 **Controller parameters Source** 设置为 `external`，将 **Controller** 设置为具有积分作用的控制器类型，并启用 **Use I\*Ts** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **D** — 微分增益 标量 | 向量

微分增益，由模块外部的来源提供。外部增益输入非常有用，例如，当您想将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部增益输入来实现增益调度 PID 控制。在增益调度控制中，您通过模型中的逻辑或其他计算确定 PID 系数，并将它们馈送到模块。

当您从外部提供增益时，微分增益的时间变化也会被微分。这一结果是由于 PID 增益在模块内部的实现方式所致。有关详细信息，请参阅 **Controller parameters Source** 参数。

#### 依赖关系

要启用此端口，请将 **Controller parameters Source** 设置为 `external`，并将 **Controller** 设置为具有微分作用的控制器类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **N** — 滤波器系数 标量 | 向量

微分滤波器系数，由模块外部的来源提供。外部系数输入非常有用，例如，当您想将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部输入来实现增益调度 PID 控制。在增益调度控制中，您通过模型中的逻辑或其他计算确定 PID 系数，并将它们馈送到模块。

#### 依赖关系

要启用此端口，请将 **Controller parameters Source** 设置为 `external`，并将 **Controller** 设置为具有滤波微分作用的控制器类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **b** — 比例设定点权重 标量 | 向量

比例设定点权重，由模块外部的来源提供。外部输入非常有用，例如，当您想将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部输入来实现增益调度 PID 控制。在增益调度控制中，您通过模型中的逻辑或其他计算确定 PID 系数，并将它们馈送到模块。

#### 依赖关系

要启用此端口，请将 **Controller parameters Source** 设置为 `external`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **c** — 微分设定点权重 标量 | 向量

微分设定点权重，由模块外部的来源提供。外部输入非常有用，例如，当您想将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部输入来实现增益调度 PID 控制。在增益调度控制中，您通过模型中的逻辑或其他计算确定 PID 系数，并将它们馈送到模块。

#### 依赖关系

要启用此端口，请将 **Controller parameters Source** 设置为 `external`，并将 **Controller** 设置为具有微分作用的控制器类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Reset** — 外部复位触发 标量

将积分器和滤波器复位到其初始条件的触发信号。使用 **External reset** 参数指定何种信号触发复位。端口图标指示该参数中指定的触发类型。例如，下图显示了 **External reset** 设置为 `rising` 的连续时间 PID Controller (2DOF) 模块。

当触发发生时，模块将积分器和滤波器复位到由 **Integrator Initial condition** 和 **Filter Initial condition** 参数或 **I0** 和 **D0** 端口指定的初始条件。

**注意**

为符合汽车工业软件可靠性协会 (MISRA™) 软件标准，您的模型必须使用布尔信号来驱动 PID 控制器模块的外部复位端口。

#### 依赖关系

要启用此端口，请将 **External reset** 设置为 `none` 以外的任何值。

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

要启用此端口，请选择 **Limit output** 并将输出饱和 **Source** 设置为 `external`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **lo** — 输出饱和下限 标量 | 向量

模块输出的下限，由模块外部的来源提供。如果比例、积分和微分作用的加权和低于此端口提供的值，则模块输出保持在该值。

#### 依赖关系

要启用此端口，请选择 **Limit output** 并将输出饱和 **Source** 设置为 `external`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **TR** — 跟踪信号 标量 | 向量

控制器输出要跟踪的信号。当信号跟踪激活时，跟踪信号与模块输出之间的差值被反馈到积分器输入。信号跟踪对于在切换两个控制器的系统中实现无扰控制传递非常有用。它还可以用于防止多回路控制系统中的模块积分饱和。有关详细信息，请参阅 **Enable tracking mode** 参数。

#### 依赖关系

要启用此端口，请选择 **Enable tracking mode** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **TDTI** — 离散积分器时间 标量

离散积分器时间，作为标量提供给模块。您可以使用自己的离散时间积分器采样时间值，该值定义了模块在 Simulink 中或外部硬件上运行时的速率。当模块在条件执行子系统内使用时，离散时间积分器时间的值应与外部中断的平均采样率匹配。

换句话说，您可以为以下任何积分器方法指定 `Ts`，使其值与外部中断的平均采样率匹配。在离散时间中，控制器传递函数的微分项为：

D[N1+Nα(z)]，

其中 *α*(*z*) 取决于您使用此参数指定的积分器方法。

`Forward Euler`
:   α(z)=Tsz−1。

`Backward Euler`
:   α(z)=Tszz−1。

`Trapezoidal`
:   α(z)=Ts2z+1z−1。

有关离散时间积分的更多信息，请参阅 Discrete-Time Integrator 模块参考页。有关条件执行子系统的更多信息，请参阅 Conditionally Executed Subsystems Overview。

#### 依赖关系

要启用此端口，请将 **Time Domain** 设置为 `Discrete-time`，并选择 **PID Controller is inside a conditionally executed subsystem** 选项。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **extAW** — 外部抗积分饱和算法 标量 | 向量

*自 R2024b 起*

在此端口指定自定义抗积分饱和算法。该模块提供两种内置抗积分饱和方法，但是，为了退饱和积分器，这些方法依赖于模块分量之和超过指定的模块输出限值。如果您的应用在 PID 控制器模块下游存在饱和或限幅，您可以使用 **extAW** 输入端口来实现自定义抗积分饱和逻辑。该模块还在 **preInt** 输出端口提供积分器之前的信号，您可以使用它来实现自定义算法。

#### 依赖关系

要启用此端口，请在 **Saturation** 选项卡上选择 **Limit output** 并将 **Anti-windup Method** 设置为 `external`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
### 输出

### **Port\_1( u )** — 控制器输出 标量 | 向量

控制器输出，通常基于输入信号、输入信号的积分和输入信号的微分的加权和，由设定点权重以及比例、积分和微分增益参数加权。一阶极点对微分作用进行滤波。控制器信号中存在哪些项取决于您为 **Controller** 参数选择的内容。当前设置的基本控制器传递函数显示在模块参数的 **Compensator formula** 部分以及掩码下方。其他参数会修改模块输出，例如由 **Upper Limit** 和 **Lower Limit** 饱和参数指定的饱和限值。

当任何输入为向量信号时，控制器输出为向量信号。在这种情况下，该模块充当 *N* 个独立的 PID 控制器，其中 *N* 是输入向量中的信号数量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **preInt** — 积分器前信号 标量 | 向量

*自 R2024b 起*

该模块在此端口输出积分器之前的信号。将此信号用作您在 **extAW** 端口提供的自定义抗积分饱和算法的输入。

#### 依赖关系

要启用此端口，请在 **Saturation** 选项卡上选择 **Limit output** 并将 **Anti-windup Method** 设置为 `external`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## 参数
```yaml
parameters:
- name: Controller
  summary: 控制器类型 PID（默认）| PI | PD
  group: ''
  block_parameter: Controller
  type: string, character vector
  values: '"PID", "PI", "PD"'
  default: '"PID"'
- name: Form
  summary: 控制器结构 Parallel（默认）| Ideal
  group: ''
  block_parameter: Controller
  type: string, character vector
  values: '"Parallel", "Ideal"'
  default: '"Parallel"'
- name: Time domain
  summary: 指定连续时间或离散时间控制器 Continuous-time（默认）| Discrete-time
  group: ''
  block_parameter: TimeDomain
  type: string, character vector
  values: '"Continuous-time", "Discrete-time"'
  default: '"Continuous-time"'
- name: PID Controller is inside a conditionally executed subsystem
  summary: 启用离散积分器时间端口 off（默认）| on
  group: ''
  block_parameter: UseExternalTs
  type: string, character vector
  values: '"on", "off"'
  default: '"off"'
- name: Sample time (-1 for inherited)
  summary: 采样之间的离散间隔 –1（默认）| 正标量
  group: ''
  block_parameter: SampleTime
  type: scalar
  values: -1, positive scalar
  default: '-1'
- name: Integrator method
  summary: 离散时间控制器中计算积分的方法 Forward Euler（默认）| Backward Euler | Trapezoidal
  group: ''
  block_parameter: IntegratorMethod
  type: string, character vector
  values: '"Forward Euler", "Backward Euler", "Trapezoidal"'
  default: '"Forward Euler"'
- name: Filter method
  summary: 离散时间控制器中计算微分的方法 Forward Euler（默认）| Backward Euler | Trapezoidal
  group: ''
  block_parameter: FilterMethod
  type: string, character vector
  values: '"Forward Euler", "Backward Euler", "Trapezoidal"'
  default: '"Forward Euler"'
- name: Source
  summary: 控制器增益和滤波器系数的来源 internal（默认）| external
  group: 主要
  block_parameter: ControllerParametersSource
  type: string, character vector
  values: '"internal", "external"'
  default: '"internal"'
- name: Proportional (P)
  summary: 比例增益 1（默认）| 标量 | 向量
  group: 主要
  block_parameter: P
  type: scalar, vector
  default: '1'
- name: Integral (I)
  summary: 积分增益 1（默认）| 标量 | 向量
  group: 主要
  block_parameter: I
  type: scalar, vector
  default: '1'
- name: Integral (I\*Ts)
  summary: 积分增益乘以采样时间 1（默认）| 标量 | 向量
  group: 主要
  block_parameter: I
  type: scalar, vector
  default: '1'
- name: Use I\*Ts
  summary: 使用积分增益乘以采样时间 off（默认）| on
  group: 主要
  block_parameter: UseKiTs
  type: string, character vector
  values: '"on", "off"'
  default: '"on"'
- name: Derivative (D)
  summary: 微分增益 0（默认）| 标量 | 向量
  group: 主要
  block_parameter: D
  type: scalar, vector
  default: '0'
- name: Use externally sourced derivative
  summary: 在模块输入端口指定微分 off（默认）| on
  group: 主要
- name: Use filtered derivative
  summary: 对导数项应用滤波器 on（默认）| off
  group: 主要
  block_parameter: UseFilter
  type: string, character vector
  values: '"on", "off"'
- name: Filter coefficient (N)
  summary: 导数滤波器系数 100（默认）| 标量 | 向量
  group: 主要
  block_parameter: N
  type: scalar, vector
- name: Setpoint weight (b)
  summary: 比例设定点权重 1（默认）| 标量 | 向量
  group: 主要
  block_parameter: b
  type: scalar, vector
- name: Setpoint weight (c)
  summary: 导数设定点权重 1（默认）| 标量 | 向量
  group: 主要
  block_parameter: c
  type: scalar, vector
- name: Select tuning method
  summary: 用于自动整定控制器系数的工具 Transfer Function Based (PID Tuner App)（默认）| Frequency Response Based
  group: 主要
- name: Enable zero-crossing detection
  summary: 在复位时以及进入或离开饱和状态时检测过零 on（默认）| off
  group: 主要
  block_parameter: ZeroCross
  type: string, character vector
  values: '"on", "off"'
- name: Source
  summary: 积分器和导数初始条件的来源 internal（默认）| external
  group: 初始化
  block_parameter: InitialConditionSource
  type: string, character vector
  values: '"internal", "external"'
- name: Integrator
  summary: 积分器初始条件 0（默认）| 标量 | 向量
  group: 初始化
  block_parameter: InitialConditionForIntegrator
  type: scalar, vector
- name: Filter
  summary: 滤波器初始条件 0（默认）| 标量 | 向量
  group: 初始化
  block_parameter: InitialConditionForFilter
  type: scalar, vector
- name: Differentiator
  summary: 未滤波导数的初始条件 0（默认）| 标量 | 向量
  group: 初始化
  block_parameter: DifferentiatorICPrevScaledInput
  type: scalar, vector
- name: Initial condition setting
  summary: 应用初始条件的位置 Auto（默认）| Output
  group: 初始化
  block_parameter: InitialConditionSetting
  type: string, character vector
  values: '"Auto", "Output"'
- name: External reset
  summary: 复位积分器和滤波器值的触发条件 none（默认）| rising | falling | either | level
  group: 初始化
  block_parameter: ExternalReset
  type: string, character vector
  values: '"none", "rising", "falling", "either","level"'
- name: Ignore reset when linearizing
  summary: 强制线性化忽略复位 off（默认）| on
  group: 初始化
  block_parameter: IgnoreLimit
  type: string, character vector
  values: '"off", "on"'
- name: Enable tracking mode
  summary: 激活信号跟踪 off（默认）| on
  group: 初始化
  block_parameter: TrackingMode
  type: string, character vector
  values: '"off", "on"'
- name: Tracking coefficient (Kt)
  summary: 信号跟踪反馈环路的增益 1（默认）| 标量
  group: 初始化
  block_parameter: Kt
  type: scalar
- name: Limit Output
  summary: 将模块输出限制为指定的饱和值 off（默认）| on
  group: 饱和
  block_parameter: LimitOutput
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: Source
  summary: 输出饱和限值的来源 internal（默认）| external
  group: 饱和
  block_parameter: SatLimitsSource
  type: string, character vector
  values: '"internal", "external"'
  default: '"internal"'
- name: Upper limit
  summary: 模块输出的上限饱和限值 Inf（默认）| scalar
  group: 饱和
  block_parameter: UpperSaturationLimit
  type: scalar
  default: Inf
- name: Lower limit
  summary: 模块输出的下限饱和限值 -Inf（默认）| scalar
  group: 饱和
  block_parameter: LowerSaturationLimit
  type: scalar
  default: -Inf
- name: Ignore saturation when linearizing
  summary: 强制线性化忽略输出限值 off（默认）| on
  group: 饱和
  block_parameter: LinearizeAsGain
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: Anti-windup method
  summary: 积分器抗积分饱和方法 none（默认）| back-calculation | clamping | external
  group: 饱和
  block_parameter: AntiWindupMode
  type: string, character vector
  values: '"none", "back-calculation","clamping", "external"'
  default: '"none"'
- name: Back-calculation coefficient (Kb)
  summary: 抗积分饱和反馈环路的增益系数 1（默认）| scalar
  group: 饱和
  block_parameter: Kb
  type: scalar
  default: '1'
- name: Limit Output
  summary: 将积分器输出限制为指定的饱和限值 off（默认）| on
  group: 饱和
  block_parameter: LimitIntegratorOutput
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: Upper limit
  summary: 积分器的上限饱和限值 Inf（默认）| scalar
  group: 饱和
  block_parameter: UpperIntegratorSaturationLimit
  type: scalar
  default: Inf
- name: Lower limit
  summary: 积分器的下限饱和限值 -Inf（默认）| scalar
  group: 饱和
  block_parameter: LowerIntegratorSaturationLimit
  type: scalar
  default: -Inf
- name: Integer rounding mode
  summary: 定点运算的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型
  block_parameter: RndMeth
  values: '''Floor'' (default) | ''Ceiling'' | ''Convergent'' | ''Nearest'' | ''Round'' | ''Simplest'' | ''Zero'''
- name: Saturate on integer overflow
  summary: 溢出操作的方法 off（默认）| on
  group: 数据类型
  block_parameter: SaturateOnIntegerOverflow
  values: '''off'' (default) | ''on'''
- name: 锁定数据类型设置以防止定点工具更改
  summary: 防止定点工具覆盖数据类型 off（默认）| on
  group: 数据类型
  block_parameter: LockScale
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: 状态名称（例如 'position'）
  summary: 连续时间滤波器和积分器状态的名称 ''（默认）| 字符向量
  group: 状态属性
  block_parameter: IntegratorContinuousStateAttributes, FilterContinuousStateAttributes
  type: character vector
  default: ''''''
- name: 状态名称
  summary: 离散时间滤波器和积分器状态的名称 空字符串（默认）| 字符串 | 字符向量
  group: 状态属性
  block_parameter: IntegratorStateIdentifier, FilterStateIdentifier
  type: string, character vector
  default: '""'
- name: 状态名称必须解析为 Simulink 信号对象
  summary: 要求状态名称解析为信号对象 off（默认）| on
  group: 状态属性
  block_parameter: IntegratorStateMustResolveToSignalObject, FilterStateMustResolveToSignalObject
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
```

### **Controller** — 控制器类型 `PID`（默认）| `PI` | `PD`

指定控制器中包含比例、积分和微分项中的哪些。

`PID`
:   比例、积分和微分作用。

`PI`
:   仅比例和积分作用。

`PD`
:   仅比例和微分作用。

**提示**

当前设置的控制器输出显示在模块参数的 **Compensator formula** 部分以及掩码下方。

#### 编程用法

|  |
| --- |
| **模块参数：** `Controller` |
| **类型：** string, character vector |
| **值：** `"PID"`, `"PI"`, `"PD"` |
| **默认值：** `"PID"` |

### **Form** — 控制器结构 `Parallel`（默认）| `Ideal`

指定控制器结构是并联还是理想形式。

`Parallel`
:   比例、积分和微分增益 **P**、**I** 和 **D** 独立作用。例如，对于并联形式的连续时间 2-DOF PID 控制器，控制器输出 *u* 为：

    u=P(br−y)+I1s(r−y)+DN1+N1s(cr−y)，

    其中 *r* 是参考信号，*y* 是测量的被控对象输出信号，*b* 和 *c* 是设定点权重。

    对于并联形式的离散时间 2-DOF 控制器，控制器输出为：

    u=P(br−y)+Iα(z)(r−y)+DN1+Nβ(z)(cr−y)，

    其中 **Integrator method** 和 **Filter method** 参数分别决定 *α*(*z*) 和 *β*(*z*)。

`Ideal`
:   比例增益 **P** 作用于所有作用之和。例如，对于理想形式的连续时间 2-DOF PID 控制器，控制器输出为：

    u=P[(br−y)+I1s(r−y)+DN1+N1s(cr−y)]。

    对于理想形式的离散时间 2-DOF PID 控制器，传递函数为：

    u=P[(br−y)+Iα(z)(r−y)+DN1+Nβ(z)(cr−y)]，

    其中 **Integrator method** 和 **Filter method** 参数分别决定 *α*(*z*) 和 *β*(*z*)。

    **提示**

    当前设置的控制器输出显示在模块参数的 **Compensator formula** 部分以及掩码下方。

#### 编程用法

|  |
| --- |
| **模块参数：** `Controller` |
| **类型：** string, character vector |
| **值：** `"Parallel"`, `"Ideal"` |
| **默认值：** `"Parallel"` |

### **Time domain** — 指定连续时间或离散时间控制器 `Continuous-time`（默认）| `Discrete-time`

当您选择 `Discrete-time` 时，建议为模块指定显式采样时间。请参阅 **Sample time (-1 for inherited)** 参数。选择 `Discrete-time` 还会启用 **Integrator method** 和 **Filter method** 参数。

当 PID Controller 模块位于具有同步状态控制的模型中时（请参阅 State Control (HDL Coder) 模块），您不能选择 `Continuous-time`。

**注意**

PID Controller (2DOF) 和 Discrete PID Controller (2DOF) 模块除该参数的默认值外完全相同。

#### 编程用法

|  |
| --- |
| **模块参数：** `TimeDomain` |
| **类型：** string, character vector |
| **值：** `"Continuous-time"`, `"Discrete-time"` |
| **默认值：** `"Continuous-time"` |

### **PID Controller is inside a conditionally executed subsystem** — 启用离散积分器时间端口 `off`（默认）| `on`

对于离散时间 PID 控制器，启用离散时间积分器端口以使用您自己的离散时间积分器采样时间值。为确保正确积分，请使用 `TDTI` 端口提供 Δt 的标量值以实现精确的离散时间积分。

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

通过输入正标量值（如 0.1）来指定采样时间。默认离散采样时间 –1 表示模块从上游模块继承其采样时间。但是，建议您显式设置控制器采样时间，尤其是在您预期上游模块的采样时间会发生变化时。控制器系数 P、I、D 和 N 的效果取决于采样时间。因此，对于给定的一组系数值，更改采样时间会改变控制器的性能。

有关详细信息，请参阅 Specify Sample Time。

要实现连续时间控制器，请将 **Time domain** 设置为 `Continuous-time`。

**提示**

如果您希望模块以外部指定的或可变的采样时间运行，请将此参数设置为 –1，并将模块放入 Triggered Subsystem 中。然后，在所需的采样时间触发子系统。

#### 依赖关系

要启用此参数，请将 **Time domain** 设置为 `Discrete-time`。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** scalar |
| **值：** `-1`, positive scalar |
| **默认值：** `-1` |

### **Integrator method** — 离散时间控制器中计算积分的方法 `Forward Euler`（默认）| `Backward Euler` | `Trapezoidal`

在离散时间中，控制器传递函数的积分项为 *Ia*(*z*)，其中 *a*(*z*) 取决于您使用此参数指定的积分器方法。

`Forward Euler`
:   前向矩形（左手）近似，

    α(z)=Tsz−1。

    此方法最适合小采样时间，即奈奎斯特极限相对于控制器带宽较大的情况。对于较大的采样时间，`Forward Euler` 方法可能导致不稳定，即使离散化一个连续时间稳定的系统也是如此。

`Backward Euler`
:   后向矩形（右手）近似，

    α(z)=Tszz−1。

    `Backward Euler` 方法的一个优点是，使用此方法离散化稳定的连续时间系统总能得到稳定的离散时间结果。

`Trapezoidal`
:   双线性近似，

    α(z)=Ts2z+1z−1。

    `Trapezoidal` 方法的一个优点是，使用此方法离散化稳定的连续时间系统总能得到稳定的离散时间结果。在所有可用的积分方法中，`Trapezoidal` 方法使离散化系统的频域特性与相应的连续时间系统之间的匹配最为接近。

    **提示**

    当前设置的控制器公式显示在模块参数的 **Compensator formula** 部分以及掩码下方。

有关离散时间积分的详细信息，请参阅 Discrete-Time Integrator 模块参考页。

#### 依赖关系

要启用此参数，请将 **Time Domain** 设置为 `Discrete-time`，并将 **Controller** 设置为具有积分作用的控制器类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `IntegratorMethod` |
| **类型：** string, character vector |
| **值：** `"Forward Euler"`, `"Backward Euler"`, `"Trapezoidal"` |
| **默认值：** `"Forward Euler"` |

### **Filter method** — 离散时间控制器中计算微分的方法 `Forward Euler`（默认）| `Backward Euler` | `Trapezoidal`

在离散时间中，控制器传递函数的微分项为：

D[N1+Nα(z)]，

其中 *α*(*z*) 取决于您使用此参数指定的滤波器方法。

`Forward Euler`
:   前向矩形（左手）近似，

    α(z)=Tsz−1。

    此方法最适合小采样时间，即奈奎斯特极限相对于控制器带宽较大的情况。对于较大的采样时间，`Forward Euler` 方法可能导致不稳定，即使离散化一个连续时间稳定的系统也是如此。

`Backward Euler`
:   后向矩形（右手）近似，

    α(z)=Tszz−1。

    `Backward Euler` 方法的一个优点是，使用此方法离散化稳定的连续时间系统总能得到稳定的离散时间结果。

`Trapezoidal`
:   双线性近似，

    α(z)=Ts2z+1z−1。

    `Trapezoidal` 方法的一个优点是，使用此方法离散化稳定的连续时间系统总能得到稳定的离散时间结果。在所有可用的积分方法中，`Trapezoidal` 方法使离散化系统的频域特性与相应的连续时间系统之间的匹配最为接近。

    **提示**

    当前设置的控制器公式显示在模块参数的 **Compensator formula** 部分以及掩码下方。

有关离散时间积分的详细信息，请参阅 Discrete-Time Integrator 模块参考页。

#### 依赖关系

要启用此参数，请将 **Time Domain** 设置为 `Discrete-time`，并启用 **Use filtered derivative**。

#### 编程用法

|  |
| --- |
| **模块参数：** `FilterMethod` |
| **类型：** string, character vector |
| **值：** `"Forward Euler"`, `"Backward Euler"`, `"Trapezoidal"` |
| **默认值：** `"Forward Euler"` |

### 主要

### **Source** — 控制器增益和滤波器系数的来源 internal（默认）| external

`internal`
:   使用模块参数 **P**、**I**、**D**、**N**、**b** 和 **c** 分别指定控制器增益、滤波器系数和设定点权重。

`external`
:   使用模块输入从外部指定 PID 增益、滤波器系数和设定点权重。对于当前控制器类型所需的每个参数，模块上会出现一个额外的输入端口。

启用参数的外部输入允许您在模块外部计算其值，并将其作为信号输入提供给模块。

外部输入非常有用，例如，当您想将不同的 PID 参数化映射到模块的 PID 增益时。您还可以使用外部增益输入来实现增益调度 PID 控制。在增益调度控制中，您通过模型中的逻辑或其他计算确定 PID 增益，并将它们馈送到模块。

当您从外部提供增益时，积分增益值和微分增益值的时间变化分别被积分和微分。微分设定点权重 *c* 也被微分。出现此结果是因为在连续时间和离散时间中，增益都在积分或微分之前应用于信号。例如，对于具有外部输入的连续时间 PID 控制器，积分器项的实现如下所示。

在模块内部，输入信号 *u* 在积分之前乘以外部提供的积分器增益 *I*。此实现产生：

ui=∫(r−y)I dt。

因此，积分器增益包含在积分中。类似地，在模块的微分项中，乘以微分增益在微分之前，这导致微分增益 *D* 和微分设定点权重 *c* 被微分。

#### 编程用法

|  |
| --- |
| **模块参数：** `ControllerParametersSource` |
| **类型：** string, character vector |
| **值：** `"internal"`, `"external"` |
| **默认值：** `"internal"` |

### **Proportional (P)** — 比例增益 1（默认）| 标量 | 向量

为比例增益指定一个有限的实增益值。当 **Controller form** 为：

- `Parallel` — 比例作用独立于积分和微分作用。例如，对于并联形式的连续时间 2-DOF PID 控制器，控制器输出 *u* 为：

  u=P(br−y)+I1s(r−y)+DN1+N1s(cr−y)，

  其中 *r* 是参考信号，*y* 是测量的被控对象输出信号，*b* 和 *c* 是设定点权重。

  对于并联形式的离散时间 2-DOF 控制器，控制器输出为：

  u=P(br−y)+Iα(z)(r−y)+DN1+Nβ(z)(cr−y)，

  其中 **Integrator method** 和 **Filter method** 参数分别决定 *α*(*z*) 和 *β*(*z*)。
- `Ideal` — 比例增益乘以积分项和微分项。例如，对于理想形式的连续时间 2-DOF PID 控制器，控制器输出为：

  u=P[(br−y)+I1s(r−y)+DN1+N1s(cr−y)]。

  对于理想形式的离散时间 2-DOF PID 控制器，传递函数为：

  u=P[(br−y)+Iα(z)(r−y)+DN1+Nβ(z)(cr−y)]，

  其中 **Integrator method** 和 **Filter method** 参数分别决定 *α*(*z*) 和 *β*(*z*)。

#### 依赖关系

要启用此参数，请将控制器参数 **Source** 设置为 `internal`。

#### 编程用法

|  |
| --- |
| **模块参数：** `P` |
| **类型：** scalar, vector |
| **默认值：** 1 |

**可调：** 是

### **Integral (I)** — 积分增益 1（默认）| 标量 | 向量

为积分增益指定一个有限的实增益值。

**可调：** 是

#### 依赖关系

要启用此参数，请在 **Main** 选项卡中将控制器参数 **Source** 设置为 `internal`，并将 **Controller** 设置为具有积分作用的类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `I` |
| **类型：** scalar, vector |
| **默认值：** 1 |

### **Integral (I\*Ts)** — 积分增益乘以采样时间 1（默认）| 标量 | 向量

对于离散时间控制器，为积分增益乘以采样时间指定一个有限的实增益值。

**注意**

PID 整定工具（如 PID Tuner 应用和 Closed-Loop PID Autotuner 模块）整定增益 **I** 而非 **I\*Ts**。因此，在将此参数写入之前，请将从整定工具获得的积分增益值乘以采样时间。

当您使用 **I\*Ts** 而非 **I** 时，模块执行积分所需的计算更少。这改善了生成代码的执行时间。

对于连续时间控制器，请禁用 **Use I\*Ts** 并使用 **I** 参数。

**可调：** 否

#### 依赖关系

要启用此参数，请在 **Main** 选项卡中将控制器参数 **Source** 设置为 `internal`，将 **Controller** 设置为具有积分作用的类型，并启用 **Use I\*Ts** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `I` |
| **类型：** scalar, vector |
| **默认值：** 1 |

### **Use I\*Ts** — 使用积分增益乘以采样时间 `off`（默认）| `on`

对于具有积分作用的离散时间控制器，模块将积分增益作为输入，并在执行积分时在内部将其乘以采样时间。如果您启用此参数，则显式指定积分增益乘以采样时间作为输入（**I\*Ts**）来代替积分增益（**I**）。这样做减少了内部计算次数，在您希望改善生成代码的执行时间时非常有用。

如果您已启用信号跟踪或抗积分饱和模式反算，并且启用了 **I\*Ts**，则还必须将跟踪增益参数 **Kt** 设置为 `Kt*Ts`，将反算系数 **Kb** 设置为 `Kb*Ts`。

对于连续时间控制器，启用此参数对积分增益没有影响。

#### 依赖关系

要启用此参数，请将 **Controller** 设置为具有积分作用的控制器类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `UseKiTs` |
| **类型：** string, character vector |
| **值：** `"on"`, `"off"` |
| **默认值：** `"on"` |

### **Derivative (D)** — 微分增益 0（默认）| 标量 | 向量

为微分增益指定一个有限的实增益值。

**可调：** 是

#### 依赖关系

要启用此参数，请在 **Main** 选项卡中将控制器参数 **Source** 设置为 `internal`，并将 **Controller** 设置为 `PID` 或 `PD`。

#### 编程用法

|  |
| --- |
| **模块参数：** `D` |
| **类型：** scalar, vector |
| **默认值：** 0 |

### **Use externally sourced derivative** — 在模块输入端口指定微分 `off`（默认）| `on`

*自 R2024a 起*

选择此选项可直接将被控对象信号 *y* 的微分作为输入 **ydot** 指定给模块。当您的模型中已有微分信号并希望跳过模块内部的微分计算时，这非常有用。

#### 依赖关系

要启用此选项，请选择具有微分作用的控制器类型。

### **Use filtered derivative** — 对导数项应用滤波器 `on`（默认）| `off`

仅适用于离散时间 PID 控制器，清除此选项可将滤波导数替换为未滤波的离散时间微分器。这样做时，控制器输出的导数项变为：

Dz−1zTs(cr−y).

对于连续时间 PID 控制器，导数项始终经过滤波。

#### 依赖关系

要启用此参数，请将 **Time domain** 设置为 `Discrete-time`，并将 **Controller** 设置为具有导数项的类型。

#### 编程使用

|  |
| --- |
| **模块参数：** `UseFilter` |
| **类型：** string, character vector |
| **值：** `"on"`, `"off"` |
| **默认：** `"on"` |

### **Filter coefficient (N)** — 导数滤波器系数 100（默认）| 标量 | 向量

为滤波器系数指定一个有限实增益值。滤波器系数决定模块微分作用中滤波器的极点位置。滤波器极点的位置取决于 **Time domain** 参数。

- 当 **Time domain** 为 `Continuous-time` 时，极点位置为 `s = -N`。
- 当 **Time domain** 为 `Discrete-time` 时，极点位置取决于 **Filter method** 参数。

  | 滤波方法 | 滤波器极点位置 |
  | --- | --- |
  | `Forward Euler` | zpole=1−NTs |
  | `Backward Euler` | zpole=11+NTs |
  | `Trapezoidal` | zpole=1−NTs/21+NTs/2 |

该模块不支持 `N = Inf`（理想未滤波导数）。当 **Time domain** 为 `Discrete-time` 时，您可以清除 **Use filtered derivative** 以移除导数滤波器。

#### 依赖关系

要启用此参数，请在 **Main** 选项卡中，将控制器参数 **Source** 设置为 `internal`，并将 **Controller** 设置为 `PID` 或 `PD`。

#### 编程使用

|  |
| --- |
| **模块参数：** `N` |
| **类型：** scalar, vector |
| **默认：** 100 |

**可调：** 是

### **Setpoint weight (b)** — 比例设定点权重 1（默认）| 标量 | 向量

控制器比例项的设定点权重。2-DOF 控制器输出的比例项为 *P*(*br*–*y*)，其中 *r* 是参考信号，*y* 是测量的被控对象输出。将 *b* 设置为 0 可消除对参考信号的比例作用，这可以减少系统对设定点阶跃变化的响应超调。改变 *b* 和 *c* 的相对值会改变扰动抑制与设定点跟踪之间的平衡。

**可调：** 是

#### 依赖关系

要启用此参数，请在 **Main** 选项卡中，将控制器参数 **Source** 设置为 `internal`。

#### 编程使用

|  |
| --- |
| **模块参数：** `b` |
| **类型：** scalar, vector |
| **默认：** 1 |

### **Setpoint weight (c)** — 导数设定点权重 1（默认）| 标量 | 向量

控制器导数项的设定点权重。2-DOF 控制器的导数项作用于 *cr*–*y*，其中 *r* 是参考信号，*y* 是测量的被控对象输出。因此，将 *c* 设置为 0 可消除对参考信号的导数作用，这可以减少对设定点阶跃变化的瞬态响应。将 *c* 设置为 0 可以产生一个控制器，既能实现有效的扰动抑制，又能实现平滑的设定点跟踪，而不会产生过大的瞬态响应。改变 *b* 和 *c* 的相对值会改变扰动抑制与设定点跟踪之间的平衡。

**可调：** 是

#### 依赖关系

要启用此参数，请在 **Main** 选项卡中，将控制器参数 **Source** 设置为 `internal`，并将 **Controller** 设置为具有导数作用的类型。

#### 编程使用

|  |
| --- |
| **模块参数：** `c` |
| **类型：** scalar, vector |
| **默认：** 1 |

### **Select tuning method** — 用于自动整定控制器系数的工具 `Transfer Function Based (PID Tuner App)`（默认）| `Frequency Response Based`

如果您拥有 Simulink Control Design 软件，当 PID 系数内置于模块中时，您可以自动整定这些系数。为此，请使用此参数选择整定工具，然后点击 **Tune**。

`Transfer Function Based (PID Tuner App)`
:   使用 PID Tuner，它允许您在检查相关系统响应以验证性能的同时，交互式地整定 PID 系数。PID Tuner 可以整定所有系数 **P**、**I**、**D** 和 **N**，以及设定点系数 **b** 和 **c**。默认情况下，PID Tuner 使用被控对象模型的线性化模型。对于无法线性化的模型，您可以针对从仿真或测量响应数据估计的被控对象模型来整定 PID 系数。有关详细信息，请参阅 Design Two-Degree-of-Freedom PID Controllers (Simulink Control Design)。

`Frequency Response Based`
:   使用 Frequency Response Based PID Tuner，它基于通过仿真获得的频率响应估计数据来整定 PID 控制器系数。这种整定方法特别适用于无法线性化或线性化为零的被控对象。Frequency Response Based PID Tuner 整定系数 **P**、**I**、**D** 和 **N**，但不整定设定点系数 **b** 和 **c**。有关详细信息，请参阅 Design PID Controller from Plant Frequency-Response Data (Simulink Control Design)。

这两种整定方法都假设单回路控制配置。Simulink Control Design 软件包含适用于更复杂配置的其他整定方法。有关整定 PID Controller 模块的其他方式的信息，请参阅 Choose a Control Design Approach (Simulink Control Design)。

#### 依赖关系

要启用此参数，请在 **Main** 选项卡中，将控制器参数 **Source** 设置为 `internal`。

### **Enable zero-crossing detection** — 在复位时以及进入或离开饱和状态时检测过零 `on`（默认）| `off`

过零检测可以准确定位信号不连续点，而无需使用可能导致仿真时间过长的过小时间步长。如果您在 PID Controller 模块中选择 **Limit output** 或激活 **External reset**，激活过零检测可以减少仿真中的计算时间。选择此参数将在以下情况下激活过零检测：

- 在初始状态复位时
- 进入上限或下限饱和状态时
- 离开上限或下限饱和状态时

有关过零检测的详细信息，请参阅 Zero-Crossing Detection。

#### 编程使用

|  |
| --- |
| **模块参数：** `ZeroCross` |
| **类型：** string, character vector |
| **值：** `"on"`, `"off"` |
| **默认：** `"on"` |

### 初始化

### **Source** — 积分器和导数初始条件的来源 `internal`（默认）| `external`

Simulink 使用初始条件在仿真开始时或在指定的触发事件时初始化积分器和导数滤波器（或未滤波导数）的输出。（请参阅 **External reset** 参数。）这些初始条件决定模块的初始输出。使用此参数选择如何向模块提供初始条件值。

`internal`
:   使用 **Integrator Initial condition** 和 **Filter Initial condition** 参数指定初始条件。如果未选择 **Use filtered derivative**，请使用 **Differentiator** 参数为未滤波微分器指定初始条件，而不是滤波器初始条件。

`external`
:   使用模块输入从外部指定初始条件。模块上会出现额外的输入端口 **Io** 和 **Do**。如果未选择 **Use filtered derivative**，请在 **Do** 处为未滤波微分器提供初始条件，而不是滤波器初始条件。

#### 编程使用

|  |
| --- |
| **模块参数：** `InitialConditionSource` |
| **类型：** string, character vector |
| **值：** `"internal"`, `"external"` |
| **默认：** `"internal"` |

### **Integrator** — 积分器初始条件 0（默认）| 标量 | 向量

Simulink 使用积分器初始条件在仿真开始时或在指定的触发事件时初始化积分器（请参阅 **External reset**）。积分器初始条件和滤波器初始条件决定 PID Controller 模块的初始输出。

积分器初始条件不能为 `NaN` 或 `Inf`。

#### 依赖关系

要使用此参数，请在 **Initialization** 选项卡中，将 **Source** 设置为 `internal`，并将 **Controller** 设置为具有积分作用的类型。

#### 编程使用

|  |
| --- |
| **模块参数：** `InitialConditionForIntegrator` |
| **类型：** scalar, vector |
| **默认：** 0 |

### **Filter** — 滤波器初始条件 0（默认）| 标量 | 向量

Simulink 使用滤波器初始条件在仿真开始时或在指定的触发事件时初始化导数滤波器（请参阅 **External reset**）。积分器初始条件和滤波器初始条件决定 PID Controller 模块的初始输出。

滤波器初始条件不能为 `NaN` 或 `Inf`。

#### 依赖关系

要使用此参数，请在 **Initialization** 选项卡中，将 **Source** 设置为 `internal`，并使用具有导数滤波器的控制器。

#### 编程使用

|  |
| --- |
| **模块参数：** `InitialConditionForFilter` |
| **类型：** scalar, vector |
| **默认：** 0 |

### **Differentiator** — 未滤波导数的初始条件 0（默认）| 标量 | 向量

当您使用未滤波导数时，Simulink 使用此参数在仿真开始时或在指定的触发事件时初始化微分器（请参阅 **External reset**）。积分器初始条件和导数初始条件决定 PID Controller 模块的初始输出。

导数初始条件不能为 `NaN` 或 `Inf`。

#### 依赖关系

要使用此参数，请将 **Time domain** 设置为 `Discrete-time`，清除 **Use filtered derivative** 复选框，并在 **Initialization** 选项卡中，将 **Source** 设置为 `internal`。

#### 编程使用

|  |
| --- |
| **模块参数：** `DifferentiatorICPrevScaledInput` |
| **类型：** scalar, vector |
| **默认：** 0 |

### **Initial condition setting** — 应用初始条件的位置 `Auto`（默认）| `Output`

使用此参数指定是将 **Integrator Initial condition** 和 **Filter Initial condition** 参数应用于相应的模块状态还是输出。您只能在命令行更改此参数，使用 `set_param` 设置模块的 `InitialConditionSetting` 参数。

`Auto`
:   除模块位于触发子系统或函数调用子系统中且启用了简化初始化模式外，在所有情况下使用此选项。

`Output`
:   当模块位于触发子系统或函数调用子系统中且启用了简化初始化模式时，使用此选项。

有关 **Initial condition setting** 参数的详细信息，请参阅 Discrete-Time Integrator 模块。

此参数只能通过编程使用访问。

#### 编程使用

|  |
| --- |
| **模块参数：** `InitialConditionSetting` |
| **类型：** string, character vector |
| **值：** `"Auto"`, `"Output"` |
| **默认：** `"Auto"` |

### **External reset** — 复位积分器和滤波器值的触发条件 `none`（默认）| `rising` | `falling` | `either` | `level`

指定使模块将积分器和滤波器复位到初始条件的触发条件。（如果未选择 **Use filtered derivative**，该触发条件会将积分器和微分器复位到初始条件。）选择除 `none` 以外的任何选项都会在模块上启用用于外部复位信号的 **Reset** 端口。

`none`
:   积分器和滤波器（或微分器）输出在仿真开始时设置为初始条件，并且在仿真期间不复位。

`rising`
:   当复位信号出现上升沿时复位输出。

`falling`
:   当复位信号出现下降沿时复位输出。

`either`
:   当复位信号出现上升沿或下降沿时复位输出。

`level`
:   当复位信号满足以下任一条件时复位输出：

    - 在当前时间步为非零
    - 从前一时间步的非零变为当前时间步的零

    此选项在复位信号非零期间将输出保持在初始条件。

#### 依赖关系

要启用此参数，请将 **Controller** 设置为具有导数或积分作用的类型。

#### 编程使用

|  |
| --- |
| **模块参数：** `ExternalReset` |
| **类型：** string, character vector |
| **值：** `"none"`, `"rising"`, `"falling"`, `"either"`,`"level"` |
| **默认：** `"none"` |

### **Ignore reset when linearizing** — 强制线性化忽略复位 `off`（默认）| `on`

选择此项可强制 Simulink 和 Simulink Control Design 线性化命令忽略 **External reset** 参数中指定的任何复位机制。忽略复位状态允许您围绕工作点对模型进行线性化，即使该工作点会导致模块复位。

#### 编程使用

|  |
| --- |
| **模块参数：** `IgnoreLimit` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认：** `"off"` |

### **Enable tracking mode** — 激活信号跟踪 `off`（默认）| `on`

信号跟踪允许模块输出跟随您在 **TR** 端口提供的跟踪信号。当信号跟踪激活时，跟踪信号与模块输出之间的差值以增益 `Kt` 反馈到积分器输入，该增益由 **Tracking gain (Kt)** 参数指定。信号跟踪有多种应用，包括无扰控制切换和避免多回路控制结构中的积分饱和。

#### 无扰控制切换

使用信号跟踪可在两个控制器之间切换的系统中实现无扰控制切换。假设您要在 PID 控制器和另一个控制器之间切换控制。为此，将控制器输出连接到 **TR** 输入，如下图所示。

有关详细信息，请参阅 Bumpless Control Transfer with a Two-Degree-of-Freedom PID Controller。

#### 多回路控制

使用信号跟踪可防止多回路控制方法中的模块积分饱和。有关使用 1DOF PID 控制器说明此方法的示例，请参阅 Prevent Block Windup in Multiloop Control。

#### 依赖关系

要启用此参数，请将 **Controller** 设置为具有积分作用的类型。

#### 编程使用

|  |
| --- |
| **模块参数：** `TrackingMode` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认：** `"off"` |

### **Tracking coefficient (Kt)** — 信号跟踪反馈环路的增益 1（默认）| 标量

当您选择 **Enable tracking mode** 时，信号 **TR** 与模块输出之间的差值以增益 `Kt` 反馈到积分器输入。使用此参数指定该反馈环路中的增益。

对于离散时间控制器，如果您选择模块的 **Use I\*Ts** 参数，则将此参数设置为值 `Kt*Ts`，其中 `Kt` 是所需增益，`Ts` 是采样时间。

#### 依赖关系

要启用此参数，请选择 **Enable tracking mode**。

#### 编程使用

|  |
| --- |
| **模块参数：** `Kt` |
| **类型：** scalar |
| **默认：** 1 |

### 饱和

#### 输出饱和

### **Limit Output** — 将模块输出限制为指定的饱和值 `off`（默认）| `on`

激活此选项会限制模块输出，因此您无需在控制器之后单独使用 Saturation 模块。它还允许您激活模块内置的抗积分饱和机制（请参阅 **Anti-windup method** 参数）。使用 **Lower limit** 和 **Upper limit** 参数指定输出饱和限值。您也可以将饱和限值作为模块输入端口从外部指定。

#### 编程使用

|  |
| --- |
| **模块参数**：`LimitOutput` |
| **类型**：string, character vector |
| **值**：`"off"`, `"on"` |
| **默认值**：`"off"` |

### **Source** — 输出饱和限值的来源 internal（默认）| external

使用此参数指定如何提供模块输出的上限和下限饱和限值。

`internal`
:   使用 **Upper limit** 和 **Lower limit** 参数指定输出饱和限值。

`external`
:   使用模块输入端口从外部指定输出饱和限值。模块上会出现额外的输入端口 **up** 和 **lo**。您可以使用这些输入端口来实现由 Simulink 模型中的逻辑或其他计算确定并传递给模块的输出上限和下限饱和限值。

#### 编程使用

|  |
| --- |
| **模块参数**：`SatLimitsSource` |
| **类型**：string, character vector |
| **值**：`"internal"`, `"external"` |
| **默认值**：`"internal"` |

### **Upper limit** — 模块输出的上限饱和限值 `Inf`（默认）| scalar

指定模块输出的上限。当比例、积分和微分作用的加权和超过该值时，模块输出保持在 **Upper saturation limit**。

#### 依赖关系

要启用此参数，请选中 **Limit output**。

#### 编程使用

|  |
| --- |
| **模块参数**：`UpperSaturationLimit` |
| **类型**：scalar |
| **默认值**：`Inf` |

### **Lower limit** — 模块输出的下限饱和限值 `-Inf`（默认）| scalar

指定模块输出的下限。当比例、积分和微分作用的加权和低于该值时，模块输出保持在 **Lower saturation limit**。

#### 依赖关系

要启用此参数，请选中 **Limit output**。

#### 编程使用

|  |
| --- |
| **模块参数**：`LowerSaturationLimit` |
| **类型**：scalar |
| **默认值**：`-Inf` |

### **Ignore saturation when linearizing** — 强制线性化忽略输出限值 `off`（默认）| `on`

强制 Simulink 和 Simulink Control Design 线性化命令忽略在 **Upper limit** 和 **Lower limit** 参数中指定的模块输出限值。忽略输出限值允许您围绕工作点对模型进行线性化，即使该工作点导致模块超出输出限值。

#### 依赖关系

要启用此参数，请选中 **Limit output** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`LinearizeAsGain` |
| **类型**：string, character vector |
| **值**：`"off"`, `"on"` |
| **默认值**：`"off"` |

### **Anti-windup method** — 积分器抗积分饱和方法 `none`（默认）| `back-calculation` | `clamping` | `external`

当您选中 **Limit output** 且控制器各分量的加权和超过指定的输出限值时，模块输出保持在指定限值。但是，积分器输出可能继续增长（积分器饱和），增大模块输出与模块各分量之和之间的差异。换句话说，即使输出看起来被饱和限值所限制，模块内部的信号也可能是无界的。如果没有防止积分器饱和的机制，可能会出现两种结果：

- 如果进入积分器的信号符号从不改变，积分器会持续积分直到溢出。溢出值为积分器输出数据类型的最大值或最小值。
- 如果进入积分器的信号在加权和超出输出限值后改变符号，则可能需要很长时间才能解除积分器的饱和状态并使加权和回到模块饱和限值以内。

在任一情况下，控制器性能都可能受到影响。在没有抗积分饱和机制的情况下，为了对抗饱和的影响，可能需要降低控制器的灵敏度（例如，通过减小控制器增益），从而导致控制器响应迟缓。为避免此问题，请使用此参数激活抗积分饱和机制。

`none`
:   不使用抗积分饱和机制。

`back-calculation`
:   当模块输出饱和时，通过将饱和控制信号与未饱和控制信号之间的差值反馈给积分器来解除积分器的饱和状态。下图表示连续时间控制器的反算反馈电路。要查看您的控制器配置的实际反馈电路，请右键单击模块并选择 **Mask** > **Look Under Mask**。

    使用 **Back-calculation coefficient (Kb)** 参数指定抗积分饱和反馈电路的增益。通常设置为 `Kb = I` 即可满足要求，或者对于带微分作用的控制器，设置为 `Kb = sqrt(I*D)`。反算对于具有相对较大死区的被控对象可能是有效的 [1]。

`clamping`
:   钳位有时也称为条件积分。

    当以下两个条件同时满足时，积分停止：

    - 模块各分量之和超过输出限值。
    - 积分器输入和饱和模块输入具有相同的符号。

    当其中任一条件不再满足时，积分恢复。

    钳位对于具有相对较小死区的被控对象可能有用，但对于大死区可能产生较差的瞬态响应 [1]。

`external` *（自 R2024b 起）*
:   内置的抗积分饱和方法依赖于模块各分量之和超过指定的模块输出限值。如果您的应用在 PID 控制器模块下游存在饱和或限幅，您可以使用 **extAW** 输入端口来实现自定义抗积分饱和逻辑。该模块还在 **preInt** 输出端口提供积分器之前的信号，您可以将其用作自定义算法的输入。

#### 依赖关系

要启用此参数，请选中 **Limit output** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`AntiWindupMode` |
| **类型**：string, character vector |
| **值**：`"none"`, `"back-calculation"`,`"clamping"`, `"external"` |
| **默认值**：`"none"` |

### **Back-calculation coefficient (Kb)** — 抗积分饱和反馈环路的增益系数 1（默认）| scalar

`back-calculation` 抗积分饱和方法在模块输出饱和时解除积分器的饱和状态。它通过将饱和控制信号与未饱和控制信号之间的差值反馈给积分器来实现。使用 **Back-calculation coefficient (Kb)** 参数指定抗积分饱和反馈电路的增益。有关详细信息，请参阅 **Anti-windup method** 参数。

对于离散时间控制器，如果您选中模块的 **Use I\*Ts** 参数，则将此参数设置为值 `Kb*Ts`，其中 `Kb` 是所需系数，`Ts` 是采样时间。

#### 依赖关系

要启用此参数，请选中 **Limit output** 参数，并将 **Anti-windup method** 参数设置为 `back-calculation`。

#### 编程使用

|  |
| --- |
| **模块参数**：`Kb` |
| **类型**：scalar |
| **默认值**：1 |

#### Integrator saturation

### **Limit Output** — 将积分器输出限制为指定的饱和限值 `off`（默认）| `on`

启用此参数以将积分器输出限制在指定范围内。当积分器输出达到限值时，积分作用关闭以防止积分饱和。使用 **Lower limit** 和 **Upper limit** 参数指定饱和限值。

#### 依赖关系

要启用此参数，请将 **Controller** 设置为具有积分作用的控制器类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`LimitIntegratorOutput` |
| **类型**：string, character vector |
| **值**：`"off"`, `"on"` |
| **默认值**：`"off"` |

### **Upper limit** — 积分器的上限饱和限值 `Inf`（默认）| scalar

指定积分器输出的上限。当积分器输出将超过此值时，积分器输出保持在该值。

#### 依赖关系

要启用此参数，请在 **Integrator saturation** 下选中 **Limit output**。

#### 编程使用

|  |
| --- |
| **模块参数**：`UpperIntegratorSaturationLimit` |
| **类型**：scalar |
| **默认值**：`Inf` |

### **Lower limit** — 积分器的下限饱和限值 `-Inf`（默认）| scalar

指定积分器输出的下限。当积分器输出将低于此值时，积分器输出保持在该值。

#### 依赖关系

要启用此参数，请在 **Integrator saturation** 下选中 **Limit output**。

#### 编程使用

|  |
| --- |
| **模块参数**：`LowerIntegratorSaturationLimit` |
| **类型**：scalar |
| **默认值**：`-Inf` |

### 数据类型

此选项卡中的参数主要用于使用 Fixed-Point Designer™ 进行定点代码生成。它们定义了在生成代码时与模块相关的数值量的存储和处理方式。

如果您需要为定点代码生成配置数据类型，请点击 **Open Fixed-Point Tool** 并使用该工具配置选项卡中的其余参数。有关使用 Fixed-Point Tool 的信息，请参阅 Autoscaling Data Objects Using the Fixed-Point Tool (Fixed-Point Designer)。

使用 Fixed-Point Tool 后，如有必要，您可以使用此选项卡中的参数对定点数据类型设置进行调整。对于与模块相关的每个量，您可以指定：

- 浮点或定点数据类型，包括数据类型是否从模块中的上游值继承。
- 该量的最小值和最大值，这些值决定了该量在定点表示中如何缩放。

如需帮助选择适当的值，请点击 以打开相应量的 Data Type Assistant。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

Data Types 选项卡中列出的具体量因您配置 PID controller 模块的方式而异。通常，您可以为以下类型的量配置数据类型：

- Product output — 存储模块掩码下执行的乘法结果。例如，**P product output** 存储将模块输入与比例增益 **P** 相乘的增益模块的输出。
- Parameter — 存储数值模块参数的值，例如 **P**、**I** 或 **D**。
- Block output — 存储位于 PID controller 模块掩码下的模块的输出。例如，使用 **Integrator output** 指定名为 Integrator 的模块输出的数据类型。此模块位于 Integrator 子系统中的掩码下，计算控制器作用的积分项。
- Accumulator — 存储与求和模块相关的值。例如，**SumI2 Accumulator** 设置与求和模块 SumI2 相关的累加器的数据类型。此模块位于 Anti-Windup 子系统的 Back Calculation 子系统中的掩码下。

通常，您可以通过查看 PID Controller 模块掩码下并检查其子系统来找到与任何列出的参数相关的模块。您也可以使用 Model Explorer 在掩码下搜索列出的参数名称，例如 `SumI2`。（请参阅 Model Explorer。）

**匹配输入和内部数据类型**

默认情况下，模块中的所有数据类型都设置为 `Inherit: Inherit via internal rule`。使用此设置，Simulink 会选择数据类型以平衡数值精度、性能和生成的代码大小，同时考虑嵌入式目标硬件的属性。

在某些条件下，模块内的数据类型之间可能发生不兼容。例如，在连续时间中，掩码下的 Integrator 模块只能接受 `double` 类型的信号。如果模块输入信号是无法转换为 `double` 的类型，例如 `uint16`，则类型继承的内部规则在生成代码时会产生错误。

为避免此类错误，您可以使用 Data Types 设置强制进行数据类型转换。例如，您可以显式将 **P product output**、**I product output** 和 **D product output** 设置为 `double`，确保到达连续时间积分器的信号为 `double` 类型。

通常，不建议在代码生成应用中使用连续时间的模块。但是，如果您将某些值显式设置为与模块内下游信号约束不兼容的数据类型，则在离散时间中也可能发生类似的数据类型错误。在这种情况下，请使用 Data Types 设置确保所有数据类型在内部兼容。

#### Fixed-Point Operational Parameters

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RndMeth` |
| **值**：| `'Floor'` (default) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

指定溢出是饱和还是回绕。

- `on` — 溢出饱和到数据类型可以表示的最小值或最大值。
- `off` — 溢出回绕到数据类型可以表示的适当值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出饱和在 127。类似地，模块输出饱和在最小输出值 -128。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 -126。

#### 提示

- 当您的模型可能存在溢出并且您希望在生成的代码中显式添加饱和保护时，请考虑选中此参数。
- 当您希望优化生成代码的效率时，请考虑清除此参数。清除此参数还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors。
- 当您选中此参数时，饱和适用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **值**：| `'off'` (default) | `'on'` |

### **锁定数据类型设置以防止定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在此模块上指定的数据类型。有关详细信息，请参阅锁定输出数据类型设置 (Fixed-Point Designer)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

### 状态属性

此选项卡中的参数主要用于代码生成。

### **状态名称（例如 'position'）** — 连续时间滤波器和积分器状态的名称 `''`（默认）| 字符向量

为连续时间 PID 控制器的积分器或滤波器相关状态分配唯一名称。（有关离散时间 PID 控制器中状态名称的信息，请参阅 **状态名称** 参数。）状态名称用于，例如：

- 生成代码中的对应变量
- 仿真期间记录状态时作为存储名称的一部分
- 通过线性化模块获得的线性模型中的对应状态

有效的状态名称以字母或下划线字符开头，后跟字母数字或下划线字符。

#### 依赖关系

要启用此参数，请将 **Time domain** 设置为 `Continuous-time`。

#### 编程使用

|  |
| --- |
| **Parameter:**  `IntegratorContinuousStateAttributes`, `FilterContinuousStateAttributes` |
| **类型**：character vector |
| **默认值**：`''` |

### **状态名称** — 离散时间滤波器和积分器状态的名称 空字符串（默认）| 字符串 | 字符向量

为离散时间 PID 控制器的积分器或滤波器相关状态分配唯一名称。（有关连续时间 PID 控制器中状态名称的信息，请参阅 **状态名称（例如 'position'）** 参数。）

有效的状态名称以字母或下划线字符开头，后跟字母数字或下划线字符。状态名称用于，例如：

- 生成代码中的对应变量
- 仿真期间记录状态时作为存储名称的一部分
- 通过线性化模块获得的线性模型中的对应状态

有关代码生成中状态名称使用的详细信息，请参阅 C Data Code Interface Configuration for Model Interface Elements (Simulink Coder)。

#### 依赖关系

要启用此参数，请将 **Time domain** 设置为 `Discrete-time`。

#### 编程使用

|  |
| --- |
| **Parameter:**  `IntegratorStateIdentifier`, `FilterStateIdentifier` |
| **类型**：string, character vector |
| **默认值**：`""` |

### **状态名称必须解析为 Simulink 信号对象** — 要求状态名称解析为信号对象 `off`（默认）| `on`

选择此参数以要求离散时间积分器或滤波器状态名称解析为 Simulink 信号对象。

#### 依赖关系

要为离散时间积分器或滤波器状态启用此参数：

1. 将 **Time domain** 设置为 `Discrete-time`。
2. 为积分器或滤波器 **状态名称** 指定一个值。
3. 将模型配置参数 **Signal resolution** 设置为 `None` 以外的值。

#### 编程使用

|  |
| --- |
| **模块参数**：`IntegratorStateMustResolveToSignalObject`, `FilterStateMustResolveToSignalObject` |
| **类型**：string, character vector |
| **值**：`"off"`, `"on"` |
| **默认值**：`"off"` |
## 所属库

Simulink / Continuous

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

对于连续时间 PID 控制器（**Time domain** 设置为 `Continuous-time`）：

- 考虑使用 Model Discretizer 将连续时间模块映射到支持代码生成的离散等效模块。要访问 Model Discretizer，请在 **Apps** 选项卡的 **Control Systems** 下，点击 **Model Discretizer**。
- 不建议用于生产代码。

对于离散时间 PID 控制器（**Time domain** 设置为 `Discrete-time`）：

- 当置于触发子系统层次结构内时，依赖于绝对时间。
- 在某些条件下，生成的代码依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

仅支持离散时间 PID 控制器的定点代码生成（**Time domain** 设置为 `Discrete-time`）。

## 版本历史

**在 R2009b 中引入**

### R2024b：使用新端口从外部指定抗积分饱和算法

该模块现在允许您使用新的输入端口 **extAW** 从外部指定抗积分饱和算法。该模块还在 **preInt** 输出端口提供积分器之前的信号，您可以将其用作自定义算法的输入。PID 控制器模块提供两种内置抗积分饱和方法，但是，为了解除积分器的饱和，这些方法依赖于模块组件之和超过指定的模块输出限值。如果您的应用在 PID 控制器模块下游存在饱和或限幅，您可以使用新的 **extAW** 和 **preInt** 端口来实现自定义抗积分饱和逻辑。要启用新端口，请在 **Saturation** 选项卡上，选择 **Limit Output** 并将 **Anti-windup Method** 设置为 `external`。

### R2024a：使用来自外部源的微分信号

PID 控制器模块现在允许您将对象信号 *y* 的微分直接作为模块的输入提供。当您的模型中已有微分信号并希望跳过模块内部的微分计算时，这非常有用。

要启用用于提供微分的输入端口，请选择具有微分作用的控制器类型，并启用 **Use externally sourced derivative** 参数。

### R2022b：当积分器和滤波器初始条件超出饱和限值时发出错误

当积分器或滤波器初始条件值超出输出饱和限值时，该模块现在会发出错误。在以前的版本中，当这些初始条件具有此类值时，模块不会发出错误。

如果此更改影响您的模型，请更新 PID 积分器或滤波器初始条件值，使其在输出饱和限值范围内。

### R2021b：`ReferenceBlock` 参数返回不同的路径

从 R2021b 开始，`get_param` 函数为 `ReferenceBlock` 参数返回不同的值。`ReferenceBlock` 参数是所有 Simulink 模块共有的属性，给出模块所链接的库模块的路径。PID Controller (2DOF) 和 Discrete PID Controller (2DOF) 模块现在链接到 `'slpidlib/PID Controller (2DOF)'`。以前，这些模块链接到 `'pid_lib/PID Controller (2DOF)'`。

此更改不影响任何其他功能或工作流。您仍然可以将以前的路径与 `set_param` 函数一起使用。

### R2020b：`ReferenceBlock` 参数返回不同的路径

从 R2020b 开始，`get_param` 函数为 `ReferenceBlock` 参数返回不同的值。`ReferenceBlock` 参数是所有 Simulink 模块共有的属性，给出模块所链接的库模块的路径。PID Controller (2DOF) 和 Discrete PID Controller (2DOF) 模块现在链接到 `'pid_lib/PID Controller (2DOF)'`。以前，这些模块链接到 `'simulink/Continuous/PID Controller (2DOF)'`。

此更改不影响任何其他功能或工作流。您仍然可以将以前的路径与 `set_param` 函数一起使用。

## 描述

连续时间或离散时间二自由度 PID 控制器

PID Controller (2DOF) 模块实现二自由度 PID 控制器（PID、PI 或 PD）。该模块与 **Time domain** 参数设置为 `Continuous-time` 的 Discrete PID Controller (2DOF) 模块相同。

该模块基于参考信号与测量的系统输出之间的差值生成输出信号。该模块根据您指定的设定点权重（**b** 和 **c**）为比例和微分作用计算加权差值信号。模块输出是各自差值信号上比例、积分和微分作用之和，其中每个作用根据增益参数 **P**、**I** 和 **D** 进行加权。一阶极点对微分作用进行滤波。

该模块支持多种控制器类型和结构。模块中的可配置选项包括：

- 控制器类型（PID、PI 或 PD）— 请参阅 **Controller** 参数。
- 控制器形式（Parallel 或 Ideal）— 请参阅 **Form** 参数。
- 时间域（连续或离散）— 请参阅 **Time domain** 参数。
- 初始条件和复位触发 — 请参阅 **Source** 和 **External reset** 参数。
- 输出饱和限值和内置抗积分饱和机制 — 请参阅 **Limit output** 参数。
- 用于无扰控制切换和多回路控制的信号跟踪 — 请参阅 **Enable tracking mode** 参数。

当您更改这些选项时，模块的内部结构通过激活不同的变体子系统而改变。（请参阅 Implement Variations in Separate Hierarchy Using Variant Subsystems。）要检查模块及其变体子系统的内部结构，请右键点击模块并选择 **Mask** > **Look Under Mask**。

### 控制配置

在一个常见实现中，PID Controller 模块工作在反馈回路的前馈路径中。

对于接受误差信号（设定点与系统输出之间的差值）的单输入模块，请参阅 PID Controller。

### PID 增益整定

PID 控制器系数和设定点权重可手动或自动整定。自动整定需要 Simulink® Control Design™ 软件。有关自动整定的详细信息，请参阅 **Select tuning method** 参数。
