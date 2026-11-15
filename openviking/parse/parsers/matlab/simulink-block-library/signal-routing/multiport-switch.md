---
type: simulink-block
title: 'Multiport Switch'
family: signal-routing
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'multiportswitch'
---

# Multiport Switch

Select output signal based on control signal

## 中文

基于控制信号选择输出信号

### 所属库

Simulink / Signal Routing HDL Coder / Signal Routing

### 描述

Multiport Switch 模块用于确定将多个模块输入中的哪一个传递给输出。此模块根据第一个输入的值来确定选择哪个输入。第一个输入是控制输入，其余输入是数据输入。控制输入的值确定将哪个数据输入传递给输出。

Multiport Switch 和 Index Vector 模块是同一模块的替代配置。

- Multiport Switch - 基于控制信号选择输出信号。
- Index Vector - 基于第一个输入的值在不同输入之间切换输出。

下表概述了 Multiport Switch 如何解释控制输入，以及如何确定传递给输出的数据输入。

| 控制输入 | 截断 | 数据端口顺序的设置 | 仿真过程中的模块行为 | |
| --- | --- | --- | --- | --- |
| 选择数据输入的索引方式 | 超出范围的情况 |
| 整数值 | 无 | **从 0 开始连续** | 从零开始进行索引 | 控制输入小于 `0` 或大于数据输入数减 1。 |
| **从 1 开始连续** | 从一开始进行索引 | 控制输入小于 `1` 或大于数据输入数。 |
| **指定索引** | 按用户指定进行索引 | 控制输入与任何指定的数据端口索引均不对应。 |
| 非整数值 | 模块通过向零舍入将值截断为整数。 | **从 0 开始连续** | 从零开始进行索引 | 截断的控制输入小于 `0` 或大于数据输入数减 1。 |
| **从 1 开始连续** | 从一开始进行索引 | 截断的控制输入小于 `1` 或大于数据输入数。 |
| **指定索引** | 按用户指定进行索引 | 截断的控制输入与任何指定的数据端口索引均不对应。 |

有关此模块如何处理超出范围的情况的信息，请参阅模块如何处理超出范围的控制输入。

#### 配置为 Index Vector 模块的 Multiport Switch

Index Vector 是特殊配置的 Multiport Switch 模块，需要指定一个数据输入，控制输入从 0 开始。模块输出是其索引与控制输入匹配的输入向量的元素。例如，如果输入向量为 `[18 15 17 10]`，控制输入为 `3`，则与索引 3（从 0 开始）匹配的元素为 10，它将成为输出值。

要将 Multiport Switch 模块配置为 Index Vector 模块，请将**数据端口数量**设置为 **1** 且**数据端口顺序**设置为**从 0 开始连续**。

#### 模块如何处理超出范围的控制输入

对于整数值小于 `intmax(‘int32’)` 的输入，当此值与任何数据端口索引均不匹配时，即说明输入超出了范围。对于非整数值控制输入，当*截断*的值与任何数据端口索引均不匹配时，即说明输入超出了范围。在这两种情况下，模块行为均取决于**默认情况数据端口**和**默认情况诊断**的设置。

**注意**

如果控制输入大于 `intmax(‘int32’)`，模块会将输入值绕回为整数。

**仿真行为**

以下行为仅适用于模型仿真。

| 默认情况数据端口 | 默认情况诊断 | | |
| --- | --- | --- | --- |
| 无 | 警告 | 错误 |
| **最后一个数据端口** | 使用最后一个数据端口，不报告任何警告或错误。 | 使用最后一个数据端口并报告警告消息。 | 报告错误并停止仿真。 |
| **附加数据端口** | 使用带有 `*` 标签的其他数据端口，不报告任何警告或错误。 | 使用带有 `*` 标签的其他数据端口并报告警告消息。 | 报告错误并停止仿真。 |

**代码生成行为**

以下行为适用于模型的代码生成。

| 默认情况数据端口 | 默认情况诊断 | | |
| --- | --- | --- | --- |
| 无 | 警告 | 错误 |
| **最后一个数据端口** | 使用最后一个数据端口。 | 使用最后一个数据端口。 | 使用最后一个数据端口。 |
| **附加数据端口** | 使用带有 `*` 标签的其他数据端口。 | 使用带有 `*` 标签的其他数据端口。 | 使用带有 `*` 标签的其他数据端口。 |

#### 使用具有不同维度的数据输入

如果两个信号具有不同数量的维度或不同的维度长度，您可以将这两个信号用作 Multiport Switch 模块的数据输入。在模块对话框中，选择参数**允许不同数据输入大小**。在此例中，模块的输出是大小可变信号。如果您不选择此参数，模块将生成错误。

有关该参数的详细信息，请参阅允许不同数据输入大小(产生可变大小的输出信号)。有关大小可变信号的详细信息，请参阅可变大小信号基础知识。

#### 确定模块行为的规则

您可以使用**数据端口数量**指定数据输入的数目。

- 如果将**数据端口数量**设置为 1，则模块相当于一个*索引选择器*或*索引向量*，而不是一个 Multiport Switch 模块。有关详细信息，请参阅配置为 Index Vector 模块的 Multiport Switch。
- 如果将**数据端口数量**设置为大于 1 的整数，模块则相当于一个 Multiport Switch 模块。模块输出是与控制输入值对应的数据输入。如果数据输入中至少有一个是向量，模块输出即为向量。在这种情况下，模块会将任何标量输入都扩展为向量。
- 如果所有数据输入都为标量，则输出为标量。

