---
type: simulink-block
title: 'From File'
family: sources
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'fromfile'
---

# From File

Load data from MAT file into Simulink model

## 中文

将 MAT 文件中的数据加载到 Simulink 模型中

### 所属库

Simulink / Sources

### 描述

From File 模块将数据从 MAT 文件读入 Simulink® 模型，并在模块输出端以信号或非虚拟总线形式提供数据。您可以从 MATLAB® 路径中或路径外的 MAT 文件加载数据。模型可以包含多个从同一个 MAT 文件加载数据的 From File 模块。

您可以指定模块如何从文件中的数据构造输出，包括输出的采样时间、内插和外插行为，以及是否使用过零检测。

From File 模块图标显示向模块提供数据的 MAT 文件的名称。例如，如果使用 From File 模块从文件 `myData.mat` 加载数据，该模块将显示 `myData.mat`。

#### MAT 文件数据

From File 模块可以从存储在 `timeseries` 对象或数组中的 MAT 文件加载数据，其中第一行包含时间数据，后续行包含标量或向量信号的数据。加载存储在 `timeseries` 对象中的数据时，支持更广泛的数据和输出类型，但要求 MAT 文件是 7.3 版。

| 数据注意事项 | `timeseries` 格式 | 数组格式 |
| --- | --- | --- |
| 时间数据要求 | - 数据类型必须为 `double` - 值必须单调递增 | - 数据类型必须为 `double` - 值必须单调递增 |
| 支持的信号数据类型 | - 除 `half`、`int64` 和 `uint64` 之外的任何内置数据类型 - 枚举数据类型 - 最长 32 位字长的定点数据类型 | `double` |
| 信号数据复/实性 | 实数或复数 | 实数 |
| 信号数据要求 | 不能包含 `NaN`、`Inf` 或 `-Inf` 值 | 不能包含 `NaN`、`Inf` 或 `-Inf` 值 |
| 输出的类型 | - 标量、向量或多维信号 - 总线 | 标量或向量信号 |
| MAT 文件版本 | 版本 7.3 | 所有版本 |

From File 模块只从 MAT 文件中的一个变量加载数据，而不管该 MAT 文件包含多少个变量。当您从包含多个变量的 7.3 版 MAT 文件中加载数据时，From File 模块会将数据加载到按字母顺序排列的第一个变量中。7.0 版和更早版本的 MAT 文件使用的排序算法更加复杂，因此当您从 7.0 版或更早版本的 MAT 文件加载数据时，请确保 MAT 文件只包含单个变量的数据。

**注意**

使用**数组**格式记录连接到 To Workspace 模块的输出、状态或信号会生成与 From File 模块预期的格式不同的数组。在用于记录的**数组**格式中，第一列包含时间值，在 From File 模块的数组格式中，第一行包含时间值。From File 模块和 To File 模块使用相同的数组格式。

#### MAT 文件版本

MAT 文件的版本也会影响 From File 模块加载数据的方式。当您从 7.3 版 MAT 文件加载数据时，在仿真期间，数据将以增量方式加载。当您从 7.0 版或更早版本的 MAT 文件加载数据时，在仿真启动时，所有数据都会加载到内存中。

要将 MAT 文件转换为 7.3 版，请使用 `load` 函数将 7.0 版或更早版本的 MAT 文件中的数据加载到基础工作区中。然后，使用 `save` 函数且将版本指定为 `'-v7.3'` 将数据保存为 7.3 版的 MAT 文件。例如，以下命令将包含变量 `inputData` 的文件 `myData.mat` 转换为 7.3 版。

```
load("myData.mat");
save("myData.mat","inputData","-v7.3");
```

有关详细信息，请参阅MAT 文件版本。

### 端口

#### 输出

#### **Port\_1** — 使用 MAT 文件数据创建的输出 标量 | 向量 | 矩阵 | 数组

使用从指定的 MAT 文件加载的数据创建的输出。根据您加载的数据，输出可能是标量、多维信号或非虚拟总线。From File 模块支持加载除 `half`、`int64` 和 `uint64` 之外的所有内置数据类型的实数和复数数据。

