---
type: simulink-block
title: 'Virtual Reference Feedback Tuning'
family: 'autotuning'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Autotuning'
documentation_page: 'virtualreferencefeedbacktuning'
documentation_source_path: 'ug/virtualreferencefeedbacktuning.html'
language: zh-CN
chinese_source: worker-translation
---

# Virtual Reference Feedback Tuning

## 端口

### 输入

### **u** — 被控对象输入信号 标量信号

在此端口提供被控对象输入信号数据。对于此模块，您可以在仿真期间（在线调优）提供输入-输出数据，也可以提供预先记录的数据（离线调优）。

### **y** — 被控对象输出信号 标量信号

在此端口提供被控对象输出信号数据。对于此模块，您可以在仿真期间（在线调优）提供输入-输出数据，也可以提供预先记录的数据（离线调优）。

### **start/stop** — 调优区间信号 标量信号

要启动和停止调优过程，请在 **start/stop** 端口提供信号。当信号值发生如下变化时：

- 从负值或零变为正值，调优开始
- 从正值变为负值或零，信号生成停止

通常，您可以使用从 0 变为 1 的信号来启动调优，并使用从 1 变为 0 的信号来停止调优。您还可以使用 Start-Stop Generator 模块生成此信号。

生成足够长的调优区间信号，以便算法收集足够的数据，使所有 *θ* 值收敛。
### 输出

### **θ** — 调优后的控制器参数 向量

调优后的控制器参数，以 *n*×1 向量信号形式返回，其中 *n* 是控制器参数的数量。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上的 **准备** 库中，选择 **属性检查器**。

### **采样时间 (Ts)** — 采样时间 `0.1`（默认） | 正标量

模块的采样时间，指定为正标量。该模块使用此值对输入-输出数据进行采样。此值必须与您正在调优的控制器的采样时间匹配。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `DiscreteTs` |
| **值：** | `"0.1"`（默认） | 带引号的正标量 |

**示例：** `set_param(gcb,"DiscreteTs","0.5")`

### **参考模型** — 参考模型 `tf(1,[3 1])`（默认） | `tf` 模型对象 | `ss` 模型对象 | `zpk` 模型对象

参考模型，指定为 `tf`、`ss` 或 `zpk` 对象。参考模型描述系统从参考 *r*(*t*) 到输出 *y*(*t*) 的期望闭环行为。对于此参数，您可以提供连续时间或离散时间模型作为输入。当输入为连续时间模型时，该模块使用 Tustin 离散化对模型进行离散化。当您要提供离散时间模型时，采样时间必须与 **采样时间** 参数值匹配。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `MrefS` |
| **值：** | `"tf(1,[3 1])"`（默认） | 带引号的 `tf`、`ss` 或 `zpk` 模型对象 |

**示例：** `set_param(gcb,"MrefS","zpk([],-3,3)")`

### **加权函数** — 加权函数 `1`（默认） | `tf` 模型对象 | `ss` 模型对象 | `zpk` 模型对象

加权函数，指定为 `tf`、`ss` 或 `zpk` 对象。您可以使用此参数来强调特定频率，在这些频率处，将 *r*(*t*)-到-*y*(*t*) 传递函数与参考模型匹配最为重要。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `WeightS` |
| **值：** | `"1"`（默认） | 带引号的 `tf`、`ss` 或 `zpk` 模型对象 |

**示例：** `set_param(gcb,"WeightS","tf([0.1 3],[1
0.03])")`

### **控制器结构** — 控制器结构 `PID`（默认） | `FIR Filter` | `Generic Form`

要调优的控制器结构，指定为以下之一：

- **PID Controller** — 调优并联形式 PID 控制器。

  C(θ,z)=P+Iα(z)+D1Tsz−1zθ1=Pθ2=Iθ3=D

  这里，*α*(*z*) 是离散时间积分器公式。
- **FIR Filter** — 调优 FIR 滤波器。

  C(z,b)=b0+b1z+…+bnznθ1=b0,θ2=b1,...θn+1=bn
