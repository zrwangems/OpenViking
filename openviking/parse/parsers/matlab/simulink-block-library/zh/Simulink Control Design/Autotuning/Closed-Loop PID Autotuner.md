---
type: simulink-block
title: 'Closed-Loop PID Autotuner'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Autotuning'
documentation_page: 'closedlooppidautotuner'
documentation_source_path: 'ug/closedlooppidautotuner.html'
language: zh-CN
chinese_source: worker-translation
---

# Closed-Loop PID Autotuner

## 端口

### 输入

### **u** — 来自控制器的信号 标量

将此模块插入系统中，使该端口接受来自信号源的控制信号。通常，该端口接受来自系统中 PID 控制器的信号。

**数据类型：** `single` | `double`

### **y** — 被控对象输出 标量

将此端口连接到被控对象输出。

**数据类型：** `single` | `double`

### **start/stop** — 启动和停止自整定实验 标量

要启动和停止自整定过程，请在 `start/stop` 端口提供信号。当信号值发生以下变化时：

- 从负值或零变为正值，实验启动
- 从正值变为负值或零，实验停止

当实验未运行时，模块将信号从 **u** 原样传递到 **u+Δu**。在此状态下，模块对被控对象或控制器行为没有影响。

通常，可以使用从 0 变为 1 的信号来启动实验，使用从 1 变为 0 的信号来停止实验。配置 **start/stop** 信号时需要考虑以下几点：

