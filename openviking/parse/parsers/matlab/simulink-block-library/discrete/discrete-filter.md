---
type: simulink-block
title: 'Discrete Filter'
family: discrete
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'discretefilter'
---

# Discrete Filter

Model Infinite Impulse Response (IIR) filters

## 中文

构建无限冲激响应 (IIR) 滤波器模型

### 所属库

Simulink / Discrete DSP System Toolbox / Filtering / Filter Implementations

### 描述

Discrete Filter 模块使用指定的数字 IIR 滤波器单独对输入信号的每个通道进行滤波。您可以将滤波器结构指定为 `Direct form I`、`Direct form I transposed`、`Direct form II` 或 `Direct form II transposed`。该模块实现了具有固定系数的静态滤波器。您可以调整这些静态滤波器的系数。

此模块随时间的推移单独对输入信号的每个通道进行滤波。**输入处理**参数用于指定该模块如何处理输入的每个元素。您可以指定将输入元素作为独立通道处理（基于采样的处理），或将输入的每个列作为独立通道处理（基于帧的处理）。要执行基于帧的处理，您必须拥有 DSP System Toolbox™ 许可证。

输出维度等于输入维度，但为**分子系数**参数指定滤波器抽头矩阵时除外。当您执行此操作时，输出维度取决于您指定的不同滤波器抽头集的数量。

使用**分子系数**参数可以指定离散滤波器分子多项式的系数。使用**分母系数**参数可以指定函数的分母多项式的系数。**分母系数**参数必须为系数向量。

按 *z-1* 的升幂顺序指定分子和分母多项式的系数。Discrete Filter 模块允许使用 *z-1*（延迟算子）形式的多项式来表示离散系统。信号处理工程师通常使用这种方法。反之，Discrete Transfer Fcn 模块允许使用 *z* 形式的多项式来表示离散系统。控制工程师通常使用这种方法。当分子和分母多项式的长度相同时，两种方法相同。

#### 指定初始状态

在**对话框参数**和**输入端口**模式下，该模块默认将内部滤波器状态初始化为零，这等效于假定过去的输入和输出为零。您可以选择使用**初始状态**参数为滤波器延迟指定非零初始状态。

要确定您必须指定的初始状态值数量以及如何指定这些状态值，请参阅下面的有关有效初始状态和延迟元素数（滤波器状态）的表。**初始状态**参数可采用下表所述的四种形式之一。

**有效初始状态**

| 初始状态 | 示例 | 描述 |
| --- | --- | --- |
| 标量 | `5`  每个通道的每个延迟元素均设置为 `5`。 | 模块将滤波器中的所有延迟元素初始化为标量值。 |
| 向量  （用于将相同的延迟元素应用于每个通道） | 用于具有两个延迟元素的滤波器：[*d1* *d2*]  所有通道的延迟元素均为 d1 和 d2。 | 每个向量元素均为相应的延迟元素指定一个唯一的初始条件。模块将相同的初始条件向量应用于输入信号的每个通道。向量长度必须等于滤波器中的延迟元素数（在表延迟元素数（滤波器状态）中指定）。 |
| 向量或矩阵  （用于将不同的延迟元素应用于每个通道） | 对于三通道输入信号和具有两个延迟元素的滤波器：  [*d*1 *d2* *D1* *D2* *d1* *d2*] 或    [d1D1d1d2D2d2]    - 通道 1 的延迟元素为 *d1* 和 *d2*。 - 通道 2 的延迟元素为 *D1* 和 *D2*。 - 通道 3 的延迟元素为 *d1* 和 *d2*。 | 每个向量或矩阵元素均为相应通道中的相应延迟元素指定唯一的初始条件：  - 向量长度必须等于输入通道数与滤波器中延迟元素数（在表延迟元素数（滤波器状态）中指定）的乘积。 - 矩阵的行数必须与滤波器中的延迟元素数（在表延迟元素数（滤波器状态）中指定）相同，并且每一列还须对应输入信号的一个通道。 |
| 空矩阵 | `[ ]`  每个通道的每个延迟元素均设置为 `0`。 | 空矩阵 `[]` 等效于将**初始条件**参数设置为标量值 `0`。 |

每输入通道的延迟元素数取决于滤波器结构，如下表所示。

**延迟元素数（滤波器状态）**

| 滤波器结构 | 每通道的延迟元素数 |
| --- | --- |
| **直接 I 型   直接 I 型转置** | - `number of zeros - 1` - `number of poles - 1` |
| **直接 II 型   直接 II 型转置** | `max(number of zeros, number of poles)-1` |

下表根据您将**输入处理**参数设置为基于帧还是基于采样，分两种情况说明采用不同输入大小和不同通道数时的有效初始状态。

**基于帧的处理**

| 输入 | 通道数 | 有效初始状态（对话框） | 有效初始状态（输入端口） |
| --- | --- | --- | --- |
| - 列向量 (*K*×1) - 无向向量 (*K*) | 1 | - 标量 - 列向量 (*M*×1) - 行向量 (1×*M*) | - 标量 - 列向量 (*M*×1) |
| - 行向量 (1×*N*) - 矩阵 (*K*×*N*) | *N* | - 标量 - 列向量 (*M*×1) - 行向量 (1×*M*) - 矩阵 (*M*×*N*) | - 标量 - 矩阵 (*M*×*N*) |

**基于采样的处理**

| 输入 | 通道数 | 有效初始状态（对话框） | 有效初始状态（输入端口） |
| --- | --- | --- | --- |
| - 无向标量 | 1 | - 标量 - 列向量 (*M*×1) - 行向量 (1×*M*) | - 标量 - 列向量 (*M*×1) - 行向量 (1×*M*) |
| - 行向量 (1×*N*) - 列向量 (*N*×1) - 无向向量 (*N*) | *N* | - 标量 - 列向量 (*M*×1) - 行向量 (1×*M*) - 矩阵 (*M*×*N*) | - 标量 |
| - 矩阵 (*K*×*N*) | *K*×*N* | - 标量 - 列向量 (*M*×1) - 行向量 (1×*M*) - 矩阵 (*M*×(*K*×*N*)) | - 标量 |

