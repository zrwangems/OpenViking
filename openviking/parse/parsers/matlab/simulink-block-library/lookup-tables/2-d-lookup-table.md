---
type: simulink-block
title: '2-D Lookup Table'
family: lookup-tables
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Lookup Tables'
documentation_page: '2dlookuptable'
---

# 2-D Lookup Table

Approximate two-dimensional function

## 中文

逼近二维函数

### 所属库

Simulink / Lookup Tables HDL Coder / Lookup Tables

### 描述

#### 支持的模块运算

1-D、2-D 和 n-D Lookup Table 模块计算一个函数的 N 变量采样表示

y=F(x1,x2,x3,...,xN)

其中函数 *F* 可以是经验函数。此模块通过查找或插入您使用模块参数定义的值表，将输入映射到输出值。该模块支持均一（常量）、线性（线性点-斜率）、拉格朗日（线性拉格朗日）、最近、三次样条和 Akima 样条插值方法。您可以将这些方法应用于从 1 维到 30 维的表。

在下面的模块中，第一个输入标识第一个维度（行）断点，第二个输入标识第二个维度（列）断点，依此类推。

有关各种模块方向的端口顺序的描述，请参阅标识旋转或翻转模块上的端口位置。

设置**数学和数据类型** > **使用针对行优先数组布局优化的算法**配置参数后，2-D 和 n-D Lookup Table 模块行为会从列优先更改为行优先。对于这些模块，列优先算法和行优先算法可能在输出计算的顺序上有所不同，从而可能导致数值略有不同。此功能需要 Simulink® Coder™ 或 Embedded Coder® 许可证。有关行优先支持的详细信息，请参阅Code Generation of Matrices and Arrays (Simulink Coder)。

#### 指定断点和表数据

以下模块参数定义断点和表数据。

| 模块参数 | 用途 |
| --- | --- |
| **表维数** | 指定查找表的维数。 |
| **断点** | 指定与查找表的每个维度对应的断点向量。 |
| **表数据** | 定义关联的一组输出值。 |

**提示**

等间距断点可以使生成的代码无分割。有关详细信息，请参阅 `fixpt_evenspace_cleanup` 和Identify questionable fixed-point operations (Embedded Coder)。

#### 模块如何生成输出

n-D、1-D 和 2-D Lookup Table 模块通过基于输入值查找或估计表值来生成输出。

| 模块输入 | n-D Lookup Table 模块行为 |
| --- | --- |
| 与断点向量中的索引值匹配 | 输出位于行、列和更高维度断点的交点处的表值 |
| 与断点向量中的索引值不匹配，但在范围内 | 使用您选择的**内插方法**内插适当的表值 |
| 与断点向量中的索引值不匹配，且不在范围内 | 使用您选择的**外插方法**外插输出值 |

#### 执行等效操作的其他模块

您可以将 Interpolation Using Prelookup 模块与 Prelookup 模块一起使用，以执行等效于一个 n-D Lookup Table 模块的操作。这种模块组合可以提供更大的灵活性，从而为线性插值实现更高效的仿真性能。

当查找操作是不需要插值的数组访问时，请使用 Direct Lookup Table (n-D) 模块。例如，如果您有一个整数值 `k`，而您需要表的第 `k` 个元素 `y = table(k)`，则不需要插值。

### 端口

#### 输入

#### **u1** — 第一个维度（行）输入 标量 | 向量 | 矩阵

**u1** 端口的实数值输入，通过查找您定义的值表或对其进行插值来映射到输出值。

**示例:** `0:10`

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `enumerated` | `fixed point`

#### **u2** — 第二个维度（列）输入 标量 | 向量 | 矩阵

**u2** 端口的实数值输入，通过查找您定义的值表或对其进行插值来映射到输出值。

**示例:** `0:10`

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `enumerated` | `fixed point`

#### **T** — 定义输出值的表 值组成的矩阵，其维度与**表维数**匹配，每个维度与表中每个维度的断点长度匹配

用运行时可调的信号指定输出值表。

在仿真期间，矩阵大小必须与**表维数**参数定义的维度以及表的每个维度的断点长度相匹配。但是，在编辑模块图的过程中，您可以输入空矩阵（指定为 `[]`）或者未定义的工作区变量。利用此方法，您可以推迟为表数据指定正确设置维度的矩阵，并继续编辑模块图。

##### 依赖关系

要启用此端口，请进行如下设置：

- 将**数据设定**设置为**表和断点**。
- 将**表数据**设置为**输入端口**。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **bp1** — 显式断点值 单调递增值的 1×n 或 n×1 向量

根据**断点设定**参数的值，使用运行时可调的信号显式指定断点数据。

- 如果您将**断点设定**设置为**显式值**，请在每个**断点**行中输入与表数据的每个维度对应的断点向量。对于每个维度，将断点指定为值严格单调递增的 1×n 或 n×1 向量。

**注意**

要以等间距设定格式指定断点，请将**断点设定**设置为**等间距**，并使用**断点的第一个**点和**间距**参数。

##### 依赖关系

要启用此端口，请进行如下设置：

- 将**数据设定**设置为**表和断点**。
- 将**断点设定**设置为**显式值**。
- 将**断点 1** 设置为**输入端口**。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `enumerated` | `fixed point`

#### **bp2** — 显式断点值 单调递增值的 1×n 或 n×1 向量

根据**断点设定**参数的值，使用运行时可调的信号显式指定断点数据。

- 如果您将**断点设定**设置为**显式值**，请在每个**断点**行中输入与表数据的每个维度对应的断点向量。对于每个维度，将断点指定为值严格单调递增的 1×n 或 n×1 向量。

**注意**

要指定等间距断点数据，请使用**断点**参数。您无法通过输入端口指定等间距断点数据。

##### 依赖关系

要启用此端口，请进行如下设置：

- 将**数据设定**设置为**表和断点**。
- 将**断点设定**设置为**显式值**。
- 将**断点 2** 设置为**输入端口**。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `enumerated` | `fixed point`
#### 输出

#### **Port\_1** — 通过查找或估算表值计算的输出 标量 | 向量 | 矩阵

通过查找或基于输入值估算表值生成的输出。

| 如果模块输入... | n-D Lookup Table 模块... |
| --- | --- |
| 与断点向量中的索引值匹配 | 输出位于行、列和更高维度断点的交点处的表值 |
| 与断点向量中的索引值不匹配，但在范围内 | 使用您选择的**内插方法**内插适当的表值 |
| 与断点向量中的索引值不匹配，且不在范围内 | 使用您选择的**外插方法**外插输出值 |

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 参数

#### 表和断点

#### **表维数** — 查找表维度的数量 `2` (默认) | `1` | `3` | `4` | `...` | `30`

输入查找表的维数。此参数确定：

- 表的自变量数量以及模块输入的数量
- 要指定的断点向量数目

| 要指定... | 执行此操作... |
| --- | --- |
| 1、2、3 或 4 | 从下拉列表中选择值。 |
| 更高的表维数 | 直接在字段中输入正整数。  此模块支持的最大表维数为 30。 |

例如，大小为 *M*×*N*×... 的表表示维度 1 的大小是 *M*，维度 2 的大小是 *N*，依此类推。*M* 必须匹配第一个断点长度，*N* 必须匹配第二个断点长度，依此类推。

##### 编程用法

|  |
| --- |
| **模块参数**：`NumberOfTableDimensions` |
| **类型：**字符向量 |
| **值：**`'1' | '2' | '3' | '4' | ... | 30` |
| **默认值：**`'2'` |

#### **数据设定** — 表和断点的设定方法 **表和断点** (默认) | **查找表对象**

从列表中，选择：

- **表和断点** - 指定表数据和断点。选中此选项将启用下列参数：

  - **表数据**
  - **断点设定**
  - **断点 1**
  - **断点 2**
  - **编辑表和断点**

  要使用输入端口指定表和断点，请查看**源**参数。
- **查找表对象** - 使用现有查找表 (`Simulink.LookupTable`) 对象。选中此选项将启用**名称**字段和**编辑表和断点**按钮。

##### 编程用法

|  |
| --- |
| **模块参数**：`DataSpecification` |
| **类型：**字符向量 |
| **值：**`'Table and breakpoints' | 'Lookup table object'` |
| **默认值：**`'Table and breakpoints'` |

要将此参数从 `'Table and breakpoints'` 设置为 `'Lookup table object'`，请使用相同的 `set_param` 调用来设置 `LookupTableObject` 参数。例如：

```
set_param('myModel/myLookupBlock',...
   'DataSpecification','Lookup table object',...
   'LookupTableObject','myLUTObject')
```

#### **名称** — 查找表对象的名称 `[]` (默认) | `Simulink.LookupTable` 对象

输入查找表 (`Simulink.LookupTable`) 对象的名称。如果 `Simulink.LookupTable` 对象不存在，请点击操作按钮  并选择**创建**。新查找表对象的对应参数会自动用模块信息填充。

##### 依赖关系

要启用此参数，请将**数据设定**设置为**查找表对象**。

##### 编程用法

|  |
| --- |
| **模块参数**：`LookupTableObject` |
| **类型：**字符向量 |
| **值：**`Simulink.LookupTable` 对象的名称 |
| **默认值：**`''` |

#### **断点设定** — 断点设定的方法 **显式值** (默认) | **等间距**

指定是以显式断点形式还是参数形式输入数据，以生成等间距断点。

- 要显式指定断点数据，请将此参数设置为**显式值**，并在**断点**参数旁边的文本框中输入断点数据。
- 要指定参数以生成等间距断点，请将此参数设置为**等间距**，并为断点数据的每个维度的**第一个点**和**间距**参数输入值。模块将根据表数据计算要生成的点数。

