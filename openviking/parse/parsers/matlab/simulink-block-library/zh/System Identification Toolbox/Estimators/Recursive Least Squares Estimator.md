---
type: simulink-block
title: 'Recursive Least Squares Estimator'
family: 'ident'
product_id: 'ident'
product_name: 'System Identification Toolbox'
documentation_release: R2025b
official_category: 'Estimators'
documentation_page: 'recursiveleastsquaresestimator'
documentation_source_path: 'ref/recursiveleastsquaresestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# Recursive Least Squares Estimator

## 端口
```yaml
ports:
- name: Regressors
  summary: 回归量信号 向量 | 矩阵
  direction: input
  data_types: single | double
- name: Output
  summary: 测量输出 标量 | 向量
  direction: input
  data_types: single | double
- name: Enable
  summary: 启用估计更新 true（默认）| false
  direction: input
  data_types: single | double | Boolean | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32
- name: Reset
  summary: 重置触发器 标量
  direction: input
  data_types: single | double | Boolean | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: InitialParameters
  summary: 初始参数估计 向量
  direction: input
  data_types: single | double
- name: InitialCovariance
  summary: 参数的初始协方差 正标量（默认）| 正标量向量 | 对称正定矩阵
  direction: input
  data_types: single | double
- name: InitialRegressors
  summary: 回归量矩阵的初始值
  direction: input
  data_types: single | double
- name: InitialOutputs
  summary: 测量输出缓冲区向量的初始值
  direction: input
  data_types: single | double
- name: Parameters
  summary: 估计参数向量
  direction: output
  data_types: single | double
- name: Error
  summary: 估计误差标量 | 向量
  direction: output
  data_types: single | double
- name: Covariance
  summary: 参数估计误差协方差 P 矩阵
  direction: output
  data_types: single | double
```

### 输入

### **Regressors** — 回归量信号 向量 | 矩阵

回归量输入信号 *H*(*t*)。**Input Processing** 和 **Number of Parameters** 参数定义了该信号的维度：

- 基于采样的输入处理和 *N* 个估计参数 — 1×*N* 向量
- 基于帧的输入处理，每帧 *M* 个样本和 *N* 个估计参数 — *M*×*N* 矩阵

**数据类型：** `single` | `double`

### **Output** — 测量输出 标量 | 向量

测量输出信号 *y*(*t*)。**Input Processing** 参数定义了该信号的维度：

- 基于采样的输入处理 — 标量
- 基于帧的输入处理，每帧 *M* 个样本 — *M*×1 向量

**数据类型：** `single` | `double`

### **Enable** — 启用估计更新 `true`（默认）| `false`

外部信号，允许您启用和禁用估计更新。如果该信号值为：

- `true` — 估计并输出该时间步的参数值。
- `false` — 不估计参数值，并输出最近一次先前估计的值。

#### 依赖关系

要启用此端口，请选择 **Add enable port** 参数。

