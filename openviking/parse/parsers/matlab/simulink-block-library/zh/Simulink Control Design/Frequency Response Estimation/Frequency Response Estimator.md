---
type: simulink-block
title: 'Frequency Response Estimator'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Frequency Response Estimation'
documentation_page: 'frequencyresponseestimator'
documentation_source_path: 'ug/frequencyresponseestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# Frequency Response Estimator

## 端口

### 输入

### **u** — 扰动前的被控对象输入 标量

将模块插入系统中，使该端口接受控制信号或其他被控对象输入信号。例如，在闭环配置中，可以按下图所示连接该端口。

在开环配置中，可以将该输入端口连接到驱动被控对象达到估计所需工作点的信号源。例如，可以使用设置为适当值的 Constant 模块。

**数据类型：** `single` | `double`

### **y** — 被控对象输出 标量

将该端口连接到被控对象输出。

**数据类型：** `single` | `double`

### **start/stop** — 启动和停止估计实验 标量

要启动和停止估计过程，请在 `start/stop` 端口提供信号。当信号值发生以下变化时：

- 从负值或零变为正值，实验启动
- 从正值变为负值或零，实验停止

通常，可以使用从 0 变为 1 的信号来启动实验，使用从 1 变为 0 的信号来停止实验。当实验未运行时，模块不会在 **u + Δu** 或 **Δu** 端口添加任何扰动。在此状态下，模块对被控对象行为没有影响。

在被控对象处于所需平衡工作点时启动实验。在闭环配置中，使用控制器驱动被控对象达到工作点。在开环配置中，可以使用连接到 **u** 的信号源模块驱动被控对象达到工作点。

让实验运行足够长的时间，使算法能够收集足够的数据，以便在其探测的所有频率上获得良好的估计。模块在模块参数的 **Experiment Length** 部分显示推荐的实验长度。该值基于实验模式和您为实验指定的频率。

- 当 **Experiment mode** 为 **Sinestream** 时，推荐的实验长度为：

  ∑i2πωi(Nset,i+Nestim,i)+2TsNfreq,

  其中：

  - *ωi* 是 **Frequencies** 参数中指定的第 *i* 个频率（单位为 rad/s）。
  - *Nfreq* 是 **Frequencies** 中的频率数量。
  - *N**set*,*i* 是 **Number of settling periods** 参数的对应值。
  - *N**estim*,*i* 是 **Number of estimation periods** 参数的对应值。
  - *Ts* 是实验采样时间，由 **Sample time (Ts)** 参数指定。
- 当 **Experiment mode** 为 **Superposition** 时，推荐的实验长度为最长周期的六倍。如果您的系统不需要太多时间用于瞬态衰减或噪声平均消除，则可以使用较短的实验长度。有关如何在 superposition 模式下确定实验长度的更多信息，请参阅 Experiment Length and Data-Collection Window in Superposition Mode。
- 当 **Experiment mode** 为 **PRBS** *(自 R2023a 起)* 时，推荐的实验长度为：

  Ts(2n−1)Np,

  其中：

  - *T*s 是实验采样时间，由 **Sample time (Ts)** 参数指定。
  - *n* 是 PRBS 信号阶数，由 **Signal order** 参数指定。
  - *N*p 是 PRBS 信号中的周期数，由 **Number of periods** 参数指定。

在实验期间避免对被控对象施加任何负载扰动。负载扰动会扭曲被控对象输出并降低频率响应估计的精度。

**数据类型：** `single` | `double`

### **w** — 估计实验的频率 向量

为 **Frequencies** 参数提供值。有关如何选择频率的信息，请参阅该参数。

当通过此端口提供频率时，请使用 **Number of frequencies in the excitation signal** 参数指定频率数量。

#### 依赖关系

要启用此端口，请在 **Excitation Signal Source** 中选择
**External ports**。

**数据类型：** `single` | `double`

### **amp** — 扰动幅值 标量 | 向量

为 **Amplitudes** 参数提供一个值。有关详细信息，请参阅该
参数。

#### 依赖关系

要启用此端口，请在 **Excitation Signal Source** 中选择
**External Ports**。

**数据类型：** `single` | `double`
### 输出

