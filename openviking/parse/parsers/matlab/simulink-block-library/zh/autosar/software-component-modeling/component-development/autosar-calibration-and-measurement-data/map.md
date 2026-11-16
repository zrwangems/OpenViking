---
type: simulink-block
title: 'Map'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Software Component Modeling / Component Development / AUTOSAR Calibration and Measurement Data'
documentation_page: 'map'
documentation_source_path: 'ref/map.html'
language: zh-CN
chinese_source: worker-translation
---

# Map

## 端口

### 输入

### **u1** — 第一维输入值 标量 | 向量 | 矩阵

第一个端口的实数值输入。

当 `Targeted Routine Library` 设置为 `IFX
(fixed-point)` 时，**u1** 值的有效数据类型为：`int8`、`uint8`、
`int16`、`uint16` 和定点数据类型。

当 `Targeted Routine Library` 设置为 `IFL
(floating-point)` 时，**u1** 值的唯一有效数据类型为 `single`。

**示例：** 0:10

**数据类型：** `single` | `int8` | `int16` | `uint8` | `uint16` | `fixed point`

### **u2** — 第二维输入值 标量 | 向量 | 矩阵

第二个端口的实数值输入。

当 `Targeted Routine Library` 设置为 `IFX
(fixed-point)` 时，**u2** 值的有效数据类型为：`int8`、`uint8`、
`int16`、`uint16` 和定点数据类型。

当 `Targeted Routine Library` 设置为 `IFL
(floating-point)` 时，**u2** 值的唯一有效数据类型为 `single`。

**示例：** 0:10

**数据类型：** `single` | `int8` | `uint8` | `int16` | `uint16` | `fixed point`

### 输出

### **y** — 通过查找或估计表值计算得到的输出 标量 | 向量 | 矩阵

基于输入值通过查找或估算表值生成的输出。如果输入与断点集合的索引值匹配，Map 模块将提供一个表值作为输出。如果模块输入与断点集合中的索引值不匹配，但在范围内，模块将执行配置的插值方法，并提供表中的估算值作为输出。

**数据类型：** `single` | `int8` | `uint8` | `int16` | `uint16` | `fixed point`

## 参数

### **目标例程库** — 指示用于模块代码替换的 AUTOSAR 例程库 `IFX (fixed-point)` | `IFL (floating-point)`

如果您为模型选择 AUTOSAR 4.x 代码替换库 (CRL)，则从此模块生成的代码将从选定的 AUTOSAR 例程库进行替换。此参数使您可以选择定点 (IFX) 或浮点 (IFL) 代码替换和验证检查。

### **目标例程** — 用于代码替换的 AUTOSAR 库例程 `Ifx_IntIpoMap` | `Ifl_IntIpoMap`

此参数反映用于替换此模块生成代码的 AUTOSAR 代码替换库 (CRL) 例程的名称。命名约定包括目标例程库、插值方法和模块类型。此参数仅供参考，不得编辑。

当 `Targeted Routine Library` 设置为 `IFX
(fixed-point)` 时，该值默认为 `Ifx_IntIpoMap`。

当 `Targeted Routine Library` 设置为 `IFL
(floating-point)` 时，该值默认为
`Ifl_IntIpoMap`。

### 表规格

### **数据设定** — 表和断点的指定方法 `Table and breakpoints` (default) | `Lookup table object`

从列表中选择：

- `Table and breakpoints` — 指定表数据和断点。选择此选项将启用以下参数：

  - **表数据**
  - **断点设定**
  - **断点 1**
  - **断点 2**
  - **编辑表和断点**
