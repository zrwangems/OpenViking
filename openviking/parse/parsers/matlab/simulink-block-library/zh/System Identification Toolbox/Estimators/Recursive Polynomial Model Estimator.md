---
type: simulink-block
title: 'Recursive Polynomial Model Estimator'
family: 'ident'
product_id: 'ident'
product_name: 'System Identification Toolbox'
documentation_release: R2025b
official_category: 'Estimators'
documentation_page: 'recursivepolynomialmodelestimator'
documentation_source_path: 'ref/recursivepolynomialmodelestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# Recursive Polynomial Model Estimator

## 端口
```yaml
ports:
- name: Inputs
  summary: 输入信号向量 | 矩阵
  direction: input
  data_types: single | double
- name: Output
  summary: 测量输出信号 标量 | 向量
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
  summary: 初始参数估计 bus 对象
  direction: input
  data_types: single | double
- name: InitialCovariance
  summary: 参数的初始协方差 正标量（默认）| 正标量向量 | 对称正定矩阵
  direction: input
  data_types: single | double
- name: InitialInputs
  summary: 输入矩阵的初始值
  direction: input
  data_types: single | double
- name: InitialOutputs
  summary: 测量输出缓冲区向量的初始值
  direction: input
  data_types: single | double
- name: Parameters
  summary: 估计参数 bus 对象
  direction: output
  data_types: single | double
- name: Error
  summary: 估计误差 标量 | 向量
  direction: output
  data_types: single | double
- name: Covariance
  summary: 参数估计误差协方差 P 矩阵
  direction: output
  data_types: single | double
```

### 输入

### **Inputs** — 输入信号向量 | 矩阵

输入信号 *u*(*t*)。**Input Processing** 参数和输入数量 *nu* 定义了信号的维度。只有 ARX 模型结构可以有多个输入，此时 *nu* 大于 1。

- 基于采样的输入处理和 *nu* 个输入 —
  *nu*×1 向量
- 基于帧的输入处理，每帧 *M* 个采样且 *nu* 个输入 — *M*×*nu*
  矩阵

#### 依赖

要启用此端口，请将 **Model Structure** 参数设置为
`ARX`、`ARMAX`、
`BJ` 或 `OE`。

**数据类型：** `single` | `double`

### **Output** — 测量输出信号 标量 | 向量

测量输出信号 *y*(*t*)。**Input Processing** 参数定义了信号的维度：

- 基于采样的输入处理 — 标量
- 基于帧的输入处理，每帧 *M* 个采样 —
  *M*×1 向量

**数据类型：** `single` | `double`

### **Enable** — 启用估计更新 `true`（默认）| `false`

外部信号，允许您启用和禁用估计更新。如果信号值为：

- `true` — 估计并输出该时间步的参数值。
- `false` — 不估计参数值，并输出最近一次先前估计的值。

#### 依赖

要启用此端口，请选中 **Add enable port**
参数。

