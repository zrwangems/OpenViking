---
type: simulink-block
title: 'LPV System'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Linear Parameter Varying'
documentation_page: 'lpvsystem'
documentation_source_path: 'ref/lpvsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# LPV System

## 端口
```yaml
ports:
- name: u
  summary: 输入信号 标量 | 向量
  direction: input
- name: par
  summary: 参数值 标量 | 向量
  direction: input
- name: IC
  summary: 初始条件 向量
  direction: input
- name: y
  summary: 模型输出 标量 | 向量
  direction: output
- name: x
  summary: 状态值 标量 | 向量
  direction: output
- name: dx
  summary: 状态导数值 标量 | 向量
  direction: output
- name: ss
  summary: 局部状态空间模型 总线
  direction: output
- name: offset
  summary: LPV 模型偏移量 总线
  direction: output
```

### 输入

### **u** — 输入信号 标量 | 向量

指定输入信号 *u*(*t*)。在多输入情况下，此端口接受与输入维度相同的信号。

### **par** — 参数值 标量 | 向量

为定义调度空间（采样网格变量）的变量提供信号。调度变量可以是时间、输入和状态的函数，也可以是常数。你可以根据需要，通过使用时钟输入（用于时间）、输入信号（**u**）、LPV 模块的输出状态信号（**x**）或任何外生信号来准备调度信号，从而实现所需的依赖关系。

**注意**

避免使 *C*(*p*) 和 *D*(*p*) 依赖于系统输出 **y**。否则，得到的状态空间方程 *y* = *C*(*y*)*x* + *D*(*y*)*u* 会形成代数环，因为计算输出值 *y* 需要知道输出值。此代数环容易导致不稳定和发散。相反，应尝试用时间 *t*、模块输入 **u** 和状态输出 **x** 来表示 *C* 和 *D*。

出于类似原因，避免基于 **dx** 输出对 *A*(*p*) 和 *B*(*p*) 进行调度。请注意，当 **y** 是状态和输入的固定组合时（换句话说，当 *y* = *C**x* + *D**u*，其中 *C* 和 *D* 为常数矩阵时），*A* 和 *B* 依赖于 **y** 是安全的。

### **IC** — 初始条件 向量

*自 R2024b 起*

用于局部模型以开始仿真的初始条件，指定为长度等于模型状态数的向量。

#### 依赖关系

要启用此端口，请将 **Initial condition source** 设置为 `external`。

### 输出

### **y** — 模型输出 标量 | 向量

线性参数变化模型的响应。

### **x** — 状态值 标量 | 向量

模型状态的值。

#### 依赖关系

要启用此端口，请在模块参数的 **Outputs** 选项卡上选择 **Output states**。

### **dx** — 状态导数值 标量 | 向量

状态导数的值。状态导数有时用于定义调度参数。但是，避免基于 **dx** 输出对 *A* 和 *B* 进行调度。

#### 依赖关系

要启用此端口，请在模块参数的 **Outputs** 选项卡上选择 **Output state derivatives (continuous-time) or updates (discrete-time)**。

### **ss** — 局部状态空间模型 总线

主要仿真时间步处的局部状态空间模型数据，以包含以下元素的 bus 信号返回。

- `A` — 状态矩阵
- `B` — 输入矩阵
- `C` — 输出矩阵
- `D` — 直通矩阵
- `InputDelay` — 输入延迟
- `OutputDelay` — 输出延迟
- `InternalDelay` — 模型中的内部延迟

#### 依赖关系

要启用此端口，请在模块参数的 **Outputs** 选项卡上选择 **Output interpolated state-space data**。

### **offset** — LPV 模型偏移量 总线

主要仿真时间步处的 LPV 模型偏移量数据，以包含以下元素的 bus 信号返回。

- `InputOffset`
- `OutputOffset`
- `StateOffset`
- `StateDerivativeOffset`

#### 依赖关系