- `Lookup table object` — 使用现有的查找表 (`Simulink.LookupTable`) 对象。选择此选项将启用 **名称** 字段和 **编辑表和断点** 按钮。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataSpecification` |
| **类型：** character vector | string |
| **值：** `"Table and breakpoints" | "Lookup table object"` |
| **默认值：** `"Table and breakpoints"` |

### **名称** — 查找表对象的名称 `[]` (default) | `Simulink.LookupTable` object

输入查找表 (`Simulink.LookupTable`)
对象的名称。

#### 依赖关系

要启用此参数，请将 **数据设定** 设置为
`Lookup table object`。

#### 编程用法

|  |
| --- |
| **模块参数：** `LookupTableObject` |
| **类型：** character vector |
| **值：** `Simulink.LookupTable` 对象的名称 |
| **默认值：** `'[]'` |

### **表数据** — 定义输出值表 `[4 5 6;16 19 20;10 18 23]` (default) | character vector

输入输出值表。

在仿真期间，矩阵大小必须为二维。但是，在模块图编辑期间，您可以输入空矩阵（指定为 `[]`）或未定义的工作区变量。此方法让您可以推迟为表数据指定具有正确维度的矩阵，并继续编辑模块图。

#### 依赖关系

要启用此参数，请将 **数据设定** 设置为
`Table and breakpoints`。

#### 编程用法

|  |
| --- |
| **模块参数：** `Table` |
| **类型：** character vector |
| **值：** 表值矩阵 |
| **默认值：** `'[4 5 6;16 19 20;10 18 23]'` |

### **断点设定** — 断点指定方法 `Explicit values` (default) | `Even spacing`

指定是将数据输入为显式断点，还是输入为生成均匀间隔断点的参数。

- 要显式指定断点数据，请将此参数设置为
  `Explicit values`，并在 **断点** 参数旁边的文本框中输入断点数据。
- 要指定生成均匀间隔断点的参数，请将此参数设置为 `Even spacing`，并为每个断点数据维度输入 **第一点** 和 **间距** 参数的值。模块将根据表数据计算要生成的点数。

#### 依赖关系

要启用此参数，请将 **数据设定** 设置为
`Table and breakpoints`。

#### 编程用法

|  |
| --- |
| **模块参数：** `BreakpointsSpecification` |
| **类型：** character vector | string |
| **值：** `"Explicit values" | "Even spacing"` |
| **默认值：** `"Explicit values"` |

### **断点** — 显式断点值，或断点的第一点和间距 `[10,22,31]` (default) | 1-by-n 或 n-by-1 的单调递增值向量

根据 **断点设定** 参数的值，显式指定断点数据或指定为均匀间隔的断点。

- 如果要将 **断点设定** 设置为
  `Explicit values`，请在每一
  **断点** 行中输入与表数据每个维度对应的断点集。对于每个维度，将断点指定为
  1-by-n 或 n-by-1 向量，其值严格单调递增。
- 如果要将 **断点设定** 设置为 `Even
  spacing`，请在每一 **断点** 行中输入 **第一点** 和
  **间距** 参数，以在相应维度中生成均匀间隔的断点。表数据将确定均匀间隔点的数量。

#### 依赖关系

要启用此参数，请将 **数据设定** 设置为
`Table and breakpoints`。

#### 编程用法

|  |
| --- |
| **模块参数：** `BreakpointsForDimension1` `| BreakpointsForDimension2` |
| **类型：** character vector |
| **值：** 1-by-n 或 n-by-1 的单调递增值向量 |
| **默认值：** `'[10, 22, 31]'` |

### **第一点** — 均匀间隔断点数据中的第一点 `1` (default) | 标量

将均匀间隔断点数据中的第一点指定为实数值、有限值或标量。当您将 **断点设定** 设置为 `Even spacing` 时，此参数可用。

#### 依赖关系

要启用此参数，请将 **数据设定** 设置为
`Table and breakpoints`，并将 **断点设定** 设置为 `Even spacing`。

#### 编程用法

|  |
| --- |
| **模块参数：** `BreakpointsForDimension1FirstPoint | BreakpointsForDimensionSecondPoint` |
| **类型：** character vector |
| **值：** 实数值、有限值、标量 |
| **默认值：** `'1'` |

### **间距** — 均匀间隔断点之间的间距 `1` (default) | 标量

指定均匀间隔断点数据中点之间的间距。

#### 依赖关系

要启用此参数，请将 **数据设定** 设置为
`Table and breakpoints`，并将 **断点设定** 设置为 `Even spacing`。

#### 编程用法

|  |
| --- |
| **模块参数：** `BreakpointsForDimension1Spacing | BreakpointsForDimension2Spacing` |
| **类型：** character vector |
| **值：** 正的、实数值、有限值、标量 |
| **默认值：** `'1'` |

### **编辑表和断点** — 启动查找表编辑器对话框按钮

点击此按钮以打开查找表编辑器。然后，您可以编辑对象并保存该对象的新值。

### 算法

### **索引搜索方法** — 计算表索引的方法 `Linear search` (default) | `Evenly spaced points` | `Binary search`

选择 `Evenly spaced points`、`Linear search`
或 `Binary search`。每种搜索方法在不同情况下具有速度优势：

- 对于均匀间隔的断点集（例如 10、20、30 等），通过选择 `Evenly spaced points` 来计算表索引可获得最优速度。此算法仅使用集合的前两个断点来确定其余点的偏移和间距。

  **注意**

  使用 `Simulink.LookupTable` 对象指定表数据，并且所引用 `Simulink.LookupTable` 对象的 **断点设定** 参数设置为 `Even spacing` 时，请将 **索引搜索方法** 设置为 `Evenly spaced points`。
- 对于非均匀间隔的断点集，请遵循以下准则：

  - 如果输入信号在时间步之间没有显著变化，则选择 `Linear search` 并启用 **使用先前索引结果开始索引搜索** 可获得最佳性能。
  - 如果输入信号每个时间步跳过一个或两个以上的表区间，则选择 `Binary search` 可获得最佳性能。

次优的索引搜索方法选择可能导致严重依赖查找表的模型性能缓慢。

在以下情况下，生成的代码仅存储第一个断点、间距和断点数量：

- 断点数据不可调。
- 索引搜索方法为 `Evenly spaced points`。

#### 编程用法

|  |
| --- |
| **模块参数：** `IndexSearchMode` |
| **类型：** character vector | string |
| **值：** `"Binary search" | "Evenly spaced points" | "Linear search"` |
| **默认值：** `"Linear search"` |

### **使用先前索引结果开始索引搜索** — 从上一个时间步的索引开始使用 `off` (default) | `on`

当您希望模块使用上一时间步找到的索引开始搜索时，请选中此复选框。对于相对于区间大小变化缓慢的输入，启用此选项可以提高性能。否则，线性搜索和二分搜索方法可能需要更长时间，尤其是对于大型断点集。

#### 依赖关系

要启用此参数，请将 **索引搜索方法** 设置为
`Linear search` 或 `Binary
search`。

#### 编程用法

|  |
| --- |
| **模块参数：** `BeginIndexSearchUsingPreviousIndexResult` |
| **类型：** character vector | string |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **插值方法** — 断点值之间的插值方法 `Linear point-slope` (default) | `Flat` | `Nearest`

当输入落在断点值之间时，模块使用相邻断点对输出值进行插值。有关详细信息，请参阅插值方法。

#### 编程用法

|  |
| --- |
| **模块参数：** `InterpMode` |
| **类型：** character vector | string |
| **值：** `"Linear point-slope" | "Flat" | "Nearest"` |
| **默认值：** `"Linear point-slope"` |

### **整数舍入模式** — 定点或浮点运算的舍入模式 `Zero` (default) | `Round`

指定在仿真期间或执行从模型生成的代码期间发生的定点或浮点查找表计算的舍入模式。

此选项不影响模块参数值的舍入。Simulink™ 会将此类值舍入为最接近的可表示整数值。

#### 依赖关系

此参数仅在设置为 `Round` 时可见。AUTOSAR 4.x 和用于 SIL 测试的主机库不支持整数舍入，并且默认隐藏。要在使用 AUTOSAR 4.x 代码替换库时启用 SIL 工作流，请将此设置更改为 `Zero`。

#### 编程用法

|  |
| --- |
| **模块参数：** `RndMode` |
| **类型：** character vector | string |
| **值：** `"Round" | "Zero"` |
| **默认值：** `"Zero"` |

### 数据类型

### **表数据** — 表数据的数据类型 `Inherit: Same as output` (default) | `Inherit: Inherit from 'Table data'` | `single` | `int8` | `uint8` | `int16` | `uint16` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定表数据类型。模块将验证所选类型与目标例程的规格兼容。

当 `Targeted Routine Library` 设置为 `IFL
(floating-point)` 时，唯一有效的数据类型是
`single`。

当 `Targeted Routine Library` 设置为 `IFX
(fixed-point)` 时，您可以将表数据类型设置为：

- 继承数据类型的规则：`Inherit: Same as
  output`、`Inherit: Inherit from 'Table
  data'`。