**数据类型：** `single` | `double` | `Boolean` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32`

### **Reset** — 重置触发器 标量

将参数估计重置为其初始条件。**External reset** 参数的值决定了触发类型。触发类型决定了重置是在上升、下降、上升或下降、电平或电平保持信号上发生。

#### 依赖

要启用此端口，请在 **External reset**
下拉列表中选择除 `None` 以外的任何选项。

**数据类型：** `single` | `double` | `Boolean` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **InitialParameters** — 初始参数估计 `bus` 对象

初始参数估计，从模块外部的源提供。模块在仿真开始时或当您使用 **Reset** 信号触发算法重置时使用此输入端口。

有关 **InitialParameters** 总线对象内容的信息，请参阅 **Parameters** 端口描述。

#### 依赖

要启用此端口，请将 **History** 设置为
`Infinite`，并将 **Initial Estimate** 设置为
`External`。

**数据类型：** `single` | `double`

### **InitialCovariance** — 参数的初始协方差 正标量（默认）| 正标量向量 | 对称正定矩阵

初始参数协方差，从模块外部的源提供。有关详细信息，请参阅 **Parameter Covariance Matrix** 参数。模块在仿真开始时或当您使用 **Reset** 信号触发算法重置时使用此输入端口。

#### 依赖

要启用此端口，请设置以下参数：

- **History** 设置为 `Infinite`
- **Estimation Method** 设置为 `Forgetting
  Factor` 或 `Kalman Filter`
- **Initial Estimate** 设置为
  `External`

**数据类型：** `single` | `double`

### **InitialInputs** — 输入矩阵的初始值

使用有限历史（滑动窗口）估计时的初始输入集，由外部源提供。

- 如果 **Model Structure** 为 `ARX`，则此端口的信号必须是一个 (*W*–1+max(*nb*)+max(*nk*))×*nu* 矩阵，其中 *W* 是窗口长度，*nu* 是输入数量。*nb* 是 *B*(*q*) 多项式阶数的向量，*nk* 是输入延迟的向量。
- 如果 **Model Structure** 为 `OE`，则此端口的信号必须是一个 (*W*–1+*nb*+*nk*)×1 向量，其中 *W* 是窗口长度。*nb* 是 *B*(*q*) 多项式阶数的向量，*nk* 是输入延迟的向量。

模块在仿真开始时或每当 **Reset** 信号触发时使用此输入端口。

如果初始缓冲区设置为 `0` 或不包含足够的信息，您将在估计的初始阶段看到警告消息。该警告应在几个周期后清除。缓冲足够信息所需的周期数取决于多项式的阶数和输入延迟。如果警告持续存在，您应评估信号的内容。

#### 依赖关系

要启用此端口，请设置：

- **History** 为 `Finite`
- **Model Structure** 为 `ARX` 或 `OE`
- **Initial Estimate** 为 `External`

**Data Types:** `single` | `double`

### **InitialOutputs** — 测量输出缓冲区向量的初始值

使用有限历史（滑动窗口）估计时的初始输出测量集，由外部源提供。

- 如果 **Model Structure** 为 `AR` 或 `ARX`，则此端口的信号必须是一个 (*W*+*na*)×1 向量，其中 *W* 是窗口长度，*na* 是 *A*(*q*) 的多项式阶数。
- 如果 **Model Structure** 为 `OE`，则此端口的信号必须是一个 (*W*+*nf*)×1 向量，其中 *W* 是窗口长度，*nf* 是 *F*(*q*) 的多项式阶数。

模块在仿真开始时或每当 **Reset** 信号触发时使用此输入端口。

如果初始缓冲区设置为 `0` 或不包含足够的信息，您将在估计的初始阶段看到警告消息。该警告应在几个周期后清除。缓冲足够信息所需的周期数取决于多项式的阶数和输入延迟。如果警告持续存在，您应评估信号的内容。

#### 依赖关系

要启用此端口，请设置：

- **History** 为 `Finite`
- **Model Structure** 为 `AR`、`ARX` 或 `OE`
- **Initial Estimate** 为 `External`

**Data Types:** `single` | `double`
### 输出

### **Parameters** — 估计参数 `bus` 对象

估计的多项式系数，以总线形式返回。该总线包含对应于您在 **Model Structure** 中指定的结构的 *A*、*B*、*C*、*D* 和 *F* 多项式中的每一个元素（参见 Model Structures）。

每个总线元素是一个包含相关多项式系数的向量信号。例如，*A* 元素包含 [1 *a1*(*t*) ... *ana*(*t*)]。

估计的 *C*、*D* 和 *F* 值被约束为稳定的离散时间多项式。也就是说，这些多项式的所有根都在单位圆内。估计的 *A* 和 *B* 多项式允许不稳定。

**Data Types:** `single` | `double`

### **Error** — 估计误差 标量 | 向量

估计误差，返回为：

- 标量 — 基于采样的输入处理
- *M*×1 向量 — 基于帧的输入处理，每帧 *M* 个采样

#### 依赖关系

要启用此端口，请选择 **Output estimation error** 参数。

**Data Types:** `single` | `double`

### **Covariance** — 参数估计误差协方差 P 矩阵

参数估计误差协方差 *P*，返回为 *N*×*N* 矩阵，其中 *N* 是参数数量。有关详细信息，请参见 **Output Parameter Covariance Matrix** 参数。

#### 依赖关系

要启用此端口：

- 选择 **输出参数协方差矩阵** 参数。
- 如果 **历史** 为 `Infinite`，将 **估计方法** 设置为 `Forgetting Factor` 或 `Kalman Filter`。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: 初始估计
  summary: 初始参数估计的来源 None（默认）| Internal | External
  group: 模型参数
  block_parameter: InitialEstimateSource
  type: 字符向量、字符串
  values: '''None''、''Internal''、''External'''
- name: A(q) 中的参数数量 (na)
  summary: '*A*(*q*) 多项式中估计参数的数量 1（默认）| 非负整数'
  group: 模型参数
  block_parameter: A0
  type: 非负整数
- name: Number of Parameters in B(q) (nb)
  summary: '*B*(*q*) 多项式中估计参数的数量 1（默认）| 正整数向量'
  group: 模型参数
  block_parameter: B0
  type: 正整数
  default: '1'
- name: Number of Parameters in C(q) (nc)
  summary: '*C*(*q*) 多项式中估计参数的数量 1（默认）| 正整数'
  group: 模型参数
  block_parameter: C0
  type: 正整数
  default: '1'
- name: Number of Parameters in D(q) (nd)
  summary: '*D*(*q*) 多项式中估计参数的数量 1（默认）| 正整数'
  group: 模型参数
  block_parameter: D0
  type: 正整数
  default: '1'
- name: Number of Parameters in F(q) (nf)
  summary: '*F*(*q*) 多项式中估计参数的数量 1（默认）| 正整数'
  group: 模型参数
  block_parameter: F0
  type: 正整数
  default: '1'
- name: Input Delay (nk)
  summary: 输入延迟 1（默认）| 非负整数向量
  group: 模型参数
  block_parameter: nk
  type: 非负整数向量
  default: '1'
- name: Parameter Covariance Matrix
  summary: 初始参数协方差 1e4（默认）| 标量 | 向量 | 矩阵
  group: 模型参数
  block_parameter: P0
  type: 标量、向量或矩阵
  default: 1e4
- name: Initial A(q)
  summary: '*A*(*q*) 多项式系数的初始值 [1 eps]（默认）| 向量'
  group: 模型参数
  block_parameter: A0
  type: 实向量
  default: '[1 eps]'
- name: Initial B(q)
  summary: '*B*(*q*) 多项式系数的初始值 [0 eps]（默认）| 向量 | 矩阵'
  group: 模型参数
  block_parameter: B0
  type: 实数向量或矩阵
  default: '[0 eps]'
- name: Initial C(q)
  summary: '*C*(*q*) 多项式系数的初始值 [1 eps]（默认）| 向量'
  group: 模型参数
  block_parameter: C0
  type: 实数向量
  default: '[1 eps]'
- name: Initial D(q)
  summary: '*D*(*q*) 多项式系数的初始值 [1 eps]（默认）| 向量'
  group: 模型参数
  block_parameter: D0
  type: 实数向量
  default: '[1 eps]'
- name: Initial F(q)
  summary: '*F*(*q*) 多项式系数的初始值 [1 eps]（默认）| 向量'
  group: 模型参数
  block_parameter: F0
  type: 实数向量
  default: '[1 eps]'
- name: Initial Inputs
  summary: 输入缓冲区的初始值 0（默认）| 矩阵
  group: 模型参数
  block_parameter: InitialInputs
  type: 实数矩阵
  default: '0'
- name: Initial Outputs
  summary: 测量输出缓冲区的初始值 0（默认）| 向量
  group: 模型参数
  block_parameter: InitialOutputs
  type: 实数向量
  default: '0'
- name: Input Processing
  summary: 选择基于采样或基于帧的处理 Sample-based（默认）| Frame-based
  group: 输入处理和采样时间
  block_parameter: InputProcessing
  type: 字符向量、字符串
  values: '''Sample-based''、''Frame-based'''
  default: '''Sample-based'''
- name: Sample Time
  summary: 模块采样时间 –1（默认）| 正标量
  group: 输入处理和采样时间
  block_parameter: Ts
  type: 实标量
  values: –1、正标量
  default: –1
- name: History
  summary: 选择无限或有限数据历史 Infinite（默认）| Finite
  group: 算法和模块选项
  block_parameter: History
  type: 字符向量、字符串
  values: '''Infinite''、''Finite'''
  default: '''Infinite'''
- name: Window Length
  summary: 有限滑动窗口估计的窗口大小 200（默认）| 正整数
  group: 算法和模块选项
  block_parameter: WindowLength
  type: 正整数
  default: '200'
- name: Estimation Method
  summary: 递归估计算法 Forgetting Factor（默认）| Kalman Filter | Normalized Gradient | Gradient
  group: 算法和模块选项
  block_parameter: EstimationMethod
  type: character vector, string
  values: '''Forgetting Factor'',''Kalman Filter'',''Normalized Gradient'',''Gradient'''
  default: '''Forgetting Factor'''
- name: Forgetting Factor
  summary: 使用遗忘因子对旧数据进行折扣 1（默认）| (0 1] 范围内的正标量
  group: 算法和模块选项
  block_parameter: AdaptationParameter
  type: scalar
  values: (0 1] range
  default: '1'
- name: Process Noise Covariance
  summary: 卡尔曼滤波估计方法的过程噪声协方差 1（默认）| 非负标量 | 非负标量向量 | 对称半正定矩阵
  group: 算法和模块选项
  block_parameter: AdaptationParameter
  type: scalar, vector, matrix
  default: '1'
- name: Adaptation Gain
  summary: 梯度估计方法的自适应增益指定 1（默认）| 正标量
  group: 算法和模块选项
  block_parameter: AdaptationParameter
  type: scalar
  default: '1'
- name: Normalization Bias
  summary: 归一化梯度估计方法的自适应增益缩放偏置 eps（默认）| 非负标量
  group: 算法和模块选项
  block_parameter: NormalizationBias
  type: scalar
  default: eps
- name: Output estimation error
  summary: 向模块添加 Error 输出端口 off（默认）| on
  group: 算法和模块选项
  block_parameter: OutputError
  type: character vector, string
  values: '''off'',''on'','
  default: '''off'''
- name: Output parameter covariance matrix
  summary: 向模块添加 covariance 输出端口 off（默认）| on
  group: 算法和模块选项
  block_parameter: OutputP
  type: 字符向量、字符串
  values: '''off''、''on'''
  default: '''off'''
- name: Add enable port
  summary: 向模块添加使能输入端口 off（默认）| on
  group: 算法和模块选项
  block_parameter: AddEnablePort
  type: 字符向量、字符串
  values: '''off''、''on'''
  default: '''off'''
- name: External reset
  summary: 指定外部复位的触发条件 None（默认）| Rising | Falling | Either | Level | Level hold
  group: 算法和模块选项
  block_parameter: ExternalReset
  type: 字符向量、字符串
  values: '''None''、''Rising''、''Falling''、''Either''、''Level''、''Level hold'''
  default: '''None'''
```

