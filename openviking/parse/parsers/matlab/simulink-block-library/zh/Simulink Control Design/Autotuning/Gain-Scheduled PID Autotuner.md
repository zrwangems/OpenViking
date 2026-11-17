---
type: simulink-block
title: 'Gain-Scheduled PID Autotuner'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Autotuning'
documentation_page: 'gainscheduledpidautotuner'
documentation_source_path: 'ug/gainscheduledpidautotuner.html'
language: zh-CN
chinese_source: worker-translation
---

# Gain-Scheduled PID Autotuner

## 端口
```yaml
ports:
- name: u
  summary: 来自控制器的信号 标量
  direction: input
  data_types: single | double
- name: y
  summary: 被控对象输出 标量
  direction: input
  data_types: single | double
- name: start/stop
  summary: 启动和停止自整定实验 标量
  direction: input
  data_types: single | double
- name: bandwidth
  summary: 整定目标带宽 标量
  direction: input
  data_types: single | double
- name: target PM
  summary: 整定目标相位裕度 标量
  direction: input
  data_types: single | double
- name: signal Amp
  summary: 注入扰动信号的幅值 标量 | 向量
  direction: input
  data_types: single | double
- name: scheduling Variable
  summary: 调度变量 标量
  direction: input
- name: Breakpoints
  summary: 断点数据向量
  direction: input
- name: Update Trigger
  summary: 触发控制信号标量
  direction: input
- name: u+Δu
  summary: 被控对象输入信号标量
  direction: output
  data_types: single | double
- name: Δu
  summary: 被控对象输入扰动标量
  direction: output
  data_types: single | double
- name: pid gains
  summary: 整定后的 PID 系数总线
  direction: output
  data_types: single | double
- name: estimated PM
  summary: 使用整定后控制器的估计相位裕度标量
  direction: output
- name: frd
  summary: 估计的频率响应向量
  direction: output
```

### 输入

### **u** — 来自控制器的信号 标量

将此模块插入您的系统中，使该端口接受来自信号源的控制信号。通常，该端口接受来自系统中 PID 控制器的信号。

**数据类型：** `single` | `double`

### **y** — 被控对象输出 标量

将此端口连接到被控对象输出。

**数据类型：** `single` | `double`

### **start/stop** — 启动和停止自整定实验 标量

要启动和停止自整定过程，请在 `start/stop` 端口提供信号。当该信号的值从以下情况变化时：

- 负值或零变为正值，实验启动
- 正值变为负值或零，实验停止

当实验未运行时，模块将信号从 **u** 原样传递到 **u+Δu**。在此状态下，模块对被控对象或控制器行为没有影响。

通常，您可以使用从 0 变为 1 的信号来启动实验，使用从 1 变为 0 的信号来停止实验。配置 **start/stop** 信号时需要考虑的几点包括：

