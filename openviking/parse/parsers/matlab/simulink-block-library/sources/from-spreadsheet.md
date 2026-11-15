---
type: simulink-block
title: 'From Spreadsheet'
family: sources
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'fromspreadsheet'
---

# From Spreadsheet

Read data from spreadsheet

## 中文

从电子表格读取数据

### 所属库

Simulink / Sources

### 描述

From Spreadsheet 模块可以从 Microsoft® Excel®（所有平台）或 CSV（仅限安装了 Microsoft Office 的 Microsoft Windows® 平台）电子表格读取数据并将数据输出为信号。From Spreadsheet 模块不支持 Microsoft Excel 电子表格图。

From Spreadsheet 图标显示在模块的**文件名**和**工作表名称**参数中指定的电子表格文件名和工作表名称。

#### 存储格式

From Spreadsheet 模块从电子表格中读取的数据必须已适当格式化。

对于 Microsoft Excel 电子表格：

- From Spreadsheet 模块将第一行解释为信号名称。如果您不指定信号名称，From Spreadsheet 模块将使用格式 `Signal #` 指定默认信号名称，其中 *`#`* 随着每个未命名信号的增加而递增。
- From Spreadsheet 模块将第一列解释为时间。在此列中，时间值必须是单调递增的。
- From Spreadsheet 模块将其余列解释为信号。

以下示例显示了一个可接受格式的 Microsoft Excel 电子表格。第一列是 Time，第一行包含信号名称。每个工作表包含一个组。

对于 CSV 文本文件（仅限安装了 Microsoft Office 的 Microsoft 平台）：

- From Spreadsheet 模块将第一列解释为时间。在此列中，时间值必须是递增的。
- From Spreadsheet 模块将其余列解释为信号。
- 每个列必须具有相同的条目数。
- From Spreadsheet 模块将每个文件解释为一个信号组。

以下示例显示了一个可接受格式的 CSV 文件。内容表示一个信号组。

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

#### 仿真过程中的模块行为

From Spreadsheet 模块在仿真期间以增量方式从电子表格中读取数据。

**采样时间**参数指定 From Spreadsheet 模块用来从电子表格中读取数据的采样时间。有关详细信息，请参阅参数。文件中的时间戳必须单调非递减。

对于电子表格中不包含任何匹配时间戳的每个仿真时间点，Simulink® 软件都会使用所选方法进行内插或外插以获得所需数据。有关详细信息，请参阅没有对应电子表格时间戳的仿真时间点。

#### 没有对应电子表格时间戳的仿真时间点

如果仿真时间点没有对应的电子表格时间戳，则 From Spreadsheet 模块输出将取决于：

- 仿真时间点出现在第一个时间戳之前、时间戳范围内还是最后一个时间戳之后
- 您选择的内插或外插方法
- 电子表格数据的数据类型

有关内插和外插选项的详细信息，请参阅下列参数描述：

- 第一个数据点之前的数据外插
- 时间范围内的数据插值
- 末尾数据点后的数据外插

有时，电子表格包含两个或多个具有相同时间戳的数据值。在这种情况下，From Spreadsheet 模块的操作取决于仿真时间点的出现时间（相对于电子表格中的重复时间戳）。

例如，假设电子表格包含以下数据。三个数据值的时间戳值为 `2`。

```
time stamps:    0 1 2 2 2 3 4
data values:    2 3 6 4 9 1 5
```

下表列出了 From Spreadsheet 模块输出。

| 仿真时间（相对电子表格中的重复时间戳值） | From Spreadsheet 模块操作 |
| --- | --- |
| 在重复时间戳之前 | 执行与时间戳不同时相同的操作，使用第一个重复时间戳值作为插值的基础。（在此示例中，该时间戳值为 `6`。） |
| 在重复时间戳当时或之后 | 执行与时间戳不同时相同的操作，使用最后一个重复时间戳值作为插值的基础。（在此示例中，该时间戳值为 `9`。） |

#### COM 的读取问题

默认情况下，From Spreadsheet 模块使用 Windows 平台上的组件对象模型 (COM) 接口和其他平台上的 LibXL 库读取电子表格。如果 From Spreadsheet 模块在读取 Windows 上的电子表格时遇到问题，请使用 `set_param` 函数将 `'ReaderLibrary'` 设置为 `'LibXL'`。例如：

```
set_param(blockPath,‘ReaderLibrary’,‘LibXL’);
```

其中 *blockPath* 是模型模块路径。

### 端口

#### 输出

#### **Port\_1** — 来自电子表格的数据 标量 | 向量 | 矩阵

来自指定电子表格的增量数据。

**采样时间**参数指定 From Spreadsheet 模块用来从电子表格中读取数据的采样时间。有关详细信息，请参阅参数。文件中的时间戳必须单调非递减。

对于电子表格中不包含任何匹配时间戳的每个仿真时间点，Simulink 软件都会使用所选方法进行内插或外插以获得所需数据。有关详细信息，请参阅没有对应电子表格时间戳的仿真时间点。

From Spreadsheet 模块接受在模块级指定的数据类型。如果您要为各个信号指定不同的数据类型，请考虑选择**输出数据类型** > **Inherit: Auto**。此选项使用反向传播来解析反向信号数据类型。例如，假定 From Spreadsheet 模块中有两个信号 In1 和 In2，该模块将它们发送到具有 int8 和布尔数据类型的端口。通过反向传播，该模块将 In1 重新转换为 int8，将 In2 重新转换为布尔型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### 参数