要启用此端口，请在模块参数的 **Outputs** 选项卡上选择 **Output interpolated offsets**。
## 参数
```yaml
parameters:
- name: State-space array
  summary: ss 或 idss 模型数组的 State-space 模型数组
  group: LPV Model 选项卡
  block_parameter: sys
  values: 带引号的 ss 或 idss 模型数组名称
- name: Initial condition source
  summary: 使用外部信号设置初始条件的选项 internal（默认）| external
  group: LPV Model 选项卡
  block_parameter: InitialConditionSource
  values: internal（默认）| external
- name: Initial condition
  summary: 初始条件 0（默认）| 向量
  group: LPV Model 选项卡
  block_parameter: InitialCondition
  values: '"0"（默认）| 带引号的初始状态值'
- name: Operating Point Offsets
  summary: 偏移量指定格式 Specify Offsets as double arrays（默认）| Specify offsets as struct array | Use offsets in state-space array
  group: LPV Model 选项卡
  block_parameter: opSpecOption
  values: '"Specify Offsets as double arrays"（默认）| "Specify offsets as struct array" | "Use offsets in state-space array"'
- name: Input offset
  summary: 输入偏移 0（默认）| 数组
  group: LPV Model 选项卡
  block_parameter: uOffset
  values: '"0"（默认）| 带引号的数组名称'
- name: Output offset
  summary: 输出偏移 0（默认）| 数组
  group: LPV Model 选项卡
  block_parameter: yOffset
  values: '"0"（默认）| 带引号的数组名称'
- name: State offset
  summary: 状态偏移 0（默认）| 数组
  group: LPV Model 选项卡
  block_parameter: xOffset
  values: '"0"（默认）| 带引号的数组名称'
- name: State derivative/update offset
  summary: 状态导数/更新偏移数组
  group: LPV Model 选项卡
  block_parameter: dxOffset
  values: '"0"（默认）| 带引号的数组名称'
- name: Struct array
  summary: 偏移结构体数组 struct（默认）| 结构体数组名称
  group: LPV Model 选项卡
  block_parameter: Offset
  values: '"struct"（默认）| 带引号的结构体数组名称'
- name: Coefficients To Fix
  summary: 状态空间矩阵的固定系数 false 或 0（默认）| true 或 1 | 逻辑矩阵
  group: 固定条目选项卡
- name: Read values from
  summary: 固定系数值的来源 First model in state-space array（默认）| Custom state-space model
  group: 固定条目选项卡
- name: Interpolation method
  summary: 插值方法 Linear（默认）| Nearest | Flat
  group: 调度选项卡
  block_parameter: IMethod
  values: '"Linear" (default) | "Nearest" | "Flat"'
- name: Extrapolation method
  summary: 外插方法 Clip（默认）| Linear
  group: 调度选项卡
  block_parameter: EMethod
  values: '"Clip" (default) | "Linear"'
- name: Index search method
  summary: 预查找算法 Binary search（默认）| Linear search
  group: 调度选项卡
  block_parameter: IndexSearch
  values: '"Binary Search" (default) | "Linear Search"'
- name: Begin index search using previous index result
  summary: 从上一时间步开始搜索 on（默认）| off
  group: 调度选项卡
  block_parameter: IndexBegin
  values: '"on"（默认） | "off"'
- name: 模块数据类型（仅离散时间情况）
  summary: 模块数据类型 double（默认） | single
  group: 代码生成选项卡
  block_parameter: DataType
  values: '"double"（默认） | "single"'
- name: 延迟的初始缓冲区大小
  summary: 初始缓冲区大小 1024（默认） | 大于 5 的正整数
  group: 代码生成选项卡
  block_parameter: InitBufferSize
  values: '"1024"（默认） | 带引号的大于 5 的正整数'
- name: 使用固定缓冲区大小
  summary: 使用固定缓冲区大小 off（默认） | on
  group: 代码生成选项卡
  block_parameter: FixedBuffer
  values: '"off"（默认） | "on"'
```

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### LPV Model 选项卡

### **State-space array** — `ss` 或 `idss` 模型数组的 State-space 模型数组

State-space（`ss` 或 `idss`（System Identification Toolbox））模型的数组。数组中的所有模型必须使用相同的状态定义。

State-space 数组必须在 `SamplingGrid` 属性中指定调度参数和插值网格。当您将 **Operating Point Offsets** 参数设置为 `Use offsets in state-space array` 时，还可以在数组的 `Offsets` 属性中指定模型偏移量。有关这些属性的详细信息，请参阅 `ss` 模型参考页。

当模块位于具有同步状态控制的模型中时（请参阅 State Control (HDL Coder) 模块），您必须指定离散时间模型的数组。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `sys` |
| **值**：| 带引号的 `ss` 或 `idss` 模型数组名称 |