### 模型结构

估计的模型结构，指定为以下之一：

- `ARX` — SISO 或 MISO ARX 模型
- `ARMAX` — SISO ARMAX 模型
- `OE` — SISO OE 模型
- `BJ` — SISO BJ 模型
- `AR` — 时间序列 AR 模型
- `ARMA` — 时间序列 ARMA 模型

### 模型参数

### **初始估计** — 初始参数估计的来源 `None`（默认）| `Internal` | `External`

指定如何向模块提供初始参数估计：

- `None` — 不指定初始估计。

  模块使用 `0` 作为初始参数估计。

  根据您选择的模型结构和估计方法，指定模块启用的参数。

  - 根据您的 **模型结构** 指定模块启用的 **参数数量 ()** 参数集。例如，如果您的 **模型结构** 设置为 `AR`，请指定 **A(q) 中的参数数量 (na)** 参数。
  - 当您的模型结构使用 *B*(*q*) 元素时，指定模块启用的 **输入延迟 (nk)** 参数。
  - 如果 **估计方法** 为 `Forgetting Factor` 或 `Kalman Filter`，请指定 **参数协方差矩阵**。
- `Internal` — 在模块内部指定初始参数估计。

  - 根据您的 **模型结构** 和 **历史** 指定模块启用的初始参数值 **初始 ()** 参数。例如，如果您的 **模型结构** 设置为 `AR` 且 **历史** 为 `Infinite`，请指定 **初始 A(q)** 参数。
  - 当您的模型结构使用 *B*(*q*) 元素时，指定模块启用的 **输入延迟 (nk)** 参数。
  - 如果 **估计方法** 为 `Forgetting Factor` 或 `Kalman Filter`，请指定 **参数协方差矩阵** 参数。
  - 如果 **历史** 为 `Finite`，请指定 **初始输入** 参数（仅限 `ARX` 和 `OE`）以及 **初始输出** 参数（`ARX`、`AR` 和 `OE`）。
- `External` — 将初始参数估计指定为模块的输入信号。

  根据您的 **模型结构** 指定模块启用的 **参数数量 ()** 参数。您对 **模型结构** 和 **历史** 参数的设置决定了要连接到相关端口的信号：

  - 如果 **历史** 为 `Infinite` — **InitialParameters** 和 **InitialCovariance**
  - 如果 **历史** 为 `Finite` — `AR`、`ARX` 和 `OE` 模型结构的 **InitialOutputs**，以及 `ARX` 和 `OE` 模型结构的 **InitialInputs**

#### 编程用法

|  |
| --- |
| **模块参数：**`InitialEstimateSource` |
| **类型：** 字符向量、字符串 |
| **值：** `'None'`、`'Internal'`、`'External'` |
| **默认：** `'None'` |

### **A(q) 中的参数数量 (na)** — *A*(*q*) 多项式中估计参数的数量 `1`（默认）| 非负整数

指定 *A*(*q*) 多项式中估计参数 *na* 的数量。

#### 依赖关系

要启用此参数，需满足以下任一条件：

- 将 **历史** 设置为 `Infinite`，**模型结构** 设置为 `AR`、`ARX`、`ARMA` 或 `ARMAX`，并将 **初始估计** 设置为 `None` 或 `External`。
- 将 **历史** 设置为 `Finite`，**模型结构** 设置为 `AR` 或 `ARX`，并将 **初始估计** 设置为 `None` 或 `External`。

#### 编程用法

|  |
| --- |
| **模块参数：**`A0` |
| **类型：** 非负整数 |
| **默认：** `1` |

### **Number of Parameters in B(q) (nb)** — *B*(*q*) 多项式中估计参数的数量 `1`（默认）| 正整数向量

指定 *B*(*q*) 多项式中的估计参数数量 *nb*。

