---
type: simulink-block
title: 'Particle Filter'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'State Estimation'
documentation_page: 'pf_block'
documentation_source_path: 'ref/pf_block.html'
language: zh-CN
chinese_source: worker-translation
---

# Particle Filter

## 端口

### 输入

### **y1,y2,y3,y4,y5** — 测得系统输出 vector

与您在模块中指定的每个测量似然函数相对应的测得系统输出。端口数等于系统中测量似然函数的数量。最多可以指定五个测量似然函数。例如，如果系统有两个传感器，则在模块中指定两个测量似然函数。默认情况下，第一个端口 **y1** 可用。点击 **添加测量**，生成与第二个测量似然函数对应的端口 **y2**。

将这些端口指定为 *N* 维 vector，其中 *N* 是相应传感器测量的量数目。例如，如果系统有一个传感器测量对象的位置和速度，则只有一个端口 **y1**。该端口指定为二维 vector，其值对应位置和速度。

#### 依赖关系

第一个端口 **y1** 默认可用。要生成端口 **y2** 至 **y5**，点击 **添加测量**。

### **StateTransitionFcnInputs** — 状态转移函数的可选输入参数 scalar | vector | matrix

状态转移函数 `f` 中除状态 `x` 之外的可选输入参数。

如果您使用 MATLAB® 函数（`.m` 文件）创建 `f`，则当您输入函数名称并点击 **应用** 时，软件会生成端口 **StateTransitionFcnInputs**。

如果您的状态转移函数有多个额外输入，请使用 Simulink Function (Simulink) block 来指定该函数。使用 Simulink Function block 时，您通过 Inport (Simulink) blocks 将额外输入直接提供给 Simulink Function block。Particle Filter 模块中不会为这些额外输入生成输入端口。

#### 依赖关系

要生成此端口，应满足以下两个条件：

- 您使用 MATLAB 函数在 **函数** 中指定 `f`，并且 `f` 位于 MATLAB 路径上。
- `f` 除粒子外仅需要额外一个输入参数。

### **MeasurementLikelihoodFcn1Inputs,...,MeasurementLikelihoodFcn5Inputs** — 每个测量似然函数的可选输入参数 scalar | vector | matrix

测量似然函数中除状态 `x` 和测量 `y` 之外的可选输入。

**MeasurementLikelihoodFcn1Inputs** 对应于您指定的第一个测量似然函数，依此类推。

如果您在 **函数** 中使用 MATLAB 函数（`.m` 文件）指定两个测量输入，则点击 **应用** 时，软件会生成端口 **MeasurementLikelihoodFcn1Inputs** 和 **MeasurementLikelihoodFcn2Inputs**。您可以将这些端口的输入指定为 scalar、vector 或 matrix。

如果您的测量似然函数有多个额外输入，请使用 Simulink Function (Simulink) blocks 来指定这些函数。使用 Simulink Function block 时，您通过 Inport (Simulink) blocks 将额外输入直接提供给 Simulink Function block。Particle Filter 模块中不会为这些额外输入生成输入端口。

#### 依赖关系

要为测量似然函数 `h` 生成对应端口，应满足以下两个条件：

- 您使用 MATLAB 函数在 **函数** 中指定测量输入 `h`，并且 `h` 位于 MATLAB 路径上。
- `h` 除粒子和测量外仅需要额外一个输入参数。

### **Enable1,Enable2,Enable3,Enable4,Enable5** — 当测得数据可用时启用估计状态校正 scalar

当测得数据可用时，启用估计状态校正。

例如，假设在与第一个测量似然函数对应的端口 **y1** 处，并非所有时间点都有测得输出数据。然后，在 **Enable1** 端口使用非 `0` 的信号值，以便在测得数据可用时启用估计状态校正。当测得数据不可用时，将该端口值指定为 `0`。类似地，如果对于第 *i* 个测量似然函数，在端口 **y*`i`*** 处并非所有时间点都有测得输出数据，则将相应端口 **Enable*`i`*** 指定为非 `0` 的值。

