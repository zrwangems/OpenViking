---
type: simulink-block
title: 'Second-Order Integrator Limited'
family: continuous
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Continuous'
documentation_page: 'secondorderintegratorlimited'
---

# Second-Order Integrator Limited

Second-order integration of input signal

## 中文

输入信号的二阶积分

### 所属库

Simulink / Continuous

### 描述

Second-Order Integrator 模块和 Second-Order Integrator Limited 模块用来求解器二阶初始值问题：

d2xdt2=u,dxdt|t=0=dxo,x|t=0=xo,

其中 *u* 是系统的输入信号。因此，此模块是一个动态系统，它具有两个连续状态：*x* 和 *dx/dt*。

**注意**

这两个状态存在一种数学关系，即，*dx/dt* 是 *x* 的导数。为了在整个仿真过程中满足这种关系，Simulink 对模块的参数和行为进行了诸多限制。

Second-Order Integrator Limited 模块除了默认情况下基于指定的上限和下限值来限制状态外，它与 Second-Order Integrator 模块完全相同。有关详细信息，请参阅限制状态。

Simulink® 软件可以使用若干不同的数值积分方法来计算模块的输出。每一种方法都有适用于特定情景的优点。使用“配置参数”对话框的**求解器**窗格可以选择最适合您的应用的方法。（有关详细信息，请参阅求解器选择标准。）所选求解器使用当前输入值计算 Second-Order Integrator  模块在当前时间步的状态。

使用模块参数对话框可以：

- 指定每个状态初始条件的来源是内部还是外部
- 为状态初始条件指定值
- 为一个或两个状态定义上限和下限
- 为每个状态指定绝对容差
- 为两个状态指定名称
- 选择外部重置条件
- 启用过零检测
- 当 x 达到饱和时重新初始化 dx/dt
- 指定 Simulink 忽略状态限制和外部重置以进行线性化操作

#### 定义初始条件

可以在模块对话框上将每个状态的初始条件逐个定义为参数，或者从外部信号输入一个或全部两个初始条件。

- 要将状态 *x* 的初始条件定义为模块参数，请从 **x 初始条件来源**下拉菜单中选择**内部**，并在 **x 初始条件**字段中输入值。
- 要从状态 *x* 的外部源提供初始条件，请将**初始条件来源**参数指定为**外部**。模块上出现一个额外的输入端口。
- 要将状态 *dx/dt* 的初始条件定义为模块参数，请从 **dx/dt 初始条件来源**下拉菜单中选择**内部**，并在 **dx/dt 初始条件**字段中输入值。
- 要从外部源为状态  *dx/dt* 提供初始条件，请将 **dx/dt 初始条件来源**指定为**外部**。模块上出现一个额外的输入端口。

如果您为两个状态初始条件都选择使用外部源，您的模块将如下所示。

**注意**

- Simulink 不允许初始条件值为 `inf` 或 `NaN`。
- 如果您通过指定饱和界限来限制状态 *x* 或状态 *dx/dt* （请参阅限制状态），而一个或多个初始条件位于对应的范围外，则相应的状态将被初始化为最接近的有效值，并计算一组一致的初始条件。

#### 限制状态

为二阶系统建模时，您可能需要限制模块的状态。例如，气缸内的活塞运动受牛顿第二定律制约，对活塞的位置 (*x*) 有所限制。使用 Second-Order Integrator  模块，您可以限制状态 *x* 和 *dx/dt*，使它们相互独立。您甚至可以在仿真过程中更改限制；但是，您不能改变状态是否受限制。一个重要的原则是，上限必须严格大于对应的下限。

当您限制了一个或两个状态时，模块的外观将发生变化。在这两种状态都受限制的情况下，模块显示如下。

对于每个状态，您可以使用模块参数对话框设置适当的饱和界限范围。

#### 仅限制 *x*

如果您使用 Second-Order Integrator Limited 模块，默认情况下会限制两个状态。但是，您可以通过选择 **x 限制**并在相应的参数字段中输入范围，手动限制 Second-Order Integrator 模块上的状态 *x*。

这样，模块将按如下方式确定状态的值：

- 当 *x* 小于或等于下限值时，*x* 的值保持在下限值，*dx/dt* 设置为零。
- 当 *x* 介于下限值和上限值之间时，两个状态都按照二阶 ODE 给出的轨迹变化。
- 当 *x* 大于或等于上限值时，*x* 的值保持在上限值，*dx/dt* 设置为零。

您可以选择在 *x* 达到饱和时将 *dx/dt* 重新初始化为新的值。请参阅当 x 达到饱和时重新初始化 dx/dt。

#### 仅限制 *dx/dt*

与状态 *x* 一样，状态 *dx/dt* 默认情况下在  Second-Order Integrator Limited 模块对话框的 **dx/dt** 窗格上设置为受限制。您可以在 Second-Order Integrator 模块上手动设置参数 **dx/dt 限制**。在任一情况下，都必须为 *dx/dt* 输入适当的限制。

如果您只限制状态 *dx/dt*，模块将按如下方式确定 *dx/dt* 的值：

- 当 *dx/dt* 小于或等于下限值时，*dx/dt* 的值保持在下限值。
- 当 *dx/dt* 介于下限值和上限值之间时，两个状态都按照二阶 ODE 给出的轨迹变化。
- 当 *dx/dt* 大于或等于上限值时，*dx/dt* 的值保持在上限值。

当状态 *dx/dt* 保持在上限值或下限值时，*x* 的值受一阶初始值问题制约：

dxdt=L,x(tL)=xL,

其中 *L* 是 *dx/dt* 的限制值（上限或下限），*t**L* 是 *dx/dt* 达到此限制值的时间，*x**L* 是状态 *x*  在该时间的值。

#### 限制两个状态

当您限制两个状态时，Simulink 将通过限制允许的 *dx/dt* 上限和下限值，使状态在数学意义上保持一致。这种限制对于满足以下约束很有必要：

- 当 *x* 达到饱和界限值时，*dx/dt* 的值必须为零。
- 要使 *x* 离开上限值，*dx/dt*  的值必须严格为负。
- 要使 *x* 离开下限值，*dx/dt* 的值必须严格为正。

对于这些情况，*dx/dt* 的上限值必须严格为正，*dx/dt* 的下限值必须严格为负。

当两个状态都受限制时，模块将按如下方式确定状态：

- 当 *x* 达到其限制值时，产生的行为与“仅限制 x”中描述的相同。
- 当 *dx/dt* 达到其限制值之一时，产生的行为与“仅限制 dx/dt”中描述的相同 - 包括当 *dx/dt* 保持在其限制值时使用一阶 ODE 计算 *x*。在这种情况下，当 *x* 达到其限制值之一时，它会保持在该限制值并将  *dx/dt* 设置为零。
- 当二者同时达到各自的限制值时，状态 *x*  的行为将覆盖 *dx/dt* 的行为，以保持状态的一致性。