### **u + Δu** — 受扰对象输入 标量

将模块插入系统中，使此端口将输入信号馈送到
对象，如下图所示。

- 当实验正在运行（**start/stop** 为正）时，
  模块在此端口向对象注入测试信号。如果您有任何饱和
  或速率限制保护对象，请将来自 **u +
  Δu** 的信号馈入其中。
- 当实验未运行（**start/stop** 为零或
  负）时，模块将信号从 **u** 原样传递到
  **u + Δu**。在此状态下，模块对
  对象没有影响。

#### 依赖关系

要启用此端口，请在 **Output Signal Configuration** 中选择
**control action + perturbation**。

**数据类型：** `single` | `double`

### **Δu** — 对象输入扰动 标量

模块在此端口生成扰动信号。通常，您通过求和模块从此端口注入
扰动，如下图所示。

- 当实验正在运行（**start/stop** 为正）时，
  模块在此端口生成扰动信号。
- 当实验未运行（**start/stop** 为零或
  负）时，此端口处的信号为零。在此状态下，模块对
  对象没有影响。

#### 依赖关系

要启用此端口，请在 **Output Signal Configuration** 中选择
**perturbation only**。

**数据类型：** `single` | `double`

### **data** — 实验数据总线

此端口处的信号包含模块在频率响应估计实验期间采集的数据，包括施加到被控对象的扰动信号和测得的被控对象响应。当您希望记录实验数据以供后续使用时，请使用此端口。例如，您可以通过记录数据并离线执行估计来节省部署环境中的资源（请参阅**估计模式**）。有两种方式可以访问频率响应实验数据。

- 使用 To Workspace 模块将数据写入 MATLAB® 工作区，形式为包含 timeseries 数据的结构体。To Workspace 模块的 **Save format** 参数必须为 `Timeseries`。该结构体具有以下字段：

  - `Ready` — 逻辑信号，指示哪些时间步包含在估计计算中（1）以及哪些被排除（0）。例如，对于 sinestream 模式，此信号仅对落在由 **Number of settling periods** 和 **Number of estimation periods** 参数确定的周期内的数据为 1。在 superposition 模式下，此信号仅对落在 Experiment Length and Data-Collection Window in Superposition Mode 中描述的窗口内的数据为 1。对于 PRBS 信号，此信号仅对落在实际实验长度内的数据为 1。
  - `Perturbation` — 施加到被控对象的正弦扰动 `Δu`
  - `PlantInput` — 被控对象输入信号 `u + Δu`，其中 `u` 是在模块输入端口 **y** 处采集的信号
  - `PlantOutput` — 在模块输入端口 **y** 处采集的被控对象输出信号
- 使用 Simulink 数据记录将数据写入工作区，形式为 `Simulink.SimulationData.Dataset` 对象。在这种情况下，包含四个 timeseries 信号的结构体存储在所得 dataset 的 `Values` 字段中。例如，假设模型配置为将记录的数据保存到变量 `logsout`，并且 **data** 是唯一记录的端口。在这种情况下，该结构体包含在 `logsout{1}.Values` 中。

您可以使用此端口的数据来离线执行频率响应估计。例如，您可以通过将结构体传递给 `frestimate` 命令来在 MATLAB 中计算估计的频率响应。有关访问和使用实验数据的详细信息，请参阅 Collect Frequency Response Experiment Data for Offline Estimation。

**数据类型：** `single` | `double`

### **frd** — 估计的频率响应向量

此端口处的信号包含被控对象的估计频率响应，以向量的形式表示，其中 **Frequencies** 参数中指定的每个频率对应一个条目。您可以使用 To Workspace 模块将此信号写入 MATLAB 工作区，或使用 Simulink 数据记录将数据写入工作区，形式为 `Simulink.SimulationData.Dataset` 对象。

通常，最佳估计在实验结束时获得。因此，您可能不需要记录此端口处的所有历史数据。相反，您可以丢弃除最后一个时间步之外每个时间步的值。例如，在 To Workspace 模块中，您可以将 **Limit data points to last** 参数设置为 1。然后，当实验结束时，所得的工作区变量包含一个复数值向量，其中 **Frequencies** 参数中指定的每个频率对应一个值。