**数据类型：** `single` | `double` | `Boolean` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32`

### **Reset** — 重置触发器 标量

将参数估计重置为其初始条件。**External reset** 参数的值决定了触发类型。触发类型决定了重置是在上升、下降、上升或下降、电平或电平保持信号上发生。

#### 依赖关系

要启用此端口，请在 **External reset** 下拉列表中选择除 `None` 以外的任何选项。

**数据类型：** `single` | `double` | `Boolean` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **InitialParameters** — 初始参数估计 向量

初始参数估计，由模块外部的源提供。模块在仿真开始时或当您使用 **Reset** 信号触发算法重置时使用此输入端口。

**Number of Parameters** 参数定义了该信号的维度。如果有 *N* 个参数，则该信号为 *N*×1。

#### 依赖关系

要启用此端口，请将 **History** 设置为 `Infinite`，并将 **Initial Estimate** 设置为 `External`。

**数据类型：** `single` | `double`

### **InitialCovariance** — 参数的初始协方差 正标量（默认）| 正标量向量 | 对称正定矩阵

初始参数协方差，由模块外部的源提供。有关详细信息，请参阅 **Parameter Covariance Matrix** 参数。模块在仿真开始时或当您使用 **Reset** 信号触发算法重置时使用此输入端口。

#### 依赖关系

要启用此端口，请设置以下参数：

- **History** 设置为 `Infinite`
- **Estimation Method** 设置为 `Forgetting Factor` 或 `Kalman Filter`
- **Initial Estimate** 设置为 `External`

**数据类型：** `single` | `double`

### **InitialRegressors** — 回归量矩阵的初始值

使用有限历史（滑动窗口）估计时，初始数据窗口中回归量的初始值，由外部源提供。**Window length** 参数 *W* 和 **Number of Parameters** 参数 *N* 定义该信号的维度，即 *W*×*N*。

**InitialRegressors** 信号控制算法的初始行为。模块在仿真开始时或每当 **Reset** 信号触发时使用此输入端口。

如果初始缓冲区设置为 `0` 或不包含足够的信息，您将在估计的初始阶段看到一条警告消息。该警告应在几个周期后清除。缓冲足够信息所需的周期数取决于多项式的阶数和输入延迟。如果警告持续存在，您应评估信号的内容。

#### 依赖关系

要启用此端口，请将 **History** 设置为 `Finite`，并将 **Initial Estimate** 设置为 `External`。

**数据类型：** `single` | `double`

### **InitialOutputs** — 测量输出缓冲区向量的初始值

使用有限历史（滑动窗口）估计时，输出测量值的初始集合，由外部源提供。此端口的信号必须是 *W*×1 向量，其中 *W* 是窗口长度。

**InitialOutputs** 信号控制算法的初始行为。模块在仿真开始时或每当 **Reset** 信号触发时使用此输入端口。

如果初始缓冲区设置为 `0` 或不包含足够的信息，您将在估计的初始阶段看到一条警告消息。该警告应在几个周期后清除。缓冲足够信息所需的周期数取决于多项式的阶数和输入延迟。如果警告持续存在，您应评估信号的内容。

#### 依赖关系

要启用此端口，请将 **History** 设置为 `Finite`，并将 **Initial Estimate** 设置为 `External`。

**数据类型：** `single` | `double`
### 输出

### **Parameters** — 估计参数向量

估计参数 *θ*(*t*)，以 *N*×1 向量形式返回，其中 *N* 是参数数量。

**数据类型：** `single` | `double`

### **Error** — 估计误差标量 | 向量

估计误差，返回为：

- 标量 — 基于采样的输入处理
- *M*×1 向量 — 基于帧的输入处理，每帧 *M* 个采样

#### 依赖关系

要启用此端口，请选中 **Output estimation error** 参数。

**数据类型：** `single` | `double`

### **Covariance** — 参数估计误差协方差 P 矩阵

参数估计误差协方差 *P*，以 *N*×*N* 矩阵形式返回，其中 *N* 是参数数量。有关详细信息，请参阅 **Output Parameter Covariance Matrix** 参数。

#### 依赖关系

要启用此端口：

- 如果 **History** 为 `Infinite`，请将 **Estimation Method** 设置为 `Forgetting Factor` 或 `Kalman Filter`。
- 无论 **History** 为 `Infinite` 还是 `Finite`，请选中 **Output parameter covariance matrix** 参数。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Initial Estimate
  summary: 初始参数估计的来源 None（默认）| Internal | External
  group: 模型参数
  block_parameter: InitialEstimateSource
  type: character vector, string
  values: '''None'', ''Internal'', ''External'''
  default: '''None'''
- name: Number of Parameters
  summary: 要估计的参数数量 2（默认）| 正整数
  group: 模型参数
  block_parameter: InitialParameterData
  type: positive integer
  default: '2'
- name: Parameter Covariance Matrix
  summary: 初始参数协方差 1e4（默认）| 标量 | 向量 | 矩阵
  group: 模型参数
  block_parameter: P0
  type: scalar, vector, or matrix
  default: 1e4
- name: Initial Parameter Values
  summary: 要估计的参数的初始值 [1 1]（默认）| 向量
  group: 模型参数
  block_parameter: InitialParameterData
  type: real vector
  default: '[1 1]'
- name: Initial Regressors
  summary: 回归量缓冲区的初始值 0（默认）| 矩阵
  group: 模型参数
  block_parameter: InitialRegressors
  type: real matrix
  default: '0'
- name: Initial Outputs
  summary: 测量输出缓冲区的初始值 0（默认）| 向量
  group: 模型参数
  block_parameter: InitialOutputs
  type: real vector
  default: '0'
- name: Input Processing
  summary: 选择基于采样或基于帧的处理 Sample-based（默认）| Frame-based
  group: 模型参数
  block_parameter: InputProcessing
  type: character vector, string
  values: '''Sample-based'', ''Frame-based'''
  default: '''Sample-based'''
- name: Sample Time
  summary: 模块采样时间 -1（默认）| 正标量
  group: 模型参数
  block_parameter: Ts
  type: real scalar
  default: '-1'
- name: History
  summary: 选择无限或有限数据历史 Infinite（默认）| Finite
  group: 算法与模块选项
  block_parameter: History
  type: character vector, string
  values: '''Infinite'', ''Finite'''
  default: '''Infinite'''
- name: Window Length
  summary: 有限滑动窗口估计的窗口大小 200（默认）| 正整数
  group: 算法与模块选项
  block_parameter: WindowLength
  type: positive integer
  default: '200'
- name: Estimation Method
  summary: 递归估计算法 Forgetting Factor（默认）| Kalman Filter | Normalized Gradient | Gradient
  group: 算法与模块选项
  block_parameter: EstimationMethod
  type: character vector, string
  values: '''Forgetting Factor'',''Kalman Filter'',''Normalized Gradient'',''Gradient'''
  default: '''Forgetting Factor'''
- name: Forgetting Factor
  summary: 使用遗忘因子 1（默认值）| (0 1] 范围内的正标量对旧数据进行折扣
  group: 算法与模块选项
  block_parameter: AdaptationParameter
  type: 标量
  values: (0 1] 范围
  default: '1'
- name: Process Noise Covariance
  summary: Kalman 滤波器估计方法的过程噪声协方差 1（默认值）| 非负标量 | 非负标量向量 | 对称半正定矩阵
  group: 算法与模块选项
  block_parameter: AdaptationParameter
  type: 标量、向量、矩阵
  default: '1'
- name: Adaptation Gain
  summary: 梯度估计方法的自适应增益规范 1（默认值）| 正标量
  group: 算法与模块选项
  block_parameter: AdaptationParameter
  type: 标量
  default: '1'
- name: Normalization Bias
  summary: 归一化梯度估计方法的自适应增益缩放偏置 eps（默认）| 非负标量
  group: 算法与模块选项
  block_parameter: NormalizationBias
  type: 标量
  default: eps
- name: Output estimation error
  summary: 向模块添加 Error 输出端口 off（默认）| on
  group: 算法与模块选项
  block_parameter: OutputError
  type: 字符向量、字符串
  values: '''off''、''on''、'
  default: '''off'''
- name: Output parameter covariance matrix
  summary: 向模块添加 covariance 输出端口 off（默认）| on
  group: 算法与模块选项
  block_parameter: OutputP
  type: 字符向量、字符串
  values: '''off''、''on'''
  default: '''off'''
- name: Add enable port
  summary: 向模块添加 Enable 输入端口 off（默认）| on
  group: 算法与模块选项
  block_parameter: AddEnablePort
  type: 字符向量、字符串
  values: '''off''、''on'''
  default: '''off'''
- name: External reset
  summary: 指定外部复位的触发条件 None（默认）| Rising | Falling | Either | Level | Level hold
  group: 算法与模块选项
  block_parameter: ExternalReset
  type: character vector, string
  values: '''None'',''Rising'',''Falling'', ''Either'', ''Level'', ''Level hold'''
  default: '''None'''
```

