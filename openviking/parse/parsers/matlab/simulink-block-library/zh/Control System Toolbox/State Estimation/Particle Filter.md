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
```yaml
ports:
- name: y1,y2,y3,y4,y5
  summary: 测量的系统输出向量
  direction: input
- name: StateTransitionFcnInputs
  summary: 状态转移函数的可选输入参数 标量 | 向量 | 矩阵
  direction: input
- name: MeasurementLikelihoodFcn1Inputs,...,MeasurementLikelihoodFcn5Inputs
  summary: 每个测量似然函数的可选输入参数 标量 | 向量 | 矩阵
  direction: input
- name: Enable1,Enable2,Enable3,Enable4,Enable5
  summary: 在有测量数据时启用估计状态的校正 标量
  direction: input
- name: xhat
  summary: 估计状态 向量
  direction: output
- name: P
  summary: 状态估计误差协方差矩阵
  direction: output
- name: Particles
  summary: 用于状态估计的粒子值 数组
  direction: output
- name: Weights
  summary: 用于状态估计的粒子权重 向量
  direction: output
```

### 输入

### **y1,y2,y3,y4,y5** — 测量的系统输出向量

与您在模块中指定的每个测量似然函数相对应的测量系统输出。端口数量等于系统中的测量似然函数数量。您最多可以指定五个测量似然函数。例如，如果您的系统有两个传感器，则在模块中指定两个测量似然函数。第一个端口 **y1** 默认可用。点击 **Add Measurement**，生成与第二个测量似然函数相对应的端口 **y2**。

将端口指定为 *N* 维向量，其中 *N* 是相应传感器测量的量数。例如，如果您的系统有一个传感器测量物体的位置和速度，则只有一个端口 **y1**。该端口被指定为二维向量，其值对应于位置和速度。

#### 依赖关系

第一个端口 **y1** 默认可用。要生成端口 **y2** 到 **y5**，请点击 **Add Measurement**。

### **StateTransitionFcnInputs** — 状态转移函数的可选输入参数 标量 | 向量 | 矩阵

状态转移函数 `f` 中除状态 `x` 之外的可选输入参数。

如果您使用 MATLAB® 函数（`.m` 文件）创建 `f`，则当您输入函数名称并点击 **Apply** 时，软件会生成端口 **StateTransitionFcnInputs**。

如果您的状态转移函数有多个附加输入，请使用 Simulink Function (Simulink) 模块来指定该函数。当您使用 Simulink Function 模块时，您通过 Inport (Simulink) 模块直接向 Simulink Function 模块提供附加输入。Particle Filter 模块中不会为附加输入生成输入端口。

#### 依赖关系

要生成此端口，必须同时满足以下两个条件：

- 您在 **Function** 中使用 MATLAB 函数指定 `f`，且 `f` 在 MATLAB 路径上。
- `f` 除粒子外仅需要一个附加输入参数。

### **MeasurementLikelihoodFcn1Inputs,...,MeasurementLikelihoodFcn5Inputs** — 每个测量似然函数的可选输入参数 标量 | 向量 | 矩阵

测量似然函数中除状态 `x` 和测量 `y` 之外的可选输入。

**MeasurementLikelihoodFcn1Inputs** 对应于您指定的第一个测量似然函数，依此类推。

如果您在 **Function** 中使用 MATLAB 函数（`.m` 文件）指定两个测量输入，则当您点击 **Apply** 时，软件会生成端口 **MeasurementLikelihoodFcn1Inputs** 和 **MeasurementLikelihoodFcn2Inputs**。您可以将这些端口的输入指定为标量、向量或矩阵。

如果您的测量似然函数有多个附加输入，请使用 Simulink Function (Simulink) 模块来指定这些函数。当您使用 Simulink Function 模块时，您通过 Inport (Simulink) 模块直接向 Simulink Function 模块提供附加输入。Particle Filter 模块中不会为附加输入生成输入端口。

#### 依赖关系

要生成与测量似然函数 `h` 相对应的端口，必须同时满足以下两个条件：

- 您在 **Function** 中使用 MATLAB 函数指定测量输入 `h`，且 `h` 在 MATLAB 路径上。
- `h` 除粒子和测量外仅需要一个附加输入参数。

### **Enable1,Enable2,Enable3,Enable4,Enable5** — 在有测量数据时启用估计状态的校正 标量

在有测量数据时启用估计状态的校正。

例如，假设在对应于第一个测量似然函数的端口 **y1** 处，并非所有时间点都有测量输出数据。然后，在 **Enable1** 端口使用非 `0` 的信号值，以在有测量数据时启用估计状态的校正。当没有测量数据时，将端口值指定为 `0`。类似地，如果在第 *i* 个测量似然函数的端口 **y*`i`*** 处并非所有时间点都有测量输出数据，则将相应的端口 **Enable*`i`*** 指定为非 `0` 的值。