当**初始状态**为标量时，模块将所有滤波器状态初始化为相同的标量值。输入 `0` 可将所有状态初始化为零。当**初始状态**为向量或矩阵时，每个向量或矩阵元素都指定一个唯一的初始状态。此唯一状态对应于相应通道中的一个延迟元素：

- 向量长度必须等于滤波器中的延迟元素数，`M = max(number of zeros, number of poles)`。
- 矩阵的行数必须与滤波器中的延迟元素数相同，`M = max(number of zeros, number of poles)`。矩阵的每一列还须对应输入信号的一个通道。

初始滤波器输出 *y1*、初始输入 *u1* 和初始状态 [*x1*, *x2*] 之间的关系如以下方程所示。

y1=b1[(u1−a2x1−a3x2)a1]+b2x1+b3x2

其中

- *b1*、*b2* 和 *b3* 是离散滤波器的分子系数。
- *a1*、*a2* 和 *a3* 是离散滤波器的分母系数。

### 端口

#### 输入

#### **u** — 输入信号 标量 | 向量 | 矩阵

要滤波的输入信号，指定为标量、向量或矩阵。

当您将**输入处理**参数设置为**列作为通道(基于帧)**时，模块支持可变大小的输入信号，即您可以在仿真期间更改信号的帧大小（行数），但通道（列）的数量必须保持不变。 *(自 R2024a 起)*

##### 依赖关系

此端口的名称取决于您为分子系数、分母系数和初始状态指定的源。将**分子**、**分母**和**初始状态**设置为**对话框**时，只有一个输入端口，且该端口没有标签。将**分子**、**分母**或**初始状态**设置为**输入端口**时，此端口的标签为 **u**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

#### **Num** — 分子系数 标量 | 向量

离散滤波器的分子系数，指定为 *z* 的降幂。使用行向量可指定单个分子多项式的系数。

##### 依赖关系

要启用此端口，请将**分子源**设置为**输入端口**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

#### **Den** — 分母系数 标量 | 向量

离散滤波器的分母系数，指定为 *z* 的降幂。使用行向量可指定单个分母多项式的系数。

##### 依赖关系

要启用此端口，请将**分母源**设置为**输入端口**。

要将**分母源**设置为**输入端口**，请选择**通过跳过除以分母首项系数(a0)进行优化**参数。该模块忽略分母首项系数值 a0，并用 1 替换它。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

#### **External reset** — 外部重置信号 标量

外部重置信号，指定为标量。当指定的触发事件发生时，模块将状态重置为其初始条件。

**提示**

此端口的图标根据**外部重置**参数的值更改。

##### 依赖关系

要启用此端口，请将**外部重置**设置为**上升沿**、**下降沿**、**任一沿**、**电平**或**电平保持**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **x0** — 初始状态 标量 | 向量 | 矩阵

初始状态，指定为标量、向量或矩阵。有关指定状态的详细信息，请参阅指定初始状态。

##### 依赖关系

要启用此端口，请将**滤波器结构**设置为**直接 II 型**或**直接 II 型转置**，并将**初始状态**设置为**输入端口**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
#### 输出

#### **Port\_1** — 滤波后的输出信号 标量 | 向量 | 矩阵

滤波后的输出信号。输出维度等于输入维度，但为**分子系数**参数指定滤波器抽头矩阵时除外。当您执行此操作时，输出维度取决于您指定的不同滤波器抽头集的数量。

当您将**采样时间**设置为 `-1` 时，输出信号的采样时间与输入信号 **u** 的采样时间相同。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### 参数

#### 常设

#### **滤波器结构** — 滤波器结构 **直接 II 型** (默认) | **直接 I 型转置** | **直接 I 型** | **直接 II 型转置**

指定离散 IIR 滤波器结构。

##### 依赖关系

要使用**直接 II 型**以外的任何滤波器结构，您必须具有可用的 DSP System Toolbox 许可证。

##### 编程用法

|  |
| --- |
| **模块参数**：`FilterStructure` |
| **类型：**字符向量 |
| **值：**`'Direct form II' | 'Direct form I transposed' | 'Direct form I' | 'Direct form II transposed'` |
| **默认值：**`'Direct form II'` |

#### **分子源** — 分子系数的信源 **对话框** (默认) | **输入端口**

将分子系数的信源指定为**对话框**或**输入端口**。

##### 编程用法

|  |
| --- |
| **模块参数**：`NumeratorSource` |
| **类型：**字符向量 |
| **值：**`'Dialog' | 'Input port'` |
| **默认值：**`'Dialog'` |

#### **分子值** — 分子系数 `[1]` (默认) | 标量 | 向量 | 矩阵

将离散滤波器的分子系数指定为 *z* 的降幂。使用行向量可指定单个分子多项式的系数。要指定多个滤波器的系数，请指定系数矩阵，其中每行表示一组不同滤波器抽头。要实现多个滤波器，**滤波器结构**必须为**直接 II 型**，**输入处理**必须为**元素作为通道(基于采样)**，并且输入必须为标量。

##### 依赖关系

要启用此参数，请将**分子源**设置为**对话框**。

##### 编程用法

|  |
| --- |
| **模块参数**：`Numerator` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值：**`'[1]'` |

#### **分母源** — 分母系数的信源 **对话框** (默认) | **输入端口**

将分母系数的信源指定为**对话框**或**输入端口**。

要将**分母源**设置为**输入端口**，请选择**通过跳过除以分母首项系数(a0)进行优化**参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`DenominatorSource` |
| **类型：**字符向量 |
| **值：**`'Dialog' | 'Input port'` |
| **默认值：**`'Dialog'` |

#### **分母值** — 分母系数 `[1 0.5]` (默认) | 向量

将离散滤波器的分母系数指定为 *z* 的降幂。使用行向量可指定单个分母多项式的系数。

当您选择**通过跳过除以分母首项系数(a0)进行优化**参数时，如果您在模块对话框中指定分母系数且 *a0* ≠ 1，则会发生错误。

##### 依赖关系

要启用此参数，请将**分母源**设置为**对话框**。

##### 编程用法

|  |
| --- |
| **模块参数**：`Denominator` |
| **类型：**字符向量 |
| **值：**标量 | 向量 |
| **默认值**：`'[1 0.5]'` |

