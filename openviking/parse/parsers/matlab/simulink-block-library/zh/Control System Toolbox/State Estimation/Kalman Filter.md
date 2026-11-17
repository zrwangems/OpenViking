---
type: simulink-block
title: 'Kalman Filter'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'State Estimation'
documentation_page: 'kalmanfilter'
documentation_source_path: 'ref/kalmanfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Kalman Filter

## 端口

### 输入

### **u** — 已知输入 标量 | 向量

已知输入 `u(t)` 或 `u[k]`。

#### 依赖

要启用此端口，请选中 **Add input port u** 参数。该参数默认处于选中状态。

### **y** — 测量输出 标量 | 向量

用于更新估计状态的测量输出 `y[n]`。

### **A** — 状态矩阵 实矩阵

*n* 乘 *n* 状态（或系统）矩阵。

#### 依赖

要启用此端口，请将 **Model source** 参数设置为 **Input Port**。

### **B** — 输入矩阵 实矩阵

*n* 乘 *p* 输入矩阵。

#### 依赖

要启用此端口，请将 **Model source** 参数设置为 **Input Port** 并选中 **Add input port u** 参数。

### **C** — 输出矩阵 实矩阵

*q* 乘 *p* 输出矩阵。

#### 依赖

要启用此端口，请将 **Model source** 参数设置为 **Input Port**。

### **D** — 直通矩阵 实矩阵

*q* 乘 *p* 直通（或前馈）矩阵。在系统模型没有直接直通的情况下，**D** 为零矩阵。

#### 依赖

要启用此端口，请将 **Model source** 参数设置为 **Input Port** 并选中 **Add input port u** 参数。

### **G** — 测量输出 实矩阵

状态空间方程中的噪声变换。

#### 依赖

要启用此端口，请选中 **Use G and H matrices (default G=I and H=0)** 参数。

### **H** — 测量输出 实矩阵

状态空间方程中的噪声变换。

#### 依赖

要启用此端口，请选中 **Use G and H matrices (default G=I and H=0)** 参数。

### **Q** — 过程噪声协方差矩阵 标量 | 向量 | 矩阵

过程噪声协方差矩阵，指定为以下之一：

- 实非负标量。**Q** 是一个 *Nw* 乘 *Nw* 对角矩阵，对角线上的元素为该标量。*Nw* 是模型中过程噪声输入的数量。
- 实非负标量向量。**Q** 是一个 *Nw* 乘 *Nw* 对角矩阵，**Q** 的对角线上的元素为该向量的元素。
- *Nw* 乘 *Nw* 半正定矩阵。

#### 依赖

要启用此端口，请取消选中 **Time-invariant Q** 参数。

### **R** — 测量噪声协方差矩阵 标量 | 向量 | 矩阵

测量噪声协方差矩阵，指定为以下之一：

- 实正标量。**R** 是一个 *Ny* 乘 *Ny* 对角矩阵，对角线上的元素为该标量。*Ny* 是模型中测量输出的数量。
- 实正标量向量。**R** 是一个 *Ny* 乘 *Ny* 对角矩阵，**R** 的对角线上的元素为该向量的元素。
- *Ny* 乘 *Ny* 正定矩阵。

#### 依赖

要启用此端口，请取消选中 **Time-invariant R** 参数。

### **N** — 过程噪声与测量噪声互协方差矩阵 标量 | 向量 | 矩阵

过程噪声与测量噪声互协方差矩阵，指定为 *Nw* 乘 *Ny* 矩阵。矩阵 [Q N; NT R] 必须为正定矩阵。

#### 依赖

要启用此端口，请取消选中 **Time-invariant N** 参数。

### **P0** — 初始状态估计误差协方差 标量 | 向量 | 矩阵

初始时刻的 **P** 矩阵。

#### 依赖

要启用此端口，请将 **Model source** 参数设置为 **Input Port** 并将 **Source** 参数设置为 **Input Port**。