##### 依赖关系

要启用此参数，请将**数据设定**设置为**表和断点**。

##### 编程用法

|  |
| --- |
| **模块参数**：`BreakpointsSpecification` |
| **类型：**字符向量 |
| **值：**`'Explicit values' | 'Even spacing'` |
| **默认值：**`'Explicit values'` |

#### **支持可调大小** — 用于启用可调表大小的选项 `off` (默认) | `on`

选中此复选框可在仿真运行或生成的代码执行时启用可调表大小。此选项使软件即使在生成的代码执行期间更改查找表和断点数据的大小和值时，也能正常工作。表大小必须为 2 或更大但小于最大可调大小。

##### 依赖关系

如果您将**插值方法**设置为**三次样条**或 **Akima 样条**，**支持可调大小**将不可用。

##### 编程用法

|  |
| --- |
| **模块参数**：`SupportTunableSize` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **源** — 表和断点数据的源 **对话框** (默认) | **输入端口**

表和断点数据的源，指定为：

- **对话框** - 在**值**参数中指定表或断点数据。
- **输入端口** - 通过关联的输入端口指定表或断点数据。通过输入端口，您最多只能指定三组断点数据。要指定三组以上的断点数据，请使用**值**参数。

**注意**

使用输入端口指定表或断点数据可能会因为运行时检查对仿真的模块性能产生负面影响。要对需要在仿真期间更改断点的动态特性进行建模，请选择**对话框**并使用 Parameter Writer 模块更改断点数据。

##### 依赖关系

- 要启用此参数，请将**数据设定**设置为**表和断点**。
- 要启用关联的**值**，请将此参数设置为**对话框**。
- 要启用相关联的输入端口，请将此参数设置为**输入端口**。
- 将此参数设置为**输入端口**将禁用**值**字段，并隐藏**数据类型**选项卡上的对应参数。
- 对于任一参数，将此参数设置为**输入端口**都会禁用**编辑表和断点**按钮。

##### 编程用法

|  |
| --- |
| **模块参数：**`TableSource` | `BreakpointsForDimension1Source` | `BreakpointsForDimension2Source` | `BreakpointsForDimension3Source` |
| **类型：**字符向量 |
| **值**：`Dialog` | `Input port` |
| **默认值：**`'Dialog'` |

#### **可调大小** — 每个数组的最大元素数 `-1` (默认) | 实整数标量

将每个数组的最大大小指定为以下值之一：

- `-1` - 数组中的所有元素
- 实整数标量 - 每个数组的最大元素数

**可调大小**必须小于或等于数组的大小。

##### 依赖关系

要启用此参数，请进行如下设置：

- 将**数据设定**设置为**表和断点**。
- 选择**支持可调大小**参数。

##### 编程用法

|  |
| --- |
| **模块参数：**`N1` 到 `N31` |
| **类型：**字符向量 |
| **值：**`-1` | 实整数标量 |
| **默认值：**`-1` |

#### **表数据** — 定义输出值的表 `[4 5 6; 16 19 20; 10 18 23]` (默认) | 值矩阵

在相关联的**值**字段中输入输出值的表。

在仿真期间，矩阵大小必须与**表维数**参数定义的维度匹配。但是，在编辑模块图的过程中，您可以输入空矩阵（指定为 `[]`）或者未定义的工作区变量。利用此方法，您可以推迟为表数据指定正确设置维度的矩阵，并继续编辑模块图。

##### 依赖关系

要启用此参数，请进行如下设置：

- 将**数据设定**设置为**表和断点**。
- 将**表数据:源**设置为**对话框**。

##### 编程用法

|  |
| --- |
| **模块参数**：`Table` |
| **类型：**字符向量 |
| **值：**表值构成的矩阵 |
| **默认值：**`'[4 5 6; 16 19 20; 10 18 23]'` |

#### **断点** — 显式断点值，或断点的第一个点和间距 `[1:3]` (默认) | 单调递增值的 1×n 或 n×1 向量

显式指定断点数据或者指定为等间距断点，具体取决于**断点设定**参数。

- 如果您将**断点设定**设置为**显式值**，请在相关联的**值**字段中的每个**断点**行中输入与表数据的每个维度对应的断点向量。对于每个维度，将断点指定为值严格单调递增的 1×n 或 n×1 向量。
- 如果您将**断点设定**设置为**等间距**，请在每个**断点**行中输入参数**第一个点**和**间距**，以便在各自的维度生成等间距断点。您的表数据决定等间距点数。

##### 依赖关系

- 要启用此参数，请进行如下设置：

  - 将**数据设定**设置为**表和断点**。
  - **断点:源**设置为**对话框**。
- 当**断点设定**参数设置为**等间距**时，您只能通过对话框指定断点数据。

##### 编程用法

|  |
| --- |
| **模块参数**：`BreakpointsForDimension1` |
| **类型：**字符向量 |
| **值：**单调递增值的 1×n 或 n×1 向量 |
| **默认值：**`'[1:3]'` |

#### **第一个点** — 等间距断点数据中的第一个点 `1` (默认) | 标量

将等间距断点数据中的第一个点指定为实数值有限标量。当**断点设定**设置为**等间距**时，此参数可用。

##### 依赖关系

要启用此参数，请将**数据设定**设置为**表和断点**，并将**断点设定**设置为**等间距**。

##### 编程用法

|  |
| --- |
| **模块参数**：`BreakpointsForDimension1FirstPoint | BreakpointsForDimension2FirstPoint` |
| **类型：**字符向量 |
| **值：**实数值有限标量 |
| **默认值：**`'1'` |

#### **间距** — 等间距断点之间的间距 `1` (默认) | 标量

指定等间距断点数据中各点之间的距离。

##### 依赖关系

要启用此参数，请将**数据设定**设置为**表和断点**，并将**断点设定**设置为**等间距**。

##### 编程用法

|  |
| --- |
| **模块参数**：`BreakpointsForDimension1Spacing | BreakpointsForDimension2Spacing` |
| **类型：**字符向量 |
| **值：**正实数值有限标量 |
| **默认值：**`'1'` |

#### **编辑表和断点** — 启动“查找表编辑器”对话框 按钮

点击此按钮以打开查找表编辑器。有关详细信息，请参阅查找表编辑器。

对于查找表对象，点击此按钮可以编辑该对象并为该对象保存新值。

#### 算法

##### 查找方法

#### **插值方法** — 断点值之间插值的方法 **线性点-斜率** (默认) | **均一** | **最邻近值** | **线性拉格朗日** | **三次样条** | **Akima 样条**

当输入位于两个断点值之间时，模块将根据相邻断点内插输出值。有关插值方法的详细信息，请参阅内插方法。

##### 依赖关系

- 如果您选择**三次样条**，则模块仅支持标量信号。其他插值方法支持非标量信号。
- 如果选择 **Akima 样条**，外插方法只能是 **Akima 样条**。

  当设置为修正 Akima 插值方法时，此模块不支持：

  - 行优先数组布局和针对行优先数组布局优化的算法
  - 定标的双精度和定点数据类型
  - `Simulink.LookupTable` 对象
  - 选中配置参数**代码生成** > **接口** > **支持非有限数**复选框时的代码生成

  当设置为修正 Akima 插值方法时，如果以下条件成立，此模块的运行速度会更慢：

  - 基于代码生成的仿真目标，如加速模式、快速加速模式、受保护模型等的仿真目标。
  - 为大型断点和数据表生成的代码。例如，表大小为 629×1601。

##### 编程用法

|  |
| --- |
| **模块参数**：`InterpMethod` |
| **类型：**字符向量 |
| **值：**`'Linear point-slope' | 'Flat' | 'Nearest' | 'Linear Lagrange' | 'Cubic spline' | 'Akima spline'` |
| **默认值：**`'Linear point-slope'` |

#### **外插方法** — 处理超出断点向量范围的输入值的方法 **线性** (默认) | **裁剪** | **三次样条** | **Akima 样条**

选择**裁剪**、**线性**或**三次样条**。有关详细信息，请参阅外插方法。

如果外插方法是**线性**，则基于所选择的线性插值方法计算外插值。例如，如果插值方法是线性拉格朗日，则外插方法继承线性拉格朗日方程以计算外插值。

##### 依赖关系

- 要为**外插方法**选择**三次样条**，还必须为**内插方法**选择**三次样条**。
- 要为**外插方法**选择 **Akima 样条**，您还必须为**内插方法**选择 **Akima 样条**。

##### 编程用法

|  |
| --- |
| **模块参数**：`ExtrapMethod` |
| **类型：**字符向量 |
| **值：**`'Linear' | 'Clip' | 'Cubic spline' | 'Akima spline'` |
| **默认值：**`'Linear'` |

#### **索引搜索方法** — 计算表索引的方法 **二分搜索** (默认) | **线性搜索** | **等间距点**

选择**等间距点**、**线性搜索**或**二分搜索**。每一种搜索方法在不同的情况下均有各自的速度优势：

- 对于等间距断点向量（例如，10、20、30 等），您可以选择**等间距点**来计算表索引，以获得最佳速度。

  此算法仅使用断点集的前两个断点来确定其余点的偏移量和间距。

  **注意**

  当使用 `Simulink.LookupTable` 对象指定表数据且引用的 `Simulink.LookupTable` 对象的**断点设定**参数设置为**等间距**时，请将**索引搜索方法**设置为**等间距点**。
