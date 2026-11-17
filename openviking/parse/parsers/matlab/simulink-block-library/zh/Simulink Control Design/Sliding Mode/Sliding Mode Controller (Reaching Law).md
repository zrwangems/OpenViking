---
type: simulink-block
title: 'Sliding Mode Controller (Reaching Law)'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Sliding Mode'
documentation_page: 'slidingmodecontrollerreachinglaw'
documentation_source_path: 'ug/slidingmodecontrollerreachinglaw.html'
language: zh-CN
chinese_source: worker-translation
---

# Sliding Mode Controller (Reaching Law)

## 端口
```yaml
ports:
- name: x
  summary: 系统状态向量
  direction: input
  data_types: single | double
- name: f(x)
  summary: 系统动态函数向量
  direction: input
  data_types: single | double
- name: g(x)
  summary: 输入函数向量
  direction: input
  data_types: single | double
- name: x.ref
  summary: 状态参考轨迹向量
  direction: input
- name: x.ref.dot
  summary: 状态参考轨迹导数向量
  direction: input
- name: u
  summary: 控制动作向量
  direction: output
- name: s(x)
  summary: 滑动变量值向量
  direction: output
```

### 输入

### **x** — 系统状态向量

系统状态，指定为 *nx*×1 信号，其中 *nx* 是状态数量。

**数据类型：** `single` | `double`

### **f(x)** — 系统动态函数向量

由方程 x˙=f(x)+g(x)u 描述的系统中，系统动态函数 *f*(*x*)。

将此端口连接至 *nx*×1 信号，其中 *nx* 是状态数量。

**数据类型：** `single` | `double`

### **g(x)** — 输入函数向量

由方程 x˙=f(x)+g(x)u 描述的系统中，输入函数 *g*(*x*)。

将此端口连接至 *nx*×*nu* 信号，其中 *nx* 是状态数量，*nu* 是输入数量。

**数据类型：** `single` | `double`

### **x.ref** — 状态参考轨迹向量

跟踪模式下要跟踪的状态参考轨迹，指定为 *nx*×1 信号，其中 *nx* 是状态数量。

#### 依赖关系

要启用此端口，请将 **Task Mode** 设置为 **Tracking Mode**。

### **x.ref.dot** — 状态参考轨迹导数向量

跟踪模式下要跟踪的状态参考轨迹的导数，指定为 *nx*×1 信号，其中 *nx* 是状态数量。

当您希望从外部输入提供状态参考轨迹的导数时，使用此端口。否则，模块在仿真期间计算导数。

#### 依赖关系

要启用此端口：

- 将 **Task Mode** 设置为 **Tracking Mode**。
- 启用 **Use externally sourced derivative**。
### 输出

### **u** — 控制动作向量

计算得到的控制动作，返回为 *nu*×1 信号，其中 *nu* 是输入数量。

### **s(x)** — 滑动变量值向量

滑动变量值，返回为 *nu*×1 信号，其中 *nu* 是输入数量。

#### 依赖关系

要启用此端口，请启用 **Output Switching Function** 参数。
## 参数
```yaml
parameters:
- name: Task Mode
  summary: 模块运行模式 Regulation Mode（默认）| Tracking Mode
  group: Sliding Surface Tab
  block_parameter: TaskMode
  values: '"Regulation Mode"（默认）| "Tracking Mode"'
- name: Sliding Coefficient Matrix (C)
  summary: 滑动系数矩阵 1（默认）| 标量 | 列向量 | 矩阵
  group: Sliding Surface Tab
  block_parameter: SlidingMatrix
  values: 1（默认）| 带引号的标量 | 带引号的列向量 | 带引号的矩阵
- name: Use externally sourced derivative
  summary: 从外部指定状态参考的导数 off（默认）| on
  group: Sliding Surface Tab
  block_parameter: EnableTrackingDerivative
  values: '"off"（默认） | "on"'
- name: 输出切换函数
  summary: 输出切换函数 off（默认） | on
  group: Sliding Surface Tab
  block_parameter: EnableSwitchingFunction
  values: '"off"（默认） | "on"'
- name: 趋近律
  summary: 趋近律 Constant Rate（默认） | Exponential | Power Rate
  group: 趋近律选项卡
  block_parameter: ReachingLaw
  values: '"Constant Rate"（默认） | "Exponential" | "Power Rate"'
- name: 趋近速率 (Eta)
  summary: 趋近速率 0.01（默认） | 正标量 | 列向量
  group: 趋近律选项卡
  block_parameter: ReachingRate
  values: '"0.01"（默认） | 引号中的正标量 | 引号中的列向量'
- name: 控制增益 (K)
  summary: 控制增益 0.01（默认） | 正标量 | 列向量
  group: 趋近律选项卡
  block_parameter: ControlGain
  values: '"0.01"（默认） | 引号中的正标量 | 引号中的列向量'
- name: Power Rate Exponent (Alpha)
  summary: 幂次趋近律指数 0.01（默认）| 0 到 1 之间的正标量 | 0 到 1 之间的正数列向量
  group: 趋近律选项卡
  block_parameter: PowerRate
  values: '"0.01"（默认）| 带引号的 0 到 1 之间的正标量 | 带引号的 0 到 1 之间的正数列向量'
- name: Select Boundary Layer
  summary: 边界层函数 Sign（默认）| Relay | Hyperbolic Tangent | Saturation
  group: 趋近律选项卡
  block_parameter: BoundaryLayer
  values: '"Sign"（默认）| "Relay" | "Hyperbolic Tangent" | "Saturation"'
- name: Enable zero-crossing detection
  summary: 启用过零检测 off（默认）| on
  group: 趋近律选项卡
  block_parameter: ZeroCross
  values: '"off"（默认）| "on"'
- name: Phi
  summary: 边界层厚度 0.01（默认）| 正标量 | 列向量
  group: 趋近律选项卡
  block_parameter: Phi
  values: '"0.01"（默认）| 带引号的正标量 | 带引号的列向量'
```

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### Sliding Surface Tab

