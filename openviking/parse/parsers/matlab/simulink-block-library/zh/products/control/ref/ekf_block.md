---
type: simulink-block
title: 'Extended Kalman Filter'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Control System Design and Tuning / State-Space Control Design and Estimation / State Estimation'
documentation_page: 'ekf_block'
documentation_source_path: 'ref/ekf_block.html'
language: zh-CN
chinese_source: worker-translation
---

# Extended Kalman Filter

## 端口

### 输入

### **y1,y2,y3,y4,y5** — 测量系统输出向量

与您在模块中指定的每个测量函数对应的测量系统输出。端口数等于系统中的测量函数数。您最多可以指定五个测量函数。例如，如果您的系统有两个传感器，则在模块中指定两个测量函数。第一个端口 **y1** 默认可用。当您点击 **Apply** 时，软件会生成对应于第二个测量函数的端口 **y2**。

将这些端口指定为 *N* 维向量，其中 *N* 是对应传感器测量的量数。例如，如果您的系统有一个传感器测量对象的位置和速度，则只有一个端口 **y1**。该端口指定为 2 维向量，其值对应于位置和速度。

#### 依赖项

第一个端口 **y1** 默认可用。当您点击 **Add Measurement**，然后点击 **Apply** 时，会生成端口 **y2** 到 **y5**。

**数据类型：** `single` | `double`

### **StateTransitionFcnInputs** — 状态转移函数的附加可选输入参数 标量 | 向量 | 矩阵

状态转移函数 `f` 的附加可选输入参数，不同于状态 `x` 和过程噪声 `w`。有关状态转移函数的信息，请参阅 State Transition and Measurement Functions。

假设您的系统具有非加性过程噪声，并且状态转移函数 `f` 具有以下形式：

`x(k+1) = f(x(k),w(k),StateTransitionFcnInputs)`

这里 `k` 是时间步，`StateTransitionFcnInputs` 是不同于 `x` 和 `w` 的附加输入参数。

如果您使用 MATLAB® 函数（`.m` 文件）创建 `f`，则当您点击 **Apply** 时，软件会生成端口 **StateTransitionFcnInputs**。您可以将该端口的输入指定为标量、向量或矩阵。

如果您的状态转移函数有多个附加输入，请使用 Simulink Function (Simulink) 模块来指定该函数。当您使用 Simulink Function 模块时，您使用 Inport (Simulink) 模块将附加输入直接提供给 Simulink Function 模块。在 Extended Kalman Filter 模块中不会为这些附加输入生成输入端口。有关示例，请参阅 Online State Estimation Using Identified Nonlinear Models (System Identification Toolbox)。

#### 依赖项

仅当以下两个条件均满足时，才会生成此端口：

- 您在 **Function** 中使用 MATLAB 函数指定 `f`，并且 `f` 位于 MATLAB 路径上。
- `f` 除了 `x` 和 `w` 之外只需要一个附加输入参数。

**数据类型：** `single` | `double`

### **MeasurementFcn1Inputs,MeasurementFcn2Inputs,MeasurementFcn3Inputs,MeasurementFcn4Inputs,MeasurementFcn5Inputs** — 每个测量函数的附加可选输入参数 标量 | 向量 | 矩阵

测量函数的附加可选输入，不同于状态 `x` 和测量噪声 `v`。有关测量函数的信息，请参阅 State Transition and Measurement Functions。

**MeasurementFcn1Inputs** 对应于您指定的第一个测量函数，依此类推。例如，假设您的系统有三个传感器和非加性测量噪声，并且三个测量函数 `h1`、`h2` 和 `h3` 具有以下形式：

`y1[k] = h1(x[k],v1[k],MeasurementFcn1Inputs)`

`y2[k] = h2(x[k],v2[k],MeasurementFcn2Inputs)`

`y3[k] = h3(x[k],v3[k])`

这里 `k` 是时间步，`MeasurementFcn1Inputs` 和 `MeasurementFcn2Inputs` 是 `h1` 和 `h2` 的附加输入参数。