对于使用 ARX 模型结构的 MISO 系统，将 *nb* 指定为一个向量，其元素数量与输入数量相同。该向量的每个元素表示与对应输入相关联的 *B*(*q*) 多项式的阶数。例如，假设您有一个双输入 MISO 系统，其 *B*(*q*) 元素为：[B1B2]=[0b1100b21b22]。每个多项式开头的零表示每个输入的单个输入延迟（参见 **Initial B(q)** 参数说明）。*B1* 末尾的零用于使多项式长度相等，对估计没有影响。每个多项式的 *nb* 等于初始零之后的估计参数数量，即输入 1 为 1，输入 2 为 2。将 **Number of Parameters in B(q) (nb)** 指定为 `[1 2]`，将 **Input Delay (nk)** 指定为 `[1 1]`。

#### 依赖关系

要启用此参数，需满足以下任一条件：

- 将 **History** 设置为 `Infinite`，**Model Structure** 设置为 `ARX`、`ARMAX`、`BJ` 或 `OE`，并将 **Initial Estimate** 设置为 `None` 或 `External`。
- 将 **History** 设置为 `Finite`，**Model Structure** 设置为 `ARX` 或 `OE`，并将 **Initial Estimate** 设置为 `None` 或 `External`。

#### 编程使用

|  |
| --- |
| **模块参数：**`B0` |
| **类型：** 正整数 |
| **默认值：** `1` |

### **Number of Parameters in C(q) (nc)** — *C*(*q*) 多项式中估计参数的数量 `1`（默认）| 正整数

指定 *C*(*q*) 多项式中的估计参数数量 *nc*。

#### 依赖关系

要启用此参数，将 **History** 设置为 `Infinite`，**Model Structure** 设置为 `ARMA`、`ARMAX` 或 `BJ`，并将 **Initial Estimate** 设置为 `None` 或 `External`。

#### 编程使用

|  |
| --- |
| **模块参数：**`C0` |
| **类型：** 正整数 |
| **默认值：** `1` |

### **Number of Parameters in D(q) (nd)** — *D*(*q*) 多项式中估计参数的数量 `1`（默认）| 正整数

指定 *D*(*q*) 多项式中的估计参数数量 *nd*。

#### 依赖关系

要启用此参数，将 **History** 设置为 `Infinite`，**Model Structure** 设置为 `BJ`，并将 **Initial Estimate** 设置为 `None` 或 `External`。

#### 编程使用

|  |
| --- |
| **模块参数：**`D0` |
| **类型：** 正整数 |
| **默认值：** `1` |

### **Number of Parameters in F(q) (nf)** — *F*(*q*) 多项式中估计参数的数量 `1`（默认）| 正整数

指定 *F*(*q*) 多项式中的估计参数数量 *nf*。

#### 依赖关系

要启用此参数，将 **Initial Estimate** 设置为 `None` 或 `External`，并且满足以下任一条件：

- **History** 设置为 `Infinite`，**Model Structure** 设置为 `OE` 或 `BJ`，并将 **Initial Estimate** 设置为 `None` 或 `External`
- **History** 设置为 `Finite`，**Model Structure** 设置为 `OE`，并将 **Initial Estimate** 设置为 `None` 或 `External`

。

#### 编程使用

|  |
| --- |
| **模块参数：**`F0` |
| **类型：** 正整数 |
| **默认值：** `1` |

### **Input Delay (nk)** — 输入延迟 `1`（默认）| 非负整数向量

将输入延迟指定为一个整数，表示在输入影响输出之前发生的时间步数。此延迟在系统中也称为*死区时间*。该模块将输入延迟编码为 *B*(*q*) 多项式的固定前导零。有关更多信息，请参阅 *B*(*q*) 参数描述。

对于具有 ARX 模型结构的 MISO 系统，将 *nk* 指定为一个向量，其元素指定每个输入的延迟。此向量的长度为 *nu*，其中 *nu* 是输入的数量。

例如，假设您有一个双输入 MISO 系统，其 *B*(*q*) 元素为：[B1B2]=[0b11b1200b21]。多项式开头的零表示第一个输入的单采样延迟，以及第二个输入的双采样延迟（请参阅 **Initial B(q)** 参数描述）。每个多项式的 *nb* 等于初始零之后的估计参数数量，即输入 1 为 2，输入 2 为 1。将 **Input Delay (nk)** 指定为 `[1 2]`，将 **Number of Parameters in B(q) (nb)** 指定为 `[2 1]`。

#### 依赖关系

要启用此参数，请执行以下任一操作：

- 将 **History** 设置为 `Infinite`，将 **Model Structure** 设置为 `ARX`、`ARMAX`、`OE` 或 `BJ`，并将 **Initial Estimate** 设置为 `None` 或 `External`。
- 将 **History** 设置为 `Finite`，将 **Model Structure** 设置为 `ARX` 或 `OE`，并将 **Initial Estimate** 设置为 `None` 或 `External`。

#### 编程使用

|  |
| --- |
| **模块参数：**`nk` |
| **类型：**非负整数向量 |
| **默认值：**`1` |

### **Parameter Covariance Matrix** — 初始参数协方差 `1e4`（默认）| 标量 | 向量 | 矩阵

- 实正标量，*α* — 协方差矩阵是一个 *N*×*N* 对角矩阵，以 α 作为对角元素。
- 实正标量向量，[*α*(*a*),*α*(*b*),*α*(*c*), *α*(*d*), *α*(*f*)] — 协方差矩阵是一个 *N*×*N* 对角矩阵，以 [*α*(*a*),*α*(*b*),*α*(*c*),*α*(*d*), *α*(*f*)] 作为对角元素。*α*(*a*) 是 *A* 多项式每个系数的协方差向量。类似地，*α*(*b*)、*α*(*c*)、*α*(*d*) 和 *α*(*f*) 是分别包含 *B*、*C*、*D* 和 *F* 多项式系数协方差的向量。
- *N*×*N* 对称正定矩阵。

  *N* 可以是以下之一：

  - `AR` — *N* = *na*
  - `ARX` — N​=na+∑i=1Nunbi
  - `ARMA` — *N* = *na* + *nc*
  - `ARMAX` — *N* = *na* + *nb* + *nc*
  - `OE` — *N* = *nb* + *nf*
  - `BJ` — *N* = *nb* + *nc* + *nd* + *nf*

#### 依赖关系

要启用此参数，请设置

- **History** 为 `Infinite`
- **Initial Estimate** 为 `None` 或 `Internal`
- **Estimation Method** 为 `Forgetting Factor` 或 `Kalman Filter`

该模块在仿真开始时或每当 **Reset** 信号触发时使用此参数。

