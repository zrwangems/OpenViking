---
type: simulink-block
title: 'From Spreadsheet'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'fromspreadsheet'
documentation_source_path: 'slref/fromspreadsheet.html'
language: zh-CN
chinese_source: worker-translation
---

# From Spreadsheet

## 端口

### 输出

### **Port\_1** — 来自电子表格的数据 标量 | 向量 | 矩阵

来自指定电子表格的增量数据。

**Sample time** 参数指定 From Spreadsheet 模块从电子表格读取数据所使用的采样时间。有关详细信息，请参阅参数。文件中的时间戳必须单调非递减。

对于电子表格中不包含匹配时间戳的每个仿真时间命中点，Simulink 软件使用所选方法进行插值或外插以获取所需数据。有关详细信息，请参阅没有对应电子表格时间戳的仿真时间命中点。

From Spreadsheet 模块在模块级别接受数据类型规范。如果要为每个信号指定不同的数据类型，请考虑选择 **Output Data Type** > **Inherit: Auto**。此选项使用反向传播来解析反向信号数据类型。例如，假设 From Spreadsheet 模块中有两个信号 In1 和 In2，该模块将它们发送到具有 int8 和 Boolean 数据类型的端口。通过反向传播，该模块将 In1 重新转换为 int8，将 In2 重新转换为 Boolean。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

## 参数

### **File name** — 完整路径和文件名 `untitled.xlsx`（默认）| 完整路径 | 相对路径

输入电子表格文件的完整路径和文件名，包括文件扩展名，指定为完整路径或相对路径。注意：

此模块仅在 Microsoft 平台上支持非英文的完整路径和文件名。

**提示**

- 您可以指定完整路径、相对路径或仅文件名。

  - 对于完整路径和相对路径文件名，该模块支持仿真和代码生成。
  - 如果找不到文件，该模块会在当前文件夹中查找该文件。
  - 仅使用文件名时，该模块可以进行仿真。但是，对于代码生成，该模块会缓存完整路径。如果该模块找不到文件，它会在当前文件夹中搜索。
- 如果不包含文件扩展名，该模块假定扩展名为 `.xlsx`。

#### 编程使用

|  |
| --- |
| **模块参数**：`FileName` |
| **类型**：character vector |
| **Value**：完整路径和文件名 |
| **默认值**：`'untitled.xlsx'` |

### **Sheet name** — 电子表格中的工作表名称 `Sheet1`（默认）| 工作表名称

输入电子表格中工作表的名称。您可以在此编辑框中键入工作表名称，也可以在打开工作表后选择工作表名称。

如果您的电子表格是 CSV 格式，该模块会在此参数中填充不带扩展名的 CSV 文件名。请勿更改此值。

要打开工作表，请点击 。在工作表中，您可以通过在所需的值范围上拖动来选择数据范围。

或者，您可以通过在 **Range** 参数中指定值范围来选择数据范围。

#### 编程使用

|  |
| --- |
| **模块参数**：`SheetName` |
| **类型**：character vector |
| **Value**: Sheet name |
| **默认值**：`'Sheet1'` |

### **Range** — 单元格范围 工作表中已使用单元格的整个范围（默认）| 逗号分隔的 `column:row` 列表

要指定范围，请使用 `column:row` 格式，多个规范之间用逗号分隔。例如，`A1:B3,D1:D3,A7:B9,D7:D9`。如果未指定或为空，该模块会自动检测已使用范围，即工作表中的所有数据。

如果选择范围重叠，该模块会适当地解析选择信息。例如，如果您指定多个重叠的范围，如 `A1:B4,B1:E7`，该模块会将选择解析为 A1 到 E7（含两端）。

**Selection/History** 包含此会话期间所选范围的列表。关闭 **Range Selection** 后，该模块不会存储这些范围。

使用 **Range** 参数的替代方法是打开工作表，方法是点击 。在工作表中，您可以通过在所需的值范围上拖动来选择数据范围。范围选择会反映在 **Range** 参数文本框中。

要从模块对话框应用新范围，请点击 **Apply**。

#### 编程使用