#### **文件名** — 完整路径和文件名 `untitled.xlsx` (默认) | 完整路径 | 相对路径

输入电子表格文件的完整路径和文件名，包括文件扩展名，指定为完整路径或相对路径。注意：

只有在 Microsoft 平台上，此模块才支持非英语完整路径和文件名。

**提示**

- 您可以指定完整路径、相对路径或仅文件名。

  - 通过完整路径和相对路径文件名，模块支持仿真和代码生成。
  - 如果找不到该文件，模块将在当前文件夹中查找该文件。
  - 仅使用文件名，模块就可以仿真。但是，对于代码生成，模块会缓存完整路径。如果模块找不到文件，它将在当前文件夹中搜索。
- 如果不包含文件扩展名，该模块将采用 `.xlsx` 作为扩展名。

##### 编程用法

|  |
| --- |
| **模块参数**：`FileName` |
| **类型**：字符向量 |
| **值**：完整路径和文件名 |
| **默认值**：`'untitled.xlsx'` |

#### **工作表名称** — 电子表格中工作表的名称 `Sheet1` (默认) | 工作表名称

输入电子表格中的工作表的名称。您可以在此编辑框中键入工作表名称，或者在打开工作表之后选择工作表名称。

如果您的电子表格是 CSV 格式，则模块会使用不带扩展名的 CSV 文件名称填充此参数。不要更改此值。

要打开工作表，请点击 。在工作表中，您可以通过在所需的值范围上拖动来选择数据范围。

或者，您可以通过在**范围**参数中指定值范围来选择数据范围。

##### 编程用法

|  |
| --- |
| **模块参数**：`SheetName` |
| **类型**：字符向量 |
| **值**：工作表名称 |
| **默认值**：`'Sheet1'` |

#### **范围** — 单元格范围 工作表中使用的单元格的全部范围 (默认) | 以逗号分隔的 `column:row` 列表

要指定范围，请使用格式 `column:row`，其中用逗号分隔多个指定值。例如，`A1:B3,D1:D3,A7:B9,D7:D9`。如果未指定或为空，模块将自动检测使用的范围，即工作表中的所有数据。

如果所选范围重叠，模块将视情况解析所选范围信息。例如，如果您指定多个有重叠的范围（如 `A1:B4,B1:E7`），模块会将所选范围解析为 A1 至 E7（包括 A1 和 E7）。

**所选内容/历史记录**包含此会话期间所选范围的列表。在您关闭**范围选择**后，该模块不存储范围。

使用**范围**参数的替代方法是通过点击  打开工作表。在工作表中，您可以通过在所需的值范围上拖动来选择数据范围。范围选择反映在**范围**参数文本框中。

要应用来自模块对话框的新范围，请点击**应用**。

##### 编程用法

|  |
| --- |
| **模块参数**：`Range` |
| **类型**：字符向量 |
| **值**：工作表中所用单元格的完整范围 | 以逗号分隔的 `column:row` 列表 |
| **默认值**：`''` |

#### **输出数据类型** — 输出数据类型 `Inherit: auto` (默认) | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | **fixdt(1,16,2^0,0)** | **Enum: <class\_name>** | **<数据类型表达式>**

From Spreadsheet 模块输出的数据类型。From Spreadsheet 模块接受包含多种数据类型的电子表格。但是，该模块将电子表格数据类型作为双精度读取。它随后根据**输出数据类型**的值输出数据类型。

如果您要为各个信号指定不同的数据类型，请考虑选择**输出数据类型** > **Inherit: auto**。此选项使用反向传播来解析反向信号数据类型。例如，假定 From Spreadsheet 模块中有两个信号 In1 和 In2，该模块将它们发送到具有 int8 和布尔数据类型的端口。通过反向传播，该模块将 In1 重新转换为 int8，将 In2 重新转换为布尔型。

要允许该模块转换输出数据类型以匹配接收模块的数据类型，请使用 **Inherit: auto**。

有关详细信息，请参阅控制信号的数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: auto' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'boolean' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | 'Enum: <class name>' | '<data type expression>'` |
| **默认值**：`'Inherit: auto'` |

#### **将第一列视为** — 时间或数据 **时间** (默认) | **数据**

选择模块应该如何处理电子表格的第一列：

- **时间** - 将第一列视为时间。
- **数据** - 将第一列视为数据。

##### 依赖关系

当您选择**数据**时，该模块禁用：

- **第一个数据点之前的数据外插**
- **时间范围内的数据插值**
- **末尾数据点后的数据外插**

并且启用：

- **最后一个数据点后的输出**

##### 编程用法

|  |
| --- |
| **模块参数**：`TreatFirstColumnAs` |
| **类型**：字符向量 |
| **值**：`'Time' | 'Data'` |
| **默认值**：`'Time'` |

#### **采样时间** — 采样周期和偏移量 `0` (默认) | 标量 | 向量

采样周期和偏移量。

From Spreadsheet 模块使用以下任一采样时间从电子表格中读取数据：

- 您为 From Spreadsheet 模块指定的采样时间
- From Spreadsheet 模块从目标模块（即 From Spreadsheet 模块将数据馈送到的模块）继承的采样时间

默认值为 `0`，指定的是连续采样时间。以模型的基础（最快）速率读取电子表格。有关详细信息，请参阅指定采样时间。

##### 编程用法