#### 依赖关系

要生成与测量似然函数相对应的端口，请为该测量似然函数选择 **Add Enable port**。点击 **Apply** 后该端口会出现。
### 输出

### **xhat** — 估计状态 向量

估计状态，以大小为 *Ns* 的向量返回，其中 *Ns* 是系统的状态数。要访问各个状态，请使用 Selector (Simulink) 模块。

当选中 **Use the current measurements to improve state estimates** 参数时，模块输出时间步 `k` 处的校正状态估计 x^[k|k]，该估计使用截至时间 `k` 的测量输出进行估计。如果您清除此参数，模块返回时间 `k` 的预测状态估计 x^[k|k−1]，该估计使用截至先前时间 `k-1` 的测量输出进行估计。如果您的滤波器处于反馈环路中且 Simulink® 模型中存在代数环，请清除此参数。

### **P** — 状态估计误差协方差矩阵

状态估计误差协方差，以 *Ns*×*Ns* 矩阵返回，其中 *Ns* 是系统的状态数。要访问各个协方差，请使用 Selector (Simulink) 模块。

只有在 **Block outputs, Multirate** 选项卡中选中 **Output state estimation error covariance** 并点击 **Apply** 时，才能输出误差协方差。

#### 依赖关系

要启用此参数，请将 **Block outputs, Multirate** 选项卡中的 **State estimation method** 参数设置为 `'Mean'`。

### **Particles** — 用于状态估计的粒子值 数组

用于状态估计的粒子值，以 *Ns*×*Np* 或 *Np*×*Ns* 数组返回。*Ns* 是系统的状态数，*Np* 是粒子数。

- 如果 `StateOrientation` 参数指定为 `'column'`，则 **Particles** 以 *Ns*×*Np* 数组返回。
- 如果 `StateOrientation` 参数指定为 `'row'`，则 **Particles** 以 *Np*×*Ns* 数组返回。

#### 依赖关系

要生成此端口，请在 **Block outputs, Multirate** 选项卡中选中 **Output all particles**，然后点击 **Apply**。

### **Weights** — 用于状态估计的粒子权重 向量

用于状态估计的粒子权重，以 1×*Np* 或 *Np*×1 向量返回，其中 *Np* 是用于状态估计的粒子数。

- 如果 `StateOrientation` 参数指定为 `'column'`，则 **Weights** 以 1×*Np* 向量返回，其中每个权重与 `Particles` 数组中同一列的粒子相关联。
- 如果 `StateOrientation` 参数指定为 `'row'`，则 **Weights** 以 *Np*×1 向量返回，其中每个权重与 `Particles` 数组中同一行的粒子相关联。

#### 依赖关系