From File 模块不支持为总线数组加载数据。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`
**复数支持:** 是

### 参数

#### **文件名** — MAT 文件名或 MAT 文件的路径 `untitled.mat` (默认) | MAT 文件名 | MAT 文件的路径

包含要加载的数据的 MAT 文件的 MAT 文件名或路径。当文件不在 MATLAB 路径上或当前工作目录中时，请指定文件的路径。

您可以在文本框中键入路径或文件名，或通过点击**浏览到一个 MAT 文件**按钮  浏览到 MAT 文件。在 UNIX® 系统上，路径可以用波浪号 (~) 开头，表示这是您的主文件夹。

在同一个仿真中，您无法从模型将数据记录到其中的文件加载数据。

##### 提示

- From File 模块支持从使用 To File 模块创建的文件加载数据，而无需对数据或文件进行任何修改。
- 要确定当前工作目录，请在 MATLAB 命令行窗口中输入 `pwd`。
- 有关使用 From File 模块生成 C/C++ 代码的数据要求的信息，请参阅代码生成。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `FileName` |
| **值:** | `'untitled.mat'` (默认) | MAT file name | path to MAT file |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("mdl/From File","FileName","InputData.mat")` configures the From File block named `From File` in the model `mdl` to load input data from the file `InputData.mat`.

#### **输出数据类型** — MAT 文件中数据的数据类型 `Inherit: auto` (默认) | `double` | `single` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | **Enum: <class\_name>** | **Bus: <bus\_object>** | **<数据类型表达式>** | ...

From File 模块加载的 MAT 文件中数据的数据类型。默认情况下，From File 模块从文件中的数据或从定义信号数据类型的下游模块继承输出信号数据类型。如果 MAT 文件中数据的数据类型与继承的数据类型不匹配，则软件会引发一个错误。

加载标量或多维信号数据时，可以选择继承输出数据类型，也可以指定输出数据类型以匹配 MAT 文件中数据的数据类型。

要加载总线数据，请将**输出数据类型**设置为 **Bus: <bus object>**，并指定定义输出总线的 `Simulink.Bus` 对象的名称。