#### 依赖关系

要为测量似然函数生成对应端口，请为该测量似然函数选择 **添加使能端口**。点击 **应用** 时该端口会出现。

### 输出

### **xhat** — 估计状态 vector

估计状态，返回为大小为 *Ns* 的 vector，其中 *Ns* 是系统的状态数。要访问各个状态，请使用 Selector (Simulink) block。

当选中 **使用当前测量值改进状态估计** 参数时，模块在时间步 `k` 输出校正状态估计 x^[k|k]，该估计使用截至时间 `k` 的测得输出进行估计。如果清除此参数，模块返回时间 `k` 的预测状态估计 x^[k|k−1]，该估计使用截至前一时刻 `k-1` 的测得输出进行估计。如果您的滤波器位于反馈环路中，并且 Simulink® 模型存在代数环，请清除此参数。

### **P** — 状态估计误差协方差 matrix

状态估计误差协方差，返回为 *Ns*-by-*Ns* matrix，其中 *Ns* 是系统的状态数。要访问各个协方差，请使用 Selector (Simulink) block。

仅当您在 **模块输出、多速率** 选项卡中选择 **输出状态估计误差协方差** 并点击 **应用** 时，才能输出误差协方差。

#### 依赖关系

要启用此参数，请将 **模块输出、多速率** 选项卡中的 **状态估计方法** 参数设置为 `'Mean'`。

### **Particles** — 用于状态估计的粒子值 array

用于状态估计的粒子值，返回为 *Ns*-by-*Np* 或 *Np*-by-*Ns* array。*Ns* 是系统的状态数，*Np* 是粒子数。

- 如果 `StateOrientation` 参数指定为 `'column'`，则 **Particles** 返回为 *Ns*-by-*Np* array。
- 如果 `StateOrientation` 参数指定为 `'row'`，则 **Particles** 返回为 *Np*-by-*Ns* array。

#### 依赖关系

要生成此端口，请在 **模块输出、多速率** 选项卡中选择 **输出所有粒子**，然后点击 **应用**。

### **Weights** — 用于状态估计的粒子权重 vector

用于状态估计的粒子权重，返回为 1-by-*Np* 或 *Np*-by-1 vector，其中 *Np* 是用于状态估计的粒子数。

- 如果 `StateOrientation` 参数指定为 `'column'`，则 **Weights** 返回为 1-by-*Np* vector，其中每个权重与 `Particles` array 中同一列的粒子相关联。
- 如果 `StateOrientation` 参数指定为 `'row'`，则 **Weights** 返回为 *Np*-by-1 vector，其中每个权重与 `Particles` array 中同一行的粒子相关联。

#### 依赖关系

要生成此端口，请在 **模块输出、多速率** 选项卡中选择 **输出权重**，然后点击 **应用**。

## 参数

### 系统模型选项卡

#### 状态转移

### **函数** — 状态转移函数名称 `'vdpParticleFilterStateFcn'` (默认) | 函数名称

粒子滤波器状态转移函数根据系统的动态特性和过程噪声，在给定时间步 *k* 的粒子的情况下，计算时间步 *k+1* 的粒子。此函数的语法为：

```
particlesNext = f(particles, param1, param2, ...)
```

其中，如果 **状态方向** 指定为 `'column'`，则 *particles* 和 *particlesNext* 的维度为 *Ns*-by-*Np*；如果 **状态方向** 指定为 `'row'`，则维度为 *Np*-by-*Ns*。此外，`param_i` 表示您可能指定的可选输入参数。有关可选输入参数的详细信息，请参阅 StateTransitionFcnInputs。

您创建状态转移函数，并在 **函数** 中指定函数名称。例如，如果 `vdpParticleFilterStateFcn.m` 是您创建并保存的状态转移函数，则将 **函数** 指定为 `'vdpParticleFilterStateFcn'`。