- 对于非等间距的断点向量，请遵循以下规范：

  - 如果输入信号在时间步之间的变化不大，选择**线性搜索**与**使用上一个索引结果开始索引搜索**可以获得最佳性能。
  - 如果输入信号在每个时间步中跳过的表间隔超过一个或两个，选择**二分搜索**可以获得最佳性能。

对于严重依赖查找表的模型，选择次优索引搜索方法可能会导致性能下降。

**注意**

在以下情况下，生成的代码只存储第一个断点、间距和断点数量：

- 断点数据不可调。
- 索引搜索方法是**等间距点**。

##### 编程用法

|  |
| --- |
| **模块参数**：`IndexSearchMethod` |
| **类型：**字符向量 |
| **值：**`'Binary search' | 'Evenly spaced points' | 'Linear search'` |
| **默认值：**`'Binary search'` |

#### **尽可能应用更准确高效的舍入** — 使用高效舍入到最接近值进行更精确的定点表查找 `off` (默认) | `on`

选中此复选框可尽可能启用高效舍入到最接近的实现。启用此选项会将舍入模式设置为 `Nearest`，并调整小数长度和中间数据类型以在准确度和效率之间取得平衡。如果不能得到高效实现，则舍入模式、小数长度和中间数据类型保持不变。

##### 依赖关系

要启用此参数，请进行如下设置：

- 将**表维数**设置为 **2**。
- 将**内插方法**设置为**线性点-斜率**。
- 将**外插方法**设置为**裁剪**。

##### 编程用法

|  |
| --- |
| **模块参数**：`ApplyAccurateEfficientRounding` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **使用上一个索引结果开始索引搜索** — 开始使用来自上一时间步的索引 `off` (默认) | `on`

如果您希望模块使用在上一个时间步中找到的索引开始搜索，请选中此复选框。对于相对于间隔大小而言变化缓慢的输入，启用此选项可以提高性能。否则，线性搜索和二分搜索方法可能需要更长的时间，尤其是对于大型断点向量来说。

##### 依赖关系

要启用此参数，请将**索引搜索方法**设置为**线性搜索**或**二分搜索**。

##### 编程用法

|  |
| --- |
| **模块参数**：`BeginIndexSearchUsingPreviousIndexResult` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **假设输入在范围内** — 检查输入值是否超出范围的选项 `off` (默认) | `on`

*自 R2025a 起*

指定是否包含代码以检查超出范围的输入值。选择此参数意味着您保证该模块没有超出范围的输入，从而使模块能够进一步优化代码和仿真。有效输入范围取决于断点数据和**外插方法**设置。

当您选择**假设输入在范围内**时：

- 在仿真期间，模块假定没有超出范围的输入，并通过对超出范围的输入返回错误来强制实现此假设。
- 对于代码生成，模块不会生成超出范围的输入处理代码，因为它假定不存在超出范围的输入。这意味着，如果模块尝试为因输入超出范围而返回错误的模型生成代码，则当给生成的代码提供相同的输入时，其行为是未定义的，这可能导致严重后果。

  **警告**

  如果模型尝试生成代码，但由于模块检测到输入超出范围而生成错误，则当将相同的超出范围的输入传递给已部署的代码时，行为是未定义的。这种未定义的行为可能导致严重问题。对于安全性至关重要的应用，请不要选择**假设输入在范围内**。

如果您要为了提升效率而选择**假设输入在范围内**参数，请确保模型输入在范围内。例如：

| 参数 | 结果 | 何时使用 |
| --- | --- | --- |
| `on` | 仿真和生成的代码中未包含用来检查超出范围的断点输入的条件语句。  当输入超出范围时，仿真和生成的代码可能会发生未定义的行为。 | 为了提升仿真和代码效率 |
| `off` | 仿真和生成的代码包含用来检查超出范围的输入的条件语句。 | 适用于安全性至关重要的应用领域 |

如果您确信输入在范围内，则可以为了提升效率选择**假设输入在范围内**参数。默认情况下，此参数处于清除状态。对于安全性至关重要的应用，不要选择此参数。如果您要选择**假设输入在范围内**参数，请先检查模型输入是否在范围内。例如：

1. 清除**假设输入在范围内**参数。
2. 将**输入超出范围的诊断**参数设置为 `Error`。
3. 在普通模式下进行模型仿真。
4. 如果存在超出范围错误，模块将返回运行时错误。请将它们更正到范围之内，然后再次运行仿真。
5. 当仿真不再生成超出范围的输入错误时，选择**假设输入在范围内**参数。

   **注意**

   当您选择**假设输入在范围内**参数且输入超出范围时，模块会在仿真时返回运行时错误。生成的代码的行为是未定义的。

根据您的具体应用，您可以运行以下模型顾问检查，以验证此参数的使用：

- **按产品** > **Embedded Coder** > **标识哪些查找表模块会生成检查超范围值的高成本代码**
- **按产品** > **Simulink Check** > **建模标准** > **DO-178C/DO-331 检查** > **检查 Lookup Table 模块的使用**

有关模型顾问的详细信息，请参阅运行模型顾问检查。

此外，要确定选择此参数是否安全，如果您拥有 Simulink Design Verifier™ 许可证，请考虑使用 检测模块输入范围违规 (Simulink Design Verifier) 检查。

##### 编程用法

|  |
| --- |
| **模块参数**：`RemoveProtectionInput` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **输入超出范围的诊断** — 当输入超出范围时的模块操作 **无** (默认) | **警告** | **错误**

指定当输入超出范围时，是否生成警告或错误消息。选项包括：

- **无** - 不产生任何响应。
- **警告** - 显示警告并继续进行仿真。
- **错误** - 终止仿真并显示错误。

##### 依赖关系

要启用此参数，请清除**假设输入在范围内**或**假设索引在范围内**参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`DiagnosticForOutOfRangeInput` |
| **类型：**字符向量 |
| **值：**`'None' | 'Warning' | 'Error'` |
| **默认值：**`'None'` |

#### **尽可能应用全精度定点算法** — 更精确的定点表查找 `off` (默认) | `on`

尽可能使用此复选框为线性插值查找启用全精度定点算法查找。对于硬件效率高的定点舍入模式，此算法通常可以实现更高的精度。

##### 依赖关系

要启用此参数，请进行如下设置：

- 将**表维数**设置为 **1**。
- 将**内插方法**设置为**线性点-斜率**。
- 将**外插方法**设置为**裁剪**。
- 选择**输入等于或高于最后一个断点时使用最后一个表值**参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`ApplyFullPrecisionForLinearInterpolation` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **输入等于或高于最后一个断点时使用最后一个表值** — 用于计算最后一个断点上或高于该断点的输入的输出的方法 `off` (默认) | `on`

使用此复选框，指定模块用来定位断点向量的最后一个元素及其对应表值的索引约定。当输入等于或大于断点数据的最后一个元素时，此复选框才有意义。由于舍入原因，选中和清除此复选框可能会导致仿真与代码生成之间最后一个断点的结果不同。

| 复选框 | 模块使用的索引 | 区间比 |
| --- | --- | --- |
| 选中 | **表和断点**选项卡上的断点数据的最后一个元素 | 0 |
| 清除 | **表和断点**选项卡上的断点数据的倒数第二个元素 | 1 |

假设输入 *u* 在断点向量 *bp* 的范围内，区间比 *f*（在 0≦*f*<1 范围内）按如下所示进行计算。

假设断点向量为 `[1 4 5]`，输入 *u* 为 `5.5`。如果您选中此复选框，索引则是最后一个元素 (`5`) 的索引，区间比为 0。如果您清除此复选框，索引则是倒数第二个元素 (`4`) 的索引，区间比为 1。

##### 依赖关系

要启用此参数，请进行如下设置：

- 将**内插方法**设置为**线性**。
- 将**外插方法**设置为**裁剪**。

##### 编程用法

|  |
| --- |
| **模块参数**：`UseLastTableValue` |
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

##### 输入设置

#### **所有输入数据使用一个输入端口** — 只使用一个输入端口 `off` (默认) | `on`

选中此复选框，从而对 N 维表只使用一个输入端口，此端口需要宽度为 `n` 个元素的信号。此选项可以有效减少包含许多查找表的模块图中的杂乱线条。

**注意**

如果您选中此复选框，模块上将出现一个带有 `u` 标签的输入端口。

##### 编程用法

|  |
| --- |
| **模块参数**：`UseOneInputPortForAllInputData` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### 数据类型

#### **表数据** — 表数据的数据类型 **继承: 与输出相同** (默认) | **double** | **single** | **half** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16)** | **fixdt(1,16,0)** | **fixdt(1,16,2^0,0)** | **<数据类型表达式>**

指定表数据类型。可以将其设置为：

- 继承数据类型的规则，例如**继承: 与输出相同**
- 内置数据类型的名称，例如 `single`
- 数据类型对象的名称，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

**提示**

对于以下情况，指定与输出数据类型不同的表数据类型：

- 存储表数据（使用的类型小于输出信号）的内存要求较低
- 在具有不同输出数据类型的两个 n-D Lookup Table 模块之间共享预缩放的表数据
- 在为具有不同输出数据类型的模块生成的代码中共享自定义存储表数据

##### 依赖关系

要启用此参数，请将**表和断点**选项卡中的**表数据**设置为**对话框**。

##### 编程用法

|  |
| --- |
| **模块参数**：`TableDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Inherit from 'Table data'' | 'Inherit: Same as output' | 'double' | 'single' | 'half' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)'|'<data type expression>'` |
| **默认值：**`'Inherit: Same as output'` |

#### **表数据最小值** — 表数据的最小值 `[]` | `scalar`

指定表数据的最小值。默认值为 `[]`（未指定）。

