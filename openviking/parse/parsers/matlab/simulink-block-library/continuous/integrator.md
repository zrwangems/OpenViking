---
type: simulink-block
title: 'Integrator'
family: continuous
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Continuous'
documentation_page: 'integrator'
---

# Integrator

Integrate signal

## 中文

对信号求积分

### 所属库

Simulink / Commonly Used Blocks Simulink / Continuous

### 描述

Integrator 模块求输入信号关于时间的积分，并将结果作为输出信号。

Simulink® 将 Integrator 模块作为具有一种状态的动态系统进行处理。模块动态由以下方程指定：

{x˙(t)=u(t)y(t)=x(t)   x(t0)=x0

，其中：

- *u* 是模块输入。
- *y* 是模块输出。
- *x* 是模块状态。
- *x0* 是 *x* 的初始条件。

虽然这些方程定义了连续时间下的准确关系，但 Simulink 使用数值逼近方法以有限精度来进行计算。Simulink 可以使用若干不同的数值积分方法来计算模块的输出，每种方法都在特定的应用中各具优势。使用“配置参数”对话框的**求解器**窗格（请参阅求解器窗格）可以选择最适合您的应用的方法。

所选求解器会使用当前输入值和前一个时间步的状态值计算 Integrator 模块在当前时间步的输出。为支持此计算模型，Integrator 模块会保存在当前时间步的输出，以供求解器计算其在下一个时间步的输出。该模块还为求解器提供了初始条件，用于计算该模块在仿真开始时的初始状态。初始条件的默认值为 0。使用模块参数对话框可以为初始条件指定其他值，或在模块上创建初始值输入端口。

使用参数对话框可以：

- 定义积分的上限和下限
- 创建可将模块的输出（状态）重置为初始值的输入，具体取决于输入的变化方式。
- 创建可选的状态输出，以便模块的输出值可以触发模块重置

使用 Discrete-Time Integrator 模块可以创建纯离散系统。

#### 定义初始条件

可以在模块对话框上将初始条件定义为参数，或者从外部信号输入初始条件：

- 要将初始条件定义为模块参数，请将**初始条件来源**参数指定为**内部**并在**初始条件**字段中输入值。
- 要从外部源提供初始条件，请将**初始条件来源**参数设置为**外部**。模块上出现一个额外的输入端口。

  An Integrator block configured with an initial condition port has two input ports and one output port.

  **注意**

  如果选择**限制输出**参数，初始条件必须在饱和界限内。如果初始条件不在模块饱和界限范围内，该模块会显示错误消息。

#### 限制积分

要将输出信号限制在指定的值范围内，请选择**限制输出**并指定饱和界限。当输出达到其中一个限值时，积分作用被禁用以防止积分饱和。在仿真期间，您可以更改限制，但不能更改是否限制输出。该模块按照以下准则确定输出信号值：

- 当积分值小于或等于饱和下限时，输出信号值为饱和下限。
- 当积分值在饱和下限与饱和上限之间时，输出为积分值。
- 当积分值大于或等于饱和上限时，输出信号值为饱和上限。

要生成指示状态何时受饱和界限限制的信号，请选择**显示饱和端口**。第二个输出端口出现在模块上。

An Integrator block configured to limit the output and show the saturation port. The block has two output signals: the first is labeled Output and the second is labeled Saturation.

饱和信号具有以下三个值之一：

- `1` - 状态受饱和上限限制
- `0` - 状态不受限制
- `–1` - 状态受饱和下限限制

当限制 Integrator 模块输出时，该模块有三个过零信号：一个用于检测积分值何时超出饱和上限，一个用于检测积分值何时小于饱和下限，一个用于检测积分值何时从饱和变为不饱和。

**注意**

默认情况下，为 Integrator Limited 模块启用**限制输出**参数，其中**饱和上限**参数值设置为 `1`，**饱和下限**参数值设置为 `0`。

#### 绕回循环状态

一些物理现象，如振荡器和展示旋转运动的机器，本质上是循环的、周期的或旋转的。在 Simulink 模块图中对这些现象进行建模时，需要对周期或循环信号的变化率进行积分以获取运动状态。在长仿真时间跨度上，这种方法可以导致表示周期性或循环信号的状态会积分为很大的值。计算这些信号的三角值（如正弦或余弦）需要更长时间，因为这些值会因角度减小而变大。随着信号值变大，求解器的性能和准确性会下降。

克服这一缺点的一种方法是在角状态达到 2π 时将其重置为 `0`（或者在其达到 π 时重置为 –π，以确保数值对称）。此方法可改进正弦和余弦计算的准确性，并缩短角度减小时间。但该方法还需要过零检测，并引入了求解器重置，这会减慢变步长求解器的仿真，尤其是在大型模型中。

为消除绕回点处的求解器重置，Integrator 模块支持绕回状态，您可以通过在模块参数对话框上选中**绕回状态**来启用这些状态。当启用**绕回状态**时，模块图标将更改为指示该模块具有绕回状态。

An Integrator block configured to wrap state values. The block icon is annotated with a circle with arrows.

Integrator 模块支持以绕回状态上限和下限值参数为边界的绕回状态。下面的方程给出了确定绕回状态的算法：

y={xx∈[xl,xu)x−(xu−xl)⌊x−xlxu−xl⌋otherwise

其中：

- *xl* 是绕回状态的下限值。
- *xu* 是绕回状态的上限值。
- *y* 是输出。

支持绕回状态具有以下优势。

- 消除当模型接近大角度和大状态值时的仿真不稳定性。
- 减少仿真期间的求解器重置次数并消除对过零检测的需求，从而改善仿真时间。
- 消除大角度值，从而加速针对角状态的三角函数计算。
- 提高求解器的准确性和性能，并支持无限制仿真时间。

#### 重置状态

模块可以根据外部信号将其状态重置为指定的初始条件。要使模块重置其状态，请选中其中一个**外部重置**选项。模块输入端口下方将显示一个触发端口，并指示触发类型。

An integrator block configured to reset the state. The block has two input signals, labeled Input and Reset, and one output signal, labeled Output.

- 选择**上升沿**可在重置信号从负值或零上升到正值时重置状态。
- 选择**下降沿**可在重置信号从正值下降到零或负值时重置状态。
- 选择**任一沿**可在重置信号从零变为非零值、从非零值变为零或改变符号时重置状态。
- 选择**电平**可于重置信号在当前时间步为非零值时或者从上一个时间步的非零值更改为当前时间步的零值时重置状态。
- 选择**电平保持**可于重置信号在当前时间步为非零值时重置状态。

重置端口具有直接馈通。如果模块输出直接或通过一系列带直接馈通的模块反馈到此端口中，则会产生代数环（请参阅代数环概念）。使用 Integrator 模块的状态端口可以反馈该模块的输出，而不会创建代数环。

**注意**

为了符合汽车工业软件可靠性协会 (MISRA™) 软件标准，您的模型必须使用布尔信号来驱动 Integrator 模块的外部重置端口。

#### 关于状态端口

在 Integrator 模块的参数对话框上选中**显示状态端口**复选框会导致 Integrator 模块的顶部显示一个附加输出端口，即状态端口。

An integrator block configured to show the state port. The block has one input signal, labeled Input, and two output signals. The state output port is on the top of the block, and the port that provides the output signal value is on the right of the block.

状态端口的输出与模块的标准输出端口的输出相同，但以下情况除外。如果在当前时间步重置模块，则状态端口的输出为模块尚未重置时在模块的标准输出中显示的值。状态端口的输出在时间步中的显示会早于 Integrator 模块输出端口的输出的显示。使用状态端口可以避免以下建模场景中出现代数环：

- 使用自重置积分器的系统
- 将状态从一个使能子系统传递给另一个

  **注意**

  当更新模型时，Simulink 会检查状态端口是否适用于这两个场景中的一个。如果不适用，会显示错误消息。此外，不能将此端口的输出记录在于加速模式下执行的引用模型中。如果为该端口启用记录，Simulink 将在执行引用模型期间生成“signal not found”警告。

#### 指定模块输出的绝对容差

默认情况下，Simulink 软件会使用在“配置参数”对话框中指定的绝对容差值（请参阅Error Tolerances for Variable-Step Solvers）来计算 Integrator 模块的输出。如果此值未提供足够的误差控制，则请在 Integrator 模块对话框的**绝对容差**字段中指定更合适的值。您指定的值将用于计算所有模块输出。

### 端口

#### 输入

#### **Port\_1** — 要积分的信号 标量 | 向量 | 矩阵

输入信号是此模块积分的实数值标量、向量或矩阵。

此端口没有直接馈通。

**数据类型:** `double`

#### **External Reset** — 将状态重置为初始条件的信号 标量 | 向量 | 矩阵

外部重置信号是布尔标量、向量或矩阵，用于将模块状态重置为初始条件。请参阅重置状态。

此端口具有直接馈通。

##### 依赖关系

要启用此端口，请选择**外部重置**。

**数据类型:** `Boolean`

#### **x0** — 初始条件 标量 | 向量 | 矩阵

初始条件信号是为模块设置初始条件的实数值标量、向量或矩阵。

此端口具有直接馈通。

##### 依赖关系

要启用此端口，请将**初始条件**参数设置为**外部**。

**数据类型:** `double`
#### 输出

#### **Port\_1** — 对信号求积分 标量 | 向量 | 矩阵

输出信号是具有积分输入信号值的标量、向量或矩阵。积分信号的维度与输入信号的维度匹配。

**数据类型:** `double`

#### **Port\_2** — 输出饱和信号 标量 | 向量 | 矩阵

输出饱和信号是标量、向量或矩阵，它指示处于模块状态的每个元素何时受到饱和上限或下限的限制。信号值指示该值是否受限以及应用哪个限制。

- `-1` - 值受饱和下限限制
- `0` - 值不受任一饱和界限限制
- `1` - 值受饱和上限制

有关详细信息，请参阅限制积分。

##### 依赖关系

要启用此端口，请选择**显示饱和端口**。

**数据类型:** `double`

#### **Port\_3** — 模块状态 标量 | 向量 | 矩阵

模块状态信号是具有与模块状态值匹配的值的实数值标量、向量或矩阵。

有关详细信息，请参阅关于状态端口。

##### 依赖关系

要启用此端口，请选择**显示状态端口**。

**数据类型:** `double`

### 参数

#### **外部重置** — 将状态重置为其初始条件 **无** (默认) | **上升沿** | **下降沿** | **任一沿** | **电平** | **电平保持**

指定用于外部重置信号的触发类型。

- 选择**上升沿**可在重置信号从负值或零上升到正值或者从负值上升到零值时重置状态。
- 选择**下降沿**可在重置信号从正值下降到零或负值或者从零值下降到负值时重置状态。
- 选择**任一沿**可在重置信号从零变为非零值、从非零值变为零或改变符号时重置状态。
- 选择**电平**可于重置信号在当前时间步为非零值时或者从上一个时间步的非零值更改为当前时间步的零值时重置状态。
- 选择**电平保持**可于重置信号在当前时间步为非零值时重置状态。

##### 编程用法

|  |
| --- |
| **模块参数：**`ExternalReset` |
| **类型：**字符向量、字符串 |
| **值：**`'none'` | `'rising'` | `'falling'` | `'either'` | `'level'` | `'level hold'` |
| **默认值：**`'none'` |

#### **初始条件来源** — 使用外部信号设置初始条件的选项 **内部** (默认) | **外部**

选择初始条件的来源：

- **内部** - 从**初始条件**参数获取状态的初始条件。
- **外部** - 从外部信号获取状态的初始条件。选择此选项时，输入端口会出现在模块上。

##### 编程用法

|  |
| --- |
| **模块参数：**`InitialConditionSource` |
| **类型：**字符向量、字符串 |
| **值：**`'internal'` | `'external'` |
| **默认值：**`'internal'` |

#### **初始条件** — 初始状态 0 (默认) | 实数标量或数组

设置 Integrator 模块的初始状态。

##### 提示

Simulink 软件不允许此模块的初始条件为 `inf` 或 `NaN`。

##### 依赖关系

将**初始条件来源**设置为 `internal` 将启用此参数。

将**初始条件来源**设置为 `external` 将禁用此参数。

##### 编程用法

|  |
| --- |
| **模块参数：**`InitialCondition` |
| **类型：**标量或向量 |
| **默认值：**`'0'` |

#### **限制输出** — 将模块输出值限制在指定范围内 `off`（Integrator 的默认值） | `on`（Integrator Limited 的默认值）

将模块的输出限制为介于**饱和下限**和**饱和上限**参数之间的值。

- 选中此复选框会将模块输出限制为介于**饱和下限**和**饱和上限**参数之间的值。
- 清除此复选框后，不会限制模块的输出值。

##### 依赖关系

选择此参数将启用**饱和下限**和**饱和上限**参数。

##### 编程用法

|  |
| --- |
| **模块参数：**`LimitOutput` |
| **类型：**字符向量、字符串 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

#### **饱和上限** — 指定积分的上限 `inf` (默认) | 标量 | 向量 | 矩阵

将积分的上限指定为标量、向量或矩阵。您必须指定在**输出最小值**和**输出最大值**参数值之间的值。

##### 依赖关系

要启用此参数，请选中**限制输出**复选框。

##### 编程用法

|  |
| --- |
| **模块参数：**`UpperSaturationLimit` |
| **类型：**字符向量、字符串 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值：**`'inf'` |

#### **饱和下限** — 指定积分的下限 `-inf` (默认) | 标量 | 向量 | 矩阵

将积分的下限指定为标量、向量或矩阵。您必须指定在**输出最小值**和**输出最大值**参数值之间的值。

##### 依赖关系

要启用此参数，请选中**限制输出**复选框。

##### 编程用法

|  |
| --- |
| **模块参数：**`LowerSaturationLimit` |
| **类型：**字符向量、字符串 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值：**`'-inf'` |

#### **绕回状态** — 启用状态绕回 `off` (默认) | `on`

在**绕回状态上限值**和**绕回状态下限值**参数之间启用状态绕回。启用绕回状态可在对旋转和循环状态轨迹建模时消除对过零检测的需求，减少求解器重置，提高求解器性能和准确性，并增加仿真时间范围。

如果将**绕回状态上限值**指定为 `inf` 并将**绕回状态下限值**指定为 `-inf`，则不会发生绕回。

##### 依赖关系

选择此参数将启用**绕回状态上限值**和**绕回状态下限值**参数。

##### 编程用法

|  |
| --- |
| **模块参数：**`WrapState` |
| **类型：**字符向量、字符串 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

#### **绕回状态上限值** — 指定绕回状态的上限值 `pi` (默认) | 标量 | 向量

模块输出的上限。

##### 依赖关系

选择**绕回状态**会启用此参数。

##### 编程用法

|  |
| --- |
| **模块参数：**`WrappedStateUpperValue` |
| **类型：**标量或向量 |
| **值：**`'2*pi'` |
| **默认值：**`'pi'` |

#### **绕回状态下限值** — 指定绕回状态的下限值 `-pi` (默认) | 标量 | 向量

模块输出的下限。

##### 依赖关系

选择**绕回状态**会启用此参数。

##### 编程用法

|  |
| --- |
| **模块参数：**`WrappedStateLowerValue` |
| **类型：**标量或向量 |
| **值：**`'0'` |
| **默认值：**`'-pi'` |

#### **显示饱和端口** — 启用饱和输出端口 `off` (默认) | `on`

选中此复选框可将饱和输出端口添加到模块中。清除此复选框时，模块没有饱和输出端口。

##### 依赖关系

选择此参数将启用饱和输出端口。

##### 编程用法

|  |
| --- |
| **模块参数：**`ShowSaturationPort` |
| **类型：**字符向量、字符串 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

#### **显示状态端口** — 启用状态输出端口 `off` (默认) | `on`

选中此复选框可将状态输出端口添加到模块中。清除此复选框时，模块没有状态输出端口。

##### 依赖关系

选择此参数将启用状态输出端口。

##### 编程用法

|  |
| --- |
| **模块参数：**`ShowStatePort` |
| **类型：**字符向量、字符串 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

#### **绝对容差** — 模块状态的绝对容差 `auto` (默认) | 实数标量或向量

- 如果输入 `auto` 或 -1，则 Simulink 会使用“配置参数”对话框中的绝对容差值（请参阅求解器窗格）来计算模块状态。
- 如果输入实数标量，则在计算所有模块状态时，该值会覆盖“配置参数”对话框中的绝对容差。
- 如果输入实数向量，则该向量的维度必须匹配模块中连续状态的维度。这些值将覆盖“配置参数”对话框中的绝对容差。

##### 编程用法

|  |
| --- |
| **模块参数：**`AbsoluteTolerance` |
| **类型：**字符向量、字符串、标量或向量 |
| **值：**`'auto'` | `'-1'` | 任何正实数标量或向量 |
| **默认值：** `'auto'` |

#### **线性化时忽略限制和重置** — 线性化期间使用模块默认重置和限制行为的选项 `off` (默认) | `on`

当您选择此参数时，软件会在线性化期间忽略此模块的重置和限制参数，并使用这些参数的默认值。

##### 提示

当您要在导致积分器重置或饱和工作点附近线性化模型时，请启用此参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`IgnoreLimit` |
| **类型：**字符向量 | 字符串 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

#### **启用过零检测** — 启用过零检测 `on` (默认) | `off`

选择此项以启用过零检测。有关详细信息，请参阅过零检测。

##### 编程用法

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：字符向量 | 字符串 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

#### **状态名称(例如，'position')** — 为每个状态指定唯一名称 `' '` (默认) | 字符向量 | 字符串

- 要为单个状态分配名称，请输入名称并用引号引起来，例如 `'velocity'`。
- 要为多个状态分配名称，请输入以逗号分隔的列表并用花括号括起来，例如 `{'a', 'b', 'c'}`。每个名称都必须是唯一的。
- 状态名称只会应用于所选模块。
- 状态数量必须能够被状态名称的数量均分。
- 指定的名称数量可以少于状态数量，但不能多于状态数量。

  例如，可以在具有四个状态的系统中指定两个名称。第一个名称应用于前两个状态，第二个名称应用于后两个状态。
- 要在 MATLAB® 工作区中分配带变量的状态名称，请输入不带引号的变量。变量可以是字符向量、字符串、元胞数组或结构体。

##### 编程用法

|  |
| --- |
| **模块参数：**`ContinuousStateAttributes` |
| **类型：**字符向量、字符串 |
| **值：**`' '` | 用户定义 |
| **默认值：**`' '` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `否a` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `是` |
|  |  |
| --- | --- |
| a 此模块的端口具有不同的直接馈通特性。 | |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

- 考虑离散模型
- 不建议用于生产代码

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Commonly Used Blocks Simulink / Continuous

## Description

The Integrator block integrates an input signal with respect to time
and provides the result as an output signal.

Simulink® treats the Integrator block as a dynamic system with one state.
The block dynamics are given by:

{x˙(t)=u(t)y(t)=x(t)   x(t0)=x0

where:

- *u* is the block input.
- *y* is the block output.
- *x* is the block state.
- *x0* is the initial condition of
  *x*.

While these equations define an exact relationship in continuous time, Simulink uses numerical approximation methods to evaluate them with finite
precision. Simulink can use several different numerical integration methods to compute
the output of the block, each with advantages in particular applications. Use the **Solver** pane of the Configuration Parameters dialog box (see Solver Pane) to select the technique best suited to your application.

The selected solver computes the output of the Integrator block at the
current time step, using the current input value and the value of the state at the previous
time step. To support this computational model, the Integrator block saves
its output at the current time step for use by the solver to compute its output at the next
time step. The block also provides the solver with an initial condition for use in computing
the block's initial state at the beginning of a simulation. The default value of the initial
condition is 0. Use the block parameter dialog box to specify another value for the initial
condition or create an initial value input port on the block.

Use the parameter dialog box to:

- Define upper and lower limits on the integral
- Create an input that resets the block's output (state) to its initial value,
  depending on how the input changes
- Create an optional state output so that the value of the block's output can
  trigger a block reset

Use the Discrete-Time Integrator block to create a purely discrete
system.

### Defining Initial Conditions

You can define the initial conditions as a parameter on the block dialog box or input them from an external signal:

- To define the initial conditions as a block parameter, specify the **Initial condition source** parameter as `internal` and enter the value in the **Initial condition** field.
- To provide the initial conditions from an external source, set the
  **Initial condition source** parameter to
  `external`. An additional input port appears on the
  block.

  An Integrator block configured with an initial condition port has two input ports and one output port.

  **Note**

  If you select the **Limit output** parameter, the initial
  condition must be within the saturation limits. If the initial condition is not
  within the block saturation limits, the block displays an error message.

### Limiting the Integral

To limit the output signal to a specified range of values, select **Limit
output** and specify the saturation limits. When the output reaches one of the
limits, the integral action is disabled to prevent integral wind up. During a simulation,
you can change the limits but not whether the output is limited. The block determines output
signal value using these criteria:

- When the integral value is less than or equal to the lower saturation limit, the
  output signal value is the lower saturation limit.
- When the integral value is between the lower saturation limit and the upper
  saturation limit, the output is the integral value.
- When the integral value is greater than or equal to the upper saturation limit,
  the output signal value is the upper saturation limit.

To generate a signal that indicates when the state is limited by the saturation limits, select
**Show saturation port**. A second output port appears on the
block.

An Integrator block configured to limit the output and show the saturation port. The block has two output signals: the first is labeled Output and the second is labeled Saturation.

The saturation signal has one of three values:

- `1` — State limited by upper saturation limit
- `0` — State not limited
- `–1` — State limited by lower saturation limit

When you limit the Integrator block output, the block has three zero crossing
signals: one to detect when the integral value exceeds the upper saturation limit, one to
detect when the integral value is less than the lower saturation limit, and one to detect
when the integral value changes from being saturated to not being saturated.

**Note**

By default, the **Limit output** parameter is enabled for the
Integrator Limited block, with the **Upper saturation
limit** parameter value set to `1`, and the
**Lower saturation limit** parameter value set to
`0`.

### Wrapping Cyclic States

Several physical phenomena, such as oscillators and machinery that exhibits rotational
movement, are cyclic, periodic, or rotary in nature. Modeling these phenomena in a
Simulink block diagram involves integrating the rate of change for the periodic or
cyclic signals to obtain the state of the movement. Over long simulation time spans, this
approach can result in the states that represent periodic or cyclic signals integrating to
large values. Computing trigonometric values, such as sine or cosine, for these signals
takes longer as the values become larger due to angle reduction. As the signal values become
larger, solver performance and accuracy degrades.

One approach for overcoming this drawback is to reset the angular state to
`0` when it reaches 2π (or to –π when it reaches π, for numerical
symmetry). This approach improves the accuracy of sine and cosine computations and reduces
angle reduction time. But it also requires zero-crossing detection and introduces solver
resets, which slow down the simulation for variable step solvers, particularly in large
models.

To eliminate solver resets at wrap points, the Integrator block supports wrapped states
that you can enable by checking **Wrap state** on the block parameter
dialog box. When you enable **Wrap state**, the block icon changes to
indicate that the block has wrapping states.

An Integrator block configured to wrap state values. The block icon is annotated with a circle with arrows.

The Integrator block supports wrapping states that are bounded by upper and
lower values parameters of the wrapped state. The algorithm for determining wrapping states
is given by:

y={xx∈[xl,xu)x−(xu−xl)⌊x−xlxu−xl⌋otherwise

where:

- *xl* is the lower value of the wrapped
  state.
- *xu* is the upper value of the wrapped
  state.
- *y* is the output.

The support for wrapping states provides these advantages.

- It eliminates simulation instability when your model approaches large angles
  and large state values.
- It reduces the number of solver resets during simulation and eliminates the
  need for zero-crossing detection, improving simulation time.
- It eliminates large angle values, speeding up computation of trigonometric
  functions on angular states.
- It improves solver accuracy and performance and enables unlimited simulation
  time.

### Resetting the State

The block can reset its state to the specified initial condition based on an external signal. To cause the block to reset its state, select one of the **External reset** choices. A trigger port appears below the block's input port and indicates the trigger type.

An integrator block configured to reset the state. The block has two input signals, labeled Input and Reset, and one output signal, labeled Output.

- Select `rising` to reset the state when the reset signal rises from a negative or zero value to a positive value.
- Select `falling` to reset the state when the reset signal falls from a positive value to a zero or negative value.
- Select `either` to reset the state when the reset signal changes from zero to a nonzero value, from a nonzero value to zero, or changes sign.
- Select `level` to reset the state when the reset signal is nonzero at the current time step or changes from nonzero at the previous time step to zero at the current time step.
- Select `level hold` to reset the state when the reset signal is nonzero at the current time step.

The reset port has direct feedthrough. If the block output feeds back into this port, either directly or through a series of blocks with direct feedthrough, an algebraic loop results (see Algebraic Loop Concepts). Use the Integrator block's state port to feed back the block's output without creating an algebraic loop.

**Note**

To be compliant with the Motor Industry Software Reliability Association (MISRA™) software standard, your model must use Boolean signals to drive the external reset ports of Integrator blocks.

### About the State Port

Selecting the **Show state port** check box on the Integrator block's parameter dialog box causes an additional output port, the state port, to appear at the top of the Integrator block.

An integrator block configured to show the state port. The block has one input signal, labeled Input, and two output signals. The state output port is on the top of the block, and the port that provides the output signal value is on the right of the block.

The output of the state port is the same as the output of the block's standard output port except for the following case. If the block is reset in the current time step, the output of the state port is the value that would have appeared at the block's standard output if the block had not been reset. The state port's output appears earlier in the time step than the output of the Integrator block's output port. Use the state port to avoid creating algebraic loops in these modeling scenarios:

- Systems that use self-resetting integrators
- Passing states from one enabled subsystem to another

  **Note**

  When updating a model, Simulink checks that the state port applies to one of these two scenarios.
  If not, an error message appears. Also, you cannot log the output of this port
  in a referenced model that executes in Accelerator mode. If logging is enabled
  for the port, Simulink generates a "signal not found" warning during execution of the
  referenced model.

### Specifying the Absolute Tolerance for the Block Outputs

By default Simulink software uses the absolute tolerance value specified in the Configuration Parameters dialog box (see Error Tolerances for Variable-Step Solvers) to compute the output of the Integrator block. If this value does not provide sufficient error control, specify a more appropriate value in the **Absolute tolerance** field of the Integrator block dialog box. The value that you specify is used to compute all the block outputs.

## Ports

### Input

### **Port\_1** — Signal to integrate scalar | vector | matrix

The input signal is a real-valued scalar, vector, or matrix that this
block integrates.

This port does not have direct feedthrough.

**Data Types:** `double`

### **External Reset** — Signal for resetting state to initial condition scalar | vector | matrix

The external reset signal is a Boolean scalar, vector, or matrix that
resets the block state to the initial condition. See Resetting the State.

This port has direct feedthrough.

#### Dependencies

To enable this port, select **External
Reset**.

**Data Types:** `Boolean`

### **x0** — Initial condition scalar | vector | matrix

The initial condition signal is a real-valued scalar, vector, or
matrix that sets the initial condition for the block.

This port has direct feedthrough.

#### Dependencies

To enable this port, set the **Initial
Conditions** parameter to
`external`.

**Data Types:** `double`
### Output

### **Port\_1** — Integrated signal scalar | vector | matrix

The output signal is a scalar, vector, or matrix with the value of the
integrated input signal. The dimensions of the integrated signal match
the dimensions of the input signal.

**Data Types:** `double`

### **Port\_2** — Output saturation signal scalar | vector | matrix

The output saturation signal is a scalar, vector, or matrix that
indicates when each element in the block state is limited by the upper
or lower saturation limit. The signal value indicates whether the value
is limited and which limit is applied.

- `-1` — Value limited by lower saturation
  limit
- `0` — Value not limited by either
  saturation limit
- `1` — Value limited by upper saturation
  limit

For more information, see Limiting the Integral.

#### Dependencies

To enable this port, select **Show saturation
port**.

**Data Types:** `double`

### **Port\_3** — Block state scalar | vector | matrix

The block state signal is a real-valued scalar, vector, or matrix with
a value that matches the block state value.

For more information, see About the State Port.

#### Dependencies

To enable this port, select **Show state
port**.

**Data Types:** `double`

## Parameters

### **External reset** — Reset states to their initial conditions `none` (default) | `rising` | `falling` | `either` | `level` | `level hold`

Specify the type of trigger to use for the external reset signal.

- Select `rising` to reset the state when the
  reset signal rises from a negative or zero value to a positive value, or
  a negative value to zero value.
- Select `falling` to reset the state when the
  reset signal falls from a positive value to a zero or negative value, or
  from a zero value to negative value.
- Select `either` to reset the state when the
  reset signal changes from zero to a nonzero value, from a nonzero value
  to zero, or changes sign.
- Select `level` to reset the state when the
  reset signal is nonzero at the current time step or changes from nonzero
  at the previous time step to zero at the current time step.
- Select `level hold` to reset the state when
  the reset signal is nonzero at the current time step.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`ExternalReset` |
| **Type:**  character vector , string |
| **Values:**  `'none'` | `'rising'` | `'falling'` | `'either'` | `'level'` | `'level hold'` |
| **Default:**  `'none'` |

### **Initial condition source** — Option to set initial condition using external signal `internal` (default) | `external`

Select source of initial condition:

- `internal` — Get the initial conditions of the states
  from the **Initial condition** parameter.
- `external` — Get the initial conditions of the states
  from an external signal. When you select this option, an input port appears on
  the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`InitialConditionSource` |
| **Type:**  character vector, string |
| **Values:**  `'internal'` | `'external'` |
| **Default:**  `'internal'` |

### **Initial condition** — Initial state 0 (default) | real scalar or array

Set the initial state of the Integrator block.

#### Tips

Simulink software does not allow the initial condition of this block to be
`inf` or `NaN`.

#### Dependencies

Setting **Initial condition source** to
`internal` enables this parameter.

Setting **Initial condition source** to
`external` disables this parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`InitialCondition` |
| **Type:**  scalar or vector |
| **Default:**  `'0'` |

### **Limit output** — Limit block output values to specified range `off` (default for Integrator) | `on` (default for Integrator Limited)

Limit the block's output to a value between the **Lower
saturation limit** and **Upper saturation
limit** parameters.

- Selecting this check box limits the block output to a value between the
  **Lower saturation limit** and **Upper saturation limit** parameters.
- Clearing this check box does not limit the block output values.

#### Dependencies

Selecting this parameter enables the **Lower saturation
limit** and **Upper saturation limit**
parameters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `LimitOutput` |
| **Type:**  character vector , string |
| **Values:**  `'off'` | `'on'` |
| **Default:**  `'off'` |

### **Upper saturation limit** — Upper limit for the integral `inf` (default) | scalar | vector | matrix

Specify the upper limit for the integral as a scalar,
vector, or matrix. You must specify a value
between the **Output minimum**
and **Output maximum** parameter
values.

#### Dependencies

To enable this parameter, select the
**Limit output** check
box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UpperSaturationLimit` |
| **Type:** character vector, string |
| **Values:** scalar | vector | matrix |
| **Default:** `'inf'` |

### **Lower saturation limit** — Lower limit for the integral `-inf` (default) | scalar | vector | matrix

Specify the lower limit for the integral as a scalar, vector, or matrix. You must
specify a value between the **Output minimum** and **Output
maximum** parameter values.

#### Dependencies

To enable this parameter, select the **Limit output** check
box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LowerSaturationLimit` |
| **Type:** character vector , string |
| **Values:** scalar | vector | matrix |
| **Default:** `'-inf'` |

### **Wrap state** — Enable wrapping of states `off` (default) | `on`

Enable wrapping of states between the **Wrapped state upper
value** and **Wrapped state lower value** parameters.
Enabling wrap states eliminates the need for zero-crossing detection, reduces solver
resets, improves solver performance and accuracy, and increases simulation time span
when modeling rotary and cyclic state trajectories.

If you specify **Wrapped state upper value** as
`inf` and **Wrapped state lower value** as
`-inf`, wrapping does not occur.

#### Dependencies

Selecting this parameter enables **Wrapped state upper
value** and **Wrapped state lower value**
parameters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`WrapState` |
| **Type:**  character vector, string |
| **Values:**  `'off'` | `'on'` |
| **Default:**  `'off'` |

### **Wrapped state upper value** — Specify upper value for wrapped state `pi` (default) | scalar | vector

Upper limit of the block output.

#### Dependencies

Selecting **Wrap state** enables this parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`WrappedStateUpperValue` |
| **Type:**  scalar or vector |
| **Values:**  `'2*pi'` |
| **Default:**  `'pi'` |

### **Wrapped state lower value** — Specify lower value for wrap state `-pi` (default) | scalar | vector

Lower limit of the block output.

#### Dependencies

Selecting **Wrap state** enables this parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`WrappedStateLowerValue` |
| **Type:**  scalar or vector |
| **Values:**  `'0'` |
| **Default:**  `'-pi'` |

### **Show saturation port** — Enable saturation output port `off` (default) | `on`

Select this check box to add a saturation output port to the block. When you clear this check box, the block does not have a saturation output port.

#### Dependencies

Selecting this parameter enables a saturation output port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowSaturationPort` |
| **Type:** character vector , string |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Show state port** — Enable state output port `off` (default) | `on`

Select this check box to add a state output port to the block. When you clear this check box, the block does not have a state output port.

#### Dependencies

Selecting this parameter enables a state output port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowStatePort` |
| **Type:** character vector , string |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Absolute tolerance** — Absolute tolerance for block states `auto` (default) | real scalar or vector

- If you enter `auto` or –1, then Simulink uses the absolute tolerance value in the Configuration
  Parameters dialog box (see Solver Pane) to compute
  block states.
- If you enter a real scalar, then that value overrides the absolute
  tolerance in the Configuration Parameters dialog box for computing all block
  states.
- If you enter a real vector, then the dimension of that vector must match
  the dimension of the continuous states in the block. These values override
  the absolute tolerance in the Configuration Parameters dialog box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `AbsoluteTolerance` |
| **Type:**  character vector, string, scalar, or vector |
| **Values:**  `'auto'` | `'-1'` | any positive real scalar or vector |
| **Default:** `'auto'` |

### **Ignore limit and reset when linearizing** — Option to use default reset and limit behavior for block during linearization `off` (default) | `on`

When you select this parameter, the software ignores reset and limit parameters
for this block during linearization and uses default values for those
parameters.

#### Tip

Enable this parameter when you want to linearize a model around an operating
point that causes the integrator to reset or saturate.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IgnoreLimit` |
| **Type:**  character vector | string |
| **Values:**  `'off'` | `'on'` |
| **Default:**  `'off'` |

### **Enable zero-crossing detection** — Enable zero-crossing detection `on` (default) | `off`

Select to enable zero-crossing detection. For more information, see Zero-Crossing Detection.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ZeroCross` |
| **Type**: character vector | string |
| **Values**: `'off'` | `'on'` |
| **Default**: `'on'` |

### **State Name (e.g., 'position')** — Assign unique name to each state `' '` (default) | character vector | string

- To assign a name to a single state, enter the name between quotes, for
  example, `'velocity'`.
- To assign names to multiple states, enter a comma-delimited list
  surrounded by braces, for example, `{'a', 'b', 'c'}`. Each
  name must be unique.
- The state names apply only to the selected block.
- The number of states must divide evenly among the number of state
  names.
- You can specify fewer names than states, but you cannot specify more names
  than states.

  For example, you can specify two names in a system with four states. The
  first name applies to the first two states and the second name to the last
  two states.
- To assign state names with a variable in the MATLAB® workspace, enter the variable without quotes. A variable can
  be a character vector, string, cell array, or structure.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ContinuousStateAttributes` |
| **Type:**  character vector, string |
| **Values:**  `' '` | user-defined |
| **Default:**  `' '` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `noa` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |
|  |  |
| --- | --- |
| a Ports of this block have different direct feedthrough characteristics. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

- Consider discretizing the model
- Not recommended for production code

## Version History

**Introduced before R2006a**
