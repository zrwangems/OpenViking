---
type: simulink-block
title: 'Discrete-Time Integrator'
family: discrete
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'discretetimeintegrator'
---

# Discrete-Time Integrator

Perform discrete-time integration or accumulation of signal

## 中文

执行信号的离散时间积分或累积

### 所属库

Simulink / Commonly Used Blocks Simulink / Discrete HDL Coder / Discrete HDL Coder / HDL Floating Point Operations

### 描述

使用 Discrete-Time Integrator 模块替代 Integrator 模块来创建纯离散模型。使用 Discrete-Time Integrator 模块，您可以：

- 在模块对话框上定义初始条件，或作为模块的输入
- 定义输入增益 (K) 值
- 输出模块状态
- 定义积分的上限和下限
- 使用其他重置输入重置状态

#### 输出方程

对于第一个时间步，模块状态为 `n = 0`，具有初始输出 `y(0) = IC` 或初始状态 `x(0) = IC`，具体取决于**初始条件设置**参数值。

对于仿真时间为 `t(n)` 的给定步长 `n > 0`，Simulink® 将更新输出 `y(n)`，如下所示：

- 前向欧拉方法：

  ```
  y(n) = y(n-1) + K*[t(n) - t(n-1)]*u(n-1)
  ```
- 后向欧拉方法：

  ```
  y(n) = y(n-1) + K*[t(n) - t(n-1)]*u(n)
  ```
- 梯形法：

  ```
  y(n) = y(n-1) + K*[t(n)-t(n-1)]*[u(n)+u(n-1)]/2
  ```

Simulink 根据模块的采样时间（可以是显式或触发的采样时间）自动选择这些输出方程的状态空间实现。当使用显式采样时间时，对于所有 `n > 0` 的步长，`t(n)-t(n-1)` 将减小到采样时间 `T`。

#### 积分方法和累积方法

此模块可以使用前向欧拉、后向欧拉或梯形法对信号进行积分或累积。假定 `u` 为输入，`y` 为输出，`x` 为状态。对于给定步长 `n`，Simulink 将更新 `y(n)` 和 `x(n+1)`。在积分模式下，`T` 是模块的采样时间（如果是触发采样时间，则是 delta `T`）。在累积模式下，`T = 1`。模块采样时间决定计算输出的时间，而不是输出值。`K` 是增益值。值根据上限或下限进行剪切。

**前向欧拉方法**

前向欧拉方法（默认值），也称为正向矩形或左手逼近方法

该软件将 `1/s` 近似为 `T/(z-1)`。模块在第 `n` 个时间步的输出的表达式为：

```
x(n+1) = x(n) + K*T*u(n)
y(n)   = x(n)
```

模块按照以下时间步计算输出：

```
Step 0:          y(0)   = IC (clip if necessary)
                 x(1)   = y(0) + K*T*u(0)

Step 1:          y(1)   = x(1)
                 x(2)   = x(1) + K*T*u(1)

Step n:          y(n)   = x(n)
                 x(n+1) = x(n) + K*T*u(n) (clip if necessary)
```

使用此方法时，输入端口 1 没有直接馈通。

**后向欧拉方法**

后向欧拉方法，也称为反向矩形或右手逼近方法

该软件将 `1/s` 近似为 `T*z/(z-1)`。模块在第 `n` 个时间步生成的输出的表达式为：

```
y(n) = y(n-1) + K*T*u(n).
```

假设 `x(n) = y((n)-1)`。模块按照以下时间步计算输出。

- 如果触发子系统和函数调用子系统的参数**初始条件设置**设置为**输出**或**自动**：

  ```
  Step 0:          y(0) = IC (clipped if necessary)
                   x(1) = y(0)
  ```
- 如果非触发子系统的参数**初始条件设置**设置为 ：

  ```
  Step 0:          x(0)   = IC (clipped if necessary)
                   x(1)   = y(0) = x(0) + K*T*u(0)

  Step 1:          y(1)   = x(1) + K*T*u(1)
                   x(2)   = y(1)

  Step n:          y(n)   = x(n) + K*T*u(n)
                   x(n+1) = y(n)
  ```

使用此方法时，输入端口 1 具有直接馈通。

**梯形法**

对于此方法，本软件将 `1/s` 近似为 `T/2*(z+1)/(z-1)`。

当 `T` 固定时（等于采样周期），计算输出的表达式为：

```
x(n) = y(n-1) + K*T/2*u(n-1)
y(n) = x(n) + K*T/2*u(n)
```

- 如果触发子系统和函数调用子系统的参数**初始条件设置**设置为**输出**或**自动**：

  ```
  Step 0:          y(0)   = IC (clipped if necessary)
                   x(1)   = y(0) + K*T/2*u(0)
  ```
- 如果非触发子系统的参数**初始条件设置**设置为 ：

  ```
  Step 0:          x(0)   = IC (clipped if necessary)
                   y(0)   = x(0) + K*T/2*u(0)
                   x(1)   = y(0) + K*T/2*u(0)

  Step 1:          y(1)   = x(1) + K*T/2*u(1)
                   x(2)   = y(1) + K*T/2*u(1)

  Step n:          y(n)   = x(n) + K*T/2*u(n)
                   x(n+1) = y(n) + K*T/2*u(n)
  ```

这里，`x(n+1)` 是下一个输出的最佳估计值。它与状态的不同之处在于，`x(n)` 不等于 `y(n)`。

使用此方法时，输入端口 1 具有直接馈通。

**当 T 为变量时**

当 `T` 是变量时（例如，从触发时间获得），模块将按照以下时间步计算输出。

- 如果触发子系统和函数调用子系统的参数**初始条件设置**设置为**输出**或**自动**：

  ```
  Step 0:          y(0)   = IC (clipped if necessary)
                   x(1)   = y(0)
  ```
- 如果非触发子系统的参数**初始条件设置**设置为 ：

  ```
  Step 0:          x(0)   = IC (clipped if necessary)
                   x(1)   = y(0) = x(0) + K*T/2*u(0)

  Step 1:          y(1)   = x(1) + K*T/2*(u(1) + u(0))
                   x(2)   = y(1)

  Step n:          y(n)   = x(n) + K*T/2*(u(n) + u(n-1))
                   x(n+1) = y(n)
  ```

#### 定义初始条件

可以在模块对话框上将初始条件定义为参数，或者从外部信号输入初始条件：

- 要将初始条件定义为模块参数，请将**初始条件来源**参数设置为 `internal` 并在**初始条件**文本框中输入值。
- 要从外部源提供初始条件，请将**初始条件来源**参数设置为 `external`。模块上出现一个额外的输入端口。

#### 何时使用状态端口

在以下情况下，请使用状态端口而不是输出端口：

- 当模块输出通过重置端口或初始条件端口馈送回模块，从而产生代数环时。有关示例，请参阅 `sldemo_bounce_two_integrators` 模型。
- 当您要从一个条件执行子系统向另一个条件执行子系统传递状态，从而可能导致计时问题时。有关示例，请参阅Building a Clutch Lock-Up Model。

要解决这些问题，您可以通过状态端口而不是输出端口来传递状态。Simulink 在与输出略有不同的时间生成状态，从而避免您的模型出现这些问题。要输出模块状态，请选中**显示状态端口**复选框。状态端口出现在模块顶部。

#### 限制积分

要使输出在一定的级别内，请选中**限制输出**复选框，并在对应的文本框中输入范围限制。此操作会使该模块起到限量积分器的作用。当输出达到界限时，积分作用将关闭以防止积分饱和。在仿真期间，您可以更改限制，但不能更改是否限制输出。下表显示了模块如何决定输出。

| 积分 | 输出 |
| --- | --- |
| 低于**饱和下限** | 保持在**饱和下限** |
| 介于**饱和下限**和**饱和上限**之间 | 积分 |
| 大于**饱和上限** | 保持在**饱和上限** |

要生成指示积分何时达到限制的信号，请选中**显示饱和端口**复选框。模块输出端口下方会显示一个新饱和端口。

饱和信号具有以下三个值之一：

