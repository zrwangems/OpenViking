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



从工作区、文件或 Simulation Data Inspector 加载数据

## 库

Simulink / Sources

## 描述

使用 Playback 模块为仿真加载输入数据。Playback 模块支持加载具有固定或可变维度的实信号或复信号、离散和连续信号以及消息。使用 Playback 模块，可以从以下来源加载数据：

- Simulation Data Inspector 支持的任何数据格式的工作区变量
- 与 Record 模块和 Simulation Data Inspector 支持的格式相同的文件，例如 MAT、MLDATX *(自 R2023a 起)* 和 Microsoft® Excel® 文件
- 来自自定义文件读取器的数据
- Simulation Data Inspector 中的运行

有关 Playback 模块支持的工作区变量和文件格式的更多信息，请参阅将数据从工作区或文件导入 Simulation Data Inspector。

你还可以将 Playback 模块与 Record 模块结合使用，作为录制和回放工作流的一部分。使用 Record 模块录制来自物理设备或仿真的数据。然后，使用 Playback 模块将录制的数据加载到模型中。之后，使用真实或仿真数据，你可以开发、测试和优化模型。

### 向 Playback 模块添加数据

你可以向 Playback 模块添加信号、消息、多维信号、总线以及总线数组。要使用 Playback 模块将数据加载到模型，首先向该模块添加数据。然后，通过将信号或消息分配给端口来选择要加载的数据。运行仿真时，Playback 模块会将数据加载到模型中。

要以交互方式向 Playback 模块添加信号，请双击该模块。双击没有信号的 Playback 模块时，该模块会显示一个带有添加数据选项的屏幕。

你可以从三种类型的源中选择数据添加到 Playback 模块：

- 从基础工作区、模型工作区或掩码工作区添加工作区变量。
- 从文件添加数据。如果文件不在 MATLAB® 路径上或当前目录中，可以点击文件夹图标浏览数据。
- 使用添加信号对话框从工作区、文件或 Simulation Data Inspector 添加数据。

使用添加信号对话框可以访问更多选项，以便从工作区或文件添加数据，或从 Simulation Data Inspector 添加数据。你还可以搜索特定信号。*(自 R2024a 起)* 输入信号名称时，信号表会更新为仅显示包含搜索词的信号名称。你还可以细化搜索以排除部分匹配、匹配特定大小写，或使用正则表达式查找符合特定模式的信号。

当你从工作区或文件添加数据时，可以选择引用源中的信号，或将信号副本保存在模型中。从 Simulation Data Inspector 添加信号数据时，始终会将信号副本保存在模型中。

引用源中的信号会将 Playback 模块中的信号链接到包含信号数据的变量或文件。如果源变量或文件中的数据发生变化，该变化会反映在 Playback 模块加载的数据中。链接数据时，模块上仅存储每个信号的元数据。

当你在模型中保存信号副本时，Playback 模块会从复制的数据加载。对原始数据源变量或文件所做的更改不会反映在 Playback 模块输出中。

添加信号对话框还允许你选择自动还是手动分配端口。如果选择手动分配端口，可以使用 **端口编辑器** 创建端口，并使用信号表的 port 列分配端口。

要以编程方式向 Playback 模块添加信号，请使用 `Simulink.playback.createSignals` 函数创建包含要添加信号的 `Simulink.playback.Signal` 对象。然后，使用 `set_param` 函数将 `Simulink.playback.Signal` 对象应用于 Playback 模块的 **信号** 参数。*(自 R2024a 起)*

例如，要将工作区中变量名为 `x1` 和 `x2` 的信号添加到 Playback 模块：

1. 使用 `Simulink.playback.createSignals` 函数为 `x1` 和 `x2` 信号创建 `Simulink.playback.Signal` 对象。将数据源指定为 workspace，并列出要添加的信号的变量名。
2. 使用 `set_param` 函数将 `Simulink.playback.Signals` 对象设置为 **信号** 参数的值。

    pbSig  = Simulink.playback.createSignals("workspace","Variables",["x1","x2"]);
    set_param("PlaybackModel/Playback","Signals",pbSig);

### 在 Sparkline 可视化中查看信号

添加信号数据后，你可以在 Playback 模块中可视化信号，以便在将数据加载到模型之前验证数据。