|  |
| --- |
| **模块参数**：`Range` |
| **类型**：character vector |
| **Value**: entire range of used cells in sheet | comma-separated list of `column:row` |
| **默认值**：`''` |

### **Output data type** — 输出数据类型 `Inherit: auto`（默认）| `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class_name>` | `<data type expression>`

From Spreadsheet 模块输出的数据类型。From Spreadsheet 模块接受包含多种数据类型的电子表格。但是，该模块将电子表格数据类型读取为 double。然后，它根据 **Output data type** 的值输出数据类型。

如果要为每个信号指定不同的数据类型，请考虑选择 **Output Data Type** > **Inherit: auto**。此选项使用反向传播来解析反向信号数据类型。例如，假设 From Spreadsheet 模块中有两个信号 In1 和 In2，该模块将它们发送到具有 int8 和 Boolean 数据类型的端口。通过反向传播，该模块将 In1 重新转换为 int8，将 In2 重新转换为 boolean。

要允许该模块将输出数据类型转换为与接收模块匹配的类型，请使用 `Inherit: auto`。

有关详细信息，请参阅控制信号的数据类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: auto' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'boolean' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | 'Enum: <class name>' | '<data type expression>'` |
| **默认值**：`'Inherit: auto'` |

### **Treat first column as** — 时间或数据 `Time`（默认）| `Data`

选择该模块应如何处理电子表格的第一列：

- `Time` — 将第一列视为时间。
- `Data` — 将第一列视为数据。

#### 依赖关系

当您选择 `Data` 时，该模块会禁用：

- **第一个数据点之前的数据外推**
- **Data interpolation within time range**
- **最后一个数据点之后的数据外推**

并启用：

- **最后一个数据点之后的输出**

#### 编程使用

|  |
| --- |
| **模块参数**：`TreatFirstColumnAs` |
| **类型**：character vector |
| **Value**: `'Time' | 'Data'` |
| **默认值**：`'Time'` |

### **Sample time** — 采样周期和偏移量 `0`（默认）| 标量 | 向量

采样周期和偏移量。

From Spreadsheet 模块使用以下采样时间从电子表格读取数据：

- 您为 From Spreadsheet 模块指定的采样时间
- From Spreadsheet 模块从 From Spreadsheet 模块向其馈送数据的模块继承的采样时间

默认值为 `0`，表示连续采样时间。电子表格以模型的基本（最快）速率读取。有关详细信息，请参阅指定采样时间。

#### 编程使用

|  |
| --- |
| **Parameter:** `SampleTime` |
| **类型**：character vector |
| **值**：scalar | vector |
| **默认值**：`'0'` |

### **Data extrapolation before first data point** — 电子表格中初始时间戳之前的仿真时间的外插方法 `Linear extrapolation`（默认）| `Hold first value` | `Ground value`

Simulink 对电子表格中第一个时间戳之前的仿真时间命中点使用的外插方法。选择以下外插方法之一。

| 方法 | 描述 |
| --- | --- |
| `Linear extrapolation` | （默认）如果电子表格仅包含一个样本，From Spreadsheet 模块输出对应的数据值。如果电子表格包含多个样本，From Spreadsheet 模块使用前两个样本进行线性外插：- 对于 `double` 数据，使用前两个样本对值进行线性外插 - 对于 `Boolean` 数据，输出第一个数据值 - 对于除 `double` 或 `Boolean` 之外的内置数据类型：- 将数据向上转换为 `double` - 执行线性外插（如上文对 `double` 数据的描述）- 将外插后的数据值向下转换为原始数据类型 不能对枚举（`enum`）数据使用 `Linear extrapolation` 选项。 |
| `Hold first value` | 使用文件中的第一个数据值 |
| `Ground value` | 使用取决于电子表格样本数据值数据类型的值：- 定点数据类型 — 使用接地值 - 除定点之外的数值类型 — 使用 `0` - `Boolean` — 使用 `false` - 枚举数据类型 — 使用默认值 |

#### 依赖关系

要启用此参数，请将 **Treat first column as** 设置为 `Time`。

#### 编程使用

