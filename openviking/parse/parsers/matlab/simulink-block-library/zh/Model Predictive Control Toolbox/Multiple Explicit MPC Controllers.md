---
type: simulink-block
title: 'Multiple Explicit MPC Controllers'
family: 'model-predictive-control-toolbox'
product_id: 'mpc'
product_name: 'Model Predictive Control Toolbox'
documentation_release: R2025b
official_category: 'Model Predictive Control Toolbox'
documentation_page: 'multipleexplicitmpccontrollers'
documentation_source_path: 'ref/multipleexplicitmpccontrollers.html'
language: zh-CN
chinese_source: worker-translation
---

# Multiple Explicit MPC Controllers

## 端口

### 输入

#### 必需输入

### **switch** — 控制器选择整数

使用 **switch** 输入端口选择活动控制器。**switch** 输入信号必须是从 `1` 到 *N*c 的标量整数，其中 *N*c 是指定的候选控制器数量。在每个控制时刻，此信号指定活动控制器。switch 值为 `1` 对应候选控制器元胞数组中的第一个条目，值为 `2` 对应第二个控制器，依此类推。

如果 `switch` 信号超出 1 到 *N*c 的范围，模块将保持先前的控制器输出。

### **mo** — 测量输出向量

测量输出信号，指定为向量信号。候选控制器使用测量的被控对象输出改进其状态估计。

所有候选控制器都必须使用相同的状态估计选项，即默认或自定义。
如果候选控制器使用默认状态估计，则必须将测量的被控对象输出连接到 **mo** 输入端口。如果候选控制器使用自定义状态估计，则必须将估计的被控对象状态信号连接到 **x[k|k]** 输入端口。

#### 依赖关系

要启用此端口，请清除 **使用自定义状态估计而非使用内置 Kalman 滤波器** 参数。

### **x[k|k]** — 自定义状态估计向量

自定义状态估计，指定为向量信号。候选控制器使用连接的状态估计，而不是使用内置估计器估计状态。当替代估计技术被认为优于内置估计器，或状态完全可测量时，请使用自定义状态估计。

所有候选控制器都必须使用相同的状态估计选项，即默认或自定义。如果候选控制器使用自定义状态估计，则必须将当前状态估计连接到 **x[k|k]** 输入端口。如果候选控制器使用默认状态估计，则必须将测量输出连接到 **mo** 输入端口。

使用自定义状态估计时，所有候选控制器必须具有相同的维度。所有候选控制器必须为其各自的被控对象、扰动和测量噪声模型使用相同的状态定义（状态的数量和顺序）。

#### 依赖关系

要启用此端口，请选择 **使用自定义状态估计而非使用内置 Kalman 滤波器** 参数。

### **ref** — 模型参考输出向量

在每个控制时刻，`ref` 信号必须包含 *ny* 个输出变量的当前参考值（目标或设定点），其中 *ny* 是输出总数，包括测量输出和未测量输出。由于此模块不支持参考预览，`ref` 必须是向量信号。

#### 附加输入

### **md** — 测量扰动向量

如果控制器预测模型具有测量扰动，则必须启用此端口，并将包含 *Nmd* 个元素的行向量信号连接到该端口，其中 *Nmd* 是测量扰动的数量。

由于此模块不支持测量扰动预览，`md` 必须是向量信号。

#### 依赖关系

要启用此端口，请选择 **测量扰动** 参数。

### **ext.mv** — 上一控制区间在被控对象中使用的控制信号向量

上一控制区间在被控对象中使用的控制信号，指定为长度为 *Nmv* 的向量信号，其中 *Nmv* 是操纵变量的数量。所有候选控制器在每个控制区间使用此信号更新其控制器状态估计。这有助于在驱动控制器切换时最小化无扰切换。当被控对象中使用的操纵变量 (MV) 向量与模块计算的 MV 向量不同时（例如由于信号饱和或超控条件），使用此输入还可提高状态估计精度。

控制器状态估计假设 MV 向量是分段常数。因此，在时间 *tk*，**ext.mv** 值必须是时间 *tk–1* 和 *tk* 之间的有效 MV 向量。例如，如果 MV 在此区间内实际变化，您可以提供在时间 *tk* 求值的时间平均值。

**注意**

- 将 **ext.mv** 连接到上一控制区间实际施加到被控对象的 MV 信号。通常，这些 MV 信号是驱动控制器模块生成的值，但并非总是如此。如果控制器模块未驱动被控对象，则将实际控制信号馈送到 **ext.mv** 还可以在控制器重新上线时帮助实现无扰切换。
- 当控制器驱动被控对象时使用此选项可能会在 Simulink® 模型中导致代数环，因为存在从 **ext.mv** 输入到 **mv** 输出端口的直接馈通。要防止此类代数环，请插入 Memory 模块或 Unit Delay 模块。

