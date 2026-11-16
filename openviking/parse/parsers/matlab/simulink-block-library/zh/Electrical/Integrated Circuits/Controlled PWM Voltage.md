---
type: simulink-block
title: 'Controlled PWM Voltage'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Integrated Circuits'
documentation_page: 'controlledpwmvoltage'
documentation_source_path: 'ref/controlledpwmvoltage.html'
language: zh-CN
chinese_source: worker-translation
---

# Controlled PWM Voltage

## 端口

### 输入

### **u** — 控制信号，无量纲物理信号

指定占空比的输入物理信号。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `PS input`。

### 守恒

### **ref+** — 正极端子电气

正电气参考电压。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Electrical input ports`。

### **ref-** — 负极端子电气

负电气参考电压

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Electrical input ports`。

### **PWM** — 脉宽调制信号电气

与脉宽调制信号关联的电气守恒端口。

### **REF** — 浮动零伏参考电气

与浮动零伏参考关联的电气守恒端口。

## 参数

### **Modeling option** — 是否对电气或物理信号输入端口建模 `Electrical input ports`（默认） | `PS input`

是否对电气或物理信号输入端口建模。

### PWM

### **PWM frequency** — PWM 输出信号频率 1000 Hz（默认）

PWM 输出信号的频率。

### **Pulse delay time** — 开通延迟 0 s（默认）

在仿真时间等于 **Pulse delay time** 之前，脉冲序列不会开始。您可以为 **Pulse delay time** 指定一个较小的值，以微调开关时间，并确保关断中的器件在开通中的器件开始导通之前已完全关断。您也可以使用较大的延迟时间，例如，如果您需要脉冲序列仅在若干周期之后才开始。您提供的值必须大于或等于零。

#### 依赖关系

当 **Simulation mode** 参数设置为 `PWM` 时启用。

### **Pulse width offset** — 加长或缩短脉冲 0 s（默认）

所需脉冲宽度由所需占空比与脉冲频率的倒数之积定义，可以通过为 **Pulse width offset** 提供的值进行偏移。正值会按固定量加长脉冲。负值会缩短脉冲。您可以将此参数与 **Pulse delay time** 一起使用，以微调开关时间，从而在某些电路中最小化开关损耗。

#### 依赖关系

当 **Simulation mode** 参数设置为 `PWM` 时启用。

### **Minimum pulse width** — 最小脉冲长度 0 s（默认）

最小脉冲长度，基于内部时钟或以编程方式定义，用于保护所驱动的器件。您提供的值必须大于或等于零。

#### 依赖关系

当 **Simulation mode** 参数设置为 `PWM` 时启用。

### **Simulation mode** — 选择输出电压类型 `PWM`（默认） | `Averaged`

选择输出电压类型：

- `PWM` — 生成脉宽调制信号。
- `Averaged` — 输出为常量，其值等于 PWM 信号的平均值。

### **Switching event type** — 选择开关事件类型 `Asynchronous – Best for variable-step solvers`（默认） | `Discrete-time – Best for fixed-step solvers`

选择在输出高电平与输出低电平状态之间切换时的开关事件类型：

- `Asynchronous – Best for variable-step solvers` — 对于使用变步长求解器的桌面仿真，此选项更高效，因为达到相同精度级别需要更少的仿真步数。
- `Discrete-time – Best for fixed-step solvers` — 与定步长求解器（包括局部求解器）一起使用。有关详细信息，请参阅 Simulating with Fixed Time Step — Local and Global Fixed-Step Solvers。

#### 依赖关系

当 **Simulation mode** 参数设置为 `PWM` 时启用。

### **Sample time** — 离散采样时间 1e-6 s（默认）

模块输出状态更新之间的时间。采样时间必须是仿真步长的倍数。为了使 PWM 控制具有足够的分辨率，请将采样时间设置为小于 PWM 周期的百分之一。（PWM 周期为 PWM 频率的倒数。）

#### 依赖关系

当 **Switching event type** 参数设置为 `Discrete-time – Best for fixed-step solvers` 时启用。

### 输入缩放

### **Input voltage for 0% duty cycle** — Vmin 0 V（默认）

使 PWM 信号占空比为 0% 时的输入电压值。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Electrical input ports`。

### **Input voltage for 100% duty cycle** — Vmax 5 V（默认）

使 PWM 信号占空比为 100% 时的输入电压值。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Electrical input ports`。

### **Input value for 0% duty cycle** — 最小信号值 0（默认）

使 PWM 信号占空比为 0% 时的输入信号值。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `PS input`。