|  |
| --- |
| **参数：**`SampleTime` |
| **类型：**字符向量 |
| **值：**标量 | 向量 |
| **默认值：**`'0'` |

#### **第一个数据点之前的数据外插** — 在电子表格中的初始时间戳之前的仿真时间的外插方法 **线性外插** (默认) | **保持第一个值** | **接地值**

Simulink 针对电子表格中第一个时间戳之前的仿真时间点使用的外插法。选择下列外插方法之一。

| 方法 | 描述 |
| --- | --- |
| **线性外插** | （默认值）  如果电子表格只包含一个样本，则 From Spreadsheet 模块输出相应的数据值。  如果电子表格包含多个样本，则 From Spreadsheet 模块使用前两个样本进行线性外插：  - 对于 `double` 数据，使用前两个样本对值进行线性外插 - 对于 `Boolean` 数据，输出第一个数据值 - 对于除 `double` 或 `Boolean` 之外的内置数据类型：  - 将数据向上转换为 `double`   - 执行线性外插（如上针对 `double` 数据所述）   - 将外插的数据值向下转换为原始数据类型  不能将**线性外插**选项与枚举 (`enum`) 数据结合使用。 |
| **保持第一个值** | 使用文件中的第一个数据值 |
| **接地值** | 使用的值取决于电子表格样本数据值的数据类型：  - 定点数据类型 - 使用接地值 - 除定点之外的数值类型 - 使用 `0` - `Boolean` - 使用 `false` - 枚举数据类型 - 使用默认值 |

##### 依赖关系

要启用此参数，请将**将第一列视为**设置为**时间**。

##### 编程用法

|  |
| --- |
| **参数：**`ExtrapolationBeforeFirstDataPoint` |
| **类型：**字符向量 |
| **值：**`'Linear extrapolation' | 'Hold first value' | 'Ground value'` |
| **默认值：**`'Linear extrapolation'` |

#### **时间范围内的数据插值** — 电子表格中两个时间戳之间的仿真时间的插值方法 **线性插值** (默认) | **零阶保持**

Simulink 针对电子表格中的两个时间戳之间的仿真时间点使用的插值法。选择以下插值法之一。

| 方法 | 描述 |
| --- | --- |
| **线性插值** | （默认值）  From Spreadsheet 模块使用两个对应的电子表格样本进行插值：  - 对于 `double` 数据，使用两个对应样本进行线性插值 - 对于布尔数据，如果仿真时间在两个具有不同值的电子表格数据点之间，则 From Spreadsheet 模块会将值转换定位在这两个电子表格数据点的中间。例如，如果电子表格数据从 true 转换为 false，则在电子表格数据点转换间隔的前一半仿真时间中，From Spreadsheet 数据的输出值为 true。间隔的后半段仿真时间的输出值为 false。 - 对于除 `double` 或 `Boolean` 之外的内置数据类型：  - 将数据向上转换为 `double`   - 执行线性内插（如上针对 `double` 数据所述）   - 将插入的值向下转换为原始数据类型  不能将**线性插值**选项与枚举 (`enum`) 数据结合使用。 |
| **零阶保持** | 使用两个样本中第一个样本的数据 |

##### 依赖关系

要启用此参数，请将**将第一列视为**设置为**时间**。

##### 编程用法

|  |
| --- |
| **参数：**`InterpolationWithinTimeRange` |
| **类型：**字符向量 |
| **值：**`'Linear interpolation' | 'Zero order hold'` |
| **默认值：**`'Linear interpolation'` |

#### **末尾数据点后的数据外插** — 电子表格中最后一个时间戳之后的仿真时间的外插方法 **线性外插** (默认) | **保留最后一个值** | **接地值**

Simulink 针对电子表格中最后一个时间戳之后的仿真时间点使用的外插法。选择以下外插方法之一。

| 方法 | 描述 |
| --- | --- |
| **线性外插** | （默认值）  如果电子表格只包含一个样本，则 From Spreadsheet 模块输出相应的数据值。  如果电子表格包含多个样本，则 From Spreadsheet 模块使用最后两个样本的数据值进行线性外插：  - 对于 `double` 数据，使用最后两个样本对值进行外插。 - 对于 `Boolean` 数据，输出最后一个数据值 - 对于除 `double` 或 `Boolean` 之外的内置数据类型：  - 将数据向上转换为 `double`。   - 执行线性外插（如上针对 `double` 数据所述）。   - 将外插的值向下转换为原始数据类型。  不能将**线性外插**选项与枚举 (`enum`) 数据结合使用。 |
| **保留最后一个值** | 使用文件中的最后一个数据值 |
| **接地值** | 使用的值取决于电子表格样本数据值的数据类型：  - 定点数据类型 - 使用接地值 - 除定点之外的数值类型 - 使用 `0` - `Boolean` - 使用 `false` - 枚举数据类型 - 使用默认值 |

##### 依赖关系

要启用此参数，请将**将第一列视为**设置为**时间**。

##### 编程用法

|  |
| --- |
| **参数：**`ExtrapolationAfterLastDataPoint` |
| **类型：**字符向量 |
| **值：**`'Linear extrapolation' | 'Hold last value' | 'Ground value'` |
| **默认值：**`'Linear extrapolation'` |

#### **最后一个数据点后的输出** — 在读完最后一个数据点后的操作 **重复序列** (默认) | **保留最终值** | **接地值**

选择在读完最后一个数据点后的操作：