要生成此端口，请在 **Block outputs, Multirate** 选项卡中选中 **Output weights**，然后点击 **Apply**。
## 参数
```yaml
parameters:
- name: Function
  summary: 状态转移函数名称 'vdpParticleFilterStateFcn'（默认）| 函数名称
  group: 系统模型选项卡
  block_parameter: StateTransitionFcn
  type: 字符向量、字符串
  default: '''vdpParticleFilterStateFcn'''
- name: Number of Particles
  summary: 滤波器中使用的粒子数 1000（默认）| 正标量整数
  group: 系统模型选项卡
  block_parameter: NumberOfParticles
  type: 正标量整数
  default: '1000'
- name: Distribution
  summary: 粒子的初始分布 'Gaussian'（默认）| 'Uniform' | 'Custom'
  group: 系统模型选项卡
  block_parameter: InitialDistribution
  type: 字符向量
  values: '''Gaussian''、''Uniform''、''Custom'''
  default: '''Gaussian'''
- name: Mean
  summary: 粒子的初始均值 [0;0]（默认）| 向量
  group: 系统模型选项卡
  block_parameter: InitialMean
  type: 数组
  default: '[0,0]'
- name: Covariance
  summary: 粒子的初始协方差 1（默认）| 标量 | 向量 | 矩阵
  group: 系统模型选项卡
  block_parameter: InitialCovariance
  type: 标量、向量或矩阵
  default: '1'
- name: Circular Variables
  summary: 用于状态估计的循环变量 0（默认）| 标量 | 向量
  group: 系统模型选项卡
  block_parameter: CircularVariables
  type: 标量、向量
  default: '0'
- name: State Orientation
  summary: 输入系统状态的方向 'column'（默认）| 'row'
  group: 系统模型选项卡
  block_parameter: StateOrientation
  type: 字符向量
  values: '''column''、''row'''
  default: '''column'''
- name: State bounds
  summary: 系统状态的初始边界 [-3 3;-3 3]（默认）| 数组
  group: 系统模型选项卡
  block_parameter: InitialStateBounds
  type: 数组
  default: '[-3 3;-3 3]'
- name: Particles
  summary: 用于状态估计的自定义粒子分布 []（默认）| 数组
  group: 系统模型选项卡
  block_parameter: InitialParticles
  type: 数组
  default: '[]'
- name: Weights
  summary: 用于状态估计的自定义粒子权重值 []（默认）| 正值向量
  group: 系统模型选项卡
  block_parameter: InitialWeights
  type: 正值向量
  default: '[]'
- name: Function
  summary: 测量似然函数名称 'vdpMeasurementLikelihoodFcn'（默认）| 函数名称
  group: 系统模型选项卡
  block_parameter: MeasurementLikelihoodFcn1, MeasurementLikelihoodFcn2, MeasurementLikelihoodFcn3, MeasurementLikelihoodFcn4,
    MeasurementLikelihoodFcn5
  type: character vector, string
  default: '''vdpMeasurementLikelihoodFcn'''
- name: Add Enable Port
  summary: 仅在测量数据可用时启用估计状态的校正 off（默认）| on
  group: 系统模型选项卡
  block_parameter: HasMeasurementEnablePort1, HasMeasurementEnablePort2, HasMeasurementEnablePort3, HasMeasurementEnablePort4,
    HasMeasurementEnablePort5
  type: character vector
  values: '''off'', ''on'''
  default: '''off'''
- name: Resampling method
  summary: 用于粒子重采样的方法 'Multinomial'（默认）| 'Systemic' | 'Stratified'
  group: 系统模型选项卡
  block_parameter: ResamplingMethod
  type: character vector
  values: '''Multinomial'', ''Systemic'', ''Stratified'''
  default: '''Multinomial'''
- name: Trigger method
  summary: 确定何时进行重采样的方法 'Ratio'（默认）| 'Interval'
  group: 系统模型选项卡
  block_parameter: TriggerMethod
  type: character vector
  values: '''Ratio'', ''Interval'''
  default: '''Ratio'''
- name: Minimum effective particle ratio
  summary: 有效粒子数与总粒子数的最小期望比率 0.5（默认）| 正标量
  group: 系统模型选项卡
  block_parameter: MinEffectiveParticleRatio
  type: scalar
  values: Range [0,1]
  default: '0.5'
- name: Sampling Interval
  summary: 重采样之间的固定间隔 1（默认）| 正标量整数
  group: 系统模型选项卡
  block_parameter: SamplingInterval
  type: positive scalar integer
  default: '1'
- name: Randomness
  summary: 随机数是否可重复 'Repeatable'（默认）| 'Not repeatable'
  group: 系统模型选项卡
  block_parameter: Randomness
  type: character vector
  values: '''Repeatable'', ''Not repeatable'''
  default: '''Repeatable'''
- name: Seed
  summary: 可重复随机数的种子值 0（默认）| 标量
  group: 系统模型选项卡
  block_parameter: Seed
  type: scalar
  default: '0'
- name: Data type
  summary: 模块参数的数据类型 double（默认）| single
  group: 系统模型选项卡
  block_parameter: DataType
  type: character vector
  values: '''single'', ''double'''
  default: '''double'''
- name: Sample time
  summary: 模块采样时间 1（默认）| 正标量
  group: 系统模型选项卡
  block_parameter: SampleTime
  type: character vector, string
  default: '''1'''
- name: State Estimation Method
  summary: 用于从粒子中提取状态估计的方法 'Mean'（默认）| 'MaxWeight' | 'None'
  group: Block Outputs, Multirate Tab
  block_parameter: StateEstimationMethod
  type: character vector, string
  values: '''Mean'', ''MaxWeight'', ''None'''
  default: '''Mean'''
- name: Output all particles
  summary: 输出所有粒子 'off'（默认）| 'on'
  group: Block Outputs, Multirate Tab
  block_parameter: OutputParticles
  type: character vector
  values: '''off'', ''on'''
  default: '''off'''
- name: Output weights
  summary: 输出粒子权重 'off'（默认）| 'on'
  group: Block Outputs, Multirate Tab
  block_parameter: OutputWeights
  type: character vector
  values: '''off'', ''on'''
  default: '''off'''
- name: Output state estimation error covariance
  summary: 输出状态估计误差协方差 'off'（默认）| 'on'
  group: Block Outputs, Multirate Tab
  block_parameter: OutputStateCovariance
  type: character vector
  values: '''off'', ''on'''
  default: '''off'''
- name: Use the current measurements to improve state estimates
  summary: 使用当前测量值进行状态估计的选项 'on'（默认）| 'off'
  group: Block Outputs, Multirate Tab
  block_parameter: UseCurrentEstimator
  type: character vector
  values: '''on'', ''off'''
  default: '''on'''
- name: Enable multirate operation
  summary: 启用为状态转移和测量似然函数指定不同的采样时间 'off'（默认）| 'on'
  group: Block Outputs, Multirate Tab
  block_parameter: EnableMultirate
  type: character vector
  values: '''off'', ''on'''
  default: '''off'''
- name: Sample times
  summary: 状态转移和测量似然函数采样时间 正标量
  group: Block Outputs, Multirate Tab
  block_parameter: StateTransitionFcnSampleTime, MeasurementLikelihoodFcn1SampleTime1, MeasurementLikelihoodFcn1SampleTime2,
    MeasurementLikelihoodFcn1SampleTime3, MeasurementLikelihoodFcn1SampleTime4, MeasurementLikelihoodFcn1SampleTime5
  type: character vector, string
  default: '''1'''
```