|  |
| --- |
| **Parameter:** `ExtrapolationBeforeFirstDataPoint` |
| **类型**：character vector |
| **值**：`'Linear extrapolation' | 'Hold first value' | 'Ground value'` |
| **默认值**：`'Linear extrapolation'` |

### **Data interpolation within time range** — 落在电子表格中两个时间戳之间的仿真时间的插值方法 `Linear interpolation`（默认）| `Zero order hold`

Simulink 对电子表格中两个时间戳之间的仿真时间命中点使用的插值方法。选择以下插值方法之一。

| 方法 | 描述 |
| --- | --- |
| `Linear interpolation` | （默认）From Spreadsheet 模块使用两个对应的电子表格样本进行插值：- 对于 `double` 数据，使用两个对应的样本对值进行线性插值 - 对于 Boolean 数据，如果仿真时间位于两个具有不同值的电子表格数据点之间，From Spreadsheet 模块将值转换定位在两个电子表格数据点的中间。例如，如果电子表格数据从 true 转换为 false，From Spreadsheet 数据在电子表格数据点之间间隔的前半段为仿真时间提供 true 的输出值。在间隔的后半段为仿真时间提供 false 的输出值。- 对于除 `double` 或 `Boolean` 之外的内置数据类型：- 将数据向上转换为 `double` - 执行线性插值（如上文对 `double` 数据的描述）- 将插值后的值向下转换为原始数据类型 不能对枚举（`enum`）数据使用 `Linear interpolation` 选项。 |
| `Zero order hold` | 使用两个样本中第一个样本的数据 |

#### 依赖关系

要启用此参数，请将 **Treat first column as** 设置为 `Time`。

#### 编程使用

|  |
| --- |
| **Parameter:** `InterpolationWithinTimeRange` |
| **类型**：character vector |
| **值**：`'Linear interpolation' | 'Zero order hold'` |
| **默认值**：`'Linear interpolation'` |

### **Data extrapolation after last data point** — 电子表格中最后一个时间戳之后的仿真时间的外插方法 `Linear extrapolation`（默认）| `Hold last value` | `Ground value`

Simulink 对电子表格中最后一个时间戳之后的仿真时间命中点使用的外插方法。选择以下外插方法之一。

| 方法 | 描述 |
| --- | --- |
| `Linear extrapolation` | （默认）如果电子表格仅包含一个样本，From Spreadsheet 模块输出对应的数据值。如果电子表格包含多个样本，From Spreadsheet 模块使用最后两个样本的数据值进行线性外插：- 对于 `double` 数据，使用最后两个样本对值进行外插 - 对于 `Boolean` 数据，输出最后一个数据值 - 对于除 `double` 或 `Boolean` 之外的内置数据类型：- 将数据向上转换为 `double`。- 执行线性外插（如上文对 `double` 数据的描述）。- 将外插后的值向下转换为原始数据类型。不能对枚举（`enum`）数据使用 `Linear extrapolation` 选项。 |
| `Hold last value` | 使用文件中的最后一个数据值 |
| `Ground value` | 使用取决于电子表格样本数据值数据类型的值：- 定点数据类型 — 使用接地值 - 除定点之外的数值类型 — 使用 `0` - `Boolean` — 使用 `false` - 枚举数据类型 — 使用默认值 |

#### 依赖关系

要启用此参数，请将 **Treat first column as** 设置为 `Time`。

#### 编程使用

|  |
| --- |
| **Parameter:**  `ExtrapolationAfterLastDataPoint` |
| **类型**：character vector |
| **值**：`'Linear extrapolation' | 'Hold last value' | 'Ground value'` |
| **默认值**：`'Linear extrapolation'` |

### **Output after last data point** — 最后一个数据点之后的操作 `Repeating sequence`（默认）| `Hold final value` | `Ground value`

选择最后一个数据点之后的操作：

- `Repeating sequence` — 通过从 **Range** 中指定范围的第一行读取数据来重复序列
- `Hold final value` — 在仿真的剩余时间内输出最后定义的值。
- `Ground value` — 根据 **Output data type** 中指定的数据类型值输出接地值。

#### 依赖关系

要启用此参数，请将 **Treat first column as** 设置为 `Data`。

#### 编程使用