默认情况下，Playback 模块使用 sparkline 图绘制数据。添加到 Playback 模块的每个信号都会创建一个 sparkline。如果为总线添加输入数据，则会为每个总线元素创建一个 sparkline。多维信号必须转换为通道或帧才能可视化数据。使用每个信号名称旁边的复选框控制绘制哪些信号。

**注意**

你可以选中或清除复选框来更改 sparkline 可视化的外观，而不会影响 Playback 模块在仿真期间加载到模型中的信号。要控制加载到模型中的信号，请使用信号表中的 port 列。

要更改信号表的外观，请点击 **首选项**。在首选项对话框中，可以选择要显示的信号属性以及如何对信号表中的数据进行分组。可以按以下方式对数据分组：*(自 R2023b 起)*

- Hierarchy — 根据数据层次结构对数据分组。
- Source — 根据数据来源对数据分组。*(自 R2024b 起)*

  - File — 从文件获取并引用的信号会收集在由文件名指定的组中。如果从多个文件添加信号，则会为每个文件创建一个组。
  - Workspace — 从工作区获取并引用的信号会收集在一个名为 `Workspace` 的组中。
  - Saved in model — 保存到模型中的信号（例如从 Simulation Data Inspector 获取的信号）会收集在一个名为 `Signals saved in model` 的组中。
- No grouping — 显示信号的平面列表。

### 在数据表中查看信号

*自 R2025a 起*

要在数据表中查看信号，请在 **仿真** 选项卡的 **视图** 部分中，点击 **显示表**。默认情况下，Playback 模块会创建一个 2 行 1 列布局，其中 sparklines 可视化位于上方子图，数据表位于下方子图。通过选中或清除每个信号名称旁边的复选框，切换绘制哪些信号以及哪些信号出现在表中。表会显示所有绘制的信号，并使用颜色协调的列。当你从信号表或 sparkline 可视化中选择信号时，Playback 模块还会突出显示数据表中的相应列。

Playback 模块中 2 行 1 列布局，上方子图显示 sparkline 可视化，下方子图显示数据表。

你可以更改数据表的位置，使用光标检查数据，并配置表中数据相对于时间的呈现方式。有关更多信息，请参阅在 Playback 模块中查看数据表。

### 查看和编辑信号与端口

你可以使用 Playback 模块中的 **属性** 窗格查看和编辑信号属性。

在 **属性** 窗格中，可以编辑任何白色背景的行。可编辑字段的数量取决于你选择引用源中的信号，还是在模型中保存数据副本。

Playback 模块的端口属性可以使用 **端口编辑器** 与信号属性分开设置。

使用 **端口编辑器**，可以添加端口、删除端口和编辑端口属性。还可以使用信号表的 **Port** 列更改端口分配。默认情况下，端口属性继承自信号。但是，你可以独立于信号属性设置端口属性。当与信号属性兼容时，端口属性决定 Playback 模块的输出。例如，你可以通过将具有已分配测量单位的信号的 **单位** 属性设置为不同的测量单位，来转换该信号的单位。当信号单位和端口单位兼容时，Playback 模块会执行单位转换。

Playback 模块支持多速率采样时间，允许你为每个端口设置不同的采样时间。端口采样时间也可以与信号采样时间分开设置。

### 导出添加到 Playback 模块的数据

*自 R2023a 起*

你可以使用 Playback 模块聚合来自工作区、文件和 Simulation Data Inspector（从源链接或保存在模型中）的数据，并将该数据导出到工作区或文件。Playback 模块会导出添加到该模块的所有数据，即使信号未分配给端口也是如此。要导出添加到 Playback 模块的所有数据：

1. 在 **仿真** 选项卡的 **共享** 部分中，点击 **导出**。
2. 选择 **基础工作区** 或 **文件**，将数据导出到工作区或文件。你可以选择将数据导出到工作区，或导出为 MAT、MLDATX 或 Microsoft Excel 文件。
3. 点击 **导出**。

如果选择将数据导出到 MLDATX 文件，可以使用 **导出的运行名称** 文本框指定运行的名称。

如果选择将数据导出到 Excel 文件，请点击 **选项** 选择要导出的元数据，并指定时间数据的导出方式。

## 端口

### 输出