要加载枚举数据，请将**输出数据类型**设置为 **Enum: <class name>**，并指定定义枚举数据值的枚举类的名称。

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `OutDataTypeStr` |
| **值:** | `'Inherit (auto)'` (默认) | `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'Enum: <class name>'` | `'Bus: <object name>'` | `'<data type expression>'` |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("mdl/From File","OutputDataTypestr","double")` configures the From File block named `From File` in the model `mdl` to load data from a MAT file that contains `double` signal values and produce a signal with `double` data type.

#### **采样时间** — 输出采样周期和可选时间偏移量 `0` | 标量 | `1`×`2` 向量

**采样时间**参数指定模块在仿真期间计算新输出值的时间。有关详细信息，请参阅指定采样时间。

当您不希望输出具有时间偏移量时，请将**采样时间**参数指定为标量。要向输出添加时间偏移量，请将**采样时间**参数指定为 `1`×`2` 向量，其中第一个元素是采样周期，第二个元素是偏移量。

默认情况下，**采样时间**参数值为 `0`，表示没有时间偏移量的连续采样时间。对于离散信号，请将采样时间指定为离散采样间隔。例如，将采样时间指定为 `0.1` 以对每 100 毫秒采样一次的离散信号建模。将采样时间指定为 `-1` 以继承该值。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SampleTime` |
| **值:** | `'0'` (默认) | scalar | `1`-by-`2` vector |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("mdl/From File","SampleTime","-1")` configures the From File block named `From File` in the model `mdl` to inherit its sample time.

#### **第一个数据点之前的数据外插** — 在 MAT 文件中第一个数据点之前确定模块输出的方法 **线性外插** (默认) | **保持第一个值** | **接地值**

用于确定在 MAT 文件数据中第一个采样之前仿真时间的输出值的外插方法。

| 方法 | 描述 | 示例 |
| --- | --- | --- |
| **线性外插** | 模块如何确定输出值取决于 MAT 文件中数据的类型。  - 对于 `double` 数据，From File 模块使用前两个采样对输出值进行线性外插。 - 对于 `Boolean` 数据，From File 模块使用 MAT 文件数据中的第一个值作为输出值。 - 对于所有其他内置数据类型，From File 模块：  1. 将数据向上转换为 `double`。   2. 使用 MAT 文件数据中的前两个采样对输出值进行线性外插。   3. 将外插的数据值向下转换为原始数据类型。  如果 MAT 文件数据只包含一个采样，则 From File 模块在输出端提供该值。  当 From File 模块加载枚举或定点数据时，请不要使用**线性外插**选项。  外插设置将应用于总线中的所有信号。如果总线中有任一信号包含枚举或定点数据，请不要使用**线性外插**选项。 | Plot that shows the output for a From File block configured to linearly extrapolate the output value for simulation times before the first sample in the loaded data. The block loads data that starts 2 seconds into the simulation. |
| **保持第一个值** | From File 模块使用 MAT 文件中的第一个数据值作为输出值。 | Plot that shows the output for a From File block configured to hold the first value in the loaded data for simulation times before the first sample in the loaded data. The block loads data that starts 2 seconds into the simulation. |
| **接地值** | From File 模块输出值取决于 MAT 文件中数据的类型。  - 内置数值类型 - `0` - `Boolean` — `false` - 定点数据类型 - 值 `0` 的表示，因为要进行定标且精度有限，该值可能不会精确为 `0`。 - 枚举数据类型 - 默认值 | Plot that shows the output for a From File block configured to use the ground value as the output value for simulation times before the first sample in the loaded data. The block loads data that starts 2 seconds into the simulation. |

##### 提示

要生成构建 ERT 或 GRT 目标或使用 SIL 或 PIL 仿真模式的代码，请将**第一个数据点之前的数据外插**指定为**线性外插**。有关使用  From File 模块的 C/C++ 代码生成的详细信息，请参阅 代码生成。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ExtrapolationBeforeFirstDataPoint` |
| **值:** | `'Linear extrapolation'` (默认) | `'Hold first value'` | `'Ground value'` |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("mdl/From File","ExtrapolationBeforeFirstDataPoint","Hold first value")` configures the From File block named `From File` in the model `mdl` to extrapolate values before the first value in the file by holding the first value in the file.

#### **时间范围内的数据插值** — 插值方法 **线性插值** (默认) | **零阶保持**

用于确定 MAT 文件数据中采样之间仿真时间的输出值的插值方法。

| 方法 | 描述 | 示例 |
| --- | --- | --- |
| **线性插值** | 模块如何确定输出值取决于 MAT 文件中数据的类型。  - 对于 `double` 数据，From File 模块使用需要输出值的仿真时间前后的数据值对输出值进行线性插值。 - 对于所有其他内置数值数据类型，From File 模块：  1. 将数据向上转换为 `double`。   2. 使用需要输出值的仿真时间前后的 MAT 文件数据值对输出值进行线性插值。   3. 将外插的数据值向下转换为原始数据类型。 - 对于 `Boolean` 数据，如果仿真时间在两个具有不同值的工作区数据点之间，则 From File 模块会将值转换定位在 MAT 文件数据点的中间。例如，如果数据从 `true` 转换为 `false`，则 From File 模块为 MAT 文件数据点之间的前半段区间的仿真时间提供输出值 `true`，为后半段区间的仿真时间提供输出值 `false`。  如果 MAT 文件数据只包含一个采样，则 From File 模块在输出端提供该值。  当 From File 模块加载枚举或定点数据时，请不要使用**线性插值**选项。  插值设置将应用于总线中的所有信号。如果总线中有任一信号包含枚举数据，请不要使用**线性插值**选项。 | Plot that shows the output for a From File block configured to linearly interpolate the output value for simulation times between the samples in the loaded data. |
| **零阶保持** | From File 模块会将每一采样的数据值保持到下一个采样。MAT 文件数据中两个采样之间的仿真时间的输出值是仿真时间之前的采样的值。 | Plot that shows the output for a From File block configured to use zero-order-hold interpolation for simulation times between the samples in the loaded data. |

##### 提示

要生成构建 ERT 或 GRT 目标或使用 SIL 或 PIL 仿真模式的代码，请将**时间范围内的数据插值**指定为**线性插值**。有关使用 From File 模块的 C/C++ 代码生成的详细信息，请参阅代码生成。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `InterpolationWithinTimeRange` |
| **值:** | `'Linear interpolation'` (默认) | `'Zero order hold'` |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("mdl/From File","InterpolationWithinTimeRange","Zero order hold")` configures the From File block named `From File` in the model `mdl` to use zero order hold interpolation.

#### **末尾数据点后的数据外插** — 确定 MAT 文件中最后一个数据点之后的模块输出的方法 **线性外插** (默认) | **保留最后一个值** | **接地值**

