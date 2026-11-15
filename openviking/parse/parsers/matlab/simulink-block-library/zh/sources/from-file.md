---
type: simulink-block
title: 'From File'
family: sources
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'fromfile'
language: zh-CN
chinese_source: official
---

# From File

将 MAT 文件中的数据加载到 Simulink 模型中

## 所属库

Simulink / Sources

## 描述

From File 模块将数据从 MAT 文件读入 Simulink® 模型，并在模块输出端以信号或非虚拟总线形式提供数据。您可以从 MATLAB® 路径中或路径外的 MAT 文件加载数据。模型可以包含多个从同一个 MAT 文件加载数据的 From File 模块。

您可以指定模块如何从文件中的数据构造输出，包括输出的采样时间、内插和外插行为，以及是否使用过零检测。

From File 模块图标显示向模块提供数据的 MAT 文件的名称。例如，如果使用 From File 模块从文件 `myData.mat` 加载数据，该模块将显示 `myData.mat`。

### MAT 文件数据

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

### MAT 文件版本

MAT 文件的版本也会影响 From File 模块加载数据的方式。当您从 7.3 版 MAT 文件加载数据时，在仿真期间，数据将以增量方式加载。当您从 7.0 版或更早版本的 MAT 文件加载数据时，在仿真启动时，所有数据都会加载到内存中。

要将 MAT 文件转换为 7.3 版，请使用 `load` 函数将 7.0 版或更早版本的 MAT 文件中的数据加载到基础工作区中。然后，使用 `save` 函数且将版本指定为 `'-v7.3'` 将数据保存为 7.3 版的 MAT 文件。例如，以下命令将包含变量 `inputData` 的文件 `myData.mat` 转换为 7.3 版。

```
load("myData.mat");
save("myData.mat","inputData","-v7.3");
```

有关详细信息，请参阅MAT 文件版本。

## 端口

### 输出

### **Port\_1** — 使用 MAT 文件数据创建的输出 标量 | 向量 | 矩阵 | 数组

使用从指定的 MAT 文件加载的数据创建的输出。根据您加载的数据，输出可能是标量、多维信号或非虚拟总线。From File 模块支持加载除 `half`、`int64` 和 `uint64` 之外的所有内置数据类型的实数和复数数据。

From File 模块不支持为总线数组加载数据。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`
**复数支持:** 是

## 参数

### **文件名** — MAT 文件名或 MAT 文件的路径 `untitled.mat` (默认) | MAT 文件名 | MAT 文件的路径

包含要加载的数据的 MAT 文件的 MAT 文件名或路径。当文件不在 MATLAB 路径上或当前工作目录中时，请指定文件的路径。

您可以在文本框中键入路径或文件名，或通过点击**浏览到一个 MAT 文件**按钮  浏览到 MAT 文件。在 UNIX® 系统上，路径可以用波浪号 (~) 开头，表示这是您的主文件夹。

在同一个仿真中，您无法从模型将数据记录到其中的文件加载数据。

#### 提示

- From File 模块支持从使用 To File 模块创建的文件加载数据，而无需对数据或文件进行任何修改。
- 要确定当前工作目录，请在 MATLAB 命令行窗口中输入 `pwd`。
- 有关使用 From File 模块生成 C/C++ 代码的数据要求的信息，请参阅代码生成。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `FileName` |
| **值:** | `'untitled.mat'` (默认) | MAT file name | path to MAT file |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("mdl/From File","FileName","InputData.mat")` configures the From File block named `From File` in the model `mdl` to load input data from the file `InputData.mat`.

### **输出数据类型** — MAT 文件中数据的数据类型 `Inherit: auto` (默认) | `double` | `single` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | **Enum: <class\_name>** | **Bus: <bus\_object>** | **<数据类型表达式>** | ...

From File 模块加载的 MAT 文件中数据的数据类型。默认情况下，From File 模块从文件中的数据或从定义信号数据类型的下游模块继承输出信号数据类型。如果 MAT 文件中数据的数据类型与继承的数据类型不匹配，则软件会引发一个错误。

加载标量或多维信号数据时，可以选择继承输出数据类型，也可以指定输出数据类型以匹配 MAT 文件中数据的数据类型。

要加载总线数据，请将**输出数据类型**设置为 **Bus: <bus object>**，并指定定义输出总线的 `Simulink.Bus` 对象的名称。

