---
type: simulink-block
title: 'Unscented Kalman Filter'
family: 'state-estimation'
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

### 输入

### **y1,y2,y3,y4,y5** — 测量的系统输出向量

与您在模块中指定的每个测量函数相对应的测量系统输出。端口数等于系统中的测量函数数。最多可以指定五个测量函数。例如，如果您的系统有两个传感器，则在模块中指定两个测量函数。第一个端口 **y1** 默认可用。当您点击 **应用** 时，软件会生成与第二个测量函数对应的端口 **y2**。

将这些端口指定为 *N* 维向量，其中 *N* 是对应传感器测量的量数。例如，如果您的系统有一个传感器测量对象的位置和速度，则只有一个端口 **y1**。该端口指定为 2 维向量，其值分别对应位置和速度。

#### 依赖关系

第一个端口 **y1** 默认可用。当您点击 **添加测量** 并点击 **应用** 时，会生成端口 **y2** 到 **y5**。

**数据类型：** `single` | `double`

### **StateTransitionFcnInputs** — 状态转移函数的附加可选输入参数 标量 | 向量 | 矩阵

状态转移函数 `f` 的附加可选输入参数，不同于状态 `x` 和过程噪声 `w`。有关状态转移函数的信息，请参阅状态转移函数和测量函数。

假设您的系统具有非加性过程噪声，并且状态转移函数 `f` 具有以下形式：

`x(k+1) =
f(x(k),w(k),StateTransitionFcnInputs)`。

这里 `k` 是时间步，`StateTransitionFcnInputs` 是不同于 `x` 和 `w` 的附加输入参数。

如果您使用 MATLAB® 函数（`.m` 文件）创建 `f`，则当您点击 **应用** 时，软件会生成端口 **StateTransitionFcnInputs**。您可以将此端口的输入指定为标量、向量或矩阵。

如果您的状态转移函数有多个附加输入，请使用 Simulink Function (Simulink) 模块来指定该函数。当您使用 Simulink Function 模块时，可以使用 Inport (Simulink) 模块直接向 Simulink Function 模块提供附加输入。Unscented Kalman Filter 模块不会为附加输入生成输入端口。有关示例，请参阅 Online State Estimation Using Identified Nonlinear Models (System Identification Toolbox)。

#### 依赖关系

仅当以下两个条件均满足时，才会生成此端口：

- 您在 **函数** 中使用 MATLAB 函数指定 `f`，并且 `f` 位于 MATLAB 路径上。
- `f` 除 `x` 和 `w` 外仅需要一个附加输入参数。

**数据类型：** `single` | `double`

### **MeasurementFcn1Inputs,MeasurementFcn2Inputs,MeasurementFcn3Inputs,MeasurementFcn4Inputs,MeasurementFcn5Inputs** — 每个测量函数的附加可选输入参数 标量 | 向量 | 矩阵

测量函数的附加可选输入，不同于状态 `x` 和测量噪声 `v`。有关测量函数的信息，请参阅状态转移函数和测量函数。

**MeasurementFcn1Inputs** 对应于您指定的第一个测量函数，依此类推。例如，假设您的系统有三个传感器和非加性测量噪声，并且三个测量函数 `h1`、`h2` 和 `h3` 具有以下形式：

`y1[k] = h1(x[k],v[k],MeasurementFcn1Inputs)`

`y2[k] = h2(x[k],v[k],MeasurementFcn2Inputs)`

`y3[k] = h3(x[k],v[k])`

这里 `k` 是时间步，`MeasurementFcn1Inputs` 和 `MeasurementFcn2Inputs` 是 `h1` 和 `h2` 的附加输入参数。

如果您在 **函数** 中使用 MATLAB 函数（`.m` 文件）指定 `h1`、`h2` 和 `h3`，则当您点击 **应用** 时，软件会生成端口 **MeasurementFcn1Inputs** 和 **MeasurementFcn2Inputs**。您可以将这些端口的输入指定为标量、向量或矩阵。

如果您的测量函数有多个附加输入，请使用 Simulink Function (Simulink) 模块来指定这些函数。当您使用 Simulink Function 模块时，可以使用 Inport (Simulink) 模块直接向 Simulink Function 模块提供附加输入。Unscented Kalman Filter 模块不会为附加输入生成输入端口。有关示例，请参阅 Online State Estimation Using Identified Nonlinear Models (System Identification Toolbox)。

