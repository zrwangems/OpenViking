---
type: simulink-block
title: 'Unscented Kalman Filter'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'State Estimation'
documentation_page: 'ukf_block'
documentation_source_path: 'ref/ukf_block.html'
language: zh-CN
chinese_source: worker-translation
---

# Unscented Kalman Filter

## 端口
```yaml
ports:
- name: y1,y2,y3,y4,y5
  summary: 测量的系统输出向量
  direction: input
  data_types: single | double
- name: StateTransitionFcnInputs
  summary: 状态转移函数的附加可选输入参数 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double
- name: MeasurementFcn1Inputs,MeasurementFcn2Inputs,MeasurementFcn3Inputs,MeasurementFcn4Inputs,MeasurementFcn5Inputs
  summary: 每个测量函数的附加可选输入参数 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double
- name: Q
  summary: 时变过程噪声协方差 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double
- name: R1,R2,R3,R4,R5
  summary: 时变测量噪声协方差矩阵
  direction: input
  data_types: single | double
- name: Enable1,Enable2,Enable3,Enable4,Enable5
  summary: 当测量数据可用时启用估计状态的校正 标量
  direction: input
  data_types: single | double | Boolean
- name: xhat
  summary: 估计状态向量
  direction: output
  data_types: single | double
- name: P
  summary: 状态估计误差协方差矩阵
  direction: output
  data_types: single | double
```

### 输入

### **y1,y2,y3,y4,y5** — 测量的系统输出向量

与您在模块中指定的每个测量函数相对应的测量系统输出。端口数量等于系统中的测量函数数量。您最多可以指定五个测量函数。例如，如果您的系统有两个传感器，则您在模块中指定两个测量函数。第一个端口 **y1** 默认可用。当您点击 **Apply** 时，软件会生成与第二个测量函数对应的端口 **y2**。

将端口指定为 *N* 维向量，其中 *N* 是对应传感器测量的量数。例如，如果您的系统有一个传感器测量物体的位置和速度，则只有一个端口 **y1**。该端口被指定为二维向量，其值对应于位置和速度。

#### 依赖关系

第一个端口 **y1** 默认可用。当您点击 **Add Measurement** 并点击 **Apply** 时，会生成端口 **y2** 到 **y5**。

**数据类型：** `single` | `double`

### **StateTransitionFcnInputs** — 状态转移函数的附加可选输入参数 标量 | 向量 | 矩阵

状态转移函数 `f` 的附加可选输入参数，除状态 `x` 和过程噪声 `w` 之外。有关状态转移函数的信息，请参阅 State Transition and Measurement Functions。

假设您的系统具有非加性过程噪声，并且状态转移函数 `f` 具有以下形式：

`x(k+1) =
f(x(k),w(k),StateTransitionFcnInputs)`。

这里 `k` 是时间步，`StateTransitionFcnInputs` 是除 `x` 和 `w` 之外的附加输入参数。

如果您使用 MATLAB® 函数（`.m` 文件）创建 `f`，则当您点击 **Apply** 时，软件会生成端口 **StateTransitionFcnInputs**。您可以将此端口的输入指定为标量、向量或矩阵。

如果您的状态转移函数有多个附加输入，请使用 Simulink Function (Simulink) 模块来指定该函数。当您使用 Simulink Function 模块时，您使用 Inport (Simulink) 模块直接向 Simulink Function 模块提供附加输入。在 Unscented Kalman Filter 模块中不会为附加输入生成输入端口。有关示例，请参阅 Online State Estimation Using Identified Nonlinear Models (System Identification Toolbox)。

#### 依赖关系

仅当以下两个条件都满足时，才会生成此端口：

- 您在 **Function** 中使用 MATLAB 函数指定 `f`，并且 `f` 在 MATLAB 路径上。
- `f` 除 `x` 和 `w` 之外仅需要一个附加输入参数。

**数据类型：** `single` | `double`

### **MeasurementFcn1Inputs,MeasurementFcn2Inputs,MeasurementFcn3Inputs,MeasurementFcn4Inputs,MeasurementFcn5Inputs** — 每个测量函数的附加可选输入参数 标量 | 向量 | 矩阵

测量函数的附加可选输入，除状态 `x` 和测量噪声 `v` 之外。有关测量函数的信息，请参阅 State Transition and Measurement Functions。

**MeasurementFcn1Inputs** 对应于您指定的第一个测量函数，依此类推。例如，假设您的系统有三个传感器和非加性测量噪声，并且三个测量函数 `h1`、`h2` 和 `h3` 具有以下形式：

`y1[k] = h1(x[k],v[k],MeasurementFcn1Inputs)`

`y2[k] = h2(x[k],v[k],MeasurementFcn2Inputs)`

`y3[k] = h3(x[k],v[k])`

