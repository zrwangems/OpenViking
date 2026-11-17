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
```yaml
ports:
- name: u
  summary: 控制信号，无量纲物理信号
  direction: input
- name: ref+
  summary: 正极端子电气
  direction: input
- name: ref-
  summary: 负极端子电气
  direction: input
- name: PWM
  summary: 脉宽调制信号电气
  direction: input
- name: REF
  summary: 浮地零伏参考电气
  direction: input
```

### 输入

### **u** — 控制信号，无量纲物理信号

指定占空比的输入物理信号。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`PS input`。
### 守恒

### **ref+** — 正极端子电气

正极电气参考电压。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Electrical input ports`。

### **ref-** — 负极端子电气

负极电气参考电压

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Electrical input ports`。

### **PWM** — 脉宽调制信号电气

与脉宽调制信号关联的电气守恒端口。

### **REF** — 浮地零伏参考电气

与浮地零伏参考关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 是对电气输入端口还是物理信号输入端口进行建模 Electrical input ports（默认）| PS input
  group: ''
- name: PWM frequency
  summary: PWM 输出信号频率 1000 Hz（默认）
  group: PWM
- name: Pulse delay time
  summary: 导通延迟 0 s（默认）
  group: PWM
- name: Pulse width offset
  summary: 延长或缩短脉冲 0 s（默认）
  group: PWM
- name: Minimum pulse width
  summary: 脉冲的最小长度 0 s（默认）
  group: PWM
- name: Simulation mode
  summary: 选择输出电压类型 PWM（默认）| Averaged
  group: PWM
- name: Switching event type
  summary: 选择开关事件类型 Asynchronous – Best for variable-step solvers（默认）| Discrete-time – Best for fixed-step solvers
  group: PWM
- name: Sample time
  summary: 离散采样时间 1e-6 s（默认）
  group: PWM
- name: Input voltage for 0% duty cycle
  summary: Vmin 0 V（默认）
  group: 输入缩放
- name: Input voltage for 100% duty cycle
  summary: Vmax 5 V（默认）
  group: 输入缩放
- name: Input value for 0% duty cycle
  summary: 最小信号值 0（默认）
  group: 输入缩放
- name: Input value for 100% duty cycle
  summary: 最大信号值 1（默认）
  group: 输入缩放
- name: Output voltage amplitude
  summary: 高电平输出时的信号幅值 5 V（默认）
  group: 输出电压
```

### **Modeling option** — 是对电气输入端口还是物理信号输入端口进行建模 `Electrical input ports`（默认）| `PS input`

是对电气输入端口还是物理信号输入端口进行建模。

### PWM

### **PWM frequency** — PWM 输出信号频率 1000 Hz（默认）

PWM 输出信号的频率。

### **Pulse delay time** — 导通延迟 0 s（默认）

在仿真时间等于 **Pulse delay time** 之前，脉冲序列不会启动。您可以为 **Pulse delay time** 指定一个较小的值，以微调开关时间，并确保正在关断的器件在正在导通的器件开始导通之前完全关断。您也可以使用较大的延迟时间，例如，如果您需要脉冲序列仅在若干个周期之后才开始。您提供的值必须大于或等于零。

#### 依赖关系

当 **Simulation mode** 参数设置为 `PWM` 时启用。

### **Pulse width offset** — 延长或缩短脉冲 0 s（默认）

所要求的脉冲宽度（由所要求的占空比与脉冲频率的倒数的乘积定义）可以通过您为 **Pulse width offset** 提供的值进行偏移。正值用于将脉冲延长一个固定量。负值用于缩短脉冲。您可以将此参数与 **Pulse delay time** 一起使用，以微调开关时间，从而在某些电路中最小化开关损耗。

#### 依赖关系

当 **Simulation mode** 参数设置为 `PWM` 时启用。

### **Minimum pulse width** — 脉冲的最小长度 0 s（默认）

基于内部时钟或以编程方式定义的最小脉冲长度，用于保护所驱动的器件。您提供的值必须大于或等于零。

#### 依赖关系

当 **Simulation mode** 参数设置为 `PWM` 时启用。

### **Simulation mode** — 选择输出电压类型 `PWM`（默认）| `Averaged`

选择输出电压类型：

- `PWM` — 生成脉宽调制信号。
- `Averaged` — 输出为常数，其值等于 PWM 信号的平均值。

### **Switching event type** — 选择开关事件类型 `Asynchronous – Best for variable-step solvers`（默认）| `Discrete-time – Best for fixed-step solvers`

选择在输出高状态和输出低状态之间切换时的开关事件类型：

- `Asynchronous – Best for variable-step
  solvers` — 对于使用变步长求解器的桌面仿真，此选项更高效，因为在相同精度水平下它需要更少的仿真步数。
- `Discrete-time – Best for fixed-step
  solvers` — 与定步长求解器（包括局部求解器）一起使用。有关详细信息，请参阅 Simulating with Fixed Time Step — Local and Global Fixed-Step Solvers。

#### 依赖关系

当 **Simulation mode** 参数设置为 `PWM` 时启用。

### **Sample time** — 离散采样时间 1e-6 s（默认）

模块输出状态更新之间的时间。采样时间必须是仿真步长的倍数。为了使 PWM 控制具有足够的分辨率，请将采样时间设置为小于 PWM 周期的百分之一。（PWM 周期是 PWM 频率的倒数。）

#### 依赖关系

当 **Switching event type** 参数设置为 `Discrete-time – Best for fixed-step
solvers` 时启用。

### 输入缩放

### **Input voltage for 0% duty cycle** — Vmin 0 V（默认）

PWM 信号具有 0% 占空比时的输入电压值。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Electrical input ports`。