#### 枚举控制端口的参数设置原则

当 Multiport Switch 模块上的控制端口为枚举类型时，请遵循以下原则：

| 情况 | 操作 | 理由 |
| --- | --- | --- |
| 枚举类型包含的值代表无效、超出范围或未初始化的值。 | - 将**数据端口顺序**设置为**指定索引**。 - 将**数据端口索引**设置为针对最后一个数据端口使用此值。 - 将**默认情况数据端口**设置为**最后一个数据端口**。 | 此模块配置用于处理枚举类型显式表示的无效值。 |
| 枚举类型仅包含有效的枚举值。但是，数据输入端口可以获得无效的枚举类型值。 | - 将**默认情况数据端口**设置为**附加数据端口**。 | 此模块配置用于处理枚举类型未显式表示的无效值。 |
| 枚举类型仅包含有效的枚举值。数据输入端口永远不会获得无效的枚举类型值。 | - 将**默认情况数据端口**设置为**最后一个数据端口**。 - 将**默认情况诊断**设置为**无**。 | 此模块配置可避免不必要的诊断操作。 |
| 模块没有为枚举类型的每个值提供一个数据输入端口。 | - 将**默认情况数据端口**设置为**附加数据端口**。 | 此模块配置用于处理没有数据输入端口的枚举值和无效值。 |

### 端口

#### 输入

#### **Port\_1** — 控制信号 标量

控制信号可以是 Simulink® 支持的任何数据类型，包括定点和枚举类型。当控制输入不是整数值时，模块通过向零舍入将值截断为整数。

有关枚举类型的控制信号的信息，请参阅枚举控制端口的参数设置原则。

有关此模块如何处理超出范围的情况的信息，请参阅模块如何处理超出范围的控制输入。

##### 限制

- 如果控制信号为数值，则控制信号不能为复数。
- 如果控制信号为枚举信号，模块将使用基础整数值来选择数据端口。
- 如果基础整数没有对应的数据端口，将出现错误。
- 如果控制输入是超出整数数据类型范围的浮点值，Multiport Switch 模块将发出运行时错误。此范围包括 `Inf` 和 `NaN`。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `image`

#### **1** — 第一个数据输入 标量 | 向量 | 矩阵 | N 维数组

第一个数据输入，指定为标量、向量、矩阵或 N 维数组。所有数据信号可以是 Simulink 支持的任何数据类型。

- 如果所有数据输入都为标量，则输出为标量
- 如果数据输入中至少有一个是向量，模块输出即为向量。在这种情况下，模块会将任何标量输入都扩展为向量。
- 如果任何两个非标量信号具有不同维数量或不同维度长度，请选中**允许不同数据输入大小**复选框。有关详细信息，请参阅使用具有不同维度的数据输入。
- 如果有任何数据信号为枚举类型，则所有其他信号也必须为相同的枚举类型。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `string` | `image`

#### **2** — 第二个数据输入 标量 | 向量 | 矩阵 | N 维数组

第二个数据输入，指定为标量、向量、矩阵或 N 维数组。所有数据信号可以是 Simulink 支持的任何数据类型。

- 如果所有数据输入都为标量，则输出为标量
- 如果数据输入中至少有一个是向量，模块输出即为向量。在这种情况下，模块会将任何标量输入都扩展为向量。
- 如果任何两个非标量信号具有不同维数量或不同维度长度，请选中**允许不同数据输入大小**复选框。有关详细信息，请参阅使用具有不同维度的数据输入。
- 如果有任何数据信号为枚举类型，则所有其他信号也必须为相同的枚举类型。

##### 依赖关系

要启用此端口，请将**数据端口数量**设置为大于 1 的整数。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `string` | `image`

#### **N** — 第 N 个数据输入 标量 | 向量 | 矩阵 | N 维数组

第 N 个数据输入，指定为标量、向量、矩阵或 N 维数组。所有数据信号可以是 Simulink 支持的任何数据类型。

- 如果所有数据输入都为标量，则输出为标量
- 如果数据输入中至少有一个是向量，模块输出即为向量。在这种情况下，模块会将任何标量输入都扩展为向量。
- 如果任何两个非标量信号具有不同维数量或不同维度长度，请选中**允许不同数据输入大小**复选框。有关详细信息，请参阅使用具有不同维度的数据输入。
- 如果有任何数据信号为枚举类型，则所有其他信号也必须为相同的枚举类型。

##### 依赖关系

要启用第 *N* 个输入端口，请将**数据端口数量**设置为大于或等于 *N* 的整数值。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `string` | `image`

#### **\*** — 用于超出范围的输入的数据端口 标量 | 向量 | 矩阵 | N 维数组

用于超出范围的控制信号输入的输入数据端口，指定为标量、向量、矩阵或 N 维数组。所有数据信号可以是 Simulink 支持的任何数据类型。如果有任何数据信号为枚举类型，则所有其他信号也必须为相同的枚举类型。如果任何两个信号具有不同维数量或不同维度长度，请选中**允许不同数据输入大小**复选框。有关详细信息，请参阅使用具有不同维度的数据输入。

##### 依赖关系