### **X0** — 初始状态估计 标量 | 向量

初始时刻的估计状态。

#### 依赖

要启用此端口，请将 **Source** 参数设置为 **Input Port**。

### **Enable** — 用于启用测量更新的控制信号 标量

此端口控制测量更新并接受标量信号。

#### 依赖

要启用此端口，请选中 **Add input port Enable to control measurement updates** 参数。

### **Reset** — 用于重置状态估计的控制信号 标量

用于使用指定初始值重置估计状态和参数协方差矩阵的控制信号。有关何时触发重置的更多信息，请参阅 External Reset (System Identification Toolbox)。

#### 依赖

要启用此端口，请将 **External reset** 参数设置为 **None** 以外的任何值。
### 输出

### **xhat** — 估计状态 标量 | 向量

线性系统的估计状态。

### **yhat** — 估计输出 标量 | 向量

线性系统的估计输出。

#### 依赖

要启用此端口，请选中 **Output estimated model output y** 参数。

### **Z** — 状态估计误差协方差矩阵

向模块添加 **Z** 输出端口。

要启用此端口，请选中 **Output state estimation error covariance Z** 参数。

#### 依赖

要启用此端口，请将 **Time domain** 参数设置为 **Discrete-Time** 并选中 **Use the current measurement y[n] to improve xhat[n]** 参数。

### **P** — 状态估计误差协方差矩阵

向模块添加 **P** 输出端口。

要启用此端口，请选中 **Output state estimation error covariance P** 参数。

#### 依赖

要启用此端口，请将 **Time domain** 参数设置为 **Continuous-Time**，或将 **Time domain** 参数设置为 **Discrete-Time** 并取消选中 **Use the current measurement y[n] to improve xhat[n]** 参数。

**注意**

