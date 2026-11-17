---
type: simulink-block
title: 'H-Bridge'
family: 'semiconductors-converters'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'hbridge'
documentation_source_path: 'ref/hbridge.html'
language: zh-CN
chinese_source: worker-translation
---

# H-Bridge

## 端口

### 守恒

### **+** — 正负载连接端口（电气）

与正负载连接关联的电气守恒端口。

### **-** — 负负载连接端口（电气）

与负负载连接关联的电气守恒端口。

### **V+** — 正电源连接（电气）

与正电源连接关联的电气守恒端口。

#### 依赖关系

仅当您为 **Power supply** 参数选择 `External` 时，此端口才可见。

### **V-** — 负电源连接（电气）

与负电源连接关联的电气守恒端口。

#### 依赖关系

仅当您为 **Power supply** 参数选择 `External` 时，此端口才可见。

### **PWM** — 脉宽调制信号（电气）

与脉宽调制信号关联的电气守恒端口。电压相对于 **REF** 端口定义。

### **REF** — 参考（电气）

与浮地零伏参考关联的电气守恒端口。

### **REV** — REV（电气）

与用于控制何时反转 H-Bridge 模块输出极性的电压关联的电气守恒端口。该电压相对于 **REF** 端口定义。

### **BRK** — BRK（电气）

与用于控制何时短路 H-Bridge 模块输出的电压关联的电气守恒端口。该电压相对于 **REF** 端口定义。

### **H** — 热端口（热）