#### 依赖关系

仅当以下两个条件均满足时，才会生成与测量函数 `h` 对应的端口：

- 您在 **函数** 中使用 MATLAB 函数指定 `h`，并且 `h` 位于 MATLAB 路径上。
- `h` 除 `x` 和 `v` 外仅需要一个附加输入参数。

**数据类型：** `single` | `double`

### **Q** — 时变过程噪声协方差 标量 | 向量 | 矩阵

时变过程噪声协方差，根据 **过程噪声** 参数的值指定为标量、向量或矩阵：

- **过程噪声** 为 `Additive` — 将协方差指定为标量、*Ns* 元向量或 *Ns*×*Ns* 矩阵，其中 *Ns* 是系统的状态数。如果过程噪声项之间不存在互相关，并且所有项具有相同方差，则指定标量。如果过程噪声项之间不存在互相关，但所有项具有不同方差，则指定长度为 *Ns* 的向量。
- **过程噪声** 为 `Nonadditive` — 将协方差指定为 *W*×*W* 矩阵，其中 *W* 是状态转移函数中过程噪声项的数目。

#### 依赖关系

如果将过程噪声协方差指定为 **时变**，则会生成此端口。该端口会在您点击 **应用** 时出现。

**数据类型：** `single` | `double`

### **R1,R2,R3,R4,R5** — 时变测量噪声协方差矩阵

系统最多五个测量函数的时变测量噪声协方差，指定为矩阵。矩阵的大小取决于对应测量函数的 **测量噪声** 参数的值：

- **测量噪声** 为 `Additive` — 将协方差指定为 *N*×*N* 矩阵，其中 *N* 是系统的测量数。
- **测量噪声** 为 `Nonadditive` — 将协方差指定为 *V*×*V* 矩阵，其中 *V* 是对应测量函数中测量噪声项的数目。

#### 依赖关系

如果为对应测量函数将测量噪声协方差指定为 **时变**，则会生成端口。该端口会在您点击 **应用** 时出现。

**数据类型：** `single` | `double`

### **Enable1,Enable2,Enable3,Enable4,Enable5** — 当测量数据可用时启用估计状态校正 标量

假设在对应于第一个测量函数的端口 **y1** 处，并非所有时间点都有测量的输出数据。在 **Enable1** 端口使用非 `0` 的信号值，以在测量数据可用时启用估计状态校正。当测量数据不可用时，将该端口值指定为 `0`。类似地，如果在第 *i* 个测量函数的端口 **y*`i`*** 处并非所有时间点都有测量的输出数据，则将对应端口 **Enable*`i`*** 指定为非 `0` 的值。

#### 依赖关系

如果为某个测量函数选择 **添加启用端口**，则会生成对应于该测量函数的端口。该端口会在您点击 **应用** 时出现。

**数据类型：** `single` | `double` | `Boolean`
### 输出

### **xhat** — 估计状态向量

估计状态，以大小为 *Ns* 的向量返回，其中 *Ns* 是系统的状态数。要访问各个状态，请使用 Selector (Simulink) 模块。

当选中 **使用当前测量来改进状态估计** 参数时，模块输出在时间步 `k` 的校正状态估计 x^[k|k]，该估计使用截至时间 `k` 的测量输出进行估计。如果清除此参数，模块返回时间 `k` 的预测状态估计 x^[k|k−1]，该估计使用截至先前时间 `k-1` 的测量输出进行估计。如果您的滤波器位于反馈环路中，并且您的 Simulink 模型中存在代数环，请清除此参数。

**数据类型：** `single` | `double`

### **P** — 状态估计误差协方差矩阵

状态估计误差协方差，以 *Ns*×*Ns* 矩阵返回，其中 *Ns* 是系统的状态数。要访问各个协方差，请使用 Selector (Simulink) 模块。

#### 依赖关系

如果在 **系统模型** 选项卡中选择 **输出状态估计误差协方差**，并点击 **应用**，则会生成此端口。

**数据类型：** `single` | `double`

## 参数

### 系统模型选项卡

#### 状态转移

### **函数** — 状态转移函数名 `myStateTransitionFcn`（默认） | 函数名

状态转移函数计算系统在时间步 *k*+1 的 *Ns* 元状态向量，给定时间步 *k* 的状态向量。*Ns* 是非线性系统的状态数。您创建状态转移函数，并在 **函数** 中指定函数名。例如，如果 `vdpStateFcn.m` 是您创建并保存的状态转移函数，则将 **函数** 指定为 `vdpStateFcn`。