- 1 表示积分在上限。
- 0 表示积分不受限制。
- -1 表示积分在下限。

#### 重置状态

模块根据外部信号将其状态重置为指定的初始条件。要使模块重置其状态，请选择**外部重置**参数选项之一。将出现一个重置端口，指明重置触发器类型。

重置端口具有直接馈通。如果模块输出直接或通过一系列带直接馈通的模块反馈到此端口中，则会产生代数环。要解决此循环，请改为将模块状态端口的输出馈送给重置端口。要访问模块状态，请选中**显示状态端口**复选框。

#### 重置触发器类型

通过**外部重置**参数，您可以确定触发重置的重置信号的属性。触发器选项包括：

- **上升沿** - 当重置信号具有上升沿时重置状态。例如，下图显示了上升沿重置触发器对后向欧拉积分的影响。
- **下降沿** - 当重置信号具有下降沿时重置状态。例如，下图显示了下降沿重置触发器对后向欧拉积分的影响。
- **任一沿** - 当重置信号上升或下降时重置状态。例如，下图显示了任一沿重置触发器对后向欧拉积分的影响。
- **电平** - 当重置信号非零时重置输出并使输出保持在初始条件。例如，下图显示了电平重置触发器对后向欧拉积分的影响。
- **采样电平** - 当重置信号非零时，将输出重置为初始条件。例如，下图显示了采样电平重置触发器对后向欧拉积分的影响。

  **采样电平**重置选项需要的计算比较少，因此效率比**电平**重置选项高。

  **注意**

  对于 Discrete-Time Integrator 模块，所有触发器检测都基于具有正值的信号。例如，从 -1 变成 0 的信号不是上升沿，但从 0 变成 1 的信号是上升沿。

#### 简化初始化模式下的行为

在**配置参数**对话框中将“欠定初始化检测”设置为**简化**时，将启用简化初始化模式。如果您使用简化初始化模式，Discrete-Time Integrator 模块的行为将不同于经典初始化模式。新的初始化行为更稳定，并且在以下情况下提供更加一致的行为：

- 在代数环中
- 在启用和禁用时
- 在比较使用触发采样时间和使用显式采样时间（触发模块的速率与显式采样时间的速率相同）的结果时

在简化初始化模式下，Continuous-Time Integrator 模块更容易转换为 Discrete-Time Integrator 模块，因为初始条件对这两个模块的意义相同。

有关经典和简化初始化模式的详细信息，请参阅Underspecified initialization detection。

**“初始条件设置”设置为“输出”时的启用和禁用行为**

对于触发子系统和函数调用子系统，当您使用简化初始化模式并将**初始条件设置**设置为**输出**时，模块的启用和禁用行为将被简化，如下所示。

在禁用时间 `td`：

```
 y(td) = y(td-1)
```

在启用时间 `te`：

- 如果父级子系统控制端口的**启用时的状态**设置为**重置**：

  ```
  y(te) = IC.
  ```
- 如果父级子系统控制端口的**启用时的状态**设置为**保持**：

  ```
  y(te) = y(td).
  ```

  下图显示了这种情况。

**迭代子系统**

使用简化初始化模式时，不能在迭代子系统模块中放置 Discrete-Time Integrator 模块。

在简化初始化模式下，迭代子系统不维护已用时间。因此，如果在迭代子系统模块中放置需要已用时间的  Discrete-Time Integrator 模块，Simulink 将报告错误。

#### 函数调用子系统内的使能子系统中的行为

假设您有一个函数调用子系统，其中包含一个使能子系统，后者又包含一个 Discrete-Time Integrator 模块。将发生以下行为。

| 积分器方法 | 函数调用触发端口的采样时间类型 | 当函数调用子系统在启用后第一次执行时的 `delta T` 值 | 出现此行为的原因 |
| --- | --- | --- | --- |
| 前向欧拉 | 触发 | `t — tstart` | 当函数调用子系统第一次执行时，积分器算法将使用 `tstart` 作为上一个仿真时间。 |
| 后向欧拉和梯形 | 触发 | `t — tprevious` | 当函数调用子系统第一次执行时，积分器算法将使用 `tprevious` 作为上一个仿真时间。 |
| 前向欧拉、后向欧拉和梯形 | 周期 | 函数调用生成器的采样时间 | 在周期性模式下，Discrete-Time Integrator 模块将使用函数调用生成器的采样时间作为 `delta T`。 |

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **External reset** — 外部重置信号 标量

外部重置信号，指定为标量。当指定的触发事件发生时，模块将状态重置为其初始条件。

**提示**

此端口的图标根据**外部重置**参数的值更改。

##### 依赖关系

要启用此端口，请将**外部重置**设置为**上升沿**、**下降沿**、**任一沿**、**电平**或**采样电平**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **IC** — 状态的初始条件 标量 | 向量 | 矩阵

状态的初始条件，指定为有限标量、向量或矩阵。

##### 依赖关系

要启用此端口，请将**初始条件来源**设置为**外部**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
#### 输出

#### **Port\_1** — 输入的离散时间积分或累积 标量 | 向量 | 矩阵

输入信号的离散时间积分或累积，指定为标量、向量或矩阵。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **Port\_2** — 饱和输出 标量 | 向量 | 矩阵

指示状态何时受限的信号，指定为标量、向量或矩阵。信号具有以下三个值之一：

- `1` 表示正在应用上限。
- `0` 表示积分不受限制。
- `-1` 表示正在应用下限。

##### 依赖关系

要启用此端口，请选中**显示饱和端口**复选框。

**数据类型:** `single` | `double` | `int8`

#### **Port\_3** — 状态输出 标量 | 向量 | 矩阵

模块状态，输出为标量、向量或矩阵。默认情况下，模块将此端口添加到模块图标的顶部。在以下情况下使用状态端口：

- 模块输出通过重置端口或初始条件端口馈送回模块，从而产生代数环。有关示例，请参阅 `sldemo_bounce_two_integrators` 模型。
- 您要从一个条件执行子系统向另一个条件执行子系统传递状态，从而可能导致计时问题。有关示例，请参阅 `sldemo_clutch` 模型。

有关详细信息，请参阅何时使用状态端口。

##### 依赖关系

要启用此端口，请选中**显示状态端口**复选框。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 参数

#### 常设

#### **积分器方法** — 累积方法 **集成:前向欧拉** (默认) | **集成:后向欧拉** | **集成:梯形** | **累加:前向欧拉** | **累加:后向欧拉** | **累加:梯形**

指定积分或累积方法。有关详细信息，请参阅输出方程和积分方法和累积方法。

##### 编程用法

|  |
| --- |
| **模块参数**：`IntegratorMethod` |
| **类型：**字符向量 |
| **值：**`'Integration: Forward Euler'` | `'Integration: Backward Euler'` | `'Integration: Trapezoidal'` | `'Accumulation: Forward Euler'` | `'Accumulation: Backward Euler'` | `'Accumulation: Trapezoidal'` |
| **默认值：**`'Integration: Forward Euler'` |

#### **增益值** — 与积分器输入相乘的值 `1.0` (默认) | 标量 | 向量

指定与积分器输入相乘的标量、向量或矩阵。增益的每个元素必须为正实数。

- 指定除 1.0（默认值）之外的值在语义上等效于将 Gain 模块连接到积分器的输入。
- 有效值包括：

  - `double(1.0)`
  - `single(1.0)`
  - `[1.1 2.2 3.3 4.4]`
  - `[1.1 2.2; 3.3 4.4]`

**提示**

使用此参数指定输入增益将不需要在生成的代码中执行乘法运算。但是，此参数必须为不可调参数才能实现这一优势。如果您要调整输入增益，请将此参数设置为 1.0，并使用外部 Gain 模块来指定输入增益。

##### 编程用法

|  |
| --- |
| **模块参数**：`gainval` |
| **类型：**字符向量 |
| **值：**标量 | 向量 |
| **默认值：**`'1.0'` |

#### **外部重置** — 选择何时将状态重置为初始条件 **无** (默认) | **上升沿** | **下降沿** | **任一沿** | **电平** | **采样电平**