- 除 **Enable** 和 **Reset** 之外的所有输入端口必须具有相同的数据类型（single 或 double）。
- **Enable** 和 **Reset** 端口支持 `single`、`double`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32` 和布尔数据类型。

## 参数

### 滤波器设置

### **Time domain** — 指定估计连续时间状态还是离散时间状态 `Discrete-Time`（默认）| `Continuous-Time`

- `Discrete-Time`（默认）— 模块估计离散时间状态。
- `Continuous-Time` — 模块估计连续时间状态。

  当 Kalman Filter 模块位于具有同步状态控制的模型中时（请参阅 State Control (HDL Coder) 模块），您无法选择 **Continuous-Time**。

#### 编程使用

|  |
| --- |
| **模块参数**：`TimeDomain` |
| **类型**：string, character vector |
| **值**：`"Discrete-Time"` | `"Continuous-Time"` |
| **默认值**：`"Discrete-Time"` |

### **Use the current measurement y[n] to improve xhat[n]** — 使用测量输出更新输出状态估计 `on`（默认）| `off`

使用离散时间卡尔曼滤波器的当前估计器变体。未选中此参数时，使用延迟估计器（变体）。

此参数仅在 **Time domain** 为 **Discrete-Time** 时可用。

#### 编程使用

|  |
| --- |
| **模块参数**：`UseCurrentEstimator` |
| **类型**：string, character vector |
| **值**：`"off"` | `"on"` |
| **默认值**：`"on"` |

### **Sample Time** — 模块采样时间 `-1`（默认）| `non-negative scalar`

模块采样时间，指定为 `-1` 或正标量。

默认值为 `-1`，这意味着模块根据其在模型中的上下文继承采样时间。所有模块输入端口必须具有相同的采样时间。

#### 依赖

此参数仅在 **Time domain** 为 **Discrete-Time** 且 **Model source** 为 **Individual A, B, C, D matrices** 或 **Input port** 时可用。当 **Model source** 为 **LTI State-Space Variable** 时，模块从 LTI 状态空间变量获取其采样时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`Ts` |
| **类型**：string, character vector |
| **值**：`"-1"` | scalar |
| **默认值**：`"-1"` |

### 模型参数

#### 系统模型

### **Model source** — 指定如何向模块提供 A、B、C、D 矩阵 `LTI State-Space Variable`（默认）| `Individual A, B, C, D matrices` | `Input port`

- `LTI State-Space Variable` — 使用 **Variable** 中指定的模型。默认值为 `ss(0.95,1,1,0)`。模型的采样时间必须与 **Time domain** 参数匹配；也就是说，如果 **Time domain** 为离散时间，则模型必须为离散时间。
- `Individual A, B, C, D matrices` — 在模块参数中指定 **A**、**B**、**C** 和 **D**。
- `Input port` — 将 **A**、**B**、**C**、**D** 矩阵指定为 Kalman Filter 模块的输入信号。如果选择此选项，模块将包含额外的输入端口 **A**、**B**、**C**、**D**。您还必须在模块参数中指定 **Number of states**、**Number of inputs** 和 **Number of outputs**。

#### 编程使用

|  |
| --- |
| **模块参数**：`ModelSource` |
| **类型**：string, character vector |
| **值**：`"LTI State-Space Variable"` | `"Individual A, B, C, D matrices"` | `"Input port"` |
| **默认值**：`"LTI State-Space Variable"` |

### **A** — 状态矩阵 `0.95`（默认）

指定 **A** 矩阵。它必须是实方阵。默认值为 `0.95`。

#### 依赖

要启用此端口，请将 **Model source** 参数设置为 **Individual A, B, C, D matrices**。

#### 编程使用

|  |
| --- |
| **模块参数**：`A` |
| **类型**：string, character vector |
| **值**：`"real matrix"` |
| **默认值**：`"0.95"` |

### **B** — 输入矩阵 `1`（默认）

指定 **B** 矩阵。它必须是实矩阵，且行数与 **A** 矩阵相同。默认值为 `1`。

#### 依赖

要启用此端口，请将 **Model source** 参数设置为 **Individual A, B, C, D matrices**。

#### 编程使用

|  |
| --- |
| **模块参数**：`B` |
| **类型**：string, character vector |
| **值**：`"real matrix"` |
| **默认值**：`"1"` |

### **C** — 输出矩阵 `1`（默认）

指定 **C** 矩阵。它必须是实矩阵，且列数与 **A** 矩阵相同。默认值为 `1`。

#### 依赖

要启用此端口，请将 **Model source** 参数设置为 **Individual A, B, C, D matrices**。

#### 编程使用

|  |
| --- |
| **模块参数**：`C` |
| **类型**：string, character vector |
| **值**：`"real matrix"` |
| **默认值**：`"1"` |

### **D** — 直通矩阵 `0`（默认）

指定 **D** 矩阵。它必须是实矩阵，且行数必须与 **C** 矩阵相同，列数必须与 **B** 矩阵相同。默认值为 `0`。

#### 依赖

要启用此端口，请将 **Model source** 参数设置为 **Individual A, B, C, D matrices**。

#### 编程使用

|  |
| --- |
| **模块参数**：`D` |
| **类型**：string, character vector |
| **值**：`"real matrix"` |
| **默认值**：`"0"` |

### **Number of states** — 要估计的状态数 `1`（默认）| `non-negative scalar`

要估计的状态数，指定为正整数。默认值为 `1`。

#### 依赖

要启用此端口，请将 **Model source** 参数设置为 **Input port**。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberOfStates` |
| **类型**：string, character vector |
| **值**：`"1"` | `scalar` |
| **默认值**：`"1"` |

### **Number of inputs** — 已知输入的数量 `1`（默认）| `non-negative scalar`

模型中已知输入的数量，指定为正整数。默认值为 `1`。

#### 依赖