**Example:** `set_param(gcb,"sys","sysArrayName")`

### **Initial condition source** — 使用外部信号设置初始条件的选项 `internal`（默认）| `external`

*Since R2024b*

指定初始条件来源。

- `internal` — 使用 **Initial condition** 参数指定状态的初始条件。
- `external` — 在模块的 **IC** 输入端口指定状态的初始条件。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `InitialConditionSource` |
| **值**：| `internal`（默认）| `external` |

### **Initial condition** — 初始条件 0（默认）| 向量

用于局部模型以启动仿真的初始条件，指定为长度等于模型状态数的向量。

#### 依赖关系

要启用此参数，请将 **Initial condition source** 设置为 `internal`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `InitialCondition` |
| **值**：| `"0"`（默认）| 带引号的初始状态值 |

**Example:** `set_param(gcb,"InitialCondition","[0
0.1]")`

### **Operating Point Offsets** — 偏移量指定格式 `Specify Offsets as double arrays`（默认）| `Specify offsets as struct array` | `Use offsets in state-space array`

*Since R2024a*

指定工作点偏移量的格式。

- `Specify Offsets as double arrays` — 使用 **Input offset**、**Output offset**、**State Offset** 和 **State derivative/update offset** 参数指定偏移量。
- `Specify offsets as struct array` — 将偏移量指定为结构体数组，其字段 `u`、`y`、`x` 和 `dx` 分别指定输入、输出、状态和状态导数偏移量。
- `Use offsets in state-space array` — 使用 state-space 数组的 `Offsets` 属性中指定的偏移量。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `opSpecOption` |
| **值**：| `"Specify Offsets as double arrays"`（默认）| `"Specify offsets as struct array"` | `"Use offsets in state-space array"` |

**Example:** `set_param(gcb,"opSpecOption","Specify offsets as struct
array")`

### **Input offset** — 输入偏移 `0`（默认）| 数组

输入 `u(t)` 中的偏移，指定为以下之一：

- `0` — 当没有输入偏移时使用（u¯(p)=0 ∀ p）。
- 长度等于输入数量的双精度向量 — 当输入偏移在整个调度空间中相同时使用。
- 大小为
  *nu*-by-1-by-*N1*-by-`...`-by-*Nm*
  的双精度数组 — 当存在偏移且它们在调度空间中变化时使用。这里，
  *nu* 是输入数量，
  *N1*-by-`...`-by-*Nm*
  是调度网格的大小。例如，如果你的模型有三个输入、两个输出和四个状态，并且在 5-by-6 的工作点网格上进行调度，则输入数组大小必须为 3-by-1-by-5-by-6。使用
  `size(sys)` 确定状态空间数组
  `sys` 的大小。

#### 依赖关系

要启用此参数，请将 **Operating Point Offsets**
格式设置为 `Specify Offsets as double arrays`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `uOffset` |
| **值**：| `"0"`（默认）| 带引号的数组名称 |

**Example:** `set_param(gcb,"uOffset","uOffArray")`

### **Output offset** — 输出偏移 `0`（默认）| 数组

输出 `y(t)` 中的偏移，指定为以下之一：

- `0` — 当没有输出偏移时使用 y¯(p)=0 ∀ p。
- 长度等于输出数量的双精度向量 — 当输出偏移在整个调度空间中相同时使用。
- 大小为
  *ny*-by-1-by-*N1*-by-`...`-by-*Nm*
  的双精度数组 — 当存在偏移且它们在调度空间中变化时使用。这里，
  *ny* 是输出数量，
  *N1*-by-`...`-by-*Nm*
  是调度网格的大小。例如，如果你的模型有三个输入、两个输出和四个状态，并且在 5-by-6 的工作点网格上进行调度，则输入数组大小必须为 2-by-1-by-5-by-6。使用
  `size(sys)` 确定状态空间数组
  `sys` 的大小。

#### 依赖关系

要启用此参数，请将 **Operating Point Offsets**
格式设置为 `Specify Offsets as double arrays`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `yOffset` |
| **值**：| `"0"`（默认）| 带引号的数组名称 |

**Example:** `set_param(gcb,"yOffset","yOffArray")`