##### 编程用法

|  |
| --- |
| **模块参数**：`TableMin` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'[]'` |

#### **表数据最大值** — 表数据的最大值 `[]` | `scalar`

指定表数据的最大值。默认值为 `[]`（未指定）。

##### 编程用法

|  |
| --- |
| **模块参数**：`TableMax` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'[]'` |

#### **断点** — 断点数据类型 **继承: 与对应的输入相同** (默认) | **double** | **single** | **half** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16)** | **fixdt(1,16,0)** | **fixdt(1,16,2^0,0)** | **Enum: <class name>** | **<数据类型表达式>**

指定一组断点数据的数据类型。可以将其设置为：

- 继承数据类型的规则，例如**继承: 与对应的输入相同**
- 内置数据类型的名称，例如 `single`
- 数据类型类的名称，例如枚举数据类型类
- 数据类型对象的名称，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**提示**

- 断点支持无序枚举数据。因此，线性搜索也是无序的，这就提供了灵活性，但可能影响性能。搜索从断点中的第一个元素开始。
- 如果选中**使用上一个索引结果开始索引搜索**复选框，则必须使用有序单调递增数据。这种排序可提高性能。
- 对于枚举数据，**外插方法**必须是 `Clip`。
- 该模块不支持枚举数据的超出范围的输入。指定枚举数据时，请将整个枚举集包含在断点向量中。例如，使用 `enumeration` 函数。

以下是对此模块使用枚举数据的限制：

- 该模块不支持枚举数据的超出范围的输入。指定枚举数据时，请将整个枚举集包含在断点向量中。例如，使用 `enumeration` 函数。

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

**提示**

对于以下情况，指定的断点数据类型可以不同于对应的输入数据类型：

- 存储断点数据（使用的类型小于输出信号）的内存要求较低
- 在具有不同输入数据类型的两个 n-D Lookup Table 模块之间共享预缩放的断点数据
- 在为具有不同输入数据类型的模块生成的代码中共享自定义存储断点数据

如果断点数据类型或其对应的输入数据类型具有定点数据类型，请为二者指定相同的斜率和偏置。

##### 依赖关系

要启用此参数，请将**表和断点**选项卡中对应的**断点**参数设置为**对话框**。

##### 编程用法

|  |
| --- |
| **模块参数**：`BreakpointsForDimension1DataTypeStr | BreakpointsForDimension2DataTypeStr| ... | BreakpointsForDimension30DataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Same as corresponding input' | 'Inherit: Inherit from 'Breakpoint data'' | 'double' | 'single' | 'half' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)'|'<data type expression>'` |
| **默认值：**`'Inherit: Same as corresponding input'` |

#### **断点最小值** — 最小值断点数据可以有 `[]` | `scalar`

指定一组断点数据可以具有的最小值。默认值为 `[]`（未指定）。

##### 编程用法

|  |
| --- |
| **模块参数**：`BreakpointsForDimension1Min | BreakpointsForDimension2Min | ... | BreakpointsForDimension30Min` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'[]'` |

#### **断点最大值** — 最大值断点数据可以有 `[]` | `scalar`

指定一组断点数据可以具有的最大值。默认值为 `[]`（未指定）。

##### 编程用法

|  |
| --- |
| **模块参数**：`BreakpointsForDimension1Max | BreakpointsForDimension2Max | ... | BreakpointsForDimension30Max` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'[]'` |

#### **区间比** — 区间比数据类型 **继承: 从内部规则继承** (默认) | **double** | **single** | **fixdt(1,16,0)** | **<数据类型表达式>**

指定区间比数据类型。可以将其设置为：

- 继承数据类型的规则，例如**继承: 从内部规则继承**
- 内置数据类型的名称，例如 `single`
- 数据类型对象的名称，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`FractionDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Inherit via internal rule' | 'double' | 'single' | 'fixdt(1,16,0)'|'<data type expression>'` |
| **默认值：**`'Inherit: Inherit via internal rule'` |

#### **中间结果** — 中间结果数据类型 **继承: 与输出相同** (默认) | **继承: 从内部规则继承** | **double** | `single` | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16,0)** | **fixdt(1,16,2^0,0)** | **<数据类型表达式>**

指定中间结果数据类型。可以将其设置为：

- 继承数据类型的规则，例如**继承: 与输出相同**
- 内置数据类型的名称，例如 `single`
- 数据类型对象的名称，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

**提示**

使用此参数为内部计算指定高于（或低于）表数据或输出数据的精度。

##### 编程用法

|  |
| --- |
| **模块参数**：`IntermediateResultsDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Inherit via internal rule' | 'Inherit: Same as output' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)'|'<data type expression>'` |
| **默认值：**`'Inherit: Same as output'` |

#### **输出** — 输出数据类型 **继承: 与输入相同** (默认) | **double** | **single** | **half** | `int8` | `uint8` | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | `fixdt(1,16)` | **fixdt(1,16,0)** | **fixdt(1,16,2^0,0)** | `<data type expression>`

指定输出数据类型。可以将其设置为：

- 继承数据类型的规则，例如**继承: 通过反向传播继承**
- 内置数据类型的名称，例如 `single`
- 数据类型对象的名称，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Inherit via back propagation' | 'Inherit: Inherit from table data' | 'Inherit: Same as first input' | 'double' | 'single' | 'half' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)'|'<data type expression'` |
| **默认值：**`'Inherit: Same as first input'` |

#### **输出最小值** — 范围检查的最小值 `[]` | `scalar`

指定范围检查的最小值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutMin` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'[]'` |

#### **输出最大值** — 范围检查的最大值 `[]` | `scalar`

指定范围检查的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'[]'` |

#### **内部规则优先级** — 进行中间计算的内部规则 **速度** (默认) | **精度**

指定进行中间计算的内部规则。选择**速度**可以提高计算速度。但这样可能会损失精度，通常最多 2 位。

##### 依赖关系

仅当**中间结果**或**小数**参数设置为以下值时，此参数才生效：**继承:从内部规则继承**。

##### 编程用法

|  |
| --- |
| **模块参数**：`InternalRulePriority` |
| **类型：**字符向量 |
| **值：**`'Speed' | 'Precision'` |
| **默认值：**`'Speed'` |

#### **要求所有输入具有相同的数据类型** — 要求所有输入具有相同的数据类型 `on` (默认) | `off`

选中此项会要求所有输入具有相同的数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`InputSameDT` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'on'` |

#### **锁定数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您对此模块指定的数据类型。有关详细信息，请参阅Lock the Output Data Type Setting (Fixed-Point Designer)。

##### 编程用法

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **整数舍入模式** — 定点运算的舍入模式 **最简** (默认) | **向上** | **收敛** | **向下** | **最邻近值** | **舍入** | **零**

指定在仿真过程中或在执行从模型中生成的代码时发生的定点查找表计算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

此选项不影响模块参数值的舍入。Simulink 将此类值舍入到最邻近的可表示整数值。要控制模块参数的舍入方法，请使用 MATLAB® 舍入函数在模块对话框上的编辑字段中输入表达式。

##### 编程用法

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型：**字符向量 |
| **值：**`'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认值：**`'Simplest'` |

#### **对整数溢出进行饱和处理** — 溢出操作的方法 `off` (默认) | `on`

| 操作 | 执行此操作的原因 | 溢出时会发生的情况 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框 (`on`)。 | 您的模型可能有溢出，并且您希望在生成的代码中具有显式饱和保护。 | 将溢出饱和处理为数据类型能够表示的最小值或最大值。 | 一个有符号的 8 位整数的溢出可以饱和处理为 -128 或 127。 |
| 不选中此复选框 (`off`)。 | 您需要优化所生成代码的效率。  您希望避免过度地指定信号超出范围时的处理方式。有关详细信息，请参阅信号范围错误故障排除。 | 溢出会绕回到由数据类型表示的适当值。 | 数字 130 不适合一个有符号 8 位整数，因此绕回 -126。 |

**提示**

如果您将模型保存为 R2009a 或更早版本，此复选框设置将不起作用，且不会显示饱和代码。此行为保留了向后兼容性。

如果选中此复选框，饱和将应用于模块中的每个内部操作，而不仅仅应用于输出或结果。一般情况下，代码生成进程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

##### 编程用法

|  |
| --- |
| **模块参数**：`SaturateOnIntegerOverflow` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。有关 2-D Lookup Table 模块的 HDL 代码生成支持的信息，请参阅 HDL 代码生成。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2011a 中推出**

#### R2025a: 2-D Lookup Table 模块的**删除生成代码中防止超范围输入的代码**参数被取代

**删除生成代码中防止超范围输入的代码**参数已被**假设输入在范围内**取代。编程名称 `RemoveProtectionInput` 保持不变。

如果模型仿真因将超出范围的输入馈送到选中**假设输入在范围内**的模块而生成错误，则当生成的代码在执行期间出现相同的超出范围的输入时，该模型生成的代码具有未定义的行为。这种未定义的行为可能导致严重问题。对于安全性至关重要的应用，请不要选择**删除生成代码中防止超范围输入的代码**。

在 R2025a 之前的版本中，**删除生成代码中防止超范围输入的代码**仅会删除生成代码中对超出范围值的代码检查。模块无法检测到这些问题。作为解决方法，如果您有 R2025a 之前版本的模型且无法迁移到更高版本，请将**输入超出范围的诊断**参数设置为**错误**。下次运行模型时，当输入超出范围时将生成错误。

#### R2024b: 使用**尽可能应用更准确高效的舍入**以获得更高的精度