如果您限制了两个状态，可以选择在状态 *x* 达到饱和时重新初始化 *dx/dt*。如果重新初始化后的值超出了 *dx/dt* 的指定范围，则将 *dx/dt* 重新初始化为最接近的有效值，并计算一组一致的初始条件。请参阅 当 x 达到饱和时重新初始化 dx/dt。

#### 重置状态

模块可以根据外部信号将其状态重置为指定的初始条件。要使模块重置其状态，请选择**属性**窗格上的**外部重置**选项之一。模块输入端口下方将显示一个触发端口，并指示触发类型。

- 选择**上升沿**可在重置信号从零上升到正值、从负值上升到正值或从负值上升到零时重置状态。
- 选择**下降沿**可在重置信号从正值下降到零、从正值下降到负值或从零下降到负值时重置状态。
- 选择**任一沿**可在重置信号从零变为非零值或改变符号时重置状态。

重置端口具有直接馈通。如果模块输出直接或通过一系列带直接馈通的模块反馈到此端口中，则会产生代数环（请参阅代数环概念）。

#### 启用过零检测

此参数控制是否为此模块启用过零检测。默认情况下，**属性**窗格上的**启用过零检测**参数处于选中状态。但是，仅当“配置参数”对话框的**求解器**窗格上的**过零控制**设置为**使用局部设置**时，此参数才起作用。有关详细信息，请参阅过零检测。

#### 当 *x* 达到饱和时重新初始化 *dx/dt*

对于某些建模应用程序，当状态 *x* 达到其限制值时，必须重新初始化 *dx/dt*，以使 *x* 立即退出饱和状态。您可以通过在**属性**窗格上选择**当 x 达到饱和时重新初始化 dx/dt** 来实现这一目的。

如果启用了此选项，当 *x*  达到饱和的那一刻，Simulink 将检查 *dx/dt* 初始条件（参数或信号）的当前值是否允许状态 *x* 立即退出饱和。如果允许，Simulink 将使用那一刻的初始条件（参数或信号）值重新初始化状态 *dx/dt*。如果不允许，Simulink 将在当前时刻忽略此参数，并将 *dx/dt* 设置为零，以使模块状态保持一致。

只有在 *x* 真正达到饱和界限的那一刻，此参数才适用。在那之后的任何时间，即在 *x* 保持饱和时，此参数并不适用。

有关详细信息，请参阅关于限制状态的各节内容。有关示例，请参阅弹球的仿真。

#### 忽略状态限制和外部重置以进行线性化

如果您希望通过线性化来简化模型，可以选中**忽略状态限制和重置以便于线性化**，以使 Simulink 忽略状态限制和外部重置。

#### 指定模块输出的绝对容差

默认情况下，Simulink 软件会使用在“配置参数”对话框中指定的绝对容差值（请参阅Error Tolerances for Variable-Step Solvers）来计算 Integrator 模块的输出。如果此值不能提供足够的误差控制，请在参数对话框的 **x 绝对容差**字段中为状态 *x* 指定更合适的值，在 **dx/dt 绝对容差**字段中为状态 *dx/dt* 指定更合适的值。Simulink 将使用您指定的值来计算模块的状态值。

#### 指定输出端口的显示

您可以使用 `ShowOutput` 参数控制是显示 *x* 还是 *dx/dt* 输出端口。您可以显示一个输出端口，也可以显示两个；但必须至少选择一个。

#### 指定状态名称

您可以使用 `StateNameX` 和 `StateNameDXDT` 参数指定 *x* 状态和 *dx/dt* 状态的名称。但是，您必须为这两个状态都指定名称，或者都不指定名称；不能只为 *x*  或者只为 *dx/dt* 指定名称。这两个状态名称必须具有完全相同的类型和长度。而且，状态数量必须能够被名称数量整除。

#### 选择所有选项

如果选择所有选项，模块图标将如下所示。

### 端口

#### 输入

#### **u** — 输入信号 `u` 标量 | 向量 | 矩阵

指向积分器系统的输入信号 `u`，指定为标量、向量或矩阵。

此端口没有直接馈通。

**数据类型:** `double`

#### **x0** — 初始条件 `x0` 标量 | 向量 | 矩阵

外部信号，用于为积分器系统指定初始条件 `x0`。您可以将初始条件指定为标量、向量或矩阵。

此端口具有直接馈通。

##### 依赖关系

要启用此输入端口，请将 **x 初始条件来源**参数设置为**外部**。

**数据类型:** `double`

#### **dx0** — 初始条件 `dx0` 标量 | 向量 | 矩阵

外部信号，用于为积分器系统指定初始条件 `dx0`。您可以将初始条件 `dx0` 指定为标量、向量或矩阵。

此端口具有直接馈通。

##### 依赖关系

要启用此输入端口，请将 **dx/dt 初始条件来源**参数设置为**外部**。

**数据类型:** `double`

#### **External Reset** — 将状态重置为初始条件的信号 标量 | 向量 | 矩阵

外部重置信号是标量、向量或矩阵，用于将模块状态重置为初始条件。

此端口具有直接馈通。

##### 依赖关系

要启用此输入端口，请将**外部重置**参数设置为**上升沿**、**下降沿**或**任一沿**。

**数据类型:** `double`
#### 输出

#### **x** — 输出信号 `x` 标量 | 向量 | 矩阵

`x` 状态输出信号，以标量、向量或矩阵形式提供。

**数据类型:** `double`

#### **dx** — 输出信号 `dx` 标量 | 向量 | 矩阵

`dx` 状态输出信号，指定为标量、向量或矩阵。

**数据类型:** `double`

### 参数

#### x

#### **x 初始条件来源** — 状态 *x* 的初始条件来源 **内部** (默认) | **外部**

指定状态 *x* 的初始条件的来源。

- **内部** - 从 **x 初始条件**参数获取状态 *x* 的初始条件。
- **外部** - 从连接到 **X0** 输入端口的外部模块获取状态 *x* 的初始条件。

##### 限制

Simulink 软件不允许此模块的初始条件为 `inf` 或 `NaN`。

##### 依赖关系

选择**内部**将启用 **x 初始条件**参数并删除 **X0** 输入端口。

选择**外部**将禁用 **x 初始条件**参数并启用 **X0** 输入端口。

##### 编程用法

|  |
| --- |
| **模块参数：**`ICSourceX` |
| **类型：**字符向量、字符串 |
| **值**：`'internal'` | `'external'` |
| **默认值**：`'internal'` |

