---
type: simulink-block
title: 'n-D Lookup Table'
family: 'libsb2sl'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'ARC'
documentation_page: 'ndlookuptable'
documentation_source_path: 'slref/ndlookuptable.html'
language: zh-CN
chinese_source: worker-translation
---

# n-D Lookup Table

## 端口

### 输入

### **u1** — 第一维（行）输入 标量 | 向量 | 矩阵

**u1** 端口的实值输入，通过查找或插值您定义的值表映射到输出值。

**示例：** `0:10`

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `enumerated` | `fixed point`

### **uN** — 第 n 维输入值 标量 | 向量 | 矩阵

**uN** 端口的实值输入，通过查找或插值您定义的值表映射到输出值。

**示例：** `0:10`

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `enumerated` | `fixed point`

### **T** — 定义输出值表 维度与 **Number of table dimensions** 及表中每个维度的断点长度匹配的值矩阵

使用可在运行时调节的信号指定输出值表。

在仿真期间，矩阵大小必须与 **Number of table dimensions** 参数定义的维度匹配。但是，在模块图编辑期间，您可以输入空矩阵（指定为 `[]`）或未定义的工作区变量。此技术允许您推迟为表数据指定正确维度的矩阵，并继续编辑模块图。

#### 依赖关系

要启用此端口，请设置：

- **Data specification** 为 `Table and breakpoints`。
- **表格数据** 为 `Input port`。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **bp1** — 显式断点值 1×n 或 n×1 的单调递增向量

根据 **Breakpoints specification** 参数的值，使用可在运行时调节的信号显式指定断点数据。

- 如果将 **Breakpoints specification** 设置为 `Explicit values`，请在每个 **Breakpoints** 行中输入与表数据每个维度对应的断点向量。对于每个维度，将断点指定为值严格单调递增的 1×n 或 n×1 向量。

您最多可以创建三个断点数据输入端口。对于断点 4 到 30，只能通过相应的 **Breakpoints** 参数指定断点数据。

**注意**

要以等间距规格格式指定断点，请将 **Breakpoints specification** 设置为 `Even spacing`，并使用 **Breakpoints First** 点和 **Spacing** 参数。

#### 依赖关系

要启用此端口，请设置：

- **Data specification** 为 `Table and breakpoints`。
- **Breakpoints specification** 为 `Explicit values`。
- **Breakpoints 1** 为 `Input port`。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `enumerated` | `fixed point`

### **bp2** — 显式断点值 1×n 或 n×1 的单调递增向量

根据 **Breakpoints specification** 参数的值，使用可在运行时调节的信号显式指定断点数据。

- 如果将 **Breakpoints specification** 设置为 `Explicit values`，请在每个 **Breakpoints** 行中输入与表数据每个维度对应的断点向量。对于每个维度，将断点指定为值严格单调递增的 1×n 或 n×1 向量。

您最多可以创建三个断点数据输入端口。对于断点 4 到 30，只能通过相应的 **Breakpoints** 参数指定断点数据。

**注意**

要指定等间距断点数据，请使用 **Breakpoints** 参数。您无法通过输入端口指定等间距断点数据。

#### 依赖关系

要启用此端口，请设置：

- **Data specification** 为 `Table and breakpoints`。
- **Breakpoints specification** 为 `Explicit values`。
- **Breakpoints 2** 为 `Input port`。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `enumerated` | `fixed point`

### **bp3** — 显式断点值 1×n 或 n×1 的单调递增向量

根据 **Breakpoints specification** 参数的值，使用可在运行时调节的信号显式指定断点数据。

- 如果将 **Breakpoints specification** 设置为 `Explicit values`，请在每个 **Breakpoints** 行中输入与表数据每个维度对应的断点向量。对于每个维度，将断点指定为值严格单调递增的 1×n 或 n×1 向量。

您最多可以创建三个断点数据输入端口。对于断点 4 到 30，只能通过相应的 **Breakpoints** 参数指定断点数据。

**注意**

要指定等间距断点数据，请使用 **Breakpoints** 参数。您无法通过输入端口指定等间距断点数据。

#### 依赖关系

要启用此端口，请设置：

- **Data specification** 为 `Table and breakpoints`。
- **Breakpoints specification** 为 `Explicit values`。
- **Breakpoints 3** 为 `Input port`。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `enumerated` | `fixed point`
### 输出

### **Port\_1** — 通过查找或估计表值计算的输出 标量 | 向量 | 矩阵

基于输入值通过查找或估计表值生成的输出：

| 当模块输入... | n-D Lookup Table 模块... |
| --- | --- |
| 与断点向量中的索引值匹配 | 输出行、列和更高维断点交点处的表值 |
| 与断点向量中的索引值不匹配，但在范围内 | 使用您选择的 **Interpolation method** 插值适当的表值 |
| 与断点向量中的索引值不匹配，且超出范围 | 使用您选择的 **Extrapolation method** 外推输出值 |

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### 表和断点

### **Number of table dimensions** — 查找表维度数 `3`（默认） | `1` | `2` | `4` | `...` | `30`

输入查找表的维度数。此参数决定：

- 表的自变量数量和模块输入端口数量
- 要指定的断点向量数量

| 值 | 设置 |
| --- | --- |
| 1、2、3 或 4 | 从下拉列表中选择值。 |
| 更高的表维度数 | 直接在字段中输入正整数。此模块支持的最大表维度数为 30。 |

例如，大小为 *M* x *N* x ... 的表意味着维度 1 的大小为 *M*，维度 2 的大小为 *N*，依此类推。*M* 必须与第一个断点长度匹配，*N* 必须与第二个断点长度匹配，依此类推。

#### 程序化使用

|  |
| --- |
| **模块参数**：`NumberOfTableDimensions` |
| **类型**：character vector |
| **值**：`'1' | '2' | '3' | '4' | ... | 30` |
| **默认值**：`'3'` |

### **Data specification** — 表和断点指定方法 `Table and breakpoints`（默认） | `Lookup table object`