### 模型参数

### **Initial Estimate** — 初始参数估计的来源 `None`（默认）| `Internal` | `External`

指定如何向模块提供初始参数估计：

- `None` — 不指定初始估计。

  - 如果 **History** 为 `Infinite`，模块使用 `1` 作为初始参数估计。
  - 如果 **History** 为 `Finite`，模块根据初始 **Regressors** 和 **Outputs** 信号计算初始参数估计。

  请指定 **Number of Parameters**，并且如果 **History** 为 `Infinite`，还需指定 **Parameter Covariance Matrix**。
- `Internal` — 在模块内部指定初始参数估计

  - 如果 **History** 为 `Infinite`，请指定 **Initial Parameter Values** 和 **Parameter Covariance Matrix** 参数。
  - 如果 **History** 为 `Finite`，请指定 **Number of Parameters**、**Initial Regressors** 和 **Initial Outputs** 参数。
- `External` — 将初始参数估计指定为模块的输入信号。

  请指定 **Number of Parameters** 参数。**History** 参数的设置决定了需要将哪些附加信号连接到相关端口：

  - 如果 **History** 为 `Infinite` — **InitialParameters** 和 **InitialCovariance**
  - 如果 **History** 为 `Finite` — **InitialRegressors** 和 **InitialOutputs**

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialEstimateSource` |
| **类型**：character vector, string |
| **值**：`'None'`, `'Internal'`, `'External'` |
| **默认值**：`'None'` |

### **Number of Parameters** — 要估计的参数数量 `2`（默认）| 正整数

指定模型中要估计的参数数量，等于参数 *θ*(*t*) 向量中的元素个数。

#### 依赖关系

要启用此参数，请设置以下任一组合：

- **History** 为 `Infinite`，且 **Initial Estimate** 为 `None` 或 `External`
- **History** 为 `Finite`

指定要估计的参数数量 *N* 的另一种方法是使用 **Initial Parameter Values** 参数，为此您需要定义一个包含 *N* 个元素的初始估计向量。此方法涵盖了剩余的一种组合，即 **History** 为 `Infinite` 且 **Initial Estimate** 为 `Internal`。有关详细信息，请参阅 **Initial Parameter Values**。

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialParameterData` |
| **类型**：positive integer |
| **默认值**：`2` |