要启用此端口，请将 **Model source** 参数设置为 **Input port**。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberOfInputs` |
| **类型**：string, character vector |
| **值**：`"1"` | `scalar` |
| **默认值**：`"1"` |

### **Number of outputs** — 测量输出的数量 `1`（默认）| `non-negative scalar`

模型中测量输出的数量，指定为正整数。默认值为 `1`。

#### 依赖

要启用此端口，请将 **Model source** 参数设置为 **Input port**。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberOfOutputs` |
| **类型**：string, character vector |
| **值**：`"1"` | `scalar` |
| **默认值**：`"1"` |

#### 初始估计

### **Source** — 指定如何输入初始状态估计和初始状态估计误差协方差 `Dialog`（默认）| `Input port`

- `Dialog` — 直接在对话框中指定值。
- `Input port` — 从输入端口继承值。默认值为 `10`。模块包含一个额外的输入端口 **X0**。当使用时变卡尔曼滤波器时，会添加第二个额外输入端口 **P0**。**X0** 和 **P0** 必须分别满足与参数 Initial states x[0] 和 State estimation error covariance P[0] 相同的条件。

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialEstimateSource` |
| **类型**：string, character vector |
| **值**：`"Dialog"` | `"Input port"` |
| **默认值**：`"Dialog"` |

### **Initial states x[0]** — 指定初始状态估计 `0`（默认）| `scalar` | `vector`

将初始状态估计指定为实标量或向量。如果指定标量，所有初始状态估计都设置为该标量。如果指定向量，向量的长度必须与模型中的状态数匹配。默认值为 `0`。

#### 依赖

要启用此端口，请将 **Source** 参数设置为 **Dialog**。

#### 编程使用

|  |
| --- |
| **模块参数**：`X0` |
| **类型**：string, character vector |
| **值**：`"0"` | `scalar` | `vector` |
| **默认值**：`"0"` |

### **State estimation error covariance P[0]** — 指定初始状态估计误差协方差 `10`（默认）| `scalar` | `vector` | `matrix`

指定离散时间卡尔曼滤波器的初始状态估计误差协方差 P[0] 或连续时间的 P(0)。此参数必须指定为以下之一：

- 实非负标量。**P** 是一个 *Ns* 乘 *Ns* 对角矩阵，对角线上的元素为该标量。*Ns* 是模型中的状态数。
- 实非负标量向量。**P** 是一个 *Ns* 乘 *Ns* 对角矩阵，**P** 的对角线上的元素为该向量的元素。
- *Ns* 乘 *Ns* 半正定矩阵。

#### 依赖

要启用此端口，请将 **Model source** 参数设置为 **Input port** 并将 **Source** 参数设置为 **Dialog**。

#### 编程使用

|  |
| --- |
| **模块参数**：`P0` |
| **类型**：string, character vector |
| **值**：`"10"` | `scalar` | `vector` | `matrix` |
| **默认值**：`"10"` |

#### 噪声特性

### **Use the Kalman Gain K from the model variable** — 指定是否使用状态空间被控对象模型中包含的预辨识卡尔曼增益 `off`（默认）| `on`

指定是否使用 **Variable** 指定的状态空间模型中存在的预辨识卡尔曼增益。

#### 依赖

要启用此参数，必须满足以下条件：

- **Model source** 设置为 **LTI State-Space Variable**，且 **Variable** 是已辨识的状态空间模型（`idss` (System Identification Toolbox)），其 **K** 矩阵非零。
- 选中 **Time Invariant Q**、**Time Invariant R** 和 **Time Invariant N** 参数。
- 如果选中 **Use G and H matrices (default G=I and H=0)** 参数，则还必须选中 **Time Invariant G** 和 **Time Invariant H** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`UseK` |
| **类型**：string, character vector |
| **值**：`"off"` | `"on"` |
| **默认值**：`"off"` |

### **Use G and H matrices (default G=I and H=0)** — 指定是否对 G 和 H 矩阵使用非默认值 `off`（默认）| `on`

默认情况下 `G=I` 且 `H=0`。如果选中此选项，则必须指定 **G** 和 **H** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`UseGH` |
| **类型**：string, character vector |
| **值**：`"off"` | `"on"` |
| **默认值**：`"off"` |

### **G** — 指定 G 矩阵 `1`（默认）| `non-negative scalar` | `vector` | `matrix`

它必须是实矩阵，且行数与 **A** 矩阵相同。默认值为 `1`。

#### 依赖

要启用此参数，请选中 **Use G and H matrices (default G=I and H=0)** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`G` |
| **类型**：string, character vector |
| **值**：scalar | vector | matrix |
| **默认值**：`"1"` |

### **Time-invariant G** — 指定 G 矩阵为时不变 `on`（默认）| `off`

如果取消选择此选项，模块将包含一个额外的输入端口 **G**。

#### 编程使用

|  |
| --- |
| **模块参数**：`TimeInvariantG` |
| **类型**：string, character vector |
| **值**：`"off"` | `"on"` |
| **默认值**：`"on"` |

### **H** — 指定 H 矩阵 `0`（默认）| `non-negative scalar` | `vector` | `matrix`

它必须是一个实数矩阵，其行数与 **C** 矩阵相同，列数与 **G** 矩阵相同。默认值为 `0`。

#### 依赖关系

要启用此参数，请选择 **Use G and H matrices (default G=I and H=0)** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`H` |
| **类型**：string, character vector |
| **值**：scalar | vector | matrix |
| **默认值**：`"0"` |

### **Time-invariant H** — 指定 H 矩阵为时不变 `on`（默认）| `off`

如果取消选择此选项，模块将包含一个额外的输入端口 **H**。

#### 编程使用

|  |
| --- |
| **模块参数**：`TimeInvariantH` |
| **类型**：string, character vector |
| **值**：`"off"` | `"on"` |
| **默认值**：`"on"` |

### **Number of process noise inputs** — 过程噪声输入的数量 `1`（默认）| `non-negative scalar`

指定模型中的过程噪声输入数量。默认值为 `1`。

#### 依赖关系

此参数仅在 **Time-invariant G** 和 **Time-invariant H** 均取消选择时可用。否则，此信息将从 **G** 或 **H** 矩阵推断。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberOfProcessNoiseInputs` |
| **类型**：string, character vector |
| **值**：scalar |
| **默认值**：`"1"` |