从列表中选择：

- `Table and breakpoints` — 指定表数据和断点。选择此选项将启用以下参数：

  - **表格数据**
  - **Breakpoints specification**
  - **Breakpoints 1**
  - **Breakpoints 2**
  - **Breakpoints 3**
  - **编辑表格和断点**

  要使用输入端口指定表和断点，请参阅 **Source** 参数。
- `Lookup table object` — 使用现有的查找表（`Simulink.LookupTable`）对象。选择此选项将启用 **Name** 字段和 **Edit table and breakpoints** 按钮。

#### 程序化使用

|  |
| --- |
| **模块参数**：`DataSpecification` |
| **类型**：character vector |
| **值**：`'Table and breakpoints' | 'Lookup table object'` |
| **默认值**：`'Table and breakpoints'` |

要将此参数从 `'Table and breakpoints'` 设置为 `'Lookup table object'`，请使用同一个 `set_param` 调用设置 `LookupTableObject` 参数。例如：

```
set_param('myModel/myLookupBlock',...
   'DataSpecification','Lookup table object',...
   'LookupTableObject','myLUTObject')
```

### **Name** — 查找表对象的名称 `[]`（默认） | `Simulink.LookupTable` 对象

输入查找表（`Simulink.LookupTable`）对象的名称。如果 `Simulink.LookupTable` 对象不存在，请单击操作按钮 并选择 **Create**。新查找表对象的相应参数将自动填充模块信息。

#### 依赖关系

要启用此参数，请将 **Data specification** 设置为 `Lookup table object`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`LookupTableObject` |
| **类型**：character vector |
| **值**：name of a `Simulink.LookupTable` object |
| **默认值**：`''` |

### **Breakpoints specification** — 断点指定方法 `Explicit values`（默认） | `Even spacing`

指定是将数据输入为显式断点，还是输入为生成等间距断点的参数。

- 要显式指定断点数据，请将此参数设置为 `Explicit values`，并在 **Breakpoints** 参数旁边的文本框中输入断点数据。
- 要指定生成等间距断点的参数，请将此参数设置为 `Even spacing`，并为断点数据的每个维度输入 **First point** 和 **Spacing** 参数的值。模块根据表数据计算要生成的点数。

#### 依赖关系

- 要启用此参数，请将 **Data specification** 设置为 `Table and breakpoints`。
- 当此参数设置为 `Even spacing` 时，只能通过对话框指定断点数据。

#### 程序化使用

|  |
| --- |
| **模块参数**：`BreakpointsSpecification` |
| **类型**：character vector |
| **值**：`'Explicit values' | 'Even spacing'` |
| **默认值**：`'Explicit values'` |

### **Support tunable size** — 启用可调表大小的选项 `off`（默认） | `on`

选中此复选框可在仿真运行或生成的代码执行期间启用活动区域的可调表大小。此选项使软件即使在生成的代码执行期间更改活动区域的大小以及查找表和断点数据的值时也能正常工作。表大小必须大于或等于 2 且小于最大可调大小。

#### 依赖关系

如果将 **Interpolation method** 设置为 `Cubic spline` 或 `Akima spline`，则 **Support tunable size** 不可用。

#### 程序化使用

|  |
| --- |
| **模块参数**：`SupportTunableSize` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

### **Source** — 表和断点数据的来源 `Dialog`（默认） | `Input port`

将表和断点数据的来源指定为：

- `Dialog` — 在 **Value** 参数中指定表或断点数据。
- `Input port` — 通过关联的输入端口指定表或断点数据。

  您最多可以创建三个断点数据输入端口。对于断点 4 到 30，只能通过相应的 **Breakpoints** 参数指定断点数据。

**注意**

使用输入端口指定表或断点数据可能会因运行时检查而对仿真中的模块性能产生负面影响。要对需要在仿真期间更改断点的动态进行建模，请选择 `Dialog` 并使用 Parameter Writer 模块更改断点数据。

#### 依赖关系

- 要启用此参数，请将 **Data specification** 设置为 `Table and breakpoints`。
- 要启用关联的 **Value**，请将此参数设置为 `Dialog`。
- 要启用关联的输入端口，请将此参数设置为 `Input port`。
- 将此参数设置为 `Input port` 会禁用 **Value** 字段，并在 **Data Types** 选项卡上隐藏相应参数。
- 将任一参数的此参数设置为 `Input port` 会禁用 **Edit Table and Breakpoints** 按钮。

#### 程序化使用

|  |
| --- |
| **模块参数**：`TableSource` | `BreakpointsForDimension1Source` | `BreakpointsForDimension2Source` | `BreakpointsForDimension3Source` |
| **类型**：character vector |
| **值**：`Dialog` | `Input port` |
| **默认值**：`'Dialog'` |

### **Tunable size** — 每个数组的最大元素数 `-1`（默认） | 实整数标量

将每个数组的最大大小指定为以下值之一：

- `-1` — 数组中的所有元素
- 实整数标量 — 每个数组的最大元素数

**Tunable size** 必须小于或等于数组的大小。

#### 依赖关系

要启用此参数：

- 将 **Data specification** 设置为 `Table and breakpoints`。
- 选择 **Support tunable size** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数**：`N1` to `N31` |
| **类型**：character vector |
| **值**：`-1` | real integer scalar |
| **默认值**：`-1` |

### **Table data** — 定义输出值表 `reshape(repmat([4 5 6;16 19 20;10 18 23],1,2),[3,3,2])`（默认） | 维度与 **Number of table dimensions** 匹配的值矩阵

在关联的 **Value** 字段中输入输出值表。

在仿真期间，矩阵大小必须与 **Number of table dimensions** 参数定义的维度匹配。但是，在模块图编辑期间，您可以输入空矩阵（指定为 `[]`）或未定义的工作区变量。此技术允许您推迟为表数据指定正确维度的矩阵，并继续编辑模块图。

#### 依赖关系

要启用此参数，请设置：