要为超出范围的控制信号输入创建一个附加数据端口，请将**默认情况数据端口**设置为**附加数据端口**。如果将**默认情况数据端口**设置为**最后一个数据端口**，则当控制信号值与任何数据端口索引都不匹配时，模块将使用最后一个数据端口进行输出。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
#### 输出

#### **Port\_1** — 所选数据输入，基于控制信号值 标量 | 向量 | 矩阵 | N 维数组

模块输出根据控制信号值选择的数据输入之一。输出的维度与对应的数据输入相同。输出数据类型是需要最大内存空间的输入端口的数据类型。当您选中**允许不同数据输入大小**复选框时，模块的输出是可变大小信号。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `enumerated` | `string` | `image`

### 参数

#### 常设

#### **数据端口顺序** — 数据输入端口的排序类型 **从 1 开始连续** | **从 0 开始连续** | **指定索引**

指定数据输入端口的排序类型。

- **从 0 开始连续** - 模块使用从 0 开始的索引方式为连续数据端口排序。这是 Index Vector 模块的默认值。
- **从 1 开始连续** - 模块使用从 1 开始的索引方式为连续数据端口排序。这是 Multiport Switch 模块的默认值
- **指定索引** - 模块使用不连续的索引方式为数据端口排序。

##### 提示

- 当控制端口为枚举类型时，请选择**指定索引**。
- 如果选择**从 0 开始连续**或**从 1 开始连续**，请确认控制端口不是枚举类型。此配置已弃用，如果使用将会生成错误。您可以在模型上运行升级顾问，将此配置中的每个 Multiport Switch 模块替换为显式指定数据端口索引的模块。请参阅模型升级。
- 在仿真或代码生成中，应避免出现模块包含未使用的数据端口的情况。当控制端口为定点或内置数据类型时，请确认所有数据端口索引都可用该类型表示。否则，将发生以下模块行为：

  | 如果模块具有未使用的数据端口且数据端口顺序为： | 该模块产生： |
  | --- | --- |
  | **从 0 开始连续**或**从 1 开始连续** | 警告 |
  | **指定索引** | 错误 |

##### 依赖关系

选择**从 0 开始连续**或**从 1 开始连续**将启用**数据端口数量**参数。

选择**指定索引**将启用**数据端口索引**参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`DataPortOrder` |
| **类型：**字符向量 |
| **值：**`'Zero-based contiguous' | 'One-based contiguous' | 'Specify indices'` |
| **默认值：**`'One-based contiguous'` (Multiport Switch) | `'Zero-based contiguous'` (Index Vector) |

#### **数据端口数量** — 数据输入端口的个数 `1` | `3` | 在 1 和 65535 之间的整数

指定模块的数据输入端口数。输入端口的总数是您指定的数量加 1（用于控制信号输入端口）；如果您将**默认情况数据端口**设置为**附加数据端口**，则还要再加 1（用于额外的输入端口）。

##### 依赖关系

要启用此参数，请将**数据端口顺序**设置为**从 0 开始连续**或**从 1 开始连续**。

##### 编程用法

|  |
| --- |
| **模块参数**：`Inputs` |
| **类型：**字符向量 |
| **值：**1 和 65536 之间的整数 |
| **默认值：**`'3'` (Multiport Switch) | `'1'` (Index Vector) |

#### **数据端口索引** — 数据端口的索引数组 `{1,2,3}` (默认) | 索引数组

为数据端口指定索引数组。模块图标将发生变化以匹配您指定的数据端口索引。

##### 提示

- 要指定与枚举类型的所有值对应的索引数组，请输入 `enumeration('name of the type')`。

  例如，如果 `enumeration('MyColors')` 是枚举类型的名称，则 `MyColors` 是有效条目。
- 要输入枚举类型的特定值，请使用 *`type_name.enumerated_name`* 格式。请不要输入基础整数值。

  例如，`enumeration({MyColors.Red, MyColors.Green, MyColors.Blue})` 就是有效的输入。
- 要指示多个值映射到一个数据端口，请使用方括号。

  例如，以下两个输入均有效：

  - `enumeration({MyColors.Red, MyColors.Green, [MyColors.Blue, MyColors.Yellow]})`
  - `enumeration({[3,5],0,18})`
- 如果控制端口为定点或内置数据类型，**数据端口索引**的值必须能用该类型表示。否则，编译时将出现错误，提醒您存在未使用的数据端口。
- 如果控制端口为枚举数据类型，**数据端口索引**的值必须为该类型的枚举值。
- 如果**数据端口索引**包含枚举类型的值，控制端口必须为该数据类型。

##### 依赖关系

要启用此参数，请将**数据端口顺序**设置为**指定索引**。

##### 编程用法

|  |
| --- |
| **模块参数**：`DataPortIndices` |
| **类型：**字符向量 |
| **值：**索引数组 |
| **默认值：**`'{1,2,3}'` |

#### **默认情况数据端口** — 用于超出范围的输入的端口 **最后一个数据端口** (默认) | **附加数据端口**

指定对于超出范围的输入，是使用最后一个数据端口还是使用其他端口。端口名称旁的星号 (\*) 表示控制端口值不匹配任何数据端口索引时模块将使用的端口。

- **最后一个数据端口** - 当控制端口值与任何数据端口索引均不匹配时，模块将使用最后一个数据端口进行输出。
- **附加数据端口** - 当控制端口值与任何数据端口索引均不匹配时，模块将使用其他数据端口进行输出。

##### 提示

