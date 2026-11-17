---
type: simulink-block
title: 'Explicit MPC Controller'
family: 'mpc'
product_id: 'mpc'
product_name: 'Model Predictive Control Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'explicitmpccontroller'
documentation_source_path: 'ref/explicitmpccontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# Explicit MPC Controller

## 端口

### 输入

#### 必需输入

### **mo** — 测量输出向量

测量输出，指定为向量信号。该模块使用被控对象测量输出来改进其状态估计。如果控制器使用默认状态估计，则必须将被控对象测量输出连接到 **mo** 输入端口。如果控制器使用自定义状态估计，则必须将估计的被控对象状态连接到 **x[k|k]** 输入端口。

#### 依赖关系

要启用此端口，请清除 **Use custom state estimation instead of using the built-in Kalman filter** 参数。

### **x[k|k]** — 自定义状态估计向量

自定义状态估计，指定为向量信号。该模块使用连接的状态估计，而不是使用内置估计器估计状态。如果控制器使用自定义状态估计，则必须将当前状态估计连接到 **x[k|k]** 输入端口。如果控制器使用默认状态估计，则必须将测量输出连接到 **mo** 输入端口。

即使噪声模型状态（如果有）不用于 MPC 优化，自定义状态向量也必须包含控制器的 `mpcstate` 对象中定义的所有状态，包括被控对象、扰动和噪声模型状态。

当替代估计技术被认为优于内置估计器时，或者当状态完全可测时，请使用自定义状态估计。

#### 依赖关系

要启用此端口，请选择 **Use custom state estimation instead of using the built-in Kalman filter** 参数。

### **ref** — 模型参考输出向量

在每个控制时刻，`ref` 信号必须包含 *ny* 个输出变量的当前参考值（目标值或设定点），其中 *ny* 是输出总数，包括测量输出和未测量输出。由于此模块不支持参考预览，`ref` 必须是向量信号。

#### 附加输入

### **md** — 测量扰动向量

如果控制器预测模型具有测量扰动，则必须启用此端口，并将包含 *Nmd* 个元素的行向量信号连接到该端口，其中 *Nmd* 是测量扰动的数量。

由于此模块不支持测量扰动预览，`md` 必须是向量信号。

#### 依赖关系

要启用此端口，请选择 **Measured disturbances** 参数。

### **ext.mv** — 上一控制区间内用于被控对象的控制信号向量

上一控制区间内用于被控对象的控制信号，指定为长度为 *Nmv* 的向量信号，其中 *Nmv* 是操纵变量的数量。在以下情况下，使用此输入端口来提高状态估计精度：

- 您知道您的控制器并不总是控制被控对象。
- 施加到被控对象的实际 MV 信号可能不同于控制器生成的值，例如在控制信号饱和时。

控制器状态估计假设 MV 是分段常数。因此，在时刻 *tk*，**ext.mv** 值必须包含时刻 *tk–1* 和 *tk* 之间的有效 MV。例如，如果 MV 在此区间内实际变化，您可以提供在时刻 *tk* 评估的时间平均值。

**注意**

- 将 **ext.mv** 连接到上一控制区间内实际施加到被控对象的 MV 信号。通常，这些 MV 信号是控制器生成的值，但并非总是如此。例如，如果您的控制器离线并运行在跟踪模式（即控制器输出不驱动被控对象），则将实际控制信号馈送到 **ext.mv** 有助于在控制器重新在线时实现无扰切换。
- 当控制器驱动被控对象时，插入一个 Memory 模块或 Unit Delay 模块，以反馈上一控制区间内施加到被控对象的 MV 信号。这还可以避免从 **ext.mv** 输入端口到 **mv** 输出端口的直接馈通，从而防止 Simulink® 模型中出现代数环。

有关使用外部操纵变量输入端口进行无扰切换的示例，请参阅 Switch Controller Online and Offline with Bumpless Transfer。

#### 依赖关系

要启用此端口，请选择 **External manipulated variable** 参数。

### **switch** — 禁用评估标量

要关闭控制器评估，请将 **switch** 连接到非零信号。

当不需要控制器输出时，禁用控制器评估可减少计算量，例如当系统手动运行或另一个控制器已接管时。但是，控制器会继续以通常方式更新其内部状态估计。因此，只要 **switch** 信号返回零，它就可以随时恢复评估。当控制器评估关闭时，模块将当前 **ext.mv** 信号传递到控制器输出。如果未启用 **ext.mv** 输入端口，则控制器输出保持在禁用评估时的值。

