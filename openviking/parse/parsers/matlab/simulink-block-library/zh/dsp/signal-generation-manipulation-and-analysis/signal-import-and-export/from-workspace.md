---
type: simulink-block
title: 'From Workspace'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Sources'
documentation_page: 'fromworkspace'
documentation_source_path: 'slref/fromworkspace.html'
language: zh-CN
chinese_source: worker-translation
---

# From Workspace

## 端口

### 输出

### **Port\_1** — 从工作区加载的数据 标量 | 向量 | 矩阵 | 数组

从工作区加载的数据，在模块输出端以信号或非虚拟总线形式提供。根据加载的数据，输出信号可以是：

- 标量、向量、多维或有界可变大小信号
- 总线
- 总线数组 *(自 R2021a 起)*

From Workspace 模块支持加载所有内置数值数据类型和自定义定点数据类型的实数和复数数据。还可以加载字符串数据以及具有自定义枚举或总线数据类型的数据。

*R2024b 之前：From Workspace 模块不支持加载具有 `int64` 或 `uint64` 数据类型的输入信号值。*

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
**复数支持：** Yes

## 参数

### **Data** — 要从工作区加载的数据 `timeseries` 对象 | `timetable` 对象 | 结构体 | 二维数组 | MATLAB 表达式

要从工作区加载的数据，指定为 MATLAB 变量或 MATLAB 表达式，其计算结果为 From Workspace 模块支持的格式的数据。该表达式可以创建 From Workspace 模块在其输出端提供的数据，也可以引用包含要加载数据的工作区变量。有关表达式计算方式的详细信息，请参阅符号解析。

From Workspace 模块可以加载标量、多维和可变大小信号的实数或复数数据，以及总线或总线数组的数据。

根据您希望模块在模型中产生的输出类型，From Workspace 模块支持不同的输入数据格式。对于所有类型的输出和数据格式：

- 输入数据中的时间值必须具有 `double` 数据类型，并且必须单调递增。
- 时间值和数据值不得包含 `Inf` 或 `NaN` 值。

| 输出类型 | 数据格式 | 提示 |
| --- | --- | --- |
| 标量或向量信号 | - 包含单列的 `timetable` - `timeseries` 对象 - `Simulink.SimulationData.Signal` 对象 - 字段和层次结构与 `Structure` 或 `Structure with time` 记录格式匹配的结构体。 - 二维数组，其中第一列是时间，一个或多个附加列包含每个时间戳的信号值 | - 对于标量信号和向量信号，信号数据中的行数必须与时间向量中的行数匹配。 - 要创建 `timetable`，时间值必须为 `duration` 向量。仿真时间始终使用秒单位。当您创建使用非秒单位的 duration 向量时，软件会将该值转换为秒以用于仿真。 - 数组格式不支持复数信号值或数据类型不是 `double` 的信号值。 |
| 多维信号 | - `timeseries` 对象 - 包含单列的 `timetable` - `Simulink.SimulationData.Signal` 对象 - 字段和层次结构与 `Structure` 或 `Structure with time` 记录格式匹配的结构体 | - 对于具有两个或更多维度的值的多维信号，最后一个维度的长度必须与时间向量的长度匹配。例如，`2`-by-`2` 矩阵信号的 10 个样本的输入数据具有包含 10 行的时间向量，以及维度为 `2`-by-`2`-by-`10` 的信号值数组。 - 要创建 `timetable`，时间值必须为 `duration` 向量。仿真时间始终使用秒单位。当您创建使用非秒单位的 duration 向量时，软件会将该值转换为秒以用于仿真。 |
| 可变大小信号 | 字段和层次结构与 `Structure` 或 `Structure with time` 记录格式匹配的结构体 | 要以可使用 From Workspace 模块加载的格式记录可变大小信号，请将该信号连接到顶层 Outport 模块，并将模型的 **Save format** 配置参数设置为 `Structure` 或 `Structure with time`。 |
| 总线 | `timetable` 或 `timeseries` 对象的结构体：    - 将 **Output data type** 参数指定为定义总线的 `Simulink.Bus` 对象。 - 结构体的层次结构和字段名必须与总线的层次结构和元素名匹配。 - 每个 `timetable` 或 `timeseries` 对象包含总线中叶子信号的数据。 - 每个 `timetable` 必须只包含一列。 | 若要部分指定总线的输入数据，请在输入数据结构体中将不需要加载数据的总线元素设置为 `[]`。 |
| 总线数组 *(自 R2021a 起)* | 结构体数组，其中每个结构体表示总线数组内某个总线的数据 | - 不支持为快速加速仿真加载总线数组的数据。 - 顶层模型中的 From Workspace 模块支持在普通和加速模式仿真中加载总线数组的数据。 - 引用模型中的 From Workspace 模块仅当引用模型在普通模式下执行时才支持加载总线数组的数据。 - 若要部分指定总线数组的输入数据，请在该总线数据的表示结构体中，将不需要加载数据的总线元素设置为 `[]`。 |