用于确定 MAT 文件数据中最后一个采样后仿真时间的输出值的外插方法。

| 方法 | 描述 | 示例 |
| --- | --- | --- |
| **线性外插** | 模块如何确定输出值取决于 MAT 文件中数据的类型。  - 对于 `double` 数据，From File 模块使用 MAT 文件中的最后两个采样对输出值进行线性外插。 - 对于 `Boolean` 数据，From File 模块使用 MAT 文件中的采样值作为输出值。 - 对于所有其他内置数据类型，From File 模块：  1. 将数据向上转换为 `double`。   2. 使用 MAT 文件数据中的最后两个采样对输出值进行线性外插。   3. 将外插的数据值向下转换为原始数据类型。  如果 MAT 文件数据只包含一个采样，则 From File 模块使用该值作为输出。  当 From File 模块加载枚举或定点数据时，请不要使用**线性外插**选项。  外插设置将应用于总线中的所有信号。如果总线中有任一信号包含枚举数据，请不要使用**线性外插**选项。 | Plot that shows the output for a From File block configured to linearly interpolate the output value for simulation times after the last sample in the loaded data. The block loads data that ends 2 seconds before the end of the simulation. |
| **保留最后一个值** | From File 模块使用 MAT 文件中的最后一个数据值作为输出值。 | Plot that shows the output for a From File block configured to hold the last output value for simulation times after the last sample in the loaded data. The block loads data that ends 2 seconds before the end of the simulation. |
| **接地值** | From File 模块输出值取决于 MAT 文件中数据的类型。  - 内置数值类型 - `0` - `Boolean` — `false` - 定点数据类型 - 值 `0` 的表示，因为要进行定标且精度有限，该值可能不会精确为 `0`。 - 枚举数据类型 - 默认值 | Plot that shows the output for a From File block configured to use the ground value as the output value for simulation times after the last sample in the loaded data. The block loads data that ends 2 seconds before the end of the simulation. |

##### 提示

要生成构建 ERT 或 GRT 目标或使用 SIL 或 PIL 仿真模式的代码，请将**末尾数据点后的数据外插**指定为**线性外插**。有关使用 From File 模块的 C/C++ 代码生成的详细信息，请参阅代码生成。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ExtrapolationAfterLastDataPoint` |
| **值:** | `'Linear extrapolation'` (默认) | `'Hold last value'` | `'Ground value'` |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("mdl/From File","ExtrapolationAfterLastDataPoint","Hold last value")` configures the From File block named `From File` in the model `mdl` to extrapolate values after the last value in the file by holding the last value in the file.

#### **启用过零检测** — 用于对此模块启用过零检测的选项 `off` (默认) | `on`

过零检测可定位模块输出中的不连续点，即*过零点*，并防止变步长求解器在不连续点附近使用过小的时间步（这种情况下可能会减慢仿真速度）。对于连续采样时间，当**采样时间**参数设置为 `0` 时，From File 模块可以检测过零点。

当数据包含时间相同的多个采样时，加载的数据会在模块输出中产生不连续点。例如，对于此输入数据，在时间 `2` 处出现不连续点。

```
time:     0 1 2 2 3
signal:   2 3 4 5 6
```

From File 模块还会根据您如何配置内插和外插在输出中产生不连续点。

- 将**第一个数据点之前的数据外插**设置为**接地值**会在所加载数据的第一个采样处产生不连续点。
- 将**最后一个数据点之后的数据外插**设置为**接地值**会在所加载数据的最后一个采样处产生不连续点。
- 将**时间范围内的数据插值**设置为**零阶保持**会在所加载数据的每个采样（包括最后一个采样）处产生不连续点。

此模块仅在使用变步长求解器的仿真中支持过零检测。当使用定步长求解器进行仿真时，软件不会检测或定位此模块的过零点。

有关详细信息，请参阅过零检测。

##### 提示

要生成用于编译 ERT 或 GRT 目标或使用 SIL 或 PIL 仿真模式的代码，请清除此复选框。有关使用 From File 模块的 C/C++ 代码生成的详细信息，请参阅代码生成。