您可以使用 Simulink Function (Simulink) block 创建 **函数**，也可以将其创建为 MATLAB 函数（`.m` 文件）。

#### 编程使用

|  |
| --- |
| **模块参数：**`StateTransitionFcn` |
| **类型：** character vector, string |
| **默认值：**`'vdpParticleFilterStateFcn'` |

#### 初始化

### **粒子数** — 滤波器中使用的粒子数 1000 (默认) | positive scalar integer

滤波器中使用的粒子数，指定为 positive scalar integer。每个粒子表示系统中的一个状态假设。粒子数越多，状态估计精度越高，但运行滤波器所需的计算量也会增加。

#### 编程使用

|  |
| --- |
| **模块参数：**`NumberOfParticles` |
| **类型：** positive scalar integer |
| **默认值：**`1000` |

### **分布** — 粒子的初始分布 `'Gaussian'` (默认) | `'Uniform'` | `'Custom'`

粒子的初始分布，指定为 `'Gaussian'`、`'Uniform'` 或 `'Custom'`。

如果选择 `'Gaussian'`，则初始粒子集或状态假设按多变量高斯分布分布，您需要指定 **均值** 和 **协方差**。假定所有粒子的初始权重相等。

如果选择 `'Uniform'`，则初始粒子集按均匀分布分布，您需要指定上下 **状态边界**。假定所有粒子的初始权重相等。

`'Custom'` 允许您指定自己的初始粒子集及其权重。您可以使用任意概率分布为 **Particles** 和 **Weights** 初始化滤波器。

#### 编程使用

|  |
| --- |
| **模块参数：**`InitialDistribution` |
| **类型：** character vector |
| **值：**`'Gaussian'`, `'Uniform'`, `'Custom'` |
| **默认值：**`'Gaussian'` |

### **均值** — 粒子的初始均值 [0;0] (默认) | vector

粒子的初始均值，指定为 vector。要估计的状态数定义该 vector 的长度。

#### 依赖关系

要启用此参数，请将 **系统模型** 选项卡中的 **分布** 参数设置为 `Gaussian`。

#### 编程使用

|  |
| --- |
| **模块参数：**`InitialMean` |
| **类型：** array |
| **默认值：**`[0,0]` |

### **协方差** — 粒子的初始协方差 1 (默认) | scalar | vector | matrix

粒子的初始协方差，指定为 scalar、vector 或 matrix。

如果 **协方差** 指定为：

- scalar，则它必须为正。协方差假定为 [*Ns* *Ns*] matrix，对角线元素为此 scalar。这里，*Ns* 是状态数。
- vector，则每个元素必须为正。协方差假定为 [*Ns* *Ns*] matrix，对角线元素为 vector 的元素。
- matrix，则它必须为半正定。

#### 依赖关系

要启用此参数，请将 **系统模型** 选项卡中的 **分布** 参数设置为 `Gaussian`。

#### 编程使用

|  |
| --- |
| **模块参数：**`InitialCovariance` |
| **类型：** scalar, vector, or matrix |
| **默认值：**`1` |

### **圆周变量** — 用于状态估计的圆周变量 0 (默认) | scalar | vector

用于状态估计的圆周变量，指定为 scalar 或 *Ns*-element vector，其中 *Ns* 是状态数。

如果 **圆周变量** 指定为 scalar，则软件将其扩展为 vector，其中每个元素都等于此 scalar。圆周（或角度）分布使用范围为 [`-π` `π`] 的概率密度函数。如果系统中的某些状态表示角度量（如对象的方向），请使用圆周变量。

#### 编程使用

|  |
| --- |
| **模块参数：**`CircularVariables` |
| **类型：** scalar, vector |
| **默认值：**`0` |

### **状态方向** — 输入系统状态的方向 `'column'` (默认) | `'row'`

