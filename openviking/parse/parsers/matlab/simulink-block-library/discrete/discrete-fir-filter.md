---
type: simulink-block
title: 'Discrete FIR Filter'
family: discrete
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'discretefirfilter'
---

# Discrete FIR Filter

Model FIR filters

## 中文

构建 FIR 滤波器模型

### 所属库

Simulink / Discrete HDL Coder / Discrete HDL Coder / HDL Floating Point Operations

### 描述

Discrete FIR Filter 模块使用指定的数字 FIR 滤波器单独对输入信号的每个通道进行滤波。该模块可以实现系数固定的静态滤波器以及系数随时间变化的时变滤波器。您可以在仿真期间调整静态滤波器的系数。

此模块随时间的推移单独对输入信号的每个通道进行滤波。**输入处理**参数用于指定该模块将输入的每个元素作为独立通道处理（基于采样的处理）还是将输入的每个列作为独立通道处理（基于帧的处理）。要执行基于帧的处理，您必须拥有 DSP System Toolbox™ 许可证。

输出维度等于输入维度，但为**系数**参数指定滤波器抽头矩阵时除外。当您执行此操作时，输出维度取决于您指定的不同滤波器抽头集的数量。

此模块支持自定义状态属性以更高效地自定义和生成代码。有关示例，请参阅Custom State Attributes in Discrete FIR Filter block。在某些条件下，模块还支持 SIMD 代码生成。有关详细信息，请参阅代码生成。

此模块的输出在数值上与 DSP System Toolbox Digital Filter Design (DSP System Toolbox) 模块的输出相匹配。

此模块支持 Simulink® 状态记录功能。有关详细信息，请参阅 State。

#### 滤波器结构支持

您可以更改通过 Discrete FIR Filter 模块实现的滤波器结构，方法是从**滤波器结构**参数中选择以下选项之一：

- **直接型**
- **直接型对称**
- **直接型反对称**
- **直接型转置**
- **格型 MA**

您必须拥有可用的 DSP System Toolbox 许可证才能运行具有上述任意滤波器结构（**直接型**除外）的模型。

有关滤波器结构的详细信息，请参阅算法。

#### 指定初始状态

Discrete FIR Filter 模块默认将内部滤波器状态初始化为零，这等效于假定过去的输入和输出为零。您可以选择使用**初始状态**参数为滤波器延迟指定非零初始条件。

要确定您必须指定的初始状态数量以及如何指定这些状态，请参阅有关有效初始状态的表。**初始状态**参数可采用下表所述的形式之一。

**有效初始状态**

| 初始条件 | 描述 |
| --- | --- |
| 标量 | 模块将滤波器中的所有延迟元素初始化为标量值。 |
| 向量或矩阵  （用于将不同的延迟元素应用于每个通道） | 每个向量或矩阵元素均为相应通道中的相应延迟元素指定唯一的初始条件：  - 向量长度等于输入通道数与滤波器中延迟元素数 `#_of_filter_coeffs-1`（对于**格型 MA**，则为 `#_of_reflection_coeffs`）的乘积。 - 矩阵的行数必须与滤波器中的延迟元素数 `#_of_filter_coeffs-1`（对于**格型 MA**，则为 `#_of_reflection_coeffs`）相同，并且每一列还须对应输入信号的一个通道。 |

### 端口

#### 输入

#### **In** — 输入信号 标量 | 向量 | 矩阵

要滤波的输入信号，指定为标量、向量或矩阵。

Discrete FIR Filter 模块接受 Simulink 支持的任何数值数据类型的实信号和复信号。

##### 依赖关系

将**系数来源**设置为**对话框参数**时，输入信号的端口不带标签。将**系数来源**设置为**输入端口**时，输入信号的端口的标签为 **In**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持:** 是

#### **Num** — 滤波器系数 标量 | 向量

将滤波器系数指定为标量或向量。当指定滤波器抽头的行向量时，模块会对输入应用单个滤波器。要对输入应用多个滤波器，请通过**系数**参数以矩阵形式指定系数。

##### 依赖关系

要启用此端口，请将**系数来源**设置为**输入端口**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **External reset** — 外部重置信号 标量

外部重置信号，指定为标量。当指定的触发事件发生时，模块将状态重置为其初始条件。

**提示**

此端口的图标根据**外部重置**参数的值更改。

##### 依赖关系

要启用此端口，请将**外部重置**设置为**上升沿**、**下降沿**、**任一沿**、**电平**或**电平保持**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **⎍** — 启用信号 标量

启用信号，指定为标量。此端口可以控制模块的执行。当此端口的输入非零时，模块被启用；当输入为 `0` 时，模块被禁用。输入的值在执行模块的同一时间步进行检查。

##### 依赖关系

要启用此端口，请选中**显示使能端口**复选框。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
#### 输出

#### **Port\_1** — 滤波后的输出信号 标量 | 向量 | 矩阵

滤波后的输出信号，以标量、向量或矩阵形式返回。Discrete FIR Filter 模块输出 Simulink 支持的任何数值数据类型的实信号和复信号。

当模块的输入为定点时，模块输出的数据类型取决于您在**输出**参数中指定的值。当输入为浮点时，输出数据类型与输入数据类型匹配，因为浮点继承优先于定点设置。