有关使用外部操纵变量输入端口进行无扰切换的示例，请参阅 Switch Controller Online and Offline with Bumpless Transfer。

#### 依赖关系

要启用此端口，请选择 **Use external signal to enable controller evaluation** 参数。
### 输出

#### 必需输出

### **mv** — 最优操纵变量控制作用列向量

最优操纵变量控制作用，返回为长度为 *Nmv* 的列向量信号，其中 *Nmv* 是操纵变量的数量。

控制器在每个控制时刻使用显式 MPC 控制器对象中包含的控制律更新其 **mv** 输出。如果控制律评估不成功，`mv` 保持不变（即保持在上一成功结果），并且 `status` 输出（如果存在）变为 0 或 –1。

#### 附加输出

### **status** — 分段仿射函数评估状态 `1` | `0` | `-1`

此输出指示最新的显式 MPC 控制律评估是否成功。该输出端口提供一个标量信号，其值为以下之一：

- 1 — 显式控制律评估成功
- 0 — 由于一个或多个控制律参数超出范围而失败
- –1 — 控制律参数在有效范围内，但需要进行外推

如果 **status** 为 0 或 –1，则 **mv** 输出端口保持最后已知的良好值。

#### 依赖关系

要启用此端口，请选择 **Status of piecewise affine function evaluation** 参数。

### **region** — 已评估分段仿射函数的区域编号 非负整数

此输出提供最新显式控制律评估中使用的多面体区域的索引。如果控制律评估失败，此输出端口上的信号为零。

#### 依赖关系

要启用此端口，请选择 **Region number of evaluated piecewise affine function** 参数。

### **est.state** — 估计的控制器状态 向量

每个控制时刻的估计控制器状态，以向量信号形式返回。估计状态包括被控对象、扰动和噪声模型状态。如果使用自定义状态估计，此输出信号与 **x[k|k]** 输入信号具有相同的值。

#### 依赖关系

要启用此端口，请选择 **Estimated controller states** 参数。

## 参数

### **Explicit MPC Controller** — 显式控制器对象 `explicitMPC` 对象名称

包含要使用的控制律的 `explicitMPC` 对象。它必须存在于 MATLAB® 工作区中。使用 `generateExplicitMPC` 命令创建此对象。

#### 编程使用

|  |
| --- |
| **模块参数**：`empcobj` |
| **类型**：string, character vector |
| **默认值**：`""` |

### **Initial Controller State** — 初始状态 `mpcstate` 对象名称

一个可选的 `mpcstate` 对象，用于指定初始控制器状态。如果将此参数留空，模块将使用 `explicitMPC` 对象的 `Model.Nominal` 属性中定义的标称值。要覆盖默认值，请在工作区中创建一个 `mpcstate` 对象，并在该字段中输入其名称。您可以使用此参数使控制器状态在仿真开始时尽可能反映真实的被控对象环境。

如果启用了自定义状态估计，模块将忽略 **Initial Controller State** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`x0` |
| **类型**：string, character vector |
| **默认值**：`""` |

#### 常规选项卡

### **Measured disturbance** — 添加测量扰动输入端口 `on`（默认）| `off`

如果您的控制器具有测量扰动，则必须选择此参数以将 **md** 输出端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`md_inport` |
| **类型**：string, character vector |
| **值**：`"off"`, `"on"` |
| **默认值**：`"on"` |

### **External manipulated variable** — 添加外部操纵变量输入端口 `off`（默认）| `on`

选择此参数以将 **ext.mv** 输入端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`mv_inport` |
| **类型**：string, character vector |
| **值**：`"off"`, `"on"` |
| **默认值**：`"off"` |

### **Status of piecewise affine function evaluation** — 添加评估状态输出端口 off（默认）| on

选择此参数以将 **status** 输出端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`return_status` |
| **类型**：string, character vector |
| **值**：`"off"`, `"on"` |
| **默认值**：`"on"` |

### **Region number of evaluated piecewise affine function** — 添加区域编号输出端口 off（默认）| on

选择此参数以将 **region** 输出端口添加到模块。