### **State offset** — 状态偏移 `0`（默认）| 数组

状态 `x(t)` 中的偏移，指定为以下之一：

- `0` — 当没有状态偏移时使用 x¯(p)=0 ∀ p。
- 长度等于状态数量的双精度向量 — 当状态偏移在整个调度空间中相同时使用。
- 大小为
  *nx*-by-1-by-*N1*-by-`...`-by-*Nm*
  的双精度数组 — 当存在偏移且它们在调度空间中变化时使用。这里，
  *nx* 是状态数量，
  *N1*-by-`...`-by-*Nm*
  是调度网格的大小。例如，如果你的模型有三个输入、两个输出和四个状态，并且在 5-by-6 的工作点网格上进行调度，则输入数组大小必须为 4-by-1-by-5-by-6。使用
  `size(sys)` 确定状态空间数组
  `sys` 的大小。

#### 依赖关系

要启用此参数，请将 **Operating Point Offsets**
格式设置为 `Specify Offsets as double arrays`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `xOffset` |
| **值**：| `"0"`（默认）| 带引号的数组名称 |

**Example:** `set_param(gcb,"xOffset","xOffArray")`

### **State derivative/update offset** — 状态导数/更新偏移数组

状态导数或更新变量 `dx(t)` 中的偏移，指定为以下之一：

- 如果您通过平衡条件下的线性化获得线性系统数组，请选择 **Assume equilibrium operating conditions** 选项。此选项对应于连续时间系统的偏移 dx¯(p)=0 和离散时间系统的 dx¯(p)=x¯(p)。默认情况下选中此选项。
- 如果线性系统包含至少一个在非平衡条件下获得的系统，请清除 **Assume equilibrium operating conditions** 选项。在 **Offset value** 字段中指定以下之一：

  - 长度等于状态数的双精度向量 — 当状态导数偏移在整个调度空间中相同时使用。
  - 大小为 *nx*-by-1-by-*N1*-by-`...`-by-*Nm* 的双精度数组 — 当存在偏移且偏移在调度空间中变化时使用。此处，*nx* 是状态数，*N1*-by-`...`-by-*Nm* 是调度网格的大小。例如，如果您的模型有三个输入、两个输出和四个状态，并且在 5×6 的工作点网格上进行调度，则输入数组大小必须为 4-by-1-by-5-by-6。使用 `size(sys)` 确定状态空间数组 `sys` 的大小。

#### 依赖关系

要启用此参数，请将 **Operating Point Offsets** 格式设置为 `Specify Offsets as double arrays` 并禁用 **Assume equilibrium operating conditions**。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `dxOffset` |
| **值：** | `"0"`（默认）| 带引号的数组名称 |

**示例：** `set_param(gcb,"dxOffset","dxOffArray")`

### **Struct array** — 偏移结构体数组 `struct`（默认）| 结构体数组名称

*自 R2024a 起*

模型偏移，指定为包含以下字段的结构体。

| 字段 | 描述 |
| --- | --- |
| `u` | 输入偏移 |
| `y` | 输出偏移 |
| `x` | 状态偏移 |
| `dx` | 状态导数偏移 |

- 如果偏移值在整个调度空间中相同，请指定为长度等于对应字段的输入、输出或状态数的双精度向量。
- 如果偏移在调度空间中变化，请指定结构体数组。例如，假设您的模型有三个输入、两个输出和四个状态。如果您使用 5×6 的工作点数组对模型进行线性化，则结构体数组大小必须为 5×6，并且每个条目必须包含一个长度等于对应字段的输入、输出或状态数的向量。

当您使用 `StoreOffsets` 选项设置为 `true` 进行线性化时，`linearize` (Simulink Control Design) 函数会在 `info.Offsets` 输出中以此格式返回偏移。

#### 依赖关系

要启用此参数，请将 **Operating Point Offsets** 格式设置为 `Specify Offsets as struct array`。*（自 R2024a 起）*

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `Offset` |
| **值：** | `"struct"`（默认）| 带引号的结构体数组名称 |

**示例：** `set_param(gcb,"Offset","OffsetStructName")`

### 固定条目选项卡

