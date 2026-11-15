---
type: simulink-block
title: 'Discrete Transfer Fcn'
family: discrete
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'discretetransferfcn'
---

# Discrete Transfer Fcn

Implement discrete transfer function

## 中文

实现离散传递函数

### 所属库

Simulink / Discrete HDL Coder / Discrete HDL Coder / HDL Floating Point Operations

### 描述

Discrete Transfer Fcn 模块实现 *z* 变换传递函数，如下所示：

H(z)=num(z)den(z)=num0zm+num1zm−1+...+nummden0zn+den1zn−1+...+denn

其中 m+1 和 n+1 分别是分子和分母系数的数目。*num* 和 *den* 包含按 *z* 的降幂顺序排列的分子和分母系数。*num* 可以是向量或矩阵，而 *den* 必须为向量。分母的阶必须大于或等于分子的阶。

按 *z* 的降幂顺序指定分子和分母多项式的系数。利用此模块，您可以使用 *z* 形式的多项式来表示离散系统，这是控制工程师通常使用的方法。与之相反，Discrete Filter 模块则允许使用 *z-1*（延迟算子）形式的多项式来表示离散系统，这是信号处理工程师通常使用的方法。当分子和分母多项式的长度相同时，这两种方法相同。

Discrete Transfer Fcn 模块将 *z* 变换传递函数应用于输入的每个独立通道。**输入处理**参数用于指定该模块将输入的每个列作为单个通道处理（基于帧的处理）还是将输入的每个元素作为单个通道处理（基于采样的处理）。要执行基于帧的处理，您必须拥有 DSP System Toolbox™ 许可证。

#### 指定初始状态

使用**初始状态**参数可以指定初始滤波器状态。您指定的初始状态是在实现离散传递函数的滤波器图中使用的 Unit Delay 模块的初始条件。

要确定您必须指定的初始状态数量以及如何指定这些状态，请使用下列各表。

**基于帧的处理**

| 输入 | 通道数 | 有效初始状态（对话框） | 有效初始状态（输入端口） |
| --- | --- | --- | --- |
| - 列向量 (*K*×1) - 无向向量 (*K*) | 1 | - 标量 - 列向量 (*M*×1) - 行向量 (1×*M*) | - 标量 - 列向量 (*M*×1) |
| - 行向量 (1×*N*) - 矩阵 (*K*×*N*) | *N* | - 标量 - 列向量 (*M*×1) - 行向量 (1×*M*) - 矩阵 (*M*×*N*) | - 标量 - 矩阵 (*M*×*N*) |

**基于采样的处理**

| 输入 | 通道数 | 有效初始状态（对话框） | 有效初始状态（输入端口） |
| --- | --- | --- | --- |
| - 标量 | 1 | - 标量 - 列向量 (*M*×1) - 行向量 (1×*M*) | - 标量 - 列向量 (*M*×1) - 行向量 (1×*M*) |
| - 行向量 (1×*N*) - 列向量 (*N*×1) - 无向向量 (*N*) | *N* | - 标量 - 列向量 (*M*×1) - 行向量 (1×*M*) - 矩阵 (*M*×*N*) | - 标量 |
| - 矩阵 (*K*×*N*) | *K*×*N* | - 标量 - 列向量 (*M*×1) - 行向量 (1×*M*) - 矩阵 (*M*×(*K*×*N*)) | - 标量 |

当**初始状态**为标量时，模块将所有滤波器状态初始化为相同的标量值。要将所有状态初始化为零，请输入 `0`。当**初始状态**为向量或矩阵时，每个向量或矩阵元素都为相应通道中的相应延迟元素指定唯一的初始状态：

- 向量长度必须等于滤波器中的延迟元素数，`M = max(number of zeros, number of poles)`。
- 矩阵的行数必须与滤波器中的延迟元素数相同，`M = max(number of zeros, number of poles)`。矩阵的每一列还须对应输入信号的一个通道。