- **重复序列** - 从**范围**所指定范围的第一行开始，重复读取数据序列
- **保留最终值** - 在仿真的剩余时间段输出最后定义的值。
- **接地值** - 根据在**输出数据类型**中指定的数据类型值输出接地值。

##### 依赖关系

要启用此参数，请将**将第一列视为**设置为**数据**。

##### 编程用法

|  |
| --- |
| **参数：**`OutputAfterLastPoint` |
| **类型：**字符向量 |
| **值：**`'Repeating sequence' | 'Hold final value' | 'Ground value'` |
| **默认值：**`'Repeating sequence'` |

#### **启用过零检测** — 启用过零检测的选项 `off` (默认) | `on`

选择此项以启用过零检测。

仅当**采样时间**参数设置为 `0`（连续）时，过零检测 参数才适用。

此模块仅在使用变步长求解器的仿真中支持过零检测。当使用定步长求解器进行仿真时，软件不会检测或定位此模块的过零点。

Simulink 使用一种称为过零检测的技术来准确定位不连续性，无需借助于过小的时间步。在这种情况下，过零用于表示不连续性。

对于 From Spreadsheet 模块，过零检测只能在文件中时间戳所标记的时间点进行。Simulink 仅检查时间戳，不检查数据值。

如果输入数组包含重复的时间戳（多个条目具有相同的时间戳），Simulink 将在该时间戳处进行过零检测。例如，假设输入数组具有以下数据。

```
time:     0 1 2 2 3
signal:   2 3 4 5 6
```

在时间 2 处，存在由于输入信号不连续而产生的一个过零点。

对于没有重复时间戳的数据，过零检测取决于以下参数的设置：

- **第一个数据点之前的数据外插**
- **时间范围内的数据插值**
- **末尾数据点后的数据外插**

当模块确定在以下时间发生过零时，应用下面的规则：

- 第一个时间戳上发生过零
- 第一个和最后一个时间戳之间的时间戳上发生过零。
- 最后一个时间戳上发生过零

| 时间戳 | 发生过零检测时 |
| --- | --- |
| 第一个 | **第一个数据点之前的数据外插**设置为**接地值**。 |
| 第一个和最后一个之间 | **时间范围内的数据插值**设置为**零阶保持**。 |
| 最后一个 | 满足以下一项或两项设置：  - **末尾数据点后的数据外插**设置为**接地值**。 - **时间范围内的数据插值**设置为**零阶保持**。 |

该图显示了当 From Spreadsheet 模块具有以下设置时针对其所访问数据的过零检测：

- **第一个数据点之前的数据外插** - **线性外插**
- **时间范围内的数据插值**（用于内部点）- **零阶保持**
- **末尾数据点后的数据外插** - **线性外插**

Graph showing no zero crossing at the first point, zero crossing at each internal point, and zero crossing at the last point

该图说明对由 From Spreadsheet 模块访问的数据的过零检测。该模块具有以下时间戳（点）设置：

- **第一个数据点之前的数据外插** - **保持第一个值**
- **时间范围内的数据插值** - **零阶保持**
- **末尾数据点后的数据外插** - **保留最后一个值**

Graph showing no zero crossing at the first point, zero crossing at each internal point, and zero crossing at the last point

##### 编程用法

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

#### **模式** — 要指定的数据的类别 **继承** (默认) | **内置** | **定点** | **枚举** | **表达式**

选择要指定的数据类别。有关详细信息，请参阅控制信号的数据类型。

- **继承**

  数据类型的继承规则。选择 **inherit** 将在右侧启用另一个菜单/文本框。
- **内置**

  内置的数据类型。选择**内置**将在右侧启用另一个菜单/文本框。选择以下选项之一：

  - **double** - 默认值
  - **single**
  - **int8**
  - **uint8**
  - **int16**
  - **uint16**
  - **int32**
  - **uint32**
  - **int64**
  - **uint64**
  - **boolean**
- **定点** - 定点数据类型。
- **枚举** - 枚举数据类型。选择**枚举**将启用右侧的另一个菜单/文本框，您可以在其中输入类名称。
- **表达式** - 计算结果为数据类型的表达式。选择**表达式**将在右侧启用另一个菜单/文本框，您可以在其中输入表达式。

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

#### **定标** — 定标定点数据的方法 **二进制小数点** (默认) | **最佳精度** | **斜率和偏置**

指定定点数据的定标方法，以避免发生溢出情况并最大限度地减少量化误差。有关详细信息，请参阅指定定点数据类型。

##### 依赖关系

要启用此参数，请将**模式**设置为**定点**。

将**定标**设置为**二进制小数点**可启用：

- **小数长度**
- **计算最佳精度定标**

将**定标**设置为**斜率和偏置**可启用：