这里 `k` 是时间步，`MeasurementFcn1Inputs` 和 `MeasurementFcn2Inputs` 是 `h1` 和 `h2` 的附加输入参数。

如果您在 **Function** 中使用 MATLAB 函数（`.m` 文件）指定 `h1`、`h2` 和 `h3`，则当您点击 **Apply** 时，软件会生成端口 **MeasurementFcn1Inputs** 和 **MeasurementFcn2Inputs**。您可以将这些端口的输入指定为标量、向量或矩阵。

如果您的测量函数有多个附加输入，请使用 Simulink Function (Simulink) 模块来指定这些函数。当您使用 Simulink Function 模块时，您使用 Inport (Simulink) 模块直接向 Simulink Function 模块提供附加输入。在 Unscented Kalman Filter 模块中不会为附加输入生成输入端口。有关示例，请参阅 Online State Estimation Using Identified Nonlinear Models (System Identification Toolbox)。

#### 依赖关系

仅当以下两个条件都满足时，才会生成与测量函数 `h` 对应的端口：

- 您在 **Function** 中使用 MATLAB 函数指定 `h`，并且 `h` 在 MATLAB 路径上。
- `h` 除 `x` 和 `v` 之外仅需要一个附加输入参数。

**数据类型：** `single` | `double`

### **Q** — 时变过程噪声协方差 标量 | 向量 | 矩阵

时变过程噪声协方差，根据 **Process noise** 参数的值指定为标量、向量或矩阵：

- **Process noise** 为 `Additive` — 将协方差指定为标量、*Ns* 元素向量或 *Ns*×*Ns* 矩阵，其中 *Ns* 是系统的状态数。如果过程噪声项之间没有互相关，并且所有项具有相同的方差，则指定标量。如果过程噪声项之间没有互相关，但所有项具有不同的方差，则指定长度为 *Ns* 的向量。
- **Process noise** 为 `Nonadditive` — 将协方差指定为 *W*×*W* 矩阵，其中 *W* 是状态转移函数中过程噪声项的数量。

#### 依赖关系

如果您将过程噪声协方差指定为 **Time-Varying**，则会生成此端口。当您点击 **Apply** 时，该端口会出现。

**数据类型：** `single` | `double`

### **R1,R2,R3,R4,R5** — 时变测量噪声协方差矩阵

系统最多五个测量函数的时变测量噪声协方差，指定为矩阵。矩阵的大小取决于对应测量函数的 **Measurement noise** 参数的值：

- **Measurement noise** 为 `Additive` — 将协方差指定为 *N*×*N* 矩阵，其中 *N* 是系统的测量数。
- **Measurement noise** 为 `Nonadditive` — 将协方差指定为 *V*×*V* 矩阵，其中 *V* 是对应测量函数中测量噪声项的数量。

#### 依赖关系

如果您为对应的测量函数将测量噪声协方差指定为 **Time-Varying**，则会生成一个端口。当您点击 **Apply** 时，该端口会出现。

**数据类型：** `single` | `double`

### **Enable1,Enable2,Enable3,Enable4,Enable5** — 当测量数据可用时启用估计状态的校正 标量

假设在对应于第一个测量函数的端口 **y1** 处，测量输出数据并非在所有时间点都可用。在 **Enable1** 端口使用非 `0` 的信号值，以在测量数据可用时启用估计状态的校正。当测量数据不可用时，将端口值指定为 `0`。类似地，如果在第 *i* 个测量函数的端口 **y*`i`*** 处，测量输出数据并非在所有时间点都可用，则将对应的端口 **Enable*`i`*** 指定为非 `0` 的值。

#### 依赖关系

如果您为某个测量函数选择 **Add Enable port**，则会生成与该测量函数对应的端口。当您点击 **Apply** 时，该端口会出现。

**数据类型：** `single` | `double` | `Boolean`
### 输出

### **xhat** — 估计状态向量

估计状态，以大小为 *Ns* 的向量返回，其中 *Ns* 是系统的状态数。要访问各个状态，请使用 Selector (Simulink) 模块。

当选中 **Use the current measurements to improve state estimates** 参数时，模块在时间步 `k` 输出校正后的状态估计 x^[k|k]，该估计使用截至时间 `k` 的测量输出进行估计。如果您清除此参数，模块返回时间 `k` 的预测状态估计 x^[k|k−1]，该估计使用截至前一时刻 `k-1` 的测量输出进行估计。如果您的滤波器处于反馈环路中，并且您的 Simulink 模型中存在代数环，请清除此参数。

**数据类型：** `single` | `double`

### **P** — 状态估计误差协方差矩阵

状态估计误差协方差，以 *Ns*×*Ns* 矩阵返回，其中 *Ns* 是系统的状态数。要访问各个协方差，请使用 Selector (Simulink) 模块。

#### 依赖关系

