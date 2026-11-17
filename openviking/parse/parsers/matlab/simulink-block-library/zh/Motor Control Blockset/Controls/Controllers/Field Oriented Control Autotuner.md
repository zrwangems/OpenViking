---
type: simulink-block
title: 'Field Oriented Control Autotuner'
family: 'controls'
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

### 输入

### **PIDout daxis** — 来自直轴电流控制器的标量信号

此端口接受 d 轴控制器 `PID_daxis` 的输出，该输出是调节电机 d 轴电流的 PID 控制器的输出。该控制器生成 d 轴电压参考 `Vd_ref`，而 FOC autotuner 模块生成用于 d 轴电流环调谐实验期间使用的扰动。

显示 d 轴电流环与 autotuner 连接的图

#### 依赖项

要启用此端口，请选择 **Tune D-axis current loop**。

**数据类型：** `single` | `double`

### **measured feedback daxis** — 测得的直轴电流（标量）

此端口接受从测得的（传感或估计的）电机电流中获得的 d 轴电流。

#### 依赖项

要启用此端口，请选择 **Tune D-axis current loop**。

**数据类型：** `single` | `double`

### **PIDout qaxis** — 来自交轴电流控制器的标量信号

此端口接受 q 轴控制器 `PID_qaxis` 的输出，该输出是调节电机 q 轴电流的 PID 控制器的输出。该控制器生成 q 轴电压参考 `Vq_ref`，而 FOC autotuner 模块生成用于 q 轴电流环调谐实验期间使用的扰动。

显示 q 轴电流环与 autotuner 连接的图

#### 依赖项

要启用此端口，请选择 **Tune Q-axis current loop**。

**数据类型：** `single` | `double`

### **measured feedback qaxis** — 测得的交轴电流（标量）

此端口接受从测得的（传感或估计的）电机电流中获得的 q 轴电流。

#### 依赖项

要启用此端口，请选择 **Tune Q-axis current loop**。

**数据类型：** `single` | `double`

### **PIDout spd** — 来自速度控制器的标量信号

此端口接受速度控制器 `PID_speed` 的输出，该输出是调节电机速度的 PID 控制器的输出。该控制器生成 q 轴电流参考 `Iq_ref`，而 FOC autotuner 模块生成用于速度环调谐实验期间使用的扰动。

显示速度环与 autotuner 连接的图

#### 依赖项

要启用此端口，请选择 **Tune speed loop**。

**数据类型：** `single` | `double`

### **measured feedback spd** — 测得的速度（标量）

此端口接受来自电机的测得（传感或估计的）速度。

#### 依赖项

要启用此端口，请选择 **Tune speed loop**。

**数据类型：** `single` | `double`

### **PIDout flux** — 来自磁通控制器的标量信号

此端口接受磁通控制器 `PID_flux` 的输出，该输出是调节电机磁通的 PID 控制器的输出。该控制器生成 d 轴电流参考 `Id_ref`，而 FOC autotuner 模块生成用于磁通环调谐实验期间使用的扰动。

显示磁通环与 autotuner 连接的图

对于永磁同步电机（PMSM），不存在磁通环控制器，因为转子磁通固定且 `Id_ref` 设置为零。在某些应用中，您可以提供负的 `Id_ref` 值来实现弱磁控制，并以更高的电流为代价获得更高的转子速度。

#### 依赖项

要启用此端口，请选择 **Tune flux loop**。

**数据类型：** `single` | `double`

### **measured feedback flux** — 测得的磁通（标量）

此端口接受来自电机的测得（传感或估计的）磁通。

#### 依赖项

要启用此端口，请选择 **Tune flux loop**。

**数据类型：** `single` | `double`

### **start/stop** — 启动和停止自动调谐实验（标量）

若要外部启动和停止自动调谐过程，请在 `start/stop` 端口和 `ActiveLoop` 端口提供信号。

- 当信号值从负值或零变为正值时，实验启动。
- 当信号值从正值变为负值或零时，实验停止。

在实验持续期间，对于每个环，模块在标称工作点附近、与该环关联的被控对象输入处注入正弦扰动，以采集输入输出数据并估计频率响应。当实验停止时，模块基于在目标带宽附近估计的被控对象频率响应计算 PID 增益。

当实验未运行时，模块不会在被控对象输入处注入任何扰动。在此状态下，模块对被控对象或控制器行为没有影响。

通常，您可以使用从 0 变为 1 的信号来启动实验，并使用从 1 变为 0 的信号来停止实验。配置 `start/stop` 信号时，请考虑以下事项。