- **斜率**
- **偏置**
- **计算最佳精度定标**

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
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed pointa` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `是` |
|  |  |
| --- | --- |
| a 最高支持 32 位定点数据类型。 | |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

- 不建议用于生产代码。
- RSim 目标的代码生成提供与 Simulink 相同的支持；所有其他代码生成目标仅支持具有时间格式的数组中的一维双精度实信号。
- 在加速、快速加速、模型引用加速模式或模型引用快速加速模式下进行仿真与在普通模式下进行仿真具有相同的行为方式和要求。
- From Spreadsheet 模块不支持生成涉及编译 ERT 或 GRT 目标的代码，也不支持使用 SIL 或 PIL 仿真模式。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

支持多达 32 位的定点数据类型。

### 版本历史记录

**在 R2015b 中推出**

#### R2024a: From Spreadsheet 模块更新

From Spreadsheet 现在支持使用**文件名**的相对和完整路径进行仿真和代码生成。在 R2024a 之前的版本中，如果您为**文件名**指定相对路径，则 From Spreadsheet 模块会在代码生成期间将相对路径更改为完整路径。

#### R2022b: From Spreadsheet 在当前文件夹中搜索电子表格文件

如果在提供的完整路径中找不到电子表格文件，则 From Spreadsheet 模块现在会在当前文件夹中搜索电子表格文件。此更改使包含 From Spreadsheet 模块的 Simulink Compiler™ 独立可执行文件能够找到电子表格文件。在以前的版本中，From Spreadsheet 模块不在当前文件夹中查找电子表格文件。

#### R2022b: COM 的读取问题

`'LibXL'` 是 `set_param` 函数的 `'ReaderLibrary'` 参数的新值。

## Libraries

Simulink / Sources

## Description

The From Spreadsheet block reads data from Microsoft®
Excel® (all platforms) or CSV (Microsoft Windows® platform with Microsoft Office installed only) spreadsheets and outputs the data as a signal. The
From Spreadsheet block does not support Microsoft
Excel spreadsheet charts.

The From Spreadsheet icon displays the spreadsheet
file name and sheet name specified in the block **File name** and **Sheet name** parameters.

### Storage Formats

The data that the From Spreadsheet block reads from a spreadsheet
must be appropriately formatted.

For Microsoft
Excel spreadsheets:

- The From Spreadsheet block interprets the first row as a
  signal name. If you do not specify a signal name, the From
  Spreadsheet block assigns a default one with the format
  `Signal #`, where
  *`#`* increments with each additional unnamed
  signal.
- The From Spreadsheet block interprets the first column as
  time. In this column, the time values must monotonically increase.
- The From Spreadsheet block interprets the remaining columns
  as signals.

This example shows an acceptably formatted Microsoft
Excel spreadsheet. The first column is Time and the first row contains
signal names. Each worksheet contains a signal group.

For CSV text files (Microsoft platform with Microsoft Office installed only):

- The From Spreadsheet block interprets the first column as
  time. In this column, the time values must increase.
- The From Spreadsheet block interprets the remaining columns
  as signals.
- Each column must have the same number of entries.
- The From Spreadsheet block interprets each file as one
  signal group.

This example shows an acceptably formatted CSV file. The contents represent one
signal group.

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

The From Spreadsheet block does not accept signal values of
nonfinite data, such as `Nan`, `Inf`, or
`-Inf`.

### Block Behavior During Simulation

The From Spreadsheet block incrementally reads data from the spreadsheet during simulation.

The **Sample time** parameter specifies the
sample time that the From Spreadsheet block uses to
read data from the spreadsheet. For details, see Parameters. The time stamps in the file must be monotonically nondecreasing.

For each simulation time hit for which the spreadsheet contains
no matching time stamp, Simulink® software interpolates or extrapolates
to obtain the needed data using the selected method. For details,
see Simulation Time Hits That Have No Corresponding Spreadsheet Time Stamps.

### Simulation Time Hits That Have No Corresponding Spreadsheet Time Stamps

If the simulation time hit does not have a corresponding spreadsheet
time stamp, the From Spreadsheet block output depends on:

- Whether the simulation time hit occurs before the first time stamp, within the range of time stamps, or after the last time stamp
- The interpolation or extrapolation methods that you select
- The data type of the spreadsheet data

For details about interpolation and extrapolation options, see the descriptions of these
parameters:

- Data extrapolation before first data point
- Data interpolation within time range
- Data extrapolation after last data point

Sometimes the spreadsheet includes two or more data values that
have the same time stamp. In such cases, the From Spreadsheet block action depends on when the simulation time hit occurs, relative to the duplicate time stamps in the spreadsheet.

For example, suppose that the spreadsheet contains this data.
Three data values have a time stamp value of `2`.

```
time stamps:    0 1 2 2 2 3 4
data values:    2 3 6 4 9 1 5
```

The table describes the From Spreadsheet block output.

| Simulation Time, Relative to Duplicate Time Stamp Values in Spreadsheet | From Spreadsheet Block Action |
| --- | --- |
| Before the duplicate time stamps | Performs the same actions as when the time stamps are distinct, using the first of the duplicate time stamp values as the basis for interpolation. (In this example, the time stamp value is `6`.) |
| At or after the duplicate time stamps | Performs the same actions as when the times stamps are distinct, using the last of the duplicate time stamp values as the basis for interpolation. (In this example, that time stamp value is `9`.) |

### Read Issue with COM

By default, the From Spreadsheet block reads spreadsheets using the
Component Object Model (COM) interface on Windows platforms and the LibXL library on other platforms. If the From
Spreadsheet block has a problem reading the spreadsheet on Windows, use the `set_param` function to set
`'ReaderLibrary'` to `'LibXL'`. For
example:

```
set_param(blockPath,‘ReaderLibrary’,‘LibXL’);
```

where *blockPath* is the model block path.

## Ports

### Output

### **Port\_1** — Data from spreadsheet scalar | vector | matrix

Incremental data from the specified spreadsheet.