热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port` (默认) | `Show thermal port`

是否启用模块的热端口并对热参数建模。

### 仿真模式与负载假设

### **Power supply** — 电源端口的可见性 `Internal` (默认) | `External`

为电源类型选择以下选项之一：

- `Internal` — 电源端口为内部端口且不可见。这是默认选项。
- `External` — 电源端口暴露。

### **Simulation mode** — 仿真模式 `PWM` (默认) | `Averaged`

为输出电压类型选择以下选项之一：

- `PWM` — 输出电压为脉宽调制信号。这是默认选项。
- `Averaged` — 输出电压为常量，其值等于 PWM 信号的平均值。

### **Freewheeling mode** — 续流模式 `Via one semiconductor switch and one freewheeling diode` (默认) | `Via two freewheeling diodes` | `Via two semiconductor switches and one freewheeling diode`

为 H 桥耗散电路的类型选择以下选项之一：

- `Via one semiconductor switch and one freewheeling diode` — 在此模式下，模块通过保持一个高边桥臂永久导通，并使用 PWM 信号调制相应的低边桥臂来控制负载。这意味着当桥关断时，模块仅使用其中一个续流二极管来完成耗散电路。此选项为默认值。
- `Via two freewheeling diodes` — 在此模式下，桥关断状态期间所有桥臂均关断。这意味着模块通过两个续流二极管在电源两端耗散负载电流。
- `Via two semiconductor switches and one freewheeling diode` — 在此模式下，模块通过保持一个高边桥臂永久导通，并使用 PWM 信号在使能相应的低边桥臂和对侧高边桥臂之间切换来控制负载。这意味着当桥关断时，模块使用与一个桥臂并联的续流二极管，再加上另一个串联桥臂，来完成耗散电路。

#### 依赖关系

仅当您为 **Simulation mode** 参数选择 `PWM`，或者为 **Simulation mode** 参数选择 `Averaged` 并为 **Load current characteristics** 参数选择 `Unsmoothed or discontinuous` 时，此参数才可见。

### **Regenerative braking** — 再生制动 `Depends on REV flag and current sign` (默认) | `Always enabled (suitable for linearization)`

为 H 桥耗散电路的类型选择以下选项之一：

- `Depends on REV flag and current sign` — 此选项为默认值。
- `Always enabled (suitable for linearization)` — 当控制器始终设置 **REV** 标志以确保再生制动时，可以使用此选项。如果您需要为控制目的对模型进行线性化，以确保 H-Bridge 在零占空比需求附近可线性化，则此选项很有用。

#### 依赖关系

仅当您为 **Simulation mode** 参数选择 `Averaged` 时，此参数才可见。

### **Load current characteristics** — 负载电流特性 `Smoothed` (默认) | `Unsmoothed or discontinuous`

为负载电流类型选择以下选项之一：

- `Smoothed` — 假定由于负载电感，电流实际上是连续的。此选项为默认值。
- `Unsmoothed or discontinuous` — 用于电流不平滑或可能不连续（即在 PWM 周期之间降至零）的情况。对于此选项，您还必须为 **Total load series resistance**、**Total load series inductance** 和 **PWM frequency** 参数提供值。在仿真期间，模块使用这些值来计算更准确的 H 桥输出电压值，以实现与在 PWM 模式下仿真时相同的平均电流。

#### 依赖关系

仅当您为 **Simulation mode** 参数选择 `Averaged` 时，此参数才可见。

### **Load total series resistance** — 负载总串联电阻 `10``Ohm` (默认)

H 桥看到的总负载串联电阻。

#### 依赖关系

仅当您为 **Simulation mode** 参数选择 `Averaged` 并为 **Load current characteristics** 参数选择 `Unsmoothed or discontinuous` 时，此参数才可见。

### **Load total series inductance** — 负载总串联电感 `1e-5``H` (默认)

H 桥看到的总负载串联电感。除了电机电感外，您还应包括为平滑电流而在电机外部添加的任何串联电感。

#### 依赖关系

仅当您为 **Simulation mode** 参数选择 `Averaged` 并为 **Load current characteristics** 参数选择 `Unsmoothed or discontinuous` 时，此参数才可见。

### **PWM frequency** — PWM 频率 `10``kHz` (默认)

驱动 H 桥的 PWM 频率。为保持一致，此值应与驱动 H-Bridge 模块的 Controlled PWM Voltage 模块所指定的 PWM 频率相同。

#### 依赖关系

仅当您为 **Simulation mode** 参数选择 `Averaged` 并为 **Load current characteristics** 参数选择 `Unsmoothed or discontinuous` 时，此参数才可见。

### **Freewheeling diode off-state conductance** — 续流二极管关断态电导 `1e-6``S` (默认)

反向偏置的续流二极管的电导。

#### 依赖关系

仅当您为 **Power supply** 参数选择 `External`，或者为 **Simulation mode** 参数选择 `Averaged` 并为 **Regenerative braking** 参数选择 `Depends on REV flag and current sign` 时，此参数才可见。

### 输入阈值

### **Enable threshold voltage** — 使能阈值电压 `2.5``V` (默认)

**PWM** 端口处的电压必须上升超过该阈值，才能启用 H-Bridge 模块输出。

#### 依赖关系

仅当 **Simulation mode**（**Simulation Mode & Load Assumptions** 参数）设置为 `PWM` 时，才使用此参数。

### **PWM signal amplitude** — PWM 信号幅值 `5.0``V` (默认)

PWM 输入处信号的幅值。

#### 依赖关系

仅当 **Simulation Mode & Load Assumptions** 选项卡上的 **Simulation mode** 参数设置为 `Averaged` 时，H-Bridge 模块才使用此参数。

### **Reverse threshold voltage** — 反向阈值电压 `2.5``V` (默认)

当 **REV** 端口处的电压大于此阈值时，输出极性变为负。

### **Braking threshold voltage** — 制动阈值电压 `2.5``V` (默认)

当 **BRK** 端口处的电压大于此阈值时，H-Bridge 模块输出端子通过以下串联设备短路：

- 一个桥臂
- 一个与导通的续流二极管并联的桥臂

### 桥参数

### **Output voltage amplitude** — 输出电压幅值 `12``V` (默认)

当输出开启时，H-Bridge 模块输出端口两端电压的幅值。

#### 依赖关系

仅当您为 **Power supply** 参数选择 `Internal` 时，此参数才可见。

### **Total bridge on resistance** — 桥总导通电阻 `0.1``Ohm` (默认)

当 **PWM** 端口处的电压大于 **Input Thresholds** 选项卡上 **Enable threshold voltage** 参数的值时，将负载连接到两条电源轨的两个半导体开关的总有效电阻。

### **Freewheeling diode on resistance** — 续流二极管导通电阻 `0.05``Ohm` (默认)

当 **PWM** 端口处的电压小于 **Input Thresholds** 选项卡上 **Enable threshold voltage** 参数的值时，耗散流过电机电流的续流二极管中的总电阻。

### **Measurement temperature** — 测量温度 `298.15``K` (默认)

**Bridge Parameters** 选项卡上电阻值所对应的温度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Show thermal port`。