以下示例说明了初始滤波器输出与初始输入和状态之间的关系。假定有一个初始输入 *u1*，则第一个输出 *y1* 与初始状态 [*x1*, *x2*] 和初始输入的关系如下所示：

y1=4x1x2=1/2(u1−3x1)

### 端口

#### 输入

#### **u** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。

当您将**输入处理**参数设置为**列作为通道(基于帧)**时，模块支持可变大小的输入信号，即您可以在仿真期间更改信号的帧大小（行数），但通道（列）的数量必须保持不变。 *(自 R2024a 起)*

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

#### **Num** — 分子系数 标量 | 向量 | 矩阵

分子多项式的系数指定为 *z* 的降幂顺序的向量或矩阵。使用行向量可指定单个分子多项式的系数。使用矩阵可以指定要应用于同一输入的多个滤波器的系数。矩阵的每一行表示一组滤波器抽头。分母的阶必须大于或等于分子的阶。

##### 依赖关系

要启用此端口，请将**分子源**设置为**输入端口**。

分子和分母系数必须具有相同的复/实性。它们可以有不同的字长和小数长度。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

#### **Den** — 分母系数 标量 | 向量 | 矩阵

分母多项式的系数，指定为 *z* 的降幂形式的向量。使用行向量可指定单个分母多项式的系数。使用矩阵可以指定要应用于同一输入的多个滤波器的系数。矩阵的每一行表示一组滤波器抽头。分母的阶必须大于或等于分子的阶。分母首项系数不能为 `0`。

##### 依赖关系

要启用此端口，请将**分母源**设置为**输入端口**。

分子和分母系数必须具有相同的复/实性。它们可以有不同的字长和小数长度。

要将**分母源**设置为**输入端口**，请选择**通过跳过除以分母首项系数(a0)进行优化**参数。该模块忽略分母首项系数值 a0，并用 1 替换它。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

#### **External reset** — 外部重置信号 标量

外部重置信号，指定为标量。当指定的触发事件发生时，模块将状态重置为其初始条件。

**提示**

此端口的图标根据**外部重置**参数的值更改。

##### 依赖关系

要启用此端口，请将**外部重置**设置为**上升沿**、**下降沿**、**任一沿**、**电平**或**电平保持**。

##### 限制

重置信号必须是单精度、双精度、布尔或整数类型的标量。不支持 `ufix1` 以外的定点数据类型。

**数据类型:** `single` | `double` | `Boolean` | `int8` | `int16` | `int32` | `fixed point`

#### **x0** — 初始状态 标量 | 向量 | 矩阵

初始状态，指定为标量、向量或矩阵。有关指定状态的详细信息，请参阅指定初始状态。当输入或系数为复数时，状态为复数。

##### 依赖关系

要启用此端口，请将**初始状态源**设置为**输入端口**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
#### 输出

#### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

输出信号，指定为标量、向量或矩阵。

当您将**采样时间**设置为 `-1` 时，输出信号的采样时间与输入信号 **u** 的采样时间相同。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### 参数

#### 常设

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

离散传递函数的分子系数。要指定系数，请将**源**设置为**对话框**。然后，在**值**中按 *z* 的降幂顺序输入系数。使用行向量可指定单个分子多项式的系数。使用矩阵可以指定要应用于同一输入的多个滤波器的系数。矩阵的每一行表示一组滤波器抽头。

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

#### **分母值** — 分母系数 `[1 0.5]` (默认) | 标量 | 向量 | 矩阵

离散传递函数的分母系数。要指定系数，请将**源**设置为**对话框**。然后，在**值**中按 *z* 的降幂顺序输入系数。使用行向量可指定单个分母多项式的系数。使用矩阵可以指定要应用于同一输入的多个滤波器的系数。矩阵的每一行表示一组滤波器抽头。

当您选择**通过跳过除以分母首项系数(a0)进行优化**参数时，如果您在模块对话框中指定分母系数且 *a0* ≠ 1，则会发生错误。

