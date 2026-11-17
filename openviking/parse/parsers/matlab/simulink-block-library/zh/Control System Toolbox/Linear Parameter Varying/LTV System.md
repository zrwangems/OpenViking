---
type: simulink-block
title: 'LTV System'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Linear Parameter Varying'
documentation_page: 'ltvsystem'
documentation_source_path: 'ref/ltvsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# LTV System

## 端口
```yaml
ports:
- name: u
  summary: 输入信号 标量 | 向量
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

指定输入信号 *u*(*t*)。在多输入情况下，此端口接受维度与输入维度一致的信号。

### **IC** — 初始条件 向量

*自 R2024b 起*

用于启动仿真的局部模型初始条件，指定为长度等于模型状态数的向量。

#### 依赖关系

要启用此端口，请将 **Initial condition source** 设置为 `external`。

### 输出

### **y** — 模型输出 标量 | 向量

线性时变模型的响应。

### **x** — 状态值 标量 | 向量

模型状态的值

#### 依赖关系

要启用此端口，请在模块参数的 **Outputs** 选项卡上选择 **Output states**。

### **dx** — 状态导数值 标量 | 向量

状态导数的值。

#### 依赖关系

要启用此端口，请在模块参数的 **Outputs** 选项卡上选择 **Output state derivatives (continuous-time) or updates (discrete-time)**。

### **ss** — 局部状态空间模型 总线

主要仿真时间步处的局部状态空间模型数据，以包含以下元素的总线信号形式返回。

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

主要仿真时间步处的 LTV 模型偏移量数据，以包含以下元素的总线信号形式返回。

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
  summary: 状态空间模型数组 ss 或 idss 模型数组
  group: LTV Model 选项卡
  block_parameter: sys
  values: 带引号的 ss 或 idss 模型数组名称
- name: Initial condition source
  summary: 使用外部信号设置初始条件的选项 internal（默认）| external
  group: LTV Model 选项卡
  block_parameter: InitialConditionSource
  values: internal（默认）| external
- name: Initial condition
  summary: 初始条件 0（默认）| 向量
  group: LTV Model 选项卡
  block_parameter: InitialCondition
  values: '"0"（默认） | 带引号的初始状态值'
- name: Operating Point Offsets
  summary: 偏移量指定格式 Specify Offsets as double arrays（默认） | Specify offsets as struct array | Use offsets in state-space array
  group: LTV Model 选项卡
  block_parameter: opSpecOption
  values: '"Specify Offsets as double arrays"（默认） | "Specify offsets as struct array" | "Use offsets in state-space array"'
- name: Input offset
  summary: 输入偏移量 0（默认） | 数组
  group: LTV Model 选项卡
  block_parameter: uOffset
  values: '"0"（默认） | 带引号的数组名称'
- name: Output offset
  summary: 输出偏移量 0（默认） | 数组
  group: LTV Model 选项卡
  block_parameter: yOffset
  values: '"0"（默认） | 带引号的数组名称'
- name: State offset
  summary: 状态偏移 0（默认）| 数组
  group: LTV Model 选项卡
  block_parameter: xOffset
  values: '"0"（默认）| 带引号的数组名称'
- name: State derivative/update offset
  summary: 状态导数或更新偏移数组
  group: LTV Model 选项卡
  block_parameter: dxOffset
  values: '"0"（默认）| 带引号的数组名称'
- name: Struct array
  summary: 偏移量结构体数组 struct（默认）| 结构体数组名称
  group: LTV Model 选项卡
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
  group: Scheduling Tab
  block_parameter: IMethod
  values: '"Linear"（默认）| "Nearest" | "Flat"'
- name: Extrapolation method
  summary: 外插方法 Clip（默认）| Linear
  group: Scheduling Tab
  block_parameter: EMethod
  values: '"Clip"（默认）| "Linear"'
- name: 索引搜索方法
  summary: 预查找算法 Binary search（默认）| Linear search
  group: Scheduling Tab
  block_parameter: IndexSearch
  values: '"Binary Search"（默认）| "Linear Search"'
- name: 使用前一次索引结果开始索引搜索
  summary: 从前一时间步开始搜索 on（默认）| off
  group: Scheduling Tab
  block_parameter: IndexBegin
  values: '"on"（默认）| "off"'
- name: 模块数据类型（仅离散时间情况）
  summary: 模块数据类型 double（默认）| single
  group: 代码生成选项卡
  block_parameter: DataType
  values: '"double"（默认）| "single"'
- name: 延迟的初始缓冲区大小
  summary: 初始缓冲区大小 1024（默认）| 大于 5 的正整数
  group: 代码生成选项卡
  block_parameter: InitBufferSize
  values: '"1024"（默认）| 带引号的大于 5 的正整数'
- name: 使用固定缓冲区大小
  summary: 使用固定缓冲区大小 off（默认）| on
  group: 代码生成选项卡
  block_parameter: FixedBuffer
  values: '"off"（默认）| "on"'
```

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### LTV Model 选项卡