有关使用外部操纵变量输入端口实现无扰切换的示例，请参阅 Switch Controller Online and Offline with Bumpless Transfer。

#### 依赖关系

要启用此端口，请选择 **外部操纵变量** 参数。

### 输出

#### 必需输出

### **mv** — 最优操纵变量控制作用列向量

最优操纵变量控制作用，返回为长度为 *Nmv* 的列向量信号，其中 *Nmv* 是操纵变量的数量。

Multiple Explicit MPC Controllers 模块将活动控制器的输出传递到 **mv** 输出。因此，活动控制器在每个控制时刻使用其 explicit MPC 控制器对象中包含的控制律更新 **mv** 输出。如果控制律求值失败，此信号保持不变；也就是说，它保持在先前的成功结果。

#### 附加输出

### **status** — 分段仿射函数求值状态 `1` | `0` | `-1`

此输出指示最新的 explicit MPC 控制律求值是否成功。该输出端口提供具有以下值之一的标量信号：

- 1 — explicit 控制律求值成功
- 0 — 由于一个或多个控制律参数超出范围而失败
- –1 — 控制律参数在有效范围内，但需要进行外推

如果 **status** 为 0 或 –1，则 **mv** 输出端口保持在最后一个已知良好值。

#### 依赖关系

要启用此端口，请选择 **分段仿射函数求值状态** 参数。

### **region** — 求值分段仿射函数的区域编号 非负整数

此输出提供最新 explicit 控制律求值中使用的多面体区域的索引。如果控制律求值失败，此输出端口上的信号为零。

#### 依赖关系

要启用此端口，请选择 **求值分段仿射函数的区域编号** 参数。

### **est.state** — 估计的控制器状态向量

每个控制时刻的估计控制器状态，返回为向量信号。估计状态包括被控对象、扰动和噪声模型状态。如果使用自定义状态估计，此输出信号的值与 **x[k|k]** 输入信号相同。

#### 依赖关系

要启用此端口，请选择 **估计的控制器状态** 参数。

## 参数

### **Explicit MPC 控制器元胞数组** — 候选控制器 `explicitMPC` 对象元胞数组 | cell array of strings | cell array of character vectors

候选控制器，指定为以下之一：

- `explicitMPC` 对象的元胞数组
- string 元胞数组或 character vector 元胞数组，其中每个元素是 MATLAB® 工作区中 `explicitMPC` 对象的名称

指定的数组必须至少包含两个候选控制器。元胞数组中的第一个条目是对应于 switch 输入值 1 的控制器，第二个对应于 switch 输入值 2，依此类推。

#### 编程使用

|  |
| --- |
| **模块参数：** `empcobjs` |
| **类型：** string, character vector, cell array of strings, cell array of character vectors |
| **默认值：** `""` |

### **初始控制器状态元胞数组** — 初始状态 `mpcstate` 对象元胞数组 | cell array of strings | cell array of character vectors

候选控制器的初始状态，指定为以下之一：

- `mpcstate` 对象的元胞数组。
- string 元胞数组或 character vector 元胞数组，其中每个元素是 MATLAB 工作区中 `mpcstate` 对象的名称。
- `{[],[],...}`、`{'[]','[]',...}` 或 `{"[]","[]",...}` — 使用各候选控制器的 `Model.Nominal` 属性中定义的标称条件作为其初始状态。

如果将此参数留空，模块使用 `explicitMPC` 对象的 `Model.Nominal` 属性中定义的标称值。您可以使用此参数使控制器状态尽可能反映仿真开始时真实被控对象环境。

如果启用了自定义状态估计，模块将忽略 **初始控制器状态元胞数组** 参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `x0s` |
| **类型：** string, character vector, cell array of strings, cell array of character vectors |
| **默认值：** `""` |

#### 常规选项卡

### **测量扰动** — 添加测量扰动输入端口 `on` (默认) | `off`

如果控制器具有测量扰动，则必须选择此参数以将 **md** 输出端口添加到此模块。

#### 编程使用

|  |
| --- |
| **模块参数：** `md_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"on"` |

### **外部操纵变量** — 添加外部操纵变量输入端口 `off` (默认) | `on`

选择此参数以将 **ext.mv** 输入端口添加到此模块。

#### 编程使用

