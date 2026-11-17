---
type: simulink-block
title: 'Integrator'
family: 'libsb2sl'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'DYN / CIntegrator'
documentation_page: 'integrator'
documentation_source_path: 'slref/integrator.html'
language: zh-CN
chinese_source: worker-translation
---

# Integrator

## 端口
```yaml
ports:
- name: Port_1
  summary: 要积分的信号 标量 | 向量 | 矩阵
  direction: input
  data_types: double
- name: External Reset
  summary: 用于将状态重置为初始条件的信号 标量 | 向量 | 矩阵
  direction: input
  data_types: Boolean
- name: x0
  summary: 初始条件 标量 | 向量 | 矩阵
  direction: input
  data_types: double
- name: Port_1
  summary: 积分后的信号 标量 | 向量 | 矩阵
  direction: output
  data_types: double
- name: Port_2
  summary: 输出饱和信号 标量 | 向量 | 矩阵
  direction: output
  data_types: double
- name: Port_3
  summary: 模块状态 标量 | 向量 | 矩阵
  direction: output
  data_types: double
```

### 输入

### **Port\_1** — 要积分的信号 标量 | 向量 | 矩阵

输入信号是此模块进行积分的实值标量、向量或矩阵。

此端口不具有直接馈通。

**数据类型：** `double`

### **External Reset** — 用于将状态重置为初始条件的信号 标量 | 向量 | 矩阵

外部重置信号是布尔标量、向量或矩阵，用于将模块状态重置为初始条件。请参阅 Resetting the State。

此端口具有直接馈通。

#### 依赖关系

要启用此端口，请选择 **External Reset**。

**数据类型：** `Boolean`

### **x0** — 初始条件 标量 | 向量 | 矩阵

初始条件信号是实值标量、向量或矩阵，用于设置模块的初始条件。

此端口具有直接馈通。

#### 依赖关系

要启用此端口，请将 **Initial Conditions** 参数设置为 `external`。

**数据类型：** `double`
### 输出

### **Port\_1** — 积分后的信号 标量 | 向量 | 矩阵

输出信号是标量、向量或矩阵，其值为积分后的输入信号的值。积分信号的维度与输入信号的维度匹配。

**数据类型：** `double`

### **Port\_2** — 输出饱和信号 标量 | 向量 | 矩阵

输出饱和信号是标量、向量或矩阵，用于指示模块状态中的每个元素何时受到上限或下限饱和限制的约束。信号值指示该值是否受到限制以及应用了哪个限制。

- `-1` — 值受下限饱和限制约束
- `0` — 值不受任一饱和限制约束
- `1` — 值受上限饱和限制约束

有关详细信息，请参阅 Limiting the Integral。

#### 依赖关系

要启用此端口，请选择 **Show saturation port**。

**数据类型：** `double`

### **Port\_3** — 模块状态 标量 | 向量 | 矩阵

模块状态信号是实值标量、向量或矩阵，其值与模块状态值匹配。

有关详细信息，请参阅 About the State Port。

#### 依赖关系

要启用此端口，请选择 **Show state port**。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: External reset
  summary: 将状态重置为其初始条件 none（默认）| rising | falling | either | level | level hold
  group: ''
  block_parameter: ExternalReset
  type: character vector , string
  values: '''none'' | ''rising'' | ''falling'' | ''either'' | ''level'' | ''level hold'''
  default: '''none'''
- name: Initial condition source
  summary: 使用外部信号设置初始条件的选项 internal（默认）| external
  group: ''
  block_parameter: InitialConditionSource
  type: character vector, string
  values: '''internal'' | ''external'''
  default: '''internal'''
- name: Initial condition
  summary: 初始状态 0（默认）| 实标量或数组
  group: ''
  block_parameter: InitialCondition
  type: scalar or vector
  default: '''0'''