选择将状态重置为其初始条件的触发事件的类型：

- **无** - 不将状态重置为初始条件。
- **上升沿** - 当重置信号具有上升沿时重置状态。
- **下降沿** - 当重置信号具有下降沿时重置状态。
- **任一沿** - 当重置信号上升或下降时重置状态。
- **电平** - 当重置信号非零时重置输出并使输出保持在初始条件。
- **采样电平** - 当重置信号非零时，将输出重置为初始条件。

有关详细信息，请参阅重置状态和重置触发器类型。

##### 编程用法

|  |
| --- |
| **模块参数：**`ExternalReset` |
| **类型：**字符向量 |
| **值**：`'none'` | `'rising'` | `'falling'` | `'either'` | `'level'` | `'sampled level'` |
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

#### **初始条件** — 状态的初始条件 **0** (默认) | 标量 | 向量 | 矩阵

指定模块状态的初始条件。最小值和最大值由**输出最小值**和**输出最大值**模块参数限定。

**提示**

Simulink 软件不允许此模块的初始条件为 `inf` 或 `NaN`。

##### 依赖关系

要启用此参数，请将**初始条件来源**设置为**内部**。

##### 编程用法

|  |
| --- |
| **模块参数：**`InitialCondition` |
| **类型：**字符向量、字符串 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值：**`'0'` |

#### **初始条件设置** — 选择应用初始条件的位置 **自动** (默认) | **输出** | **兼容性**

选择是否将**初始条件**参数的值应用于模块状态或模块输出。初始条件也是重置值。

- **自动** - 模块选择应用**初始条件**参数的位置。

  - 如果模块位于非触发子系统中，并且**积分器方法**设置为积分方法，则设置初始条件：

    `x(0) = IC`

    在重置时：

    `x(n) = IC`
  - 如果模块位于触发子系统或函数调用子系统中，并且**积分器方法**设置为积分方法，请像选择了**输出**一样设置初始条件。
- **输出** - 当模块在触发子系统或函数调用子系统中且**积分器方法**设置为积分方法时，使用此选项。

  设置初始条件：

  `y(0) = IC`

  在重置时：

  `y(n) = IC`
- **兼容性** - 提供此选项是为了实现向后兼容性。您无法为 Simulink 模型中的 Discrete-Time Integrator 模块选择此选项，但可以为库中的 Discrete-Time Integrator 模块选择此选项。使用此选项维护与在 R2014a 之前创建的 Simulink 模型的兼容性。

  在 R2014a 之前，选项**自动**曾为**仅状态(最高效)**。选项**输出**曾为**状态和输出**。具有**兼容性**选项的模块的行为如下所示：

  - 如果**欠定初始化检测**设置为**典型**，则**初始条件设置**参数的行为与**自动**相同。
  - 如果**欠定初始化检测**设置为**简化**，则**初始条件设置**参数的行为与**输出**相同。

**注意**

在 R2014a 之前的 Simulink 版本中，此参数名为**将初始条件用作初始值和重置值**。

##### 编程用法

|  |
| --- |
| **模块参数：**`InitialConditionSetting` |
| **类型：**字符向量 |
| **值：**`'Auto'` | `'Output'` | `'Compatibility'` |
| **默认值：**`'Auto'` |

#### **采样时间(-1 表示继承)** — 采样之间的时间间隔 `-1` (默认) | 标量 | 向量

输入时间步之间的离散时间间隔。

默认情况下，模块使用的离散采样时间为 `1`。要设置不同的采样时间，请输入其他离散值，例如 0.1。

有关详细信息，请参阅 指定采样时间。

##### 提示

- 不要将采样时间指定为 0。此值指定连续采样时间，Discrete-Time Integrator 模块不支持此方式。
- 不要将采样时间指定为 `inf` 或 `NaN`，因为它们不是离散值。
- 如果您指定 -1 以从上游模块继承采样时间，请验证上游模块使用离散采样时间。例如，Discrete-Time Integrator 模块无法继承采样时间 0。

##### 编程用法

|  |
| --- |
| **模块参数：**`SampleTime` |
| **类型：**字符向量 |
| **值：**标量 | 向量 |
| **默认值：**`'-1'` |

#### **限制输出** — 将模块输出值限制在指定范围内 `off` (默认) | `on`

将模块的输出限制为介于**饱和下限**和**饱和上限**参数之间的值。

- 选中此复选框会将模块的输出限制为介于**饱和下限**和**饱和上限**参数之间的值。
- 清除此复选框后，不会限制模块的输出值。

##### 依赖关系

选择此参数将启用**饱和下限**和**饱和上限**参数。

##### 编程用法

|  |
| --- |
| **模块参数：**`LimitOutput` |
| **类型：**字符向量 |
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

#### **线性化时忽略限制和重置** — 将模块视为不可重置 `off` (默认) | `on`

选中此复选框可使 Simulink 线性化命令将此模块视为不可重置且输出无任何限制，而不管此模块的重置和输出限制选项设置如何。

**提示**

若忽略限制并重置，您可以围绕某个工作点对模型进行线性化。此点可能会导致积分器重置或饱和。

##### 编程用法

|  |
| --- |
| **模块参数**：`IgnoreLimit` |
| **类型：**字符向量 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

#### 信号属性

#### **输出最小值** — 范围检查的最小输出值 `[]` (默认) | 标量

软件检查的输出范围的下限值。

软件使用最小值执行下列操作：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围和启用仿真范围检查）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

##### 提示

**输出最小值**不会对实际输出信号进行饱和处理或截断。请改用 Saturation 模块。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `OutMin` |
| **值:** | `'[]'` (默认) | scalar in quotes |

#### **输出最大值** — 范围检查的最大输出值 `[]` (默认) | 标量

软件检查的输出范围的上限值。

软件使用最大值执行下列操作：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围和启用仿真范围检查）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

##### 提示

**输出最大值**不会对实际输出信号进行饱和处理或截断。请改用 Saturation 模块。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `OutMax` |
| **值:** | `'[]'` (默认) | scalar in quotes |

#### **数据类型** — 输出数据类型 **继承: 从内部规则继承** (默认) | **继承: 通过反向传播继承** | **double** | **single** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16)** | **fixdt(1,16,0)** | **fixdt(1,16,2^0,0)** | **<数据类型表达式>**

为输出选择数据类型。该类型可以继承、直接指定或表示为数据类型对象，如 `Simulink.NumericType`。有关详细信息，请参阅 控制信号的数据类型。

当您选择继承的选项时，模块的行为如下所示：

- **继承: 从内部规则继承** - Simulink 在考虑嵌入式目标硬件的属性的同时，会选择相应的数据类型来平衡数值准确性、性能和生成的代码大小。如果更改了嵌入式目标的设置，则依内部规则选择的数据类型可能会发生变化。例如，如果该模块将 `int8` 类型的输入乘以 `int16` 的增益，并且将 **ASIC/FPGA** 指定为目标硬件类型，则输出数据类型为 `sfix24`。如果指定**未指定(假定通用 32 位)**（即通用 32 位微处理器）为目标硬件，则输出数据类型为 `int32`。如果目标微处理器不能提供适应输出范围的字长，Simulink 软件将在诊断查看器中显示错误。

  有时软件不能同时满足优化代码效率和保证数值准确性这两个需求。如果内部规则不能满足您对数值准确性或性能的特定需求，请使用下列选项之一：

  - 显式指定输出数据类型。
  - 使用简单的选项**继承: 与输入相同**。
  - 显式指定默认数据类型（例如 `fixdt(1,32,16)`），然后使用定点工具为您的模型提供数据类型建议。有关详细信息，请参阅 `fxptdlg` (Fixed-Point Designer)。
  - 要指定您自己的继承规则，请使用**继承: 通过反向传播继承**，然后使用 Data Type Propagation 模块。有关如何使用此模块的示例说明，请参阅 Signal Attributes 模块库中的 Data Type Propagation Examples 模块。
- **继承: 通过反向传播继承** - 使用驱动模块的数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Inherit via internal rule` | `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