The **Sample time** parameter specifies the sample
time that the From Spreadsheet block uses to read data
from the spreadsheet. For details, see Parameters. The time
stamps in the file must be monotonically nondecreasing.

For each simulation time hit for which the spreadsheet contains no
matching time stamp, Simulink software interpolates or extrapolates to obtain the needed
data using the selected method. For details, see Simulation Time Hits That Have No Corresponding Spreadsheet Time Stamps.

The From Spreadsheet block accepts data type specifications at a block
level. If you want to specify different data types for each signal,
consider selecting **Output Data Type** > **Inherit: Auto**. This option resolves back signal data types using back
propagation. For example, assume that there are two signals in the
From Spreadsheet block, In1 and In2, which the block
sends to ports that have int8 and Boolean data types. With back
propagation, the block recasts In1 as int8 and In2 as Boolean.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

## Parameters

### **File name** — Full path and file name `untitled.xlsx` (default) | full path | relative path

Enter full path and file name of a spreadsheet file, including the file extension,
specified as a full path or relative path. Note:

This block supports non-English full paths and file names only on
Microsoft platforms.

**Tip**

- You can specify a full-path, relative path, or just the file
  name.

  - With both full path and relative path file names, the
    block supports simulation and code-generation.
  - If the file is not found, the block looks for the file
    in the current folder.
  - With just the file name, the block simulates. However,
    for code-generation, the block caches the full path. If
    the block cannot find the file, it searches in the
    current folder.
- If you do not include a file extension, the block assumes
  `.xlsx` as the extension.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `FileName` |
| **Type**: character vector |
| **Value**: full path and file name |
| **Default**: `'untitled.xlsx'` |

### **Sheet name** — Name of sheet in spreadsheet `Sheet1` (default) | sheet name

Enter the name of the sheet in the spreadsheet. You can type the sheet name in this edit
box or select the sheet name after you open the sheet.

If your spreadsheet is the CSV format, the block populates this parameter with the name
of the CSV file without the extension. Do not change this value.

To open the sheet, click . In the sheet, you can select the range
of data by dragging over the desired range of values.

Alternatively, you can select the range of data by specifying the range of
values in the **Range** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SheetName` |
| **Type**: character vector |
| **Value**: Sheet name |
| **Default**: `'Sheet1'` |

### **Range** — Cell range entire range of used cells in sheet (default) | comma-separated list of `column:row`

To specify the range, use the format
`column:row`,
with multiple specifications separated by commas. For example,
`A1:B3,D1:D3,A7:B9,D7:D9`. If unspecified, or empty,
the block automatically detects the used range, which is all the data in the
sheet.

If the selections overlap, the block resolves the selection information as
appropriate. For example, if you specify multiple ranges that overlap, such
as `A1:B4,B1:E7`, the block resolves the selection to A1 to
E7, inclusive.

**Selection/History** contains the list of selected
ranges during this session. The block does not store the ranges after you
close **Range Selection**.

An alternate to using the **Range** parameter is to open the sheet, by
clicking . In the sheet, you can select the range
of data by dragging over the desired range of values. The range selection
reflects in the **Range** parameter text box.

To apply a new range from the block dialog, click
**Apply**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Range` |
| **Type**: character vector |
| **Value**: entire range of used cells in sheet | comma-separated list of `column:row` |
| **Default**: `''` |

### **Output data type** — Output data type `Inherit: auto` (default) | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class_name>` | `<data type expression>`

The data type for the From Spreadsheet block output. The
From Spreadsheet block accepts spreadsheets that contain
many data types. However, the block reads the spreadsheet data type as
doubles. It then outputs the data type according to the value of
**Output data type**.

If you want to specify different data types for each signal, consider
selecting **Output Data Type** > **Inherit: auto**. This option resolves back signal data types using back
propagation. For example, assume that there are two signals in the
From Spreadsheet block, In1 and In2, which the block
sends to ports that have int8 and Boolean data types. With back propagation,
the block recasts In1 as int8 and In2 as boolean.

To allow the block to cast the output data type to match that of the receiving block, use
`Inherit: auto`.

For more information, see Control Data Types of Signals.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: auto' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'boolean' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | 'Enum: <class name>' | '<data type expression>'` |
| **Default**: `'Inherit: auto'` |

### **Treat first column as** — Time or data `Time` (default) | `Data`

Select how the block should treat the first column of the
spreadsheet:

- `Time` — Treat first column as
  time.
- `Data` — Treat first column as
  data.

#### Dependencies

When you select `Data`, the block
disables:

- **Data extrapolation before first data
  point**
- **Data interpolation within time
  range**
- **Data extrapolation after last data
  point**

And enables:

- **Output after last data point**

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `TreatFirstColumnAs` |
| **Type**: character vector |
| **Value**: `'Time' | 'Data'` |
| **Default**: `'Time'` |

### **Sample time** — Sampling period and offset `0` (default) | scalar | vector

The sample period and offset.

The From Spreadsheet block reads data from a spreadsheet using a sample
time that either:

- You specify for the From Spreadsheet block
- The From Spreadsheet block inherits from the blocks into which the
  From Spreadsheet block feeds data