当您将**采样时间**设置为 `-1` 时，输出信号的采样时间与输入信号 **In** 的采样时间相同。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 参数

#### 常设

#### **系数来源** — 系数的信源 **对话框参数** (默认) | **输入端口**

选择以指定是使用可调参数对话框参数还是通过输入端口指定滤波器系数，这对于时变系数非常有用。

##### 编程用法

|  |
| --- |
| **模块参数**：`CoefSource` |
| **类型：**字符向量 |
| **值**：`'Dialog parameters' | 'Input port'` |
| **默认值：**`'Dialog parameters'` |

#### **滤波器结构** — 滤波器结构 **直接型** (默认) | **直接型对称** | **直接型反对称** | **直接型转置** | **格型 MA**

选择您要模块实现的滤波器结构。有关详细信息，请参阅算法。

##### 依赖关系

如果模型包含 Discrete FIR Filter 模块且该模块实现**直接型**以外的滤波器结构，则您必须有可用的 DSP System Toolbox 许可证才能运行该模型。

##### 编程用法

|  |
| --- |
| **模块参数**：`FilterStructure` |
| **类型：**字符向量 |
| **值：**`'Direct form' | 'Direct form symmetric' | 'Direct form antisymmetric' | 'Direct form transposed' | 'Lattice MA'` |
| **默认值：**`'Direct form'` |

#### **系数** — 滤波器系数 `[0.5 0.5]` (默认) | 标量 | 向量 | 矩阵

将滤波器系数指定为标量、向量或矩阵。

当指定滤波器抽头的行向量时，模块会对输入应用单个滤波器。要为同一输入应用多个滤波器，请指定一介系数矩阵，其中每一行代表一组不同的滤波器抽头。要实现多个滤波器，请将**滤波器结构**设置为**直接型**，并且输入必须为标量。

##### 依赖关系

要启用此参数，请将**系数来源**设置为**对话框参数**。

##### 编程用法

|  |
| --- |
| **模块参数**：`Coefficients` |
| **类型：**字符向量 |
| **值：**向量 |
| **默认值：**`'[0.5 0.5]'` |

#### **输入处理** — 基于采样或基于帧的处理 **元素作为通道(基于采样)** (默认) | **列作为通道(基于帧)**

指定模块是执行基于采样还是基于帧的处理。您可以选择以下选项之一：

- **元素作为通道(基于采样)** - 将输入的每个元素作为独立通道处理（基于采样的处理）。
- **列作为通道(基于帧)** - 将输入的每列作为独立通道处理（基于帧的处理）。

  **注意**

  基于帧的处理需要具有 DSP System Toolbox 许可证。

  有关详细信息，请参阅Sample- and Frame-Based Concepts (DSP System Toolbox)。

##### 编程用法

|  |
| --- |
| **模块参数**：`InputProcessing` |
| **类型：**字符向量 |
| **值：**`'Columns as channels (frame based)' | 'Elements as channels (sample based)'` |
| **默认值：**`'Elements as channels (sample based)'` |

#### **初始状态** — 滤波器状态的初始条件 `0` (默认) | 标量 | 向量 | 矩阵

指定滤波器状态的初始条件。要了解如何指定初始状态，请参阅指定初始状态。

##### 编程用法

|  |
| --- |
| **模块参数**：`InitialStates` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值：**`'0'` |

#### **显示使能端口** — 创建使能端口 `off` (默认) | `on`

此选项使用使能端口来控制此模块的执行。当此端口的输入非零时，模块被视为启用；当输入为 `0` 时，模块被视为禁用。输入的值在执行模块的同一时间步进行检查。

##### 编程用法

|  |
| --- |
| **模块参数**：`ShowEnablePort` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

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

要启用此参数，请将**系数来源**参数设置为**对话框参数**。

仅当您有有效的 DSP System Toolbox 许可证时，此参数才会出现。

#### 数据类型

#### **抽头总和** — 抽头加和数据类型 `Inherit: Same as input` (默认) | `Inherit: Inherit via internal rule` | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16,0)** | **<数据类型表达式>**

指定直接型对称或直接型反对称滤波器的抽头加和数据类型，这是滤波器在乘以系数之前计算输入总和时使用的数据类型。可以将其设置为：

- 继承数据类型的规则，例如**继承: 从内部规则继承**
- 内置整数，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 依赖关系

仅当**滤波器结构**设置为**直接型对称**或**直接型反对称**时，此参数才可见。

##### 编程用法

|  |
| --- |
| **模块参数**： `TapSumDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Same as input' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值：**`'Inherit: Same as input'` |

#### **系数** — 系数数据类型 `Inherit: Same wordlength as input` (默认) | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16,0)** | **<数据类型表达式>**

指定系数数据类型。可以将其设置为：

- 继承数据类型的规则，例如**继承: 与输入的字长相同**
- 内置整数，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**： `CoefDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Same word length as input'| 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值：**`'Inherit: Same wordlength as input'` |

#### **系数最小值** — 系数的最小值 `[]` (默认) | 标量

指定滤波器系数应具有的最小值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 参数范围检查（请参阅指定模块参数的最小值和最大值）
- 定点数据类型的自动定标

##### 编程用法