### 系统模型选项卡

#### 状态转移

### **Function** — 状态转移函数名称 `'vdpParticleFilterStateFcn'`（默认）| 函数名称

粒子滤波器状态转移函数根据系统的动态特性和过程噪声，在给定时间步 *k* 的粒子的情况下，计算时间步 *k+1* 的粒子。此函数的语法为：

```
particlesNext = f(particles, param1, param2, ...)
```

其中，如果 **State Orientation** 指定为 `'column'`，则 *particles* 和 *particlesNext* 的维度为 *Ns*×*Np*；如果 **State Orientation** 指定为 `'row'`，则维度为 *Np*×*Ns*。此外，`param_i` 表示您可以指定的可选输入参数。有关可选输入参数的更多信息，请参阅 StateTransitionFcnInputs。

您创建状态转移函数并在 **Function** 中指定函数名称。例如，如果 `vdpParticleFilterStateFcn.m` 是您创建并保存的状态转移函数，则将 **Function** 指定为 `'vdpParticleFilterStateFcn'`。

您可以使用 Simulink Function (Simulink) 模块或 MATLAB 函数（`.m` 文件）创建 **Function**。

#### 编程用法

|  |
| --- |
| **模块参数：**`StateTransitionFcn` |
| **类型：**字符向量、字符串 |
| **默认值：**`'vdpParticleFilterStateFcn'` |

#### 初始化

### **Number of Particles** — 滤波器中使用的粒子数 1000（默认）| 正标量整数

滤波器中使用的粒子数，指定为正标量整数。每个粒子代表系统中的一个状态假设。粒子数越多，状态估计精度越高，但运行滤波器所需的计算量也越大。

#### 编程用法

|  |
| --- |
| **模块参数：**`NumberOfParticles` |
| **类型：**正标量整数 |
| **默认值：**`1000` |

### **Distribution** — 粒子的初始分布 `'Gaussian'`（默认）| `'Uniform'` | `'Custom'`

粒子的初始分布，指定为 `'Gaussian'`、`'Uniform'` 或 `'Custom'`。

如果选择 `'Gaussian'`，初始粒子集或状态假设按照多元高斯分布分布，您需要指定 **Mean** 和 **Covariance**。所有粒子的初始权重假定相等。

如果选择 `'Uniform'`，初始粒子集按照均匀分布分布，您需要指定 **State bounds** 的上界和下界。所有粒子的初始权重假定相等。

`'Custom'` 允许您指定自己的初始粒子集及其权重。您可以使用任意概率分布来初始化滤波器的 **Particles** 和 **Weights**。

#### 编程用法

|  |
| --- |
| **模块参数：**`InitialDistribution` |
| **类型：**字符向量 |
| **值：**`'Gaussian'`、`'Uniform'`、`'Custom'` |
| **默认值：**`'Gaussian'` |

### **Mean** — 粒子的初始均值 [0;0]（默认）| 向量

粒子的初始均值，指定为向量。要估计的状态数决定了向量的长度。

#### 依赖关系

要启用此参数，请将 **System model** 选项卡中的 **Distribution** 参数设置为 `Gaussian`。

#### 编程用法

|  |
| --- |
| **模块参数：**`InitialMean` |
| **类型：**数组 |
| **默认值：**`[0,0]` |

### **Covariance** — 粒子的初始协方差 1（默认）| 标量 | 向量 | 矩阵

粒子的初始协方差，指定为标量、向量或矩阵。

如果 **Covariance** 指定为：

- 标量，则它必须为正。协方差假定为 [*Ns* *Ns*] 矩阵，对角线元素为该标量。此处，*Ns* 是状态数。
- 向量，则每个元素必须为正。协方差假定为 [*Ns* *Ns*] 矩阵，对角线元素为向量的元素。
- 矩阵，则它必须是半正定的。

#### 依赖关系

要启用此参数，请将 **System model** 选项卡中的 **Distribution** 参数设置为 `Gaussian`。

#### 编程用法

|  |
| --- |
| **模块参数：**`InitialCovariance` |
| **类型：**标量、向量或矩阵 |
| **默认值：**`1` |

