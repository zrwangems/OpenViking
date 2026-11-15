---
type: simulink-block
title: 'Trigonometric Function'
family: math-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'trigonometricfunction'
---

# Trigonometric Function

Specified trigonometric function on input

## 中文

指定应用于输入信号的三角函数

### 所属库

Simulink / Math Operations HDL Coder / Math Operations HDL Coder / HDL Floating Point Operations

### 描述

Trigonometric Function 模块执行常见的三角函数，并以 rad 或 rev 为单位输出结果。

#### 支持的函数

可以从**函数**下拉列表中选择以下函数之一。

| 函数 | 描述 | 数学表达式 | MATLAB® 等效函数 |
| --- | --- | --- | --- |
| `sin` | 输入信号的正弦 | `sin(u)` | `sin` |
| `cos` | 输入信号的余弦 | `cos(u)` | `cos` |
| `tan` | 输入信号的正切 | `tan(u)` | `tan` |
| `asin` | 输入信号的反正弦 | `asin(u)` | `asin` |
| `acos` | 输入信号的反余弦 | `acos(u)` | `acos` |
| `atan` | 输入信号的反正切 | `atan(u)` | `atan` |
| `atan2` | 输入信号的四象限反正切 | `atan2(u)` | `atan2` |
| `sinh` | 输入信号的双曲正弦 | `sinh(u)` | `sinh` |
| `cosh` | 输入信号的双曲余弦 | `cosh(u)` | `cosh` |
| `tanh` | 输入信号的双曲正切 | `tanh(u)` | `tanh` |
| `asinh` | 输入信号的反双曲正弦 | `asinh(u)` | `asinh` |
| `acosh` | 输入信号的反双曲余弦 | `acosh(u)` | `acosh` |
| `atanh` | 输入信号的反双曲正切 | `atanh(u)` | `atanh` |
| `sincos` | 输入信号的正弦；输入信号的余弦 | — | — |
| `cos + jsin` | 输入信号的复指数 | — | — |

#### CORDIC 逼近方法

CORDIC 是 COordinate Rotation DIgital Computer（坐标旋转数字计算方法）的缩写。基于吉文斯旋转的 CORDIC 算法是最节省硬件资源的可用算法之一，因为它只需进行迭代移位相加运算。有关详细信息，请参阅详细信息。模块输入有进一步的要求。

有关何时将**函数**设置为 `sin`、`cos`、`sincos` 或 `cos + jsin`，并将**逼近方法**设置为 **CORDIC** 的详细信息，请参阅 Port\_1。

下表概述了输入无效时发生的情况。

| 模块用法 | 无效输入的影响 |
| --- | --- |
| 仿真模式 | 出现错误。 |
| 生成的代码 | 发生未定义的行为。对于生成的代码，避免依赖未定义的行为。 |

#### 查找逼近方法

有关何时将**函数**设置为 `sin`、`cos`、`sincos` 或 `cos + jsin`，并将**逼近方法**设置为**查找**的详细信息，请参阅 Port\_1。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

指定为标量、向量或矩阵的输入。此模块接受以下数据类型的输入信号：

| 函数 | 输入数据类型 |
| --- | --- |
| - `sin` - `cos` - `sincos` - `cos + jsin` - `atan2` | - 浮点 - 定点（仅当**逼近方法**为 **CORDIC** 或**查找**时） |
| - `tan` - `asin` - `acos` - `atan` - `sinh` - `cosh` - `tanh` - `asinh` - `acosh` - `atanh` | - 浮点 |

CORDIC 逼近定点类型传播：

| 输入数据类型 | 函数 | 输出数据类型 |
| --- | --- | --- |
| 定点，有符号或无符号 | `sin`、`cos`、`sincos` 和 `cos + jsin` | `fixdt``(1, WL, WL - 2)`，其中 *`WL`* 是输入的字长  此定点类型为 CORDIC 算法提供最佳精度。 |
| 定点，有符号 | `atan2` | `fixdt``(1, WL, WL – 3)` |
| 定点，无符号 | `atan2` | `fixdt``(1, WL, WL – 2)` |

查找逼近定点类型传播：

| 输入数据类型 | 函数 | 输出数据类型 |
| --- | --- | --- |
| 定点，有符号 | `sin`, `cos`, `sincos`, `cos + jsin`, `atan2` | `fixdt``(1, WL, FL)` |
| 定点，无符号 | `sin`, `cos`, `sincos`, `cos + jsin`, `atan2` | `fixdt``(1, WL - 1, FL)` |

##### 依赖关系

- 当您将**函数**设置为 `atan2` 时，模块显示两个输入端口。第一个输入 (**Port\_1**) 是函数参量的 *y* 轴坐标，即虚部。第二个输入 (**Port\_2**) 是函数参量的 *x* 轴坐标，即实部。
- 如果您将**逼近方法**设置为**无**、**CORDIC** 或**查找**，则可以使用浮点输入信号。但是，模块输出的数据类型取决于您选择的逼近方法选项。

  | 输入数据类型 | 逼近方法 | 输出数据类型 |
  | --- | --- | --- |
  | 浮点 | **无** | 取决于您选择的**输出信号类型**。选项为 `auto`（与输入的数据类型相同）、`real` 或 `complex`。 |
  | 浮点 | **CORDIC** | 与输入相同。当您使用 CORDIC 逼近方法计算模块输出时，**输出信号类型**不可用。 |
  | 浮点 | **查找** | 与输入相同。当您使用 Lookup 逼近方法计算模块输出时，**输出信号类型**不可用。 |