### **Port\_1** — 从工作区、文件或 Simulation Data Inspector 加载的数据 标量 | 向量 | 矩阵 | 数组

Playback 模块支持加载具有固定或可变维度的实信号或复信号、离散和连续信号、消息、多维信号、总线和总线数组。

当你加载总线数据时，Playback 模块会为总线的每个元素分配一个端口。

如果数据类型为浮点 `half`，Playback 模块无法将数据作为消息加载。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`
**复数支持：** Yes

## 参数

### 端口参数

你可以通过 **端口编辑器** 访问端口参数。双击 Playback 模块。在 **仿真** 选项卡的 **端口** 部分中，点击 **端口编辑器**。可以使用 **端口编辑器** 独立设置每个端口的属性。

### **端口数** — 输出端口数量 `0` (default) | integer in the range [`0,100`]

当你向 Playback 模块添加信号并自动将信号分配给端口时，会为添加的每个信号或总线元素创建一个新端口。添加信号数据后，可以添加或删除端口。端口数量不必等于添加到模块的信号数量。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `NumPorts` |
| **值：** | `0` (default) | integer in the range [`0`,`100`] |
| **数据类型：** | `integer` |

**示例：** `set_param(gcb,"NumPorts",5)`

### **数据类型** — 每个端口的输出数据类型 `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `string` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | ...

默认情况下，端口数据类型继承自源数据类型或下游模块。

你可以独立于信号数据类型设置端口的数据类型。对于数值数据，Playback 模块会转换为端口指定的数据类型。如果无法转换，例如将数值数据转换为字符串的情况，软件会抛出错误。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