### **Input voltage for 100% duty cycle** — Vmax 5 V（默认）

PWM 信号具有 100% 占空比时的输入电压值。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Electrical input ports`。

### **Input value for 0% duty cycle** — 最小信号值 0（默认）

PWM 信号具有 0% 占空比时的输入信号值。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `PS input`。

### **Input value for 100% duty cycle** — 最大信号值 1（默认）

PWM 信号具有 100% 占空比时的输入信号值

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `PS input`。

### 输出电压

### **Output voltage amplitude** — 高电平输出时的信号幅值 5 V（默认）

输出为高电平时 PWM 信号的幅值。
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

Controlled PWM Voltage 模块表示脉宽调制（PWM）电压源。您可以通过将 **Modeling option** 参数设置为以下任一值来对电气输入端口或物理信号输入端口进行建模：

- `Electrical input ports` — 模块基于其 **ref+** 和 **ref-** 端口两端的参考电压计算占空比。此选项为默认值。
- `PS input` — 通过使用输入物理信号端口直接指定占空比值。

如果将 **Modeling option** 设置为 `Electrical input
ports`，则所要求的占空比为

100\*Vref−VminVmax−Vmin percent

其中：

- *V*ref 是 **ref+** 和 **ref-** 端口两端的参考电压。
- *V*min 是最小参考电压。
- *V*max 是最大参考电压。

**Output voltage amplitude** 参数的值决定输出电压的幅值。

在时间为零时，脉冲初始化为高电平，除非 **Pulse delay
time** 参数大于零，或者所要求的占空比为零。

您可以使用参数 **Pulse delay time** 和 **Pulse width
offset** 来添加一个小的导通延迟和一个小关断提前量。这在微调开关时间以最小化开关损耗时可能很有用。

在 PWM 模式下，模块在输出高状态和输出低状态之间切换时有两种开关事件类型选项：

- `Asynchronous – Best for variable-step solvers`
  — 异步事件更适合变步长求解器，因为在相同精度水平下它们需要更少的仿真步数。在异步模式下，PWM 开关事件生成过零点，因此无论仿真最大步长如何，开关时间始终能够准确确定。
- `Discrete—time – Best for fixed-step solvers`
  — 离散时间事件更适合定步长操作，因为此时开关事件始终与仿真步长同步。将异步实现与定步长求解器一起使用有时可能导致事件最多延迟一个仿真步长。有关详细信息，请参阅 Simulating with Fixed Time Step — Local and Global Fixed-Step Solvers。

如果您使用定步长或局部求解器以及离散时间开关事件类型，则以下限制适用于 **Sample time** 参数值：

- 采样时间必须是仿真步长的倍数。
- 采样时间必须相对于 PWM 周期较小，以确保足够的分辨率。

### 假设和限制

该模型基于以下假设：

- 此模块的 REF 输出是浮地的，它不连接到 Electrical Reference。其后果之一是，如果您将 PWM 和 REF 电气端口直接连接到 H 桥或栅极驱动器的 PWM 和 REF 电气端口，则必须在 REF 连接线上连接一个 Electrical Reference 模块。
- 不要将 Controlled PWM 模块直接连接到半导体栅极，因为这会忽略决定开关动态的栅极驱动器输出阻抗。请使用 Gate Driver 或 Half-Bridge Driver 模块来设置栅源电压或栅射电压。
- 不要使用 Controlled PWM 模块直接驱动电机模块。PWM 电机驱动器在脉冲之间会开路。请使用 H-Bridge 模块来驱动电机模块。
- 当通过 H-Bridge 模块驱动电机时，将 **Simulation mode** 参数设置为 `Averaged` 以加速仿真。您还必须将 H-Bridge 模块的 **Simulation mode** 参数设置为 `Averaged` 模式。这会将所要求 PWM 电压的平均值施加到电机上。`Averaged` 模式假设电机感性项的阻抗在 **PWM frequency** 下很小。要验证此假设，请使用 `PWM` 模式运行仿真，并将结果与使用 `Averaged` 模式获得的结果进行比较。
- 如果您正在对模型进行线性化，请将 **Simulation
  mode** 参数设置为 `Averaged`，并确保已正确指定模块的工作点。您只能对占空比大于零且小于 100% 的输入对应的模块进行线性化。
- 当您在 Solver Configuration 模块中选择了 **Use local solver option** 的情况下以 `PWM` 模式使用此模块时，请将 **Switching event type** 参数设置为 `Discrete—time – Best for fixed-step
  solvers`。在这种情况下使用 `Asynchronous – Best for
  variable-step solvers` 选项可能会产生不准确的结果，因为使用局部求解器进行仿真意味着定步长，而 PWM 事件不会始终与仿真步长精确重合。这会导致 PWM 事件有时延迟一个仿真步长发生。