对于 CORDIC 和查找逼近：

- `sin`、`cos`、`sincos`、`cos + jsin` 和 `atan2` 函数的输入必须是实数。
- `sin`、`cos`、`sincos` 和 `atan2` 函数的输出为实数。
- `cos + jsin` 函数的输出为复数。

有关详细信息，请参阅限制。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **Port\_2** — `atan2` 的函数参量的 *x* 轴坐标，即实部 标量 | 向量 | 矩阵

输入 `atan2` 的函数参量的 *x* 轴坐标，即实部。当您将**函数**设置为 `atan2` 时，模块显示两个输入端口。第一个输入 (**Port\_1**) 是函数参量的 *y* 轴坐标，即虚部。第二个输入 (**Port\_2**) 是函数参量的 *x* 轴坐标，即实部。（有关各种模块方向的端口顺序的描述，请参阅标识旋转或翻转模块上的端口位置。）

仅当**逼近**方法设置为 **CORDIC** 或**查找**时才支持定点输入信号。

##### 依赖关系

要启用此端口，请将**函数**设置为 **atan2**。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
#### 输出

#### **Port\_1** — 指定输入信号的三角函数 标量 | 向量 | 矩阵

将指定的三角函数应用于一个或多个输入（以 rad 为单位）的结果。每个函数支持：

- 标量运算
- 按元素的向量和矩阵运算

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **sin** — 输入信号的正弦 标量 | 向量 | 矩阵

输入信号的正弦，以 rad 和 rev 为单位。

##### 依赖关系

要启用此端口，请将**函数**设置为 **sincos**。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **cos** — 输入信号的余弦 标量 | 向量 | 矩阵

输入信号的余弦，以 rad 和 rev 为单位。

##### 依赖关系

要启用此端口，请将**函数**设置为 **sincos**。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 参数

#### 算法

#### **函数** — 三角函数 **sin** (默认) | **cos** | **tan** | **asin** | **acos** | **atan** | **atan2** | **sinh** | **cosh** | **Tanh** | **asinh** | **acosh** | **atanh** | **sincos** | **cos + jsin**

指定三角函数。模块图标上的函数名称发生变化以反映您的选择。

有关何时将**函数**设置为 `sin`、`cos`、`sincos` 或 `cos + jsin`，并将**逼近方法**设置为 **CORDIC** 的详细信息，请参阅 限制。

##### 编程用法

|  |
| --- |
| **模块参数**：`Operator` |
| **类型：**字符向量 |
| **值：**`'sin' | 'cos' | 'tan' | 'asin' | 'acos' | 'atan' | 'atan2' | 'sinh' | 'cosh' | 'tanh' | 'asinh' | 'acosh' | 'atanh' | 'sincos' | 'cos + jsin'` |
| **默认值：**`'sin'` |

#### **逼近方法** — CORDIC、查找或无 **无** (默认) | **CORDIC** | **查找**

指定计算输出的逼近方法类型。

| 逼近方法 | 支持的数据类型 | 何时使用此方法 |
| --- | --- | --- |
| **无**（默认值） | 浮点 | 您想使用默认的泰勒级数算法。 |
| **CORDIC** | 浮点和定点 | 您需要快速的近似迭代计算。 |
| **查找** | 浮点（双精度和单精度）和定点，其**偏置**值为 `0`，**斜率**值为 2 的幂 | 您需要快速的近似查找表实现。 |

有关何时将**函数**设置为 `sin`、`cos`、`sincos` 或 `cos + jsin`，并将**逼近方法**设置为 **CORDIC** 的详细信息，请参阅 限制。

##### 依赖关系

- 要启用此参数，请将**函数**设置为 **sin**、**cos**、**sincos**、**cos + jsin** 或 `atan2`。
- 要使用定点输入信号，必须将**逼近方法**设置为 **CORDIC** 或**查找**。
- 要启用**表数据类型**参数，请将此方法设置为**查找**。

##### 编程用法

|  |
| --- |
| **模块参数**：`ApproximationMethod` |
| **类型：**字符向量 |
| **值：**`'None' | 'CORDIC' | 'Lookup'` |
| **默认值：**`'None'` |

#### **插值方法** — 断点值之间插值的方法 **线性点-斜率** (默认) | **均一**

当输入位于两个断点值之间时，模块将根据相邻断点内插输出值。有关插值方法的详细信息，请参阅内插方法。

##### 编程用法

|  |
| --- |
| **模块参数**：`InterpMethod` |
| **类型：**字符向量 |
| **值：**`'Linear point-slope' | 'Flat'` |
| **默认值：**`'Linear point-slope'` |

#### **迭代次数** — CORDIC 算法的迭代次数 `11` (默认) | 正整数，小于或等于定点输入的字长

指定要执行 CORDIC 算法的迭代次数。默认值为 11。

- 当模块输入使用浮点数据类型时，迭代次数可以是正整数。
- 当模块输入是定点数据类型时，迭代次数不能超过字长。

  例如，如果模块输入是 `fixdt(1,16,15)`，字长为 16。在这种情况下，迭代次数不能超过 16。

##### 依赖关系

要启用此参数，必须按如下所示设置**函数**和**逼近方法**参数：

- 将**函数**设置为 **sin**、**cos**、**sincos**、**cos + jsin** 或 `atan2`。
- 将**逼近方法**设置为 **CORDIC**。

##### 编程用法