- 当电机处于期望的平衡工作点时启动实验。使用初始控制器将电机驱动到该工作点。
- 在实验期间避免电机上的任何输入或输出扰动。如果您现有的闭环系统具有良好的扰动抑制能力，则实验可以处理小扰动。否则，大扰动可能使被控对象输出失真，并降低频率响应估计的准确性。
- 让实验运行足够长时间，以便算法在其探测的所有频率上采集足够的数据以进行良好估计。有两种方法可以确定何时停止实验：

  - 提前确定实验持续时间。实验持续时间的保守估计为叠加实验模式下的 200/*ωc*，或 sinestream 实验模式下的 550/*ωc*，其中 *ωc* 是您的目标带宽。
  - 观察 `convergence` 输出处的信号，并在信号稳定在 100% 附近时停止实验。

  对于 **PRBS** 模式，基于指定的 **Target bandwidth** 和 **Controller sample time** 值，模块对话框会在 **实验** 选项卡的 **描述** 部分显示推荐的实验长度。过早停止实验可能导致不正确的调谐结果。*(since R2024a)*
- 当您停止实验时，模块会计算调谐后的 PID 增益，并更新 `pid gains` 端口处的信号。

您可以配置适合您的应用的任何逻辑来控制实验的启动和停止时间。`start/stop` 信号与 `ActiveLoop` 一起指定。`ActiveLoop` 采用整数值 1 到 4，并指定要调谐的环。

或者，如果您在仿真或外部模式下进行调谐，可以在模块参数中指定调谐实验序列、开始时间和持续时间。

#### 依赖项

要启用此端口，在 Block 选项卡上的 **参数源** 下，选择 **Use external source for start/stop of experiment**。

**数据类型：** `single` | `double`

### **ActiveLoop** — 指定自动调谐实验的活动环（标量）

在提供调谐实验启动和停止时间的外部源时，设置 `ActiveLoop` 值以指定要调谐的环。

| `ActiveLoop` 值 | 要调谐的环 |
| --- | --- |
| `1` | `D-axis` 电流环 |
| `2` | `Q-axis` 电流环 |
| `3` | `Speed` 环 |
| `4` | `Flux` 环 |

您可以配置适合您的应用的任何逻辑，与 `start/stop` 端口一起控制环调谐实验运行的顺序和时间。`ActiveLoop` 采用 1 到 4 的整数值，并指定要调谐的环。任何其他数字都将导致不发生调谐，无论 `start/stop` 信号如何。例如，当您在 `ActiveLoop` 处提供常量值 2，并且 `start/stop` 处的信号上升时，模块会启动 q 轴电流环的调谐实验。

或者，您可以在模块参数中指定调谐实验序列、开始时间和持续时间。

#### 依赖项

要启用此端口，在 Block 选项卡上的 **参数源** 下，选择 **Use external source for start/stop of experiment**。

**数据类型：** `single` | `double`

### **bandwidth** — 用于调谐的目标带宽 标量 | 向量 | bus

为每个要调谐的环提供 `Target bandwidth (rad/sec)` 参数的值。如果要调谐多个环，您可以将带宽指定为向量或 bus，其条目按以下顺序对应于各环的目标带宽：

- D-axis 电流环
- Q-axis 电流环
- 速度环
- 磁通环

向量信号必须指定为 N×1 或 1×N 信号，或者如果指定为 bus，则必须具有 N 个元素，其中 N 是要调谐的环数。例如，如果您要调谐 q 轴电流环和速度环，并在此端口指定向量 [5000, 200]，则模块会以目标带宽 5000 rad/sec 调谐 q 轴电流控制器，并以目标带宽 200 rad/sec 调谐速度环控制器。

如果您要调谐多个环，并在此端口指定标量值，则模块使用相同的目标带宽来调谐所有控制器。为了有效级联控制，内环（d 轴和 q 轴）必须比外环（磁通和速度）响应快得多。因此，在调谐多个环时，您必须将目标带宽作为向量或 bus 信号提供。

或者，您可以在模块参数中为各个环指定目标带宽。有关如何选择带宽的详细信息，请参阅该参数描述。

#### 依赖项

要启用此端口，在 Block 选项卡上的 **参数源** 下，选择 **Use external source for bandwidth**。

**数据类型：** `single` | `double`

### **target PM** — 用于调谐的目标相位裕度 标量 | 向量 | bus

为每个要调谐的环提供 `Target phase margin (degrees)` 参数的值。如果要调谐多个环，您可以将 `target PM` 指定为向量或 bus，其条目按以下顺序对应于各环的目标相位裕度：

- D-axis 电流环
- Q-axis 电流环
- 速度环
- 磁通环

向量信号必须指定为 N×1 或 1×N 信号，或者如果指定为 bus，则必须具有 N 个元素，其中 N 是要调谐的环数。例如，如果您要调谐 q 轴电流环和速度环，并在此端口指定向量 [60, 45]，则模块会以目标相位裕度 60 degrees 调谐 q 轴电流控制器，并以目标相位裕度 45 degrees 调谐速度环控制器。

如果您要调谐多个环，并在此端口指定标量值，则模块使用相同的目标相位裕度来调谐所有控制器。

或者，您可以在模块参数中为各个环指定目标相位裕度。有关如何选择目标相位裕度的详细信息，请参阅该参数描述。

#### 依赖项

要启用此端口，在 Block 选项卡上的 **参数源** 下，选择 **Use external source for target phase margin**。

**数据类型：** `single` | `double`

### **sine Amp** — 注入正弦扰动信号的幅值 向量 | 矩阵

为每个要调谐的环提供 `Sine Amplitudes` 参数的值。指定以下之一：

- 长度为 5 的向量，用于在 [1/10, 1/3, 1, 3, 10]*ωc* 的每个点指定不同幅值，其中 *ωc* 是用于调谐的目标带宽。
- N×5 矩阵，其中 N 是要调谐的环数。每一行条目长度必须为 5，以在 [1/10, 1/3, 1, 3, 10]*ωc* 的每个点指定不同幅值。

如果您要调谐多个环，并在此端口指定长度为 5 的向量，则模块会为所有环在该环对应的 [1/10, 1/3, 1, 3, 10]*ωc* 的每个点使用指定的幅值。

或者，您可以在模块参数中为各个环指定正弦扰动幅值。有关详细信息，请参阅参数描述。

#### 依赖项

要启用此端口，在 Block 选项卡上的 **参数源** 下，选择 **Use external source for sine amplitudes**。

**数据类型：** `single` | `double`

### 输出

### **perturbation daxis** — 直轴电流输入扰动（标量）

用于估计与 d 轴电流控制环关联的频率响应数据模型的扰动信号输入。通过使用求和模块将此端口的扰动信号注入到调节 d 轴电流的 PID 控制器的输出。

- 当实验正在运行时，模块会在此端口生成扰动信号。
- 当实验未运行时，此端口处的信号为零。在此状态下，模块对被控对象没有影响。

#### 依赖项

要启用此端口，请选择 **Tune D-axis current loop**。

**数据类型：** `single` | `double`

### **perturbation qaxis** — 交轴电流输入扰动（标量）

用于估计与 q 轴电流控制环关联的频率响应数据模型的扰动信号输入。通过使用求和模块将此端口的扰动信号注入到调节 q 轴电流的 PID 控制器的输出。

- 当实验正在运行时，模块会在此端口生成扰动信号。
- 当实验未运行时，此端口处的信号为零。在此状态下，模块对被控对象没有影响。

#### 依赖项

要启用此端口，请选择 **Tune Q-axis current loop**。

**数据类型：** `single` | `double`

### **perturbation spd** — 速度输入扰动（标量）

用于估计与电机速度控制环关联的频率响应数据模型的扰动信号输入。通过使用求和模块将此端口的扰动信号与调节电机速度的 PID 控制器的输出相加。

- 当实验正在运行时，模块会在此端口生成扰动信号。
- 当实验未运行时，此端口处的信号为零。在此状态下，模块对被控对象没有影响。

#### 依赖项

要启用此端口，请选择 **Tune speed loop**。

**数据类型：** `single` | `double`

### **perturbation flux** — 磁通输入扰动（标量）

用于估计与电机磁通控制环关联的频率响应数据模型的扰动信号输入。通过使用求和模块将此端口的扰动信号注入到调节电机磁链的 PID 控制器的输出。

- 当实验正在运行时，模块会在此端口生成扰动信号。
- 当实验未运行时，此端口处的信号为零。在此状态下，模块对被控对象没有影响。

#### 依赖项

要启用此端口，请选择 **Tune flux loop**。

**数据类型：** `single` | `double`

### **pid gains** — 调谐后的 PID 系数 bus

此 4 元素 bus 信号包含模块为每个控制环调谐后的 PID 增益 *P*、*I*、*D* 以及滤波器系数 *N*。这些值对应于 `Form` 参数中给出的表达式里的 `P`、`I`、`D` 和 `N` 参数。初始时，这些值分别为 0、0、0 和 100。模块在实验结束时更新这些值。对应于模块调谐的每个环的 bus 信号始终有四个元素，即使您没有调谐 PIDF 控制器。

**数据类型：** `single` | `double`

### **convergence** — 实验期间 FRD 估计的收敛性 标量

该模块使用扰动信号，在目标带宽附近的多个频率处估计与每个环路相关联的被控对象的频率响应，以进行整定。`convergence` 表示被控对象频率响应估计的完成程度。通常，该值在实验开始后迅速升至约 90%，然后逐渐收敛到更高的值。当它稳定在接近 100% 时，停止实验。

对于 **PRBS** 实验模式，此端口处的信号仅在估计实验完成后更新。*（自 R2024a 起）*

**数据类型：** `single` | `double`

### **estimated PM** — 最近整定环路的估计相位裕度 标量

此端口输出已整定控制器针对最近整定环路实现的估计相位裕度，单位为度。该模块在每环路的整定实验结束时更新此值。估计相位裕度根据 *G*(*jωc*)*C*(*jωc*) 的角度计算，其中 *G* 是该环路的估计被控对象，*C* 是已整定控制器，*ωc* 是穿越频率（带宽）。估计相位裕度可能不同于由 `Target phase margin (degrees)` 参数指定的目标相位裕度。它是已整定系统所实现的鲁棒性和稳定性的指标。

- 通常，估计相位裕度接近目标相位裕度。一般来说，该值越大，已整定系统越鲁棒，超调越少。
- 负相位裕度表示闭环系统可能不稳定。

#### 依赖关系

要启用此端口，请在 Block 选项卡上选择 **已整定控制器实现的估计相位裕度**。

**数据类型：** `single` | `double`

### **frd** — 最近整定环路的估计频率响应 向量

此端口输出实验针对最近整定环路估计的频率响应数据。最初，`frd` 处的值为 [0, 0, 0, 0, 0]。在实验期间，该模块在频率 [1/10, 1/3, 1, 3, 10]*ωc* 处注入信号，其中 *ωc* 是目标带宽。在实验期间的每个采样时间，该模块用包含这些频率处复数频率响应的向量更新 `frd`。您可以使用响应的进展作为 `convergence` 的替代方法，以检查估计的收敛情况。当实验停止时，该模块用用于计算 PID 增益的最终估计频率响应更新 `frd`。

对于 **PRBS** 实验模式，此端口处的信号仅在估计实验完成后更新。*（自 R2024a 起）*

#### 依赖关系

要启用此端口，请在 Block 选项卡上选择 **带宽附近的被控对象频率响应**。

**数据类型：** `single` | `double`

### **nominal** — 最近整定环路的标称工作点处被控对象输入和输出 向量

此端口输出一个向量，其中包含最近整定环路或当前正在整定环路的被控对象输入和被控对象输出。这些值是模块执行实验的标称工作点处的被控对象输入和输出。

#### 依赖关系

要启用此端口，请在 Block 选项卡上选择 **被控对象标称输入和输出**。

**数据类型：** `single` | `double`

### **loop startstops** — 活动环路总线

此 4 元素总线信号指示该模块整定的每个环路的整定实验是否处于活动状态。对于总线中的每个信号，当整定实验正在运行时，该端口为环路输出逻辑值 `1`（`true`）。当实验结束或尚未开始时，该值为逻辑 `0`（`false`）。您可以使用此端口触发各个环路的 PID 增益更新。

#### 依赖关系

要启用此端口，请在 Block 选项卡上禁用 **使用外部源启动/停止实验**，然后选择 **自整定过程的启动/停止**。

**数据类型：** `single` | `double`

## 参数

### **整定 D 轴电流环** — 启用 d 轴电流环整定 `on`（默认） | `off`

使用此参数启用或禁用 d 轴电流环自整定。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TuneDaxisLoop` |
| **类型：** character vector |
| **取值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **整定 Q 轴电流环** — 启用 q 轴电流环整定 `on`（默认） | `off`

使用此参数启用或禁用 q 轴电流环自整定。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TuneQaxisLoop` |
| **类型：** character vector |
| **取值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **整定速度环** — 启用速度环整定 `on`（默认） | `off`

使用此参数启用或禁用速度环自整定。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TuneSpeedLoop` |
| **类型：** character vector |
| **取值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **整定磁通环** — 启用磁通环整定 `on`（默认） | `off`

使用此参数启用或禁用磁通环自整定。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TuneSpeedLoop` |
| **类型：** character vector |
| **取值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **对电流环控制器使用相同设置（D 轴 + Q 轴）** — 为直轴和交轴电流环启用相同的整定和实验设置 `off`（默认） | `on`

选择此参数可为 d 轴和 q 轴电流环启用相同的整定和实验设置。启用后，该模块使用相同的控制器设置、目标带宽、相位裕度和其他实验设置来整定 d 轴和 q 轴电流环。

#### 程序化使用

|  |
| --- |
| **模块参数：** `UseSameSettingsInner` |
| **类型：** character vector |
| **取值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **对外环控制器使用相同设置（速度 + 磁通）** — 为速度和磁通环启用相同的整定和实验设置 `off`（默认） | `on`

选择此参数可为速度和磁通环启用相同的整定和实验设置。启用后，该模块使用相同的控制器设置、目标带宽、相位裕度和其他实验设置来整定速度和磁通环。

#### 程序化使用

|  |
| --- |
| **模块参数：** `UseSameSettingsOuter` |
| **类型：** character vector |
| **取值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **实验采样时间** — 频率响应估计实验的采样时间 –1（默认） | positive scalar

指定该模块执行的频率响应估计实验的采样时间，单位为秒。

默认情况下，实验采样时间设置为 inherited（–1），该模块在每个环路的 inherited 采样时间执行频率响应估计实验。使用此参数可为频率响应估计实验指定不同于整定和 PID 增益计算采样率的采样时间。对于您整定的每个环路，频率响应都按此参数中指定的采样时间进行估计。

当您为整定、实验和环路指定不同的采样时间时，可以将 Simulink 配置为将每个模块速率视为单独任务，以便为模型启用多任务执行。此多任务模式有助于提高硬件性能。有关详细信息，请参阅将每个离散速率视为单独任务。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TsExperiment` |
| **类型：** scalar |
| **值** positive scalar |
| **默认值：** –1 (inherited) |

### 整定选项卡

### **对整定使用不同的采样时间** — 使用与环路 PID 控制器和实验不同的采样时间进行整定 `off`（默认） | `on`

默认情况下，该模块以您为该环路在 **控制器采样时间 (sec)** 参数中指定的相同采样时间，对每个环路运行整定。启用此参数可使整定以不同于您正在整定的 PID 控制器的采样率以及该模块执行的频率响应估计实验的采样率运行。PID 增益整定算法计算密集；当您要将该模块部署到硬件并整定具有快速采样时间的控制器时，某些硬件可能无法在单个时间步内完成 PID 增益计算。为降低硬件吞吐量需求，请使用 **整定采样时间 (sec)** 参数指定比控制器采样时间更慢的整定采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `UseTuningTs` |
| **类型：** character vector |
| **值** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **整定采样时间 (sec)** — 整定算法的采样时间 0.2（默认） | positive scalar

指定整定算法的采样时间，单位为秒。

如果您打算将该模块部署到处理能力有限的硬件上，并希望整定具有快速采样时间的控制器，请指定一个采样时间，使整定算法以比您正在整定的 PID 控制器更慢的速率运行。对于您整定的每个环路，在频率响应估计实验结束后，控制器整定将按此参数指定的采样时间进行。

#### 依赖关系

要启用此参数，请选择 **对整定使用不同的采样时间**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TsTuning` |
| **类型：** scalar |
| **值** positive scalar |
| **默认值：** 0.2 |

#### D 轴电流环

### **类型** — D 轴电流环 PID 控制器动作 `PI`（默认） | `PID` | `PIDF` | ...

指定与 d 轴电流控制环相关联的 PID 控制器类型。

控制器类型指示调节该环路的控制器中存在哪些动作。以下控制器类型可用于 PID 自整定：

- `P` — 仅比例
- `I` — 仅积分
- `PI` — 比例和积分
- `PD` — 比例和微分
- `PDF` — 比例和带微分滤波器的微分
- `PID` — 比例、积分和微分
- `PIDF` — 比例、积分和带微分滤波器的微分

确保控制器类型与调节该环路的控制器匹配。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PIDTypeDaxis` |
| **类型：** character vector |
| **取值：** `'P'` | `'I'` | `'PI'` | `'PD'` | `'PDF'` | `'PID'` | `'PIDF'` |
| **默认值：** `'PI'` |

### **形式** — D 轴电流环 PID 控制器形式 `Parallel`（默认） | `Ideal`

指定与您的 d 轴电流控制环相关联的 PID 控制器形式。

控制器形式决定 PID 系数 *P*、*I*、*D* 和 *N* 的解释。

- `Parallel` — 在 `Parallel` 形式中，离散时间 PIDF 控制器的传递函数为

  C=P+IFi(z)+D[N1+NFd(z)],

  其中 *Fi*(*z*) 和 *Fd*(*z*) 是积分器和滤波器公式（请参阅 `Integrator method` 和 `Filter method`）。

  其他控制器动作相当于将 *P*、*I* 或 *D* 设置为零。
- `Ideal` — 在 `Ideal` 形式中，离散时间 PIDF 控制器的传递函数为

  C=P[1+IFi(z)+D(N1+NFd(z))].

  其他控制器动作相当于将 *D* 设置为零或将 *I* 设置为 `Inf`。（在 `Ideal` 形式中，控制器必须具有比例作用。）

确保控制器形式与调节该环路的控制器匹配。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PIDFormDaxis` |
| **类型：** character vector |
| **取值：** `'Parallel'` | `'Ideal'` |
| **默认值：** `'Parallel'` |

**可调：** 是

### **控制器采样时间 (sec)** — D 轴电流环 PID 控制器采样时间 0.001（默认） | positive scalar | –1

指定与 d 轴电流控制环相关联的 PID 控制器的采样时间，单位为秒。此参数设置用于计算该环路 PID 控制器增益的采样时间。

为执行 PID 整定，该模块测量高达目标带宽 10 倍的频率处的频率响应信息。为确保该频率小于 Nyquist 频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* *ωc* 是您使用 `Controller sample time (sec)` 参数指定的控制器采样时间。

确保控制器采样时间与调节该环路的控制器匹配。

#### 提示

如果要在应用中以不同的采样时间运行已部署模块，请将此参数设置为 –1，并将该模块放入 Triggered Subsystem 中。然后，以所需采样时间触发该子系统。如果不打算在部署后更改采样时间，请指定固定且有限的采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TsDaxis` |
| **类型：** scalar |
| **值** positive scalar | –1 |
| **默认值：** 0.001 |

### **积分器方法** — D 轴电流环控制器积分项的离散积分公式 `Forward Euler`（默认） | `Backward Euler` | `Trapezoidal`

指定控制器中积分项的离散积分公式。在离散时间中，该模块假定的 PID 控制器传递函数为

C=P+IFi(z)+D[N1+NFd(z)],

采用并联形式，或采用理想形式，

C=P[1+IFi(z)+D(N1+NFd(z))].

对于控制器采样时间 *Ts*，`Integrator method` 参数按下式确定公式 *Fi*。

| 积分器方法 | *Fi* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优势的详细信息，请参阅 Discrete PID Controller 模块参考页。

确保控制器积分器方法与调节该环路的控制器匹配。

#### 依赖关系

当控制器包含积分作用时，此参数启用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `IntegratorMethodDaxis` |
| **类型：** character vector |
| **取值：** `'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认值：** `'Forward Euler'` |

**可调：** 是

### **滤波器方法** — D 轴电流环控制器微分滤波器项的离散积分公式 `Forward Euler`（默认） | `Backward Euler` | `Trapezoidal`

指定控制器中微分滤波器项的离散积分公式。在离散时间中，该模块假定的 PID 控制器传递函数为

C=P+IFi(z)+D[N1+NFd(z)],

采用并联形式，或采用理想形式，

C=P[1+IFi(z)+D(N1+NFd(z))].

对于控制器采样时间 *Ts*，`Filter method` 参数按下式确定公式 *Fd*。

| 滤波器方法 | *Fd* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优势的详细信息，请参阅 Discrete PID Controller 模块参考页。

确保控制器微分滤波器方法与调节该环路的控制器匹配。

#### 依赖关系

当控制器包含带微分滤波器项的微分作用时，此参数启用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FilterMethodDaxis` |
| **类型：** character vector |
| **取值：** `'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认值：** `'Forward Euler'` |

**可调：** 是

### **Target bandwidth (rad/sec)** — d 轴电流环调谐响应的目标穿越频率 100（默认）| positive scalar

目标带宽是调谐开环响应 *CP* 的 0 dB 增益穿越频率的目标值，其中 *P* 是与该环相关的被控对象响应，*C* 是控制器响应。该穿越频率大致设定控制带宽。对于上升时间 *τ* seconds，目标带宽的良好估计为 2/*τ* rad/sec。

要执行 PID 调谐，自动调谐器模块测量频率响应信息，最高频率为目标带宽的 10 倍。为确保该频率低于 Nyquist 频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* 是您使用 **Controller sample time (sec)** 参数指定的控制器采样时间。由于此条件，您可强制实现的最快上升时间约为 6.67*Ts*。如果此上升时间不满足您的设计目标，请考虑减小 *Ts*。

为获得最佳结果，请使用与初始 PID 控制器带宽相差约不超过 10 倍的目标带宽。若要针对更大的带宽变化调谐控制器，请使用较小的变化逐步调谐。

若要通过输入端口提供目标带宽，请在 Block 选项卡上选择 **Use external source for bandwidth**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `BandwidthDaxis` |
| **类型：** positive scalar |
| **默认值：** `100` |

### **Target phase margin (degrees)** — d 轴电流环目标最小相位裕度 60（默认）| scalar in range 0–90

在穿越频率处，为与 d 轴电流控制环相关的调谐开环响应指定目标最小相位裕度。

目标相位裕度反映调谐系统的期望鲁棒性。通常，选择约 45°–60° 范围内的值。一般而言，更高的相位裕度可减少超调，但可能限制响应速度。默认值 60° 往往能在性能和鲁棒性之间取得平衡，根据被控对象特性产生约 5–10% 的超调。

若要通过输入端口提供目标相位裕度，请在 Block 选项卡上选择 **Use external source for target phase margins**。

**可调：** Yes

#### 程序化使用

|  |
| --- |
| **模块参数：** `TargetPMDaxis` |
| **类型：** scalar |
| **值：** 0–90 |
| **默认值：** 60 |

#### q 轴电流环

### **Type** — q 轴电流环 PID 控制器动作 `PI`（默认） | `PID` | `PIDF` | ...

指定与 q 轴电流控制环相关的 PID 控制器类型。

控制器类型指示调节该环路的控制器中具有哪些动作。以下控制器类型可用于 PID 自动调谐：

- `P` — 仅比例
- `I` — 仅积分
- `PI` — 比例和积分
- `PD` — 比例和微分
- `PDF` — 带微分滤波器的比例和微分
- `PID` — 比例、积分和微分
- `PIDF` — 带微分滤波器的比例、积分和微分

确保控制器类型与调节该环路的控制器匹配。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PIDTypeQaxis` |
| **类型：** character vector |
| **值：** `'P'` | `'I'` | `'PI'` | `'PD'` | `'PDF'` | `'PID'` | `'PIDF'` |
| **默认值：** `'PI'` |

### **Form** — q 轴电流环 PID 控制器形式 `Parallel`（默认） | `Ideal`

指定与 q 轴电流控制环相关的 PID 控制器形式。

控制器形式决定 PID 系数 *P*、*I*、*D* 和 *N* 的解释。

- `Parallel` — 在 `Parallel` 形式下，
  离散时间 PIDF 控制器的传递函数为

  C=P+IFi(z)+D[N1+NFd(z)],

  其中 *Fi*(*z*) 和 *Fd*(*z*) 是积分器和滤波器公式（参见 `Integrator method` 和 `Filter method`）。

  其他控制器动作相当于将 *P*、*I* 或 *D* 设为零。
- `Ideal` — 在 `Ideal` 形式下，
  离散时间 PIDF 控制器的传递函数为

  C=P[1+IFi(z)+D(N1+NFd(z))].

  其他控制器动作相当于将 *D* 设为零或将 *I* 设置为 `Inf`。（在 ideal 形式下，控制器必须具有比例动作。）

确保控制器形式与调节该环路的控制器匹配。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PIDFormQaxis` |
| **类型：** character vector |
| **值：** `'Parallel'` | `'Ideal'` |
| **默认值：** `'Parallel'` |

**可调：** Yes

### **Controller sample time (sec)** — q 轴电流环 PID 控制器采样时间 0.001（默认） | positive scalar | –1

以 seconds 为单位指定与 q 轴电流控制环相关的 PID 控制器采样时间。此参数设置用于计算该环路 PID 控制器增益的采样时间。

要执行 PID 调谐，该模块测量频率响应信息，最高频率为目标带宽的 10 倍。为确保该频率低于 Nyquist 频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* *ωc* 是您使用 `Controller sample time (sec)` 参数指定的控制器采样时间。

确保控制器采样时间与调节该环路的控制器匹配。

#### 提示

如果希望在应用中用不同采样时间运行部署的模块，请将此参数设置为 –1，并将该模块放入 Triggered Subsystem。然后，以所需采样时间触发该子系统。如果部署后不打算更改采样时间，请指定固定且有限的采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TsQaxis` |
| **类型：** scalar |
| **值：** positive scalar | –1 |
| **默认值：** 0.001 |

### **Integrator method** — q 轴电流环控制器积分项的离散积分公式 `Forward Euler`（默认） | `Backward Euler` | `Trapezoidal`

指定控制器中积分项的离散积分公式。在离散时间下，该模块假定的 PID 控制器传递函数为

C=P+IFi(z)+D[N1+NFd(z)],

在 parallel 形式下，或在 ideal 形式下，

C=P[1+IFi(z)+D(N1+NFd(z))].

对于控制器采样时间 *Ts*，`Integrator method` 参数按如下方式确定公式 *Fi*。

| Integrator method | *Fi* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优势的更多信息，请参阅 Discrete PID Controller 模块参考页。

确保控制器积分器方法与调节该环路的控制器匹配。

#### 依赖关系

当控制器包含积分动作时，此参数启用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `IntegratorMethodQaxis` |
| **类型：** character vector |
| **值：** `'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认值：** `'Forward Euler'` |

**可调：** Yes

### **Filter method** — q 轴电流环控制器微分滤波项的离散积分公式 `Forward Euler`（默认） | `Backward Euler` | `Trapezoidal`

指定控制器中微分滤波项的离散积分公式。在离散时间下，该模块假定的 PID 控制器传递函数为

C=P+IFi(z)+D[N1+NFd(z)],

在 parallel 形式下，或在 ideal 形式下，

C=P[1+IFi(z)+D(N1+NFd(z))].

对于控制器采样时间 *Ts*，`Filter method` 参数按如下方式确定公式 *Fd*。

| Filter method | *Fd* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优势的更多信息，请参阅 Discrete PID Controller 模块参考页。

确保控制器微分滤波器方法与调节该环路的控制器匹配。

#### 依赖关系

当控制器包含带微分滤波项的微分动作时，此参数启用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FilterMethodQaxis` |
| **类型：** character vector |
| **值：** `'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认值：** `'Forward Euler'` |

**可调：** Yes

### **Target bandwidth (rad/sec)** — q 轴电流环调谐响应的目标穿越频率 100（默认）| positive scalar

目标带宽是调谐开环响应 *CP* 的 0 dB 增益穿越频率的目标值，其中 *P* 是与该环相关的被控对象响应，*C* 是控制器响应。该穿越频率大致设定控制带宽。对于上升时间 *τ* seconds，目标带宽的良好估计为 2/*τ* rad/sec。

要执行 PID 调谐，自动调谐器模块测量频率响应信息，最高频率为目标带宽的 10 倍。为确保该频率低于 Nyquist 频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* 是您使用 **Controller sample time (sec)** 参数指定的控制器采样时间。由于此条件，您可强制实现的最快上升时间约为 6.67*Ts*。如果此上升时间不满足您的设计目标，请考虑减小 *Ts*。

为获得最佳结果，请使用与初始 PID 控制器带宽相差约不超过 10 倍的目标带宽。若要针对更大的带宽变化调谐控制器，请使用较小的变化逐步调谐。

若要通过输入端口提供目标带宽，请在 Block 选项卡上选择 **Use external source for bandwidth**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `BandwidthQaxis` |
| **类型：** positive scalar |
| **默认值：** `100` |

### **Target phase margin (degrees)** — q 轴电流环目标最小相位裕度 60（默认）| scalar in range 0–90

在穿越频率处，为与 q 轴电流控制环相关的调谐开环响应指定目标最小相位裕度。

目标相位裕度反映调谐系统的期望鲁棒性。通常，选择约 45°–60° 范围内的值。一般而言，更高的相位裕度可减少超调，但可能限制响应速度。默认值 60° 往往能在性能和鲁棒性之间取得平衡，根据被控对象特性产生约 5–10% 的超调。

若要通过输入端口提供目标相位裕度，请在 Block 选项卡上选择 **Use external source for target phase margins**。

**可调：** Yes

#### 程序化使用

|  |
| --- |
| **模块参数：** `TargetPMQaxis` |
| **类型：** scalar |
| **值：** 0–90 |
| **默认值：** 60 |

#### 速度环

### **Type** — 速度环 PID 控制器动作 `PI`（默认） | `PID` | `PIDF` | ...

指定与速度控制环相关的 PID 控制器类型。

控制器类型指示调节该环路的控制器中具有哪些动作。以下控制器类型可用于 PID 自动调谐：

- `P` — 仅比例
- `I` — 仅积分
- `PI` — 比例和积分
- `PD` — 比例和微分
- `PDF` — 带微分滤波器的比例和微分
- `PID` — 比例、积分和微分
- `PIDF` — 带微分滤波器的比例、积分和微分

确保控制器类型与调节该环路的控制器匹配。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PIDTypeSpeed` |
| **类型：** character vector |
| **值：** `'P'` | `'I'` | `'PI'` | `'PD'` | `'PDF'` | `'PID'` | `'PIDF'` |
| **默认值：** `'PI'` |

### **Form** — 速度环 PID 控制器形式 `Parallel`（默认） | `Ideal`

指定与速度控制环相关的 PID 控制器形式。

控制器形式决定 PID 系数 *P*、*I*、*D* 和 *N* 的解释。

- `Parallel` — 在 `Parallel` 形式下，
  离散时间 PIDF 控制器的传递函数为

  C=P+IFi(z)+D[N1+NFd(z)],

  其中 *Fi*(*z*) 和 *Fd*(*z*) 是积分器和滤波器公式（参见 `Integrator method` 和 `Filter method`）。

  其他控制器动作相当于将 *P*、*I* 或 *D* 设为零。
- `Ideal` — 在 `Ideal` 形式下，
  离散时间 PIDF 控制器的传递函数为

  C=P[1+IFi(z)+D(N1+NFd(z))].

  其他控制器动作相当于将 *D* 设为零或将 *I* 设置为 `Inf`。（在 ideal 形式下，控制器必须具有比例动作。）

确保控制器形式与调节该环路的控制器匹配。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PIDFormSpeed` |
| **类型：** character vector |
| **值：** `'Parallel'` | `'Ideal'` |
| **默认值：** `'Parallel'` |

**可调：** Yes

### **Controller sample time (sec)** — 速度环 PID 控制器采样时间 0.1（默认） | positive scalar | –1

以 seconds 为单位指定与速度控制环相关的 PID 控制器采样时间。此参数设置用于计算该环路 PID 控制器增益的采样时间。

要执行 PID 调谐，该模块测量频率响应信息，最高频率为目标带宽的 10 倍。为确保该频率低于 Nyquist 频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* *ωc* 是您使用 `Controller sample time (sec)` 参数指定的控制器采样时间。

确保控制器采样时间与调节该环路的控制器匹配。

#### 提示

如果希望在应用中用不同采样时间运行部署的模块，请将此参数设置为 –1，并将该模块放入 Triggered Subsystem。然后，以所需采样时间触发该子系统。如果部署后不打算更改采样时间，请指定固定且有限的采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TsSpeed` |
| **类型：** scalar |
| **值：** positive scalar | –1 |
| **默认值：** 0.1 |

### **Integrator method** — 速度环控制器积分项的离散积分公式 `Forward Euler`（默认） | `Backward Euler` | `Trapezoidal`

指定控制器中积分项的离散积分公式。在离散时间下，该模块假定的 PID 控制器传递函数为

C=P+IFi(z)+D[N1+NFd(z)],

在 parallel 形式下，或在 ideal 形式下，

C=P[1+IFi(z)+D(N1+NFd(z))].

对于控制器采样时间 *Ts*，`Integrator method` 参数按如下方式确定公式 *Fi*。

| Integrator method | *Fi* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优势的更多信息，请参阅 Discrete PID Controller 模块参考页。

确保控制器积分器方法与调节该环路的控制器匹配。

#### 依赖关系

当控制器包含积分动作时，此参数启用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `IntegratorMethodSpeed` |
| **类型：** character vector |
| **值：** `'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认值：** `'Forward Euler'` |

**可调：** Yes

### **Filter method** — 速度环控制器微分滤波项的离散积分公式 `Forward Euler`（默认） | `Backward Euler` | `Trapezoidal`

指定控制器中微分滤波项的离散积分公式。在离散时间下，模块假定的 PID 控制器传递函数为

C=P+IFi(z)+D[N1+NFd(z)],

并联形式，或理想形式，

C=P[1+IFi(z)+D(N1+NFd(z))].

对于控制器采样时间 *Ts*，`Filter method` 参数按下述方式确定公式 *Fd*。

| Filter method | *Fd* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优势的更多信息，请参阅 Discrete PID Controller 模块参考页。

确保控制器微分滤波方法与调节该环路的控制器匹配。

#### 依赖关系

当控制器包含带微分滤波项的微分作用时，启用此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FilterMethodSpeed` |
| **类型：** character vector |
| **值：** `'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认值：** `'Forward Euler'` |

**可调：** Yes

### **Target bandwidth (rad/sec)** — 速度环调谐响应的目标穿越频率 1（默认） | positive scalar

目标带宽是调谐开环响应 *CP* 的 0 dB 增益穿越频率的目标值，其中 *P* 是与该环路关联的被控对象响应，*C* 是控制器响应。该穿越频率大致设定控制带宽。对于上升时间 *τ* 秒，目标带宽的良好估计值为 2/*τ* rad/sec。

为执行 PID 调谐，autotuner 模块测量高达目标带宽 10 倍的频率响应信息。为确保该频率低于 Nyquist 频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* 是您使用 **Controller sample time (sec)** 参数指定的控制器采样时间。由于此条件，您可以为调谐强制实现的最快上升时间约为 6.67*Ts*。如果该上升时间不满足您的设计目标，请考虑减小 *Ts*。

为获得最佳结果，请使用与初始 PID 控制器带宽相差约 10 倍以内的目标带宽。要针对带宽的更大变化调谐控制器，请使用较小变化逐步调谐。

要通过输入端口提供目标带宽，请在 Block 选项卡上选择 **Use external source for bandwidth**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `BandwidthSpeed` |
| **类型：** positive scalar |
| **默认值：** `1` |

### **Target phase margin (degrees)** — 速度环目标最小相位裕度 60（默认） | scalar in range 0–90

为与速度控制环路关联的调谐开环响应在穿越频率处指定目标最小相位裕度。

目标相位裕度反映调谐系统所需的鲁棒性。通常，选择约 45°–60° 范围内的值。一般而言，较高的相位裕度会减少超调，但可能限制响应速度。默认值 60° 倾向于平衡性能和鲁棒性，根据您的被控对象特性，产生约 5–10% 的超调。

要通过输入端口提供目标相位裕度，请在 Block 选项卡上选择 **Use external source for target phase margins**。

**可调：** Yes

#### 程序化使用

|  |
| --- |
| **模块参数：** `TargetPMSpeed` |
| **类型：** scalar |
| **值：** 0–90 |
| **默认值：** 60 |

#### 磁通环

### **Type** — 磁通环 PID 控制器作用 `PI`（默认） | `PID` | `PIDF` | ...

指定与磁通控制环路关联的 PID 控制器类型。

控制器类型指示调节该环路的控制器中存在哪些作用。以下控制器类型可用于 PID 自动调谐：

- `P` — 仅比例
- `I` — 仅积分
- `PI` — 比例和积分
- `PD` — 比例和微分
- `PDF` — 比例和带微分滤波器的微分
- `PID` — 比例、积分和微分
- `PIDF` — 比例、积分和带微分滤波器的微分

确保控制器类型与调节该环路的控制器匹配。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PIDTypeFlux` |
| **类型：** character vector |
| **值：** `'P'` | `'I'` | `'PI'` | `'PD'` | `'PDF'` | `'PID'` | `'PIDF'` |
| **默认值：** `'PI'` |

### **Form** — 磁通环 PID 控制器形式 `Parallel`（默认） | `Ideal`

指定与您的磁通控制环路关联的 PID 控制器形式。

控制器形式确定 PID 系数 *P*、*I*、*D* 和 *N* 的解释。

- `Parallel` — 在 `Parallel` 形式中，离散时间 PIDF 控制器的传递函数为

  C=P+IFi(z)+D[N1+NFd(z)],

  其中 *Fi*(*z*) 和 *Fd*(*z*) 是积分器和滤波器公式（请参阅 `Integrator method` 和 `Filter method`）。

  其他控制器作用相当于将 *P*、*I* 或 *D* 设置为零。
- `Ideal` — 在 `Ideal` 形式中，离散时间 PIDF 控制器的传递函数为

  C=P[1+IFi(z)+D(N1+NFd(z))].

  其他控制器作用相当于将 *D* 设置为零或将 *I* 设置为 `Inf`。（在理想形式中，控制器必须具有比例作用。）

确保控制器形式与调节该环路的控制器匹配。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PIDFormFlux` |
| **类型：** character vector |
| **值：** `'Parallel'` | `'Ideal'` |
| **默认值：** `'Parallel'` |

**可调：** Yes

### **Controller sample time (sec)** — 磁通环 PID 控制器采样时间 0.1（默认） | positive scalar | –1

指定与磁通控制环路关联的 PID 控制器的采样时间（以秒为单位）。此参数设置用于计算该环路 PID 控制器增益的采样时间。

为执行 PID 调谐，模块测量高达目标带宽 10 倍的频率响应信息。为确保该频率低于 Nyquist 频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* 是您使用 `Controller sample time (sec)` 参数指定的控制器采样时间。

确保控制器采样时间与调节该环路的控制器匹配。

#### 提示

如果要在应用中部署的模块使用不同的采样时间运行，请将此参数设置为 –1，并将模块放入 Triggered Subsystem 中。然后，以所需采样时间触发该子系统。如果您不打算在部署后更改采样时间，请指定固定且有限的采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TsFlux` |
| **类型：** scalar |
| **值：** positive scalar | –1 |
| **默认值：** 0.1 |

### **Integrator method** — 磁通环控制器积分项的离散积分公式 `Forward Euler`（默认） | `Backward Euler` | `Trapezoidal`

指定控制器中积分项的离散积分公式。在离散时间下，模块假定的 PID 控制器传递函数为

C=P+IFi(z)+D[N1+NFd(z)],

并联形式，或理想形式，

C=P[1+IFi(z)+D(N1+NFd(z))].

对于控制器采样时间 *Ts*，`Integrator method` 参数按下述方式确定公式 *Fi*。

| Integrator method | *Fi* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优势的更多信息，请参阅 Discrete PID Controller 模块参考页。

确保控制器积分器方法与调节该环路的控制器匹配。

#### 依赖关系

当控制器包含积分作用时，启用此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `IntegratorMethodFlux` |
| **类型：** character vector |
| **值：** `'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认值：** `'Forward Euler'` |

**可调：** Yes

### **Filter method** — 磁通环控制器微分滤波项的离散积分公式 `Forward Euler`（默认） | `Backward Euler` | `Trapezoidal`

指定控制器中微分滤波项的离散积分公式。在离散时间下，模块假定的 PID 控制器传递函数为

C=P+IFi(z)+D[N1+NFd(z)],

并联形式，或理想形式，

C=P[1+IFi(z)+D(N1+NFd(z))].

对于控制器采样时间 *Ts*，`Filter method` 参数按下述方式确定公式 *Fd*。

| Filter method | *Fd* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优势的更多信息，请参阅 Discrete PID Controller 模块参考页。

确保控制器微分滤波方法与调节该环路的控制器匹配。

#### 依赖关系

当控制器包含带微分滤波项的微分作用时，启用此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FilterMethodFlux` |
| **类型：** character vector |
| **值：** `'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认值：** `'Forward Euler'` |

**可调：** Yes

### **Target bandwidth (rad/sec)** — 磁通环调谐响应的目标穿越频率 1（默认） | positive scalar

目标带宽是调谐开环响应 *CP* 的 0 dB 增益穿越频率的目标值，其中 *P* 是与该环路关联的被控对象响应，*C* 是控制器响应。该穿越频率大致设定控制带宽。对于上升时间 *τ* 秒，目标带宽的良好估计值为 2/*τ* rad/sec。

为执行 PID 调谐，autotuner 模块测量高达目标带宽 10 倍的频率响应信息。为确保该频率低于 Nyquist 频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* 是您使用 **Controller sample time (sec)** 参数指定的控制器采样时间。由于此条件，您可以为调谐强制实现的最快上升时间约为 6.67*Ts*。如果该上升时间不满足您的设计目标，请考虑减小 *Ts*。

为获得最佳结果，请使用与初始 PID 控制器带宽相差约 10 倍以内的目标带宽。要针对带宽的更大变化调谐控制器，请使用较小变化逐步调谐。

要通过输入端口提供目标带宽，请在 Block 选项卡上选择 **Use external source for bandwidth**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `BandwidthFlux` |
| **类型：** positive scalar |
| **默认值：** `1` |

### **Target phase margin (degrees)** — 磁通环目标最小相位裕度 60（默认） | scalar in range 0–90

为与磁通控制环路关联的调谐开环响应在穿越频率处指定目标最小相位裕度。

目标相位裕度反映调谐系统所需的鲁棒性。通常，选择约 45°–60° 范围内的值。一般而言，较高的相位裕度会减少超调，但可能限制响应速度。默认值 60° 倾向于平衡性能和鲁棒性，根据您的被控对象特性，产生约 5–10% 的超调。

要通过输入端口提供目标相位裕度，请在 Block 选项卡上选择 **Use external source for target phase margins**。

**可调：** Yes

#### 程序化使用

|  |
| --- |
| **模块参数：** `TargetPMFlux` |
| **类型：** scalar |
| **值：** 0–90 |
| **默认值：** 60 |

#### 电流环（Q 轴 + D 轴）

### **Type** — 电流环 PID 控制器作用 `PI`（默认） | `PID` | `PIDF` | ...

指定与电流控制环路关联的 PID 控制器类型。

控制器类型指示调节该环路的控制器中存在哪些作用。以下控制器类型可用于 PID 自动调谐：

- `P` — 仅比例
- `I` — 仅积分
- `PI` — 比例和积分
- `PD` — 比例和微分
- `PDF` — 比例和带微分滤波器的微分
- `PID` — 比例、积分和微分
- `PIDF` — 比例、积分和带微分滤波器的微分

确保控制器类型与调节该环路的控制器匹配。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PIDTypeAllInner` |
| **类型：** character vector |
| **值：** `'P'` | `'I'` | `'PI'` | `'PD'` | `'PDF'` | `'PID'` | `'PIDF'` |
| **默认值：** `'PI'` |

### **Form** — 电流环 PID 控制器形式 `Parallel`（默认） | `Ideal`

指定与您的电流控制环路关联的 PID 控制器形式。

控制器形式确定 PID 系数 *P*、*I*、*D* 和 *N* 的解释。

- `Parallel` — 在 `Parallel` 形式中，离散时间 PIDF 控制器的传递函数为

  C=P+IFi(z)+D[N1+NFd(z)],

  其中 *Fi*(*z*) 和 *Fd*(*z*) 是积分器和滤波器公式（请参阅 `Integrator method` 和 `Filter method`）。

  其他控制器作用相当于将 *P*、*I* 或 *D* 设置为零。
- `Ideal` — 在 `Ideal` 形式中，离散时间 PIDF 控制器的传递函数为

  C=P[1+IFi(z)+D(N1+NFd(z))].

  其他控制器作用相当于将 *D* 设置为零或将 *I* 设置为 `Inf`。（在理想形式中，控制器必须具有比例作用。）

确保控制器形式与调节该环路的控制器匹配。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PIDFormAllInner` |
| **类型：** character vector |
| **值：** `'Parallel'` | `'Ideal'` |
| **默认值：** `'Parallel'` |

**可调：** Yes

### **Controller sample time (sec)** — 电流环 PID 控制器采样时间 0.001（默认） | positive scalar | –1

指定与电流控制环路关联的 PID 控制器的采样时间（以秒为单位）。此参数设置用于计算该环路 PID 控制器增益的采样时间。

为执行 PID 调谐，模块测量高达目标带宽 10 倍的频率响应信息。为确保该频率低于 Nyquist 频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* 是您使用 `Controller sample time (sec)` 参数指定的控制器采样时间。

确保控制器采样时间与调节该环路的控制器匹配。

#### 提示

如果要在应用中部署的模块使用不同的采样时间运行，请将此参数设置为 –1，并将模块放入 Triggered Subsystem 中。然后，以所需采样时间触发该子系统。如果您不打算在部署后更改采样时间，请指定固定且有限的采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TsAllInner` |
| **类型：** scalar |
| **值：** positive scalar | –1 |
| **默认值：** 0.001 |

### **Integrator method** — 用于积分器项的电流环控制器离散积分公式 `Forward Euler`（默认） | `Backward Euler` | `Trapezoidal`

指定控制器中积分器项的离散积分公式。在离散时间下，模块假定的 PID 控制器传递函数为

C=P+IFi(z)+D[N1+NFd(z)],

并联形式，或理想形式，

C=P[1+IFi(z)+D(N1+NFd(z))].

对于控制器采样时间 *Ts*，`Integrator method` 参数按如下方式确定公式 *Fi*。

| Integrator method | *Fi* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优势的更多信息，请参阅 Discrete PID Controller 模块参考页。

确保控制器积分器方法与调节该回路的控制器匹配。

#### 依赖项

此参数在控制器包含积分作用时启用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `IntegratorMethodAllInner` |
| **类型：** character vector |
| **取值：** `'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认值：** `'Forward Euler'` |

**可调：** Yes

### **Filter method** — 用于微分滤波项的电流环控制器离散积分公式 `Forward Euler`（默认） | `Backward Euler` | `Trapezoidal`

指定控制器中微分滤波项的离散积分公式。在离散时间下，模块假定的 PID 控制器传递函数为

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

确保控制器微分滤波器方法与调节该回路的控制器匹配。

#### 依赖项

此参数在控制器包含带微分滤波项的微分作用时启用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FilterMethodAllInner` |
| **类型：** character vector |
| **取值：** `'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认值：** `'Forward Euler'` |

**可调：** Yes

### **Target bandwidth (rad/sec)** — 电流环已调响应的目标穿越频率 100（默认） | positive scalar

目标带宽是已调开环响应 *CP* 的 0 dB 增益穿越频率的目标值，其中 *P* 是与该回路相关的被控对象响应，*C* 是控制器响应。该穿越频率大致设定控制带宽。对于上升时间 *τ* 秒，目标带宽的一个良好猜测是 2/*τ* rad/sec。

为执行 PID 调优，自动调优器模块会测量最高达到目标带宽 10 倍的频率响应信息。为确保该频率低于 Nyquist 频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* 是您使用 **Controller sample time (sec)** 参数指定的控制器采样时间。由于此条件，您可为调优强制实现的最快上升时间约为 6.67*Ts*。如果该上升时间不满足您的设计目标，请考虑减小 *Ts*。

为获得最佳结果，请使用与初始 PID 控制器的带宽相差约 10 倍以内的目标带宽。要针对更大的带宽变化调优控制器，请使用较小变化逐步调优。

要通过输入端口提供目标带宽，请在 Block 选项卡上选择 **Use external source for bandwidth**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `BandwidthAllInner` |
| **类型：** positive scalar |
| **默认值：** `1` |

### **Target phase margin (degrees)** — 电流环目标最小相位裕度 60（默认） | scalar in range 0–90

指定在穿越频率处与电流控制回路相关的已调开环响应的目标最小相位裕度。

目标相位裕度反映已调系统的期望鲁棒性。通常，选择约 45°–60° 范围内的值。一般情况下，较高的相位裕度会减少超调，但可能限制响应速度。默认值 60° 倾向于平衡性能和鲁棒性，根据您被控对象的特性，产生约 5–10% 的超调。

要通过输入端口提供目标相位裕度，请在 Block 选项卡上选择 **Use external source for target phase margins**。

**可调：** Yes

#### 程序化使用

|  |
| --- |
| **模块参数：** `TargetPMAllInner` |
| **类型：** scalar |
| **取值：** 0–90 |
| **默认值：** 60 |

#### 外环（Speed + Flux）

### **Type** — 外环 PID 控制器作用 `PI`（默认） | `PID` | `PIDF` | ...

指定与外环控制回路相关的 PID 控制器类型。

控制器类型指示调节该回路的控制器中存在哪些作用。以下控制器类型可用于 PID 自动调优：

- `P` — 仅比例
- `I` — 仅积分
- `PI` — 比例和积分
- `PD` — 比例和微分
- `PDF` — 比例和带微分滤波的微分
- `PID` — 比例、积分和微分
- `PIDF` — 比例、积分和带微分滤波的微分

确保控制器类型与调节该回路的控制器匹配。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PIDTypeAllOuter` |
| **类型：** character vector |
| **取值：** `'P'` | `'I'` | `'PI'` | `'PD'` | `'PDF'` | `'PID'` | `'PIDF'` |
| **默认值：** `'PI'` |

### **Form** — 外环 PID 控制器形式 `Parallel`（默认） | `Ideal`

指定与您的外环控制回路相关的 PID 控制器形式。

控制器形式决定 PID 系数 *P*、*I*、*D* 和 *N* 的解释。

- `Parallel` — 在 `Parallel` 形式中，
  离散时间 PIDF 控制器的传递函数为

  C=P+IFi(z)+D[N1+NFd(z)],

  其中 *Fi*(*z*) 和 *Fd*(*z*) 是积分器和滤波器公式（请参阅 `Integrator method` 和 `Filter method`）。

  其他控制器作用相当于将 *P*、*I* 或 *D* 设置为零。
- `Ideal` — 在 `Ideal` 形式中，
  离散时间 PIDF 控制器的传递函数为

  C=P[1+IFi(z)+D(N1+NFd(z))].

  其他控制器作用相当于将 *D* 设置为零或将 *I* 设置为 `Inf`。（在理想形式中，控制器必须具有比例作用。）

确保控制器形式与调节该回路的控制器匹配。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PIDFormAllOuter` |
| **类型：** character vector |
| **取值：** `'Parallel'` | `'Ideal'` |
| **默认值：** `'Parallel'` |

**可调：** Yes

### **Controller sample time (sec)** — 外环 PID 控制器采样时间 0.1（默认） | positive scalar | –1

指定与您的外环控制回路相关的 PID 控制器采样时间（以秒为单位）。此参数设置用于计算该回路 PID 控制器增益的采样时间。

为执行 PID 调优，模块会测量最高达到目标带宽 10 倍的频率响应信息。为确保该频率低于 Nyquist 频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* 是您使用 `Controller sample time (sec)` 参数指定的控制器采样时间。

确保控制器采样时间与调节该回路的控制器匹配。

#### 提示

如果您希望在应用中以不同采样时间运行部署的模块，请将此参数设置为 –1，并将该模块放在 Triggered Subsystem 中。然后，以所需采样时间触发该子系统。如果您不打算在部署后更改采样时间，请指定一个固定且有限的采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TsAllOuter` |
| **类型：** scalar |
| **取值** positive scalar | –1 |
| **默认值：** 0.1 |

### **Integrator method** — 外环控制器用于积分器项的离散积分公式 `Forward Euler`（默认） | `Backward Euler` | `Trapezoidal`

指定控制器中积分器项的离散积分公式。在离散时间下，模块假定的 PID 控制器传递函数为

C=P+IFi(z)+D[N1+NFd(z)],

并联形式，或理想形式，

C=P[1+IFi(z)+D(N1+NFd(z))].

对于控制器采样时间 *Ts*，`Integrator method` 参数按如下方式确定公式 *Fi*。

| Integrator method | *Fi* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

有关每种方法相对优势的更多信息，请参阅 Discrete PID Controller 模块参考页。

确保控制器积分器方法与调节该回路的控制器匹配。

#### 依赖项

此参数在控制器包含积分作用时启用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `IntegratorMethodAllOuter` |
| **类型：** character vector |
| **取值：** `'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认值：** `'Forward Euler'` |

**可调：** Yes

### **Filter method** — 外环控制器用于微分滤波项的离散积分公式 `Forward Euler`（默认） | `Backward Euler` | `Trapezoidal`

指定控制器中微分滤波项的离散积分公式。在离散时间下，模块假定的 PID 控制器传递函数为

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

确保控制器微分滤波器方法与调节该回路的控制器匹配。

#### 依赖项

此参数在控制器包含带微分滤波项的微分作用时启用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FilterMethodAllOuter` |
| **类型：** character vector |
| **取值：** `'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认值：** `'Forward Euler'` |

**可调：** Yes

### **Target bandwidth (rad/sec)** — 外环已调响应的目标穿越频率 1（默认） | positive scalar

目标带宽是已调开环响应 *CP* 的 0 dB 增益穿越频率的目标值，其中 *P* 是与该回路相关的被控对象响应，*C* 是控制器响应。该穿越频率大致设定控制带宽。对于上升时间 *τ* 秒，目标带宽的一个良好猜测是 2/*τ* rad/sec。

为执行 PID 调优，自动调优器模块会测量最高达到目标带宽 10 倍的频率响应信息。为确保该频率低于 Nyquist 频率，目标带宽 *ωc* 必须满足 *ωc**Ts* ≤ 0.3，其中 *Ts* 是您使用 **Controller sample time (sec)** 参数指定的控制器采样时间。由于此条件，您可为调优强制实现的最快上升时间约为 6.67*Ts*。如果该上升时间不满足您的设计目标，请考虑减小 *Ts*。

为获得最佳结果，请使用与初始 PID 控制器的带宽相差约 10 倍以内的目标带宽。要针对更大的带宽变化调优控制器，请使用较小变化逐步调优。

要通过输入端口提供目标带宽，请在 Block 选项卡上选择 **Use external source for bandwidth**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `BandwidthAllOuter` |
| **类型：** positive scalar |
| **默认值：** `1` |

### **Target phase margin (degrees)** — 外环目标最小相位裕度 60（默认） | scalar in range 0–90

指定在穿越频率处与外环控制回路相关的已调开环响应的目标最小相位裕度。

目标相位裕度反映已调系统的期望鲁棒性。通常，选择约 45°–60° 范围内的值。一般情况下，较高的相位裕度会减少超调，但可能限制响应速度。默认值 60° 倾向于平衡性能和鲁棒性，根据您被控对象的特性，产生约 5–10% 的超调。

要通过输入端口提供目标相位裕度，请在 Block 选项卡上选择 **Use external source for target phase margins**。

**可调：** Yes

#### 程序化使用

|  |
| --- |
| **模块参数：** `TargetPMAllOuter` |
| **类型：** scalar |
| **取值：** 0–90 |
| **默认值：** 60 |

### 实验选项卡

#### 实验启动/停止

### **D-axis current loop start time (sec)** — 指定直轴电流环调优实验开始时间 `1`（默认）

指定 d 轴电流环调优实验开始时的仿真时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `StartTimeDaxis` |
| **类型：** positive scalar |
| **默认值：** 1 |

### **D-axis current loop experiment duration (sec)** — 指定直轴电流环调优实验持续时间 `0.05`（默认）

指定 d 轴电流环调优实验持续时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DurationDaxis` |
| **类型：** positive scalar |
| **默认值：** 0.05 |

### **Q-axis current loop start time (sec)** — 指定交轴电流环调优实验开始时间 `1.1`（默认）

指定 q 轴电流环调优实验开始时的仿真时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `StartTimeQaxis` |
| **类型：** positive scalar |
| **默认值：** 1.1 |

### **Q-axis current loop experiment duration (sec)** — 指定交轴电流环调优实验持续时间 `0.05`（默认）

指定 q 轴电流环调优实验持续时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DurationQaxis` |
| **类型：** positive scalar |
| **默认值：** 0.05 |

### **Speed loop start time (sec)** — 指定速度环调优实验开始时间 `2`（默认）

指定速度环调优实验开始时的仿真时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `StartTimeSpeed` |
| **类型：** positive scalar |
| **默认值：** 2 |

### **Speed loop experiment duration (sec)** — 指定速度环调优实验持续时间 `3`（默认）

指定速度环调优实验持续时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DurationSpeed` |
| **类型：** positive scalar |
| **默认值：** 3 |

### **Flux loop start time (sec)** — 指定磁通环调优实验开始时间 `6`（默认）

指定磁通调优实验开始时的仿真时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `StartTimeFlux` |
| **类型：** positive scalar |
| **默认值：** 6 |

### **Flux loop experiment duration (sec)** — 指定磁通环调优实验持续时间 `3`（默认）

指定磁通环调优实验持续时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DurationFlux` |
| **类型：** positive scalar |
| **默认值：** 3 |

#### 回路实验设置

### **实验模式** — 正弦扰动信号类型 `Superposition`（默认） | `Sinestream` | **PRBS** *（自 R2024a 起）*

指定每个频率处的扰动是作为顺序正弦（**Sinestream**）、同时正弦（**Superposition**）还是伪随机二进制序列（**PRBS**）施加。

- **Sinestream** — 在此模式下，模块分别在每个频率处施加扰动。有关用于估计的 sinestream 信号的详细信息，请参阅 Sinestream Input Signals (Simulink Control Design)。
- **Superposition** — 在此模式下，扰动信号一次性包含所有指定的频率。对于在频率向量 *ω* = [*ω*1, … , *ω*N*] 处以幅值 *A* = [*A*1, … , *A*N*] 进行频率响应估计，扰动信号为：

  Δu=∑iAisin(ωit).
- **PRBS** — 一种在两个值之间切换并具有类白噪声特性的确定性伪随机二进制序列。与使用 sinestream 输入信号相比，PRBS 信号可减少总估计时间，同时产生相当的估计结果。PRBS 信号可用于估计通信和电力电子系统的频率响应。有关详细信息，请参阅 PRBS Input Signals (Simulink Control Design)。*（自 R2024a 起）*

**Sinestream** 模式可以更准确，并且侵入性也更小，因为扰动的总大小永远不会大于 **Sine Amplitudes** 参数指定的值。但是，由于 sinestream 扰动的顺序性质，您添加的每个频率点都会增加建议的实验时间（有关详细信息，请参阅 **start/stop** 输入端口）。因此，在 **Superposition** 模式下，估计实验通常要快得多，并且结果令人满意。

与 superposition 输入信号相比，sinestream 信号可减少执行时间，但估计频率响应也需要更长时间。当处理能力有限且希望减少执行时间时，使用 sinestream 信号进行频率响应估计很有用。

为了覆盖相似的频率范围，**PRBS** 模式下的实验长度通常比其他两种模式短得多。但是，结果的速度和质量之间存在权衡。*（自 R2024a 起）*

#### 编程使用

|  |
| --- |
| **模块参数：** `ExperimentMode` |
| **类型：** character vector |
| **值：** `'Superposition'` | `'Sinestream'` | `'PRBS'` |
| **默认值：** `'Superposition'` |

#### D 轴电流环

### **被控对象类型** — D 轴电流被控对象的稳定性 `Stable`（默认） | `Integrating`

指定与 d 轴电流控制环关联的被控对象是稳定还是积分。如果被控对象有一个或多个积分器，请选择 `Integrating`。

#### 编程使用

|  |
| --- |
| **模块参数：** `PlantTypeDaxis` |
| **类型：** character vector |
| **值：** `'Stable'` | `'Integrating'` |
| **默认值：** `'Stable'` |

### **被控对象符号** — D 轴电流被控对象的符号 `Positive`（默认） | `Negative`

指定与 d 轴电流控制环关联的被控对象是正还是负。如果在标称工作点处被控对象输入的正变化导致被控对象输出的正变化，请指定 `Positive`。否则，指定负。对于稳定被控对象，被控对象的符号就是被控对象 DC 增益的符号。

#### 编程使用

|  |
| --- |
| **模块参数：** `PlantSignDaxis` |
| **类型：** character vector |
| **值：** `'Positive'` | `'Negative'` |
| **默认值：** `'Positive'` |

### **正弦幅值** — D 轴电流环中正弦扰动的幅值 1（默认） | scalar | vector of length 5

在实验期间，模块以频率 [1/10, 1/3, 1, 3, 10]*ωc* 向与该环关联的被控对象注入正弦信号，其中 *ωc* 是用于整定的目标带宽。使用 **Sine Amplitudes** 指定每个注入信号的幅值。指定：

- Scalar value 以在每个频率注入相同幅值
- Vector of length 5 以在 [1/10, 1/3, 1, 3, 10]*ωc* 的每个频率指定不同幅值

在具有典型目标带宽的典型被控对象中，实验频率处的被控对象响应幅值变化不大。在这种情况下，您可以使用标量值在所有频率施加相同幅值的扰动。但是，如果您知道响应在频率范围内急剧衰减，请考虑降低较低频率输入的幅值并增加较高频率输入的幅值。当所有被控对象响应具有可比较的幅值时，估计实验在数值上会更好。

扰动幅值必须：

- 足够大，使扰动克服被控对象执行器中的任何死区，并生成高于噪声水平的响应
- 足够小，使被控对象在标称工作点附近的近似线性区域内运行，并避免使被控对象输入或输出饱和

当 **Experiment mode** 为 **Superposition** 时，正弦信号会叠加。因此，扰动至少可以与所有幅值之和一样大。确保最大可能的扰动在被控对象执行器的范围内。使执行器饱和可能会给估计的频率响应引入误差。

要通过输入端口提供正弦幅值，请在 Block 选项卡上，选择 **Use external source for sine amplitudes**。

**可调：** Yes

#### 编程使用

|  |
| --- |
| **模块参数：** `AmpSineDaxis` |
| **类型：** scalar, vector of length 5 |
| **默认值：** 1 |

#### Q 轴电流环

### **被控对象类型** — Q 轴电流被控对象的稳定性 `Stable`（默认） | `Integrating`

指定与 q 轴电流控制环关联的被控对象是稳定还是积分。如果被控对象有一个或多个积分器，请选择 `Integrating`。

#### 编程使用

|  |
| --- |
| **模块参数：** `PlantTypeQaxis` |
| **类型：** character vector |
| **值：** `'Stable'` | `'Integrating'` |
| **默认值：** `'Stable'` |

### **被控对象符号** — Q 轴电流被控对象的符号 `Positive`（默认） | `Negative`

指定与 q 轴电流控制环关联的被控对象是正还是负。如果在标称工作点处被控对象输入的正变化导致被控对象输出的正变化，请指定 `Positive`。否则，指定负。对于稳定被控对象，被控对象的符号就是被控对象 DC 增益的符号。

#### 编程使用

|  |
| --- |
| **模块参数：** `PlantSignQaxis` |
| **类型：** character vector |
| **值：** `'Positive'` | `'Negative'` |
| **默认值：** `'Positive'` |

### **正弦幅值** — Q 轴电流环中正弦扰动的幅值 1（默认） | scalar | vector of length 5

在实验期间，模块以频率 [1/10, 1/3, 1, 3, 10]*ωc* 向与该环关联的被控对象注入正弦信号，其中 *ωc* 是用于整定的目标带宽。使用 **Sine Amplitudes** 指定每个注入信号的幅值。指定：

- Scalar value 以在每个频率注入相同幅值
- Vector of length 5 以在 [1/10, 1/3, 1, 3, 10]*ωc* 的每个频率指定不同幅值

在具有典型目标带宽的典型被控对象中，实验频率处的被控对象响应幅值变化不大。在这种情况下，您可以使用标量值在所有频率施加相同幅值的扰动。但是，如果您知道响应在频率范围内急剧衰减，请考虑降低较低频率输入的幅值并增加较高频率输入的幅值。当所有被控对象响应具有可比较的幅值时，估计实验在数值上会更好。

扰动幅值必须：

- 足够大，使扰动克服被控对象执行器中的任何死区，并生成高于噪声水平的响应
- 足够小，使被控对象在标称工作点附近的近似线性区域内运行，并避免使被控对象输入或输出饱和

当 **Experiment mode** 为 **Superposition** 时，正弦信号会叠加。因此，扰动至少可以与所有幅值之和一样大。确保最大可能的扰动在被控对象执行器的范围内。使执行器饱和可能会给估计的频率响应引入误差。

要通过输入端口提供正弦幅值，请在 Block 选项卡上，选择 **Use external source for sine amplitudes**。

**可调：** Yes

#### 编程使用

|  |
| --- |
| **模块参数：** `AmpSineQaxis` |
| **类型：** scalar, vector of length 5 |
| **默认值：** 1 |

#### 速度环

### **被控对象类型** — 速度环被控对象的稳定性 `Stable`（默认） | `Integrating`

指定与速度控制环关联的被控对象是稳定还是积分。如果被控对象有一个或多个积分器，请选择 `Integrating`。

#### 编程使用

|  |
| --- |
| **模块参数：** `PlantTypeSpeed` |
| **类型：** character vector |
| **值：** `'Stable'` | `'Integrating'` |
| **默认值：** `'Stable'` |

### **被控对象符号** — 速度环被控对象的符号 `Positive`（默认） | `Negative`

指定与速度控制环关联的被控对象是正还是负。如果在标称工作点处被控对象输入的正变化导致被控对象输出的正变化，请指定 `Positive`。否则，指定负。对于稳定被控对象，被控对象的符号就是被控对象 DC 增益的符号。

#### 编程使用

|  |
| --- |
| **模块参数：** `PlantSignSpeed` |
| **类型：** character vector |
| **值：** `'Positive'` | `'Negative'` |
| **默认值：** `'Positive'` |

### **正弦幅值** — 速度环中正弦扰动的幅值 1（默认） | scalar | vector of length 5

在实验期间，模块以频率 [1/10, 1/3, 1, 3, 10]*ωc* 向与该环关联的被控对象注入正弦信号，其中 *ωc* 是用于整定的目标带宽。使用 **Sine Amplitudes** 指定每个注入信号的幅值。指定：

- Scalar value 以在每个频率注入相同幅值
- Vector of length 5 以在 [1/10, 1/3, 1, 3, 10]*ωc* 的每个频率指定不同幅值

在具有典型目标带宽的典型被控对象中，实验频率处的被控对象响应幅值变化不大。在这种情况下，您可以使用标量值在所有频率施加相同幅值的扰动。但是，如果您知道响应在频率范围内急剧衰减，请考虑降低较低频率输入的幅值并增加较高频率输入的幅值。当所有被控对象响应具有可比较的幅值时，估计实验在数值上会更好。

扰动幅值必须：

- 足够大，使扰动克服被控对象执行器中的任何死区，并生成高于噪声水平的响应
- 足够小，使被控对象在标称工作点附近的近似线性区域内运行，并避免使被控对象输入或输出饱和

当 **Experiment mode** 为 **Superposition** 时，正弦信号会叠加。因此，扰动至少可以与所有幅值之和一样大。确保最大可能的扰动在被控对象执行器的范围内。使执行器饱和可能会给估计的频率响应引入误差。

要通过输入端口提供正弦幅值，请在 Block 选项卡上，选择 **Use external source for sine amplitudes**。

**可调：** Yes

#### 编程使用

|  |
| --- |
| **模块参数：** `AmpSineSpeed` |
| **类型：** scalar, vector of length 5 |
| **默认值：** 1 |

#### 磁通环

### **被控对象类型** — 磁通环被控对象的稳定性 `Stable`（默认） | `Integrating`

指定与磁通控制环关联的被控对象是稳定还是积分。如果被控对象有一个或多个积分器，请选择 `Integrating`。

#### 编程使用

|  |
| --- |
| **模块参数：** `PlantTypeFlux` |
| **类型：** character vector |
| **值：** `'Stable'` | `'Integrating'` |
| **默认值：** `'Stable'` |

### **被控对象符号** — 磁通环被控对象的符号 `Positive`（默认） | `Negative`

指定与磁通控制环关联的被控对象是正还是负。如果在标称工作点处被控对象输入的正变化导致被控对象输出的正变化，请指定 `Positive`。否则，指定负。对于稳定被控对象，被控对象的符号就是被控对象 DC 增益的符号。

#### 编程使用

|  |
| --- |
| **模块参数：** `PlantSignFlux` |
| **类型：** character vector |
| **值：** `'Positive'` | `'Negative'` |
| **默认值：** `'Positive'` |

### **正弦幅值** — 磁通环中正弦扰动的幅值 1（默认） | scalar | vector of length 5

在实验期间，模块以频率 [1/10, 1/3, 1, 3, 10]*ωc* 向与该环关联的被控对象注入正弦信号，其中 *ωc* 是用于整定的目标带宽。使用 **Sine Amplitudes** 指定每个注入信号的幅值。指定：

- Scalar value 以在每个频率注入相同幅值
- Vector of length 5 以在 [1/10, 1/3, 1, 3, 10]*ωc* 的每个频率指定不同幅值

在具有典型目标带宽的典型被控对象中，实验频率处的被控对象响应幅值变化不大。在这种情况下，您可以使用标量值在所有频率施加相同幅值的扰动。但是，如果您知道响应在频率范围内急剧衰减，请考虑降低较低频率输入的幅值并增加较高频率输入的幅值。当所有被控对象响应具有可比较的幅值时，估计实验在数值上会更好。

扰动幅值必须：

- 足够大，使扰动克服被控对象执行器中的任何死区，并生成高于噪声水平的响应
- 足够小，使被控对象在标称工作点附近的近似线性区域内运行，并避免使被控对象输入或输出饱和

当 **Experiment mode** 为 **Superposition** 时，正弦信号会叠加。因此，扰动至少可以与所有幅值之和一样大。确保最大可能的扰动在被控对象执行器的范围内。使执行器饱和可能会给估计的频率响应引入误差。

要通过输入端口提供正弦幅值，请在 Block 选项卡上，选择 **Use external source for sine amplitudes**。

**可调：** Yes

#### 编程使用

|  |
| --- |
| **模块参数：** `AmpSineFlux` |
| **类型：** scalar, vector of length 5 |
| **默认值：** 1 |

#### 电流环（D 轴 + Q 轴）

### **被控对象类型** — 电流环被控对象的稳定性 `Stable`（默认） | `Integrating`

指定与电流控制环关联的被控对象是稳定还是积分。如果被控对象有一个或多个积分器，请选择 `Integrating`。

#### 编程使用

|  |
| --- |
| **模块参数：** `PlantTypeAllInner` |
| **类型：** character vector |
| **值：** `'Stable'` | `'Integrating'` |
| **默认值：** `'Stable'` |

### **Plant Sign** — 电流环被控对象的符号 `Positive`（默认）| `Negative`

指定与电流控制环相关联的被控对象是正还是负。如果标称工作点处被控对象输入的正变化导致被控对象输出的正变化，请指定 `Positive`。否则，请指定负。对于稳定被控对象，被控对象的符号就是被控对象直流增益的符号。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PlantSignAllInner` |
| **类型：** character vector |
| **值：** `'Positive'` | `'Negative'` |
| **默认值：** `'Positive'` |

### **Sine Amplitudes** — 电流环中正弦扰动的幅值 1（默认）| scalar | vector of length 5

在实验期间，模块会在频率 [1/10, 1/3, 1, 3, 10]*ωc* 处向与该环关联的被控对象注入正弦信号，其中 *ωc* 是用于整定的目标带宽。使用 **Sine Amplitudes** 指定每个注入信号的幅值。指定：

- 标量值以在每个频率注入相同幅值
- 长度为 5 的向量，以在 [1/10, 1/3, 1, 3, 10]*ωc* 的每个频率指定不同幅值

在具有典型目标带宽的典型被控对象中，实验频率处被控对象响应的幅值变化不大。在这种情况下，可以使用标量值在所有频率施加相同的幅值扰动。但是，如果知道响应在频率范围内急剧衰减，请考虑降低较低频率输入的幅值并提高较高频率输入的幅值。当所有被控对象响应具有可比较的幅值时，估计实验在数值上更好。

扰动幅值必须：

- 足够大，以使扰动克服被控对象执行器中的任何死区，并生成高于噪声水平的响应
- 足够小，以使被控对象在标称工作点附近的近似线性区域内运行，并避免使被控对象输入或输出饱和

当 **Experiment mode** 为 **Superposition** 时，正弦信号叠加。因此，扰动至少可以达到所有幅值之和那么大。确保最大可能的扰动在被控对象执行器的范围内。使执行器饱和可能会给估计的频率响应引入误差。

要通过输入端口提供正弦幅值，请在模块选项卡上选中 **Use external source for sine amplitudes**。

**可调：** Yes

#### 程序化使用

|  |
| --- |
| **模块参数：** `AmpSineAllInner` |
| **类型：** scalar, vector of length 5 |
| **默认值：** 1 |

#### 外环（Speed + Flux）

### **Plant Type** — 外环被控对象的稳定性 `Stable`（默认）| `Integrating`

指定与外环控制环相关联的被控对象是稳定还是积分。如果被控对象有一个或多个积分器，请选择 `Integrating`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PlantTypeAllOuter` |
| **类型：** character vector |
| **值：** `'Stable'` | `'Integrating'` |
| **默认值：** `'Stable'` |

### **Plant Sign** — 外环被控对象的符号 `Positive`（默认）| `Negative`

指定与外环控制环相关联的被控对象是正还是负。如果标称工作点处被控对象输入的正变化导致被控对象输出的正变化，请指定 `Positive`。否则，请指定负。对于稳定被控对象，被控对象的符号就是被控对象直流增益的符号。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PlantSignAllOuter` |
| **类型：** character vector |
| **值：** `'Positive'` | `'Negative'` |
| **默认值：** `'Positive'` |

### **Sine Amplitudes** — 外环中正弦扰动的幅值 1（默认）| scalar | vector of length 5

在实验期间，模块会在频率 [1/10, 1/3, 1, 3, 10]*ωc* 处向与该环关联的被控对象注入正弦信号，其中 *ωc* 是用于整定的目标带宽。使用 **Sine Amplitudes** 指定每个注入信号的幅值。指定：

- 标量值以在每个频率注入相同幅值
- 长度为 5 的向量，以在 [1/10, 1/3, 1, 3, 10]*ωc* 的每个频率指定不同幅值

在具有典型目标带宽的典型被控对象中，实验频率处被控对象响应的幅值变化不大。在这种情况下，可以使用标量值在所有频率施加相同的幅值扰动。但是，如果知道响应在频率范围内急剧衰减，请考虑降低较低频率输入的幅值并提高较高频率输入的幅值。当所有被控对象响应具有可比较的幅值时，估计实验在数值上更好。

扰动幅值必须：

- 足够大，以使扰动克服被控对象执行器中的任何死区，并生成高于噪声水平的响应
- 足够小，以使被控对象在标称工作点附近的近似线性区域内运行，并避免使被控对象输入或输出饱和

当 **Experiment mode** 为 **Superposition** 时，正弦信号叠加。因此，扰动至少可以达到所有幅值之和那么大。确保最大可能的扰动在被控对象执行器的范围内。使执行器饱和可能会给估计的频率响应引入误差。

要通过输入端口提供正弦幅值，请在模块选项卡上选中 **Use external source for sine amplitudes**。

**可调：** Yes

#### 程序化使用

|  |
| --- |
| **模块参数：** `AmpSineAllOuter` |
| **类型：** scalar, vector of length 5 |
| **默认值：** 1 |

### 模块选项卡

### **Use external source for bandwidths** — 为目标带宽提供外部信号 off（默认）| on

选中此参数以启用模块的 `bandwidth` 输入端口。可以在此端口为模块整定的所有环指定目标带宽。当禁用此参数时，请在模块参数中指定目标带宽。更多详细信息，请参阅 `bandwidth` 端口描述。

#### 程序化使用

|  |
| --- |
| **模块参数：** `UseExternalWc` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Use external source for target phase margins** — 为目标相位裕度提供外部信号 off（默认）| on

选中此参数以启用模块的 `target PM` 输入端口。可以在此端口为模块整定的所有环指定目标相位裕度。当禁用此参数时，请在模块参数中指定目标相位裕度。更多详细信息，请参阅 `target PM` 端口描述。

#### 程序化使用

|  |
| --- |
| **模块参数：** `UseExternalPM` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Use external source for start/stops of experiment** — 为整定实验的开始和停止提供外部信号 off（默认）| on

选中此参数以启用模块的 `start/stop` 和 `ActiveLoop` 输入端口。可以在此端口指定实验的开始和停止以及模块整定的环。当禁用此参数时，请在模块参数中指定整定实验的开始时间和持续时间。更多详细信息，请参阅 `start/stop` 和 `ActiveLoop` 端口描述。

#### 程序化使用

|  |
| --- |
| **模块参数：** `UseExternalSourceStartStop` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Use external source for sine amplitudes** — 为正弦扰动幅值提供外部信号 off（默认）| on

选中此参数以启用模块的 `sine Amp` 输入端口。可以在此端口为模块整定的所有环指定正弦扰动幅值。当禁用此参数时，请在模块参数中提供正弦幅值。更多详细信息，请参阅 `sine Amp` 端口描述。

#### 程序化使用

|  |
| --- |
| **模块参数：** `UseExternalAmpSine` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Data Type** — 浮点精度 `double`（默认）| `single`

根据仿真环境或硬件要求指定浮点精度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `BlockDataType` |
| **类型：** character vector |
| **值：** `'double'` | `'single'` |
| **默认值：** `'double'` |

### **Estimated phase margin achieved by tuned controllers** — 最近整定环达到的相位裕度 off（默认）| on

选中此参数以启用模块的 `estimated PM` 输出端口。模块返回最近整定环的整定控制器所达到的相位裕度。当禁用此参数时，可以使用 **Export to MATLAB** 参数查看整定结果。更多详细信息，请参阅 `estimated PM` 端口描述。

#### 程序化使用

|  |
| --- |
| **模块参数：** `UseExternalAchievedPM` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Plant frequency responses near bandwidth** — 最近整定环的估计频率响应 off（默认）| on

选中此参数以启用模块的 `frd` 输出端口。模块返回最近整定环的整定控制器所达到的相位裕度。当禁用此参数时，可以使用 **Export to MATLAB** 参数查看整定结果。更多详细信息，请参阅 `frd` 端口描述。

#### 程序化使用

|  |
| --- |
| **模块参数：** `UseExternalFRD` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Plant nominal input and output** — 标称工作点处的被控对象输入和输出 off（默认）| on

选中此参数以启用模块的 `nominal` 输出端口。模块返回最近整定环在标称工作点处的被控对象输入和输出。当禁用此参数时，可以使用 **Export to MATLAB** 参数查看整定结果。更多详细信息，请参阅该端口描述。

#### 程序化使用

|  |
| --- |
| **模块参数：** `UseExternalU0` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Start/stop of autotuning process** — 指示每个整定环实验开始和结束的信号 off（默认）| on

选中此参数以启用模块的 `loop start/stops` 输出端口。模块返回一个信号，指示模块整定的每个环的自整定实验开始和结束的时间。当禁用此参数时，可以使用 **Export to MATLAB** 参数查看整定结果。更多详细信息，请参阅 `loop start/stops` 端口描述。

#### 程序化使用

|  |
| --- |
| **模块参数：** `UseExternalActiveLoop` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Export to MATLAB** — 将实验和整定结果发送到 MATLAB 工作区按钮

单击此按钮时，模块会在 MATLAB® 工作区中创建一个结构体，其中包含实验和整定结果。此结构体 `FOCTuningResult` 包含模块整定的每个环的整定结果。

- `Daxis` — D 轴电流环整定结果
- `Qaxis` — Q 轴电流环整定结果
- `Speed` — 速度环整定结果
- `Flux` — 磁通环整定结果

对于模块整定的每个环，结果包含以下字段：

- `P`, `I`, `D`, `N` — 整定后的 PID 增益。该结构体包含所整定控制器类型所需的这些字段中的任意字段。例如，如果要整定 PI 控制器，则该结构体包含 `P` 和 `I`，但不包含 `D` 和 `N`。
- `TargetBandwidth` — 在模块的 `Target bandwidth (rad/sec)` 参数中指定的值。
- `TargetPhaseMargin` — 在模块的 `Target phase margin (degrees)` 参数中指定的值。
- `EstimatedPhaseMargin` — 整定后系统达到的估计相位裕度。
- `Controller` — 整定后的 PID 控制器，返回为 `pid`（用于并联形式）或 `pidstd`（用于理想形式）模型对象。
- `Plant` — 估计的被控对象，返回为 `frd` 模型对象。此 `frd` 包含在实验频率 [1/10, 1/3, 1, 3, 10]*ωc* 处获得的响应数据。
- `PlantNominal` — 实验开始时标称工作点处的被控对象输入和输出，指定为具有字段 `u`（输入）和 `y`（输出）的结构体。

可以在仿真运行时导出到 MATLAB 工作区，包括在外部模式下运行时。

## 所属库

Motor Control Blockset / Controls / Controllers

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块生成的代码可能占用大量资源。对于实时应用，建议将代码部署到快速原型硬件上，例如 Speedgoat 实时目标机。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a：支持 PRBS 输入信号

Field Oriented Control Autotuner 模块现在支持使用伪随机二进制序列（PRBS）输入信号进行估计。PRBS 信号是一种周期性、确定性信号，具有类似白噪声的特性，并在两个值之间切换。与使用 sinestream 或 superposition 输入信号相比，PRBS 信号可减少总估计时间，同时产生可比的估计结果。PRBS 信号可用于估计通信和电力电子应用的频率响应。

## 描述

在磁场定向控制应用中自动且顺序地整定多个 PID 控制环

Field Oriented Control Autotuner 模块允许您在磁场定向控制 (FOC) 应用中实时自动整定 PID 控制环。有关磁场定向控制的详细信息，请参阅 Field-Oriented Control (FOC)。

您可以自动整定与以下环关联的 PID 控制器：

- 直轴（d-axis）电流环
- 交轴（q-axis）电流环
- 速度环
- 磁通环

对于该模块整定的每个环，Field Oriented Control Autotuner 模块会在闭环中执行自动整定实验，而无需与该环关联的参数模型。该模块允许您指定控制环的整定顺序。当针对一个环运行整定实验时，该模块对其他环没有影响。在实验期间，该模块：

1. 将测试信号注入与该环关联的被控对象，以收集被控对象输入输出数据并实时估计频率响应。该测试信号是叠加在被控对象输入上的正弦扰动信号的组合。
2. 在实验结束时，根据目标带宽附近的估计被控对象频率响应整定 PID 控制器参数。
3. 在模块输出端写入更新后的 PID 增益，使您能够将新增益传输到现有控制器并验证闭环性能。

您可以使用 Field Oriented Control Autotuner 模块来整定 FOC 结构中现有的 PID 控制器。如果您没有初始 PID 控制器，可以使用 Estimate Control Gains and Use Utility Functions 工作流来获取它们。然后，您可以使用 Field Oriented Control Autotuner 模块进行细化或重新整定。

如果您有代码生成产品（例如 Simulink® Coder™），则可以生成在硬件上实现整定算法的代码，让您能够实时整定，使用或不使用 Simulink 来管理自动整定过程。

如果您在 Simulink 中使用 Motor Control Blockset™ 对电机进行了建模，并且具有带 PID 控制器的初始 FOC 结构，则您可以针对建模的电机执行闭环 PID 自动整定。这样做可以让您在实时整定控制器之前预览被控对象响应并调整 PID 自动整定设置。

该模块支持使用 Simulink Coder、Embedded Coder® 和 Simulink PLC Coder™ 进行代码生成。它不支持使用 HDL Coder™ 进行代码生成。对于实时应用，请将生成的代码部署到快速原型硬件（例如 Speedgoat® 实时目标机）上。

有关使用 Field Oriented Control Autotuner 模块的详细信息，请参阅 How to Use Field Oriented Control Autotuner Block。

此模块需要 Simulink Control Design™ 软件。