如果您在 **System Model** 选项卡中选择 **Output state estimation error covariance**，并点击 **Apply**，则会生成此端口。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Function
  summary: 状态转移函数名称 myStateTransitionFcn（默认）| 函数名称
  group: System Model 选项卡
  block_parameter: StateTransitionFcn
  type: character vector, string
  default: '''myStateTransitionFcn'''
- name: Process noise
  summary: 过程噪声特性 Additive（默认）| Nonadditive
  group: System Model 选项卡
  block_parameter: HasAdditiveProcessNoise
  type: character vector
  values: '''Additive'', ''Nonadditive'''
  default: '''Additive'''
- name: Covariance
  summary: 时不变过程噪声协方差 1（默认）| 标量 | 向量 | 矩阵
  group: System Model 选项卡
  block_parameter: ProcessNoise
  type: character vector, string
  default: '''1'''
- name: Time-varying
  summary: 时变过程噪声协方差 'off'（默认）| 'on'
  group: System Model 选项卡
  block_parameter: HasTimeVaryingProcessNoise
  type: character vector
  values: '''off'', ''on'''
  default: '''off'''
- name: Initial state
  summary: 初始状态估计 0（默认）| 向量
  group: System Model 选项卡
  block_parameter: InitialState
  type: character vector, string
  default: '''0'''
- name: Initial covariance
  summary: 状态估计误差协方差 1（默认）| 标量 | 向量 | 矩阵
  group: System Model 选项卡
  block_parameter: InitialStateCovariance
  type: character vector, string
  default: '''1'''
- name: Alpha
  summary: sigma 点的散布 1e-3（默认）| 0 到 1 之间的标量值
  group: System Model 选项卡
  block_parameter: Alpha
  type: character vector, string
  default: '''1e-3'''
- name: Beta
  summary: 状态分布的表征 2（默认）| 大于或等于 0 的标量值
  group: System Model 选项卡
  block_parameter: Beta
  type: character vector, string
  default: '''2'''
- name: Kappa
  summary: sigma 点的散布 0（默认）| 0 到 3 之间的标量值
  group: System Model 选项卡
  block_parameter: Kappa
  type: character vector, string
  default: '''0'''
- name: Function
  summary: 测量函数名称 myMeasurementFcn（默认）| 函数名称
  group: System Model 选项卡
  block_parameter: MeasurementFcn1, MeasurementFcn2, MeasurementFcn3, MeasurementFcn4, MeasurementFcn5
  type: character vector, string
  default: '''myMeasurementFcn'''
- name: Measurement noise
  summary: 测量噪声特性 Additive（默认）| Nonadditive
  group: System Model 选项卡
  block_parameter: HasAdditiveMeasurementNoise1, HasAdditiveMeasurementNoise2, HasAdditiveMeasurementNoise3, HasAdditiveMeasurementNoise4,
    HasAdditiveMeasurementNoise5
  type: character vector
  values: '''Additive'', ''Nonadditive'''
  default: '''Additive'''
- name: Enable measurement wrapping
  summary: 启用测量环绕 off（默认）| on
  group: System Model 选项卡
  block_parameter: EnableMeasurementWrapping1, EnableMeasurementWrapping2, EnableMeasurementWrapping3, EnableMeasurementWrapping4,
    EnableMeasurementWrapping5
  type: character vector
  values: '''off'', ''on'''
  default: '''off'''
- name: Covariance
  summary: 时不变测量噪声协方差 1（默认）| 矩阵
  group: System Model 选项卡
  block_parameter: MeasurementNoise1, MeasurementNoise2, MeasurementNoise3, MeasurementNoise4, MeasurementNoise5
  type: character vector, string
  default: '''1'''
- name: Time-varying
  summary: 时变测量噪声协方差 off（默认）| on
  group: System Model 选项卡
  block_parameter: HasTimeVaryingMeasurementNoise1, HasTimeVaryingMeasurementNoise2, HasTimeVaryingMeasurementNoise3, HasTimeVaryingMeasurementNoise4,
    HasTimeVaryingMeasurementNoise5
  type: character vector
  values: '''off'', ''on'''
  default: '''off'''
- name: Add Enable Port
  summary: 仅在测量数据可用时启用估计状态的校正 off（默认）| on
  group: System Model 选项卡
  block_parameter: HasMeasurementEnablePort1, HasMeasurementEnablePort2, HasMeasurementEnablePort3, HasMeasurementEnablePort4,
    HasMeasurementEnablePort5
  type: character vector
  values: '''off'', ''on'''
  default: '''off'''
- name: Use the current measurements to improve state estimates
  summary: 在校正或预测状态估计之间选择 on（默认）| off
  group: System Model 选项卡
  block_parameter: UseCurrentEstimator
  type: character vector
  values: '''off'', ''on'''
  default: '''on'''