#### **初始状态源** — 初始状态的信源 **对话框** (默认) | **输入端口**

将初始状态的信源指定为**对话框**或**输入端口**。

##### 编程用法

|  |
| --- |
| **模块参数**：`InitialStatesSource` |
| **类型：**字符向量 |
| **值：**`'Dialog' | 'Input port'` |
| **默认值：**`'Dialog'` |

#### **初始状态值** — 初始滤波器状态 `0` (默认) | 标量 | 向量 | 矩阵

将初始滤波器状态指定为标量、向量或矩阵。要了解如何指定初始状态，请参阅指定初始状态。

##### 依赖关系

要启用此参数，请将**滤波器结构**设置为**直接 II 型**或**直接 II 型转置**，并将**初始状态源**设置为**对话框**。

##### 编程用法

|  |
| --- |
| **模块参数**：`InitialStates` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值：**`'0'` |

此外，还可以使用 `IC`。

#### **初始分子状态** — 初始分子状态 `0` (默认) | 标量 | 向量 | 矩阵

将初始分子滤波器状态指定为标量、向量或矩阵。要了解如何指定初始状态，请参阅指定初始状态。

##### 依赖关系

要启用此端口，请将**滤波器结构**设置为**直接 I 型**或**直接 I 型转置**。

##### 编程用法

|  |
| --- |
| **模块参数**：`InitialStates` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值：**`'0'` |

#### **初始分母状态** — 初始分母状态 `0` (默认) | 标量 | 向量 | 矩阵

将初始分母滤波器状态指定为标量、向量或矩阵。要了解如何指定初始状态，请参阅指定初始状态。

##### 依赖关系

要启用此端口，请将**滤波器结构**设置为**直接 I 型**或**直接 I 型转置**。

##### 编程用法

|  |
| --- |
| **模块参数**：`InitialDenominatorStates` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值：**`'0'` |

#### **外部重置** — 外部状态重置 **无** (默认) | **上升沿** | **下降沿** | **任一沿** | **电平** | **电平保持**

指定用于将状态重置为初始条件的触发事件。

| 重置模式 | 行为 |
| --- | --- |
| **无** | 不重置。 |
| **上升沿** | 基于上升沿重置。 |
| **下降沿** | 基于下降沿重置。 |
| **任一沿** | 基于上升或下降沿重置。 |
| **电平** | 在下列任一情况下重置：  - 当重置信号在当前时间步为非零值时 - 当重置信号值从上一时间步的非零更改为当前时间步的零时 |
| **电平保持** | 当重置信号在当前时间步为非零值时重置 |

##### 编程用法

|  |
| --- |
| **模块参数**：`ExternalReset` |
| **类型**：字符向量 |
| **值**：`'None'` | `'Rising'` | `'Falling'` | `'Either'` | `'Level'` | `'Level hold'` |
| **默认值**：`'None'` |

#### **输入处理** — 基于采样或基于帧的处理 **元素作为通道(基于采样)** (默认) | **列作为通道(基于帧)**

指定模块是执行基于采样还是基于帧的处理。

- **元素作为通道(基于采样)** - 将输入的每个元素作为独立通道处理。
- **列作为通道(基于帧)** - 将输入的每列作为独立通道处理。

##### 依赖关系

基于帧的处理需要具有 DSP System Toolbox 许可证。

有关详细信息，请参阅Sample- and Frame-Based Concepts (DSP System Toolbox)。

##### 编程用法

|  |
| --- |
| **模块参数**：`InputProcessing` |
| **类型：**字符向量 |
| **值：**`'Columns as channels (frame based)' | 'Elements as channels (sample based)'` |
| **默认值：**`'Elements as channels (sample based)'` |

#### **通过跳过除以分母首项系数(a0)进行优化** — 跳过除以 a0 的运算 `off` (默认) | `on`

当选中此复选框时，该模块在仿真或生成的代码中不会除以 *a0*。此参数可以优化您的代码。如果在“模块”对话框中指定分母系数并且 *a0*≠1，则会出错。

如果从输入端口**分母**指定分母系数，则您必须选择**通过跳过除以分母首项系数(a0)进行优化**参数。选中此复选框时，模块会忽略分母首项系数 *a0* 并用 1 替换它。

当清除此复选框时，该模块在仿真期间完全可调。它在仿真和代码生成中均除以 *a0*。

##### 编程用法

|  |
| --- |
| **模块参数**：`a0EqualsOne` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **采样时间(-1 表示继承)** — 采样之间的时间间隔 `-1` (默认) | 标量 | 向量

指定采样时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

##### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时才可见。要了解详细信息，请参阅不建议设置采样时间的模块。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SampleTime` |
| **值:** | `"-1"` (默认) | scalar or vector in quotes |

#### **查看滤波器响应** — 查看滤波器响应 按钮

点击此按钮以打开滤波器可视化工具 (`fvtool` (DSP System Toolbox))，并显示在模块对话框中定义的滤波器的滤波器响应。

##### 依赖关系

要启用此参数，请将**分子源**和**分母源**参数设置为**对话框**。

仅当您有有效的 DSP System Toolbox 许可证时，此参数才会出现。

#### 数据类型

#### **状态** — 状态数据类型 `Inherit: Same as input` (默认) | **int8** | **int16** | **int32** | **int64** | **fixdt(1,16,0)** | **<数据类型表达式>**

指定状态数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如**继承: 与输入相同**
- 内置整数，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`StateDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值：**`'Inherit: Same as input'` |

#### **分子系数** — 分子系数数据类型 **继承: 从内部规则继承** (默认) | **int8** | **int16** | **int32** | **int64** | **fixdt(1,16)** | **fixdt(1,16,0)** | **<数据类型表达式>**

指定分子系数数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如**继承: 从内部规则继承**
- 内置有符号整数，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`NumCoefDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Inherit via internal rule' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值：**`'Inherit: Inherit via internal rule'` |

#### **分子系数最小值** — 分子系数的最小值 `[]` (默认) | 标量

指定分子系数可以具有的最小值。默认值为 `[]`（未指定）。Simulink® 软件使用此值执行：

- 参数范围检查（请参阅指定模块参数的最小值和最大值）
- 定点数据类型的自动定标