- **Data specification** 为 `Table and breakpoints`。
- **Table data: Source** 为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Table` |
| **类型**：character vector |
| **值**：matrix of table values |
| **默认值**：`'reshape(repmat([4 5 6;16 19 20;10 18 23],1,2),[3,3,2])'` |

### **Breakpoints** — 显式断点值或断点的第一点和间距 `[10,22,31]`（默认） | 1×n 或 n×1 的单调递增向量

根据 **Breakpoints specification** 参数的值，显式指定断点数据或将其指定为等间距断点。

- 如果将 **Breakpoints specification** 设置为 `Explicit values`，请在关联的 **Value** 字段中为每个 **Breakpoints** 行输入与表数据每个维度对应的断点向量。对于每个维度，将断点指定为值严格单调递增的 1×n 或 n×1 向量。
- 如果将 **Breakpoints specification** 设置为 `Even spacing`，请在每个 **Breakpoints** 行中输入 **First point** 和 **Spacing** 参数，以在相应维度中生成等间距断点。您的表数据决定等间距点的数量。

#### 依赖关系

- 要启用此参数，请设置：

  - **Data specification** 为 `Table and breakpoints`。
  - **Table data: Source** 为 `Dialog`。
- 当 **Breakpoints specification** 参数设置为 `Even spacing` 时，只能通过对话框指定断点数据。

#### 编程用法

|  |
| --- |
| **模块参数：** `BreakpointsForDimension1` | `BreakpointsForDimension2` | ... | `BreakpointsForDimension30` |
| **类型：** 字符向量 |
| **值：** 1×n 或 n×1 的单调递增数值向量 |
| **默认值：** `'[10, 22, 31]'` | `'[10, 22, 31]'` | … | `'[1:3]'` |

### **First point** — 均匀间隔断点数据中的第一个点 `1`（默认）| 标量

将均匀间隔断点数据中的第一个点指定为实值有限标量。当 **Breakpoints specification** 设置为 `Even spacing` 时，此参数可用。

#### 依赖关系

要启用此参数，请将 **Data specification** 设置为 `Table and breakpoints`，并将 **Breakpoints specification** 设置为 `Even spacing`。

#### 编程用法

|  |
| --- |
| **模块参数：** `BreakpointsForDimension1FirstPoint | BreakpointsForDimension2FirstPoint | ... | BreakpointsForDimension30FirstPoint` |
| **类型：** 字符向量 |
| **值：** 实值、有限、标量 |
| **默认值：** `'1'` |

### **Spacing** — 均匀间隔断点之间的间距 `1`（默认）| 标量

指定均匀间隔断点数据中点与点之间的间距。

#### 依赖关系

要启用此参数，请将 **Data specification** 设置为 `Table and breakpoints`，并将 **Breakpoints specification** 设置为 `Even spacing`。

#### 编程用法

|  |
| --- |
| **模块参数：** `BreakpointsForDimension1Spacing | BreakpointsForDimension2Spacing | ... | BreakpointsForDimension30Spacing` |
| **类型：** 字符向量 |
| **值：** 正的、实值、有限、标量 |
| **默认值：** `'1'` |

### **Edit table and breakpoints** — 打开查找表编辑器对话框按钮

点击此按钮以打开查找表编辑器。有关详细信息，请参阅查找表编辑器。

为查找表对象点击此按钮可让您编辑该对象并保存该对象的新值。

### 算法

#### 查找方法

### **Interpolation method** — 断点值之间的插值方法 `Linear point-slope`（默认）| `Flat` | `Nearest` | `Linear Lagrange` | `Cubic spline` | `Akima spline`

当输入落在断点值之间时，模块使用相邻断点对输出值进行插值。有关插值方法的详细信息，请参阅插值方法。

#### 依赖关系

- 如果选择 `Cubic spline`，模块仅支持标量信号。其他插值方法支持非标量信号。
- 如果选择 `Akima spline`，外插方法只能为 `Akima spline`。

  当设置为修改后的 Akima 插值方法时，此模块不支持：

  - 行主序数组布局以及针对行主序数组布局优化的算法
  - 缩放双精度和定点数据类型
  - `Simulink.LookupTable` 对象
  - 当配置参数 **Code Generation** > **Interface** > **Support non-finite numbers** 复选框被选中时的代码生成

  当设置为修改后的 Akima 插值方法时，在以下条件为真时，已知此模块运行较慢：

  - 基于代码生成的仿真目标，例如用于加速模式、快速加速模式、受保护模型等的目标。
  - 为大型断点和数据表大小生成的代码。例如表大小为 629×1601 时。

#### 编程用法

|  |
| --- |
| **模块参数：** `InterpMethod` |
| **类型：** 字符向量 |
| **值：** `'Linear point-slope' | 'Flat' | 'Nearest' | 'Linear Lagrange' | 'Cubic spline' | 'Akima spline'` |
| **默认值：** `'Linear point-slope'` |

### **Extrapolation method** — 处理超出断点向量范围的输入值的方法 `Linear`（默认）| `Clip` | `Cubic spline` | `Akima spline`

选择 `Clip`、`Linear` 或 `Cubic spline`。有关详细信息，请参阅外插方法。

如果外插方法为 `Linear`，则外插值基于所选的线性插值方法计算。例如，如果插值方法为 linear Lagrange，则外插方法继承 linear Lagrange 方程来计算外插值。

#### 依赖关系

- 要为 **Extrapolation method** 选择 `Cubic spline`，还必须为 **Interpolation method** 选择 `Cubic spline`。
- 要为 **Extrapolation method** 选择 `Akima spline`，还必须为 **Interpolation method** 选择 `Akima spline`。

#### 编程用法

|  |
| --- |
| **模块参数：** `ExtrapMethod` |
| **类型：** 字符向量 |
| **值：** `'Linear' | 'Clip' | 'Cubic spline' | 'Akima spline'` |
| **默认值：** `'Linear'` |

### **Index search method** — 计算表索引的方法 `Binary search`（默认）| `Linear search` | `Evenly spaced points`

选择 `Evenly spaced points`、`Linear search` 或 `Binary search`。每种搜索方法在不同情况下具有速度优势：

- 对于均匀间隔的断点向量（例如 10、20、30 等），通过选择 `Evenly spaced points` 来计算表索引可获得最佳速度。

  此算法仅使用一组断点的前两个断点来确定剩余点的偏移和间距。

  **注意**

  当使用 `Simulink.LookupTable` 对象指定表数据，且所引用的 `Simulink.LookupTable` 对象的 **Breakpoints Specification** 参数设置为 `Even spacing` 时，请将 **Index search method** 设置为 `Evenly spaced points`。
- 对于非均匀间隔的断点向量，请遵循以下准则：

  - 如果输入信号在时间步之间变化不大，选择 `Linear search` 并启用 **Begin index search using previous index result** 可获得最佳性能。
  - 如果输入信号每个时间步跳跃超过一个或两个表区间，选择 `Binary search` 可获得最佳性能。

索引搜索方法选择不佳可能导致严重依赖查找表的模型性能变慢。

**注意**

当以下条件成立时，生成的代码仅存储第一个断点、间距和断点数量：

- 断点数据不可调。
- 索引搜索方法为 `Evenly spaced points`。

#### 编程用法

|  |
| --- |
| **模块参数：** `IndexSearchMethod` |
| **类型：** 字符向量 |
| **值：** `'Binary search' | 'Evenly spaced points' | 'Linear search'` |
| **默认值：** `'Binary search'` |

### **Apply more accurate and efficient rounding when possible** — 使用高效就近舍入实现更精确的定点表查找 `off`（默认）| `on`

选中此复选框可在可能时启用高效的就近舍入实现。启用此选项会将舍入模式设置为 `Nearest`，并调整小数长度和中间数据类型，以在精度和效率之间取得平衡。如果无法实现高效实现，则舍入模式、小数长度和中间数据类型保持不变。

#### 依赖关系

要启用此参数：

- 将 **Number of table dimensions** 设置为 `2`。
- 将 **Interpolation method** 设置为 `Linear point-slope`。
- 将 **Extrapolation method** 设置为 `Clip`。

#### 编程用法

|  |
| --- |
| **模块参数：** `ApplyAccurateEfficientRounding` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **Begin index search using previous index result** — 从上一个时间步的索引开始搜索 `off`（默认）| `on`

当您希望模块使用上一个时间步找到的索引开始搜索时，选中此复选框。对于相对于区间大小变化缓慢的输入，启用此选项可以提高性能。否则，线性搜索和二分搜索方法可能耗时更长，尤其是对于大型断点向量。

#### 依赖关系

要启用此参数，请将 **Index search method** 设置为 `Linear search` 或 `Binary search`。

#### 编程用法

|  |
| --- |
| **模块参数：** `BeginIndexSearchUsingPreviousIndexResult` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **Assume input is within range** — 检查超出范围输入值的选项 `off`（默认）| `on`

*自 R2025a 起*

指定是否包含检查超出范围输入值的代码。选择此参数意味着您保证模块没有超出范围的输入，使模块能够进一步优化代码和仿真。有效输入范围取决于断点数据和 **Extrapolation method** 设置。

当您选择 **Assume input is within range** 时：

- 在仿真期间，模块假定没有超出范围的输入，并通过为超出范围的输入返回错误来强制执行此假设。
- 对于代码生成，模块不生成超出范围输入处理代码，因为它假定没有超出范围的输入。这意味着如果模块尝试为因超出范围输入而返回错误的模型生成代码，当生成的代码被赋予相同输入时，行为是未定义的，这可能导致严重后果。

  **警告**

  如果模型尝试生成代码，而是因为模块检测到超出范围输入而生成错误，那么将相同的超出范围输入传递给已部署代码时，行为是未定义的。此未定义行为可能导致严重问题。对于安全关键应用，请勿选择 **Assume input is within range**。

如果您为了效率想要选择 **Assume input is within range** 参数，请确保您的模型输入在范围内。例如：

| 参数 | 结果 | 何时使用 |
| --- | --- | --- |
| `on` | 仿真和生成的代码不包含检查超出范围断点输入的条件语句。当输入超出范围时，可能导致仿真和生成代码的未定义行为。 | 用于仿真和代码效率 |
| `off` | 仿真和生成的代码包含检查超出范围输入的条件语句。 | 用于安全关键应用 |

如果您确信输入在范围内，可以选择 **Assume input is within range** 参数以提高效率。默认情况下，此参数被清除。对于安全关键应用，请勿选择此参数。如果您想选择 **Assume input is within range** 参数，请先检查您的模型输入是否在范围内。例如：

1. 清除 **Assume input is within range** 参数。
2. 将 **Diagnostic for out-of-range input** 参数设置为 `Error`。
3. 在正常模式下仿真模型。
4. 如果存在超出范围错误，模块将返回运行时错误。修复它们使其在范围内，然后再次运行仿真。
5. 当仿真不再生成超出范围输入错误时，选择 **Assume input is within range** 参数。

   **注意**

   当您选择 **Assume input is within range** 参数且输入超出范围时，模块在仿真时返回运行时错误。对于生成的代码，行为是未定义的。

根据您的应用，您可以运行以下模型顾问检查来验证此参数的使用：

- **按产品** > **Embedded Coder** > **识别生成昂贵越界检查代码的查找表模块**
- **按产品** > **Simulink Check** > **建模标准** > **DO-178C/DO-331 检查** > **检查查找表模块的使用**

有关模型顾问的详细信息，请参阅运行模型顾问检查。

此外，要确定选择此参数是否安全，如果您有 Simulink Design Verifier™ 许可证，请考虑使用 Detect Block Input Range Violations (Simulink Design Verifier) 检查。

#### 编程用法

|  |
| --- |
| **模块参数：** `RemoveProtectionInput` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **Diagnostic for out-of-range input** — 输入超出范围时的模块操作 `None`（默认）| `Warning` | `Error`

指定当输入超出范围时是否产生警告或错误。选项包括：

- `None` — 不产生响应。
- `Warning` — 显示警告并继续仿真。
- `Error` — 终止仿真并显示错误。

#### 依赖关系

要启用此参数，请清除 **Assume input is within range** 或 **Assume index is within range** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `DiagnosticForOutOfRangeInput` |
| **类型：** 字符向量 |
| **值：** `'None' | 'Warning' | 'Error'` |
| **默认值：** `'None'` |

### **Apply full precision fixed-point algorithm when possible** — 更精确的定点表查找 `off`（默认）| `on`

使用此复选框可在可能时为线性插值查找启用全精度定点算法查找。此算法通常对硬件高效的定点舍入模式实现更好的精度。

#### 依赖关系

要启用此参数，请设置：

- **Number of table dimensions** 为 `1`。
- **Interpolation method** 为 `Linear point-slope`。
- **Extrapolation method** 为 `Clip`。
- 选中 **Use last table value for inputs at or above last breakpoint** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `ApplyFullPrecisionForLinearInterpolation` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **Use last table value for inputs at or above last breakpoint** — 计算位于或高于最后一个断点的输入的输出的方法 `off`（默认）| `on`

使用此复选框，指定模块用于寻址断点向量最后一个元素及其对应表值的索引约定。如果输入等于或大于断点数据的最后一个元素，则此复选框相关。由于舍入，选中和清除此复选框可能导致仿真和代码生成之间最后一个断点的结果不同。

| 复选框 | 模块使用的索引 | 区间分数 |
| --- | --- | --- |
| 选中 | **Table and Breakpoints** 选项卡上断点数据的最后一个元素 | 0 |
| 清除 | **Table and Breakpoints** 选项卡上断点数据的倒数第二个元素 | 1 |

给定断点向量 *bp* 范围内的输入 *u*，区间分数 *f* 在 0≦*f*<1 范围内，计算如下所示。

假设断点向量为 `[1 4 5]`，输入 *u* 为 `5.5`。如果选中此复选框，索引为最后一个元素（`5`）的索引，区间分数为 0。如果清除此复选框，索引为倒数第二个元素（`4`）的索引，区间分数为 1。

#### 依赖关系

要启用此参数，请设置：

- **Interpolation method** 为 `Linear`。
- **Extrapolation method** 为 `Clip`。

#### 编程用法

|  |
| --- |
| **模块参数：** `UseLastTableValue` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **Sample time (-1 for inherited)** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

#### 依赖关系

仅当您将其设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅不建议使用采样时间的模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认）| 带引号的标量或向量 |

#### 输入设置

### **Use one input port for all input data** — 对所有输入数据使用一个输入端口 `off`（默认）| `on`

选中此复选框可仅使用一个输入端口，该端口期望对于 n 维表具有 `n` 个元素宽度的信号。此选项可用于消除包含许多查找表的框图中的线条杂乱。

**注意**

当您选中此复选框时，模块上会出现一个标签为 `u` 的输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`UseOneInputPortForAllInputData` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

### 数据类型

### **Table data** — 表数据的数据类型 `Inherit: Same as output`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定表数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit:
  Same as output`