|  |
| --- |
| **模块参数**：`NumberOfIterations` |
| **类型：**字符向量 |
| **值：**正整数，小于等于定点输入的字长 |
| **默认值：**`'11'` |

#### **角度单位** — 角度单位 **radian** (默认) | **revolution**

将查找方法的角度单位指定为 **radian** 或 **revolution**。

##### 依赖关系

要启用此参数，请进行如下设置：

- 将**函数**设置为 **sin**、**cos**、**sincos**、**cos + jsin** 或 `atan2`。
- 将**逼近方法**设置为**查找**。

##### 编程用法

|  |
| --- |
| **模块参数**：`AngleUnit` |
| **类型：**字符向量 |
| **值：**`'radian' | 'revolution'` |
| **默认值：**`'radian'` |

#### **数据点数** — 查找表的数据点数 `16` (默认) | 标量

将查找表的数据点数指定为标量实数。

##### 依赖关系

要启用此参数，请进行如下设置：

- 将**函数**设置为 **sin**、**cos**、**sincos**、**cos + jsin** 或 `atan2`。
- 将**逼近方法**设置为**查找**。

##### 编程用法

|  |
| --- |
| **模块参数**：`NumberOfDataPoints` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'16'` |

#### **输出信号类型** — 输出信号的复/实性 **自动** (默认) | **实数** | **复**

将 Trigonometric Function 模块输出信号类型指定为 `auto`、`real` 或 `complex`。

| 函数 | 输入信号类型 | 输出信号类型 | | |
| --- | --- | --- | --- | --- |
| 自动 | 实数 | 复数 |
| 任意**函数**参数选择项 | 实数 | 实数 | 实数 | 复数 |
| 复数 | 复数 | 错误 | 复数 |

##### 依赖关系

将**逼近方法**设置为 **CORDIC** 将禁用此参数。

**注意**

当**函数**为 `atan2` 时，仿真或代码生成不支持复输入信号。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutputSignalType` |
| **类型：**字符向量 |
| **值：**`'auto' | 'real' | 'complex'` |
| **默认值：**`'auto'` |

#### **删除防止超范围输入的代码** — 删除防止超范围输入的代码 off (默认) | on

对于 **acos** 和 **asin**，选中此复选框将不会防范超出范围的输入，从而减少冗余。

- 如果清除此复选框，则会启用防范。在执行任何操作之前，模块会将超出范围的输入饱和处理为 `1` 或 `-1`。生成的代码包含用于检查超出范围输入的代码。
- 如果选中此复选框，则会取消防范。模块将对输入值执行所有运算而不进行任何更改。生成的代码不包含用于检查超出范围输入的代码。

如果输入已在范围内，启用此复选框可以消除冗余。

##### 依赖关系

将**函数**设置为 **acos** 和 **asin** 会启用此参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`RemoveProtectionAgainstOutOfRangeInput` |
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

#### 数据类型

#### **表数据类型** — 表的数据类型 **继承: 从输入继承** (默认) | **double** | **single** | **fixdt(1,16,0)** | **<数据类型表达式>**

查找表的数据类型，指定为：

- **继承: 从输入继承**
- **double**
- **single**
- **fixdt(1,16,0)**
- **<数据类型表达式>**

有关设置数据类型的详细信息，请参阅控制信号的数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`TableDataTypeStr` |
| **类型：**字符串标量或字符向量 |
| **值：** `Inherit: Inherit via input` | `single` | `double` | `fixdt(1,16,0)` | 数据类型表达式 |
| **默认值：**`Inherit: Inherit via input` |

#### **模式** — 要指定的数据的类别 **继承** (默认) | **内置** | **定点** | **表达式**

选择您要如何指定**输出**数据类型的数据类型属性。您可以选择：

- **继承** - 用于指定继承数据类型的规则，例如**继承: 从内部规则继承**
- **内置** - 用于指定内置数据类型。
- **定点** - 用于指定数据类型的定点属性。
- **表达式** - 用于指定计算结果为有效数据类型的表达式，例如 `fixdt([],16,0)`

##### 依赖关系

要启用此参数，请在**输出数据类型**参数处点击 **>>**。

#### **符号性** — 指定有符号或无符号 `Signed` (默认) | `Unsigned`

为**输出**数据类型指定**符号性**。

##### 依赖关系

要启用此参数，请将**模式**设置为**定点**。

#### **定标** — 定标定点数据的方法 **二进制小数点** (默认)

为**输出**数据类型指定**定标**。

##### 依赖关系

要启用此参数，请将**模式**设置为**定点**。

#### **数据类型覆盖** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

为此信号选择数据类型覆盖模式。

- **继承** - 继承为模型指定的数据类型覆盖设置。
- **关闭** - 忽略为模型指定的数据类型覆盖设置，并使用您指定的定点数据类型

有关详细信息，请参阅 Simulink® 文档中的使用数据类型助手指定数据类型。

##### 提示

由于能够关闭单个数据类型的数据类型覆盖，您可以在应用数据类型覆盖时更好地控制模型中的数据类型。例如，您可以使用此选项确保数据类型满足下游模块的要求，而忽略数据类型覆盖设置。

##### 依赖关系

要启用此参数，请点击**显示数据类型助手**按钮，并将**模式**设置为**内置**或**定点**。

#### **字长** — 存储量化整数的字的位大小 `16` (默认) | 从 0 到 32 的整数

指定存储量化整数的字的位大小。有关详细信息，请参阅指定定点数据类型。

##### 依赖关系

