---
type: simulink-block
title: 'Iterative Learning Control'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Adaptive Control'
documentation_page: 'iterativelearningcontrol'
documentation_source_path: 'ug/iterativelearningcontrol.html'
language: zh-CN
chinese_source: worker-translation
---

# Iterative Learning Control

## 端口
```yaml
ports:
- name: error
  summary: 误差信号 标量 | 向量
  direction: input
  data_types: single | double
- name: control/reset
  summary: ILC 模式信号 标量
  direction: input
  data_types: Boolean
- name: u
  summary: 更新后的控制信号 标量 | 向量
  direction: output
  data_types: single | double
```

### 输入

### **error** — 误差信号 标量 | 向量

指定此端口处期望参考信号与输出之间的误差。

**数据类型：** `single` | `double`

### **control/reset** — ILC 模式信号 标量

指定此端口处的 ILC 模式信号。在运行时，模块在两种模式之间切换：控制和重置。在控制模式下，模块在指定的时间点输出
*uk*(*t*)
并测量期望参考 *r*(*t*) 与输出
*yk*(*t*)
之间的误差。在控制模式结束时，模块计算新的控制序列
*uk+1*(*t*)
以在下次迭代中使用。在重置模式下，模块输出为 0。

通常，您可以使用从 0 变为 1 的信号来切换到控制模式，使用从 1 变为 0 的信号来切换到重置模式。重置模式必须足够长，以便此模式下的参考信号通过标称控制器将被控对象带回其初始条件。

**数据类型：** `Boolean`
### 输出

### **u** — 更新后的控制信号 标量 | 向量

第 *k* 次迭代的更新控制信号。模块在指定的时间点输出
*uk*(*t*)
并测量期望参考与输出之间的误差。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Sample time (Ts)
  summary: ILC 采样时间 0.01（默认）| 正标量
  group: ''
  block_parameter: Ts
  values: '"0.01"（默认）| 带引号的正标量'
- name: Iteration duration (Tspan)
  summary: 迭代持续时间 1（默认）| 正标量
  group: ''
  block_parameter: Tspan
  values: '"1"（默认）| 带引号的正标量'
- name: Data Type
  summary: 数据类型 double（默认）| single | <data type expression>
  group: ''
- name: ILC Algorithm
  summary: ILC 算法 Model free ILC（默认）| Model based ILC
  group: ''
  block_parameter: Algorithm
  values: '"Model free ILC"（默认）| "Model based ILC"'
- name: P-gain (gamma_p)
  summary: 无模型 ILC 中的比例增益 1（默认）| 非负标量
  group: ''
  block_parameter: gamma_p
  values: '"1"（默认）| 带引号的非负标量'
- name: D-gain (gamma_d)
  summary: 无模型 ILC 中的微分增益 0（默认）| 非负标量
  group: ''
  block_parameter: gamma_d
  values: '"0"（默认）| 带引号的非负标量'
- name: State Space Model
  summary: 模型时域 Continuous time（默认）| Discrete time (Ts)
  group: ''
  block_parameter: ModelTimeDomain
  values: '"Continuous time"（默认）| "Discrete time (Ts)"'
- name: A、B、C
  summary: 状态空间模型矩阵 1（默认）| 矩阵
  group: ''
- name: ILC methods
  summary: 基于模型的 ILC 方法 Gradient based（默认）| Inverse-model based
  group: ''
  block_parameter: ModelBasedILCType
  values: '"Gradient based"（默认）| "Inverse-model based"'
- name: ILC Gain (gamma_gradient)
  summary: 基于梯度的 ILC 增益 1（默认）| 正标量
  group: ''
  block_parameter: gamma_grad
  values: '"1"（默认）| 带引号的正标量'
- name: ILC Gain (gamma_inverse)
  summary: 基于逆模型的 ILC 增益 1（默认）
  group: ''
  block_parameter: gamma_inverse
  values: '"1"（默认）| 带引号的小于 2 的正标量'