- 以下内置数据类型之一：`int8`、
  `uint8`、`int16`、
  `uint16`。
- 数据类型对象的名称，例如
  `Simulink.NumericType` 对象。
- 求值结果为数据类型的表达式。例如，软件提供以下常用定点数据类型表达式：
  `fixdt(1,16)`、
  `fixdt(1,16,0)` 或
  `fixdt(1,16,2^0,0)`。

单击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型。

**提示**

在以下情况下，指定与输出数据类型不同的表数据类型：

- 存储使用比输出信号更小类型的表数据时降低内存需求。
- 在两个具有不同输出数据类型的 Map 模块之间共享预缩放的表数据。
- 在具有不同输出数据类型的模块的生成代码中共享自定义存储表数据。

#### 依赖关系

要启用此选项卡，请在 **表规格** 选项卡上，将
**数据设定** 设置为 `Table and
breakpoints`。

#### 编程用法

|  |
| --- |
| **模块参数：** `TableDataTypeStr` |
| **类型：** character vector | string |
| **值：** `"Inherit: Inherit from 'Table data'" | "Inherit: Same as output" | "single" | "int8" | "uint8" | "int16" | "uint16" | "fixdt(1,16)" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"` |
| **默认值：** `"Inherit: Same as output"` |

## 所属库