在某些情况下，您的 LPV 模型可能包含变化很小的系数。使用此选项卡上的参数，您可以指定哪些模型矩阵是固定的及其标称值，以覆盖模型数据中的条目。在某些情况下，您可能希望将参数依赖矩阵（例如 *A*(*p*)）替换为固定值 *A\** 用于仿真。例如，*A\** 可以表示调度范围内的平均值。默认情况下，模块使用 **State-space array** 数据来决定哪些条目是固定的，哪些条目是变化的（出于性能原因，模块仅对变化的条目进行插值）。

使用此选项卡，您可以覆盖此默认行为，例如尝试简化 LPV 模型。例如，您可以确定 *A* 的第三个条目变化不大，并希望将其固定为其平均值。逻辑数组指定哪些条目应被视为固定，**Read values from** 指定这些固定条目使用哪个值。`false` 对应于不覆盖 LTI 数组数据，即依赖数据来决定此条目是固定还是变化。

### **Coefficients To Fix** — 状态空间矩阵的固定系数 `false` 或 `0`（默认）| `true` 或 `1` | 逻辑矩阵

将这些系数的位置指定为以下之一：

- 标量布尔值（`true` 或 `false`），如果矩阵的所有条目都以相同方式处理。

  状态空间矩阵和延迟向量的默认值为 `false`，这意味着它们被视为自由的。
- 与相应矩阵大小兼容的逻辑矩阵：

  | 状态空间矩阵 | 固定条目矩阵的大小 |
  | --- | --- |
  | **A matrix** | *nx*-by-*nx* |
  | **B matrix** | *nx*-by-*nu* |
  | **C matrix** | *ny*-by-*nx* |
  | **D matrix** | *ny*-by-*nu* |
  | **Input delay** | *nu*-by-1 |
  | **Output delay** | *ny*-by-1 |
  | **Internal delay** | *ni*-by-1 |

  其中，*nu* 是输入数量，*ny* 是输出数量，*nx* 是状态数量，*ni* 是内部延迟向量的长度。
- 用于指定固定条目位置的数值索引。有关如何为矩阵元素生成与给定下标 `(i,j)` 对应的数值索引的更多信息，请参阅 `sub2ind` 参考页。

指定位置后，使用 **Read values from** 参数提供固定系数的值。

### **Read values from** — 固定系数值的来源 `First model in state-space array`（默认）| `Custom state-space model`

提供固定系数值的状态空间模型，指定为以下之一：

- `First model in state-space array` — 状态空间数组中的第一个模型用于 LPV 模型的固定系数。在以下示例中，状态空间数组由对象 `sys` 指定，固定系数取自模型 `sys(:,:,1)`。

  ```
  % Specify a 4-by-5 array of state-space models.
  sys = rss(4,2,3,4,5);
  a = 1:4;
  b = 10:10:50;
  [av,bv] = ndgrid(a,b);
  % Use "alpha" and "beta" variables as scheduling parameters.
  sys.SamplingGrid = struct('alpha',av,'beta',bv);
  ```

  固定系数取自模型 `sysFixed = sys(:,:,1)`，其对应于 `[alpha=1, beta=10]`。如果 `A` 矩阵的 (2,1) 条目被强制固定，则仿真期间使用的值为 `sysFixed.A(2,1)`。
- `Custom state-space model` — 为固定条目指定不同的状态空间模型。在 **Custom model** 字段中为固定模型指定一个变量。固定模型必须使用与 LPV 模型中的状态空间数组相同的状态基。

### 调度选项卡

### **Interpolation method** — 插值方法 `Linear`（默认）| `Nearest` | `Flat`

插值方法。定义对于位于其网格位置之外的调度参数值，必须如何计算状态空间数据。

指定以下选项之一：

- `Flat` — 选择最接近但不大于当前点的网格点处的状态空间数据。*当前点*是当前时刻调度参数的值。
- `Nearest` — 选择调度空间中最近网格点处的状态空间数据。
- `Linear` — 通过对调度空间中最近的 2d 个相邻点进行线性插值来获取状态空间数据，其中 d = 调度参数的数量。

对于调度参数值的规则网格，默认插值方案为 `Linear`。对于不规则网格，无论您做出何种选择，始终使用 `Nearest` 插值方案。要了解有关规则网格和不规则网格的更多信息，请参阅 Regular vs. Irregular Grids。

`Linear` 方法提供最高精度，但计算时间更长。`Flat` 和 `Nearest` 方法适用于具有模式切换动态的模型。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `IMethod` |
| **值**：| `"Linear"` (default) | `"Nearest"` | `"Flat"` |