#### 编程使用

|  |
| --- |
| **模块参数：**`P0` |
| **类型：**标量、向量或矩阵 |
| **默认值：**`1e4` |

### **Initial A(q)** — *A*(*q*) 多项式系数的初始值 `[1 eps]`（默认）| 向量

将 *A*(*q*) 多项式系数的初始估计指定为长度为 *na*+1 的行向量。

*A* 的首项系数必须为 `1`。

#### 依赖关系

要启用此参数，请设置：

- **Model Structure** 为 `AR`、`ARX`、`ARMA` 或 `ARMAX`
- **Initial Estimate** 为 `Internal`

#### 编程使用

|  |
| --- |
| **模块参数：**`A0` |
| **类型：**实向量 |
| **默认值：**`[1 eps]` |

### **Initial B(q)** — *B*(*q*) 多项式系数的初始值 `[0 eps]`（默认）| 向量 | 矩阵

将 *B*(*q*) 多项式系数的初始估计值指定为长度为
*nb*+*nk* 的行向量。对于多输入模型，指定一个矩阵，其中第 *i* 行对应第 *i* 个输入。

该模块统计 *B*(*q*) 中的前导零，并将其解释为输入延迟 *nk*。这些零在整个估计过程中保持固定。*nb* 是 *B*(*q*) 中第一个非零元素之后的元素个数。该模块估计这 *nb* 个元素的值。

例如：

- `[0 eps]` 对应于 *nk*=1 和
  *nb*=1。
- `[0 0 eps]` 对应于 *nk*=2 和
  *nb*=1。
- `[0 0 eps 0 eps]` 对应于 *nk*=2 和
  *nb*=3。

默认值为 `[0 eps]`。

#### 依赖关系

要启用此参数，请设置：

- **Model Structure** 为 `ARX`、
  `ARMAX`、`OE` 或
  `BJ`
- **Initial Estimate** 为
  `Internal`

#### 编程用法

|  |
| --- |
| **模块参数：**`B0` |
| **类型：** 实数向量或矩阵 |
| **默认值：** `[0 eps]` |

### **Initial C(q)** — *C*(*q*) 多项式系数的初始值 `[1 eps]`（默认）| 向量

将 *C*(*q*) 多项式系数的初始估计值指定为长度为 *nc*+1 的行向量。

*C*(*q*) 的首项系数必须为
1。

这些系数必须定义稳定的离散时间多项式，即所有多项式根均位于单位圆内。

#### 依赖关系

要启用此参数，请设置：

- **History** 为 `Infinite`
- **Model Structure** 为 `ARMA`、
  `ARMAX` 或 `BJ`
- **Initial Estimate** 为
  `Internal`

#### 编程用法

|  |
| --- |
| **模块参数：**`C0` |
| **类型：** 实数向量 |
| **默认值：** `[1 eps]` |

### **Initial D(q)** — *D*(*q*) 多项式系数的初始值 `[1 eps]`（默认）| 向量

将 *D*(*q*) 多项式系数的初始估计值指定为长度为 *nd*+1 的行向量。

*D*(*q*) 的首项系数必须为
1。

这些系数必须定义稳定的离散时间多项式，即所有多项式根均位于单位圆内。

#### 依赖关系

要启用此参数，请设置：

- **History** 为 `Infinite`
- **Model Structure** 为
  `BJ`
- **Initial Estimate** 为
  `Internal`

#### 编程用法

|  |
| --- |
| **模块参数：**`D0` |
| **类型：** 实数向量 |
| **默认值：** `[1 eps]` |

### **Initial F(q)** — *F*(*q*) 多项式系数的初始值 `[1 eps]`（默认）| 向量

将 *F*(*q*) 多项式系数的初始估计值指定为长度为 *nf*+1 的行向量。

*F*(*q*) 的首项系数必须为
1。

这些系数必须定义稳定的离散时间多项式，即所有多项式根均位于单位圆内。

#### 依赖关系

要启用此参数，请设置：

- **Model Structure** 为 `OE` 或
  `BJ`
- **Initial Estimate** 为
  `Internal`

#### 编程用法

|  |
| --- |
| **模块参数：**`F0` |
| **类型：** 实数向量 |
| **默认值：** `[1 eps]` |

### **Initial Inputs** — 输入缓冲区的初始值 `0`（默认）| 矩阵

在使用有限历史（滑动窗口）估计时，指定输入缓冲区的初始值。缓冲区维度需容纳指定的窗口长度、该窗口内与多项式相关的回归量、输入延迟以及输入数量。这些元素决定了矩阵大小为：

- ARX 模型结构 —
  (*W*–1+max(*nb*)+max(*nk*))-by-*nu*
- OE 模型结构 —
  (*W*–1+*nb*+*nk*)-by-1

其中 *W* 是窗口长度，*nu* 是输入数量。*nb* 是 *B*(*q*) 多项式阶数的向量，*nk* 是输入延迟的向量。

当初始值设置为 `0` 时，模块用零填充缓冲区。

如果初始缓冲区设置为 `0` 或不包含足够的信息，您会在估计的初始阶段看到一条警告消息。该警告应在几个周期后清除。缓冲足够信息所需的周期数取决于多项式的阶数和输入延迟。如果警告持续存在，您应评估信号的内容。

模块在仿真开始时或每当 **Reset** 信号触发时使用此参数。

#### 依赖关系

要启用此参数，请设置

- **History** 为 `Finite`
- **Model Structure** 为 `ARX` 或
  `OE`
- **Initial Estimate** 为
  `Internal`

。

#### 编程使用

|  |
| --- |
| **模块参数：**`InitialInputs` |
| **类型：** 实数矩阵 |
| **默认值：** `0` |

### **Initial Outputs** — 测量输出缓冲区的初始值 `0`（默认）| 向量

在使用有限历史（滑动窗口）估计时，指定测量输出缓冲区的初始值。缓冲区维度需容纳指定的窗口长度以及该窗口内与多项式相关的回归量。

- AR 或 ARX 模型结构 —
  (*W*+*na*)-by-1 向量，其中
  *W* 是窗口长度，*na* 是
  *A*(*q*) 的多项式阶数。
- OE 模型结构 — (*W*+*nf*)-by-1
  向量，其中 *W* 是窗口长度，
  *nf* 是
  *F*(*q*) 的多项式阶数。

当初始值设置为 `0` 时，模块用零填充缓冲区。