如果您在 **Function** 中使用 MATLAB 函数（`.m` 文件）指定 `h1`、`h2` 和 `h3`，则当您点击 **Apply** 时，软件会生成端口 **MeasurementFcn1Inputs** 和 **MeasurementFcn2Inputs**。您可以将这些端口的输入指定为标量、向量或矩阵。

如果您的测量函数有多个附加输入，请使用 Simulink Function (Simulink) 模块来指定这些函数。当您使用 Simulink Function 模块时，您使用 Inport (Simulink) 模块将附加输入直接提供给 Simulink Function 模块。在 Extended Kalman Filter 模块中不会为这些附加输入生成输入端口。有关示例，请参阅 Online State Estimation Using Identified Nonlinear Models (System Identification Toolbox)。

#### 依赖项

仅当以下两个条件均满足时，才会生成对应于测量函数 `h` 的端口：

- 您在 **Function** 中使用 MATLAB 函数指定 `h`，并且 `h` 位于 MATLAB 路径上。
- `h` 除了 `x` 和 `v` 之外只需要一个附加输入参数。

**数据类型：** `single` | `double`

### **Q** — 时变过程噪声协方差 标量 | 向量 | 矩阵

时变过程噪声协方差，根据 **Process noise** 参数的值指定为标量、向量或矩阵：

- **Process noise** 为 `Additive` — 将协方差指定为标量、*Ns* 元素向量或 *Ns*×*Ns* 矩阵，其中 *Ns* 是系统的状态数。如果过程噪声项之间没有互相关，并且所有项具有相同方差，则指定标量。如果过程噪声项之间没有互相关，但所有项具有不同方差，则指定长度为 *Ns* 的向量。
- **Process noise** 为 `Nonadditive` — 将协方差指定为 *W*×*W* 矩阵，其中 *W* 是状态转移函数中的过程噪声项数。

#### 依赖项

如果您将过程噪声协方差指定为 **Time-Varying**，则会生成此端口。该端口在您点击 **Apply** 时出现。

**数据类型：** `single` | `double`

### **R1,R2,R3,R4,R5** — 时变测量噪声协方差矩阵

系统最多五个测量函数的时变测量噪声协方差，指定为矩阵。矩阵的大小取决于对应测量函数的 **Measurement noise** 参数的值：

- **Measurement noise** 为 `Additive` — 将协方差指定为 *N*×*N* 矩阵，其中 *N* 是系统的测量数。
- **Measurement noise** 为 `Nonadditive` — 将协方差指定为 *V*×*V* 矩阵，其中 *V* 是对应测量函数中的测量噪声项数。

#### 依赖项

如果您为对应测量函数将测量噪声协方差指定为 **Time-Varying**，则会生成一个端口。该端口在您点击 **Apply** 时出现。

**数据类型：** `single` | `double`

### **Enable1,Enable2,Enable3,Enable4,Enable5** — 当测量数据可用时启用估计状态校正 标量

假设在对应于第一个测量函数的端口 **y1** 处并非所有时间点都有测量输出数据。在 **Enable1** 端口使用非 `0` 的信号值，以在测量数据可用时启用估计状态校正。当测量数据不可用时，将该端口值指定为 `0`。类似地，如果对于第 *i* 个测量函数，在端口 **y*`i`*** 处并非所有时间点都有测量输出数据，则将对应端口 **Enable*`i`*** 指定为非 `0` 的值。

#### 依赖项

如果您为某个测量函数选择 **Add Enable port**，则会生成对应于该测量函数的端口。该端口在您点击 **Apply** 时出现。

**数据类型：** `single` | `double` | `Boolean`

### 输出

### **xhat** — 估计状态向量

估计状态，以大小为 *Ns* 的向量返回，其中 *Ns* 是系统的状态数。要访问各个状态，请使用 Selector (Simulink) 模块。

当选中 **Use the current measurements to improve state estimates** 参数时，模块在时间步 `k` 输出校正后的状态估计 x^[k|k]，该估计使用截至时间 `k` 的测量输出进行估计。如果清除此参数，则模块返回时间 `k` 的预测状态估计 x^[k|k−1]，该估计使用截至前一时刻 `k-1` 的测量输出进行估计。如果您的滤波器位于反馈回路中并且 Simulink 模型存在代数环，请清除此参数。

**数据类型：** `single` | `double`