- name: Output state estimation error covariance
  summary: 输出状态估计误差协方差 off（默认）| on
  group: System Model 选项卡
  block_parameter: OutputStateCovariance
  type: character vector
  values: '''off'',''on'''
  default: '''off'''
- name: Data type
  summary: 模块参数的数据类型 double（默认）| single
  group: System Model 选项卡
  block_parameter: DataType
  type: character vector
  values: '''single'', ''double'''
  default: '''double'''
- name: Sample time
  summary: 模块采样时间 1（默认）| 正标量
  group: System Model 选项卡
  block_parameter: SampleTime
  type: character vector, string
  default: '''1'''
- name: Enable multirate operation
  summary: 启用为状态转移函数和测量函数指定不同的采样时间 off（默认）| on
  group: Multirate Tab
  block_parameter: EnableMultirate
  type: character vector
  values: '''off'', ''on'''
  default: '''off'''
- name: Sample times
  summary: 状态转移函数和测量函数采样时间 正标量
  group: Multirate Tab
  block_parameter: StateTransitionFcnSampleTime, MeasurementFcn1SampleTime1, MeasurementFcn1SampleTime2, MeasurementFcn1SampleTime3,
    MeasurementFcn1SampleTime4, MeasurementFcn1SampleTime5
  type: 字符向量、字符串
  default: '''1'''
```

### System Model 选项卡

#### State Transition

### **Function** — 状态转移函数名称 `myStateTransitionFcn`（默认）| 函数名称

状态转移函数计算系统在时间步 *k*+1 的 *Ns* 元素状态向量，给定时间步 *k* 的状态向量。*Ns* 是非线性系统的状态数。您创建状态转移函数并在 **Function** 中指定函数名称。例如，如果 `vdpStateFcn.m` 是您创建并保存的状态转移函数，则将 **Function** 指定为 `vdpStateFcn`。

您创建的函数输入取决于您在 **Process noise** 中将过程噪声指定为加性还是非加性。

- **Process noise** 为 `Additive` — 状态转移函数 *f* 指定状态如何作为前一时间步状态值的函数演化：

  `x(k+1) = f(x(k),Us1(k),...,Usn(k))`，

  其中 `x(k)` 是时间 `k` 的估计状态，`Us1,...,Usn` 是您的状态转移函数所需的任何附加输入参数，例如系统输入或采样时间。要查看具有加性过程噪声的状态转移函数示例，请在命令行键入 `edit vdpStateFcn`。
- **Process noise** 为 `Nonadditive` — 状态转移函数还指定状态如何作为过程噪声 `w` 的函数演化：

  `x(k+1) =
  f(x(k),w(k),Us1(k),...,Usn(k))`。

有关详细信息，请参阅 State Transition and Measurement Functions。

您可以使用 Simulink Function (Simulink) 模块或 MATLAB 函数（`.m` 文件）创建 *f*。

- 仅当 *f* 除 `x` 和 `w` 之外有一个附加输入参数 `Us1` 时，您才可以使用 MATLAB 函数。

  `x(k+1) = f(x(k),w(k),Us1(k))`

  软件会生成一个附加输入端口 **StateTransitionFcnInputs** 来指定此参数。
- 如果您使用 Simulink Function 模块，请在 Simulink Function 模块中使用 Argument Inport (Simulink) 模块指定 `x` 和 `w`，并使用 Inport (Simulink) 模块指定附加输入 `Us1,...,Usn`。Simulink Function 模块中 Argument Inport (Simulink) 和 Argument Outport (Simulink) 模块的 **Argument name** 参数必须彼此不同。您不向 Unscented Kalman Filter 模块提供 `Us1,...,Usn`。有关示例，请参阅 Online State Estimation Using Identified Nonlinear Models (System Identification Toolbox)。

#### 编程使用

|  |
| --- |
| **模块参数**：`StateTransitionFcn` |
| **类型**：character vector, string |
| **默认值**：`'myStateTransitionFcn'` |

### **Process noise** — 过程噪声特性 `Additive`（默认）| `Nonadditive`

过程噪声特性，指定为以下值之一：

- `Additive` — 过程噪声 `w` 是加性的，您在 **Function** 中指定的状态转移函数 *f* 具有以下形式：

  `x(k+1) = f(x(k),Us1(k),...,Usn(k))`，

  其中 `x(k)` 是时间 `k` 的估计状态，`Us1,...,Usn` 是您的状态转移函数所需的任何附加输入参数。
- `Nonadditive` — 过程噪声是非加性的，状态转移函数指定状态如何作为前一时间步的状态*和*过程噪声的函数演化：

  `x(k+1) = f(x(k),w(k),Us1(k),...,Usn(k))`。

#### 编程使用

|  |
| --- |
| **模块参数**：`HasAdditiveProcessNoise` |
| **类型**：character vector |
| **值**：`'Additive'`, `'Nonadditive'` |
| **默认值**：`'Additive'` |

### **Covariance** — 时不变过程噪声协方差 `1`（默认）| 标量 | 向量 | 矩阵

时不变过程噪声协方差，根据 **Process noise** 参数的值指定为标量、向量或矩阵：

- **Process noise** 为 `Additive` — 将协方差指定为标量、*Ns* 元素向量或 *Ns*×*Ns* 矩阵，其中 *Ns* 是系统的状态数。如果过程噪声项之间没有互相关，并且所有项具有相同的方差，则指定标量。如果过程噪声项之间没有互相关，但所有项具有不同的方差，则指定长度为 *Ns* 的向量。
- **Process noise** 为 `Nonadditive` — 将协方差指定为 *W*×*W* 矩阵，其中 *W* 是过程噪声项的数量。

如果过程噪声协方差是时变的，请选择 **Time-varying**。模块会生成输入端口 **Q** 来指定时变协方差。

#### 依赖关系

如果您未将过程噪声指定为 **Time-Varying**，则此参数启用。

#### 编程使用

|  |
| --- |
| **模块参数**：`ProcessNoise` |
| **类型**：character vector, string |
| **默认值**：`'1'` |

### **Time-varying** — 时变过程噪声协方差 `'off'`（默认）| `'on'`

如果您选择此参数，模块会包含一个附加输入端口 **Q** 来指定时变过程噪声协方差。

#### 编程使用

|  |
| --- |
| **模块参数**：`HasTimeVaryingProcessNoise` |
| **类型**：character vector |
| **值**：`'off'`, `'on'` |
| **默认值**：`'off'` |

#### Initialization

### **Initial state** — 初始状态估计 `0`（默认）| 向量

初始状态估计值，指定为 *Ns* 元素向量，其中 *Ns* 是系统中的状态数。根据您对系统的了解指定初始状态值。

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialState` |
| **类型**：character vector, string |
| **默认值**：`'0'` |