要启用此参数，请将**模式**设置为**定点**。

#### **小数长度** — 指定定点数据类型的小数长度 `0` (默认) | 整数标量

将定点数据类型的小数长度指定为正整数或负整数。有关详细信息，请参阅指定定点数据类型。

##### 依赖关系

要启用此参数，请进行如下设置：

- 将**模式**设置为**定点**
- 将**定标**设置为**二进制小数点**

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed pointa` | `half` | `integera` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |
|  |  |
| --- | --- |
| a 当采用 CORDIC 逼近方法时，此模块支持定点和基整数数据类型。 | |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

并非所有编译器都支持 `asinh`、`acosh` 和 `atanh` 函数。如果您使用不支持这些函数的编译器，将会出现警告，且生成的代码无法链接。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

要从使用定点数据的模块中生成 HDL 代码，请将**架构**设置为 `Cordic` 或 `LUT`。下表显示模块支持这些设置的函数：

| 模块参数 | HDL 模块属性 | 支持的函数 |
| --- | --- | --- |
| 将**逼近方法**设置为 **CORDIC**，将**数据点数**设置为任何标量实数。 | 将**架构**设置为 **Cordic**。 | - **sin** - **cos** - **sincos** - **cos+jsin** - **atan2** |
| 将**逼近方法**设置为**查找**，将**插值方法**设置为**均一**，将**角度单位**设置为**转**，将**数据点数**设置为任何标量实数。 | 将**架构**设置为 **LUT**。 | - **sin** - **cos** - **sincos** - **cos+jsin** |

要为使用浮点数据的模块的所有函数生成 HDL 代码，请将**逼近方法**模块参数设置为**无**，并将**输出信号类型**参数设置为**自动**或**实数**或**复数**。此外，将 HDL 模块属性中的**架构**参数设置为**三角函数**。

此模块具有多周期实现，这会在生成的代码中引入额外的延迟。要查看增加的延迟，请查看生成的模型或验证模型。请参阅Generated Model and Validation Model (HDL Coder)。

延迟计算取决于字长和 **LatencyStrategy** 设置。要查看定点数据类型的延迟计算，请参阅：

- Sin (HDL Coder)
- Cos (HDL Coder)
- Cos+jSin (HDL Coder)
- SinCos (HDL Coder)
- Atan2 (HDL Coder)

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |
| **LatencyStrategy** | 要为定点类型启用此属性，请将**函数**设置为 `sin`、`cos`、`sincos`、`cos+jsin`，或 `atan2` 并将**逼近方法**设置为 `CORDIC`。对于定点和浮点类型，指定是将设计中的模块映射到 `MAX`、`Min`、`CUSTOM` 还是 `ZERO` 延迟。默认值为 **MAX**。另请参阅LatencyStrategy (HDL Coder)。 |
| **CustomLatency** | 要为定点类型启用此属性，请将**函数**设置为 `sin`、`cos`、`sincos`、`cos+jsin`，或 `atan2` 并将**逼近方法**设置为 `CORDIC`。当 **LatencyStrategy** 设置为 `CUSTOM` 时，使用此属性为定点类型指定介于 `ZERO` 和 `MAX` 之间的自定义延迟值。另请参阅LatencyStrategy (HDL Coder)。 |
| **IterationsPerPipeline** | 要为定点类型启用此属性，请将**函数**设置为 `sin`、`cos`、`sincos`、`cos+jsin`，或 `atan2` 并将**逼近方法**设置为 `CORDIC`。  当 **LatencyStrategy** 设置为 `Custom(PerIterations)` 时，使用此设置指定每个流水线阶段的迭代次数。有关详细信息，请参阅Atan2 (HDL Coder)。 |

| 原生浮点 | |
| --- | --- |
| **InputRangeReduction** | 将此属性用于 `sin`、`cos`、`sincos`、`cos+jsin` 和 `atan2` 函数。如果您的输入范围是无界的，请为 HDL Coder 启用此属性，以插入额外的逻辑来缩小 `[-pi, pi]` 的输入范围。另请参阅InputRangeReduction (HDL Coder)。 |
| **HandleDenormals** | 指定是否希望 HDL Coder 在设计中插入额外的逻辑来处理非正规数字。非正规数是大小非常小、必须使用包含前导零的尾数才能表示的浮点数。默认值为 **inherit**。另请参阅HandleDenormals (HDL Coder)。 |
| **LatencyStrategy** | 指定对于浮点运算符是否将设计中的模块映射到 `inherit`、`Max`、`Min` 或 `Zero`。默认值为 **inherit**。另请参阅LatencyStrategy (HDL Coder)。 |
| **MultiplyStrategy** | 将此属性用于 `sin`、`cos`、`sincos`、`cos+jsin` 和 `atan2` 函数。默认值为 `inherit`。指定您要使用 `FullMultiplier` 还是 `PartMultiplierPartAddShift`。另请参阅MantissaMultiplyStrategy (HDL Coder)。 |

**ULP 注意事项**

对于浮点运算，Trigonometric Function 模块的最后一位非零单位 (ULP) 误差。有关详细信息，请参阅ULP Considerations of Native Floating-Point Operators (HDL Coder)。

**限制**

- 对于 **sin** 和 **cos** 函数，该模块仅支持将有符号定点数据类型用于 CORDIC 逼近。
- 对于具有 CORDIC 模式的函数，如 **sin**、**cos**、**sincos**、**atan2** 和 **cos+jsin**，HDL 代码生成不支持大于 `127` 位的定点数据类型。
- HDL 代码生成不支持对三角函数使用双精度数据类型，但 **sin** 和 **cos** 函数除外。
- 在以下情况下，HDL 代码生成不支持查找逼近方法：

  - **插值方法**参数设置为**线性点-斜率**，**角度单位**参数设置为**弧度**或**旋转**。
  - **插值方法**参数为**均一**，**角度单位**参数为**弧度**。
- 当 Trigonometric Function 模块位于反馈环中且采用以下设置时，HDL Coder 会显示错误：

  - 将**架构**设置为 `Cordic`
  - 将 **UsePipelinedKernel** 设置为 `On`

  出现错误是因为该模块处于反馈环中，并且代码生成器无法插入额外的延迟。为避免此错误，请在模块附近添加长度等于**迭代次数** + 3 的延迟。然后，代码生成器吸收该延迟以满足 Trigonometric Function 模块的额外延迟。

  例如，此 Trigonometric Function 模块将**迭代次数**设置为 `30`。添加与该模块相邻的长度为 `33` 的 Delay 模块满足额外的延迟。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

当**函数**设置为 **sin**、**cos**、**sincos**、**cos + jsin** 或 `atan2` 且**逼近方法**设置为 **CORDIC** 时，此模块支持定点和基整数数据类型。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Math Operations HDL Coder / Math Operations HDL Coder / HDL Floating Point Operations

## Description

The Trigonometric Function block performs common trigonometric
functions and outputs the result in rad or rev.

### Supported Functions

You can select one of these functions from the **Function**
parameter list.

| Function | Description | Mathematical Expression | MATLAB® Equivalent |
| --- | --- | --- | --- |
| `sin` | Sine of the input | `sin(u)` | `sin` |
| `cos` | Cosine of the input | `cos(u)` | `cos` |
| `tan` | Tangent of the input | `tan(u)` | `tan` |
| `asin` | Inverse sine of the input | `asin(u)` | `asin` |
| `acos` | Inverse cosine of the input | `acos(u)` | `acos` |
| `atan` | Inverse tangent of the input | `atan(u)` | `atan` |
| `atan2` | Four-quadrant inverse tangent of the input | `atan2(u)` | `atan2` |
| `sinh` | Hyperbolic sine of the input | `sinh(u)` | `sinh` |
| `cosh` | Hyperbolic cosine of the input | `cosh(u)` | `cosh` |
| `tanh` | Hyperbolic tangent of the input | `tanh(u)` | `tanh` |
| `asinh` | Inverse hyperbolic sine of the input | `asinh(u)` | `asinh` |
| `acosh` | Inverse hyperbolic cosine of the input | `acosh(u)` | `acosh` |
| `atanh` | Inverse hyperbolic tangent of the input | `atanh(u)` | `atanh` |
| `sincos` | Sine of the input; cosine of the input | — | — |
| `cos + jsin` | Complex exponential of the input | — | — |

### CORDIC Approximation Method

CORDIC is an acronym for COordinate Rotation DIgital Computer. The Givens
rotation-based CORDIC algorithm is one of the most hardware-efficient algorithms
available because it requires only iterative shift-add operations. For more
information, see More About. The block input has further
requirements.

For more information on when you set **Function** to
`sin`, `cos`, `sincos`, or
`cos + jsin` and set the **Approximation
method** to `CORDIC`, see Port\_1.

This table summarizes what happens for an invalid input.

| Block Usage | Effect of Invalid Input |
| --- | --- |
| Simulation modes | An error appears. |
| Generated code | Undefined behavior occurs. Avoid relying on undefined behavior for generated code. |

### Lookup Approximation Method

For more information on when you set **Function**  to
`sin`, `cos`, `sincos`,
or `cos + jsin` and set the **Approximation method** to `Lookup`, see Port\_1.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input specified as a scalar, vector, or matrix. The block accepts
input signals of the following data types:

| Functions | Input Data Types |
| --- | --- |
| - `sin` - `cos` - `sincos` - `cos + jsin` - `atan2` | - Floating point - Fixed point (only when   **Approximation method** is   `CORDIC` or   `Lookup`) |
| - `tan` - `asin` - `acos` - `atan` - `sinh` - `cosh` - `tanh` - `asinh` - `acosh` - `atanh` | - Floating point |

CORDIC approximation fixed-point type propagations:

| Input Data Type | Function | Output Data Type |
| --- | --- | --- |
| Fixed point, signed or unsigned | `sin`, `cos`, `sincos`, and `cos + jsin` | `fixdt``(1, WL, WL - 2)` where *`WL`* is the input word length  This fixed-point type provides the best precision for the CORDIC algorithm. |
| Fixed point, signed | `atan2` | `fixdt``(1, WL, WL – 3)` |
| Fixed point, unsigned | `atan2` | `fixdt``(1, WL, WL – 2)` |

Lookup approximation fixed-point type propagations:

| Input Data Type | Function | Output Data Type |
| --- | --- | --- |
| Fixed point, signed | `sin`, `cos`, `sincos`, `cos + jsin`, `atan2` | `fixdt``(1, WL, FL)` |
| Fixed point, unsigned | `sin`, `cos`, `sincos`, `cos + jsin`, `atan2` | `fixdt``(1, WL - 1, FL)` |

#### Dependencies

- When you set **Function** to
  `atan2`, the block shows two input
  ports. The first input (**Port\_1**) is the
  *y*-axis or imaginary part of the
  function argument. The second input
  (**Port\_2**) is the
  *x*-axis or real part of the function
  argument.
- You can use floating-point input signals when you set
  **Approximation method** to
  `None`,
  `CORDIC`, or
  `Lookup`. However, the block
  output data type depends on which of these approximation
  method options you choose.

  | Input Data Type | Approximation Method | Output Data Type |
  | --- | --- | --- |
  | Floating point | `None` | Depends on your selection for **Output signal type**. Options are `auto` (same data type as input), `real`, or `complex`. |
  | Floating point | `CORDIC` | Same as input. **Output signal type** is not available when you use the CORDIC approximation method to compute the block output. |
  | Floating point | `Lookup` | Same as input. **Output signal type** is not available when you use the Lookup approximation method to compute the block output. |

For CORDIC and Lookup approximations:

- Input must be real for the `sin`,
  `cos`, `sincos`,
  `cos + jsin`, and
  `atan2` functions.
- Output is real for the `sin`,
  `cos`, `sincos`, and
  `atan2` functions.
- Output is complex for the `cos + jsin`
  function.

For more information, see Limitations.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_2** — *x*-axis or real part of the function argument for `atan2` scalar | vector | matrix

Input the *x*-axis or real part of the function
argument for `atan2`. When you set
**Function** to `atan2`, the block
shows two input ports. The first input (**Port\_1**) is
the *y*-axis or imaginary part of the function
argument. The second input (**Port\_2**) is the
*x*-axis or real part of the function argument.
(See Identify Port Location on Rotated or Flipped Block for a description of
the port order for various block orientations.)

Fixed-point input signals are supported only when you set
**Approximation** method to
`CORDIC` or
`Lookup`.

#### Dependencies

To enable this port, set **Function** to
`atan2`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Specified trigonometric function of input scalar | vector | matrix

Result of applying the specified trigonometric function to one or more
inputs in rad. Each function supports:

- Scalar operations
- Element-wise vector and matrix operations

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **sin** — Sine of input signal scalar | vector | matrix

Sine of the input signal, in rad and rev.

#### Dependencies

To enable this port, set **Function** to
`sincos`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **cos** — Cosine of input signal scalar | vector | matrix

Cosine of the input signal, in rad and rev.

#### Dependencies

To enable this port, set **Function** to
`sincos`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### Algorithm

### **Function** — Trigonometric function `sin` (default) | `cos` | `tan` | `asin` | `acos` | `atan` | `atan2` | `sinh` | `cosh` | `tanh` | `asinh` | `acosh` | `atanh` | `sincos` | `cos + jsin`

Specify the trigonometric function. The name of the function on the
block icon changes to match your selection.

For more information on when you set **Function** to
`sin`, `cos`,
`sincos`, or `cos + jsin` and set
the **Approximation method** to
`CORDIC`, see Limitations.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Operator` |
| **Type:** character vector |
| **Values:** `'sin' | 'cos' | 'tan' | 'asin' | 'acos' | 'atan' | 'atan2' | 'sinh' | 'cosh' | 'tanh' | 'asinh' | 'acosh' | 'atanh' | 'sincos' | 'cos + jsin'` |
| **Default:** `'sin'` |