对于 **PRBS** 实验模式，此端口处的信号仅在估计实验完成后更新。*（自 R2023a 起）*

#### 依赖关系

要启用此端口，请将 **Estimation Mode** 设置为 **Online**。

**数据类型：** `single` | `double`

## 参数

### **Sample time (Ts)** — 实验采样时间 0.1（默认）| 正标量 | –1

该模块是一个离散时间模块，以固定的采样时间运行，采样时间由该参数指定。您可以估计的最大频率为奈奎斯特频率，*π*/*Ts* rad/s。最佳实践是使用至少比奈奎斯特频率快五倍的采样时间。

*Ts* =
*π*/(5*ωmax*) ≅
0.6/*ωmax* 或
0.1/*fmax*，

此处，*ωmax* 是 **Frequencies** 中的最高频率，单位为 rad/s，*fmax* 是以 Hz 为单位的最高频率。采样时间必须足够小，以估计所需的最快频率，但也不能太小，以免引入不必要的计算负担。

如果将采样时间设置为 –1，则软件在编译时根据模块外部的源确定采样时间。将采样时间设置为 –1 会禁用模块内部的检查，这些检查用于确保您的估计频率低于奈奎斯特频率。

#### 提示

如果您希望在应用中以不同的采样时间运行已部署的模块，请将此参数设置为 –1，并将该模块放入 Triggered Subsystem 中。然后，以所需的采样时间触发该子系统。如果您不打算在部署后更改采样时间，请指定一个固定且有限的采样时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`DiscreteTs` |
| **类型**：scalar |
| **Value** positive scalar | –1 |
| **默认值**：0.1 |

### **Output Signal Configuration** — 提供控制信号加扰动或仅扰动 **control action + perturbation**（默认）| **perturbation only**

默认情况下，该模块将控制信号作为输入，并在端口 **u+Δu** 处提供控制信号加实验扰动。然后，您将此信号馈入被控对象输入，如下图所示。

此默认配置需要在控制器和被控对象之间插入该模块。如果您想自行将扰动信号添加到控制信号中，请选择 **perturbation only**。在此配置中，模块输出仅包含扰动信号，位于端口 **Δu**。您可以使用例如求和模块将此扰动信号注入被控对象，如下图所示。

在此配置中，由于 Frequency Response Estimator 不属于闭环的一部分，您可以选择将其注释掉而不会破坏回路配置。

### **Data Type** — 浮点精度 `double`（默认）| `single`

根据仿真环境或硬件要求指定浮点精度。

#### 编程使用

|  |
| --- |
| **模块参数**：`BlockDataType` |
| **类型**：character vector |
| **值**：`'double'` | `'single'` |
| **默认值**：`'double'` |

### **Excitation signal source** — 激励信号源 **Block parameters**（默认）| **External ports**

指定是通过模块参数还是通过外部端口提供实验扰动信号的频率和幅值。

- **Block parameters** — 选择此项以启用 **Frequencies** 和 **Amplitudes** 参数。
- **External ports** — 选择此项以启用 **w** 和 **amp** 输入端口。如果您希望在部署后更改扰动信号的频率和幅值，请使用此选项。

#### 编程使用

|  |
| --- |
| **模块参数**：`SineSource` |
| **类型**：character vector, string |
| **值**：`'Block parameters'` | `'External ports'` |
| **默认值**：`'Block parameters'` |

### **Frequencies** — 用于估计的频率 [0.5 1 2]（默认）| 向量

用于估计被控对象频率响应的频率。该模块会在每个频率处注入扰动。您可以估计的最高频率受奈奎斯特频率限制，即 *π*/*Ts* rad/s，其中 *Ts* 是您为 **Sample time (Ts)** 参数设置的值。

当 **Experiment mode** 为 **Superposition** 时：

- 为保持合理的收敛速度和估计精度，通常使用约 20–30 个频率进行估计。最佳实践是指定不超过约 50 个频率。
- 最佳实践是将最低频率与最高频率之间的范围限制在不超过约两个数量级。该限制可降低某些频率的响应过于主导，从而损害其他频率处响应估计的可能性。
- 尝试使用叠加模式且频率超过 50 个来线性化包含 Frequency Response Estimator 模块的模型时，可能会生成错误。该错误指出“The model contains too many elements for linearization. Please reduce the model size.”要完成线性化，您必须注释掉频率响应估计器模块或减少频率数量。