##### 编程用法

|  |
| --- |
| **模块参数**：`NumCoefMin` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'[]'` |

#### **分子系数最大值** — 分子系数的最大值 `[]` (默认) | 标量

指定分子系数可以具有的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 参数范围检查（请参阅指定模块参数的最小值和最大值）
- 定点数据类型的自动定标

##### 编程用法

|  |
| --- |
| **模块参数**：`NumCoefMax` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'[]'` |

#### **分子乘积输出** — 分子乘积输出数据类型 **继承: 从内部规则继承** (默认) | **继承: 与输入相同** | **int8** | **int16** | **int32** | **int64** | **fixdt(1,16,0)** | **<数据类型表达式>**

指定分子系数的乘积输出数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如**继承: 从内部规则继承**
- 内置数据类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`NumProductDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值：**`'Inherit: Inherit via internal rule'` |

#### **分子累加器** — 分子累加器数据类型 **继承: 从内部规则继承** (默认) | **继承: 与输入相同** | **继承: 与乘积输出相同** | **int8** | **int16** | **int32** | **int64** | **fixdt(1,16,0)** | **<数据类型表达式>**

指定分子系数的累加器数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如**继承: 从内部规则继承**
- 内置数据类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`NumAccumDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'Inherit: Same as product output' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值：**`'Inherit: Inherit via internal rule'` |

#### **分母系数** — 分母系数数据类型 **继承: 从内部规则继承** (默认) | **int8** | **int16** | **int32** | **int64** | **fixdt(1,16)** | **fixdt(1,16,0)** | **<数据类型表达式>**

指定分母系数数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如**继承: 从内部规则继承**
- 内置整数，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`DenCoefDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Inherit via internal rule' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值：**`'Inherit: Inherit via internal rule'` |

#### **分母系数最小值** — 分母系数的最小值 `[]` (默认) | 标量

指定分母系数可以具有的最小值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 参数范围检查（请参阅指定模块参数的最小值和最大值）
- 定点数据类型的自动定标

##### 编程用法

|  |
| --- |
| **模块参数**：`DenCoefMin` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'[]'` |

#### **分母系数最大值** — 分母系数的最大值 `[]` (默认) | 标量

指定分母系数可以具有的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 参数范围检查（请参阅指定模块参数的最小值和最大值）
- 定点数据类型的自动定标

##### 编程用法

|  |
| --- |
| **模块参数**：`DenCoefMax` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'[]'` |

#### **分母乘积输出** — 分母乘积输出数据类型 **继承: 从内部规则继承** (默认) | **继承: 与输入相同** | **int8** | **int16** | **int32** | **int64** | **fixdt(1,16,0)** | **<数据类型表达式>**

指定分母系数的乘积输出数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如**继承: 从内部规则继承**
- 内置数据类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`DenProductDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值：**`'Inherit: Inherit via internal rule'` |

#### **分母累加器** — 分母累加器数据类型 **继承: 从内部规则继承** (默认) | **继承: 与输入相同** | **继承: 与乘积输出相同** | **int8** | **int16** | **int32** | **int64** | **fixdt(1,16,0)** | **<数据类型表达式>**

指定分母系数的累加器数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如**继承: 从内部规则继承**
- 内置数据类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`DenAccumDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'Inherit: Same as product output' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值：**`'Inherit: Inherit via internal rule'` |

#### **输出** — 输出数据类型 **继承: 从内部规则继承** (默认) | **继承: 与输入相同** | **int8** | **int16** | **int32** | **int64** | **fixdt(1,16)** | **fixdt(1,16,0)** | **<数据类型表达式>**

指定输出数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如**继承: 从内部规则继承**
- 内置数据类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值：**`'Inherit: Inherit via internal rule'` |

#### **输出最小值** — 输出的最小值 `[]` (默认) | 标量

指定模块可以输出的最小值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅指定信号范围）
- 定点数据类型的自动定标

##### 编程用法

|  |
| --- |
| **模块参数**：`OutMin` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'[]'` |

#### **输出最大值** — 输出的最大值 `[]` (默认) | 标量

指定模块可以输出的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅指定信号范围）
- 定点数据类型的自动定标

##### 编程用法

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'[]'` |

#### **被乘数数据类型** — 被乘数数据类型 `Inherit: Same as input` (默认) | **int8** | **int16** | **int32** | **int64** | **fixdt(1,16,0)** | **<数据类型表达式>**

指定被乘数数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如**继承: 与输入相同**
- 内置数据类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 依赖关系

要启用此参数，请将**滤波器结构**设置为**直接 I 型转置**

##### 编程用法

|  |
| --- |
| **模块参数**：`MultiplicandDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值：**`'Inherit: Same as input'` |

#### **锁定数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选择此选项可锁定数据类型设置，防止使用定点工具和定点顾问进行更改。有关详细信息，请参阅Lock the Output Data Type Setting (Fixed-Point Designer)。

##### 编程用法

|  |
| --- |
| **模块参数：**`LockScale` |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **整数舍入模式** — 定点运算的舍入模式 **向下** (默认) | **向上** | **收敛** | **最邻近值** | **舍入** | **最简** | **零**

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

##### 编程用法

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型：**字符向量 |
| **值：**`'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认值：**`'Floor'` |

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

#### 状态属性

#### **状态名称** — 为每个状态指定唯一名称 `' '` (默认) | `'position'` | `{'a', 'b', 'c'}` | `a` | ...

为每个状态分配唯一名称。如果此字段为空 (`' '`)，则不会分配任何名称。

- 要为单个状态分配名称，请输入名称并用引号引起来，例如 `'position'`。
- 要为多个状态分配名称，请输入以逗号分隔的列表并用花括号括起来，例如 `{'a', 'b', 'c'}`。每个名称都必须是唯一的。
- 要在 MATLAB® 工作区中分配带变量的状态名称，请输入不带引号的变量。变量可以是字符向量、元胞数组或结构体。

##### 限制

- 状态名称只会应用于所选模块。
- 状态数量必须能够被状态名称的数量均分。
- 指定的名称数量可以少于状态数量，但不能多于状态数量。

  例如，可以在具有四个状态的系统中指定两个名称。第一个名称应用于前两个状态，第二个名称应用于后两个状态。

##### 依赖关系

要启用此参数，请将**滤波器结构**设置为**直接 II 型**。

##### 编程用法

|  |
| --- |
| **模块参数**：`StateName` |
| **类型：**字符向量 |
| **值：**`' '` | 用户定义 |
| **默认值：**`' '` |

#### **状态名称必须解析为 Simulink 信号对象** — 要求将状态名称解析为信号对象 `off` (默认) | `on`

选中此复选框会要求将状态名称解析为 Simulink 信号对象。

##### 依赖关系

要启用此参数，请将**滤波器结构**设置为**直接 II 型**，并为**状态名称**指定值。仅当将模型配置参数**信号解析**设置为除**无**以外的值时，才会显示此参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`StateMustResolveToSignalObject` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed pointa` | `integera` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |
|  |  |
| --- | --- |
| a 此模块仅支持有符号定点数据类型。 | |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