系统状态的方向，指定为 `'column'` 或 `'row'`。

如果 **状态方向** 指定为：

- `'column'`，则状态转移和测量似然函数的第一个输入参数为 [*Ns* *Np*]。在这种情况下，此 matrix 的第 *i* 列是第 *i* 个粒子（状态假设）。此外，状态估计 **xhat** 输出为 [*Ns* 1] vector。这里，*Ns* 是状态数，*Np* 是粒子数。
- `'row'`，则状态转移和测量似然函数的第一个输入参数为 [*Np* *Ns*]，并且此 matrix 的每一行包含一个粒子。此外，状态估计 **xhat** 输出为 [1 *Ns*] vector。

#### 编程使用

|  |
| --- |
| **模块参数：**`StateOrientation` |
| **类型：** character vector |
| **值：**`'column'`, `'row'` |
| **默认值：**`'column'` |

### **状态边界** — 系统状态的初始边界 [-3 3;-3 3] (默认) | array

系统状态的初始边界，指定为 *Ns*-by-2 array，其中 *Ns* 是状态数。

第 *i* 行列出第 *i* 个状态的粒子初始分布的均匀分布下界和上界。

#### 依赖关系

要启用此参数，请将 **系统模型** 选项卡中的 **分布** 参数设置为 `Uniform`。

#### 编程使用

|  |
| --- |
| **模块参数：**`InitialStateBounds` |
| **类型：** array |
| **默认值：** `[-3 3;-3 3]` |

### **Particles** — 用于状态估计的自定义粒子分布 [] (默认) | array

用于状态估计的自定义粒子分布，指定为 *Ns*-by-*Np* 或 *Np*-by-*Ns* array。*Ns* 是系统的状态数，*Np* 是粒子数。

您选择一个分布，使用 `makedist` 函数为其创建概率分布对象，并使用 `random` 函数生成所需分布的粒子。

- 如果 `StateOrientation` 参数为 `'column'`，则将 **Particles** 指定为 *Ns*-by-*Np* array。

  例如，

  ```
  pd = makedist('Poisson');
  Particles = random(pd,Ns,Np);
  ```
- 如果 `StateOrientation` 参数为 `'row'`，则将 **Particles** 指定为 *Np*-by-*Ns* array。

  例如，

  ```
  pd = makedist('Poisson');
  Particles = random(pd,Np,Ns);
  ```

#### 依赖关系

要启用此参数，请将 **系统模型** 选项卡中的 **分布** 参数设置为 `Custom`。

#### 编程使用

|  |
| --- |
| **模块参数：**`InitialParticles` |
| **类型：** array |
| **默认值：**`[]` |

### **Weights** — 用于状态估计的自定义粒子权重值 [] (默认) | vector of positive values

用于状态估计的自定义粒子权重值，指定为 1-by-*Np* 或 *Np*-by-1 vector of positive values，其中 *Np* 是用于状态估计的粒子数。

- 如果 `StateOrientation` 参数为 `'column'`，则将 **Weights** 指定为 1-by-*Np* vector。该 vector 中的每个权重与 `Particles` array 中同一列的粒子相关联。

  例如，

  ```
  Weights = ones(1,Np)/Np;
  ```
- 如果 `StateOrientation` 参数为 `'row'`，则将 **Weights** 指定为 *Np*-by-1 vector。该 vector 中的每个权重与 `Particles` array 中同一行的粒子相关联。

  例如，

  ```
  Weights = ones(Np,1)/Np;
  ```

#### 依赖关系

要启用此参数，请将 **系统模型** 选项卡中的 **分布** 参数设置为 `Custom`。

#### 编程使用

|  |
| --- |
| **模块参数：**`InitialWeights` |
| **类型：** vector of positive values |
| **默认值：**`[]` |

#### 测量

### **函数** — 测量似然函数名称 `'vdpMeasurementLikelihoodFcn'` (默认) | 函数名称

