---
type: simulink-block
title: 'From File'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'fromfile'
documentation_source_path: 'slref/fromfile.html'
language: zh-CN
chinese_source: worker-translation
---

# From File

## 端口

### 输出

### **Port\_1** — 使用 MAT 文件数据创建的输出 标量 | 向量 | 矩阵 | 数组

使用从指定 MAT 文件加载的数据创建的输出。根据所加载的数据，输出可能是标量或多维信号，也可能是非虚拟总线。From File 模块支持加载所有内置数据类型的实数和复数数据，但 `half`、`int64` 和 `uint64` 除外。

From File 模块不支持为总线数组加载数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`
**复数支持：** 是

## 参数

### **File name** — MAT 文件名或 MAT 文件路径 `untitled.mat`（默认）| MAT 文件名 | MAT 文件路径

包含要加载数据的 MAT 文件名或 MAT 文件路径。当文件不在 MATLAB 路径或当前工作目录中时，请指定该文件的路径。

您可以在文本框中键入路径或文件名，也可以通过点击 **Browse for a MAT-file** 按钮浏览到该 MAT 文件。在 UNIX® 系统上，路径可以以波浪号（~）开头，表示您的主文件夹。

您不能从模型在同一次仿真中记录数据的文件加载数据。

#### 提示

- From File 模块支持从使用 To File 模块创建的文件加载数据，无需对数据或文件进行任何修改。
- 要确定当前工作目录，请在 MATLAB 命令窗口中输入 `pwd`。
- 有关使用 From File 模块进行 C/C++ 代码生成的数据要求的信息，请参阅 Code Generation。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `FileName` |
| **值**：| `'untitled.mat'`（默认）| MAT 文件名 | MAT 文件路径 |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mdl/From
File","FileName","InputData.mat")` 将模型 `mdl` 中名为 `From File` 的 From File 模块配置为从文件 `InputData.mat` 加载输入数据。

### **Output data type** — MAT 文件中数据的数据类型 `Inherit: auto`（默认）| `double` | `single` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class_name>` | `Bus: <bus_object>` | `<data type expression>` | ...

From File 模块加载的 MAT 文件中数据的数据类型。默认情况下，From File 模块从文件中的数据或从为该信号定义数据类型的下游模块继承输出信号数据类型。如果 MAT 文件中数据的数据类型与继承的数据类型不匹配，软件将报错。

当您为标量或多维信号加载数据时，您可以选择继承输出数据类型，也可以指定输出数据类型以匹配 MAT 文件中数据的数据类型。

要加载总线的数据，请将 **Output data type** 设置为 `Bus: <bus object>`，并指定定义输出总线的 `Simulink.Bus` 对象的名称。

要加载枚举数据，请将 **Output data type** 设置为 `Enum: <class name>`，并指定定义枚举数据值的枚举类的名称。

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `OutDataTypeStr` |
| **值**：| `'Inherit (auto)'`（默认）| `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'Enum: <class name>'` | `'Bus: <object name>'` | `'<data type expression>'` |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mdl/From
File","OutputDataTypestr","double")` 将模型 `mdl` 中名为 `From File` 的 From File 模块配置为从包含 `double` 信号值的 MAT 文件加载数据，并生成数据类型为 `double` 的信号。

### **Sample time** — 输出采样周期和可选时间偏移 `0` | 标量 | `1`×`2` 向量

**Sample time** 参数指定模块在仿真期间计算新输出值的时间。有关详细信息，请参阅 Specify Sample Time。

当您不希望输出具有时间偏移时，请将 **Sample time** 参数指定为标量。要为输出添加时间偏移，请将 **Sample time** 参数指定为 `1`×`2` 向量，其中第一个元素是采样周期，第二个元素是偏移量。

默认情况下，**Sample time** 参数值为 `0`，表示无时间偏移的连续采样时间。对于离散信号，请将采样时间指定为离散采样间隔。例如，将采样时间指定为 `0.1` 以对每 100ms 采样的离散信号进行建模。将采样时间指定为 `-1` 以继承该值。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **值**：| `'0'`（默认）| 标量 | `1`×`2` 向量 |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mdl/From
File","SampleTime","-1")` 将模型 `mdl` 中名为 `From File` 的 From File 模块配置为继承其采样时间。

### **Data extrapolation before first data point** — 确定 MAT 文件中第一个数据点之前模块输出的方法 `Linear extrapolation`（默认）| `Hold first value` | `Ground value`

用于确定 MAT 文件数据中第一个样本之前仿真时间输出值的外推方法。