|  |
| --- |
| **Parameter:**  `OutputAfterLastPoint` |
| **类型**：character vector |
| **值**：`'Repeating sequence' | 'Hold final value' | 'Ground value'` |
| **默认值**：`'Repeating sequence'` |

### **启用过零检测** — 启用过零检测的选项 `off`（默认）| `on`

选择以启用过零检测。

过零检测参数仅在**采样时间**参数设置为 `0`（连续）时适用。

此模块仅在使用变步长求解器的仿真中支持过零检测。当您使用定步长求解器进行仿真时，软件不会为此模块检测或定位过零点。

Simulink 使用一种称为过零检测的技术来准确定位不连续点，而无需使用过小的步长。在此上下文中，过零用于表示不连续点。

对于 From Spreadsheet 模块，过零检测只能发生在文件中的时间戳处。Simulink 仅检查时间戳，而不检查数据值。

如果输入数组包含重复的时间戳（多个条目具有相同的时间戳），Simulink 将在该时间戳处检测到过零点。例如，假设输入数组具有以下数据。

```
time:     0 1 2 2 3
signal:   2 3 4 5 6
```

在时间 2 处，输入信号不连续产生了一个过零点。

对于具有非重复时间戳的数据，过零检测取决于以下参数的设置：

- **第一个数据点之前的数据外推**
- **时间范围内的数据插值**
- **最后一个数据点之后的数据外推**

模块在确定以下情况时应用以下规则：

- 第一个时间戳处是否发生过零
- 第一个和最后一个时间戳之间的时间戳
- 最后一个时间戳

| 时间戳 | 过零检测发生条件 |
| --- | --- |
| 第一个 | **第一个数据点之前的数据外推**设置为 `Ground value`。 |
| 第一个和最后一个之间 | **时间范围内的数据插值**设置为 `Zero-order hold`。 |
| 最后一个 | 以下设置之一或两者同时发生：  - **最后一个数据点之后的数据外推**设置为 `Ground value`。 - **时间范围内的数据插值**设置为 `Zero-order hold`。 |

下图说明了 From Spreadsheet 模块访问数据的过零检测，该模块具有以下设置：

- **第一个数据点之前的数据外推** — `Linear extrapolation`
- **时间范围内的数据插值**（对于内部点）— `Zero order hold`
- **最后一个数据点之后的数据外推** — `Linear extrapolation`

图表显示第一个点处无过零，每个内部点处有过零，最后一个点处有过零

下图说明了 From Spreadsheet 模块访问数据的过零检测。该模块对时间戳（点）具有以下设置：

- **第一个数据点之前的数据外推** — `Hold first value`
- **时间范围内的数据插值** — `Zero order hold`
- **最后一个数据点之后的数据外推** — `Hold last value`

图表显示第一个点处无过零，每个内部点处有过零，最后一个点处有过零

#### 程序化使用

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **模式** — 要指定的数据类型类别 `Inherit`（默认）| `Built in` | `Fixed point` | `Enumerated` | `Expression`

选择要指定的数据类型类别。有关详细信息，请参阅 Control Data Types of Signals。

- `Inherit`

  数据类型的继承规则。选择 `Inherit` 会启用右侧的第二个菜单/文本框。
- `Built in`

  内置数据类型。选择 `Built in` 会启用右侧的第二个菜单/文本框。选择以下选项之一：

  - `double` — 默认
  - `single`
  - `int8`
  - `uint8`
  - `int16`
  - `uint16`
  - `int32`
  - `uint32`
  - `int64`
  - `uint64`
  - `boolean`
- `Fixed point` — 定点数据类型。
- `Enumerated` — 枚举数据类型。选择 `Enumerated` 会启用右侧的第二个菜单/文本框，您可以在其中输入类名。
- `Expression` — 计算结果为数据类型的表达式。选择 `Expression` 会启用右侧的第二个菜单/文本框，您可以在其中输入表达式。

### **数据类型覆盖** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

选择此信号的数据类型覆盖模式。