### **Q** — 过程噪声协方差矩阵 `0.05`（默认）| `non-negative scalar` | `vector` | `matrix`

指定为以下之一：

- 实数非负标量。**Q** 是一个 *Nw*×*Nw* 对角矩阵，标量位于对角线上。*Nw* 是模型中的过程噪声输入数量。
- 实数非负标量向量。**Q** 是一个 *Nw*×*Nw* 对角矩阵，向量的元素位于 **Q** 的对角线上。
- *Nw*×*Nw* 半正定矩阵。

#### 依赖关系

要启用此参数，请选择 **Time-invariant Q** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`Q` |
| **类型**：string, character vector |
| **值**：scalar | vector | matrix |
| **默认值**：`"0.05"` |

### **Time-invariant Q** — 指定 Q 矩阵是否为时不变 `on`（默认）| `off`

如果取消选择此参数，模块将包含一个额外的输入端口 **Q**。

#### 编程使用

|  |
| --- |
| **模块参数**：`TimeInvariantQ` |
| **类型**：string, character vector |
| **值**：`"off"` | `"on"` |
| **默认值**：`"on"` |

### **R** — 测量噪声协方差矩阵 `1`（默认）| `non-negative scalar` | `vector` | `matrix`

指定为以下之一：

- 实数正标量。**R** 是一个 *Ny*×*Ny* 对角矩阵，标量位于对角线上。*Ny* 是模型中的测量输出数量。
- 实数正标量向量。**R** 是一个 *Ny*×*Ny* 对角矩阵，向量的元素位于 **R** 的对角线上。
- *Ny*×*Ny* 正定矩阵。