- 内置数据类型的名称，例如
  `single`
- 数据类型对象的名称，例如
  `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如
  `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

**提示**

在以下情况下，指定与输出数据类型不同的表数据类型：

- 使用比输出信号更小的类型存储表数据时降低内存需求
- 在具有不同输出数据类型的两个 n-D Lookup Table 模块之间共享预缩放的表数据
- 在具有不同输出数据类型的模块的生成代码中共享自定义存储表数据

#### 依赖关系

要启用此参数，请将 **Table and Breakpoints** 选项卡中的 **Table data** 设置为 `Dialog`。

#### 编程使用

|  |
| --- |
| **模块参数**：`TableDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit from 'Table data'' | 'Inherit: Same as output' | 'double' | 'single' | 'half' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)'|'<data type expression>'` |
| **默认值**：`'Inherit: Same as output'` |

### **Table data Minimum** — 表数据的最小值 `[]` | `scalar`

指定表数据的最小值。默认值为 `[]`（未指定）。

#### 编程使用

|  |
| --- |
| **模块参数**：`TableMin` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'[]'` |

### **Table data Maximum** — 表数据的最大值 `[]` | `scalar`

指定表数据的最大值。默认值为 `[]`（未指定）。

#### 编程使用

|  |
| --- |
| **模块参数**：`TableMax` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'[]'` |