### 温度依赖性

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Total bridge on resistance at second measurement temperature** — 第二测量温度下的桥总导通电阻 `0.1``Ohm` (默认)

将负载连接到两条电源轨的两个半导体开关的总有效电阻（如 **Total bridge on resistance** 参数定义中所述），在 **Second measurement temperature** 下给出。

### **Freewheeling diode on resistance at second measurement temperature** — 第二测量温度下的续流二极管导通电阻 `0.05``Ohm` (默认)

耗散流过电机电流的续流二极管中的总电阻（如 **Total bridge on resistance** 参数定义中所述），在 **Second measurement temperature** 下给出。

### **Second measurement temperature** — 第二测量温度 `398.15``K` (默认)

**Temperature Dependence** 选项卡上电阻值所对应的温度。

### 热端口

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Thermal mass** — 热质量 `100``J/K` (默认)

与热端口 **H** 关联的热质量。它表示将热端口温度升高一度所需的能量。默认值为 `100` J/K。

### **Initial temperature** — 初始温度 `298.15``K` (默认)

仿真开始时热端口的温度。

## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

### R2019b: 续流模式

从 R2019b 起，H-Bridge 模块可以选择暴露内部电源轨连接。

由于此更改，在较早版本中保存的模型内，请检查 Averaged 模式下且采用 `Unsmoothed or discontinuous` 电流假设的 H-Bridge 模块的 `Freewheeling mode` 参数是否仍设置为您需要的选项。

### R2019b: 再生制动

在 R2019b 之前，在 `Averaged` 仿真模式下，无论施加到 **REV** 端口用于控制模块输出极性反转的电压如何，H-Bridge 模块都假定为再生制动。从较早版本保存的、包含处于 `Averaged` 仿真模式的 H-Bridge 模块的模型，在后续版本中打开时，**Regenerative braking** 参数将设置为 `Always enabled (suitable for parameterization)`，并且结果保持不变。建议您将此参数改为 `Depends on REV flag and current sign`，以便在控制器未将其设置为再生制动时，**REV** 标志能被正确解释。

## 描述

H 桥电机驱动器

H-Bridge 模块表示一个 H 桥电机驱动器。
该模块具有以下两个 **Simulation mode** 选项：

- `PWM` — H-Bridge 模块输出是一个受控电压，取决于 **PWM** 端口处的输入信号。如果输入信号的值大于 **Enable threshold voltage** 参数值，则 H-Bridge 模块输出开启，并且其值等于 **Output voltage amplitude** 参数值。如果其值小于 **Enable threshold voltage** 参数值，则该模块使用以下三个 **Freewheeling mode** 选项之一来维持负载电路：

  - `Via one semiconductor switch and one freewheeling
    diode`
  - `Via two freewheeling diodes`
  - `Via two semiconductor switches and one freewheeling
    diode`

  第一个和第三个选项有时称为同步运行。

  **REV** 端口处的信号决定输出的极性。如果 **REV** 端口处信号的值小于 **Reverse threshold voltage** 参数值，则输出为正极性；否则，输出为负极性。