##### 编程用法

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ZeroCross` |
| **值:** | `'on'` (默认) | `'off'` |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("mdl/From File","ZeroCross","off")` configures the From File block named `From File` in the model `mdl` to disable zero-crossing detection.

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed pointa` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `是` |
|  |  |
| --- | --- |
| a 最高支持 32 位定点数据类型。 | |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不建议用于生产代码。

为 RSim 目标生成代码没有特殊要求或限制。所有其他代码生成目标仅支持从 MAT 文件中的数组加载双精度实数一维信号数据，其中第一列包含时间数据，后续列包含信号数据。生成用于编译 ERT 或 GRT 目标的代码时，或者使用 SIL 或 PIL 仿真模式时，都要求：

- 加载的 MAT 文件包含一个有至少两行且没有 `NaN`、`Inf` 或 `-Inf` 值的数组。
- **第一个数据点之前的数据外插**和**末尾数据点后的数据外插**参数设置为**线性外插**。
- **时间范围内的数据插值**参数设置为**线性插值**。
- **启用过零检测**参数处于清除状态。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

From File 模块支持最多 32 位的定点数据类型。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Sources

## Description

The From File block reads data into a Simulink® model from a MAT file and provides the data as a signal or nonvirtual bus
at the block output. You can load data from a MAT file that is on or off the MATLAB® path. A model can contain multiple From File blocks that
load data from the same MAT file.

You can specify how the block constructs the output from the data in the file, including the
sample time for the output, interpolation and extrapolation behavior, and whether to use
zero-crossing detection.

The From File block icon shows the name of the MAT file that supplies the
data to the block. For example, if you use the From File block to load
data from the file `myData.mat`, the block displays
`myData.mat`.

### MAT File Data

The From File block can load data from a MAT file that is stored in
a `timeseries` object or in an array where the first row contains
time data and subsequent rows contain data for a scalar or vector signal. Loading
data stored in a `timeseries` object supports a wider range of data
and output types and requires that the MAT file is Version 7.3.

| Data Consideration | `timeseries` Format | Array Format |
| --- | --- | --- |
| Time data requirements | - Data type must be `double` - Values must increase monotonically | - Data type must be `double` - Values must increase monotonically |
| Supported signal data types | - Any built-in data types except   `half`, `int64`, and   `uint64` - Enumerated data type - Fixed-point data type with up to a 32-bit word   length | `double` |
| Signal data complexity | Real or complex | Real |
| Signal data requirements | Must not contain `NaN`, `Inf`, or `-Inf` values | Must not contain `NaN`, `Inf`, or `-Inf` values |
| Type of output | - Scalar, vector, or multidimensional signal - Bus | Scalar or vector signal |
| MAT file version | Version 7.3 | All versions |

The From File block loads data from only one variable in the MAT file,
regardless of the number of variables the MAT file contains. When you load data from
a Version 7.3 MAT file that contains multiple variables, the From
File block loads the data in the variable that is first alphabetically.
The ordering algorithm used by Version 7.0 and earlier MAT files is more
complicated, so ensure that the MAT file only contains data for a single variable
when you load data from a Version 7.0 or earlier MAT file.

**Note**

Logging outputs, states, or a signal connected to a To
Workspace block using the `Array` format
generates an array in a different format than the From File block
expects. In the `Array` format for logging, the first
column contains time values, and in the array format for the From
File block, the first row contains time values. The From
File block and To File block use the same array
format.

### MAT File Version

The version of the MAT file also affects how the From File block
loads the data. When you load data from a Version 7.3 MAT file, data is loaded
incrementally during simulation. When you load data from a Version 7.0 or earlier
MAT file, all the data is loaded into memory at the start of simulation.

To convert a MAT file to Version 7.3, use the `load` function to load the data in
the Version 7.0 or earlier MAT file into the base workspace. Then, save the data to
a Version 7.3 MAT file using the `save` function with the version
specified as `'-v7.3'`. For example, these commands convert the
file `myData.mat` that contains the variable
`inputData` to Version
7.3.

```
load("myData.mat");
save("myData.mat","inputData","-v7.3");
```

For more information, see MAT-File Versions.

## Ports

### Output

### **Port\_1** — Output created using MAT file data scalar | vector | matrix | array

Output created using data loaded from the specified MAT file. Depending on the data you
load, the output might be a scalar or multidimensional signal or a
nonvirtual bus. The From File block supports loading real
and complex data of all built-in data types except
`half`, `int64`, and
`uint64`.

The From File block does not support loading data for
an array of buses.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`
**Complex Number Support:** Yes

## Parameters