**Example:** `set_param(gcb,"IMethod","Flat")`

### **Extrapolation method** — 外插方法 `Clip`（默认）| `Linear`

外插方法。定义如何为超出状态空间数组所提供范围（如 `SamplingGrid` 属性中所指定）的调度参数值计算状态空间数据。

指定以下选项之一：

- `Clip`（默认）— 禁用外插，并返回与最接近当前点的最后一个可用调度网格点对应的数据。
- `Linear` — 根据当前值是分别小于第一个网格点值还是大于最后一个网格点值，为每个调度参数在第一个或最后一对值之间拟合一条直线。此方法返回该直线上对应当前值的点。线性外插要求插值方案也必须是线性的。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `EMethod` |
| **值**：| `"Clip"` (default) | `"Linear"` |

**Example:** `set_param(gcb,"EMethod","Linear")`

### **Index search method** — 预查找算法 `Binary search`（默认）| `Linear search`

该模块使用预查找算法确定当前调度参数值在调度空间中的位置。选择 `Linear search` 或 `Binary search`。每种搜索方法在不同情况下各有速度优势。有关此参数的更多信息，请参阅 Prelookup (Simulink) 模块参考页。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `IndexSearch` |
| **值**：| `"Binary Search"` (default) | `"Linear Search"` |

**Example:** `set_param(gcb,"IndexSearch","Linear
Search")`

### **Begin index search using previous index result** — 从上一时间步开始搜索 `on`（默认）| `off`

当您希望模块使用上一时间步找到的索引开始搜索时，请选中此复选框。有关此参数的更多信息，请参阅 Prelookup (Simulink) 模块参考页。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `IndexBegin` |
| **值：** | `"on"`（默认） | `"off"` |

**示例：** `set_param(gcb,"IndexBegin","off")`

### 代码生成选项卡

### **模块数据类型（仅离散时间情况）** — 模块数据类型 `double`（默认） | `single`

模块数据类型，指定为 `double` 或 `single`。

#### 依赖关系

要启用此选项，请使用离散时间状态空间模型作为输入。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `DataType` |
| **值：** | `"double"`（默认） | `"single"` |

**示例：** `set_param(gcb,"DataType","single")`

### **延迟的初始缓冲区大小** — 初始缓冲区大小 `1024`（默认） | 大于 5 的正整数

为包含延迟的模型存储输入点数的初始内存分配。如果输入点数超过初始缓冲区大小，模块将分配额外内存。默认大小为 1024。

当您在 Accelerator 模式下运行模型或构建模型时，请确保初始缓冲区大小足够大，以处理模型中预期的最大延迟。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `InitBufferSize` |
| **值：** | `"1024"`（默认） | 带引号的大于 5 的正整数 |

**示例：** `set_param(gcb,"InitBufferSize","512")`

### **使用固定缓冲区大小** — 使用固定缓冲区大小 `off`（默认） | `on`

指定是否使用固定缓冲区大小来保存前一时间步的延迟输入和输出数据。对于包含输入或输出延迟的连续时间 LPV 系统，请使用此选项。如果缓冲区已满，新数据将替换缓冲区中已有的数据。软件使用线性外推来估计不在缓冲区中的输出值。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `FixedBuffer` |
| **值：** | `"off"`（默认） | `"on"` |

**示例：** `set_param(gcb,"FixedBuffer","on")`
## 所属库

Control System Toolbox / Linear Parameter Varying

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014b 中引入**

### R2024b：将初始条件外部指定为模块输入

LPV System 模块现在允许您在模块输入端口 **IC** 处指定初始状态值。要启用此端口，请将 **初始条件源** 参数设置为 `external`。

### R2024b：初始状态参数 `x0` 重命名为 `InitialCondition`

初始状态参数 `x0` 现在称为 `InitialCondition`。如果您的代码以编程方式设置此参数，例如使用 `set_param(blockPath,"x0","[0 0.1]")`，请将代码更新为 `set_param(blockPath,"InitialCondition","[0 0.1]")`。

### R2024a：改进的偏移支持及其他增强功能

LPV System 模块现在支持以两种新格式指定工作点偏移：

- 将偏移指定为结构体数组
- 在状态空间数组中使用偏移