### **Circular Variables** — 用于状态估计的循环变量 0（默认）| 标量 | 向量

用于状态估计的循环变量，指定为标量或 *Ns* 元素向量，其中 *Ns* 是状态数。

如果 **Circular Variables** 指定为标量，软件将其扩展为每个元素都等于该标量的向量。循环（或角度）分布使用范围为 [`-π` `π`] 的概率密度函数。如果系统中的某些状态表示角度量（如物体的方向），请使用循环变量。

#### 编程用法

|  |
| --- |
| **模块参数：**`CircularVariables` |
| **类型：**标量、向量 |
| **默认值：**`0` |

### **State Orientation** — 输入系统状态的方向 `'column'`（默认）| `'row'`

系统状态的方向，指定为 `'column'` 或 `'row'`。

如果 **State Orientation** 指定为：

- `'column'`，则状态转移和测量似然函数的第一个输入参数为 [*Ns* *Np*]。在这种情况下，此矩阵的第 *i* 列是第 *i* 个粒子（状态假设）。此外，状态估计 **xhat** 输出为 [*Ns* 1] 向量。此处，*Ns* 是状态数，*Np* 是粒子数。
- `'row'`，则状态转移和测量似然函数的第一个输入参数为 [*Np* *Ns*]，此矩阵的每一行包含一个粒子。此外，状态估计 **xhat** 输出为 [1 *Ns*] 向量。

#### 编程用法

|  |
| --- |
| **模块参数：**`StateOrientation` |
| **类型：**字符向量 |
| **值：**`'column'`、`'row'` |
| **默认值：**`'column'` |

### **State bounds** — 系统状态的初始边界 [-3 3;-3 3]（默认）| 数组

系统状态的初始边界，指定为 *Ns*×2 数组，其中 *Ns* 是状态数。

第 *i* 行列出了第 *i* 个状态的粒子初始分布的均匀分布的下界和上界。

#### 依赖关系

要启用此参数，请将 **System model** 选项卡中的 **Distribution** 参数设置为 `Uniform`。

#### 编程用法

|  |
| --- |
| **模块参数：**`InitialStateBounds` |
| **类型：**数组 |
| **默认值：** `[-3 3;-3 3]` |

### **Particles** — 用于状态估计的自定义粒子分布 []（默认）| 数组

用于状态估计的自定义粒子分布，指定为 *Ns*×*Np* 或 *Np*×*Ns* 数组。*Ns* 是系统的状态数，*Np* 是粒子数。

您选择一个分布，使用 `makedist` 函数为其创建概率分布对象，并使用 `random` 函数生成所需分布的粒子。

- 如果 `StateOrientation` 参数为 `'column'`，则将 **Particles** 指定为 *Ns*×*Np* 数组。

  例如，

  ```
  pd = makedist('Poisson');
  Particles = random(pd,Ns,Np);
  ```
- 如果 `StateOrientation` 参数为 `'row'`，则将 **Particles** 指定为 *Np*×*Ns* 数组。

  例如，

  ```
  pd = makedist('Poisson');
  Particles = random(pd,Np,Ns);
  ```

#### 依赖关系

要启用此参数，请将 **System model** 选项卡中的 **Distribution** 参数设置为 `Custom`。

#### 编程用法

|  |
| --- |
| **模块参数：**`InitialParticles` |
| **类型：**数组 |
| **默认值：**`[]` |

### **Weights** — 用于状态估计的自定义粒子权重值 []（默认）| 正值向量

用于状态估计的自定义粒子权重值，指定为 1×*Np* 或 *Np*×1 正值向量，其中 *Np* 是用于状态估计的粒子数。

- 如果 `StateOrientation` 参数为 `'column'`，则将 **Weights** 指定为 1×*Np* 向量。向量中的每个权重与 `Particles` 数组中同一列的粒子相关联。

  例如，

  ```
  Weights = ones(1,Np)/Np;
  ```
- 如果 `StateOrientation` 参数为 `'row'`，则将 **Weights** 指定为 *Np*×1 向量。向量中的每个权重与 `Particles` 数组中同一行的粒子相关联。

  例如，

  ```
  Weights = ones(Np,1)/Np;
  ```

#### 依赖关系

要启用此参数，请将 **System model** 选项卡中的 **Distribution** 参数设置为 `Custom`。

#### 编程用法

|  |
| --- |
| **模块参数：**`InitialWeights` |
| **类型：**正值向量 |
| **默认值：**`[]` |

#### 测量

### **Function** — 测量似然函数名称 `'vdpMeasurementLikelihoodFcn'`（默认）| 函数名称

测量似然函数使用传感器测量值计算粒子（状态假设）的似然度。对于每个状态假设（粒子），该函数首先计算一个 *Nm* 元素的测量假设向量。然后，基于传感器测量值和测量噪声概率分布计算每个测量假设的似然度。该函数的语法为：

