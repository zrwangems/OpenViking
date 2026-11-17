---
type: simulink-block
title: 'Field Oriented Control Autotuner'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Controllers'
documentation_page: 'fieldorientedcontrolautotuner'
documentation_source_path: 'ref/fieldorientedcontrolautotuner.html'
language: zh-CN
chinese_source: worker-translation
---

# Field Oriented Control Autotuner

## 端口
```yaml
ports:
- name: PIDout daxis
  summary: 来自直轴电流控制器的信号 标量
  direction: input
  data_types: single | double
- name: measured feedback daxis
  summary: 测量的直轴电流 标量
  direction: input
  data_types: single | double
- name: PIDout qaxis
  summary: 来自交轴电流控制器的信号 标量
  direction: input
  data_types: single | double
- name: measured feedback qaxis
  summary: 测量的交轴电流 标量
  direction: input
  data_types: single | double
- name: PIDout spd
  summary: 来自速度控制器的信号 标量
  direction: input
  data_types: single | double
- name: measured feedback spd
  summary: 测量的速度 标量
  direction: input
  data_types: single | double
- name: PIDout flux
  summary: 来自磁通控制器的信号 标量
  direction: input
  data_types: single | double
- name: measured feedback flux
  summary: 测量的磁通 标量
  direction: input
  data_types: single | double
- name: start/stop
  summary: 启动和停止自整定实验标量
  direction: input
  data_types: single | double
- name: ActiveLoop
  summary: 指定自整定实验的活动回路 标量
  direction: input
  data_types: single | double
- name: bandwidth
  summary: 用于整定的目标带宽 标量 | 向量 | 总线
  direction: input
  data_types: single | double
- name: target PM
  summary: 用于整定的目标相位裕度 标量 | 向量 | 总线
  direction: input
  data_types: single | double
- name: sine Amp
  summary: 注入正弦扰动信号的幅值 向量 | 矩阵
  direction: input
  data_types: single | double
- name: perturbation daxis
  summary: 直轴电流输入扰动 标量
  direction: output
  data_types: single | double
- name: perturbation qaxis
  summary: 交轴电流输入扰动 标量
  direction: output
  data_types: single | double
- name: perturbation spd
  summary: 速度输入扰动 标量
  direction: output
  data_types: single | double
- name: perturbation flux
  summary: 磁通输入扰动 标量
  direction: output
  data_types: single | double
- name: pid gains
  summary: 整定后的 PID 系数总线
  direction: output
  data_types: single | double
- name: convergence
  summary: 实验期间 FRD 估计的收敛性 标量
  direction: output
  data_types: single | double
- name: estimated PM
  summary: 最近整定回路的估计相位裕度 标量
  direction: output
  data_types: single | double
- name: frd
  summary: 最近整定回路的估计频率响应 向量
  direction: output
  data_types: single | double
- name: nominal
  summary: 最近整定回路在标称工作点处的被控对象输入和输出 向量
  direction: output
  data_types: single | double
- name: loop startstops
  summary: 活动循环总线
  direction: output
  data_types: single | double
```

### 输入

### **PIDout daxis** — 来自直轴电流控制器的信号 标量

此端口接受 d 轴控制器 `PID_daxis` 的输出，该输出是调节电机 d 轴电流的 PID 控制器的输出。控制器生成 d 轴电压参考 `Vd_ref`，而 FOC 自整定模块生成用于 d 轴电流环整定实验的扰动。

图示为 d 轴电流环与自整定模块的连接

#### 依赖

要启用此端口，请选择 **Tune D-axis current loop**。

**数据类型：** `single` | `double`

### **measured feedback daxis** — 测量的直轴电流 标量

此端口接受从测量的（传感或估计的）电机电流中获得的 d 轴电流。

#### 依赖

要启用此端口，请选择 **Tune D-axis current loop**。

**数据类型：** `single` | `double`

### **PIDout qaxis** — 来自交轴电流控制器的信号 标量

此端口接受 q 轴控制器 `PID_qaxis` 的输出，该输出是调节电机 q 轴电流的 PID 控制器的输出。控制器生成 q 轴电压参考 `Vq_ref`，而 FOC 自整定模块生成用于 q 轴电流环整定实验的扰动。

图示为 q 轴电流环与自整定模块的连接

#### 依赖

要启用此端口，请选择 **Tune Q-axis current loop**。

**数据类型：** `single` | `double`

### **measured feedback qaxis** — 测量的交轴电流 标量

此端口接受从测量的（传感或估计的）电机电流中获得的 q 轴电流。

#### 依赖

要启用此端口，请选择 **Tune Q-axis current loop**。

**数据类型：** `single` | `double`

### **PIDout spd** — 来自速度控制器的信号 标量

此端口接受速度控制器 `PID_speed` 的输出，该输出是调节电机速度的 PID 控制器的输出。控制器生成 q 轴电流参考 `Iq_ref`，而 FOC 自整定模块生成用于速度环整定实验的扰动。

图示为速度环与自整定模块的连接

#### 依赖

要启用此端口，请选择 **Tune speed loop**。

**数据类型：** `single` | `double`

### **measured feedback spd** — 测量的速度 标量

此端口接受来自电机的测量（传感或估计的）速度。

#### 依赖

要启用此端口，请选择 **Tune speed loop**。

**数据类型：** `single` | `double`

### **PIDout flux** — 来自磁通控制器的信号 标量

此端口接受磁通控制器 `PID_flux` 的输出，该输出是调节电机磁通的 PID 控制器的输出。控制器生成 d 轴电流参考 `Id_ref`，而 FOC 自整定模块生成用于磁通环整定实验的扰动。

图示为磁通环与自整定模块的连接

对于永磁同步电机（PMSM），由于转子磁通固定且 `Id_ref` 设置为零，因此没有磁通环控制器。在某些应用中，您可以提供负的 `Id_ref` 值来实现弱磁控制，以更高的电流为代价获得更高的转子速度。

#### 依赖

要启用此端口，请选择 **Tune flux loop**。

**数据类型：** `single` | `double`

### **measured feedback flux** — 测量的磁通 标量

此端口接受来自电机的测量（传感或估计的）磁通。

#### 依赖

要启用此端口，请选择 **Tune flux loop**。

**数据类型：** `single` | `double`

### **start/stop** — 启动和停止自整定实验标量

要通过外部方式启动和停止自整定过程，请在
`start/stop` 端口和
`ActiveLoop` 端口提供信号。

- 当信号值从负值或零变为正值时，实验启动。
- 当信号值从正值变为负值或零时，实验停止。

在实验持续期间，对于每个回路，模块会在与回路关联的被控对象输入端、标称工作点附近注入正弦扰动，以采集输入输出数据并估计频率响应。当实验停止时，模块基于在目标带宽附近估计的被控对象频率响应计算 PID 增益。

当实验未运行时，模块不会在被控对象输入端注入任何扰动。在此状态下，模块对被控对象或控制器行为没有影响。

通常，您可以使用从 0 变为 1 的信号来启动实验，并使用从 1 变为 0 的信号来停止实验。配置 `start/stop` 信号时，请考虑以下事项。