### **Parameter Covariance Matrix** — 初始参数协方差 `1e4`（默认）| 标量 | 向量 | 矩阵

将 **Parameter Covariance Matrix** 指定为：

- 实正标量 *α* — 协方差矩阵为 *N*×*N* 对角矩阵，对角线元素为 *α*。
- 实正标量向量 [*α*1,...,*α**N*] — 协方差矩阵为 *N*×*N* 对角矩阵，对角线元素为 [*α*1,...,*α**N*]。
- *N*×*N* 对称正定矩阵。

此处，*N* 是要估计的参数数量。

#### 依赖关系

要启用此参数，请设置以下参数：

- **History** 为 `Infinite`
- **Initial Estimate** 为 `None` 或 `Internal`
- **Estimation Method** 为 `Forgetting Factor` 或 `Kalman Filter`

#### 编程使用

|  |
| --- |
| **模块参数**：`P0` |
| **类型**：scalar, vector, or matrix |
| **默认值**：`1e4` |

### **Initial Parameter Values** — 要估计的参数的初始值 `[1 1]`（默认）| 向量

将初始参数值指定为长度为 *N* 的向量，其中 *N* 是要估计的参数数量。

#### 依赖关系

要启用此参数，请将 **History** 设置为 `Infinite`，并将 **Initial Estimate** 设置为 `Internal`。

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialParameterData` |
| **类型**：real vector |
| **默认值**：`[1 1]` |

### **Initial Regressors** — 回归量缓冲区的初始值 `0`（默认）| 矩阵

在使用有限历史（滑动窗口）估计时，指定回归量缓冲区的初始值。**Window length** 参数 *W* 和 **Number of Parameters** 参数 *N* 定义回归量缓冲区的维度，即 *W*×*N*。

**Initial Regressors** 参数控制算法的初始行为。该模块在仿真开始时或每当 **Reset** 信号触发时使用此参数。

当初始值设置为 `0` 时，该模块用零填充缓冲区。

如果初始缓冲区设置为 `0` 或包含的信息不足，您会在估计的初始阶段看到警告消息。该警告应在几个周期后清除。缓冲足够信息所需的周期数取决于多项式的阶数和输入延迟。如果警告持续存在，您应评估信号的内容。

#### 依赖关系

要启用此参数，请将 **History** 设置为 `Finite`，并将 **Initial Estimate** 设置为 `Internal`。

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialRegressors` |
| **类型**：real matrix |
| **默认值**：`0` |

