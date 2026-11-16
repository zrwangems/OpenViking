---
type: simulink-block
title: 'Gain-Scheduled PID Autotuner'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Control System Design and Tuning / PID Controller Tuning / Real-Time PID Autotuning'
documentation_page: 'gainscheduledpidautotuner'
documentation_source_path: 'ug/gainscheduledpidautotuner.html'
language: zh-CN
chinese_source: worker-translation
---

# Gain-Scheduled PID Autotuner

## 端口

### 输入

### **u** — 来自控制器的信号 标量

将模块插入系统中，使该端口接受来自某个源的控制信号。通常，该端口接受来自系统中 PID 控制器的信号。

**数据类型：** `single` | `double`

### **y** — 被控对象输出 标量

将该端口连接到被控对象输出。

**数据类型：** `single` | `double`

### **start/stop** — 启动和停止自整定实验 标量

要启动和停止自整定过程，请在 `start/stop` 端口提供信号。当信号值从以下情况变化时：

- 负值或零变为正值时，实验启动
- 正值变为负值或零时，实验停止

当实验未运行时，模块将信号从 **u** 原样传递到 **u+Δu**。在此状态下，模块对被控对象或控制器行为没有影响。

通常，您可以使用从 0 变为 1 的信号来启动实验，并使用从 1 变为 0 的信号来停止实验。配置 **start/stop** 信号时需要考虑的一些要点包括：