测量似然函数使用传感器测量值计算粒子（状态假设）的似然。对于每个状态假设（粒子），该函数首先计算 *Nm*-element 测量假设 vector。然后基于传感器测量值和测量噪声概率分布计算每个测量假设的似然。此函数的语法为：

```
likelihood = h(particles, measurement, param1, param2, ...)
```

其中，*likelihood* 是 *Np*-element vector，其中 *Np* 是粒子数。如果 **状态方向** 指定为 `'column'`，则 *particles* 的维度为 *Ns*-by-*Np*；如果 **状态方向** 指定为 `'row'`，则维度为 *Np*-by-*Ns*。*measurement* 是 *Nm*-element vector，其中 *Nm* 是传感器提供的测量数。*param\_i* 表示您可能指定的可选输入参数。有关可选输入参数的详细信息，请参阅 MeasurementLikelihoodFcn1Inputs,...,MeasurementLikelihoodFcn5Inputs。

您创建测量似然函数，并在 **函数** 中指定函数名称。例如，如果 `vdpMeasurementLikelihoodFcn.m` 是您创建并保存的测量似然函数，则将 **函数** 指定为 `'vdpMeasurementLikelihoodFcn'`。

您可以使用 Simulink Function (Simulink) block 创建 **函数**，也可以将其创建为 MATLAB 函数（`.m` 文件）。

- 仅当 *h* 除 **Particles** 和 **Measurement** 之外具有零个或一个额外输入参数 `param_i` 时，才能使用 MATLAB 函数。

  软件会生成额外输入端口 **MeasurementLikelihoodFcn*`i`*Inputs**，以便为第 *i* 个测量似然函数指定此参数，然后点击 **应用**。
- 如果您使用 Simulink Function block，请在 Simulink Function block 中使用 Argument Inport (Simulink) blocks 指定 `x` 和 `y`，并使用 Inport (Simulink) blocks 指定额外输入 `param_i`。您不需要将 `param_i` 提供给 Particle Filter 模块。

如果系统中有多个传感器，您可以指定多个测量似然函数。您可以使用 **添加测量** 按钮最多指定五个测量似然函数。要移除测量似然函数，请使用 **移除测量**。

#### 编程使用

|  |
| --- |
| **模块参数：**`MeasurementLikelihoodFcn1`, `MeasurementLikelihoodFcn2`, `MeasurementLikelihoodFcn3`, `MeasurementLikelihoodFcn4`, `MeasurementLikelihoodFcn5` |
| **类型：** character vector, string |
| **默认值：**`'vdpMeasurementLikelihoodFcn'` |

### **添加使能端口** — 仅当测得数据可用时启用估计状态校正 `off` (默认) | `on`

假设在与第一个测量似然函数对应的端口 **y1** 处，并非所有时间点都有测得输出数据。要生成输入端口 **Enable1**，请选择 **添加使能端口**。使用此端口处的信号，仅在测得数据可用时启用估计状态校正。类似地，如果对于第 *i* 个测量似然函数，在端口 **y*`i`*** 处并非所有时间点都有测得输出数据，请选择相应的 **添加使能端口**。

#### 编程使用

|  |
| --- |
| **模块参数：**`HasMeasurementEnablePort1`, `HasMeasurementEnablePort2`, `HasMeasurementEnablePort3`, `HasMeasurementEnablePort4`, `HasMeasurementEnablePort5` |
| **类型：** character vector |
| **值：**`'off'`, `'on'` |
| **默认值：**`'off'` |

#### 重采样

### **重采样方法** — 用于粒子重采样的方法 `'Multinomial'` (默认) | `'Systemic'` | `'Stratified'`

用于粒子重采样的方法，指定为以下之一：