您创建函数的输入取决于您在 **过程噪声** 中将过程噪声指定为加性还是非加性。

- **过程噪声** 为 `Additive` — 状态转移函数 *f* 指定状态如何作为上一时间步状态值的函数演化：

  `x(k+1) = f(x(k),Us1(k),...,Usn(k))`，

  其中 `x(k)` 是时间 `k` 的估计状态，`Us1,...,Usn` 是状态转移函数所需的任何附加输入参数，例如系统输入或采样时间。要查看具有加性过程噪声的状态转移函数示例，请在命令行键入 `edit vdpStateFcn`。
- **过程噪声** 为 `Nonadditive` — 状态转移函数还指定状态如何作为过程噪声 `w` 的函数演化：

  `x(k+1) =
  f(x(k),w(k),Us1(k),...,Usn(k))`。

有关详细信息，请参阅状态转移函数和测量函数。

您可以使用 Simulink Function (Simulink) 模块或 MATLAB 函数（`.m` 文件）创建 *f*。

- 仅当 *f* 除 `x` 和 `w` 外还有一个附加输入参数 `Us1` 时，才能使用 MATLAB 函数。

  `x(k+1) = f(x(k),w(k),Us1(k))`

  软件会生成一个附加输入端口 **StateTransitionFcnInputs** 来指定此参数。
- 如果您使用 Simulink Function 模块，请使用 Argument Inport (Simulink) 模块指定 `x` 和 `w`，并使用 Simulink Function 模块中的 Inport (Simulink) 模块指定附加输入 `Us1,...,Usn`。Simulink Function 模块中 Argument Inport (Simulink) 和 Argument Outport (Simulink) 模块的 **参数名称** 参数必须彼此不同。您不需要向 Unscented Kalman Filter 模块提供 `Us1,...,Usn`。有关示例，请参阅 Online State Estimation Using Identified Nonlinear Models (System Identification Toolbox)。

#### 程序化使用

|  |
| --- |
| **模块参数：**`StateTransitionFcn` |
| **类型：** character vector, string |
| **默认值：**`'myStateTransitionFcn'` |

### **过程噪声** — 过程噪声特性 `Additive`（默认） | `Nonadditive`

过程噪声特性，指定为以下值之一：

- `Additive` — 过程噪声 `w` 是加性的，并且您在 **函数** 中指定的状态转移函数 *f* 具有以下形式：

  `x(k+1) = f(x(k),Us1(k),...,Usn(k))`，

  其中 `x(k)` 是时间 `k` 的估计状态，`Us1,...,Usn` 是状态转移函数所需的任何附加输入参数。
- `Nonadditive` — 过程噪声是非加性的，并且状态转移函数指定状态如何作为上一时间步的状态 *和* 过程噪声的函数演化：

  `x(k+1) = f(x(k),w(k),Us1(k),...,Usn(k))`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `HasAdditiveProcessNoise` |
| **类型：** character vector |
| **值：** `'Additive'`, `'Nonadditive'` |
| **默认值：** `'Additive'` |

### **协方差** — 时不变过程噪声协方差 `1`（默认） | 标量 | 向量 | 矩阵

时不变过程噪声协方差，根据 **过程噪声** 参数的值指定为标量、向量或矩阵：

- **过程噪声** 为 `Additive` — 将协方差指定为标量、*Ns* 元向量或 *Ns*×*Ns* 矩阵，其中 *Ns* 是系统的状态数。如果过程噪声项之间不存在互相关，并且所有项具有相同方差，则指定标量。如果过程噪声项之间不存在互相关，但所有项具有不同方差，则指定长度为 *Ns* 的向量。
- **过程噪声** 为 `Nonadditive` — 将协方差指定为 *W*×*W* 矩阵，其中 *W* 是过程噪声项的数目。

如果过程噪声协方差是时变的，请选择 **时变**。模块会生成输入端口 **Q** 来指定时变协方差。

#### 依赖关系

