---
type: simulink-block
title: 'From Workspace'
family: sources
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'fromworkspace'
language: zh-CN
chinese_source: official
---

# From Workspace

将信号数据从工作区加载到 Simulink 模型中

## 所属库

Simulink / Sources

## 描述

From Workspace 模块将数据从工作区读入 Simulink® 模型，并在模块的输出端以信号或非虚拟总线形式提供数据。您可以从基础工作区、模型工作区或封装工作区加载数据。您可以使用 From Workspace 模块将信号数据从引用模型或子系统可访问的工作区加载到模型层次结构中的任何模型或子系统中。

您可以指定模块如何从工作区数据构造输出，包括输出采样周期、内插和外插行为，以及是否使用过零检测。

From Workspace 模块图标显示**数据**参数的值。例如，如果您使用 From Workspace 模块加载变量 *x* 中的数据，并且指定 `x` 作为**数据**参数的值，则该模块将显示 `x`。

### 指定要加载的数据

使用**数据**参数指定要加载的 From Workspace 模块的数据。您可以将**数据**参数的值指定为 MATLAB® 表达式，例如变量名称。**数据**参数中的表达式的计算结果必须为 From Workspace 模块支持的格式的数据。有关如何计算表达式的详细信息，请参阅符号解析。

From Workspace 模块不从数据字典加载数据。使用数据字典仅存储模型的设计数据，不存储仿真输入数据。您可以在数据字典中存储与 From Workspace 模块相关的设计数据，例如**采样时间**参数的值。

## 端口

### 输出

### **Port\_1** — 从工作区加载的数据 标量 | 向量 | 矩阵 | 数组

从工作区加载的数据，在模块输出端作为信号或非虚拟总线提供。根据加载的数据，输出信号可能为：

- 标量、向量、多维或有界可变大小信号
- 总线
- 总线数组 *(自 R2021a 起)*

From Workspace 模块支持加载所有内置数值数据类型和自定义定点数据类型的实数和复数数据。您还可以加载字符串数据和具有自定义枚举或总线数据类型的数据。

*在 R2024b 之前的版本中: From Workspace 模块不支持加载具有 `int64` 或 `uint64` 数据类型的输入信号值。*

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
**复数支持:** 是

## 参数

### **数据** — 要从工作区加载的数据 `timeseries` 对象 | `timetable` 对象 | 结构体 | 二维数组 | MATLAB 表达式

要从工作区加载的数据，指定为 MATLAB 变量或 MATLAB 表达式，该表达式的计算结果为 From Workspace 模块支持的格式的数据。该表达式可以创建 From Workspace 模块在其输出端提供的数据，也可以引用包含要加载的数据的工作区变量。有关如何计算表达式的详细信息，请参阅符号解析。

From Workspace 模块可以加载标量的实数或复数数据、多维和可变大小信号的数据以及总线或总线数组的数据。

From Workspace 模块支持不同输入数据格式，具体取决于您要该模块在模型中生成的输出的类型。对于所有类型的输出和数据格式：

- 输入数据中的时间值必须具有 `double` 数据类型并且单调递增。
- 时间和数据值不能包含 `Inf` 或 `NaN` 值。