如果初始缓冲区设置为 `0` 或不包含足够的信息，您会在估计的初始阶段看到一条警告消息。该警告应在几个周期后清除。缓冲足够信息所需的周期数取决于多项式的阶数和输入延迟。如果警告持续存在，您应评估信号的内容。

模块在仿真开始时或每当 **Reset** 信号触发时使用此参数。

#### 依赖关系

要启用此参数，请设置：

- **History** 为 `Finite`
- **Model Structure** 为 `AR`、
  `ARX` 或 `OE`
- **Initial Estimate** 为
  `Internal`

#### 编程使用

|  |
| --- |
| **模块参数：**`InitialOutputs` |
| **类型：** 实数向量 |
| **默认值：** `0` |

### 输入处理和采样时间

### **Input Processing** — 选择基于采样或基于帧的处理 `Sample-based`（默认）| `Frame-based`

- `Sample-based` 处理对一次流式传输一个采样的信号进行操作。
- `Frame-based` 处理对包含多个时间步采样的信号进行操作。许多机器传感器接口将多个采样打包并以帧的形式一起传输这些采样。
  `Frame-based` 处理允许您直接输入此数据，而无需先对其进行解包。

指定基于帧的数据会为您的一些数据输入端口和输出端口添加一个额外的 *M* 维度，其中 *M* 是一帧中的时间步数。这些端口是：

- **Inputs**
- **Output**
- **Error**

有关更多信息，请参阅端口中的端口描述。

#### 编程用法

|  |
| --- |
| **模块参数：**`InputProcessing` |
| **类型：** 字符向量、字符串 |
| **值：** `'Sample-based'`、`'Frame-based'` |
| **默认值：**`'Sample-based'` |

### **Sample Time** — 模块采样时间 `–1`（默认）| 正标量

指定数据采样时间，可以按基于采样的处理方式使用单个采样（*ts*），也可以按基于帧的处理方式使用帧（*tf* =
*M**ts*），其中 *M* 是帧长度。当您将 **Sample Time** 设置为其默认值 –1 时，模块会根据信号继承其
*ts* 或
*tf*。

将 **Sample Time** 指定为正标量以覆盖继承值。

#### 编程用法

|  |
| --- |
| **模块参数：**`Ts` |
| **类型：** 实标量 |
| **值：** `–1`、正标量 |
| **默认值：** `–1` |

### 算法和模块选项

#### 算法选项

### **History** — 选择无限或有限数据历史 `Infinite`（默认）| `Finite`

**History** 参数决定您使用哪种类型的递归算法：

- `Infinite` — 此类别中的算法旨在生成能够解释自仿真开始以来所有数据的参数估计。这些算法将历史信息保留在数据摘要中。模块在固定内存量内维护此摘要，该内存量不会随时间增长。

  模块提供多种 `Infinite` 类型的算法。选择此选项会启用 **Estimation Method** 参数，您可以通过该参数指定算法。
- `Finite` — 此类别中的算法旨在生成仅能解释有限数量过去数据采样的参数估计。模块使用有限窗口内的所有数据，一旦数据不再处于窗口范围内就将其丢弃。此方法也称为滑动窗口估计。

  模块提供一种 `Finite` 类型的算法。您只能将此选项与 `AR`、`ARX` 和 `OE` 模型结构一起使用。

  选择此选项会启用 **Window Length** 参数。

有关递归估计方法的更多信息，请参阅 Recursive Algorithms for Online Parameter Estimation。

#### 编程用法

|  |
| --- |
| **模块参数：**`History` |
| **类型：** 字符向量、字符串 |
| **值：** `'Infinite'`、`'Finite'` |
| **默认值：**`'Infinite'` |

### **Window Length** — 有限滑动窗口估计的窗口大小 `200`（默认）| 正整数

**Window Length** 参数决定用于有限历史（滑动窗口）估计方法的时间采样数量。请选择能够在估计性能与计算和内存负担之间取得平衡的窗口大小。确定大小的因素包括模型中参数的数量和时变特性。即使您使用基于帧的输入处理，也始终以采样为单位指定 **Window Length**。

**Window Length** 必须大于或等于估计参数的数量。

合适的窗口长度与您使用的是基于采样还是基于帧的输入处理无关。但是，当使用基于帧的处理时，**Window Length** 必须大于或等于帧中包含的采样（时间步）数量。

#### 依赖关系

要启用此参数，请将 **History** 设置为 `Finite`。

#### 编程用法

|  |
| --- |
| **模块参数：**`WindowLength` |
| **类型：** 正整数 |
| **默认值：** `200` |

### **Estimation Method** — 递归估计算法 `Forgetting Factor`（默认）| `Kalman Filter` | `Normalized Gradient` | `Gradient`

指定执行无限历史估计时使用的估计算法。当您选择这些方法中的任意一种时，模块会启用额外的相关参数。

遗忘因子和卡尔曼滤波算法比梯度法和归一化梯度法具有更高的计算量。然而，这些计算量更大的方法比梯度法具有更好的收敛特性。有关这些算法的更多信息，请参阅 Recursive Algorithms for Online Parameter Estimation。

#### 编程使用

|  |
| --- |
| **模块参数**：`EstimationMethod` |
| **类型**：character vector, string |
| **值**：`'Forgetting Factor'`,`'Kalman Filter'`,`'Normalized Gradient'`,`'Gradient'` |
| **默认值**：`'Forgetting Factor'` |

### **Forgetting Factor** — 使用遗忘因子对旧数据进行折扣 `1`（默认）| (0 1] 范围内的正标量

遗忘因子 *λ* 指定在估计中是否以及有多少旧数据被折扣。假设系统在 *T0* 个采样点上保持近似恒定。您可以选择 *λ* 使得：

T0=11−λ

- 设置 *λ* = 1 对应于“无遗忘”并估计恒定系数。
- 设置 *λ* < 1 意味着过去的测量对参数估计的重要性较低，可以被“遗忘”。设置 *λ* < 1 以估计时变系数。

*λ* 的典型选择在 [0.98 0.995] 范围内。

#### 依赖关系

要启用此参数，请将 **History** 设置为 `Infinite`，并将 **Estimation Method** 设置为 `Forgetting Factor`。

#### 编程使用

|  |
| --- |
| **模块参数**：`AdaptationParameter` |
| **类型**：scalar |
| **值**：(0 1] range |
| **默认值**：`1` |