字符串数组的大小等于端口数量。每个元素的索引由端口编号确定。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `"Inherit: auto"` (default) | `"double"` | `"single"` | `"half"` | `"int8"` |  `"uint8"`  | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"string"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` |
| **数据类型：** | `string array` |

**示例：** `set_param(gcb,"OutDataTypeStr",["double","int64"])`

### **Complexity** — 每个端口的复数性 `"auto"` (default) | `"real"` | `"complex"`

你可以独立指定每个端口的复数性。端口复数性不必与相应信号的复数性匹配。默认情况下，端口的复数性为 `"auto"`，并继承自信号数据。

- 如果信号数据为实数，则加载该信号的端口的复数性可以为实数或复数。如果端口设置为 `"complex"`，则信号的虚部为信号接地。
- 如果信号数据为复数，则加载该信号的端口的复数性必须为复数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

字符串数组的大小等于端口数量。每个元素的索引由端口编号确定。

|  |  |
| --- | --- |
| **参数：** | `PortComplexity` |
| **值：** | `"auto"` (default) | `"real"` | `"complex"` |
| **数据类型：** | `string array` |

**示例：** `set_param(gcb,"PortComplexity",["auto","real","complex","real"])`

### **Units** — 每个端口的物理单位 inherit (default) | supported physical unit

每个端口的物理单位，指定为支持的物理单位。要查看支持的物理单位列表，请使用函数 `showunitslist`。

    showunitslist

- 如果未在端口上设置单位，则输出单位继承自信号单位。
- 如果信号和端口上设置了不同的单位，则当单位兼容时，Playback 模块会执行单位转换。

Playback 模块会为每个端口传播单位。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

字符串数组的大小等于端口数量。每个元素的索引由端口编号确定。

|  |  |
| --- | --- |
| **参数：** | `PortUnits` |
| **值：** | `" "` (default) | supported physical unit |
| **数据类型：** | `string array` |

**示例：** `set_param(gcb,"PortUnits",["m","m/s","m/s^2"])`

### **Sample time** — 输出采样周期和可选时间偏移 `-1` | scalar | vector

**Sample time** 参数指定模块在仿真期间计算新输出值的时间。有关详细信息，请参阅指定采样时间。

当你不希望输出具有时间偏移时，将 **Sample time** 参数指定为标量。要向输出添加时间偏移，请将 **Sample time** 参数指定为 `1`×`2` 向量，其中第一个元素是采样周期，第二个元素是偏移量。

默认情况下，**Sample time** 参数值为 `-1`，表示端口采样时间继承自信号。如果端口的采样时间与关联信号的采样时间不同，Playback 模块会根据信号的插值设置按需对数据进行插值。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

字符串数组的大小等于端口数量。每个元素的索引由端口编号确定。

|  |  |
| --- | --- |
| **参数：** | `PortSampleTimes` |
| **值：** | `"-1"` (default) | scalar | vector |
| **数据类型：** | `string array` |

**示例：** `set_param(gcb,"PortSampleTimes",["-1","0","inf"])`

### **Dimensions** — 每个端口的维度 `" "` (default) | integer | integer array

要从数据继承端口的维度，请将参数留空。如果端口没有分配数据，设置维度会生成 ground。

Playback 模块将多维信号存储为具有非标量样本值的单个信号、一组通道或帧。有关更多信息，请参阅分析多维信号数据。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

cell array 的大小等于端口数量。每个元素的索引由端口编号确定。

|  |  |
| --- | --- |
| **参数：** | `PortDimensions` |
| **值：** | 空 `1×1` cell array (default) | cell array of positive integers | cell array of vectors |
| **数据类型：** | `cell array` |

**示例：** `set_param(gcb,"PortDimensions",[{2},{[1,2,3]}])`

### **Dimension Mode** — 每个端口的维度模式 `"auto"` (default) | `"Fixed"` | `"Variable"`

每个端口的维度模式，返回为字符串数组，其中每个元素可以为 `"auto"`、`"Fixed"` 或 `"Variable"`。

- 如果维度模式为 `"auto"`，则端口从数据继承维度模式。
- 如果维度模式为 `"Fixed"`，则端口仅允许固定大小信号。
- 如果维度模式为 `"Variable"`，则端口仅允许可变大小信号。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

字符串数组的大小等于端口数量。每个元素的索引由端口编号确定。

|  |  |
| --- | --- |
| **参数：** | `PortDimsModes` |
| **值：** | `"auto"` (default) | `"Fixed"` | `"Variable"` |
| **数据类型：** | `string array` |

**示例：** `set_param(gcb,"PortDimsModes",["Fixed","auto"])`

### 模块参数

你可以通过 **参数设置** 访问大多数模块参数。双击 Playback 模块。在 **仿真** 选项卡中，点击 **参数设置** 配置模块参数。

模块参数设置适用于所有端口。

### **第一个点之前** — 用于确定加载数据中第一个数据点之前模块输出的外插方法 `Linear` (default) | `Hold First Value` | `Ground Value`

用于确定在文件、工作区或 Simulation Data Inspector 数据中第一个样本之前的仿真时间输出值的外插方法。

| 方法 | 描述 | 示例 |
| --- | --- | --- |
| `Linear` | 外插输出取决于数据类型。  - 对于 `double` 数据，Playback 模块使用前两个样本对输出值进行线性外插。 - 对于 `Boolean` 数据，Playback 模块使用第一个数据点的值作为输出值。 - 对于所有其他内置数据类型，Playback 模块：  1. 将数据上转型为 `double`   2. 使用前两个数据样本对输出值进行线性外插   3. 将外插后的数据值下转型为原始数据类型  如果数据仅包含一个样本，Playback 模块会在输出端提供该值。 当 Playback 模块加载枚举或定点数据时，不要使用 `Linear` 选项。 外插设置会应用于总线中的所有信号。如果总线中的任何信号包含枚举或定点数据，请不要使用 `Linear` 选项。 | 显示 Playback 模块输出的图，该模块配置为对加载数据中第一个样本之前的仿真时间输出值进行线性外插。该模块加载从仿真开始后 2 秒开始的数据。 |
| `Hold First Value` | Playback 模块使用第一个数据值作为输出值。 | 显示 Playback 模块输出的图，该模块配置为对加载数据中第一个样本之前的仿真时间保持加载数据中的第一个值。该模块加载从仿真开始后 2 秒开始的数据。 |
| `Ground Value` | 外插输出取决于数据类型。  - 内置数值类型 — `0` - `Boolean` — `false` - 定点数据类型 — 值 `0` 的表示形式，由于缩放和有限精度，该值可能并不精确等于 `0`。 - 枚举数据类型 — 默认值 | 显示 Playback 模块输出的图，该模块配置为对加载数据中第一个样本之前的仿真时间使用 ground 值作为输出值。该模块加载从仿真开始后 2 秒开始的数据。 |

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ExtrapolationBeforeFirstDataPoint` |
| **值：** | `"Linear extrapolation"` (default) | `"Hold first value"` | `"Ground value"` |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param(gcb,"ExtrapolationBeforeFirstDataPoint","Hold first value")`

### **最后一个点之后** — 用于确定加载数据中最后一个数据点之后模块输出的外插方法 `Linear` (default) | `Hold Last Value` | `Ground Value`

用于确定在文件、工作区或 Simulation Data Inspector 数据中最后一个样本之后的仿真时间输出值的外插方法。

| 方法 | 描述 | 示例 |
| --- | --- | --- |
| `Linear` | 外插输出取决于数据类型。  - 对于 `double` 数据，Playback 模块使用最后两个样本对输出值进行线性外插。 - 对于 `Boolean` 数据，Playback 模块使用最后一个样本值作为输出值。 - 对于所有其他内置数据类型，Playback 模块：  1. 将数据上转型为 `double`   2. 使用最后两个数据样本对输出值进行线性外插   3. 将外插后的数据值下转型为原始数据类型  如果数据仅包含一个样本，Playback 模块会将该值用作输出。 当 Playback 模块加载枚举或定点数据时，不要使用 `Linear` 选项。 | 显示 Playback 模块输出的图，该模块配置为对加载数据中最后一个样本之后的仿真时间输出值进行线性插值。该模块加载在仿真结束前 2 秒结束的数据。 |
| `Hold Last Value` | Playback 模块使用最后一个数据值作为输出值。 | 显示 Playback 模块输出的图，该模块配置为对加载数据中最后一个样本之后的仿真时间保持最后一个输出值。该模块加载在仿真结束前 2 秒结束的数据。 |
| `Ground Value` | Playback 模块输出值取决于数据类型。  - 内置数值类型 — `0` - `Boolean` — `false` - 定点数据类型 — 值 `0` 的表示形式，由于缩放和有限精度，该值可能并不精确等于 `0`。 - 枚举数据类型 — 默认值 | 显示 Playback 模块输出的图，该模块配置为对加载数据中最后一个样本之后的仿真时间使用 ground 值作为输出值。该模块加载在仿真结束前 2 秒结束的数据。 |

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ExtrapolationAfterLastDataPoint` |
| **值：** | `"Linear extrapolation"` (default) | `"Hold last value"` | `"Ground value"` |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param(gcb,"ExtrapolationAfterLastDataPoint","Hold last value")`

### **启用零交叉检测** — 零交叉检测 `'off'` (default) | `'on'`

零交叉检测可定位模块输出中的不连续性，即 *zero crossings*，并防止在不连续点附近出现过小的时间步长，从而避免减慢仿真。仅当信号的采样时间为连续时，Playback 模块才会检测信号的零交叉。

当加载的数据包含多个具有相同时间的样本时，会在模块输出中产生不连续性。例如，对于以下输入数据，在时间 `2` 处发生不连续性。

    time:     0 1 2 2 3
    signal:   2 3 4 5 6

Playback 模块还可能根据你配置插值和外插的方式在输出中产生不连续性。

- 将 **第一个点之前** 设置为 `Ground Value` 可能会在加载数据的第一个样本处产生不连续性。
- 将 **最后一个点之后** 设置为 `Ground Value` 可能会在加载数据的最后一个样本处产生不连续性。

此模块仅在使用可变步长求解器的仿真中支持零交叉检测。当你使用固定步长求解器进行仿真时，软件不会检测或定位此模块的零交叉。

有关更多信息，请参阅零交叉检测。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ZeroCross` |
| **值：** | `"off"` (default) | `"on"` |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param(gcb,"ZeroCross","on")`

### **信号** — 添加到 Playback 模块的信号的信息 `Simulink.playback.Signal` 对象

*自 R2024a 起*

添加到 Playback 模块的信号的信息，指定为 `Simulink.playback.Signal` 对象。

你可以使用 **信号** 参数通过 `get_param` 函数检索模块中信号的信息，或使用 `set_param` 函数向模块添加新信号。`Simulink.playback.Signal` 对象存储有关添加到 Playback 模块的信号的信息。

要向 Playback 模块添加一个或多个信号，请使用 `Simulink.playback.createSignals` 函数创建 `Simulink.playback.Signal` 对象。然后，使用 `set_param` 函数将 `Simulink.playback.Signal` 对象应用于 Playback 模块的 **信号** 参数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Signals` |
| **值：** | `Simulink.playback.Signal` 对象 |