AUTOSAR Blockset / Classic Platform / Library Routines / Interpolation

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

### R2025a：整数舍入模式已隐藏

**整数舍入模式** 设置为 `"Zero"`
并默认隐藏，因为 AUTOSAR 4.x 和用于 SIL 测试的主机库仅支持 `"Zero"`。

### R2025a：AUTOSAR 代码替换库支持 Release 4.0 之后的架构

从 25a 开始，AUTOSAR 代码替换库支持 AUTOSAR 4.0 之后的 AUTOSAR 架构版本。要使用最新的 AUTOSAR 例程，请在模型配置参数对话框的 **代码生成** > **接口** 窗格中，将 **代码替换库** 指定为
`AUTOSAR 4.x`。

## 描述

近似二维函数

Map 模块执行二维插值表查找，包括索引搜索。该表是两个变量中函数的采样表示。断点集将输入值关联到表中的位置。您还可以将 Prelookup 和 Prelookup Using Map 模块一起使用，以执行与此模块相同的操作。

当您设置 **数学和数据类型** > **使用针对行优先数组布局优化的算法** 配置参数时，模块行为将从列优先更改为行优先。对于这些模块，列优先和行优先算法可能在输出计算顺序上有所不同，从而可能导致数值略有不同。此功能需要 Simulink Coder™ 或 Embedded Coder™ 软件。有关行优先支持的详细信息，请参阅矩阵和数组的代码生成 (Simulink Coder)。

如果您为 AUTOSAR 模型选择 AUTOSAR 4.x 代码替换库 (CRL)，则从此模块生成的代码将替换为您在模块参数对话框中配置的 AUTOSAR 库例程。