此模块仅支持有符号定点数据类型。

Discrete Filter 模块接受并输出 Simulink 支持的任何有符号数值数据类型的实信号和复信号。该模块支持相同类型的分子和分母系数。

分子和分母系数必须具有相同的复/实性。它们可以有不同的字长和小数长度。

下图显示了 Discrete Filter 模块内用于定点信号的滤波器结构和数据类型。

选择**通过跳过除以分母首项系数(a0)进行优化**参数时，该模块将忽略标虚线的除法。

### 版本历史记录

**在 R2006a 之前推出**

#### R2024b: 查看滤波器响应

点击**查看滤波器响应**按钮，以可视化您在模块对话框中指定的滤波器的频率响应。

#### R2024a: Discrete Filter 模块支持可变大小的输入信号

当您将**输入处理**参数设置为**列作为通道(基于帧)** 时，Discrete Filter 模块支持可变大小的输入信号。

当输入是可变大小信号时，您可以在仿真期间更改信号的帧大小（行数），但通道（列）数必须保持不变。

#### R2023b: **采样时间**参数的条件显示

默认情况下，Discrete Filter 模块不再在“模块参数”对话框中显示**采样时间**参数。仅在命令行或现有模型中将采样时间设置为默认值 (`-1`) 以外的值时，该参数才可见。有关详细信息，请参阅不建议设置采样时间的模块。

## Libraries

Simulink / Discrete DSP System Toolbox / Filtering / Filter Implementations

## Description

The Discrete Filter block independently filters each channel of the input
signal with the specified digital IIR filter. You can specify the filter structure as
`Direct form I`, `Direct form I transposed`,
`Direct form II`, or `Direct form II transposed`.
The block implements static filters with fixed coefficients. You can tune the
coefficients of these static filters.

This block filters each channel of the input signal independently
over time. The **Input processing** parameter allows
you to specify how the block treats each element of the input. You
can specify treating input elements as an independent channel (sample-based
processing), or treating each column of the input as an independent
channel (frame-based processing). To perform frame-based processing,
you must have a DSP System Toolbox™ license.

The output dimensions equal the input dimensions, except when you specify a matrix of filter
taps for the **Numerator coefficients** parameter. When you do so, the
output dimensions depend on the number of different sets of filter taps you
specify.

Use the **Numerator coefficients** parameter
to specify the coefficients of the discrete filter numerator polynomial.
Use the **Denominator coefficients** parameter to
specify the coefficients of the denominator polynomial of the function.
The **Denominator coefficients** parameter must be a vector of coefficients.

Specify the coefficients of the numerator and denominator polynomials in ascending powers of
*z-1*. The Discrete
Filter block lets you use polynomials in
*z-1* (the delay operator) to
represent a discrete system. Signal processing engineers typically use this method.
Conversely, the Discrete Transfer Fcn block lets you use
polynomials in *z* to represent a discrete system. Control engineers
typically use this method. When the numerator and denominator polynomials have the same
length, the two methods are identical.

### Specifying Initial States

In **Dialog parameters** and **Input port(s)** modes, the block initializes the internal filter
states to zero by default, which is equivalent to assuming past inputs
and outputs are zero. You can optionally use the **Initial states** parameter to specify nonzero initial states for the filter delays.

To determine the number of initial state values you must specify, and how to specify them,
see the following table on valid initial states and Number of Delay Elements (Filter States). The **Initial
states** parameter can take one of four forms as described in the
following table.

**Valid Initial States**

| Initial state | Examples | Description |
| --- | --- | --- |
| Scalar | `5`  Each delay element for each channel is set to `5`. | The block initializes all delay elements in the filter to the scalar value. |
| Vector   (for applying the same delay elements to each channel) | For a filter with two delay elements: [*d1**d2*]  The delay elements for all channels are d1 and d2. | Each vector element specifies a unique initial condition for a corresponding delay element. The block applies the same vector of initial conditions to each channel of the input signal. The vector length must equal the number of delay elements in the filter (specified in the table Number of Delay Elements (Filter States)). |
| Vector or matrix   (for applying different delay elements to each channel) | For a three-channel input signal and a filter with two delay elements:  [*d*1*d2**D1**D2**d1**d2*] or    [d1D1d1d2D2d2]    - The delay elements for channel 1 are   *d1* and   *d2*. - The delay elements for channel 2 are   *D1* and   *D2*. - The delay elements for channel 3 are   *d1*and   *d2*. | Each vector or matrix element specifies a unique initial condition for a corresponding delay element in a corresponding channel:  - The vector length must be equal to the product of   the number of input channels and the number of delay elements in the   filter (specified in the table Number of Delay Elements (Filter States)). - The matrix must have the same number of rows as the   number of delay elements in the filter (specified in the table Number of Delay Elements (Filter States)), and must have one column for each channel of the input signal. |
| Empty matrix | `[ ]`  Each delay element for each channel is set to `0`. | The empty matrix, `[]`, is equivalent to setting the **Initial conditions** parameter to the scalar value `0`. |

The number of delay elements (filter states) per input channel depends on the filter structure, as indicated in the following table.

**Number of Delay Elements (Filter States)**