### **P** — 状态估计误差协方差矩阵

状态估计误差协方差，以 *Ns*×*Ns* 矩阵返回，其中 *Ns* 是系统的状态数。要访问各个协方差，请使用 Selector (Simulink) 模块。

#### 依赖项

如果您在 **System Model** 选项卡中选择 **Output state estimation error covariance**，然后点击 **Apply**，则会生成此端口。

**数据类型：** `single` | `double`

## 参数

### 系统模型选项卡

#### 状态转移

### **Function** — 状态转移函数名称 `myStateTransitionFcn`（默认）| 函数名称

状态转移函数根据时间步 *k* 的状态向量计算系统在时间步 *k*+1 的 *Ns* 元素状态向量。*Ns* 是非线性系统的状态数。您创建状态转移函数，并在 **Function** 中指定函数名称。例如，如果 `vdpStateFcn.m` 是您创建并保存的状态转移函数，则将 **Function** 指定为 `vdpStateFcn`。

您创建函数的输入取决于您在 **Process noise** 中将过程噪声指定为加性还是非加性。

- **Process noise** 为 `Additive` — 状态转移函数 *f* 指定状态如何作为前一时间步状态值的函数演化：

  `x(k+1) = f(x(k),Us1(k),...,Usn(k))`，

  其中 `x(k)` 是时间 `k` 的估计状态，`Us1,...,Usn` 是您的状态转移函数所需的任何附加输入参数，例如系统输入或采样时间。要查看具有加性过程噪声的状态转移函数示例，请在命令行键入 `edit vdpStateFcn`。

- **Process noise** 为 `Nonadditive` — 状态转移函数还指定状态如何作为过程噪声 `w` 的函数演化：

  `x(k+1) = f(x(k),w(k),Us1(k),...,Usn(k))`。

有关详细信息，请参阅 State Transition and Measurement Functions。

您可以使用 Simulink Function (Simulink) 模块或 MATLAB 函数（`.m` 文件）创建 *f*。

- 仅当 *f* 除了 `x` 和 `w` 之外有一个附加输入参数 `Us1` 时，您才能使用 MATLAB 函数。

  `x(k+1) = f(x(k),w(k),Us1(k))`

  软件会生成附加输入端口 **StateTransitionFcnInputs** 来指定此参数。

- 如果您使用 Simulink Function 模块，请在 Simulink Function 模块中使用 Argument Inport (Simulink) 模块指定 `x` 和 `w`，并使用 Inport (Simulink) 模块指定附加输入 `Us1,...,Usn`。Simulink Function 模块中 Argument Inport (Simulink) 和 Argument Outport (Simulink) 模块的 **Argument name** 参数必须彼此不同。您不向 Extended Kalman Filter 模块提供 `Us1,...,Usn`。有关示例，请参阅 Online State Estimation Using Identified Nonlinear Models (System Identification Toolbox)。

#### 编程使用

|  |
| --- |
| **模块参数：**`StateTransitionFcn` |
| **类型：**字符向量、字符串 |
| **默认值：**`'myStateTransitionFcn'` |

### **Jacobian** — 状态转移函数的 Jacobian `off`（默认）| `on`

状态转移函数 *f* 的 Jacobian，指定为以下之一：

- `off` — 软件以数值方式计算 Jacobian。此计算可能会增加处理时间以及状态估计的数值不准确性。
- `on` — 您创建一个函数来计算 Jacobian，并在 **Jacobian** 中指定函数名称。例如，如果 `vdpStateJacobianFcn.m` 是 Jacobian 函数，则将 **Jacobian** 指定为 `vdpStateJacobianFcn`。如果您使用 Simulink Function (Simulink) 模块创建状态转移函数 *f*，则使用 Simulink Function 模块创建 Jacobian。如果您使用 MATLAB 函数（`.m` 文件）创建 *f*，则使用 MATLAB 函数创建 Jacobian。

  该函数计算状态转移函数相对于状态和过程噪声的偏导数。Jacobian 函数的输入数必须等于状态转移函数的输入数，并且在两个函数中必须按相同顺序指定。Jacobian 函数的输出数取决于 **Process noise** 参数：

  - **Process noise** 为 `Additive` — 该函数计算状态转移函数 *f* 相对于状态的偏导数（∂f/∂x）。输出是 *Ns*×*Ns* Jacobian 矩阵，其中 *Ns* 是状态数。

    要查看加性过程噪声的 Jacobian 函数示例，请在命令行键入 `edit vdpStateJacobianFcn`。

  - **Process noise** 为 `Nonadditive` — 该函数还必须返回第二个输出，即状态转移函数 *f* 相对于过程噪声项的偏导数（∂f/∂w）。第二个输出以 *Ns*×*W* 矩阵返回，其中 *W* 是状态转移函数中的过程噪声项数。

