---
type: simulink-block
title: 'Playback'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Sources'
documentation_page: 'playback'
documentation_source_path: 'slref/playback.html'
language: zh-CN
chinese_source: worker-translation
---

# Playback

## 端口

### 输出

### **Port\_1** — 从工作区、文件或 Simulation Data Inspector 加载的数据 scalar | vector | matrix | array

Playback 模块支持加载具有固定或可变维度的实数或复数信号、离散和连续信号、消息、多维信号、总线和总线数组。

当加载总线数据时，Playback 模块会为该总线的每个元素分配一个端口。

如果数据类型为浮点 `half`，则 Playback 模块无法将数据作为消息加载。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`
**复数支持：** Yes

## 参数

### 端口参数

你可以通过 **端口编辑器** 访问端口参数。双击 Playback 模块。在 **仿真** 选项卡中，在 **端口** 部分中，点击 **端口编辑器**。可以使用 **端口编辑器** 独立设置每个端口的属性。

### **端口数量** — 输出端口数量 `0`（默认） | 范围 [`0,100`] 内的整数

当你向 Playback 模块添加信号并自动将信号分配给端口时，为你添加的每个信号或总线元素创建一个新端口。添加信号数据后，你可以添加或删除端口。端口数量不必等于添加到模块的信号数量。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `NumPorts` |
| **值：** | `0` (default) | integer in the range [`0`,`100`] |
| **数据类型：** | `integer` |

**示例：** `set_param(gcb,"NumPorts",5)`

### **数据类型** — 每个端口的输出数据类型 `Inherit: auto`（默认） | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `string` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | ...

默认情况下，端口数据类型继承自源数据类型或下游模块。

你可以独立于信号数据类型设置端口的数据类型。对于数值数据，Playback 模块转换为端口指定的数据类型。如果无法转换，例如将数值数据转换为字符串，软件会抛出错误。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

string array 的大小等于端口数量。每个元素的索引由端口号决定。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `"Inherit: auto"` (default) | `"double"` | `"single"` | `"half"` | `"int8"` |  `"uint8"`  | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"string"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` |
| **数据类型：** | `string array` |

**示例：** `set_param(gcb,"OutDataTypeStr",["double","int64"])`

### **复杂度** — 每个端口的复杂度 `"auto"`（默认） | `"real"` | `"complex"`

你可以独立指定每个端口的复杂度。端口复杂度不需要匹配对应信号的复杂度。默认情况下，端口的复杂度为 `"auto"`，并从信号数据继承。

- 如果信号数据为实数，则加载该信号的端口复杂度可以为实数或复数。如果端口设置为 `"complex"`，则信号的复数部分为信号地。
- 如果信号数据为复数，则加载该信号的端口复杂度必须为复数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

string array 的大小等于端口数量。每个元素的索引由端口号决定。

|  |  |
| --- | --- |
| **参数：** | `PortComplexity` |
| **值：** | `"auto"` (default) | `"real"` | `"complex"` |
| **数据类型：** | `string array` |

**示例：** `set_param(gcb,"PortComplexity",["auto","real","complex","real"])`

### **单位** — 每个端口的物理单位 inherit（默认） | 支持的物理单位

每个端口的物理单位，指定为支持的物理单位。要查看支持的物理单位列表，请使用函数 `showunitslist`。

`showunitslist`

- 如果端口上未设置单位，则输出单位从信号单位继承。
- 如果信号和端口上都设置了不同的单位，则如果单位兼容，Playback 模块会执行单位转换。

Playback 模块会传播每个端口的单位。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

string array 的大小等于端口数量。每个元素的索引由端口号决定。

|  |  |
| --- | --- |
| **参数：** | `PortUnits` |
| **值：** | `" "` (default) | supported physical unit |
| **数据类型：** | `string array` |

**示例：** `set_param(gcb,"PortUnits",["m","m/s","m/s^2"])`

### **采样时间** — 输出采样周期和可选时间偏移 `-1` | scalar | vector

**采样时间** 参数指定模块在仿真期间计算新输出值的时间。有关详细信息，请参阅 Specify Sample Time。

当你希望输出没有时间偏移时，将 **采样时间** 参数指定为 scalar。要向输出添加时间偏移，将 **采样时间** 参数指定为 `1`-by-`2` 向量，其中第一个元素是采样周期，第二个元素是偏移量。