- **Generic Form** — 调优通用形式控制器。这可以表示线性参数化控制器的组合。

  C(z,θ)=θ1C1(z)+θ2C2(z)+…+θnCn(z)

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ControlType` |
| **值：** | `"PID"`（默认） | `"FIR Filter"` | `"Generic Form"` |

**示例：** `set_param(gcb,"ControlType","Generic
Form")`

### **类型** — PID 控制器类型 `PI`（默认） | `P` | `I` | `PD` | `PID`

指定控制器中包含比例、积分和微分项中的哪些项。

- `P` — 仅比例作用。
- `I` — 仅积分作用。
- `PI` — 仅比例和积分作用。
- `PD` — 仅比例和微分作用。
- `PID` — 比例、积分和微分作用。

#### 依赖关系

要启用此参数，请将 **控制器结构** 设置为 **PID**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PIDControlType` |
| **值：** | `"PI"`（默认） | `"P"` | `"I"` | `"PD"` | `"PID"` |

**示例：** `set_param(gcb,"PIDControlType","PID")`

### **积分器方法** — 离散积分方法 `Forward Euler`（默认） | `Backward Euler` | `Trapezoidal`

用于离散时间 PID 控制器中积分的离散积分器公式 *α*(*z*)：

C(z)=P+Iα(z)+D1Tsz−1z

将 **积分器方法** 指定为以下之一：

- `Forward Euler` — α(z)=Tsz−1.
- `Backward Euler` — α(z)=Tszz−1.
- `Trapezoidal` — α(z)=Ts2z+1z−1.

有关离散时间积分的详细信息，请参阅 Discrete-Time Integrator 模块参考页。

#### 依赖关系

要启用此参数，请将 **控制器结构** 设置为 **PID**，并将 **类型** 设置为具有积分作用的控制器类型。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PIDIntegratorMethod` |
| **值：** | `"Forward Euler"`（默认） | `"Backward Euler"` | `"Trapezoidal"` |

**示例：** `set_param(gcb,"PIDIntegratorMethod","Trapezoidal")`

### **FIR 滤波器阶数** — FIR 滤波器阶数 `2`（默认） | 2 到 10 之间的正整数

要调优的 FIR 滤波器阶数，指定为 2 到 10 之间的正整数。

#### 依赖关系

要启用此参数，请将 **控制器结构** 设置为 **FIR Filter**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FIRFilterOrder` |
| **值：** | `"2"`（默认） | 带引号的 2 到 10 之间的正整数 |

**示例：** `set_param(gcb,"FIRFilterOrder","5")`

### **SISO 线性系统 Ci(z)** — SISO 线性系统数组 `{tf([1],[1],0.1);0.1*tf([1],[1 -1],0.1)}`（默认） | 元胞数组 | LTI 模型数组

通用形式控制结构中的线性系统 *Ci*(*z*)，指定为 LTI 对象（`ss`、`tf`、`zpk`）的元胞数组或 LTI 模型数组。

C(z,θ)=θ1C1(z)+θ2C2(z)+…+θnCn(z)

指定此参数，使该值与要调优的控制器的形式匹配。这也可以表示线性参数化控制器的组合。这里，控制器参数 *θi* 的顺序对应于数组中提供的 LTI 对象的索引。例如，此参数的默认值表示离散时间并联形式 PID 控制器，其中 *θ1* 为比例增益，*θ2* 为积分增益。

#### 依赖关系

要启用此参数，请将 **控制器结构** 设置为 **Generic Form**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `LTIInputObj` |
| **值：** | `"{tf([1],[1],0.1);0.1*tf([1],[1 -1],0.1)}"`（默认） | 带引号的元胞数组 | 带引号的 LTI 模型数组 |

**示例：** `set_param(gcb,"LTIInputObj","{tf([1],[1],0.1);(1/0.1)*tf([1
-1],[1 0],0.1)}")`

### **调优时显示 θ 值** — 输出调优后的参数值 `on`（默认） | `off`

启用此选项可在调优时在模块输出端口 **θ** 输出 *θ* 的瞬态值。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ShowThetaWhileTuning` |
| **值：** | `"on"`（默认） | `"off"` |

**示例：** `set_param(gcb,"ShowThetaWhileTuning","off")`

## 所属库

Simulink Control Design / Autotuning

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

基于输入-输出数据自动调优线性参数化控制器

虚拟参考反馈调优 (VRFT) 是一种直接数据驱动控制技术，允许您基于被控对象输入和输出数据调优线性参数化控制器。您可以使用 Virtual Reference Feedback Tuning 模块实现 VRFT。Virtual Reference Feedback Tuning 模块的主要优点包括：能够执行一次性调优，仅需单个实验；适用于调优线性控制律的线性组合，包括 PID 和 FIR；以及支持在线和离线工作流。使用此模块，您可以调优按以下形式之一参数化的控制器：

- **PID Controller** — 调优并联形式 PID 控制器。

  C(θ,z)=P+Iα(z)+D1Tsz−1zθ1=Pθ2=Iθ3=D

  这里，*α*(*z*) 是离散时间积分器公式。
- **FIR Filter** — 调优 FIR 滤波器。

  C(z,b)=b0+b1z+…+bnznθ1=b0,θ2=b1,...θn+1=bn
- **Generic Form** — 调优通用形式控制器。这可以表示线性参数化控制器的组合。

  C(z,θ)=θ1C1(z)+θ2C2(z)+…+θnCn(z)

有关 VRFT 的详细信息，请参阅 Virtual Reference Feedback Tuning。