- 在被控对象处于期望的平衡工作点时启动实验。使用初始控制器将被控对象驱动到工作点。如果没有初始控制器（仅开环整定），可以使用连接到 **u** 的源模块将被控对象驱动到工作点。
- 在实验期间避免对被控对象施加任何负载扰动。负载扰动会扭曲被控对象输出，降低频率响应估计的精度。
- 让实验运行足够长的时间，使算法能够在其探测的所有频率上收集足够的数据以获得良好的估计。

  对于 **Sinestream** 和 **Superposition** 模式，有两种方法可以确定何时停止实验：

  - 提前确定实验持续时间。实验持续时间的保守估计为叠加实验模式下的 200/*ωc* 或正弦流实验模式下的 550/*ωc*，其中 *ωc* 是您的目标带宽。
  - 观察 `% conv` 输出处的信号，当信号稳定在接近 100% 时停止实验。

  对于 **PRBS** 模式，根据指定的 **Target bandwidth** 和 **Controller sample time** 值，模块对话框会在 **Experiment** 选项卡的 **Description** 部分显示推荐的实验长度。过早停止实验可能导致不正确的整定结果。
- 当您停止实验时，模块会计算整定后的 PID 增益并更新 `pid gains` 端口处的信号。

您可以配置适合您应用的任何逻辑来控制实验的启动和停止时间。

**数据类型：** `single` | `double`

### **bandwidth** — 整定目标带宽 标量

为 `Target bandwidth (rad/sec)` 参数提供一个值。有关详细信息，请参阅该参数。

#### 依赖关系

要启用此端口，请在 Tuning 选项卡中，在 `Target bandwidth (rad/sec)` 旁边选择 **Use external source**。

**数据类型：** `single` | `double`

### **target PM** — 整定目标相位裕度 标量

为 `Target phase margin (degrees)` 参数提供一个值。有关详细信息，请参阅该参数。

#### 依赖关系

要启用此端口，请在 Tuning 选项卡中，在 `Target phase margin (degrees)` 旁边选择 **Use external source**。

**数据类型：** `single` | `double`

### **signal Amp** — 注入扰动信号的幅值 标量 | 向量

为 `Signal Amplitudes` 参数提供一个值。有关详细信息，请参阅该参数。

#### 依赖关系

要启用此端口，请在 Experiment 选项卡中，在 `Signal Amplitudes` 旁边选择 **Use external source**。

**数据类型：** `single` | `double`

### **scheduling Variable** — 调度变量 标量

指定调度变量。此信号指示系统在给定时刻处于工作范围内的位置。查找表使用此信号来确定 PID 增益的值。

### **Breakpoints** — 断点数据向量

用于增益调度的断点数据，指定为向量。

#### 依赖

要启用此端口，请选择 **Use external signal**。

### **Update Trigger** — 触发控制信号标量

用于触发增益更新的控制信号。

#### 依赖

要启用此端口，请将 **Method to trigger gain update** 设置为
**External trigger**。
### 输出

### **u+Δu** — 被控对象输入信号标量

将此模块插入系统中，使此端口将输入信号馈送到被控对象。

- 当实验正在运行（`start/stop` 为正）时，模块在此端口向被控对象注入测试信号。如果您有任何保护被控对象的饱和或速率限制，请将来自 **u+Δu** 的信号馈入其中。
- 当实验未运行（`start/stop` 为零或负）时，模块将信号从 **u** 原样传递到 **u+Δu**。

#### 依赖

要启用此端口，请在 **Output Signal Configuration** 中选择
**control + perturbation**。

**数据类型：** `single` | `double`

### **Δu** — 被控对象输入扰动标量

模块在此端口生成扰动信号。通常，您通过求和模块从此端口注入扰动。

- 当实验正在运行（**start/stop** 为正）时，模块在此端口生成扰动信号。
- 当实验未运行（**start/stop** 为零或负）时，此端口处的信号为零。在此状态下，模块对被控对象没有影响。

#### 依赖

要启用此端口，请在 **Output Signal Configuration** 中选择
**perturbation only**。

**数据类型：** `single` | `double`

### **pid gains** — 整定后的 PID 系数总线

此 4 元素总线信号包含整定后的 PID 增益 *P*、
*I*、*D* 以及滤波器系数
*N*。这些值对应于 `Form` 参数中所给表达式中的 `P`、
`I`、`D` 和 `N` 参数。初始时，这些值分别为 0、0、0 和 100。模块在实验结束时更新这些值。此总线信号始终有四个元素，即使您并未整定 PIDF 控制器。

**数据类型：** `single` | `double`

### **estimated PM** — 使用整定后控制器的估计相位裕度标量

此端口输出整定后控制器所达到的估计相位裕度，以度为单位。模块在整定实验结束时更新此值。估计相位裕度根据
*G*(*jωc*)*C*(*jωc*)
的相角计算，其中 *G* 是估计的被控对象，*C* 是整定后的
控制器，*ωc* 是穿越频率（带宽）。估计相位裕度可能与 `Target phase margin (degrees)` 参数指定的目标相位
裕度不同。它是整定后系统所达到的鲁棒性和稳定性的指标。

- 通常，估计相位裕度接近目标相位裕度。一般来说，该值越大，整定后系统越鲁棒，超调越少。
- 负相位裕度表示闭环系统可能不稳定。

#### 依赖

要启用此端口，请在 Tuning 选项卡中，选择 **Output estimated phase
margin achieved by tuned controller**。

### **frd** — 估计的频率响应向量

该端口输出实验估计的频率响应数据。
初始时，`frd` 处的值为 [0, 0, 0, 0, 0]。在实验过程中，该模块在频率 [1/10, 1/3, 1, 3, 10]*ωc* 处注入信号，其中 *ωc* 是目标带宽。在实验期间的每个采样时间，该模块用包含这些频率处复数频率响应的向量分别更新 `frd`。对于正弦流和叠加信号，你可以使用响应的进展作为 `% conv` 的替代，以检查估计的收敛性。当实验停止时，该模块用用于计算 PID 增益的最终估计频率响应更新 `frd`。

对于 **PRBS** 实验模式，该端口处的信号仅在估计实验完成后更新。

#### 依赖关系

要启用此端口，请在实验选项卡中，选择 **Plant frequency responses near bandwidth**。
## 参数
```yaml
parameters:
- name: Controller type
  summary: PID 控制器动作 PIDN（默认）| P | I | PI | PD | PDN | PID | ...
  group: 控制器设置
- name: Form
  summary: PID 控制器形式 Parallel（默认）| Ideal
  group: 控制器设置
- name: Sample time (-1 for inherited)
  summary: PID 控制器的采样时间 0.1（默认）| 正标量 | –1
  group: 控制器设置
- name: Data Type
  summary: 浮点精度 double（默认）| single
  group: 控制器设置
- name: Tune at different sample time
  summary: 启用与 PID 控制器不同的采样时间下的整定和实验 off（默认）| on
  group: Autotuner 选项卡
- name: Tuning sample time (sec)
  summary: 整定算法的采样时间 0.2（默认）| 正标量
  group: Autotuner 选项卡
- name: Integrator method
  summary: 积分项的离散积分公式 Forward Euler（默认）| Backward Euler | Trapezoidal
  group: Autotuner 选项卡
- name: Filter method
  summary: 微分滤波器项的离散积分公式 Forward Euler（默认）| Backward Euler | Trapezoidal
  group: Autotuner 选项卡
- name: 目标带宽 (rad/sec)
  summary: 整定后响应的目标穿越频率 1（默认）| 正标量
  group: Autotuner 选项卡
- name: 目标相位裕度 (degrees)
  summary: 开环响应的目标最小相位裕度 60（默认）| 范围 0–90 内的标量
  group: Autotuner 选项卡
- name: Experiment Mode
  summary: 扰动信号类型 Superposition（默认）| Sinestream | PRBS
  group: Autotuner 选项卡
- name: Plant Type
  summary: 被控对象稳定性 Stable（默认）| Integrating
  group: Autotuner 选项卡
- name: Plant Sign
  summary: 被控对象符号 Positive（默认）| Negative
  group: Autotuner 选项卡
- name: Signal Amplitudes
  summary: 扰动幅度 1（默认）| 标量 | 长度为 5 的向量
  group: Autotuner 选项卡
- name: Breakpoints
  summary: 增益调度断点 [1 2 3]（默认）| 向量
  group: Gain Scheduling Tab
- name: Use external signal
  summary: 从输入端口指定断点 off（默认）| on
  group: Gain Scheduling Tab
- name: Number of breakpoints
  summary: 断点数量 3（默认）| 正标量
  group: Gain Scheduling Tab
- name: Gain index tolerance
  summary: 增益索引容差 1e-3（默认）| 非负标量
  group: Gain Scheduling Tab
- name: Use y as scheduling variable
  summary: 使用被控对象输出调度断点 on（默认）| off
  group: Gain Scheduling Tab
- name: Method of storing gains
  summary: 存储增益的方法 Internal to block（默认）| Data store memory
  group: Gain Scheduling Tab
- name: P Gain initial conditions
  summary: 比例增益初始值 0（默认）| 标量 | 向量
  group: Gain Scheduling Tab
- name: P Gain Parameter Name
  summary: 比例增益数据名称 PGain（默认）| 字符串
  group: Gain Scheduling Tab
- name: I Gain initial conditions
  summary: 积分增益初始值 0（默认）| 标量 | 向量
  group: Gain Scheduling Tab
- name: I Gain Parameter Name
  summary: 积分增益数据名称 IGain（默认）| 字符串
  group: Gain Scheduling Tab
- name: D Gain initial conditions
  summary: 微分增益初始值 0（默认）| 标量 | 向量
  group: Gain Scheduling Tab
- name: D Gain Parameter Name
  summary: 微分增益数据名称 DGain（默认）| 字符串
  group: Gain Scheduling Tab
- name: N Gain initial conditions
  summary: 滤波器增益初始值 100（默认）| 标量 | 向量
  group: Gain Scheduling Tab
- name: N Gain Parameter Name
  summary: 滤波器增益数据名称 NGain（默认）| 字符串
  group: Gain Scheduling Tab
- name: Save breakpoints in gain array
  summary: 将断点与 PID 增益一起保存 off（默认）| on
  group: Gain Scheduling Tab
- name: Method to trigger gain update
  summary: 更新触发方法 Detect change in PID gains（默认）| External trigger
  group: Gain Scheduling Tab
- name: Number of samples to delay update
  summary: 延迟更新的采样数 1（默认）| 非负标量
  group: Gain Scheduling Tab
- name: P gain lookup method
  summary: 比例增益查找方法 Interpolation-Use End Values（默认）| Interpolation-Extrapolation | Use Input Nearest | Use Input Below |
    Use Input Above
  group: Gain Scheduling Tab
- name: I gain lookup method
  summary: 积分增益查找方法 Interpolation-Use End Values（默认）| Interpolation-Extrapolation | Use Input Nearest | Use Input Below |
    Use Input Above
  group: Gain Scheduling Tab
- name: D gain lookup method
  summary: 微分增益查找方法 Interpolation-Use End Values（默认）| Interpolation-Extrapolation | Use Input Nearest | Use Input Below |
    Use Input Above
  group: Gain Scheduling Tab
- name: N gain lookup method
  summary: 微分滤波器增益查找方法 Interpolation-Use End Values（默认）| Interpolation-Extrapolation | Use Input Nearest | Use Input Below
    | Use Input Above
  group: Gain Scheduling Tab
- name: Saturate to max or min when overflows occur
  summary: 溢出时的处理方式 off（默认）| on
  group: Gain Scheduling Tab
- name: 锁定输出数据类型设置以防止定点工具更改
  summary: 防止定点工具覆盖输出数据类型 off（默认）| on
  group: Gain Scheduling Tab
- name: 整数舍入模式
  summary: 定点运算的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: Gain Scheduling Tab
- name: 输出信号配置
  summary: 提供控制信号加扰动或仅扰动 control action + perturbation（默认）| perturbation only
  group: 模块选项卡
- name: 显示 Bode 图
  summary: 绘制估计频率响应 off（默认）| on
  group: 可视化选项卡
- name: 基线被控对象模型
  summary: Bode 图的基线模型 []（默认）| LTI 模型
  group: 可视化选项卡
- name: 显示增益曲面图
  summary: 显示增益曲面图 off（默认）| on
  group: 可视化选项卡
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### 控制器设置

### **Controller type** — PID 控制器动作 `PIDN`（默认）| `P` | `I` | `PI` | `PD` | `PDN` | `PID` | ...

指定系统中 PID 控制器的类型。控制器类型指示控制器中存在哪些动作。以下控制器类型可用于 PID 自整定：

- `P` — 仅比例
- `I` — 仅积分
- `PI` — 比例和积分
- `PD` — 比例和微分
- `PDN` — 带微分滤波器的比例和微分
- `PID` — 比例、积分和微分
- `PIDN` — 带微分滤波器的比例、积分和微分

控制器类型必须与你正在整定的 PID 控制器匹配。

### **Form** — PID 控制器形式 `Parallel`（默认）| `Ideal`

指定控制器形式。控制器形式决定 PID 系数 *P*、*I*、*D* 和 *N* 的解释。

- `Parallel` — 在 `Parallel` 形式中，离散时间 PIDF 控制器的传递函数为：

  C=P+IFi(z)+D[N1+NFd(z)]，

  其中 *Fi*(*z*) 和 *Fd*(*z*) 是积分器和滤波器公式（参见 `Integrator method` 和 `Filter method`）。连续时间并联形式 PIDF 控制器的传递函数为：

  C=P+I(1s)+D(Nss+N)。

  其他控制器动作相当于将 *P*、*I* 或 *D* 设置为零。
- `Ideal` — 在 `Ideal` 形式中，离散时间 PIDF 控制器的传递函数为：

  C=P[1+IFi(z)+D(N1+NFd(z))]。

  连续时间理想形式 PIDF 控制器的传递函数为：

  C=P[1+I(1s)+D(Nss+N)]。

  其他控制器动作相当于将 *D* 设置为零或将 *I* 设置为 `Inf`。（在理想形式中，控制器必须具有比例动作。）

控制器形式必须与你正在整定的 PID 控制器匹配。

**可调：** 是

### **Sample time (-1 for inherited)** — PID 控制器的采样时间 0.1（默认）| 正标量 | –1

指定 PID 控制器的采样时间，以秒为单位。此值还设置该模块执行实验的采样时间。

要执行 PID 整定，该模块测量高达目标带宽 10 倍频率的频率响应信息。为确保此频率小于奈奎斯特频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* *ωc* 是你使用 **Sample time** 参数指定的控制器采样时间。

当你使用整定后的参数值更新 PID Controller 模块或自定义 PID 控制器时，请确保控制器采样时间匹配。

#### 提示

如果要在应用程序中以不同的采样时间运行部署的模块，请将此参数设置为 –1，并将该模块放入 Triggered Subsystem 中。然后，以所需的采样时间触发该子系统。如果部署后不打算更改采样时间，请指定一个固定且有限的采样时间。

### **Data Type** — 浮点精度 `double`（默认）| `single`

根据仿真环境或硬件要求指定浮点精度。

### Autotuner 选项卡

### **Tune at different sample time** — 启用与 PID 控制器不同的采样时间下的整定和实验 `off`（默认）| `on`

启用此参数以在与所整定的 PID 控制器的采样率以及该模块执行的频率响应估计实验不同的采样率下运行整定。PID 增益整定算法计算量大，当您要将模块部署到硬件并以快速采样时间整定控制器时，某些硬件可能无法在单个时间步内完成 PID 增益计算。为降低硬件吞吐量要求，请使用 **Tuning sample time** 参数指定比控制器采样时间更慢的整定采样时间。

### **Tuning sample time (sec)** — 整定算法的采样时间 0.2（默认）| 正标量

以秒为单位指定整定算法的采样时间。

如果您打算将模块部署到处理能力有限的硬件上，并希望以快速采样时间整定控制器，请指定一个使整定算法以比所整定的 PID 控制器更慢的速率运行的采样时间。

#### 依赖关系

要启用此参数，请选择 **Tune at different sample time**。

### **Integrator method** — 积分项的离散积分公式 `Forward Euler`（默认）| `Backward Euler` | `Trapezoidal`

指定控制器中积分项的离散积分公式。在离散时间下，该模块所假设的 PID 控制器传递函数为：

C=P+IFi(z)+D[N1+NFd(z)]，

为并联形式，或为理想形式，

C=P[1+IFi(z)+D(N1+NFd(z))]。

对于控制器采样时间 *Ts*，`Integrator method` 参数按如下方式确定公式 *Fi*：

| Integrator method | *Fi* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优势的更多信息，请参阅 Discrete PID Controller 模块参考页。

**Tunable:** Yes

### **Filter method** — 微分滤波器项的离散积分公式 `Forward Euler`（默认）| `Backward Euler` | `Trapezoidal`

指定控制器中微分滤波器项的离散积分公式。在离散时间下，该模块所假设的 PID 控制器传递函数为：

C=P+IFi(z)+D[N1+NFd(z)]，

为并联形式，或为理想形式，

C=P[1+IFi(z)+D(N1+NFd(z))]。

对于控制器采样时间 *Ts*，`Filter method` 参数按如下方式确定公式 *Fd*：

| Filter method | *Fd* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优势的更多信息，请参阅 Discrete PID Controller 模块参考页。

**Tunable:** Yes

### **目标带宽 (rad/sec)** — 整定后响应的目标穿越频率 1（默认）| 正标量

目标带宽，以 rad/sec 为单位指定，是整定后开环响应 *CP* 的 0 dB 增益穿越频率的目标值，其中 *P* 是被控对象响应，*C* 是控制器响应。该穿越频率大致设定了控制带宽。对于上升时间 *τ* 秒，目标带宽的一个良好估计值是 2/*τ* rad/sec。

要执行 PID 整定，autotuner 模块会测量高达目标带宽 10 倍频率处的频率响应信息。为确保该频率小于奈奎斯特频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* 是您通过 **Sample time** 参数指定的控制器采样时间。由于这一条件，您可以为整定强制的最快上升时间约为 6.67*Ts*。如果该上升时间不满足您的设计目标，请考虑减小 *Ts*。

为获得闭环整定的最佳结果，请使用与初始 PID 控制器的带宽相差约 10 倍以内的目标带宽。要为带宽的更大变化整定控制器，请使用较小的变化逐步整定。

要通过输入端口提供目标带宽，请选择 **Use external source**。

### **目标相位裕度 (degrees)** — 开环响应的目标最小相位裕度 60（默认）| 范围 0–90 内的标量

指定整定后开环响应在穿越频率处的目标最小相位裕度。目标相位裕度反映了整定系统的期望鲁棒性。通常，选择约 45°–60° 范围内的值。一般来说，更高的相位裕度可改善超调，但可能限制响应速度。默认值 60° 倾向于平衡性能和鲁棒性，根据您被控对象的特性，产生约 5–10% 的超调。

要通过输入端口提供目标相位裕度，请选择 **Use external source**。

**可调：** 是

### **Experiment Mode** — 扰动信号类型 **Superposition**（默认）| **Sinestream** | **PRBS**

指定每个频率处的扰动是按顺序正弦（**Sinestream**）、同时正弦（**Superposition**）还是伪随机二进制序列（**PRBS**）施加。

- **Sinestream** — 在此模式下，模块在每个频率处分别施加扰动。有关用于估计的 sinestream 信号的详细信息，请参阅 Sinestream Input Signals。
- **Superposition** — 在此模式下，扰动信号一次性包含所有指定频率。对于在频率向量 *ω* = [*ω*1, … , *ωN*] 处以幅值 *A* = [*A*1, … , *AN*] 进行频率响应估计，扰动信号为：

  Δu=∑iAisin(ωit)。
- **PRBS** — 一种确定性伪随机二进制序列，在两个值之间切换，并具有类似白噪声的特性。与使用 sinestream 输入信号相比，PRBS 信号可减少总估计时间，同时产生可比的估计结果。PRBS 信号可用于估计通信和电力电子系统的频率响应。有关详细信息，请参阅 PRBS Input Signals。

**Sinestream** 模式可能更准确，也可能更少侵入，因为扰动的总大小永远不会大于 **Signal Amplitudes** 参数指定的值。然而，由于 sinestream 扰动的顺序性质，您添加的每个频率点都会增加推荐的实验时间（有关详细信息，请参阅 **start/stop** 输入端口）。因此，估计实验在 **Superposition** 模式下通常要快得多，且结果令人满意。

与 superposition 输入信号相比，sinestream 信号减少了执行时间，但估计频率响应也需要更长时间。当您的处理能力有限且希望减少执行时间时，使用 sinestream 信号进行频率响应估计很有用。

为覆盖相似的频率范围，**PRBS** 模式下的实验时长通常比其他两种模式短得多。然而，结果的速度和质量之间存在权衡。

### **Plant Type** — 被控对象稳定性 `Stable`（默认）| `Integrating`

指定被控对象是稳定还是积分。如果被控对象具有一个或多个积分器，请选择 `Integrating`。

### **Plant Sign** — 被控对象符号 `Positive`（默认）| `Negative`

指定被控对象是正还是负。如果在标称工作点处被控对象输入的正变化导致被控对象输出的正变化，请指定 `Positive`。否则，请指定 negative。对于稳定被控对象，被控对象的符号是被控对象直流增益的符号。

### **Signal Amplitudes** — 扰动幅度 1（默认）| 标量 | 长度为 5 的向量

在实验过程中，该模块以频率 [1/10, 1/3, 1, 3, 10]*ωc* 向被控对象注入扰动信号，其中 *ωc* 是整定的目标带宽。使用 **Signal Amplitudes** 指定每个注入信号的幅度。指定：

- 标量值以在每个频率注入相同的幅度
- 长度为 5 的向量以在 [1/10, 1/3, 1, 3, 10]*ωc* 的每个频率指定不同的幅度

在具有典型目标带宽的典型被控对象中，实验频率处被控对象响应的幅值不会变化很大。在这种情况下，您可以使用标量值在所有频率处施加相同幅值的扰动。但是，如果您知道响应在频率范围内急剧衰减，请考虑减小低频输入的幅度并增大高频输入的幅度。当所有被控对象响应具有可比幅值时，估计实验在数值上会更好。

扰动幅度必须：

- 足够大，使扰动能够克服被控对象执行器中的任何死区，并产生高于噪声水平的响应
- 足够小，使被控对象在标称工作点附近的近似线性区域内运行，并避免使被控对象输入或输出饱和

当 **Experiment mode** 为 **Superposition** 时，正弦信号会叠加。因此，扰动至少可以与所有幅度之和一样大。确保最大可能的扰动在被控对象执行器的范围内。使执行器饱和可能会在估计的频率响应中引入误差。

要通过输入端口提供信号幅度，请选择 **Use external source**。

**Tunable:** Yes

### Gain Scheduling Tab

### **Breakpoints** — 增益调度断点 `[1 2 3]`（默认）| 向量

指定增益调度断点数据。

### **Use external signal** — 从输入端口指定断点 `off`（默认）| `on`

从模块输入端口指定断点。

### **Number of breakpoints** — 断点数量 `3`（默认）| 正标量

指定外部断点信号中的断点数量。

#### 依赖关系

要启用此参数，请选择 **Use external signal**。

### **Gain index tolerance** — 增益索引容差 `1e-3`（默认）| 非负标量

指定调度变量与断点之间的容差。为了确定要更新数组中的哪个断点，该模块将调度变量与断点数组进行比较，并使用此容差值来确定最接近的值。

### **Use y as scheduling variable** — 使用被控对象输出调度断点 `on`（默认）| `off`

选择此选项以使用被控对象输出 **y** 调度断点。

### **Method of storing gains** — 存储增益的方法 `Internal to block`（默认）| `Data store memory`

指定存储增益的方法。

- `Internal to block` — 使用 **PID Gains Out** 输出端口。您可以将此输出信号直接馈入 PID Gain Scheduler 模块。
- `Data store memory` — 使用 Data Store Memory 模块存储增益。要创建数据存储模块，首先使用每个增益的 **Parameter Name** 参数指定数据存储的名称，然后单击 **Add Data Store Memory blocks to model** 按钮。该模块会在模型的顶层创建 Data Store Memory 模块。您可以使用 PID Controller 指定这些数据存储名称，以执行基于查找表的增益调度。

使用 **Gain initial conditions** 参数指定增益的初始值。当整定后的增益不可用时，该模块使用初始值。

### **P Gain initial conditions** — 比例增益初始值 `0`（默认）| 标量 | 向量

将比例增益的初始值指定为标量或向量。当来自外部来源（如 Closed-Loop PID Autotuner）的整定增益数据不可用时，模块使用此值。

- 标量 — 模块对所有断点使用此值。
- 向量 — 指定一个与 **Breakpoints** 长度相同的向量。模块使用与当前断点对应的索引处的初始值。

#### 依赖关系

要启用此端口，请将 **Controller type** 设置为具有比例作用的控制器类型。

### **P Gain Parameter Name** — 比例增益数据名称 `PGain`（默认）| 字符串

指定比例增益数据的数据存储名称。

#### 依赖关系

要启用此参数，请设置

- **Controller type** 为具有比例作用的控制器类型。
- **Method of obtaining gains** 为 `Data store memory`。

### **I Gain initial conditions** — 积分增益初始值 `0`（默认）| 标量 | 向量

将积分增益的初始值指定为标量或向量。当来自外部来源的整定增益数据不可用时，模块使用此值。

- 标量 — 模块对所有断点使用此值。
- 向量 — 指定一个与 **Breakpoints** 长度相同的向量。模块使用与当前断点对应的索引处的初始值。

#### 依赖关系

要启用此参数，请将 **Controller type** 设置为具有积分作用的控制器类型。

### **I Gain Parameter Name** — 积分增益数据名称 `IGain`（默认）| 字符串

指定积分增益数据的数据存储名称。

#### 依赖关系

要启用此参数，请设置

- **Controller type** 为具有积分作用的控制器类型。
- **Method of obtaining gains** 为 `Data store memory`。

### **D Gain initial conditions** — 微分增益初始值 `0`（默认）| 标量 | 向量

将微分增益的初始值指定为标量或向量。当来自外部来源的整定增益数据不可用时，模块使用此值。

- 标量 — 模块对所有断点使用此值。
- 向量 — 指定一个与 **Breakpoints** 长度相同的向量。模块使用与当前断点对应的索引处的初始值。

#### 依赖关系

要启用此参数，请将 **Controller type** 设置为具有微分作用的控制器类型。

### **D Gain Parameter Name** — 微分增益数据名称 `DGain`（默认）| 字符串

指定微分增益数据的数据存储名称。

#### 依赖关系

要启用此参数，请设置

- **Controller type** 为具有微分作用的控制器类型。
- **Method of obtaining gains** 为 `Data store memory`。

### **N Gain initial conditions** — 滤波器增益初始值 `100`（默认）| 标量 | 向量

将微分滤波器增益的初始值指定为标量或向量。当来自外部来源的整定增益数据不可用时，模块使用此值。

- 标量 — 模块对所有断点使用此值。
- 向量 — 指定一个与 **Breakpoints** 长度相同的向量。模块使用与当前断点对应的索引处的初始值。

#### 依赖关系

要启用此参数，请将 **Controller type** 设置为具有滤波微分作用的控制器类型。

### **N Gain Parameter Name** — 滤波器增益数据名称 `NGain`（默认）| 字符串

指定微分滤波器增益数据的数据存储名称。

#### 依赖关系

要启用此参数，请设置：

- **Controller type** 为具有滤波微分作用的控制器类型。
- **Method of obtaining gains** 为 `Data store memory`。

### **Save breakpoints in gain array** — 将断点与 PID 增益一起保存 `off`（默认）| `on`

使用此选项可将断点与存储的增益数组一起保存。PID Gain Scheduler 模块可以解释此组合数据，以用于增益调度应用。

#### 依赖关系

要启用此参数，请将 **Method of obtaining gains** 设置为 `Data store memory`。

### **Method to trigger gain update** — 更新触发方法 **Detect change in PID gains**（默认）| **External trigger**

指定触发增益更新的方法。

- **Detect change in PID gains** — 当输入增益发生变化时自动更新增益。
- **External trigger** — 使用外部信号触发增益更新。

### **Number of samples to delay update** — 延迟更新的采样数 `1`（默认）| 非负标量

在触发事件之后延迟增益更新的采样数。使用此选项可延迟更新增益，以便为自整定算法留出足够的时间来计算增益。

#### 查找表设置

### **P gain lookup method** — 比例增益查找方法 `Interpolation-Use End Values`（默认）| `Interpolation-Extrapolation` | `Use Input Nearest` | `Use Input Below` | `Use Input Above`

该模块通过将您选择的查找方法应用于断点数据（**Breakpoints**）和表数据（**PID Gains**）的输入向量来计算输出。有关详细信息，请参阅 How the Block Generates Output。

#### 依赖关系

要启用此参数，请将 **Controller type** 设置为具有比例作用的控制器类型。

### **I gain lookup method** — 积分增益查找方法 `Interpolation-Use End Values`（默认）| `Interpolation-Extrapolation` | `Use Input Nearest` | `Use Input Below` | `Use Input Above`

该模块通过将您选择的查找方法应用于断点数据（**Breakpoints**）和表数据（**PID Gains**）的输入向量来计算输出。有关详细信息，请参阅 How the Block Generates Output。

#### 依赖关系

要启用此参数，请将 **Controller type** 设置为具有积分作用的控制器类型。

### **D gain lookup method** — 微分增益查找方法 `Interpolation-Use End Values`（默认）| `Interpolation-Extrapolation` | `Use Input Nearest` | `Use Input Below` | `Use Input Above`

该模块通过将您选择的查找方法应用于断点数据（**Breakpoints**）和表数据（**PID Gains**）的输入向量来计算输出。有关详细信息，请参阅 How the Block Generates Output。

#### 依赖关系

要启用此端口，请将 **Controller type** 设置为具有微分作用的控制器类型。

### **N gain lookup method** — 微分滤波器增益查找方法 `Interpolation-Use End Values`（默认）| `Interpolation-Extrapolation` | `Use Input Nearest` | `Use Input Below` | `Use Input Above`

该模块通过将您选择的查找方法应用于断点数据（**Breakpoints**）和表数据（**PID Gains**）的输入向量来计算输出。有关详细信息，请参阅 How the Block Generates Output。

#### 依赖关系

要启用此参数，请将 **Controller type** 设置为具有滤波微分的控制器类型。

### **Saturate to max or min when overflows occur** — 溢出时的处理方式 `off`（默认）| `on`

当您选中此复选框时，溢出会饱和到该数据类型所能表示的最大值或最小值。否则，溢出会回绕。

当您选中此复选框时，饱和会应用于模块上的每个内部运算，而不仅仅是输出或结果。通常，代码生成过程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

### **锁定输出数据类型设置以防止定点工具更改** — 防止定点工具覆盖输出数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在模块上指定的 **Output** 数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

### **整数舍入模式** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

### 模块选项卡

### **输出信号配置** — 提供控制信号加扰动或仅扰动 **control action + perturbation**（默认）| **perturbation only**

默认情况下，该模块将控制信号作为输入，并在端口 **u+Δu** 处提供控制信号加实验扰动。然后，您将此信号直接馈入被控对象输入。

此默认配置需要在控制器和被控对象之间插入该模块。如果您想自行将扰动信号添加到控制信号中，请选择 **perturbation only**。在此配置中，模块输出仅包含扰动信号，位于端口 **Δu**。您使用求和模块将此扰动信号注入被控对象，并与 PID 控制器输出 **u** 相加。

### 可视化选项卡

### **显示 Bode 图** — 绘制估计频率响应 `off`（默认）| `on`

*自 R2024b 起*

选择此项可生成 Bode 图，显示您调节的每个工作点的以下估计频率响应：

- 被控对象响应
- 开环响应
- 参考跟踪响应
- 控制器输出响应
- 输入扰动抑制响应
- 输出扰动抑制响应

您可以将模块配置为在调节每个断点后或在仿真结束时更新绘图。如果您有表示预期被控对象响应或其他相关基线的 LTI 模型，请使用 **Baseline plant model** 参数将其包含在绘图中以供参考。

有关示例，请参阅 Tune and Validate Gain-Scheduled PID Autotuning Results。

### **基线被控对象模型** — Bode 图的基线模型 `[]`（默认）| LTI 模型

*自 R2024b 起*

指定要与估计频率响应一起绘制的基线模型。使用 LTI 模型，例如 `tf`、`ss` 或 `frd` 模型。

**示例：** `tf(10,[1 10 1000])`

#### 依赖关系

要启用此参数，请选择 **Display Bode plot**。

### **显示增益曲面图** — 显示增益曲面图 `off`（默认）| `on`

*自 R2024b 起*

选择此项可显示您调节的每个增益值相对于调度变量的绘图。您可以将模块配置为在调节每个断点后或在仿真结束时更新绘图。

要在调节前绘制初始增益值，请选择 **Plot baseline gain array using gain initial conditions**。您在 **Gain scheduling** 选项卡上指定基线增益值。

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

您现在可以使用 Gain-Scheduled PID Autotuner 模块参数中新增的 **Visualization** 选项卡来验证增益调度 PID 自动整定结果。该模块允许您可视化控制回路的频率响应图，例如估计被控对象、开环、控制器输出、参考跟踪和扰动抑制响应。该模块显示您整定的每个工作点的响应。此外，您还可以绘制指定调度变量的增益曲面。

当您想要将实际被控对象的响应与估计被控对象进行验证时，可视化控制回路的频率响应会很有帮助。这样做可以让您调整自动整定设置，以获得更准确的性能。

## 描述

在多个工作点自动整定 PID 增益

使用 **Autotuning** 库中新增的 Gain-Scheduled PID Autotuner 模块，基于从闭环实验估计的被控对象频率响应，在多个工作点自动整定 PID 增益。整定工作流与 Closed-Loop PID Autotuner 模块类似，并且该模块允许您指定其他选项来设置增益调度，例如断点和调度变量。该模块对每个工作点依次执行整定。当自动整定完成后，该模块允许您基于调度变量和断点数据存储和查找 PID 增益值，并将它们写入 PID 控制器，而无需停止仿真。