当 **Experiment mode** 为 **Sinestream** 时，对频率数量或范围没有推荐限制。但是，由于 sinestream 扰动的顺序性质，您添加的每个频率点都会增加所需的实验时间（有关详细信息，请参见 **start/stop** 输入端口）。此外，频率范围过宽会要求您对高频使用快速采样时间，而这对于较低频率而言效率低下。

当 **Experiment mode** 为 **PRBS** 时，频率范围会影响实验长度。最低频率值决定可覆盖指定频率的最小信号阶数。降低最低频率范围会增加所需的最小信号阶数，因此会增加实验长度。但是，由于 PRBS 输入信号的宽带特性，添加更多频率点不会增加实验长度。

当您在闭环配置中使用该模块时，远高于开环带宽的频率可能会导致估计精度降低。

#### 提示

此参数不可调。要在部署后提供频率，请将 **Excitation Signal Source** 设置为 **External ports**，并使用 **w** 输入端口。有关详细信息，请参见 Deploy Frequency Response Estimation Algorithm for Real-Time Use。

#### 依赖关系

要启用此参数，请将 **Excitation Signal Source** 设置为 **Block parameters**。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Frequencies` |
| **类型**：vector |
| **值**：positive real values |
| **默认值**：`'[0.5 1 2]'` |

### **Frequency units** — 频率单位 `rad/s`（默认）| `Hz`

指示 **Frequencies** 参数的值是以弧度每秒还是赫兹为单位。

要启用此参数，请将 **Excitation Signal Source** 设置为 **Block parameters**。

#### 程序化使用

|  |
| --- |
| **模块参数**：`FreqUnits` |
| **类型**：string, character vector |
| **值**：`'rad/s'`,`'Hz'` |
| **默认值**：`'rad/s'` |

### **Amplitudes** — 注入扰动信号的幅值 1（默认）| 标量 | 向量

指定注入到被控对象中的扰动信号的幅值。若要对所有频率使用相同的幅值，请指定一个标量值。如果您知道响应在待估计的频率范围内变化显著，则可以使用向量为每个频率指定不同的幅值。例如，您可以在已知谐振频率附近使用较小的值，而在滚降频率以上使用较大的值。该向量必须与您为 **Frequencies** 提供的向量长度相同。

幅值必须满足：

- 足够大，使扰动能够克服被控对象执行器中的任何死区，并产生高于噪声水平的响应
- 足够小，使被控对象在标称工作点附近的近似线性区域内运行，并避免使被控对象输入或输出饱和

当 **Experiment mode** 为 **Superposition** 时，正弦信号无相移地叠加。因此，最大扰动可能超过任何单个分量的幅值，最高可达所有幅值之和。请确保最大可能的扰动在被控对象执行器的范围内。使执行器饱和可能会在估计的频率响应中引入误差。

#### 提示

此参数不可调。要在部署后提供幅值，请将 **Excitation Signal Source** 设置为 **External ports**，并使用 **amp** 输入端口。有关详细信息，请参阅 Deploy Frequency Response Estimation Algorithm for Real-Time Use。

#### 依赖关系

要启用此参数，请将 **Excitation Signal Source** 设置为 **Block parameters**。

#### 编程用法

|  |
| --- |
| **模块参数：** `Amplitudes` |
| **类型：** 标量、向量 |
| **默认值：** `'1'` |

### **Number of frequencies in the excitation signal** — 外部提供的频率数量 3（默认）| 正整数

当您通过外部端口 **w** 提供实验频率时，请使用此参数指定频率数量（即 **w** 处向量信号的长度）。

#### 依赖关系

要启用此参数，请将 **Excitation Signal Source** 设置为 **External ports**。

#### 编程用法

|  |
| --- |
| **模块参数：** `NumOfFreq` |
| **类型：** 标量 |
| **默认值：** `'3'` |

### **Experiment mode** — 实验模式 **Sinestream**（默认）| **Superposition** | **PRBS** *（自 R2023a 起）*

指定每个频率处的扰动是以顺序正弦（**Sinestream**）、同时正弦（**Superposition**）还是伪随机二进制序列（**PRBS**）方式施加。

- **Sinestream** — 在此模式下，每个频率处分别施加扰动。使用 **Number of settling periods** 参数指定每个频率处允许系统稳定的周期数。使用 **Number of estimation periods** 参数指定测量响应的周期数。有关用于估计的 sinestream 信号的更多信息，请参阅 Sinestream Input Signals。
- **Superposition** — 在此模式下，扰动信号一次性包含所有指定频率。对于在频率向量 *ω* = [*ω*1, … , *ωN*] 处以幅值 *A* = [*A*1, … , *AN*] 进行频率响应估计，扰动信号为：

  Δu=∑iAisin(ωit)。

  最佳实践是在 superposition 信号中使用不超过约 50 个频率。
- **PRBS** — 一种确定性的伪随机二进制序列，在两个值之间切换，具有类似白噪声的特性。与使用 sinestream 输入信号相比，PRBS 信号可减少总估计时间，同时产生相当的估计结果。PRBS 信号对于估计通信和电力电子系统的频率响应非常有用。有关更多信息，请参阅 PRBS Input Signals。*（自 R2023a 起）*

**Sinestream** 模式比 **Superposition** 模式更精确，并且可以适应更宽的频率范围（请参阅 **Frequencies** 参数）。**Sinestream** 模式还可以具有更低的侵入性，因为扰动的总大小永远不会大于 **Amplitudes** 参数指定的值。然而，由于 sinestream 扰动的顺序特性，您添加的每个频率点都会增加推荐的实验时间（有关详细信息，请参阅 **start/stop** 输入端口）。因此，**Superposition** 模式下的估计实验通常比 **Sinestream** 模式快得多，且结果令人满意。

**PRBS** 模式可以包含比其他两种模式多得多的频率点，因为 PRBS 输入信号是宽带信号。要覆盖相似的频率范围，实验长度通常比其他两种模式短得多。然而，速度和结果质量之间存在权衡。为了获得更高质量的结果，您可能希望使用具有多个周期的信号，但这也会导致更长的实验长度。*（自 R2023a 起）*

#### 提示

尝试使用 superposition 模式和超过 50 个频率对包含 Frequency Response Estimator 模块的模型进行线性化可能会生成错误。错误信息为“The model contains too many elements for linearization. Please reduce the model size.”要完成线性化，您必须注释掉频率响应估计器模块或减少频率数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`ExperimentMode` |
| **类型**：character vector, string |
| **值**：`'Sinestream'` | `'Superposition'` | `'PRBS'` |
| **默认值**：`'Sinestream'` |

### **Number of settling periods** — 等待瞬态稳定的周期数 2（默认）| 正整数 | 正整数向量

在 sinestream 实验模式下，模块在 **Frequencies** 中指定的每个频率处注入单独的扰动。使用 **Number of settling periods** 指定在每个频率处等待多长时间后开始该频率的估计。等待可以让被控对象响应中的任何瞬态衰减，从而提高估计频率响应的精度。等待更多周期可以提高估计精度，但也会增加实验时间。

要对所有频率使用相同的稳定周期数，请指定一个正标量值。如果您知道在要估计的频率范围内瞬态以不同速率稳定，则可以使用向量为每个频率指定不同的稳定周期数。

有关用于估计的 sinestream 信号的详细信息，请参阅 Sinestream Input Signals。

**可调：** 是

#### 依赖关系

要启用此参数，请在 **Experiment Mode** 中选择 **Sinestream**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `NumOfSetPeriod` |
| **类型：** integer, vector of integers |
| **默认：** `'2'` |

### **Number of estimation periods** — 稳定后用于估计的周期数 4（默认）| 整数 ≥ 2 | 整数向量

在 sinestream 实验模式下，模块在 **Frequencies** 中指定的每个频率处注入单独的扰动。使用 **Number of estimation periods** 指定在每个频率处用于估计的注入信号周期数。使用更多周期可以提高估计精度，但也会增加实验时间。

要对所有频率使用相同的估计周期数，请指定一个大于或等于 2 的标量值。您可以使用向量为每个频率指定不同的稳定周期数。当您知道系统在某些频率处噪声较小，或者您不太关心某些频率处的精度时，此方法很有用。

有关用于估计的 sinestream 信号的详细信息，请参阅 Sinestream Input Signals。

**可调：** 是

#### 依赖关系

要启用此参数，请在 **Experiment Mode** 中选择 **Sinestream**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `NumOfEstPeriod` |
| **类型：** integer, vector of integers |
| **默认：** `'4'` |

### **Number of periods of the lowest frequency used for estimation** — 数据收集窗口的持续时间 3（默认）| 1 到 5 之间的整数

在 superposition 实验模式下，模块在实验运行期间同时在所有频率处施加扰动。模块使用此参数确定用于估计的数据收集窗口的长度。有关数据收集窗口的详细信息，请参阅 Experiment Length and Data-Collection Window in Superposition Mode。

#### 依赖关系

要启用此参数，请在 **Experiment Mode** 中选择 **Superposition**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `NumOfSlowestPeriod` |
| **类型：** integer |
| **默认：** `'3'` |

### **Number of periods** — PRBS 信号中的周期数 1（默认）| 正整数

*自 R2023a 起*

PRBS 信号中的周期数，指定为正整数。

根据指定的频率和采样时间，模块在模块对话框的 **Experiment Length** 部分中显示此参数的推荐值。

#### 依赖关系

要启用此参数，请在 **Experiment Mode** 中选择 **PRBS**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `NumOfPRBSPeriod` |
| **类型：** positive integer |
| **默认：** `'1'` |

### **Signal order** — PRBS 信号阶数 12（默认）| 小于等于 24 的正整数

*自 R2023a 起*

信号阶数，指定为正整数。PRBS 信号的最大长度为 2*n*–1，其中 *n* 为信号阶数。要获得准确的频率响应估计，PRBS 的长度必须足够大。

对于给定的采样时间，要获得更高的频率分辨率，请指定更大的信号阶数。指定小于等于 24 的值以防止实验运行时间过长。

根据指定的频率和采样时间，模块会在模块对话框的 **Experiment Length** 部分显示此参数的推荐值。

#### 依赖关系

要启用此参数，请在 **Experiment Mode** 中选择 **PRBS**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PRBSSignalOrder` |
| **类型：** 小于等于 24 的正整数 |
| **默认值：** `'12'` |