- 在被控对象处于期望的平衡工作点时启动实验。使用初始控制器将被控对象驱动到工作点。如果没有初始控制器（仅开环整定），可以使用连接到 **u** 的源模块将被控对象驱动到工作点。
- 在实验期间避免对被控对象施加任何负载扰动。负载扰动会扭曲被控对象输出，降低频率响应估计的精度。
- 让实验运行足够长的时间，使算法能够在其探测的所有频率上收集足够的数据以获得良好的估计。

  对于 **Sinestream** 和 **Superposition** 模式，有两种方法可以确定何时停止实验：

  - 提前确定实验持续时间。实验持续时间的保守估计为叠加实验模式下 200/*ωc*，正弦流实验模式下 550/*ωc*，其中 *ωc* 是目标带宽。
  - 观察 `% conv` 输出处的信号，当信号稳定在接近 100% 时停止实验。

  对于 **PRBS** 模式，根据指定的 **Target bandwidth** 和 **Controller sample time** 值，模块对话框会在 **Experiment** 选项卡的 **Description** 部分显示推荐的实验长度。过早停止实验可能导致不正确的整定结果。*（自 R2023b 起）*
- 停止实验时，模块计算整定后的 PID 增益并更新 `pid gains` 端口处的信号。

您可以配置适合您应用的任何逻辑来控制实验的启动和停止时间。

**数据类型：** `single` | `double`

### **bandwidth** — 用于整定的目标带宽 标量

为 `Target bandwidth (rad/sec)` 参数提供值。详见该参数。

#### 依赖关系

要启用此端口，请在 Tuning 选项卡中 `Target bandwidth (rad/sec)` 旁边选择 **Use external source**。

**数据类型：** `single` | `double`

### **target PM** — 用于整定的目标相位裕度 标量

为 `Target phase margin (degrees)` 参数提供值。详见该参数。

#### 依赖关系

要启用此端口，请在 Tuning 选项卡中 `Target phase margin (degrees)` 旁边选择 **Use external source**。

**数据类型：** `single` | `double`

### **signal Amp** — 注入扰动信号的幅值 标量 | 向量

为 `Signal Amplitudes` 参数提供值。详见该参数。

#### 依赖关系

要启用此端口，请在 Experiment 选项卡中 `Signal Amplitudes` 旁边选择 **Use external source**。

**数据类型：** `single` | `double`

### **isExpGood** — 禁用扰动和整定 标量

*自 R2025a 起*

当您在此输入提供值 1（true）时，闭环 PID 自整定模块正常输出实验（扰动）。如果值为 0（false），模块将扰动设置为零并且不执行整定。为了再次允许扰动和整定，您必须先将 **start/stop** 信号设置为 0，然后重新设置为 1 并启动新的实验。**isExpGood** 端口在其值为 false 时锁存，直到触发新的实验。

如果您的被控对象在闭环 PID 自整定模块下游具有信号限幅，由于扰动可能饱和，估计实验可能不准确。类似地，系统中的任何故障也可能导致实验不准确。您可以使用 **isExpGood** 提供一个信号来禁用扰动和整定。有关示例，请参阅 Disable PID Autotuning in Presence of Downstream Signal Limiting。

#### 依赖关系

要启用此端口，请在 **Block** 选项卡上，选择 **Use isExpGood port to disable perturbations and tuning**。

**数据类型：** `single` | `double`
### 输出

### **u+Δu** — 被控对象输入信号 标量

将模块插入您的系统，使此端口将输入信号馈送到您的被控对象。

- 当实验运行时（`start/stop` 为正），模块在此端口向被控对象注入测试信号。如果您有任何保护被控对象的饱和或速率限制，请将 **u+Δu** 的信号馈入其中。
- 当实验未运行时（`start/stop` 为零或负），模块将信号从 **u** 原样传递到 **u+Δu**。

#### 依赖关系

要启用此端口，请在 **Output Signal Configuration** 中，选择 **control + perturbation**。

**数据类型：** `single` | `double`

### **Δu** — 被控对象输入扰动 标量

模块在此端口生成扰动信号。通常，您通过求和模块从此端口注入扰动，如下图所示。

- 当实验运行时（**start/stop** 为正），模块在此端口生成扰动信号。
- 当实验未运行时（**start/stop** 为零或负），此端口处的信号为零。在此状态下，模块对被控对象没有影响。

#### 依赖关系

要启用此端口，请在 **Output Signal Configuration** 中，选择 **perturbation only**。

**数据类型：** `single` | `double`

### **% conv** — 实验期间 FRD 估计的收敛度 标量

当实验运行时（`start/stop` 为正），模块向被控对象注入测试信号并在 `y` 处测量被控对象响应。它使用这些信号来估计被控对象在目标带宽附近若干频率处的频率响应以进行整定。对于正弦流和叠加信号，`% conv` 表示被控对象频率响应估计的完成程度。通常，该值在实验开始后迅速上升至约 90%，然后逐渐收敛到更高的值。当它在接近 100% 处趋于平稳时停止实验。

对于 **PRBS** 实验模式，此端口处的信号仅在估计实验完成后更新。*（自 R2023b 起）*

**数据类型：** `single` | `double`

### **pid gains** — 整定后的 PID 系数 总线

此 4 元素总线信号包含整定后的 PID 增益 *P*、*I*、*D* 以及滤波器系数 *N*。这些值对应于 `Form` 参数中给出的表达式中的 `P`、`I`、`D` 和 `N` 参数。初始时，这些值分别为 0、0、0 和 100。模块在实验结束时更新这些值。此总线信号始终具有四个元素，即使您未整定 PIDF 控制器。

如果您有与此模块关联的 PID 控制器，您可以在实验结束后使用这些值更新该控制器。为此，请在 Block 选项卡中，点击 **Update PID Block**。

**数据类型：** `single` | `double`

### **estimated PM** — 使用整定控制器得到的估计相位裕度标量

此端口输出整定控制器所达到的估计相位裕度，单位为度。当整定实验结束时，模块会更新此值。估计相位裕度根据 *G*(*jωc*)*C*(*jωc*) 的相角计算，其中 *G* 是估计的被控对象，*C* 是整定后的控制器，*ωc* 是穿越频率（带宽）。估计相位裕度可能与 `Target phase margin (degrees)` 参数指定的目标相位裕度不同。它是整定后系统所达到的鲁棒性和稳定性的指标。

- 通常，估计相位裕度接近目标相位裕度。一般来说，该值越大，整定后的系统越鲁棒，超调越小。
- 负的相位裕度表明闭环系统可能不稳定。

#### 依赖关系

要启用此端口，请在 Tuning 选项卡中，选择 **Output estimated phase margin achieved by tuned controller**。

### **frd** — 估计的频率响应向量

此端口输出实验估计的频率响应数据。初始时，`frd` 处的值为 [0, 0, 0, 0, 0]。在实验过程中，模块在频率 [1/10, 1/3, 1, 3, 10]*ωc* 处注入信号，其中 *ωc* 是目标带宽。在实验期间的每个采样时刻，模块用包含分别在这些频率处的复数频率响应的向量更新 `frd`。对于正弦流和叠加信号，您可以使用响应的进展作为 `% conv` 的替代，以检查估计的收敛性。当实验停止时，模块用用于计算 PID 增益的最终估计频率响应更新 `frd`。

对于 **PRBS** 实验模式，此端口上的信号仅在估计实验完成后更新。*(自 R2023b 起)*

#### 依赖关系

要启用此端口，请在 Experiment 选项卡中，选择 **Plant frequency responses near bandwidth**。

### **nominal** — 标称工作点处的被控对象输入和输出向量

此端口输出一个向量，包含实验开始时被控对象的输入（**u+Δu**）和被控对象输出（**y**）。这些值是模块执行实验时所处的标称工作点处的被控对象输入和输出。

#### 依赖关系

要启用此端口，请在 Experiment 选项卡中，选择 **Plant nominal input and output**。

## 参数

#### Tuning Tab

### **Type** — PID 控制器动作 `PI`（默认）| `PID` | `PIDF` | ...

指定系统中 PID 控制器的类型。控制器类型指示控制器中存在哪些动作。以下控制器类型可用于 PID 自整定：

- `P` — 仅比例
- `I` — 仅积分
- `PI` — 比例和积分
- `PD` — 比例和微分
- `PDF` — 带微分滤波器的比例和微分
- `PID` — 比例、积分和微分
- `PIDF` — 带微分滤波器的比例、积分和微分

当您使用整定后的参数值更新 PID Controller 模块或自定义 PID 控制器时，请确保控制器类型匹配。

**Tunable:** Yes

#### 编程使用

|  |
| --- |
| **模块参数**：`PIDType` |
| **类型**：character vector |
| **值**：`'P'` | `'I'` | `'PI'` | `'PD'` | `'PDF'` | `'PID'` | `'PIDF'` |
| **默认值**：`'PI'` |

### **Form** — PID 控制器形式 `Parallel`（默认）| `Ideal`

指定控制器形式。控制器形式决定 PID 系数 *P*、*I*、*D* 和 *N* 的解释方式。

- `Parallel` — 在 `Parallel`
  形式中，离散时间 PIDF 控制器的传递函数为：

  C=P+IFi(z)+D[N1+NFd(z)]，

  其中 *Fi*(*z*) 和 *Fd*(*z*) 是积分器和滤波器公式（参见
  `Integrator method` 和 `Filter
  method`）。连续时间并联形式
  PIDF 控制器的传递函数为：

  C=P+I(1s)+D(Nss+N)。

  其他控制器动作相当于将 *P*、
  *I* 或 *D* 设为零。
- `Ideal` — 在 `Ideal` 形式中，离散时间 PIDF 控制器的传递函数为：

  C=P[1+IFi(z)+D(N1+NFd(z))]。

  连续时间理想形式 PIDF 控制器的传递函数为：

  C=P[1+I(1s)+D(Nss+N)]。

  其他控制器动作相当于将 *D* 设为零或将 *I* 设为 `Inf`。（在理想形式中，控制器必须具有比例动作。）

当您使用调优后的参数值更新 PID Controller 模块或自定义 PID 控制器时，请确保控制器形式匹配。

#### 编程使用

|  |
| --- |
| **模块参数**：`PIDForm` |
| **类型**：character vector |
| **值**：`'Parallel'` | `'Ideal'` |
| **默认值**：`'Parallel'` |

**Tunable:** Yes

### **Time Domain** — PID 控制器时域 discrete-time（默认）| continuous-time

指定您的 PID 控制器是离散时间控制器还是连续时间
控制器。

- 对于离散时间，您必须使用 **Controller sample time (sec)** 参数指定 PID 控制器的采样时间。
- 对于连续时间，您还必须使用 **Experiment sample time
  (sec)** 参数为 PID 自整定实验指定采样时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`TimeDomain` |
| **类型**：character vector |
| **值**：`'discrete-time'` | `'continuous-time'` |
| **默认值**：`'discrete-time'` |

### **Controller sample time (sec)** — PID 控制器的采样时间 0.1（默认）| 正标量 | –1

以秒为单位指定 PID 控制器的采样时间。此值还设置模块所执行实验的
采样时间。

要执行 PID 整定，模块会测量高达目标带宽 10 倍频率的频率响应信息。为确保该频率小于
奈奎斯特频率，目标带宽
*ωc* 必须满足 *ωc**Ts*
≤ 0.3，其中 *Ts*
*ωc* 是您使用 **Controller sample time (sec)** 参数指定的控制器采样时间。

当您使用调优后的参数值更新 PID Controller 模块或自定义 PID 控制器时，请确保控制器采样时间匹配。

#### 提示

如果您希望在应用程序中以不同的采样时间运行部署的模块，请将此参数设置为 –1，并将该模块放入 Triggered Subsystem 中。然后，以所需的采样时间触发
该子系统。如果您不打算在部署后更改采样
时间，请指定一个固定且有限的采样时间。

#### 依赖关系

要启用此参数，请将 **Time Domain** 设置为
`discrete-time`。

#### 编程使用

|  |
| --- |
| **模块参数**：`DiscreteTs` |
| **类型**：scalar |
| **Value** positive scalar | –1 |
| **默认值**：0.1 |

### **Tune at different sample time** — 启用从 PID 控制器以不同采样时间进行整定和实验 `off`（默认）| `on`

启用此参数以使用与您正在整定的 PID 控制器的采样率以及该模块执行的频率响应估计实验不同的采样率来运行整定。PID 增益整定算法计算量大，当您要将模块部署到硬件并以快速采样时间整定控制器时，某些硬件可能无法在单个时间步内完成 PID 增益计算。为降低硬件吞吐量要求，请使用 **Tuning sample time (sec)** 参数指定比控制器采样时间更慢的整定采样时间。

#### 依赖关系

要启用此参数，请将 **Time Domain** 设置为 `discrete-time`。

#### 编程使用

|  |
| --- |
| **模块参数**：`UseTuningTs` |
| **类型**：character vector |
| **Value** `'off'` | `'on'` |
| **默认值**：`'off'` |

### **Tuning sample time (sec)** — 整定算法的采样时间 0.2（默认）| 正标量

以秒为单位指定整定算法的采样时间。

如果您打算将模块部署到处理能力有限的硬件上，并希望以快速采样时间整定控制器，请指定一个使整定算法以比您正在整定的 PID 控制器更慢的速率运行的采样时间。

#### 依赖关系

要启用此参数，请将 **Time Domain** 设置为 `discrete-time` 并选中 **Tune at different sample time**。

#### 编程使用

|  |
| --- |
| **模块参数**：`TuningTs` |
| **类型**：scalar |
| **Value** positive scalar |
| **默认值**：0.2 |

### **Experiment sample time (sec)** — 实验的采样时间 0.02（默认）| 正标量

即使您整定的是连续时间控制器，也必须为该模块执行的实验指定采样时间。通常，不建议针对物理被控对象进行 PID 自整定的连续时间控制器整定。如果您要针对被控对象的 Simulink 模型进行连续时间整定，请使用快速的实验采样时间，例如 0.02/*ωc*。

#### 依赖关系

当 **Time Domain** 为 `continuous-time` 时，此参数启用。

#### 编程使用

|  |
| --- |
| **模块参数**：`ContinuousTs` |
| **类型**：positive scalar |
| **默认值**：0.02 |

### **Integrator method** — 积分项的离散积分公式 `Forward Euler`（默认）| `Backward Euler` | `Trapezoidal`

指定控制器中积分项的离散积分公式。在离散时间中，该模块所假设的 PID 控制器传递函数为：

C=P+IFi(z)+D[N1+NFd(z)],

并联形式，或理想形式，

C=P[1+IFi(z)+D(N1+NFd(z))].

对于控制器采样时间 *Ts*，`Integrator method` 参数按如下方式确定公式 *Fi*：

| Integrator method | *Fi* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优点的更多信息，请参阅 Discrete PID Controller 模块参考页面。

当您使用整定后的参数值更新 PID Controller 模块或自定义 PID 控制器时，请确保积分方法与之一致。

#### 依赖关系

当 **Time Domain** 为 `discrete-time` 且控制器包含积分作用时，此参数启用。

#### 编程使用

|  |
| --- |
| **模块参数**：`IntegratorFormula` |
| **类型**：character vector |
| **值**：`'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认值**：`'Forward Euler'` |

**Tunable:** Yes

### **Filter method** — 微分滤波项的离散积分公式 `Forward Euler`（默认）| `Backward Euler` | `Trapezoidal`

指定控制器中微分滤波项的离散积分公式。在离散时间下，该模块所假设的 PID 控制器传递函数为：

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

当您使用整定后的参数值更新 PID Controller 模块或自定义 PID 控制器时，请确保滤波方法匹配。

#### 依赖关系

当 **Time Domain** 为 `discrete-time` 且控制器包含微分滤波项时，此参数启用。

#### 编程使用

|  |
| --- |
| **模块参数**：`FilterFormula` |
| **类型**：character vector |
| **值**：`'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认值**：`'Forward Euler'` |

**Tunable:** Yes

### **Target bandwidth (rad/sec)** — 整定响应的目标穿越频率 1（默认）| 正标量

目标带宽以 rad/sec 为单位指定，是整定后开环响应 *CP* 的 0 dB 增益穿越频率的目标值，其中 *P* 是被控对象响应，*C* 是控制器响应。该穿越频率大致设定了控制带宽。对于上升时间 *τ* 秒，目标带宽的一个良好估计值是 2/*τ* rad/sec。

为执行 PID 整定，autotuner 模块会测量高达目标带宽 10 倍频率的频率响应信息。为确保该频率低于 Nyquist 频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* 是您通过 **Controller sample time (sec)** 参数指定的控制器采样时间。由于此条件，您可以为整定强制的最快上升时间约为 6.67*Ts*。如果该上升时间不满足您的设计目标，请考虑减小 *Ts*。

为获得闭环整定的最佳结果，请使用与初始 PID 控制器带宽相差约 10 倍以内的目标带宽。若要为更大的带宽变化整定控制器，请使用较小的变化逐步整定。

若要通过输入端口提供目标带宽，请选择 **Use external source**。

#### 编程使用

|  |
| --- |
| **模块参数**：`Bandwidth` |
| **类型**：positive scalar |
| **默认值**：`1` |

### **Target phase margin (degrees)** — 开环响应的目标最小相位裕度 60（默认）| 0–90 范围内的标量

指定整定后开环响应在穿越频率处的目标最小相位裕度。目标相位裕度反映了整定系统的期望鲁棒性。通常，选择约 45°–60° 范围内的值。一般来说，更高的相位裕度可改善超调，但可能限制响应速度。默认值 60° 倾向于平衡性能和鲁棒性，根据被控对象的特性，产生约 5–10% 的超调。

若要通过输入端口提供目标相位裕度，请选择 **Use external source**。

**Tunable:** Yes

#### 编程使用

|  |
| --- |
| **模块参数**：`TargetPM` |
| **类型**：scalar |
| **值**：0–90 |
| **默认值**：60 |

#### Experiment Tab

### **Experiment Mode** — 扰动信号类型 **Superposition**（默认）| **Sinestream** | **PRBS** *（自 R2023b 起）*

指定每个频率处的扰动是以顺序正弦（**Sinestream**）、同时正弦（**Superposition**）还是伪随机二进制序列（**PRBS**）方式施加。

- **Sinestream** — 在此模式下，模块分别在每个频率处施加扰动。有关用于估计的 sinestream 信号的详细信息，请参阅 Sinestream Input Signals。
- **Superposition** — 在此模式下，扰动信号一次性包含所有指定的频率。对于在频率向量 *ω* = [*ω*1, … , *ωN*] 处以幅值 *A* = [*A*1, … , *AN*] 进行频率响应估计，扰动信号为：

  Δu=∑iAisin(ωit)。
- **PRBS** — 一种确定性伪随机二进制序列，在两个值之间切换，具有类似白噪声的特性。与使用 sinestream 输入信号相比，PRBS 信号可减少总估计时间，同时产生相当的估计结果。PRBS 信号可用于估计通信和电力电子系统的频率响应。有关详细信息，请参阅 PRBS Input Signals。*（自 R2023b 起）*

**Sinestream** 模式可以更准确，也可以具有更低的侵入性，因为扰动的总大小永远不会超过 **Signal Amplitudes** 参数指定的值。然而，由于 sinestream 扰动的顺序特性，您添加的每个频率点都会增加推荐的实验时间（有关详细信息，请参阅 **start/stop** 输入端口）。因此，**Superposition** 模式下的估计实验通常要快得多，且结果令人满意。

与 superposition 输入信号相比，sinestream 信号减少了执行时间，但估计频率响应也需要更长时间。当您的处理能力有限且希望减少执行时间时，使用 sinestream 信号进行频率响应估计很有用。

为覆盖相似的频率范围，**PRBS** 模式下的实验长度通常比其他两种模式短得多。然而，结果的速度和质量之间存在权衡。*（自 R2023b 起）*

#### 编程使用

|  |
| --- |
| **模块参数**：`ExperimentMode` |
| **类型**：character vector |
| **值**：`'Sinestream'` | `'Superposition'` | `'PRBS'` |
| **默认值**：`'Superposition'` |

### **Plant Type** — 被控对象的稳定性 `Stable`（默认）| `Integrating`

指定被控对象是稳定的还是积分的。如果被控对象具有一个或多个积分器，请选择 `Integrating`。

#### 编程使用

|  |
| --- |
| **模块参数**：`PlantType` |
| **类型**：character vector |
| **值**：`'Stable'` | `'Integrating'` |
| **默认值**：`'Stable'` |

### **Plant Sign** — 被控对象的符号 `Positive`（默认）| `Negative`

指定被控对象是正的还是负的。如果在标称工作点处被控对象输入的正变化导致被控对象输出的正变化，请指定 `Positive`。否则，请指定 negative。对于稳定被控对象，被控对象的符号就是被控对象 DC 增益的符号。

#### 编程使用

|  |
| --- |
| **模块参数**：`PlantSign` |
| **类型**：character vector |
| **值**：`'Positive'` | `'Negative'` |
| **默认值**：`'Positive'` |

### **Signal Amplitudes** — 扰动幅度 1（默认）| 标量 | 长度为 5 的向量

在实验过程中，该模块以频率 [1/10, 1/3, 1, 3, 10]*ωc* 向被控对象注入扰动信号，其中 *ωc* 是用于整定的目标带宽。使用 **Signal Amplitudes** 指定每个注入信号的幅度。指定：

- 标量值，以在每个频率注入相同的幅度
- 长度为 5 的向量，以在 [1/10, 1/3, 1, 3, 10]*ωc* 的每个频率指定不同的幅度

在具有典型目标带宽的典型被控对象中，实验频率处被控对象响应的幅值通常不会发生很大变化。在这种情况下，您可以使用标量值在所有频率处施加相同幅值的扰动。但是，如果您知道响应在频率范围内急剧衰减，请考虑降低低频输入的幅度并提高高频输入的幅度。当所有被控对象响应具有可比幅值时，估计实验在数值上会更好。

扰动幅度必须：

- 足够大，使扰动能够克服被控对象执行器中的任何死区，并产生高于噪声水平的响应
- 足够小，使被控对象在标称工作点附近的近似线性区域内运行，并避免使被控对象输入或输出饱和

当 **Experiment mode** 为 **Superposition** 时，正弦信号会叠加。因此，扰动至少可以与所有幅度之和一样大。确保最大可能的扰动在被控对象执行器的范围内。使执行器饱和可能会在估计的频率响应中引入误差。

要通过输入端口提供信号幅度，请选择 **Use external source**。

**Tunable:** Yes

#### 编程使用

|  |
| --- |
| **模块参数**：`AmpSine` |
| **类型**：scalar, vector of length 5 |
| **默认值**：1 |

#### Block Tab

### **减少内存并避免任务超限（仅外部模式）** — 仅部署整定算法 `off`（默认）| `on`

该模块包含两个模块，一个执行实时频率响应估计，另一个使用所得的估计响应来整定 PID 增益。当您在外部仿真模式下运行包含该模块的 Simulink 模型时，默认情况下两个模块都会被部署。您可以通过仅部署估计模块来节省目标硬件上的内存（参见 Control Real-Time PID Autotuning in Simulink）。在这种情况下，整定算法在 Simulink 主机上运行，而不是在目标硬件上运行。选中此选项时，所部署的算法使用的内存约为清除该选项时的三分之一。

PID 增益计算比频率响应估计需要更大的计算负载。对于快速的控制器采样时间，某些硬件可能无法在一个执行周期内完成增益计算。因此，在使用计算能力有限的硬件时，选中此选项可以让您以快速采样时间整定 PID 控制器。

此外，当您启用此选项时，从整定实验结束到新的 PID 增益到达 **pid gains** 输出端口之间可能存在数个采样周期的延迟。在将增益推送到控制器之前，请先在 **pid gains** 输出端口确认变化，而不是使用 **start/stop** 信号作为更新的触发。

如果您打算在不使用外部仿真模式的情况下部署该模块并执行 PID 整定，请不要选中此选项。

**注意**

当您使用此选项时，必须将模型配置为数值模块参数在生成的代码中可调，而不是内联。要指定可调参数：

- 在模型编辑器中：在 **Configuration Parameters** 中，在 **Code Generation** > **Optimization** 下，将 **Default parameter behavior** 设置为 `Tunable`。
- 在命令行中：使用 `set_param(mdl,'DefaultParameterBehavior','Tunable')`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DeployTuningModule` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **为 PLC Coder 配置模块** — 为使用 Simulink PLC Coder 进行代码生成配置模块 off（默认）| on

如果您使用 Simulink PLC Coder 为 autotuner 模块生成代码，请选中此参数。对于使用任何其他 MathWorks® 代码生成产品进行代码生成的情况，请清除此参数。

选中此参数仅影响内部模块配置，以兼容 Simulink PLC Coder。该参数对生成的代码没有实际影响。

### **输出信号配置** — 提供控制信号加扰动或仅扰动 **control action + perturbation**（默认）| **perturbation only**

默认情况下，该模块将控制信号作为输入，并在端口 **u+Δu** 处提供控制信号加上实验扰动。然后您将该信号馈入被控对象输入，如下图所示。

此默认配置需要将该模块插入控制器和被控对象之间。如果您想自己将扰动信号添加到控制信号中，请选择 **perturbation only**。在此配置中，模块输出仅包含扰动信号，位于端口 **Δu**。您可以使用例如求和模块将该扰动信号注入被控对象，如下图所示。

在此配置中，您可以选择性地注释掉 Closed-Loop PID Autotuner 模块而不中断模型。

### **数据类型** — 浮点精度 `double`（默认）| `single`

根据仿真环境或硬件要求指定浮点精度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `BlockDataType` |
| **类型：** 字符向量 |
| **值：** `'double'` | `'single'` |
| **默认：** `'double'` |

### **点击“Update PID Block”将整定后的增益写入连接到“u”端口的 PID 模块** — 自动检测用于写入整定后 PID 系数的目标 `on`（默认）| `off`

在某些条件下，自动整定器模块可以将整定后的增益写入标准或自定义 PID 控制器模块。若要指示目标 PID 控制器是连接到自动整定器模块 **u** 端口的模块，请选择此选项。若要指定未连接到 **u** 的 PID 控制器，请清除此选项。

要将自动整定器模块中的整定后增益写入模型中任意位置的 PID 控制器，目标模块必须是以下之一：

- 一个 PID Controller 或 Discrete PID Controller 模块。
- 一个掩膜子系统，其中 PID 系数是名为 `P`、`I`、`D` 和 `N` 的掩膜参数，或你的控制器中存在的这些参数的任意子集。例如，如果你使用自定义 PI 控制器，那么你只需要掩膜参数 `P` 和 `I`。

### **指定 PID 模块路径** — 用于写入整定后系数的目标 PID 控制器模块 `[]`（默认）| 模块路径

在某些条件下，自动整定器模块可以将整定后的增益写入标准或自定义 PID 控制器模块。使用此参数指定目标 PID 控制器的路径。

要将自动整定器模块中的整定后增益写入模型中任意位置的 PID 控制器，目标模块必须是以下之一：

- 一个 PID Controller 或 Discrete PID Controller 模块。
- 一个掩膜子系统，其中 PID 系数是名为 `P`、`I`、`D` 和 `N` 的掩膜参数，或你的控制器中存在的这些参数的任意子集

#### 依赖关系

当选择 **点击“Update PID Block”将整定后的增益写入连接到“u”端口的 PID 模块** 时，此参数启用。

### **Update PID Block** — 将整定后的 PID 增益写入目标控制器模块 按钮

该模块不会自动将整定后的增益推送到目标 PID 模块。如果你的 PID 控制器模块满足 `指定 PID 模块路径` 参数描述中所述的条件，则在整定后，点击此按钮将整定后的增益传输到该模块。

你可以在仿真运行时更新 PID 模块，包括在外部模式下运行时。这样做有助于立即验证整定后的 PID 增益。在仿真期间的任何时刻，你都可以更改参数、再次开始实验，并将新的整定后增益推送到 PID 模块。然后你可以继续运行模型并观察被控对象的行为。

### **导出到 MATLAB** — 将实验和整定结果发送到 MATLAB® 工作区 按钮

当你点击此按钮时，该模块会在 MATLAB 工作区中创建一个包含实验和整定结果的结构体。此结构体 `OnlinePIDTuningResult` 包含以下字段：

- `P`、`I`、`D`、`N` — 整定后的 PID 增益。该结构体包含你所整定的控制器类型所需的这些字段中的任意字段。例如，如果你正在整定 PI 控制器，则该结构体包含 `P` 和 `I`，但不包含 `D` 和 `N`。
- `TargetBandwidth` — 你在该模块的 **Target bandwidth (rad/sec)** 参数中指定的值。
- `TargetPhaseMargin` — 你在该模块的 **Target phase margin (degrees)** 参数中指定的值。
- `EstimatedPhaseMargin` — 整定后系统达到的估计相位裕度。
- `Controller` — 整定后的 PID 控制器，以 `pid`（用于并联形式）或 `pidstd`（用于理想形式）模型对象返回。
- `Plant` — 估计的被控对象，以 `frd` 模型对象返回。此 `frd` 包含在实验频率 [1/10, 1/3, 1, 3, 10]*ωc* 处获得的响应数据。
- `PlantNominal` — 实验开始时的标称工作点处的被控对象输入和输出，指定为具有字段 `u`（输入）和 `y`（输出）的结构体。

你可以在仿真运行时导出到 MATLAB 工作区，包括在外部模式下运行时。

## 所属库

Simulink Control Design / Autotuning

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

## 版本历史

**在 R2018a 中引入**

### R2025a：在存在下游限幅时禁用扰动和整定的选项

Closed-Loop PID Autotuner 模块基于使用扰动信号估计的被控对象频率响应来整定 PID 控制器。如果您的被控对象在 Closed-Loop PID Autotuner 模块下游存在信号限幅，则由于扰动可能饱和，估计实验可能不准确。类似地，系统中的任何故障也可能导致实验不准确。您现在可以使用新的输入端口 **isExpGood** 来提供禁用扰动和整定的信号。该端口接受类似于 **start/stop** 输入的信号，并禁用扰动和整定，直到您开始新的实验。要启用 **isExpGood** 端口，请在 **Block** 选项卡上启用 **Use isExperimentGood port to disable perturbations and tuning**。

有关示例，请参阅 Disable PID Autotuning in Presence of Downstream Signal Limiting。

### R2023b：`sine Amp` 端口和 **Sine Amplitudes** 参数名称已更改

`sine Amp` 输入端口现在为 `signal Amp`，**Sine Amplitudes** 参数现在为 **Signal Amplitudes**。

用于程序化使用的参数名称保持不变。

### R2023b：PRBS 输入信号

Closed-Loop PID Controller 模块现在支持使用伪随机二进制序列（PRBS）输入信号进行估计。PRBS 信号是一种周期性的确定性信号，具有类似白噪声的特性，在两个值之间切换。与使用 sinestream 或叠加输入信号相比，PRBS 信号可减少总估计时间，同时产生相当的估计结果。PRBS 信号对于估计通信和电力电子应用的频率响应非常有用。

### R2023b：库位置已更改

Closed-Loop PID Controller 模块现在位于 **Simulink Control Design/Autotuner** 子库中。

在 R2023b 中，当您打开在先前版本中保存的模型时，Closed-Loop PID Controller 模块的库链接会自动更新。

### R2021b：Sinestream 输入信号

您现在可以使用 sinestream 输入信号来估计被控对象的频率响应。sinestream 信号由一系列依次施加的正弦扰动组成。当您使用 sinestream 输入信号执行频率响应估计实验时，模块会在每个频率处分别施加扰动。

与叠加输入信号相比，Sinestream 信号可减少执行时间，但估计频率响应也需要更长时间。当您的处理能力有限且希望减少执行时间时，使用 sinestream 信号进行频率响应估计非常有用。

## 描述

基于闭环实验实时估计的被控对象频率响应，自动整定 PID 增益

闭环 PID 自整定器模块允许你针对物理被控对象实时整定 PID 控制器，前提是你已有一个能使回路稳定的初始 PID 控制器。在整个自整定过程中，被控对象始终处于初始 PID 控制器的闭环控制之下。该模块可以在没有参数化被控对象模型的情况下，将 PID 控制器整定到指定的带宽和相位裕度。如果你拥有 Simulink® Coder™ 等代码生成产品，你可以生成在硬件上实现整定算法的代码，从而在使用或不使用 Simulink 管理自整定过程的情况下进行实时整定。

如果你有在 Simulink 中建模的被控对象和初始 PID 控制器，你可以针对模型化的被控对象执行闭环 PID 自整定。这样做可以让你在实时整定控制器之前预览被控对象响应并调整 PID 自整定的设置。

为实现无模型整定，闭环 PID 自整定器模块会：

1. 向被控对象注入测试信号，以采集被控对象输入输出数据并实时估计频率响应。测试信号是叠加在被控对象输入上的扰动信号的组合。
2. 在实验结束时，基于目标带宽附近估计的被控对象频率响应来整定 PID 控制器参数。
3. 用整定后的参数更新 PID Controller 模块或自定义 PID 控制器，使你能够实时验证闭环性能。

与开环 PID 自整定器模块不同，整个实验过程中回路保持闭合。保持回路闭合有助于在估计实验期间维持被控对象的安全运行。

你可以使用闭环 PID 自整定器模块为以下对象整定 PID 控制器：

- 任何稳定被控对象
- 任何具有一个或多个积分器（极点在 *s* = 0 处）或一对或多对位于虚轴上的复极点的连续时间被控对象
- 任何具有一个或多个积分器（极点在 *z* = –1 处）或位于单位圆 |*z*| = 1 上的复极点对的离散时间被控对象

如果你没有初始 PID 控制器，你可以使用开环 PID 自整定器模块来获得一个。然后你可以切换到闭环 PID 自整定以进行细化或重新整定。

该模块支持使用 Simulink Coder、Embedded Coder® 和 Simulink PLC Coder™ 进行代码生成。它不支持使用 HDL Coder™ 进行代码生成。

有关使用闭环 PID 自整定器模块的更多信息，请参阅：

- PID Autotuning for a Plant Modeled in Simulink
- PID Autotuning in Real Time

有关 PID 自整定的一般信息以及闭环和开环方法的比较，请参阅 When to Use PID Autotuning。