#### 编程使用

|  |
| --- |
| **模块参数：**`HasStateTransitionJacobianFcn` |
| **类型：**字符向量 |
| **值：**`'off'`,`'on'` |
| **默认值：**`'off'` |

|  |
| --- |
| **模块参数：**`StateTransitionJacobianFcn` |
| **类型：**字符向量、字符串 |
| **默认值：**`''` |

### **Process noise** — 过程噪声特性 `Additive`（默认）| `Nonadditive`

过程噪声特性，指定为以下值之一：

- `Additive` — 过程噪声 `w` 是加性的，并且您在 **Function** 中指定的状态转移函数 *f* 具有以下形式：

  `x(k+1) = f(x(k),Us1(k),...,Usn(k))`，

  其中 `x(k)` 是时间 `k` 的估计状态，`Us1,...,Usn` 是您的状态转移函数所需的任何附加输入参数。

- `Nonadditive` — 过程噪声是非加性的，并且状态转移函数指定状态如何作为前一时间步的状态 *和* 过程噪声的函数演化：

  `x(k+1) = f(x(k),w(k),Us1(k),...,Usn(k))`。

#### 编程使用

|  |
| --- |
| **模块参数：** `HasAdditiveProcessNoise` |
| **类型：** 字符向量 |
| **值：** `'Additive'`, `'Nonadditive'` |
| **默认值：** `'Additive'` |

### **Covariance** — 时不变过程噪声协方差 `1`（默认）| 标量 | 向量 | 矩阵

时不变过程噪声协方差，根据 **Process noise** 参数的值指定为标量、向量或矩阵：

- **Process noise** 为 `Additive` — 将协方差指定为标量、*Ns* 元素向量或 *Ns*×*Ns* 矩阵，其中 *Ns* 是系统的状态数。如果过程噪声项之间没有互相关并且所有项具有相同方差，则指定标量。如果过程噪声项之间没有互相关但所有项具有不同方差，则指定长度为 *Ns* 的向量。
- **Process noise** 为 `Nonadditive` — 将协方差指定为 *W*×*W* 矩阵，其中 *W* 是过程噪声项数。

如果过程噪声协方差是时变的，请选择 **Time-varying**。模块会生成输入端口 **Q** 以指定时变协方差。

#### 依赖项

如果您未将过程噪声指定为 **Time-Varying**，则启用此参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `ProcessNoise` |
| **类型：** 字符向量、字符串 |
| **默认值：** `'1'` |

### **Time-varying** — 时变过程噪声协方差 `'off'`（默认）| `'on'`

如果选中此参数，则模块包含一个附加输入端口 **Q**，用于指定时变过程噪声协方差。

#### 编程使用

|  |
| --- |
| **模块参数：** `HasTimeVaryingProcessNoise` |
| **类型：** 字符向量 |
| **值：** `'off'`, `'on'` |
| **默认值：** `'off'` |

#### 初始化

### **Initial state** — 初始状态估计 `0`（默认）| 向量

初始状态估计值，指定为 *Ns* 元素向量，其中 *Ns* 是系统中的状态数。根据您对系统的了解指定初始状态值。

#### 编程使用

|  |
| --- |
| **模块参数：** `InitialState` |
| **类型：** 字符向量、字符串 |
| **默认值：** `'0'` |

### **Initial covariance** — 状态估计误差协方差 `1`（默认）| 标量 | 向量 | 矩阵

状态估计误差协方差，指定为标量、*Ns* 元素向量或 *Ns*×*Ns* 矩阵，其中 *Ns* 是系统的状态数。如果您指定标量或向量，软件会创建一个 *Ns*×*Ns* 对角矩阵，其对角线上为标量或向量元素。