### **Use Auto-Generated Value** — 自动设置 PRBS 信号参数 `off`（默认）| `on`

*自 R2023b 起*

模块根据指定的频率和采样时间计算 **Number of periods** 和 **Signal order** 参数的推荐值。启用此选项可对 PRBS 信号参数中的一个或两个使用自动生成的值。当您在频率范围或采样时间变化的情况下运行多个实验时，这非常有用。

#### 依赖关系

- 要启用此参数，请将 **Experiment Mode** 设置为 **PRBS**。
- 当 **Excitation Signal Source** 设置为 **External ports** 且 **Estimation Mode** 为 **Online** 时，此参数不可用。

### **Estimation mode** — 模块执行估计还是仅收集响应数据 **Online**（默认）| **Offline**

指定是在线执行频率响应估计计算，还是仅收集频率响应数据以供后续离线估计。

- **Online** — 模块在实验运行期间收集实验数据并计算估计的频率响应。您可以在 **frd** 端口获取所得的估计频率响应（有关更多信息，请参阅该端口描述）。
- **Offline** — 模块仅收集实验数据，不计算估计的频率响应。您可以在 **data** 端口获取实验数据（有关更多信息，请参阅该端口描述）。然后您可以离线执行频率响应估计。例如，您可以使用 MATLAB 中的数据通过 `frestimate` 命令计算估计的频率响应。有关更多信息，请参阅 Collect Frequency Response Experiment Data for Offline Estimation。