### **File name** — MAT file name or path to MAT file `untitled.mat` (default) | MAT file name | path to MAT file

MAT file name or path to MAT file with data you want to load. Specify the
path to the file when the file is not on the MATLAB path or in the current working directory.

You can type the path or file name into the text box, or you can browse to the MAT file
by clicking the **Browse for a MAT-file** button
. On UNIX® systems, the path can start with a tilde (~), which indicates
your home folder.

You cannot load data from a file to which the model logs data in the same
simulation.

#### Tips

- The From File block supports loading data from
  a file created using a To File block without any
  modification to the data or file.
- To determine the current working directory, enter
  `pwd` into the MATLAB Command Window.
- For information about data requirements for C/C++ code
  generation with the From File block, see Code Generation.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `FileName` |
| **Values:** | `'untitled.mat'` (default) | MAT file name | path to MAT file |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mdl/From
File","FileName","InputData.mat")` configures the From
File block named `From File` in the model
`mdl` to load input data from the file
`InputData.mat`.

### **Output data type** — Data type of data in MAT file `Inherit: auto` (default) | `double` | `single` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class_name>` | `Bus: <bus_object>` | `<data type expression>` | ...

Data type of the data in the MAT file loaded by the From
File block. By default, the From File block
inherits the output signal data type from the data in the file or from a
downstream block that defines the data type for the signal. The software
issues an error if the data type of the data in the MAT file does not match
the inherited data type.

When you load data for a scalar or multidimensional signal, you can choose
to inherit the output data type, or you can specify the output data type to
match the data type of the data in the MAT file.

To load data for a bus, set the **Output data type** to
`Bus: <bus object>` and specify the name
of the `Simulink.Bus` object that
defines the output bus.

To load enumerated data, set the **Output data type** to
`Enum: <class name>` and specify the name of
the enumeration class that defines the enumerated data values.

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutDataTypeStr` |
| **Values:** | `'Inherit (auto)'` (default) | `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'Enum: <class name>'` | `'Bus: <object name>'` | `'<data type expression>'` |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mdl/From
File","OutputDataTypestr","double")` configures the
From File block named `From File` in the model
`mdl` to load data from a MAT file that
contains `double` signal values and produce a
signal with `double` data type.

### **Sample time** — Output sample period and optional time offset `0` | scalar | `1`-by-`2` vector

The **Sample time** parameter specifies when the block
computes a new output value during simulation. For details, see Specify Sample Time.

Specify the **Sample time** parameter as a scalar when
you do not want the output to have a time offset. To add a time offset to
the output, specify the **Sample time** parameter as a
`1`-by-`2` vector where the first
element is the sampling period and the second element is the offset.

By default, the **Sample time** parameter value is `0`,
which indicates continuous sample time with no time offset. For a discrete
signal, specify the sample time as the discrete sampling interval. For
example, specify the sample time as `0.1` to model a
discrete signal sampled every 100ms. Specify the sample time as
`-1` to inherit the value.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `'0'` (default) | scalar | `1`-by-`2` vector |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mdl/From
File","SampleTime","-1")` configures the From File
block named `From File` in the model
`mdl` to inherit its sample
time.

### **Data extrapolation before first data point** — Method to determine block output before first data point in MAT file `Linear extrapolation` (default) | `Hold first value` | `Ground value`

Extrapolation method used to determine output values for simulation times before the
first sample in the MAT file data.

| Method | Description | Example |
| --- | --- | --- |
| `Linear extrapolation` | How the block determines the output value depends on the type of data in the MAT file.  - For `double` data, the   From File block linearly   extrapolates the output value using the first two   samples. - For `Boolean` data, the   From File block uses the first   value in MAT file data for the output   value. - For all other built-in data types, the   From File block:  1. Upcasts the data to      `double`.   2. Linearly extrapolates the output value using      the first two samples in the MAT file data.   3. Downcasts the extrapolated data value to the      original data type.  If the MAT file data only contains one sample, the From File block provides that value at the output.  Do not use the `Linear extrapolation` option when the From File block loads enumerated or fixed-point data.  The extrapolation setting is applied to all signals in a bus. If any signal in the bus contains enumerated or fixed-point data, do not use the `Linear extrapolation` option. | Plot that shows the output for a From File block configured to linearly extrapolate the output value for simulation times before the first sample in the loaded data. The block loads data that starts 2 seconds into the simulation. |
| `Hold first value` | The From File block uses the first data value in the MAT file as the output value. | Plot that shows the output for a From File block configured to hold the first value in the loaded data for simulation times before the first sample in the loaded data. The block loads data that starts 2 seconds into the simulation. |
| `Ground value` | The From File block output value depends on the type of data in the MAT file.  - Built-in numeric types —   `0` - `Boolean` —   `false` - Fixed-point data types — Representation for   value of `0`, which may not be   exactly `0` due to scaling and   limited precision. - Enumerated data types — Default value | Plot that shows the output for a From File block configured to use the ground value as the output value for simulation times before the first sample in the loaded data. The block loads data that starts 2 seconds into the simulation. |