##### 依赖关系

要启用此参数，请将**分母源**设置为**对话框**。

##### 编程用法

|  |
| --- |
| **模块参数**：`Denominator` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 |
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

要启用此参数，请将**初始状态源**设置为**对话框**。

##### 编程用法

|  |
| --- |
| **模块参数**：`InitialStates` |
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

  **注意**

  基于帧的处理需要具有 DSP System Toolbox 许可证。

  有关详细信息，请参阅Sample- and Frame-Based Concepts (DSP System Toolbox)。

##### 编程用法

|  |
| --- |
| **模块参数**：`InputProcessing` |
| **类型：**字符向量 |
| **值：**`'Elements as channels (sample based)' | 'Columns as channels (frame based)'` |
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

指定状态数据类型。可以将其设置为：

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

#### **分子系数** — 分子系数数据类型 `Inherit: Inherit via internal rule` (默认) | **int8** | **int16** | **int32** | **int64** | **fixdt(1,16)** | **fixdt(1,16,0)** | **<数据类型表达式>**

指定分子系数数据类型。可以将其设置为：

- 继承数据类型的规则，例如**继承: 从内部规则继承**
- 内置整数，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**： `NumCoefDataTypeStr` |
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

#### **分子乘积输出** — 分子乘积输出数据类型 `Inherit: Inherit via internal rule` (默认) | **继承: 与输入相同** | **int8** | **int16** | **int32** | **int64** | **fixdt(1,16,0)** | **<数据类型表达式>**

指定分子系数的乘积输出数据类型。可以将其设置为：

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

#### **分子累加器** — 分子累加器数据类型 `Inherit: Inherit via internal rule` (默认) | **继承: 与输入相同** | **继承: 与乘积输出相同** | **int8** | **int16** | **int32** | **int64** | **fixdt(1,16,0)** | **<数据类型表达式>**

指定分子系数的累加器数据类型。可以将其设置为：

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

#### **分母系数** — 分母系数数据类型 `Inherit: Inherit via internal rule` (默认) | **int8** | **int16** | **int32** | **int64** | **fixdt(1,16)** | **fixdt(1,16,0)** | **<数据类型表达式>**

指定分母系数数据类型。可以将其设置为：

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

#### **分母乘积输出** — 分母乘积输出数据类型 `Inherit: Inherit via internal rule` (默认) | **继承: 与输入相同** | **int8** | **int16** | **int32** | **int64** | **fixdt(1,16,0)** | **<数据类型表达式>**

指定分母系数的乘积输出数据类型。可以将其设置为：

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

#### **分母累加器** — 分母累加器数据类型 `Inherit: Inherit via internal rule` (默认) | **继承: 与输入相同** | **继承: 与乘积输出相同** | **int8** | **int16** | **int32** | **int64** | **fixdt(1,16,0)** | **<数据类型表达式>**

指定分母系数的累加器数据类型。可以将其设置为：

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

#### **输出** — 输出数据类型 `Inherit: Inherit via internal rule` (默认) | `Inherit: Same as input` | **int8** | **int16** | **int32** | **int64** | **fixdt(1,16)** | **fixdt(1,16,0)** | **<数据类型表达式>**

指定输出数据类型。可以将其设置为：

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

指定模块可以输出的最小值。默认值为 `[]`（未指定）。Simulink 使用此值来执行：

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

指定模块可以输出的最大值。默认值为 `[]`（未指定）。Simulink 使用此值来执行：

- 仿真范围检查（请参阅指定信号范围）
- 定点数据类型的自动定标

##### 编程用法

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'[]'` |

#### **锁定数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您对此模块指定的数据类型。有关详细信息，请参阅Lock the Output Data Type Setting (Fixed-Point Designer)。

##### 编程用法

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **整数舍入模式** — 定点运算的舍入模式 **向下** (默认) | **向上** | **收敛** | **最邻近值** | **舍入** | **最简** | **零**

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最邻近的可表示值。要控制模块参数的舍入方法，请在封装字段中使用 MATLAB® 舍入函数输入表达式。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RndMeth` |
| **值:** | `'Floor'` (默认) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

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

