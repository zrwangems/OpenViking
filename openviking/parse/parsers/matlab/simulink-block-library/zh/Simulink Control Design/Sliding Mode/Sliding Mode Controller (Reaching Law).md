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

### 输入

### **x** — 系统状态向量

系统状态，指定为 *nx*-by-1 信号，其中 *nx* 是状态数。

**数据类型：** `single` | `double`

### **f(x)** — 系统动态函数向量

系统动态函数 *f*(*x*) 位于由方程 x˙=f(x)+g(x)u 描述的系统中。

将此端口连接到 *nx*-by-1 信号，其中 *nx* 是状态数。

**数据类型：** `single` | `double`

### **g(x)** — 输入函数向量

输入函数 *g*(*x*) 位于由方程 x˙=f(x)+g(x)u 描述的系统中。

将此端口连接到 *nx*-by-*nu* 信号，其中 *nx* 是状态数，*nu* 是输入数。

**数据类型：** `single` | `double`

### **x.ref** — 状态参考轨迹向量

跟踪模式下要跟随的状态参考轨迹，指定为 *nx*-by-1 信号，其中 *nx* 是状态数。

#### 依赖项

要启用此端口，请将 **Task Mode** 设置为 **Tracking Mode**。

### **x.ref.dot** — 状态参考轨迹的导数向量

跟踪模式下要跟随的状态参考轨迹的导数，指定为 *nx*-by-1 信号，其中 *nx* 是状态数。

当您想从外部输入提供状态参考轨迹的导数时，请使用此端口。否则，模块在仿真期间计算该导数。

#### 依赖项

要启用此端口：

- 将 **Task Mode** 设置为 **Tracking Mode**。
- 启用 **Use externally sourced derivative**。

### 输出

### **u** — 控制作用向量

计算得到的控制作用，返回为 *nu*-by-1 信号，其中 *nu* 是输入数。

### **s(x)** — 滑模变量值向量

滑模变量值，返回为 *nu*-by-1 信号，其中 *nu* 是输入数。

#### 依赖项

要启用此端口，请启用 **Output Switching Function** 参数。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，在 **Simulation** 选项卡的 **Prepare** 库中，选择 **Property Inspector**。

### 滑模面选项卡

### **Task Mode** — 模块工作模式 **Regulation Mode**（默认） | **Tracking Mode**

模块工作模式，指定为以下之一：