当您对在 **Initial state** 中指定的初始状态值没有信心时，请为协方差指定较高的值。

#### 编程使用

|  |
| --- |
| **模块参数：** `InitialStateCovariance` |
| **类型：** 字符向量、字符串 |
| **默认值：** `'1'` |

#### 测量

### **Function** — 测量函数名称 `myMeasurementFcn`（默认）| 函数名称

测量函数根据时间步 *k* 的状态向量计算非线性系统在时间步 *k* 的 *N* 元素输出测量向量。您创建测量函数，并在 **Function** 中指定函数名称。例如，如果 `vdpMeasurementFcn.m` 是您创建并保存的测量函数，则将 **Function** 指定为 `vdpMeasurementFcn`。

您创建函数的输入取决于您在 **Measurement noise** 中将测量噪声指定为加性还是非加性。

- **Measurement noise** 为 `Additive` — 测量函数 *h* 指定测量值如何作为状态值的函数演化：

  `y(k) = h(x(k),Um1(k),...,Umn(k))`，

  其中 `y(k)` 和 `x(k)` 是时间 `k` 的估计输出和估计状态，`Um1,...,Umn` 是您的测量函数所需的任何可选输入参数。例如，如果您使用传感器跟踪对象，则附加输入可以是传感器位置。

  要查看具有加性过程噪声的测量函数示例，请在命令行键入 `edit vdpMeasurementFcn`。

- **Measurement noise** 为 `Nonadditive`— 测量函数还指定输出测量值如何作为测量噪声 `v` 的函数演化：

  `y(k) = h(x(k),v(k),Um1(k),...,Umn(k))`。

  要查看具有非加性过程噪声的测量函数示例，请在命令行键入 `edit vdpMeasurementNonAdditiveNoiseFcn`。

有关详细信息，请参阅 State Transition and Measurement Functions。

您可以使用 Simulink Function (Simulink) 模块或 MATLAB 函数（`.m` 文件）创建 *h*。

- 仅当 *h* 除了 `x` 和 `v` 之外有一个附加输入参数 `Um1` 时，您才能使用 MATLAB 函数。

  `y[k] = h(x[k],v[k],Um1(k))`

  软件会生成附加输入端口 **MeasurementFcn*`i`*Inputs**，用于为第 *i* 个测量函数指定此参数。

- 如果您使用 Simulink Function 模块，请在 Simulink Function 模块中使用 Argument Inport (Simulink) 模块指定 `x` 和 `v`，并使用 Inport (Simulink) 模块指定附加输入 `Um1,...,Umn`。Simulink Function 模块中 Argument Inport (Simulink) 和 Argument Outport (Simulink) 模块的 **Argument name** 参数必须彼此不同。您不向 Extended Kalman Filter 模块提供 `Um1,...,Umn`。有关示例，请参阅 Online State Estimation Using Identified Nonlinear Models (System Identification Toolbox)。

如果您的系统中有多个传感器，则可以指定多个测量函数。您可以使用 **Add Measurement** 按钮最多指定五个测量函数。要删除测量函数，请使用 **Remove Measurement**。

#### 编程使用

|  |
| --- |
| **模块参数：**`MeasurementFcn1`, `MeasurementFcn2`, `MeasurementFcn3`, `MeasurementFcn4`, `MeasurementFcn5` |
| **类型：** 字符向量、字符串 |
| **默认值：**`'myMeasurementFcn'` |

### **Jacobian** — 测量函数的 Jacobian `off`（默认）| `on`

测量函数 *h* 的 Jacobian，指定为以下之一：