### **Initial covariance** — 状态估计误差协方差 `1`（默认）| 标量 | 向量 | 矩阵

状态估计误差协方差，指定为标量、*Ns* 元素向量或 *Ns*×*Ns* 矩阵，其中 *Ns* 是系统的状态数。如果您指定标量或向量，软件会创建一个 *Ns*×*Ns* 对角矩阵，标量或向量元素位于对角线上。

当您对在 **Initial state** 中指定的初始状态值没有信心时，请为协方差指定一个较高的值。

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialStateCovariance` |
| **类型**：character vector, string |
| **默认值**：`'1'` |

#### Unscented Transformation Parameters

### **Alpha** — sigma 点的散布 `1e-3`（默认）| 0 到 1 之间的标量值

无迹卡尔曼滤波算法将系统状态视为具有均值状态值和方差的随机变量。为了计算下一时间步的状态及其统计特性，该算法首先使用无迹变换生成一组围绕均值分布的状态值。这些生成的状态值称为 sigma 点。该算法将每个 sigma 点用作状态转移函数和测量函数的输入，以获得一组新的变换状态点和测量值。变换后的点用于计算下一时间步的状态和状态估计误差协方差值。

sigma 点围绕均值状态值的散布由两个参数 **Alpha** 和 **Kappa** 控制。第三个参数 **Beta** 影响状态和测量协方差计算期间变换点的权重：

- **Alpha** — 确定 sigma 点围绕均值状态值的散布。指定为 0 到 1 之间的标量值（`0` < **Alpha** <= `1`）。它通常是一个较小的正值。sigma 点的散布与 **Alpha** 成正比。较小的值对应于更接近均值状态的 sigma 点。
- **Kappa** — 第二个缩放参数，通常设置为 0。较小的值对应于更接近均值状态的 sigma 点。散布与 `Kappa` 的平方根成正比。
- **Beta** — 纳入关于状态分布的先验知识。对于高斯分布，**Beta** = 2 是最优的。

如果您知道状态和状态协方差的分布，可以调整这些参数以捕获分布高阶矩的变换。该算法只能跟踪状态概率分布中的单个峰值。如果您的系统状态分布中存在多个峰值，可以调整这些参数以使 sigma 点保持在单个峰值附近。例如，选择较小的 **Alpha** 以生成接近均值状态值的 sigma 点。

有关更多信息，请参阅 Unscented Kalman Filter Algorithm。

#### 编程使用

|  |
| --- |
| **模块参数**：`Alpha` |
| **类型**：character vector, string |
| **默认值**：`'1e-3'` |

### **Beta** — 状态分布的表征 `2`（默认）| 大于或等于 0 的标量值

用于调整变换 sigma 点权重的状态分布表征，指定为大于或等于 0 的标量值。对于高斯分布，`Beta` = 2 是最优选择。

有关更多信息，请参阅 **Alpha** 的描述。

#### 编程使用

|  |
| --- |
| **模块参数**：`Beta` |
| **类型**：character vector, string |
| **默认值**：`'2'` |

### **Kappa** — sigma 点的散布 `0`（默认）| 0 到 3 之间的标量值

sigma 点围绕均值状态值的散布，指定为 0 到 3 之间的标量值（`0` <= **Kappa** <= `3`）。**Kappa** 通常指定为 `0`。较小的值对应于更接近均值状态的 sigma 点。散布与 **Kappa** 的平方根成正比。有关更多信息，请参阅 **Alpha** 的描述。

#### 编程使用

|  |
| --- |
| **模块参数**：`Kappa` |
| **类型**：character vector, string |
| **默认值**：`'0'` |

#### Measurement

### **Function** — 测量函数名称 `myMeasurementFcn`（默认）| 函数名称

测量函数计算非线性系统在时间步 *k* 的 *N* 元素输出测量向量，给定时间步 *k* 的状态向量。您创建测量函数并在 **Function** 中指定函数名称。例如，如果 `vdpMeasurementFcn.m` 是您创建并保存的测量函数，请将 **Function** 指定为 `vdpMeasurementFcn`。

您创建的函数的输入取决于您在 **Measurement noise** 中将测量噪声指定为加性还是非加性：

- **Measurement noise** 为 `Additive` — 测量函数 *h* 指定测量值如何作为状态值的函数演化：

  `y(k) = h(x(k),Um1(k),...,Umn(k))`，

  其中 `y(k)` 和 `x(k)` 是时间 `k` 的估计输出和估计状态，`Um1,...,Umn` 是测量函数所需的任何可选输入参数。例如，如果您使用传感器跟踪对象，附加输入可以是传感器位置。

  要查看具有加性过程噪声的测量函数示例，请在命令行键入 `edit vdpMeasurementFcn`。
- **Measurement noise** 为 `Nonadditive` — 测量函数还指定输出测量值如何作为测量噪声 `v` 的函数演化：

  `y(k) = h(x(k),v(k),Um1(k),...,Umn(k))`。

  要查看具有非加性过程噪声的测量函数示例，请在命令行键入 `edit vdpMeasurementNonAdditiveNoiseFcn`。

有关更多信息，请参阅 State Transition and Measurement Functions。

您可以使用 Simulink Function (Simulink) 模块或 MATLAB 函数（`.m` 文件）创建 *h*。

- 仅当 *h* 除了 `x` 和 `v` 之外还有一个附加输入参数 `Um1` 时，才能使用 MATLAB 函数。

  `y[k] = h(x[k],v[k],Um1(k))`

  软件生成一个附加输入端口 **MeasurementFcnInput** 来指定此参数。
- 如果您使用 Simulink Function 模块，请在 Simulink Function 模块中使用 Argument Inport (Simulink) 模块指定 `x` 和 `v`，并使用 Inport (Simulink) 模块指定附加输入 `Um1,...,Umn`。Simulink Function 模块中 Argument Inport (Simulink) 和 Argument Outport (Simulink) 模块的 **Argument name** 参数必须彼此不同。您不向 Unscented Kalman Filter 模块提供 `Um1,...,Umn`。有关示例，请参阅 Online State Estimation Using Identified Nonlinear Models (System Identification Toolbox)。

如果您的系统中有多个传感器，可以指定多个测量函数。您可以使用 **Add Measurement** 按钮指定最多五个测量函数。要删除测量函数，请使用 **Remove Measurement**。

#### 编程使用

|  |
| --- |
| **模块参数**：`MeasurementFcn1`, `MeasurementFcn2`, `MeasurementFcn3`, `MeasurementFcn4`, `MeasurementFcn5` |
| **类型**：character vector, string |
| **默认值**：`'myMeasurementFcn'` |

### **Measurement noise** — 测量噪声特性 `Additive`（默认）| `Nonadditive`

测量噪声特性，指定为以下值之一：

- `Additive` — 测量噪声 `v` 是加性的，您在 **Function** 中指定的测量函数 *h* 具有以下形式：

  `y(k) = h(x(k),Um1(k),...,Umn(k))`，

  其中 `y(k)` 和 `x(k)` 是时间 `k` 的估计输出和估计状态，`Um1,...,Umn` 是测量函数所需的任何可选输入参数。
- `Nonadditive` — 测量噪声是非加性的，测量函数指定输出测量值如何作为状态*和*测量噪声的函数演化：

  `y(k) = h(x(k),v(k),Um1(k),...,Umn(k))`。

#### 编程使用

|  |
| --- |
| **模块参数**：`HasAdditiveMeasurementNoise1`, `HasAdditiveMeasurementNoise2`, `HasAdditiveMeasurementNoise3`, `HasAdditiveMeasurementNoise4`, `HasAdditiveMeasurementNoise5` |
| **类型**：character vector |
| **值**：`'Additive'`, `'Nonadditive'` |
| **默认值**：`'Additive'` |

### **Enable measurement wrapping** — 启用测量环绕 `off`（默认）| `on`

当您具有独立于模型状态的圆形测量值时，选择此参数以启用测量环绕来估计状态。如果选择此参数，则您指定的测量函数必须包含以下两个输出：

1. 测量值，指定为非线性系统在时间步 *k* 的 *N* 元素输出测量向量，给定时间步 *k* 的状态向量。*N* 是系统的测量数量。
2. 测量环绕边界，指定为 *N* 乘 `2` 矩阵，其中第一列提供最小测量边界，第二列提供最大测量边界。

启用 **Enable measurement wrapping** 复选框会在定义的边界内环绕测量残差，这有助于防止滤波器因不正确的测量残差值而发散。有关示例，请参阅 State Estimation with Wrapped Measurements Using Extended Kalman Filter。

#### 编程使用

|  |
| --- |
| **模块参数**：`EnableMeasurementWrapping1`, `EnableMeasurementWrapping2`, `EnableMeasurementWrapping3`, `EnableMeasurementWrapping4`, `EnableMeasurementWrapping5` |
| **类型**：character vector |
| **值**：`'off'`, `'on'` |
| **默认值**：`'off'` |

### **Covariance** — 时不变测量噪声协方差 `1`（默认）| 矩阵

时不变测量噪声协方差，指定为矩阵。矩阵的大小取决于 **Measurement noise** 参数的值：

- **Measurement noise** 为 `Additive` — 将协方差指定为 *N* 乘 *N* 矩阵，其中 *N* 是系统的测量数量。
- **Measurement noise** 为 `Nonadditive` — 将协方差指定为 *V* 乘 *V* 矩阵，其中 *V* 是测量噪声项的数量。

如果测量噪声协方差是时变的，请选择 **Time-varying**。该模块生成输入端口 **R*`i`*** 以指定第 *i* 个测量函数的时变协方差。

#### 依赖关系

如果您未将过程噪声指定为 **Time-Varying**，则启用此参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`MeasurementNoise1`, `MeasurementNoise2`, `MeasurementNoise3`, `MeasurementNoise4`, `MeasurementNoise5` |
| **类型**：character vector, string |
| **默认值**：`'1'` |

### **Time-varying** — 时变测量噪声协方差 `off`（默认）| `on`

如果您为第一个测量函数的测量噪声协方差选择此参数，该模块将包含一个附加输入端口 **R1**。您在 **R1** 中指定时变测量噪声协方差。类似地，如果您为第 *i* 个测量函数选择 **Time-varying**，该模块将包含一个附加输入端口 **R*`i`*** 以指定该函数的时变测量噪声协方差。

#### 编程使用

|  |
| --- |
| **模块参数**：`HasTimeVaryingMeasurementNoise1`, `HasTimeVaryingMeasurementNoise2`, `HasTimeVaryingMeasurementNoise3`, `HasTimeVaryingMeasurementNoise4`, `HasTimeVaryingMeasurementNoise5` |
| **类型**：character vector |
| **值**：`'off'`, `'on'` |
| **默认值**：`'off'` |

### **Add Enable Port** — 仅在测量数据可用时启用估计状态的校正 `off`（默认）| `on`

假设对应于第一个测量函数的端口 **y1** 处并非在所有时间点都有测量输出数据。选择 **Add Enable port** 以生成输入端口 **Enable1**。使用此端口处的信号仅在测量数据可用时启用估计状态的校正。类似地，如果第 *i* 个测量函数的端口 **y*`i`*** 处并非在所有时间点都有测量输出数据，请选择相应的 **Add Enable port**。

#### 编程使用

|  |
| --- |
| **模块参数**：`HasMeasurementEnablePort1`, `HasMeasurementEnablePort2`, `HasMeasurementEnablePort3`, `HasMeasurementEnablePort4`, `HasMeasurementEnablePort5` |
| **类型**：character vector |
| **值**：`'off'`, `'on'` |
| **默认值**：`'off'` |

#### Settings

### **Use the current measurements to improve state estimates** — 在校正或预测状态估计之间选择 `on`（默认）| `off`

选择此参数时，该模块在时间步 `k` 输出校正状态估计 x^[k|k]，使用直到时间 `k` 的测量输出进行估计。如果清除此参数，该模块返回时间 `k` 的预测状态估计 x^[k|k−1]，使用直到先前时间 `k-1` 的测量输出进行估计。如果您的滤波器处于反馈环路中且 Simulink 模型中存在代数环，请清除此参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`UseCurrentEstimator` |
| **类型**：character vector |
| **值**：`'off'`, `'on'` |
| **默认值**：`'on'` |

### **Output state estimation error covariance** — 输出状态估计误差协方差 `off`（默认）| `on`

如果选择此参数，该模块中将生成状态估计误差协方差输出端口 **P**。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputStateCovariance` |
| **类型**：character vector |
| **值**：`'off'`,`'on'` |
| **默认值**：`'off'` |