#### 依赖关系

要启用此参数，请选择 **Time-invariant R** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`R` |
| **类型**：string, character vector |
| **值**：scalar | vector | matrix |
| **默认值**：`"1"` |

### **Time-invariant R** — 指定 R 矩阵是否为时不变 `on`（默认）| `off`

如果取消选择此参数，模块将包含一个额外的输入端口 **R**。

#### 编程使用

|  |
| --- |
| **模块参数**：`TimeInvariantR` |
| **类型**：string, character vector |
| **值**：`"off"` | `"on"` |
| **默认值**：`"on"` |

### **N** — 过程噪声和测量噪声的互协方差矩阵 `0`（默认）| `non-negative scalar` | `vector` | `matrix`

将此参数指定为 *Nw*×*Ny* 矩阵。矩阵 [Q N; NT R] 必须是正定的。

#### 依赖关系

要启用此参数，请选择 **Time-invariant N** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`N` |
| **类型**：string, character vector |
| **值**：scalar | vector | matrix |
| **默认值**：`"0"` |

### **Time-invariant N** — 指定 N 矩阵是否为时不变 `on`（默认）| `off`

如果取消选择此参数，模块将包含一个额外的输入端口 **N**。

#### 编程使用

|  |
| --- |
| **模块参数**：`TimeInvariantN` |
| **类型**：string, character vector |
| **值**：`"off"` | `"on"` |
| **默认值**：`"on"` |

### Options

#### Additional Inports

### **Add input port u** — 指定模型是否包含已知输入 `on`（默认）| `off`

如果您的模型包含已知输入 `u(t)` 或 `u[k]`，请选择此选项。此参数默认被选中。取消选择此参数将从模块中移除输入端口 **u**，并从模块对话框中移除 **B**、**D** 和 **Number of inputs** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`AddInputPort` |
| **类型**：string, character vector |
| **值**：`"off"` | `"on"` |
| **默认值**：`"on"` |

### **Add input port Enable to control measurement updates** — 控制测量更新 `off`（默认）| `on`

如果您想控制测量更新，请选择此选项。模块将包含一个额外的输入端口 **Enable**。**Enable** 输入端口接受标量信号。此参数默认未被选中。

默认情况下，模块在每个时间步执行测量更新，以基于测量输出改进状态和输出估计值 x^ 和 y^。当 **Enable** 端口中的信号为 `0` 时，当前采样时刻的测量更新将被跳过。具体而言，对于连续时间卡尔曼滤波器，状态估计的方程变为 x^˙(t)=A(t)x^(t)+B(t)u(t)；对于离散时间，变为 x^[n+1|n]=A[n]x^[n|n−1]+B[n]u[n]。

**Note**

启用 **Enable** 端口允许控制测量更新。默认情况下，Kalman Filter 执行测量更新。

#### 编程使用

|  |
| --- |
| **模块参数**：`AddEnablePort` |
| **类型**：string, character vector |
| **值**：`"off"` | `"on"` |
| **默认值**：`"off"` |

### **External Reset** — 使用指定初始值重置估计状态和参数协方差矩阵的选项 `None`（默认）| `Rising` | `Falling` | `Either` | `Level` | `Level hold`

此参数有助于控制模块何时被重置。假设您在时间步 `t` 重置模块。如果模块在 `t` 时刻被使能，软件将使用模块对话框中指定的初始参数值或输入端口 **P0** 和 **X0** 来估计状态。换句话说，在 `t` 时刻，模块执行时间更新，如果被使能，则在重置后执行测量更新。模块输出这些更新后的估计值。

指定以下之一：