- `off` — 软件以数值方式计算 Jacobian。此计算可能会增加处理时间以及状态估计的数值不准确性。
- `on` — 您创建一个函数来计算测量函数 *h* 的 Jacobian，并在 **Jacobian** 中指定函数名称。例如，如果 `vdpMeasurementJacobianFcn.m` 是 Jacobian 函数，则将 `MeasurementJacobianFcn` 指定为 `vdpMeasurementJacobianFcn`。如果您使用 Simulink Function (Simulink) 模块创建 *h*，则使用 Simulink Function 模块创建 Jacobian。如果您使用 MATLAB 函数（`.m` 文件）创建 *h*，则使用 MATLAB 函数创建 Jacobian。

  该函数计算测量函数 *h* 相对于状态和测量噪声的偏导数。Jacobian 函数的输入数必须等于测量函数的输入数，并且在两个函数中必须按相同顺序指定。Jacobian 函数的输出数取决于 **Measurement noise** 参数：

  - **Measurement noise** 为 `Additive` — 该函数计算测量函数相对于状态的偏导数（∂h/∂x）。输出为 *N*×*Ns* Jacobian 矩阵，其中 *N* 是系统的测量数，*Ns* 是状态数。

    要查看加性测量噪声的 Jacobian 函数示例，请在命令行键入 `edit vdpMeasurementJacobianFcn`。

  - **Measurement noise** 为 `Nonadditive` — 该函数还返回第二个输出，即测量函数相对于测量噪声项的偏导数（∂h/∂v）。第二个输出以 *N*×*V* Jacobian 矩阵返回，其中 *V* 是测量噪声项数。

#### 编程使用

|  |
| --- |
| **模块参数：**`HasMeasurementJacobianFcn1`, `HasMeasurementJacobianFcn2`, `HasMeasurementJacobianFcn3`, `HasMeasurementJacobianFcn4`,`HasMeasurementJacobianFcn5` |
| **类型：** 字符向量 |
| **值：**`'off'`,`'on'` |
| **默认值：**`'off'` |

|  |
| --- |
| **模块参数：**`MeasurementJacobianFcn1`, `MeasurementJacobianFcn2`, `MeasurementJacobianFcn3`, `MeasurementJacobianFcn4`, `MeasurementJacobianFcn5` |
| **类型：** 字符向量 |
| **默认值：**`''` |

### **Measurement noise** — 测量噪声特性 `Additive`（默认）| `Nonadditive`

测量噪声特性，指定为以下值之一：

- `Additive` — 测量噪声 `v` 是加性的，并且您在 **Function** 中指定的测量函数 *h* 具有以下形式：

  `y(k) = h(x(k),Um1(k),...,Umn(k))`，

  其中 `y(k)` 和 `x(k)` 是时间 `k` 的估计输出和估计状态，`Um1,...,Umn` 是您的测量函数所需的任何可选输入参数。

- `Nonadditive` — 测量噪声是非加性的，并且测量函数指定输出测量值如何作为状态 *和* 测量噪声的函数演化：

  `y(k) = h(x(k),v(k),Um1(k),...,Umn(k))`。

#### 编程使用

|  |
| --- |
| **模块参数：** `HasAdditiveMeasurementNoise1`, `HasAdditiveMeasurementNoise2`, `HasAdditiveMeasurementNoise3`, `HasAdditiveMeasurementNoise4`, `HasAdditiveMeasurementNoise5` |
| **类型：** 字符向量 |
| **值：** `'Additive'`, `'Nonadditive'` |
| **默认值：** `'Additive'` |

### **Enable measurement wrapping** — 启用测量环绕 `off`（默认）| `on`

当您具有独立于模型状态的循环测量值时，选中此参数以启用测量环绕来估计状态。如果选中此参数，则您指定的测量函数必须包含以下两个输出：

1. 测量值，指定为非线性系统在时间步 *k* 的 *N* 元素输出测量向量，给定时间步 *k* 的状态向量。*N* 是系统的测量数。
2. 测量环绕边界，指定为 *N*×`2` 矩阵，其中第一列提供最小测量边界，第二列提供最大测量边界。

选中 **Enable measurement wrapping** 复选框会将测量残差环绕在定义的边界内，这有助于防止滤波器因测量残差值不正确而发散。有关示例，请参阅 State Estimation with Wrapped Measurements Using Extended Kalman Filter。

#### 编程使用

|  |
| --- |
| **模块参数：**`EnableMeasurementWrapping1`, `EnableMeasurementWrapping2`, `EnableMeasurementWrapping3`, `EnableMeasurementWrapping4`, `EnableMeasurementWrapping5` |
| **类型：** 字符向量 |
| **值：** `'off'`, `'on'` |
| **默认值：** `'off'` |