### **State-space array** — 状态空间模型数组 `ss` 或 `idss` 模型数组

状态空间（`ss` 或 `idss`（System Identification Toolbox））模型的数组。数组中的所有模型必须使用相同的状态定义。

状态空间数组必须在 `SamplingGrid` 属性中指定对时间的依赖性。当您将 **Operating Point Offsets** 参数设置为 `Use offsets in state-space array` 时，还可以在数组的 `Offsets` 属性中指定模型偏移量。有关这些属性的详细信息，请参阅 `ss` 模型参考页。

当模块位于具有同步状态控制的模型中时（请参阅 State Control (HDL Coder) 模块），您必须指定离散时间模型的数组。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `sys` |
| **值：** | 带引号的 `ss` 或 `idss` 模型数组名称 |

**示例：** `set_param(gcb,"sys","sysArrayName")`

### **Initial condition source** — 使用外部信号设置初始条件的选项 `internal`（默认）| `external`

*自 R2024b 起*

指定初始条件源。

- `internal` — 使用 **Initial condition** 参数指定状态的初始条件。
- `external` — 在模块的 **IC** 输入端口处指定状态的初始条件。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `InitialConditionSource` |
| **值：** | `internal`（默认）| `external` |

### **Initial condition** — 初始条件 0（默认）| 向量

用于启动仿真的局部模型初始条件，指定为长度等于模型状态数的向量。

#### 依赖关系

要启用此参数，请将 **Initial condition source** 设置为
`internal`。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `InitialCondition` |
| **值：** | `"0"`（默认） | 带引号的初始状态值 |

**示例：** `set_param(gcb,"InitialCondition","[0
0.1]")`

### **Operating Point Offsets** — 偏移量指定格式 `Specify Offsets as double arrays`（默认） | `Specify offsets as struct array` | `Use offsets in state-space array`

指定工作点偏移量的格式。

- `Specify Offsets as double arrays` — 使用 **Input offset**、**Output offset**、
  **State Offset** 和 **State derivative/update
  offset** 参数指定偏移量。
- `Specify offsets as struct array` — 将偏移量指定为结构体数组，其字段 `u`、`y`、
  `x` 和 `dx` 分别指定输入、输出、
  状态和状态导数偏移量。
- `Use offsets in state-space array` — 使用状态空间数组的 `Offsets` 属性中
  指定的偏移量。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `opSpecOption` |
| **值：** | `"Specify Offsets as double arrays"`（默认） | `"Specify offsets as struct array"` | `"Use offsets in state-space array"` |

**示例：** `set_param(gcb,"opSpecOption","Specify offsets as struct
array")`

### **Input offset** — 输入偏移量 `0`（默认） | 数组

输入 *u*(*t*) 中的偏移量，指定为以下之一：

- `0` — 当没有输入偏移量时使用。
- 长度等于输入数量的双精度向量 — 当输入偏移量
  在整个调度空间中相同时使用。