如果将此参数设置为**附加数据端口**且**数据端口数量**为 **3**，则模块上的输入端口数为 5。第一个输入是控制端口，后面三个输入为数据端口，第五个输入是用于超出范围的输入的默认端口。

##### 编程用法

|  |
| --- |
| **模块参数**：`DataPortForDefault` |
| **类型：**字符向量 |
| **值：**`'Last data port' | 'Additional data port'` |
| **默认值：**`'Last data port'` |

#### **默认情况诊断** — 控制端口值与数据端口索引不匹配时的诊断操作 **错误** (默认) | **警告** | **无**

指定当控制端口值与任何端口索引均不匹配时要采取的诊断操作。

- **无** - 不产生任何响应。
- **警告** - 显示警告并继续进行仿真。
- **错误** - 终止仿真并显示错误。在这种情况下，**默认情况数据端口**只用于代码生成，而不用于仿真。

有关详细信息，请参阅模块如何处理超出范围的控制输入。

##### 编程用法

|  |
| --- |
| **模块参数**：`DiagnosticForDefault` |
| **类型：**字符向量 |
| **值：**`'None' | 'Warning' | 'Error'` |
| **默认值：**`'Error'` |

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

#### 信号属性

#### **要求所有数据端口输入具有相同的数据类型** — 要求所有输入具有相同的数据类型 `off` (默认) | `on`

选中此复选框将要求所有数据输入端口具有相同的数据类型。清除此复选框时，模块允许数据端口输入具有不同数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`InputSameDT` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

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

#### **输出数据类型** — 指定输出数据类型 **继承: 从内部规则继承** (默认) | **继承: 通过反向传播继承** | **继承: 与第一个数据输入相同** | **double** | **single** | **half** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16)** | **fixdt(1,16,0)** | **fixdt(1,16,2^0,0)** | **字符串** | **Simulink.ImageType(480,640,3)** | **<数据类型表达式>**

为输出选择数据类型。该类型可以继承、直接指定或表示为数据类型对象，如 `Simulink.NumericType`。

当您选择继承的选项时，模块的行为如下所示：

- **继承: 从内部规则继承** - Simulink 在考虑嵌入式目标硬件的属性的同时，会选择相应的数据类型来平衡数值准确性、性能和生成的代码大小。如果更改了嵌入式目标的设置，则依内部规则选择的数据类型可能会发生变化。有时软件不能同时满足优化代码效率和保证数值准确性这两个需求。如果内部规则不能满足您对数值准确性或性能的特定需求，请使用下列选项之一：

  - 显式指定输出数据类型。
  - 显式指定默认数据类型（例如 `fixdt(1,32,16)`），然后使用定点工具为您的模型提供数据类型建议。有关详细信息，请参阅 `fxptdlg` (Fixed-Point Designer)。
  - 要指定您自己的继承规则，请使用**继承: 通过反向传播继承**，然后使用 Data Type Propagation 模块。有关如何使用此模块的示例说明，请参阅 Signal Attributes 模块库中的 Data Type Propagation Examples 模块。
- **继承: 通过反向传播继承** - 使用驱动模块的数据类型。
- **继承: 与第一个数据输入相同** - 使用第一个数据输入端口的数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Inherit via internal rule` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'string'` | `Simulink.ImageType(480,640,3)` | `'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

#### **锁定输出数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选中此选项将锁定此模块的输出数据类型设置，从而防止通过定点工具和定点顾问进行更改。有关详细信息，请参阅Use Lock Output Data Type Setting (Fixed-Point Designer)。

##### 编程用法

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

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

#### **允许不同数据输入大小(产生可变大小的输出信号)** — 允许不同大小的输入信号 `off` (默认) | `on`

选中此复选框将允许输入信号具有不同大小。

- `On` - 允许输入信号具有不同大小，并将输入信号的大小传播给输出信号。在此模式下，模块产生可变大小的输出信号。
- `Off` - 要求所有非标量数据输入信号的大小相同。

##### 编程用法

|  |
| --- |
| **参数：**`AllowDiffInputSizes` |
| **类型：**字符向量 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'off'` |

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

#### **符号性** — 指定有符号或无符号 `Signed` (默认) | `Unsigned`

指定定点数据是有符号还是无符号。有符号数据可以表示正值和负值，无符号数据只表示正值。

- **有符号**，将定点数据指定为有符号数据。
- **无符号**，将定点数据指定为无符号数据。

有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 依赖关系

要启用此参数，请将**模式**设置为 `Fixed point`。

#### **定标** — 定标定点数据的方法 **最佳精度** (默认) | **二进制小数点** | **斜率和偏置**

指定定点数据的定标方法，以避免发生溢出情况并最大限度地减少量化误差。有关详细信息，请参阅指定定点数据类型。

##### 依赖关系

要启用此参数，请将**模式**设置为**定点**。

#### **字长** — 存储量化整数的字的位大小 `16` (默认) | 从 0 到 32 的整数