- 当被控对象处于所需平衡工作点时启动实验。使用初始控制器将被控对象驱动到工作点。如果没有初始控制器（仅开环整定），您可以使用连接到 **u** 的源模块将被控对象驱动到工作点。
- 实验期间避免对被控对象造成任何负载扰动。负载扰动可能会使被控对象输出失真，并降低频率响应估计的精度。
- 让实验运行足够长时间，以便算法收集足够的数据，在其探测的所有频率上获得良好估计。

  对于 **Sinestream** 和 **Superposition** 模式，有两种方法可以确定何时停止实验：

  - 提前确定实验持续时间。在 superposition 实验模式下，实验持续时间的保守估计为 200/*ωc*，在 sinestream 实验模式下为 550/*ωc*，其中 *ωc* 是目标带宽。
  - 观察 `% conv` 输出处的信号，并在信号稳定在接近 100% 时停止实验。

  对于 **PRBS** 模式，根据指定的 **Target bandwidth** 和 **Controller sample time** 值，模块对话框会在 **Experiment** 选项卡的 **描述** 部分显示推荐的实验长度。过早停止实验可能会导致不正确的整定结果。
- 当您停止实验时，模块会计算整定后的 PID 增益，并更新 `pid gains` 端口处的信号。

您可以配置适合您应用的任何逻辑来控制实验的启动和停止时间。

**数据类型：** `single` | `double`

### **bandwidth** — 用于整定的目标带宽 标量

为 `Target bandwidth (rad/sec)` 参数提供值。有关详细信息，请参见该参数。

#### 依赖关系

要启用此端口，请在 Tuning 选项卡中，在 `Target bandwidth (rad/sec)` 旁边，选择 **Use external source**。

**数据类型：** `single` | `double`

### **target PM** — 用于整定的目标相位裕度 标量

为 `Target phase margin (degrees)` 参数提供值。有关详细信息，请参见该参数。

#### 依赖关系

要启用此端口，请在 Tuning 选项卡中，在 `Target phase margin (degrees)` 旁边，选择 **Use external source**。

**数据类型：** `single` | `double`

### **signal Amp** — 注入扰动信号的幅度 标量 | 向量

为 `Signal Amplitudes` 参数提供值。有关详细信息，请参见该参数。

#### 依赖关系

要启用此端口，请在 Experiment 选项卡中，在 `Signal Amplitudes` 旁边，选择 **Use external source**。

**数据类型：** `single` | `double`

### **scheduling Variable** — 调度变量 标量

指定调度变量。此信号指示系统在给定时间处于工作范围内的位置。查找表使用此信号确定 PID 增益的值。

### **Breakpoints** — 断点数据 向量

用于增益调度的断点数据，指定为向量。

#### 依赖关系

要启用此端口，请选择 **Use external signal**。

### **Update Trigger** — 触发控制信号 标量

用于触发增益更新的控制信号。

#### 依赖关系

要启用此端口，请将 **Method to trigger gain update** 设置为 **External trigger**。

### 输出

### **u+Δu** — 用于被控对象输入的信号 标量

将模块插入系统中，使该端口将输入信号馈送到被控对象。

- 当实验正在运行（`start/stop` 为正值）时，模块会在此端口向被控对象注入测试信号。如果有任何保护被控对象的饱和或速率限制，请将来自 **u+Δu** 的信号馈入其中。
- 当实验未运行时（`start/stop` 为零或负值），模块将信号从 **u** 原样传递到 **u+Δu**。

#### 依赖关系

要启用此端口，请在 **Output Signal Configuration** 中，选择 **control + perturbation**。

**数据类型：** `single` | `double`

### **Δu** — 被控对象输入扰动 标量

模块在此端口生成扰动信号。通常，您通过求和模块从此端口注入扰动。

- 当实验正在运行（**start/stop** 为正值）时，模块会在此端口生成扰动信号。
- 当实验未运行时（**start/stop** 为零或负值），此端口处的信号为零。在此状态下，模块对被控对象没有影响。

#### 依赖关系

要启用此端口，请在 **Output Signal Configuration** 中，选择 **perturbation only**。

**数据类型：** `single` | `double`

### **pid gains** — 整定后的 PID 系数 总线

此 4 元素总线信号包含整定后的 PID 增益 *P*、*I*、*D* 以及滤波器系数 *N*。这些值对应于 `Form` 参数中给出的表达式中的 `P`、`I`、`D` 和 `N` 参数。初始时，这些值分别为 0、0、0 和 100。模块在实验结束时更新这些值。即使您未整定 PIDF 控制器，此总线信号也始终具有四个元素。

**数据类型：** `single` | `double`

### **estimated PM** — 使用整定后控制器估计的相位裕度 标量

此端口输出由整定后控制器实现的估计相位裕度，以 degrees 为单位。模块在整定实验结束时更新此值。估计相位裕度根据 *G*(*jωc*)*C*(*jωc*) 的角度计算，其中 *G* 是估计的被控对象，*C* 是整定后的控制器，*ωc* 是穿越频率（带宽）。估计相位裕度可能不同于 `Target phase margin (degrees)` 参数指定的目标相位裕度。它是整定后系统所实现的鲁棒性和稳定性的指标。

- 通常，估计相位裕度接近目标相位裕度。一般来说，该值越大，整定后系统越鲁棒，超调越小。
- 负相位裕度表示闭环系统可能不稳定。

#### 依赖关系

要启用此端口，请在 Tuning 选项卡中，选择 **Output estimated phase margin achieved by tuned controller**。

### **frd** — 估计的频率响应 向量

此端口输出由实验估计的频率响应数据。初始时，`frd` 处的值为 [0, 0, 0, 0, 0]。在实验期间，模块在频率 [1/10, 1/3, 1, 3, 10]*ωc* 处注入信号，其中 *ωc* 是目标带宽。在实验期间的每个采样时间，模块使用分别包含这些频率处复数频率响应的向量更新 `frd`。对于 sinestream 和 superposition 信号，您可以使用响应的进度作为 `% conv` 的替代，以检查估计的收敛情况。当实验停止时，模块使用用于计算 PID 增益的最终估计频率响应更新 `frd`。

对于 **PRBS** 实验模式，此端口处的信号仅在估计实验完成后更新。

#### 依赖关系

要启用此端口，请在 Experiment 选项卡中，选择 **Plant frequency responses near bandwidth**。

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### 控制器设置

### **Controller type** — PID 控制器动作 `PIDN` (默认) | `P` | `I` | `PI` | `PD` | `PDN` | `PID` | ...

指定系统中 PID 控制器的类型。控制器类型指示控制器中存在的动作。以下控制器类型可用于 PID 自整定：

- `P` — 仅比例
- `I` — 仅积分
- `PI` — 比例和积分
- `PD` — 比例和微分
- `PDN` — 带微分滤波器的比例和微分
- `PID` — 比例、积分和微分
- `PIDN` — 带微分滤波器的比例、积分和微分

控制器类型必须与您正在整定的 PID 控制器匹配。

### **Form** — PID 控制器形式 `Parallel` (默认) | `Ideal`

指定控制器形式。控制器形式决定 PID 系数 *P*、*I*、*D* 和 *N* 的解释。

- `Parallel` — 在 `Parallel` 形式中，离散时间 PIDF 控制器的传递函数为：

  C=P+IFi(z)+D[N1+NFd(z)],

  其中 *Fi*(*z*) 和 *Fd*(*z*) 是积分器和滤波器公式（请参见 `Integrator method` 和 `Filter method`）。连续时间并联形式 PIDF 控制器的传递函数为：

  C=P+I(1s)+D(Nss+N).

  其他控制器动作相当于将 *P*、*I* 或 *D* 设置为零。
- `Ideal` — 在 `Ideal` 形式中，离散时间 PIDF 控制器的传递函数为：

  C=P[1+IFi(z)+D(N1+NFd(z))].

  连续时间理想形式 PIDF 控制器的传递函数为：

  C=P[1+I(1s)+D(Nss+N)].

  其他控制器动作相当于将 *D* 设置为零或将 *I* 设置为 `Inf`。（在理想形式中，控制器必须具有比例动作。）

控制器形式必须与您正在整定的 PID 控制器匹配。

**可调：** Yes

### **Sample time (-1 for inherited)** — PID 控制器的采样时间 0.1 (默认) | 正标量 | –1

指定 PID 控制器的采样时间，以 seconds 为单位。此值还设置模块执行的实验的采样时间。

要执行 PID 整定，模块会测量高达目标带宽 10 倍的频率处的频率响应信息。为确保该频率小于 Nyquist 频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* *ωc* 是您使用 **Sample time** 参数指定的控制器采样时间。

当您使用整定后的参数值更新 PID Controller 模块或自定义 PID 控制器时，请确保控制器采样时间匹配。

#### 提示

如果您希望在应用中针对不同采样时间运行已部署的模块，请将此参数设置为 –1，并将该模块放入 Triggered Subsystem 中。然后，以所需采样时间触发该子系统。如果您不打算在部署后更改采样时间，请指定固定且有限的采样时间。

### **Data Type** — 浮点精度 `double` (默认) | `single`

根据仿真环境或硬件要求指定浮点精度。

### Autotuner 选项卡

### **Tune at different sample time** — 启用与 PID 控制器和实验不同的采样时间进行整定 `off` (默认) | `on`

启用此参数可让整定以不同于您正在整定的 PID 控制器采样率以及模块执行的频率响应估计实验采样率的采样率运行。PID 增益整定算法计算量大，当您希望将模块部署到硬件并整定具有快速采样时间的控制器时，某些硬件可能无法在单个时间步内完成 PID 增益计算。为降低硬件吞吐量要求，请使用 **Tuning sample time** 参数指定比控制器采样时间更慢的整定采样时间。

### **Tuning sample time (sec)** — 整定算法的采样时间 0.2 (默认) | 正标量

指定整定算法的采样时间，以 seconds 为单位。

如果您打算将模块部署到处理能力有限的硬件上，并希望整定具有快速采样时间的控制器，请指定一个采样时间，使整定算法的运行速率慢于您正在整定的 PID 控制器。

#### 依赖关系

要启用此参数，请选择 **Tune at different sample time**。

### **Integrator method** — 积分器项的离散积分公式 `Forward Euler` (默认) | `Backward Euler` | `Trapezoidal`

指定控制器中积分器项的离散积分公式。在离散时间中，模块假定的 PID 控制器传递函数为：

C=P+IFi(z)+D[N1+NFd(z)],

采用并联形式，或采用理想形式，

C=P[1+IFi(z)+D(N1+NFd(z))].

对于控制器采样时间 *Ts*，`Integrator method` 参数按如下方式确定公式 *Fi*：

| Integrator method | *Fi* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优点的详细信息，请参见 Discrete PID Controller 模块参考页。

**可调：** Yes

### **Filter method** — 微分滤波器项的离散积分公式 `Forward Euler` (默认) | `Backward Euler` | `Trapezoidal`

指定控制器中微分滤波器项的离散积分公式。在离散时间中，模块假定的 PID 控制器传递函数为：

C=P+IFi(z)+D[N1+NFd(z)],

采用并联形式，或采用理想形式，

C=P[1+IFi(z)+D(N1+NFd(z))].

对于控制器采样时间 *Ts*，`Filter method` 参数按如下方式确定公式 *Fd*：

| Filter method | *Fd* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优点的详细信息，请参见 Discrete PID Controller 模块参考页。

**可调：** Yes

### **Target bandwidth (rad/sec)** — 整定后响应的目标穿越频率 1 (默认) | 正标量

目标带宽，以 rad/sec 为单位指定，是整定后开环响应 *CP* 的 0-dB 增益穿越频率的目标值，其中 *P* 是被控对象响应，*C* 是控制器响应。此穿越频率大致设定控制带宽。对于上升时间 *τ* seconds，目标带宽的良好猜测值为 2/*τ* rad/sec。

要执行 PID 整定，自整定器模块会测量高达目标带宽 10 倍的频率处的频率响应信息。为确保该频率小于 Nyquist 频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* 是您使用 **Sample time** 参数指定的控制器采样时间。由于此条件，您可以为整定强制的最快上升时间约为 6.67*Ts*。如果此上升时间不满足您的设计目标，请考虑减小 *Ts*。

为在闭环整定中获得最佳结果，请使用与初始 PID 控制器的带宽相差约 10 倍以内的目标带宽。要为更大的带宽变化整定控制器，请使用较小的变化逐步整定。

要通过输入端口提供目标带宽，请选择 **Use external source**。

### **Target phase margin (degrees)** — 开环响应的目标最小相位裕度 60（默认）| 0–90 范围内的标量

为整定的开环响应在穿越频率处指定目标最小相位裕度。目标相位裕度反映整定系统所需的鲁棒性。通常，选择约 45°–60° 范围内的值。一般而言，更高的相位裕度可改善超调，但可能限制响应速度。默认值 60° 倾向于平衡性能与鲁棒性，根据您被控对象的特性，产生约 5–10% 超调。

要通过输入端口提供目标相位裕度，请选择 **Use external source**。

**可调:** Yes

### **Experiment Mode** — 扰动信号类型 **Superposition**（默认）| **Sinestream** | **PRBS**

指定每个频率处的扰动是作为顺序正弦（**Sinestream**）、同时正弦（**Superposition**）还是伪随机二进制序列（**PRBS**）施加。

- **Sinestream** — 在此模式下，模块分别在每个频率处施加扰动。有关用于估计的 sinestream 信号的信息，请参阅 Sinestream Input Signals。
- **Superposition** — 在此模式下，扰动信号一次性包含所有指定频率。对于在频率向量 *ω* =
  [*ω*1, … ,
  *ω*N*]、幅值
  *A* = [*A*1, … ,
  *AN*] 处的频率响应估计，扰动信号为：

  Δu=∑iAisin(ωit).
- **PRBS** — 一种确定性伪随机二进制序列，在两个值之间切换，并具有类似白噪声的特性。与使用 sinestream 输入信号相比，PRBS 信号可减少总估计时间，同时产生可比的估计结果。PRBS 信号可用于估计通信和电力电子系统的频率响应。有关详细信息，请参阅 PRBS Input Signals。

**Sinestream** 模式可以更准确，也可以侵入性更小，因为扰动的总大小永远不会大于 **Signal Amplitudes** 参数指定的值。但是，由于 sinestream 扰动的顺序特性，您添加的每个频率点都会增加建议的实验时间（有关详细信息，请参阅 **start/stop** 输入端口）。因此，在 **Superposition** 模式下，估计实验通常快得多，且结果令人满意。

与 superposition 输入信号相比，Sinestream 信号可减少执行时间，但估计频率响应也需要更长时间。当处理能力有限且希望减少执行时间时，使用 sinestream 信号进行频率响应估计很有用。

要覆盖相似的频率范围，**PRBS** 模式下的实验长度通常比其他两种模式短得多。但是，在结果的速度和质量之间存在权衡。

### **Plant Type** — 被控对象的稳定性 `Stable`（默认）| `Integrating`

指定被控对象是稳定还是积分。如果被控对象有一个或多个积分器，请选择 `Integrating`。

### **Plant Sign** — 被控对象的符号 `Positive`（默认）| `Negative`

指定被控对象是正还是负。如果在标称工作点处，被控对象输入的正变化导致被控对象输出的正变化，请指定 `Positive`。否则，请指定 `Negative`。对于稳定被控对象，被控对象的符号是被控对象 DC 增益的符号。

### **Signal Amplitudes** — 扰动幅值 1（默认）| 标量 | 长度为 5 的向量

在实验期间，模块以频率 [1/10, 1/3, 1, 3, 10]*ωc* 将扰动信号注入被控对象，其中 *ωc* 是整定的目标带宽。使用 **Signal Amplitudes** 指定每个注入信号的幅值。指定：

- 标量值以在每个频率处注入相同幅值
- 长度为 5 的向量以在 [1/10, 1/3, 1, 3, 10]*ωc* 的每个频率处指定不同幅值

在具有典型目标带宽的典型被控对象中，实验频率处的被控对象响应幅值通常不会变化很大。在这种情况下，您可以使用标量值在所有频率处施加相同幅值的扰动。但是，如果您知道响应在频率范围内急剧衰减，请考虑降低低频输入的幅值并提高高频输入的幅值。当所有被控对象响应具有可比幅值时，估计实验在数值上更好。

扰动幅值必须：

- 足够大，使扰动克服被控对象执行器中的任何死区，并生成高于噪声水平的响应
- 足够小，使被控对象在标称工作点附近的近似线性区域内运行，并避免使被控对象输入或输出饱和

当 **Experiment mode** 为 **Superposition** 时，正弦信号会叠加。因此，扰动至少可以与所有幅值之和一样大。确保最大可能扰动在被控对象执行器的范围内。使执行器饱和可能会在估计的频率响应中引入误差。

要通过输入端口提供信号幅值，请选择 **Use external source**。

**可调:** Yes

### 增益调度选项卡

### **Breakpoints** — 增益调度断点 `[1 2 3]`（默认）| 向量

指定增益调度断点数据。

### **Use external signal** — 从输入端口指定断点 `off`（默认）| `on`

从模块输入端口指定断点。

### **Number of breakpoints** — 断点数 `3`（默认）| 正标量

指定外部断点信号中的断点数。

#### 依赖关系

要启用此参数，请选择 **Use external signal**。

### **Gain index tolerance** — 增益索引容差 `1e-3`（默认）| 非负标量

指定调度变量与断点之间的容差。为确定要更新数组中的哪个断点，模块将调度变量与断点数组进行比较，并使用此容差值确定最接近的值。

### **Use y as scheduling variable** — 使用被控对象输出调度断点 `on`（默认）| `off`

选择此选项可使用被控对象输出 **y** 调度断点。

### **Method of storing gains** — 存储增益的方法 `Internal to block`（默认）| `Data store memory`

指定存储增益的方法。

- `Internal to block` — 使用 **PID Gains Out** 输出端口。您可以将此输出信号直接馈入 PID Gain Scheduler 模块。
- `Data store memory` — 使用 Data Store Memory 模块存储增益。要创建数据存储模块，首先使用每个增益的 **Parameter Name** 参数为数据存储指定名称，然后单击 **将 Data Store Memory 块添加到模型** 按钮。该模块会在模型的顶层创建 Data Store Memory 模块。您可以使用 PID Controller 指定这些数据存储名称，以执行基于查找表的增益调度。

使用 **Gain initial conditions** 参数指定增益的初始值。当整定后的增益不可用时，模块使用初始值。

### **P Gain initial conditions** — 比例增益初始值 `0`（默认）| 标量 | 向量

将比例增益的初始值指定为标量或向量。当来自外部源（如 Closed-Loop PID Autotuner）的整定增益数据不可用时，模块使用此值。

- 标量 — 模块对所有断点使用此值。
- 向量 — 指定与 **Breakpoints** 长度相同的向量。模块使用当前断点对应索引处的初始值。

#### 依赖关系

要启用此端口，请将 **Controller type** 设置为具有比例作用的控制器类型。

### **P Gain Parameter Name** — 比例增益数据名称 `PGain`（默认）| 字符串

指定比例增益数据的数据存储名称。

#### 依赖关系

要启用此参数，请设置

- **Controller type** 为具有比例作用的控制器类型。
- **Method of obtaining gains** 为 `Data store memory`。

### **I Gain initial conditions** — 积分增益初始值 `0`（默认）| 标量 | 向量

将积分增益的初始值指定为标量或向量。当来自外部源的整定增益数据不可用时，模块使用此值。

- 标量 — 模块对所有断点使用此值。
- 向量 — 指定与 **Breakpoints** 长度相同的向量。模块使用当前断点对应索引处的初始值。

#### 依赖关系

要启用此参数，请将 **Controller type** 设置为具有积分作用的控制器类型。

### **I Gain Parameter Name** — 积分增益数据名称 `IGain`（默认）| 字符串

指定积分增益数据的数据存储名称。

#### 依赖关系

要启用此参数，请设置

- **Controller type** 为具有积分作用的控制器类型。
- **Method of obtaining gains** 为 `Data store memory`。

### **D Gain initial conditions** — 微分增益初始值 `0`（默认）| 标量 | 向量

将微分增益的初始值指定为标量或向量。当来自外部源的整定增益数据不可用时，模块使用此值。

- 标量 — 模块对所有断点使用此值。
- 向量 — 指定与 **Breakpoints** 长度相同的向量。模块使用当前断点对应索引处的初始值。

#### 依赖关系

要启用此参数，请将 **Controller type** 设置为具有微分作用的控制器类型。

### **D Gain Parameter Name** — 微分增益数据名称 `DGain`（默认）| 字符串

指定微分增益数据的数据存储名称。

#### 依赖关系

要启用此参数，请设置

- **Controller type** 为具有微分作用的控制器类型。
- **Method of obtaining gains** 为 `Data store memory`。

### **N Gain initial conditions** — 滤波器增益初始值 `100`（默认）| 标量 | 向量

将微分滤波器增益的初始值指定为标量或向量。当来自外部源的整定增益数据不可用时，模块使用此值。

- 标量 — 模块对所有断点使用此值。
- 向量 — 指定与 **Breakpoints** 长度相同的向量。模块使用当前断点对应索引处的初始值。

#### 依赖关系

要启用此参数，请将 **Controller type** 设置为具有滤波微分的控制器类型。

### **N Gain Parameter Name** — 滤波器增益数据名称 `NGain`（默认）| 字符串

指定微分滤波器增益数据的数据存储名称。

#### 依赖关系

要启用此参数，请设置：

- **Controller type** 为具有滤波微分的控制器类型。
- **Method of obtaining gains** 为 `Data store memory`。

### **Save breakpoints in gain array** — 将断点与 PID 增益一起保存 `off`（默认）| `on`

使用此选项可保存断点以及存储的增益数组。PID Gain Scheduler 模块可以解释此组合数据，用于增益调度应用。

#### 依赖关系

要启用此参数，请将 **Method of obtaining gains** 设置为 `Data store memory`。

### **Method to trigger gain update** — 更新触发方法 **Detect change in PID gains**（默认）| **External trigger**

指定触发增益更新的方法。

- **Detect change in PID gains** — 当输入增益发生变化时自动更新增益。
- **External trigger** — 使用外部信号触发增益更新。

### **Number of samples to delay update** — 延迟更新的样本数 `1`（默认）| 非负标量

触发事件后延迟增益更新的样本数。使用此选项可延迟更新增益，以便为自动整定算法留出足够时间来计算增益。

#### 查找表设置

### **P gain lookup method** — 比例增益查找方法 `Interpolation-Use End Values`（默认）| `Interpolation-Extrapolation` | `Use Input Nearest` | `Use Input Below` | `Use Input Above`

模块通过对断点数据（**Breakpoints**）和表数据（**PID Gains**）的输入向量应用您选择的查找方法来计算输出。有关详细信息，请参阅 How the Block Generates Output。

#### 依赖关系

要启用此参数，请将 **Controller type** 设置为具有比例作用的控制器类型。

### **I gain lookup method** — 积分增益查找方法 `Interpolation-Use End Values`（默认）| `Interpolation-Extrapolation` | `Use Input Nearest` | `Use Input Below` | `Use Input Above`

模块通过对断点数据（**Breakpoints**）和表数据（**PID Gains**）的输入向量应用您选择的查找方法来计算输出。有关详细信息，请参阅 How the Block Generates Output。

#### 依赖关系

要启用此参数，请将 **Controller type** 设置为具有积分作用的控制器类型。

### **D gain lookup method** — 微分增益查找方法 `Interpolation-Use End Values`（默认）| `Interpolation-Extrapolation` | `Use Input Nearest` | `Use Input Below` | `Use Input Above`

模块通过对断点数据（**Breakpoints**）和表数据（**PID Gains**）的输入向量应用您选择的查找方法来计算输出。有关详细信息，请参阅 How the Block Generates Output。

#### 依赖关系

要启用此端口，请将 **Controller type** 设置为具有微分作用的控制器类型。

### **N gain lookup method** — 微分滤波器增益查找方法 `Interpolation-Use End Values`（默认）| `Interpolation-Extrapolation` | `Use Input Nearest` | `Use Input Below` | `Use Input Above`

模块通过对断点数据（**Breakpoints**）和表数据（**PID Gains**）的输入向量应用您选择的查找方法来计算输出。有关详细信息，请参阅 How the Block Generates Output。

#### 依赖关系

要启用此参数，请将 **Controller type** 设置为具有滤波微分的控制器类型。

### **Saturate to max or min when overflows occur** — 溢出操作方法 `off`（默认）| `on`

当您选中此复选框时，溢出会饱和到数据类型可以表示的最大值或最小值。否则，溢出会回绕。

当您选中此复选框时，饱和会应用于模块上的每个内部运算，而不仅仅是输出或结果。通常，代码生成过程可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖 **Output** 数据类型的选项 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在模块上指定的 **Output** 数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

### 模块选项卡

### **输出信号配置** — 提供控制信号加扰动或仅扰动 **control action + perturbation**（默认） | **perturbation only**

默认情况下，该模块将控制信号作为输入，并在端口 **u+Δu** 处提供控制信号加上实验扰动。然后，您将此信号直接馈入被控对象输入。

此默认配置要求将该模块插入到控制器和被控对象之间。如果您希望自行将扰动信号加到控制信号上，请选择 **perturbation only**。在此配置中，模块输出仅包含扰动信号，位于端口 **Δu**。您使用求和模块将此扰动信号与 PID 控制器输出 **u** 相加后注入被控对象。

### 可视化选项卡

### **显示 Bode 图** — 绘制估计频率响应 `off`（默认） | `on`

*自 R2024b 起*

选择此项可生成 Bode 图，显示您整定的每个工作点的以下估计频率响应：

- 被控对象响应
- 开环响应
- 参考跟踪响应
- 控制器作用响应
- 输入扰动抑制响应
- 输出扰动抑制响应

您可以将模块配置为在整定每个断点后或在仿真结束时更新绘图。如果您有一个表示预期被控对象响应或其他相关基线的 LTI 模型，可使用 **基线被控对象模型** 参数将其包含在绘图中作为参考。

有关示例，请参阅 Tune and Validate Gain-Scheduled PID Autotuning Results。

### **基线被控对象模型** — Bode 图的基线模型 `[]`（默认） | LTI 模型

*自 R2024b 起*

指定要与估计频率响应一起绘制的基线模型。使用 LTI 模型，例如 `tf`、`ss` 或 `frd` 模型。

**示例：** `tf(10,[1 10 1000])`

#### 依赖关系

要启用此参数，请选择 **显示 Bode 图**。

### **显示增益曲面图** — 显示增益曲面图 `off`（默认） | `on`

*自 R2024b 起*

选择此项可显示您整定的每个增益相对于调度变量的增益值绘图。您可以将模块配置为在整定每个断点后或在仿真结束时更新绘图。

要在整定前绘制初始增益值，请选择 **使用增益初始条件绘制基线增益数组**。您在 **增益调度** 选项卡上指定基线增益值。

有关示例，请参阅 Tune and Validate Gain-Scheduled PID Autotuning Results。

## 所属库

Simulink Control Design / Autotuning

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2024b：使用频率响应和增益曲面图验证自动整定结果

现在，您可以使用 Gain-Scheduled PID Autotuner 模块参数中新增的 **可视化** 选项卡来验证增益调度 PID 自动整定结果。该模块允许您可视化控制回路的频率响应图，例如估计被控对象、开环、控制器作用、参考跟踪和扰动抑制响应。该模块显示您整定的每个工作点的响应。此外，您还可以绘制指定调度变量的增益曲面。

当您想根据估计被控对象验证实际被控对象的响应时，可视化控制回路的频率响应会很有帮助。这样做可以让您调整自动整定设置，以获得更准确的性能。

## 描述

在多个工作点自动整定 PID 增益

使用 **Autotuning** 库中的新 Gain-Scheduled PID Autotuner 模块，基于从闭环实验估计的被控对象频率响应，在多个工作点自动整定 PID 增益。整定工作流与 Closed-Loop PID Autotuner 模块类似，并且该模块允许您指定其他选项来设置增益调度，例如断点和调度变量。该模块对每个工作点依次执行整定。当自动整定完成后，该模块允许您基于调度变量和断点数据存储和查找 PID 增益值，并将其写入 PID 控制器，而无需停止仿真。