#### **锁定输出数据类型设置以防止被定点工具更改** — 用于防止定点工具覆盖输出数据类型的选项 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您在模块上指定的**输出**数据类型。有关详细信息，请参阅Use Lock Output Data Type Setting (Fixed-Point Designer)。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `LockScale` |
| **值:** | `'off'` (默认) | `'on'` |

#### **整数舍入模式** — 指定定点运算的舍入模式 **向下** (默认) | **向上** | **收敛** | **最邻近值** | **舍入** | **最简** | **零**

选择下列舍入模式之一。

**向上**
:   将正值和负值朝正无穷方向舍入。等同于 MATLAB® `ceil` 函数。

**收敛**
:   将数值舍入到最邻近的可表示值。如果出现结值，则舍入到最邻近的偶数整数。等同于 Fixed-Point Designer™ `convergent` 函数。

**向下**
:   将正值和负值朝负无穷方向舍入。等同于 MATLAB `floor` 函数。

**最邻近值**
:   将数值舍入到最邻近的可表示值。如果出现结值，则朝正无穷方向舍入。等同于 Fixed-Point Designer `nearest` 函数。

**舍入**
:   将数值舍入到最邻近的可表示值。如果出现结值，则将正数朝正无穷方向舍入，将负数朝负无穷方向舍入。等同于 Fixed-Point Designer `round` 函数。

**最简**
:   自动选择是向负无穷大方向舍入还是向零舍入，以生成尽可能有效的舍入代码。

**零**
:   将数值向零舍入。等同于 MATLAB `fix` 函数。

##### 编程用法

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型**：字符向量 |
| **值**：`'Ceiling'` | `'Convergent'` | `'Floor'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |
| **默认值**：`'Floor'` |

##### 另请参阅

有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

#### **对整数溢出进行饱和处理** — 溢出操作的方法 `off` (默认) | `on`

指定对溢出是进行饱和处理还是绕回处理。

- `on` - 将溢出饱和处理为数据类型能够表示的最小值或最大值。
- `off` - 溢出将绕回到数据类型可以表示的合适值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。

- 选择此参数后，模块输出将在达到 127 时饱和。类似地，模块输出将在达到最小输出值 -128 时饱和。
- 清除此参数后，软件会将导致溢出的值解释为 `int8`，这可能产生意外结果。例如，以 `int8` 表示的模块结果 130（二进制 1000 0010）为 -126。

##### 提示

- 如果您的模型存在可能的溢出，而您希望在生成的代码中进行显式饱和保护，请考虑选中此参数。
- 如果您希望优化生成的代码的效率，请考虑清除此参数。清除此参数还可以帮助您避免过度地指定信号超出范围时模块的处理方式。有关详细信息，请参阅信号范围错误故障排除。
- 如果选中此参数，饱和将应用于模块中的每个内部操作，而不仅仅应用于输出或结果。
- 一般情况下，代码生成进程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SaturateOnIntegerOverflow` |
| **值:** | `'off'` (默认) | `'on'` |

#### **模式** — 选择数据类型模式 `Inherit` (默认) | `Built in` | `Fixed Point`

选择要指定的数据类别。

- **继承** - 数据类型的继承规则。选择 `Inherit` 将在右侧启用另一个菜单/文本框，您可以在其中选择继承模式。
- **内置** - 内置数据类型。选择 `Built in` 将在右侧启用另一个菜单/文本框，您可以在其中选择内置数据类型。
- **定点** - 定点数据类型。选择**定点**将启用可用于指定定点数据类型的其他参数。
- **表达式** - 计算结果为数据类型的表达式。选择 `Expression` 将在右侧启用另一个菜单/文本框，您可以在其中输入表达式。

有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 依赖关系

要启用此参数，请点击**显示数据类型助手**按钮。

#### **数据类型覆盖** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

为此信号选择数据类型覆盖模式。

- 当您选择 **inherit** 时，Simulink 从信号的上下文（即：从 Simulink 中使用该信号的模块、`Simulink.Signal` 对象或 Stateflow® 图）中继承数据类型覆盖设置。
- 当您选择 **off** 时，Simulink 忽略信号上下文的数据类型覆盖设置，并使用为信号指定的定点数据类型。

有关详细信息，请参阅 Simulink 文档中的使用数据类型助手指定数据类型。

##### 依赖关系

要启用此参数，请将**模式**设置为**内置**或**定点**。

##### 提示

由于能够关闭单个数据类型的数据类型覆盖，您可以在应用数据类型覆盖时更好地控制模型中的数据类型。例如，您可以使用此选项确保数据类型满足下游模块的要求，而忽略数据类型覆盖设置。

#### **符号性** — 定点数据的符号性 **有符号** (默认) | **无符号**

指定您希望定点数据为有符号还是无符号数据。有符号数据可以表示正值和负值，无符号数据只表示正值。有关详细信息，请参阅指定定点数据类型。

##### 依赖关系

要启用此参数，请将**模式**设置为**定点**。

#### **字长** — 存储量化整数的字的位大小 `16` (默认) | 从 0 到 32 的整数

指定存储量化整数的字的位大小。有关详细信息，请参阅指定定点数据类型。

##### 依赖关系

要启用此参数，请将**模式**设置为**定点**。

#### **定标** — 定标定点数据的方法 **最佳精度** (默认) | **二进制小数点** | **斜率和偏置**

指定定点数据的定标方法，以避免发生溢出情况并最大限度地减少量化误差。有关详细信息，请参阅指定定点数据类型。

##### 依赖关系

要启用此参数，请将**模式**设置为**定点**。

#### **小数长度** — 指定定点数据类型的小数长度 `0` (默认) | 整数标量

将定点数据类型的小数长度指定为正整数或负整数。有关详细信息，请参阅指定定点数据类型。

##### 依赖关系

要启用此参数，请将**定标**设置为**二进制小数点**。

#### **斜率** — 指定定点数据类型的斜率。 `2^0` (默认) | 正实数值标量

指定定点数据类型的斜率。有关详细信息，请参阅指定定点数据类型。

##### 依赖关系

要启用此参数，请将**定标**设置为**斜率和偏置**。

#### **偏置** — 指定定点数据类型的偏置。 `0` (默认) | 实数值标量

将定点数据类型的偏置指定为任意实数。有关详细信息，请参阅指定定点数据类型。

##### 依赖关系

要启用此参数，请将**定标**设置为**斜率和偏置**。

#### 状态属性

#### **状态名称** — 模块状态的唯一名称 `''` (默认) | 字母数字字符串

使用此参数为模块状态指定唯一名称。默认值为 `' '`。如果此字段为空，则表示未指定任何名称。使用此参数时，请记住以下注意事项：

- 有效的标识符以字母或下划线字符开始，后跟字母数字或下划线字符。
- 状态名称仅适用于所选模块。

有关详细信息，请参阅模型接口元素的 C 数据代码接口配置 (Simulink Coder)。

##### 依赖关系

为**状态名称**指定值并点击**应用**时，将启用**状态名称必须解析为 Simulink 信号对象**参数。

##### 编程用法

|  |
| --- |
| **参数：**`StateName` |
| **类型：**字符向量 |
| **值：**唯一名称 |
| **默认值：**`''` |

#### **状态名称必须解析为 Simulink 信号对象** — 要求状态名称解析为信号对象的选项 `off` (默认) | `on`

指定是否需要将状态名称解析为信号对象。如果选中此选项，则在指定的状态名称与信号对象的名称不匹配时，软件会在运行时生成错误。

选择此参数将禁用**代码生成存储类**参数。

##### 依赖关系

当您为**状态名称**参数指定值并将**信号解析**模型配置参数设置为**无**以外的值时启用。

##### 编程用法

|  |
| --- |
| **模块参数**：`StateMustResolveToSignalObject` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

在触发子系统层次结构中使用时取决于绝对时间。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