#### **x 初始条件** — 状态 *x* 的初始条件 `0.0` (默认) | 标量 | 向量 | 矩阵

指定状态 *x* 的初始条件。

##### 限制

Simulink 软件不允许此模块的初始条件为 `inf` 或 `NaN`。

##### 依赖关系

要启用此参数，请将 **x 初始条件来源**设置为**内部**。

将 **x 初始条件来源**设置为**外部**会禁用此参数并启用 **X0** 输入端口。

##### 编程用法

|  |
| --- |
| **模块参数：**`ICX` |
| **类型：**字符向量、字符串 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值：**`'0.0'` |

#### **x 限制** — 状态 *x* 的范围值 `off` | `on`

将模块的状态 *x* 限制为介于 **x 下限**和 **x 上限**参数之间的值。Second-Order Integrator 模块的默认值为 `off`。Second-Order Integrator Limited 的默认值为 `on`。

- 要将状态 *x* 限制为介于 **x 下限**和 **x 上限**参数之间的值，请选中此复选框。
- 要删除对状态 *x* 的范围限制，请清除此复选框。

##### 依赖关系

选中此复选框将启用 **x 上限**和 **x 下限**参数。

##### 编程用法

|  |
| --- |
| **模块参数：**`LimitX` |
| **类型：**字符向量、字符串 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` (Second-Order Integrator) | `'on'` (Second-Order Integrator Limited) |

#### **x 上限** — 状态 *x* 的上限 `1` | `inf` | 标量 | 向量 | 矩阵

指定状态 *x* 的上限值。Second-Order Integrator 模块的默认值为 `inf`。Second-Order Integrator Limited 模块的默认值为 `1`。

##### 提示

状态 *x* 的饱和上限必须严格大于饱和下限。

##### 依赖关系

要启用此参数，请选中 **x 限制**复选框。

##### 编程用法

|  |
| --- |
| **模块参数：**`UpperLimitX` |
| **类型：**字符向量、字符串 |
| **值：**`'1' | 'inf' |` 标量 | 向量 | 矩阵 |
| **默认值：**`'1'` (Second-Order Integrator Limited) | `'inf'` (Second-Order Integrator) |

#### **x 下限** — 状态 *x* 的下限 `0` (默认) | `-inf` | 标量 | 向量 | 矩阵

指定状态 *x* 的下限。Second-Order Integrator 模块的默认值为 `-inf`。Second-Order Integrator Limited 模块的默认值为 `0`。

##### 提示

状态 *x* 的饱和下限必须严格小于饱和上限。

##### 依赖关系

要启用此参数，请选中 **x 限制**复选框。

##### 编程用法

|  |
| --- |
| **模块参数：**`LowerLimitX` |
| **类型：**字符向量、字符串 |
| **值：**`'0' | '-inf' |` 标量 | 向量 | 矩阵 |
| **默认值：**`'0'` (Second-Order Integrator Limited) | `'-inf'` (Second-Order Integrator) |

#### **绕回 x** — 启用 x 的绕回 `off` (默认) | `on`

在 **x 绕回上限值**和 **x 绕回下限值**参数之间启用 *x* 绕回。启用 *x* 绕回可在对旋转和循环状态轨迹建模时消除对过零检测的需求，减少求解器重置，提高求解器性能和准确性，并增加仿真时间范围。

如果将 **x 绕回上限值**指定为 `inf` 并将 **x 绕回下限值**指定为 `-inf`，则永远不会发生绕回。

##### 依赖关系

选中此复选框将启用 **x 绕回上限值**和 **x 绕回下限值**。

##### 编程用法

|  |
| --- |
| **模块参数：**`WrapX` |
| **类型：**字符向量、字符串 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

#### **x 绕回上限值** — 绕回 x 的上限值 `pi` (默认) | 标量 | 向量 | 矩阵

指定绕回 *x* 的上限值。

##### 依赖关系

要启用此参数，请选中**绕回 x** 复选框。

##### 编程用法

|  |
| --- |
| **模块参数：**`WrappedUpperValueX` |
| **类型：**字符向量、字符串 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值：**`'pi'` |

#### **x 绕回下限值** — 绕回 x 的下限值 `-pi` (默认) | 标量 | 向量 | 矩阵

指定绕回 *x* 的下限值。

##### 依赖关系

要启用此参数，请选中**绕回 x** 复选框。

##### 编程用法

|  |
| --- |
| **模块参数：**`WrappedLowerValueX` |
| **类型：**字符向量、字符串 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值**：`'-pi'` |

#### **x 绝对容差** — 用于计算状态 *x* 的绝对容差。 `auto` (默认) | `-1` | 标量 | 向量

指定用于计算状态 *x* 的绝对容差。

- 可以输入**自动**、-1、正实数标量或向量。
- 如果输入**自动**或 -1，则 Simulink 会使用“配置参数”对话框中的绝对容差值（请参阅求解器窗格）来计算模块状态 *x*。
- 如果输入实数标量值，则该值会覆盖“配置参数”对话框中的绝对容差且用于计算所有 *x* 状态。
- 如果输入实数向量，则该向量的维度必须匹配状态 *x* 的维度。这些值将覆盖“配置参数”对话框中的绝对容差。

##### 编程用法

|  |
| --- |
| **模块参数：** `AbsoluteToleranceX` |
| **类型：**字符向量、字符串 |
| **值：**`'auto'` | `'-1'` | 任何正实数标量或向量 |
| **默认值：**`'auto'` |

#### **x 状态名称** — 状态 *x* 的名称 `''` (默认) | 字符向量 | 字符串

为状态 *x* 分配唯一名称。

##### 提示

- 要为单个状态分配名称，请输入名称并用引号引起来，例如 ’position’。
- 要为多个 *x* 状态分配名称，请输入以逗号分隔的列表并用花括号括起来，例如 {'a', 'b', 'c'}。每个名称都必须是唯一的。
- 状态名称只会应用于所选模块。
- 如果您为 *x* 指定状态名称，还必须为 *dx/dt* 指定状态名称。
- *x* 和 *dx/dt* 的状态名称必须具有相同的类型和长度。
- 状态数量必须能够被状态名称的数量整除。指定的名称数量可以少于 *x* 状态数量，但不能多于  *x* 状态数量。例如，可以在具有四个状态的系统中指定两个名称。第一个名称应用于前两个状态，第二个名称应用于后两个状态。但是，您必须保持一致，并对 *dx/dt* 的状态名称应用相同的方案。
- 要在 MATLAB® 工作区中分配带变量的状态名称，请输入不带引号的变量。变量可以是字符向量、字符串或元胞数组。

##### 编程用法

|  |
| --- |
| **模块参数：**`StateNameX` |
| **类型：**字符向量、字符串 |
| **值：**`' '` | 用户定义 |
| **默认值：**`' '` |

#### dx/dt

#### **dx/dt 初始条件来源** — 状态 *dx/dt* 的初始条件来源 **内部** (默认) | **外部**

将状态 *dx/dt* 的初始条件来源指定为**内部**或**外部**。

##### 限制

Simulink 软件不允许此模块的初始条件为 `inf` 或 `NaN`。

##### 依赖关系

- 选择**内部**启用 **dx/dt 初始条件**参数并删除 **dx 0** 输入端口。
- 选择**外部**将禁用 **dx/dt 初始条件**参数并启用 **dx 0** 输入端口。

##### 编程用法

|  |
| --- |
| **模块参数**：`ICSourceDXDT` |
| **类型：**字符向量 |
| **值**：`'internal'` | `'external'` |
| **默认值**：`'internal'` |

#### **dx/dt 初始条件** — 状态 *dx/dt* 的初始条件 `0.0` (默认) | 标量 | 向量 | 矩阵

指定状态 *dx/dt* 的初始条件。

##### 限制

Simulink 软件不允许此模块的初始条件为 `inf` 或 `NaN`。

##### 依赖关系

- 将 **dx/dt 初始条件来源**设置为**内部**将启用此参数。
- 将 **dx/dt 初始条件来源**设置为**外部**将禁用此参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`ICDXDT` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值：**`'0.0'` |

#### **dx/dt 限制** — 状态 *dx/dt* 的范围值 `off` | `on`

将模块的 *dx/dt* 状态限制为介于 **dx/dt 下限**和 **dx/dt 上限**参数之间的值。Second-Order Integrator 模块的默认值为 `off`。Second-Order Integrator Limited 的默认值为 `on`。

##### 提示

如果您为 *x* 设置了饱和界限值，则 **dx/dt 上限**和 **dx/dt 下限**定义的区间必须包含零。

##### 依赖关系

选中此复选框将启用 **dx/dt 上限**和 **dx/dt 下限**参数。

##### 编程用法

|  |
| --- |
| **参数：**`LimitDXDT` |
| **类型：**字符向量 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` (Second-Order Integrator) | `'on'` (Second-Order Integrator Limited) |