有关详细信息，请参阅使用 From Workspace 模块加载数据。

#### 提示

- 要加载使用 To File 模块以数组格式记录的数据，请转置该数组，使时间值位于单列而不是单行中。您可以使用 `transpose` 函数并将转置后的数据保存到新文件。
- 对于使用 `sim`、`parsim` 或 `batchsim` 函数运行的编程仿真，您可以使用 `Simulink.SimulationInput` 对象指定 From Workspace 模块要加载的数据。

  - 使用 `setBlockParameter` 函数设置模块上要在仿真中使用的 `VariableName` 参数值。
  - 使用 `setVariable` 函数将包含输入数据的变量添加到 `SimulationInput` 对象中。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `VariableName` |
| **值：** | `'simin'` (default) | MATLAB 表达式 | `timeseries` 对象 | `timetable` | 结构体 | 二维数组 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("myModel/From Workspace","VariableName","inData")` 配置模型 `myModel` 中名为 `From Workspace` 的 From Workspace 模块，以加载存储在名为 `inData` 的 MATLAB 变量中的数据。

### **Output data type** — 加载的工作区数据类型 `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | ...

From Workspace 模块加载的工作区数据的数据类型。默认情况下，From Workspace 模块从工作区数据或者从定义信号数据类型的下游模块继承输出信号数据类型。

#### 提示

- 当您为标量、向量或多维信号加载数据时，可以选择继承输出数据类型，也可以指定输出数据类型以匹配工作区数据的数据类型。
- 要加载总线或总线数组的数据，请将 **Output data type** 设置为 `Bus: <bus_object>`，并指定定义输出总线的 `Simulink.Bus` 对象的名称。

  当您加载枚举数据时，请将 **Output data type** 设置为 `Enum: <class_name>`，并指定定义枚举数据值的枚举类的名称。
- **Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关详细信息，请参阅使用 Data Type Assistant 指定数据类型。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `'Inherit: auto'` (default) | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'string'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'Enum: <class name>'` | `'Bus: <object name>'` | 数据类型表达式 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("myModel/From Workspace","OutDataTypeStr","int32")` 指定名为 `From Workspace` 的 From Workspace 模块加载到模型 `myModel` 中的数据的数据类型必须为 `int32`。

### **Sample time** — 输出采样周期和可选时间偏移 `0` (default) | 标量 | 向量

**Sample time** 参数指定模块在仿真期间何时计算新的输出值。有关详细信息，请参阅指定采样时间。

当您不希望输出具有时间偏移时，请将 **Sample time** 参数指定为标量。要为输出添加时间偏移，请将 **Sample time** 参数指定为 `1`-by-`2` 向量，其中第一个元素是采样周期，第二个元素是偏移。