- `'Multinomial'` — 多项重采样，也称为简化随机采样，从开区间 `(0,1)` 上的均匀分布独立生成 `N` 个随机数，并使用它们按权重比例选择粒子。
- `'Stratified'` — 分层重采样将整个粒子总体划分为称为层的子集。它预先将 `(0,1)` 区间划分为 `N` 个大小为 `1/N` 的不相交子区间。在每个子区间中独立抽取随机数，并在各层中选择样本索引。
- `'Systematic'` — 系统重采样与分层重采样类似，因为它也利用层。一个区别是它仅从开区间 `(0,1/N)` 中抽取一个随机数，其余样本点以固定 `1/N` 步长确定性地计算。

#### 编程使用

|  |
| --- |
| **模块参数：**`ResamplingMethod` |
| **类型：** character vector |
| **值：**`'Multinomial'`, `'Systemic'`, `'Stratified'` |
| **默认值：**`'Multinomial'` |

### **触发方法** — 确定何时进行重采样的方法 `'Ratio'` (默认) | `'Interval'`

确定何时进行重采样的方法，指定为 `'Ratio'` 或 `'Interval'`。`'Ratio'` 值基于有效总粒子比率触发重采样。`'Interval'` 值在粒子滤波器运行的固定时间步触发重采样。

#### 编程使用

|  |
| --- |
| **模块参数：**`TriggerMethod` |
| **类型：** character vector |
| **值：**`'Ratio'`, `'Interval'` |
| **默认值：**`'Ratio'` |

### **最小有效粒子比率** — 有效粒子数与总粒子数的最小期望比率 0.5 (默认) | positive scalar

有效粒子数与总粒子数的最小期望比率，指定为 positive scalar。有效粒子数是当前粒子集对后验分布近似程度的度量。有效粒子比率越低，意味着参与估计的粒子数越少，需要进行重采样。

如果有效粒子数与总粒子数的比率低于最小有效粒子比率，则触发重采样步骤。

将最小有效粒子比率指定为 0 到 1 之间的任意值。

#### 依赖关系

要启用此参数，请将 **系统模型** 选项卡中的 **触发方法** 参数设置为 `Ratio`。

#### 编程使用

|  |
| --- |
| **模块参数：**`MinEffectiveParticleRatio` |
| **类型：** scalar |
| **值：**  范围 `[0,1]` |
| **默认值：**`0.5` |

### **采样间隔** — 重采样之间的固定间隔 1 (默认) | positive scalar integer

重采样之间的固定间隔，指定为 positive scalar integer。采样间隔确定在哪些校正步骤执行重采样。例如，值为二表示每隔一个校正步骤执行重采样。值为 `inf` 表示从不执行重采样。

#### 依赖关系

要启用此参数，请将 **系统模型** 选项卡中的 **触发方法** 参数设置为 `Interval`。

#### 编程使用

|  |
| --- |
| **模块参数：**`SamplingInterval` |
| **类型：** positive scalar integer |
| **默认值：**`1` |

#### 随机数生成器选项

### **随机性** — 随机数是否可重复 `'Repeatable'` (默认) | `'Not repeatable'`

随机数是否可重复，指定为 `'Repeatable'` 或 `'Not repeatable'`。如果您希望能够多次生成相同结果，请将 **随机性** 设置为 `'Repeatable'`，并在 **种子** 中指定相同的随机数生成器种子值。

#### 编程使用

|  |
| --- |
| **模块参数：**`Randomness` |
| **类型：** character vector |
| **值：**  `'Repeatable'`, `'Not repeatable'` |
| **默认值：**`'Repeatable'` |

### **种子** — 可重复随机数的种子值 0 (默认) | scalar

可重复随机数的种子值，指定为 scalar。

#### 依赖关系

要启用此参数，请将 **系统模型** 选项卡中的 **随机性** 参数设置为 `'Repeatable'`。

#### 编程使用

|  |
| --- |
| **模块参数：**`Seed` |
| **类型：** scalar |
| **默认值：**`0` |

#### 设置