| Filter Structure | Number of Delay Elements Per Channel |
| --- | --- |
| `Direct form I   Direct form I transposed` | - `number of zeros - 1` - `number of poles - 1` |
| `Direct form II   Direct form II transposed` | `max(number of zeros, number of poles)-1` |

The following tables describe the valid initial states for different sizes of input and
different number of channels depending on whether you set the  **Input
processing** parameter to frame based or sample based.

**Frame-Based Processing**

| Input | Number of Channels | Valid Initial States (Dialog Box) | Valid Initial States (Input Port) |
| --- | --- | --- | --- |
| - Column vector (*K*-by-1) - Unoriented vector (*K*) | 1 | - Scalar - Column vector (*M*-by-1) - Row vector (1-by-*M*) | - Scalar - Column vector (*M*-by-1) |
| - Row vector (1-by-*N*) - Matrix (*K*-by-*N*) | *N* | - Scalar - Column vector (*M*-by-1) - Row vector (1-by-*M*) - Matrix (*M*-by-*N*) | - Scalar - Matrix (*M*-by-*N*) |

**Sample-Based Processing**

| Input | Number of Channels | Valid Initial States (Dialog Box) | Valid Initial States (Input Port) |
| --- | --- | --- | --- |
| - Unoriented scalar | 1 | - Scalar - Column vector (*M*-by-1) - Row vector (1-by-*M*) | - Scalar - Column vector (*M*-by-1) - Row vector (1-by-*M*) |
| - Row vector (1-by-*N*) - Column vector (*N*-by–1) - Unoriented vector (*N*) | *N* | - Scalar - Column vector (*M*-by-1) - Row vector (1-by-*M*) - Matrix (*M*-by-*N*) | - Scalar |
| - Matrix (*K*-by-*N*) | *K* × *N* | - Scalar - Column vector (*M*-by-1) - Row vector (1-by-*M*) - Matrix (*M*-by-(*K*×*N*)) | - Scalar |

When the **Initial states** is a scalar, the block initializes all filter
states to the same scalar value. Enter `0` to initialize all states
to zero. When the **Initial states** is a vector or a matrix, each
vector or matrix element specifies a unique initial state. This unique state
corresponds to a delay element in a corresponding channel:

- The vector length must equal the number of delay elements in the
  filter, `M = max(number of zeros, number of
  poles)`.
- The matrix must have the same number of rows as the number of delay
  elements in the filter, `M = max(number of zeros, number of
  poles)`. The matrix must also have one column for each
  channel of the input signal.

The relationship between the initial filter output
*y1*, the initial input
*u1*, and the initial state
[*x1*,
*x2*] is given by the following
equation.

y1=b1[(u1−a2x1−a3x2)a1]+b2x1+b3x2

where,

- *b1*,
  *b2*, and
  *b3* are the numerator
  coefficients of the discrete filter.
- *a1*,
  *a2*, and
  *a3* are the denominator
  coefficients of the discrete filter.

## Ports

### Input

### **u** — Input signal scalar | vector | matrix

Input signal to filter, specified as a scalar, vector, or
matrix.

When you set the **Input
processing** parameter to `Columns as channels
(frame based)`, the block supports variable-size input
signals, that is, you can change the frame size (number of rows) of the
signal during simulation but the number of channels (columns) must
remain constant. *(since R2024a)*

#### Dependencies

The name of this port depends on the source you specify for the
numerator coefficients, denominator coefficients and initial states.
When you set **Numerator**,
**Denominator**, and **Initial
states** to `Dialog`, there is
only one input port, and the port is unlabeled. When you set
**Numerator**,
**Denominator**, or **Initial
states** to `Input port`, this
port is labeled **u**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **Num** — Numerator coefficients scalar | vector

Numerator coefficients of the discrete filter, specified as descending powers of
*z*. Use a row vector to specify the coefficients
for a single numerator polynomial.

#### Dependencies

To enable this port, set **Numerator Source** to `Input
port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **Den** — Denominator coefficients scalar | vector

Denominator coefficients of the discrete filter, specified as
descending powers of *z*. Use a row vector to specify
the coefficients for a single denominator polynomial.

#### Dependencies

To enable this port, set **Denominator Source**
to `Input port`.

To set **Denominator Source** to `Input
port`, select the **Optimize by skipping divide
by leading denominator coefficient (a0)** parameter.
The block ignores the leading denominator coefficient value a0 and
replaces it with 1.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **External reset** — External reset signal scalar

External reset signal, specified as a scalar. When the specified
trigger event occurs, the block resets the states to their initial conditions.

**Tip**

The icon for this port changes based on the value of the
**External reset** parameter.

#### Dependencies

To enable this port, set **External reset** to
`Rising`,
`Falling`,
`Either`,
`Level`, or `Level
hold`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **x0** — Initial states scalar | vector | matrix

Initial states, specified as a scalar, vector, or matrix. For more information about
specifying states, see Specifying Initial States.

#### Dependencies

To enable this port, set the **Filter structure**
to `Direct form II` or `Direct
form II transposed`, and set **Initial
states** to `Input
port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
### Output

### **Port\_1** — Filtered output signal scalar | vector | matrix

Filtered output signal. The output dimensions equal the input dimensions, except when
you specify a matrix of filter taps for the **Numerator
coefficients** parameter. When you do so, the output
dimensions depend on the number of different sets of filter taps you
specify.

When you set **Sample time** to
`-1`, sample time of the output signal is same as the
sample time of the input signal **u**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

## Parameters

### Main

### **Filter structure** — Filter structure `Direct form II` (default) | `Direct form I transposed` | `Direct form I` | `Direct form II transposed`

Specify the discrete IIR filter structure.

#### Dependencies

To use any filter structure other than `Direct form
II`, you must have an available DSP System Toolbox license.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FilterStructure` |
| **Type:** character vector |
| **Values:** `'Direct form II' | 'Direct form I transposed' | 'Direct form I' | 'Direct form II transposed'` |
| **Default:** `'Direct form II'` |

### **Numerator Source** — Source of numerator coefficients `Dialog` (default) | `Input port`

Specify the source of the numerator coefficients as
`Dialog` or `Input
port`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumeratorSource` |
| **Type:** character vector |
| **Values:** `'Dialog' | 'Input port'` |
| **Default:** `'Dialog'` |