- `None`（默认）— 估计状态 x^ 和状态估计误差协方差矩阵 **P** 的值不会被重置。
- `Rising` — 当控制信号从负值或零值上升到正值时触发重置。如果初始值为负值，上升到零也会触发重置。
- `Falling` — 当控制信号从正值或零值下降到负值时触发重置。如果初始值为正值，下降到零也会触发重置。
- `Either` — 当控制信号上升或下降时触发重置。
- `Level` — 在以下任一情况下触发重置：

  - 控制信号在当前时间步非零。
  - 控制信号在上一时间步非零而在当前时间步变为零。
- `Level hold` — 当控制信号在当前时间步非零时触发重置。

当您选择 `None` 以外的选项时，模块将添加一个 **Reset** 输入端口，以提供重置控制输入信号。

#### 编程使用

|  |
| --- |
| **模块参数**：`ExternalReset` |
| **类型**：string, character vector |
| **值**：`"None"` | `"Rising"` | `"Falling"` | `"Either"` | `"Level"` | `"Level hold"` |
| **默认值**：`"None"` |

#### Additional Outports

### **Output estimated model output y** — 包含估计的模型输出 `off`（默认）| `on`

向模块添加一个 y^ 输出端口，以输出估计的模型输出。此参数默认未被选中。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputEstimatedY` |
| **类型**：string, character vector |
| **值**：`"off"` | `"on"` |
| **默认值**：`"off"` |

### **Output state estimation error covariance Z** — 向模块添加 Z 输出端口 `off`（默认）| `on`

向模块添加一个 **Z** 输出端口。**Z** 矩阵仅在 **Time domain** 为 **Discrete-Time** 且 **Use the current measurement y[n] to improve xhat[n]** 参数被选中时提供。否则，将提供 **P** 矩阵，如 Algorithms (System Identification Toolbox) 部分所述。

此参数默认未被选中。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputZ` |
| **类型**：string, character vector |
| **值**：`"off"` | `"on"` |
| **默认值**：`"off"` |

### **Output state estimation error covariance P** — 向模块添加 P 输出端口 `off`（默认）| `on`

向模块添加一个 **P** 输出端口。此参数默认未被选中。

#### 依赖关系

要启用此端口，请将 **Time domain** 参数设置为 **Continuous-Time**，或将 **Time domain** 参数设置为 **Discrete-Time** 并取消选择 **Use the current measurement y[n] to improve xhat[n]** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputP` |
| **类型**：string, character vector |
| **值**：`"off"` | `"on"` |
| **默认值**：`"off"` |

## 所属库

Control System Toolbox / State Estimation System Identification Toolbox / Estimators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**在 R2014b 中引入**

### R2021a: Kalman Filter 模块：数值变化

从 2021a 开始，Kalman Filter 模块所用算法的数值改进可能会产生与之前版本不同的结果。

## 描述

估计离散时间或连续时间线性系统的状态

使用 Kalman Filter 模块，根据过程噪声和测量噪声协方差数据估计状态空间被控对象模型的状态。状态空间模型可以是时变的。如果状态空间模型和噪声协方差矩阵都是时不变的，则使用稳态卡尔曼滤波器实现；否则使用时变卡尔曼滤波器。

卡尔曼滤波器为 Continuous-Time Estimation (System Identification Toolbox) 和 Discrete-Time Estimation (System Identification Toolbox) 中的连续或离散估计问题提供最优解。

Kalman Filter 模块与 `kalman` 命令在以下方面有所不同：

- 当您调用 `kalman(sys,...)` 时，它假设 `sys` 包含 `G` 和 `H` 矩阵。具体而言，`sys.B` 的形式为 `[B G]`，`sys.D` 的形式为 `[D H]`。当您向 Kalman Filter 模块提供 LTI 变量时，它不假设所提供的 LTI 变量包含 `G` 和 `H`。它们是可选的且独立的。
- 由 `kalman` 命令创建的滤波器默认输出 `[yhat;xhat]`。该模块默认仅输出 `xhat`。
- `Kalman` 命令可以为离散时间系统输出 `P` 和 `Z` 协方差矩阵。该模块对此类系统只能输出 `P` 或 `Z`。