#### Tips

To generate code that builds ERT or GRT targets or uses SIL or PIL
simulation modes, specify **Data extrapolation before first data
point** as `Linear extrapolation`.
For more information about C/C++ code generation with the  From
File block, see Code Generation.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ExtrapolationBeforeFirstDataPoint` |
| **Values:** | `'Linear extrapolation'` (default) | `'Hold first value'` | `'Ground value'` |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mdl/From
File","ExtrapolationBeforeFirstDataPoint","Hold first
value")` configures the From File block named
`From File` in the model `mdl`
to extrapolate values before the first value in the file by holding
the first value in the file.

### **Data interpolation within time range** — Interpolation method `Linear interpolation` (default) | `Zero order hold`

Interpolation method used to determine output values for simulation times
between samples in the MAT file data.

| Method | Description | Example |
| --- | --- | --- |
| `Linear interpolation` | How the block determines the output value depends on the type of data in the MAT file.  - For `double` data, the   From File block linearly   interpolates the output value using data values   before and after the simulation time that needs an   output value. - For all other built-in numeric data types, the   From File block:  1. Upcasts the data to      `double`.   2. Linearly interpolates the output value using      the MAT file data values before and after the      simulation time that needs an output value.   3. Downcasts the extrapolated data value to the      original data type. - For `Boolean` data, if the   simulation time is between two workspace data   points with different values, the From   File block positions the value transition   halfway between the MAT file data points. For   example, if the data transitions from   `true` to   `false`, the From   File block provides an output value of   `true` for simulation times in   the first half of the interval between the MAT   file data points and an output value of   `false` for simulation times in   the latter half of the interval.  If the MAT file data only contains one sample, the From File block provides that value at the output.  Do not use the `Linear interpolation` option when the From File block loads enumerated or fixed-point data.  The interpolation setting is applied to all signals in a bus. If any signal in the bus contains enumerated data, do not use the `Linear interpolation` option. | Plot that shows the output for a From File block configured to linearly interpolate the output value for simulation times between the samples in the loaded data. |
| `Zero order hold` | The From File block holds each data value from one sample to the next. The output value for a simulation time between two samples in the MAT file data is the value of the sample that precedes the simulation time. | Plot that shows the output for a From File block configured to use zero-order-hold interpolation for simulation times between the samples in the loaded data. |

#### Tips

To generate code that builds ERT or GRT targets or uses SIL or PIL
simulation modes, specify **Data interpolation within time
range** as `Linear interpolation`.
For more information on C/C++ code generation with the From
File block, see Code Generation.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `InterpolationWithinTimeRange` |
| **Values:** | `'Linear interpolation'` (default) | `'Zero order hold'` |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mdl/From
File","InterpolationWithinTimeRange","Zero order
hold")` configures the From File block named
`From File` in the model `mdl`
to use zero order hold interpolation.

### **Data extrapolation after last data point** — Method to determine block output after final data point in MAT file `Linear extrapolation` (default) | `Hold last value` | `Ground value`

Extrapolation method used to determine output values for simulation times
after the last sample in the MAT file data.