- 当电机处于期望的平衡工作点时启动实验。使用初始控制器将电机驱动到该工作点。
- 在实验期间避免电机上的任何输入或输出扰动。如果您现有的闭环系统具有良好的扰动抑制能力，那么实验可以处理小扰动。否则，大扰动可能会使被控对象输出失真，并降低频率响应估计的准确性。
- 让实验运行足够长的时间，以便算法采集足够的数据，在其探测的所有频率上获得良好的估计。有两种方法可以确定何时停止实验：

  - 提前确定实验持续时间。实验持续时间的保守估计为
    叠加实验模式下为 200/*ωc*，
    正弦流实验模式下为 550/*ωc*，
    其中 *ωc* 是您的目标带宽。
  - 观察
    `convergence` 输出处的信号，并在信号稳定在 100% 附近时停止实验。

  对于 **PRBS**
  模式，基于指定的 **Target
  bandwidth** 和 **Controller sample time** 值，模块对话框会在
  **Experiment** 选项卡的
  **Description** 部分显示推荐的实验长度。
  过早停止实验可能导致不正确的整定
  结果。*（自 R2024a 起）*
- 当您停止实验时，模块会计算整定后的 PID
  增益，并更新 `pid
  gains` 端口处的信号。

您可以配置适合您应用的任何逻辑来控制实验的启动和停止时间。`start/stop` 信号与 `ActiveLoop` 一起指定。`ActiveLoop` 取整数 1 到 4，并指定要整定的回路。

或者，如果您在仿真或外部模式下进行整定，可以在模块参数中指定整定实验序列、开始时间和持续时间。

#### 依赖关系

要启用此端口，请在 Block 选项卡的 **Parameters
Source** 下，选择 **Use external source for
start/stop of experiment**。

**数据类型：** `single` | `double`

### **ActiveLoop** — 指定自整定实验的活动回路 标量

设置 `ActiveLoop` 值，以在提供整定实验开始和停止时间的外部源时，指定要整定的回路。

| `ActiveLoop` 值 | 要整定的回路 |
| --- | --- |
| `1` | `D-axis` 电流回路 |
| `2` | `Q-axis` 电流回路 |
| `3` | `Speed` 回路 |
| `4` | `Flux` 回路 |

您可以结合 `start/stop` 端口配置适合您应用的任何逻辑，以控制回路整定实验运行的顺序和时间。
`ActiveLoop` 取 1 到 4 的整数值，并指定要整定的回路。任何其他数字都将导致不进行整定，无论 `start/stop` 信号如何。例如，当您在 `ActiveLoop` 处提供常量值 2 且 `start/stop` 处的信号上升时，模块将启动 q 轴电流回路的整定实验。

或者，您可以在模块参数中指定整定实验顺序、开始时间和持续时间。

#### 依赖关系

要启用此端口，请在 Block 选项卡的 **Parameters Source** 下，选择 **Use external source for start/stop of experiment**。

**Data Types:** `single` | `double`

### **bandwidth** — 用于整定的目标带宽 标量 | 向量 | 总线

为每个要整定的回路提供 `Target bandwidth (rad/sec)` 参数的值。如果您要整定多个回路，可以将带宽指定为向量或总线，其元素按以下顺序对应于各回路的目标带宽：

- D-axis 电流回路
- Q-axis 电流回路
- Speed 回路
- Flux 回路

向量信号必须指定为 N×1 或 1×N 信号，或者如果指定为总线，则必须具有 N 个元素，其中 N 是要整定的回路数。
例如，如果您要整定 q 轴电流回路和速度回路，并在此端口指定向量 [5000, 200]，则模块将以目标带宽 5000 rad/sec 整定 q 轴电流控制器，并以目标带宽 200 rad/sec 整定速度回路控制器。

如果您要整定多个回路并在此端口指定标量值，则模块将使用相同的目标带宽来整定所有控制器。为了实现有效的串级控制，内控制回路（d 轴和 q 轴）必须比外控制回路（磁通和速度）响应快得多。
因此，在整定多个回路时，您必须将目标带宽提供为向量或总线信号。

或者，您可以在模块参数中为各个回路指定目标带宽。有关如何选择带宽的更多信息，请参阅该参数说明。

#### 依赖关系

要启用此端口，请在 Block 选项卡的 **Parameters Source** 下，选择 **Use external source for bandwidth**。

**Data Types:** `single` | `double`

### **target PM** — 用于整定的目标相位裕度 标量 | 向量 | 总线

为每个要整定的回路提供 `Target phase margin (degrees)` 参数的值。如果您要整定多个回路，可以将 `target PM` 指定为向量或总线，其元素按以下顺序对应于各回路的目标相位裕度：

- D-axis 电流回路
- Q-axis 电流回路
- Speed 回路
- Flux 回路

向量信号必须指定为 N×1 或 1×N 信号，或者如果指定为总线，则必须具有 N 个元素，其中 N 是要整定的回路数。
例如，如果您要整定 q 轴电流回路和速度回路，并在此端口指定向量 [60, 45]，则模块将以目标相位裕度 60 度整定 q 轴电流控制器，并以目标相位裕度 45 度整定速度回路控制器。

如果您要整定多个回路并在此端口指定标量值，则模块将使用相同的目标相位裕度来整定所有控制器。

或者，您可以在模块参数中为各个回路指定目标相位裕度。有关如何选择目标相位裕度的更多信息，请参阅该参数说明。

#### 依赖关系

要启用此端口，请在模块选项卡的 **Parameters Source** 下，选择 **Use external source for target phase margin**。

**数据类型：** `single` | `double`

### **sine Amp** — 注入正弦扰动信号的幅值 向量 | 矩阵

为每个待整定的回路提供 `Sine Amplitudes` 参数的值。指定以下之一：

- 长度为 5 的向量，用于在 [1/10, 1/3, 1, 3, 10]*ωc* 的每个频率点指定不同的幅值，其中 *ωc* 是整定的目标带宽。
- N×5 矩阵，其中 N 是待整定的回路数。每个行条目长度必须为 5，用于在 [1/10, 1/3, 1, 3, 10]*ωc* 的每个频率点指定不同的幅值。

如果您要整定多个回路，并在此端口指定长度为 5 的向量，则模块会在对应于该回路的 [1/10, 1/3, 1, 3, 10]*ωc* 的每个频率点对所有回路使用指定的幅值。

或者，您可以在模块参数中为各个回路指定正弦扰动幅值。有关详细信息，请参阅参数说明。

#### 依赖关系

要启用此端口，请在模块选项卡的 **Parameters Source** 下，选择 **Use external source for sine amplitudes**。

**数据类型：** `single` | `double`
### 输出

### **perturbation daxis** — 直轴电流输入扰动 标量

用于估计与 d 轴电流控制回路相关的频率响应数据模型的扰动信号输入。通过使用求和模块将此端口的扰动信号注入到调节 d 轴电流的 PID 控制器输出。

- 当实验运行时，模块在此端口生成扰动信号。
- 当实验未运行时，此端口的信号为零。在此状态下，模块对被控对象没有影响。

#### 依赖关系

要启用此端口，请选择 **Tune D-axis current loop**。

**数据类型：** `single` | `double`

### **perturbation qaxis** — 交轴电流输入扰动 标量

用于估计与 q 轴电流控制回路相关的频率响应数据模型的扰动信号输入。通过使用求和模块将此扰动信号注入到调节 q 轴电流的 PID 控制器输出。

- 当实验运行时，模块在此端口生成扰动信号。
- 当实验未运行时，此端口的信号为零。在此状态下，模块对被控对象没有影响。

#### 依赖关系

要启用此端口，请选择 **Tune Q-axis current loop**。

**数据类型：** `single` | `double`

### **perturbation spd** — 速度输入扰动 标量

用于估计与电机速度控制回路相关的频率响应数据模型的扰动信号输入。通过使用求和模块将此扰动信号与调节电机速度的 PID 控制器输出相加。

- 当实验运行时，模块在此端口生成扰动信号。
- 当实验未运行时，此端口的信号为零。在此状态下，模块对被控对象没有影响。

#### 依赖关系

要启用此端口，请选择 **Tune speed loop**。

**数据类型：** `single` | `double`

### **perturbation flux** — 磁通输入扰动 标量

用于估计与电机磁通控制回路相关的频率响应数据模型的扰动信号输入。通过使用求和模块将此扰动信号注入到调节电机磁链的 PID 控制器输出。

- 当实验运行时，模块在此端口生成扰动信号。
- 当实验未运行时，此端口的信号为零。在此状态下，模块对被控对象没有影响。

#### 依赖关系

要启用此端口，请选择 **Tune flux loop**。

**数据类型：** `single` | `double`

### **pid gains** — 整定后的 PID 系数总线

该 4 元素总线信号包含模块所整定的每个控制回路的整定后 PID 增益 *P*、*I*、*D* 以及滤波器系数 *N*。这些值对应于 `Form` 参数中所给表达式中的 `P`、`I`、`D` 和 `N` 参数。初始时，这些值分别为 0、0、0 和 100。模块在实验结束时更新这些值。模块所整定的每个控制回路对应的总线信号始终具有四个元素，即使您并未整定 PIDF 控制器。

**数据类型：** `single` | `double`

### **convergence** — 实验期间 FRD 估计的收敛性 标量

模块使用扰动信号来估计与每个控制回路相关联的被控对象在目标带宽附近若干频率处的频率响应，以进行整定。`convergence` 表示被控对象频率响应估计的完成程度。通常，该值在实验开始后迅速上升至约 90%，然后逐渐收敛至更高的值。当该值在接近 100% 处趋于平稳时，停止实验。

对于 **PRBS** 实验模式，该端口上的信号仅在估计实验完成后更新。*（自 R2024a 起）*

**数据类型：** `single` | `double`

### **estimated PM** — 最近整定回路的估计相位裕度 标量

该端口输出最近整定回路中整定后控制器所达到的估计相位裕度，以度为单位。模块在每个回路的整定实验结束时更新该值。估计相位裕度由 *G*(*jωc*)*C*(*jωc*) 的相角计算得出，其中 *G* 是该回路的估计被控对象，*C* 是整定后的控制器，*ωc* 是穿越频率（带宽）。估计相位裕度可能与 `Target phase margin (degrees)` 参数指定的目标相位裕度不同。它是整定后系统所达到的鲁棒性和稳定性的指标。

- 通常，估计相位裕度接近目标相位裕度。一般而言，该值越大，整定后系统越鲁棒，超调越小。
- 负相位裕度表明闭环系统可能不稳定。

#### 依赖关系

要启用该端口，请在模块选项卡上选择 **Estimated phase margin achieved by tuned controllers**。

**数据类型：** `single` | `double`

### **frd** — 最近整定回路的估计频率响应 向量

该端口输出实验对最近整定回路所估计的频率响应数据。初始时，`frd` 处的值为 [0, 0, 0, 0, 0]。在实验期间，模块在频率 [1/10, 1/3, 1, 3, 10]*ωc* 处注入信号，其中 *ωc* 是目标带宽。在实验期间的每个采样时间，模块用包含这些频率处复数频率响应的向量更新 `frd`。您可以使用响应的进展作为 `convergence` 的替代来检查估计的收敛性。当实验停止时，模块用用于计算 PID 增益的最终估计频率响应更新 `frd`。

对于 **PRBS** 实验模式，该端口上的信号仅在估计实验完成后更新。*（自 R2024a 起）*

#### 依赖关系

要启用该端口，请在模块选项卡上选择 **Plant frequency responses near bandwidth**。

**数据类型：** `single` | `double`

### **nominal** — 最近整定回路在标称工作点处的被控对象输入和输出 向量

该端口输出一个向量，包含最近整定回路或当前正在整定回路的被控对象输入和被控对象输出。这些值是模块执行实验时所处标称工作点处的被控对象输入和输出。

#### 依赖关系

要启用该端口，请在模块选项卡上选择 **Plant nominal input and output**。

**数据类型：** `single` | `double`

### **loop startstops** — 活动循环总线

此 4 元素总线信号指示由该模块整定的每个循环的整定实验是否处于活动状态。对于总线中的每个信号，当整定实验正在运行时，该端口为循环输出逻辑值 `1`（`true`）。当实验结束或尚未开始时，该值为逻辑 `0`（`false`）。您可以使用此端口触发各个循环的 PID 增益更新。

#### 依赖关系

要启用此端口，请在模块选项卡上，禁用 **Use external source for start/stop of experiment** 并选择 **Start/stop of autotuning process**。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Tune D-axis current loop
  summary: 启用 d 轴电流环整定 on（默认）| off
  group: ''
  block_parameter: TuneDaxisLoop
  type: 字符向量
  values: '''on'' | ''off'''
- name: Tune Q-axis current loop
  summary: 启用 q 轴电流环整定 on（默认）| off
  group: ''
  block_parameter: TuneQaxisLoop
  type: 字符向量
  values: '''on'' | ''off'''
- name: Tune speed loop
  summary: 启用速度环整定 on（默认）| off
  group: ''
  block_parameter: TuneSpeedLoop
  type: 字符向量
  values: '''on'' | ''off'''
- name: Tune flux loop
  summary: 启用磁通环整定 on（默认）| off
  group: ''
  block_parameter: TuneSpeedLoop
  type: 字符向量
  values: '''on'' | ''off'''
- name: Use same settings for current loop controllers (D-axis + Q-axis)
  summary: 为直轴和交轴电流环启用相同的整定和实验设置 off（默认）| on
  group: ''
  block_parameter: UseSameSettingsInner
  type: 字符向量
  values: '''off'' | ''on'''
- name: Use same settings for outer loop controllers (Speed + Flux)
  summary: 为速度环和磁通环启用相同的整定和实验设置 off（默认）| on
  group: ''
  block_parameter: UseSameSettingsOuter
  type: 字符向量
  values: '''off'' | ''on'''
- name: Experiment sample time
  summary: 频率响应估计实验的采样时间 –1（默认）| 正标量
  group: ''
  block_parameter: TsExperiment
  type: scalar
  values: positive scalar
  default: –1 (inherited)
- name: Use different sample time for tuning
  summary: 启用与回路 PID 控制器和实验不同的采样时间进行整定 off（默认）| on
  group: Tuning Tab
  block_parameter: UseTuningTs
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Tuning sample time (sec)
  summary: 整定算法的采样时间 0.2（默认）| 正标量
  group: Tuning Tab
  block_parameter: TsTuning
  type: scalar
  values: positive scalar
  default: '0.2'
- name: Type
  summary: D 轴电流回路 PID 控制器动作 PI（默认）| PID | PIDF | ...
  group: Tuning Tab
  block_parameter: PIDTypeDaxis
  type: 字符向量
  values: '''P'' | ''I'' | ''PI'' | ''PD'' | ''PDF'' | ''PID'' | ''PIDF'''
  default: '''PI'''
- name: Form
  summary: d 轴电流环 PID 控制器形式 Parallel（默认）| Ideal
  group: Tuning Tab
  block_parameter: PIDFormDaxis
  type: 字符向量
  values: '''Parallel'' | ''Ideal'''
  default: '''Parallel'''
- name: Controller sample time (sec)
  summary: d 轴电流环 PID 控制器采样时间 0.001（默认）| 正标量 | –1
  group: Tuning Tab
  block_parameter: TsDaxis
  type: 标量
  values: 正标量 | –1
  default: '0.001'
- name: Integrator method
  summary: d 轴电流环控制器积分项的离散积分公式 Forward Euler（默认）| Backward Euler | Trapezoidal
  group: Tuning Tab
  block_parameter: IntegratorMethodDaxis
  type: 字符向量
  values: '''Forward Euler'' | ''Backward Euler'' | ''Trapezoidal'''
  default: '''Forward Euler'''
- name: Filter method
  summary: d 轴电流环控制器导数滤波项的离散积分公式 Forward Euler（默认）| Backward Euler | Trapezoidal
  group: Tuning Tab
  block_parameter: FilterMethodDaxis
  type: character vector
  values: '''Forward Euler'' | ''Backward Euler'' | ''Trapezoidal'''
  default: '''Forward Euler'''
- name: Target bandwidth (rad/sec)
  summary: d 轴电流环调谐响应的目标穿越频率 100（默认）| 正标量
  group: Tuning Tab
  block_parameter: BandwidthDaxis
  type: positive scalar
  default: '100'
- name: Target phase margin (degrees)
  summary: d 轴电流环目标最小相位裕度 60（默认）| 范围 0–90 的标量
  group: Tuning Tab
  block_parameter: TargetPMDaxis
  type: scalar
  values: 0–90
  default: '60'
- name: Type
  summary: q 轴电流环 PID 控制器动作 PI（默认）| PID | PIDF | ...
  group: Tuning Tab
  block_parameter: PIDTypeQaxis
  type: character vector
  values: '''P'' | ''I'' | ''PI'' | ''PD'' | ''PDF'' | ''PID'' | ''PIDF'''
  default: '''PI'''
- name: Form
  summary: q 轴电流环 PID 控制器形式 Parallel（默认）| Ideal
  group: Tuning Tab
  block_parameter: PIDFormQaxis
  type: character vector
  values: '''Parallel'' | ''Ideal'''
  default: '''Parallel'''
- name: Controller sample time (sec)
  summary: q 轴电流环 PID 控制器采样时间 0.001（默认）| 正标量 | –1
  group: Tuning Tab
  block_parameter: TsQaxis
  type: scalar
  values: positive scalar | –1
  default: '0.001'
- name: 积分器方法
  summary: 用于积分项 Forward Euler（默认）| Backward Euler | Trapezoidal 的 q 轴电流环控制器离散积分公式
  group: Tuning Tab
  block_parameter: IntegratorMethodQaxis
  type: 字符向量
  values: '''Forward Euler'' | ''Backward Euler'' | ''Trapezoidal'''
- name: 滤波器方法
  summary: 用于微分滤波器项 Forward Euler（默认）| Backward Euler | Trapezoidal 的 q 轴电流环控制器离散积分公式
  group: Tuning Tab
  block_parameter: FilterMethodQaxis
  type: 字符向量
  values: '''Forward Euler'' | ''Backward Euler'' | ''Trapezoidal'''
- name: 目标带宽 (rad/sec)
  summary: 调优响应的 q 轴电流环目标穿越频率 100（默认）| 正标量
  group: Tuning Tab
  block_parameter: BandwidthQaxis
  type: 正标量
- name: 目标相位裕度（度）
  summary: Q 轴电流环目标最小相位裕度 60（默认）| 0–90 范围内的标量
  group: Tuning Tab
  block_parameter: TargetPMQaxis
  type: 标量
  values: 0–90
- name: 类型
  summary: 速度环 PID 控制器动作 PI（默认）| PID | PIDF | ...
  group: Tuning Tab
  block_parameter: PIDTypeSpeed
  type: 字符向量
  values: '''P'' | ''I'' | ''PI'' | ''PD'' | ''PDF'' | ''PID'' | ''PIDF'''
- name: 形式
  summary: 速度环 PID 控制器形式 Parallel（默认）| Ideal
  group: Tuning Tab
  block_parameter: PIDFormSpeed
  type: 字符向量
  values: '''Parallel'' | ''Ideal'''
- name: 控制器采样时间（秒）
  summary: 速度环 PID 控制器采样时间 0.1（默认）| 正标量 | –1
  group: Tuning Tab
  block_parameter: TsSpeed
  type: scalar
  values: positive scalar | –1
- name: Integrator method
  summary: 速度环控制器积分项离散积分公式 Forward Euler（默认） | Backward Euler | Trapezoidal
  group: Tuning Tab
  block_parameter: IntegratorMethodSpeed
  type: character vector
  values: '''Forward Euler'' | ''Backward Euler'' | ''Trapezoidal'''
- name: Filter method
  summary: 速度环控制器微分滤波项离散积分公式 Forward Euler（默认） | Backward Euler | Trapezoidal
  group: Tuning Tab
  block_parameter: FilterMethodSpeed
  type: character vector
  values: '''Forward Euler'' | ''Backward Euler'' | ''Trapezoidal'''
- name: 目标带宽 (rad/sec)
  summary: 调谐响应 1 的速度环目标穿越频率（默认）| 正标量
  group: Tuning Tab
  block_parameter: BandwidthSpeed
  type: positive scalar
  default: '1'
- name: 目标相位裕度 (degrees)
  summary: 速度环目标最小相位裕度 60（默认）| 范围 0–90 的标量
  group: Tuning Tab
  block_parameter: TargetPMSpeed
  type: scalar
  values: 0–90
  default: '60'
- name: Type
  summary: 磁通环 PID 控制器动作 PI（默认）| PID | PIDF | ...
  group: Tuning Tab
  block_parameter: PIDTypeFlux
  type: character vector
  values: '''P'' | ''I'' | ''PI'' | ''PD'' | ''PDF'' | ''PID'' | ''PIDF'''
  default: '''PI'''
- name: Form
  summary: 磁通环 PID 控制器形式 Parallel（默认）| Ideal
  group: Tuning Tab
  block_parameter: PIDFormFlux
  type: character vector
  values: '''Parallel'' | ''Ideal'''
  default: '''Parallel'''
- name: Controller sample time (sec)
  summary: 磁通环 PID 控制器采样时间 0.1（默认）| 正标量 | –1
  group: Tuning Tab
  block_parameter: TsFlux
  type: scalar
  values: positive scalar | –1
  default: '0.1'
- name: Integrator method
  summary: 磁通环控制器积分项的离散积分公式 Forward Euler（默认）| Backward Euler | Trapezoidal
  group: Tuning Tab
  block_parameter: IntegratorMethodFlux
  type: character vector
  values: '''Forward Euler'' | ''Backward Euler'' | ''Trapezoidal'''
  default: '''Forward Euler'''
- name: Filter method
  summary: 导数滤波器项的磁通环控制器离散积分公式 Forward Euler（默认）| Backward Euler | Trapezoidal
  group: Tuning Tab
  block_parameter: FilterMethodFlux
  type: character vector
  values: '''Forward Euler'' | ''Backward Euler'' | ''Trapezoidal'''
  default: '''Forward Euler'''
- name: Target bandwidth (rad/sec)
  summary: 磁通环整定响应的目标穿越频率 1（默认）| 正标量
  group: Tuning Tab
  block_parameter: BandwidthFlux
  type: positive scalar
  default: '1'
- name: Target phase margin (degrees)
  summary: 磁通环目标最小相位裕度 60（默认）| 0–90 范围内的标量
  group: Tuning Tab
  block_parameter: TargetPMFlux
  type: scalar
  values: 0–90
  default: '60'
- name: Type
  summary: 电流环 PID 控制器动作 PI（默认）| PID | PIDF | ...
  group: Tuning Tab
  block_parameter: PIDTypeAllInner
  type: character vector
  values: '''P'' | ''I'' | ''PI'' | ''PD'' | ''PDF'' | ''PID'' | ''PIDF'''
  default: '''PI'''
- name: Form
  summary: 电流环 PID 控制器形式 Parallel（默认）| Ideal
  group: Tuning Tab
  block_parameter: PIDFormAllInner
  type: character vector
  values: '''Parallel'' | ''Ideal'''
  default: '''Parallel'''
- name: Controller sample time (sec)
  summary: 电流环 PID 控制器采样时间 0.001（默认）| 正标量 | –1
  group: Tuning Tab
  block_parameter: TsAllInner
  type: scalar
  values: positive scalar | –1
  default: '0.001'
- name: Integrator method
  summary: 电流环控制器积分项离散积分公式 Forward Euler（默认）| Backward Euler | Trapezoidal
  group: Tuning Tab
  block_parameter: IntegratorMethodAllInner
  type: character vector
  values: '''Forward Euler'' | ''Backward Euler'' | ''Trapezoidal'''
  default: '''Forward Euler'''
- name: Filter method
  summary: 电流环控制器微分滤波项离散积分公式 Forward Euler（默认）| Backward Euler | Trapezoidal
  group: Tuning Tab
  block_parameter: FilterMethodAllInner
  type: character vector
  values: '''Forward Euler'' | ''Backward Euler'' | ''Trapezoidal'''
  default: '''Forward Euler'''
- name: Target bandwidth (rad/sec)
  summary: 电流环整定响应的目标穿越频率 100（默认）| 正标量
  group: Tuning Tab
  block_parameter: BandwidthAllInner
  type: positive scalar
  default: '1'
- name: 目标相位裕度（度）
  summary: 电流环目标最小相位裕度 60（默认）| 0–90 范围内的标量
  group: Tuning Tab
  block_parameter: TargetPMAllInner
  type: 标量
  values: 0–90
- name: 类型
  summary: 外环 PID 控制器动作 PI（默认）| PID | PIDF | ...
  group: Tuning Tab
  block_parameter: PIDTypeAllOuter
  type: 字符向量
  values: '''P'' | ''I'' | ''PI'' | ''PD'' | ''PDF'' | ''PID'' | ''PIDF'''
- name: 形式
  summary: 外环 PID 控制器形式 Parallel（默认）| Ideal
  group: Tuning Tab
  block_parameter: PIDFormAllOuter
  type: 字符向量
  values: '''Parallel'' | ''Ideal'''
- name: 控制器采样时间（秒）
  summary: 外环 PID 控制器采样时间 0.1（默认）| 正标量 | –1
  group: Tuning Tab
  block_parameter: TsAllOuter
  type: 标量
  values: 正标量 | –1
  default: '0.1'
- name: Integrator method
  summary: 外环控制器积分项离散积分公式 Forward Euler（默认） | Backward Euler | Trapezoidal
  group: Tuning Tab
  block_parameter: IntegratorMethodAllOuter
  type: 字符向量
  values: '''Forward Euler'' | ''Backward Euler'' | ''Trapezoidal'''
  default: '''Forward Euler'''
- name: Filter method
  summary: 外环控制器微分滤波器项离散积分公式 Forward Euler（默认） | Backward Euler | Trapezoidal
  group: Tuning Tab
  block_parameter: FilterMethodAllOuter
  type: 字符向量
  values: '''Forward Euler'' | ''Backward Euler'' | ''Trapezoidal'''
  default: '''Forward Euler'''
- name: 目标带宽 (rad/sec)
  summary: 整定响应的外环目标穿越频率 1（默认）| 正标量
  group: Tuning Tab
  block_parameter: BandwidthAllOuter
  type: positive scalar
  default: '1'
- name: 目标相位裕度 (degrees)
  summary: 外环目标最小相位裕度 60（默认）| 范围 0–90 的标量
  group: Tuning Tab
  block_parameter: TargetPMAllOuter
  type: scalar
  values: 0–90
  default: '60'
- name: D 轴电流环启动时间 (sec)
  summary: 指定直轴电流环整定实验启动时间 1（默认）
  group: 实验选项卡
  block_parameter: StartTimeDaxis
  type: positive scalar
  default: '1'
- name: D 轴电流环实验持续时间 (sec)
  summary: 指定直轴电流环整定实验持续时间 0.05（默认）
  group: 实验选项卡
  block_parameter: DurationDaxis
  type: positive scalar
  default: '0.05'
- name: Q 轴电流环启动时间 (sec)
  summary: 指定交轴电流环整定实验启动时间 1.1（默认）
  group: 实验选项卡
  block_parameter: StartTimeQaxis
  type: positive scalar
  default: '1.1'
- name: Q 轴电流环实验持续时间 (sec)
  summary: 指定交轴电流环整定实验持续时间 0.05（默认）
  group: 实验选项卡
  block_parameter: DurationQaxis
  type: positive scalar
  default: '0.05'
- name: 速度环启动时间 (sec)
  summary: 指定速度环整定实验启动时间 2（默认）
  group: 实验选项卡
  block_parameter: StartTimeSpeed
  type: positive scalar
  default: '2'
- name: Speed loop experiment duration (sec)
  summary: 指定速度环整定实验持续时间 3（默认值）
  group: 实验选项卡
  block_parameter: DurationSpeed
  type: positive scalar
  default: '3'
- name: Flux loop start time (sec)
  summary: 指定磁链环整定实验开始时间 6（默认值）
  group: 实验选项卡
  block_parameter: StartTimeFlux
  type: positive scalar
  default: '6'
- name: Flux loop experiment duration (sec)
  summary: 指定磁链环整定实验持续时间 3（默认值）
  group: 实验选项卡
  block_parameter: DurationFlux
  type: positive scalar
  default: '3'
- name: Experiment Mode
  summary: 正弦扰动信号类型 Superposition（默认值）| Sinestream | PRBS *（自 R2024a 起）*
  group: 实验选项卡
  block_parameter: ExperimentMode
  type: character vector
  values: '''Superposition'' | ''Sinestream'' | ''PRBS'''
  default: '''Superposition'''
- name: Plant Type
  summary: 直轴电流被控对象稳定性 Stable（默认值）| Integrating
  group: 实验选项卡
  block_parameter: PlantTypeDaxis
  type: 字符向量
  values: '''Stable'' | ''Integrating'''
  default: '''Stable'''
- name: 被控对象符号
  summary: 直轴电流被控对象符号 Positive（默认）| Negative
  group: 实验选项卡
  block_parameter: PlantSignDaxis
  type: 字符向量
  values: '''Positive'' | ''Negative'''
  default: '''Positive'''
- name: 正弦幅值
  summary: 直轴电流环路中正弦扰动的幅值 1（默认）| 标量 | 长度为 5 的向量
  group: 实验选项卡
  block_parameter: AmpSineDaxis
  type: 标量，长度为 5 的向量
  default: '1'
- name: 被控对象类型
  summary: 交轴电流被控对象的稳定性 Stable（默认）| Integrating
  group: 实验选项卡
  block_parameter: PlantTypeQaxis
  type: 字符向量
  values: '''Stable'' | ''Integrating'''
  default: '''Stable'''
- name: 被控对象符号
  summary: 交轴电流被控对象符号 Positive（默认）| Negative
  group: 实验选项卡
  block_parameter: PlantSignQaxis
  type: 字符向量
  values: '''Positive'' | ''Negative'''
  default: '''Positive'''
- name: Sine Amplitudes
  summary: 交轴电流环 1 中正弦扰动的幅值（默认）| 标量 | 长度为 5 的向量
  group: 实验选项卡
  block_parameter: AmpSineQaxis
  type: scalar, vector of length 5
  default: '1'
- name: Plant Type
  summary: 速度环被控对象的稳定性 Stable（默认）| Integrating
  group: 实验选项卡
  block_parameter: PlantTypeSpeed
  type: character vector
  values: '''Stable'' | ''Integrating'''
  default: '''Stable'''
- name: Plant Sign
  summary: 速度环被控对象的符号 Positive（默认）| Negative
  group: 实验选项卡
  block_parameter: PlantSignSpeed
  type: character vector
  values: '''Positive'' | ''Negative'''
  default: '''Positive'''
- name: Sine Amplitudes
  summary: 速度环 1 中正弦扰动的幅值（默认）| 标量 | 长度为 5 的向量
  group: 实验选项卡
  block_parameter: AmpSineSpeed
  type: scalar, vector of length 5
  default: '1'
- name: Plant Type
  summary: 磁通环被控对象的稳定性 Stable（默认）| Integrating
  group: 实验选项卡
  block_parameter: PlantTypeFlux
  type: character vector
  values: '''Stable'' | ''Integrating'''
  default: '''Stable'''
- name: Plant Sign
  summary: 磁通环被控对象的符号 Positive（默认）| Negative
  group: 实验选项卡
  block_parameter: PlantSignFlux
  type: character vector
  values: '''Positive'' | ''Negative'''
  default: '''Positive'''
- name: Sine Amplitudes
  summary: 磁链环 1 中正弦扰动的幅值（默认）| 标量 | 长度为 5 的向量
  group: 实验选项卡
  block_parameter: AmpSineFlux
  type: scalar, vector of length 5
  default: '1'
- name: Plant Type
  summary: 电流环被控对象的稳定性 Stable（默认）| Integrating
  group: 实验选项卡
  block_parameter: PlantTypeAllInner
  type: character vector
  values: '''Stable'' | ''Integrating'''
  default: '''Stable'''
- name: Plant Sign
  summary: 电流环被控对象的符号 Positive（默认）| Negative
  group: 实验选项卡
  block_parameter: PlantSignAllInner
  type: character vector
  values: '''Positive'' | ''Negative'''
  default: '''Positive'''
- name: Sine Amplitudes
  summary: 电流环 1 中正弦扰动的幅值（默认）| 标量 | 长度为 5 的向量
  group: 实验选项卡
  block_parameter: AmpSineAllInner
  type: scalar, vector of length 5
  default: '1'
- name: Plant Type
  summary: 外环被控对象的稳定性 Stable（默认）| Integrating
  group: 实验选项卡
  block_parameter: PlantTypeAllOuter
  type: character vector
  values: '''Stable'' | ''Integrating'''
  default: '''Stable'''
- name: Plant Sign
  summary: 外环被控对象的符号 Positive（默认）| Negative
  group: 实验选项卡
  block_parameter: PlantSignAllOuter
  type: character vector
  values: '''Positive'' | ''Negative'''
  default: '''Positive'''
- name: Sine Amplitudes
  summary: 外环 1 中正弦扰动的幅值（默认）| 标量 | 长度为 5 的向量
  group: 实验选项卡
  block_parameter: AmpSineAllOuter
  type: scalar, vector of length 5
  default: '1'
- name: Use external source for bandwidths
  summary: 为目​​标带宽提供外部信号 off (default) | on
  group: Block Tab
  block_parameter: UseExternalWc
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Use external source for target phase margins
  summary: 为目标相位裕度提供外部信号 off (default) | on
  group: Block Tab
  block_parameter: UseExternalPM
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Use external source for start/stops of experiment
  summary: 为整定实验的开始和停止提供外部信号 off (default) | on
  group: Block Tab
  block_parameter: UseExternalSourceStartStop
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Use external source for sine amplitudes
  summary: 为正弦扰动幅值提供外部信号 off（默认）| on
  group: Block Tab
  block_parameter: UseExternalAmpSine
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Data Type
  summary: 浮点精度 double（默认）| single
  group: Block Tab
  block_parameter: BlockDataType
  type: character vector
  values: '''double'' | ''single'''
  default: '''double'''
- name: Estimated phase margin achieved by tuned controllers
  summary: 最近整定回路所达到的相位裕度 off（默认）| on
  group: Block Tab
  block_parameter: UseExternalAchievedPM
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Plant frequency responses near bandwidth
  summary: 最近整定回路的估计频率响应 off（默认）| on
  group: Block Tab
  block_parameter: UseExternalFRD
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Plant nominal input and output
  summary: 标称工作点处的被控对象输入和输出 off（默认）| on
  group: Block Tab
  block_parameter: UseExternalU0
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Start/stop of autotuning process
  summary: 指示每个整定回路的实验开始和结束的信号 off（默认）| on
  group: Block Tab
  block_parameter: UseExternalActiveLoop
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Export to MATLAB
  summary: 将实验和整定结果发送到 MATLAB 工作区按钮
  group: Block Tab
```

### **Tune D-axis current loop** — 启用 d 轴电流环整定 `on`（默认）| `off`

使用此参数启用或禁用 d 轴电流环自整定。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TuneDaxisLoop` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认：** `'on'` |

### **Tune Q-axis current loop** — 启用 q 轴电流环整定 `on`（默认）| `off`

使用此参数启用或禁用 q 轴电流环自整定。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TuneQaxisLoop` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认：** `'on'` |

### **Tune speed loop** — 启用速度环整定 `on`（默认）| `off`

使用此参数启用或禁用速度环自整定。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TuneSpeedLoop` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认：** `'on'` |

### **Tune flux loop** — 启用磁通环整定 `on`（默认）| `off`

使用此参数启用或禁用磁通环自整定。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TuneSpeedLoop` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认：** `'on'` |

### **Use same settings for current loop controllers (D-axis + Q-axis)** — 为直轴和交轴电流环启用相同的整定和实验设置 `off`（默认）| `on`

选择此参数可为 d 轴和 q 轴电流环启用相同的整定和实验设置。启用后，该模块使用相同的控制器设置、目标带宽、相位裕度和其他实验设置来整定 d 轴和 q 轴电流环。

#### 程序化使用

|  |
| --- |
| **模块参数：** `UseSameSettingsInner` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **Use same settings for outer loop controllers (Speed + Flux)** — 为速度环和磁通环启用相同的整定和实验设置 `off`（默认）| `on`

选择此参数可为速度环和磁通环启用相同的整定和实验设置。启用后，该模块使用相同的控制器设置、目标带宽、相位裕度和其他实验设置来整定速度环和磁通环。

#### 程序化使用

|  |
| --- |
| **模块参数：** `UseSameSettingsOuter` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **Experiment sample time** — 频率响应估计实验的采样时间 –1（默认）| 正标量

指定模块执行的频率响应估计实验的采样时间，单位为秒。

默认情况下，实验采样时间设置为继承（–1），模块在每个回路上以继承的采样时间执行频率响应估计实验。使用此参数可以指定与整定和 PID 增益计算采样率不同的频率响应估计实验采样时间。对于您整定的每个回路，频率响应将按此参数中指定的采样时间进行估计。

当您为整定、实验和回路指定不同的采样时间时，您可以将 Simulink 配置为将每个模块速率视为单独的任务，从而为您的模型启用多任务执行。此多任务模式有助于提高硬件上的性能。有关详细信息，请参阅 Treat each discrete rate as a separate task。

#### 编程使用

|  |
| --- |
| **模块参数**：`TsExperiment` |
| **类型**：scalar |
| **Value** positive scalar |
| **默认值**：–1 (inherited) |

### Tuning Tab

### **Use different sample time for tuning** — 启用与回路 PID 控制器和实验不同的采样时间进行整定 `off`（默认）| `on`

默认情况下，模块对每个回路以您在该回路的 **Controller sample time (sec)** 参数中指定的相同采样时间运行整定。启用此参数可以以与您正在整定的 PID 控制器采样率以及模块执行的频率响应估计实验采样率不同的采样率运行整定。PID 增益整定算法计算量大，当您希望将模块部署到硬件并以快速采样时间整定控制器时，某些硬件可能无法在单个时间步内完成 PID 增益计算。为降低硬件吞吐量要求，请使用 **Tuning sample time (sec)** 参数指定比控制器采样时间更慢的整定采样时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`UseTuningTs` |
| **类型**：character vector |
| **Value** `'off'` | `'on'` |
| **默认值**：`'off'` |

### **Tuning sample time (sec)** — 整定算法的采样时间 0.2（默认）| 正标量

指定整定算法的采样时间，单位为秒。

如果您打算将模块部署到处理能力有限的硬件上，并希望以快速采样时间整定控制器，请指定一个使整定算法以比您正在整定的 PID 控制器更慢的速率运行的采样时间。对于您整定的每个回路，在频率响应估计实验结束后，控制器整定将按此参数中指定的采样时间进行。

#### 依赖关系

要启用此参数，请选择 **Use different sample time for tuning**。

#### 编程使用

|  |
| --- |
| **模块参数**：`TsTuning` |
| **类型**：scalar |
| **Value** positive scalar |
| **默认值**：0.2 |

#### D-axis Current Loop

### **Type** — D 轴电流回路 PID 控制器动作 `PI`（默认）| `PID` | `PIDF` | ...

指定与 d 轴电流控制回路关联的 PID 控制器类型。

控制器类型表示调节该回路的控制器中存在的动作。以下控制器类型可用于 PID 自动整定：

- `P` — 仅比例
- `I` — 仅积分
- `PI` — 比例和积分
- `PD` — 比例和微分
- `PDF` — 带微分滤波器的比例和微分
- `PID` — 比例、积分和微分
- `PIDF` — 带微分滤波器的比例、积分和微分

确保控制器类型与调节该回路的控制器匹配。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PIDTypeDaxis` |
| **类型：** 字符向量 |
| **值：** `'P'` | `'I'` | `'PI'` | `'PD'` | `'PDF'` | `'PID'` | `'PIDF'` |
| **默认值：** `'PI'` |

### **Form** — d 轴电流环 PID 控制器形式 `Parallel`（默认）| `Ideal`

指定与 d 轴电流控制环关联的 PID 控制器形式。

控制器形式决定了 PID 系数 *P*、*I*、*D* 和 *N* 的解释方式。

- `Parallel` — 在 `Parallel` 形式下，
  离散时间 PIDF 控制器的传递函数为

  C=P+IFi(z)+D[N1+NFd(z)]，

  其中 *Fi*(*z*) 和 *Fd*(*z*) 为积分器和滤波器公式（参见 `Integrator
  method` 和 `Filter method`）。

  其他控制器动作相当于将 *P*、
  *I* 或 *D* 设为零。
- `Ideal` — 在 `Ideal` 形式下，
  离散时间 PIDF 控制器的传递函数为

  C=P[1+IFi(z)+D(N1+NFd(z))]。

  其他控制器动作相当于将 *D* 设为零或将
  *I* 设为 `Inf`。（在理想形式下，控制器必须具有比例动作。）

确保控制器形式与调节该环路的控制器匹配。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PIDFormDaxis` |
| **类型：** 字符向量 |
| **值：** `'Parallel'` | `'Ideal'` |
| **默认值：** `'Parallel'` |

**可调：** 是

### **Controller sample time (sec)** — d 轴电流环 PID 控制器采样时间 0.001（默认）| 正标量 | –1

以秒为单位指定与 d 轴电流控制环关联的 PID 控制器的采样时间。此参数设置用于计算该环路 PID 控制器增益的采样时间。

要执行 PID 整定，该模块会测量高达目标带宽 10 倍频率的频率响应信息。为确保该频率低于奈奎斯特频率，目标带宽 *ωc* 必须满足 *ωc**Ts*
≤ 0.3，其中 *Ts*
*ωc* 是您通过 `Controller sample time (sec)` 参数指定的控制器采样时间。

确保控制器采样时间与调节该环路的控制器匹配。

#### 提示

如果您希望在应用中以不同采样时间运行已部署的模块，请将此参数设为 –1，并将该模块放入
Triggered Subsystem 中。
然后，以所需采样时间触发该子系统。如果您不打算在部署后更改采样时间，请指定固定且有限的采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TsDaxis` |
| **类型：** 标量 |
| **值** 正标量 | –1 |
| **默认值：** 0.001 |

### **Integrator method** — d 轴电流环控制器积分项的离散积分公式 `Forward Euler`（默认）| `Backward Euler` | `Trapezoidal`

指定控制器中积分项的离散积分公式。在离散时间下，该模块假定的 PID 控制器传递函数为

C=P+IFi(z)+D[N1+NFd(z)]，

为并联形式，或者为理想形式，

C=P[1+IFi(z)+D(N1+NFd(z))]。

对于控制器采样时间 *Ts*，`Integrator method` 参数按如下方式确定公式
*Fi*。

| 积分方法 | *Fi* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优势的更多信息，请参见 Discrete PID Controller 模块参考页。

确保控制器积分方法与调节该环路的控制器匹配。

#### 依赖关系

当控制器包含积分动作时，此参数启用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `IntegratorMethodDaxis` |
| **类型：** 字符向量 |
| **值：** `'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认值：** `'Forward Euler'` |

**可调：** 是

### **Filter method** — d 轴电流环控制器导数滤波项的离散积分公式 `Forward Euler`（默认）| `Backward Euler` | `Trapezoidal`

指定控制器中导数滤波项的离散积分公式。在离散时间下，该模块所假设的 PID 控制器传递函数为

C=P+IFi(z)+D[N1+NFd(z)],

为并联形式，或为理想形式，

C=P[1+IFi(z)+D(N1+NFd(z))].

对于控制器采样时间 *Ts*，`Filter method` 参数按如下方式确定公式 *Fd*。

| Filter method | *Fd* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优点的更多信息，请参见 Discrete PID Controller 模块参考页。

确保控制器导数滤波方法与调节该环路的控制器相匹配。

#### 依赖关系

当控制器包含带导数滤波项的微分作用时，此参数启用。

#### 编程使用

|  |
| --- |
| **模块参数**：`FilterMethodDaxis` |
| **类型**：character vector |
| **值**：`'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认值**：`'Forward Euler'` |

**Tunable:** Yes

### **Target bandwidth (rad/sec)** — d 轴电流环调谐响应的目标穿越频率 100（默认）| 正标量

目标带宽是调谐开环响应 *CP* 的 0 dB 增益穿越频率的目标值，其中 *P* 是与该环路相关的被控对象响应，*C* 是控制器响应。该穿越频率大致设定控制带宽。对于上升时间 *τ* 秒，目标带宽的一个良好估计值为 2/*τ* rad/sec。

为执行 PID 调谐，自动调谐器模块会测量最高达目标带宽 10 倍频率的频率响应信息。为确保该频率小于奈奎斯特频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* 是您通过 **Controller sample time (sec)** 参数指定的控制器采样时间。由于此条件，您可为调谐强制实现的最快上升时间约为 6.67*Ts*。如果该上升时间不满足您的设计目标，请考虑减小 *Ts*。

为获得最佳结果，请使用与初始 PID 控制器带宽相差约 10 倍以内的目标带宽。若要为更大的带宽变化调谐控制器，请使用较小的变化逐步调谐。

若要通过输入端口提供目标带宽，请在 Block 选项卡上选择 **Use external source for bandwidth**。

#### 编程使用

|  |
| --- |
| **模块参数**：`BandwidthDaxis` |
| **类型**：positive scalar |
| **默认值**：`100` |

### **Target phase margin (degrees)** — d 轴电流环目标最小相位裕度 60（默认）| 范围 0–90 的标量

指定与 d 轴电流控制环路相关的调谐开环响应在穿越频率处的目标最小相位裕度。

目标相位裕度反映调谐系统的期望鲁棒性。通常，选择约 45°–60° 范围内的值。一般来说，更高的相位裕度会减少超调，但可能限制响应速度。默认值 60° 倾向于平衡性能和鲁棒性，根据被控对象特性不同，可产生约 5–10% 的超调。

若要通过输入端口提供目标相位裕度，请在 Block 选项卡上选择 **Use external source for target phase margins**。

**Tunable:** Yes

#### 编程使用

|  |
| --- |
| **模块参数**：`TargetPMDaxis` |
| **类型**：scalar |
| **值**：0–90 |
| **默认值**：60 |

#### Q-axis Current Loop

### **Type** — q 轴电流环 PID 控制器动作 `PI`（默认）| `PID` | `PIDF` | ...

指定与 q 轴电流控制环关联的 PID 控制器类型。

控制器类型表示用于调节该环路的控制器中存在的动作。以下控制器类型可用于 PID 自整定：

- `P` — 仅比例
- `I` — 仅积分
- `PI` — 比例和积分
- `PD` — 比例和微分
- `PDF` — 带微分滤波器的比例和微分
- `PID` — 比例、积分和微分
- `PIDF` — 带微分滤波器的比例、积分和微分

确保控制器类型与调节该环路的控制器匹配。

#### 编程使用

|  |
| --- |
| **模块参数**：`PIDTypeQaxis` |
| **类型**：character vector |
| **值**：`'P'` | `'I'` | `'PI'` | `'PD'` | `'PDF'` | `'PID'` | `'PIDF'` |
| **默认值**：`'PI'` |

### **Form** — q 轴电流环 PID 控制器形式 `Parallel`（默认）| `Ideal`

指定与 q 轴电流控制环关联的 PID 控制器形式。

控制器形式决定 PID 系数 *P*、*I*、*D* 和 *N* 的解释方式。

- `Parallel` — 在 `Parallel` 形式中，离散时间 PIDF 控制器的传递函数为

  C=P+IFi(z)+D[N1+NFd(z)]，

  其中 *Fi*(*z*) 和 *Fd*(*z*) 是积分器和滤波器公式（参见 `Integrator
  method` 和 `Filter method`）。

  其他控制器动作相当于将 *P*、*I* 或 *D* 设为零。
- `Ideal` — 在 `Ideal` 形式中，离散时间 PIDF 控制器的传递函数为

  C=P[1+IFi(z)+D(N1+NFd(z))]。

  其他控制器动作相当于将 *D* 设为零或将 *I* 设为 `Inf`。（在 ideal 形式中，控制器必须具有比例动作。）

确保控制器形式与调节该环路的控制器匹配。

#### 编程使用

|  |
| --- |
| **模块参数**：`PIDFormQaxis` |
| **类型**：character vector |
| **值**：`'Parallel'` | `'Ideal'` |
| **默认值**：`'Parallel'` |

**Tunable:** Yes

### **Controller sample time (sec)** — q 轴电流环 PID 控制器采样时间 0.001（默认）| 正标量 | –1

以秒为单位指定与 q 轴电流控制环关联的 PID 控制器的采样时间。此参数设置用于计算该环路 PID 控制器增益的采样时间。

要执行 PID 整定，该模块会测量高达目标带宽 10 倍频率的频率响应信息。为确保该频率低于奈奎斯特频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* *ωc* 是您使用 `Controller sample time (sec)` 参数指定的控制器采样时间。

确保控制器采样时间与调节该环路的控制器匹配。

#### 提示

如果您希望在应用中以不同采样时间运行已部署的模块，请将此参数设置为 –1，并将该模块放入 Triggered Subsystem 中。然后，以所需采样时间触发该子系统。如果您不打算在部署后更改采样时间，请指定固定且有限的采样时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`TsQaxis` |
| **类型**：scalar |
| **Value** positive scalar | –1 |
| **默认值**：0.001 |

### **积分器方法** — 用于积分项 `Forward Euler`（默认）| `Backward Euler` | `Trapezoidal` 的 q 轴电流环控制器离散积分公式

指定控制器中积分项的离散积分公式。在离散时间下，该模块所假设的 PID 控制器传递函数为

C=P+IFi(z)+D[N1+NFd(z)]，

为并联形式，或为理想形式，

C=P[1+IFi(z)+D(N1+NFd(z))]。

对于控制器采样时间 *Ts*，`Integrator method` 参数按如下方式确定公式 *Fi*。

| 积分器方法 | *Fi* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优势的更多信息，请参阅 Discrete PID Controller 模块参考页。

确保控制器积分器方法与调节该环路的控制器匹配。

#### 依赖关系

当控制器包含积分作用时，此参数启用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `IntegratorMethodQaxis` |
| **类型：** 字符向量 |
| **值：** `'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认：** `'Forward Euler'` |

**可调：** 是

### **滤波器方法** — 用于微分滤波器项 `Forward Euler`（默认）| `Backward Euler` | `Trapezoidal` 的 q 轴电流环控制器离散积分公式

指定控制器中微分滤波器项的离散积分公式。在离散时间下，该模块所假设的 PID 控制器传递函数为

C=P+IFi(z)+D[N1+NFd(z)]，

为并联形式，或为理想形式，

C=P[1+IFi(z)+D(N1+NFd(z))]。

对于控制器采样时间 *Ts*，`Filter method` 参数按如下方式确定公式 *Fd*。

| 滤波器方法 | *Fd* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优势的更多信息，请参阅 Discrete PID Controller 模块参考页。

确保控制器微分滤波器方法与调节该环路的控制器匹配。

#### 依赖关系

当控制器包含带微分滤波器项的微分作用时，此参数启用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FilterMethodQaxis` |
| **类型：** 字符向量 |
| **值：** `'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认：** `'Forward Euler'` |

**可调：** 是

### **目标带宽 (rad/sec)** — 调优响应的 q 轴电流环目标穿越频率 100（默认）| 正标量

目标带宽是调优开环响应 *CP* 的 0 dB 增益穿越频率的目标值，其中 *P* 是与该环路相关的被控对象响应，*C* 是控制器响应。该穿越频率大致设定控制带宽。对于上升时间 *τ* 秒，目标带宽的一个良好估计值为 2/*τ* rad/sec。

为执行 PID 调优，自动调优器模块会测量最高达目标带宽 10 倍频率处的频率响应信息。为确保该频率低于奈奎斯特频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* 是您通过 **Controller sample time (sec)** 参数指定的控制器采样时间。由于此条件，您可为调优强制实现的最快上升时间约为 6.67*Ts*。如果该上升时间不满足您的设计目标，请考虑减小 *Ts*。

为获得最佳结果，请使用与初始 PID 控制器带宽相差约 10 倍以内的目标带宽。若要为带宽的更大变化调优控制器，请使用较小的变化逐步调优。

若要通过输入端口提供目标带宽，请在 Block 选项卡上选择 **Use external source for bandwidth**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `BandwidthQaxis` |
| **类型：** 正标量 |
| **默认：** `100` |

### **目标相位裕度（度）** — Q 轴电流环目标最小相位裕度 60（默认）| 0–90 范围内的标量

指定在穿越频率处与 q 轴电流控制环相关的已调开环响应的目标最小相位裕度。

目标相位裕度反映了已调系统所需的鲁棒性。通常，选择大约 45°–60° 范围内的值。一般来说，更高的相位裕度会减少超调，但可能会限制响应速度。默认值 60° 倾向于平衡性能和鲁棒性，根据被控对象的特性，会产生大约 5–10% 的超调。

要通过输入端口提供目标相位裕度，请在模块选项卡上，选择 **Use external source for target phase margins**。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **模块参数：** `TargetPMQaxis` |
| **类型：** 标量 |
| **值：** 0–90 |
| **默认：** 60 |

#### 速度环

### **类型** — 速度环 PID 控制器动作 `PI`（默认）| `PID` | `PIDF` | ...

指定与速度控制环相关的 PID 控制器类型。

控制器类型表示调节该环的控制器中存在哪些动作。以下控制器类型可用于 PID 自整定：

- `P` — 仅比例
- `I` — 仅积分
- `PI` — 比例和积分
- `PD` — 比例和微分
- `PDF` — 带微分滤波器的比例和微分
- `PID` — 比例、积分和微分
- `PIDF` — 带微分滤波器的比例、积分和微分

确保控制器类型与调节该环的控制器匹配。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PIDTypeSpeed` |
| **类型：** 字符向量 |
| **值：** `'P'` | `'I'` | `'PI'` | `'PD'` | `'PDF'` | `'PID'` | `'PIDF'` |
| **默认：** `'PI'` |

### **形式** — 速度环 PID 控制器形式 `Parallel`（默认）| `Ideal`

指定与速度控制环相关的 PID 控制器形式。

控制器形式决定 PID 系数 *P*、*I*、*D* 和 *N* 的解释。

- `Parallel` — 在 `Parallel` 形式中，离散时间 PIDF 控制器的传递函数为

  C=P+IFi(z)+D[N1+NFd(z)]，

  其中 *Fi*(*z*) 和 *Fd*(*z*) 是积分器和滤波器公式（参见 `Integrator
  method` 和 `Filter method`）。

  其他控制器动作相当于将 *P*、*I* 或 *D* 设置为零。
- `Ideal` — 在 `Ideal` 形式中，离散时间 PIDF 控制器的传递函数为

  C=P[1+IFi(z)+D(N1+NFd(z))]。

  其他控制器动作相当于将 *D* 设置为零或将 *I* 设置为 `Inf`。（在理想形式中，控制器必须具有比例动作。）

确保控制器形式与调节该环的控制器匹配。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PIDFormSpeed` |
| **类型：** 字符向量 |
| **值：** `'Parallel'` | `'Ideal'` |
| **默认：** `'Parallel'` |

**可调：** 是

### **控制器采样时间（秒）** — 速度环 PID 控制器采样时间 0.1（默认）| 正标量 | –1

指定与速度控制环相关的 PID 控制器的采样时间（以秒为单位）。此参数设置用于计算该环 PID 控制器增益的采样时间。

要执行 PID 整定，模块会测量高达目标带宽 10 倍频率的频率响应信息。为确保该频率小于奈奎斯特频率，目标带宽 *ωc* 必须满足 *ωc**Ts*
≤ 0.3，其中 *Ts*
*ωc* 是您使用 `Controller sample time (sec)` 参数指定的控制器采样时间。

确保控制器采样时间与调节该环的控制器匹配。

#### 提示

如果要在应用程序中以不同的采样时间运行已部署的模块，请将此参数设置为 –1，并将该模块放入 Triggered Subsystem 中。
然后，以所需的采样时间触发该子系统。如果部署后不打算更改采样时间，请指定一个固定且有限的采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TsSpeed` |
| **类型：** scalar |
| **值** positive scalar | –1 |
| **默认：** 0.1 |

### **Integrator method** — 速度环控制器积分项离散积分公式 `Forward Euler`（默认） | `Backward Euler` | `Trapezoidal`

指定控制器中积分项的离散积分公式。在离散时间下，该模块所假设的 PID 控制器传递函数为

C=P+IFi(z)+D[N1+NFd(z)]，

为并联形式，或为理想形式，

C=P[1+IFi(z)+D(N1+NFd(z))]。

对于控制器采样时间 *Ts*，`Integrator method` 参数按如下方式确定公式 *Fi*。

| Integrator method | *Fi* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优点的更多信息，请参阅 Discrete PID Controller 模块参考页。

确保控制器积分方法与调节该环路的控制器相匹配。

#### 依赖关系

当控制器包含积分作用时，此参数启用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `IntegratorMethodSpeed` |
| **类型：** character vector |
| **值：** `'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认：** `'Forward Euler'` |

**可调：** 是

### **Filter method** — 速度环控制器微分滤波项离散积分公式 `Forward Euler`（默认） | `Backward Euler` | `Trapezoidal`

指定控制器中微分滤波项的离散积分公式。在离散时间下，该模块所假设的 PID 控制器传递函数为

C=P+IFi(z)+D[N1+NFd(z)]，

为并联形式，或为理想形式，

C=P[1+IFi(z)+D(N1+NFd(z))]。

对于控制器采样时间 *Ts*，`Filter method` 参数按如下方式确定公式 *Fd*。

| Filter method | *Fd* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优点的更多信息，请参阅 Discrete PID Controller 模块参考页。

确保控制器微分滤波方法与调节该环路的控制器相匹配。

#### 依赖关系

当控制器包含带微分滤波项的微分作用时，此参数启用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FilterMethodSpeed` |
| **类型：** character vector |
| **值：** `'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认：** `'Forward Euler'` |

**可调：** 是

### **目标带宽 (rad/sec)** — 调谐响应 1 的速度环目标穿越频率（默认）| 正标量

目标带宽是调谐开环响应 *CP* 的 0 dB 增益穿越频率的目标值，其中 *P* 是与该环相关联的被控对象响应，*C* 是控制器响应。该穿越频率大致设定了控制带宽。对于上升时间 *τ* 秒，目标带宽的良好估计值为 2/*τ* rad/sec。

要执行 PID 调谐，自动调谐器模块会测量高达目标带宽 10 倍频率的频率响应信息。为确保该频率小于奈奎斯特频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* 是您通过 **Controller sample time (sec)** 参数指定的控制器采样时间。由于此条件，您可以强制用于调谐的最快上升时间约为 6.67*Ts*。如果该上升时间不满足您的设计目标，请考虑减小 *Ts*。

为获得最佳结果，请使用与初始 PID 控制器带宽相差约 10 倍以内的目标带宽。要为带宽的较大变化调谐控制器，请使用较小的变化进行增量调谐。

要通过输入端口提供目标带宽，请在 Block 选项卡上选择 **Use external source for bandwidth**。

#### 编程使用

|  |
| --- |
| **模块参数**：`BandwidthSpeed` |
| **类型**：positive scalar |
| **默认值**：`1` |

### **目标相位裕度 (degrees)** — 速度环目标最小相位裕度 60（默认）| 范围 0–90 的标量

为与速度控制环相关联的调谐开环响应在穿越频率处指定目标最小相位裕度。

目标相位裕度反映了调谐系统所需的鲁棒性。通常，选择约 45°–60° 范围内的值。一般来说，较高的相位裕度会减少超调，但可能会限制响应速度。默认值 60° 倾向于平衡性能和鲁棒性，根据您被控对象的特性，产生约 5–10% 的超调。

要通过输入端口提供目标相位裕度，请在 Block 选项卡上选择 **Use external source for target phase margins**。

**Tunable:** Yes

#### 编程使用

|  |
| --- |
| **模块参数**：`TargetPMSpeed` |
| **类型**：scalar |
| **值**：0–90 |
| **默认值**：60 |

#### Flux Loop

### **Type** — 磁通环 PID 控制器动作 `PI`（默认）| `PID` | `PIDF` | ...

指定与磁通控制环相关联的 PID 控制器类型。

控制器类型指示调节该环的控制器中存在哪些动作。以下控制器类型可用于 PID 自动调谐：

- `P` — 仅比例
- `I` — 仅积分
- `PI` — 比例和积分
- `PD` — 比例和微分
- `PDF` — 带微分滤波器的比例和微分
- `PID` — 比例、积分和微分
- `PIDF` — 带微分滤波器的比例、积分和微分

确保控制器类型与调节该环的控制器匹配。

#### 编程使用

|  |
| --- |
| **模块参数**：`PIDTypeFlux` |
| **类型**：character vector |
| **值**：`'P'` | `'I'` | `'PI'` | `'PD'` | `'PDF'` | `'PID'` | `'PIDF'` |
| **默认值**：`'PI'` |

### **Form** — 磁通环 PID 控制器形式 `Parallel`（默认）| `Ideal`

指定与您的磁通控制环相关联的 PID 控制器形式。

控制器形式决定了 PID 系数 *P*、*I*、*D* 和 *N* 的解释方式。

- `Parallel` — 在 `Parallel` 形式中，
  离散时间 PIDF 控制器的传递函数为

  C=P+IFi(z)+D[N1+NFd(z)]，

  其中 *Fi*(*z*) 和 *Fd*(*z*) 是积分器和滤波器公式（参见 `Integrator
  method` 和 `Filter method`）。

  其他控制器动作相当于将 *P*、
  *I* 或 *D* 设为零。
- `Ideal` — 在 `Ideal` 形式中，
  离散时间 PIDF 控制器的传递函数为

  C=P[1+IFi(z)+D(N1+NFd(z))]。

  其他控制器动作相当于将 *D* 设为零或将
  *I* 设为 `Inf`。（在理想形式中，控制器
  必须具有比例动作。）

确保控制器形式与调节该环的控制器匹配。

#### 编程使用

|  |
| --- |
| **模块参数**：`PIDFormFlux` |
| **类型**：character vector |
| **值**：`'Parallel'` | `'Ideal'` |
| **默认值**：`'Parallel'` |

**Tunable:** Yes

### **Controller sample time (sec)** — 磁通环 PID 控制器采样时间 0.1（默认）| 正标量 | –1

以秒为单位指定与磁通控制环相关联的 PID 控制器的采样时间。此参数设置用于计算该环 PID
控制器增益的采样时间。

要执行 PID 整定，该模块测量高达目标带宽 10 倍频率的频率响应信息。为确保该频率小于奈奎斯特
频率，目标带宽 *ωc* 必须满足 *ωc**Ts*
≤ 0.3，其中 *Ts*
*ωc* 是您通过 `Controller sample time (sec)` 参数指定的控制器采样时间。

确保控制器采样时间与调节该环的控制器匹配。

#### 提示

如果您希望在应用程序中以不同的采样时间运行部署的模块，请将此参数设置为 –1，并将该模块放入
Triggered Subsystem 中。
然后，以所需的采样时间触发该子系统。如果您
不打算在部署后更改采样时间，请指定一个固定
且有限的采样时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`TsFlux` |
| **类型**：scalar |
| **Value** positive scalar | –1 |
| **默认值**：0.1 |

### **Integrator method** — 磁通环控制器积分项的离散积分公式 `Forward Euler`（默认）| `Backward Euler` | `Trapezoidal`

指定控制器中积分项的离散积分公式。在
离散时间中，该模块假设的 PID 控制器传递函数为

C=P+IFi(z)+D[N1+NFd(z)]，

为并联形式，或为理想形式，

C=P[1+IFi(z)+D(N1+NFd(z))]。

对于控制器采样时间 *Ts*，
`Integrator method` 参数按如下方式确定公式
*Fi*。

| Integrator method | *Fi* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优势的更多信息，请参见 Discrete PID Controller 模块参考页。

确保控制器积分器方法与调节该环的控制器匹配。

#### 依赖关系

当控制器包含积分
动作时，此参数启用。

#### 编程使用

|  |
| --- |
| **模块参数**：`IntegratorMethodFlux` |
| **类型**：character vector |
| **值**：`'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认值**：`'Forward Euler'` |

**Tunable:** Yes

### **Filter method** — 导数滤波器项的磁通环控制器离散积分公式 `Forward Euler`（默认）| `Backward Euler` | `Trapezoidal`

指定控制器中导数滤波器项的离散积分公式。在离散时间下，该模块所假设的 PID 控制器传递函数为

C=P+IFi(z)+D[N1+NFd(z)],

并联形式，或理想形式，

C=P[1+IFi(z)+D(N1+NFd(z))].

对于控制器采样时间 *Ts*，`Filter method` 参数按如下方式确定公式 *Fd*。

| Filter method | *Fd* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优势的更多信息，请参阅 Discrete PID Controller 模块参考页。

确保控制器导数滤波器方法与调节该环路的控制器相匹配。

#### 依赖关系

当控制器包含带导数滤波器项的微分作用时，此参数启用。

#### 编程使用

|  |
| --- |
| **模块参数**：`FilterMethodFlux` |
| **类型**：character vector |
| **值**：`'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认值**：`'Forward Euler'` |

**Tunable:** Yes

### **Target bandwidth (rad/sec)** — 磁通环整定响应的目标穿越频率 1（默认）| 正标量

目标带宽是整定后开环响应 *CP* 的 0 dB 增益穿越频率的目标值，其中 *P* 是与该环路相关的被控对象响应，*C* 是控制器响应。该穿越频率大致设定了控制带宽。对于上升时间 *τ* 秒，目标带宽的一个良好估计值为 2/*τ* rad/sec。

为执行 PID 整定，自整定模块会测量高达目标带宽 10 倍频率处的频率响应信息。为确保该频率低于奈奎斯特频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* 是您通过 **Controller sample time (sec)** 参数指定的控制器采样时间。由于此条件，您可以为整定强制实现的最快上升时间约为 6.67*Ts*。如果该上升时间不满足您的设计目标，请考虑减小 *Ts*。

为获得最佳结果，请使用与初始 PID 控制器带宽相差约 10 倍以内的目标带宽。若要为带宽的更大变化整定控制器，请使用较小的变化进行增量整定。

若要通过输入端口提供目标带宽，请在 Block 选项卡上选择 **Use external source for bandwidth**。

#### 编程使用

|  |
| --- |
| **模块参数**：`BandwidthFlux` |
| **类型**：positive scalar |
| **默认值**：`1` |

### **Target phase margin (degrees)** — 磁通环目标最小相位裕度 60（默认）| 0–90 范围内的标量

为磁通控制环在穿越频率处的整定开环响应指定目标最小相位裕度。

目标相位裕度反映了整定系统所需的鲁棒性。通常，选择约 45°–60° 范围内的值。一般来说，较高的相位裕度会减少超调，但可能限制响应速度。默认值 60° 倾向于平衡性能和鲁棒性，根据被控对象特性，产生约 5–10% 的超调。

若要通过输入端口提供目标相位裕度，请在 Block 选项卡上选择 **Use external source for target phase margins**。

**Tunable:** Yes

#### 编程使用

|  |
| --- |
| **模块参数**：`TargetPMFlux` |
| **类型**：scalar |
| **值**：0–90 |
| **默认值**：60 |

#### Current Loops (Q-axis + D-axis)

### **Type** — 电流环 PID 控制器动作 `PI`（默认）| `PID` | `PIDF` | ...

指定与电流控制环关联的 PID 控制器类型。

控制器类型表示调节该环路的控制器中包含哪些动作。以下控制器类型可用于 PID 自整定：

- `P` — 仅比例
- `I` — 仅积分
- `PI` — 比例和积分
- `PD` — 比例和微分
- `PDF` — 比例和带微分滤波器的微分
- `PID` — 比例、积分和微分
- `PIDF` — 比例、积分和带微分滤波器的微分

确保控制器类型与调节该环路的控制器匹配。

#### 编程使用

|  |
| --- |
| **模块参数**：`PIDTypeAllInner` |
| **类型**：character vector |
| **值**：`'P'` | `'I'` | `'PI'` | `'PD'` | `'PDF'` | `'PID'` | `'PIDF'` |
| **默认值**：`'PI'` |

### **Form** — 电流环 PID 控制器形式 `Parallel`（默认）| `Ideal`

指定与电流控制环关联的 PID 控制器形式。

控制器形式决定了 PID 系数 *P*、*I*、*D* 和 *N* 的解释方式。

- `Parallel` — 在 `Parallel` 形式下，离散时间 PIDF 控制器的传递函数为

  C=P+IFi(z)+D[N1+NFd(z)]，

  其中 *Fi*(*z*) 和 *Fd*(*z*) 是积分器和滤波器公式（参见 `Integrator
  method` 和 `Filter method`）。

  其他控制器动作相当于将 *P*、*I* 或 *D* 设为零。
- `Ideal` — 在 `Ideal` 形式下，离散时间 PIDF 控制器的传递函数为

  C=P[1+IFi(z)+D(N1+NFd(z))]。

  其他控制器动作相当于将 *D* 设为零或将 *I* 设为 `Inf`。（在理想形式下，控制器必须具有比例动作。）

确保控制器形式与调节该环路的控制器匹配。

#### 编程使用

|  |
| --- |
| **模块参数**：`PIDFormAllInner` |
| **类型**：character vector |
| **值**：`'Parallel'` | `'Ideal'` |
| **默认值**：`'Parallel'` |

**Tunable:** Yes

### **Controller sample time (sec)** — 电流环 PID 控制器采样时间 0.001（默认）| 正标量 | –1

以秒为单位指定与电流控制环关联的 PID 控制器的采样时间。此参数设置用于计算该环路 PID 控制器增益的采样时间。

要执行 PID 整定，该模块测量高达目标带宽 10 倍频率的频率响应信息。为确保该频率小于奈奎斯特频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* 是您通过 `Controller sample time (sec)` 参数指定的控制器采样时间。

确保控制器采样时间与调节该环路的控制器匹配。

#### 提示

如果您希望在应用中以不同采样时间运行部署的模块，请将此参数设为 –1，并将该模块放入 Triggered Subsystem 中。然后，以所需的采样时间触发该子系统。如果您不打算在部署后更改采样时间，请指定一个固定且有限的采样时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`TsAllInner` |
| **类型**：scalar |
| **Value** positive scalar | –1 |
| **默认值**：0.001 |

### **Integrator method** — 电流环控制器积分项离散积分公式 `Forward Euler`（默认）| `Backward Euler` | `Trapezoidal`

指定控制器中积分项的离散积分公式。在离散时间下，该模块所假设的 PID 控制器传递函数为

C=P+IFi(z)+D[N1+NFd(z)]，

为并联形式，或为理想形式，

C=P[1+IFi(z)+D(N1+NFd(z))]。

对于控制器采样时间 *Ts*，`Integrator method` 参数按如下方式确定公式 *Fi*。

| Integrator method | *Fi* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优点的更多信息，请参阅 Discrete PID Controller 模块参考页。

确保控制器积分方法与调节该环路的控制器相匹配。

#### 依赖关系

当控制器包含积分作用时，此参数启用。

#### 编程使用

|  |
| --- |
| **模块参数**：`IntegratorMethodAllInner` |
| **类型**：character vector |
| **值**：`'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认值**：`'Forward Euler'` |

**Tunable:** Yes

### **Filter method** — 电流环控制器微分滤波项离散积分公式 `Forward Euler`（默认）| `Backward Euler` | `Trapezoidal`

指定控制器中微分滤波项的离散积分公式。在离散时间下，该模块所假设的 PID 控制器传递函数为

C=P+IFi(z)+D[N1+NFd(z)]，

为并联形式，或为理想形式，

C=P[1+IFi(z)+D(N1+NFd(z))]。

对于控制器采样时间 *Ts*，`Filter method` 参数按如下方式确定公式 *Fd*。

| Filter method | *Fd* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优点的更多信息，请参阅 Discrete PID Controller 模块参考页。

确保控制器微分滤波方法与调节该环路的控制器相匹配。

#### 依赖关系

当控制器包含带微分滤波项的微分作用时，此参数启用。

#### 编程使用

|  |
| --- |
| **模块参数**：`FilterMethodAllInner` |
| **类型**：character vector |
| **值**：`'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认值**：`'Forward Euler'` |

**Tunable:** Yes

### **Target bandwidth (rad/sec)** — 电流环整定响应的目标穿越频率 100（默认）| 正标量

目标带宽是整定后开环响应 *CP* 的 0 dB 增益穿越频率的目标值，其中 *P* 是与该环路相关的被控对象响应，*C* 是控制器响应。该穿越频率大致设定了控制带宽。对于上升时间 *τ* 秒，目标带宽的一个良好估计值为 2/*τ* rad/sec。

为执行 PID 整定，自动整定模块会测量最高达目标带宽 10 倍频率处的频率响应信息。为确保该频率低于奈奎斯特频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* 是您通过 **Controller sample time (sec)** 参数指定的控制器采样时间。由于此条件，您可为整定强制实现的最快上升时间约为 6.67*Ts*。如果该上升时间不满足您的设计目标，请考虑减小 *Ts*。

为获得最佳结果，请使用与初始 PID 控制器带宽相差约 10 倍以内的目标带宽。若要为更大的带宽变化整定控制器，请使用较小的变化逐步整定。

若要通过输入端口提供目标带宽，请在 Block 选项卡上选择 **Use external source for bandwidth**。

#### 编程使用

|  |
| --- |
| **模块参数**：`BandwidthAllInner` |
| **类型**：positive scalar |
| **默认值**：`1` |

### **目标相位裕度（度）** — 电流环目标最小相位裕度 60（默认）| 0–90 范围内的标量

指定与电流控制环相关的整定开环响应在穿越频率处的目标最小相位裕度。

目标相位裕度反映了整定系统期望的鲁棒性。通常，选择大约 45°–60° 范围内的值。一般来说，较高的相位裕度会减少超调，但可能限制响应速度。默认值 60° 倾向于平衡性能和鲁棒性，根据被控对象特性，可产生约 5–10% 的超调。

要通过输入端口提供目标相位裕度，请在 Block 选项卡上选择 **Use external source for target phase margins**。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **模块参数：** `TargetPMAllInner` |
| **类型：** 标量 |
| **值：** 0–90 |
| **默认：** 60 |

#### 外环（速度 + 磁通）

### **类型** — 外环 PID 控制器动作 `PI`（默认）| `PID` | `PIDF` | ...

指定与外环控制环相关的 PID 控制器类型。

控制器类型表示调节该环的控制器中存在的动作。以下控制器类型可用于 PID 自整定：

- `P` — 仅比例
- `I` — 仅积分
- `PI` — 比例和积分
- `PD` — 比例和微分
- `PDF` — 带微分滤波器的比例和微分
- `PID` — 比例、积分和微分
- `PIDF` — 带微分滤波器的比例、积分和微分

确保控制器类型与调节该环的控制器匹配。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PIDTypeAllOuter` |
| **类型：** 字符向量 |
| **值：** `'P'` | `'I'` | `'PI'` | `'PD'` | `'PDF'` | `'PID'` | `'PIDF'` |
| **默认：** `'PI'` |

### **形式** — 外环 PID 控制器形式 `Parallel`（默认）| `Ideal`

指定与外环控制环相关的 PID 控制器形式。

控制器形式决定 PID 系数 *P*、*I*、*D* 和 *N* 的解释。

- `Parallel` — 在 `Parallel` 形式中，离散时间 PIDF 控制器的传递函数为

  C=P+IFi(z)+D[N1+NFd(z)]，

  其中 *Fi*(*z*) 和 *Fd*(*z*) 是积分器和滤波器公式（参见 `Integrator method` 和 `Filter method`）。

  其他控制器动作相当于将 *P*、*I* 或 *D* 设置为零。
- `Ideal` — 在 `Ideal` 形式中，离散时间 PIDF 控制器的传递函数为

  C=P[1+IFi(z)+D(N1+NFd(z))]。

  其他控制器动作相当于将 *D* 设置为零或将 *I* 设置为 `Inf`。（在理想形式中，控制器必须具有比例动作。）

确保控制器形式与调节该环的控制器匹配。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PIDFormAllOuter` |
| **类型：** 字符向量 |
| **值：** `'Parallel'` | `'Ideal'` |
| **默认：** `'Parallel'` |

**可调：** 是

### **控制器采样时间（秒）** — 外环 PID 控制器采样时间 0.1（默认）| 正标量 | –1

指定与外环控制环相关的 PID 控制器的采样时间，单位为秒。此参数设置用于计算该环 PID 控制器增益的采样时间。

要执行 PID 整定，模块会测量高达目标带宽 10 倍频率的频率响应信息。为确保该频率小于奈奎斯特频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* *ωc* 是您使用 `Controller sample time (sec)` 参数指定的控制器采样时间。

确保控制器采样时间与调节该环的控制器匹配。

#### 提示

如果要在应用程序中以不同的采样时间运行已部署的模块，请将此参数设置为 –1，并将该模块放入触发子系统（Triggered Subsystem）中。
然后，以所需的采样时间触发该子系统。如果部署后不打算更改采样时间，请指定一个固定且有限的采样时间。

#### 编程用法

|  |
| --- |
| **模块参数：** `TsAllOuter` |
| **类型：** 标量 |
| **值** 正标量 | –1 |
| **默认值：** 0.1 |

### **Integrator method** — 外环控制器积分项离散积分公式 `Forward Euler`（默认） | `Backward Euler` | `Trapezoidal`

指定控制器中积分项的离散积分公式。在离散时间下，该模块所假设的 PID 控制器传递函数为

C=P+IFi(z)+D[N1+NFd(z)]，

为并联形式，或为理想形式，

C=P[1+IFi(z)+D(N1+NFd(z))]。

对于控制器采样时间 *Ts*，`Integrator method` 参数按如下方式确定公式 *Fi*。

| Integrator method | *Fi* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优点的更多信息，请参阅 Discrete PID Controller 模块参考页。

确保控制器积分方法与调节该环路的控制器相匹配。

#### 依赖关系

当控制器包含积分作用时，此参数启用。

#### 编程用法

|  |
| --- |
| **模块参数：** `IntegratorMethodAllOuter` |
| **类型：** 字符向量 |
| **值：** `'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认值：** `'Forward Euler'` |

**可调：** 是

### **Filter method** — 外环控制器微分滤波器项离散积分公式 `Forward Euler`（默认） | `Backward Euler` | `Trapezoidal`

指定控制器中微分滤波器项的离散积分公式。在离散时间下，该模块所假设的 PID 控制器传递函数为

C=P+IFi(z)+D[N1+NFd(z)]，

为并联形式，或为理想形式，

C=P[1+IFi(z)+D(N1+NFd(z))]。

对于控制器采样时间 *Ts*，`Filter method` 参数按如下方式确定公式 *Fd*。

| Filter method | *Fd* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优点的更多信息，请参阅 Discrete PID Controller 模块参考页。

确保控制器微分滤波器方法与调节该环路的控制器相匹配。

#### 依赖关系

当控制器包含带微分滤波器项的微分作用时，此参数启用。

#### 编程用法

|  |
| --- |
| **模块参数：** `FilterMethodAllOuter` |
| **类型：** 字符向量 |
| **值：** `'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认值：** `'Forward Euler'` |

**可调：** 是

### **目标带宽 (rad/sec)** — 整定响应的外环目标穿越频率 1（默认）| 正标量

目标带宽是整定开环响应 *CP* 的 0 dB 增益穿越频率的目标值，其中 *P* 是与该环路相关的被控对象响应，*C* 是控制器响应。该穿越频率大致设定了控制带宽。对于上升时间 *τ* 秒，目标带宽的良好估计值为 2/*τ* rad/sec。

要执行 PID 整定，自整定模块会测量高达目标带宽 10 倍频率的频率响应信息。为确保该频率小于奈奎斯特频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* 是您通过 **控制器采样时间 (sec)** 参数指定的控制器采样时间。由于此条件，您可以为整定强制的最快上升时间约为 6.67*Ts*。如果该上升时间不满足您的设计目标，请考虑减小 *Ts*。

为获得最佳结果，请使用与初始 PID 控制器带宽相差约 10 倍以内的目标带宽。要为更大的带宽变化整定控制器，请使用较小的变化进行增量整定。

要通过输入端口提供目标带宽，请在 Block 选项卡上，选择 **使用外部源提供带宽**。

#### 编程使用

|  |
| --- |
| **模块参数**：`BandwidthAllOuter` |
| **类型**：positive scalar |
| **默认值**：`1` |

### **目标相位裕度 (degrees)** — 外环目标最小相位裕度 60（默认）| 范围 0–90 的标量

为与穿越频率处外控制环路相关的整定开环响应指定目标最小相位裕度。

目标相位裕度反映了整定系统所需的鲁棒性。通常，选择约 45°–60° 范围内的值。一般来说，更高的相位裕度会减少超调，但可能限制响应速度。默认值 60° 倾向于平衡性能和鲁棒性，根据被控对象的特性，产生约 5–10% 的超调。

要通过输入端口提供目标相位裕度，请在 Block 选项卡上，选择 **使用外部源提供目标相位裕度**。

**Tunable:** Yes

#### 编程使用

|  |
| --- |
| **模块参数**：`TargetPMAllOuter` |
| **类型**：scalar |
| **值**：0–90 |
| **默认值**：60 |

### 实验选项卡

#### 实验启动/停止

### **D 轴电流环启动时间 (sec)** — 指定直轴电流环整定实验启动时间 `1`（默认）

指定 d 轴电流环整定实验启动时的仿真时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`StartTimeDaxis` |
| **类型**：positive scalar |
| **默认值**：1 |

### **D 轴电流环实验持续时间 (sec)** — 指定直轴电流环整定实验持续时间 `0.05`（默认）

指定 d 轴电流环整定实验持续时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`DurationDaxis` |
| **类型**：positive scalar |
| **默认值**：0.05 |

### **Q 轴电流环启动时间 (sec)** — 指定交轴电流环整定实验启动时间 `1.1`（默认）

指定 q 轴电流环整定实验启动时的仿真时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`StartTimeQaxis` |
| **类型**：positive scalar |
| **默认值**：1.1 |

### **Q 轴电流环实验持续时间 (sec)** — 指定交轴电流环整定实验持续时间 `0.05`（默认）

指定 q 轴电流环整定实验持续时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`DurationQaxis` |
| **类型**：positive scalar |
| **默认值**：0.05 |

### **速度环启动时间 (sec)** — 指定速度环整定实验启动时间 `2`（默认）

指定速度环整定实验启动时的仿真时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `StartTimeSpeed` |
| **类型：** positive scalar |
| **默认值：** 2 |

### **Speed loop experiment duration (sec)** — 指定速度环整定实验持续时间 `3`（默认值）

指定速度环整定实验持续时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DurationSpeed` |
| **类型：** positive scalar |
| **默认值：** 3 |

### **Flux loop start time (sec)** — 指定磁链环整定实验开始时间 `6`（默认值）

指定磁链整定实验开始时的仿真时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `StartTimeFlux` |
| **类型：** positive scalar |
| **默认值：** 6 |

### **Flux loop experiment duration (sec)** — 指定磁链环整定实验持续时间 `3`（默认值）

指定磁链环整定实验持续时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DurationFlux` |
| **类型：** positive scalar |
| **默认值：** 3 |

#### 环路实验设置

### **Experiment Mode** — 正弦扰动信号类型 `Superposition`（默认值）| `Sinestream` | **PRBS** *（自 R2024a 起）*

指定每个频率处的扰动是以顺序正弦（**Sinestream**）、同时正弦（**Superposition**）还是伪随机二进制序列（**PRBS**）方式施加。

- **Sinestream** — 在此模式下，模块分别在每个频率处施加扰动。有关用于估计的 sinestream 信号的详细信息，请参阅 Sinestream Input Signals (Simulink Control Design)。
- **Superposition** — 在此模式下，扰动信号一次性包含所有指定的频率。对于在频率向量 *ω* = [*ω*1, … , *ωN*] 处、幅值 *A* = [*A*1, … , *AN*] 下的频率响应估计，扰动信号为：

  Δu=∑iAisin(ωit)。
- **PRBS** — 一种确定性伪随机二进制序列，在两个值之间切换，具有类似白噪声的特性。与使用 sinestream 输入信号相比，PRBS 信号可减少总估计时间，同时产生相当的估计结果。PRBS 信号可用于估计通信和电力电子系统的频率响应。有关详细信息，请参阅 PRBS Input Signals (Simulink Control Design)。*（自 R2024a 起）*

**Sinestream** 模式可以更准确，也可以具有更低的侵入性，因为扰动的总大小永远不会超过 **Sine Amplitudes** 参数指定的值。然而，由于 sinestream 扰动的顺序特性，您添加的每个频率点都会增加推荐的实验时间（有关详细信息，请参阅 **start/stop** 输入端口）。因此，在 **Superposition** 模式下，估计实验通常要快得多，且结果令人满意。

与 superposition 输入信号相比，sinestream 信号可减少执行时间，但估计频率响应也需要更长时间。当处理能力有限且希望减少执行时间时，使用 sinestream 信号进行频率响应估计很有用。

要覆盖相似的频率范围，**PRBS** 模式下的实验长度通常比其他两种模式短得多。然而，结果的速度和质量之间存在权衡。*（自 R2024a 起）*

#### 程序化使用

|  |
| --- |
| **模块参数：** `ExperimentMode` |
| **类型：** character vector |
| **值：** `'Superposition'` | `'Sinestream'` | `'PRBS'` |
| **默认值：** `'Superposition'` |

#### D 轴电流环

### **Plant Type** — 直轴电流被控对象稳定性 `Stable`（默认值）| `Integrating`

指定与 d 轴电流控制环相关的被控对象是稳定还是积分。如果被控对象具有一个或多个积分器，请选择 `Integrating`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PlantTypeDaxis` |
| **类型：** 字符向量 |
| **值：** `'Stable'` | `'Integrating'` |
| **默认值：** `'Stable'` |

### **被控对象符号** — 直轴电流被控对象符号 `Positive`（默认）| `Negative`

指定与 d 轴电流控制环路关联的被控对象是正还是负。如果在标称工作点处被控对象输入的正变化导致被控对象输出的正变化，则指定 `Positive`。否则，指定负。对于稳定被控对象，被控对象的符号是被控对象直流增益的符号。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PlantSignDaxis` |
| **类型：** 字符向量 |
| **值：** `'Positive'` | `'Negative'` |
| **默认值：** `'Positive'` |

### **正弦幅值** — 直轴电流环路中正弦扰动的幅值 1（默认）| 标量 | 长度为 5 的向量

在实验期间，模块将与环路关联的被控对象注入频率为 [1/10, 1/3, 1, 3, 10]*ωc* 的正弦信号，其中 *ωc* 是用于整定的目标带宽。使用 **正弦幅值** 指定每个注入信号的幅值。指定：

- 标量值以在每个频率处注入相同的幅值
- 长度为 5 的向量以在 [1/10, 1/3, 1, 3, 10]*ωc* 的每个频率处指定不同的幅值

在具有典型目标带宽的典型被控对象中，实验频率处被控对象响应的幅值变化不大。在这种情况下，您可以使用标量值在所有频率处施加相同幅值的扰动。但是，如果您知道响应在频率范围内急剧衰减，请考虑减小低频输入的幅值并增大高频输入的幅值。当所有被控对象响应具有可比幅值时，对于估计实验在数值上更好。

扰动幅值必须：

- 足够大，使扰动克服被控对象执行器中的任何死区，并产生高于噪声水平的响应
- 足够小，使被控对象在标称工作点附近的近似线性区域内运行，并避免使被控对象输入或输出饱和

当 **实验模式** 为 **叠加** 时，正弦信号被叠加。因此，扰动至少可以与所有幅值之和一样大。确保最大可能的扰动在被控对象执行器的范围内。使执行器饱和可能会在估计的频率响应中引入误差。

要通过输入端口提供正弦幅值，请在模块选项卡上，选择 **使用正弦幅值的外部源**。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **模块参数：** `AmpSineDaxis` |
| **类型：** 标量，长度为 5 的向量 |
| **默认值：** 1 |

#### Q 轴电流环路

### **被控对象类型** — 交轴电流被控对象的稳定性 `Stable`（默认）| `Integrating`

指定与 q 轴电流控制环路关联的被控对象是稳定还是积分。如果被控对象具有一个或多个积分器，请选择 `Integrating`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PlantTypeQaxis` |
| **类型：** 字符向量 |
| **值：** `'Stable'` | `'Integrating'` |
| **默认值：** `'Stable'` |

### **被控对象符号** — 交轴电流被控对象符号 `Positive`（默认）| `Negative`

指定与 q 轴电流控制环路关联的被控对象是正还是负。如果在标称工作点处被控对象输入的正变化导致被控对象输出的正变化，则指定 `Positive`。否则，指定负。对于稳定被控对象，被控对象的符号是被控对象直流增益的符号。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PlantSignQaxis` |
| **类型：** 字符向量 |
| **值：** `'Positive'` | `'Negative'` |
| **默认值：** `'Positive'` |

### **Sine Amplitudes** — 交轴电流环 1 中正弦扰动的幅值（默认）| 标量 | 长度为 5 的向量

在实验过程中，模块会以频率 [1/10, 1/3, 1, 3, 10]*ωc* 向与该环关联的被控对象注入正弦信号，其中 *ωc* 是用于整定的目标带宽。使用 **Sine Amplitudes** 指定每个注入信号的幅值。指定：

- 标量值，以在每个频率处注入相同的幅值
- 长度为 5 的向量，以在 [1/10, 1/3, 1, 3, 10]*ωc* 的每个频率处指定不同的幅值

在具有典型目标带宽的典型被控对象中，实验频率处被控对象响应的幅值不会发生很大变化。在这种情况下，您可以使用标量值在所有频率处施加相同的幅值扰动。但是，如果您知道响应在该频率范围内急剧衰减，请考虑降低较低频率输入的幅值并增加较高频率输入的幅值。当所有被控对象响应具有可比较的幅值时，估计实验在数值上会更好。

扰动幅值必须：

- 足够大，使扰动能够克服被控对象执行器中的任何死区，并产生高于噪声水平的响应
- 足够小，使被控对象在标称工作点附近的近似线性区域内运行，并避免使被控对象输入或输出饱和

当 **Experiment mode** 为 **Superposition** 时，正弦信号会叠加。因此，扰动至少可以与所有幅值之和一样大。确保最大可能的扰动在被控对象执行器的范围内。使执行器饱和可能会在估计的频率响应中引入误差。

要通过输入端口提供正弦幅值，请在 Block 选项卡上选择 **Use external source for sine amplitudes**。

**Tunable:** Yes

#### 编程使用

|  |
| --- |
| **模块参数**：`AmpSineQaxis` |
| **类型**：scalar, vector of length 5 |
| **默认值**：1 |

#### Speed Loop

### **Plant Type** — 速度环被控对象的稳定性 `Stable`（默认）| `Integrating`

指定与速度控制环关联的被控对象是稳定还是积分。如果被控对象具有一个或多个积分器，请选择 `Integrating`。

#### 编程使用

|  |
| --- |
| **模块参数**：`PlantTypeSpeed` |
| **类型**：character vector |
| **值**：`'Stable'` | `'Integrating'` |
| **默认值**：`'Stable'` |

### **Plant Sign** — 速度环被控对象的符号 `Positive`（默认）| `Negative`

指定与速度控制环关联的被控对象是正还是负。如果在标称工作点处被控对象输入的正变化导致被控对象输出的正变化，请指定 `Positive`。否则，指定 negative。对于稳定被控对象，被控对象的符号是被控对象 DC 增益的符号。

#### 编程使用

|  |
| --- |
| **模块参数**：`PlantSignSpeed` |
| **类型**：character vector |
| **值**：`'Positive'` | `'Negative'` |
| **默认值**：`'Positive'` |

### **Sine Amplitudes** — 速度环 1 中正弦扰动的幅值（默认）| 标量 | 长度为 5 的向量

在实验过程中，模块将与环路相关的被控对象以频率 [1/10, 1/3, 1, 3, 10]*ωc* 注入正弦信号，其中 *ωc* 是整定的目标带宽。使用 **Sine Amplitudes** 指定每个注入信号的幅值。指定：

- 标量值以在每个频率注入相同的幅值
- 长度为 5 的向量以在 [1/10, 1/3, 1, 3, 10]*ωc* 的每个频率指定不同的幅值

在具有典型目标带宽的典型被控对象中，实验频率下被控对象响应的幅值不会有很大变化。在这种情况下，您可以使用标量值在所有频率上施加相同幅值的扰动。但是，如果您知道响应在频率范围内急剧衰减，请考虑减小低频输入的幅值并增大高频输入的幅值。当所有被控对象响应具有可比幅值时，估计实验在数值上会更好。

扰动幅值必须：

- 足够大，使扰动能够克服被控对象执行器中的任何死区，并产生高于噪声水平的响应
- 足够小，使被控对象在标称工作点附近的近似线性区域内运行，并避免使被控对象输入或输出饱和

当 **Experiment mode** 为 **Superposition** 时，正弦信号叠加。因此，扰动至少可以与所有幅值之和一样大。确保最大可能的扰动在被控对象执行器的范围内。使执行器饱和可能会在估计的频率响应中引入误差。

要通过输入端口提供正弦幅值，请在 Block 选项卡上，选择 **Use external source for sine amplitudes**。

**Tunable:** Yes

#### 编程使用

|  |
| --- |
| **模块参数**：`AmpSineSpeed` |
| **类型**：scalar, vector of length 5 |
| **默认值**：1 |

#### Flux Loop

### **Plant Type** — 磁通环被控对象的稳定性 `Stable`（默认）| `Integrating`

指定与磁通控制环相关的被控对象是稳定的还是积分的。如果被控对象具有一个或多个积分器，请选择 `Integrating`。

#### 编程使用

|  |
| --- |
| **模块参数**：`PlantTypeFlux` |
| **类型**：character vector |
| **值**：`'Stable'` | `'Integrating'` |
| **默认值**：`'Stable'` |

### **Plant Sign** — 磁通环被控对象的符号 `Positive`（默认）| `Negative`

指定与磁通控制环相关的被控对象是正的还是负的。如果在标称工作点处被控对象输入的正变化导致被控对象输出的正变化，请指定 `Positive`。否则，指定 negative。对于稳定被控对象，被控对象的符号是被控对象直流增益的符号。

#### 编程使用

|  |
| --- |
| **模块参数**：`PlantSignFlux` |
| **类型**：character vector |
| **值**：`'Positive'` | `'Negative'` |
| **默认值**：`'Positive'` |

### **Sine Amplitudes** — 磁链环 1 中正弦扰动的幅值（默认）| 标量 | 长度为 5 的向量

在实验过程中，模块将与环路相关的被控对象以频率 [1/10, 1/3, 1, 3, 10]*ωc* 注入正弦信号，其中 *ωc* 是整定的目标带宽。使用 **Sine Amplitudes** 指定每个注入信号的幅值。指定：

- 标量值以在每个频率注入相同的幅值
- 长度为 5 的向量以在 [1/10, 1/3, 1, 3, 10]*ωc* 的每个频率指定不同的幅值

在具有典型目标带宽的典型被控对象中，实验频率下被控对象响应的幅值变化不大。在这种情况下，您可以使用标量值在所有频率上施加相同幅值的扰动。但是，如果您知道响应在频率范围内急剧衰减，请考虑减小低频输入的幅值并增大高频输入的幅值。当所有被控对象响应具有可比幅值时，估计实验在数值上更好。

扰动幅值必须：

- 足够大，使扰动克服被控对象执行器中的任何死区，并产生高于噪声水平的响应
- 足够小，使被控对象在标称工作点附近的近似线性区域内运行，并避免使被控对象输入或输出饱和

当 **Experiment mode** 为 **Superposition** 时，正弦信号被叠加。因此，扰动至少可以与所有幅值之和一样大。确保最大可能的扰动在被控对象执行器的范围内。使执行器饱和可能会在估计的频率响应中引入误差。

要通过输入端口提供正弦幅值，请在 Block 选项卡上选择 **Use external source for sine amplitudes**。

**Tunable:** Yes

#### 编程使用

|  |
| --- |
| **模块参数**：`AmpSineFlux` |
| **类型**：scalar, vector of length 5 |
| **默认值**：1 |

#### Current Loops (D-axis + Q-axis)

### **Plant Type** — 电流环被控对象的稳定性 `Stable`（默认）| `Integrating`

指定与电流控制环相关的被控对象是稳定的还是积分的。如果被控对象具有一个或多个积分器，请选择 `Integrating`。

#### 编程使用

|  |
| --- |
| **模块参数**：`PlantTypeAllInner` |
| **类型**：character vector |
| **值**：`'Stable'` | `'Integrating'` |
| **默认值**：`'Stable'` |

### **Plant Sign** — 电流环被控对象的符号 `Positive`（默认）| `Negative`

指定与电流控制环相关的被控对象是正的还是负的。如果在标称工作点处被控对象输入的正变化导致被控对象输出的正变化，请指定 `Positive`。否则，指定 negative。对于稳定被控对象，被控对象的符号是被控对象直流增益的符号。

#### 编程使用

|  |
| --- |
| **模块参数**：`PlantSignAllInner` |
| **类型**：character vector |
| **值**：`'Positive'` | `'Negative'` |
| **默认值**：`'Positive'` |

### **Sine Amplitudes** — 电流环 1 中正弦扰动的幅值（默认）| 标量 | 长度为 5 的向量

在实验过程中，该模块将与环路相关的被控对象注入频率为 [1/10, 1/3, 1, 3, 10]*ωc* 的正弦信号，其中 *ωc* 是用于整定的目标带宽。使用 **Sine Amplitudes** 指定每个注入信号的幅值。指定：

- 标量值以在每个频率注入相同的幅值
- 长度为 5 的向量以在 [1/10, 1/3, 1, 3, 10]*ωc* 的每个频率指定不同的幅值

在具有典型目标带宽的典型被控对象中，实验频率下被控对象响应的幅值变化不大。在这种情况下，您可以使用标量值在所有频率上施加相同幅值的扰动。但是，如果您知道响应在频率范围内急剧衰减，请考虑减小低频输入的幅值并增大高频输入的幅值。当所有被控对象响应具有可比幅值时，估计实验在数值上会更好。

扰动幅值必须：

- 足够大，使扰动克服被控对象执行器中的任何死区，并产生高于噪声水平的响应
- 足够小，使被控对象在标称工作点附近的近似线性区域内运行，并避免使被控对象输入或输出饱和

当 **Experiment mode** 为 **Superposition** 时，正弦信号被叠加。因此，扰动至少可以与所有幅值之和一样大。确保最大可能的扰动在被控对象执行器的范围内。使执行器饱和可能会在估计的频率响应中引入误差。

要通过输入端口提供正弦幅值，请在 Block 选项卡上选择 **Use external source for sine amplitudes**。

**Tunable:** Yes

#### 编程使用

|  |
| --- |
| **模块参数**：`AmpSineAllInner` |
| **类型**：scalar, vector of length 5 |
| **默认值**：1 |

#### Outer Loops (Speed + Flux)

### **Plant Type** — 外环被控对象的稳定性 `Stable`（默认）| `Integrating`

指定与外环控制回路相关的被控对象是稳定的还是积分的。如果被控对象具有一个或多个积分器，请选择 `Integrating`。

#### 编程使用

|  |
| --- |
| **模块参数**：`PlantTypeAllOuter` |
| **类型**：character vector |
| **值**：`'Stable'` | `'Integrating'` |
| **默认值**：`'Stable'` |

### **Plant Sign** — 外环被控对象的符号 `Positive`（默认）| `Negative`

指定与外环控制回路相关的被控对象是正还是负。如果在标称工作点处被控对象输入的正变化导致被控对象输出的正变化，请指定 `Positive`。否则，指定 negative。对于稳定被控对象，被控对象的符号是被控对象 DC 增益的符号。

#### 编程使用

|  |
| --- |
| **模块参数**：`PlantSignAllOuter` |
| **类型**：character vector |
| **值**：`'Positive'` | `'Negative'` |
| **默认值**：`'Positive'` |

### **Sine Amplitudes** — 外环 1 中正弦扰动的幅值（默认）| 标量 | 长度为 5 的向量

在实验过程中，该模块以频率 [1/10, 1/3, 1, 3, 10]*ωc* 向与回路相关的被控对象注入正弦信号，其中 *ωc* 是整定的目标带宽。使用 **Sine Amplitudes** 指定每个注入信号的幅值。指定一个：

- 标量值，以在每个频率处注入相同的幅值
- 长度为 5 的向量，以在 [1/10, 1/3, 1, 3, 10]*ωc* 的每个频率处指定不同的幅值

在具有典型目标带宽的典型被控对象中，被控对象在实验频率处的响应幅值不会有很大变化。在这种情况下，您可以使用标量值在所有频率处施加相同幅值的扰动。但是，如果您知道响应在频率范围内急剧衰减，请考虑减小低频输入的幅值并增大高频输入的幅值。当所有被控对象响应具有可比较的幅值时，对于估计实验来说数值上更好。

扰动幅值必须：

- 足够大，使扰动能够克服被控对象执行器中的任何死区，并产生高于噪声水平的响应
- 足够小，使被控对象在标称工作点附近的近似线性区域内运行，并避免使被控对象输入或输出饱和

当 **Experiment mode** 为 **Superposition** 时，正弦信号被叠加。因此，扰动至少可以与所有幅值之和一样大。确保最大可能的扰动在被控对象执行器的范围内。使执行器饱和可能会在估计的频率响应中引入误差。

要通过输入端口提供正弦幅值，请在 Block 选项卡上选择 **Use external source for sine amplitudes**。

**Tunable:** Yes

#### 编程使用

|  |
| --- |
| **模块参数**：`AmpSineAllOuter` |
| **类型**：scalar, vector of length 5 |
| **默认值**：1 |

### Block Tab

### **Use external source for bandwidths** — 为目​​标带宽提供外部信号 off (default) | on

选择此参数以启用模块的 `bandwidth` 输入端口。您可以在此端口处指定模块所整定的所有回路的目标带宽。当此参数被禁用时，请在模块参数处指定目标带宽。有关更多详细信息，请参阅 `bandwidth` 端口描述。

#### 编程使用

|  |
| --- |
| **模块参数**：`UseExternalWc` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Use external source for target phase margins** — 为目标相位裕度提供外部信号 off (default) | on

选择此参数以启用模块的 `target PM` 输入端口。您可以在此端口处指定模块所整定的所有回路的目标相位裕度。当此参数被禁用时，请在模块参数处指定目标相位裕度。有关更多详细信息，请参阅 `target PM` 端口描述。

#### 编程使用

|  |
| --- |
| **模块参数**：`UseExternalPM` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Use external source for start/stops of experiment** — 为整定实验的开始和停止提供外部信号 off (default) | on

选择此参数以启用模块的 `start/stop` 和 `ActiveLoop` 输入端口。您可以在此端口处指定实验的开始和停止以及模块所整定的回路。当此参数被禁用时，请在模块参数处指定整定实验的开始时间和持续时间。有关更多详细信息，请参阅 `start/stop` 和 `ActiveLoop` 端口描述。

#### 编程使用

|  |
| --- |
| **模块参数**：`UseExternalSourceStartStop` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Use external source for sine amplitudes** — 为正弦扰动幅值提供外部信号 off（默认）| on

选择此参数以启用模块的 `sine Amp` 输入端口。
您可以在此端口为模块所整定的所有回路指定正弦扰动幅值。当此参数禁用时，请在模块参数中提供正弦幅值。有关更多详细信息，请参阅 `sine Amp` 端口描述。

#### 编程使用

|  |
| --- |
| **模块参数**：`UseExternalAmpSine` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Data Type** — 浮点精度 `double`（默认）| `single`

根据仿真环境或硬件要求指定浮点精度。

#### 编程使用

|  |
| --- |
| **模块参数**：`BlockDataType` |
| **类型**：character vector |
| **值**：`'double'` | `'single'` |
| **默认值**：`'double'` |

### **Estimated phase margin achieved by tuned controllers** — 最近整定回路所达到的相位裕度 off（默认）| on

选择此参数以启用模块的 `estimated PM` 输出端口。模块返回最近整定回路的已整定控制器所达到的相位裕度。当此参数禁用时，您可以通过 **Export to MATLAB** 参数查看整定结果。有关更多详细信息，请参阅 `estimated PM` 端口描述。

#### 编程使用

|  |
| --- |
| **模块参数**：`UseExternalAchievedPM` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Plant frequency responses near bandwidth** — 最近整定回路的估计频率响应 off（默认）| on

选择此参数以启用模块的 `frd` 输出端口。模块返回最近整定回路的已整定控制器所达到的相位裕度。当此参数禁用时，您可以通过 **Export to MATLAB** 参数查看整定结果。有关更多详细信息，请参阅 `frd` 端口描述。

#### 编程使用

|  |
| --- |
| **模块参数**：`UseExternalFRD` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Plant nominal input and output** — 标称工作点处的被控对象输入和输出 off（默认）| on

选择此参数以启用模块的 `nominal` 输出端口。模块返回最近整定回路在标称工作点处的被控对象输入和输出。当此参数禁用时，您可以通过 **Export to MATLAB** 参数查看整定结果。有关更多详细信息，请参阅端口描述。

#### 编程使用

|  |
| --- |
| **模块参数**：`UseExternalU0` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Start/stop of autotuning process** — 指示每个整定回路的实验开始和结束的信号 off（默认）| on

选择此参数以启用模块的 `loop start/stops` 输出端口。模块返回一个信号，指示模块所整定的每个回路的自整定实验开始和结束的时间。当此参数禁用时，您可以通过 **Export to MATLAB** 参数查看整定结果。有关更多详细信息，请参阅 `loop start/stops` 端口描述。

#### 编程使用

|  |
| --- |
| **模块参数**：`UseExternalActiveLoop` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Export to MATLAB** — 将实验和整定结果发送到 MATLAB 工作区按钮

当您点击此按钮时，该模块会在 MATLAB® 工作区中创建一个包含实验和整定结果的结构体。该结构体 `FOCTuningResult` 包含模块所整定的每个环路的整定结果。

- `Daxis` — D 轴电流环整定结果
- `Qaxis` — Q 轴电流环整定结果
- `Speed` — 速度环整定结果
- `Flux` — 磁通环整定结果

对于模块所整定的每个环路，结果包含以下字段：

- `P`、`I`、`D`、`N` — 整定后的 PID 增益。该结构体包含您所整定的控制器类型所需的相应字段。例如，如果您整定的是 PI 控制器，则该结构体包含 `P` 和 `I`，但不包含 `D` 和 `N`。
- `TargetBandwidth` — 您在模块的 `Target bandwidth (rad/sec)` 参数中指定的值。
- `TargetPhaseMargin` — 您在模块的 `Target phase margin (degrees)` 参数中指定的值。
- `EstimatedPhaseMargin` — 整定后系统所达到的估计相位裕度。
- `Controller` — 整定后的 PID 控制器，以 `pid`（用于并联形式）或 `pidstd`（用于理想形式）模型对象返回。
- `Plant` — 估计的被控对象，以 `frd` 模型对象返回。该 `frd` 包含在实验频率 [1/10, 1/3, 1, 3, 10]*ωc* 处获得的响应数据。
- `PlantNominal` — 实验开始时标称工作点处的被控对象输入和输出，以包含字段 `u`（输入）和 `y`（输出）的结构体形式指定。

您可以在仿真运行期间导出到 MATLAB 工作区，包括在外部模式下运行时。
## 所属库

Motor Control Blockset / Controls / Controllers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

该模块生成的代码可能占用较多资源。对于实时应用，建议将代码部署到快速原型硬件上，例如 Speedgoat 实时目标机。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

## 版本历史

**在 R2020a 中引入**

### R2024a：支持 PRBS 输入信号

磁场定向控制自整定模块现在支持使用伪随机二进制序列（PRBS）输入信号进行估计。PRBS 信号是一种周期性、确定性的信号，具有类似白噪声的特性，在两个值之间切换。与使用正弦流或叠加输入信号相比，PRBS 信号可减少总估计时间，同时产生相当的估计结果。PRBS 信号对于估计通信和电力电子应用的频率响应非常有用。

## 描述

在磁场定向控制应用中自动且顺序地整定多个 PID 控制回路

磁场定向控制自整定模块允许您在磁场定向控制 (FOC) 应用中实时自动整定 PID 控制回路。有关磁场定向控制的更多信息，请参阅磁场定向控制 (FOC)。

您可以自动整定与以下回路相关的 PID 控制器：

- 直轴 (d 轴) 电流回路
- 交轴 (q 轴) 电流回路
- 速度回路
- 磁通回路

对于模块整定的每个回路，磁场定向控制自整定模块在闭环中执行自整定实验，而无需与该回路相关的参数模型。该模块允许您指定控制回路的整定顺序。当一个回路的整定实验正在运行时，该模块对其他回路没有影响。在实验过程中，该模块：

1. 向与该回路相关的被控对象注入测试信号，以采集被控对象输入输出数据并实时估计频率响应。测试信号是叠加在被控对象输入上的正弦扰动信号的组合。
2. 在实验结束时，根据目标带宽附近估计的被控对象频率响应来整定 PID 控制器参数。
3. 在模块输出端写入更新后的 PID 增益，允许您将新增益传输到现有控制器并验证闭环性能。

您可以使用磁场定向控制自整定模块来整定 FOC 结构中现有的 PID 控制器。如果您没有初始 PID 控制器，可以使用估计控制增益和使用实用函数工作流来获取它们。然后，您可以使用磁场定向控制自整定模块进行细化或重新整定。

如果您拥有 Simulink® Coder™ 等代码生成产品，您可以生成在硬件上实现整定算法的代码，让您实时整定，使用或不使用 Simulink 来管理自整定过程。

如果您在 Simulink 中使用 Motor Control Blockset™ 对电机进行了建模，并且拥有带有 PID 控制器的初始 FOC 结构，您可以针对建模的电机执行闭环 PID 自整定。这样做可以让您预览被控对象响应，并在实时整定控制器之前调整 PID 自整定的设置。

该模块支持使用 Simulink Coder、Embedded Coder® 和 Simulink PLC Coder™ 进行代码生成。它不支持使用 HDL Coder™ 进行代码生成。对于实时应用，请将生成的代码部署到快速原型硬件上，例如 Speedgoat® 实时目标机。

有关使用磁场定向控制自整定模块的更多信息，请参阅如何使用磁场定向控制自整定模块。

该模块需要 Simulink Control Design™ 软件。