| 原生浮点 | |
| --- | --- |
| **HandleDenormals** | 指定是否希望 HDL Coder 在设计中插入额外的逻辑来处理非正规数字。非正规数是大小非常小、必须使用包含前导零的尾数才能表示的浮点数。默认值为 **inherit**。另请参阅HandleDenormals (HDL Coder)。 |
| **LatencyStrategy** | 指定对于浮点运算符是否将设计中的模块映射到 `inherit`、`Max`、`Min` 或 `Zero`。默认值为 **inherit**。另请参阅LatencyStrategy (HDL Coder)。 |
| **MantissaMultiplyStrategy** | 指定在代码生成期间如何实现尾数乘法运算。通过使用不同设置，您可以控制目标 FPGA 设备上 DSP 的使用。默认值为 **inherit**。另请参阅MantissaMultiplyStrategy (HDL Coder)。 |

**限制**

- HDL 代码生成不支持状态端口。清除**显示状态端口**选项。
- HDL 代码生成不支持外部初始条件。将**初始条件来源**设置为**内部**。
- **外部重置**必须设置为 `none`、`rising`、`falling` 或 `level`。
- 不支持连续采样时间。对模块使用离散采样时间。
- HDL 代码生成不支持输入使用浮点数据类型而**增益值**模块参数使用定点数据类型，反之亦然。

**注意**

为 Discrete-Time Integrator 模块生成 HDL 代码时，建议在**硬件实现**配置参数设置中将**设备供应商**配置参数设置为 **ASIC/FPGA**。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Commonly Used Blocks Simulink / Discrete HDL Coder / Discrete HDL Coder / HDL Floating Point Operations

## Description

Use the Discrete-Time Integrator block in place of the Integrator block to create a purely discrete model. With the Discrete-Time
Integrator block, you can:

- Define initial conditions on the block dialog box or as input to the
  block
- Define an input gain (K) value
- Output the block state
- Define upper and lower limits on the integral
- Reset the state with an additional reset input

### Output Equations

With the first time step, block state `n = 0`, with either initial output
`y(0) = IC` or initial state `x(0) = IC`,
depending on the **Initial condition setting** parameter
value.

For a given step `n > 0` with simulation time
`t(n)`, Simulink® updates output `y(n)` as follows:

- Forward Euler method:

  ```
  y(n) = y(n-1) + K*[t(n) - t(n-1)]*u(n-1)
  ```
- Backward Euler method:

  ```
  y(n) = y(n-1) + K*[t(n) - t(n-1)]*u(n)
  ```
- Trapezoidal method:

  ```
  y(n) = y(n-1) + K*[t(n)-t(n-1)]*[u(n)+u(n-1)]/2
  ```

Simulink automatically selects a state-space realization of these output
equations depending on the block sample time, which can be explicit or triggered.
When using explicit sample time, `t(n)-t(n-1)` reduces to the
sample time `T` for all `n > 0`.

### Integration and Accumulation Methods

This block can integrate or accumulate a signal using a forward Euler, backward Euler, or
trapezoidal method. Assume that `u` is the input,
`y` is the output, and `x` is the state. For a
given step `n`, Simulink updates `y(n)` and `x(n+1)`. In
integration mode, `T` is the block sample time (delta
`T` in the case of triggered sample time). In accumulation
mode, `T = 1`. The block sample time determines when the output is
computed but not the output value. `K` is the gain value. Values
clip according to upper or lower limits.

**Forward Euler Method**

Forward Euler method (default), also known as forward rectangular, or
left-hand approximation

The software approximates `1/s` as
`T/(z-1)`. The expressions for the output of the block at step
`n` are:

```
x(n+1) = x(n) + K*T*u(n)
y(n)   = x(n)
```

The block uses these steps to compute the output:

```
Step 0:          y(0)   = IC (clip if necessary)
                 x(1)   = y(0) + K*T*u(0)

Step 1:          y(1)   = x(1)
                 x(2)   = x(1) + K*T*u(1)

Step n:          y(n)   = x(n)
                 x(n+1) = x(n) + K*T*u(n) (clip if necessary)
```

Using this method, input port 1 does not have direct feedthrough.

**Backward Euler Method**

Backward Euler method, also known as backward rectangular or right-hand
approximation

The software approximates `1/s` as
`T*z/(z-1)`. The resulting expression for the output of the
block at step `n` is

```
y(n) = y(n-1) + K*T*u(n).
```

Let `x(n) = y((n)-1)`. The block uses these steps to compute
the output.

- If the parameter **Initial condition setting** is set
  to `Output` or `Auto`
  for triggered and function-call subsystems:

  ```
  Step 0:          y(0) = IC (clipped if necessary)
                   x(1) = y(0)
  ```
- If the parameter **Initial condition setting** is set
  to `Auto` for non-triggered subsystems:

  ```
  Step 0:          x(0)   = IC (clipped if necessary)
                   x(1)   = y(0) = x(0) + K*T*u(0)

  Step 1:          y(1)   = x(1) + K*T*u(1)
                   x(2)   = y(1)

  Step n:          y(n)   = x(n) + K*T*u(n)
                   x(n+1) = y(n)
  ```

Using this method, input port 1 has direct feedthrough.

**Trapezoidal Method**

For this method, the software approximates `1/s` as
`T/2*(z+1)/(z-1)`.

When `T` is fixed (equal to the sampling period), the
expressions to compute the output are:

```
x(n) = y(n-1) + K*T/2*u(n-1)
y(n) = x(n) + K*T/2*u(n)
```

- If the parameter **Initial condition setting** is set
  to `Output` or `Auto`
  for triggered and function-call subsystems:

  ```
  Step 0:          y(0)   = IC (clipped if necessary)
                   x(1)   = y(0) + K*T/2*u(0)
  ```
- If the parameter **Initial condition setting** is set
  to `Auto` for non-triggered subsystems:

  ```
  Step 0:          x(0)   = IC (clipped if necessary)
                   y(0)   = x(0) + K*T/2*u(0)
                   x(1)   = y(0) + K*T/2*u(0)

  Step 1:          y(1)   = x(1) + K*T/2*u(1)
                   x(2)   = y(1) + K*T/2*u(1)

  Step n:          y(n)   = x(n) + K*T/2*u(n)
                   x(n+1) = y(n) + K*T/2*u(n)
  ```

Here, `x(n+1)` is the best estimate of the next output. It is
not the same as the state, in that `x(n)` is not equal to
`y(n)`.

Using this method, input port 1 has direct feedthrough.

**When T is a Variable**

When`T` is a variable (for example, obtained from the
triggering times), the block uses these steps to compute the output.

- If the parameter **Initial condition setting** is set
  to `Output` or `Auto`
  for triggered and function-call subsystems:

  ```
  Step 0:          y(0)   = IC (clipped if necessary)
                   x(1)   = y(0)
  ```
- If the parameter **Initial condition setting** is set
  to `Auto` for non-triggered subsystems:

  ```
  Step 0:          x(0)   = IC (clipped if necessary)
                   x(1)   = y(0) = x(0) + K*T/2*u(0)

  Step 1:          y(1)   = x(1) + K*T/2*(u(1) + u(0))
                   x(2)   = y(1)

  Step n:          y(n)   = x(n) + K*T/2*(u(n) + u(n-1))
                   x(n+1) = y(n)
  ```

### Define Initial Conditions

You can define the initial conditions as a parameter on the block dialog box or
input them from an external signal:

- To define the initial conditions as a block parameter, set the
  **Initial condition source** parameter to
  `internal` and enter the value in the **Initial
  condition** text box.
- To provide the initial conditions from an external source, set the
  **Initial condition source** parameter to
  `external`. An additional input port appears on the
  block.

### When to Use the State Port

Use the state port instead of the output port:

- When the output of the block is fed back into the block through the reset
  port or the initial condition port, causing an algebraic loop. For an
  example, see the `sldemo_bounce_two_integrators`
  model.
- When you want to pass the state from one conditionally executed subsystem
  to another, which can cause timing problems. For an example, see Building a Clutch Lock-Up Model.

You can work around these problems by passing the state through the state port
rather than the output port. Simulink generates the state at a slightly different time from the output,
which protects your model from these problems. To output the block state, select the
**Show state port** check box. The state port appears on the
top of the block.

### Limit the Integral