### **Approximation method** — CORDIC, Lookup, or none `None` (default) | `CORDIC` | `Lookup`

Specify the type of approximation for computing output.

| Approximation Method | Data Types Supported | When to Use This Method |
| --- | --- | --- |
| `None` (default) | Floating point | You want to use the default Taylor series algorithm. |
| `CORDIC` | Floating point and fixed point | You want a fast, approximate iterative calculation. |
| `Lookup` | Floating point (double and single) and fixed point with a **Bias** value of `0` and a **Slope** value of the power of 2 | You want a fast, approximate lookup table implementation. |

For more information on when you set **Function** to
`sin`, `cos`,
`sincos`, or `cos + jsin` and set
the **Approximation method** to
`CORDIC`, see Limitations.

#### Dependencies

- To enable this parameter, set
  **Function** to
  `sin`,
  `cos`,
  `sincos`, `cos +
  jsin`, or `atan2`.
- To use fixed-point input signals, you must set
  **Approximation method** to
  `CORDIC` or
  `Lookup`.
- To enable the **Table data type**
  parameter, set this method to
  `Lookup`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ApproximationMethod` |
| **Type:** character vector |
| **Values:** `'None' | 'CORDIC' | 'Lookup'` |
| **Default:** `'None'` |

### **Interpolation method** — Method of interpolation between breakpoint values `Linear point-slope` (default) | `Flat`

When an input falls between breakpoint values, the block interpolates
the output value using neighboring breakpoints. For more information on
interpolation methods, see Interpolation Methods.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InterpMethod` |
| **Type:** character vector |
| **Values:** `'Linear point-slope' | 'Flat'` |
| **Default:** `'Linear point-slope'` |

