---
type: simulink-block
title: 'Virtual Reference Feedback Tuning'
family: 'slcontrol'
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
```yaml
ports:
- name: u
  summary: 被控对象输入信号 标量信号
  direction: input
- name: y
  summary: 被控对象输出信号 标量信号
  direction: input
- name: start/stop
  summary: 整定区间信号 标量信号
  direction: input
- name: θ
  summary: 整定后的控制器参数 向量
  direction: output
```

### 输入

### **u** — 被控对象输入信号 标量信号

在此端口提供被控对象输入信号数据。对于此模块，您可以在仿真期间提供输入-输出数据（在线整定），也可以提供预先记录的数据（离线整定）。

### **y** — 被控对象输出信号 标量信号

在此端口提供被控对象输出信号数据。对于此模块，您可以在仿真期间提供输入-输出数据（在线整定），也可以提供预先记录的数据（离线整定）。

### **start/stop** — 整定区间信号 标量信号

要启动和停止整定过程，请在 **start/stop** 端口提供信号。当信号值发生以下变化时：

- 从负值或零变为正值，整定开始
- 从正值变为负值或零，信号生成停止

通常，您可以使用从 0 变为 1 的信号来启动整定，使用从 1 变为 0 的信号来停止整定。您也可以使用 Start-Stop Generator 模块来生成此信号。

生成足够长的整定区间信号，使算法能够收集足够的数据，以便所有 *θ* 值收敛。

### 输出

### **θ** — 整定后的控制器参数 向量

整定后的控制器参数，以 *n*×1 向量信号形式返回，其中 *n* 是控制器参数的数量。
## 参数
```yaml
parameters:
- name: Sample time (Ts)
  summary: 采样时间 0.1（默认）| 正标量
  group: ''
  block_parameter: DiscreteTs
  values: '"0.1"（默认）| 带引号的正标量'
- name: Reference Model
  summary: 参考模型 tf(1,[3 1])（默认）| tf 模型对象 | ss 模型对象 | zpk 模型对象
  group: ''
  block_parameter: MrefS
  values: '"tf(1,[3 1])"（默认）| 带引号的 tf、ss 或 zpk 模型对象'
- name: Weighting Function
  summary: 加权函数 1（默认）| tf 模型对象 | ss 模型对象 | zpk 模型对象
  group: ''
  block_parameter: WeightS
  values: '"1"（默认）| 带引号的 tf、ss 或 zpk 模型对象'
- name: Controller Structure
  summary: 控制器结构 PID（默认）| FIR Filter | Generic Form
  group: ''
  block_parameter: ControlType
  values: '"PID"（默认）| "FIR Filter" | "Generic Form"'
- name: Type
  summary: PID 控制器类型 PI（默认）| P | I | PD | PID
  group: ''
  block_parameter: PIDControlType
  values: '"PI"（默认）| "P" | "I" | "PD" | "PID"'
- name: Integrator Method
  summary: 离散积分方法 Forward Euler（默认）| Backward Euler | Trapezoidal
  group: ''
  type: 设置为具有积分作用的控制器类型。
  block_parameter: PIDIntegratorMethod
  values: '"Forward Euler"（默认）| "Backward Euler" | "Trapezoidal"'
- name: FIR Filter Order
  summary: FIR 滤波器阶数 2（默认）| 介于 2 和 10 之间的正整数
  group: ''
  block_parameter: FIRFilterOrder
  values: '"2"（默认）| 带引号的介于 2 和 10 之间的正整数'
- name: SISO Linear Systems Ci(z)
  summary: SISO 线性系统数组 {tf([1],[1],0.1);0.1*tf([1],[1 -1],0.1)}（默认）| 元胞数组 | LTI 模型数组
  group: ''
  block_parameter: LTIInputObj
  values: '"{tf([1],[1],0.1);0.1*tf([1],[1 -1],0.1)}"（默认） | 带引号的元胞数组 | 带引号的 LTI 模型数组'
- name: 整定时显示 θ 值
  summary: 输出整定后的参数值 on（默认） | off
  group: ''
  block_parameter: ShowThetaWhileTuning
  values: '"on"（默认） | "off"'
```

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### **Sample time (Ts)** — 采样时间 `0.1`（默认）| 正标量