To keep the output within certain levels, select the **Limit
output** check box and enter the limits in the corresponding text box.
Doing so causes the block to function as a limited integrator. When the output
reaches the limits, the integral action turns off to prevent integral windup. During
a simulation, you can change the limits but you cannot change whether the output is
limited. The table shows how the block determines output.

| Integral | Output |
| --- | --- |
| Less than the **Lower saturation limit** | Held at the **Lower saturation limit** |
| Between the **Lower saturation limit** and the **Upper saturation limit** | The integral |
| Greater than the **Upper saturation limit** | Held at the **Upper saturation limit** |

To generate a signal that indicates when the integral reaches limit, select the
**Show saturation port** check box. A new saturation port
appears below the block output port.

The saturation signal has one of three values:

- 1 indicates that the integral is at the upper limit.
- 0 indicates that the integral is not limited.
- -1 indicates that the integral is at the lower limit.

### Reset the State

The block resets its state to the specified initial condition, based on an
external signal. To cause the block to reset its state, select one of the
**External reset** parameter options. A reset port appears that
indicates the reset trigger type.

The reset port has direct feedthrough. If the block output feeds back into this
port, either directly or through a series of blocks with direct feedthrough, an
algebraic loop results. To resolve this loop, feed the output of the block state
port into the reset port instead. To access the block state, select the
**Show state port** check box.

### Reset Trigger Types

The **External reset** parameter lets you determine the attribute
of the reset signal that triggers the reset. The trigger options include:

- `rising` – Resets the state when the reset signal
  has a rising edge. For example, this figure shows the effect that a rising
  reset trigger has on backward Euler integration.
- `falling` — Resets the state when the reset
  signal has a falling edge. For example, this figure shows the effect that a
  falling reset trigger has on backward Euler integration.
- `either` — Resets the state when the reset signal
  rises or falls. For example, the following figure shows the effect that an
  either reset trigger has on backward Euler integration.
- `level` — Resets and holds the output to the
  initial condition while the reset signal is nonzero. For example, this
  figure shows the effect that a level reset trigger has on backward Euler integration.
- `sampled level` — Resets the output to the
  initial condition when the reset signal is nonzero. For example, this figure
  shows the effect that a sampled level reset trigger has on backward Euler integration.

  The `sampled level` reset option requires fewer
  computations, making it more efficient than the
  `level` reset option.

  **Note**

  For the Discrete-Time Integrator block, all trigger
  detections are based on signals with positive values. For example, a
  signal changing from -1 to 0 is not considered a rising edge, but a
  signal changing from 0 to 1 is.

### Behavior in Simplified Initialization Mode

Simplified initialization mode is enabled when you set **Underspecified
initialization detection** to `Simplified` in
the Configuration Parameters dialog box. If you use simplified initialization mode,
the behavior of the Discrete-Time Integrator block differs from
classic initialization mode. The new initialization behavior is more robust and
provides more consistent behavior in these cases:

- In algebraic loops
- On enable and disable
- When comparing results using triggered sample time against explicit sample
  time, where the block is triggered at the same rate as the explicit sample
  time

Simplified initialization mode enables easier conversion from
Continuous-Time Integrator blocks to Discrete-Time
Integrator blocks, because the initial conditions have the same meaning
for both blocks.

For more information on classic and simplified initialization modes, see Underspecified initialization detection.

**Enable and Disable Behavior with Initial Condition Setting set to
Output**

When you use simplified initialization mode with **Initial condition
setting** set to `Output` for triggered
and function-call subsystems, the enable and disable behavior of the block is
simplified as follows.

At disable time `td`:

```
 y(td) = y(td-1)
```

At enable time `te`:

- If the parent subsystem control port has **States when
  enabling** set to `reset`:

  ```
  y(te) = IC.
  ```
- If the parent subsystem control port has **States when
  enabling** set to `held`:

  ```
  y(te) = y(td).
  ```

  The following figure shows this condition.

**Iterator Subsystems**

When using simplified initialization mode, you cannot place the
Discrete-Time Integrator block in an iterator subsystem
block.

In simplified initialization mode, Iterator subsystems do not maintain elapsed
time. Thus, if a Discrete-Time Integrator block, which needs
elapsed time, is placed inside an iterator subsystem block, Simulink reports an error.

### Behavior in an Enabled Subsystem Inside a Function-Call Subsystem

Suppose you have a function-call subsystem that includes an enabled subsystem,
which contains a Discrete-Time Integrator block. The following behavior
applies.

| Integrator Method | Sample Time Type of Function-Call Trigger Port | Value of `delta T` When Function-Call Subsystem Executes for the First Time After Enabled | Reason for Behavior |
| --- | --- | --- | --- |
| Forward Euler | Triggered | `t — tstart` | When the function-call subsystem executes for the first time, the integrator algorithm uses `tstart` as the previous simulation time. |
| Backward Euler and Trapezoidal | Triggered | `t — tprevious` | When the function-call subsystem executes for the first time, the integrator algorithm uses `tprevious` as the previous simulation time. |
| Forward Euler, Backward Euler, and Trapezoidal | Periodic | Sample time of the function-call generator | In periodic mode, the Discrete-Time Integrator block uses sample time of the function-call generator for `delta T`. |

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input signal, specified as a scalar, vector, or matrix

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **External reset** — External reset signal scalar

External reset signal, specified as a scalar. When the specified
trigger event occurs, the block resets the states to their initial conditions.

**Tip**

The icon for this port changes based on the value of the
**External reset** parameter.

#### Dependencies

To enable this port, set **External reset** to
`rising`,
`falling`,
`either`,
`level`, or `sampled
level`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **IC** — Initial conditions of the states scalar | vector | matrix

Initial conditions of the states, specified as a finite scalar,
vector, or matrix.

#### Dependencies

To enable this port, set **Initial condition
source** to `external`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Discrete-time integration or accumulation of input scalar | vector | matrix

Discrete-time integration or accumulation of the input signal, specified as a scalar,
vector, or matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_2** — Saturation output scalar | vector | matrix

Signal indicating when the state is being limited, specified as a
scalar, vector, or matrix. The signal has one of three values:

- `1` indicates that the upper limit is being
  applied.
- `0` indicates that the integral is not
  limited.
- `-1` indicates that the lower limit is being
  applied.

#### Dependencies

To enable this port, select the **Show saturation
port** check box.

**Data Types:** `single` | `double` | `int8`

### **Port\_3** — State output scalar | vector | matrix

Block states, output as a scalar, vector, or matrix. By default, the block adds this
port to the top of the block icon. Use the state port when:

- The output of the block is fed back into the block through the
  reset port or the initial condition port, causing an algebraic
  loop. For an example, see the
  `sldemo_bounce_two_integrators`
  model.
- You want to pass the state from one conditionally executed
  subsystem to another, which can cause timing problems. For an
  example, see the `sldemo_clutch` model.

For more information, see When to Use the State Port.

#### Dependencies

To enable this port, select the **Show state
port** check box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### Main

### **Integrator method** — Accumulation method `Integration: Forward Euler` (default) | `Integration: Backward Euler` | `Integration: Trapezoidal` | `Accumulation: Forward Euler` | `Accumulation: Backward Euler` | `Accumulation: Trapezoidal`

Specify the integration or accumulation method. See Output Equations and Integration and Accumulation Methods for more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IntegratorMethod` |
| **Type:** character vector |
| **Values:** `'Integration: Forward Euler'` | `'Integration: Backward Euler'` | `'Integration: Trapezoidal'` | `'Accumulation: Forward Euler'` | `'Accumulation: Backward Euler'` | `'Accumulation: Trapezoidal'` |
| **Default:** `'Integration: Forward Euler'` |

### **Gain value** — Value to multiply with integrator input `1.0` (default) | scalar | vector

Specify a scalar, vector, or matrix by which to multiply the
integrator input. Each element of the gain must be a positive real
number.

- Specifying a value other than 1.0 (the default) is
  semantically equivalent to connecting a Gain block to the input
  of the integrator.
- Valid entries include:

  - `double(1.0)`
  - `single(1.0)`
  - `[1.1 2.2 3.3 4.4]`
  - `[1.1 2.2; 3.3 4.4]`

**Tip**

Using this parameter to specify the input gain eliminates a
multiplication operation in the generated code. However, this
parameter must be nontunable to realize this benefit. If you want to
tune the input gain, set this parameter to 1.0 and use an external
Gain block to specify the input gain.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `gainval` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'1.0'` |