|  |
| --- |
| **模块参数：** `mv_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **分段仿射函数求值状态** — 添加求值状态输出端口 off (默认) | on

选择此参数以将 **status** 输出端口添加到此模块。

#### 编程使用

|  |
| --- |
| **模块参数：** `return_status_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **求值分段仿射函数的区域编号** — 添加区域编号输出端口 off (默认) | on

选择此参数以将 **region** 输出端口添加到此模块。

#### 编程使用

|  |
| --- |
| **模块参数：** `return_region_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **估计的控制器状态** — 添加估计状态输出端口 `off` (默认) | `on`

选择此参数以将 **est.state** 输出端口添加到此模块。

#### 编程使用

|  |
| --- |
| **模块参数：** `return_state_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **使用自定义状态估计而非使用内置 Kalman 滤波器** — 使用自定义状态估计输入端口 `off` (默认) | `on`

选择此参数以移除 **mo** 输入端口并添加 **x[k|k]** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数：** `state_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

#### 其他选项卡

### **模块数据类型** — 指定操纵变量的数据类型 `double` (默认) | `single` | `data type expression`

将操纵变量的模块数据类型指定为以下之一：

- `double` — 双精度浮点
- `single` — 单精度浮点

  如果要在 single 精度目标上实现此模块，请将输出数据类型指定为 `single`。
- `data type expression` — 求值为 `double` 或 `single` 的表达式。有关详细信息，请参阅 Control Data Types of Signals (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数：** `BlockDataType_multiple` |
| **类型：** string, character vector |
| **值：** `"double"`, `"single"`, `data type expression` |
| **默认值：** `"double"` |

### **继承采样时间** — 从父子系统继承模块采样时间 `off` (默认) | `on`

选择此参数以将父子系统的采样时间继承为模块采样时间。这样做允许您在 Function-Call Subsystem (Simulink) 或 Triggered Subsystem (Simulink) 模块内有条件地执行此模块。有关示例，请参阅 Using MPC Controller Block Inside Function-Call and Triggered Subsystems。

**注意**

必须在控制器的采样率下执行 Function-Call Subsystem 或 Triggered Subsystem 模块。否则，可能由于以下两个原因看到意外结果。

- MV 速率向量的第一个元素（即操纵变量当前值与上一个值之间的差）通常被加权和约束，假设上一个 MV 值发生在过去，且处于 MPC 对象中指定的采样时间；当模块以不同的采样率执行时，此假设不再成立。
- 内置 Kalman 估计器使用 MPC 对象中指定的采样时间向 MPC 优化问题提供当前状态的估计，因此当模块以不同的采样率执行时，估计状态不再正确。

如果清除此参数（默认），模块的采样时间将从控制器对象继承。

要查看模块的采样时间，请在 Simulink 模型窗口中，在 **Debug** 选项卡上的 **Information Overlays** 下，选择 **colors** 或 **Text**。有关详细信息，请参阅 View Sample Time Information (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数：** `SampleTimeInherited_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

## 所属库

Model Predictive Control Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

多个显式 MPC 控制器

Multiple Explicit MPC Controllers 模块使用以下输入信号：

- 被控对象测量输出 (`mo`)
- 参考或设定点 (`ref`)
- 被控对象测量扰动 (`md`)，如果有
- 切换信号 (`switch`)

Multiple Explicit MPC Controllers 模块使您能够基于当前工况在多个显式 MPC 控制器之间实时切换。通常，您针对操作空间的特定区域设计每个控制器。使用可用的测量值，您检测当前操作区域，并使用 `switch` 输入端口选择合适的活动控制器。

切换信号在包含两个或多个候选显式 MPC 控制器的列表中选择 *活动控制器*。这些控制器通过在每个控制区间使用查表控制律，而不是求解二次规划问题，来减少在线计算量。有关详细信息，请参见 Explicit MPC Controller。

为了提高效率，非活动控制器不计算其控制律。但是，为了在控制器之间提供无扰切换，非活动控制器继续执行状态估计。

与 Multiple MPC Controllers 模块一样，对于 Multiple Explicit MPC Controllers 模块，您不能禁用计算。必须始终有一个控制器处于活动状态。

与 Explicit MPC Controller 模块一样，Multiple Explicit MPC Controllers 模块仅支持可选 MPC 功能的一个子集，如下表所示。

| 支持的功能 | 不支持的功能 |
| --- | --- |
| - 内置（Kalman filter）和自定义状态估计 - 状态估计结果的输出端口 - 外部操纵变量反馈信号输入端口 - Single-precision 模块数据（默认为 double precision） - 继承采样时间 | - 在线整定（惩罚权重调整） - 在线约束调整 - 在线操纵变量目标调整 - 参考和/或测量扰动预览 |