指定存储量化整数的字的位大小。有关详细信息，请参阅指定定点数据类型。

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

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **CodingStyle** | 指定是用 case 语句还是 if-else 语句生成 HDL 代码。默认情况下，HDL Coder 会生成 if-else 语句。另请参阅CodingStyle (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

| 原生浮点 | |
| --- | --- |
| **LatencyStrategy** | 指定对于浮点运算符是否将设计中的模块映射到 `inherit`、`Max`、`Min` 或 `Zero`。默认值为 **inherit**。另请参阅LatencyStrategy (HDL Coder)。 |

**复数数据支持**

此模块支持复信号的代码生成。

**使用指定索引模式设置数据端口索引**

您可以使用指定索引模式指定输入端口的数据端口索引。要使用指定索引模式配置 Multiport Switch 模块，请将**数据端口顺序**模块参数设置为**指定索引**。然后，在**数据端口索引**模块参数中输入端口索引。对于以 HDL 代码生成为目标的模型，您可以在指定索引模式下将这些输入数据类型用于控制输入：

- 定点和浮点类型
- 有符号和无符号整数类型
- 枚举类型
- 向量、矩阵和总线类型

**使用枚举类型作为端口索引**

您可以将**数据端口顺序**设置为**指定索引**，并为**数据端口索引**输入枚举值。例如，您可以将 Enumerated Constant 模块连接到 Multiport Switch 控制端口，并将枚举类型用作数据端口索引。

**限制**

您必须避免在控制端口上使用 `NaN` 或超出范围的值。它会导致在验证模型中的仿真不匹配。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

#### R2024a: 当输入具有浮点值时，Multiport Switch 模块出现运行时错误

当第一个端口中的控制信号的浮点值超出整数的数据类型范围时，Multiport Switch 模块现在会发出运行时错误。此范围包括 `Inf` 和 `NaN`。

## Libraries

Simulink / Signal Routing HDL Coder / Signal Routing

## Description

The Multiport Switch block determines which of several inputs to the block
passes to the output. The block bases this decision on the value of the first input. The
first input is the control input and the remaining inputs are the data inputs. The value
of the control input determines which data input passes to the output.

The Multiport Switch and Index Vector blocks are alternative
configurations of the same block.

- Multiport Switch — Select output signal based on control signal.
- Index Vector — Switch output between different inputs based on
  value of first input.

The table summarizes how Multiport Switch interprets the control input and
determines the data input that is passed to the output.

| Control Input | Truncation | Setting for Data Port Order | Block Behavior During Simulation | |
| --- | --- | --- | --- | --- |
| Indexing to Select Data Input | Out-of-Range Condition |
| Integer value | None | `Zero-based contiguous` | Zero-based indexing | The control input is less than `0` or greater than the number of data inputs minus one. |
| `One-based contiguous` | One-based indexing | The control input is less than `1` or greater than the number of data inputs. |
| `Specify indices` | Indices you specify | The control input does not correspond to any specified data port index. |
| Not an integer value | The block truncates the value to an integer by rounding to zero. | `Zero-based contiguous` | Zero-based indexing | The truncated control input is less than `0` or greater than the number of data inputs minus one. |
| `One-based contiguous` | One-based indexing | The truncated control input is less than `1` or greater than the number of data inputs. |
| `Specify indices` | Indices you specify | The truncated control input does not correspond to any specified data port index. |

For information on how the block handles the out-of-range condition, see
How the Block Handles an Out-of-Range Control Input.

### Multiport Switch Configured as an Index Vector Block

An Index Vector is a special
configuration of a Multiport Switch block in which you specify one
data input and the control input is zero-based. The block output is the element of
the input vector whose index matches the control input. For example, if the input
vector is `[18 15 17 10]` and the control input is
`3`, the element that matches the index of 3 (zero-based) is
10, and that becomes the output value.

To configure a Multiport Switch block to work as an Index
Vector block, set **Number of data ports** to
`1` and **Data port order** to
`Zero-based contiguous`.

### How the Block Handles an Out-of-Range Control Input

For an input with an integer value less than `intmax(‘int32’)`, the input
is out of range when the value does not match any data port indices. For a control
input that is not an integer value, the input is out of range when the
*truncated* value does not match any data port indices. In
both cases, the block behavior depends on your settings for **Data port for
default case** and **Diagnostic for default
case**.

**Note**

If the control input is larger than `intmax(‘int32’)`, the
block wraps the input value to an integer.

**Behavior for Simulation**

The following behavior applies only to simulation for your model.

| Data Port for Default Case | Diagnostic for Default Case | | |
| --- | --- | --- | --- |
| None | Warning | Error |
| `Last data port` | Use the last data port and do not report any warning or error. | Use the last data port and report a warning. | Report an error and stop simulation. |
| `Additional data port` | Use the additional data port with a `*` label and do not report any warning or error. | Use the additional data port with a `*` label and report a warning. | Report an error and stop simulation. |

**Behavior for Code Generation**

The following behavior applies to code generation for your model.

| Data Port for Default Case | Diagnostic for Default Case | | |
| --- | --- | --- | --- |
| None | Warning | Error |
| `Last data port` | Use the last data port. | Use the last data port. | Use the last data port. |
| `Additional data port` | Use the additional data port with a `*` label. | Use the additional data port with a `*` label. | Use the additional data port with a `*` label. |

### Use Data Inputs That Have Different Dimensions

If two signals have a different number of dimensions or different
dimension lengths, you can use the signals as data inputs to a Multiport Switch block. In the block dialog box, select the parameter **Allow different data input sizes**. In this case, the output of the block is a variable-size signal. If you do not select this parameter, the block generates an error.

For more information about the parameter, see Allow different data input sizes (Results in variable-size output signal). For
more information about variable-size signals, see Variable-Size Signal Basics.

### Rules That Determine the Block Behavior

You specify the number of data inputs with **Number of data ports**.

- If you set **Number of data ports** to
  1, the block behaves as an *index selector* or *index vector* and not as a multiport switch. For more details,
  see Multiport Switch Configured as an Index Vector Block.
- If you set **Number of data ports** to an integer greater than 1, the block behaves as a multiport switch. The block output is the data input that corresponds to the value of the control input. If at least one of the data inputs is a vector, the block output is a vector. In this case, the block expands any scalar inputs to vectors.
- If all the data inputs are scalar, the output is a scalar.

### Guidelines on Setting Parameters for Enumerated Control Port

When the control port on the Multiport Switch block is of enumerated type, follow these guidelines:

| Scenario | What to Do | Rationale |
| --- | --- | --- |
| The enumerated type contains a value that represents invalid, out-of-range, or uninitialized values. | - Set **Data port order** to `Specify indices`. - Set **Data port indices** to use this value for the last data port. - Set **Data port for default case** to `Last data port`. | This block configuration handles invalid values that the enumerated type explicitly represents. |
| The enumerated type contains only valid enumerated values. However, a data input port can get invalid values of enumerated type. | - Set **Data port for default case** to `Additional data port`. | This block configuration handles invalid values that the enumerated type does not explicitly represent. |
| The enumerated type contains only valid enumerated values. Data input ports can never get invalid values of enumerated type. | - Set **Data port for default case** to `Last data port`. - Set **Diagnostic for default case** to `None`. | This block configuration avoids unnecessary diagnostic action. |
| The block does not have a data input port for every value of the enumerated type. | - Set **Data port for default case** to `Additional data port`. | This block configuration handles enumerated values that do not have a data input port, along with invalid values. |

## Ports

### Input

### **Port\_1** — Control signal scalar

The control signal can be of any data type that Simulink® supports, including fixed-point and enumerated types. When
the control input is not an integer value, the block truncates the value
to an integer by rounding to zero.

For information on control signals of enumerated type, see Guidelines on Setting Parameters for Enumerated Control Port.

For information on how the block handles the out-of-range condition,
see How the Block Handles an Out-of-Range Control Input.

#### Limitations

- If the control signal is numeric, the control signal
  cannot be complex.
- If the control signal is an enumerated signal, the block
  uses the value of the underlying integer to select a data
  port.
- If the underlying integer does not correspond to a data
  port, an error occurs.
- If the control input is a floating point value that
  exceeds the datatype range of integers, the Multiport
  Switch block issues a runtime error. This range
  includes `Inf` and
  `NaN`.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `image`

### **1** — First data input scalar | vector | matrix | N-D array

First data input, specified as a scalar, vector, matrix, or N-D array.
All input data signals can be of any data type that Simulink supports.

- If all the data inputs are scalar, the output is scalar
- If at least one of the data inputs is a vector, the block
  output is a vector. In this case, the block expands any scalar
  inputs to vectors.
- If any two nonscalar signals have a different number of
  dimensions or different dimension lengths, select the
  **Allow different data input sizes** check
  box. For more information, see Use Data Inputs That Have Different Dimensions
- If any data signal is of an enumerated type, all others must
  be of the same enumerated type.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `string` | `image`

### **2** — Second data input scalar | vector | matrix | N-D array

Second data input, specified as a scalar, vector, matrix, or N-D
array. All input data signals can be of any data type that Simulink supports.

- If all the data inputs are scalar, the output is scalar
- If at least one of the data inputs is a vector, the block
  output is a vector. In this case, the block expands any scalar
  inputs to vectors.
- If any two nonscalar signals have a different number of
  dimensions or different dimension lengths, select the
  **Allow different data input sizes** check
  box. For more information, see Use Data Inputs That Have Different Dimensions
- If any data signal is of an enumerated type, all others must
  be of the same enumerated type.

#### Dependencies

To enable this port, set **Number of data ports**
to an integer greater than 1.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `string` | `image`

### **N** — Nth data input scalar | vector | matrix | N-D array

Nth data input, specified as a scalar, vector, matrix, or N-D array.
All input data signals can be of any data type that Simulink supports.

- If all the data inputs are scalar, the output is scalar
- If at least one of the data inputs is a vector, the block
  output is a vector. In this case, the block expands any scalar
  inputs to vectors.
- If any two nonscalar signals have a different number of
  dimensions or different dimension lengths, select the
  **Allow different data input sizes** check
  box. For more information, see Use Data Inputs That Have Different Dimensions
- If any data signal is of an enumerated type, all others must
  be of the same enumerated type.

#### Dependencies

To enable the *N*th input port, set **Number of data
ports** to an integer value greater than or equal to
*N*.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `string` | `image`

### **\*** — Data port for out-of-range inputs scalar | vector | matrix | N-D array

Input data port for out-of-range control signal inputs, specified as a
scalar, vector, matrix, or N-D array. All input data signals can be of
any data type that Simulink supports. If any data signal is of an enumerated type, all
others must be of the same enumerated type. If any two signals have a
different number of dimensions or different dimension lengths, select
the **Allow different data input sizes** check box. For
more information, see Use Data Inputs That Have Different Dimensions.

#### Dependencies

To create an additional data port for out-of-range control signal
inputs, set **Data port for default case** to
`Additional data port`. When you set
**Data port for default case** to
`Last data port`, the block uses the
last data port for output when the control signal value does not
match any data port indices.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### Output

### **Port\_1** — Selected data input, based on control signal value scalar | vector | matrix | N-D array

The block outputs one of the data inputs, selected according to the control signal
value. The output has the same dimensions as the corresponding data
input. The output data type is the data type of the input port that
requires the largest memory space. When you select the **Allow
different data input sizes** check box, the output of the
block is a variable size signal.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `enumerated` | `string` | `image`

## Parameters

### Main

### **Data port order** — Type of ordering for data input ports `One-based contiguous` | `Zero-based contiguous` | `Specify indices`

Specify the type of ordering for your data input ports.

- `Zero-based contiguous` — Block uses
  zero-based indexing for ordering contiguous data ports. This is
  the default value of the Index Vector
  block.
- `One-based contiguous` — Block uses
  one-based indexing for ordering contiguous data ports. This is
  the default value of the Multiport Switch
  block
- `Specify indices` — Block uses
  noncontiguous indexing for ordering data ports.

#### Tips

- When the control port is of enumerated type, select
  `Specify indices`.
- If you select `Zero-based
  contiguous` or `One-based
  contiguous`, verify that the control port
  is not of enumerated type. This configuration is deprecated
  and produces an error. You can run the Upgrade Advisor on
  your model to replace each Multiport Switch
  block of this configuration with a block that explicitly
  specifies data port indices. See Model Upgrades.
- Avoid situations where the block contains unused data
  ports for simulation or code generation. When the control
  port is of fixed-point or built-in data type, verify that
  all data port indices are representable with that type.
  Otherwise, the following block behavior occurs.

  | If the Block Has Unused Data Ports and Data Port Order Is: | The Block Produces: |
  | --- | --- |
  | `Zero-based contiguous` or `One-based contiguous` | A warning |
  | `Specify indices` | An error |

#### Dependencies

Selecting `Zero-based contiguous` or
`One-based contiguous` enables the
**Number of data ports** parameter.

Selecting `Specify indices` enables the
**Data port indices** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataPortOrder` |
| **Type:** character vector |
| **Values:** `'Zero-based contiguous' | 'One-based contiguous' | 'Specify indices'` |
| **Default:** `'One-based contiguous'` (Multiport Switch) | `'Zero-based contiguous'` (Index Vector) |

### **Number of data ports** — Number of data input ports `1` | `3` | integer between 1 and 65535

Specify the number of data input ports to the block. The total number of input ports is
the number you specify, plus one for the control signal input port, and
plus one more if you set **Data port for default case**
to `Additional data port`.

#### Dependencies

To enable this parameter, set **Data port order**
to `Zero-based contiguous` or
`One-based contiguous`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Inputs` |
| **Type:** character vector |
| **Values:** integer between 1 and 65536 |
| **Default:** `'3'` (Multiport Switch) | `'1'` (Index Vector) |

### **Data port indices** — Array of indices for data ports `{1,2,3}` (default) | array of indices

Specify an array of indices for your data ports. The block icon
changes to match the data port indices you specify.

#### Tips

- To specify an array of indices that correspond to all
  values of an enumerated type, enter
  `enumeration('name of the
  type')`.

  For example, `enumeration('MyColors')` is
  a valid entry if `MyColors` is the name of
  an enumerated type.
- To enter specific values of an enumerated type, use the
  *`type_name.enumerated_name`*
  format. Do not enter the underlying integer value.

  For example, `enumeration({MyColors.Red, MyColors.Green,
  MyColors.Blue})` is a valid entry.
- To indicate that more than one value maps to a data port,
  use brackets.

  For example, the following entries are both valid:

  - `enumeration({MyColors.Red,
    MyColors.Green, [MyColors.Blue,
    MyColors.Yellow]})`
  - `enumeration({[3,5],0,18})`
- If the control port is of fixed-point or built-in data
  type, the values for **Data port indices**
  must be representable with that type. Otherwise, an error
  appears at compile time to alert you to unused data
  ports.
- If the control port is of enumerated data type, the values
  for **Data port indices** must be
  enumerated values of that type.
- If **Data port indices** contains values
  of enumerated type, the control port must be of that data
  type.

#### Dependencies

To enable this parameter, set **Data port order**
to `Specify indices`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataPortIndices` |
| **Type:** character vector |
| **Values:** array of indices |
| **Default:** `'{1,2,3}'` |

### **Data port for default case** — Port to use for out-of-range inputs `Last data port` (default) | `Additional data port`

Specify whether to use the last data port for out-of-range inputs, or to use an
additional port. An asterisk (\*) next to the port name indicates the
port the block uses when the control port value does not match any data
port indices.

- `Last data port` — Block uses the
  last data port for output when the control port value does not
  match any data port indices.
- `Additional data port` — Block uses
  an additional data port for output when the control port value
  does not match any data port indices.

#### Tip

If you set this parameter to `Additional data
port` and **Number of data ports**
is `3`, the number of input ports on the
block is 5. The first input is the control port, the next three
inputs are data ports, and the fifth input is the default port for
out-of-range inputs.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataPortForDefault` |
| **Type:** character vector |
| **Values:** `'Last data port' | 'Additional data port'` |
| **Default:** `'Last data port'` |

### **Diagnostic for default case** — Diagnostic action when control port value does not match data port indices `Error` (default) | `Warning` | `None`

Specify the diagnostic action to take when the control port value does not match any
data port indices.

- `None` — Produce no response.
- `Warning` — Display a warning and
  continue the simulation.
- `Error` — Terminate the simulation
  and display an error. In this case, the **Data port for
  default case** is used only for code generation and
  not simulation.

For more information, see How the Block Handles an Out-of-Range Control Input.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DiagnosticForDefault` |
| **Type:** character vector |
| **Values:** `'None' | 'Warning' | 'Error'` |
| **Default:** `'Error'` |

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

### Signal Attributes

### **Require all data port inputs to have the same data type** — Require all inputs to have the same data type `off` (default) | `on`

Select this check box to require that all data input ports have the same data
type. When you clear this check box, the block allows data port inputs to have
different data types.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputSameDT` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

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

### **Output data type** — Specify the output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Inherit via back propagation` | `Inherit: Same as first data input` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `string` | `Simulink.ImageType(480,640,3)` | `<data type expression>`

Choose the data type for the output. The type can be inherited, specified
directly, or expressed as a data type object such as
`Simulink.NumericType`.

When you select an inherited option, the block behaves as follows:

- `Inherit: Inherit via internal
  rule`—Simulink chooses a data type to balance numerical accuracy,
  performance, and generated code size, while taking into account the
  properties of the embedded target hardware. If you change the embedded
  target settings, the data type selected by the internal rule might
  change. It is not always possible for the software to optimize code
  efficiency and numerical accuracy at the same time. If the internal rule
  doesn’t meet your specific needs for numerical accuracy or performance,
  use one of the following options:

  - Specify the output data type explicitly.
  - Explicitly specify a default data type such as
    `fixdt(1,32,16)` and then use the
    Fixed-Point Tool to propose data types for your model. For more
    information, see `fxptdlg` (Fixed-Point Designer).
  - To specify your own inheritance rule, use
    `Inherit: Inherit via back
    propagation` and then use a Data Type
    Propagation block. Examples of how to use this block
    are available in the Signal Attributes library Data Type
    Propagation Examples block.
- `Inherit: Inherit via back propagation` —
  Uses the data type of the driving block.
- `Inherit: Same as first data input` — Uses
  the data type of the first data input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via internal rule` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'string'` | `Simulink.ImageType(480,640,3)` | `'<data type expression>'` |
| **Default**: `'Inherit: Inherit via internal rule'` |

### **Lock output data type setting against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select to lock the output data type setting of this block against changes
by the Fixed-Point Tool and the Fixed-Point Advisor. For more
information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LockScale` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

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

### **Allow different data input sizes (Results in variable-size output signal)** — Allow input signals with different sizes `off` (default) | `on`

Select this check box to allow input signals with different sizes.

- `On` — Allows input signals with different sizes, and
  propagate the input signal size to the output signal. In this mode, the
  block produces a variable-size output signal.
- `Off` — Requires that all nonscalar data input signals be
  the same size.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `AllowDiffInputSizes` |
| **Type:** character vector |
| **Value:** `'on'` | `'off'` |
| **Default:** `'off'` |

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

### **Signedness** — Specify signed or unsigned `Signed` (default) | `Unsigned`

Specify whether the fixed-point data is signed or unsigned. Signed data can represent
positive and negative values, but unsigned data represents positive values only.

- `Signed`, specifies the fixed-point data as
  signed.
- `Unsigned`, specifies the fixed-point data as
  unsigned.

For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, set the **Mode** to `Fixed
point`.

### **Scaling** — Method for scaling fixed-point data `Best precision` (default) | `Binary point` | `Slope and bias`

Specify the method for scaling your fixed-point data to avoid overflow
conditions and minimize quantization errors. For more information, see
Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Word length** — Bit size of the word that holds the quantized integer `16` (default) | integer from 0 to 32

Specify the bit size of the word that holds the quantized integer. For
more information, see Specifying a Fixed-Point Data Type.

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

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

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
| **CodingStyle** | Specify whether to generate HDL code with case statements or if-else statements. By default, HDL Coder generates if-else statements. See also CodingStyle (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

| Native Floating Point | |
| --- | --- |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `inherit`, `Max`, `Min`, or `Zero` for the floating-point operator. The default is `inherit`. See also LatencyStrategy (HDL Coder). |

**Complex Data Support**

This block supports code generation for complex signals.

**Setting Data Port Indices Using Specify Indices mode**

You can specify the data port indices to the input port using specify indices
mode. To configure the Multiport Switch block with specify indices mode, set the
**Data port order** block parameter to `Specify
indices`. Then, enter the port indices in the **Data
port indices** block parameter. For a model targeted for HDL code
generation, you can use these input data types for the control input in a
specify indices mode:

- Fixed-point and floating-point types
- Signed and unsigned integer types
- Enumerated types
- Vector, matrix, and bus types

**Using an Enumerated Type as Port Index**

You can set **Data port order** to **Specify
indices**, and enter enumeration values for the **Data
port indices**. For example, you can connect the Enumerated
Constant block to the Multiport Switch control
port and use the enumerated types as data port indices.

**Restrictions**

You must avoid using of `NaN` or out of range values at the
control port. It can cause simulation mismatch in the validation model.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2024a: Multiport Switch block has runtime error when input has floating point value

The Multiport Switch block now issues a runtime error when the
control signal in the first port has a floating point value that exceeds the
datatype range of integers. This range includes `Inf` and
`NaN`.