### **Initial Outputs** — 测量输出缓冲区的初始值 `0`（默认）| 向量

在使用有限历史（滑动窗口）估计时，指定测量输出缓冲区的初始值。此参数是一个 *W*×1 向量，其中 *W* 是窗口长度。

当初始值设置为 `0` 时，该模块用零填充缓冲区。

如果初始缓冲区设置为 `0` 或包含的信息不足，您会在估计的初始阶段看到警告消息。该警告应在几个周期后清除。缓冲足够信息所需的周期数取决于多项式的阶数和输入延迟。如果警告持续存在，您应评估信号的内容。

**Initial Outputs** 参数控制算法的初始行为。该模块在仿真开始时或每当 **Reset** 信号触发时使用此参数。

#### 依赖关系

要启用此参数，请将 **History** 设置为 `Finite`，并将 **Initial Estimate** 设置为 `Internal`。

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialOutputs` |
| **类型**：real vector |
| **默认值**：`0` |

#### 输入处理与采样时间

### **Input Processing** — 选择基于采样或基于帧的处理 `Sample-based`（默认）| `Frame-based`

- `Sample-based` 处理对一次流式传输一个采样的信号进行操作。
- `Frame-based` 处理对包含多个时间步采样的信号进行操作。许多机器传感器接口将多个采样打包，并将这些采样一起以帧的形式传输。`Frame-based` 处理允许您直接输入此数据，而无需先将其解包。

指定基于帧的数据会为某些数据输入端口和输出端口添加一个额外的 *M* 维度，其中 *M* 是帧中的时间步数。这些端口包括：

- **Regressors**
- **Output**
- **Error**

有关详细信息，请参阅端口中的端口描述。

#### 编程使用

|  |
| --- |
| **模块参数**：`InputProcessing` |
| **类型**：character vector, string |
| **值**：`'Sample-based'`, `'Frame-based'` |
| **默认值**：`'Sample-based'` |

### **Sample Time** — 模块采样时间 `-1`（默认）| 正标量

指定数据采样时间，无论是基于采样的处理的单个采样（*ts*），还是基于帧的处理的帧（*tf* = *M**ts*），其中 *M* 是帧长度。当您将 **Sample Time** 设置为其默认值 -1 时，该模块根据信号继承其 *ts* 或 *tf*。

将 **Sample Time** 指定为正标量以覆盖继承。

#### 编程用法

|  |
| --- |
| **模块参数：**`Ts` |
| **类型：** real scalar |
| **默认值：** `-1` |

### 算法与模块选项

#### 算法选项

### **History** — 选择无限或有限数据历史 `Infinite`（默认）| `Finite`

**History** 参数决定使用何种类型的递归算法：

- `Infinite` — 此类算法旨在生成能够解释自仿真开始以来所有数据的参数估计。这些算法将历史数据保留在数据摘要中。模块在固定的内存量内维护此摘要，该内存量不随时间增长。

  模块提供多种 `Infinite` 类型的算法。选择此选项将启用 **Estimation Method** 参数，您可以通过该参数指定算法。
- `Finite` — 此类算法旨在生成仅能解释有限数量过去数据样本的参数估计。模块使用有限窗口内的所有数据，一旦数据不再处于窗口范围内便将其丢弃。此方法也称为滑动窗口估计。

  选择此选项将启用 **Window Length** 参数，用于设置滑动窗口的大小。

有关递归估计方法的更多信息，请参阅 Recursive Algorithms for Online Parameter Estimation

#### 编程用法

|  |
| --- |
| **模块参数：**`History` |
| **类型：** character vector, string |
| **值：** `'Infinite'`, `'Finite'` |
| **默认值：**`'Infinite'` |

### **Window Length** — 有限滑动窗口估计的窗口大小 `200`（默认）| 正整数

**Window Length** 参数决定用于滑动窗口估计方法的时间样本数。请选择在估计性能与计算和内存负担之间取得平衡的窗口大小。大小设定因素包括模型中参数的数量和时变特性。即使您使用基于帧的输入处理，也始终以样本为单位指定 **Window Length**。

**Window Length** 必须大于或等于估计参数的数量。

合适的窗口长度与您使用的是基于样本还是基于帧的输入处理无关。但是，当使用基于帧的处理时，**Window Length** 必须大于或等于帧中包含的样本数（时间步数）。

#### 依赖关系

要启用此参数，请将 **History** 设置为 `Finite`。

#### 编程用法

|  |
| --- |
| **模块参数：**`WindowLength` |
| **类型：** positive integer |
| **默认值：** `200` |

### **Estimation Method** — 递归估计算法 `Forgetting Factor`（默认）| `Kalman Filter` | `Normalized Gradient` | `Gradient`

在执行无限历史估计时指定估计算法。当您选择这些方法中的任何一种时，模块将启用相关的附加参数。

遗忘因子和卡尔曼滤波算法比梯度及归一化梯度方法的计算量更大。然而，这些计算量更大的方法比梯度方法具有更好的收敛特性。有关这些算法的更多信息，请参阅 Recursive Algorithms for Online Parameter Estimation。

#### 编程用法

|  |
| --- |
| **模块参数：**`EstimationMethod` |
| **类型：** character vector, string |
| **值：** `'Forgetting Factor'`,`'Kalman Filter'`,`'Normalized Gradient'`,`'Gradient'` |
| **默认值：** `'Forgetting Factor'` |

### **Forgetting Factor** — 使用遗忘因子 `1`（默认值）| (0 1] 范围内的正标量对旧数据进行折扣

遗忘因子 *λ* 指定在估计中是否以及多少旧数据被折扣。假设系统在 *T0* 个样本上保持近似恒定。您可以选择 *λ* 使得：

T0=11−λ

- 设置 *λ* = 1 对应于“无遗忘”并估计常数系数。
- 设置 *λ* < 1 意味着过去的测量对参数估计不太重要，可以被“遗忘”。设置 *λ* < 1 以估计时变系数。

*λ* 的典型选择在 [0.98 0.995] 范围内。

#### 依赖关系

要启用此参数，请将 **History** 设置为 `Infinite`，并将 **Estimation Method** 设置为 `Forgetting Factor`。

#### 编程使用

|  |
| --- |
| **模块参数：**`AdaptationParameter` |
| **类型：** 标量 |
| **值：** (0 1] 范围 |
| **默认值：** `1` |

### **Process Noise Covariance** — Kalman 滤波器估计方法的过程噪声协方差 `1`（默认值）| 非负标量 | 非负标量向量 | 对称半正定矩阵

**Process Noise Covariance** 指定 Kalman 滤波器估计中噪声协方差矩阵的元素和结构。使用 *N* 作为要估计的参数数量，将 **Process Noise Covariance** 指定为以下之一：

- 实非负标量 *α* — 协方差矩阵是一个 *N*×*N* 对角矩阵，以 *α* 为对角元素。
- 实非负标量向量 [*α*1,...,*α**N*] — 协方差矩阵是一个 *N*×*N* 对角矩阵，以 [*α*1,...,*α**N*] 为对角元素。
- *N*×*N* 对称半正定矩阵。

Kalman 滤波器算法将参数视为动态系统的状态，并使用 Kalman 滤波器估计这些参数。**Process Noise Covariance** 是作用于这些参数的过程噪声的协方差。噪声协方差矩阵中的零值对应于常数系数或参数。大于 0 的值对应于时变参数。对于快速变化的参数使用较大的值。但是，预期较大的值会导致参数估计更加嘈杂。默认值为 1。

#### 依赖关系

要启用此参数，请将 **History** 设置为 `Infinite`，并将 **Estimation Method** 设置为 `Kalman Filter`。

#### 编程使用

|  |
| --- |
| **模块参数：**`AdaptationParameter` |
| **类型：** 标量、向量、矩阵 |
| **默认值：** `1` |

### **Adaptation Gain** — 梯度估计方法的自适应增益规范 `1`（默认值）| 正标量

自适应增益 *γ* 缩放新测量数据对梯度和归一化梯度方法估计结果的影响。当您的测量可信时，换句话说具有高信噪比时，为 *γ* 指定较大的值。但是，将 *γ* 设置得太高可能导致参数估计发散。即使测量无噪声，这种发散也是可能的。

当 **Estimation Method** 为 `NormalizedGradient` 时，**Adaptation Gain** 应小于 2。对于任一种梯度方法，如果误差随时间增长（换句话说，估计正在发散），或者参数估计频繁跳动，请考虑减小 **Adaptation Gain**。

#### 依赖关系

要启用此参数，请将 **History** 设置为 `Infinite`，并将 **Estimation Method** 设置为 `Normalized Gradient` 或 `Gradient`。

#### 编程使用

|  |
| --- |
| **模块参数：**`AdaptationParameter` |
| **类型：** 标量 |
| **默认值：** `1` |

### **Normalization Bias** — 归一化梯度估计方法的自适应增益缩放偏置 `eps`（默认）| 非负标量

归一化梯度算法在每一步通过梯度向量二范数的平方来缩放自适应增益。如果梯度接近零，接近零的分母可能导致估计参数出现跳变。
**Normalization Bias** 是引入分母中的项，用于防止这些跳变。如果观察到估计参数出现跳变，请增大 **Normalization Bias**。

#### 依赖关系

要启用此参数，请将 **History** 设置为
`Infinite`，并将 **Estimation Method** 设置为
`Normalized Gradient`。

#### 编程用法

|  |
| --- |
| **模块参数：**`NormalizationBias` |
| **类型：** 标量 |
| **默认值：** `eps` |

#### 模块选项

### **Output estimation error** — 向模块添加 Error 输出端口 `off`（默认）| on

使用 **Error** 输出端口信号来验证估计。对于
给定的时间步 *t*，估计误差
*e*(*t*) 计算如下：

e(t)=y(t)−yest(t)，

其中 *y*(*t*) 是您
提供的测量输出，*yest*(*t*) 是
使用回归量 *H*(*t*)
和参数估计 *θ*(*t*-1) 得到的估计输出。

#### 编程用法

|  |
| --- |
| **模块参数：**`OutputError` |
| **类型：** 字符向量、字符串 |
| **值：**`'off'`、`'on'`、 |
| **默认值：** `'off'` |

### **Output parameter covariance matrix** — 向模块添加 covariance 输出端口 `off`（默认）| on

使用 **Covariance** 输出端口信号来检查参数
估计不确定性。该软件计算参数协方差
`P`，假设残差
*e*(*t*) 为白噪声，并且
这些残差的方差为 1。

`P` 的解释取决于您在 **History** 和 **Estimation Method** 中
指定的估计方法，如下所示：

- 如果 **History** 为 `Infinite`，则
  您选择的 **Estimation Method** 会导致：

  - `Forgetting Factor` —
    (*R2*`/2`)`P`
    大约等于估计参数的协方差矩阵，
    其中 *R2* 是残差的真实方差。该模块在
    **Error** 端口中输出残差。
  - `Kalman Filter` —
    *R2*`P` 是
    估计参数的协方差矩阵，并且
    *R1*
    /*R2* 是参数变化的协方差矩阵。这里，*R1*
    是您在 **Parameter Covariance
    Matrix** 中指定的协方差矩阵。
  - `Normalized Gradient` 或
    `Gradient` — 协方差 *P*
    不可用。
- 如果 **History** 为 `Finite`
  （滑动窗口估计）— *R2*
  *P* 是估计参数的协方差。滑动窗口算法在
  参数估计过程中不使用此协方差。但是，该算法会为输出计算协方差，
  以便您可以将其用于统计评估。

#### 编程用法

|  |
| --- |
| **模块参数：**`OutputP` |
| **类型：** 字符向量、字符串 |
| **值：**`'off'`、`'on'` |
| **默认值：** `'off'` |

### **Add enable port** — 向模块添加 Enable 输入端口 `off`（默认）| on

使用 **Enable** 信号提供一个控制信号，用于
启用或禁用参数估计。该模块会在参数估计启用的
每个时间步估计参数值。如果您在给定步 *t* 禁用参数
估计，则该软件不会更新该时间步的参数。
相反，该模块会输出最后估计的参数值。

- 例如，您可以在以下情况使用此选项：

  - 您的回归量或输出信号变得噪声过大，或在某些时间步不包含
    信息
  - 您的系统进入参数值不随时间变化的
    模式

#### 编程用法

|  |
| --- |
| **模块参数：**`AddEnablePort` |
| **类型：** 字符向量、字符串 |
| **值：**`'off'`、`'on'` |
| **默认值：** `'off'` |

### **External reset** — 指定外部复位的触发条件 `None`（默认）| `Rising` | `Falling` | `Either` | `Level` | `Level hold`

将 **External reset** 参数设置为同时添加一个 **Reset** 输入端口，并指定触发算法状态复位到其指定初始值的输入端口信号条件。例如，如果由于测量信号中缺乏足够的激励或信息而导致参数协方差变得过大，则复位估计。

假设您在时间步 *t* 复位该模块。如果该模块在 *t* 时刻使能，软件将使用 **Initial Estimate** 中指定的初始参数值来估计参数值。换句话说，在 *t* 时刻，该模块使用初始估计和输入端口的当前值执行参数更新。

如果该模块在 *t* 时刻禁用，并且您复位该模块，则该模块输出 **Initial Estimate** 中指定的值。

将此选项指定为以下之一：

- `None` — 算法状态和估计参数不复位。
- `Rising` — 当控制信号从负值或零值上升到正值时触发复位。如果初始值为负值，上升到零会触发复位。
- `Falling` — 当控制信号从正值或零值下降到负值时触发复位。如果初始值为正值，下降到零会触发复位。
- `Either` — 当控制信号上升或下降时触发复位。
- `Level` — 在以下任一情况下触发复位：

  - 控制信号在当前时间步非零。
  - 控制信号从上一时间步的非零变为当前时间步的零。
- `Level hold` — 当控制信号在当前时间步非零时触发复位。

当您选择除 `None` 以外的任何选项时，软件会向该模块添加一个 Reset 输入端口。您向此输入端口提供复位控制输入信号。

#### 编程使用

|  |
| --- |
| **模块参数**：`ExternalReset` |
| **类型**：character vector, string |
| **值**：`'None'`,`'Rising'`,`'Falling'`, `'Either'`, `'Level'`, `'Level hold'` |
| **默认值**：`'None'` |
## 所属库

System Identification Toolbox / Estimators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**在 R2014a 中引入**

## 描述

使用递归最小二乘（RLS）算法估计模型系数

递归最小二乘估计器使用一个关于参数线性的模型来估计系统参数。这样的系统具有以下形式：

y(t)=H(t)θ(t)。

*y* 和 *H* 是已知量，您将它们提供给模块以估计 *θ*。该模块可以为 *θ* 提供无限历史 [1] 和有限历史 [2]（也称为滑动窗口）估计。有关这些方法的更多信息，请参阅 Recursive Algorithms for Online Parameter Estimation。

该模块支持多种估计方法和数据输入格式。模块中的可配置选项包括：

- 基于采样或基于帧的数据格式 — 请参阅 **Input Processing** 参数。
- 无限历史或有限历史估计 — 请参阅 **History** 参数。
- 多种无限历史估计方法 — 请参阅 **Estimation Method** 参数。
- 初始条件、使能标志和复位触发 — 请参阅 **Initial Estimate**、**Add enable port** 和 **External Reset** 参数。

对于给定的时间步 *t*，*y*(*t*) 和 *H*(*t*) 分别对应于 Recursive Least Squares Estimator 模块的 **Output** 和 **Regressors** 输入端口。*θ*(*t*) 对应于 **Parameters** 输出端口。

例如，假设您想要估计系统 *y* = *h*2*θ* 中的标量增益 *θ*。这里，*y* 相对于 *θ* 是线性的。您可以使用 Recursive Least Squares Estimator 模块来估计 *θ*。将 *y* 和 *h*2 指定为 **Output** 和 **Regressor** 输入端口的输入。