### **Task Mode** — 模块运行模式 **Regulation Mode**（默认）| **Tracking Mode**

模块运行模式，指定为以下之一：

- **Regulation Mode** — 当您希望将系统稳定在固定点，即将所有状态 *x* 驱动至零时，使用此模式。
- **Tracking Mode** — 当您希望系统状态跟随参考轨迹 *xref* 时，使用此模式。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `TaskMode` |
| **值**：| `"Regulation Mode"`（默认）| `"Tracking Mode"` |

**Example:** `set_param(gcb,"TaskMode","Tracking Mode")`

### **Sliding Coefficient Matrix (C)** — 滑动系数矩阵 `1`（默认）| 标量 | 列向量 | 矩阵

滑动系数矩阵（*C*），指定为 *nx*×*nu* 矩阵，其中 *nx* 是状态数量，*nu* 是控制输入数量。

矩阵 *C* 决定了滑模控制将系统状态驱动至的超平面。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SlidingMatrix` |
| **值**：| `1`（默认）| 带引号的标量 | 带引号的列向量 | 带引号的矩阵 |

**Example:** `set_param(gcb,"SlidingMatrix","[1;2]")`

### **Use externally sourced derivative** — 从外部指定状态参考的导数 `off`（默认）| `on`

选择此项以在输入端口 **x.ref.dot** 处从外部指定状态参考信号的导数。

#### 依赖关系

要启用此参数，请将 **Task Mode** 设置为 **Tracking Mode**。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `EnableTrackingDerivative` |
| **值：** | `"off"`（默认） | `"on"` |

**示例：** `set_param(gcb,"EnableTrackingDerivative","on")`

### **输出切换函数** — 输出切换函数 `off`（默认） | `on`

选择以在输出端口返回滑模面值
**s(x)**。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `EnableSwitchingFunction` |
| **值：** | `"off"`（默认） | `"on"` |

**示例：** `set_param(gcb,"EnableSwitchingFunction","on")`

### 趋近律选项卡

### **趋近律** — 趋近律 `Constant Rate`（默认） | `Exponential` | `Power Rate`

滑模面的趋近律
*h*(*s*(*x*))，指定为以下之一。

- `Constant Rate` — h(s(x))=−ηiθ(si)

  该律提供到达滑模面的恒定速率。此处，
  *θ*(*si*)
  是边界层，
  *ηi* 是第 *i* 个控制输入的趋近
  速率。
- `Exponential` — h(s(x))=−ηiθ(si)−Kisi

  该律添加了一个与滑模变量成比例的项，并在状态偏差
  显著时提供更激进的收敛。此处，
  *Ki* 是控制
  增益项，用于缩放与第
  *i* 个滑模变量相关的控制作用。
- `Power Rate` — h(s(x))i=−ηi|si|αθ(si)

  该律在状态远离滑模面时提供快速趋近
  速度，但在状态接近时降低速度。这确保了减少抖振并提供
  快速收敛。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ReachingLaw` |
| **值：** | `"Constant Rate"`（默认） | `"Exponential"` | `"Power Rate"` |

**示例：** `set_param(gcb,"ReachingLaw","Power
Rate")`

### **趋近速率 (Eta)** — 趋近速率 `0.01`（默认） | 正标量 | 列向量

趋近速率（*η*），指定为正标量
或长度等于控制输入数量的正值列向量。

趋近速率决定系统轨迹
接近滑模面的速率。*η*
值越大，收敛到滑模面越快，但也可能导致
更高的控制作用，这在所有情况下都不理想，因为
可能存在执行器饱和或抖振增加等问题。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ReachingRate` |
| **值：** | `"0.01"`（默认） | 引号中的正标量 | 引号中的列向量 |

**示例：** `set_param(gcb,"ReachingRate","0.05")`

### **控制增益 (K)** — 控制增益 `0.01`（默认） | 正标量 | 列向量

指数趋近律中比例项的控制增益，指定为
正标量或长度等于控制输入数量的列向量。在指数趋近律中，该项增加
与偏离滑模面成比例的控制作用。

#### 依赖关系

要启用此参数，请将 **趋近律** 设置为
`Exponential`。

#### 程序化使用

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ControlGain` |
| **值：** | `"0.01"`（默认） | 引号中的正标量 | 引号中的列向量 |