**示例：** `set_param(gcb,"Signals",pgSigObj)`

### 表参数

你可以通过表可视化的 **格式** 选项卡访问表参数。要查看所绘制信号的数据表，请在 **仿真** 选项卡的 **视图** 部分中点击 **显示表**。要配置表参数，请选择表可视化，然后点击 **格式** 选项卡。

### **Table Placement** — 表可视化的位置 `Bottom` (default) | `Top` | `Left` | `Right` | `Center`

表可视化相对于 sparklines 可视化的位置，指定为以下选项之一：

- `Bottom` — 2 行 1 列布局，数据表位于下方子图，sparklines 可视化位于上方子图
- `Top` — 2 行 1 列布局，数据表位于上方子图，sparklines 可视化位于下方子图
- `Left` — 1 行 2 列布局，数据表位于左侧子图，sparklines 可视化位于右侧子图
- `Right` — 1 行 2 列布局，数据表位于右侧子图，sparklines 可视化位于左侧子图
- `Center` — 仅包含数据表的 1 行 1 列布局

### **Time Values** — 基于时间的列组织选项 `Union Time` (default) | `Shared Time` | `Individual Time`

基于时间的列组织，指定为 `Union Time`、`Shared Time` 或 `Individual Time`。

| 列组织选项 | 描述 | 表格式 |
| --- | --- | --- |
| `Shared Time` | 数据按共享时间列分组。 | 具有共享时间列的数据表 |
| `Individual Time` | 每个信号与其对应的时间列配对。 | 具有单独时间列的数据表 |
| `Union Time` | 数据与单个时间列对齐，该列包含信号之间的每个样本时间。  当某个信号在给定时间步没有数据值时，该单元格为空。要插值缺失的数据值，请在 **格式** 选项卡中点击 **使用信号插值**。使用 **属性** 窗格中的 `Interp Method` 属性查看或更改所选信号的插值方法。 | 具有统一时间列的数据表 |