#### 程序化使用

|  |
| --- |
| **模块参数：** `EstimationMode` |
| **类型：** 字符向量、字符串 |
| **值：** `'Online'` | `'Offline'` |
| **默认值：** `'Online'` |

### **Display Bode plot** — 绘制估计的频率响应 `off`（默认）| `on`

选择此项可生成显示估计频率响应的 Bode 图。该图在估计实验期间定期更新。如果您有表示预期被控对象响应或其他相关基线的 LTI 模型，请使用 **Baseline plant model** 参数将其包含在图中以供参考。

#### 提示

- 要加速包含 Frequency Response Estimator 模块的模型的修剪或线性化，请清除此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `UseBodePlot` |
| **类型：** 字符向量、字符串 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Baseline plant model** — Bode 图的基线模型 `[]`（默认）| LTI 模型

指定要与估计的频率响应一起绘制的基线模型。使用 LTI 模型，例如 `tf`、`ss` 或 `frd` 模型。

**示例：** `tf(10,[1 10 1000])`

#### 依赖关系

要启用此参数，请选择 **Display Bode plot**。

#### 编程用法

|  |
| --- |
| **模块参数：** `BaselinePlant` |
| **类型：** LTI model |
| **默认值：** `'[]'` |

### **Refresh plot every N\*Ts seconds where N is** — 更新 Bode 图的频率 100（默认）| 标量