The default is `0`, which specifies a continuous sample
time. The spreadsheet is read at the base (fastest) rate of the model. For
details, see Specify Sample Time.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `SampleTime` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'0'` |

### **Data extrapolation before first data point** — Extrapolation method for simulation times before initial time stamp in spreadsheet `Linear extrapolation` (default) | `Hold first value` | `Ground value`

Extrapolation method that Simulink uses for a simulation time hit that is before the first time
stamp in the spreadsheet. Choose one of these extrapolation methods.

| Method | Description |
| --- | --- |
| `Linear extrapolation` | (Default)  If the spreadsheet contains only one sample, the From Spreadsheet block outputs the corresponding data value.  If the spreadsheet contains more than one sample, the From Spreadsheet block linearly extrapolates using the first two samples:  - For `double` data, linearly   extrapolates the value using the first two   samples - For `Boolean` data, outputs   the first data value - For a built-in data type other than   `double` or   `Boolean`:  - Upcasts the data to     `double`   - Performs linear extrapolation (as described     above for `double` data)   - Downcasts the extrapolated data value to the     original data type  You cannot use the `Linear extrapolation` option with enumerated (`enum`) data. |
| `Hold first value` | Uses the first data value in the file |
| `Ground value` | Uses a value that depends on the data type of spreadsheet sample data values:  - Fixed-point data types — Uses the   ground value - Numeric types other than fixed–point —   Uses `0` - `Boolean` — Uses   `false` - Enumerated data types — Uses default   value |

#### Dependencies

To enable this parameter, set **Treat first column
as** to `Time`.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `ExtrapolationBeforeFirstDataPoint` |
| **Type:** character vector |
| **Values:** `'Linear extrapolation' | 'Hold first value' | 'Ground value'` |
| **Default:** `'Linear extrapolation'` |

### **Data interpolation within time range** — Interpolation method for simulation times that fall between two time stamps in spreadsheet `Linear interpolation` (default) | `Zero order hold`

The interpolation method that Simulink uses for a simulation time hit between two time stamps in the
spreadsheet. Choose one of the following interpolation methods.

| Method | Description |
| --- | --- |
| `Linear interpolation` | (Default)  The From Spreadsheet block interpolates using the two corresponding spreadsheet samples:  - For `double` data, linearly   interpolates the value using the two corresponding   samples - For Boolean data, if the simulation time is   between two spreadsheet data points with different   values, the From Spreadsheet block   positions the value transition halfway between the   spreadsheet data points. For example, if the   spreadsheet data transitions from true to false,   the From Spreadsheet data provides   an output value of true for simulation times in   the first half of the interval between the   spreadsheet data points. It provides an output   value of false for simulation times in the latter   half of the interval. - For a built-in data type other than   `double` or   `Boolean`:  - Upcasts the data to     `double`   - Performs linear interpolation (as described     above for `double` data)   - Downcasts the interpolated value to the     original data type  You cannot use the `Linear interpolation` option with enumerated (`enum`) data. |
| `Zero order hold` | Uses the data from the first of the two samples |

#### Dependencies

To enable this parameter, set **Treat first column
as** to `Time`.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `InterpolationWithinTimeRange` |
| **Type:** character vector |
| **Values:** `'Linear interpolation' | 'Zero order hold'` |
| **Default:** `'Linear interpolation'` |

### **Data extrapolation after last data point** — Extrapolation method for simulation times after last time stamp in spreadsheet `Linear extrapolation` (default) | `Hold last value` | `Ground value`

The extrapolation method that Simulink uses for a simulation time hit that is after the last time
stamp in the spreadsheet. Choose one of the following extrapolation
methods.

| Method | Description |
| --- | --- |
| `Linear extrapolation` | (Default)  If the spreadsheet contains only one sample, the From Spreadsheet block outputs the corresponding data value.  If the spreadsheet contains more than one sample, the From Spreadsheet block linearly extrapolates using data values of the last two samples:  - For `double` data,   extrapolates the value using the last two   samples - For `Boolean` data, outputs   the last data value - For a built-in data type other than   `double` or   `Boolean`:  - Upcasts the data to     `double`.   - Performs linear extrapolation (as described     above for `double` data).   - Downcasts the extrapolated value to the     original data type.  You cannot use the `Linear extrapolation` option with enumerated (`enum`) data. |
| `Hold last value` | Uses the last data value in the file |
| `Ground value` | Uses a value that depends on the data type of spreadsheet sample data values:  - Fixed-point data types — Uses the   ground value - Numeric types other than fixed–point —   uses `0` - `Boolean` — Uses   `false` - Enumerated data types — Uses default   value |

#### Dependencies

To enable this parameter, set **Treat first column
as** to `Time`.

#### Programmatic Use

|  |
| --- |
| **Parameter:**  `ExtrapolationAfterLastDataPoint` |
| **Type:**  character vector |
| **Values:** `'Linear extrapolation' | 'Hold last value' | 'Ground value'` |
| **Default:** `'Linear extrapolation'` |

### **Output after last data point** — Action after last data point `Repeating sequence` (default) | `Hold final value` | `Ground value`

Select action after last data point:

- `Repeating sequence` — Repeat the
  sequence by reading the data from the first row of the range
  specified in **Range**
- `Hold final value` — Output the last
  defined value for the remainder of the simulation.
- `Ground value` — Output a ground value
  depending on the data type value specified in **Output data
  type**.

#### Dependencies

To enable this parameter, set **Treat first column
as** to `Data`.

#### Programmatic Use

|  |
| --- |
| **Parameter:**  `OutputAfterLastPoint` |
| **Type:**  character vector |
| **Values:** `'Repeating sequence' | 'Hold final value' | 'Ground value'` |
| **Default:** `'Repeating sequence'` |

### **Enable zero-crossing detection** — Option to enable zero-crossing detection `off` (default) | `on`

Select to enable zero-crossing detection.

The Zero-Crossing Detection
parameter applies only if the **Sample time** parameter is
set to `0` (continuous).

This block supports zero-crossing detection only in simulations
that use a variable-step solver. When you use a fixed-step solver for simulation, the software
does not detect or locate zero crossings for this block.

Simulink uses a technique known as zero-crossing detection to locate
accurately a discontinuity, without resorting to excessively small time
steps. In this context, zero-crossing is used to represent
discontinuities.

For the From Spreadsheet block, zero-crossing detection can
only occur at time stamps in the file. Simulink examines only the time stamps, not the data values.

If the input array contains duplicate time stamps (more than one entry
with the same time stamp), Simulink detects a zero crossing at that time stamp. For example,
suppose that the input array has this data.

```
time:     0 1 2 2 3
signal:   2 3 4 5 6
```

At time 2, there is a zero crossing from the input signal
discontinuity.

For data with nonduplicate time stamps, zero-crossing detection depends on
the settings of the following parameters:

- **Data extrapolation before first data
  point**
- **Data interpolation within time range**
- **Data extrapolation after last data
  point**

The block applies the following rules when determining when:

- Zero-crossing occurs for the first time stamp
- For time stamps between the first and last time stamp
- For the last time stamp

| Time Stamp | When Zero-Crossing Detection Occurs |
| --- | --- |
| First | **Data extrapolation before first data point** is set to `Ground value`. |
| Between first and last | **Data interpolation within time range** is set to `Zero-order hold`. |
| Last | One or both of these settings occur:  - **Data extrapolation after last data   point** is set to `Ground   value`. - **Data interpolation within time   range** is set to `Zero-order   hold`. |

The figure illustrates zero-crossing detection for data accessed by a
From Spreadsheet block that has these settings:

- **Data extrapolation before first data point**
  — `Linear extrapolation`
- **Data interpolation within time range** (for
  internal points) — `Zero order
  hold`
- **Data extrapolation after last data point**
  — `Linear extrapolation`

Graph showing no zero crossing at the first point, zero crossing at each internal point, and zero crossing at the last point

The figure illustrates zero-crossing detection for data accessed by a
From Spreadsheet block. The block has these settings for
the time stamps (points):

- **Data extrapolation before first data point**
  — `Hold first value`
- **Data interpolation within time range** —
  `Zero order hold`
- **Data extrapolation after last data point**
  — `Hold last value`

Graph showing no zero crossing at the first point, zero crossing at each internal point, and zero crossing at the last point

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ZeroCross` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Mode** — Category of data to specify `Inherit` (default) | `Built in` | `Fixed point` | `Enumerated` | `Expression`