- 大小为
  *nu*-by-1-by-*N* 的双精度数组 — 当存在偏移量且它们在整个调度空间中变化时使用。其中，
  *nu* 是输入数量，
  *N* 是时间快照数量。例如，如果您的模型
  有三个输入、两个输出和四个状态，并且在 10 个时间
  快照上进行调度，则数组大小必须为 3-by-1-by-10。使用 `size(sys)`
  确定状态空间数组 `sys` 的大小。

#### 依赖关系

要启用此参数，请将 **Operating Point Offsets**
格式设置为 `Specify Offsets as double arrays`

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `uOffset` |
| **值：** | `"0"`（默认） | 带引号的数组名称 |

**示例：** `set_param(gcb,"uOffset","uOffArray")`

### **Output offset** — 输出偏移量 `0`（默认） | 数组

输出 *y*(*t*) 中的偏移量，指定为以下之一：

- `0` 当没有输出偏移量时使用。
- 长度等于输出数量的双精度向量。当输出
  偏移量在整个调度空间中相同时使用。
- 大小为
  *ny*-by-1-by-*N* 的双精度数组 — 当存在偏移量且它们在整个调度空间中变化时使用。其中，
  *ny* 是输出数量，
  *N* 是时间快照数量。例如，如果您的模型
  有三个输入、两个输出和四个状态，并且在 10 个时间
  快照上进行调度，则数组大小必须为 2-by-1-by-10。使用 `size(sys)`
  确定状态空间数组 `sys` 的大小。

#### 依赖关系

要启用此参数，请将 **Operating Point Offsets**
格式设置为 `Specify Offsets as double arrays`

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `yOffset` |
| **值：** | `"0"`（默认） | 带引号的数组名称 |

**示例：** `set_param(gcb,"yOffset","yOffArray")`

### **State offset** — 状态偏移 `0`（默认）| 数组

状态 *x*(*t*) 中的偏移，指定为以下之一：

- `0` — 当没有状态偏移时使用。
- 长度等于状态数量的双精度向量 — 当状态偏移在调度空间中相同时使用。
- 大小为 *nx*-by-1-by-*N* 的双精度数组 — 当存在偏移且它们在调度空间中变化时使用。此处，*nx* 是状态数量，*N* 是时间快照数量。例如，如果您的模型有三个输入、两个输出和四个状态，并且在 10 个时间快照上进行调度，则数组大小必须为 4-by-1-by-10。使用 `size(sys)` 确定状态空间数组 `sys` 的大小。

#### 依赖关系

要启用此参数，请将 **Operating Point Offsets** 格式设置为 `Specify Offsets as double arrays`

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `xOffset` |
| **值：** | `"0"`（默认）| 带引号的数组名称 |

**示例：** `set_param(gcb,"xOffset","xOffArray")`

### **State derivative/update offset** — 状态导数或更新偏移数组

状态导数或更新变量 *dx*(*t*) 中的偏移，指定为以下之一：

- 如果您通过在平衡条件下进行线性化获得了线性系统数组，请选择 **Assume equilibrium operating conditions** 选项。此选项对应于连续时间系统的偏移 dx¯(t)=0 和离散时间系统的 dx¯(t)=x¯(t)。默认情况下选中此选项。
- 如果线性系统包含至少一个您在非平衡条件下获得的系统，请清除 **Assume equilibrium operating conditions** 选项。在 **Offset value** 字段中指定以下之一：

  - 如果 `dx` 偏移值在调度空间中相同，请指定为长度等于状态数量的双精度向量。
  - 如果存在 `dx` 偏移且它们在调度空间中变化，请指定为大小为 *nx*-by-1-by-*N* 的双精度数组 — 当存在偏移且它们在调度空间中变化时使用。此处，*nx* 是状态数量，*N* 是时间快照数量。例如，如果您的模型有三个输入、两个输出和四个状态，并且在 10 个时间快照上进行调度，则数组大小必须为 4-by-1-by-10。使用 `size(sys)` 确定状态空间数组 `sys` 的大小。