如果您未将过程噪声指定为 **时变**，则启用此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ProcessNoise` |
| **类型：** character vector, string |
| **默认值：** `'1'` |

### **时变** — 时变过程噪声协方差 `'off'`（默认） | `'on'`

如果选择此参数，模块会包含一个附加输入端口 **Q** 来指定时变过程噪声协方差。

#### 程序化使用

|  |
| --- |
| **模块参数：** `HasTimeVaryingProcessNoise` |
| **类型：** character vector |
| **值：** `'off'`, `'on'` |
| **默认值：** `'off'` |

#### 初始化

### **初始状态** — 初始状态估计 `0`（默认） | 向量

初始状态估计值，指定为 *Ns* 元向量，其中 *Ns* 是系统中的状态数。根据您对系统的了解指定初始状态值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialState` |
| **类型：** character vector, string |
| **默认值：** `'0'` |

### **初始协方差** — 状态估计误差协方差 `1`（默认） | 标量 | 向量 | 矩阵

状态估计误差协方差，指定为标量、*Ns* 元向量或 *Ns*×*Ns* 矩阵，其中 *Ns* 是系统的状态数。如果指定标量或向量，软件会创建一个 *Ns*×*Ns* 对角矩阵，其对角线上为标量或向量元素。

当您对在 **初始状态** 中指定的初始状态值没有信心时，请为协方差指定一个高值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialStateCovariance` |
| **类型：** character vector, string |
| **默认值：** `'1'` |

#### 无迹变换参数

### **Alpha** — sigma 点的散布 `1e-3`（默认） | 0 到 1 之间的标量值

无迹卡尔曼滤波器算法将系统状态视为具有均值状态值和方差的随机变量。为了计算下一时间步的状态及其统计特性，算法首先使用无迹变换生成一组围绕均值分布的状态值。这些生成的状态值称为 sigma 点。算法将每个 sigma 点用作状态转移函数和测量函数的输入，以获得一组新的变换状态点和测量值。变换后的点用于计算下一时间步的状态和状态估计误差协方差值。

sigma 点围绕均值状态值的散布由两个参数 **Alpha** 和 **Kappa** 控制。第三个参数 **Beta** 会影响状态和测量协方差计算期间变换点的权重：

- **Alpha** — 确定 sigma 点围绕均值状态值的散布。指定为 0 到 1 之间的标量值（`0` < **Alpha** <= `1`）。它通常是较小的正值。sigma 点的散布与 **Alpha** 成正比。较小的值对应于更接近均值状态的 sigma 点。
- **Kappa** — 第二个缩放参数，通常设置为 0。较小的值对应于更接近均值状态的 sigma 点。散布与 `Kappa` 的平方根成正比。
- **Beta** — 纳入关于状态分布的先验知识。对于高斯分布，**Beta** = 2 是最优的。

如果您知道状态和状态协方差的分布，可以调整这些参数以捕获分布高阶矩的变换。该算法只能跟踪状态概率分布中的单个峰值。如果系统的状态分布中有多个峰值，您可以调整这些参数，使 sigma 点保持在单个峰值附近。例如，选择较小的 **Alpha** 以生成接近均值状态值的 sigma 点。

有关详细信息，请参阅无迹卡尔曼滤波器算法。

#### 程序化使用

|  |
| --- |
| **模块参数：**`Alpha` |
| **类型：** character vector, string |
| **默认值：**`'1e-3'` |

### **Beta** — 状态分布特征 `2`（默认） | 大于或等于 0 的标量值

用于调整变换 sigma 点权重的状态分布特征，指定为大于或等于 0 的标量值。对于高斯分布，`Beta` = 2 是最佳选择。

有关详细信息，请参阅 **Alpha** 的说明。

#### 程序化使用

|  |
| --- |
| **模块参数：**`Beta` |
| **类型：** character vector, string |
| **默认值：**`'2'` |

### **Kappa** — sigma 点的散布 `0`（默认） | 0 到 3 之间的标量值

sigma 点围绕均值状态值的散布，指定为 0 到 3 之间的标量值（`0` <= **Kappa** <= `3`）。**Kappa** 通常指定为 `0`。较小的值对应于更接近均值状态的 sigma 点。散布与 **Kappa** 的平方根成正比。有关详细信息，请参阅 **Alpha** 的说明。

#### 程序化使用

|  |
| --- |
| **模块参数：**`Kappa` |
| **类型：** character vector, string |
| **默认值：**`'0'` |

#### 测量

### **函数** — 测量函数名 `myMeasurementFcn`（默认） | 函数名

测量函数计算非线性系统在时间步 *k* 的 *N* 元输出测量向量，给定时间步 *k* 的状态向量。您创建测量函数，并在 **函数** 中指定函数名。例如，如果 `vdpMeasurementFcn.m` 是您创建并保存的测量函数，则将 **函数** 指定为 `vdpMeasurementFcn`。

您创建函数的输入取决于您在 **测量噪声** 中将测量噪声指定为加性还是非加性。

- **测量噪声** 为 `Additive` — 测量函数 *h* 指定测量值如何作为状态值的函数演化：

  `y(k) = h(x(k),Um1(k),...,Umn(k))`，

  其中 `y(k)` 和 `x(k)` 是时间 `k` 的估计输出和估计状态，`Um1,...,Umn` 是测量函数所需的任何可选输入参数。例如，如果您使用传感器跟踪对象，附加输入可以是传感器位置。

  要查看具有加性过程噪声的测量函数示例，请在命令行键入 `edit vdpMeasurementFcn`。
- **测量噪声** 为 `Nonadditive`— 测量函数还指定输出测量值如何作为测量噪声 `v` 的函数演化：

  `y(k) =
  h(x(k),v(k),Um1(k),...,Umn(k))`。

  要查看具有非加性过程噪声的测量函数示例，请在命令行键入 `edit vdpMeasurementNonAdditiveNoiseFcn`。

有关详细信息，请参阅状态转移函数和测量函数。

您可以使用 Simulink Function (Simulink) 模块或 MATLAB 函数（`.m` 文件）创建 *h*。

- 仅当 *h* 除 `x` 和 `v` 外还有一个附加输入参数 `Um1` 时，才能使用 MATLAB 函数。

  `y[k] = h(x[k],v[k],Um1(k))`

  软件会生成一个附加输入端口 **MeasurementFcnInput** 来指定此参数。
- 如果您使用 Simulink Function 模块，请使用 Argument Inport (Simulink) 模块指定 `x` 和 `v`，并使用 Simulink Function 模块中的 Inport (Simulink) 模块指定附加输入 `Um1,...,Umn`。Simulink Function 模块中 Argument Inport (Simulink) 和 Argument Outport (Simulink) 模块的 **参数名称** 参数必须彼此不同。您不需要向 Unscented Kalman Filter 模块提供 `Um1,...,Umn`。有关示例，请参阅 Online State Estimation Using Identified Nonlinear Models (System Identification Toolbox)。

如果您的系统中有多个传感器，可以指定多个测量函数。您可以使用 **添加测量** 按钮最多指定五个测量函数。要删除测量函数，请使用 **删除测量**。

#### 程序化使用

|  |
| --- |
| **模块参数：**`MeasurementFcn1`, `MeasurementFcn2`, `MeasurementFcn3`, `MeasurementFcn4`, `MeasurementFcn5` |
| **类型：** character vector, string |
| **默认值：**`'myMeasurementFcn'` |

### **测量噪声** — 测量噪声特性 `Additive`（默认） | `Nonadditive`

测量噪声特性，指定为以下值之一：

- `Additive` — 测量噪声 `v` 是加性的，并且您在 **函数** 中指定的测量函数 *h* 具有以下形式：

  `y(k) = h(x(k),Um1(k),...,Umn(k))`，

  其中 `y(k)` 和 `x(k)` 是时间 `k` 的估计输出和估计状态，`Um1,...,Umn` 是测量函数所需的任何可选输入参数。
- `Nonadditive` — 测量噪声是非加性的，并且测量函数指定输出测量值如何作为状态 *和* 测量噪声的函数演化：

  `y(k) = h(x(k),v(k),Um1(k),...,Umn(k))`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `HasAdditiveMeasurementNoise1`, `HasAdditiveMeasurementNoise2`, `HasAdditiveMeasurementNoise3`, `HasAdditiveMeasurementNoise4`, `HasAdditiveMeasurementNoise5` |
| **类型：** character vector |
| **值：** `'Additive'`, `'Nonadditive'` |
| **默认值：** `'Additive'` |

### **启用测量回绕** — 启用测量回绕 `off`（默认） | `on`

选择此参数以在您具有独立于模型状态的圆形测量时启用测量回绕来估计状态。如果选择此参数，则您指定的测量函数必须包含以下两个输出：

1. 测量值，指定为非线性系统在时间步 *k* 的 *N* 元输出测量向量，给定时间步 *k* 的状态向量。*N* 是系统的测量数。
2. 测量回绕边界，指定为 *N*×`2` 矩阵，其中第一列提供最小测量边界，第二列提供最大测量边界。

启用 **启用测量回绕** 复选框会将测量残差包裹在定义的边界内，这有助于防止滤波器由于不正确的测量残差值而发散。有关示例，请参阅 State Estimation with Wrapped Measurements Using Extended Kalman Filter。

#### 程序化使用

|  |
| --- |
| **模块参数：**`EnableMeasurementWrapping1`, `EnableMeasurementWrapping2`, `EnableMeasurementWrapping3`, `EnableMeasurementWrapping4`, `EnableMeasurementWrapping5` |
| **类型：** character vector |
| **值：** `'off'`, `'on'` |
| **默认值：** `'off'` |

### **协方差** — 时不变测量噪声协方差 `1`（默认） | 矩阵

时不变测量噪声协方差，指定为矩阵。矩阵的大小取决于 **测量噪声** 参数的值：

- **测量噪声** 为 `Additive` — 将协方差指定为 *N*×*N* 矩阵，其中 *N* 是系统的测量数。
- **测量噪声** 为 `Nonadditive` — 将协方差指定为 *V*×*V* 矩阵，其中 *V* 是测量噪声项的数目。

如果测量噪声协方差是时变的，请选择 **时变**。模块会生成输入端口 **R*`i`*** 来指定第 *i* 个测量函数的时变协方差。

#### 依赖关系

如果您未将过程噪声指定为 **时变**，则启用此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MeasurementNoise1`, `MeasurementNoise2`, `MeasurementNoise3`, `MeasurementNoise4`, `MeasurementNoise5` |
| **类型：** character vector, string |
| **默认值：** `'1'` |