### **Number of iterations** — Number of iterations for CORDIC algorithm `11` (default) | positive integer, less than or equal to word length of fixed-point input

Specify the number of iterations to perform the CORDIC algorithm. The
default value is 11.

- When the block input uses a floating-point data type, the
  number of iterations can be a positive integer.
- When the block input is a fixed-point data type, the number of
  iterations cannot exceed the word length.

  For example, if the block input is
  `fixdt(1,16,15)`, the word length is 16. In
  this case, the number of iterations cannot exceed 16.

#### Dependencies

To enable this parameter, you must set the
**Function** and **Approximation
method** parameters as follows:

- Set **Function** to
  `sin`,
  `cos`,
  `sincos`, `cos +
  jsin`, or `atan2`.
- Set **Approximation method** to
  `CORDIC`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumberOfIterations` |
| **Type:** character vector |
| **Values:** positive integer, less than or equal to word length of fixed-point input |
| **Default:** `'11'` |

### **Angle unit** — Angle unit `radian` (default) | `revolution`

Specify the angle unit for lookup method as
`radian` or
`revolution`.

#### Dependencies

To enable this parameter:

- Set **Function** to
  `sin`,
  `cos`,
  `sincos`, `cos +
  jsin`, or `atan2`.
- Set **Approximation method** to
  `Lookup`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AngleUnit` |