- 当您选择 `Inherit` 时，Simulink 从其上下文中继承数据类型覆盖设置，即从使用该信号的模块、`Simulink.Signal` 对象或 Simulink 中的 Stateflow® 图继承。
- 当您选择 `Off` 时，Simulink 忽略其上下文的数据类型覆盖设置，并使用为信号指定的定点数据类型。

有关详细信息，请参阅 Simulink 文档中的 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将**模式**设置为 `Built in` 或 `Fixed point`。

#### 提示

为单个数据类型关闭数据类型覆盖的能力，使您在使用数据类型覆盖时能更好地控制模型中的数据类型。例如，您可以使用此选项确保数据类型满足下游模块的要求，而不受数据类型覆盖设置的影响。

### **符号性** — 指定有符号或无符号 `Signed`（默认）| `Unsigned`

指定定点数据是有符号还是无符号。有符号数据可以表示正值和负值，但无符号数据仅表示正值。

- `Signed`，将定点数据指定为有符号。
- `Unsigned`，将定点数据指定为无符号。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将**模式**设置为 `Fixed point`。

### **定标** — 定点数据的定标方法 `Binary point`（默认）| `Best precision` | `Slope and bias`

指定定点数据的定标方法，以避免溢出条件并最小化量化误差。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将**模式**设置为 `Fixed point`。

将**定标**设置为 `Binary point` 会启用：

- **小数长度**
- **计算最佳精度定标**

将**定标**设置为 `Slope and bias` 会启用：

- **斜率**
- **偏置**
- **计算最佳精度定标**

### **字长** — 保存量化整数的字的位大小 `16`（默认）| 0 到 32 的整数

指定保存量化整数的字的位大小。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将**模式**设置为 `Fixed point`。

### **小数长度** — 指定定点数据类型的小数长度 `0`（默认）| 标量整数

将定点数据类型的小数长度指定为正整数或负整数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将**定标**设置为 `Binary point`。

### **斜率** — 指定定点数据类型的斜率 `2^0`（默认）| 正实值标量

指定定点数据类型的斜率。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将**定标**设置为 `Slope and bias`。

### **偏置** — 指定定点数据类型的偏置 `0`（默认）| 实值标量

将定点数据类型的偏置指定为任意实数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将**定标**设置为 `Slope and bias`。

## 所属库

Simulink / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed pointa` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `yes` |
|  |  |
| --- | --- |
| a 支持最多 32 位定点数据类型。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

- 不建议用于生产代码。
- RSim 目标的代码生成提供与 Simulink 相同的支持；所有其他代码生成目标仅支持数组格式中具有时间格式的 double、一维、实数信号。
- 在加速器、快速加速器、模型引用加速器模式或模型引用快速加速器模式下仿真，其行为方式与在正常模式下仿真相同，并具有相同的要求。
- From Spreadsheet 模块不支持生成涉及构建 ERT 或 GRT 目标，或使用 SIL 或 PIL 仿真模式的代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

支持最多 32 位定点数据类型。

## 版本历史

**在 R2015b 中引入**

### R2024a：From Spreadsheet 模块更新

From Spreadsheet 现在支持**文件名**的相对路径和完整路径，用于仿真和代码生成。在 R2024a 之前的版本中，如果您为**文件名**指定了相对路径，From Spreadsheet 模块会在代码生成期间将相对路径更改为完整路径。

### R2022b：From Spreadsheet 在当前文件夹中搜索电子表格文件

如果 From Spreadsheet 模块在提供的完整路径中找不到电子表格文件，它现在会在当前文件夹中搜索该电子表格文件。此更改使包含 From Spreadsheet 模块的 Simulink Compiler™ 独立可执行文件能够找到电子表格文件。在以前的版本中，From Spreadsheet 模块不会在当前文件夹中查找电子表格文件。

### R2022b：COM 读取问题

`'LibXL'` 是 `set_param` 函数的 `'ReaderLibrary'` 参数的新值。

## 描述

从电子表格读取数据

From Spreadsheet 模块从 Microsoft® Excel®（所有平台）或 CSV（仅限安装了 Microsoft Office 的 Microsoft Windows® 平台）电子表格读取数据，并将数据作为信号输出。From Spreadsheet 模块不支持 Microsoft Excel 电子表格图表。

From Spreadsheet 图标显示在模块**文件名**和**工作表名称**参数中指定的电子表格文件名和工作表名称。

### 存储格式

From Spreadsheet 模块从电子表格读取的数据必须具有适当的格式。

对于 Microsoft Excel 电子表格：

- From Spreadsheet 模块将第一行解释为信号名称。如果您未指定信号名称，From Spreadsheet 模块将分配一个默认名称，格式为 `Signal #`，其中 *`#`* 随每个额外的未命名信号递增。
- From Spreadsheet 模块将第一列解释为时间。在此列中，时间值必须单调递增。
- From Spreadsheet 模块将其余列解释为信号。