| 方法 | 描述 | 示例 |
| --- | --- | --- |
| `Linear extrapolation` | 模块确定输出值的方式取决于 MAT 文件中数据的类型。  - 对于 `double` 数据，From File 模块使用前两个样本对输出值进行线性外推。 - 对于 `Boolean` 数据，From File 模块使用 MAT 文件数据中的第一个值作为输出值。 - 对于所有其他内置数据类型，From File 模块：  1. 将数据向上转型为 `double`。   2. 使用 MAT 文件数据中的前两个样本对输出值进行线性外推。   3. 将外推的数据值向下转型为原始数据类型。  如果 MAT 文件数据仅包含一个样本，From File 模块将在输出端提供该值。 当 From File 模块加载枚举或定点数据时，请勿使用 `Linear extrapolation` 选项。 外推设置应用于总线中的所有信号。如果总线中的任何信号包含枚举或定点数据，请勿使用 `Linear extrapolation` 选项。 | 显示配置为对加载数据中第一个样本之前的仿真时间输出值进行线性外推的 From File 模块输出的绘图。该模块加载从仿真开始 2 秒后开始的数据。 |
| `Hold first value` | From File 模块使用 MAT 文件中的第一个数据值作为输出值。 | 显示配置为对加载数据中第一个样本之前的仿真时间保持加载数据中第一个值的 From File 模块输出的绘图。该模块加载从仿真开始 2 秒后开始的数据。 |
| `Ground value` | From File 模块输出值取决于 MAT 文件中数据的类型。  - 内置数值类型 — `0` - `Boolean` — `false` - 定点数据类型 — 值 `0` 的表示，由于缩放和有限精度，可能不完全是 `0`。 - 枚举数据类型 — 默认值 | 显示配置为对加载数据中第一个样本之前的仿真时间使用接地值作为输出值的 From File 模块输出的绘图。该模块加载从仿真开始 2 秒后开始的数据。 |

#### 提示

要生成构建 ERT 或 GRT 目标或使用 SIL 或 PIL 仿真模式的代码，请将 **Data extrapolation before first data point** 指定为 `Linear extrapolation`。有关使用 From File 模块进行 C/C++ 代码生成的详细信息，请参阅 Code Generation。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `ExtrapolationBeforeFirstDataPoint` |
| **值**：| `'Linear extrapolation'`（默认）| `'Hold first value'` | `'Ground value'` |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mdl/From
File","ExtrapolationBeforeFirstDataPoint","Hold first
value")` 将模型 `mdl` 中名为 `From File` 的 From File 模块配置为通过保持文件中的第一个值来外推文件中第一个值之前的值。

### **Data interpolation within time range** — 插值方法 `Linear interpolation`（默认）| `Zero order hold`

用于确定 MAT 文件数据中样本之间仿真时间输出值的插值方法。

| 方法 | 描述 | 示例 |
| --- | --- | --- |
| `Linear interpolation` | 模块确定输出值的方式取决于 MAT 文件中数据的类型。  - 对于 `double` 数据，From File 模块使用需要输出值的仿真时间之前和之后的数据值对输出值进行线性插值。 - 对于所有其他内置数值数据类型，From File 模块：  1. 将数据向上转型为 `double`。   2. 使用需要输出值的仿真时间之前和之后的 MAT 文件数据值对输出值进行线性插值。   3. 将外推的数据值向下转型为原始数据类型。 - 对于 `Boolean` 数据，如果仿真时间介于两个具有不同值的工作区数据点之间，From File 模块将值转换定位在 MAT 文件数据点的中点。例如，如果数据从 `true` 转换为 `false`，From File 模块在 MAT 文件数据点之间间隔的前半段仿真时间提供输出值 `true`，在间隔的后半段仿真时间提供输出值 `false`。  如果 MAT 文件数据仅包含一个样本，From File 模块将在输出端提供该值。 当 From File 模块加载枚举或定点数据时，请勿使用 `Linear interpolation` 选项。 插值设置应用于总线中的所有信号。如果总线中的任何信号包含枚举数据，请勿使用 `Linear interpolation` 选项。 | 显示配置为对加载数据中样本之间的仿真时间输出值进行线性插值的 From File 模块输出的绘图。 |
| `Zero order hold` | From File 模块将每个数据值从一个样本保持到下一个样本。MAT 文件数据中两个样本之间的仿真时间的输出值是紧邻该仿真时间之前的样本的值。 | 显示配置为对加载数据中样本之间的仿真时间使用零阶保持插值的 From File 模块输出的绘图。 |

#### 提示

要生成构建 ERT 或 GRT 目标或使用 SIL 或 PIL 仿真模式的代码，请将 **Data interpolation within time range** 指定为 `Linear interpolation`。有关使用 From File 模块进行 C/C++ 代码生成的详细信息，请参阅 Code Generation。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `InterpolationWithinTimeRange` |
| **值**：| `'Linear interpolation'`（默认）| `'Zero order hold'` |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mdl/From
File","InterpolationWithinTimeRange","Zero order
hold")` 将模型 `mdl` 中名为 `From File` 的 From File 模块配置为使用零阶保持插值。