**示例：** `set_param(gcb,"ControlGain","2")`

### **Power Rate Exponent (Alpha)** — 幂次趋近律指数 `0.01`（默认）| 0 到 1 之间的正标量 | 0 到 1 之间的正数列向量

幂次趋近律中的指数值，指定为 0 到 1 之间的正标量或长度等于控制输入数量的列向量。此参数决定控制作用相对于距滑模面距离的非线性程度。具体而言，它调整控制努力随滑模变量幅值的缩放方式。*α* 的值影响趋近滑模面的平滑度。较低的值导致更柔和的趋近，并可能减少抖振。

#### 依赖关系

要启用此参数，请将 **Reaching Law** 设置为 `Power Rate`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PowerRate` |
| **值：** | `"0.01"`（默认）| 带引号的 0 到 1 之间的正标量 | 带引号的 0 到 1 之间的正数列向量 |

**示例：** `set_param(gcb,"PowerRate","0.02")`

### **Select Boundary Layer** — 边界层函数 `Sign`（默认）| `Relay` | `Hyperbolic Tangent` | `Saturation`

边界层函数，指定为以下之一：

- `Sign` — θ(s)=sgn(s(x))

  此选项使用默认符号函数，并在 –1 和 1 之间不连续切换。
- `Relay` — θ(s)=s|s|+ϕ

  此选项使用继电器函数来定义滑模面周围的切换边界。
- `Hyperbolic Tangent` — θ(s)=tanh(sϕ)

  此选项使用双曲正切函数来定义滑模面周围的切换边界。
- `Saturation` — θ(s)={1s>ϕkss≤ϕ−1s<−ϕk=1ϕ

  此选项使用饱和函数，在滑模变量位于边界层 [*–ϕ*,*ϕ*] 内时，在 –1 和 1 之间平滑插值，从而减少高频切换。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `BoundaryLayer` |
| **值：** | `"Sign"`（默认）| `"Relay"` | `"Hyperbolic Tangent"` | `"Saturation"` |

**示例：** `set_param(gcb,""BoundaryLayer,"Saturation")`

### **Enable zero-crossing detection** — 启用过零检测 `off`（默认）| `on`

选择以启用过零检测。有关详细信息，请参阅 Zero-Crossing Detection。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ZeroCross` |
| **值：** | `"off"`（默认）| `"on"` |

**示例：** `set_param(gcb,"ZeroCross","on")`

### **Phi** — 边界层厚度 `0.01`（默认）| 正标量 | 列向量

边界层厚度参数，指定为正标量或长度等于控制输入数量的列向量。

此参数定义滑模面周围的边界层厚度。较大的 **Phi** 值导致较少的抖振，但可能增加稳态误差。相反，较小的 **Phi** 值可以减少稳态误差，但会增加抖振。

#### 依赖关系

要启用此参数，请将 **Select Boundary Layer** 设置为以下任一值：

- `Relay`
- `Hyperbolic Tangent`
- `Saturation`

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Phi` |
| **值：** | `"0.01"`（默认）| 带引号的正标量 | 带引号的列向量 |

**示例：** `set_param(gcb,"Phi","0.05")`
## 所属库

Simulink Control Design / Sliding Mode

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

基于趋近律设计滑模控制器

滑模控制（SMC）是一种鲁棒控制策略，它将系统状态轨迹引导至指定的滑模面并使其保持在该滑模面上。这种方法对于需要高精度和高鲁棒性的系统具有优势，尤其是在存在扰动和不确定性的情况下。一旦系统到达滑模面，SMC 确保系统即使面对系统动态的外部或内部变化也能保持在该路径上。

滑模控制器模块使您能够为以方程 x˙=f(x)+g(x)u 为特征的非线性系统实现 SMC。使用此模块，您可以创建一个使用趋近律的补偿器，趋近律是一种动态调整控制作用以高效引导系统状态趋向滑模面的方法。该模块提供以下两种操作模式：

- 调节模式

  u=(CTg(x))−1(−CTf(x)+h(s(x)))s(x)=CTx
- 跟踪模式

  u=(CTg(x))−1(CTx˙ref−CTf(x)+h(s(x)))s(x)=CT(xref−x)

其中，*C* 是滑模系数矩阵，*s*(*x*) 是切换函数，*h*(*s*(*x*)) 是趋近律。

此外，SMC 能够最小化抖振效应，这是以控制信号快速振荡或高频切换为特征的控制系统中常见的挑战。该模块允许您自定义滑模面并调整趋近律参数。这使您能够根据特定的系统动态和目标来调节控制策略，从而增强系统在各种条件下的稳定性和响应能力。

有关 SMC 的更多信息，请参阅滑模控制。