默认情况下，**采样时间** 参数值为 `-1`，这表示端口采样时间从信号继承。如果端口的采样时间与关联信号的采样时间不同，Playback 模块会根据信号的插值设置按需插值数据。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

string array 的大小等于端口数量。每个元素的索引由端口号决定。

|  |  |
| --- | --- |
| **参数：** | `PortSampleTimes` |
| **值：** | `"-1"` (default) | scalar | vector |
| **数据类型：** | `string array` |

**示例：** `set_param(gcb,"PortSampleTimes",["-1","0","inf"])`

### **维度** — 每个端口的维度 `" "`（默认） | integer | integer array

要从数据继承端口的维度，请将参数留空。如果端口没有分配数据，则设置维度会生成信号地。

Playback 模块将多维信号存储为具有非标量采样值的单个信号、一组通道或帧。有关详细信息，请参阅 Analyze Multidimensional Signal Data。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

cell array 的大小等于端口数量。每个元素的索引由端口号决定。

|  |  |
| --- | --- |
| **参数：** | `PortDimensions` |
| **值：** | empty `1×1` cell array (default) | cell array of positive integers | cell array of vectors |
| **数据类型：** | `cell array` |

**示例：** `set_param(gcb,"PortDimensions",[{2},{[1,2,3]}])`

### **维度模式** — 每个端口的维度模式 `"auto"`（默认） | `"Fixed"` | `"Variable"`

每个端口的维度模式，以 string array 形式返回，其中每个元素可以为 `"auto"`、`"Fixed"` 或 `"Variable"`。

- 如果维度模式为 `"auto"`，则端口从数据继承维度模式。
- 如果维度模式为 `"Fixed"`，则端口仅允许固定大小的信号。
- 如果维度模式为 `"Variable"`，则端口仅允许可变大小信号。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

string array 的大小等于端口数量。每个元素的索引由端口号决定。

|  |  |
| --- | --- |
| **参数：** | `PortDimsModes` |
| **值：** | `"auto"` (default) | `"Fixed"` | `"Variable"` |
| **数据类型：** | `string array` |

**示例：** `set_param(gcb,"PortDimsModes",["Fixed","auto"])`

### 模块参数

你可以通过 **参数设置** 访问大多数模块参数。双击 Playback 模块。在 **仿真** 选项卡中，点击 **参数设置** 以配置模块参数。

模块参数设置适用于所有端口。

### **第一个点之前** — 用于确定加载数据中第一个数据点之前模块输出的外插方法 `Linear`（默认） | `Hold First Value` | `Ground Value`

用于确定仿真时间在文件、工作区或 Simulation Data Inspector 数据中第一个采样之前时输出值的外插方法。

| 方法 | 描述 | 示例 |
| --- | --- | --- |
| `Linear` | 外插输出取决于数据类型。<br>  - 对于 `double` 数据，Playback 模块使用前两个采样对输出值进行线性外插。<br>  - 对于 `Boolean` 数据，Playback 模块使用第一个数据点值作为输出值。<br>  - 对于所有其他内置数据类型，Playback 模块：<br>  1. 将数据向上转换为 `double`<br>  2. 使用前两个数据采样对输出值进行线性外插<br>  3. 将外插后的数据值向下转换为原始数据类型<br>  如果数据仅包含一个采样，则 Playback 模块在输出端提供该值。<br>  当 Playback 模块加载 enumerated 或 fixed-point 数据时，请勿使用 `Linear` 选项。<br>  外插设置应用于总线中的所有信号。如果总线中的任何信号包含 enumerated 或 fixed-point 数据，请勿使用 `Linear` 选项。 | 显示为在加载数据中的第一个采样之前的仿真时间线性外插输出值而配置的 Playback 模块输出的图。该模块加载从仿真第 2 秒开始的数据。 |
| `Hold First Value` | Playback 模块使用第一个数据值作为输出值。 | 显示为在加载数据中的第一个采样之前的仿真时间保持加载数据中第一个值而配置的 Playback 模块输出的图。该模块加载从仿真第 2 秒开始的数据。 |
| `Ground Value` | 外插输出取决于数据类型。<br>  - 内置数值类型 — `0`<br>  - `Boolean` — `false`<br>  - 定点数据类型 — 值 `0` 的表示，由于定标和有限精度，它可能不精确为 `0`。<br>  - 枚举数据类型 — 默认值 | 显示为在加载数据中的第一个采样之前的仿真时间使用接地值作为输出值而配置的 Playback 模块输出的图。该模块加载从仿真第 2 秒开始的数据。 |

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ExtrapolationBeforeFirstDataPoint` |
| **值：** | `"Linear extrapolation"` (default) | `"Hold first value"` | `"Ground value"` |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param(gcb,"ExtrapolationBeforeFirstDataPoint","Hold
first value")`