### **Numerator Value** — Numerator coefficients `[1]` (default) | scalar | vector | matrix

Specify the numerator coefficients of the discrete filter as descending powers of
*z*. Use a row vector to specify the coefficients
for a single numerator polynomial. To specify coefficients for multiple
filters, specify a matrix of coefficients, where each row represents a
different set of filter taps. To implement multiple filters,
**Filter structure** must be `Direct
form II`, **Input processing** must be
`Elements as channels (sample based)`, and
the input must be a scalar.

#### Dependencies

To enable this parameter, set the **Numerator
Source** to `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Numerator` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'[1]'` |

### **Denominator Source** — Source of denominator coefficients `Dialog` (default) | `Input port`

Specify the source of the denominator coefficients as
`Dialog` or `Input
port`.

To set **Denominator Source** to `Input port`,
select the **Optimize by skipping divide by leading denominator
coefficient (a0)** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DenominatorSource` |
| **Type:** character vector |
| **Values:** `'Dialog' | 'Input port'` |
| **Default:** `'Dialog'` |

### **Denominator Value** — Denominator coefficients `[1 0.5]` (default) | vector

Specify the denominator coefficients of the discrete filter as
descending powers of *z*. Use a row vector to specify
the coefficients for a single denominator polynomial.

When you select the **Optimize by skipping divide by leading
denominator coefficient (a0)** parameter, an error occurs
if you specify the denominator coefficients in the block dialog box and
*a0* ≠ 1.

#### Dependencies

To enable this parameter, set the **Denominator
Source** to `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Denominator` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'[1 0.5]'` |

### **Initial states Source** — Source of initial states `Dialog` (default) | `Input port`

Specify the source of the initial states as
`Dialog` or `Input
port`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialStatesSource` |
| **Type:** character vector |
| **Values:** `'Dialog' | 'Input port'` |
| **Default:** `'Dialog'` |

### **Initial states Value** — Initial filter states `0` (default) | scalar | vector | matrix

Specify the initial filter states as a scalar, vector, or matrix. To learn how to
specify initial states, see Specifying Initial States.

#### Dependencies

To enable this parameter, set the **Filter
structure** to `Direct form
II` or `Direct form II
transposed`, and set **Initial states
Source** to `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialStates` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'0'` |

Alternatively, use
`IC`.

### **Initial states on numerator side** — Initial numerator states `0` (default) | scalar | vector | matrix

Specify the initial numerator filter states as a scalar, vector, or
matrix. To learn how to specify initial states, see Specifying Initial States.

#### Dependencies

To enable this port, set the **Filter structure**
to `Direct form I` or `Direct
form I transposed`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialStates` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'0'` |

### **Initial states on denominator side** — Initial denominator states `0` (default) | scalar | vector | matrix

Specify the initial denominator filter states as a scalar, vector, or
matrix. To learn how to specify initial states, see Specifying Initial States.

#### Dependencies

To enable this port, set the **Filter structure**
to `Direct form I` or `Direct
form I transposed`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialDenominatorStates` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'0'` |

### **External reset** — External state reset `None` (default) | `Rising` | `Falling` | `Either` | `Level` | `Level hold`

Specify the trigger event to use to reset the states to the initial conditions.

| Reset Mode | Behavior |
| --- | --- |
| `None` | No reset |
| `Rising` | Reset on a rising edge |
| `Falling` | Reset on a falling edge |
| `Either` | Reset on either a rising or falling edge |
| `Level` | Reset in either of these cases:  - When the reset signal is nonzero at the current time   step - When the reset signal value changes from nonzero at the   previous time step to zero at the current time step |
| `Level hold` | Reset when the reset signal is nonzero at the current time step |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ExternalReset` |
| **Type**: character vector |
| **Values**: `'None'` | `'Rising'` | `'Falling'` | `'Either'` | `'Level'` | `'Level hold'` |
| **Default**: `'None'` |

### **Input processing** — Sample- or frame-based processing `Elements as channels (sample based)` (default) | `Columns as channels (frame based)`

Specify whether the block performs sample- or frame-based processing.

- `Elements as channels (sample based)`
  — Process each element of the input as an independent
  channel.
- `Columns as channels (frame based)`
  — Process each column of the input as an independent
  channel.

#### Dependencies

Frame-based processing requires a DSP System Toolbox license.

For more information, see Sample- and Frame-Based Concepts (DSP System Toolbox).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputProcessing` |
| **Type:** character vector |
| **Values:** `'Columns as channels (frame based)' | 'Elements as channels (sample based)'` |
| **Default:** `'Elements as channels (sample based)'` |

### **Optimize by skipping divide by leading denominator coefficient (a0)** — Skip divide by a0 `off` (default) | `on`

When you select this check box, the block does not divide by
*a0* either in
simulation or in the generated code. This parameter optimizes your code.
An error occurs if you specify the denominator coefficients in the block
dialog box and *a0* ≠ 1.

If you specify the denominator coefficients from the input port
**Den**, you must select the **Optimize by
skipping divide by leading denominator coefficient (a0)**
parameter. When you select this checkbox, the block ignores the leading
denominator coefficient *a0* and
replaces it with 1.

When you clear this check box, the block is fully tunable during simulation. It divides
by *a0* in both simulation and
code generation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `a0EqualsOne` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Sample time (-1 for inherited)** — Interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples. To inherit the sample time, set this
parameter to `-1`. For more information, see Specify Sample Time.

#### Dependencies

This parameter is visible only if you set it to a value other than
`-1`. To learn more, see Blocks for Which Sample Time Is Not Recommended.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | scalar or vector in quotes |

### **View Filter Response** — View filter response button

Click this button to open the Filter Visualization Tool (`fvtool` (DSP System Toolbox)) and display the filter response of the filter
defined in the block dialog box.

#### Dependencies

To enable this parameter, set the **Numerator Source** and
**Denominator Source** parameters to
`Dialog`.

This parameter appears only if you have a valid DSP System Toolbox license.

### Data Types

### **State** — State data type `Inherit: Same as input` (default) | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

Specify the state data type. You can set this parameter to:

- A rule that inherits a data type, for example,
  `Inherit: Same as input`
- A built-in integer, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Same as input'` |

