---
type: simulink-block
title: 'Fuzzy PID Controller'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Fuzzy Logic in Simulink'
documentation_page: 'fuzzypidcontroller'
documentation_source_path: 'fuzzypidcontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# Fuzzy PID Controller

## 端口

### 输入

### **r** — 参考标量

要跟踪的参考信号。

### **y** — 被控对象输出标量

受控系统的输出。
### 输出

### **u** — 控制器输出标量

控制器输出，基于 PI、PD 和前馈控制器路径之和。

### **e** — 误差标量

参考信号 **r** 与被控对象输出 **y** 之间的差值。使用此输出进行跟踪误差指标计算，例如绝对误差积分 (IAE)。

#### 依赖项

- 要启用此端口，请选择 **Add error (e) output** 参数。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### 控制器选项

### **Time Domain** — 控制器时域 **Discrete-time**（默认） | **Continuous-time**

指定离散时间或连续时间控制器。

当您选择 **Discrete-time** 时，建议使用 **Sample time** 参数为模块指定显式采样时间。选择 **Discrete-time** 还会启用 **Integrator method** 和 **Filter method** 参数。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `TimeDomainType` |
| **值：** | `"Discrete-time"`（默认） | `"Continuous-time"` |

### **Ce** — 误差增益 `1`（默认） | 标量

指定一个增益因子，将误差信号缩放至 FIS 对应输入变量的范围。

有关选择初始控制器增益的详细信息，请参阅从常规 PID 增益推导控制器增益。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `CE` |
| **值：** | `"1"`（默认） | 带引号的非负标量 |

### **Cd** — 导数信号增益 `1`（默认） | 标量

指定在导数信号进入 FIS 之前施加于该信号的增益因子。

当 **Derivative signal** 为 `Process output (y)` 时，此增益因子也会应用于参考前馈路径。

有关选择初始控制器增益的详细信息，请参阅从常规 PID 增益推导控制器增益。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `CD` |
| **值：** | `"1"` | 带引号的非负标量 |

### **C0** — FIS 输出变化量增益 `1`（默认） | 标量

指定在 PI 控制分支中施加于 FIS 输出的增益因子。

当 **Derivative signal** 为 `Process output (y)` 时，此增益因子也会应用于参考前馈路径。

要设计 PD 控制器，请将 **C0** 设置为零。

有关选择初始控制器增益的详细信息，请参阅从常规 PID 增益推导控制器增益。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `C0` |
| **值：** | `"1"` | 带引号的非负标量 |

### **C1** — FIS 输出增益 `1`（默认） | 标量

指定在 PD 控制路径中施加于 FIS 输出的增益因子。

要设计 PI 控制器，请将 **C1** 设置为零。

有关选择初始控制器增益的详细信息，请参阅从常规 PID 增益推导控制器增益。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `C1` |
| **值：** | `"1"` | 带引号的非负标量 |

### **Integrator method** — 离散时间控制器中计算积分的方法 `Forward Euler`（默认） | `Backward Euler` | `Trapezoidal`

在离散时间中，控制器传递函数的积分项为 *Iα*(*z*)，其中 *α*(*z*) 取决于您用此参数指定的积分器方法。

您可以指定以下积分方法之一：

- `Forward Euler` — 前向矩形（左手）
- `Backward Euler` — 后向矩形（右手）近似
- `Trapezoidal` — 双线性近似

有关滤波导数的详细信息，请参阅 PID Controller 模块的 **Integrator method (Simulink)** 参数。

#### 依赖项

- 要启用此参数，请将 **Time Domain** 参数设置为 **Discrete-time**。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `IntegratorMethod` |
| **值：** | `"Forward Euler"`（默认） | `"Backward Euler"` | `"Trapezoidal"` |

### **Use accumulator** — 在积分器中累加信号 `off`（默认） | `on`

选择此参数可在积分阶段累加信号。

当您清除 **Use accumulator** 时，控制器的积分采样时间为模块采样时间，如 **Sample time** 参数中所指定。