### **Input value for 100% duty cycle** — 最大信号值 1（默认）

使 PWM 信号占空比为 100% 时的输入信号值

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `PS input`。

### 输出电压

### **Output voltage amplitude** — 高输出时的信号幅度 5 V（默认）

输出为高电平时 PWM 信号的幅度。

## 所属库

Simscape / Electrical / Integrated Circuits

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008b 中引入**

## 描述

脉宽调制电压源

Controlled PWM Voltage 模块表示脉宽调制 (PWM) 电压源。您可以通过将 **Modeling option** 参数设置为以下任一值来对电气或物理信号输入端口建模：

- `Electrical input ports` — 模块根据其 **ref+** 和 **ref-** 端口两端的参考电压计算占空比。此选项为默认值。
- `PS input` — 通过使用输入物理信号端口直接指定占空比值。

如果将 **Modeling option** 设置为 `Electrical input ports`，则所需占空比为

100\*(Vref−Vmin)/(Vmax−Vmin) percent

其中：

- *V*ref 是 **ref+** 和 **ref-** 端口两端的参考电压。
- *V*min 是最小参考电压。
- *V*max 是最大参考电压。

**Output voltage amplitude** 参数的值决定输出电压的幅度。

在零时刻，脉冲初始化为高电平，除非 **Pulse delay time** 参数大于零，或所需占空比为零。

您可以使用 **Pulse delay time** 和 **Pulse width offset** 参数添加小的开通延迟和小的关断提前。这在微调开关时间以最小化开关损耗时可能很有用。

在 PWM 模式下，模块在输出高电平与输出低电平状态之间切换时，有两种开关事件类型选项：

- `Asynchronous – Best for variable-step solvers` — 异步事件更适合变步长求解器，因为达到相同精度级别需要更少的仿真步数。在异步模式下，PWM 开关事件会生成过零点，因此无论仿真最大步长如何，开关时间始终能准确确定。
- `Discrete—time – Best for fixed-step solvers` — 离散时间事件更适合定步长操作，因为这样开关事件始终与仿真步长同步。在定步长求解器中使用异步实现有时可能导致事件最多晚一个仿真步长。有关详细信息，请参阅 Simulating with Fixed Time Step — Local and Global Fixed-Step Solvers。

如果您使用定步长或局部求解器以及离散时间开关事件类型，则以下限制适用于 **Sample time** 参数值：

- 采样时间必须是仿真步长的倍数。
- 采样时间必须相对于 PWM 周期足够小，以确保足够的分辨率。

### 假设和限制

该模型基于以下假设：

- 此模块的 REF 输出是浮动的，它不连接到 Electrical Reference。这样做的一个后果是，如果您将 PWM 和 REF 电气端口直接连接到 H 桥或栅极驱动器的 PWM 和 REF 电气端口，则必须将 Electrical Reference 模块连接到 REF 连接线。
- 不要将 Controlled PWM 模块直接连接到半导体栅极，因为这会忽略决定开关动态的栅极驱动器输出阻抗。使用 Gate Driver 或 Half-Bridge Driver 模块设置栅源或栅射电压。
- 不要使用 Controlled PWM 模块直接驱动电机模块。PWM 电机驱动器在脉冲之间会开路。使用 H-Bridge 模块驱动电机模块。
- 当通过 H-Bridge 模块驱动电机时，将 **Simulation mode** 参数设置为 `Averaged` 以加速仿真。您还必须将 H-Bridge 模块的 **Simulation mode** 参数设置为 `Averaged` 模式。这会将所需 PWM 电压的平均值施加到电机。`Averaged` 模式假设电机感性项的阻抗在 **PWM frequency** 下很小。要验证此假设，请使用 `PWM` 模式运行仿真，并将结果与使用 `Averaged` 模式获得的结果进行比较。
- 如果您正在对模型进行线性化，请将 **Simulation mode** 参数设置为 `Averaged`，并确保已正确指定模块的工作点。您只能针对对应占空比大于零且小于 100% 的输入对模块进行线性化。
- 当您在 `PWM` 模式下使用此模块，并且在 Solver Configuration 模块中选中 **Use local solver option** 时，请将 **Switching event type** 参数设置为 `Discrete—time – Best for fixed-step solvers`。在这种情况下使用 `Asynchronous – Best for variable-step solvers` 选项可能会产生不准确结果，因为使用局部求解器进行仿真意味着定步长，并且 PWM 事件不会始终与仿真步长精确重合。这会导致 PWM 事件有时晚一个仿真步长发生。