### **最后一个点之后** — 用于确定加载数据中最后一个数据点之后模块输出的外插方法 `Linear`（默认） | `Hold Last Value` | `Ground Value`

用于确定仿真时间在文件、工作区或 Simulation Data Inspector 数据中最后一个采样之后时输出值的外插方法。

| 方法 | 描述 | 示例 |
| --- | --- | --- |
| `Linear` | 外插输出取决于数据类型。<br>  - 对于 `double` 数据，Playback 模块使用最后两个采样对输出值进行线性外插。<br>  - 对于 `Boolean` 数据，Playback 模块使用最后一个采样值作为输出值。<br>  - 对于所有其他内置数据类型，Playback 模块：<br>  1. 将数据向上转换为 `double`<br>  2. 使用最后两个数据采样对输出值进行线性外插<br>  3. 将外插后的数据值向下转换为原始数据类型<br>  如果数据仅包含一个采样，则 Playback 模块使用该值作为输出。<br>  当 Playback 模块加载 enumerated 或 fixed-point 数据时，请勿使用 `Linear` 选项。 | 显示为在加载数据中的最后一个采样之后的仿真时间线性插值输出值而配置的 Playback 模块输出的图。该模块加载在仿真结束前 2 秒结束的数据。 |
| `Hold Last Value` | Playback 模块使用最后一个数据值作为输出值。 | 显示为在加载数据中的最后一个采样之后的仿真时间保持最后一个输出值而配置的 Playback 模块输出的图。该模块加载在仿真结束前 2 秒结束的数据。 |
| `Ground Value` | Playback 模块输出值取决于数据类型。<br>  - 内置数值类型 — `0`<br>  - `Boolean` — `false`<br>  - 定点数据类型 — 值 `0` 的表示，由于定标和有限精度，它可能不精确为 `0`。<br>  - 枚举数据类型 — 默认值 | 显示为在加载数据中的最后一个采样之后的仿真时间使用接地值作为输出值而配置的 Playback 模块输出的图。该模块加载在仿真结束前 2 秒结束的数据。 |

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ExtrapolationAfterLastDataPoint` |
| **值：** | `"Linear extrapolation"` (default) | `"Hold last value"` | `"Ground value"` |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param(gcb,"ExtrapolationAfterLastDataPoint","Hold
last value")`

### **启用过零检测** — 过零检测 `'off'`（默认） | `'on'`

过零检测定位模块输出中的不连续点，或 *零交叉*，并防止在不连续点附近出现过小的时间步长，这可能会减慢仿真。仅当信号的采样时间为连续时，Playback 模块才会检测信号的过零点。

当数据包含多个具有相同时间的采样时，加载的数据会在模块输出中产生不连续点。例如，对于此输入数据，不连续点发生在时间 `2`。

    time:     0 1 2 2 3
    signal:   2 3 4 5 6

Playback 模块还可以根据你配置插值和外插的方式在输出中产生不连续点。

- 将 **第一个点之前** 设置为 `Ground Value` 可以在加载数据中的第一个采样处产生不连续点。
- 将 **最后一个点之后** 设置为 `Ground Value` 可以在加载数据中的最后一个采样处产生不连续点。

此模块仅在使用可变步长求解器的仿真中支持过零检测。当你使用固定步长求解器进行仿真时，软件不会为此模块检测或定位过零点。

有关详细信息，请参阅 Zero-Crossing Detection。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ZeroCross` |
| **值：** | `"off"` (default) | `"on"` |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param(gcb,"ZeroCross","on")`

### **Signals** — 有关添加到 Playback 模块的信号的信息，`Simulink.playback.Signal` 对象

*自 R2024a 起*

有关添加到 Playback 模块的信号的信息，指定为 `Simulink.playback.Signal` 对象。