### **Data type** — 模块参数的数据类型 `double`（默认）| `single`

使用此参数指定所有模块参数的数据类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`DataType` |
| **类型**：character vector |
| **值**：`'single'`, `'double'` |
| **默认值**：`'double'` |

### **Sample time** — 模块采样时间 `1`（默认）| 正标量

模块采样时间，指定为正标量。如果状态转移函数和测量函数的采样时间不同，请在 **Multirate** 选项卡中选择 **Enable multirate operation**，并在 **Multirate** 选项卡中指定采样时间。

#### 依赖关系

如果在 **Multirate** 选项卡中 **Enable multirate operation** 参数为 `off`，则此参数可用。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：character vector, string |
| **默认值**：`'1'` |

### Multirate Tab

### **Enable multirate operation** — 启用为状态转移函数和测量函数指定不同的采样时间 `off`（默认）| `on`

如果状态转移函数和测量函数的采样时间不同，请选择此参数。您在 **Multirate** 选项卡的 **Sample time** 中指定采样时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`EnableMultirate` |
| **类型**：character vector |
| **值**：`'off'`, `'on'` |
| **默认值**：`'off'` |

### **Sample times** — 状态转移函数和测量函数采样时间 正标量

如果状态转移函数和测量函数的采样时间不同，请指定 **Sample time**。将测量函数的采样时间指定为状态转移采样时间的正整数倍。您指定的采样时间对应于以下输入端口：

