---
type: simulink-block
title: 'Fuzzy PID Controller'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'fuzzypidcontroller'
documentation_source_path: 'fuzzypidcontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# Fuzzy PID Controller

## 端口
```yaml
ports:
- name: r
  summary: 参考标量
  direction: input
- name: y
  summary: 被控对象输出标量
  direction: input
- name: u
  summary: 控制器输出标量
  direction: output
- name: e
  summary: 误差标量
  direction: output
```

### 输入

### **r** — 参考标量

要跟踪的参考信号。

### **y** — 被控对象输出标量

受控系统的输出。
### 输出

### **u** — 控制器输出标量

控制器输出，基于 PI、PD 和前馈控制器路径之和。

### **e** — 误差标量

参考信号 **r** 与被控对象输出 **y** 之间的差值。使用此输出进行跟踪误差指标计算，例如绝对误差积分（IAE）。

#### 依赖关系

- 要启用此端口，请选择 **Add error (e) output** 参数。
## 参数
```yaml
parameters:
- name: Time Domain
  summary: 控制器时域 Discrete-time（默认）| Continuous-time
  group: 控制器选项
  block_parameter: TimeDomainType
  values: '"Discrete-time" (default) | "Continuous-time"'
- name: Ce
  summary: 误差增益 1（默认）| 标量
  group: 控制器选项
  block_parameter: CE
  values: '"1" (default) | nonnegative scalar in quotes'
- name: Cd
  summary: 微分信号增益 1（默认）| 标量
  group: 控制器选项
  block_parameter: CD
  values: '"1" | nonnegative scalar in quotes'
- name: C0
  summary: FIS 输出变化增益 1（默认）| 标量
  group: 控制器选项
  block_parameter: C0
  values: '"1" | nonnegative scalar in quotes'
- name: C1
  summary: FIS 输出增益 1（默认）| 标量
  group: 控制器选项
  block_parameter: C1
  values: '"1" | nonnegative scalar in quotes'
- name: Integrator method
  summary: 离散时间控制器中用于计算积分的方法 Forward Euler（默认）| Backward Euler | Trapezoidal
  group: 控制器选项
  block_parameter: IntegratorMethod
  values: '"Forward Euler"（默认）| "Backward Euler" | "Trapezoidal"'
- name: Use accumulator
  summary: 在积分器中累积信号 off（默认）| on
  group: 控制器选项
  block_parameter: UseAccumulator
  values: '"off"（默认）| "on"'
- name: Derivative signal
  summary: 用于计算导数的信号 Error (e)（默认）| Process output (y)
  group: 控制器选项
  block_parameter: DerivativeSignal
  values: '"Error (e)"（默认）| "Process output (y)"'
- name: Use filtered derivative
  summary: 对导数项应用滤波器 on（默认）| off
  group: 控制器选项
  block_parameter: UseFilter
  values: '"on"（默认）| "off"'
- name: 滤波器系数
  summary: 微分滤波器系数 100（默认）| 正标量
  group: 控制器选项
  block_parameter: N
  values: '"100"（默认）| 带引号的正标量'
- name: 滤波方法
  summary: 离散时间控制器中计算微分的方法 Forward Euler（默认）| Backward Euler | Trapezoidal
  group: 控制器选项
  block_parameter: DerivativeFilterMethod
  values: '"Forward Euler"（默认）| "Backward Euler" | "Trapezoidal"'
- name: 添加误差 (e) 输出
  summary: 启用 e 输出端口 off（默认）| on
  group: 控制器选项
  block_parameter: E
  values: '"off"（默认）| "on"'
- name: 采样时间（–1 表示继承）
  summary: 采样时间 -1（默认）| 正标量
  group: 控制器选项
  block_parameter: SampleTime
  values: '"-1"（默认）| 带引号的正标量'
- name: FIS name
  summary: 模糊推理系统 mamfis 对象 | sugfis 对象 | mamfistype2 对象 | sugfistype2 对象 | 带引号的 FIS 文件名 | 带引号的 MAT 文件名
  group: 模糊推理系统
  block_parameter: FIS
  values: '''"fuzzycontroller"''（默认） | 带引号的变量名 | 带引号的文件名'
- name: Number of samples for output discretization
  summary: 输出模糊集中的点数 101（默认） | 大于 1 的整数
  group: 模糊推理系统
  block_parameter: OutputSampleNumber
  values: '"101"（默认） | 带引号的、大于 1 的整数'
- name: Implement FIS as lookup table
  summary: 将 FIS 转换为查找表 off（默认） | on
  group: 模糊推理系统
  block_parameter: UseLookupTable
  values: '"off"（默认） | "on"'
- name: Number of input breakpoints (samples)
  summary: 查找表断点数量 10（默认） | 正整数
  group: 模糊推理系统
  block_parameter: NumBreakpoints
  values: '"10"（默认） | 带引号的正整数'
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### 控制器选项

### **Time Domain** — 控制器时域 **Discrete-time**（默认）| **Continuous-time**

指定离散时间或连续时间控制器。

当您选择 **Discrete-time** 时，建议使用 **Sample time** 参数为该模块指定显式采样时间。选择 **Discrete-time** 还会启用 **Integrator method** 和 **Filter method** 参数。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `TimeDomainType` |
| **值**：| `"Discrete-time"` (default) | `"Continuous-time"` |

### **Ce** — 误差增益 `1`（默认）| 标量

指定一个增益因子，用于将误差信号缩放到 FIS 对应输入变量的范围。

有关选择初始控制器增益的更多信息，请参阅 Derive Controller Gains from Conventional PID Gains。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `CE` |
| **值**：| `"1"` (default) | nonnegative scalar in quotes |

### **Cd** — 微分信号增益 `1`（默认）| 标量

指定在微分信号进入 FIS 之前施加的增益因子。

当 **Derivative signal** 为 `Process output (y)` 时，此增益因子也应用于参考前馈路径。

有关选择初始控制器增益的更多信息，请参阅 Derive Controller Gains from Conventional PID Gains。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `CD` |
| **值**：| `"1"` | nonnegative scalar in quotes |

### **C0** — FIS 输出变化增益 `1`（默认）| 标量

指定在 PI 控制分支中施加于 FIS 输出的增益因子。

当 **Derivative signal** 为 `Process output (y)` 时，此增益因子也应用于参考前馈路径。

要设计 PD 控制器，请将 **C0** 设置为零。

有关选择初始控制器增益的更多信息，请参阅 Derive Controller Gains from Conventional PID Gains。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `C0` |
| **值**：| `"1"` | nonnegative scalar in quotes |

### **C1** — FIS 输出增益 `1`（默认）| 标量

指定在 PD 控制路径中施加于 FIS 输出的增益因子。

要设计 PI 控制器，请将 **C1** 设置为零。

有关选择初始控制器增益的更多信息，请参阅 Derive Controller Gains from Conventional PID Gains。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `C1` |
| **值**：| `"1"` | nonnegative scalar in quotes |

### **Integrator method** — 离散时间控制器中用于计算积分的方法 `Forward Euler`（默认）| `Backward Euler` | `Trapezoidal`

在离散时间中，控制器传递函数的积分项为
*Iα*(*z*)，其中
*α*(*z*) 取决于你通过此参数指定的积分器方法。

你可以指定以下积分方法之一：

- `Forward Euler` — 前向矩形
  （左手）
- `Backward Euler` — 后向矩形（右手）
  近似
- `Trapezoidal` — 双线性近似

有关滤波导数的详细信息，请参阅 PID Controller
模块的 **Integrator method (Simulink)** 参数。

#### 依赖关系

- 要启用此参数，请将 **Time Domain** 参数
  设置为 **Discrete-time**。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `IntegratorMethod` |
| **值：** | `"Forward Euler"`（默认）| `"Backward Euler"` | `"Trapezoidal"` |

### **Use accumulator** — 在积分器中累积信号 `off`（默认）| `on`

选择此参数以在积分阶段累积信号。

当你清除 **Use accumulator** 时，控制器的积分采样时间为模块采样时间，如 **Sample
time** 参数中所指定。

当你选择 **Use accumulator** 时，控制器的积分采样时间为 1。在这种情况下，模块采样时间决定何时计算积分输出，但不影响积分输出值。

当你使用累加器时，将 **C0** 乘以
**Sample time**。

#### 依赖关系

- 要启用此参数，请将 **Time Domain** 参数
  设置为 **Discrete-time**。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `UseAccumulator` |
| **值：** | `"off"`（默认）| `"on"` |

### **Derivative signal** — 用于计算导数的信号 `Error (e)`（默认）| `Process output (y)`

从以下信号之一计算导数：

- `Error (e)` — 使用误差信号，即被控对象输出与参考信号之间的差值，如下图所示。

  使用误差信号计算导数的模糊 PID 控制器结构。
- `Process output (y)` — 直接使用被控对象输出，
  如下图所示。当你选择此选项时，控制器包含一条从参考信号到控制器
  输出的前馈路径。

  使用被控对象输出计算导数的模糊 PID 控制器结构。控制器现在包含一条前馈路径，其中包含 Cd 和 C0 控制器增益。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `DerivativeSignal` |
| **值：** | `"Error (e)"`（默认）| `"Process output (y)"` |

### **Use filtered derivative** — 对导数项应用滤波器 `on`（默认）| `off`

对于离散时间控制器，清除此选项以将滤波导数替换为未滤波的离散时间微分器，其极点位置
取决于 **Filter method** 参数。

对于连续时间控制器，导数项始终经过滤波。

有关滤波导数的详细信息，请参阅 PID Controller
模块的 **Use filtered derivative (Simulink)** 参数。

#### 依赖关系

要启用此参数，请将 **Time domain** 设置为
**Discrete-time**。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `UseFilter` |
| **值：** | `"on"`（默认）| `"off"` |

### **滤波器系数** — 微分滤波器系数 `100`（默认）| 正标量

为滤波器系数指定一个有限实增益值。滤波器系数决定模块微分作用中滤波器的极点位置。滤波器极点的位置取决于 **Time domain** 参数。

有关滤波器系数及其对极点位置影响的详细信息，请参阅 PID Controller 模块的 **Filter coefficient (N) (Simulink)** 参数。

#### 依赖关系

- 要为离散时间控制器启用此参数，请选择 **Use filtered derivative** 参数。
- 对于连续时间控制器，此参数始终启用。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `N` |
| **值**：| `"100"`（默认）| 带引号的正标量 |

### **滤波方法** — 离散时间控制器中计算微分的方法 `Forward Euler`（默认）| `Backward Euler` | `Trapezoidal`

您可以为控制器的微分项指定以下滤波方法之一：

- `Forward Euler` — 前向矩形（左手）
- `Backward Euler` — 后向矩形（右手）近似
- `Trapezoidal` — 双线性近似

有关这些方法的详细信息，请参阅 PID Controller 模块的 **Filter method (Simulink)** 参数。

#### 依赖关系

- 要启用此参数，请将 **Time Domain** 参数设置为 **Discrete-time**，并选择 **Use filtered derivative** 参数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `DerivativeFilterMethod` |
| **值**：| `"Forward Euler"`（默认）| `"Backward Euler"` | `"Trapezoidal"` |

### **添加误差 (e) 输出** — 启用 `e` 输出端口 `off`（默认）| `on`

启用 **e** 输出端口以访问误差信号。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `E` |
| **值**：| `"off"`（默认）| `"on"` |

### **采样时间（–1 表示继承）** — 采样时间 `-1`（默认）| 正标量

通过输入正标量值（例如 0.1）来指定采样时间。默认离散采样时间 –1 表示模块从上游模块继承其采样时间。但是，建议您显式设置控制器采样时间，尤其是在您预计上游模块的采样时间会发生变化时。控制器系数的效果取决于采样时间。因此，对于给定的一组系数值，更改采样时间会改变控制器的性能。

#### 依赖关系

- 要启用此参数，请将 **Time Domain** 参数设置为 **Discrete-time**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **值**：| `"-1"`（默认）| 带引号的正标量 |

### 模糊推理系统

### **FIS name** — 模糊推理系统 `mamfis` 对象 | `sugfis` 对象 | `mamfistype2` 对象 | `sugfistype2` 对象 | 带引号的 FIS 文件名 | 带引号的 MAT 文件名

模糊推理系统，指定为以下之一：

- `mamfis` 或
  `sugfis`
  对象 — 在 MATLAB® 工作区中指定一个 1 型 FIS 对象的名称。
- `mamfistype2` 或 `sugfistype2` 对象 — 在
  MATLAB 工作区中指定一个 2 型 FIS 对象的名称。
- 当前工作文件夹或
  MATLAB 路径上的 FIS 文件（`*.fis`）名称。文件名中是否包含文件扩展名是可选的。
  文件名需用引号指定。
- 当前工作文件夹或
  MATLAB 路径上的 MAT 文件（`*.mat`）名称。该 MAT 文件必须仅包含一个 FIS 对象。文件名中是否包含
  文件扩展名是可选的。文件名需用
  引号指定。

该 FIS 必须有两个输入变量（误差信号和导数信号）和一个
输出变量。

默认 FIS `fuzzycontroller` 是一个线性 FIS，其配置
允许根据指定的常规
PID 控制器增益更轻松地选择模糊 PID 控制器增益。有关此 FIS 的详细信息，请参阅 Default FIS。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `FIS` |
| **值**：| `'"fuzzycontroller"'`（默认） | 带引号的变量名 | 带引号的文件名 |

### **Number of samples for output discretization** — 输出模糊集中的点数 101（默认） | 大于 `1` 的整数

用于离散化 FIS 输出变量范围的样本数，指定为大于 `1` 的整数。此值对应于每条规则的输出模糊集中的点数。

为了在评估 Mamdani FIS 时减少内存使用量，请指定较少的样本数。这样做会牺牲去模糊化输出值的精度。指定过少的样本数可能会使去模糊化的输出区域为零。在这种情况下，去模糊化输出值为输出变量范围的中点。

**Note**

该模块在评估 Sugeno FIS 时会忽略此参数。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `OutputSampleNumber` |
| **值**：| `"101"`（默认） | 带引号的、大于 `1` 的整数 |

### **Implement FIS as lookup table** — 将 FIS 转换为查找表 `off`（默认） | `on`

为了减少控制器的处理时间，您可以将 FIS 表示为查找表。

该模块会根据断点数量将每个 FIS 输入的范围划分为大小相等的区域，断点数量由 **Number of
input breakpoints** 参数指定。

对于每种输入组合，该模块会计算相应的 FIS 输出。
在评估期间，控制器使用这些预先计算的输出，而不是执行
模糊推理过程。

#### 编程使用

要以编程方式设置模块参数值，
请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `UseLookupTable` |
| **值**：| `"off"`（默认） | `"on"` |

### **Number of input breakpoints (samples)** — 查找表断点数量 `10`（默认） | 正整数

查找表断点数量，指定为正整数。增加
断点数量会提高查找表的精度，同时增加
其内存需求。

#### 依赖关系

- 要启用此参数，请选择 **Implement FIS as lookup
  table** 参数。

#### 编程使用

要以编程方式设置模块参数值，
请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `NumBreakpoints` |
| **值**：| `"10"`（默认） | 带引号的正整数 |
## 所属库

Fuzzy Logic Toolbox

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 连续时间控制器：

  - 不建议用于生产代码。
- 离散时间控制器：

  - 当置于触发子系统层级内时，依赖于绝对时间。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

## 版本历史

**在 R2024b 中引入**

## 描述

基于模糊逻辑的 PID 控制器

Fuzzy PID Controller 模块使用单个 Fuzzy Logic Controller 模块和并行结构实现 PID 控制器。控制架构如下图所示。

模糊 PID 控制器结构

对于此控制器：

- 模块的输入是参考信号 (*r*) 和被控对象输出 (*y*)。
- FIS 的输入是误差 (*E*) 和误差变化 (*ΔE*)。
- 误差信号由增益因子 *Ce* 缩放。
- 误差变化由增益因子 *Cd* 缩放。
- FIS 具有单个输出，该输出分为 PI 控制分支和 PD 控制分支。
- PI 控制分支包含增益 *C0* 和一个积分器。
- PD 控制分支包含增益 *C1*。
- 模块输出的控制信号是 PI 和 PD 分支之和。

有关此控制器结构的更多信息，请参阅 [1]。