### **数据类型** — 模块参数的数据类型 `double` (默认) | `single`

使用此参数指定所有模块参数的数据类型。

#### 编程使用

|  |
| --- |
| **模块参数：** `DataType` |
| **类型：** character vector |
| **值：** `'single'`, `'double'` |
| **默认值：** `'double'` |

### **采样时间** — 模块采样时间 `1` (默认) | positive scalar

模块采样时间，指定为 positive scalar。

如果您的状态转移和所有测量似然函数具有相同的采样时间，请使用 **采样时间** 参数。否则，请在 **多速率** 选项卡中选择 **启用多速率操作** 选项，并在同一选项卡中指定采样时间。

#### 依赖关系

要启用此参数，请将 **模块输出、多速率** 选项卡中的 **启用多速率操作** 参数设置为 `off`。

#### 编程使用

|  |
| --- |
| **模块参数：**`SampleTime` |
| **类型：** character vector, string |
| **默认值：**`'1'` |

### 模块输出、多速率选项卡

#### 输出

### **状态估计方法** — 用于从粒子中提取状态估计的方法 `'Mean'` (默认) | `'MaxWeight'` | `'None'`

用于从粒子中提取状态估计的方法，指定为以下之一：

- `'Mean'` — Particle Filter 模块根据参数 **Weights** 和 **Particles**，输出粒子的加权均值作为状态估计。
- `'Maxweight'` — Particle Filter 模块输出具有最高权重的粒子作为状态估计。
- `'None'` — 使用此选项，通过从 **模块输出、多速率** 选项卡中使用 **输出所有粒子** 参数访问所有粒子，以实现自定义状态估计方法。

#### 编程使用

|  |
| --- |
| **模块参数：**`StateEstimationMethod` |
| **类型：** character vector, string |
| **值：**  `'Mean'`, `'MaxWeight'`, `'None'` |
| **默认值：**`'Mean'` |

### **输出所有粒子** — 输出所有粒子 `'off'` (默认) | `'on'`

如果选择此参数，模块中将生成用于估计的粒子的输出端口 **Particles**。

- 如果 `StateOrientation` 参数指定为 `'column'`，则粒子输出为 *Ns*-by-*Np* array。*Ns* 是系统的状态数，*Np* 是粒子数。
- 如果 `StateOrientation` 参数指定为 `'row'`，则粒子输出为 *Np*-by-*Ns* array。

#### 编程使用

|  |
| --- |
| **模块参数：**`OutputParticles` |
| **类型：** character vector |
| **值：**`'off'`, `'on'` |
| **默认值：**`'off'` |

### **输出权重** — 输出粒子权重 `'off'` (默认) | `'on'`

如果选择此参数，模块中将生成用于估计的粒子权重的输出端口 **Weights**。

- 如果 `StateOrientation` 参数指定为 `'column'`，则粒子权重输出为 1-by-*Np* vector。这里，每个权重与 `Particles` array 中同一列的粒子相关联。*Np* 是用于状态估计的粒子数。
- 如果 `StateOrientation` 参数指定为 `'row'`，则粒子权重输出为 *Np*-by-1 vector。

#### 编程使用

|  |
| --- |
| **模块参数：**`OutputWeights` |
| **类型：** character vector |
| **值：**`'off'`, `'on'` |
| **默认值：**`'off'` |

### **输出状态估计误差协方差** — 输出状态估计误差协方差 `'off'` (默认) | `'on'`

如果选择此参数，模块中将生成状态估计误差协方差输出端口 **P**。

#### 依赖关系

要启用此参数，请将 **模块输出、多速率** 选项卡中的 **状态估计方法** 参数设置为 `'Mean'`。

#### 编程使用

|  |
| --- |
| **模块参数：**`OutputStateCovariance` |
| **类型：** character vector |
| **值：**`'off'`, `'on'` |
| **默认值：**`'off'` |