Select the category of data to specify. For more information, see Control Data Types of Signals.

- `Inherit`

  Inheritance rule for data types. Selecting
  `Inherit` enables a second menu/text
  box to the right.
- `Built in`

  Built-in data types. Selecting `Built in` enables a second
  menu/text box to the right. Select one of these choices:

  - `double` —
    Default
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
- `Fixed point` — Fixed-point data
  types.
- `Enumerated` — Enumerated data
  types. Selecting `Enumerated` enables a
  second menu/text box to the right, where you can enter the class
  name.
- `Expression` — Expression that
  evaluates to a data type. Selecting
  `Expression` enables a second menu/text
  box to the right, where you enter the expression.

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

### **Scaling** — Method for scaling fixed-point data `Binary point` (default) | `Best precision` | `Slope and bias`

Specify the method for scaling your fixed-point data to avoid overflow
conditions and minimize quantization errors. For more information, see
Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

Setting **Scaling** to `Binary
point` enables:

- **Fraction length**
- **Calculate Best-Precision
  Scaling**

Setting **Scaling** to `Slope and
bias` enables:

- **Slope**
- **Bias**
- **Calculate Best-Precision
  Scaling**

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
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed pointa` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |
|  |  |
| --- | --- |
| a Supports up to 32-bit fixed-point data types. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

- Not recommended for production code.
- Code generation for RSim target provides identical support as Simulink;
  all other code generation targets support only double, one-dimensional, real
  signals in array with time format.
- Simulating in accelerator, rapid accelerator, model reference accelerator
  mode, or model reference rapid accelerator mode behaves the same way, and
  has the same requirements, as simulating in normal mode.
- The From Spreadsheet block does not support generating code
  that involves building ERT or GRT targets, or using SIL or PIL simulation
  modes.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Supports up to 32-bit fixed-point data types.

## Version History

**Introduced in R2015b**

### R2024a: From Spreadsheet Block Updates

The From Spreadsheet now supports relative and full paths for
**File name** for simulation and code
generation. In releases prior to R2024a, if you specified a relative path for
**File name**, the From Spreadsheet block
changed the relative path to the full path during code generation.

### R2022b: From Spreadsheet Searches for Spreadsheet File Within Current Folder

The From Spreadsheet block now searches for the spreadsheet file
within the current folder if it cannot find the spreadsheet file in the full path
provided. This change enables Simulink
Compiler™ standalone executables containing From Spreadsheet
blocks to find spreadsheet files. In previous releases, the From
Spreadsheet block did not look for spreadsheet files in current
folders.

### R2022b: Read Issue with COM

`'LibXL'` is a new value for the `'ReaderLibrary'`
parameter of the `set_param` function.