为了在获得更高精度的同时尽可能不增加性能开销，请使用**尽可能应用更准确高效的舍入**参数。要启用此参数，请进行如下设置：

- 将**内插方法**设置为**线性点-斜率**。
- 将**外插方法**设置为**裁剪**。

#### R2024b: **在代码生成中支持可调表大小**参数替换为**支持可调大小**

在 Lookup Table 模块中，**在代码生成中支持可调表大小**参数已替换为**支持可调表大小**。此变更造成的影响是：

- 如果您使用 `SupportTunableTableSize` 以编程方式设置**表和断点** > **支持可调大小**参数，则下次打开 Lookup Table 模块时，该模块将显示一条警告。现有模型继续正常工作。
- **表和断点**选项卡上的**支持可调大小**参数取代了**算法**选项卡上的**在代码生成中支持可调表大小**和**每个维度的最大索引**参数。在 R2024b 之前，选择**在代码生成中支持可调表大小**参数将启用**每个维度的最大索引**参数，该参数设置每个表维度的最大索引值。从 R2024b 开始，选择**支持可调大小**参数将为**断点**参数启用**可调大小**字段。这些**可调大小**字段取代了**每个维度的最大索引**参数的功能。模块在模块对话框中显示警告。现有模型继续正常工作。有关详细信息，请参阅可调大小。

## Libraries

Simulink / Lookup Tables HDL Coder / Lookup Tables

## Description

### Supported Block Operations

The 1-D, 2-D, and n-D Lookup Table blocks evaluate a sampled representation of a function in N
variables

y=F(x1,x2,x3,...,xN)

where the function *F* can be empirical. The block maps inputs to an output
value by looking up or interpolating a table of values you define with block parameters. The
block supports flat (constant), linear (linear point-slope), Lagrange (linear Lagrange),
nearest, cubic-spline, and Akima spline interpolation methods. You can apply these methods to
a table of any dimension from 1 through 30.

In the following block, the first input identifies the first dimension (row) breakpoints, the second input identifies the second dimension (column) breakpoints, and so on.

See Identify Port Location on Rotated or Flipped Block for a description of the port order for various block orientations.

When the **Math and Data Types** > **Use algorithms optimized for row-major array layout** configuration parameter is set, the 2-D and n-D Lookup Table block behavior
changes from column-major to row-major. For these blocks, the column-major and row-major
algorithms may differ in the order of the output calculations, possibly resulting in slightly
different numerical values. This capability requires a Simulink®
Coder™ or Embedded Coder® license. For more information on row-major support, see Code Generation of Matrices and Arrays (Simulink Coder).

### Specification of Breakpoint and Table Data

These block parameters define the breakpoint and table data.

| Block Parameter | Purpose |
| --- | --- |
| **Number of table dimensions** | Specifies the number of dimensions of your lookup table. |
| **Breakpoints** | Specifies a breakpoint vector that corresponds to each dimension of your lookup table. |
| **Table data** | Defines the associated set of output values. |

**Tip**

Evenly spaced breakpoints can make the generated code division-free. For more information, see `fixpt_evenspace_cleanup` and Identify questionable fixed-point operations (Embedded Coder).

### How the Block Generates Output

The n-D, 1-D and 2-D Lookup Table blocks generate output by looking up or estimating table
values based on the input values.

| Block Inputs | n-D Lookup Table Block Behavior |
| --- | --- |
| Match the values of indices in breakpoint vectors | Outputs the table value at the intersection of the row, column, and higher dimension breakpoints |
| Do not match the values of indices in breakpoint vectors, but are within range | Interpolates appropriate table values, using the **Interpolation method** you select |
| Do not match the values of indices in breakpoint vectors, and are out of range | Extrapolates the output value, using the **Extrapolation method** you select |

### Other Blocks That Perform Equivalent Operations

You can use the Interpolation Using Prelookup block with the Prelookup block to perform the equivalent operation of one n-D Lookup Table block. This combination of blocks offers greater flexibility that can result in more efficient simulation performance for linear interpolations.

When the lookup operation is an array access that does not require interpolation, use the Direct Lookup Table (n-D) block. For example, if you have an integer value `k` and you want the `k`th element of a table, `y = table(k)`, interpolation is unnecessary.

## Ports

### Input

### **u1** — First-dimension (row) inputs scalar | vector | matrix

Real-valued inputs to the **u1** port, mapped to an output value
by looking up or interpolating the table of values that you define.

**Example:** `0:10`

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `enumerated` | `fixed point`

### **u2** — Second-dimension (column) inputs scalar | vector | matrix

Real-valued inputs to the **u2** port, mapped to an output value
by looking up or interpolating the table of values that you define.

**Example:** `0:10`

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `enumerated` | `fixed point`

### **T** — Define the table of output values matrix of values with dimensions that match the **Number of table dimensions** and the breakpoint lengths for each dimension of the table

Specify the table of output values with a signal that is tunable at
runtime.

During simulation, the matrix size must match the dimensions defined by the
**Number of table dimensions** parameter and the breakpoint lengths
for each dimension of the table. However, during block diagram editing, you can enter
an empty matrix (specified as `[]`) or an undefined workspace
variable. This technique lets you postpone specifying a correctly dimensioned matrix
for the table data and continue editing the block diagram.

#### Dependencies

To enable this port, set:

- **Data specification** to `Table and
  breakpoints`.
- **Table data** to `Input
  port`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **bp1** — Explicit breakpoint values 1-by-n or n-by-1 vector of monotonically increasing values

Specify the breakpoint data explicitly, based on the value of the
**Breakpoints specification** parameter, with a signal that is
tunable at runtime.

- If you set **Breakpoints specification** to
  `Explicit values`, enter the breakpoint vector that
  corresponds to each dimension of table data in each
  **Breakpoints** row. For each dimension, specify breakpoints as
  a 1-by-n or n-by-1 vector whose values are strictly monotonically
  increasing.

**Note**

To specify breakpoints in the even spacing specification format, set
**Breakpoints specification** to `Even
spacing` and use the **Breakpoints First** point and
**Spacing** parameters.

#### Dependencies

To enable this port, set:

- **Data specification** to `Table and
  breakpoints`.
- **Breakpoints specification** to `Explicit
  values`.
- **Breakpoints 1** to `Input
  port`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `enumerated` | `fixed point`

### **bp2** — Explicit breakpoint values 1-by-n or n-by-1 vector of monotonically increasing values

Specify the breakpoint data explicitly, based on the value of the
**Breakpoints specification** parameter, with a signal that is
tunable at runtime.

- If you set **Breakpoints specification** to
  `Explicit values`, enter the breakpoint vector that
  corresponds to each dimension of table data in each
  **Breakpoints** row. For each dimension, specify breakpoints as
  a 1-by-n or n-by-1 vector whose values are strictly monotonically
  increasing.

**Note**

To specify evenly spaced breakpoint data, use the
**Breakpoints** parameter. You cannot specify evenly spaced
breakpoint data through the input port.

#### Dependencies

To enable this port, set:

- **Data specification** to `Table and
  breakpoints`.
- **Breakpoints specification** to `Explicit
  values`.
- **Breakpoints 2** to `Input
  port`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `enumerated` | `fixed point`
### Output

### **Port\_1** — Output computed by looking up or estimating table values scalar | vector | matrix

Output generated by looking up or estimating table values based on the input
values.

| When block inputs... | The n-D Lookup Table block... |
| --- | --- |
| Match the values of indices in breakpoint vectors | Outputs the table value at the intersection of the row, column, and higher dimension breakpoints |
| Do not match the values of indices in breakpoint vectors, but are within range | Interpolates appropriate table values, using the **Interpolation method** you select |
| Do not match the values of indices in breakpoint vectors, and are out of range | Extrapolates the output value, using the **Extrapolation method** you select |

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### Table and Breakpoints

### **Number of table dimensions** — Number of lookup table dimensions `2` (default) | `1` | `3` | `4` | `...` | `30`

Enter the number of dimensions of the lookup table. This parameter
determines:

- The number of independent variables for the table and the
  number of block inputs
- The number of breakpoint vectors to specify

| To specify... | Do this... |
| --- | --- |
| 1, 2, 3, or 4 | Select the value from the drop-down list. |
| A higher number of table dimensions | Enter a positive integer directly in the field.  The maximum number of table dimensions that this block supports is 30. |

For example, a table with a size of *M* x
*N* x ... means that the size of dimension 1 is
*M*, the size of dimension 2 is
*N*, and so forth. *M* must match
the first breakpoint length, *N* must match the second
breakpoint length, and so forth.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumberOfTableDimensions` |
| **Type:** character vector |
| **Values:** `'1' | '2' | '3' | '4' | ... | 30` |
| **Default:** `'2'` |

### **Data specification** — Method of table and breakpoint specification `Table and breakpoints` (default) | `Lookup table object`

From the list, select:

- `Table and breakpoints` —
  Specify the table data and breakpoints. Selecting this option
  enables these parameters:

  - **Table data**
  - **Breakpoints
    specification**
  - **Breakpoints 1**
  - **Breakpoints 2**
  - **Edit table and
    breakpoints**

  To specify the table and breakpoints using input ports, see
  the **Source** parameter.
- `Lookup table object` — Use an
  existing lookup table (`Simulink.LookupTable`) object. Selecting this
  option enables the **Name** field and
  **Edit table and breakpoints**
  button.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataSpecification` |
| **Type:** character vector |
| **Values:** `'Table and breakpoints' | 'Lookup table object'` |
| **Default:** `'Table and breakpoints'` |

To set this parameter from `'Table and
breakpoints'` to `'Lookup table
object'`, use the same `set_param`
call to set the `LookupTableObject` parameter. For
example:

```
set_param('myModel/myLookupBlock',...
   'DataSpecification','Lookup table object',...
   'LookupTableObject','myLUTObject')
```

### **Name** — Name of the lookup table object `[]` (default) | `Simulink.LookupTable` object

Enter the name of the lookup table
(`Simulink.LookupTable`) object. If a
`Simulink.LookupTable` object does not exist, click
the action button  and select
**Create**. The corresponding parameters of the
new lookup table object are automatically populated with the block
information.

#### Dependencies

To enable this parameter, set **Data
specification** to `Lookup table
object`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LookupTableObject` |
| **Type:** character vector |
| **Values:** name of a `Simulink.LookupTable` object |
| **Default:** `''` |

### **Breakpoints specification** — Method of breakpoint specification `Explicit values` (default) | `Even spacing`

Specify whether to enter data as explicit breakpoints or as parameters
that generate evenly spaced breakpoints.

- To explicitly specify breakpoint data, set this parameter to
  `Explicit values` and enter
  breakpoint data in the text box next to the
  **Breakpoints** parameters.
- To specify parameters that generate evenly spaced breakpoints,
  set this parameter to `Even spacing`
  and enter values for the **First point** and
  **Spacing** parameters for each dimension
  of breakpoint data. The block calculates the number of points to
  generate from the table data.

#### Dependencies

To enable this parameter, set **Data
specification** to `Table and
breakpoints`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsSpecification` |
| **Type:** character vector |
| **Values:** `'Explicit values' | 'Even spacing'` |
| **Default:** `'Explicit values'` |

### **Support tunable size** — Option to enable tunable table size `off` (default) | `on`

Select this check box to enable tunable table sizing of the active
region while the simulation is running or the generated code is
executing. This option enables the software to work properly
even if you change the size of the active region and values of
the lookup table and breakpoint data while the generated code is
executing. The table size must be 2 or greater and less than the
maximum tunable size.

#### Dependencies

If you set **Interpolation method** to `Cubic spline` or `Akima spline`, **Support tunable size** is not available.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SupportTunableSize` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Source** — Source of table and breakpoint data `Dialog` (default) | `Input port`

Source of table and breakpoint data, specified as:

- `Dialog` — Specify the table or
  breakpoint data in **Value** parameter.
- `Input port` — Specify the table or
  breakpoint data through the associated input port. Through the
  input port, you can specify only up to three sets of breakpoint
  data. To specify breakpoint data above three, use the
  **Value** parameter.

**Note**

Using the input port to specify table or breakpoint data might
negatively affect block performance for simulation due to runtime
checks. To model dynamics that require breakpoints to change during
simulation, select `Dialog` and change the
breakpoint data using the Parameter Writer block.

#### Dependencies

- To enable this parameter, set **Data
  specification** to `Table and
  breakpoints`.
- To enable the associated **Value**, set
  this parameter to `Dialog`.
- To enable the associated input port, set this parameter to
  `Input port`.
- Setting this parameter to `Input
  port` disables the
  **Value** field and hides the
  corresponding parameter on the **Data
  Types** tab.
- Setting this parameter to `Input
  port` for any one of the parameters
  disables the **Edit Table and Breakpoints**
  button.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableSource` | `BreakpointsForDimension1Source` | `BreakpointsForDimension2Source` | `BreakpointsForDimension3Source` |
| **Type:** character vector |
| **Values:** `Dialog` | `Input port` |
| **Default:** `'Dialog'` |

### **Tunable size** — Maximum number of elements for each array `-1` (default) | real integer scalar

Specify the maximum size of each array as one of these values:

- `-1` — All of the elements in the array
- Real integer scalar — Maximum number of elements for each array

**Tunable size** must be less than or equal to the size of the
array.

#### Dependencies

To enable this parameter:

- Set **Data specification** to `Table and breakpoints`.
- Select the **Support tunable size** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `N1` to `N31` |
| **Type:** character vector |
| **Values:** `-1` | real integer scalar |
| **Default:** `-1` |

### **Table data** — Define the table of output values `[4 5 6; 16 19 20; 10 18 23]` (default) | matrix of values

Enter the table of output values in the associated
**Value** field.

During simulation, the matrix size must match the dimensions defined
by the **Number of table dimensions** parameter.
However, during block diagram editing, you can enter an empty matrix
(specified as `[]`) or an undefined workspace variable.
This technique lets you postpone specifying a correctly dimensioned
matrix for the table data and continue editing the block diagram.

#### Dependencies

To enable this parameter, set:

- **Data specification** to
  `Table and
  breakpoints`.
- **Table data: Source** to
  `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Table` |
| **Type:** character vector |
| **Values:** matrix of table values |
| **Default:** `'[4 5 6; 16 19 20; 10 18 23]'` |

### **Breakpoints** — Explicit breakpoint values, or first point and spacing of breakpoints `[1:3]` (default) | 1-by-n or n-by-1 vector of monotonically increasing values

Specify the breakpoint data explicitly or as evenly-spaced
breakpoints, based on the value of the **Breakpoints
specification** parameter.

- If you set **Breakpoints specification** to
  `Explicit values`, enter the
  breakpoint vector that corresponds to each dimension of table
  data in each **Breakpoints** row in the
  associated **Value** field. For each dimension,
  specify breakpoints as a 1-by-n or n-by-1 vector whose values
  are strictly monotonically increasing.
- If you set **Breakpoints specification** to
  `Even spacing`, enter the
  parameters **First point** and
  **Spacing** in each
  **Breakpoints** row to generate
  evenly-spaced breakpoints in the respective dimension. Your
  table data determines the number of evenly spaced points.

#### Dependencies

- To enable this parameter, set

  - **Data specification** to
    `Table and
    breakpoints`.
  - **Breakpoints: Source** to
    `Dialog`.
- When the **Breakpoints specification**
  parameter is set to `Even spacing`,
  you can only specify breakpoints data through the dialog
  box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsForDimension1` |
| **Type:** character vector |
| **Values:** 1-by-n or n-by-1 vector of monotonically increasing values |
| **Default:** `'[1:3]'` |

### **First point** — First point in evenly spaced breakpoint data `1` (default) | scalar

Specify the first point in your evenly spaced breakpoint data as a
real-valued, finite, scalar. This parameter is available when
**Breakpoints specification** is set to
`Even spacing`.

#### Dependencies

To enable this parameter, set **Data
specification** to `Table and
breakpoints`, and **Breakpoints
specification** to `Even
spacing`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsForDimension1FirstPoint | BreakpointsForDimension2FirstPoint` |
| **Type:** character vector |
| **Values:** real-valued, finite, scalar |
| **Default:** `'1'` |

### **Spacing** — Spacing between evenly spaced breakpoints `1` (default) | scalar

Specify the spacing between points in your evenly-spaced breakpoint
data.

#### Dependencies

To enable this parameter, set **Data
specification** to `Table and
breakpoints`, and **Breakpoints
specification** to `Even
spacing`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsForDimension1Spacing | BreakpointsForDimension2Spacing` |
| **Type:** character vector |
| **Values:** positive, real-valued, finite, scalar |
| **Default:** `'1'` |

### **Edit table and breakpoints** — Launch Lookup Table Editor dialog box button

Click this button to open the Lookup Table Editor. For more
information, see Lookup Table Editor.

Clicking this button for a lookup table object lets you edit the
object and save the new values for the object.

### Algorithm

#### Lookup method

### **Interpolation method** — Method of interpolation between breakpoint values `Linear point-slope` (default) | `Flat` | `Nearest` | `Linear Lagrange` | `Cubic spline` | `Akima spline`

When an input falls between breakpoint values, the block interpolates the output value using neighboring breakpoints. For more information on interpolation methods, see Interpolation Methods.

#### Dependencies

- If you select `Cubic spline`, the block
  supports only scalar signals. The other interpolation methods
  support nonscalar signals.
- If you select `Akima spline`, the
  extrapolation method can only be `Akima
  spline`.

  When set to the modified Akima interpolation method, this block
  does not support:

  - Row-major array layout and algorithms optimized for
    row-major array layout
  - Scaled double and fixed-point data types
  - `Simulink.LookupTable` objects
  - Code generation when the configuration parameter **Code Generation** > **Interface** > **Support non-finite numbers** check box is selected

  When set to the modified Akima interpolation method, this block is
  known to run more slowly when these conditions are true:

  - Code generation-based simulation targets, such as those
    for accelerator mode, rapid accelerator mode, protected
    models, and so forth.
  - Code generated for large breakpoint and data table sizes.
    For example with a table size of 629x1601.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InterpMethod` |
| **Type:** character vector |
| **Values:** `'Linear point-slope' | 'Flat' | 'Nearest' | 'Linear Lagrange' | 'Cubic spline' | 'Akima spline'` |
| **Default:** `'Linear point-slope'` |

### **Extrapolation method** — Method of handling input values that fall outside the range of a breakpoint vector `Linear` (default) | `Clip` | `Cubic spline` | `Akima spline`

Select `Clip`, `Linear`, or
`Cubic spline`. See Extrapolation Methods for more
information.

If the extrapolation method is `Linear`, the
extrapolation value is calculated based on the selected linear interpolation
method. For example, if the interpolation method is linear Lagrange, the
extrapolation method inherits the linear Lagrange equation to compute the
extrapolated value.

#### Dependencies

- To select `Cubic spline` for
  **Extrapolation method**, you must also select
  `Cubic spline` for
  **Interpolation method**.