要加载枚举数据，请将**输出数据类型**设置为 **Enum: <class name>**，并指定定义枚举数据值的枚举类的名称。

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `OutDataTypeStr` |
| **值:** | `'Inherit (auto)'` (默认) | `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'Enum: <class name>'` | `'Bus: <object name>'` | `'<data type expression>'` |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("mdl/From File","OutputDataTypestr","double")` configures the From File block named `From File` in the model `mdl` to load data from a MAT file that contains `double` signal values and produce a signal with `double` data type.

### **采样时间** — 输出采样周期和可选时间偏移量 `0` | 标量 | `1`×`2` 向量

**采样时间**参数指定模块在仿真期间计算新输出值的时间。有关详细信息，请参阅指定采样时间。

当您不希望输出具有时间偏移量时，请将**采样时间**参数指定为标量。要向输出添加时间偏移量，请将**采样时间**参数指定为 `1`×`2` 向量，其中第一个元素是采样周期，第二个元素是偏移量。

默认情况下，**采样时间**参数值为 `0`，表示没有时间偏移量的连续采样时间。对于离散信号，请将采样时间指定为离散采样间隔。例如，将采样时间指定为 `0.1` 以对每 100 毫秒采样一次的离散信号建模。将采样时间指定为 `-1` 以继承该值。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SampleTime` |
| **值:** | `'0'` (默认) | scalar | `1`-by-`2` vector |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("mdl/From File","SampleTime","-1")` configures the From File block named `From File` in the model `mdl` to inherit its sample time.

### **第一个数据点之前的数据外插** — 在 MAT 文件中第一个数据点之前确定模块输出的方法 **线性外插** (默认) | **保持第一个值** | **接地值**

用于确定在 MAT 文件数据中第一个采样之前仿真时间的输出值的外插方法。

| 方法 | 描述 | 示例 |
| --- | --- | --- |
| **线性外插** | 模块如何确定输出值取决于 MAT 文件中数据的类型。  - 对于 `double` 数据，From File 模块使用前两个采样对输出值进行线性外插。 - 对于 `Boolean` 数据，From File 模块使用 MAT 文件数据中的第一个值作为输出值。 - 对于所有其他内置数据类型，From File 模块：  1. 将数据向上转换为 `double`。   2. 使用 MAT 文件数据中的前两个采样对输出值进行线性外插。   3. 将外插的数据值向下转换为原始数据类型。  如果 MAT 文件数据只包含一个采样，则 From File 模块在输出端提供该值。  当 From File 模块加载枚举或定点数据时，请不要使用**线性外插**选项。  外插设置将应用于总线中的所有信号。如果总线中有任一信号包含枚举或定点数据，请不要使用**线性外插**选项。 | Plot that shows the output for a From File block configured to linearly extrapolate the output value for simulation times before the first sample in the loaded data. The block loads data that starts 2 seconds into the simulation. |
| **保持第一个值** | From File 模块使用 MAT 文件中的第一个数据值作为输出值。 | Plot that shows the output for a From File block configured to hold the first value in the loaded data for simulation times before the first sample in the loaded data. The block loads data that starts 2 seconds into the simulation. |
| **接地值** | From File 模块输出值取决于 MAT 文件中数据的类型。  - 内置数值类型 - `0` - `Boolean` — `false` - 定点数据类型 - 值 `0` 的表示，因为要进行定标且精度有限，该值可能不会精确为 `0`。 - 枚举数据类型 - 默认值 | Plot that shows the output for a From File block configured to use the ground value as the output value for simulation times before the first sample in the loaded data. The block loads data that starts 2 seconds into the simulation. |

#### 提示

要生成构建 ERT 或 GRT 目标或使用 SIL 或 PIL 仿真模式的代码，请将**第一个数据点之前的数据外插**指定为**线性外插**。有关使用  From File 模块的 C/C++ 代码生成的详细信息，请参阅 代码生成。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ExtrapolationBeforeFirstDataPoint` |
| **值:** | `'Linear extrapolation'` (默认) | `'Hold first value'` | `'Ground value'` |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("mdl/From File","ExtrapolationBeforeFirstDataPoint","Hold first value")` configures the From File block named `From File` in the model `mdl` to extrapolate values before the first value in the file by holding the first value in the file.

### **时间范围内的数据插值** — 插值方法 **线性插值** (默认) | **零阶保持**

用于确定 MAT 文件数据中采样之间仿真时间的输出值的插值方法。

| 方法 | 描述 | 示例 |
| --- | --- | --- |
| **线性插值** | 模块如何确定输出值取决于 MAT 文件中数据的类型。  - 对于 `double` 数据，From File 模块使用需要输出值的仿真时间前后的数据值对输出值进行线性插值。 - 对于所有其他内置数值数据类型，From File 模块：  1. 将数据向上转换为 `double`。   2. 使用需要输出值的仿真时间前后的 MAT 文件数据值对输出值进行线性插值。   3. 将外插的数据值向下转换为原始数据类型。 - 对于 `Boolean` 数据，如果仿真时间在两个具有不同值的工作区数据点之间，则 From File 模块会将值转换定位在 MAT 文件数据点的中间。例如，如果数据从 `true` 转换为 `false`，则 From File 模块为 MAT 文件数据点之间的前半段区间的仿真时间提供输出值 `true`，为后半段区间的仿真时间提供输出值 `false`。  如果 MAT 文件数据只包含一个采样，则 From File 模块在输出端提供该值。  当 From File 模块加载枚举或定点数据时，请不要使用**线性插值**选项。  插值设置将应用于总线中的所有信号。如果总线中有任一信号包含枚举数据，请不要使用**线性插值**选项。 | Plot that shows the output for a From File block configured to linearly interpolate the output value for simulation times between the samples in the loaded data. |
| **零阶保持** | From File 模块会将每一采样的数据值保持到下一个采样。MAT 文件数据中两个采样之间的仿真时间的输出值是仿真时间之前的采样的值。 | Plot that shows the output for a From File block configured to use zero-order-hold interpolation for simulation times between the samples in the loaded data. |

#### 提示

要生成构建 ERT 或 GRT 目标或使用 SIL 或 PIL 仿真模式的代码，请将**时间范围内的数据插值**指定为**线性插值**。有关使用 From File 模块的 C/C++ 代码生成的详细信息，请参阅代码生成。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `InterpolationWithinTimeRange` |
| **值:** | `'Linear interpolation'` (默认) | `'Zero order hold'` |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("mdl/From File","InterpolationWithinTimeRange","Zero order hold")` configures the From File block named `From File` in the model `mdl` to use zero order hold interpolation.