```
likelihood = h(particles, measurement, param1, param2, ...)
```

其中，*likelihood* 是一个 *Np* 元素的向量，*Np* 是粒子数。如果 **State Orientation** 指定为 `'column'`，则 *particles* 的维度为 *Ns*×*Np*；如果 **State Orientation** 指定为 `'row'`，则维度为 *Np*×*Ns*。*measurement* 是一个 *Nm* 元素的向量，其中 *Nm* 是传感器提供的测量值数量。*param\_i* 表示您可以指定的可选输入参数。有关可选输入参数的详细信息，请参阅 MeasurementLikelihoodFcn1Inputs,...,MeasurementLikelihoodFcn5Inputs。

您创建测量似然函数并在 **Function** 中指定函数名称。例如，如果 `vdpMeasurementLikelihoodFcn.m` 是您创建并保存的测量似然函数，请将 **Function** 指定为 `'vdpMeasurementLikelihoodFcn'`。

您可以使用 Simulink Function (Simulink) 模块或 MATLAB 函数（`.m` 文件）创建 **Function**。

- 仅当 *h* 除了 **Particles** 和 **Measurement** 之外具有零个或一个额外输入参数 `param_i` 时，您才能使用 MATLAB 函数。

  软件会生成一个额外的输入端口 **MeasurementLikelihoodFcn*`i`*Inputs**，用于为第 *i* 个测量似然函数指定此参数，然后单击 **Apply**。
- 如果您使用 Simulink Function 模块，请在 Simulink Function 模块中使用 Argument Inport (Simulink) 模块指定 `x` 和 `y`，并使用 Inport (Simulink) 模块指定额外输入 `param_i`。您不需要向 Particle Filter 模块提供 `param_i`。

如果系统中有多个传感器，您可以指定多个测量似然函数。您可以使用 **Add Measurement** 按钮指定最多五个测量似然函数。要删除测量似然函数，请使用 **Remove Measurement**。

#### 编程使用

|  |
| --- |
| **模块参数**：`MeasurementLikelihoodFcn1`, `MeasurementLikelihoodFcn2`, `MeasurementLikelihoodFcn3`, `MeasurementLikelihoodFcn4`, `MeasurementLikelihoodFcn5` |
| **类型**：character vector, string |
| **默认值**：`'vdpMeasurementLikelihoodFcn'` |

### **Add Enable Port** — 仅在测量数据可用时启用估计状态的校正 `off`（默认）| `on`

假设在对应于第一个测量似然函数的端口 **y1** 处，测量输出数据并非在所有时间点都可用。要生成输入端口 **Enable1**，请选择 **Add Enable port**。在此端口使用信号，仅在测量数据可用时启用估计状态的校正。类似地，如果对于第 *i* 个测量似然函数，在端口 **y*`i`*** 处测量输出数据并非在所有时间点都可用，请选择相应的 **Add Enable port**。

#### 编程使用

|  |
| --- |
| **模块参数**：`HasMeasurementEnablePort1`, `HasMeasurementEnablePort2`, `HasMeasurementEnablePort3`, `HasMeasurementEnablePort4`, `HasMeasurementEnablePort5` |
| **类型**：character vector |
| **值**：`'off'`, `'on'` |
| **默认值**：`'off'` |

#### Resampling

### **Resampling method** — 用于粒子重采样的方法 `'Multinomial'`（默认）| `'Systemic'` | `'Stratified'`

用于粒子重采样的方法，指定为以下之一：

- `'Multinomial'` — 多项式重采样，也称为简化随机采样，从开区间 `(0,1)` 上的均匀分布独立生成 `N` 个随机数，并使用它们按权重比例选择粒子。
- `'Stratified'` — 分层重采样将整个粒子群体划分为称为层的子集。它预先将 `(0,1)` 区间划分为 `N` 个大小为 `1/N` 的不相交子区间。在每个子区间中独立抽取随机数，并在各层中选择样本索引。
- `'Systematic'` — 系统重采样与分层重采样类似，也利用了分层。一个区别是它仅从开区间 `(0,1/N)` 中抽取一个随机数，其余样本点以固定的 `1/N` 步长确定性计算。

#### 编程使用

|  |
| --- |
| **模块参数**：`ResamplingMethod` |
| **类型**：character vector |
| **值**：`'Multinomial'`, `'Systemic'`, `'Stratified'` |
| **默认值**：`'Multinomial'` |

### **Trigger method** — 确定何时进行重采样的方法 `'Ratio'`（默认）| `'Interval'`

确定何时进行重采样的方法，指定为 `'Ratio'` 或 `'Interval'`。`'Ratio'` 值基于有效总粒子比率触发重采样。`'Interval'` 值在粒子滤波器操作的固定时间步长触发重采样。

#### 编程使用