#### 依赖关系

要启用此参数，请将 **Operating Point Offsets** 格式设置为 `Specify Offsets as double arrays` 并禁用 **Assume equilibrium operating conditions**。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `dxOffset` |
| **值：** | `"0"`（默认）| 带引号的数组名称 |

**示例：** `set_param(gcb,"dxOffset","dxOffArray")`

### **Struct array** — 偏移量结构体数组 `struct`（默认）| 结构体数组名称

模型偏移量，指定为具有以下字段的结构体。

| 字段 | 描述 |
| --- | --- |
| `u` | 输入偏移量 |
| `y` | 输出偏移量 |
| `x` | 状态偏移量 |
| `dx` | 状态导数偏移量 |

- 如果偏移量值在整个调度空间中相同，则指定为长度等于对应字段的输入、输出或状态数量的双精度向量。
- 如果偏移量在调度空间中变化，则为每个字段指定多维数组。例如，假设您的模型有三个输入、两个输出和四个状态。如果您使用 5×6 的工作点数组对模型进行线性化，则结构体数组大小必须为 5×6，并且每个条目必须包含一个向量，其长度等于对应字段的输入、输出或状态数量。

当您使用 `StoreOffsets` 选项设置为 `true` 进行线性化时，`linearize` (Simulink Control Design) 函数会在 `info.Offsets` 输出中以此格式返回偏移量。

#### 依赖关系

要启用此参数，请将 **Operating Point Offsets** 格式设置为 `Specify Offsets as struct array`

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `Offset` |
| **值：** | `"struct"`（默认）| 带引号的结构体数组名称 |

**示例：** `set_param(gcb,"Offset","OffsetStructName")`

### 固定条目选项卡

在某些情况下，您的 LTV 模型可能包含具有微小变化的系数。使用此选项卡上的参数，您可以指定哪些模型矩阵是固定的及其标称值，以覆盖模型数据中的条目。在某些情况下，您可能希望将时间相关矩阵（如 *A*(*t*)）替换为固定值 *A\** 用于仿真。例如，*A\** 可以表示调度范围内的平均值。默认情况下，模块使用 **State-space array** 数据来决定哪些条目是固定的以及哪些条目是变化的（出于性能原因，模块仅对变化的条目进行插值）。

使用此选项卡，您可以覆盖此默认行为，例如尝试简化 LTV 模型。例如，您可以确定 *A* 的第三个条目变化不大，并希望将其固定为其平均值。逻辑数组指定哪些条目应被视为固定，**Read values from** 指定这些固定条目使用哪个值。`false` 对应于不覆盖 LTI 数组数据，即依赖数据来决定此条目是固定还是变化。

### **Coefficients To Fix** — 状态空间矩阵的固定系数 `false` 或 `0`（默认）| `true` 或 `1` | 逻辑矩阵

将这些系数的位置指定为以下之一：

- 标量布尔值（`true` 或 `false`），如果矩阵的所有条目都以相同方式处理。

  状态空间矩阵和延迟向量的默认值为 `false`，这意味着它们被视为自由的。
- 与对应矩阵大小兼容的逻辑矩阵：

  | 状态空间矩阵 | 固定条目矩阵的大小 |
  | --- | --- |
  | **A matrix** | *nx*×*nx* |
  | **B matrix** | *nx*×*nu* |
  | **C matrix** | *ny*×*nx* |
  | **D matrix** | *ny*×*nu* |
  | **Input delay** | *nu*×1 |
  | **Output delay** | *ny*×1 |
  | **Internal delay** | *ni*×1 |

  其中，*nu* 是输入数量，*ny* 是输出数量，*nx* 是状态数量，*ni* 是内部延迟向量的长度。
- 用于指定固定条目位置的数值索引。有关如何为矩阵元素生成与给定下标 `(i,j)` 对应的数值索引的更多信息，请参阅 `sub2ind` 参考页。