| **Type:** character vector |
| **Values:** `'radian' | 'revolution'` |
| **Default:** `'radian'` |

### **Number of data points** — Number of data points for lookup table `16` (default) | scalar

Specify the number of data points for lookup table as a scalar real
number.

#### Dependencies

To enable this parameter:

- Set **Function** to
  `sin`,
  `cos`,
  `sincos`, `cos +
  jsin`, or `atan2`.
- Set **Approximation method** to
  `Lookup`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumberOfDataPoints` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'16'` |

### **Output signal type** — Complexity of output signal `auto` (default) | `real` | `complex`

Specify the output signal type of the Trigonometric
Function block as `auto`,
`real`, or `complex`.

| Function | Input Signal Type | Output Signal Type | | |
| --- | --- | --- | --- | --- |
| Auto | Real | Complex |
| Any selection for the **Function** parameter | real | real | real | complex |
| complex | complex | error | complex |

#### Dependencies

Setting **Approximation method** to
`CORDIC` disables this
parameter.

**Note**

When **Function** is
`atan2`, complex input signals are not
supported for simulation or code generation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputSignalType` |
| **Type:** character vector |
| **Values:** `'auto' | 'real' | 'complex'` |
| **Default:** `'auto'` |

### **Remove protection against out-of-range input** — Remove protection against out-of-range input off (default) | on

For `acos` and
`asin`, select this check box to remove the
protection against out-of-range inputs, which reduces redundancy.

- When you clear this check box, the protection is enabled. The
  block saturates out-of-range inputs to `1` or
  `-1` before any operation is performed.
  Generated code contains code to check for out-of-range
  input.
- When you select this check box, the protection is removed. The
  block performs all operations on the input value without any
  changes. Generated code does not contain code to check for the
  out-of-range input.

Enabling this check box can eliminate redundancy if the input is
already in range.

#### Dependencies

Setting **Function** to
`acos` and
`asin` enables this parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RemoveProtectionAgainstOutOfRangeInput` |
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

### Data Types

### **Table data type** — Data type of table `Inherit: Inherit via input` (default) | `double` | `single` | `fixdt(1,16,0)` | `<data type expression>`

Data type for the lookup table, specified as:

- `Inherit: Inherit via input`
- `double`
- `single`
- `fixdt(1,16,0)`
- `<data type expression>`

For more information on setting data types, see Control Data Types of Signals.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableDataTypeStr` |
| **Type:** string scalar or character vector |
| **Values:** `Inherit: Inherit via input` | `single` | `double` | `fixdt(1,16,0)` | data type expression |
| **Default:** `Inherit: Inherit via input` |

### **Mode** — Category of data to specify `Inherit` (default) | `Built in` | `Fixed point` | `Expression`

Select how you would like to specify the data type properties of the
**Output** data type. You can choose:

- `Inherit` — Lets you
  specify a rule for inheriting a data type, for example,
  `Inherit: Inherit via internal
  rule`
- `Built in`— Lets you
  specify a built-in data type.
- `Fixed point` — Lets you
  specify the fixed-point attributes of the data type.
- `Expression` — Lets you
  specify an expression that evaluates to a valid data type,
  for example, `fixdt([],16,0)`

#### Dependencies

To enable this parameter, click **>>** at the
**Output data type** parameter.

### **Signedness** — Specify signed or unsigned `Signed` (default) | `Unsigned`

Specify the **Signedness** for the
**Output** data type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Scaling** — Method for scaling fixed-point data `Binary point` (default)

Specify the **Scaling** for the
**Output** data type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Data type override** — Specify data type override mode for this signal `Inherit` | `Off`

Select the data type override mode for this signal.

- `Inherit` — Inherits the data
  type override setting specified for the model.
- `Off` — Ignores the data type
  override setting specified for the model and uses the
  fixed-point data type you specify

For more information, see Specify Data Types Using Data Type Assistant in the Simulink® documentation.

#### Tips

The ability to turn off data type override for an individual data
type provides greater control over the data types in your model when
you apply data type override. For example, you can use this option
to ensure that data types meet the requirements of downstream blocks
regardless of the data type override setting.

#### Dependencies

To enable this parameter, click the **Show data type
assistant** button, and set **Mode**
to `Built in` or `Fixed
point`.

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

To enable this parameter, set:

- **Mode** to `Fixed
  point`
- **Scaling** to `Binary
  point`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed pointa` | `half` | `integera` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a This block supports fixed-point and base integer data types for 'Approximation method' CORDIC. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not all compilers support the `asinh`, `acosh`,
and `atanh` functions. If you use a compiler that does not support
those functions, a warning appears and the generated code fails to link.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

To generate HDL code from the blocks that use fixed-point data, set **Architecture** to `Cordic` or `LUT`. This table
shows the functions the block supports for these
setting:

| Block Parameters | HDL Block Properties | Supported Functions |
| --- | --- | --- |
| Set **Approximation method** to `CORDIC`, **Number of data Points** to any scalar real number. | Set **Architecture** to `Cordic`. | - `sin` - `cos` - `sincos` - `cos+jsin` - `atan2` |
| Set **Approximation method** to `Lookup`, **Interpolation method** to `Flat`, **Angle Unit** to `revolution`, and **Number of data Points** to any scalar real number. | Set **Architecture** to `LUT`. | - `sin` - `cos` - `sincos` - `cos+jsin` |

To generate HDL code for all functions of the block that use floating-point data, set the
**Approximation method** block parameter to
`none`, and the **Output signal
type** parameter to `auto` or
`real` or `complex`.
Additionally, set the **Architecture** parameter in the HDL
Block Properties to `Trigonometric`.

This block has multi-cycle implementations that introduce additional
latency in the generated code. To see the added latency, view the
generated model or validation model. See Generated Model and Validation Model (HDL Coder).

The latency calculation depends on the word length and
**LatencyStrategy** settings. To view the latency
calculation for fixed-point data types, see:

- Sin (HDL Coder)
- Cos (HDL Coder)
- Cos+jSin (HDL Coder)
- SinCos (HDL Coder)
- Atan2 (HDL Coder)

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **LatencyStrategy** | To enable this property for fixed-point types, set **Function** as `sin`, `cos`, `sincos`, `cos+jsin`, or `atan2` and **Approximation method** as `CORDIC`. Specify whether to map the blocks in your design to `MAX`, `Min`, `CUSTOM`, or `ZERO` latency for fixed-point and floating-point types. The default is `MAX`. See also LatencyStrategy (HDL Coder). |
| **CustomLatency** | To enable this property for fixed-point types, set **Function** as `sin`, `cos`, `sincos`, `cos+jsin`, or `atan2` and **Approximation method** as `CORDIC`. When **LatencyStrategy** is set to `CUSTOM`, use this property to specify a custom latency value between `ZERO` and `MAX` for fixed-point types. See also LatencyStrategy (HDL Coder). |
| **IterationsPerPipeline** | To enable this property for fixed-point types, set **Function** as `sin`, `cos`, `sincos`, `cos+jsin`, or `atan2` and **Approximation method** as `CORDIC`.  When you set **LatencyStrategy** to `Custom(PerIterations)`, use this setting to specify the number of iterations per pipeline stages. For more information, see Atan2 (HDL Coder). |

| Native Floating Point | |
| --- | --- |
| **InputRangeReduction** | Use this property for the `sin`, `cos`, `sincos`, `cos+jsin`, and `atan2` functions. If your input range is unbounded, enable this property for HDL Coder to insert additional logic to reduce the range of inputs to `[-pi, pi]`. See also InputRangeReduction (HDL Coder). |
| **HandleDenormals** | Specify whether you want HDL Coder to insert additional logic to handle denormal numbers in your design. Denormal numbers are numbers that have magnitudes less than the smallest floating-point number that can be represented without leading zeros in the mantissa. The default is `inherit`. See also HandleDenormals (HDL Coder). |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `inherit`, `Max`, `Min`, or `Zero` for the floating-point operator. The default is `inherit`. See also LatencyStrategy (HDL Coder). |
| **MultiplyStrategy** | Use this property for the `sin`, `cos`, `sincos`, `cos+jsin`, and `atan2` functions. The default is `inherit`. Specify whether you want to use `FullMultiplier` or `PartMultiplierPartAddShift`. See also MantissaMultiplyStrategy (HDL Coder). |

**ULP Considerations**

The Trigonometric Function blocks have nonzero units in the last place (ULP)
error for floating point operations. For more information, see ULP Considerations of Native Floating-Point Operators (HDL Coder).

**Restrictions**

- For the `sin` and
  `cos` functions, the block supports
  only signed fixed-point data types for
  CORDIC approximations.
- For functions that have the CORDIC mode, such as
  `sin`, `cos`,
  `sincos`, `atan2`,
  and `cos+jsin`, HDL code generation does not
  support fixed-point data types greater than `127`
  bits.
- HDL code generation does not support the double data types for
  trigonometric functions, except for `sin` and
  `cos` functions.
- HDL code generation does not support the lookup approximation method
  when:

  - The **Interpolation method** parameter is
    set to `Linear point-slope` and the
    **Angle Unit** parameter is set to
    `radian` or
    `revolution`.
  - The **Interpolation method** parameter is
    `Flat` and the **Angle
    Unit** parameter is
    `radian`.
- HDL Coder displays an error when a Trigonometric
  Function block is inside a feedback loop and you set:

  - **Architecture** to
    `Cordic`
  - **UsePipelinedKernel** to
    `On`

  The error occurs because the block is in a feedback loop
  and the code generator is unable to insert additional latency. To avoid
  this error, add a delay of length equal to the **Number of
  iterations** plus 3 adjacent to the block. The code
  generator then absorbs this delay to meet the additional latency of the
  Trigonometric Function block.

  For example, this Trigonometric Function block has **Number of
  iterations** set to `30`. Adding a
  Delay block with a length `33`
  adjacent to the block meets the additional latency.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

This block supports fixed-point and base integer data types when you set the
**Function** to `sin`,
`cos`, `sincos`,
`cos + jsin`, or `atan2` and set the
**Approximation method** to
`CORDIC`.

## Version History

**Introduced before R2006a**