| 输出的类型 | 数据格式 | 提示 |
| --- | --- | --- |
| 标量或向量信号 | - 只包含单列的 `timetable` - `timeseries` 对象 - `Simulink.SimulationData.Signal` 对象 - 具有与**结构体**或**带时间的结构体**记录格式匹配的字段和层次结构的结构体。 - 二维数组，其中第一列是时间，一个或多个其他列包含每个时间戳对应的信号值 | - 对于标量和向量信号，信号数据中的行数必须与时间向量中的行数匹配。 - 要创建一个 `timetable` 对象，时间值必须为 `duration` 向量。  仿真时间始终使用秒为单位。当创建使用秒以外的单位的持续时间向量时，软件会将值转换为秒以便在仿真中使用。 - 数组格式不支持复信号值或数据类型不是 `double` 的信号值。 |
| 多维信号 | - `timeseries` 对象 - 只包含单列的 `timetable` - `Simulink.SimulationData.Signal` 对象 - 具有与**结构体**或**带时间的结构体**记录格式匹配的字段和层次结构的结构体 | - 对于具有二维或更多维的值的多维信号，最后一个维度的长度必须与时间向量的长度匹配。  例如，`2`×`2` 矩阵信号的 10 个采样的输入数据具有一个包含 10 行的时间向量和一个由维度为 `2`×`2`×`10` 的信号值组成的数组。 - 要创建一个 `timetable` 对象，时间值必须为 `duration` 向量。  仿真时间始终使用秒为单位。当创建使用秒以外的单位的持续时间向量时，软件会将值转换为秒以便在仿真中使用。 |
| 可变大小信号 | 具有与**结构体**或**带时间的结构体**记录格式匹配的字段和层次结构的结构体 | 要以可使用 From Workspace 模块加载的格式记录可变大小信号，请将该信号连接到一个顶层 Outport 模块，并将模型的**保存格式**配置参数设置为**结构体**或**带时间的结构体**。 |
| 总线 | `timetable` 或 `timeseries` 对象的结构体：    - 将**输出数据类型**参数指定为定义总线的 `Simulink.Bus` 对象。 - 结构体的层次结构和字段名称必须与总线的层次结构和元素名称匹配。 - 每个 `timetable` 或 `timeseries` 对象包含总线中一个叶信号的数据。 - 每个 `timetable` 只能包含一列。 | 要部分指定总线的输入数据，请在输入数据结构体中将不需要加载数据的总线元素设置为 `[]`。 |
| 总线数组 *(自 R2021a 起)* | 结构体数组，其中每个结构体表示总线数组内的一个总线的数据 | - 快速加速仿真不支持加载总线数组的数据。 - From Workspace 顶层模型中的模块支持在普通和加速模式仿真中加载总线数组的数据。 - 仅当引用模型在普通模式下执行时，引用模型中的 From Workspace 模块才支持加载总线数组的数据。 - 要部分指定总线数组的输入数据，请在表示该总线的数据的结构体中将不需要加载数据的总线元素设置为 `[]`。 |

有关详细信息，请参阅使用 From Workspace 模块加载数据。

#### 提示

- 要加载使用 To File 模块以数组格式记录的数据，请转置数组以使时间值位于单列而不是单行中。您可以使用 `transpose` 函数，并将转置后的数据保存到一个新文件中。
- 对于使用 `sim`、`parsim` 或 `batchsim` 函数运行的编程仿真，您可以使用 `Simulink.SimulationInput` 对象来指定 From Workspace 模块要加载的数据。

  - 使用 `setBlockParameter` 函数设置 `VariableName` 参数的值以用于模块上的仿真。
  - 使用 `setVariable` 函数将包含输入数据的变量添加到 `SimulationInput` 对象中。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `VariableName` |