### **使用信号插值** — 用于插值缺失数据值的选项 `off` (default) | `on`

当你使用 `Union Time` 列组织选项组织表数据时，某些信号可能没有每个时间步的数据点。点击 **使用信号插值** 按钮，使用每个信号的插值设置来插值缺失的数据值。要查看或更改所选信号的插值方法，请使用 **属性** 窗格中的 `Interp Method` 属性。

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **零交叉检测** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不推荐用于生产代码。

## 版本历史

**在 R2022b 中引入**

### R2025a：在数据表中查看信号

除了 sparklines 可视化外，你还可以在数据表中查看绘制的信号。

### R2024b：按源对数据分组

你可以按源对信号表中的数据分组。按源对信号分组时，信号会根据数据来源于文件、工作区还是保存在模型中进行组织。

### R2024a：以编程方式向 Playback 模块添加数据

你可以通过将 `Simulink.playback.Signal` 对象应用于模块的 **信号** 参数，以编程方式将来自工作区、文件或 Simulation Data Inspector 的数据添加到 Playback 模块。

### R2024a：在添加信号对话框中搜索信号

当你使用添加信号对话框向 Playback 模块添加信号时，可以搜索特定信号。你还可以细化搜索以排除部分匹配、匹配特定大小写，或使用正则表达式查找符合特定模式的信号。

### R2023b：添加了首选项对话框

Playback 模块中新增了首选项对话框，可用于选择如何对信号表中的数据分组以及显示哪些信号属性。你可以选择按数据层次结构对信号分组，也可以选择不对数据分组，而是显示信号的平面列表。

### R2023a：加载 MLDATX 文件

Playback 模块支持从 Simulation Data Inspector 会话文件加载数据。从原生 MLDATX 文件格式添加数据可加快加载时间，并允许你从大型数据集中选择性地加载单个信号。

### R2023a：从 Playback 模块导出数据

你可以聚合已从不同源（从源链接或保存在模型中）添加到 Playback 模块的数据，并将该数据导出到工作区或文件。