- To select `Akima spline` for
  **Extrapolation method**, you must also select
  `Akima spline` for
  **Interpolation method**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ExtrapMethod` |
| **Type:** character vector |
| **Values:** `'Linear' | 'Clip' | 'Cubic spline' | 'Akima spline'` |
| **Default:** `'Linear'` |

### **Index search method** — Method of calculating table indices `Binary search` (default) | `Linear search` | `Evenly spaced points`

Select `Evenly spaced points`, `Linear
search`, or `Binary search`. Each
search method has speed advantages in different circumstances:

- For evenly spaced breakpoint vectors (for example, 10, 20, 30, and so
  on), you achieve optimal speed by selecting `Evenly spaced
  points` to calculate table indices.

  This algorithm uses only the first two breakpoints of a set to
  determine the offset and spacing of the remaining points.

  **Note**

  Set **Index search method** to
  `Evenly spaced points` when using the
  `Simulink.LookupTable` object to specify table
  data and the **Breakpoints Specification**
  parameter of the referenced `Simulink.LookupTable`
  object is set to `Even spacing`.
- For unevenly spaced breakpoint vectors, follow these
  guidelines:

  - If input signals do not vary much between time steps,
    selecting `Linear search` with
    **Begin index search using previous index
    result** produces the best performance.
  - If input signals jump more than one or two table intervals per
    time step, selecting `Binary search`
    produces the best performance.

A suboptimal choice of index search method can lead to slow performance of models that rely heavily on lookup tables.

**Note**

The generated code stores only the first breakpoint, the spacing, and the number of breakpoints when:

- The breakpoint data is not tunable.
- The index search method is `Evenly spaced
  points`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IndexSearchMethod` |
| **Type:** character vector |
| **Values:** `'Binary search' | 'Evenly spaced points' | 'Linear search'` |
| **Default:** `'Binary search'` |

### **Apply more accurate and efficient rounding when possible** — More accurate fixed-point table lookup using efficient round to nearest `off` (default) | `on`

Select this check box to enable an efficient round to nearest implementation
when possible. Enabling this option sets the rounding mode to
`Nearest` and adjusts the fraction lengths and intermediate
data types to offer a balance between accuracy and efficiency. If an efficient
implementation is not possible, the rounding mode, fraction lengths and
intermediate data types remain unchanged.

#### Dependencies

To enable this parameter:

- Set **Number of table dimensions** to
  `2`.
- Set **Interpolation method** to
  `Linear point-slope`.
- Set **Extrapolation method** to
  `Clip`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ApplyAccurateEfficientRounding` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Begin index search using previous index result** — Start using the index from the previous time step `off` (default) | `on`

Select this check box when you want the block to start its search using the index found at the
previous time step. For inputs that change slowly with respect to the interval
size, enabling this option can improve performance. Otherwise, the linear search
and binary search methods can take longer, especially for large breakpoint
vectors.

#### Dependencies

To enable this parameter, set **Index search method** to `Linear search` or `Binary search`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BeginIndexSearchUsingPreviousIndexResult` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Assume input is within range** — Option to check for out-of-range input values `off` (default) | `on`

*Since R2025a*

Specify whether or not to include code that checks for out-of-range input values.
Selecting this parameter means that you guarantee that the block has no out-of-range
inputs, enabling the block to further optimize the code and simulation. The valid input
range depends on the breakpoint data and the **Extrapolation method**
setting.

When you select **Assume input is within range**:

- During simulation, the block assumes that there are no out-of-range inputs and
  enforces this assumption by returning an error for out-of-range inputs.
- For code generation, the block does not generate out-of-range input handling
  code because it assumes there is no out-of-range input. This means that if the
  block tries to generate code for a model that returns an error because of
  out-of-range inputs, when the generated code is given the same input, the
  behavior is undefined, which can lead to severe consequence.

  **Warning**

  If the model tries to generate code and instead generates an error
  because the block detects out-of-range input, the behavior is undefined
  if the same out-of-range input is passed to deployed code. This
  undefined behavior might cause severe issues. For safety critical
  applications, do not select **Assume input is within
  range**.

If you want to select the **Assume input is within range** parameter
for efficiency, ensure that your model inputs are in range. For example:

| Parameter | Result | When to Use |
| --- | --- | --- |
| `on` | Simulation and generated code does not include conditional statements to check for out-of-range breakpoint inputs.  When the input is out-of-range, it may cause undefined behavior for simulation and generated code. | For simulation and code efficiency |
| `off` | Simulation and generated code includes conditional statements to check for out-of-range inputs. | For safety-critical applications |

If you are confident your input is within range, you can select the **Assume
input is within range** parameter for efficiency. By default, this
parameter is cleared. For safety-critical applications, do not select this parameter. If
you want to select the **Assume input is within range** parameter,
first check that your model inputs are in range. For example:

1. Clear the **Assume input is within range** parameter.
2. Set the **Diagnostic for out-of-range input** parameter to
   `Error`.
3. Simulate the model in normal mode.
4. If there are out-of-range errors, the block returns runtime errors. Fix them
   to be in range and run the simulation again.
5. When the simulation no longer generates out-of-range input errors, select the
   **Assume input is within range** parameter.

   **Note**

   When you select the **Assume input is within range**
   parameter and the input is out of range, the block returns a runtime error
   at simulation. The behavior is undefined for generated code.

Depending on your application, you can run the following Model Advisor checks to
verify the usage of this parameter:

- **By Product** > **Embedded Coder** > **Identify lookup table blocks that generate expensive
  out-of-range checking code**
- **By Product** > **Simulink Check** > **Modeling Standards** > **DO-178C/DO-331 Checks** > **Check usage of lookup table blocks**

For more information about the Model Advisor, see Run Model Advisor Checks.

Additionally, to determine if it is safe to select this parameter, if you have a
Simulink
Design Verifier™ license, consider using the Detect Block Input Range Violations (Simulink Design Verifier) check.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RemoveProtectionInput` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Diagnostic for out-of-range input** — Block action when input is out of range `None` (default) | `Warning` | `Error`

Specify whether to produce a warning or error when the input is out of range. Options include:

- `None` — Produce no response.
- `Warning` — Display a warning and continue the simulation.
- `Error` — Terminate the simulation and display an error.

#### Dependencies

To enable this parameter, clear the **Assume input is within
range** or **Assume index is within range**
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DiagnosticForOutOfRangeInput` |
| **Type:** character vector |
| **Values:** `'None' | 'Warning' | 'Error'` |
| **Default:** `'None'` |

### **Apply full precision fixed-point algorithm when possible** — More accurate fixed-point table lookup `off` (default) | `on`

Use this check box to enable full-precision fixed-point algorithm lookup for
linear interpolation lookup when possible. This algorithm generally achieves
better precision for hardware-efficient fixed-point rounding modes.

#### Dependencies

To enable this parameter, set:

- **Number of table dimensions** to
  `1`.
- **Interpolation method** to `Linear
  point-slope`.
- **Extrapolation method** to
  `Clip`.
- Select the **Use last table value for inputs at or above
  last breakpoint** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ApplyFullPrecisionForLinearInterpolation` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Use last table value for inputs at or above last breakpoint** — Method for computing output for inputs at or above last breakpoint `off` (default) | `on`

Using this check box, specify the indexing convention that the block uses to address the last
element of a breakpoint vector and its corresponding table value. This check box
is relevant if the input is equal to or larger than the last element of the
breakpoint data. Due to rounding, selecting and clearing this check box may
result in differing results for the last breakpoint between simulation and code
generation.

| Check Box | Index Used by Block | Interval Fraction |
| --- | --- | --- |
| Selected | Last element of breakpoint data on the **Table and Breakpoints** tab | 0 |
| Cleared | Next-to-last element of breakpoint data on the **Table and Breakpoints** tab | 1 |

Given an input *u* within range of a breakpoint vector *bp*,
the interval fraction *f*, in the range
0≦*f*<1, is computed as shown below.

Suppose the breakpoint vector is `[1 4 5]` and
input *u* is `5.5`. If you select this check
box, the index is that of the last element (`5`) and the
interval fraction is 0. If you clear this check box, the index is that of the
next-to-last element (`4`) and the interval fraction is
1.

#### Dependencies

To enable this parameter, set:

- **Interpolation method** to `Linear`.
- **Extrapolation method** to `Clip`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UseLastTableValue` |
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

#### Input settings

### **Use one input port for all input data** — Use only one input port `off` (default) | `on`

Select this check box to use only one input port that expects a signal that is
`n` elements wide for an n-dimensional table. This option
is useful for removing line clutter on a block diagram with many lookup
tables.

**Note**

When you select this check box, one input port with the label
`u` appears on the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UseOneInputPortForAllInputData` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### Data Types

### **Table data** — Data type of table data `Inherit: Same as output` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the table data type. You can set it to:

- A rule that inherits a data type, for example, `Inherit:
  Same as output`
- The name of a built-in data type, for example,
  `single`
- The name of a data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

**Tip**

Specify a table data type different from the output data type for these
cases:

- Lower memory requirement for storing table data that uses a
  smaller type than the output signal
- Sharing of prescaled table data between two n-D Lookup
  Table blocks with different output data types
- Sharing of custom storage table data in the generated code for
  blocks with different output data types

#### Dependencies

To enable this parameter, set **Table data** from the
**Table and Breakpoints** tab to
`Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit from 'Table data'' | 'Inherit: Same as output' | 'double' | 'single' | 'half' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)'|'<data type expression>'` |
| **Default:** `'Inherit: Same as output'` |

### **Table data Minimum** — Minimum value of the table data `[]` | `scalar`

Specify the minimum value for table data. The default value is `[]` (unspecified).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableMin` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Table data Maximum** — Maximum value of the table data `[]` | `scalar`