#### **dx/dt 上限** — 状态 *dx/dt* 的上限 `inf` (默认) | 标量 | 向量 | 矩阵

指定状态 *dx/dt* 的上限。

##### 依赖关系

如果您限制 *x*，则此参数的值必须严格为正。

要启用此参数，请选中 **dx/dt 限制**复选框。

##### 编程用法

|  |
| --- |
| **模块参数**：`UpperLimitDXDT` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值：**`'inf'` |

#### **dx/dt 下限** — 状态 *dx/dt* 的下限 `-inf` (默认) | 标量 | 向量 | 矩阵

指定状态 *dx/dt* 的下限。

##### 依赖关系

如果您限制 *x*，则此参数的值必须严格为负。

要启用此参数，请选中 **dx/dt 限制**复选框。

##### 编程用法

|  |
| --- |
| **模块参数**：`LowerLimitDXDT` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值：**`'-inf'` |

#### **dx/dt 绝对容差** — 用于计算状态 *dx/dt* 的绝对容差。 `auto` (默认) | `-1` | 标量 | 向量

指定用于计算状态 *dx/dt* 的绝对容差。

- 您可以输入 `auto`、`–1`、正实数标量或向量。
- 如果输入 `auto` 或 `–1`，则 Simulink 会使用“配置参数”对话框中的绝对容差值（请参阅求解器窗格）来计算模块的 *dx/dt* 输出。
- 如果您输入一个数值，该值将覆盖“配置参数”对话框中的绝对容差。

##### 编程用法

|  |
| --- |
| **模块参数**： `AbsoluteToleranceDXDT` |
| **类型：**字符向量、字符串、标量或向量 |
| **值：**`'auto'` | `'-1'` | 任何正实数标量或向量 |
| **默认值：**`'auto'` |

#### **dx/dt 状态名称** — 状态 *dx/dt* 的名称 `' '` (默认) | 字符向量 | 字符串

为状态 *dx/dt* 分配唯一名称。

##### 提示

- 要为单个状态分配名称，请输入名称并用引号引起来，例如 ‘velocity’。
- 要为多个 *dx/dt* 状态分配名称，请输入以逗号分隔的列表并用花括号括起来，例如 {'a', 'b', 'c'}。每个名称都必须是唯一的。
- 状态名称只会应用于所选模块。
- 如果您为 *dx/dt* 指定状态名称，也必须为  *x* 指定状态名称。
- *x* 和 *dx/dt*  的状态名称必须具有相同的类型和长度。
- 状态数量必须能够被状态名称的数量整除。指定的名称数量可以少于 *dx/dt* 状态数量，但不能多于 *dx/dt* 状态数量。例如，可以在具有四个状态的系统中指定两个名称。第一个名称应用于前两个状态，第二个名称应用于后两个状态。但是，您必须保持一致，并对 *x* 的状态名称应用相同的方案。
- 要在 MATLAB 工作区中分配带变量的状态名称，请输入不带引号的变量。变量可以是字符向量、字符串或元胞数组。

##### 编程用法

|  |
| --- |
| **模块参数：**`StateNameDXDT` |
| **类型：**字符向量、字符串 |
| **值：**`' '` | 用户定义 |
| **默认值：**`' '` |

#### 属性

#### **外部重置** — 将状态重置为其初始条件 **无** (默认) | **上升沿** | **下降沿** | **任一沿**

当重置信号中发生触发事件时，将状态重置为其初始条件。

- **无** - 不将状态重置为初始条件。
- **上升沿** - 当重置信号从零上升到正值或从负值上升到正值时重置状态。
- **下降沿** - 当重置信号从正值下降到零或从正值下降到负值时重置状态。
- **任一沿** - 当重置信号从零变为非零值或改变符号时重置状态。

##### 编程用法

|  |
| --- |
| **模块参数：**`ExternalReset` |
| **类型：**字符向量、字符串 |
| **值**：`'none'` | `'rising'` | `'falling'` | `'either'` |
| **默认值：**`'none'` |

#### **启用过零检测** — 启用过零检测 `on` (默认) | `off`

选择此项以启用过零检测。有关详细信息，请参阅过零检测。

##### 编程用法