您可以使用 **Signals** 参数通过 `get_param` 函数检索模块中信号的信息，或通过 `set_param` 函数向模块添加新信号。`Simulink.playback.Signal` 对象存储有关添加到 Playback 模块的信号的信息。

要向 Playback 模块添加一个或多个信号，请使用 `Simulink.playback.createSignals` 函数创建 `Simulink.playback.Signal` 对象。然后，使用 `set_param` 函数将 `Simulink.playback.Signal` 对象应用到 Playback 模块的 **Signals** 参数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Signals` |
| **值:** | `Simulink.playback.Signal` object |

**示例:** `set_param(gcb,"Signals",pgSigObj)`

### 表参数

您可以通过表格可视化的 **Format** 选项卡访问表参数。要查看绘制信号的数据表，请在 **Simulation** 选项卡的 **View** 部分中点击 **Show Table**。要配置表参数，请选择表格可视化，然后点击 **Format** 选项卡。

### **Table Placement** — 表格可视化的位置 `Bottom`（默认） | `Top` | `Left` | `Right` | `Center`

表格可视化相对于迷你图可视化的位置，指定为以下选项之一：

- `Bottom` — 2×1 布局，数据表位于下方子图中，迷你图可视化位于上方子图中
- `Top` — 2×1 布局，数据表位于上方子图中，迷你图可视化位于下方子图中
- `Left` — 1×2 布局，数据表位于左侧子图中，迷你图可视化位于右侧子图中
- `Right` — 1×2 布局，数据表位于右侧子图中，迷你图可视化位于左侧子图中
- `Center` — 仅数据表的 1×1 布局

### **Time Values** — 基于时间的列组织选项 `Union Time`（默认） | `Shared Time` | `Individual Time`

基于时间的列组织，指定为 `Union Time`、`Shared Time` 或 `Individual Time`。

| 列组织选项 | 描述 | 表格格式 |
| --- | --- | --- |
| `Shared Time` | 数据按共享时间列分组。 | 具有共享时间列的数据表 |
| `Individual Time` | 每个信号与其对应的时间列配对。 | 具有单独时间列的数据表 |
| `Union Time` | 数据与单个时间列对齐，该时间列包含信号之间的每个采样时间。当某个信号在给定时间步没有数据值时，该单元格为空。要插补缺失数据值，请在 **Format** 选项卡上点击 **Use Signal Interpolation**。使用 **Properties** 窗格中的 `Interp Method` 属性查看或更改所选信号的插值方法。 | 具有统一时间列的数据表 |

### **Use Signal Interpolation** — 用于插补缺失数据值的选项 `off`（默认） | `on`

当您使用 `Union Time` 列组织选项组织表数据时，某些信号可能没有每个时间步的数据点。点击 **Use Signal Interpolation** 按钮，以使用每个信号的插值设置来插补缺失数据值。要查看或更改所选信号的插值方法，请使用 **Properties** 窗格中的 `Interp Method` 属性。

## 所属库

Simulink / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不推荐用于生产代码。

## 版本历史

**在 R2022b 中引入**

### R2025a：在数据表中查看信号

除了迷你图可视化外，您还可以在数据表中查看绘制的信号。

### R2024b：按来源对数据分组

您可以按来源对信号表中的数据分组。当您按来源对信号分组时，信号将根据数据来源于文件、工作区还是保存在模型中来进行组织。

### R2024a：以编程方式向 Playback 模块添加数据

通过将 `Simulink.playback.Signal` 对象应用到模块的 **Signals** 参数，您可以以编程方式将来自工作区、文件或 Simulation Data Inspector 的数据添加到 Playback 模块。

### R2024a：在 Add Signals 对话框中搜索信号

当您使用 Add Signals 对话框向 Playback 模块添加信号时，可以搜索特定信号。您还可以细化搜索以排除部分匹配、匹配特定大小写，或使用正则表达式查找遵循特定模式的信号。

### R2023b：新增 Preferences 对话框

Playback 模块中新增了 Preferences 对话框，让您选择如何对信号表中的数据分组以及显示哪些信号属性。您可以选择按数据层次结构对信号分组，或者选择不分组数据，而是显示信号的平铺列表。

### R2023a：加载 MLDATX 文件

Playback 模块支持从 Simulation Data Inspector 会话文件加载数据。从原生 MLDATX 文件格式添加数据可加快加载时间，并允许您从大型数据集中选择性地加载单个信号。

### R2023a：从 Playback 模块导出数据

您可以聚合已从不同来源（从源链接或保存在模型中）添加到 Playback 模块的数据，并将该数据导出到工作区或文件。

## 描述

从工作区、文件或 Simulation Data Inspector 加载数据

使用 Playback 模块加载用于仿真的输入数据。Playback 模块支持加载具有固定或可变维度的实数或复数信号、离散和连续信号以及消息。使用 Playback 模块，您可以从以下位置加载数据：

- Simulation Data Inspector 支持的任何数据格式的工作区变量
- Record 模块和 Simulation Data Inspector 支持的相同格式的文件，例如 MAT、MLDATX *（自 R2023a 起）* 和 Microsoft® Excel® 文件
- 来自自定义文件读取器的数据
- Simulation Data Inspector 中的运行

有关 Playback 模块支持的工作区变量和文件格式的详细信息，请参阅 Import Data from Workspace or File into Simulation Data Inspector。

您还可以将 Playback 模块与 Record 模块结合使用，作为记录和回放工作流的一部分。使用 Record 模块记录来自物理设备或仿真的数据。然后，使用 Playback 模块将记录的数据加载到模型中。使用真实或仿真数据，您可以随后开发、测试和优化模型。

### 向 Playback 模块添加数据

您可以向 Playback 模块添加信号、消息、多维信号、总线和总线数组。要使用 Playback 模块将数据加载到模型，首先向模块添加数据。然后，通过将信号或消息分配给端口来选择要加载的数据。运行仿真时，Playback 模块会将数据加载到模型中。

要以交互方式向 Playback 模块添加信号，请双击该模块。当您双击没有信号的 Playback 模块时，模块会显示一个包含添加数据选项的屏幕。

您可以从三种类型的来源中选择向 Playback 模块添加数据：

- 从基础工作区、模型工作区或封装工作区添加工作区变量。
- 从文件添加数据。如果该文件不在 MATLAB® 路径上或当前目录中，您可以点击文件夹图标浏览您的数据。
- 使用 Add Signals 对话框从工作区、文件或 Simulation Data Inspector 添加数据。

使用 Add Signals 对话框可访问更多选项，以从工作区或文件添加数据，或从 Simulation Data Inspector 添加数据。您还可以搜索特定信号。*（自 R2024a 起）* 当您键入信号名称时，信号表会更新，仅显示包含您搜索词的信号名称。您还可以细化搜索以排除部分匹配、匹配特定大小写，或使用正则表达式查找遵循特定模式的信号。

当您从工作区或文件添加数据时，您可以选择引用源中的信号，或将信号副本保存在模型中。从 Simulation Data Inspector 添加信号数据始终会将信号副本保存在模型中。

引用源中的信号会将 Playback 模块中的信号链接到包含信号数据的变量或文件。如果源变量或文件中的数据发生变化，该变化会反映在 Playback 模块加载的数据中。链接数据时，模块上仅存储每个信号的元数据。

当您将信号副本保存在模型中时，Playback 模块会从复制的数据加载。对原始数据源变量或文件所做的更改不会反映在 Playback 模块输出中。

Add Signals 对话框还允许您选择自动或手动分配端口。如果您选择手动分配端口，可以使用 **Port Editor** 创建端口，并使用信号表的 port 列分配端口。

要以编程方式向 Playback 模块添加信号，请使用 `Simulink.playback.createSignals` 函数创建一个包含要添加信号的 `Simulink.playback.Signal` 对象。然后，使用 `set_param` 函数将 `Simulink.playback.Signal` 对象应用到 Playback 模块的 **Signals** 参数。*（自 R2024a 起）*

例如，要将工作区中变量名为 `x1` 和 `x2` 的信号添加到 Playback 模块：

1. 使用 `Simulink.playback.createSignals` 函数为 `x1` 和 `x2` 信号创建 `Simulink.playback.Signal` 对象。将数据源指定为工作区，并列出要添加信号的变量名。
2. 使用 `set_param` 函数将 `Simulink.playback.Signals` 对象设置为 **Signals** 参数的值。

    pbSig  = Simulink.playback.createSignals("workspace","Variables",["x1","x2"]);
    set_param("PlaybackModel/Playback","Signals",pbSig);

### 在迷你图可视化中查看信号

添加信号数据后，您可以在 Playback 模块中可视化信号，以在将数据加载到模型之前验证数据。

默认情况下，Playback 模块使用迷你图绘制您的数据。为添加到 Playback 模块的每个信号创建一个迷你图。如果您为总线添加输入数据，则为每个总线元素创建一个迷你图。多维信号必须转换为通道或帧才能可视化数据。使用每个信号名称旁边的复选框控制绘制哪些信号。

**注意**

您可以选择或清除复选框来更改迷你图可视化的外观，而不会影响 Playback 模块在仿真期间加载到模型中的信号。要控制哪些信号加载到模型，请使用信号表中的 port 列。

要更改信号表的外观，请点击 **Preferences**。在 Preferences 对话框中，您可以选择要显示哪些信号属性以及如何对信号表中的数据分组。您可以按以下方式对数据分组：*（自 R2023b 起）*

- Hierarchy — 基于数据层次结构对数据分组。
- Source — 基于数据来源对数据分组。*（自 R2024b 起）*

  - File — 从文件获取并引用的信号会收集在由文件名指定的组中。如果您从多个文件添加信号，则为每个文件创建一个组。
  - Workspace — 从工作区获取并引用的信号会收集在名为 `Workspace` 的组中。
  - Saved in model — 保存到模型中的信号（例如来自 Simulation Data Inspector 的信号）会收集在名为 `Signals saved in model` 的组中。
- No grouping — 显示信号的平铺列表。

### 在数据表中查看信号

*自 R2025a 起*

要在数据表中查看信号，请在 **Simulation** 选项卡的 **View** 部分中点击 **Show Table**。默认情况下，Playback 模块创建一个 2×1 布局，迷你图可视化位于上方子图中，数据表位于下方子图中。通过选中或清除每个信号名称旁边的复选框，切换绘制并显示在表中的信号。表显示所有绘制的信号，并使用颜色协调的列。当您从信号表或迷你图可视化中选择一个信号时，Playback 模块还会突出显示数据表中的相应列。

Playback 模块中的 2×1 布局，上方子图中显示迷你图可视化，下方子图中显示数据表。

您可以更改数据表的位置，使用光标检查数据，并配置表中数据相对于时间的呈现方式。有关详细信息，请参阅 View Table of Data in Playback Block。

### 查看和编辑信号与端口

您可以使用 Playback 模块中的 **Properties** 窗格查看和编辑信号属性。

在 **Properties** 窗格中，您可以编辑任何白色背景的行。可编辑字段的数量取决于您选择引用源中的信号，还是将数据副本保存在模型中。

Playback 模块的端口属性可以使用 **Port Editor** 与信号属性分开设置。

使用 **Port Editor**，您可以添加端口、删除端口和编辑端口属性。您还可以使用信号表的 **Port** 列更改端口分配。默认情况下，端口属性继承自信号。但是，您可以独立于信号属性设置端口属性。当与信号属性兼容时，端口属性决定 Playback 模块的输出。例如，您可以通过将该端口的 **Units** 属性设置为不同的测量单位，来转换具有已分配测量的信号单位。当信号单位和端口单位兼容时，Playback 模块会执行单位转换。

Playback 模块支持多速率采样时间，允许您为每个端口设置不同的采样时间。端口采样时间也可以与信号采样时间分开设置。

### 导出添加到 Playback 模块的数据

*自 R2023a 起*

您可以使用 Playback 模块聚合来自工作区、文件和 Simulation Data Inspector（从源链接或保存在模型中）的数据，并将该数据导出到工作区或文件。Playback 模块会导出添加到模块的所有数据，甚至包括未分配给端口的信号。要导出添加到 Playback 模块的所有数据：

1. 在 **Simulation** 选项卡的 **Share** 部分中，点击 **Export**。
2. 选择 **Base workspace** 或 **File**，将数据导出到工作区或文件。您可以选择将数据导出到工作区，或导出到 MAT、MLDATX 或 Microsoft Excel 文件。
3. 点击 **Export**。

如果您选择将数据导出到 MLDATX 文件，可以使用 **Exported run name** 文本框指定运行的名称。

如果您选择将数据导出到 Excel 文件，请点击 **Options** 选择要导出的元数据，并指定时间数据的导出方式。