在 R2024a 之前，模块仅支持在模块参数中以双精度数组形式指定偏移。使用 **工作点偏移** 列表来指定偏移的格式。

此外，该模块还具有以下新增强功能：

- 模块架构现在底层使用 Varying State Space 模块。这简化了对偏移的支持。
- 该模块现在支持仿真的快速重启。在此模式下，仅模块输入和 **初始状态** 参数可调。其余模块参数不可调，因为更改它们会改变模型拓扑。

### R2024a: 忽略 `SamplingGrid` 中的常量参数

LPV System 模块现在会忽略输入模型数组采样网格中的单一维度和常量参数。因此，不得将常量值参数（即 `SamplingGrid` 结构中具有常量值的字段）馈送到模块的 **par** 端口。此端口仅使用变化的字段。

在 R2024a 之前，当馈送具有常量值的参数时，模块会返回错误。

## 描述

仿真线性参数变化（LPV）系统

*线性参数变化*（LPV）系统是一种线性状态空间模型，其动态特性作为某些时变参数（称为*调度参数*）的函数而变化。在 MATLAB® 中，LPV 模型使用依赖于参数的系数以状态空间形式表示。

在数学上，可以将 LPV 系统表示如下。

dx(t)=dx0(p)+A(p)(x(t)−x0(p))+B(p)(u(t)−u0(p))y(t)=y0(p)+C(p)(x(t)−x0(p))+D(p)(u(t)−u0(p))x(0)=xinit

其中：

- *u*(*t*) 是输入
- *y*(*t*) 是输出
- *x*(*t*) 是模型状态，初始值为 *xinit*
- dx(t) 是连续时间系统的状态导数向量 x˙，以及离散时间系统的状态更新向量 *x*[*k*+1]。其中，*k* 是计算采样周期 *Ts* 数量的整数索引。
- *A*(*p*)、*B*(*p*)、*C*(*p*) 和 *D*(*p*) 是由调度参数向量 *p* 参数化的状态空间矩阵。
- 参数 *p* = *p*(*t*) 是模型输入和状态的可测函数。它们可以是标量或由多个参数组成的向量。调度参数的集合定义了 LPV 模型所定义的*调度空间*。
- *dx*0(*p*)、*x*0(*p*)、*u*0(*p*) 和 *y*0(*p*) 是在给定参数值 *p* = *p*(*t*) 或 *p*[*k*] 处 dx(t)、*x*(*t*)、*u*(*t*) 和 *y*(*t*) 值的偏移量。

  可以通过在调用 `linearize` (Simulink Control Design) 或 `getIOTransfer` (Simulink Control Design) 等函数时返回额外的线性化信息来获得这些偏移量。有关示例，请参见 LPV Approximation of Boost Converter Model (Simulink Control Design)。

**注意**

避免使 *C*(*p*) 和 *D*(*p*) 依赖于系统输出 **y**。否则，得到的状态空间方程 *y* = *C*(*y*)*x* + *D*(*y*)*u* 会产生代数环，因为计算输出值 *y* 需要知道输出值。此代数环容易导致不稳定和发散。相反，请尝试用时间 *t*、模块输入 **u** 和状态输出 **x** 来表示 *C* 和 *D*。

出于类似原因，避免基于 **dx** 输出调度 *A*(*p*) 和 *B*(*p*)。请注意，当 **y** 是状态和输入的固定组合时（换句话说，当 *y* = *C**x* + *D**u*，其中 *C* 和 *D* 是常量矩阵时），*A* 和 *B* 依赖于 **y** 是安全的。

该模块实现 LPV 系统的基于网格的表示。为调度参数选择一组网格值。在每个值 *p* = *p\** 处，将对应的线性系统指定为状态空间（`ss` 或 `idss` (System Identification Toolbox)）模型对象。使用生成的状态空间模型数组来配置 LPV System 模块。

该模块接受带有工作点信息的状态空间模型数组。该模块从 LTI 数组的 `SamplingGrid` 属性中提取调度变量信息。调度变量定义 LPV 模型的网格。它们是标量值量，可以是时间、输入和状态的函数，也可以是常量。它们用于选择工作空间中的局部动态。软件对这些变量的值进行插值。该模块使用此数组以及数据插值和外推技术进行仿真。