### **Data extrapolation after last data point** — 确定 MAT 文件中最后一个数据点之后模块输出的方法 `Linear extrapolation`（默认）| `Hold last value` | `Ground value`

用于确定 MAT 文件数据中最后一个样本之后仿真时间输出值的外推方法。

| 方法 | 描述 | 示例 |
| --- | --- | --- |
| `Linear extrapolation` | 模块确定输出值的方式取决于 MAT 文件中数据的类型。  - 对于 `double` 数据，From File 模块使用 MAT 文件中的最后两个样本对输出值进行线性外推。 - 对于 `Boolean` 数据，From File 模块使用 MAT 文件中的样本值作为输出值。 - 对于所有其他内置数据类型，From File 模块：  1. 将数据向上转型为 `double`。   2. 使用 MAT 文件数据中的最后两个样本对输出值进行线性外推。   3. 将外推的数据值向下转型为原始数据类型。  如果 MAT 文件数据仅包含一个样本，From File 模块将该值用作输出。 当 From File 模块加载枚举或定点数据时，请勿使用 `Linear extrapolation` 选项。 外推设置应用于总线中的所有信号。如果总线中的任何信号包含枚举数据，请勿使用 `Linear extrapolation` 选项。 | 显示配置为对加载数据中最后一个样本之后的仿真时间输出值进行线性插值的 From File 模块输出的绘图。该模块加载在仿真结束前 2 秒结束的数据。 |
| `Hold last value` | From File 模块使用 MAT 文件中的最后一个数据值作为输出值。 | 显示配置为对加载数据中最后一个样本之后的仿真时间保持最后一个输出值的 From File 模块输出的绘图。该模块加载在仿真结束前 2 秒结束的数据。 |
| `Ground value` | From File 模块输出值取决于 MAT 文件中数据的类型。  - 内置数值类型 — `0` - `Boolean` — `false` - 定点数据类型 — 值 `0` 的表示，由于缩放和有限精度，可能不完全是 `0`。 - 枚举数据类型 — 默认值 | 显示配置为对加载数据中最后一个样本之后的仿真时间使用接地值作为输出值的 From File 模块输出的绘图。该模块加载在仿真结束前 2 秒结束的数据。 |

#### 提示

要生成构建 ERT 或 GRT 目标或使用 SIL 或 PIL 仿真模式的代码，请将 **Data extrapolation after last data point** 指定为 `Linear extrapolation`。有关使用 From File 模块进行 C/C++ 代码生成的详细信息，请参阅 Code Generation。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `ExtrapolationAfterLastDataPoint` |
| **值**：| `'Linear extrapolation'`（默认）| `'Hold last value'` | `'Ground value'` |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mdl/From
File","ExtrapolationAfterLastDataPoint","Hold last
value")` 将模型 `mdl` 中名为 `From File` 的 From File 模块配置为通过保持文件中的最后一个值来外推文件中最后一个值之后的值。

### **Enable zero-crossing detection** — 用于为此模块启用零交叉检测的选项 `off`（默认）| `on`

零交叉检测用于定位模块输出中的不连续点，即*零交叉*，并防止变步长求解器在不连续点附近采用过小的时间步长，从而避免拖慢仿真速度。当 **Sample time** 参数设置为 `0` 以表示连续采样时间时，From File 模块可以检测零交叉。

当数据包含多个具有相同时间的采样点时，加载的数据会在模块输出中产生不连续点。例如，对于以下输入数据，不连续点出现在时间 `2` 处。

```
time:     0 1 2 2 3
signal:   2 3 4 5 6
```

From File 模块还可以根据您配置插值和外推的方式来在输出中产生不连续点。

- 将 **Data extrapolation before first data point** 设置为 `Ground value` 会在加载数据中的第一个采样点处产生不连续点。
- 将 **Data extrapolation after the last data point** 设置为 `Ground value` 会在加载数据中的最后一个采样点处产生不连续点。
- 将 **Data interpolation within time range** 设置为 `Zero-order hold` 会在加载数据中的每个采样点处产生不连续点，包括最后一个采样点。

此模块仅在使用变步长求解器的仿真中支持零交叉检测。当您使用定步长求解器进行仿真时，软件不会为此模块检测或定位零交叉。

有关详细信息，请参阅 Zero-Crossing Detection。

#### 提示

要生成构建 ERT 或 GRT 目标或使用 SIL 或 PIL 仿真模式的代码，请清除此复选框。有关使用 From File 模块生成 C/C++ 代码的详细信息，请参阅 Code Generation。