### **Process Noise Covariance** — 卡尔曼滤波估计方法的过程噪声协方差 `1`（默认）| 非负标量 | 非负标量向量 | 对称半正定矩阵

**Process Noise Covariance** 为卡尔曼滤波估计规定噪声协方差矩阵的元素和结构。使用 *N* 作为要估计的参数数量，将 **Process Noise Covariance** 指定为以下之一：

- 实数非负标量 *α* — 协方差矩阵为 *N*×*N* 对角矩阵，以 *α* 为对角元素。
- 实数非负标量向量 [*α*1,...,*α**N*] — 协方差矩阵为 *N*×*N* 对角矩阵，以 [*α*1,...,*α**N*] 为对角元素。
- *N*×*N* 对称半正定矩阵。

卡尔曼滤波算法将参数视为动态系统的状态，并使用卡尔曼滤波器估计这些参数。**Process Noise Covariance** 是作用在这些参数上的过程噪声的协方差。噪声协方差矩阵中的零值对应于恒定系数或参数。大于 0 的值对应于时变参数。对于快速变化的参数使用较大的值。但是，预期较大的值会导致参数估计更加嘈杂。默认值为 1。

#### 依赖关系

要启用此参数，请将 **History** 设置为 `Infinite`，并将 **Estimation Method** 设置为 `Kalman Filter`。

#### 编程使用

|  |
| --- |
| **模块参数**：`AdaptationParameter` |
| **类型**：scalar, vector, matrix |
| **默认值**：`1` |

### **Adaptation Gain** — 梯度估计方法的自适应增益指定 `1`（默认）| 正标量

自适应增益 *γ* 缩放新测量数据对梯度和归一化梯度方法的估计结果的影响。当您的测量可信时，换句话说具有高信噪比时，为 *γ* 指定较大的值。然而，将 *γ* 设置得太高可能导致参数估计发散。即使测量无噪声，这种发散也是可能的。

当 **Estimation Method** 为 `NormalizedGradient` 时，**Adaptation Gain** 应小于 2。对于任一梯度方法，如果误差随时间增长（换句话说，估计正在发散），或者参数估计频繁跳动，请考虑减小 **Adaptation Gain**。

#### 依赖关系

要启用此参数，请将 **History** 设置为 `Infinite`，并将 **Estimation Method** 设置为 `Normalized Gradient` 或 `Gradient`。

#### 编程使用

|  |
| --- |
| **模块参数**：`AdaptationParameter` |
| **类型**：scalar |
| **默认值**：`1` |

### **Normalization Bias** — 归一化梯度估计方法的自适应增益缩放偏置 `eps`（默认）| 非负标量

归一化梯度算法在每一步通过梯度向量二范数的平方来缩放自适应增益。如果梯度接近零，接近零的分母可能导致估计参数跳变。**Normalization Bias** 是引入分母以防止这些跳变的项。如果您观察到估计参数跳变，请增大 **Normalization Bias**。

#### 依赖关系

要启用此参数，请将 **History** 设置为 `Infinite`，并将 **Estimation Method** 设置为 `Normalized Gradient`。

#### 编程使用

|  |
| --- |
| **模块参数**：`NormalizationBias` |
| **类型**：scalar |
| **默认值**：`eps` |

#### Block Options

### **Output estimation error** — 向模块添加 Error 输出端口 `off`（默认）| on

使用 **Error** 输出端口信号来验证估计。对于给定的时间步 *t*，估计误差 *e*(*t*) 计算如下：

e(t)=y(t)−yest(t)，