|  |
| --- |
| **模块参数**：`TriggerMethod` |
| **类型**：character vector |
| **值**：`'Ratio'`, `'Interval'` |
| **默认值**：`'Ratio'` |

### **Minimum effective particle ratio** — 有效粒子数与总粒子数的最小期望比率 0.5（默认）| 正标量

有效粒子数与总粒子数的最小期望比率，指定为正标量。有效粒子数是衡量当前粒子集对后验分布近似程度的指标。较低的有效粒子比率意味着贡献于估计的粒子数较少，需要进行重采样。

如果有效粒子数与总粒子数的比率低于最小有效粒子比率，则触发重采样步骤。

将最小有效粒子比率指定为 0 到 1 之间的任意值。

#### 依赖关系

要启用此参数，请将 **System model** 选项卡中的 **Trigger method** 参数设置为 `Ratio`。

#### 编程使用

|  |
| --- |
| **模块参数**：`MinEffectiveParticleRatio` |
| **类型**：scalar |
| **值**：Range `[0,1]` |
| **默认值**：`0.5` |

### **Sampling Interval** — 重采样之间的固定间隔 1（默认）| 正标量整数

重采样之间的固定间隔，指定为正标量整数。采样间隔决定在哪些校正步骤中执行重采样。例如，值为 2 表示每第二个校正步骤执行一次重采样。值为 `inf` 表示从不执行重采样。

#### 依赖关系

要启用此参数，请将 **System model** 选项卡中的 **Trigger method** 参数设置为 `Interval`。

#### 编程使用

|  |
| --- |
| **模块参数**：`SamplingInterval` |
| **类型**：positive scalar integer |
| **默认值**：`1` |

#### Random Number Generator Options

### **Randomness** — 随机数是否可重复 `'Repeatable'`（默认）| `'Not repeatable'`

随机数是否可重复，指定为 `'Repeatable'` 或 `'Not repeatable'`。如果您希望能够多次产生相同的结果，请将 **Randomness** 设置为 `'Repeatable'`，并在 **Seed** 中指定相同的随机数生成器种子值。

#### 编程使用

|  |
| --- |
| **模块参数**：`Randomness` |
| **类型**：character vector |
| **值**：`'Repeatable'`, `'Not repeatable'` |
| **默认值**：`'Repeatable'` |

### **Seed** — 可重复随机数的种子值 0（默认）| 标量

可重复随机数的种子值，指定为标量。

#### 依赖关系

要启用此参数，请将 **System model** 选项卡中的 **Randomness** 参数设置为 `'Repeatable'`。

#### 编程使用

|  |
| --- |
| **模块参数**：`Seed` |
| **类型**：scalar |
| **默认值**：`0` |

#### Settings

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

模块采样时间，指定为正标量。

如果您的状态转移函数和所有测量似然函数具有相同的采样时间，请使用 **Sample time** 参数。否则，请在 **Multirate** 选项卡中选择 **Enable multirate operation** 选项，并在同一选项卡中指定采样时间。

#### 依赖关系

要启用此参数，请将 **Block output, Multirate** 选项卡中的 **Enable multirate operation** 参数设置为 `off`。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：character vector, string |
| **默认值**：`'1'` |

### Block Outputs, Multirate Tab

#### 输出

### **State Estimation Method** — 用于从粒子中提取状态估计的方法 `'Mean'`（默认）| `'MaxWeight'` | `'None'`

用于从粒子中提取状态估计的方法，指定为以下之一：

- `'Mean'` — Particle Filter 模块根据参数 **Weights** 和 **Particles** 输出粒子的加权均值作为状态估计。
- `'Maxweight'` — Particle Filter 模块输出权重最高的粒子作为状态估计。
- `'None'` — 使用此选项可通过 **Block outputs, Multirate** 选项卡中的 **Output all particles** 参数访问所有粒子来实现自定义状态估计方法。

#### 编程使用

|  |
| --- |
| **模块参数**：`StateEstimationMethod` |
| **类型**：character vector, string |
| **值**：`'Mean'`, `'MaxWeight'`, `'None'` |
| **默认值**：`'Mean'` |

### **Output all particles** — 输出所有粒子 `'off'`（默认）| `'on'`

如果选择此参数，模块中将生成用于估计的粒子的输出端口 **Particles**。