- 对应于状态转移函数的端口 — 状态转移函数的附加输入 **StateTransitionFcnInputs** 和时变过程噪声协方差 **Q**。这些端口的采样时间必须始终等于状态转移函数采样时间，但可以与测量函数的采样时间不同。
- 对应于第 *i* 个测量函数的端口 — 测量输出 **y*`i`***、测量函数的附加输入 **MeasurementFcn*`i`*Inputs**、端口 **Enable*`i`*** 处的使能信号以及时变测量噪声协方差 **R*`i`***。同一测量函数的这些端口的采样时间必须始终相同，但可以与状态转移函数和其他测量函数的采样时间不同。

#### 依赖关系

如果在 **Multirate** 选项卡中 **Enable multirate operation** 参数为 `on`，则此参数可用。

#### 程序化使用

|  |
| --- |
| **模块参数：**`StateTransitionFcnSampleTime`, `MeasurementFcn1SampleTime1`, `MeasurementFcn1SampleTime2`, `MeasurementFcn1SampleTime3`, `MeasurementFcn1SampleTime4`, `MeasurementFcn1SampleTime5` |
| **类型：** 字符向量、字符串 |
| **默认值：** `'1'` |
## 所属库

Control System Toolbox / State Estimation System Identification Toolbox / Estimators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