#### **状态名称** — 模块状态的唯一名称 `''` (默认) | 字母数字字符串

使用此参数为模块状态指定唯一名称。默认值为 `' '`。如果此字段为空，则表示未指定任何名称。使用此参数时，请记住以下注意事项：

- 有效的标识符以字母或下划线字符开始，后跟字母数字或下划线字符。
- 状态名称仅适用于所选模块。

当您点击**应用**时，此参数将启用**状态名称必须解析为 Simulink 信号对象**。

有关详细信息，请参阅模型接口元素的 C 数据代码接口配置 (Simulink Coder)。

##### 编程用法

|  |
| --- |
| **模块参数**：`StateName` |
| **类型：**字符向量 |
| **值：**唯一名称 |
| **默认值：**`''` |

#### **状态名称必须解析为 Simulink 信号对象** — 要求将状态名称解析为信号对象 `off` (默认) | `on`

选中此复选框会要求将状态名称解析为 Simulink 信号对象。

##### 依赖关系

要启用此参数，请为**状态名称**指定值。仅当将模型配置参数**信号解析**设置为除**无**以外的值时，才会显示此参数。

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

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **ConstMultiplierOptimization** | 正则有符号数 (CSD) 或因子化 CSD 优化。默认值为**无**。另请参阅ConstMultiplierOptimization (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

| 原生浮点 | |
| --- | --- |
| **HandleDenormals** | 指定是否希望 HDL Coder 在设计中插入额外的逻辑来处理非正规数字。非正规数是大小非常小、必须使用包含前导零的尾数才能表示的浮点数。默认值为 **inherit**。另请参阅HandleDenormals (HDL Coder)。 |
| **LatencyStrategy** | 指定对于浮点运算符是否将设计中的模块映射到 `inherit`、`Max`、`Min` 或 `Zero`。默认值为 **inherit**。另请参阅LatencyStrategy (HDL Coder)。 |
| **MantissaMultiplyStrategy** | 指定在代码生成期间如何实现尾数乘法运算。通过使用不同设置，您可以控制目标 FPGA 设备上 DSP 的使用。默认值为 **inherit**。另请参阅MantissaMultiplyStrategy (HDL Coder)。 |

**限制**

- 此模块不支持双精度数据类型。请改用单精度数据类型。
- 不支持帧、矩阵和向量输入数据类型。
- 分母首项系数 (a0) 必须为 1 或 -1。
- 不支持将数据类型设置为 `Inherit: Inherit via internal rule`。

以下优化中不包括 Discrete Transfer Fcn 模块：

- 资源复用
- 分布式流水线

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

此模块仅支持有符号定点数据类型。

### 版本历史记录

**在 R2006a 之前推出**

#### R2024b: 查看滤波器响应

点击**查看滤波器响应**按钮，以可视化您在模块对话框中指定的滤波器的频率响应。

#### R2024a: Discrete Transfer Fcn 模块支持可变大小的输入信号

当您将**输入处理**参数设置为**列作为通道(基于帧)** 时，Discrete Transfer Fcn 模块支持可变大小的输入信号。

当输入是可变大小信号时，您可以在仿真期间更改信号的帧大小（行数），但通道（列）数必须保持不变。

#### R2023b: **采样时间**参数的条件显示

默认情况下，Discrete Transfer Fcn 模块不再在“模块参数”对话框中显示**采样时间**参数。仅在命令行或现有模型中将采样时间设置为默认值 (`-1`) 以外的值时，该参数才可见。有关详细信息，请参阅不建议设置采样时间的模块。

## Libraries

Simulink / Discrete HDL Coder / Discrete HDL Coder / HDL Floating Point Operations

## Description

The Discrete Transfer Fcn block implements the *z*-transform
transfer function as follows:

H(z)=num(z)den(z)=num0zm+num1zm−1+...+nummden0zn+den1zn−1+...+denn

where m+1 and n+1 are the number of numerator and denominator coefficients,
respectively. *num* and *den* contain the coefficients
of the numerator and denominator in descending powers of *z*.
*num* can be a vector or matrix, while *den* must
be a vector. The order of the denominator must be greater than or equal to the order of
the numerator.

Specify the coefficients of the numerator and denominator polynomials in descending powers
of *z*. This block lets you use polynomials in *z* to
represent a discrete system, a method that control engineers typically use. Conversely,
the Discrete Filter block lets you use polynomials in
*z-1* (the delay operator) to
represent a discrete system, a method that signal processing engineers typically use.
The two methods are identical when the numerator and denominator polynomials have the
same length.

The Discrete Transfer Fcn block applies the *z*-transform
transfer function to each independent channel of the input. The **Input
processing** parameter allows you to specify whether the block treats each
column of the input as an individual channel (frame-based processing) or each element of
the input as an individual channel (sample-based processing). To perform frame-based
processing, you must have a DSP System Toolbox™ license.

### Specifying Initial States

Use the **Initial states** parameter to specify the initial filter states.
The initial states you specify are the initial conditions of the unit delay blocks
that are used in the filter digram implementing the discrete transfer
function.

To determine the number of initial states you must specify and how to specify
them, use the following tables.

**Frame-Based Processing**

| Input | Number of Channels | Valid Initial States (Dialog Box) | Valid Initial States (Input Port) |
| --- | --- | --- | --- |
| - Column vector (*K*-by-1) - Unoriented vector (*K*) | 1 | - Scalar - Column vector (*M*-by-1) - Row vector (1-by-*M*) | - Scalar - Column vector (*M*-by-1) |
| - Row vector (1-by-*N*) - Matrix (*K*-by-*N*) | *N* | - Scalar - Column vector (*M*-by-1) - Row vector (1-by-*M*) - Matrix (*M*-by-*N*) | - Scalar - Matrix (*M*-by-*N*) |

**Sample-Based Processing**

| Input | Number of Channels | Valid Initial States (Dialog Box) | Valid Initial States (Input Port) |
| --- | --- | --- | --- |
| - Scalar | 1 | - Scalar - Column vector (*M*-by-1) - Row vector (1-by-*M*) | - Scalar - Column vector (*M*-by-1) - Row vector (1-by-*M*) |
| - Row vector (1-by-*N*) - Column vector (*N*-by-1) - Unoriented vector (*N*) | *N* | - Scalar - Column vector (*M*-by-1) - Row vector (1-by-*M*) - Matrix (*M*-by-*N*) | - Scalar |
| - Matrix (*K*-by-*N*) | *K* × *N* | - Scalar - Column vector (*M*-by-1) - Row vector (1-by-*M*) - Matrix (*M*-by-(*K*×*N*)) | - Scalar |

When the **Initial states** is a scalar, the block initializes all filter
states to the same scalar value. To initialize all states to zero, enter
`0`. When the **Initial states** is a vector
or a matrix, each vector or matrix element specifies a unique initial state for a
corresponding delay element in a corresponding channel:

- The vector length must equal the number of delay elements in the
  filter, `M = max(number of zeros, number of
  poles)`.
- The matrix must have the same number of rows as the number of delay
  elements in the filter, `M = max(number of zeros, number of
  poles)`. The matrix must also have one column for each
  channel of the input signal.

The following example shows the relationship between the initial filter output and the
initial input and state. Given an initial input
*u1*, the first output
*y1* is related to the initial state
[*x1*,
*x2*] and initial input by as
follows:

y1=4x1x2=1/2(u1−3x1)

## Ports

### Input

### **u** — Input signal scalar | vector | matrix

Input signal, specified as a scalar, vector, or matrix.

When you set the **Input
processing** parameter to `Columns as channels
(frame based)`, the block supports variable-size input
signals, that is, you can change the frame size (number of rows) of the
signal during simulation but the number of channels (columns) must
remain constant. *(since R2024a)*

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **Num** — Numerator coefficients scalar | vector | matrix

Coefficients of the numerator polynomial specified as a vector or matrix in descending
powers of *z*. Use a row vector to specify the
coefficients for a single numerator polynomial. Use a matrix to specify
coefficients for multiple filters to be applied to the same input. Each
matrix row represents a set of filter taps. The order of the denominator
must be greater than or equal to the order of the numerator.

#### Dependencies

To enable this port, set **Numerator Source** to
`Input port`.

Numerator and denominator coefficients must have the same
complexity. They can have different word lengths and fraction
lengths.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **Den** — Denominator coefficients scalar | vector | matrix

Coefficients of the denominator polynomial, specified as a vector in descending powers
of *z*. Use a row vector to specify the coefficients
for a single denominator polynomial. Use a matrix to specify
coefficients for multiple filters to apply to the same input. Each
matrix row represents a set of filter taps. The order of the denominator
must be greater than or equal to the order of the numerator. The leading
denominator coefficient cannot be `0`.

#### Dependencies

To enable this port, set **Denominator Source**
to `Input port`.

Numerator and denominator coefficients must have the same
complexity. They can have different word lengths and fraction
lengths.

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

#### Limitations

The reset signal must be a scalar of type single, double, Boolean, or integer.
Fixed-point data types, except for `ufix1`, are not
supported.

**Data Types:** `single` | `double` | `Boolean` | `int8` | `int16` | `int32` | `fixed point`

### **x0** — Initial states scalar | vector | matrix

Initial states, specified as a scalar, vector, or matrix. For more information about
specifying states, see Specifying Initial States. States are complex when
either the input or the coefficients are complex.

#### Dependencies

To enable this port, set **Initial states
Source** to `Input
port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector | matrix

Output signal specified as a scalar, vector, or matrix.

When you set **Sample time** to
`-1`, sample time of the output signal is same as the
sample time of the input signal **u**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

## Parameters

### Main

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

Numerator coefficients of the discrete transfer function. To specify the coefficients,
set the **Source** to
`Dialog`. Then, enter the coefficients in
**Value** as descending powers of
*z*. Use a row vector to specify the coefficients
for a single numerator polynomial. Use a matrix to specify coefficients
for multiple filters to be applied to the same input. Each matrix row
represents a set of filter taps.

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

### **Denominator Value** — Denominator coefficients `[1 0.5]` (default) | scalar | vector | matrix

Denominator coefficients of the discrete transfer function. To specify the coefficients,
set the **Source** to
`Dialog`. Then, enter the coefficients in
**Value** as descending powers of
*z*. Use a row vector to specify the coefficients
for a single denominator polynomial. Use a matrix to specify
coefficients for multiple filters to apply to the same input. Each
matrix row represents a set of filter taps.

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
| **Values:** scalar | vector | matrix |
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

Specify the initial filter states as a scalar, vector, or matrix. To
learn how to specify initial states, see Specifying Initial States.

#### Dependencies

To enable this parameter, set **Initial states
Source** to `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialStates` |
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

Specify whether the block performs sample- or frame-based
processing.

- `Elements as channels (sample based)`
  — Process each element of the input as an independent
  channel.
- `Columns as channels (frame based)`
  — Process each column of the input as an independent
  channel.

  **Note**

  Frame-based processing requires a DSP System Toolbox license.

  For more information, see Sample- and Frame-Based Concepts (DSP System Toolbox).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputProcessing` |
| **Type:** character vector |
| **Values:** `'Elements as channels (sample based)' | 'Columns as channels (frame based)'` |
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

Specify the state data type. You can set it to:

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

Specify the numerator coefficient data type. You can set it to:

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
| **Block Parameter:**  `NumCoefDataTypeStr` |
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
You can set it to:

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
can set it to:

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

Specify the denominator coefficient data type. You can set it
to:

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
You can set it to:

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
You can set it to:

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

Specify the output data type. You can set it to:

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
is `[]` (unspecified). Simulink uses this value to perform:

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
is `[]` (unspecified). Simulink uses this value to perform:

- Simulation range checking (see Specify Signal Ranges)
- Automatic scaling of fixed-point data types

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutMax` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types you specify on this block. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LockScale` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations. For more information, see Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To control the
rounding of a block parameter, enter an expression using a MATLAB® rounding function into the mask field.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RndMeth` |
| **Values:** | `'Floor'` (default) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

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

### **State name** — Unique name for block state `''` (default) | alphanumeric string

Use this parameter to assign a unique name to the block state. The default is `' '`. When this field is blank, no name is assigned. When using this parameter, remember these considerations:

- A valid identifier starts with an alphabetic or underscore character, followed by alphanumeric or underscore characters.
- The state name applies only to the selected block.

This parameter enables **State name must resolve to Simulink signal object** when you click **Apply**.

For more information, see C Data Code Interface Configuration for Model Interface Elements (Simulink Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateName` |
| **Type:** character vector |
| **Values:** unique name |
| **Default:** `''` |

### **State name must resolve to Simulink signal object** — Require state name resolve to a signal object `off` (default) | `on`

Select this check box to require that the state name resolves to a Simulink signal object.

#### Dependencies

To enable this parameter, specify a value for **State name**. This parameter appears only if you set the model configuration parameter **Signal resolution** to a value other than `None`.

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

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstMultiplierOptimization** | Canonical signed digit (CSD) or factored CSD optimization. The default is `none`. See also ConstMultiplierOptimization (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

| Native Floating Point | |
| --- | --- |
| **HandleDenormals** | Specify whether you want HDL Coder to insert additional logic to handle denormal numbers in your design. Denormal numbers are numbers that have magnitudes less than the smallest floating-point number that can be represented without leading zeros in the mantissa. The default is `inherit`. See also HandleDenormals (HDL Coder). |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `inherit`, `Max`, `Min`, or `Zero` for the floating-point operator. The default is `inherit`. See also LatencyStrategy (HDL Coder). |
| **MantissaMultiplyStrategy** | Specify how to implement the mantissa multiplication operation during code generation. By using different settings, you can control the DSP usage on the target FPGA device. The default is `inherit`. See also MantissaMultiplyStrategy (HDL Coder). |

**Restrictions**

- Double data types are not supported for this block. Use single
  data types instead.
- Frame, matrix, and vector input data types are not
  supported.
- The leading denominator coefficient (a0) must be 1 or -1.
- Setting the data type as `Inherit: Inherit via internal
  rule` is not supported.

The Discrete Transfer Fcn block is excluded from the following optimizations:

- Resource sharing
- Distributed pipelining

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

This block only supports signed fixed-point data types.

## Version History

**Introduced before R2006a**

### R2024b: View filter response

Click the **View Filter Response** button to visualize the frequency
response of the filter that you specify in the block dialog box.

### R2024a: The Discrete Transfer Fcn block supports variable-size input signals

The Discrete Transfer Fcn block supports variable-size input
signals when you set the **Input processing** parameter to
`Columns as channels (frame based)`.

When the input is a variable-size signal, you can change the frame size (number of
rows) of the signal during simulation but the number of channels (columns) must
remain constant.

### R2023b: Conditional display of the **Sample time** parameter

The Discrete Transfer Fcn block no longer displays the **Sample
time** parameter in the block parameters dialog box by default. The
parameter is visible only if you set the sample time to a value other the default
value (`-1`) at the command line or in an existing model. For more
information, see Blocks for Which Sample Time Is Not Recommended.