- 如果 `StateOrientation` 参数指定为 `'column'`，则粒子输出为 *Ns*×*Np* 数组。*Ns* 是系统的状态数，*Np* 是粒子数。
- 如果 `StateOrientation` 参数指定为 `'row'`，则粒子输出为 *Np*×*Ns* 数组。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputParticles` |
| **类型**：character vector |
| **值**：`'off'`, `'on'` |
| **默认值**：`'off'` |

### **Output weights** — 输出粒子权重 `'off'`（默认）| `'on'`

如果选择此参数，模块中将生成用于估计的粒子权重的输出端口 **Weights**。

- 如果 `StateOrientation` 参数指定为 `'column'`，则粒子权重输出为 1×*Np* 向量。此处，每个权重与 `Particles` 数组中同一列的粒子相关联。*Np* 是用于状态估计的粒子数。
- 如果 `StateOrientation` 参数指定为 `'row'`，则粒子权重输出为 *Np*×1 向量。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputWeights` |
| **类型**：character vector |
| **值**：`'off'`, `'on'` |
| **默认值**：`'off'` |

### **Output state estimation error covariance** — 输出状态估计误差协方差 `'off'`（默认）| `'on'`

如果选择此参数，模块中将生成状态估计误差协方差输出端口 **P**。

#### 依赖关系

要启用此参数，请将 **Block outputs, Multirate** 选项卡中的 **State estimation method** 参数设置为 `'Mean'`。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputStateCovariance` |
| **类型**：character vector |
| **值**：`'off'`, `'on'` |
| **默认值**：`'off'` |

### **Use the current measurements to improve state estimates** — 使用当前测量值进行状态估计的选项 `'on'`（默认）| `'off'`

当选择此参数时，模块在时间步 `k` 输出校正后的状态估计 x^[k|k]，该估计使用截至时间 `k` 的测量输出进行估计。如果清除此参数，模块返回时间 `k` 的预测状态估计 x^[k|k−1]，该估计使用截至先前时间 `k-1` 的测量输出进行估计。如果您的滤波器处于反馈回路中且 Simulink 模型中存在代数环，请清除此参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`UseCurrentEstimator` |
| **类型**：character vector |
| **值**：`'on'`, `'off'` |
| **默认值**：`'on'` |

#### Multirate

### **Enable multirate operation** — 启用为状态转移和测量似然函数指定不同的采样时间 `'off'`（默认）| `'on'`

如果状态转移函数或任何测量似然函数的采样时间与其他函数不同，请选择此参数。您在 **Multirate** 选项卡的 **Sample time** 中指定采样时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`EnableMultirate` |
| **类型**：character vector |
| **值**：`'off'`, `'on'` |
| **默认值**：`'off'` |

### **Sample times** — 状态转移和测量似然函数采样时间 正标量

如果状态转移和测量似然函数的采样时间不同，请指定 **Sample time**。将测量函数的采样时间指定为状态转移采样时间的正整数倍。您指定的采样时间对应于以下输入端口：

- 对应于状态转移函数的端口 — 状态转移函数的额外输入 **StateTransitionFcnInputs**。这些端口的采样时间必须始终等于状态转移函数采样时间，但可以与测量似然函数的采样时间不同。
- 对应于第 *i* 个测量似然函数的端口 — 测量输出 **y*`i`***，测量似然函数的额外输入 **MeasurementLikelihoodFcn*`i`*Inputs**，端口 **Enable*`i`*** 处的使能信号。同一测量似然函数的这些端口的采样时间必须始终相同，但可以与状态转移函数和其他测量似然函数的采样时间不同。

#### 依赖关系

要启用此参数，请将 **Block outputs, Multirate** 选项卡中的 **Enable multirate operation** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数**：`StateTransitionFcnSampleTime`, `MeasurementLikelihoodFcn1SampleTime1`, `MeasurementLikelihoodFcn1SampleTime2`, `MeasurementLikelihoodFcn1SampleTime3`, `MeasurementLikelihoodFcn1SampleTime4`, `MeasurementLikelihoodFcn1SampleTime5` |
| **类型**：character vector, string |
| **默认值**：`'1'` |
## 所属库

Control System Toolbox / State Estimation System Identification Toolbox / Estimators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

您指定的状态转移和测量似然函数必须仅使用支持代码生成的 MATLAB 命令和 Simulink 模块。有关支持代码生成的模块列表，请参阅 Blocks Supported for Code Generation (Simulink Coder)。有关支持代码生成的命令列表，请参阅 Functions and Objects Supported for C/C++ Code Generation (MATLAB Coder)。

## 版本历史

**在 R2018a 中引入**

## 描述

使用粒子滤波器估计离散时间非线性系统的状态

粒子滤波器模块使用离散时间粒子滤波算法估计离散时间非线性系统的状态。

考虑一个具有状态 *x*、输入 *u*、输出 *m*、过程噪声 *w* 和测量 *y* 的被控对象。假设您可以将该被控对象表示为非线性系统。

该算法使用您指定的状态转移函数和测量似然函数来计算非线性系统的状态估计 x^。

您为系统创建非线性状态转移函数和测量似然函数，并在模块中指定这些函数。该模块支持对具有多个以不同采样率运行的传感器的系统进行状态估计。您最多可以指定五个测量似然函数，每个函数对应系统中的一个传感器。