### **时变** — 时变测量噪声协方差 `off`（默认） | `on`

如果您为第一个测量函数的测量噪声协方差选择此参数，模块会包含一个附加输入端口 **R1**。您在 **R1** 中指定时变测量噪声协方差。类似地，如果您为第 *i* 个测量函数选择 **时变**，模块会包含一个附加输入端口 **R*`i`***，用于指定该函数的时变测量噪声协方差。

#### 程序化使用

|  |
| --- |
| **模块参数：** `HasTimeVaryingMeasurementNoise1`, `HasTimeVaryingMeasurementNoise2`, `HasTimeVaryingMeasurementNoise3`, `HasTimeVaryingMeasurementNoise4`, `HasTimeVaryingMeasurementNoise5` |
| **类型：** character vector |
| **值：** `'off'`, `'on'` |
| **默认值：** `'off'` |

### **添加启用端口** — 仅在测量数据可用时启用估计状态校正 `off`（默认） | `on`

假设在对应于第一个测量函数的端口 **y1** 处，并非所有时间点都有测量的输出数据。选择 **添加启用端口** 以生成输入端口 **Enable1**。在此端口使用信号，仅在测量数据可用时启用估计状态校正。类似地，如果在第 *i* 个测量函数的端口 **y*`i`*** 处并非所有时间点都有测量的输出数据，请选择对应的 **添加启用端口**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `HasMeasurementEnablePort1`, `HasMeasurementEnablePort2`, `HasMeasurementEnablePort3`, `HasMeasurementEnablePort4`, `HasMeasurementEnablePort5` |
| **类型：** character vector |
| **值：** `'off'`, `'on'` |
| **默认值：** `'off'` |