模块的采样时间，指定为正标量。模块使用此值对输入-输出数据进行采样。此值必须与您正在整定的控制器的采样时间一致。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `DiscreteTs` |
| **值**：| `"0.1"`（默认）| 带引号的正标量 |

**Example:** `set_param(gcb,"DiscreteTs","0.5")`

### **Reference Model** — 参考模型 `tf(1,[3 1])`（默认）| `tf` 模型对象 | `ss` 模型对象 | `zpk` 模型对象

参考模型，指定为 `tf`、`ss` 或 `zpk` 对象。参考模型描述了系统从参考 *r*(*t*) 到输出 *y*(*t*) 的期望闭环行为。对于此参数，您可以提供连续时间或离散时间模型作为输入。当输入为连续时间模型时，模块使用 Tustin 离散化方法对模型进行离散化。当您想提供离散时间模型时，采样时间必须与 **Sample Time** 参数值一致。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `MrefS` |
| **值**：| `"tf(1,[3 1])"`（默认）| 带引号的 `tf`、`ss` 或 `zpk` 模型对象 |

**Example:** `set_param(gcb,"MrefS","zpk([],-3,3)")`

### **Weighting Function** — 加权函数 `1`（默认）| `tf` 模型对象 | `ss` 模型对象 | `zpk` 模型对象

加权函数，指定为 `tf`、`ss` 或 `zpk` 对象。您可以使用此参数来强调特定频率，在这些频率处，将 *r*(*t*) 到 *y*(*t*) 的传递函数与参考模型进行匹配最为重要。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `WeightS` |
| **值**：| `"1"`（默认）| 带引号的 `tf`、`ss` 或 `zpk` 模型对象 |

**Example:** `set_param(gcb,"WeightS","tf([0.1 3],[1
0.03])")`

### **Controller Structure** — 控制器结构 `PID`（默认）| `FIR Filter` | `Generic Form`

要整定的控制器结构，指定为以下选项之一：

- **PID Controller** — 整定
  并联形式 PID 控制器。

  C(θ,z)=P+Iα(z)+D1Tsz−1zθ1=Pθ2=Iθ3=D

  此处，*α*(*z*) 是
  离散时间积分器公式。
- **FIR Filter** — 整定 FIR
  滤波器。

  C(z,b)=b0+b1z+…+bnznθ1=b0,θ2=b1,...θn+1=bn
- **Generic Form** — 整定
  通用形式控制器。这可以表示线性参数化控制器的组合。

  C(z,θ)=θ1C1(z)+θ2C2(z)+…+θnCn(z)

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `ControlType` |
| **值**：| `"PID"`（默认）| `"FIR Filter"` | `"Generic Form"` |

**Example:** `set_param(gcb,"ControlType","Generic
Form")`

### **Type** — PID 控制器类型 `PI`（默认）| `P` | `I` | `PD` | `PID`

指定控制器中包含比例、积分和微分项中的哪些项。

- `P` — 仅比例作用。
- `I` — 仅积分作用。
- `PI` — 仅比例和积分作用。
- `PD` — 仅比例和微分作用。
- `PID` — 比例、积分和微分作用。

#### 依赖关系

要启用此参数，请将 **Controller
Structure** 设置为 **PID**。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PIDControlType` |
| **值**：| `"PI"`（默认）| `"P"` | `"I"` | `"PD"` | `"PID"` |

**Example:** `set_param(gcb,"PIDControlType","PID")`

### **Integrator Method** — 离散积分方法 `Forward Euler`（默认）| `Backward Euler` | `Trapezoidal`

用于离散时间 PID 控制器中积分的离散积分器公式 *α*(*z*)：

C(z)=P+Iα(z)+D1Tsz−1z

将 **Integrator Method** 指定为以下选项之一：

- `Forward Euler` — α(z)=Tsz−1。
- `Backward Euler` — α(z)=Tszz−1。
- `Trapezoidal` — α(z)=Ts2z+1z−1。

有关离散时间积分的详细信息，请参阅 Discrete-Time Integrator
模块参考页。

#### 依赖关系

要启用此参数，请将 **Controller
Structure** 设置为 **PID**，并将
**Type** 设置为具有积分作用的控制器类型。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PIDIntegratorMethod` |
| **值**：| `"Forward Euler"`（默认）| `"Backward Euler"` | `"Trapezoidal"` |