### **Breakpoints** — 断点数据类型 `Inherit: Same as corresponding input`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

指定一组断点数据的数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit:
  Same as corresponding input`
- 内置数据类型的名称，例如
  `single`
- 数据类型类的名称，例如枚举数据类型类
- 数据类型对象的名称，例如
  `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如
  `fixdt(1,16,0)`

**提示**

- 断点支持无序枚举数据。因此，线性搜索也是无序的，这提供了灵活性但可能影响性能。搜索从断点中的第一个元素开始。
- 如果选中了 **Begin index search using previous index
  result** 复选框，则必须使用有序单调递增数据。这种排序可提高性能。
- 对于枚举数据，**Extrapolation method** 必须为 `Clip`。
- 模块不支持枚举数据的越界输入。指定枚举数据时，请在断点向量中包含整个枚举集。例如，使用 `enumeration` 函数。

这是在此模块中使用枚举数据的限制：

- 模块不支持枚举数据的越界输入。指定枚举数据时，请在断点向量中包含整个枚举集。例如，使用 `enumeration` 函数。

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

**提示**

在以下情况下，指定与对应输入数据类型不同的断点数据类型：

- 使用比输入信号更小的类型存储断点数据时降低内存需求
- 在具有不同输入数据类型的两个 n-D Lookup Table 模块之间共享预缩放的断点数据
- 在具有不同输入数据类型的模块的生成代码中共享自定义存储断点数据

如果断点数据类型或其对应输入数据类型中的任一个具有定点数据类型，请为它们指定相同的斜率和偏置。