当您选择 **Use accumulator** 时，控制器的积分采样时间为 1。在这种情况下，模块采样时间决定何时计算积分输出，但不影响积分输出值。

使用累加器时，请将 **C0** 乘以 **Sample time**。

#### 依赖项

- 要启用此参数，请将 **Time Domain** 参数设置为 **Discrete-time**。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `UseAccumulator` |
| **值：** | `"off"`（默认） | `"on"` |

### **Derivative signal** — 用于计算导数的信号 `Error (e)`（默认） | `Process output (y)`

根据以下信号之一计算导数：

- `Error (e)` — 使用误差信号，即被控对象输出与参考信号之间的差值，如下图所示。

  使用误差信号计算导数的 Fuzzy PID controller 结构。
- `Process output (y)` — 直接使用被控对象输出，如下图所示。当您选择此选项时，控制器包含一条从参考信号到控制器输出的前馈路径。

  使用被控对象输出计算导数的 Fuzzy PID controller 结构。控制器现在包含一条前馈路径，其中含有 Cd 和 C0 控制器增益。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `DerivativeSignal` |
| **值：** | `"Error (e)"`（默认） | `"Process output (y)"` |

### **Use filtered derivative** — 对导数项应用滤波器 `on`（默认） | `off`

对于离散时间控制器，请清除此选项，以用未滤波的离散时间微分器替换滤波导数，其极点位置取决于 **Filter method** 参数。

对于连续时间控制器，导数项始终经过滤波。

有关滤波导数的详细信息，请参阅 PID Controller 模块的 **Use filtered derivative (Simulink)** 参数。

#### 依赖项

要启用此参数，请将 **Time domain** 设置为 **Discrete-time**。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `UseFilter` |
| **值：** | `"on"`（默认） | `"off"` |

### **Filter coefficient** — 导数滤波器系数 `100`（默认） | 正标量

指定滤波系数的有限实增益值。滤波系数决定模块导数作用中滤波器的极点位置。滤波器极点的位置取决于 **Time domain** 参数。

有关滤波系数及其对极点位置影响的详细信息，请参阅 PID Controller 模块的 **Filter coefficient (N) (Simulink)** 参数。

#### 依赖项

- 对于离散时间控制器，要启用此参数，请选择 **Use filtered derivative** 参数。
- 对于连续时间控制器，此参数始终启用。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `N` |
| **值：** | `"100"`（默认） | 带引号的正标量 |

### **Filter method** — 离散时间控制器中计算导数的方法 `Forward Euler`（默认） | `Backward Euler` | `Trapezoidal`

您可以为控制器导数项指定以下滤波方法之一：

- `Forward Euler` — 前向矩形（左手）
- `Backward Euler` — 后向矩形（右手）近似
- `Trapezoidal` — 双线性近似

有关这些方法的详细信息，请参阅 PID Controller 模块的 **Filter method (Simulink)** 参数。

#### 依赖项

- 要启用此参数，请将 **Time Domain** 参数设置为 **Discrete-time**，并选择 **Use filtered derivative** 参数。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `DerivativeFilterMethod` |
| **值：** | `"Forward Euler"`（默认） | `"Backward Euler"` | `"Trapezoidal"` |

### **Add error (e) output** — 启用 `e` 输出端口 `off`（默认） | `on`

启用 **e** 输出端口以访问误差信号。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `E` |
| **值：** | `"off"`（默认） | `"on"` |

### **Sample time (–1 for inherited)** — 采样时间 `-1`（默认） | 正标量

通过输入正标量值（例如 0.1）来指定采样时间。默认离散采样时间 –1 表示模块从上游模块继承其采样时间。但是，建议显式设置控制器采样时间，尤其是在您预期上游模块的采样时间会变化时。控制器系数的效果取决于采样时间。因此，对于给定的一组系数值，更改采样时间会改变控制器的性能。

#### 依赖项

- 要启用此参数，请将 **Time Domain** 参数设置为 **Discrete-time**。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认） | 带引号的正标量 |

### 模糊推理系统