|  |
| --- |
| **参数：**`ZeroCross` |
| **类型：**字符向量、字符串 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'on'` |

#### **当 x 达到饱和时重新初始化 dx/dt** — 当 *x* 达到饱和时，重置 *dx/dt* `off` (默认) | `on`

在状态 *x* 达到饱和的瞬间，将 *dx/dt* 重置为其当前初始条件。

##### 提示

*dx/dt*  初始条件的值必须能够让 *x* 立即变得不饱和。否则，Simulink 将忽略 *dx/dt* 的初始条件，以保持模块状态在数学意义上的一致性。

##### 编程用法

|  |
| --- |
| **模块参数：** `ReinitDXDTwhenXreachesSaturation` |
| **类型：**字符向量、字符串 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

#### **忽略状态限制和重置以便于线性化** — 忽略状态限制和外部重置以进行线性化 `off` (默认) | `on`

为了进行线性化，让 Simulink 忽略指定的状态限制和外部重置。

##### 编程用法

|  |
| --- |
| **模块参数：** `IgnoreStateLimitsAndResetForLinearization` |
| **类型：**字符向量、字符串 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

#### **显示输出** — 要显示的输出端口 **两者** (默认) | **x** | **dxdt**

指定模块上的输出端口。

- **两者** - 同时显示 *x* 和 *dx/dt* 输出端口。
- **x** - 只显示 *x* 输出端口。
- **dx/dt** - 只显示 *dx/dt* 输出端口。

##### 编程用法

|  |
| --- |
| **模块参数：**`ShowOutput` |
| **类型：**字符向量、字符串 |
| **值**：`'both'` | `'x'` | `'dxdt'` |
| **默认值**：`'both'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不建议用于生产级的代码。涉及到嵌入式系统中常见的资源限制以及对速度和内存的限制。生成的代码可以包含内存的动态分配和释放、递归、额外的内存开销以及长短不等的执行时间。虽然代码在功能上有效并且在资源丰富的环境中通常可接受，但较小的嵌入式目标通常不能支持此类代码。

通常，考虑使用 Simulink 模型离散化器将连续模块映射到支持生产代码生成的离散等效模块。要启动模型离散化器，请在 Simulink 编辑器中，在 **App** 选项卡上，在 **App** 下，在**控制系统**下，点击**模型离散化器**。一个例外是 Second-Order Integrator 模块，因为对于该模块，模型离散化器产生近似离散化。

### 版本历史记录

**在 R2010a 中推出**

## Libraries

Simulink / Continuous

## Description

The Second-Order Integrator block and the Second-Order Integrator Limited block solve the second-order initial value problem:

d2xdt2=u,dxdt|t=0=dxo,x|t=0=xo,

where *u* is the input to the system. The block is therefore a dynamic system with two continuous states: *x* and *dx/dt*.

**Note**

These two states have a mathematical relationship, namely, that *dx/dt* is the derivative of *x*. To satisfy this relationship throughout the simulation, Simulink places various constraints on the block parameters and behavior.

The Second-Order Integrator Limited block is identical to the Second-Order Integrator block with the exception that it defaults to limiting the states based on the specified upper and lower limits. For more information, see Limiting the States.

Simulink® software can use several different numerical integration methods to compute the outputs of the block. Each has advantages for specific applications. Use the **Solver** pane of the Configuration Parameters dialog box to select the technique best suited to your application. (For more information, see Solver Selection Criteria.) The selected solver computes the states of the Second-Order Integrator block at the current time step using the current input value.

Use the block parameter dialog box to:

- Specify whether the source of each state initial condition is internal or external
- Specify a value for the state initial conditions
- Define upper and lower limits on either or both states
- Specify absolute tolerances for each state
- Specify names for both states
- Choose an external reset condition
- Enable zero-crossing detection
- Reinitialize dx/dt when x reaches saturation
- Specify that Simulink disregard the state limits and external reset for linearization operations

### Defining Initial Conditions

You can define the initial conditions of each state individually as a parameter on the block dialog box or input one or both of them from an external signal.

- To define the initial conditions of state *x* as a block parameter, use the **Initial condition source x** drop-down menu to select `internal` and enter the value in the **Initial condition x** field.
- To provide the initial conditions from an external source for state *x*, specify the **Initial condition source x** parameter as `external`. An additional input port appears on the block.
- To define the initial conditions of state *dx/dt* as a block parameter, use the **Initial condition source dx/dt** drop-down menu to select `internal` and enter the value in the **Initial condition dx/dt** field.
- To provide the initial conditions from an external source for state *dx/dt*, specify **Initial condition source dx/dt** as `external`. An additional input port appears on the block.

If you choose to use an external source for both state initial conditions, your block appears as follows.

**Note**

- Simulink does not allow initial condition values of `inf` or `NaN`.
- If you limit state *x* or state *dx/dt*  by specifying saturation limits (see Limiting the States) and one or more initial conditions are outside the corresponding limits, then the respective states are initialized to the closest valid value and a set of consistent initial conditions is calculated.

### Limiting the States

When modeling a second-order system, you may need to limit the block states. For example, the motion of a piston within a cylinder is governed by Newton's Second Law and has constraints on the piston position (*x*). With the Second-Order Integrator  block, you can limit the states *x* and *dx/dt* independent of each other. You can even change the limits during simulation; however, you cannot change whether or not the states are limited. An important rule to follow is that an upper limit must be strictly greater than its corresponding lower limit.

The block appearance changes when you limit one or both states. With both states limited, the block appears as follows.

For each state, you can use the block parameter dialog box to set appropriate saturation limits.

### Limiting *x* Only

If you use the Second-Order Integrator Limited block, both states are limited by default. But you can also manually limit state *x* on the Second-Order Integrator block by selecting **Limit x** and entering the limits in the appropriate parameter fields.

The block then determines the values of the states as follows:

- When *x* is less than or equal to its lower limit, the value of *x* is held at its lower limit and *dx/dt* is set to zero.
- When *x* is in between its lower and upper limits, both states follow the trajectory given by the second-order ODE.
- When *x* is greater than or equal to its upper limit, the value of *x* is held at its upper limit and *dx/dt* is set to zero.

You can choose to reinitialize *dx/dt* to a new value at the time when *x* reaches saturation. See Reinitializing dx/dt When x Reaches Saturation.

### Limiting *dx/dt* Only

As with state *x*, state *dx/dt* is set as limited by default on the **dx/dt** pane of the Second-Order Integrator Limited block dialog box. You can manually set this parameter, **Limit dx/dt**, on the Second-Order Integrator block. In either case, you must enter the appropriate limits for *dx/dt*.

If you limit only the state *dx/dt*, then the block determines the values of *dx/dt* as follows:

- When *dx/dt* is less than or equal to its lower limit, the value of *dx/dt* is held at its lower limit.
- When *dx/dt* is in between its lower and upper limits, both states follow the trajectory given by the second-order ODE.
- When *dx/dt* is greater than or equal to its upper limit, the value of *dx/dt* is held at its upper limit.

When state *dx/dt* is held at it upper or lower limit, the value of *x* is governed by the first-order initial value problem:

dxdt=L,x(tL)=xL,