- **Regulation Mode** — 当您想要将系统稳定在固定点（即，将所有状态 *x* 置零）时，使用此模式。
- **Tracking Mode** — 当您想要系统状态跟随参考轨迹 *xref* 时，使用此模式。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TaskMode` |
| **值：** | `"Regulation Mode"`（默认） | `"Tracking Mode"` |

**示例：** `set_param(gcb,"TaskMode","Tracking
Mode")`

### **Sliding Coefficient Matrix (C)** — 滑模系数矩阵 `1`（默认） | 标量 | 列向量 | 矩阵

滑模系数矩阵 (*C*)，指定为 *nx*-by-*nu* 矩阵，其中 *nx* 是状态数，*nu* 是控制输入数。

矩阵 *C* 确定滑模控制将系统状态驱动到的超平面。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SlidingMatrix` |
| **值：** | `1`（默认） | 带引号的标量 | 带引号的列向量 | 带引号的矩阵 |

**示例：** `set_param(gcb,"SlidingMatrix","[1;2]")`

### **Use externally sourced derivative** — 外部指定状态参考的导数 `off`（默认） | `on`

选择此项以在输入端口 **x.ref.dot** 外部指定状态参考信号的导数。

#### 依赖项

要启用此参数，请将 **Task Mode** 设置为 **Tracking Mode**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `EnableTrackingDerivative` |
| **值：** | `"off"`（默认） | `"on"` |

**示例：** `set_param(gcb,"EnableTrackingDerivative","on")`

### **Output Switching Function** — 输出开关函数 `off`（默认） | `on`

选择此项以在输出端口 **s(x)** 返回滑模面值。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `EnableSwitchingFunction` |
| **值：** | `"off"`（默认） | `"on"` |

**示例：** `set_param(gcb,"EnableSwitchingFunction","on")`

### 趋近律选项卡

### **Reaching Law** — 趋近律 `Constant Rate`（默认） | `Exponential` | `Power Rate`

滑模面的趋近律 *h*(*s*(*x*))，指定为以下之一。

- `Constant Rate` — h(s(x))=−ηiθ(si)

  该律提供到达滑模面的恒定速率。这里，*θ*(*si*) 是边界层，*ηi* 是第 *i* 个控制输入的趋近速率。
- `Exponential` — h(s(x))=−ηiθ(si)−Kisi

  该律添加与滑模变量成比例的项，并在状态偏差显著时提供更积极的收敛。这里，*Ki* 是控制增益项，用于缩放与第 *i* 个滑模变量相关的控制作用。
- `Power Rate` — h(s(x))i=−ηi|si|αθ(si)

  该律在状态远离滑模面时提供快速趋近速度，但当状态接近时降低速度。这可确保减少抖振并提供快速收敛。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ReachingLaw` |
| **值：** | `"Constant Rate"`（默认） | `"Exponential"` | `"Power Rate"` |

**示例：** `set_param(gcb,"ReachingLaw","Power
Rate")`

### **Reaching Rate (Eta)** — 趋近速率 `0.01`（默认） | 正标量 | 列向量

趋近速率 (*η*)，指定为正标量或长度等于控制输入数的正值列向量。

趋近速率决定系统轨迹接近滑模面的速率。*η* 的较大值会导致更快收敛到滑模面，但也可能导致更高的控制作用，由于可能的问题（如执行器饱和或抖振增加），这在所有情况下都不理想。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ReachingRate` |
| **值：** | `"0.01"`（默认） | 带引号的正标量 | 带引号的列向量 |

**示例：** `set_param(gcb,"ReachingRate","0.05")`

### **Control Gain (K)** — 控制增益 `0.01`（默认） | 正标量 | 列向量

指数趋近律中比例项的控制增益，指定为正标量或长度等于控制输入数的列向量。在指数趋近律中，该项按与滑模面偏差成比例的方式增加控制作用。

#### 依赖项

要启用此参数，请将 **Reaching Law** 设置为 `Exponential`。

#### 编程用法

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ControlGain` |
| **值：** | `"0.01"`（默认） | 带引号的正标量 | 带引号的列向量 |

**示例：** `set_param(gcb,"ControlGain","2")`

### **Power Rate Exponent (Alpha)** — 幂次趋近律指数 `0.01`（默认） | 介于 0 和 1 之间的正标量 | 介于 0 和 1 之间的正值列向量

幂次趋近律中的指数值，指定为介于 0 和 1 之间的正标量，或长度等于控制输入数的介于 0 和 1 之间的正值列向量。该参数确定控制作用相对于距滑模面距离的非线性。具体而言，它调整控制作用如何随滑模变量的幅值缩放。*α* 的值影响接近滑模面的平滑度。较低值会导致更柔和的接近，并可能减少抖振。

#### 依赖项

要启用此参数，请将 **Reaching Law** 设置为 `Power Rate`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PowerRate` |
| **值：** | `"0.01"`（默认） | 带引号的介于 0 和 1 之间的正标量 | 带引号的介于 0 和 1 之间的正值列向量 |

**示例：** `set_param(gcb,"PowerRate","0.02")`

### **Select Boundary Layer** — 边界层函数 `Sign`（默认） | `Relay` | `Hyperbolic Tangent` | `Saturation`

边界层函数，指定为以下之一：

- `Sign` — θ(s)=sgn(s(x))

  此选项使用默认 signum 函数，并在 –1 和 1 之间不连续地切换。
- `Relay` — θ(s)=s|s|+ϕ

  此选项使用继电函数来定义滑模面周围的切换边界。
- `Hyperbolic Tangent` — θ(s)=tanh(sϕ)

  此选项使用双曲正切函数来定义滑模面周围的切换边界。
- `Saturation` — θ(s)={1s>ϕkss≤ϕ−1s<−ϕk=1ϕ

  此选项使用饱和函数，在滑模变量位于边界层 [*–ϕ*,*ϕ*] 内时在 –1 和 1 之间平滑插值，从而减少高频切换。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `BoundaryLayer` |
| **值：** | `"Sign"`（默认） | `"Relay"` | `"Hyperbolic Tangent"` | `"Saturation"` |

**示例：** `set_param(gcb,""BoundaryLayer,"Saturation")`

### **Enable zero-crossing detection** — 启用过零检测 `off`（默认） | `on`

选择此项以启用过零检测。有关详细信息，请参阅 Zero-Crossing Detection。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ZeroCross` |
| **值：** | `"off"`（默认） | `"on"` |

**示例：** `set_param(gcb,"ZeroCross","on")`

### **Phi** — 边界层厚度 `0.01`（默认） | 正标量 | 列向量

边界层厚度参数，指定为正标量或长度等于控制输入数的列向量。

该参数定义滑模面周围的边界层厚度。较大的 **Phi** 值会导致较少的抖振，但可能增加稳态误差。相反，较小的 **Phi** 值可以减少稳态误差，但会增加抖振。

#### 依赖项

要启用此参数，请将 **Select Boundary Layer** 设置为以下任一值：

- `Relay`
- `Hyperbolic Tangent`
- `Saturation`

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Phi` |
| **值：** | `"0.01"`（默认） | 带引号的正标量 | 带引号的列向量 |

**示例：** `set_param(gcb,"Phi","0.05")`

## 所属库

Simulink Control Design / Sliding Mode

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2024b 中引入**

## 描述

基于趋近律设计滑模控制器

滑模控制 (SMC) 是一种鲁棒控制策略，它将系统状态轨迹带到指定的滑模面，并将其保持在那里。对于需要高精度和鲁棒性的系统，尤其是在存在扰动和不确定性时，这种方法具有优势。一旦系统到达滑模面，SMC 确保它保持在该路径上，尽管系统动力学发生任何外部或内部变化。

Sliding Mode Controller 模块使您能够为以方程 x˙=f(x)+g(x)u 描述的非线性系统实现 SMC。使用此模块，您可以创建一个补偿器，该补偿器使用趋近律，这是一种动态调整控制作用以有效地引导系统状态趋向滑模面的方法。该模块提供以下两种工作模式：

- Regulation mode

  u=(CTg(x))−1(−CTf(x)+h(s(x)))s(x)=CTx
- Tracking mode

  u=(CTg(x))−1(CTx˙ref−CTf(x)+h(s(x)))s(x)=CT(xref−x)

这里，*C* 是滑模系数矩阵，*s*(*x*) 是切换函数，*h*(*s*(*x*)) 是趋近律。

此外，SMC 可最小化抖振效应，这是控制系统中的一个常见挑战，其特征是控制信号的快速振荡或高频切换。该模块允许您自定义滑模面并调整趋近律参数。这使您能够根据特定系统动力学和目标调整控制策略，从而增强系统在各种条件下的稳定性和响应。

有关 SMC 的详细信息，请参阅 Sliding Mode Control。