|  |
| --- |
| **模块参数**： `CoeffMin` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'[]'` |

#### **系数最大值** — 系数的最大值 `[]` (默认) | 标量

指定滤波器系数应具有的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 参数范围检查（请参阅指定模块参数的最小值和最大值）
- 定点数据类型的自动定标

##### 编程用法

|  |
| --- |
| **模块参数**： `CoeffMax` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'[]'` |

#### **乘积输出** — 乘积输出数据类型 `Inherit: Inherit via internal rule` (默认) | **继承: 与输入相同** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16,0)** | **<数据类型表达式>**

指定乘积输出的数据类型。可以将其设置为：

- 继承数据类型的规则，例如**继承: 从内部规则继承**
- 内置数据类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**： `ProductDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值：**`'Inherit: Inherit via internal rule'` |

#### **累加器** — 累加器数据类型 `Inherit: Inherit via internal rule` (默认) | **继承: 与输入相同** | **继承: 与乘积输出相同** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16,0)** | **<数据类型表达式>**

指定累加器数据类型。可以将其设置为：

- 继承数据类型的规则，例如**继承: 从内部规则继承**
- 内置数据类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**： `AccumDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'Inherit: Same as product output' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值：**`'Inherit: Inherit via internal rule'` |

#### **状态** — 状态数据类型 `Inherit: Same as accumulator` (默认) | **继承: 与输入相同** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16,0)** | **<数据类型表达式>**

指定状态数据类型。可以将其设置为：

- 继承数据类型的规则，例如**继承: 与累加器相同**
- 内置整数，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

##### 依赖关系

要启用此参数，请将**滤波器结构**设置为**格型 MA**。

##### 编程用法

|  |
| --- |
| **模块参数**： `StateDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Same as accumulator' | 'Inherit: Same as input' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值：**`'Inherit: Same as accumulator'` |

#### **输出** — 输出数据类型 `Inherit: Same as accumulator` (默认) | **继承: 与输入相同** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16)** | **fixdt(1,16,0)** | **<数据类型表达式>**

指定输出数据类型。可以将其设置为：

- 继承数据类型的规则，例如**继承: 与累加器相同**
- 内置数据类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

当模块的输入是浮点时，输出数据类型匹配输入数据类型，因为浮点继承优先于定点设置。

##### 编程用法

|  |
| --- |
| **模块参数**： `OutDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Same as accumulator' | 'Inherit: Same as input' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值：**`'Inherit: Same as accumulator'` |

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

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

此模块支持自定义状态属性以更高效地自定义和生成代码。要访问或设置这些属性，请打开模型数据编辑器。在**建模**选项卡上，点击**模型数据编辑器**。有关示例，请参阅Custom State Attributes in Discrete FIR Filter block。

**使用 Intel AVX2 代码替换库生成 SIMD 代码**

**注意**

需要 Embedded Coder® 许可证

Discrete FIR Filter 模块支持在以下情况下使用 Intel AVX2 代码替换库生成 SIMD 代码：

- **滤波器结构**设置为**直接型**或**直接型转置**。
- **输入处理**设置为**列作为通道(基于帧)**。
- 输入信号是具有实数滤波器系数的实数值。
- 当**滤波器结构**设置为**直接型**时，输入信号是复数值且具有实数或复数滤波器系数。
- 输入信号的数据类型为 `single` 或 `double`。

**利用目标硬件指令集扩展生成 SIMD 代码** *(自 R2022b 起)*

**注意**

需要 Simulink Coder™ 或 Embedded Coder 许可证

在以下情况下，您可以使用模型配置参数**利用目标硬件指令集扩展**为所有 Intel® 平台上、ARM® Cortex®-A 处理器和 Apple 芯片处理器上的 Discrete FIR Filter 模块生成 SIMD 代码：

- 您将**滤波器结构**设置为**直接型**
- 您将**输入处理**设置为**列作为通道(基于帧)**
- 输入信号是具有实数滤波器系数的实数值
- 输入信号是实数值或复数值。
- 输入信号的数据类型为 `single`（ARM Cortex-A 处理器）
- 输入信号的数据类型为 `single` 或 `double`（Intel 平台）

此外，适当地配置您的模型。

在 Simulink 模型窗口的**建模**选项卡中，点击**模型设置**，并在**代码生成**下配置这些参数。

- 在**优化**窗格中：

  - 在**利用目标硬件指令集扩展**参数中提供特定指令集。
  - 选择**优化归约**参数。
  - 在**优化级别**下，将**级别**设置为**最大值**，将**优先级**设置为**最大化执行速度**。
- 在**接口**窗格中的**软件环境**下，清除**非有限数**。

要使用此工作流从此模块生成 SIMD 代码，请参阅Use Intel AVX2 Code Replacement Library to Generate SIMD Code from Simulink Blocks (DSP System Toolbox)。

对于受支持模块上的计算密集型运算，SIMD 固有函数可以显著提高在 Intel 平台上生成代码的性能。有关详细信息，请参阅Optimize Code for Reduction Operations by Using SIMD (Simulink Coder)。要从此模块生成 SIMD 代码，请参阅Generate SIMD Code from Simulink Blocks for Intel Platforms (Simulink Coder)。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**注意**