#### 编程使用

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `ZeroCross` |
| **值**：| `'on'`（默认）| `'off'` |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mdl/From File","ZeroCross","off")` 将模型 `mdl` 中名为 `From File` 的 From File 模块配置为禁用零交叉检测。

## 所属库

Simulink / Sources

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed pointa` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |
|  |  |
| --- | --- |
| a 支持最高 32 位定点数据类型。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不建议用于生产代码。

为 RSim 目标生成代码没有特殊要求或限制。所有其他代码生成目标仅支持从 MAT 文件中的数组加载实数、双精度、一维信号数据，其中第一列包含时间数据，后续列包含信号数据。生成构建 ERT 或 GRT 目标或使用 SIL 或 PIL 仿真模式的代码要求：

- 加载的 MAT 文件包含一个至少有两行且不包含 `NaN`、`Inf` 或 `-Inf` 值的数组。
- **Data extrapolation before first data point** 和 **Data extrapolation after last data point** 参数设置为 `Linear extrapolation`。
- **Data interpolation within time range** 参数设置为 `Linear interpolation`。
- **Enable zero-crossing detection** 参数已清除。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

From File 模块支持最高 32 位的定点数据类型。

## 版本历史

**在 R2006a 之前引入**

## 描述

将 MAT 文件中的数据加载到 Simulink 模型中

From File 模块从 MAT 文件读取数据到 Simulink® 模型中，并将该数据作为信号或非虚拟总线提供到模块输出。您可以从位于 MATLAB® 路径上或路径外的 MAT 文件加载数据。一个模型可以包含多个 From File 模块，它们从同一个 MAT 文件加载数据。

您可以指定模块如何根据文件中的数据构造输出，包括输出的采样时间、插值和外推行为，以及是否使用零交叉检测。

From File 模块图标显示为该模块提供数据的 MAT 文件的名称。例如，如果您使用 From File 模块从文件 `myData.mat` 加载数据，则该模块显示 `myData.mat`。

### MAT 文件数据

From File 模块可以从存储在 `timeseries` 对象中的 MAT 文件加载数据，也可以从数组中加载数据，其中第一行包含时间数据，后续行包含标量或向量信号的数据。加载存储在 `timeseries` 对象中的数据支持更广泛的数据和输出类型，并要求 MAT 文件为版本 7.3。

| 数据注意事项 | `timeseries` 格式 | 数组格式 |
| --- | --- | --- |
| 时间数据要求 | - 数据类型必须为 `double` - 值必须单调递增 | - 数据类型必须为 `double` - 值必须单调递增 |
| 支持的信号数据类型 | - 除 `half`、`int64` 和 `uint64` 之外的任何内置数据类型 - 枚举数据类型 - 字长最高为 32 位的定点数据类型 | `double` |
| 信号数据复数性 | 实数或复数 | 实数 |
| 信号数据要求 | 不得包含 `NaN`、`Inf` 或 `-Inf` 值 | 不得包含 `NaN`、`Inf` 或 `-Inf` 值 |
| 输出类型 | - 标量、向量或多维信号 - 总线 | 标量或向量信号 |
| MAT 文件版本 | 版本 7.3 | 所有版本 |

无论 MAT 文件包含多少个变量，From File 模块仅从 MAT 文件中的一个变量加载数据。当您从包含多个变量的版本 7.3 MAT 文件加载数据时，From File 模块加载按字母顺序排在第一位的变量中的数据。版本 7.0 及更早版本的 MAT 文件所使用的排序算法更为复杂，因此当您从版本 7.0 或更早版本的 MAT 文件加载数据时，请确保该 MAT 文件仅包含单个变量的数据。

**注意**

使用 `Array` 格式记录输出、状态或连接到 To Workspace 模块的信号时，生成的数组格式与 From File 模块所期望的格式不同。在用于记录的 `Array` 格式中，第一列包含时间值；而在用于 From File 模块的数组格式中，第一行包含时间值。From File 模块和 To File 模块使用相同的数组格式。

### MAT 文件版本

MAT 文件的版本也会影响 From File 模块加载数据的方式。当您从版本 7.3 MAT 文件加载数据时，数据会在仿真期间增量加载。当您从版本 7.0 或更早版本的 MAT 文件加载数据时，所有数据会在仿真开始时加载到内存中。

要将 MAT 文件转换为版本 7.3，请使用 `load` 函数将版本 7.0 或更早版本 MAT 文件中的数据加载到基础工作区。然后，使用 `save` 函数将数据保存为版本 7.3 MAT 文件，并将版本指定为 `'-v7.3'`。例如，以下命令将包含变量 `inputData` 的文件 `myData.mat` 转换为版本 7.3。

```
load("myData.mat");
save("myData.mat","inputData","-v7.3");
```

有关详细信息，请参阅 MAT-File Versions。