- name: Enable first-order low-pass filter
  summary: 启用一阶低通滤波器 off（默认）| on
  group: ''
  block_parameter: LPFEnable
  values: '"off"（默认）| "on"'
- name: 滤波器时间常数 (tau)
  summary: 滤波器时间常数 1（默认）| 正标量
  group: ''
  block_parameter: tau
  values: '"1"（默认）| 带引号的正标量'
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### **Sample time (Ts)** — ILC 采样时间 `0.01`（默认）| 正标量

ILC 控制器的采样时间，指定为正标量。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ts` |
| **值：** | `"0.01"`（默认）| 带引号的正标量 |

**示例：** `set_param(gcb,"Ts","0.1")`

### **Iteration duration (Tspan)** — 迭代持续时间 `1`（默认）| 正标量

一次 ILC 迭代的持续时间，指定为正标量。此参数决定模块在控制模式下提供多少个控制动作。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tspan` |
| **值：** | `"1"`（默认）| 带引号的正标量 |

**示例：** `set_param(gcb,"Tspan","10")`

### **Data Type** — 数据类型 `double`（默认）| `single` | `<data type expression>`

指定输出数据类型。

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请点击 。

您可以指定以下数据类型。

- `Built in` —
  `single` 或
  `double` 数据类型。
- `Expression` — 使用指定类型的 MATLAB 表达式。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

### **ILC Algorithm** — ILC 算法 **Model free ILC**（默认）| **Model based ILC**