- name: Limit output
  summary: 将模块输出值限制在指定范围内 off（Integrator 的默认值）| on（Integrator Limited 的默认值）
  group: ''
  block_parameter: LimitOutput
  type: character vector , string
  values: '''off'' | ''on'''
  default: '''off'''
- name: Upper saturation limit
  summary: 积分的上限 inf（默认）| 标量 | 向量 | 矩阵
  group: ''
  block_parameter: UpperSaturationLimit
  type: character vector, string
  values: scalar | vector | matrix
  default: '''inf'''
- name: Lower saturation limit
  summary: 积分的下限 -inf（默认）| 标量 | 向量 | 矩阵
  group: ''
  block_parameter: LowerSaturationLimit
  type: character vector , string
  values: scalar | vector | matrix
  default: '''-inf'''
- name: Wrap state
  summary: 启用状态环绕 off（默认）| on
  group: ''
  block_parameter: WrapState
  type: character vector, string
  values: '''off'' | ''on'''
  default: '''off'''
- name: Wrapped state upper value
  summary: 指定环绕状态的上限值 pi（默认）| 标量 | 向量
  group: ''
  block_parameter: WrappedStateUpperValue
  type: scalar or vector
  values: '''2*pi'''
  default: '''pi'''
- name: Wrapped state lower value
  summary: 指定环绕状态的下限值 -pi（默认）| 标量 | 向量
  group: ''
  block_parameter: WrappedStateLowerValue
  type: scalar or vector
  values: '''0'''
  default: '''-pi'''
- name: Show saturation port
  summary: 启用饱和输出端口 off（默认）| on
  group: ''
  block_parameter: ShowSaturationPort
  type: character vector , string
  values: '''off'' | ''on'''
  default: '''off'''
- name: Show state port
  summary: 启用状态输出端口 off（默认）| on
  group: ''
  block_parameter: ShowStatePort
  type: character vector , string
  values: '''off'' | ''on'''
  default: '''off'''
- name: Absolute tolerance
  summary: 模块状态的绝对容差 auto（默认）| 实标量或向量
  group: ''
  block_parameter: AbsoluteTolerance
  type: character vector, string, scalar, or vector
  values: '''auto'' | ''-1'' | any positive real scalar or vector'
  default: '''auto'''
- name: Ignore limit and reset when linearizing
  summary: 在线性化期间对模块使用默认重置和限制行为的选项 off（默认）| on
  group: ''
  block_parameter: IgnoreLimit
  type: character vector | string
  values: '''off'' | ''on'''
  default: '''off'''
- name: Enable zero-crossing detection
  summary: 启用零交叉检测 on（默认）| off
  group: ''
  block_parameter: ZeroCross
  type: character vector | string
  values: '''off'' | ''on'''
  default: '''on'''
- name: State Name (e.g., 'position')
  summary: 为每个状态分配唯一名称 ' '（默认）| 字符向量 | 字符串
  group: ''
  block_parameter: ContinuousStateAttributes
  type: character vector, string
  values: ''' '' | user-defined'
  default: ''' '''
```

### **External reset** — 将状态重置为其初始条件 `none`（默认）| `rising` | `falling` | `either` | `level` | `level hold`

指定用于外部重置信号的触发类型。

- 选择 `rising` 以在重置信号从负值或零值上升到正值，或从负值变为零值时重置状态。
- 选择 `falling` 以在重置信号从正值下降到零值或负值，或从零值变为负值时重置状态。
- 选择 `either` 以在重置信号从零变为非零值、从非零值变为零或改变符号时重置状态。
- 选择 `level` 以在重置信号在当前时间步为非零，或在前一时间步为非零而在当前时间步变为零时重置状态。
- 选择 `level hold` 以在重置信号在当前时间步为非零时重置状态。

#### 编程使用

|  |
| --- |
| **模块参数**：`ExternalReset` |
| **类型**：character vector , string |
| **值**：`'none'` | `'rising'` | `'falling'` | `'either'` | `'level'` | `'level hold'` |
| **默认值**：`'none'` |

### **Initial condition source** — 使用外部信号设置初始条件的选项 `internal`（默认）| `external`

选择初始条件的来源：

- `internal` — 从 **Initial condition** 参数获取状态的初始条件。
- `external` — 从外部信号获取状态的初始条件。选择此选项时，模块上会出现一个输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialConditionSource` |
| **类型**：character vector, string |
| **值**：`'internal'` | `'external'` |
| **默认值**：`'internal'` |