### **使用当前测量值改进状态估计** — 使用当前测量值进行状态估计的选项 `'on'` (默认) | `'off'`

当选中此参数时，模块在时间步 `k` 输出校正状态估计 x^[k|k]，该估计使用截至时间 `k` 的测得输出进行估计。如果清除此参数，模块返回时间 `k` 的预测状态估计 x^[k|k−1]，该估计使用截至前一时刻 `k-1` 的测得输出进行估计。如果您的滤波器位于反馈环路中，并且 Simulink 模型存在代数环，请清除此参数。

#### 编程使用

|  |
| --- |
| **模块参数：**`UseCurrentEstimator` |
| **类型：** character vector |
| **值：**`'on'`, `'off'` |
| **默认值：**`'on'` |

#### 多速率

### **启用多速率操作** — 启用为状态转移和测量似然函数指定不同采样时间 `'off'` (默认) | `'on'`

如果状态转移或任何测量似然函数的采样时间与其余函数不同，请选择此参数。您在 **多速率** 选项卡中的 **采样时间** 中指定采样时间。

#### 编程使用

|  |
| --- |
| **模块参数：**`EnableMultirate` |
| **类型：** character vector |
| **值：**`'off'`, `'on'` |
| **默认值：**`'off'` |

### **采样时间** — 状态转移和测量似然函数采样时间 positive scalar

如果状态转移和测量似然函数的采样时间不同，请指定 **采样时间**。将测量函数的采样时间指定为状态转移采样时间的正整数倍。您指定的采样时间对应于以下输入端口：

- 对应于状态转移函数的端口 — 状态转移函数的额外输入 **StateTransitionFcnInputs**。这些端口的采样时间必须始终等于状态转移函数采样时间，但可以不同于测量似然函数的采样时间。
- 对应于第 *i* 个测量似然函数的端口 — 测得输出 **y*`i`***、测量似然函数的额外输入 **MeasurementLikelihoodFcn*`i`*Inputs**、端口 **Enable*`i`*** 处的使能信号。同一测量似然函数的这些端口的采样时间必须始终相同，但可以不同于状态转移函数和其他测量似然函数的采样时间。

#### 依赖关系

要启用此参数，请将 **模块输出、多速率** 选项卡中的 **启用多速率操作** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数：**`StateTransitionFcnSampleTime`, `MeasurementLikelihoodFcn1SampleTime1`, `MeasurementLikelihoodFcn1SampleTime2`, `MeasurementLikelihoodFcn1SampleTime3`, `MeasurementLikelihoodFcn1SampleTime4`, `MeasurementLikelihoodFcn1SampleTime5` |
| **类型：** character vector, string |
| **默认值：**`'1'` |

## 所属库

Control System Toolbox / State Estimation System Identification Toolbox / Estimators

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

您指定的状态转移和测量似然函数必须仅使用支持代码生成的 MATLAB 命令和 Simulink 模块。有关支持代码生成的模块列表，请参阅 Blocks Supported for Code Generation (Simulink Coder)。有关支持代码生成的命令列表，请参阅 Functions and Objects Supported for C/C++ Code Generation (MATLAB Coder)。

## 版本历史

**在 R2018a 中引入**

## 描述

使用粒子滤波器估计离散时间非线性系统的状态

Particle Filter 模块使用离散时间粒子滤波算法估计离散时间非线性系统的状态。

考虑一个具有状态 *x*、输入 *u*、输出 *m*、过程噪声 *w* 和测量 *y* 的被控对象。假设您可以将该被控对象表示为非线性系统。

该算法使用您指定的状态转移和测量似然函数计算非线性系统的状态估计 x^。

您为系统创建非线性状态转移函数和测量似然函数，并在模块中指定这些函数。该模块支持对具有以不同采样率运行的多个传感器的系统进行状态估计。最多可以指定五个测量似然函数，每个函数对应于系统中的一个传感器。