默认情况下，**Sample time** 参数值为 `0`，这表示无时间偏移的连续采样时间。对于离散信号，请将 **Sample time** 指定为离散采样间隔。例如，将 **Sample time** 指定为 `0.1`，以对每 100ms 采样的离散信号建模。将 **Sample time** 指定为 `-1` 以继承该值。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `'0'` (default) | 标量 | 向量 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("myModel/From Workspace","SampleTime","0.1")` 配置模型 `myModel` 中名为 `From Workspace` 的 From Workspace 模块以 `0.1` 秒的采样时间执行。

### **Interpolate data** — 插值方法 `on` (default) | `off`

用于为位于已加载工作区数据中时间值之间的仿真时间提供输出值的插值方法。当您选择 **Interpolate data** 时，From Workspace 模块使用已加载工作区数据中的相邻值对输出值进行线性插值。当未选择 **Interpolate data** 时，From Workspace 模块提供已加载工作区数据中前一个数据点的值。有关插值算法的详细信息，请参阅插值。

**Interpolate data** 和 **Form output after final data value by** 参数控制 From Workspace 模块如何为发生在已加载工作区数据中第一个数据点之前或最后一个数据点之后的仿真时间外推输出值。有关 From Workspace 模块外推行为的完整信息，请参阅外推。

在以下情况下，请清除 **Interpolate data** 参数，并将 **Form output after final data value by** 参数设置为 `Extrapolation` 以外的值：

- 您加载字符串、枚举、定点或可变大小信号数据。
- 您为快速加速仿真加载 `int64` 或 `uint64` 数据。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Interpolate` |
| **值：** | `'on'` (default) | `'off'` |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("myModel/From Workspace","Interpolate","off")` 配置名为 `From Workspace` 的 From Workspace 模块使用零阶保持插值将数据加载到模型 `myModel` 中。

### **Enable zero-crossing detection** — 过零检测 `on` (default) | `off`

过零检测是一种用于定位模块输出中不连续点并避免在不连续点附近使用过小时间步长的技术，过小的时间步长可能会减慢仿真速度。*过零* 指数据中的不连续点。当采样时间为连续 (`0`) 时，From Workspace 模块可以检测过零。

当数据包含多个具有相同时间的样本时，已加载的工作区数据会在模块输出中产生不连续点。例如，对于以下输入数据，不连续点发生在时间 `2`。

    time:     0 1 2 2 3
    signal:   2 3 4 5 6

仅当您选择 **Interpolation** 参数时，From Workspace 模块才会检测由输入数据中重复时间值引起的过零。

当您将 **Form output after final data value by** 设置为 `Setting to zero` 时，From Workspace 模块还可以在工作区数据的最后一个样本处产生输出不连续点。

当您为总线加载输入数据时，From Workspace 模块会检测所有总线元素的过零。

此模块仅在使用可变步长求解器的仿真中支持过零检测。当您使用定步长求解器进行仿真时，软件不会检测或定位此模块的过零。

有关详细信息，请参阅过零检测。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ZeroCross` |
| **值：** | `'on'` (default) | `'off'` |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("myModel/From Workspace","ZeroCross","off")` 禁用模型 `myModel` 中名为 `From Workspace` 的 From Workspace 模块的 **Enable zero-crossing detection** 参数。

### **Form output after final data value by** — 确定最终数据点之后模块输出的方法 `Extrapolation` (default) | `Setting to zero` | `Holding final value` | `Cyclic repetition`

From Workspace 模块使用 **Interpolate data** 和 **Form output after final data value by** 设置来确定工作区数据中最后一个可用样本之后的仿真时间的模块输出。

| Form output after final data value by 的设置 | Interpolate data 的设置 | 最终数据之后的模块输出 |
| --- | --- | --- |
| **Extrapolation** | On | 从最终数据值外推 |
| Off | 错误 |
| **Setting to zero** | On | 零 |
| Off |
| **Holding final value** | On | 工作区中的最终值 |
| Off |
| **Cyclic repetition** | On | 错误 |
| Off | 当已加载的工作区数据使用不带时间格式的结构体时，从第一个值开始重复工作区数据。对于除 structure with time 以外的工作区数据格式，会出错。 |

有关 From Workspace 模块外推行为的完整信息，请参阅外推。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutputAfterFinalValue` |
| **值：** | `'Extrapolation'` (default) | `'Setting to zero'` | `'Holding final value'` | `'Cyclic repetition'` |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("myModel/From Workspace","OutputAfterFinalValue","Holding final value")` 配置模型 `myModel` 中名为 `From Workspace` 的 From Workspace 模块，将最终输入数据值用作输入数据中最后一个时间值之后发生的时间步的输出值。

## 所属库

Simulink / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed pointa` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `yes` |
|  |  |
| --- | --- |
| a 支持通过使用 Fixed-Point Designer 创建的 fi 对象进行输入。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不建议用于生产代码。From Workspace 模块加载的数据在生成的代码中会硬编码为静态分配的数组。将 From Workspace 模块用于代码生成可能会显著增加生成代码的大小和内存使用量。要在生成的代码中实现输入端口，请使用 Inport 模块或 In Bus Element 模块。