| **值:** | `'simin'` (默认) | MATLAB expression | `timeseries` object | `timetable` | structure | 2-D array |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("myModel/From Workspace","VariableName","inData")` configures the From Workspace block named `From Workspace` in the model `myModel` to load data stored in the MATLAB variable named `inData`.

### **输出数据类型** — 加载的工作区数据类型 `Inherit: auto` (默认) | `double` | `single` | **half** | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | ...

From Workspace 模块加载的工作区数据的数据类型。默认情况下，From Workspace 模块从工作区数据或定义信号数据类型的下游模块继承输出信号数据类型。

#### 提示

- 加载标量、向量或多维信号数据时，可以选择继承输出数据类型，也可以指定输出数据类型以匹配工作区数据的数据类型。
- 要加载总线或总线数组数据，请将**输出数据类型**设置为 `Bus: <bus_object>`，并指定定义输出总线的 `Simulink.Bus` 对象的名称。

  加载枚举数据时，请将**输出数据类型**设置为 `Enum: <class_name>`，并指定定义枚举数据值的枚举类的名称。
- **数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `OutDataTypeStr` |
| **值:** | `'Inherit: auto'` (默认) | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'string'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'Enum: <class name>'` | `'Bus: <object name>'` | data type expression |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("myModel/From Workspace","OutDataTypeStr","int32")` specifies that data type must be `int32` for the data the From Workspace block named `From Workspace` loads into the model `myModel`.

### **采样时间** — 输出采样周期和可选时间偏移量 `0` (默认) | 标量 | 向量

**采样时间**参数指定模块在仿真期间计算新输出值的时间。有关详细信息，请参阅指定采样时间。

当您不希望输出具有时间偏移量时，请将**采样时间**参数指定为标量。要向输出添加时间偏移量，请将**采样时间**参数指定为 `1`×`2` 向量，其中第一个元素是采样周期，第二个元素是偏移量。

默认情况下，**采样时间**参数值为 `0`，表示没有时间偏移量的连续采样时间。对于离散信号，请将**采样时间**指定为离散采样间隔。例如，将**采样时间**指定为 `0.1` 以对每 100 毫秒采样一次的离散信号建模。将**采样时间**指定为 `-1` 以继承该值。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SampleTime` |
| **值:** | `'0'` (默认) | scalar | vector |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("myModel/From Workspace","SampleTime","0.1")` configures the From Workspace block named `From Workspace` in the model `myModel` to execute with a sample time of `0.1` seconds.

### **数据插值** — 插值方法 `on` (默认) | `off`

用于为加载的工作区数据中的时间值之间的仿真时间提供输出值的插值方法。当您选择**数据插值**时，From Workspace 模块使用加载的工作区数据中的相邻值对输出值进行线性插值。当未选择**数据插值**时，From Workspace 模块提供加载的工作区数据中前一个数据点的值。有关插值算法的详细信息，请参阅插值。

**内插数据**和**最终数据值之后的输出**参数控制 From Workspace 模块对加载的工作区数据中的第一个数据点前或最后一个数据点后发生的仿真时间的输出值进行外插的方式。有关 From Workspace 模块外插行为的完整信息，请参阅外插。

在以下情况下，请清除**数据插值**参数，并将**最终数据值之后的输出**参数设置为**外插**以外的值：

- 您加载字符串、枚举、定点或可变大小信号数据。
- 您为快速加速仿真加载 `int64` 或 `uint64` 数据。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Interpolate` |
| **值:** | `'on'` (默认) | `'off'` |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("myModel/From Workspace","Interpolate","off")` configures the From Workspace block named `From Workspace` to use zero-order hold interpolation for loading data into the model `myModel`.

### **启用过零检测** — 过零检测 `on` (默认) | `off`

过零检测是一种用于定位模块输出中的不连续点并避免在不连续点附近使用过小的时间步的方法，它可能会减慢仿真速度。*过零*指数据中的不连续点。当采样时间连续时 (`0`)，From Workspace 模块可以检测过零点。

当数据包含时间相同的多个采样时，加载的工作区数据会在模块输出中产生不连续点。例如，对于此输入数据，在时间 `2` 处出现不连续点。

```
time:     0 1 2 2 3
signal:   2 3 4 5 6
```

仅在您选择**插值**参数时，From Workspace 模块才检测由输入数据中的重复时间值引起的过零。

当您将**最终数据值之后的输出**设置为**设置为零**时，From Workspace 模块还会在工作区数据中的最后一个采样的输出中产生不连续点。

加载总线的输入数据时，From Workspace 模块会检测所有总线元素的过零点。

此模块仅在使用变步长求解器的仿真中支持过零检测。当使用定步长求解器进行仿真时，软件不会检测或定位此模块的过零点。

有关详细信息，请参阅过零检测。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ZeroCross` |
| **值:** | `'on'` (默认) | `'off'` |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("myModel/From Workspace","ZeroCross","off")` disables the **Enable zero-crossing detection** parameter for the From Workspace block named `From Workspace` in the model `myModel`.

### **最终数据值之后的输出** — 确定最后一个数据点之后的模块输出的方法 **外插** (默认) | **设置为零** | **保持最终值** | **循环重复**

From Workspace 模块使用**数据插值**和**最终数据值之后的输出**设置来确定工作区数据中最后一个可用样本后的仿真时间的模块输出。

| 最终数据值之后的输出的设置 | 数据插值的设置 | 最终数据之后的模块输出 |
| --- | --- | --- |
| **外插** | On | 根据最终数据值外插 |
| Off | 错误 |
| **设置为零** | On | 零 |
| Off |
| **保持最终值** | On | 工作区中的最终值 |
| Off |
| **循环重复** | On | 错误 |
| Off | 当加载的工作区数据使用不带时间格式的结构体时，从工作区数据的第一个值开始重复。  如果工作区数据格式不是带时间的结构体格式，则会出错。 |

有关 From Workspace 模块外插行为的完整信息，请参阅外插。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `OutputAfterFinalValue` |
| **值:** | `'Extrapolation'` (默认) | `'Setting to zero'` | `'Holding final value'` | `'Cyclic repetition'` |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("myModel/From Workspace","OutputAfterFinalValue","Holding final value")` configures the From Workspace block named `From Workspace` in the model `myModel` to use the final input data value as the output value for time steps that occur after the last time value in the input data.

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed pointa` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `是` |
|  |  |
| --- | --- |
| a 支持通过由 Fixed-Point Designer 创建的 fi 对象实现输入。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不建议用于生产代码。From Workspace 模块加载的数据在生成的代码中被硬编码为静态分配的数组。使用 From Workspace 模块生成代码会显著增大生成代码的大小和内存使用量。要在生成的代码中实现输入端口，请使用 Inport 模块或 In Bus Element 模块。

对于软件在环 (SIL) 测试，请考虑使用 SIL/PIL 管理器 (Embedded Coder)。您可以使用 From Workspace 模块为针对模型引用生成的代码的 SIL 测试提供输入。有关详细信息，请参阅用 SIL 和 PIL 仿真测试生成的代码 (Embedded Coder)。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

通过使用 Fixed-Point Designer™ 创建的 `fi` (Fixed-Point Designer) 对象支持输入。

## 版本历史记录

**在 R2006a 之前推出**

### R2024b: `int64` 和 `uint64` 数据类型支持

From Workspace 模块支持加载数据类型为 `int64` 或 `uint64` 的输入信号数据值。当使用 From Workspace 模块加载 `int64` 或 `uint64` 信号数据时：

- 只有信号值可以具有 `int64` 或 `uint64` 数据类型。时间值必须具有 `double` 数据类型。
- 使用数组以外的格式，如 `timetable`、`timeseries` 或结构体。数组格式不支持除 `double` 以外的任何数据类型。

虽然所有仿真模式都支持加载 `int64` 和 `uint64` 信号数据，但在快速加速仿真中不支持 `int64` 和 `uint64` 数据的插值。要将 `int64` 或 `uint64` 数据加载到快速加速仿真中，请执行以下操作：

1. 清除**数据插值**参数。
2. 将**最终数据值之后的输出**参数设置为除**外插**之外的任何值。

### R2021a: 总线数组支持

From Workspace 模块支持加载总线数组的数据。顶层模型中的 From Workspace 模块可以在普通或加速模式仿真中加载总线数组的数据。仅当引用模型在普通模式下执行时，才支持使用引用模型中的 From Workspace 模块加载总线数组的数据。

### R2020a: `timetable` 支持

From Workspace 模块支持加载存储为 `timetable` 的数据。`timetable` 只能包含一列数据。

当您为总线加载输入数据时，包含数据的结构体可以包括一个或多个 `timetable` 对象，这些对象只包含一个叶信号的一列数据。

### R2018b: 字符串支持

From Workspace 模块支持加载字符串数据。当使用 From Workspace 模块加载字符串数据时：

- 只有信号值可以具有 `string` 数据类型。时间值必须具有 `double` 数据类型。
- 使用数组以外的格式，如 `timeseries` 或结构体。数组格式不支持除 `double` 以外的任何数据类型。