ILC 算法，指定为 **Model free ILC** 或 **Model based ILC**。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Algorithm` |
| **值：** | `"Model free ILC"`（默认）| `"Model based ILC"` |

**示例：** `set_param(gcb,"Algorithm","Model based
ILC")`

### **P-gain (gamma\_p)** — 无模型 ILC 中的比例增益 `1`（默认）| 非负标量

无模型 ILC 更新律中的比例增益（*γp*），指定为非负标量。无模型 ILC 更新律定义如下：

uk+1(t)=Q(q)(uk(t)+γpek(t+1)+γd(ek(t+1)−ek(t)))。

#### 依赖关系

要启用此参数，请将 **ILC Algorithm** 设置为 **Model free ILC**。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `gamma_p` |
| **值：** | `"1"`（默认）| 带引号的非负标量 |

**示例：** `set_param(gcb,"gamma_p","5")`

### **D-gain (gamma\_d)** — 无模型 ILC 中的微分增益 `0`（默认）| 非负标量

无模型 ILC 更新律中的微分增益 *γd*，指定为非负标量。无模型 ILC 更新律定义如下：

uk+1(t)=Q(q)(uk(t)+γpek(t+1)+γd(ek(t+1)−ek(t)))。

#### 依赖关系

要启用此参数，请将 **ILC Algorithm** 设置为 **Model free ILC**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `gamma_d` |
| **值：** | `"0"`（默认）| 带引号的非负标量 |

**示例：** `set_param(gcb,"gamma_d","1")`

### **State Space Model** — 模型时域 **Continuous time**（默认）| **Discrete time (Ts)**

基于模型 ILC 中状态空间模型的时域，指定为 **Continuous time** 或 **Discrete time (Ts)**。模型的采样时间必须等于使用 **Sample time (Ts)** 指定的 ILC 采样时间。

#### 依赖关系

要启用此参数，请将 **ILC Algorithm** 设置为 **Model based ILC**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ModelTimeDomain` |
| **值：** | `"Continuous time"`（默认）| `"Discrete time (Ts)"` |

**示例：** `set_param(gcb,"ModelTimeDomain","Discrete time (Ts)")`

### **A**、**B**、**C** — 状态空间模型矩阵 `1`（默认）| 矩阵

指定用于基于模型 ILC 算法的标称或近似状态空间模型的矩阵。该模块要求您按以下形式指定被控对象动态：

x(t+1)=Ax(t)+Bu(t)y(t)=Cx(t)。

#### 依赖关系

要启用这些参数，请将 **ILC Algorithm** 设置为 **Model based ILC**。

### **ILC methods** — 基于模型的 ILC 方法 **Gradient based**（默认）| **Inverse-model based**

基于模型的 ILC 方法，指定为 **Gradient based** 或 **Inverse-model based**。

#### 依赖关系

要启用此参数，请将 **ILC Algorithm** 设置为 **Model based ILC**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ModelBasedILCType` |
| **值：** | `"Gradient based"`（默认）| `"Inverse-model based"` |

**示例：** `set_param(gcb,"ModelBasedILCType","Inverse-model based")`

### **ILC Gain (gamma\_gradient)** — 基于梯度的 ILC 增益 `1`（默认）| 正标量

基于梯度的 ILC 增益，指定为正标量。

#### 依赖关系

要启用此参数，请将 **ILC Algorithm** 设置为 **Model based ILC**，并将 **ILC methods** 设置为 **Gradient based**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `gamma_grad` |
| **值：** | `"1"`（默认）| 带引号的正标量 |

**示例：** `set_param(gcb,"gamma_grad","2")`

### **ILC Gain (gamma\_inverse)** — 基于逆模型的 ILC 增益 `1`（默认）

基于逆模型的 ILC 增益，指定为小于 2 的正标量。

#### 依赖关系

要启用此参数，请将 **ILC Algorithm** 设置为 **Model based ILC**，并将 **ILC methods** 设置为 **Inverse-model based**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `gamma_inverse` |
| **值：** | `"1"`（默认）| 带引号的小于 2 的正标量 |

**示例：** `set_param(gcb,"gamma_inverse","1.5")`

### **Enable first-order low-pass filter** — 启用一阶低通滤波器 `off`（默认）| `on`

选择此参数以将一阶低通滤波器应用于 ILC 更新律。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `LPFEnable` |
| **值：** | `"off"`（默认）| `"on"` |

**示例：** `set_param(gcb,"LPFEnable","on")`

### **滤波器时间常数 (tau)** — 滤波器时间常数 `1`（默认）| 正标量

一阶低通滤波器的时间常数，指定为正标量。

#### 依赖关系

要启用此参数，请选择 **Enable first-order low-pass filter**。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tau` |
| **值：** | `"1"`（默认）| 带引号的正标量 |

**示例：** `set_param(gcb,"tau","10")`
## 所属库

Simulink Control Design / Adaptive Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

为重复性控制任务设计迭代学习控制器

迭代学习控制（ILC）是逐批次控制的一种改进。该方法利用前一批次运行的误差轨迹形式的频繁测量来更新后续批次运行的控制信号。ILC 提高了在相同初始运行条件下执行重复操作的系统的性能。您可以在制造业、机器人技术和化学加工等许多实际工业系统中使用 ILC，这些领域中流水线的大规模生产需要重复操作。

迭代学习控制模块提供以下配置：

- 无模型 ILC — 该方法不需要系统动力学的先验知识，使用比例-微分（PD）误差反馈来更新控制历史。无模型 ILC 更新律为：

  uk+1(t)=Q(q)(uk(t)+γpek(t+1)+γd(ek(t+1)−ek(t)))。

  其中，*γp* 是比例增益，*γd* 是微分增益，*Q*(*q*) 是一阶低通滤波器。根据 PD 增益的选择，您可以选择实现 P 型、D 型或 PD 型 ILC。该方法仅适用于 SISO 系统。
- 基于模型的 ILC — 该方法是 ILC 的一种更一般的形式，适用于以下形式的连续时间和离散时间 LTI 状态空间系统：

  xk(t+1)=Axk(t)+Buk(t),x(0)=x0,yk(t)=Cxk(t)。

  此外，该方法允许您使用以下两种更新方法之一：

  - 基于梯度的 ILC — uk+1(t)=Q(q)(uk(t)+γGTek(t))
  - 基于逆模型的 ILC — uk+1(t)=Q(q)(uk(t)+γG−1ek(t))

有关 ILC 的更多信息，请参阅 Iterative Learning Control。
