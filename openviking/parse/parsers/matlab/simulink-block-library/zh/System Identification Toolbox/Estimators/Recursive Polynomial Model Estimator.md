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

### 输入

### **Inputs** — 输入信号向量 | 矩阵

输入信号 *u*(*t*)。**Input Processing** 参数和输入数量 *nu* 定义信号的维度。只有 ARX 模型结构可以有多个输入，且 *nu* 大于 1。

- 基于采样的输入处理和 *nu* 个输入 — *nu*×1 向量
- 基于帧的输入处理，每帧 *M* 个样本和 *nu* 个输入 — *M*×*nu* 矩阵

#### 依赖关系

要启用此端口，将 **Model Structure** 参数设置为 `ARX`、`ARMAX`、`BJ` 或 `OE`。

**数据类型：** `single` | `double`

### **Output** — 测量输出信号 标量 | 向量

测量输出信号 *y*(*t*)。**Input Processing** 参数定义信号的维度：

- 基于采样的输入处理 — 标量
- 基于帧的输入处理，每帧 *M* 个样本 — *M*×1 向量

**数据类型：** `single` | `double`

### **Enable** — 启用估计更新 `true`（默认） | `false`

外部信号，允许您启用和禁用估计更新。如果信号值为：

- `true` — 估计并输出该时间步的参数值。
- `false` — 不估计参数值，并输出最近一次先前估计的值。

#### 依赖关系

要启用此端口，选择 **Add enable port** 参数。