对于适合硬件的验证和重置控制信号，要在 Simulink 中对硬件延迟行为精确建模，请改用 Discrete FIR Filter (DSP HDL Toolbox) 模块。

**HDL 架构**

该模块将 **HDLDataPath** 作为默认架构。此架构提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 模块属性**

| HDL 模块属性 | 描述 |
| --- | --- |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **FlattenFilter** | 从生成的 HDL 代码中删除滤波器子系统的层次结构。默认值为**自动**。请参阅FlattenHierarchy (HDL Coder)。 |
| **DSPStyle** | 乘法器映射的综合属性。默认值为**无**。另请参阅DSPStyle (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的功能等效的资源的数量。默认值为 0。另请参阅Resource Sharing (HDL Coder)。 |
| **StreamingFactor** | 并行数据路径或向量的数量，这些路径或向量通过时间多路复用的方式变换为串行标量数据路径。默认值为 0，表示实现完全并行的数据路径。另请参阅Streaming (HDL Coder)。 |
| **ConstMultiplierOptimization** | 正则有符号数 (CSD) 或因子化 CSD 优化。默认值为**无**。另请参阅ConstMultiplierOptimization (HDL Coder)。 |
| **MultiplerArchitecture** | 对于乘法器架构，选择**线性**或 **shiftadd**。默认值为**线性**。有关详细信息，请参阅 Product, Matrix Multiply 中的“HDL 代码生成”部分。 |
| **MultiplierInputPipeline** | 指定要在滤波器乘法器输入端添加的流水线阶段数。另请参阅 MultiplierInputPipeline (HDL Coder)。 |
| **MultiplierOutputPipeline** | 指定要在滤波器乘法器输出端添加的流水线阶段数。另请参阅 MultiplierOutputPipeline (HDL Coder)。 |
| **AdderChainArchitecture** | 选择加法器架构以生成加法器的线性链或树状结构来计算元素之和。默认值为**树**。有关详细信息，请参阅 Sum 中的“HDL 代码生成”部分。 |
| **AdderOutputPipeline** | 为执行加法运算而在生成的代码中插入的输出流水线阶段数。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

**数据类型支持**

该模块支持使用以下数据类型进行 HDL 代码生成：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 总线 | 布尔 | 枚举 | 复信号 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **In** | 标量  向量  矩阵 | 是 | 半精度  单精度  双精度 | 是 | 是 | 是 | 是 | 是 |

**优化**

模块参与以下 HDL 优化，以优化速度和面积。

**面积优化**

| 优化 | 描述 |
| --- | --- |
| Resource Sharing (HDL Coder) | *资源复用*是一种面积优化，其中 HDL Coder 确定多个在功能上等效的资源，并用单个资源替换它们。 |
| Streaming (HDL Coder) | *流式处理*是一种面积优化，其中 HDL Coder 将向量数据路径变换为标量数据路径（或多个较小的向量数据路径）。 |

**速度优化**

| 优化 | 描述 |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *分布式流水线*或寄存器重定时是一种速度优化，它可以移动设计中的现有延迟，以在缩减关键路径的同时保留功能性行为。 |
| Clock-Rate Pipelining (HDL Coder) | *时钟频率流水线*是 HDL Coder 中的一个优化框架，它允许其他速度优化和面积优化在时钟频率下引入延迟。 |
| Adaptive Pipelining (HDL Coder) | *自适应流水线*优化创建带寄存器的模块模式或组合，通过在设计中的模块中插入流水线寄存器，可以提高可实现的时钟频率并减少 FPGA 板上的面积使用量。 |
| 关键路径估计 (HDL Coder) | 要快速确定设计中最可能的关键路径，请使用*关键路径估计*。关键路径估计加速寻找关键路径的迭代过程。要了解在关键路径估计中表征的模块，请参阅Characterized Blocks (HDL Coder)。 |

**限制和注意事项**

该模块具有以下限制：

- 您必须将**初始条件**设置为 `0`。非零初始状态不支持 HDL 代码生成。
- **滤波器结构**：**格型 MA**。
- **外部重置**参数必须设置为**无**或**电平保持**。

要为可编程滤波器或多通道滤波器等特殊情况配置 Discrete FIR Filter 模块，请使用以下模块设置：

| 滤波器情形 | 注意事项 |
| --- | --- |
| **可编程滤波器** | HDL Coder 支持对 Discrete FIR Filter 模块使用可编程滤波器。  1. 在过滤器模块封装上，将**系数来源**设置为**输入端口**。 2. 将向量信号连接到 `Num` 系数端口。 |
| **多通道滤波器** | HDL Coder 支持对 Discrete FIR Filter 模块使用向量输入，其中向量的每个元素表示一个独立的通道。  1. 将向量信号连接到 Discrete FIR Filter 模块输入端口。 2. 将**输入处理**指定为**元素作为通道(基于采样)**。 |
| **基于帧的输入** | HDL Coder 支持对 Discrete FIR Filter 模块使用向量输入，其中向量的每个元素表示一个时间点上的采样。一个输入向量最多可包含 512 个采样。基于帧的实现支持定点输入和输出数据类型，并使用全精度内部数据类型。您可以使用具有实系数的实输入信号、具有实系数的复输入信号或具有复系数的实输入信号。您也可以使用具有可编程系数的基于帧的输入。  1. 将向量信号连接到 Discrete FIR Filter 模块输入端口。 2. 将**输入处理**指定为**列作为通道(基于帧)**。对于具有可编程系数的基于帧的输入，请将**滤波器结构**设置为**直接型**。  当您使用基于帧的输入数据时，您可以使用复输入信号和实系数，或复系数和实输入信号。 |
| **具有控制端口的滤波器** | 您可以为具有可选的使能端口和可选的重置端口的滤波器生成 HDL 代码。 |

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2008a 中推出**

#### R2024b: 为 Apple 芯片处理器生成 SIMD 代码

在 R2024b 中，如果您有 Embedded Coder，则可以通过使用模型配置参数**利用目标硬件指令集扩展**，为适用于 Apple 芯片处理器的 Discrete FIR Filter 模块生成 SIMD 代码。有关详细信息，请参阅Use Target Hardware Instruction Set Extensions to Generate SIMD Code from Simulink Blocks for Apple silicon (DSP System Toolbox)。

#### R2024b: 查看滤波器响应

点击**查看滤波器响应**按钮，以可视化您在模块对话框中指定的滤波器的频率响应。

#### R2023b: 为复信号生成 SIMD 代码

在 R2023b 中，如果您有 Embedded Coder，则当输入信号为复数值时，您可以通过使用模型配置参数**利用目标硬件指令集扩展**为 Discrete FIR Filter 模块生成 SIMD 代码。

#### R2023b: **采样时间**参数的条件显示

默认情况下，Discrete FIR Filter 模块不再在“模块参数”对话框中显示**采样时间**参数。仅在命令行或现有模型中将采样时间设置为默认值 (`-1`) 以外的值时，该参数才可见。有关详细信息，请参阅不建议设置采样时间的模块。

## Libraries

Simulink / Discrete HDL Coder / Discrete HDL Coder / HDL Floating Point Operations

## Description

The Discrete FIR Filter block independently filters each channel of the input
signal with the specified digital FIR filter. The block can implement static filters
with fixed coefficients, and time-varying filters with coefficients that change over
time. You can tune the coefficients of a static filter during simulation.

This block filters each channel of the input signal independently
over time. The **Input processing** parameter allows
you to specify whether the block treats each element of the input
as an independent channel (sample-based processing), or each column
of the input as an independent channel (frame-based processing). To
perform frame-based processing, you must have a DSP System Toolbox™ license.

The output dimensions equal the input dimensions, except when you specify a matrix of filter
taps for the **Coefficients** parameter. When you do so, the output
dimensions depend on the number of different sets of filter taps you specify.

This block supports custom state attributes to customize and generate code more efficiently.
For an example, see Custom State Attributes in Discrete FIR Filter block. Under certain
conditions, the block also supports SIMD code generation. For details, see Code Generation.

The outputs of this block numerically match the outputs of the DSP System Toolbox
Digital Filter Design (DSP System Toolbox) block.

This block supports the Simulink® state logging feature. For more information, see State.

### Filter Structure Support

You can change the filter structure implemented with the Discrete FIR Filter block by selecting one of the following from the **Filter structure** parameter:

- `Direct form`
- `Direct form symmetric`
- `Direct form antisymmetric`
- `Direct form transposed`
- `Lattice MA`

You must have an available DSP System Toolbox license
to run a model with any of these filter structures other than `Direct form`.

For more information on the filter structures, see Algorithms.

### Specifying Initial States

The Discrete FIR Filter block initializes the
internal filter states to zero by default, which has the same effect
as assuming that past inputs and outputs are zero. You can optionally
use the **Initial states** parameter to specify nonzero initial conditions for the filter delays.

To determine the number of initial states you must specify and
how to specify them, see the table on valid initial states. The **Initial states** parameter can take one of the forms described in the next table.

**Valid Initial States**

| Initial Condition | Description |
| --- | --- |
| Scalar | The block initializes all delay elements in the filter to the scalar value. |
| Vector or matrix   (for applying different delay elements to each channel) | Each vector or matrix element specifies a unique initial condition for a corresponding delay element in a corresponding channel:  - The vector length equals the product of the number of   input channels and the number of delay elements in the   filter, `#_of_filter_coeffs-1` (or   `#_of_reflection_coeffs` for   `Lattice MA`). - The matrix must have the same number of rows as the   number of delay elements in the filter, `#_of_filter_coeffs-1` (`#_of_reflection_coeffs` for `Lattice MA`), and must have one column for each channel of the input signal. |

## Ports

### Input

### **In** — Input signal scalar | vector | matrix

Input signal to filter, specified as a scalar, vector, or
matrix.

The Discrete FIR Filter block accepts real and complex
signals of any numeric data type supported by Simulink.

#### Dependencies

When you set **Coefficient source** to
`Dialog parameters`, the port for the
input signal is unlabeled. When you set **Coefficient
source** to `Input port`, the
port for the input signal is labeled **In**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes

### **Num** — Filter coefficients scalar | vector

Specify the filter coefficients as a scalar or a vector. When you specify a row vector
of filter taps, the block applies a single filter to the input. To apply
multiple filters to the input, specify the coefficients in the matrix
form through the **Coefficients** parameter.

#### Dependencies

To enable this port, set **Coefficient source**
to `Input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

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

### **⎍** — Enable signal scalar

Enable signal, specified as a scalar. This port can control execution
of the block. The block is enabled when the input to this port is
nonzero, and is disabled when the input is `0`. The
value of the input is checked at the same time step as the block
execution.

#### Dependencies

To enable this port, select the **Show enable
port** check box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Filtered output signal scalar | vector | matrix

Filtered output signal, returned as a scalar, vector, or a matrix. The Discrete
FIR Filter block outputs real and complex signals of any
numeric data type supported by Simulink.

When the input to the block is fixed-point, the data type of the block output is
determined based on the value you specify in the
**Output** parameter. When the input is
floating-point, the output data type matches the input data type since
floating-point inheritance takes precedence over the fixed-point
settings.

When you set **Sample time** to
`-1`, sample time of the output signal is same as the
sample time of the input signal **In**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### Main

### **Coefficient source** — Source of coefficients `Dialog parameters` (default) | `Input port`

Choose to specify the filter coefficients using tunable dialog parameters or through an
input port, which is useful for time-varying coefficients.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CoefSource` |
| **Type:** character vector |
| **Values:** `'Dialog parameters' | 'Input port'` |
| **Default:** `'Dialog parameters'` |

### **Filter structure** — Filter structure `Direct form` (default) | `Direct form symmetric` | `Direct form antisymmetric` | `Direct form transposed` | `Lattice MA`

Select the filter structure you want the block to implement. For more information, see
Algorithms.

#### Dependencies

You must have an available DSP System Toolbox license to run a model with a Discrete FIR
Filter block that implements any filter structure other
than `Direct form`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FilterStructure` |
| **Type:** character vector |
| **Values:** `'Direct form' | 'Direct form symmetric' | 'Direct form antisymmetric' | 'Direct form transposed' | 'Lattice MA'` |
| **Default:** `'Direct form'` |

### **Coefficients** — Filter coefficients `[0.5 0.5]` (default) | scalar | vector | matrix

Specify the filter coefficients as a scalar, vector or a matrix.

When you specify a row vector of filter taps, the block applies a
single filter to the input. To apply multiple filters to the same input,
specify a matrix of coefficients, where each row represents a different
set of filter taps. To implement multiple filters, set **Filter
structure** to `Direct form` and
the input must be a scalar.

#### Dependencies

To enable this parameter, set **Coefficient
source** to `Dialog
parameters`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Coefficients` |
| **Type:** character vector |
| **Values:** vector |
| **Default:** `'[0.5 0.5]'` |

### **Input processing** — Sample- or frame-based processing `Elements as channels (sample based)` (default) | `Columns as channels (frame based)`

Specify whether the block performs sample- or frame-based processing.
You can select one of the following options:

- `Elements as channels (sample based)`
  — Treat each element of the input as an independent
  channel (sample-based processing).
- `Columns as channels (frame based)`
  — Treat each column of the input as an independent
  channel (frame-based processing).

  **Note**

  Frame-based processing requires a DSP System Toolbox license.

  For more information, see Sample- and Frame-Based Concepts (DSP System Toolbox).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputProcessing` |
| **Type:** character vector |
| **Values:** `'Columns as channels (frame based)' | 'Elements as channels (sample based)'` |
| **Default:** `'Elements as channels (sample based)'` |

### **Initial states** — Initial conditions of filter states `0` (default) | scalar | vector | matrix

Specify the initial conditions of the filter states. To learn how to
specify initial states, see Specifying Initial States.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialStates` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'0'` |

### **Show enable port** — Create enable port `off` (default) | `on`

Select to control execution of this block with an enable port. The block is considered
enabled when the input to this port is nonzero, and is disabled when the input is
`0`. The value of the input is checked at the same time step as the
block execution.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowEnablePort` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

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

To enable this parameter, set the **Coefficient source** parameter to
`Dialog parameters`.

This parameter appears only if you have a valid DSP System Toolbox license.

### Data Types

### **Tap sum** — Tap sum data type `Inherit: Same as input` (default) | `Inherit: Inherit via internal rule` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `<data type expression>`

Specify the tap sum data type of a direct form symmetric or direct
form antisymmetric filter, which is the data type the filter uses when
it sums the inputs prior to multiplication by the coefficients. You can
set it to:

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

#### Dependencies

This parameter is only visible when you set the **Filter
structure** to `Direct form
symmetric` or `Direct form
antisymmetric`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `TapSumDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Same as input' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Same as input'` |

### **Coefficients** — Coefficient data type `Inherit: Same wordlength as input` (default) | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `<data type expression>`

Specify the coefficient data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Same word length as
  input`
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
| **Block Parameter:**  `CoefDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Same word length as input'| 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Same wordlength as input'` |

### **Coefficients minimum** — Minimum value of coefficients `[]` (default) | scalar

Specify the minimum value that a filter coefficient should have. The
default value is `[]` (unspecified). Simulink software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
- Automatic scaling of fixed-point data types

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `CoeffMin` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Coefficients maximum** — Maximum value of coefficients `[]` (default) | scalar

Specify the maximum value that a filter coefficient should have. The
default value is `[]` (unspecified). Simulink software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
- Automatic scaling of fixed-point data types

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `CoeffMax` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Product output** — Product output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `<data type expression>`

Specify the product output data type. You can set it to:

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
| **Block Parameter:**  `ProductDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Accumulator** — Accumulator data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `<data type expression>`

Specify the accumulator data type. You can set it to:

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
| **Block Parameter:**  `AccumDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'Inherit: Same as product output' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **State** — State data type `Inherit: Same as accumulator` (default) | `Inherit: Same as input` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `<data type expression>`

Specify the state data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Same as
  accumulator`
- A built-in integer, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

#### Dependencies

To enable this parameter, set the **Filter
structure** to `Lattice
MA`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `StateDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Same as accumulator' | 'Inherit: Same as input' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Same as accumulator'` |

### **Output** — Output data type `Inherit: Same as accumulator` (default) | `Inherit: Same as input` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

Specify the output data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Same as
  accumulator`
- A built-in data type, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

When the input to the block is floating-point, the output data type
matches the input data type since floating-point inheritance takes
precedence over the fixed-point settings.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Same as accumulator' | 'Inherit: Same as input' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Same as accumulator'` |

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

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports custom state attributes to customize and generate code more
efficiently. To access or set these attributes, open the Model Data Editor. On the
**Modeling** tab, click **Model
Data Editor**. For an example, see Custom State Attributes in Discrete FIR Filter block.

**Generate SIMD code using Intel AVX2 code replacement
library**

**Note**

Requires Embedded Coder® license

The Discrete FIR Filter block supports SIMD code generation using Intel AVX2
code replacement library under these conditions:

- **Filter structure** is set to `Direct
  form` or `Direct form
  transposed`.
- **Input processing** is set to `Columns
  as channels (frame based)`.
- Input signal is real-valued with real filter coefficients.
- When **Filter structure** is set to
  `Direct form`, input signal is
  complex-valued with real or complex filter coefficients.
- Input signal has a data type of `single` or
  `double`.

**Generate SIMD code by
leveraging target hardware instruction set extensions** *(since R2022b)*

**Note**

Requires Simulink
Coder™ or Embedded Coder license

You can generate SIMD code for the Discrete FIR Filter block on all
Intel® platforms, ARM®
Cortex®-A processors, and Apple silicon processors by using the model configuration parameter
**Leverage target hardware instruction set extensions** under
these conditions:

- You set **Filter structure** to `Direct
  form`
- You set **Input processing** to `Columns
  as channels (frame based)`
- Input signal is real-valued with real filter coefficients
- Input signal is real-valued or complex-valued.
- Data type of the input signal is `single`
  (ARM
  Cortex-A processors)
- Data type of the input signal is `single` or
  `double` (Intel platforms)

In addition, configure your model appropriately.

In the **Modeling** tab of the Simulink model window, click **Model Settings** and configure
these parameters under **Code Generation**.

- In the **Optimization** pane:

  - Provide a specific instruction set in the
    **Leverage target hardware instruction set
    extensions** parameter.
  - Select the **Optimize reductions**
    parameter.
  - Under **Optimization levels**, set
    **Level** to
    `Maximum` and
    **Priority** to `Maximize
    execution speed`.
- In the **Interface** pane, under **Software
  environment**, clear **non-finite
  numbers**.

To generate SIMD code from this block using this workflow, see Use Intel AVX2 Code Replacement Library to Generate SIMD Code from Simulink Blocks (DSP System Toolbox).

For computationally intensive operations on supported blocks, SIMD intrinsics can
significantly improve the performance of the generated code on Intel platforms. For
more details, see Optimize Code for Reduction Operations by Using SIMD (Simulink Coder). To generate SIMD
code from this block, see Generate SIMD Code from Simulink Blocks for Intel Platforms (Simulink Coder).

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**Note**

For hardware-friendly valid and reset control signals, and to model exact
hardware latency behavior in Simulink, use the Discrete FIR Filter (DSP HDL Toolbox) block
instead.

**HDL Architecture**

The block has `HDLDataPath` as a default
architecture. This architecture provides additional configuration options that
affect HDL implementation and synthesized logic.

**HDL Block Properties**

| HDL Block Properties | Description |
| --- | --- |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **FlattenFilter** | Remove hierarchy of Filter subsystem from generated HDL code. The default is `auto`. See FlattenHierarchy (HDL Coder). |
| **DSPStyle** | Synthesis attributes for multiplier mapping. The default is `none`. See also DSPStyle (HDL Coder). |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing (HDL Coder). |
| **StreamingFactor** | Number of parallel data paths, or vectors, that are time multiplexed to transform into serial, scalar data paths. The default is 0, which implements fully parallel data paths. See also Streaming (HDL Coder). |
| **ConstMultiplierOptimization** | Canonical signed digit (CSD) or factored CSD optimization. The default is `none`. See also ConstMultiplierOptimization (HDL Coder). |
| **MultiplerArchitecture** | Select the multipler architecture as `linear` or `shiftadd`. The default is `linear`. For more information, see HDL Code Generation section in Product, Matrix Multiply. |
| **MultiplierInputPipeline** | Specify the number of pipeline stages to add at filter multiplier inputs. See also MultiplierInputPipeline (HDL Coder). |
| **MultiplierOutputPipeline** | Specify the number of pipeline stages to add at filter multiplier outputs. See also MultiplierOutputPipeline (HDL Coder). |
| **AdderChainArchitecture** | Select the adder architecture to generate linear chain or tree structure of adders to compute sum of elements. The default is `tree`. For more information, see HDL Code Generation section in Sum. |
| **AdderOutputPipeline** | Number of output pipeline stages to insert in the generated code for addition operation. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Data Type Support**

The block supports these data types for HDL code generation:

| Input Port | Dimension | Fixed-Point | Floating-Point | Built-in Integers | Bus | Boolean | Enumerated | Complex Signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **In** | Scalar  Vector  Matrix | Yes | Half  Single  Double | Yes | Yes | Yes | Yes | Yes |

**Optimizations**

The block participates in these HDL optimizations to optimize the speed, and
area.

**Area Optimization**

| Optimization | Description |
| --- | --- |
| Resource Sharing (HDL Coder) | *Resource sharing* is an area optimization in which HDL Coder identifies multiple functionally equivalent resources and replaces them with a single resource. |
| Streaming (HDL Coder) | *Streaming* is an area optimization in which HDL Coder transforms a vector data path to a scalar data path (or to several smaller-sized vector data paths). |

**Speed Optimization**

| Optimization | Description |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *Distributed pipelining*, or register retiming, is a speed optimization that moves existing delays in a design to reduce the critical path while preserving functional behavior. |
| Clock-Rate Pipelining (HDL Coder) | *Clock-rate pipelining* is an optimization framework in HDL Coder that allows other speed and area optimizations to introduce latency at the clock rate. |
| Adaptive Pipelining (HDL Coder) | *Adaptive pipelining* optimization creates patterns or combination of blocks with registers that can improve the achievable clock frequency and reduce the area usage on the FPGA boards by inserting pipeline registers to the blocks in your design. |
| Critical Path Estimation (HDL Coder) | To quickly identify the most likely critical path in your design, use *Critical Path Estimation*. Critical path estimation speeds up the iterative process of finding the critical path. To know blocks that are characterized in critical path estimation, see Characterized Blocks (HDL Coder). |

**Limitations and Considerations**

The block has these limitations:

- You must set **Initial conditions** to
  `0`. HDL code generation is not supported for
  nonzero initial states.
- **Filter Structure**: `Lattice
  MA`.
- **External reset** parameter must be set to
  `None` or `Level
  hold`.

To configure the Discrete FIR Filter block for special cases
such as a programmable filter or a multichannel filter, use the following block
settings:

| Filter Case | Considerations |
| --- | --- |
| **Programmable Filter** | HDL Coder supports programmable filters for Discrete FIR Filter blocks.  1. On the filter block mask, set    **Coefficient source** to    **Input port**. 2. Connect a vector signal to the    `Num` coefficient port. |
| **Multichannel Filter** | HDL Coder supports the use of vector inputs to Discrete FIR Filter blocks, where each element of the vector represents an independent channel.  1. Connect a vector signal to the Discrete FIR    Filter block input port. 2. Specify **Input processing** as    `Elements as channels (sample    based)`. |
| **Frame-Based Input** | HDL Coder supports the use of vector inputs to Discrete FIR Filter blocks, where each element of the vector represents a sample in time. You can use an input vector of up to 512 samples. The frame-based implementation supports fixed-point input and output data types, and uses full-precision internal data types. You can use real input signals with real coefficients, complex input signals with real coefficients, or real input signals with complex coefficients. You can also use frame-based input with programmable coefficients.  1. Connect a vector signal to the Discrete FIR    Filter block input port. 2. Specify **Input processing** as    `Columns as channels (frame    based)`. For frame-based input with    programmable coefficients, set **Filter    structure**  to `Direct    form`.  When you use frame-based input data you can use either complex input signals and real coefficients, or complex coefficients and real input signals. |
| **Filter with Control Ports** | You can generate HDL code for filters with the optional enable port, and with the optional reset port. |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2008a**

### R2024b: Generate SIMD code for Apple silicon processors

In R2024b, if you have Embedded Coder, you can generate SIMD code for the Discrete FIR Filter
block for Apple silicon processors by using the model configuration parameter
**Leverage target hardware instruction set extensions**. For
more information, see Use Target Hardware Instruction Set Extensions to Generate SIMD Code from Simulink Blocks for Apple silicon (DSP System Toolbox).

### R2024b: View filter response

Click the **View Filter Response** button to visualize the frequency
response of the filter that you specify in the block dialog box.

### R2023b: Generate SIMD Code for Complex Signals

In R2023b, if you have Embedded Coder, you can generate SIMD code for the Discrete FIR Filter
block when the input signal is complex-valued by using the model configuration
parameter **Leverage target hardware instruction set
extensions**.

### R2023b: Conditional display of the **Sample time** parameter

The Discrete FIR Filter block no longer displays the
**Sample time** parameter in the block parameters dialog box by
default. The parameter is visible only if you set the sample time to a value other
the default value (`-1`) at the command line or in an existing
model. For more information, see Blocks for Which Sample Time Is Not Recommended.