- `Averaged` — 此模式有两个 **Load current characteristics** 选项：

  - `Smoothed`
  - `Unsmoothed or discontinuous`

  `Smoothed` 选项假设由于负载电感，电流实际上是连续的。在这种情况下，H-Bridge 模块输出为：

  VOVPWMAPWM−IOUTRON

  其中：

  - *VO* 是 **Output voltage amplitude** 参数的值。
  - *VPWM* 是 **PWM** 端口处电压的值。
  - *APWM* 是 **PWM signal amplitude** 参数的值。
  - *IOUT* 是输出电流的值。
  - *RON* 是 **Bridge on resistance** 参数。

  如果 PWM 频率足够大，电流将是平滑的。通过桥臂回馈到电源进行续流的同步运行也有助于平滑电流。对于电流不平滑，或者可能不连续（即，在 PWM 周期之间降为零）的情况，请使用 `Unsmoothed or discontinuous` 选项。对于此选项，还必须为 **Total load series resistance**、**Total load series inductance** 和 **PWM frequency** 提供值。在仿真期间，该模块使用这些值来计算 H 桥输出电压的更准确值，该值可实现与在 PWM 模式下仿真时相同的平均电流。

当使用 Controlled PWM Voltage 模块驱动 H-Bridge 模块时，将 **Simulation mode** 参数设置为 `Averaged` 以加速仿真。还必须将 Controlled PWM Voltage 模块的 **Simulation mode** 参数设置为 `Averaged` 模式。这会将所需 PWM 电压的平均值施加到电机。`Averaged` 模式仿真结果的准确性取决于你对负载电流所作假设的有效性。如果指定电流为 `Unsmoothed or discontinuous`，则准确性还取决于你提供的负载电阻和电感值是否具有代表性。此模式还对电流不连续情况下的底层方程做出一些简化假设。对于典型的电机和桥参数，准确性应在几个百分点以内。要验证 `Averaged` 模式准确性，请使用 `PWM` 模式运行仿真，并将结果与使用 `Averaged` 模式获得的结果进行比较。

当 **BRK** 端口处呈现的电压大于 **Braking threshold voltage** 时，会调用制动模式。无论处于 `PWM` 还是 `Averaged` 模式，当处于制动模式时，H 桥由两个电阻 *R1* 和 *R2* 的串联组合建模，其中：

- *R1* 是单个桥臂的电阻，即 **Total bridge on resistance** 参数值的一半。
- *R2* 是单个桥臂与二极管电阻并联的电阻，即 *R1* · *Rd* / ( *R1* + *Rd* )，其中 *Rd* 是二极管电阻。

### 外部电源

要对直流电源承受的需求进行建模，你可以通过将 **Power supply** 参数设置为 `External` 来暴露 H-Bridge 模块的电源端口。如果电源端口已暴露，则仅支持 PWM 仿真模式。

**注意**

如果 **Power supply** 参数设置为 `External`，则该模块能够通过参考电源轨电压来计算负载侧电压偏移。但是，如果电源轨连接未暴露，则必须在负载侧添加一个 Electrical Reference 模块。

### 热效应建模

此模块有一个可选热端口。要控制热端口的可见性，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 该模块不包含热端口。
- `Show thermal port` — 该模块包含一个热守恒端口。

当你暴露热端口时：

- 由桥导通电阻和续流二极管产生的热量会添加到热端口。热端口具有关联的热质量和初始温度，你可以从 **Thermal Port** 参数进行设置。
- 桥导通电阻和续流二极管电阻成为温度的函数。你可以从 **Temperature Dependence** 参数定义这些电阻的值以及第二个测量温度。假设电阻在两个测量温度之间线性变化。对于此范围之外的温度，将使用外推，但在以 Averaged 模式且具有不连续负载电流特性进行仿真时除外。