**数据类型：** `single` | `double` | `Boolean` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32`

### **Reset** — 复位触发 标量

将参数估计复位到其初始条件。**External reset** 参数的值决定触发类型。触发类型决定复位是在上升、下降、上升或下降、电平信号上发生，还是在电平保持时发生。

#### 依赖关系

要启用此端口，在 **External reset** 下拉列表中选择除 `None` 之外的任何选项。

**数据类型：** `single` | `double` | `Boolean` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **InitialParameters** — 初始参数估计 `bus` 对象

初始参数估计，由模块外部源提供。模块在仿真开始时或当您使用 **Reset** 信号触发算法复位时使用此输入端口。

有关 **InitialParameters** 总线对象内容的信息，请参阅 **Parameters** 端口描述。

#### 依赖关系

要启用此端口，将 **History** 设置为 `Infinite`，并将 **Initial Estimate** 设置为 `External`。

**数据类型：** `single` | `double`

### **InitialCovariance** — 参数的初始协方差 正标量（默认） | 正标量向量 | 对称正定矩阵

初始参数协方差，由模块外部源提供。有关详细信息，请参阅 **Parameter Covariance Matrix** 参数。模块在仿真开始时或当您使用 **Reset** 信号触发算法复位时使用此输入端口。

#### 依赖关系

要启用此端口，设置以下参数：

- **History** 为 `Infinite`
- **Estimation Method** 为 `Forgetting Factor` 或 `Kalman Filter`
- **Initial Estimate** 为 `External`

**数据类型：** `single` | `double`

### **InitialInputs** — 输入矩阵的初始值

使用有限历史（滑动窗口）估计时的初始输入集，由外部源提供。

- 如果 **Model Structure** 为 `ARX`，则此端口的信号必须是 (*W*–1+max(*nb*)+max(*nk*))×*nu* 矩阵，其中 *W* 是窗口长度，*nu* 是输入数量。*nb* 是 *B*(*q*) 多项式阶数向量，*nk* 是输入延迟向量。
- 如果 **Model Structure** 为 `OE`，则此端口的信号必须是 (*W*–1+*nb*+*nk*)×1 向量，其中 *W* 是窗口长度。*nb* 是 *B*(*q*) 多项式阶数向量，*nk* 是输入延迟向量。

模块在仿真开始时或每当 **Reset** 信号触发时使用此输入端口。

如果初始缓冲区设置为 `0` 或包含的信息不足，您会在估计的初始阶段看到警告消息。该警告应在几个周期后清除。缓冲足够信息所需的周期数取决于多项式的阶数和输入延迟。如果警告持续存在，您应评估信号的内容。

#### 依赖关系

要启用此端口，设置：

- **History** 为 `Finite`
- **Model Structure** 为 `ARX` 或 `OE`
- **Initial Estimate** 为 `External`

**数据类型：** `single` | `double`

### **InitialOutputs** — 测量输出缓冲区向量的初始值

使用有限历史（滑动窗口）估计时的初始输出测量集，由外部源提供。

- 如果 **Model Structure** 为 `AR` 或 `ARX`，则此端口的信号必须是 (*W*+*na*)×1 向量，其中 *W* 是窗口长度，*na* 是 *A*(*q*) 的多项式阶数。
- 如果 **Model Structure** 为 `OE`，则此端口的信号必须是 (*W*+*nf*)×1 向量，其中 *W* 是窗口长度，*nf* 是 *F*(*q*) 的多项式阶数。

模块在仿真开始时或每当 **Reset** 信号触发时使用此输入端口。

如果初始缓冲区设置为 `0` 或包含的信息不足，您会在估计的初始阶段看到警告消息。该警告应在几个周期后清除。缓冲足够信息所需的周期数取决于多项式的阶数和输入延迟。如果警告持续存在，您应评估信号的内容。

#### 依赖关系

要启用此端口，设置：

- **History** 为 `Finite`
- **Model Structure** 为 `AR`、`ARX` 或 `OE`
- **Initial Estimate** 为 `External`

**数据类型：** `single` | `double`

### 输出

### **Parameters** — 估计参数 `bus` 对象

估计的多项式系数，以总线形式返回。该总线为 *A*、*B*、*C*、*D* 和 *F* 多项式各包含一个元素，这些多项式对应于您在 **Model Structure** 中指定的结构（参见 Model Structures）。

每个总线元素都是一个向量信号，包含关联的多项式系数。例如，*A* 元素包含 [1 *a1*(*t*) ... *ana*(*t*)]。

估计的 *C*、*D* 和 *F* 值被约束为稳定的离散时间多项式。也就是说，这些多项式的所有根都在单位圆内。估计的 *A* 和 *B* 多项式允许不稳定。

**数据类型：** `single` | `double`

### **Error** — 估计误差 标量 | 向量

估计误差，以下列形式返回：

- 标量 — 基于采样的输入处理
- *M*×1 向量 — 基于帧的输入处理，每帧 *M* 个样本

#### 依赖关系

要启用此端口，选择 **Output estimation error** 参数。

**数据类型：** `single` | `double`

### **Covariance** — 参数估计误差协方差 P 矩阵

参数估计误差协方差 *P*，以 *N*×*N* 矩阵返回，其中 *N* 是参数数量。有关详细信息，请参阅 **Output Parameter Covariance Matrix** 参数。

#### 依赖关系

要启用此端口：

- 选择 **Output parameter covariance matrix** 参数。
- 如果 **History** 为 `Infinite`，将 **Estimation Method** 设置为 `Forgetting Factor` 或 `Kalman Filter`。

**数据类型：** `single` | `double`

## 参数

### Model Structure

估计的模型结构，指定为以下之一：

- `ARX` — SISO 或 MISO ARX 模型
- `ARMAX` — SISO ARMAX 模型
- `OE` — SISO OE 模型
- `BJ` — SISO BJ 模型
- `AR` — 时间序列 AR 模型
- `ARMA` — 时间序列 ARMA 模型

### 模型参数

### **Initial Estimate** — 初始参数估计的来源 `None`（默认） | `Internal` | `External`

指定如何向模块提供初始参数估计：

- `None` — 不指定初始估计。

  模块使用 `0` 作为初始参数估计。

  根据您选择的模型结构和估计方法，指定模块启用的参数。

  - 根据您的 **Model Structure** 指定模块启用的一组 **Number of Parameters ()** 参数。例如，如果您的 **Model Structure** 设置为 `AR`，请指定 **Number of Parameters in A(q) (na)** 参数。
  - 当您的模型结构使用 *B*(*q*) 元素时，指定模块启用的 **Input Delay (nk)** 参数。
  - 如果 **Estimation Method** 为 `Forgetting Factor` 或 `Kalman Filter`，请指定 **Parameter Covariance Matrix**。
- `Internal` — 在模块内部指定初始参数估计。

  - 根据您的 **Model Structure** 和 **History** 指定模块启用的初始参数值 **Initial ()** 参数。例如，如果您的 **Model Structure** 设置为 `AR` 且 **History** 为 `Infinite`，请指定 **Initial A(q)** 参数。
  - 当您的模型结构使用 *B*(*q*) 元素时，指定模块启用的 **Input Delay (nk)** 参数。
  - 如果 **Estimation Method** 为 `Forgetting Factor` 或 `Kalman Filter`，请指定 **Parameter Covariance Matrix** 参数。
  - 如果 **History** 为 `Finite`，请指定 **Initial Inputs** 参数（仅 `ARX` 和 `OE`）以及 **Initial Outputs** 参数（`ARX`、`AR` 和 `OE`）。
- `External` — 将初始参数估计指定为模块的输入信号。

  根据您的 **Model Structure** 指定模块启用的 **Number of Parameters ()** 参数。您对 **Model Structure** 和 **History** 参数的设置决定要连接到相关端口的信号：

  - 如果 **History** 为 `Infinite` — **InitialParameters** 和 **InitialCovariance**
  - 如果 **History** 为 `Finite` — `AR`、`ARX` 和 `OE` 模型结构的 **InitialOutputs**，以及 `ARX` 和 `OE` 模型结构的 **InitialInputs**

#### 编程使用

|  |
| --- |
| **模块参数：**`InitialEstimateSource` |
| **类型：**character vector, string |
| **值：**`'None'`, `'Internal'`, `'External'` |
| **默认：**`'None'` |

### **Number of Parameters in A(q) (na)** — *A*(*q*) 多项式中的估计参数数量 `1`（默认） | 非负整数

指定 *A*(*q*) 多项式中的估计参数数量 *na*。

#### 依赖关系

要启用此参数，请执行以下任一操作：

- 将 **History** 设置为 `Infinite`，将 **Model Structure** 设置为 `AR`、`ARX`、`ARMA` 或 `ARMAX`，并将 **Initial Estimate** 设置为 `None` 或 `External`。
- 将 **History** 设置为 `Finite`，将 **Model Structure** 设置为 `AR` 或 `ARX`，并将 **Initial Estimate** 设置为 `None` 或 `External`。

#### 编程使用

|  |
| --- |
| **模块参数：**`A0` |
| **类型：**非负整数 |
| **默认：**`1` |

### **Number of Parameters in B(q) (nb)** — *B*(*q*) 多项式中的估计参数数量 `1`（默认） | 正整数向量

指定 *B*(*q*) 多项式中的估计参数数量 *nb*。

对于使用 ARX 模型结构的 MISO 系统，将 *nb* 指定为元素数量与输入数量相同的向量。此向量的每个元素表示与对应输入关联的 *B*(*q*) 多项式的阶数。例如，假设您有一个双输入 MISO 系统，其 *B*(*q*) 元素为：[B1B2]=[0b1100b21b22]。每个多项式开头的零表示每个输入的单个输入延迟（参见 **Initial B(q)** 参数描述）。*B1* 中的尾随零用于使多项式长度相等，并且对估计没有影响。每个多项式的 *nb* 等于初始零之后的估计参数数量，即输入 1 为 1，输入 2 为 2。将 **Number of Parameters in B(q) (nb)** 指定为 `[1 2]`，并将 **Input Delay (nk)** 指定为 `[1 1]`。

#### 依赖关系

要启用此参数，请执行以下任一操作：

- 将 **History** 设置为 `Infinite`，将 **Model Structure** 设置为 `ARX`、`ARMAX`、`BJ` 或 `OE`，并将 **Initial Estimate** 设置为 `None` 或 `External`。
- 将 **History** 设置为 `Finite`，**Model Structure** 为 `ARX` 或 `OE`，并将 **Initial Estimate** 设置为 `None` 或 `External`。

#### 编程使用

|  |
| --- |
| **模块参数：**`B0` |
| **类型：**正整数 |
| **默认：**`1` |

### **Number of Parameters in C(q) (nc)** — *C*(*q*) 多项式中的估计参数数量 `1`（默认） | 正整数

指定 *C*(*q*) 多项式中的估计参数数量 *nc*。

#### 依赖关系

要启用此参数，将 **History** 设置为 `Infinite`，将 **Model Structure** 设置为 `ARMA`、`ARMAX` 或 `BJ`，并将 **Initial Estimate** 设置为 `None` 或 `External`。

#### 编程使用

|  |
| --- |
| **模块参数：**`C0` |
| **类型：**正整数 |
| **默认：**`1` |

### **Number of Parameters in D(q) (nd)** — *D*(*q*) 多项式中的估计参数数量 `1`（默认） | 正整数

指定 *D*(*q*) 多项式中的估计参数数量 *nd*。

#### 依赖关系

要启用此参数，将 **History** 设置为 `Infinite`，将 **Model Structure** 设置为 `BJ`，并将 **Initial Estimate** 设置为 `None` 或 `External`。

#### 编程使用

|  |
| --- |
| **模块参数：**`D0` |
| **类型：**正整数 |
| **默认：**`1` |

### **Number of Parameters in F(q) (nf)** — *F*(*q*) 多项式中的估计参数数量 `1`（默认） | 正整数

指定 *F*(*q*) 多项式中的估计参数数量 *nf*。

#### 依赖关系

要启用此参数，将 **Initial Estimate** 设置为 `None` 或 `External`，并且满足以下任一条件：

- **History** 为 `Infinite`，**Model Structure** 为 `OE` 或 `BJ`，并且 **Initial Estimate** 为 `None` 或 `External`
- **History** 为 `Finite`，**Model Structure** 为 `OE`，并且 **Initial Estimate** 为 `None` 或 `External`

.

#### 编程使用

|  |
| --- |
| **模块参数：**`F0` |
| **类型：**正整数 |
| **默认：**`1` |

### **Input Delay (nk)** — 输入延迟 `1`（默认） | 非负整数向量

将输入延迟指定为整数，表示输入影响输出之前发生的时间步数。此延迟在系统中也称为 *dead time*。模块将输入延迟编码为 *B*(*q*) 多项式的固定前导零。有关更多信息，请参阅 *B*(*q*) 参数描述。

对于使用 ARX 模型结构的 MISO 系统，将 *nk* 指定为一个向量，其元素指定每个输入的延迟。此向量的长度为 *nu*，其中 *nu* 是输入数量。

例如，假设您有一个双输入 MISO 系统，其 *B*(*q*) 元素为：[B1B2]=[0b11b1200b21]。多项式开头的零表示第一个输入的单个样本延迟，以及第二个输入的两个样本延迟（参见 **Initial B(q)** 参数描述）。每个多项式的 *nb* 等于初始零之后的估计参数数量，即输入 1 为 2，输入 2 为 1。将 **Input Delay (nk)** 指定为 `[1 2]`，并将 **Number of Parameters in B(q) (nb)** 指定为 `[2 1]`。

#### 依赖关系

要启用此参数，请执行以下任一操作：

- 将 **History** 设置为 `Infinite`，将 **Model Structure** 设置为 `ARX`、`ARMAX`、`OE` 或 `BJ`，并将 **Initial Estimate** 设置为 `None` 或 `External`。
- 将 **History** 设置为 `Finite`，将 **Model Structure** 设置为 `ARX` 或 `OE`，并将 **Initial Estimate** 设置为 `None` 或 `External`。

#### 编程使用

|  |
| --- |
| **模块参数：**`nk` |
| **类型：**非负整数向量 |
| **默认：**`1` |

### **参数协方差矩阵** — 初始参数协方差 `1e4`（默认） | scalar | vector | matrix

- Real positive scalar, *α* —
  协方差矩阵是 *N*×*N* diagonal matrix，其中 α 为对角元素。
- Vector of real positive scalars,
  [*α*(*a*),*α*(*b*),*α*(*c*),
  *α*(*d*),
  *α*(*f*)] — 协方差矩阵是
  *N*×*N* diagonal matrix，其中
  [*α*(*a*),*α*(*b*),*α*(*c*),*α*(*d*),
  *α*(*f*)] 为对角元素。
  *α*(*a*) 是 *A* 多项式每个系数的协方差 vector。类似地，
  *α*(*b*)，
  *α*(*c*)，
  *α*(*d*) 和
  *α*(*f*) 分别是包含 *B*、*C*、
  *D* 和 *F* 多项式系数协方差的 vector。
- *N*×*N* symmetric
  positive-definite matrix。

  *N* 可以是以下之一：

  - `AR` — *N* = *na*
  - `ARX` — N​=na+∑i=1Nunbi
  - `ARMA` — *N* = *na* + *nc*
  - `ARMAX` — *N* = *na* + *nb* + *nc*
  - `OE` — *N* = *nb* + *nf*
  - `BJ` — *N* = *nb* + *nc* + *nd* + *nf*

#### 依赖项

要启用此参数，请设置

- **历史** 为 `Infinite`
- **初始估计** 为 `None`
  或 `Internal`
- **估计方法** 为 `Forgetting
  Factor` 或 `Kalman Filter`

模块在仿真开始时或每当 **Reset** 信号触发时使用此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：**`P0` |
| **类型：** scalar, vector, or matrix |
| **默认：** `1e4` |

### **初始 A(q)** — *A*(*q*) 多项式系数的初始值 `[1 eps]`（默认） | vector

将 *A*(*q*) 多项式系数的初始估计指定为长度为 *na*+1 的 row vector。

*A* 的首项系数必须为 `1`。

#### 依赖项

要启用此参数，请设置：

- **模型结构** 为 `AR`、
  `ARX`、`ARMA` 或
  `ARMAX`
- **初始估计** 为 `Internal`

#### 程序化使用

|  |
| --- |
| **模块参数：**`A0` |
| **类型：** real vector |
| **默认：** `[1 eps]` |

### **初始 B(q)** — *B*(*q*) 多项式系数的初始值 `[0 eps]`（默认） | vector | matrix

将 *B*(*q*) 多项式系数的初始估计指定为长度为
*nb*+*nk* 的 row vector。对于多输入模型，指定一个
matrix，其中第 *i* 行对应第 *i* 个输入。

模块计算 *B*(*q*) 中的前导零，并将其解释为输入延迟 *nk*。这些零在整个估计过程中固定。*nb* 是 *B*(*q*) 中第一个非零元素之后的元素数。模块估计这 *nb* 个元素的值。

例如：

- `[0 eps]` 对应于 *nk*=1 且
  *nb*=1。
- `[0 0 eps]` 对应于 *nk*=2 且
  *nb*=1。
- `[0 0 eps 0 eps]` 对应于 *nk*=2 且
  *nb*=3。

默认值为 `[0 eps]`。

#### 依赖项

要启用此参数，请设置：

- **模型结构** 为 `ARX`、
  `ARMAX`、`OE` 或 `BJ`
- **初始估计** 为
  `Internal`

#### 程序化使用

|  |
| --- |
| **模块参数：**`B0` |
| **类型：** real vector or matrix |
| **默认：** `[0 eps]` |

### **初始 C(q)** — *C*(*q*) 多项式系数的初始值 `[1 eps]`（默认） | vector

将 *C*(*q*) 多项式系数的初始估计指定为长度为 *nc*+1 的 row vector。

*C*(*q*) 的首项系数必须为
1。

系数必须定义稳定的离散时间多项式，即所有多项式根都在单位圆内。

#### 依赖项

要启用此参数，请设置：

- **历史** 为 `Infinite`
- **模型结构** 为 `ARMA`、
  `ARMAX` 或 `BJ`
- **初始估计** 为
  `Internal`

#### 程序化使用

|  |
| --- |
| **模块参数：**`C0` |
| **类型：** real vector |
| **默认：** `[1 eps]` |

### **初始 D(q)** — *D*(*q*) 多项式系数的初始值 `[1 eps]`（默认） | vector

将 *D*(*q*) 多项式系数的初始估计指定为长度为 *nd*+1 的 row vector。

*D*(*q*) 的首项系数必须为
1。

系数必须定义稳定的离散时间多项式，即所有多项式根都在单位圆内。

#### 依赖项

要启用此参数，请设置：

- **历史** 为 `Infinite`
- **模型结构** 为
  `BJ`
- **初始估计** 为
  `Internal`

#### 程序化使用

|  |
| --- |
| **模块参数：**`D0` |
| **类型：** real vector |
| **默认：** `[1 eps]` |

### **初始 F(q)** — *F*(*q*) 多项式系数的初始值 `[1 eps]`（默认） | vector

将 *F*(*q*) 多项式系数的初始估计指定为长度为 *nf*+1 的 row vector。

*F*(*q*) 的首项系数必须为
1。

系数必须定义稳定的离散时间多项式，即所有多项式根都在单位圆内。

#### 依赖项

要启用此参数，请设置：

- **模型结构** 为 `OE` 或
  `BJ`
- **初始估计** 为
  `Internal`

#### 程序化使用

|  |
| --- |
| **模块参数：**`F0` |
| **类型：** real vector |
| **默认：** `[1 eps]` |

### **初始输入** — 输入缓冲区的初始值 `0`（默认） | matrix

在使用有限历史（滑动窗口）估计时，指定输入缓冲区的初始值。缓冲区维度适应指定的窗口长度、该窗口内与多项式关联的回归量、输入延迟以及输入数量。这些元素决定 matrix 大小为：

- ARX 模型结构 —
  (*W*–1+max(*nb*)+max(*nk*))-by-*nu*
- OE 模型结构 —
  (*W*–1+*nb*+*nk*)-by-1

其中 *W* 是窗口长度，*nu* 是输入数量。*nb* 是 *B*(*q*) 多项式阶数的 vector，*nk* 是输入延迟的 vector。

当初始值设置为 `0` 时，模块用零填充缓冲区。

如果初始缓冲区设置为 `0` 或不包含足够信息，您会在估计的初始阶段看到警告消息。该警告应在几个周期后清除。缓冲足够信息所需的周期数取决于多项式的阶数和输入延迟。如果警告持续存在，您应评估信号的内容。

模块在仿真开始时或每当 **Reset** 信号触发时使用此参数。

#### 依赖项

要启用此参数，请设置

- **历史** 为 `Finite`
- **模型结构** 为 `ARX` 或
  `OE`
- **初始估计** 为
  `Internal`
。

#### 程序化使用

|  |
| --- |
| **模块参数：**`InitialInputs` |
| **类型：** real matrix |
| **默认：** `0` |

### **初始输出** — 测量输出缓冲区的初始值 `0`（默认） | vector

在使用有限历史（滑动窗口）估计时，指定测量输出缓冲区的初始值。缓冲区维度适应指定的窗口长度以及该窗口内与多项式关联的回归量。

- AR 或 ARX 模型结构 —
  (*W*+*na*)-by-1 vector，其中
  *W* 是窗口长度，*na* 是
  *A*(*q*) 的多项式阶数。
- OE 模型结构 — (*W*+*nf*)-by-1
  vector，其中 *W* 是窗口长度，
  *nf* 是 *F*(*q*) 的多项式阶数。

当初始值设置为 `0` 时，模块用零填充缓冲区。

如果初始缓冲区设置为 `0` 或不包含足够信息，您会在估计的初始阶段看到警告消息。该警告应在几个周期后清除。缓冲足够信息所需的周期数取决于多项式的阶数和输入延迟。如果警告持续存在，您应评估信号的内容。

模块在仿真开始时或每当 **Reset** 信号触发时使用此参数。

#### 依赖项

要启用此参数，请设置：

- **历史** 为 `Finite`
- **模型结构** 为 `AR`、
  `ARX` 或 `OE`
- **初始估计** 为
  `Internal`

#### 程序化使用

|  |
| --- |
| **模块参数：**`InitialOutputs` |
| **类型：** real vector |
| **默认：** `0` |

### 输入处理与采样时间

### **输入处理** — 选择基于样本或基于帧的处理 `Sample-based`（默认） | `Frame-based`

- `Sample-based` 处理一次对一个样本流式传输的信号进行操作。
- `Frame-based` 处理对包含多个时间步样本的信号进行操作。许多机器传感器接口将多个样本打包，并将这些样本一起以帧的形式传输。`Frame-based` 处理允许您直接输入此数据，而无需先对其进行解包。

指定基于帧的数据会为某些数据 inports 和 outports 添加额外维度 *M*，其中 *M* 是帧中的时间步数。这些端口是：

- **Inputs**
- **Output**
- **Error**

有关更多信息，请参阅端口中的端口描述。

#### 程序化使用

|  |
| --- |
| **模块参数：**`InputProcessing` |
| **类型：** character vector, string |
| **值：** `'Sample-based'`, `'Frame-based'` |
| **默认：**`'Sample-based'` |

### **采样时间** — 模块采样时间 `–1`（默认） | positive scalar

指定数据采样时间，对于基于样本的处理，按单个 samples（*ts*）指定；对于基于帧的处理，按帧（*tf* =
*M**ts*）指定，其中 *M* 是帧长度。当您将 **采样时间** 设置为其默认值 –1 时，模块根据信号继承其 *ts* 或 *tf*。

将 **采样时间** 指定为 positive scalar 以覆盖继承。

#### 程序化使用

|  |
| --- |
| **模块参数：**`Ts` |
| **类型：** real scalar |
| **值：** `–1`, positive scalar |
| **默认：** `–1` |

### 算法与模块选项

#### 算法选项

### **历史** — 选择无限或有限数据历史 `Infinite`（默认） | `Finite`

**历史** 参数确定您使用的递归算法类型：

- `Infinite` — 此类算法旨在生成解释自仿真开始以来所有数据的参数估计。这些算法将历史保留在数据摘要中。模块将此摘要维护在固定数量的内存中，该内存不会随时间增长。

  模块提供多种 `Infinite` 类型的算法。选择此选项会启用 **估计方法** 参数，您可以通过该参数指定算法。
- `Finite` — 此类算法旨在生成仅解释有限数量过去数据样本的参数估计。模块使用有限窗口内的所有数据，并在数据不再处于窗口边界内时丢弃该数据。此方法也称为滑动窗口估计。

  模块提供一种 `Finite` 类型的算法。您只能将此选项用于 `AR`、`ARX` 和 `OE` 模型结构。

  选择此选项会启用 **窗口长度** 参数。

有关递归估计方法的更多信息，请参阅 Recursive Algorithms for Online Parameter Estimation。

#### 程序化使用

|  |
| --- |
| **模块参数：**`History` |
| **类型：** character vector, string |
| **值：** `'Infinite'`, `'Finite'` |
| **默认：**`'Infinite'` |

### **窗口长度** — 有限滑动窗口估计的窗口大小 `200`（默认） | positive integer

**窗口长度** 参数确定用于有限历史（滑动窗口）估计方法的时间样本数。选择可平衡估计性能与计算和内存负担的窗口大小。确定大小的因素包括模型中参数的数量和时间方差。始终以 samples 为单位指定 **窗口长度**，即使您使用的是基于帧的输入处理。

**窗口长度** 必须大于或等于估计参数的数量。

合适的窗口长度与您使用的是基于样本还是基于帧的输入处理无关。但是，使用基于帧的处理时，**窗口长度** 必须大于或等于帧中包含的 samples（时间步）数。

#### 依赖项

要启用此参数，请将 **历史** 设置为
`Finite`。

#### 程序化使用

|  |
| --- |
| **模块参数：**`WindowLength` |
| **类型：** positive integer |
| **默认：** `200` |

### **估计方法** — 递归估计算法 `Forgetting Factor`（默认） | `Kalman Filter` | `Normalized Gradient` | `Gradient`

在执行无限历史估计时指定估计算法。当您选择其中任一方法时，模块会启用其他相关参数。

遗忘因子和 Kalman filter 算法比梯度及归一化梯度方法的计算量更大。然而，这些计算量更大的方法比梯度方法具有更好的收敛特性。有关这些算法的更多信息，请参阅 Recursive Algorithms for Online Parameter Estimation。

#### 程序化使用

|  |
| --- |
| **模块参数：**`EstimationMethod` |
| **类型：** character vector, string |
| **值：** `'Forgetting Factor'`,`'Kalman Filter'`,`'Normalized Gradient'`,`'Gradient'` |
| **默认：** `'Forgetting Factor'` |

### **遗忘因子** — 使用遗忘因子对旧数据进行折扣 `1`（默认） | positive scalar in (0 1] range

遗忘因子 *λ* 指定估计中是否以及多少旧数据被折扣。假设系统在 *T0* 个 samples 内保持近似恒定。您可以选择 *λ*，使得：

T0=11−λ

- 设置 *λ* = 1 对应于“无遗忘”并估计常数系数。
- 设置 *λ* < 1 意味着过去测量对参数估计的重要性较低，并且可以被“遗忘”。设置 *λ* < 1 以估计时变系数。

通常 *λ* 的选择在 [0.98 0.995] 范围内。

#### 依赖项

要启用此参数，请将 **历史** 设置为
`Infinite`，并将 **估计方法** 设置为
`Forgetting Factor`。

#### 程序化使用

|  |
| --- |
| **模块参数：**`AdaptationParameter` |
| **类型：** scalar |
| **值：** (0 1] range |
| **默认：** `1` |

### **过程噪声协方差** — Kalman filter 估计方法的过程噪声协方差 `1`（默认） | nonnegative scalar | vector of nonnegative scalars | symmetric positive semidefinite matrix

**过程噪声协方差** 规定 Kalman filter 估计的噪声协方差矩阵的元素和结构。使用 *N* 作为要估计的参数数量，将 **过程噪声协方差** 指定为以下之一：

- Real nonnegative scalar, *α* — 协方差矩阵是
  *N*×*N* diagonal matrix，其中
  *α* 为对角元素。
- Vector of real nonnegative scalars,
  [*α*1,...,*α**N*]
  — 协方差矩阵是 *N*×*N* diagonal
  matrix，其中
  [*α*1,...,*α**N*]
  为对角元素。
- *N*×*N* symmetric positive semidefinite
  matrix。

Kalman filter 算法将参数视为动态系统的状态，并使用 Kalman filter 估计这些参数。**过程噪声协方差** 是作用于这些参数的过程噪声的协方差。噪声协方差矩阵中的零值对应于常数系数或参数。大于 0 的值对应于时变参数。对于快速变化的参数，使用较大的值。但是，预期较大的值会导致参数估计噪声更大。默认值为 1。

#### 依赖项

要启用此参数，请将 **历史** 设置为
`Infinite`，并将 **估计方法** 设置为
`Kalman Filter`。

#### 程序化使用

|  |
| --- |
| **模块参数：**`AdaptationParameter` |
| **类型：** scalar, vector, matrix |
| **默认：** `1` |

### **Adaptation Gain** — 梯度估计方法的自适应增益规范 `1`（默认）| positive scalar

自适应增益 *γ* 缩放新测量数据对梯度法和归一化梯度法估计结果的影响。当你的测量数据可信，或者说具有高信噪比时，为 *γ* 指定较大的值。但是，将 *γ* 设置得太高会导致参数估计发散。即使测量无噪声，也可能发生这种发散。

当 **Estimation Method** 为 `NormalizedGradient` 时，**Adaptation Gain** 应小于 2。对于任一种梯度法，如果误差随时间增长（换句话说，估计正在发散），或参数估计频繁跳动，请考虑减小 **Adaptation Gain**。

#### 依赖项

要启用此参数，请将 **History** 设置为 `Infinite`，并将 **Estimation Method** 设置为 `Normalized Gradient` 或 `Gradient`。

#### 编程用法

|  |
| --- |
| **模块参数：**`AdaptationParameter` |
| **类型：** scalar |
| **默认：** `1` |

### **Normalization Bias** — 归一化梯度估计方法中自适应增益缩放的偏置 `eps`（默认）| nonnegative scalar

归一化梯度算法在每一步通过梯度向量二范数的平方来缩放自适应增益。如果梯度接近零，接近零的分母可能会导致估计参数跳变。**Normalization Bias** 是引入分母以防止这些跳变的项。如果观察到估计参数发生跳变，请增大 **Normalization Bias**。

#### 依赖项

要启用此参数，请将 **History** 设置为 `Infinite`，并将 **Estimation Method** 设置为 `Normalized Gradient`。

#### 编程用法

|  |
| --- |
| **模块参数：**`NormalizationBias` |
| **类型：** scalar |
| **默认：** `eps` |

#### 模块选项

### **Output estimation error** — 向模块添加 Error 输出端口 `off`（默认）| on

使用 **Error** 输出端口信号来验证估计。对于给定时间步 *t*，估计误差 *e*(*t*) 计算为：

e(t)=y(t)−yest(t)，

其中 *y*(*t*) 是你提供的测量输出，*yest*(*t*) 是使用回归量 *H*(*t*) 和参数估计 *θ*(*t*-1) 得到的估计输出。

#### 编程用法

|  |
| --- |
| **模块参数：**`OutputError` |
| **类型：** character vector, string |
| **值：**`'off'`,`'on'`, |
| **默认：** `'off'` |

### **Output parameter covariance matrix** — 向模块添加 covariance 输出端口 `off`（默认）| on

使用 **Covariance** 输出端口信号来检查参数估计不确定性。软件计算参数协方差 `P`，假设残差 *e*(*t*) 为白噪声，并且这些残差的方差为 1。

`P` 的解释取决于你在 **History** 和 **Estimation Method** 中指定的估计方法，如下所示：

- 如果 **History** 为 `Infinite`，那么你的 **Estimation Method** 选择会导致：

  - `Forgetting Factor` — (*R2*/2)`P` 近似等于估计参数的协方差矩阵，其中 *R2* 是残差的真实方差。模块通过 **Error** 端口返回这些残差。
  - `Kalman Filter` — *R2*`P` 是估计参数的协方差矩阵，而 *R1*/*R2* 是参数变化的协方差矩阵。这里，*R1* 是你在 **Parameter Covariance Matrix** 中指定的协方差矩阵。
  - `Normalized Gradient` 或 `Gradient` — 协方差 `P` 不可用。
- 如果 **History** 为 `Finite`（滑动窗口估计）— *R2*`P` 是估计参数的协方差。滑动窗口算法在参数估计过程中不使用此协方差。但是，该算法会计算协方差以供输出，以便你可以将其用于统计评估。

#### 编程用法

|  |
| --- |
| **模块参数：**`OutputP` |
| **类型：** character vector, string |
| **值：**`'off'`,`'on'` |
| **默认：** `'off'` |

### **Add enable port** — 向模块添加 Enable 输入端口 `off`（默认）| on

使用 **Enable** 信号提供控制信号，以启用或禁用参数估计。模块在参数估计启用的每个时间步估计参数值。如果在给定步 *t* 禁用参数估计，则软件不会更新该时间步的参数。相反，模块输出包含最近估计的参数值。

你可以在以下情况使用此选项，例如：

- 你的回归量或输出信号变得过于嘈杂，或在某些时间步不包含信息
- 你的系统进入参数值不随时间变化的模式

#### 编程用法

|  |
| --- |
| **模块参数：**`AddEnablePort` |
| **类型：** character vector, string |
| **值：**`'off'`,`'on'` |
| **默认：** `'off'` |

### **External reset** — 指定外部复位的触发条件 `None`（默认）| `Rising` | `Falling` | `Either` | `Level` | `Level hold`

将 **External reset** 参数设置为同时添加 **Reset** 输入端口，并指定触发将算法状态复位为其指定初始值的输入端口信号条件。例如，如果由于测量信号中缺乏足够的激励或信息而导致参数协方差变得过大，请复位估计。**External reset** 参数决定复位时机。

假设你在时间步 *t* 复位模块。如果模块在 *t* 启用，则软件使用 **Initial Estimate** 中指定的初始参数值来估计参数值。换句话说，在 *t*，模块使用初始估计和输入端口的当前值执行参数更新。

如果模块在 *t* 禁用并且你复位模块，则模块输出包含 **Initial Estimate** 中指定的值。

将此选项指定为以下之一：

- `None` — 不重置算法状态和估计参数。
- `Rising` — 当控制信号从负值或零上升到正值时触发复位。如果初始值为负，上升到零会触发复位。
- `Falling` — 当控制信号从正值或零下降到负值时触发复位。如果初始值为正，下降到零会触发复位。
- `Either` — 当控制信号上升或下降时触发复位。
- `Level` — 在以下任一情况下触发复位：

  - 控制信号在当前时间步非零。
  - 控制信号从前一时间步非零变为当前时间步零。
- `Level hold` — 当控制信号在当前时间步非零时触发复位。

当你选择除 `None` 以外的任何选项时，软件会向模块添加 Reset 输入端口。你将复位控制输入信号提供到此输入端口。

#### 编程用法

|  |
| --- |
| **模块参数：**`ExternalReset` |
| **类型：** character vector, string |
| **值：**`'None'`,`'Rising'`,`'Falling'`, `'Either'`, `'Level'`, `'Level hold'` |
| **默认：** `'None'` |

## 所属库

System Identification Toolbox / Estimators

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**在 R2014a 中引入**

## 描述

估计输入-输出和时间序列多项式模型系数

### 模型结构

使用 Recursive Polynomial Model Estimator 模块估计离散时间输入-输出多项式模型和时间序列模型。

这些模型结构为：

- AR — *A*(*q*)*y*(*t*) = *e*(*t*)
- ARMA — *A*(*q*)*y*(*t*) = *C*(*q*)*e*(*t*)
- ARX — *A*(*q*)*y*(*t*) = *B*(*q*)*u*(*t* – *nk*) + *e*(*t*)
- ARMAX — *A*(*q*)*y*(*t*) = *B*(*q*)*u*(*t* – *nk*) + *C*(*q*)*e*(*t*)
- OE — y(t)=B(q)F(q)u(t−nk)+e(t)
- BJ — y(t)=B(q)F(q)u(t−nk)+​C(q)D(q)e(t)

*q* 是时移算子，*nk* 是输入延迟。*u*(*t*) 是输入，*y*(*t*) 是输出，*e*(*t*) 是误差。对于 MISO 模型，*B*(*q*) 多项式的数量与输入数量相同。

这些模型的阶数对应于最大时移数量，由 *q* 的指数表示。例如，阶数 *na* 在 *A*(*q*) 多项式中表示为：

1 + *a1**q*-1 + *a2**q*-2 + … + *ana**q*-*na*.

等价的表示适用于 *C*(*q*)、*D*(*q*) 和 *F*(*q*) 多项式及其对应阶数 *nc*、*nd* 和 *nf*。

*B*(*q*) 多项式相对于其他多项式是独特的，因为该多项式作用于输入并包含系统零点。对于 *B*(*q*)，阶数 *nb* 是多项式 *B*(*q*) + 1 的阶数：

*b*1 + *b2**q*-1 + *b3**q*-2 + … + *bnb**q*-(*nb*-1).

阶数 *na*、*nb*、*nc*、*nd*、*nf* 和输入延迟 *nk* 是预先已知的。将这些值指定为模块参数。分别通过 **Inputs** 和 **Outputs** 输入端口提供 *u*(*t*) 和 *y*(*t*)。模块估计模型结构使用的 *A*(*q*)、*B*(*q*)、*C*(*q*)、*D*(*q*) 和 *F*(*q*) 系数集合，并将它们输出到 **Parameters** 输出端口。在估计期间，模块将估计的 *C*、*D* 和 *F* 多项式约束到根位于单位圆内的稳定区域，同时允许估计的 *A* 和 *B* 多项式不稳定。**Parameters** 输出端口提供具有以下元素的 bus 信号：

- A — 包含 [1 *a1*(*t*) ... *ana*(*t*)] 的向量。
- B — 包含 [01 … 0*nk*, *b1*(*t*) ... *bnb*(*t*)] 的向量。对于 MISO 数据，*B* 是一个矩阵，其中第 *i* 行参数对应于第 *i* 个输入。
- C — 包含 [1 *c1*(*t*) ... *cnc*(*t*)] 的向量。
- D — 包含 [1 *d1*(*t*) ... *dnd*(*t*)] 的向量。
- F — 包含 [1 *f1*(*t*) ... *fnf*(*t*)] 的向量。

例如，假设你要估计以下 SISO ARMAX 模型的系数：

*y*(*t*) + *a1**y*(*t* – 1) +...+*ana**y*(*t* – *na*) = *b1**u*(*t* – *nk*) + … + *bnb**u*(*t* – *nb* – *nk* + 1) + *e*(*t*) + *c1**e*(*t* – 1) + … + *cnc**e*(*t* – *nc*)

*y*、*u*、*na*、*nb*、*nc* 和 *nk* 是你提供给模块的已知量。对于每个时间步 *t*，模块估计 *A*、*B* 和 *C* 参数值，仅将 *C* 多项式约束到稳定区域。然后，模块使用 **Parameters** 输出端口输出这些估计值。

### 模块能力

该模块支持多种估计方法和数据输入格式。该模块可以为 *θ* 提供无限历史 [1] 和有限历史 [2]（也称为滑动窗口）估计。模块中可配置的选项包括：

- 多个输入（仅 ARX 模型结构）— 请参阅 **Inputs** 端口。
- 基于样本或基于帧的数据格式 — 请参阅 **Input Processing** 参数。
- 多种无限历史估计方法 [1] — 请参阅 **Estimation Method** 参数。
- 无限历史（所有模型结构）或有限历史（仅 AR、ARX 或 OE 模型结构）— 请参阅 **History** 参数。
- 初始条件、使能标志和复位触发 — 请参阅 **Initial Estimate**、**Add enable port** 和 **External Reset** 参数。

有关估计方法的更多信息，请参阅 Recursive Algorithms for Online Parameter Estimation。