在频率响应估计实验期间，该模块按照您使用此参数指定的频率，使用估计的频率响应更新 Bode 图。如果刷新 Bode 图耗时过长，请增大该值。

对于 **PRBS** 模式，估计在实验结束时进行，因此 Bode 图仅更新一次。

#### 依赖关系

要启用此参数，请选择 **Display Bode plot**。

#### 编程用法

|  |
| --- |
| **模块参数：** `PlotRefreshFactor` |
| **类型：** integer |
| **默认值：** `'100'` |

## 所属库

Simulink Control Design / Frequency Response Estimation

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**在 R2019a 中引入**

### R2023b：库位置变更

Frequency Response Estimator 模块现在位于 **Simulink Control Design/Frequency Response Estimation** 子库中。

在 R2023b 中，当您打开在先前版本中保存的模型时，Frequency Response Estimator 模块的库链接会自动更新。

### R2023a：PRBS 输入信号

Frequency Response Estimator 模块现在支持使用伪随机二进制序列（PRBS）输入信号进行估计。PRBS 信号是一种周期性的确定性信号，具有类似白噪声的特性，并在两个值之间切换。与使用 sinestream 或 superposition 输入信号相比，PRBS 信号可减少总估计时间，同时产生相当的估计结果。PRBS 信号对于估计通信和电力电子应用的频率响应非常有用。

## 描述

在仿真期间或实时估计被控对象频率响应

使用频率响应估计器模块，通过物理被控对象实时或在仿真期间在 Simulink® 模型中执行基于实验的估计。为获得估计的频率响应，该模块同时：

- 在标称工作点向被控对象注入扰动信号
- 从被控对象输出采集响应数据
- 计算估计的频率响应

您指定扰动被控对象和测量系统响应的频率。您通过启动/停止信号触发估计过程。该信号允许您在任何时候启动估计，通常在被控对象处于标称工作点时。在频率响应收敛后停止估计。

您可以对任何稳定的 SISO 被控对象使用在线频率响应估计。对于不稳定被控对象，在线估计在闭环配置下工作，前提是闭环是内部稳定的。闭环系统是内部稳定的，当且仅当标称闭环特征方程的所有根都位于开左半平面。对于传递函数为 *G* = *NG*/*DG* 的被控对象和控制器 *C* = *NC*/*DC*，特征方程为：

*DGDC* + *NGNC* = 0。

在实践中，此条件意味着 *G* 中没有不稳定极点被 *GC* 中的零极点对消所稳定。不要对不满足此条件的不稳定被控对象使用在线估计。

您可以生成代码并将频率响应估计器模块部署到硬件上以实时执行估计。该模块支持使用 Simulink Coder™、Embedded Coder® 和 Simulink PLC Coder™ 进行代码生成。它不支持使用 HDL Coder™ 进行代码生成。

有关使用频率响应估计器模块的更多信息，请参阅：

- 使用 Simulink 中建模的被控对象进行在线估计
- 部署频率响应估计算法用于实时应用

有关在线频率响应估计的更一般信息，请参阅在线频率响应估计基础。