### **External reset** — Select when to reset states to initial conditions `none` (default) | `rising` | `falling` | `either` | `level` | `sampled level`

Select the type of trigger event that resets the states to their
initial conditions:

- `none` — Do not reset the state to
  initial conditions.
- `rising` — Reset the state when the
  reset signal has a rising edge.
- `falling` — Reset the state when the
  reset signal has a falling edge.
- `either` — Reset the state when the
  reset signal rises or falls.
- `level` — Reset and hold the output
  to the initial condition while the reset signal is
  nonzero.
- `sampled level` — Reset the output to
  the initial condition when the reset signal is nonzero.

For more information, see Reset the State and Reset Trigger Types.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `ExternalReset` |
| **Type:**  character vector |
| **Values:**  `'none'` | `'rising'` | `'falling'` | `'either'` | `'level'` | `'sampled level'` |
| **Default:** `'none'` |

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

### **Initial condition** — Initial condition of states `0` (default) | scalar | vector | matrix

Specify initial condition of the block states. The minimum and maximum values are
bound by the **Output minimum** and **Output maximum**
block parameters.

**Tip**

Simulink software does not allow the initial condition of this block to be
`inf` or `NaN`.

#### Dependencies

To enable this parameter, set the **Initial condition source** to
`internal`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialCondition` |
| **Type:** character vector, string |
| **Values:** scalar | vector | matrix |
| **Default:** `'0'` |

### **Initial condition setting** — Select where to apply the initial condition `Auto` (default) | `Output` | `Compatibility`

Select whether to apply the value of the **Initial
condition** parameter to the block state or block output.
The initial condition is also the reset value.

- `Auto` — Block chooses where to apply
  the **Initial condition** parameter.

  - If the block is in a non-triggered subsystem and
    **Integrator method** is set to an
    integration method, set initial conditions:

    `x(0) = IC`

    At reset:

    `x(n) = IC`
  - If the block is in a triggered or function-call
    subsystem and **Integrator method** is
    set to an integration method, set initial conditions as
    if `output` was
    selected.
- `Output` — Use this option when the
  block is in a triggered or a function-call subsystem and
  **Integrator method** is set to an
  integration method.

  Set initial conditions:

  `y(0) = IC`

  At reset:

  `y(n) = IC`
- `Compatibility` — This option is
  present to provide backward compatibility. You cannot select
  this option for Discrete-Time Integrator blocks
  in Simulink models but you can select it for
  Discrete-Time Integrator blocks in a library.
  Use this option to maintain compatibility with Simulink models
  created before R2014a.

  Prior to R2014a, the option `Auto`
  was known as `State only (most
  efficient)`. The option
  `Output` was known as
  `State and output`. The behavior of
  the block with the option
  `Compatibility` is as follows.

  - If **Underspecified initialization
    detection** is set to
    `Classic`, the
    **Initial condition setting**
    parameter behaves as
    `Auto`.
  - If **Underspecified initialization
    detection** is set to
    `Simplified`, the
    **Initial condition setting**
    parameter behaves as
    `Output`.

**Note**

This parameter was named **Use initial condition as
initial and reset value for** in Simulink before R2014a.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `InitialConditionSetting` |
| **Type:** character vector |
| **Value:**  `'Auto'` | `'Output'` | `'Compatibility'` |
| **Default:**  `'Auto'` |

### **Sample time (-1 for inherited)** — Interval between samples `-1` (default) | scalar | vector

Enter the discrete time interval between steps.

By default, the block uses a discrete sample time of
`1`. To set a different sample time, enter another
discrete value, such as 0.1.

See Specify Sample Time
for more information.

#### Tips

- Do not specify a sample time of 0. This value specifies a
  continuous sample time, which the Discrete-Time Integrator
  block does not support.
- Do not specify a sample time of `inf` or
  `NaN` because these values are not
  discrete.
- If you specify -1 to inherit the sample time from an
  upstream block, verify that the upstream block uses a
  discrete sample time. For example, the Discrete-Time
  Integrator block cannot inherit a sample time of 0.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `SampleTime` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:**  `'-1'` |

### **Limit output** — Limit block output values to specified range `off` (default) | `on`

Limit the block's output to a value between the **Lower saturation limit** and **Upper saturation limit** parameters.

- Selecting this check box limits the block's output to a value between the **Lower saturation limit** and **Upper saturation limit** parameters.
- Clearing this check box does not limit the block's output values.

#### Dependencies

Selecting this parameter enables the **Lower saturation limit** and **Upper saturation limit** parameters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `LimitOutput` |
| **Type:**  character vector |
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

### **Ignore limit and reset when linearizing** — Treat block as not resettable `off` (default) | `on`

Select this check box to have Simulink linearization commands treat this block as not resettable and as having no limits on its output, regardless of the settings of the block reset and output limitation options.

**Tip**

Ignoring the limit and resetting allows you to linearize a model around an operating point. This point may cause the integrator to reset or saturate.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IgnoreLimit` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### Signal Attributes

### **Output minimum** — Minimum output value for range checking `[]` (default) | scalar

Lower value of the output range that the software checks.

The software uses the minimum to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
  for some blocks.
- Simulation range checking (see Specify Signal Ranges and
  Enable Simulation Range Checking).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

#### Tips

**Output minimum** does not saturate or clip the actual output
signal. Use the Saturation block instead.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutMin` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Output maximum** — Maximum output value for range checking `[]` (default) | scalar

Upper value of the output range that the software checks.

The software uses the maximum value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
  for some blocks.
- Simulation range checking (see Specify Signal Ranges and
  Enable Simulation Range Checking).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

#### Tips

**Output maximum** does not saturate or clip the actual output
signal. Use the Saturation block instead.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutMax` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Data type** — Output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Inherit via back propagation` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Choose the data type for the output. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`. For more information, see Control Data Types of Signals.

When you select an inherited option, the block behaves as follows:

- `Inherit: Inherit via internal rule` — Simulink chooses a data type to balance numerical accuracy, performance, and generated code size, while taking into account the properties of the embedded target hardware. If you change the embedded target settings, the data type selected by the internal rule might change. For example, if the block multiplies an input of type `int8` by a gain of `int16` and `ASIC/FPGA` is specified as the targeted hardware type, the output data type is `sfix24`. If `Unspecified (assume 32-bit Generic)`, i.e., a generic 32-bit microprocessor, is specified as the target hardware, the output data type is `int32`. If none of the word lengths provided by the target microprocessor can accommodate the output range, Simulink software displays an error in the Diagnostic Viewer.

  It is not always possible for the software to optimize code efficiency and numerical accuracy at the same time. If the internal rule doesn’t meet your specific needs for numerical accuracy or performance, use one of the following options:

  - Specify the output data type explicitly.
  - Use the simple choice of `Inherit: Same as input`.
  - Explicitly specify a default data type such as
    `fixdt(1,32,16)` and then use the Fixed-Point
    Tool to propose data types for your model. For more information, see
    `fxptdlg` (Fixed-Point Designer).
  - To specify your own inheritance rule, use `Inherit: Inherit via back propagation` and then use a Data Type Propagation block. Examples of how to use this block are available in the Signal Attributes library Data Type Propagation Examples block.
- `Inherit: Inherit via back propagation` — Use data type of the driving block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via internal rule` | `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **Default**: `'Inherit: Inherit via internal rule'` |