### **Initial condition** — 初始状态 0（默认）| 实标量或数组

设置 Integrator 模块的初始状态。

#### 提示

Simulink 软件不允许此模块的初始条件为 `inf` 或 `NaN`。

#### 依赖关系

将 **Initial condition source** 设置为 `internal` 会启用此参数。

将 **Initial condition source** 设置为 `external` 会禁用此参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialCondition` |
| **类型**：scalar or vector |
| **默认值**：`'0'` |

### **Limit output** — 将模块输出值限制在指定范围内 `off`（Integrator 的默认值）| `on`（Integrator Limited 的默认值）

将模块的输出限制在 **Lower saturation limit** 和 **Upper saturation limit** 参数之间的值。

- 选中此复选框会将模块输出限制在 **Lower saturation limit** 和 **Upper saturation limit** 参数之间的值。
- 清除此复选框不会限制模块输出值。

#### 依赖关系

选择此参数会启用 **Lower saturation limit** 和 **Upper saturation limit** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`LimitOutput` |
| **类型**：character vector , string |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Upper saturation limit** — 积分的上限 `inf`（默认）| 标量 | 向量 | 矩阵

将积分的上限指定为标量、向量或矩阵。您必须指定一个介于 **Output minimum** 和 **Output maximum** 参数值之间的值。

#### 依赖关系

要启用此参数，请选中 **Limit output** 复选框。

#### 编程使用

|  |
| --- |
| **模块参数**：`UpperSaturationLimit` |
| **类型**：character vector, string |
| **值**：scalar | vector | matrix |
| **默认值**：`'inf'` |

### **Lower saturation limit** — 积分的下限 `-inf`（默认）| 标量 | 向量 | 矩阵

将积分的下限指定为标量、向量或矩阵。您必须指定一个介于 **Output minimum** 和 **Output maximum** 参数值之间的值。

#### 依赖关系

要启用此参数，请选中 **Limit output** 复选框。

#### 编程使用

|  |
| --- |
| **模块参数**：`LowerSaturationLimit` |
| **类型**：character vector , string |
| **值**：scalar | vector | matrix |
| **默认值**：`'-inf'` |

### **Wrap state** — 启用状态环绕 `off`（默认）| `on`

在 **Wrapped state upper value** 和 **Wrapped state lower value** 参数之间启用状态环绕。启用状态环绕可消除对零交叉检测的需求，减少求解器重置，提高求解器性能和精度，并在对旋转和循环状态轨迹建模时增加仿真时间跨度。

如果将 **Wrapped state upper value** 指定为 `inf`，将 **Wrapped state lower value** 指定为 `-inf`，则不会发生环绕。

#### 依赖关系

选择此参数会启用 **Wrapped state upper value** 和 **Wrapped state lower value** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`WrapState` |
| **类型**：character vector, string |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Wrapped state upper value** — 指定环绕状态的上限值 `pi`（默认）| 标量 | 向量

模块输出的上限。

#### 依赖关系

选择 **Wrap state** 会启用此参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`WrappedStateUpperValue` |
| **类型**：scalar or vector |
| **值**：`'2*pi'` |
| **默认值**：`'pi'` |

### **Wrapped state lower value** — 指定环绕状态的下限值 `-pi`（默认）| 标量 | 向量

模块输出的下限。

#### 依赖关系

选择 **Wrap state** 会启用此参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`WrappedStateLowerValue` |
| **类型**：scalar or vector |
| **值**：`'0'` |
| **默认值**：`'-pi'` |

### **Show saturation port** — 启用饱和输出端口 `off`（默认）| `on`

选中此复选框可向模块添加饱和输出端口。清除此复选框时，模块没有饱和输出端口。

#### 依赖关系

选择此参数会启用饱和输出端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`ShowSaturationPort` |
| **类型**：character vector , string |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Show state port** — 启用状态输出端口 `off`（默认）| `on`

选中此复选框可向模块添加状态输出端口。清除此复选框时，模块没有状态输出端口。

#### 依赖关系

选择此参数会启用状态输出端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`ShowStatePort` |
| **类型**：character vector , string |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Absolute tolerance** — 模块状态的绝对容差 `auto`（默认）| 实标量或向量

- 如果输入 `auto` 或 –1，则 Simulink 使用 Configuration Parameters 对话框中的绝对容差值（请参阅 Solver Pane）来计算模块状态。
- 如果输入实标量，则该值将覆盖 Configuration Parameters 对话框中的绝对容差，用于计算所有模块状态。
- 如果输入实向量，则该向量的维度必须与模块中连续状态的维度匹配。这些值将覆盖 Configuration Parameters 对话框中的绝对容差。

#### 编程使用

|  |
| --- |
| **模块参数**：`AbsoluteTolerance` |
| **类型**：character vector, string, scalar, or vector |
| **值**：`'auto'` | `'-1'` | any positive real scalar or vector |
| **默认值**：`'auto'` |

### **Ignore limit and reset when linearizing** — 在线性化期间对模块使用默认重置和限制行为的选项 `off`（默认）| `on`

选中此参数时，软件在线性化期间忽略此模块的重置和限制参数，并对这些参数使用默认值。

#### 提示

当您希望围绕导致积分器重置或饱和的工作点对模型进行线性化时，请启用此参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`IgnoreLimit` |
| **类型**：character vector | string |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Enable zero-crossing detection** — 启用零交叉检测 `on`（默认）| `off`

选择以启用零交叉检测。有关详细信息，请参阅 Zero-Crossing Detection。

#### 编程使用

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：character vector | string |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

### **State Name (e.g., 'position')** — 为每个状态分配唯一名称 `' '`（默认）| 字符向量 | 字符串

- 要为单个状态分配名称，请在引号之间输入名称，例如 `'velocity'`。
- 要为多个状态分配名称，请输入用花括号括起来的逗号分隔列表，例如 `{'a', 'b', 'c'}`。每个名称必须唯一。
- 状态名称仅适用于所选模块。
- 状态数必须能被状态名称数整除。
- 您可以指定的名称数少于状态数，但不能指定的名称数多于状态数。

  例如，您可以在具有四个状态的系统中指定两个名称。第一个名称适用于前两个状态，第二个名称适用于后两个状态。
- 要使用 MATLAB® 工作区中的变量分配状态名称，请输入不带引号的变量。变量可以是字符向量、字符串、元胞数组或结构体。

#### 编程使用

|  |
| --- |
| **模块参数**：`ContinuousStateAttributes` |
| **类型**：character vector, string |
| **值**：`' '` | user-defined |
| **默认值**：`' '` |
## 所属库

Simulink / Commonly Used Blocks Simulink / Continuous

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `noa` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |
|  |  |
| --- | --- |
| a 此模块的端口具有不同的直接馈通特性。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

- 考虑对模型进行离散化
- 不建议用于生产代码

## 版本历史

**在 R2006a 之前推出**

## 描述

对信号进行积分

Integrator 模块对输入信号关于时间进行积分，并将结果作为输出信号提供。

Simulink® 将 Integrator 模块视为具有一个状态的动态系统。模块动态由以下方程给出：

{x˙(t)=u(t)y(t)=x(t)   x(t0)=x0

其中：

- *u* 是模块输入。
- *y* 是模块输出。
- *x* 是模块状态。
- *x0* 是 *x* 的初始条件。

虽然这些方程定义了连续时间中的精确关系，但 Simulink 使用数值近似方法以有限精度对其进行求值。Simulink 可以使用多种不同的数值积分方法来计算模块的输出，每种方法在特定应用中各有优势。使用 Configuration Parameters 对话框的 **Solver** 窗格（请参阅 Solver Pane）选择最适合您的应用的技术。

所选求解器使用当前输入值和前一时间步的状态值，在当前时间步计算 Integrator 模块的输出。为支持此计算模型，Integrator 模块保存其在当前时间步的输出，以供求解器在下一时间步计算其输出时使用。该模块还向求解器提供初始条件，用于在仿真开始时计算模块的初始状态。初始条件的默认值为 0。使用模块参数对话框为初始条件指定另一个值，或在模块上创建初始值输入端口。

使用参数对话框可以：

- 定义积分的上限和下限
- 创建一个输入，根据输入的变化方式将模块的输出（状态）重置为其初始值
- 创建一个可选的状态输出，以便模块输出的值可以触发模块重置

使用 Discrete-Time Integrator 模块创建纯离散系统。

### 定义初始条件

您可以将初始条件定义为模块对话框上的参数，或从外部信号输入它们：

- 要将初始条件定义为模块参数，请将 **Initial condition source** 参数指定为 `internal`，并在 **Initial condition** 字段中输入值。
- 要从外部源提供初始条件，请将 **Initial condition source** 参数设置为 `external`。模块上会出现一个额外的输入端口。

  配置了初始条件端口的 Integrator 模块具有两个输入端口和一个输出端口。

  **注意**

  如果选择 **Limit output** 参数，则初始条件必须在饱和限制之内。如果初始条件不在模块饱和限制之内，模块将显示错误消息。

### 限制积分

要将输出信号限制在指定的值范围内，请选择 **Limit output** 并指定饱和限值。当输出达到其中一个限值时，积分作用被禁用，以防止积分饱和。在仿真期间，您可以更改限值，但不能更改输出是否受限。该模块使用以下准则确定输出信号值：

- 当积分值小于或等于饱和下限时，输出信号值为饱和下限。
- 当积分值介于饱和下限和饱和上限之间时，输出为积分值。
- 当积分值大于或等于饱和上限时，输出信号值为饱和上限。

要生成一个指示状态何时受饱和限值限制的信号，请选择 **Show saturation port**。模块上会出现第二个输出端口。

一个配置为限制输出并显示饱和端口的 Integrator 模块。该模块有两个输出信号：第一个标记为 Output，第二个标记为 Saturation。

饱和信号具有以下三个值之一：

- `1` — 状态受饱和上限限制
- `0` — 状态不受限制
- `–1` — 状态受饱和下限限制

当您限制 Integrator 模块输出时，该模块具有三个过零信号：一个用于检测积分值何时超过饱和上限，一个用于检测积分值何时小于饱和下限，还有一个用于检测积分值何时从饱和变为不饱和。

**注意**

默认情况下，Integrator Limited 模块的 **Limit output** 参数处于启用状态，**Upper saturation limit** 参数值设置为 `1`，**Lower saturation limit** 参数值设置为 `0`。

### 环绕循环状态

若干物理现象，例如振荡器和表现旋转运动的机械，在本质上是循环的、周期的或旋转的。在 Simulink 框图中对这些现象进行建模，涉及对周期或循环信号的变化率进行积分，以获得运动状态。在较长的仿真时间跨度内，这种方法可能导致表示周期或循环信号的状态积分到很大的值。对于这些信号计算三角函数值（例如正弦或余弦）时，由于角度缩减，随着值变大，计算时间会更长。随着信号值变大，求解器性能和精度会下降。

克服这一缺点的一种方法是在角度状态达到 2π 时将其重置为 `0`（或者为了数值对称性，在达到 π 时重置为 –π）。这种方法提高了正弦和余弦计算的精度，并减少了角度缩减时间。但它也需要过零检测，并引入求解器重置，这会减慢变步长求解器的仿真速度，尤其是在大型模型中。

为了消除环绕点处的求解器重置，Integrator 模块支持环绕状态，您可以通过在模块参数对话框中选中 **Wrap state** 来启用它。当您启用 **Wrap state** 时，模块图标会发生变化，以指示该模块具有环绕状态。

一个配置为环绕状态值的 Integrator 模块。模块图标上标注有一个带箭头的圆圈。

Integrator 模块支持由环绕状态的上限值和下限值参数限定的环绕状态。确定环绕状态的算法如下：

y={xx∈[xl,xu)x−(xu−xl)⌊x−xlxu−xl⌋otherwise

其中：

- *xl* 是环绕状态的下限值。
- *xu* 是环绕状态的上限值。
- *y* 是输出。

对环绕状态的支持提供了以下优势。

- 当您的模型接近大角度和大状态值时，它消除了仿真不稳定性。
- 它减少了仿真期间求解器重置的次数，并消除了对过零检测的需求，从而缩短了仿真时间。
- 它消除了大角度值，加快了角度状态上三角函数的计算速度。
- 它提高了求解器精度和性能，并支持无限仿真时间。

### 重置状态

该模块可以基于外部信号将其状态重置为指定的初始条件。要使模块重置其状态，请选择 **External reset** 选项之一。触发端口会出现在模块输入端口下方，并指示触发类型。

一个配置为重置状态的 Integrator 模块。该模块有两个输入信号，标记为 Input 和 Reset，以及一个输出信号，标记为 Output。

- 选择 `rising`，当重置信号从负值或零上升到正值时重置状态。
- 选择 `falling`，当重置信号从正值下降到零或负值时重置状态。
- 选择 `either`，当重置信号从零变为非零值、从非零值变为零或改变符号时重置状态。
- 选择 `level`，当重置信号在当前时间步为非零，或从前一时间步的非零变为当前时间步的零时重置状态。
- 选择 `level hold`，当重置信号在当前时间步为非零时重置状态。

重置端口具有直接馈通。如果模块输出直接反馈到该端口，或通过一系列具有直接馈通的模块反馈到该端口，则会产生代数环（请参阅代数环概念）。使用 Integrator 模块的状态端口反馈模块输出，而不会产生代数环。

**注意**

为了符合汽车工业软件可靠性协会（MISRA™）软件标准，您的模型必须使用布尔信号来驱动 Integrator 模块的外部重置端口。

### 关于状态端口

在 Integrator 模块的参数对话框中选中 **Show state port** 复选框，会导致一个附加输出端口（状态端口）出现在 Integrator 模块的顶部。

一个配置为显示状态端口的 Integrator 模块。该模块有一个输入信号，标记为 Input，以及两个输出信号。状态输出端口位于模块顶部，提供输出信号值的端口位于模块右侧。

状态端口的输出与模块标准输出端口的输出相同，但以下情况除外。如果模块在当前时间步被重置，则状态端口的输出是如果模块未被重置时本应出现在模块标准输出处的值。状态端口的输出在时间步中出现的时间早于 Integrator 模块输出端口的输出。在这些建模场景中使用状态端口以避免产生代数环：

- 使用自重置积分器的系统
- 将状态从一个使能子系统传递到另一个使能子系统

  **注意**

  更新模型时，Simulink 会检查状态端口是否适用于这两种场景之一。如果不适用，则会出现错误消息。此外，您无法在 Accelerator 模式下执行的引用模型中记录此端口的输出。如果为该端口启用了记录，Simulink 会在执行引用模型期间生成“signal not found”警告。

### 指定模块输出的绝对容差

默认情况下，Simulink 软件使用 Configuration Parameters 对话框中指定的绝对容差值（请参阅变步长求解器的误差容限）来计算 Integrator 模块的输出。如果该值不能提供足够的误差控制，请在 Integrator 模块对话框的 **Absolute tolerance** 字段中指定更合适的值。您指定的值用于计算所有模块输出。