### **FIS name** — 模糊推理系统 `mamfis` 对象 | `sugfis` 对象 | `mamfistype2` 对象 | `sugfistype2` 对象 | 带引号的 FIS 文件名 | 带引号的 MAT 文件名

模糊推理系统，指定为以下之一：

- `mamfis` 或 `sugfis` 对象 — 在 MATLAB® 工作区中指定 type-1 FIS 对象的名称。
- `mamfistype2` 或 `sugfistype2` 对象 — 在 MATLAB 工作区中指定 type-2 FIS 对象的名称。
- 当前工作文件夹或 MATLAB 路径中的 FIS 文件（`*.fis`）的名称。文件名中包含文件扩展名是可选的。用引号指定文件名。
- 当前工作文件夹或 MATLAB 路径中的 MAT 文件（`*.mat`）的名称。MAT 文件必须只包含一个 FIS 对象。文件名中包含文件扩展名是可选的。用引号指定文件名。

FIS 必须有两个输入变量（误差信号和导数信号）和一个输出变量。

默认 FIS `fuzzycontroller` 是一个线性 FIS，其配置为允许根据指定的常规 PID 控制器增益更轻松地选择模糊 PID 控制器增益。有关此 FIS 的详细信息，请参阅默认 FIS。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `FIS` |
| **值：** | `'"fuzzycontroller"'`（默认） | 带引号的变量名 | 带引号的文件名 |

### **Number of samples for output discretization** — 输出模糊集中的点数 101（默认） | 大于 `1` 的整数

用于离散化 FIS 输出变量范围的样本数，指定为大于 `1` 的整数。此值对应于每条规则的输出模糊集中的点数。

为了在评估 Mamdani FIS 时减少内存使用量，请指定较少的样本数。这样做会牺牲去模糊化输出值的准确性。指定过低的样本数可能会使去模糊化的输出面积为 0。在这种情况下，去模糊化输出值为输出变量范围的中点。

**注意**

在评估 Sugeno FIS 时，模块会忽略此参数。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutputSampleNumber` |
| **值：** | `"101"`（默认） | 带引号的、大于 `1` 的整数 |

### **Implement FIS as lookup table** — 将 FIS 转换为查找表 `off`（默认） | `on`

为了减少控制器的处理时间，您可以将 FIS 表示为查找表。

该模块根据断点数量将每个 FIS 输入的输入范围划分为大小相等的区域，断点数量由您使用 **Number of input breakpoints** 参数指定。

对于每种输入组合，模块都会计算相应的 FIS 输出。在评估期间，控制器使用这些预先计算的输出，而不是执行模糊推理过程。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `UseLookupTable` |
| **值：** | `"off"`（默认） | `"on"` |

### **Number of input breakpoints (samples)** — 查找表断点数 `10`（默认） | 正整数

查找表断点数，指定为正整数。增加断点数可提高查找表的准确性，同时增加其内存需求。

#### 依赖项

- 要启用此参数，请选择 **Implement FIS as lookup table** 参数。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `NumBreakpoints` |
| **值：** | `"10"`（默认） | 带引号的正整数 |

## 所属库

Fuzzy Logic Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 连续时间控制器：

  - 不建议用于生产代码。
- 离散时间控制器：

  - 置于触发子系统层级中时取决于绝对时间。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**R2024b 中引入**

## 描述

基于模糊逻辑的 PID 控制器

Fuzzy PID Controller 模块使用单个 Fuzzy Logic Controller 模块和并行结构实现 PID 控制器。控制架构如下图所示。

Fuzzy PID 控制器结构

对于此控制器：

- 模块的输入是参考信号（*r*）和被控对象输出（*y*）。
- FIS 的输入是误差（*E*）和误差变化量（*ΔE*）。
- 误差信号由增益因子（*Ce*）缩放。
- 误差变化量由增益因子（*Cd*）缩放。
- FIS 有一个输出，该输出分为 PI 控制支路和 PD 控制支路。
- PI 控制支路包含增益 *C0* 和一个积分器。
- PD 控制支路包含增益 *C1*。
- 模块输出的控制信号是 PI 和 PD 支路之和。

有关此控制器结构的更多信息，请参见 [1]。