#### 设置

### **使用当前测量来改进状态估计** — 在校正状态估计或预测状态估计之间选择 `on`（默认） | `off`

选中此参数时，模块输出在时间步 `k` 的校正状态估计 x^[k|k]，该估计使用截至时间 `k` 的测量输出进行估计。如果清除此参数，模块返回时间 `k` 的预测状态估计 x^[k|k−1]，该估计使用截至先前时间 `k-1` 的测量输出进行估计。如果您的滤波器位于反馈环路中，并且您的 Simulink 模型中存在代数环，请清除此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `UseCurrentEstimator` |
| **类型：** character vector |
| **值：** `'off'`, `'on'` |
| **默认值：** `'on'` |

### **输出状态估计误差协方差** — 输出状态估计误差协方差 `off`（默认） | `on`

如果选择此参数，模块中会生成状态估计误差协方差输出端口 **P**。

#### 程序化使用

|  |
| --- |
| **模块参数：**`OutputStateCovariance` |
| **类型：** character vector |
| **值：**`'off'`,`'on'` |
| **默认值：** `'off'` |

### **数据类型** — 模块参数的数据类型 `double`（默认） | `single`

使用此参数指定所有模块参数的数据类型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DataType` |
| **类型：** character vector |
| **值：** `'single'`, `'double'` |
| **默认值：** `'double'` |

### **采样时间** — 模块采样时间 `1`（默认） | 正标量

模块采样时间，指定为正标量。如果状态转移函数和测量函数的采样时间不同，请在 **多速率** 选项卡中选择 **启用多速率操作**，并改为在 **多速率** 选项卡中指定采样时间。

#### 依赖关系

如果在 **多速率** 选项卡中，**启用多速率操作** 参数为 `off`，则此参数可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** character vector, string |
| **默认值：** `'1'` |

### 多速率选项卡

### **启用多速率操作** — 为状态转移函数和测量函数启用不同采样时间的指定 `off`（默认） | `on`

如果状态转移函数和测量函数的采样时间不同，请选择此参数。您在 **多速率** 选项卡的 **采样时间** 中指定采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `EnableMultirate` |
| **类型：** character vector |
| **值：** `'off'`, `'on'` |
| **默认值：** `'off'` |

### **采样时间** — 状态转移函数和测量函数采样时间 正标量

如果状态转移函数和测量函数的采样时间不同，请指定 **采样时间**。将测量函数的采样时间指定为状态转移采样时间的正整数倍。您指定的采样时间对应以下输入端口：

- 对应于状态转移函数的端口 — 状态转移函数的附加输入 **StateTransitionFcnInputs** 和时变过程噪声协方差 **Q**。这些端口的采样时间必须始终等于状态转移函数采样时间，但可以不同于测量函数的采样时间。
- 对应于第 *i* 个测量函数的端口 — 测量输出 **y*`i`***、测量函数的附加输入 **MeasurementFcn*`i`*Inputs**、端口 **Enable*`i`*** 处的启用信号，以及时变测量噪声协方差 **R*`i`***。同一测量函数的这些端口的采样时间必须始终相同，但可以不同于状态转移函数和其他测量函数的采样时间。

#### 依赖关系

如果在 **多速率** 选项卡中，**启用多速率操作** 参数为 `on`，则此参数可用。

#### 程序化使用

|  |
| --- |
| **模块参数：**`StateTransitionFcnSampleTime`, `MeasurementFcn1SampleTime1`, `MeasurementFcn1SampleTime2`, `MeasurementFcn1SampleTime3`, `MeasurementFcn1SampleTime4`, `MeasurementFcn1SampleTime5` |
| **类型：** character vector, string |
| **默认值：** `'1'` |

## 所属库

Control System Toolbox / State Estimation System Identification Toolbox / Estimators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

您指定的状态转移函数和测量函数必须仅使用支持代码生成的 MATLAB 命令和 Simulink 模块。有关支持代码生成的模块列表，请参阅 Blocks Supported for Code Generation (Simulink Coder)。有关支持代码生成的命令列表，请参阅 Functions and Objects Supported for C/C++ Code Generation (MATLAB Coder)。

生成的代码使用与 Unscented Kalman Filter 模块本身所用算法不同的算法。您可能会看到使用这两种方法获得的结果存在一些数值差异。

## 版本历史

**在 R2017a 中引入**

### R2020b：数值变更

从 R2020b 开始，Unscented Kalman Filter 算法中的数值改进可能会产生与以前版本获得的结果不同的结果。

## 描述

使用无迹卡尔曼滤波器估计离散时间非线性系统的状态

Unscented Kalman Filter 模块使用离散时间无迹卡尔曼滤波器算法估计离散时间非线性系统的状态。

考虑一个具有状态 *x*、输入 *u*、输出 *y*、过程噪声 *w* 和测量噪声 *v* 的被控对象。假设您可以将该被控对象表示为非线性系统。

使用系统的状态转移函数和测量函数以及无迹卡尔曼滤波器算法，模块为当前时间步生成状态估计 x^。有关该算法的信息，请参阅 Extended and Unscented Kalman Filter Algorithms for Online State Estimation。

您为系统创建非线性状态转移函数和测量函数，并在模块中指定这些函数。该模块支持对具有多个传感器的系统进行状态估计，这些传感器以不同采样率运行。您最多可以指定五个测量函数，每个对应于系统中的一个传感器。有关详细信息，请参阅状态转移函数和测量函数。