指定位置后，使用 **Read values from** 参数提供固定系数的值。

### **Read values from** — 固定系数值的来源 `First model in state-space array`（默认）| `Custom state-space model`

为固定系数提供值的状态空间模型，指定为以下之一：

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

  固定系数取自模型 `sysFixed = sys(:,:,1)`，其对应于 `[alpha=1, beta=10]`。如果 `A` 矩阵的 (2,1) 项被强制为固定值，则仿真期间使用的值为 `sysFixed.A(2,1)`。
- `Custom state-space model` — 为固定项指定不同的状态空间模型。在 **Custom model** 字段中为固定模型指定一个变量。固定模型必须使用与 LPV 模型中的状态空间数组相同的状态基。

### Scheduling Tab

### **Interpolation method** — 插值方法 `Linear`（默认）| `Nearest` | `Flat`

插值方法。定义如何为位于其网格位置之外的调度参数值计算状态空间数据。

指定以下选项之一：

- `Flat` — 选择最接近但不大于当前点的网格点处的状态空间数据。*当前点* 是当前时刻调度参数的值。
- `Nearest` — 选择调度空间中最近的网格点处的状态空间数据。
- `Linear` — 通过对调度空间中最近的 2d 个邻居进行线性插值来获取状态空间数据，其中 d = 调度参数的数量。

对于调度参数值的规则网格，默认插值方案为 `Linear`。对于不规则网格，无论您做出何种选择，始终使用 `Nearest` 插值方案。要了解有关规则网格和不规则网格的更多信息，请参阅 Regular vs. Irregular Grids。

`Linear` 方法提供最高的精度，但计算时间更长。`Flat` 和 `Nearest` 方法适用于具有模式切换动态的模型。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `IMethod` |
| **值**：| `"Linear"`（默认）| `"Nearest"` | `"Flat"` |

**Example:** `set_param(gcb,"IMethod","Flat")`

### **Extrapolation method** — 外插方法 `Clip`（默认）| `Linear`

外插方法。定义如何为超出状态空间数组所提供范围（如 `SamplingGrid` 属性中所指定）的调度参数值计算状态空间数据。

指定以下选项之一：

- `Clip`（默认）— 禁用外插，并返回对应于最接近当前点的最后一个可用调度网格点的数据。
- `Linear` — 根据当前值分别小于第一个网格点值还是大于最后一个网格点值，为每个调度参数的第一对或最后一对值之间拟合一条直线。此方法返回该直线上对应于当前值的点。线性外插要求插值方案也是线性的。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `EMethod` |
| **值**：| `"Clip"`（默认）| `"Linear"` |

**Example:** `set_param(gcb,"EMethod","Linear")`

### **索引搜索方法** — 预查找算法 `Binary search`（默认）| `Linear search`

该模块使用预查找算法确定当前调度参数值在调度空间中的位置。选择 `Linear search` 或 `Binary search`。每种搜索方法在不同情况下各有速度优势。有关此参数的详细信息，请参阅 Prelookup (Simulink) 模块参考页。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `IndexSearch` |
| **值：** | `"Binary Search"`（默认）| `"Linear Search"` |

**示例：** `set_param(gcb,"IndexSearch","Linear Search")`

### **使用前一次索引结果开始索引搜索** — 从前一时间步开始搜索 `on`（默认）| `off`

当您希望模块使用前一时间步找到的索引开始搜索时，请选中此复选框。有关此参数的详细信息，请参阅 Prelookup (Simulink) 模块参考页。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `IndexBegin` |
| **值：** | `"on"`（默认）| `"off"` |

**示例：** `set_param(gcb,"IndexBegin","off")`

### 代码生成选项卡

### **模块数据类型（仅离散时间情况）** — 模块数据类型 `double`（默认）| `single`

模块数据类型，指定为 `double` 或 `single`。

#### 依赖关系