此示例显示了一个格式正确的 Microsoft Excel 电子表格。第一列是 Time，第一行包含信号名称。每个工作表包含一个信号组。

对于 CSV 文本文件（仅限安装了 Microsoft Office 的 Microsoft 平台）：

- From Spreadsheet 模块将第一列解释为时间。在此列中，时间值必须递增。
- From Spreadsheet 模块将其余列解释为信号。
- 每列必须具有相同数量的条目。
- From Spreadsheet 模块将每个文件解释为一个信号组。

此示例显示了一个格式正确的 CSV 文件。内容表示一个信号组。

```
0,0,0,5,0
1,0,1,5,0
2,0,1,5,0
3,0,1,5,0
4,5,1,5,0
5,5,1,5,0
6,5,1,5,0
7,0,1,5,0
8,0,1,5,1
9,0,1,5,1
10,0,1,5,0
```

From Spreadsheet 模块不接受非有限数据的信号值，例如 `Nan`、`Inf` 或 `-Inf`。

### 仿真期间的模块行为

From Spreadsheet 模块在仿真期间从电子表格增量读取数据。

**采样时间**参数指定 From Spreadsheet 模块用于从电子表格读取数据的采样时间。有关详细信息，请参阅参数。文件中的时间戳必须单调非递减。

对于电子表格中没有匹配时间戳的每个仿真时间命中，Simulink® 软件使用所选方法进行插值或外推以获得所需数据。有关详细信息，请参阅没有对应电子表格时间戳的仿真时间命中。

### 没有对应电子表格时间戳的仿真时间命中

如果仿真时间命中没有对应的电子表格时间戳，From Spreadsheet 模块的输出取决于：

- 仿真时间命中是发生在第一个时间戳之前、时间戳范围内还是最后一个时间戳之后
- 您选择的插值或外推方法
- 电子表格数据的数据类型

有关插值和外推选项的详细信息，请参阅以下参数的描述：

- 第一个数据点之前的数据外推
- 时间范围内的数据插值
- 最后一个数据点之后的数据外推

有时电子表格包含两个或多个具有相同时间戳的数据值。在这种情况下，From Spreadsheet 模块的操作取决于仿真时间命中相对于电子表格中重复时间戳的发生时间。

例如，假设电子表格包含以下数据。三个数据值的时间戳值为 `2`。

```
time stamps:    0 1 2 2 2 3 4
data values:    2 3 6 4 9 1 5
```

下表描述了 From Spreadsheet 模块的输出。

| 仿真时间，相对于电子表格中的重复时间戳值 | From Spreadsheet 模块操作 |
| --- | --- |
| 在重复时间戳之前 | 执行与时间戳不同时相同的操作，使用重复时间戳值中的第一个作为插值的基础。（在此示例中，时间戳值为 `6`。） |
| 在重复时间戳处或之后 | 执行与时间戳不同时相同的操作，使用重复时间戳值中的最后一个作为插值的基础。（在此示例中，该时间戳值为 `9`。） |

### COM 读取问题

默认情况下，From Spreadsheet 模块在 Windows 平台上使用组件对象模型（COM）接口，在其他平台上使用 LibXL 库来读取电子表格。如果 From Spreadsheet 模块在 Windows 上读取电子表格时出现问题，请使用 `set_param` 函数将 `'ReaderLibrary'` 设置为 `'LibXL'`。例如：

```
set_param(blockPath,‘ReaderLibrary’,‘LibXL’);
```

其中 *blockPath* 是模型模块路径。