### **Covariance** — 时不变过程噪声协方差 `1`（默认）| 标量 | 向量 | 矩阵

时不变过程噪声协方差，根据 **Process noise** 参数的值指定为标量、向量或矩阵：

- **Process noise** 为 `Additive` — 将协方差指定为标量、*Ns* 元素向量或 *Ns*×*Ns* 矩阵，其中 *Ns* 是系统的状态数。如果过程噪声项之间没有互相关并且所有项具有相同方差，则指定标量。如果过程噪声项之间没有互相关但所有项具有不同方差，则指定长度为 *Ns* 的向量。
- **Process noise** 为 `Nonadditive` — 将协方差指定为 *W*×*W* 矩阵，其中 *W* 是过程噪声项数。

如果过程噪声协方差是时变的，请选择 **Time-varying**。模块会生成输入端口 **Q** 以指定时变协方差。

#### 依赖项

如果您未将过程噪声指定为 **Time-Varying**，则启用此参数。

#### 编程使用

|  |
| --- |
| **模块参数：**`ProcessNoise` |
| **类型：** 字符向量、字符串 |
| **默认值：**`'1'` |

### **Time-varying** — 时变测量噪声协方差 `off`（默认）| `on`

如果您为第一个测量函数的测量噪声协方差选中此参数，则模块包含一个附加输入端口 **R1**。您在 **R1** 中指定时变测量噪声协方差。类似地，如果您为第 *i* 个测量函数选择 **Time-varying**，则模块包含一个附加输入端口 **R*`i`***，用于指定该函数的时变测量噪声协方差。

#### 编程使用

|  |
| --- |
| **模块参数：**`HasTimeVaryingMeasurementNoise1`, `HasTimeVaryingMeasurementNoise2`, `HasTimeVaryingMeasurementNoise3`, `HasTimeVaryingMeasurementNoise4`, `HasTimeVaryingMeasurementNoise5` |
| **类型：** 字符向量 |
| **值：**`'off'`, `'on'` |
| **默认值：**`'off'` |

### **Add Enable Port** — 仅当测量数据可用时启用估计状态校正 `off`（默认）| `on`

假设在对应于第一个测量函数的端口 **y1** 处并非所有时间点都有测量输出数据。选择 **Add Enable port** 以生成输入端口 **Enable1**。使用此端口处的信号以仅当测量数据可用时启用估计状态校正。类似地，如果对于第 *i* 个测量函数，在端口 **y*`i`*** 处并非所有时间点都有测量输出数据，则选择对应的 **Add Enable port**。

#### 编程使用

|  |
| --- |
| **模块参数：** `HasMeasurementEnablePort1`, `HasMeasurementEnablePort2`, `HasMeasurementEnablePort3`, `HasMeasurementEnablePort4`, `HasMeasurementEnablePort5` |
| **类型：** 字符向量 |
| **值：** `'off'`, `'on'` |
| **默认值：** `'off'` |

#### 设置

### **Use the current measurements to improve state estimates** — 在校正状态估计或预测状态估计之间选择 `on`（默认）| `off`

选中此参数时，模块在时间步 `k` 输出校正后的状态估计 x^[k|k]，该估计使用截至时间 `k` 的测量输出进行估计。如果清除此参数，则模块返回时间 `k` 的预测状态估计 x^[k|k−1]，该估计使用截至前一时刻 `k-1` 的测量输出进行估计。如果您的滤波器位于反馈回路中并且 Simulink 模型存在代数环，请清除此参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `UseCurrentEstimator` |
| **类型：** 字符向量 |
| **值：** `'off'`, `'on'` |
| **默认值：** `'on'` |

### **Output state estimation error covariance** — 输出状态估计误差协方差 `off`（默认）| `on`

如果选中此参数，则会在模块中生成状态估计误差协方差输出端口 **P**。

#### 编程使用

|  |
| --- |
| **模块参数：**`OutputStateCovariance` |
| **类型：** 字符向量 |
| **值：**`'off'`,`'on'` |
| **默认值：** `'off'` |

### **Data type** — 模块参数的数据类型 `double`（默认）| `single`