Specify the maximum value for table data. The default value is `[]` (unspecified).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableMax` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Breakpoints** — Breakpoint data type `Inherit: Same as corresponding input` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

Specify the data type for a set of breakpoint data. You can set it to:

- A rule that inherits a data type, for example, `Inherit:
  Same as corresponding input`
- The name of a built-in data type, for example,
  `single`
- The name of a data type class, for example, an enumerated data type
  class
- The name of a data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

**Tip**

- Breakpoints support unordered enumerated data. As a result, linear
  searches are also unordered, which offers flexibility but can impact
  performance. The search begins from the first element in the
  breakpoint.
- If the **Begin index search using previous index
  result** check box is selected, you must use ordered
  monotonically increasing data. This ordering improves
  performance.
- For enumerated data, **Extrapolation method**
  must be `Clip`.
- The block does not support out-of-range input for enumerated data.
  When specifying enumerated data, include the entire enumeration set
  in the breakpoint vector. For example, use the `enumeration`
  function.

This is a limitation for using enumerated data with this block:

- The block does not support out-of-range input for enumerated data.
  When specifying enumerated data, include the entire enumeration set in
  the breakpoint vector. For example, use the `enumeration`
  function.

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

**Tip**

Specify a breakpoint data type different from the corresponding input data
type for these cases:

- Lower memory requirement for storing breakpoint data that uses a
  smaller type than the input signal
- Sharing of prescaled breakpoint data between two n-D Lookup
  Table blocks with different input data types
- Sharing of custom storage breakpoint data in the generated code
  for blocks with different input data types

Specify the same slope and bias for a breakpoint data type and its
corresponding input data type if either of them has a fixed-point data type.

#### Dependencies

To enable this parameter, set the corresponding
**Breakpoints** parameter from the **Table and
Breakpoints** tab to `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsForDimension1DataTypeStr | BreakpointsForDimension2DataTypeStr| ... | BreakpointsForDimension30DataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Same as corresponding input' | 'Inherit: Inherit from 'Breakpoint data'' | 'double' | 'single' | 'half' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)'|'<data type expression>'` |
| **Default:** `'Inherit: Same as corresponding input'` |

### **Breakpoints Minimum** — Minimum value breakpoint data can have `[]` | `scalar`

Specify the minimum value that a set of breakpoint data can have. The default value is `[]` (unspecified).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsForDimension1Min | BreakpointsForDimension2Min | ... | BreakpointsForDimension30Min` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Breakpoints Maximum** — Maximum value breakpoint data can have `[]` | `scalar`

Specify the maximum value that a set of breakpoint data can have. The default value is `[]` (unspecified).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsForDimension1Max | BreakpointsForDimension2Max | ... | BreakpointsForDimension30Max` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Fraction** — Fraction data type `Inherit: Inherit via internal rule` (default) | `double` | `single` | `fixdt(1,16,0)` | `<data type expression>`

Specify the fraction data type. You can set it to:

- A rule that inherits a data type, for example, `Inherit:
  Inherit via internal rule`
- The name of a built-in data type, for example,
  `single`
- The name of a data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FractionDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'double' | 'single' | 'fixdt(1,16,0)'|'<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Intermediate results** — Intermediate results data type `Inherit: Same as output` (default) | `Inherit: Inherit via internal rule` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the intermediate results data type. You can set it to:

- A rule that inherits a data type, for example, `Inherit:
  Same as output`
- The name of a built-in data type, for example,
  `single`
- The name of a data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

**Tip**

Use this parameter to specify higher (or lower) precision for internal
computations than for table data or output data.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IntermediateResultsDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'Inherit: Same as output' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)'|'<data type expression>'` |
| **Default:** `'Inherit: Same as output'` |

### **Output** — Output data type `Inherit: Same as input` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the output data type. You can set it to:

- A rule that inherits a data type, for example, `Inherit:
  Inherit via back propagation`
- The name of a built-in data type, for example,
  `single`
- The name of a data type object, for example, a
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
| **Values:** `'Inherit: Inherit via back propagation' | 'Inherit: Inherit from table data' | 'Inherit: Same as first input' | 'double' | 'single' | 'half' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)'|'<data type expression'` |
| **Default:** `'Inherit: Same as first input'` |

### **Output Minimum** — Minimum value for range checking `[]` | `scalar`

Specify the minimum value for range checking. The default value is
`[]` (unspecified). Simulink software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters).
- Simulation range checking (see Specify Signal Ranges).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutMin` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Output Maximum** — Maximum value for range checking `[]` | `scalar`

Specify the maximum value for range checking. The default value is
`[]` (unspecified). Simulink software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters).
- Simulation range checking (see Specify Signal Ranges).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutMax` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Internal rule priority** — Internal rule for intermediate calculations `Speed` (default) | `Precision`

Specify the internal rule for intermediate calculations. Select `Speed` for faster calculations. If you do, a loss of accuracy might occur, usually up to 2 bits.

#### Dependencies

This parameter takes effect only when the **Intermediate
results** or **Fraction** parameter is set to
`Inherit: Inherit via internal rule`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InternalRulePriority` |
| **Type:** character vector |
| **Values:** `'Speed' | 'Precision'` |
| **Default:** `'Speed'` |

### **Require all inputs to have the same data type** — Require all inputs to have the same data type `on` (default) | `off`

Select to require all inputs to have the same data type.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputSameDT` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'on'` |

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types you specify on this block. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LockScale` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Simplest` (default) | `Ceiling` | `Convergent` | `Floor` | `Nearest` | `Round` | `Zero`

Specify the rounding mode for fixed-point lookup table calculations that occur during simulation or execution of code generated from the model. For more information, see Rounding Modes (Fixed-Point Designer).

This option does not affect rounding of values of block parameters. Simulink rounds such values to the nearest representable integer value. To control the rounding of a block parameter, enter an expression using a MATLAB® rounding function into the edit field on the block dialog box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **Default:** `'Simplest'` |

### **Saturate on integer overflow** — Method of overflow action `off` (default) | `on`

| Action | Reasons for Taking This Action | What Happens for Overflows | Example |
| --- | --- | --- | --- |
| Select this check box (`on`). | Your model has possible overflow and you want explicit saturation protection in the generated code. | Overflows saturate to either the minimum or maximum value that the data type can represent. | An overflow associated with a signed 8-bit integer can saturate to -128 or 127. |
| Do not select this check box (`off`). | You want to optimize efficiency of your generated code.  You want to avoid overspecifying how a block handles out-of-range signals. For more information, see Troubleshoot Signal Range Errors. | Overflows wrap to the appropriate value that is representable by the data type. | The number 130 does not fit in a signed 8-bit integer and wraps to -126. |

**Tip**

If you save your model as version R2009a or earlier, this check box setting has no effect and no saturation code appears. This behavior preserves backward compatibility.

When you select this check box, saturation applies to every internal operation on the block, not just the output or result. In general, the code generation process can detect when overflow is not possible. In this case, the code generator does not produce saturation code.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SaturateOnIntegerOverflow` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic. For information about HDL code generation
support for 2-D Lookup Table blocks, see HDL Code Generation.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2011a**

### R2025a: 2-D Lookup Table block **Remove protection against out-of-range input in generated code** parameter replaced

The **Remove protection against out-of-range input in generated code**
parameter has been replaced by **Assume input is within range**. The
programmatic name, `RemoveProtectionInput`, remains the same.

If the model simulation generates errors because the out-of-range input is fed to a block with
**Assume input is within range** selected, the code generated by the
model has undefined behavior when the same out-of-range input occurs during execution of the
generated code. This undefined behavior might cause severe issues. For safety critical
applications, do not select **Remove protection against out-of-range input in
generated code**.

In releases prior to R2025a, the **Remove protection against out-of-range input in
generated code** only removed the code checks for out-of-range values for
generated code. The block failed to detect these issues. As a workaround. if you have a
model from a release prior to R2025a and cannot migrate to a later release, set the
**Diagnostic for out-of-range input** parameter to
`Error`. The next time you run the model, an error is generated
when the input is out-of-range.

### R2024b: Use **Apply more accurate and efficient rounding when possible** for better accuracy

For better accuracy without performance overhead when possible, use the
**Apply more accurate and efficient rounding when possible**
parameter. To enable this parameter:

- Set **Interpolation method** to `Linear
  point-slope`.
- Set **Extrapolation method** to
  `Clip`.

### R2024b: **Support tunable table size in code generation** parameter replaced with **Support tunable size**

In lookup table blocks, the **Support tunable table size in code
generation** parameter has been replaced with **Support
tunable table size**. Due to this change:

- If you set the **Table and Breakpoints** > **Support tunable size** parameter programmatically with
  `SupportTunableTableSize`, the next time you open the
  lookup table block, the block displays a warning. Existing models continue
  to work.
- The **Support tunable size** parameter on the
  **Table and Breakpoints** tab replaces the
  **Support tunable table size in code generation** and
  **Maximum indices for each dimension** parameters on
  the **Algorithm** tab. Prior to R2024b, selecting the
  **Support tunable table size in code generation**
  parameter enabled the **Maximum indices for each
  dimension** parameter, which set the maximum index value for
  each table dimension. Starting in R2024b, selecting the **Support
  tunable size** parameter enables **Tunable
  Size** fields for the **Breakpoints**
  parameters. These **Tunable Size** fields replace the
  functionality of the **Maximum indices for each
  dimension** parameter. The block displays a warning on the
  block dialog box. Existing models continue to work. For more information,
  see Tunable size.