**Example:** `set_param(gcb,"PIDIntegratorMethod","Trapezoidal")`

### **FIR Filter Order** — FIR 滤波器阶数 `2`（默认）| 介于 2 和 10 之间的正整数

要整定的 FIR 滤波器阶数，指定为介于 2 和 10 之间的正整数。

#### 依赖关系

要启用此参数，请将 **Controller
Structure** 设置为 **FIR Filter**。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `FIRFilterOrder` |
| **值**：| `"2"`（默认）| 带引号的介于 2 和 10 之间的正整数 |

**Example:** `set_param(gcb,"FIRFilterOrder","5")`

### **SISO Linear Systems Ci(z)** — SISO 线性系统数组 `{tf([1],[1],0.1);0.1*tf([1],[1 -1],0.1)}`（默认）| 元胞数组 | LTI 模型数组

通用形式控制结构中的线性系统
*Ci*(*z*)，指定为 LTI 对象
（`ss`、`tf`、`zpk`）的元胞数组或
LTI 模型数组。

C(z,θ)=θ1C1(z)+θ2C2(z)+…+θnCn(z)

指定此参数时应使该值与要整定的控制器形式匹配。这也可以表示线性
参数化控制器的组合。此处，控制器参数
*θi* 的顺序
对应于数组中提供的 LTI 对象的索引。例如，此参数的默认值表示一个离散时间
并联形式 PID 控制器，其中
*θ1* 为比例增益，
*θ2* 为积分
增益。

#### 依赖关系

要启用此参数，请将 **控制器结构** 设置为 **通用形式**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `LTIInputObj` |
| **值：** | `"{tf([1],[1],0.1);0.1*tf([1],[1 -1],0.1)}"`（默认） | 带引号的元胞数组 | 带引号的 LTI 模型数组 |

**示例：** `set_param(gcb,"LTIInputObj","{tf([1],[1],0.1);(1/0.1)*tf([1
-1],[1 0],0.1)}")`

### **整定时显示 θ 值** — 输出整定后的参数值 `on`（默认） | `off`

启用此选项可在整定时于模块输出端口 **θ** 输出 *θ* 的瞬态值。

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

基于输入-输出数据自动整定线性参数化控制器

虚拟参考反馈整定（VRFT）是一种直接数据驱动控制技术，允许您基于被控对象输入和输出数据整定线性参数化控制器。您可以使用 Virtual Reference Feedback Tuning 模块实现 VRFT。Virtual Reference Feedback Tuning 模块的主要优势包括：能够执行一次性整定，仅需一次实验；适用于整定线性控制律的线性组合，包括 PID 和 FIR；以及支持在线和离线工作流。使用此模块，您可以整定以下列形式之一参数化的控制器：

- **PID 控制器** — 整定并联形式 PID 控制器。

  C(θ,z)=P+Iα(z)+D1Tsz−1zθ1=Pθ2=Iθ3=D

  此处，*α*(*z*) 是离散时间积分器公式。
- **FIR 滤波器** — 整定 FIR 滤波器。

  C(z,b)=b0+b1z+…+bnznθ1=b0,θ2=b1,...θn+1=bn
- **通用形式** — 整定通用形式控制器。这可以表示线性参数化控制器的组合。

  C(z,θ)=θ1C1(z)+θ2C2(z)+…+θnCn(z)

有关 VRFT 的更多信息，请参阅 Virtual Reference Feedback Tuning。