使用此参数指定所有模块参数的数据类型。

#### 编程使用

|  |
| --- |
| **模块参数：** `DataType` |
| **类型：** 字符向量 |
| **值：** `'single'`, `'double'` |
| **默认值：** `'double'` |

### **Sample time** — 模块采样时间 `1`（默认）| 正标量

模块采样时间，指定为正标量。如果您的状态转移函数和测量函数的采样时间不同，请在 **Multirate** 选项卡中选择 **Enable multirate operation**，并改为在 **Multirate** 选项卡中指定采样时间。

#### 依赖项

如果在 **Multirate** 选项卡中 **Enable multirate operation** 参数为 `off`，则此参数可用。

#### 编程使用

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** 字符向量、字符串 |
| **默认值：** `'1'` |

### 多速率选项卡

### **Enable multirate operation** — 启用为状态转移和测量函数指定不同采样时间 `off`（默认）| `on`

如果状态转移函数和测量函数的采样时间不同，请选择此参数。您在 **Multirate** 选项卡中的 **Sample time** 中指定采样时间。

#### 编程使用

|  |
| --- |
| **模块参数：** `EnableMultirate` |
| **类型：** 字符向量 |
| **值：** `'off'`, `'on'` |
| **默认值：** `'off'` |

### **Sample times** — 状态转移和测量函数采样时间 正标量

如果状态转移函数和测量函数的采样时间不同，请指定 **Sample time**。将测量函数的采样时间指定为状态转移采样时间的正整数倍。您指定的采样时间对应于以下输入端口：

- 对应于状态转移函数的端口 — 状态转移函数的附加输入 **StateTransitionFcnInputs** 和时变过程噪声协方差 **Q**。这些端口的采样时间必须始终等于状态转移函数采样时间，但可以不同于测量函数的采样时间。
- 对应于第 *i* 个测量函数的端口 — 测量输出 **y*`i`***、测量函数的附加输入 **MeasurementFcn*`i`*Inputs**、端口 **Enable*`i`*** 处的使能信号，以及时变测量噪声协方差 **R*`i`***。同一测量函数的这些端口的采样时间必须始终相同，但可以不同于状态转移函数和其他测量函数的采样时间。

#### 依赖项

如果在 **Multirate** 选项卡中 **Enable multirate operation** 参数为 `on`，则此参数可用。

#### 编程使用

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

您指定的状态转移、测量和 Jacobian 函数只能使用支持代码生成的 MATLAB 命令和 Simulink 模块。有关支持代码生成的模块列表，请参阅 Blocks Supported for Code Generation (Simulink Coder)。有关支持代码生成的命令列表，请参阅 Functions and Objects Supported for C/C++ Code Generation (MATLAB Coder)。

生成的代码使用的算法与 Extended Kalman Filter 模块本身使用的算法不同。您可能会看到使用这两种方法获得的结果存在一些数值差异。

## 版本历史

**在 R2017a 中引入**

### R2020b：数值变化

从 R2020b 开始，Extended Kalman Filter 算法中的数值改进可能会产生与您在先前版本中获得的结果不同的结果。

## 描述

使用扩展卡尔曼滤波器估计离散时间非线性系统的状态

Extended Kalman Filter 模块使用一阶离散时间扩展卡尔曼滤波器算法估计离散时间非线性系统的状态。

考虑一个具有状态 *x*、输入 *u*、输出 *y*、过程噪声 *w* 和测量噪声 *v* 的被控对象。假设您可以将该被控对象表示为非线性系统。

使用系统的状态转移函数和测量函数以及扩展卡尔曼滤波器算法，模块为当前时间步生成状态估计 x^。有关该算法的信息，请参阅 Extended and Unscented Kalman Filter Algorithms for Online State Estimation。

您为系统创建非线性状态转移函数和测量函数，并在模块中指定这些函数。该模块支持对具有多个以不同采样率运行的传感器的系统进行状态估计。您最多可以指定五个测量函数，每个对应于系统中的一个传感器。您还可以指定状态转移函数和测量函数的 Jacobian。如果您不指定它们，软件会以数值方式计算 Jacobian。有关详细信息，请参阅 State Transition and Measurement Functions。