#### 依赖关系

要启用此参数，请将 **Table and Breakpoints** 选项卡中对应的 **Breakpoints** 参数设置为 `Dialog`。

#### 编程使用

|  |
| --- |
| **模块参数**：`BreakpointsForDimension1DataTypeStr | BreakpointsForDimension2DataTypeStr| ... | BreakpointsForDimension30DataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Same as corresponding input' | 'Inherit: Inherit from 'Breakpoint data'' | 'double' | 'single' | 'half' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)'|'<data type expression>'` |
| **默认值**：`'Inherit: Same as corresponding input'` |

### **Breakpoints Minimum** — 断点数据可以具有的最小值 `[]` | `scalar`

指定一组断点数据可以具有的最小值。默认值为 `[]`（未指定）。

#### 编程使用

|  |
| --- |
| **模块参数**：`BreakpointsForDimension1Min | BreakpointsForDimension2Min | ... | BreakpointsForDimension30Min` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'[]'` |

### **Breakpoints Maximum** — 断点数据可以具有的最大值 `[]` | `scalar`

指定一组断点数据可以具有的最大值。默认值为 `[]`（未指定）。

#### 编程使用

|  |
| --- |
| **模块参数**：`BreakpointsForDimension1Max | BreakpointsForDimension2Max | ... | BreakpointsForDimension30Max` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'[]'` |

### **Fraction** — 小数数据类型 `Inherit: Inherit via internal rule`（默认）| `double` | `single` | `fixdt(1,16,0)` | `<data type expression>`

指定小数数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit:
  Inherit via internal rule`
- 内置数据类型的名称，例如
  `single`
- 数据类型对象的名称，例如
  `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如
  `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程使用

|  |
| --- |
| **模块参数**：`FractionDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule' | 'double' | 'single' | 'fixdt(1,16,0)'|'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Intermediate results** — 中间结果数据类型 `Inherit: Same as output`（默认）| `Inherit: Inherit via internal rule` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定中间结果数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit:
  Same as output`
- 内置数据类型的名称，例如
  `single`
- 数据类型对象的名称，例如
  `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如
  `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

**提示**

使用此参数可为内部计算指定比表数据或输出数据更高（或更低）的精度。

#### 编程使用

|  |
| --- |
| **模块参数**：`IntermediateResultsDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule' | 'Inherit: Same as output' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)'|'<data type expression>'` |
| **默认值**：`'Inherit: Same as output'` |

### **Output** — 输出数据类型 `Inherit: Same as input`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定输出数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit:
  Inherit via back propagation`
- 内置数据类型的名称，例如
  `single`
- 数据类型对象的名称，例如
  `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如
  `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via back propagation' | 'Inherit: Inherit from table data' | 'Inherit: Same as first input' | 'double' | 'single' | 'half' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)'|'<data type expression'` |
| **默认值**：`'Inherit: Same as first input'` |

### **Output Minimum** — 用于范围检查的最小值 `[]` | `scalar`

指定用于范围检查的最小值。默认值为
`[]`（未指定）。Simulink 软件使用此值来执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（请参阅 Specify Signal Ranges）。
- 定点数据类型的自动缩放。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutMin` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'[]'` |

### **Output Maximum** — 用于范围检查的最大值 `[]` | `scalar`

指定用于范围检查的最大值。默认值为
`[]`（未指定）。Simulink 软件使用此值来执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（请参阅 Specify Signal Ranges）。
- 定点数据类型的自动缩放。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'[]'` |

### **Internal rule priority** — 用于中间计算的内部规则 `Speed`（默认）| `Precision`

指定用于中间计算的内部规则。选择 `Speed` 可加快计算速度。如果这样做，可能会发生精度损失，通常最多 2 位。

#### 依赖关系

此参数仅在 **Intermediate
results** 或 **Fraction** 参数设置为
`Inherit: Inherit via internal rule` 时生效。

#### 编程使用

|  |
| --- |
| **模块参数**：`InternalRulePriority` |
| **类型**：character vector |
| **值**：`'Speed' | 'Precision'` |
| **默认值**：`'Speed'` |

### **Require all inputs to have the same data type** — 要求所有输入具有相同的数据类型 `on`（默认）| `off`

选中此项可要求所有输入具有相同的数据类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`InputSameDT` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'on'` |

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选中此参数可防止定点工具覆盖您在此模块上指定的数据类型。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

### **Integer rounding mode** — 定点运算的舍入模式 `Simplest`（默认）| `Ceiling` | `Convergent` | `Floor` | `Nearest` | `Round` | `Zero`

指定在仿真或执行从模型生成的代码期间发生的定点查找表计算的舍入模式。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

此选项不影响模块参数值的舍入。Simulink 会将这些值舍入到最接近的可表示整数值。要控制模块参数的舍入，请在模块对话框的编辑字段中输入使用 MATLAB® 舍入函数的表达式。

#### 编程使用

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型**：character vector |
| **值**：`'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认值**：`'Simplest'` |

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

| 操作 | 采取此操作的原因 | 溢出时发生的情况 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框（`on`）。 | 您的模型可能存在溢出，并且您希望在生成的代码中提供显式的饱和保护。 | 溢出饱和到数据类型能够表示的最小值或最大值。 | 与有符号 8 位整数相关的溢出可以饱和到 -128 或 127。 |
| 不选中此复选框（`off`）。 | 您希望优化生成代码的效率。您希望避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors。 | 溢出回绕到数据类型可表示的相应值。 | 数字 130 无法放入有符号 8 位整数，并回绕到 -126。 |

**提示**

如果将模型保存为 R2009a 或更早版本，此复选框设置无效，并且不会出现饱和代码。此行为保留了向后兼容性。

选中此复选框时，饱和应用于模块上的每个内部操作，而不仅仅是输出或结果。通常，代码生成过程可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程使用

|  |
| --- |
| **模块参数**：`SaturateOnIntegerOverflow` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

## 所属库