where *L* is the *dx/dt* limit (upper or lower), *t**L* is the time when *dx/dt* reaches this limit, and *x**L* is the value of state *x*  at that time.

### Limiting Both States

When you limit both states, Simulink maintains mathematical consistency of the states by limiting the allowable values of the upper and lower limits for *dx/dt*. Such limitations are necessary to satisfy the following constraints:

- When *x* is at its saturation limits, the value of *dx/dt* must be zero.
- In order for *x* to leave the upper limit, the value of *dx/dt*  must be strictly negative.
- In order for *x* to leave its lower limit, the value of *dx/dt* must be strictly positive.

For such cases, the upper limit of *dx/dt* must be strictly positive and the lower limit of *dx/dt* must be strictly negative.

When both states are limited, the block determines the states as follows:

- Whenever *x* reaches its limits, the resulting behavior is the same as that described in “Limiting x only”.
- Whenever *dx/dt* reaches one of its limits, the resulting behavior is the same as that described in “Limiting dx/dt only” — including the computation of *x* using a first-order ODE when *dx/dt* is held at one of its limits. In such cases, when *x* reaches one of its limits, it is held at that limit and *dx/dt* is set to zero.
- Whenever both reach their respective limits simultaneously, the state *x*  behavior overrides *dx/dt* behavior to maintain consistency of the states.

When you limit both states, you can choose to reinitialize *dx/dt* at the time when state *x* reaches saturation. If the reinitialized value is outside specified limits on *dx/dt*, then *dx/dt* is reinitialized to the closest valid value and a consistent set of initial conditions is calculated. See Reinitializing dx/dt When x Reaches Saturation

### Resetting the State

The block can reset its states to the specified initial conditions based on an external signal. To cause the block to reset its states, select one of the **External reset** choices on the **Attributes** pane. A trigger port appears on the block below its input port and indicates the trigger type.

- Select `rising` to reset the states when the reset signal rises from zero to a positive value, from a negative to a positive value, or a negative value to zero.
- Select `falling` to reset the states when the reset signal falls from a positive value to zero, from a positive to a negative value, or from zero to negative.
- Select `either` to reset the states when the reset signal changes from zero to a nonzero value or changes sign.

The reset port has direct feedthrough. If the block output feeds back into this port, either directly or through a series of blocks with direct feedthrough, an algebraic loop results (see Algebraic Loop Concepts).

### Enabling Zero-Crossing Detection

This parameter controls whether zero-crossing detection is enabled for this block. By default, the **Enable zero-crossing detection** parameter is selected on the **Attributes** pane. However, this parameter is only in affect if the **Zero-crossing control**, on the **Solver** pane of the Configuration Parameters dialog box, is set to `Use local settings`. For more information, see Zero-Crossing Detection.

### Reinitializing *dx/dt* When *x* Reaches Saturation

For certain modeling applications, *dx/dt* must be reinitialized when state *x* reaches its limits in order to pull *x* out of saturation immediately. You can achieve this by selecting **Reinitialize dx/dt when x reaches saturation** on the **Attributes** pane.

If this option is on, then at the instant when *x*  reaches saturation, Simulink checks whether the current value of the *dx/dt* initial condition (parameter or signal) allows the state *x* to leave saturation immediately. If so, Simulink reinitializes state *dx/dt* with the value of the initial condition (parameter or signal) at that instant. If not, Simulink ignores this parameter at the current instant and sets *dx/dt* to zero to make the block states consistent.

This parameter only applies at the time when *x* actually reaches saturation limit. It does not apply at any future time when *x* is being held at saturation.

Refer to the sections on limiting the states for more information. For an example, see Simulation of Bouncing Ball.

### Disregarding State Limits and External Reset for Linearization

For cases where you simplify your model by linearizing it, you can have Simulink disregard the limits of the states and the external reset by selecting **Ignore state limits and the reset for linearization**.

### Specifying the Absolute Tolerance for the Block Outputs

By default Simulink software uses the absolute tolerance value specified in the Configuration Parameters dialog box (see Error Tolerances for Variable-Step Solvers) to compute the output of the integrator blocks. If this value does not provide sufficient error control, specify a more appropriate value for state *x* in the **Absolute tolerance x** field and for state *dx/dt* in the **Absolute tolerance dx/dt** field of the parameter dialog box. Simulink uses the values that you specify to compute the state values of the block.

### Specifying the Display of the Output Ports

You can control whether to display the *x* or the *dx/dt* output port using the `ShowOutput` parameter. You can display one output port or both; however, you must select at least one.

### Specifying the State Names

You can specify the name of *x* states and *dx/dt* states using the `StateNameX` and `StateNameDXDT` parameters. However, you must specify names for both or neither; you cannot specify names for just *x*  or just *dx/dt*. Both state names must have identical type and length. Furthermore, the number of names must evenly divide the number of states.

### Selecting All Options

When you select all options, the block icon looks like this.

## Ports

### Input

### **u** — Input signal `u` scalar | vector | matrix

Input signal `u` to the integrator system, specified as a scalar, vector, or matrix.

This port does not have direct feedthrough.

**Data Types:** `double`

### **x0** — Initial condition `x0` scalar | vector | matrix

External signal specifying the initial condition `x0` to the integrator system. You can specify the initial condition as a scalar, vector, or matrix.

This port has direct feedthrough.

#### Dependencies

To enable this input port, set the **Initial condition source x** parameter to `external`.

**Data Types:** `double`

### **dx0** — Initial condition `dx0` scalar | vector | matrix

External signal specifying the initial condition `dx0` to the integrator system. You can specify the initial condition `dx0` as a scalar, vector, or matrix.

This port has direct feedthrough.

#### Dependencies

To enable this input port, set the **Initial condition source dx/dt** parameter to `external`.

**Data Types:** `double`

### **External Reset** — Signal for resetting states to initial conditions scalar | vector | matrix

The external reset signal is a scalar, vector, or matrix that resets the
block states to the initial conditions.

This port has direct feedthrough.

#### Dependencies

To enable this input port, set the **External reset**
parameter to `rising`,
`falling`, or
`either`.

**Data Types:** `double`
### Output

### **x** — Output signal `x` scalar | vector | matrix

`x` state output signal, provided as a scalar, vector, or matrix.

**Data Types:** `double`

### **dx** — Output signal `dx` scalar | vector | matrix

`dx` state output signal, specified as a scalar, vector, or matrix.

**Data Types:** `double`

## Parameters

### x

### **Initial condition source x** — Source of initial condition for state *x* `internal` (default) | `external`

Specify the source of the initial conditions for state *x*.

- `internal` — Get the initial conditions of state *x* from the **Initial condition x** parameter.
- `external` — Get the initial conditions of state *x* from an external block connected to the **X0** input port.