#### 编程用法

|  |
| --- |
| **模块参数：** `return_region` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **估计的控制器状态** — 添加估计状态输出端口 `off`（默认）| `on`

选择此参数可将 **est.state** 输出端口添加到模块中。

#### 编程用法

|  |
| --- |
| **模块参数：** `return_state` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **使用自定义状态估计代替使用内置卡尔曼滤波器** — 使用自定义状态估计输入端口 `off`（默认）| `on`

选择此参数可移除 **mo** 输入端口并添加 **x[k|k]** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数：** `state_inport` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

#### 其他选项卡

### **模块数据类型** — 指定操纵变量的数据类型 `double`（默认）| `single` | `data type expression`

将操纵变量的模块数据类型指定为以下之一：

- `double` — 双精度浮点
- `single` — 单精度浮点

  如果您在单精度目标上实现该模块，请将输出数据类型指定为 `single`。
- `data type expression` — 一个求值为
  `double` 或 `single` 的表达式。有关更多
  信息，请参阅 Control Data Types of Signals (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数：** `BlockDataType` |
| **类型：** string, character vector |
| **值：** `"double"`, `"single"`, `data type expression` |
| **默认值：** `"double"` |

### **继承采样时间** — 从父子系统继承模块采样时间 `off`（默认）| `on`

选择此参数可将父子系统的采样时间继承为模块
采样时间。这样做允许您在 Function-Call Subsystem (Simulink) 或 Triggered Subsystem (Simulink) 模块内有条件地执行此模块。有关示例，请参阅 Using MPC Controller Block Inside Function-Call and Triggered Subsystems。

**注意**

您必须按照控制器的采样率执行 Function-Call Subsystem 或 Triggered
Subsystem 模块。否则，
由于以下两个原因，您可能会看到意外结果。

- MV 速率向量的第一个元素（即操纵变量的当前值与上一个值之间的差值）
  通常是在假设上一个 MV 值发生在 MPC 对象中指定的采样时间的过去时刻的
  情况下进行加权和约束的，当模块以不同的采样率执行时，此假设
  不再成立。
- 内置卡尔曼估计器使用 MPC 对象中指定的采样时间来向 MPC
  优化问题提供当前状态的估计，因此当模块以不同的采样时间执行时，
  估计的状态不再正确。

如果您清除此参数（默认），模块的采样时间将从
控制器对象继承。

要查看模块的采样时间，请在 Simulink 模型窗口中，在 **Debug** 选项卡下，
**Information Overlays** 中，选择
**colors** 或 **Text**。有关更多
信息，请参阅 View Sample Time Information (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTimeInherited` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **使用外部信号启用控制器评估** — 添加关断输入端口 off（默认）| on

选择此参数可将 **switch** 输入端口添加到
模块中。每当向 switch 输入端口馈入非零信号时，控制器
评估将被关闭。有关更多
详细信息，请参阅 **switch** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数：** `switch_inport` |
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

**在 R2014b 中引入**

## 描述

显式模型预测控制器

Explicit MPC Controller 模块使用以下输入信号：

- 被测对象输出（`mo`）或自定义状态估计（`x[k|k]`）
- 参考或设定点（`ref`）
- 被测对象扰动（`md`），如果有的话

Explicit MPC Controller 模块使用查找表存储预先计算的分段仿射最优控制律，而不是像 MPC Controller 模块那样在每个控制区间运行时求解二次规划优化问题。给定相同的 MPC 问题，这两个模块返回相同的解。Explicit MPC Controller 模块需要更少的在线计算量，这对于需要短控制区间的应用非常有用。然而，它具有更重的离线计算量和更大的内存占用。事实上，显式 MPC 的组合特性限制了其仅适用于输入、输出和状态变量相对较少、预测时域较短且输出约束较少的应用。

Explicit MPC Controller 仅支持可选 MPC 功能的一个子集，如下表所示。

| 支持的功能 | 不支持的功能 |
| --- | --- |
| - 内置（Kalman 滤波器）和自定义状态估计 - 状态估计结果的输出端口 - 外部操纵变量反馈信号输入端口 - 单精度模块数据（默认为双精度） - 继承采样时间 | - 在线整定（惩罚权重调整） - 在线约束调整 - 在线操纵变量目标调整 - 参考和/或被测扰动预览 |