您指定的状态转移函数和测量函数只能使用支持代码生成的 MATLAB 命令和 Simulink 模块。有关支持代码生成的模块列表，请参阅 Blocks Supported for Code Generation (Simulink Coder)。有关支持代码生成的命令列表，请参阅 Functions and Objects Supported for C/C++ Code Generation (MATLAB Coder)。

生成的代码使用的算法与 Unscented Kalman Filter 模块本身使用的算法不同。使用这两种方法获得的结果可能会出现一些数值差异。

## 版本历史

**在 R2017a 中引入**

### R2020b：数值变化

从 R2020b 开始，Unscented Kalman Filter 算法中的数值改进可能会产生与您在先前版本中获得的结果不同的结果。

## 描述

使用无迹卡尔曼滤波器估计离散时间非线性系统的状态

Unscented Kalman Filter 模块使用离散时间无迹卡尔曼滤波器算法估计离散时间非线性系统的状态。

考虑一个具有状态 *x*、输入 *u*、输出 *y*、过程噪声 *w* 和测量噪声 *v* 的被控对象。假设您可以将该被控对象表示为非线性系统。

使用系统的状态转移函数和测量函数以及无迹卡尔曼滤波器算法，该模块为当前时间步生成状态估计 x^。有关该算法的信息，请参阅 Extended and Unscented Kalman Filter Algorithms for Online State Estimation。

您为系统创建非线性状态转移函数和测量函数，并在模块中指定这些函数。该模块支持对具有多个以不同采样率运行的传感器的系统进行状态估计。您最多可以指定五个测量函数，每个函数对应系统中的一个传感器。有关详细信息，请参阅 State Transition and Measurement Functions。