#### Limitations

Simulink software does not allow the initial condition of this block to be `inf` or `NaN`.

#### Dependencies

Selecting `internal` enables the **Initial condition x** parameter and removes the **X0** input port.

Selecting `external` disables the **Initial condition x** parameter and enables the **X0** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ICSourceX` |
| **Type:** character vector, string |
| **Values:** `'internal'` | `'external'` |
| **Default:** `'internal'` |

### **Initial condition x** — Initial condition of state *x* `0.0` (default) | scalar | vector | matrix

Specify the initial condition of state *x*.

#### Limitations

Simulink software does not allow the initial condition of this block to be `inf` or `NaN`.

#### Dependencies

To enable this parameter, set **Initial condition source x** to `internal`.

Setting **Initial condition source x** to `external` disables this parameter and enables the **X0** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ICX` |
| **Type:** character vector, string |
| **Values:** scalar | vector | matrix |
| **Default:** `'0.0'` |

### **Limit x** — Limit values of state *x* `off` | `on`

Limit state *x* of the block to a value between the **Lower limit x** and **Upper limit x** parameters. The default value of the Second-Order Integrator block is `off`. The default value of the Second-Order Integrator Limited is `on`.

- To limit state *x* to a value between the **Lower limit x** and **Upper limit x** parameters, select this check box.
- To remove range limitations on state *x*, clear this check box.

#### Dependencies

Selecting this check box enables the **Upper limit x** and **Lower limit x** parameters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LimitX` |
| **Type:** character vector, string |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` (Second-Order Integrator) | `'on'` (Second-Order Integrator Limited) |

### **Upper limit x** — Upper limit of state *x* `1` | `inf` | scalar | vector | matrix

Specify the upper limit of state *x*. The default value for the Second-Order Integrator block is `inf`. The default value for the Second-Order Integrator Limited block is `1`.

#### Tips

The upper saturation limit for state *x* must be strictly greater than the lower saturation limit.

#### Dependencies

To enable this parameter, select the **Limit x** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UpperLimitX` |
| **Type:** character vector, string |
| **Values:** `'1' | 'inf' |` scalar | vector | matrix |
| **Default:** `'1'` (Second-Order Integrator Limited) | `'inf'` (Second-Order Integrator) |

### **Lower limit x** — Lower limit of state *x* `0` (default) | `-inf` | scalar | vector | matrix

Specify the lower limit of state *x*. The default value for the Second-Order Integrator block is `-inf`. The default value for the Second-Order Integrator Limited block is `0`.

#### Tip

The lower saturation limit for state *x* must be strictly less than the upper saturation limit.

#### Dependencies

To enable this parameter, select the **Limit x** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LowerLimitX` |
| **Type:** character vector, string |
| **Values:** `'0' | '-inf' |` scalar | vector | matrix |
| **Default:** `'0'` (Second-Order Integrator Limited) | `'-inf'` (Second-Order Integrator) |

### **Wrap x** — Enable wrapping of x `off` (default) | `on`

Enable wrapping of *x* between the **Wrapped upper value x** and **Wrapped lower value x** parameters. Enabling wrapping of *x* eliminates the need for zero-crossing detection, reduces solver resets, improves solver performance and accuracy, and increases simulation time span when modeling rotary and cyclic state trajectories.

If you specify **Wrapped upper value x** as `inf` and **Wrapped lower value x** as `-inf`, wrapping will never occur.

#### Dependencies

Selecting this check box enables **Wrapped upper value x** and **Wrapped lower value x**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `WrapX` |
| **Type:** character vector, string |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Wrapped upper value x** — Upper value for wrapping x `pi` (default) | scalar | vector | matrix

Specify the upper value for wrapping *x*.

#### Dependencies

To enable this parameter, select the **Wrap x** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `WrappedUpperValueX` |
| **Type:** character vector, string |
| **Values:** scalar | vector | matrix |
| **Default:** `'pi'` |

### **Wrapped lower value x** — Lower value for wrapping x `-pi` (default) | scalar | vector | matrix

Specify the lower value for wrapping *x*.

#### Dependencies

To enable this parameter, select the **Wrap x** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `WrappedLowerValueX` |
| **Type:** character vector, string |
| **Values:** scalar | vector | matrix |
| **Default:** `'-pi'` |

### **Absolute tolerance x** — Absolute tolerance for computing state *x* `auto` (default) | `-1` | scalar | vector

Specify the absolute tolerance for computing state *x*.

- You can enter `auto`, –1, a positive real scalar or vector.
- If you enter `auto` or –1, Simulink uses the absolute tolerance value in the Configuration Parameters dialog box (see Solver Pane) to compute state *x*.
- If you enter a real scalar value, that value overrides the absolute tolerance in the Configuration Parameters dialog box and is used for computing all *x* states.
- If you enter a real vector, the dimension of that vector must match the dimension of state *x*. These values override the absolute tolerance in the Configuration Parameters dialog box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `AbsoluteToleranceX` |
| **Type:** character vector, string |
| **Values:** `'auto'` | `'-1'` | any positive real scalar or vector |
| **Default:** `'auto'` |

### **State name x** — Name for state *x* `''` (default) | character vector | string

Assign a unique name to state *x*.

#### Tips

- To assign a name to a single state, enter the name between quotes, for example, position'.
- To assign names to multiple *x* states, enter a comma-delimited list surrounded by braces, for example, {'a', 'b', 'c'}. Each name must be unique.
- The state names apply only to the selected block.
- If you specify a state name for *x*, you must also specify a state name for *dx/dt*.
- State names for *x* and *dx/dt* must have identical types and lengths.
- The number of states must be evenly divided by the number of state names. You can specify fewer names than *x* states, but you cannot specify more names than *x* states. For example, you can specify two names in a system with four states. The first name applies to the first two states and the second name to the last two states. However, you must be consistent and apply the same scheme to the state names for *dx/dt*.
- To assign state names with a variable in the MATLAB® workspace, enter the variable without quotes. A
  variable can be a character vector, string or a cell array.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateNameX` |
| **Type:** character vector, string |
| **Values:** `' '` | user-defined |
| **Default:** `' '` |

### dx/dt

### **Initial condition source dx/dt** — Source of initial condition for state *dx/dt* `internal` (default) | `external`

Specify the source of initial conditions for state *dx/dt* as `internal` or `external`.

#### Limitations

Simulink software does not allow the initial condition of this block to be `inf` or `NaN`.

#### Dependencies

- Selecting `internal` enables the **Initial condition dx/dt** parameter and removes the **dx0** input port.
- Selecting `external` disables the **Initial condition dx/dt** parameter and enables the **dx0** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ICSourceDXDT` |
| **Type:** character vector |
| **Values:** `'internal'` | `'external'` |
| **Default:** `'internal'` |