### **末尾数据点后的数据外插** — 确定 MAT 文件中最后一个数据点之后的模块输出的方法 **线性外插** (默认) | **保留最后一个值** | **接地值**

用于确定 MAT 文件数据中最后一个采样后仿真时间的输出值的外插方法。

| 方法 | 描述 | 示例 |
| --- | --- | --- |
| **线性外插** | 模块如何确定输出值取决于 MAT 文件中数据的类型。  - 对于 `double` 数据，From File 模块使用 MAT 文件中的最后两个采样对输出值进行线性外插。 - 对于 `Boolean` 数据，From File 模块使用 MAT 文件中的采样值作为输出值。 - 对于所有其他内置数据类型，From File 模块：  1. 将数据向上转换为 `double`。   2. 使用 MAT 文件数据中的最后两个采样对输出值进行线性外插。   3. 将外插的数据值向下转换为原始数据类型。  如果 MAT 文件数据只包含一个采样，则 From File 模块使用该值作为输出。  当 From File 模块加载枚举或定点数据时，请不要使用**线性外插**选项。  外插设置将应用于总线中的所有信号。如果总线中有任一信号包含枚举数据，请不要使用**线性外插**选项。 | Plot that shows the output for a From File block configured to linearly interpolate the output value for simulation times after the last sample in the loaded data. The block loads data that ends 2 seconds before the end of the simulation. |
| **保留最后一个值** | From File 模块使用 MAT 文件中的最后一个数据值作为输出值。 | Plot that shows the output for a From File block configured to hold the last output value for simulation times after the last sample in the loaded data. The block loads data that ends 2 seconds before the end of the simulation. |
| **接地值** | From File 模块输出值取决于 MAT 文件中数据的类型。  - 内置数值类型 - `0` - `Boolean` — `false` - 定点数据类型 - 值 `0` 的表示，因为要进行定标且精度有限，该值可能不会精确为 `0`。 - 枚举数据类型 - 默认值 | Plot that shows the output for a From File block configured to use the ground value as the output value for simulation times after the last sample in the loaded data. The block loads data that ends 2 seconds before the end of the simulation. |

#### 提示

要生成构建 ERT 或 GRT 目标或使用 SIL 或 PIL 仿真模式的代码，请将**末尾数据点后的数据外插**指定为**线性外插**。有关使用 From File 模块的 C/C++ 代码生成的详细信息，请参阅代码生成。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ExtrapolationAfterLastDataPoint` |
| **值:** | `'Linear extrapolation'` (默认) | `'Hold last value'` | `'Ground value'` |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("mdl/From File","ExtrapolationAfterLastDataPoint","Hold last value")` configures the From File block named `From File` in the model `mdl` to extrapolate values after the last value in the file by holding the last value in the file.

### **启用过零检测** — 用于对此模块启用过零检测的选项 `off` (默认) | `on`

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

#### 提示

要生成用于编译 ERT 或 GRT 目标或使用 SIL 或 PIL 仿真模式的代码，请清除此复选框。有关使用 From File 模块的 C/C++ 代码生成的详细信息，请参阅代码生成。

#### 编程用法

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ZeroCross` |
| **值:** | `'on'` (默认) | `'off'` |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("mdl/From File","ZeroCross","off")` configures the From File block named `From File` in the model `mdl` to disable zero-crossing detection.

## 模块特性

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

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不建议用于生产代码。

为 RSim 目标生成代码没有特殊要求或限制。所有其他代码生成目标仅支持从 MAT 文件中的数组加载双精度实数一维信号数据，其中第一列包含时间数据，后续列包含信号数据。生成用于编译 ERT 或 GRT 目标的代码时，或者使用 SIL 或 PIL 仿真模式时，都要求：

- 加载的 MAT 文件包含一个有至少两行且没有 `NaN`、`Inf` 或 `-Inf` 值的数组。
- **第一个数据点之前的数据外插**和**末尾数据点后的数据外插**参数设置为**线性外插**。
- **时间范围内的数据插值**参数设置为**线性插值**。
- **启用过零检测**参数处于清除状态。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

From File 模块支持最多 32 位的定点数据类型。

## 版本历史记录

**在 R2006a 之前推出**