### **Lock output data type setting against changes by the fixed-point tools** — Option to prevent fixed-point tools from overriding Output data type `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the
**Output** data type you specify on the block. For more
information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LockScale` |
| **Values:** | `'off'` (default) | `'on'` |

### **Integer rounding mode** — Specify the rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Choose one of these rounding modes.

`Ceiling`
:   Rounds both positive and negative numbers
    toward positive infinity. Equivalent to the
    MATLAB®
    `ceil` function.

`Convergent`
:   Rounds number to the nearest representable
    value. If a tie occurs, rounds to the nearest even
    integer. Equivalent to the Fixed-Point Designer™
    `convergent` function.

`Floor`
:   Rounds both positive and negative numbers
    toward negative infinity. Equivalent to the
    MATLAB
    `floor` function.

`Nearest`
:   Rounds number to the nearest representable
    value. If a tie occurs, rounds toward positive
    infinity. Equivalent to the Fixed-Point Designer
    `nearest` function.

`Round`
:   Rounds number to the nearest representable
    value. If a tie occurs, rounds positive numbers
    toward positive infinity and rounds negative
    numbers toward negative infinity. Equivalent to
    the Fixed-Point Designer
    `round` function.

`Simplest`
:   Automatically chooses between round toward
    floor and round toward zero to generate rounding
    code that is as efficient as possible.

`Zero`
:   Rounds number toward zero. Equivalent to the
    MATLAB
    `fix` function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `RndMeth` |
| **Type**: character vector |
| **Values**: `'Ceiling'` | `'Convergent'` | `'Floor'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |
| **Default**: `'Floor'` |

#### See Also

For more information, see Rounding Modes (Fixed-Point Designer).

### **Saturate on integer overflow** — Method of overflow action `off` (default) | `on`

Specify whether overflows saturate or wrap.

- `on` — Overflows saturate to either the minimum or maximum
  value that the data type can represent.
- `off` — Overflows wrap to the appropriate value that the data
  type can represent.

For example, the maximum value that the signed 8-bit integer `int8`
can represent is 127. Any block operation result greater than this maximum value causes
overflow of the 8-bit integer.

- With this parameter selected, the block output saturates at 127.
  Similarly, the block output saturates at a minimum output value of
  -128.
- With this parameter cleared, the software interprets the overflow-causing
  value as `int8`, which can produce an unintended result.
  For example, a block result of 130 (binary 1000 0010) expressed as
  `int8` is -126.

#### Tips

- Consider selecting this parameter when your model has a possible overflow
  and you want explicit saturation protection in the generated code.
- Consider clearing this parameter when you want to optimize efficiency of
  your generated code. Clearing this parameter also helps you to avoid
  overspecifying how a block handles out-of-range signals. For more
  information, see Troubleshoot Signal Range Errors.
- When you select this parameter, saturation applies to every internal
  operation on the block, not just the output or result.
- In general, the code generation process can detect when overflow is not
  possible. In this case, the code generator does not produce saturation
  code.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **Values:** | `'off'` (default) | `'on'` |

### **Mode** — Select data type mode `Inherit` (default) | `Built in` | `Fixed Point`

Select the category of data to specify.

- `Inherit` — Inheritance rules for data types.
  Selecting `Inherit` enables a second menu/text box to the right
  where you can select the inheritance mode.
- `Built in` — Built-in data types. Selecting
  `Built in` enables a second menu/text box to the right
  where you can select a built-in data type.
- `Fixed point` — Fixed-point data types. Selecting
  `Fixed point` enables additional parameters that
  you can use to specify a fixed-point data type.
- `Expression` — Expressions that evaluate to data
  types. Selecting `Expression` enables a second menu/text box to
  the right, where you can enter the expression.

For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, click the **Show data type
assistant** button.

### **Data type override** — Specify data type override mode for this signal `Inherit` | `Off`

Select the data type override mode for this signal.

- When you select `Inherit`, Simulink inherits the data
  type override setting from its context, that is, from the block,
  `Simulink.Signal` object or Stateflow® chart in Simulink that is using the signal.
- When you select `Off`, Simulink ignores the data type
  override setting of its context and uses the fixed-point data type specified for
  the signal.

For more information, see Specify Data Types Using Data Type Assistant in the
Simulink documentation.

#### Dependencies

To enable this parameter, set **Mode** to `Built
in` or `Fixed point`.

#### Tips

The ability to turn off data type override for an individual data type provides
greater control over the data types in your model when you apply data type override.
For example, you can use this option to ensure that data types meet the requirements
of downstream blocks regardless of the data type override setting.

### **Signedness** — Signedness of fixed-point data `Signed` (default) | `Unsigned`

Specify whether you want the fixed-point data as signed or unsigned.
Signed data can represent positive and negative values, but unsigned
data represents positive values only. For more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Word length** — Bit size of the word that holds the quantized integer `16` (default) | integer from 0 to 32

Specify the bit size of the word that holds the quantized integer. For
more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Scaling** — Method for scaling fixed-point data `Best precision` (default) | `Binary point` | `Slope and bias`

Specify the method for scaling your fixed-point data to avoid overflow
conditions and minimize quantization errors. For more information, see
Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Fraction length** — Specify fraction length for fixed-point data type `0` (default) | scalar integer

Specify fraction length for fixed-point data type as a positive or
negative integer. For more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Scaling** to
`Binary point`.

### **Slope** — Specify slope for the fixed-point data type `2^0` (default) | positive, real-valued scalar

Specify slope for the fixed-point data type. For more information, see
Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Scaling** to
`Slope and bias`.

### **Bias** — Specify bias for the fixed-point data type `0` (default) | real-valued scalar

Specify bias for the fixed-point data type as any real number. For more
information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Scaling** to
`Slope and bias`.

### State Attributes

### **State name** — Unique name for block state `''` (default) | alphanumeric string

Use this parameter to assign a unique name to the block state. The default is `' '`. When this field is blank, no name is assigned. When using this parameter, remember these considerations:

- A valid identifier starts with an alphabetic or underscore character, followed by alphanumeric or underscore characters.
- The state name applies only to the selected block.

For more information, see C Data Code Interface Configuration for Model Interface Elements (Simulink Coder).

#### Dependencies

When you specify a value for **State name** and click
**Apply**, you enable the **State name must resolve
to Simulink signal object** parameter.

#### Programmatic Use

|  |
| --- |
| **Parameter:**  `StateName` |
| **Type:**  character vector |
| **Values:**  unique name |
| **Default:**  `''` |

### **State name must resolve to Simulink signal object** — Option to require that state names resolve to signal object `off` (default) | `on`

Specify whether state names are required to resolve to signal objects. If selected,
the software generates an error at run time if you specify a state name that does not
match the name of a signal object.

Selecting this parameter disables the **Code generation storage
class** parameter.

#### Dependencies

Enabled when you specify a value for the **State name** parameter
and set the **Signal resolution** model configuration parameter to
a value other than `None`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `StateMustResolveToSignalObject` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Depends on absolute time when used inside a triggered subsystem hierarchy.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

| Native Floating Point | |
| --- | --- |
| **HandleDenormals** | Specify whether you want HDL Coder to insert additional logic to handle denormal numbers in your design. Denormal numbers are numbers that have magnitudes less than the smallest floating-point number that can be represented without leading zeros in the mantissa. The default is `inherit`. See also HandleDenormals (HDL Coder). |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `inherit`, `Max`, `Min`, or `Zero` for the floating-point operator. The default is `inherit`. See also LatencyStrategy (HDL Coder). |
| **MantissaMultiplyStrategy** | Specify how to implement the mantissa multiplication operation during code generation. By using different settings, you can control the DSP usage on the target FPGA device. The default is `inherit`. See also MantissaMultiplyStrategy (HDL Coder). |

**Restrictions**

- State ports are not supported for HDL code generation. Clear the
  **Show state port** option.
- External initial conditions are not supported for HDL code generation.
  Set **Initial condition source** to
  `Internal`.
- **External Reset** must be set to
  `none`, `rising`,
  `falling` or `level`.
- Continuous sample time is not supported. Use a discrete sample time
  for the block.
- Using a floating-point data type for input and a fixed-point data type
  for **Gain value** block parameter, or vice versa, is
  not supported for HDL code generation.

**Note**

When generating HDL code for the Discrete Time Integrator block, it is
recommended to set the **Device Vendor** configuration
parameter to `ASIC/FPGA` in the **Hardware
Implementation** configuration parameter settings.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