### **Initial condition dx/dt** — Initial condition of state *dx/dt* `0.0` (default) | scalar | vector | matrix

Specify the initial condition of state *dx/dt*.

#### Limitations

Simulink software does not allow the initial condition of this block to be `inf` or `NaN`.

#### Dependencies

- Setting **Initial condition source dx/dt** to `internal` enables this parameter.
- Setting **Initial condition source dx/dt** to `external` disables this parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ICDXDT` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'0.0'` |

### **Limit dx/dt** — Limit values of state *dx/dt* `off` | `on`

Limit the *dx/dt* state of the block to a value between the **Lower limit dx/dt** and **Upper limit dx/dt** parameters. The default value of the Second-Order Integrator block is `off`. The default value of the Second-Order Integrator Limited is `on`.

#### Tip

If you set saturation limits for *x*, then the interval defined by the **Upper limit dx/dt** and **Lower limit dx/dt** must contain zero.

#### Dependencies

Selecting this check box enables the **Upper limit dx/dt** and **Lower limit dx/dt** parameters.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `LimitDXDT` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` (Second-Order Integrator) | `'on'` (Second-Order Integrator Limited) |

### **Upper limit dx/dt** — Upper limit of state *dx/dt* `inf` (default) | scalar | vector | matrix

Specify the upper limit for state *dx/dt*.

#### Dependencies

If you limit *x*, then this parameter must have a strictly positive value.

To enable this parameter, select the **Limit dx/dt** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UpperLimitDXDT` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'inf'` |

### **Lower limit dx/dt** — Lower limit of state *dx/dt* `-inf` (default) | scalar | vector | matrix

Specify the lower limit for state *dx/dt*.

#### Dependencies

If you limit *x*, then this parameter must have a strictly negative value.

To enable this parameter, select the **Limit dx/dt** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LowerLimitDXDT` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'-inf'` |

### **Absolute tolerance dx/dt** — Absolute tolerance for computing state *dx/dt* `auto` (default) | `-1` | scalar | vector

Specify the absolute tolerance for computing state *dx/dt*.

- You can enter `auto`, `–1`, a positive real scalar or vector.
- If you enter `auto` or `–1`, then Simulink uses the absolute tolerance value in the Configuration Parameters dialog box (see Solver Pane) to compute the *dx/dt* output of the block.
- If you enter a numeric value, that value overrides the absolute tolerance in the Configuration Parameters dialog box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `AbsoluteToleranceDXDT` |
| **Type:** character vector, string, scalar, or vector |
| **Values:** `'auto'` | `'-1'` | any positive real scalar or vector |
| **Default:** `'auto'` |

### **State name dx/dt** — Name for state *dx/dt* `' '` (default) | character vector | string

Assign a unique name to state *dx/dt*.

#### Tips

- To assign a name to a single state, enter the name between quotes, for example, 'velocity'.
- To assign names to multiple *dx/dt* states, enter a comma-delimited list surrounded by braces, for example, {'a', 'b', 'c'}. Each name must be unique.
- The state names apply only to the selected block.
- If you specify a state name for *dx/dt*, you must also specify a state name for *x*.
- State names for *x* and *dx/dt*  must have identical types and lengths.
- The number of states must be evenly divided by the number of state names. You can specify fewer names than *dx/dt* states, but you cannot specify more names than *dx/dt* states. For example, you can specify two names in a system with four states. The first name applies to the first two states and the second name to the last two states. However, you must be consistent and apply the same scheme to the state names for *x*.
- To assign state names with a variable in the
  MATLAB workspace, enter the variable without
  quotes. A variable can be a character vector,
  string, or a cell array.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateNameDXDT` |
| **Type:** character vector, string |
| **Values:** `' '` | user-defined |
| **Default:** `' '` |

### Attributes

### **External reset** — Reset states to their initial conditions `none` (default) | `rising` | `falling` | `either`

Reset the states to their initial conditions when a trigger event occurs in the reset signal.

- `none` — Do not reset the state to initial conditions.
- `rising` — Reset the state when the reset signal rises from a zero to a positive value or from a negative to a positive value.
- `falling` — Reset the state when the reset signal falls from a positive value to zero or from a positive to a negative value.
- `either` — Reset the state when the reset signal changes from zero to a nonzero value or changes sign.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ExternalReset` |
| **Type:** character vector, string |
| **Values:** `'none'` | `'rising'` | `'falling'` | `'either'` |
| **Default:** `'none'` |

### **Enable zero-crossing detection** — Enable zero-crossing detection `on` (default) | `off`

Select to enable zero-crossing detection. For more information, see Zero-Crossing Detection.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `ZeroCross` |
| **Type:** character vector, string |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Reinitialize dx/dt when x reaches saturation** — Reset *dx/dt* when *x* reaches saturation `off` (default) | `on`

At the instant when state *x* reaches saturation, reset *dx/dt* to its current initial conditions.

#### Tip

The *dx/dt*  initial condition must have a value that enables *x* to leave saturation immediately. Otherwise, Simulink ignores the initial conditions for *dx/dt* to preserve mathematical consistency of block states.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `ReinitDXDTwhenXreachesSaturation` |
| **Type:** character vector, string |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Ignore state limits and the reset for linearization** — Ignore state limits and external reset for linearization `off` (default) | `on`

For linearization purposes, have Simulink ignore the specified state limits and the external reset.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `IgnoreStateLimitsAndResetForLinearization` |
| **Type:** character vector, string |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Show output** — Output ports to display `both` (default) | `x` | `dxdt`

Specify the output ports on the block.

- `both` — Show both *x* and *dx/dt* output ports.
- `x` — Show only the *x* output port.
- `dx/dt` — Show only the *dx/dt* output port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowOutput` |
| **Type:** character vector, string |
| **Values:** `'both'` | `'x'` | `'dxdt'` |
| **Default:** `'both'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Multidimensional Signals** | `No` |
| **Variable-Size Signals** | `No` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production-quality code. Relates to resource limits and restrictions on speed and memory often found in embedded systems. The code generated can contain dynamic allocation and freeing of memory, recursion, additional memory overhead, and widely-varying execution times. While the code is functionally valid and generally acceptable in resource-rich environments, smaller embedded targets often cannot support such code.

In general, consider using the Simulink Model Discretizer to map continuous blocks into
discrete equivalents that support production code generation. To start the Model
Discretizer, in the Simulink Editor, on the **Apps** tab, under
**Apps**, under **Control Systems**, click
**Model Discretizer**. One exception is the Second-Order
Integrator block because, for this block, the Model Discretizer produces an
approximate discretization.

## Version History

**Introduced in R2010a**