### **Numerator coefficients** — Numerator coefficient data type `Inherit: Inherit via internal rule` (default) | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

Specify the numerator coefficient data type. You can set this
parameter to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`
- A built-in signed integer, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumCoefDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Numerator coefficient minimum** — Minimum value of numerator coefficients `[]` (default) | scalar

Specify the minimum value that a numerator coefficient can have. The
default value is `[]` (unspecified). Simulink® software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
- Automatic scaling of fixed-point data types

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumCoefMin` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Numerator coefficient maximum** — Maximum value of numerator coefficients `[]` (default) | scalar

Specify the maximum value that a numerator coefficient can have. The
default value is `[]` (unspecified). Simulink software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
- Automatic scaling of fixed-point data types

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumCoefMax` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Numerator product output** — Numerator product output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

Specify the product output data type for the numerator coefficients.
You can set this parameter to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`
- A built-in data type, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumProductDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Numerator accumulator** — Numerator accumulator data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

Specify the accumulator data type for the numerator coefficients. You
can set this parameter to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`
- A built-in data type, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumAccumDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'Inherit: Same as product output' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Denominator coefficients** — Denominator coefficient data type `Inherit: Inherit via internal rule` (default) | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

Specify the denominator coefficient data type. You can set this
parameter to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`
- A built-in integer, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DenCoefDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Denominator coefficient minimum** — Minimum value of denominator coefficients `[]` (default) | scalar

Specify the minimum value that a denominator coefficient can have. The
default value is `[]` (unspecified). Simulink software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
- Automatic scaling of fixed-point data types

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DenCoefMin` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Denominator coefficient maximum** — Maximum value of denominator coefficients `[]` (default) | scalar

Specify the maximum value that a denominator coefficient can have. The
default value is `[]` (unspecified). Simulink software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
- Automatic scaling of fixed-point data types

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DenCoefMax` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Denominator product output** — Denominator product output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

Specify the product output data type for the denominator coefficients.
You can set this parameter to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`
- A built-in data type, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DenProductDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Denominator accumulator** — Denominator accumulator data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

Specify the accumulator data type for the denominator coefficients.
You can set this parameter to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`
- A built-in data type, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DenAccumDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'Inherit: Same as product output' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Output** — Output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

Specify the output data type. You can set this parameter to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`
- A built-in data type, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Output minimum** — Minimum value of output `[]` (default) | scalar

Specify the minimum value that the block can output. The default value
is `[]` (unspecified). Simulink software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges)
- Automatic scaling of fixed-point data types

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutMin` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Output maximum** — Maximum value of output `[]` (default) | scalar

Specify the maximum value that the block can output. The default value
is `[]` (unspecified). Simulink software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges)
- Automatic scaling of fixed-point data types

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutMax` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Multiplicand data type** — Multiplicand data type `Inherit: Same as input` (default) | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

Specify the multiplicand data type. You can set this parameter
to:

- A rule that inherits a data type, for example,
  `Inherit: Same as input`
- A built-in data type, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, set the **Filter
structure** to `Direct form I
transposed`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MultiplicandDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Same as input'` |

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select to lock data type settings of this block against changes by the
Fixed-Point Tool and the Fixed-Point Advisor. For more information,
see Lock the Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LockScale` |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations.
For more information, see Rounding Modes (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **Default:** `'Floor'` |

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

### State Attributes

### **State name** — Assign unique name to each state `' '` (default) | `'position'` | `{'a', 'b', 'c'}` | `a` | ...

Assign a unique name to each state. If this field is blank (`'
'`), no name assignment occurs.

- To assign a name to a single state, enter the name between
  quotes, for example, `'position'`.
- To assign names to multiple states, enter a comma-delimited
  list surrounded by braces, for example, `{'a', 'b',
  'c'}`. Each name must be unique.
- To assign state names with a variable in the MATLAB® workspace, enter the variable without quotes. A
  variable can be a character vector, cell array, or
  structure.

#### Limitations

- The state names apply only to the selected block.
- The number of states must divide evenly among the number
  of state names.
- You can specify fewer names than states, but you cannot
  specify more names than states.

  For example, you can specify two names in a system with
  four states. The first name applies to the first two states
  and the second name to the last two states.

#### Dependencies

To enable this parameter, set **Filter
structure** to `Direct form
II`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateName` |
| **Type:** character vector |
| **Values:** `' '` | user-defined |
| **Default:** `' '` |

### **State name must resolve to Simulink signal object** — Require state name resolve to a signal object `off` (default) | `on`

Select this check box to require that the state name resolves to a
Simulink signal object.

#### Dependencies

To enable this parameter, set **Filter
structure** to `Direct form
II` and specify a value for **State
name**. This parameter appears only if you set the
model configuration parameter **Signal resolution**
to a value other than `None`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateMustResolveToSignalObject` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed pointa` | `integera` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a This block only supports signed fixed-point data types. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

This block only supports signed fixed-point data types.

The Discrete Filter block accepts and outputs real and complex signals of any
signed numeric data type that Simulink supports. The block supports the same types for the numerator and
denominator coefficients.

Numerator and denominator coefficients must have the same complexity. They can
have different word lengths and fraction lengths.

The following diagrams show the filter structure and the data types used within
the Discrete Filter block for fixed-point signals.

The block omits the dashed divide when you select the **Optimize by
skipping divide by leading denominator coefficient (a0)**
parameter.

## Version History

**Introduced before R2006a**

### R2024b: View filter response

Click the **View Filter Response** button to visualize the
frequency response of the filter that you specify in the block dialog box.

### R2024a: The Discrete Filter block supports variable-size input signals

The Discrete Filter block supports variable-size input signals when
you set the **Input processing** parameter to `Columns
as channels (frame based)`.

When the input is a variable-size signal, you can change the frame size (number of
rows) of the signal during simulation but the number of channels (columns) must
remain constant.

### R2023b: Conditional display of the **Sample time** parameter

The Discrete Filter block no longer displays the **Sample
time** parameter in the block parameters dialog box by default. The
parameter is visible only if you set the sample time to a value other the default
value (`-1`) at the command line or in an existing model. For more
information, see Blocks for Which Sample Time Is Not Recommended.