Simulink / Lookup Tables HDL Coder / Lookup Tables

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **MapToRAM** | 将查找表（LUT）映射到 RAM。默认值为 `on`。另请参阅 MapToRAM (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

| Native Floating Point | |
| --- | --- |
| **HandleDenormals** | 指定是否希望 HDL Coder 插入附加逻辑来处理设计中的非规格化数。非规格化数是幅值小于最小浮点数的数，该最小浮点数可以在尾数中没有前导零的情况下表示。默认值为 `inherit`。另请参阅 HandleDenormals (HDL Coder)。 |
| **LatencyStrategy** | 指定是否将设计中的模块映射到浮点运算符的 `inherit`、`Max`、`Min` 或 `Zero`。默认值为 `inherit`。另请参阅 LatencyStrategy (HDL Coder)。 |
| **MantissaMultiplyStrategy** | 指定在代码生成期间如何实现尾数乘法运算。通过使用不同的设置，您可以控制目标 FPGA 设备上的 DSP 使用情况。默认值为 `inherit`。另请参阅 MantissaMultiplyStrategy (HDL Coder)。 |
| **PrecomputeCoefficients** | 要启用此属性，请将 **Interpolation method** 设置为 `Linear point-slope`。启用此属性后，斜率和偏置系数将根据表数据和断点静态预计算。此设置减少了在运行时为计算系数而执行的除法运算数量。它还减少了执行的浮点加法和乘法运算的总数。启用此属性可减少延迟并节省所需的查找表资源面积。但是，此属性会重新排列浮点运算，这可能会导致较小的数值差异。您可以在生成的验证模型中观察到这些数值差异。 |
| **AreaOptimization** | 对于 4-D 和 5-D LUT，HDL 代码生成支持完全并行和串行实现。要启用此属性，请对 4-D 和 5-D LUT 使用线性插值方法。将此属性设置为 `Parallel` 或 `Serial` 时，HDL Coder 会操纵设计的资源。要减少设计面积，请使用串行实现以最小化资源。要观察完全并行和串行实现的结果，请比较设计的本机浮点运算符的资源利用率报告。您还可以比较完全并行和串行实现的设计综合结果。 |

**查找表的延迟考虑**

当在本机浮点（NFP）模式下为 LUT 使用浮点数据类型时，代码生成器会根据 Add、Divide 和 Multiplication 运算符的延迟值来计算 LUT 的延迟。LUT 的延迟还取决于 HDL 模块属性，例如 **PrecomputeCoefficients** 和 **MapToRAM**。其计算方式如下：

- 当 **PrecomputeCoefficients** 为 `Off` 时，LUT 的延迟计算为，

  `LUT Latency = D + N(2A + M)`

  其中，

  `D` 是 Divide 运算符的 NFP 延迟

  `A` 是 Add 运算符的 NFP 延迟

  `M` 是 Multiplication 运算符的 NFP 延迟

  `N` 是表维度数
- 当 **PrecomputeCoefficients** 为 `On` 时，LUT 的延迟计算为，

  `LUT Latency = (2^N - 1)A + N(M)`
- 当您为 LUT 打开 **MapToRAM** 属性，并为模型指定综合工具和目标设备时，会增加一个额外的延迟。

浮点运算符（例如 Add、Divide 和 Multiply）的延迟值列于表中。有关更多信息，请参阅 Latency Values of Floating-Point Operators (HDL Coder)。

| 浮点运算符 | 数据类型 | 最小延迟 | 最大延迟 |
| --- | --- | --- | --- |
| Add | Double | 6 | 11 |
| Single | 6 | 11 |
| Half | 4 | 8 |
| Divide | Double | 31 | 61 |
| Single | 17 | 32 |
| Half | 10 | 19 |
| Multiply | Double | 6 | 9 |
| Single | 6 | 8 |
| Half | 4 | 6 |

例如，考虑一个具有单精度数据类型且 **PrecomputeCoefficients** 为 `off` 的 1-D 查找表。1-D LUT 的延迟为

`LUT Latency = 32 + 1(2x11 + 8) = 62`。

如果打开 **MapToRAM** 选项，则 LUT 延迟为 63。

**复数数据支持**

此模块支持复数信号的代码生成。

**必需的模块设置**

| Block Setting | HDL Coder Support |
| --- | --- |
| **Number of table dimensions** | 选择 1 到 30 之间的表维度。 |
| **Breakpoints specification** | 选择 `Explicit values` 或 `Even spacing`。 |
| **Extrapolation method** | 选择 `Clip` 或 `Linear`。代码生成器不支持超出偶数边界的外插。 |
| **Interpolation method** | 选择 `Flat` 或 `Linear point-slope`。 |
| **Diagnostic for out-of-range input** | 选择 `Error`。如果指定其他选项，HDL Coder 会生成警告。 |
| **Use last table value for inputs at or above last breakpoint** | 选中此复选框。 |
| **Require all inputs to have the same data type** | 选中此复选框。 |
| **Fraction** | 选择 `Inherit: Inherit via internal rule`。 |
| **Integer rounding mode** | 选择 `Zero`、`Floor` 或 `Simplest`。 |
| **Use one input port for all input data** | 清除此复选框。 |

**定点数据类型支持**

您可以为具有定点数据类型的模块生成代码。您可以在 n-D Lookup Table 模块的所有维度中使用定点数据类型。要为该模块生成具有定点数据类型的代码，请使用以下模块参数设置：

| Block Setting | HDL Coder Support |
| --- | --- |
| **Number of table dimensions** | 选择 1 到 30 之间的表维度。 |
| **Breakpoints specification** | 选择 `Explicit values` 或 `Even spacing`。 |
| **Extrapolation method** | 选择 `Clip` |
| **Interpolation method** | 选择 `Flat` 或 `Linear point-slope`。 |
| **Index search methods** | 选择 `Evenly spaced points`、`Binary search` 或 `Linear search`。 |

**MAX 10 设备设置**

如果您使用 Intel® MAX 10 设备，要将查找表映射到 RAM，请在 Quartus 工具中创建项目时添加以下 Tcl 命令：

`set_global_assignment -name INTERNAL_FLASH_UPDATE_MODE "SINGLE IMAGE WITH ERAM"`

**表数据键入和大小调整**

- 最好将表结构化为断点之间的间距为 2 的幂。如果断点间距不满足此条件，HDL Coder 会发出警告。当断点间距为 2 的幂时，您可以将预查找步骤中的除法运算替换为右移运算。

**限制**

- 当您将 **Interpolation method** 设置为 `Flat` 时，该模块支持数据输入、断点和输出的 `half` 数据类型。半数据类型不支持线性插值。
- HDL 代码生成不支持表元素超过 131072 个的 LUT。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

Simulink PLC Coder™ 对查找表模块的支持有限。该代码生成器不支持：

- 维度数大于 2
- 三次样条插值方法
- 使用先前索引模式开始索引搜索
- 三次样条外插方法

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2011a 中引入**

### R2025a：n-D Lookup Table 模块 **Remove protection against out-of-range input in generated code** 参数已替换

**Remove protection against out-of-range input in generated code** 参数已替换为 **Assume input is within range**。程序化名称 `RemoveProtectionInput` 保持不变。

如果模型仿真因为将超出范围的输入馈送到选中了 **Assume input is within range** 的模块而生成错误，则当在生成的代码执行期间出现相同的超出范围输入时，模型生成的代码具有未定义行为。此未定义行为可能导致严重问题。对于安全关键型应用，请勿选择 **Remove protection against out-of-range input in generated code**。

在 R2025a 之前的版本中，**Remove protection against out-of-range input in generated code** 仅移除生成代码中针对超出范围值的代码检查。该模块无法检测这些问题。作为一种变通方法，如果您有来自 R2025a 之前版本的模型并且无法迁移到更高版本，请将 **Diagnostic for out-of-range input** 参数设置为 `Error`。下次运行模型时，当输入超出范围时会生成错误。

### R2024b：**Support tunable table size in code generation** 参数已替换为 **Support tunable size**

在查找表模块中，**Support tunable table size in code generation** 参数已替换为 **Support tunable table size**。由于此更改：

- 如果您使用 `SupportTunableTableSize` 以程序化方式设置 **Table and Breakpoints** > **Support tunable size** 参数，则下次打开查找表模块时，该模块会显示警告。现有模型继续工作。
- **Table and Breakpoints** 选项卡上的 **Support tunable size** 参数替换了 **Algorithm** 选项卡上的 **Support tunable table size in code generation** 和 **Maximum indices for each dimension** 参数。在 R2024b 之前，选择 **Support tunable table size in code generation** 参数会启用 **Maximum indices for each dimension** 参数，该参数为每个表维度设置最大索引值。从 R2024b 开始，选择 **Support tunable size** 参数会为 **Breakpoints** 参数启用 **Tunable Size** 字段。这些 **Tunable Size** 字段替换了 **Maximum indices for each dimension** 参数的功能。该模块会在模块对话框中显示警告。现有模型继续工作。有关更多信息，请参阅 Tunable size。

## 描述

近似 n 维函数

### 支持的模块操作

1-D、2-D 和 n-D Lookup Table 模块计算 N 个变量的函数的采样表示

y=F(x1,x2,x3,...,xN)

其中函数 *F* 可以是经验函数。该模块通过查找或插值您使用模块参数定义的值表，将输入映射到输出值。该模块支持平坦（常量）、线性（线性点斜率）、Lagrange（线性 Lagrange）、最近邻、三次样条和 Akima 样条插值方法。您可以将这些方法应用于从 1 到 30 的任意维度的表。

在以下模块中，第一个输入标识第一维（行）断点，第二个输入标识第二维（列）断点，依此类推。

有关各种模块方向的端口顺序说明，请参阅 Identify Port Location on Rotated or Flipped Block。

当 **Math and Data Types** > **Use algorithms optimized for row-major array layout** 配置参数设置后，2-D 和 n-D Lookup Table 模块行为从列主序变为行主序。对于这些模块，列主序和行主序算法可能在输出计算顺序上有所不同，可能导致数值略有不同。此功能需要 Simulink® Coder™ 或 Embedded Coder® 许可证。有关行主序支持的更多信息，请参阅 Code Generation of Matrices and Arrays (Simulink Coder)。

### 断点和表数据的指定

这些模块参数定义断点和表数据。

| 模块参数 | 用途 |
| --- | --- |
| **Number of table dimensions** | 指定查找表的维度数。 |
| **Breakpoints** | 指定与查找表每个维度对应的断点向量。 |
| **Table data** | 定义关联的输出值集合。 |

**提示**

均匀间隔的断点可以使生成的代码无除法。有关更多信息，请参阅 `fixpt_evenspace_cleanup` 和 Identify questionable fixed-point operations (Embedded Coder)。

### 模块如何生成输出

n-D、1-D 和 2-D Lookup Table 模块通过基于输入值查找或估计表值来生成输出。

| 模块输入 | n 维查找表模块行为 |
| --- | --- |
| 与断点向量中的索引值匹配 | 输出行、列和更高维断点交点处的表值 |
| 与断点向量中的索引值不匹配，但在范围内 | 使用您选择的 **Interpolation method** 插值适当的表值 |
| 与断点向量中的索引值不匹配，并且超出范围 | 使用您选择的 **Extrapolation method** 外插输出值 |

### 执行等效操作的其他模块

您可以将 Interpolation Using Prelookup 模块与 Prelookup 模块配合使用，以执行与一个 n-D Lookup Table 模块等效的操作。这种模块组合提供了更大的灵活性，从而可以在线性插值时实现更高效的仿真性能。

当查找操作是不需要插值的数组访问时，请使用 Direct Lookup Table (n-D) 模块。例如，如果您有一个整数值 `k`，并且想要获取表中的第 `k` 个元素 `y = table(k)`，则不需要插值。