| Method | Description | Example |
| --- | --- | --- |
| `Linear extrapolation` | How the block determines the output value depends on the type of data in the MAT file.  - For `double` data, the   From File block linearly   extrapolates the output value using the last two   samples in the MAT file. - For `Boolean` data, the   From File block uses the sample   value in MAT file for the output value. - For all other built-in data types, the   From File block:  1. Upcasts the data to      `double`.   2. Linearly extrapolates the output value using      the last two samples in the MAT file data.   3. Downcasts the extrapolated data value to the      original data type.  If the MAT file data only contains one sample, the From File block uses that value as the output.  Do not use the `Linear extrapolation` option when the From File block loads enumerated or fixed-point data.  The extrapolation setting is applied to all signals in a bus. If any signal in the bus contains enumerated data, do not use the `Linear extrapolation` option. | Plot that shows the output for a From File block configured to linearly interpolate the output value for simulation times after the last sample in the loaded data. The block loads data that ends 2 seconds before the end of the simulation. |
| `Hold last value` | The From File block uses the last data value in the MAT file as the output value. | Plot that shows the output for a From File block configured to hold the last output value for simulation times after the last sample in the loaded data. The block loads data that ends 2 seconds before the end of the simulation. |
| `Ground value` | The From File block output value depends on the type of data in the MAT file.  - Built-in numeric types —   `0` - `Boolean` —   `false` - Fixed-point data types — Representation for   value of `0`, which may not be   exactly `0` due to scaling and   limited precision. - Enumerated data types — Default value | Plot that shows the output for a From File block configured to use the ground value as the output value for simulation times after the last sample in the loaded data. The block loads data that ends 2 seconds before the end of the simulation. |

#### Tips

To generate code that builds ERT or GRT targets or uses SIL or PIL
simulation modes, specify **Data extrapolation after last data
point** as `Linear extrapolation`.
For more information on C/C++ code generation with the From
File block, see Code Generation.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ExtrapolationAfterLastDataPoint` |
| **Values:** | `'Linear extrapolation'` (default) | `'Hold last value'` | `'Ground value'` |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mdl/From
File","ExtrapolationAfterLastDataPoint","Hold last
value")` configures the From File block named
`From File` in the model `mdl`
to extrapolate values after the last value in the file by holding
the last value in the file.

### **Enable zero-crossing detection** — Option to enable zero-crossing detection for this block `off` (default) | `on`

Zero-crossing detection locates discontinuities, or *zero
crossings*, in the block output and prevents variable-step
solvers from taking excessively small time steps near the discontinuities,
which can slow down a simulation. The From File block can
detect zero crossings when the **Sample time** parameter is
set to `0` for continuous sample time.

The loaded data creates a discontinuity in the block output when the data
includes multiple samples with the same time. For example, for this input
data, a discontinuity occurs at time
`2`.

```
time:     0 1 2 2 3
signal:   2 3 4 5 6
```

The From File block can also create discontinuities in the
output based on how you configure interpolation and extrapolation.

- Setting **Data extrapolation before first data
  point** to `Ground value`
  can create a discontinuity at the first sample in the loaded
  data.
- Setting **Data extrapolation after the last data
  point** to `Ground value`
  can create a discontinuity at the last sample in the loaded
  data.
- Setting **Data interpolation within time
  range** to `Zero-order
  hold` creates a discontinuity at each sample in
  the loaded data, including the last.

This block supports zero-crossing detection only in simulations
that use a variable-step solver. When you use a fixed-step solver for simulation, the software
does not detect or locate zero crossings for this block.

For more information, see Zero-Crossing Detection.

#### Tips

To generate code that builds ERT or GRT targets or uses SIL or PIL
simulation modes, clear this check box. For more information on C/C++
code generation with the From File block, see Code Generation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ZeroCross` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'on'` |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ZeroCross` |
| **Values:** | `'on'` (default) | `'off'` |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mdl/From
File","ZeroCross","off")` configures the From File
block named `From File` in the model
`mdl` to disable zero-crossing
detection.

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed pointa` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |
|  |  |
| --- | --- |
| a Supports up to 32-bit fixed-point data types. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code.

Generating code for an RSim target has no special requirements or limitations. All other
code generation targets support loading only real, double, one-dimensional signal
data from an array in a MAT file where the first column contains time data and
subsequent columns contain the signal data. Generating code that builds ERT or GRT
targets or uses SIL or PIL simulation modes requires that:

- The loaded MAT file contains an array with at least two rows and no
  `NaN`, `Inf`, or
  `-Inf` values.
- The **Data extrapolation before first data point** and
  **Data extrapolation after last data point** parameters
  are set to `Linear extrapolation`.
- The **Data interpolation within time range** parameter is
  set to `Linear interpolation`.
- The **Enable zero-crossing detection** parameter is
  cleared.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

The From File block supports fixed-point data types up to 32 bits.

## Version History

**Introduced before R2006a**