其中 *y*(*t*) 是您提供的测量输出，*yest*(*t*) 是使用回归量 *H*(*t*) 和参数估计 *θ*(*t*-1) 得到的估计输出。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputError` |
| **类型**：character vector, string |
| **值**：`'off'`,`'on'`, |
| **默认值**：`'off'` |

### **Output parameter covariance matrix** — 向模块添加 covariance 输出端口 `off`（默认）| on

使用 **Covariance** 输出端口信号来检查参数估计不确定性。该软件计算参数协方差 `P`，假设残差 *e*(*t*) 为白噪声，并且这些残差的方差为 1。

`P` 的解释取决于您在 **History** 和 **Estimation Method** 中指定的估计方法，如下所示：

- 如果 **History** 为 `Infinite`，则您的 **Estimation Method** 选择会导致：

  - `Forgetting Factor` — (*R2*/2)`P` 近似等于估计参数的协方差矩阵，其中 *R2* 是残差的真实方差。该模块通过 **Error** 端口返回这些残差。
  - `Kalman Filter` — *R2*`P` 是估计参数的协方差矩阵，并且 *R1*/*R2* 是参数变化的协方差矩阵。这里，*R1* 是您在 **Parameter Covariance Matrix** 中指定的协方差矩阵。
  - `Normalized Gradient` 或 `Gradient` — 协方差 `P` 不可用。
- 如果 **History** 为 `Finite`（滑动窗口估计）— *R2*`P` 是估计参数的协方差。滑动窗口算法在参数估计过程中不使用此协方差。但是，该算法确实会计算协方差以供输出，以便您可以将其用于统计评估。

#### 程序化使用

|  |
| --- |
| **模块参数：**`OutputP` |
| **类型：** 字符向量、字符串 |
| **值：**`'off'`、`'on'` |
| **默认值：** `'off'` |

### **Add enable port** — 向模块添加使能输入端口 `off`（默认）| `on`

使用 **Enable** 信号提供控制信号，以启用或禁用参数估计。模块在参数估计启用的每个时间步估计参数值。如果在给定步 *t* 禁用参数估计，则软件不会更新该时间步的参数。此时，模块输出包含上一次估计的参数值。

例如，在以下情况下可以使用此选项：

- 回归量或输出信号变得过于嘈杂，或在某些时间步不包含信息
- 系统进入参数值不随时间变化的模式

#### 程序化使用

|  |
| --- |
| **模块参数：**`AddEnablePort` |
| **类型：** 字符向量、字符串 |
| **值：**`'off'`、`'on'` |
| **默认值：** `'off'` |

### **External reset** — 指定外部复位的触发条件 `None`（默认）| `Rising` | `Falling` | `Either` | `Level` | `Level hold`

设置 **External reset** 参数可同时添加 **Reset** 输入端口，并指定触发算法状态复位到其指定初始值的输入端口信号条件。例如，如果由于测量信号中缺乏足够的激励或信息而导致参数协方差变得过大，则复位估计。**External reset** 参数决定复位的时机。

假设在时间步 *t* 复位模块。如果模块在 *t* 启用，则软件使用 **Initial Estimate** 中指定的初始参数值来估计参数值。换句话说，在 *t* 时，模块使用初始估计和输入端口的当前值执行参数更新。

如果模块在 *t* 禁用且您复位模块，则模块输出包含 **Initial Estimate** 中指定的值。

将此选项指定为以下之一：

- `None` — 算法状态和估计参数不复位。
- `Rising` — 当控制信号从负值或零值上升到正值时触发复位。如果初始值为负，上升到零会触发复位。
- `Falling` — 当控制信号从正值或零值下降到负值时触发复位。如果初始值为正，下降到零会触发复位。
- `Either` — 当控制信号上升或下降时触发复位。
- `Level` — 在以下任一情况下触发复位：

  - 控制信号在当前时间步非零。
  - 控制信号从前一时间步的非零变为当前时间步的零。
- `Level hold` — 当控制信号在当前时间步非零时触发复位。

当您选择除 `None` 以外的任何选项时，软件会向模块添加一个 Reset 输入端口。您向此输入端口提供复位控制输入信号。

#### 程序化使用

|  |
| --- |
| **模块参数：**`ExternalReset` |
| **类型：** 字符向量、字符串 |
| **值：**`'None'`、`'Rising'`、`'Falling'`、`'Either'`、`'Level'`、`'Level hold'` |
| **默认值：** `'None'` |
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

估计输入-输出和时间序列多项式模型系数

### 模型结构

使用 Recursive Polynomial Model Estimator 模块估计离散时间输入-输出多项式和时序模型。

这些模型结构包括：

- AR — *A*(*q*)*y*(*t*)
  = *e*(*t*)
- ARMA — *A*(*q*)*y*(*t*)
  =
  *C*(*q*)*e*(*t*)
- ARX — *A*(*q*)*y*(*t*)
  =
  *B*(*q*)*u*(*t*
  – *nk*) +
  *e*(*t*)
- ARMAX — *A*(*q*)*y*(*t*)
  =
  *B*(*q*)*u*(*t*
  – *nk*) +
  *C*(*q*)*e*(*t*)
- OE — y(t)=B(q)F(q)u(t−nk)+e(t)
- BJ — y(t)=B(q)F(q)u(t−nk)+​C(q)D(q)e(t)

*q* 是时移算子，*nk* 是输入延迟。*u*(*t*) 是输入，*y*(*t*) 是输出，*e*(*t*) 是误差。对于 MISO 模型，*B*(*q*) 多项式的数量与输入数量相同。

这些模型的阶数对应于最大时移数量，由 *q* 的指数表示。例如，阶数 *na* 在 *A*(*q*) 多项式中的表示为：

1 +
*a1**q*-1
+
*a2**q*-2
+ … +
*ana**q*-*na*。

*C*(*q*)、*D*(*q*) 和 *F*(*q*) 多项式及其对应的阶数 *nc*、*nd* 和 *nf* 也适用等效表示。

*B*(*q*) 多项式与其他多项式不同，因为该多项式作用于输入并包含系统零点。对于 *B*(*q*)，阶数 *nb* 是多项式 *B*(*q*) + 1 的阶数：

*b*1 +
*b2**q*-1
+
*b3**q*-2
+ … +
*bnb**q*-(*nb*-1)。

阶数 *na*、*nb*、*nc*、*nd*、*nf* 和输入延迟 *nk* 是预先已知的。将这些值指定为模块参数。分别通过 **Inputs** 和 **Outputs** 输入端口提供 *u*(*t*) 和 *y*(*t*)。该模块估计模型结构所使用的 *A*(*q*)、*B*(*q*)、*C*(*q*)、*D*(*q*) 和 *F*(*q*) 系数集，并将它们输出到 **Parameters** 输出端口。在估计过程中，该模块将估计的 *C*、*D* 和 *F* 多项式约束在根位于单位圆内的稳定区域，同时允许估计的 *A* 和 *B* 多项式不稳定。**Parameters** 输出端口提供具有以下元素的 bus 信号：

- A — 包含 [1
  *a1*(*t*) ...
  *ana*(*t*)] 的向量。
- B — 包含 [01 …
  0*nk*,
  *b1*(*t*) ...
  *bnb*(*t*)] 的向量。对于 MISO 数据，*B* 是一个矩阵，其中第 *i* 行参数对应于第 *i* 个输入。
- C — 包含 [1
  *c1*(*t*) ...
  *cnc*(*t*)] 的向量。
- D — 包含 [1
  *d1*(*t*) ...
  *dnd*(*t*)] 的向量。
- F — 包含 [1
  *f1*(*t*) ...
  *fnf*(*t*)] 的向量。

例如，假设您要估计以下 SISO ARMAX 模型的系数：

*y*(*t*) +
*a1**y*(*t*
– 1)
+...+*ana**y*(*t*
– *na*) =
*b1**u*(*t*
– *nk*) + … +
*bnb**u*(*t*
– *nb* – *nk* + 1) +
*e*(*t*) +
*c1**e*(*t*
– 1) + … +
*cnc**e*(*t*
– *nc*)

*y*、*u*、*na*、*nb*、*nc* 和 *nk* 是您提供给该模块的已知量。对于每个时间步 *t*，该模块估计 *A*、*B* 和 *C* 参数值，仅将 *C* 多项式约束在稳定区域。然后，该模块使用 **Parameters** 输出端口输出这些估计值。

### 模块功能

该模块支持多种估计方法和数据输入格式。该模块可以为 *θ* 提供无限历史 [1] 和有限历史 [2]（也称为滑动窗口）估计。该模块中的可配置选项包括：

- 多输入（仅 ARX 模型结构）— 请参阅 **Inputs** 端口。
- 基于采样或基于帧的数据格式 — 请参阅 **Input Processing** 参数。
- 多种无限历史估计方法 [1] — 请参阅 **Estimation Method** 参数。
- 无限历史（所有模型结构）或有限历史（仅 AR、ARX 或 OE 模型结构）— 请参阅 **History** 参数。
- 初始条件、使能标志和复位触发 — 请参阅 **Initial Estimate**、**Add enable port** 和 **External Reset** 参数。

有关估计方法的更多信息，请参阅 Recursive Algorithms for Online Parameter Estimation。