对于软件在环 (SIL) 测试，请考虑使用 SIL/PIL Manager (Embedded Coder)。您可以使用 From Workspace 模块为针对模型引用生成的代码的 SIL 测试提供输入。有关详细信息，请参阅使用 SIL 和 PIL 仿真测试生成的代码 (Embedded Coder)。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

支持通过使用 Fixed-Point Designer™ 创建的 `fi` (Fixed-Point Designer) 对象进行输入。

## 版本历史

**在 R2006a 之前引入**

### R2024b：`int64` 和 `uint64` 数据类型支持

From Workspace 模块支持加载具有 `int64` 或 `uint64` 数据类型的输入信号数据值。当您使用 From Workspace 模块加载 `int64` 或 `uint64` 信号数据时：

- 只有信号值可以具有 `int64` 或 `uint64` 数据类型。时间值必须具有 `double` 数据类型。
- 使用除数组以外的格式，例如 `timetable`、`timeseries` 或结构体。数组格式不支持除 `double` 以外的任何数据类型。

虽然所有仿真模式都支持加载 `int64` 和 `uint64` 信号数据，但快速加速仿真不支持对 `int64` 和 `uint64` 数据进行插值。要将 `int64` 或 `uint64` 数据加载到快速加速仿真中：

1. 清除 **Interpolate data** 参数。
2. 将 **Form output after final data value by** 参数设置为除 `Extrapolation` 以外的任何值。

### R2021a：总线数组支持

From Workspace 模块支持加载总线数组的数据。顶层模型中的 From Workspace 模块可以在普通或加速模式仿真中加载总线数组的数据。仅当引用模型在普通模式下执行时，才支持使用引用模型中的 From Workspace 模块加载总线数组的数据。

### R2020a：`timetable` 支持

From Workspace 模块支持加载存储为 `timetable` 的数据。`timetable` 必须只包含单列数据。

当您为总线加载输入数据时，包含数据的结构体可以包括一个或多个 `timetable` 对象，这些对象仅包含叶子信号的单列数据。

### R2018b：字符串支持

From Workspace 模块支持加载字符串数据。当您使用 From Workspace 模块加载字符串数据时：

- 只有信号值可以具有 `string` 数据类型。时间值必须具有 `double` 数据类型。
- 使用除数组以外的格式，例如 `timeseries` 或结构体。数组格式不支持除 `double` 以外的任何数据类型。

## 描述

将信号数据从工作区加载到 Simulink 模型中

From Workspace 模块从工作区读取数据到 Simulink® 模型中，并在模块输出端将数据作为信号或非虚拟总线提供。您可以从基础工作区、模型工作区或掩码工作区加载数据。您可以使用 From Workspace 模块，从引用模型或子系统可访问的工作区将信号数据加载到模型层次结构中的任何模型或子系统中。

您可以指定模块如何根据工作区数据构造输出，包括输出采样周期、插值和外推行为，以及是否使用过零检测。

From Workspace 模块图标显示 **Data** 参数的值。例如，如果您使用 From Workspace 模块加载变量 *x* 中的数据，您将 `x` 指定为 **Data** 参数的值，模块会显示 `x`。

### 指定要加载的数据

使用 **Data** 参数指定 From Workspace 模块要加载的数据。您可以将 **Data** 参数的值指定为 MATLAB® 表达式，例如变量名。**Data** 参数中的表达式必须计算为 From Workspace 模块支持的格式的数据。有关表达式如何计算的详细信息，请参阅符号解析。

From Workspace 模块不会从数据字典加载数据。使用数据字典仅存储模型的设计数据，而不是仿真输入数据。您可以将与 From Workspace 模块相关的设计数据（例如 **Sample time** 参数的值）存储在数据字典中。