要启用此选项，请使用离散时间状态空间模型作为输入。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `DataType` |
| **值：** | `"double"`（默认）| `"single"` |

**示例：** `set_param(gcb,"DataType","single")`

### **延迟的初始缓冲区大小** — 初始缓冲区大小 `1024`（默认）| 大于 5 的正整数

为包含延迟的模型存储输入点数的初始内存分配。如果输入点数超过初始缓冲区大小，模块将分配额外内存。默认大小为 1024。

当您在 Accelerator 模式下运行模型或构建模型时，请确保初始缓冲区大小足够大，以处理模型中预期的最大延迟。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `InitBufferSize` |
| **值：** | `"1024"`（默认）| 带引号的大于 5 的正整数 |

**示例：** `set_param(gcb,"InitBufferSize","512")`

### **使用固定缓冲区大小** — 使用固定缓冲区大小 `off`（默认）| `on`

指定是否使用固定缓冲区大小来保存前一时间步的延迟输入和输出数据。对于包含输入或输出延迟的连续时间 LTV 系统，请使用此选项。如果缓冲区已满，新数据将替换缓冲区中已有的数据。软件使用线性外推来估计不在缓冲区中的输出值。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `FixedBuffer` |
| **值：** | `"off"`（默认）| `"on"` |

**示例：** `set_param(gcb,"FixedBuffer","on")`
## 所属库

Control System Toolbox / Linear Parameter Varying

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2024b：在模块输入端口外部指定初始条件

LTV System 模块现在允许您在模块输入端口 **IC** 处指定初始状态值。要启用此端口，请将 **Initial condition source** 参数设置为 `external`。

### R2024b：初始状态参数 `x0` 已重命名为 `InitialCondition`

初始状态参数 `x0` 现在称为 `InitialCondition`。如果您的代码以编程方式设置此参数，例如使用 `set_param(blockPath,"x0","[0 0.1]")`，请将代码更新为 `set_param(blockPath,"InitialCondition","[0 0.1]")`。

## 描述

仿真线性时变 (LTV) 系统

*线性时变* (LTV) 系统是一种线性状态空间模型，其动态特性随时间变化。在 MATLAB® 中，LTV 模型使用随时间变化的系数以状态空间形式表示。

在数学上，您可以将 LTV 系统表示如下。

dx(t)=dx0(t)+A(t)(x(t)−x0(t))+B(t)(u(t)−u0(t))y(t)=y0(t)+C(t)(x(t)−x0(t))+D(t)(u(t)−u0(t))x(0)=xinit

其中，

- *u*(*t*) 是输入
- *y*(*t*) 是输出
- *x*(*t*) 是模型状态，其初始值为 *xinit*
- dx(t) 对于连续时间系统是状态导数向量 x˙，对于离散时间系统是状态更新向量 *x*[*k*+1]。其中，*k* 是计算采样周期 *Ts* 数量的整数索引。
- *A*(*t*)、*B*(*t*)、*C*(*t*) 和 *D*(*t*) 是依赖于时间 *t* 的状态空间矩阵。
- *dx*0(*t*)、*x*0(*t*)、*u*0(*t*) 和 *y*0(*t*) 是在给定时间 *t* 处 dx(t)、*x*(*t*)、*u*(*t*) 和 *y*(*t*) 值的偏移量。

  您可以在调用诸如 `linearize` (Simulink Control Design) 或 `getIOTransfer` (Simulink Control Design) 等函数时，通过返回额外的线性化信息来获取这些偏移量。

该模块接受带有工作点信息的状态空间模型数组。该模块从 LTI 数组的 `SamplingGrid` 属性中提取时间依赖性信息，并从此工作空间中选取局部动态特性。该模块使用此数组以及数据插值和外推技术进行仿真。

您可以在调用诸如 `linearize` (Simulink Control Design) 或 `getIOTransfer` (Simulink Control Design) 等函数时，通过返回额外的线性化信息来获取这些偏移量。
