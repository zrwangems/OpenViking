---
type: simulink-block
title: 'Prelookup'
family: lookup-tables
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Lookup Tables'
documentation_page: 'prelookup'
---

# Prelookup

Compute index and fraction for Interpolation Using Prelookup block

## 中文

计算 Interpolation Using Prelookup 模块的索引和区间比

### 所属库

Simulink / Lookup Tables HDL Coder / Lookup Tables

### 描述

Prelookup 模块计算索引和区间比，这些数据说明输入值 `u` 与断点数据集的相对关系。Prelookup 模块最适合与 Interpolation Using Prelookup 模块结合使用。将生成的索引和区间比值馈送给 Interpolation Using Prelookup 模块，以便对 *n* 维表进行插值。这两个模块采用分布式算法。二者结合使用时，执行的运算与 n-D Lookup Table 模块中的积分算法相同。但是，相比 n-D Lookup Table 模块，Prelookup 和 Interpolation Using Prelookup 模块提供了更大的灵活性以及更高效的仿真和代码生成。有关详细信息，请参阅 执行效率。

#### 支持的模块运算

要使用 Prelookup 模块，您必须指定一组断点值。您可以选择是直接在对话框中指定断点值，还是通过将**源**参数设置为**对话框**或**输入端口**来向 `bp` 输入端口馈送值。通常情况下，此断点数据集对应于 Interpolation Using Prelookup 模块中一个维度的表数据。Prelookup 模块通过计算以下项为每个输入值 `u` 生成一对输出：

- 小于或等于 `u` 且构成包含 `u` 的区间的断点集元素的索引
- 区间比（0 ≤ f < 1），表示 `u` 在其所在断点区间前后索引值间的归一化位置

例如，如果断点数据集是 `[0 5 10 20 50 100]` 且输入值 `u` 是 55，则索引为 4 且区间比值为 0.1。索引和区间比的标签在 Prelookup 模块图标上显示为 **k** 和 **f**。索引值从零开始。

对于超出范围的输入，区间比可以为负或大于 `1`。请参阅**外插方法**模块参数以了解详细信息。

### 端口

#### 输入

#### **Port\_1** — 输入信号，`u` 标量 | 向量 | 矩阵

Prelookup 模块接受 Simulink® 支持的任何数值数据类型的实数值信号，但布尔类型除外。Prelookup 模块支持信号和断点数据的定点数据类型。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `enumerated` | `bus`

#### **bp** — 断点数据 实数值信号的一维向量

Prelookup 模块接受以 Simulink 支持的任何数值数据类型的断点数据表示的实数值信号，但布尔类型除外。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `enumerated`
#### 输出

#### **k** — 包含输入 `u` 的区间的索引 标量 | 向量 | 矩阵

从 0 开始的索引 *k* 是实数值整数，它指定包含输入 `u` 的区间。

##### 依赖关系

要启用此端口，请将**输出选择**设置为**索引和区间比**或**仅索引**。

**数据类型:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **f** — 表示区间 *k* 内输入 `u` 的归一化位置的小数 标量 | 向量 | 矩阵

比值 *f* 表示区间 *k* 内输入 `u` 的归一化位置。

##### 依赖关系

要启用此端口，请将**输出选择**设置为**索引和区间比**。

**数据类型:** `single` | `double` | `fixed point`

#### **Port\_2** — 包含索引 *k* 和区间比 *f* 的总线 总线

将索引 *k* 和区间比 *f* 作为总线对象输出可以帮助简化模型。

##### 依赖关系

要启用此端口，请将**输出选择**设置为**索引和区间比作为总线**。

**数据类型:** `bus`

### 参数

#### 常设

##### 断点数据

#### **设定** — 选择如何输入断点数据 **显式值** (默认) | **等间距** | **断点对象**

如果将此参数设置为：

- **显式值**，则**源**和**值**参数在对话框中可见。
- **等间距**，则**第一个点**、**间距**和**点数**参数在对话框中可见。
- **断点对象**，则**名称**参数在对话框中可见。

##### 编程用法

|  |
| --- |
| **模块参数**：`BreakpointsSpecification` |
| **类型：**字符向量 |
| **值：**`'Explicit values' | 'Even spacing' | 'Breakpoint object'` |
| **默认值：**`'Explicit values'` |

要将此参数从 `'Explicit values'` 或 `'Even spacing'` 设置为 `'Breakpoint object'`，请使用相同的 `set_param` 调用来设置 `BreakpointObject` 参数。例如：

```
set_param('myModel/myPrelookupBlock',...
   'BreakpointsSpecification','Breakpoint object',...
   'BreakpointObject','myBPObject')
```

#### **源** — 指定断点数据的来源 **对话框** (默认) | **输入端口**

如果将**源**设置为：

- **对话框**，则在**值**下指定断点数据。
- **输入端口**，请验证上游信号为 `bp` 输入端口提供了断点数据。每个断点数据集必须是包含两个或更多元素的严格单调递增的向量。对于此选项，您的模块从 `bp` 输入端口继承断点属性。

**注意**

使用输入端口指定表或断点数据可能会因为运行时检查对仿真的模块性能产生负面影响。要对需要在仿真期间更改断点的动态特性进行建模，请选择**对话框**并使用 Parameter Writer 模块更改断点数据。

##### 依赖关系

要启用此参数，请将**设定**设置为**显式值**。

##### 编程用法

|  |
| --- |
| **模块参数**：`BreakpointsDataSource` |
| **类型：**字符向量 |
| **值：**`'Dialog' | 'Input port'` |
| **默认值：**`'Dialog'` |

#### **值** — 断点数据值 `[10:10:110]` (默认) | 包含两个或更多元素的严格单调递增值的向量

显式指定断点数据。每个断点数据集必须是包含两个或更多元素的严格单调递增的向量。对于此选项，请在**数据类型**窗格上指定其他断点属性。

要打开查找表编辑器，请点击**编辑**（请参阅查找表编辑器）。

**注意**

当您将**设定**设置为**显式值**且**源**设置为**输入端口**时，请验证上游信号为 `bp` 输入端口提供了断点数据。每个断点数据集必须是包含两个或更多元素的严格单调递增的向量。对于此选项，您的模块从 `bp` 输入端口继承断点属性（包括数据类型）。

##### 依赖关系

要启用此参数，请将**设定**设置为**显式值**并将**源**设置为**对话框**。

##### 编程用法

|  |
| --- |
| **模块参数**：`BreakpointsData` |
| **类型：**字符向量 |
| **值：**包含两个或更多元素的严格单调递增值的向量 |
| **默认值：**`'[10:10:110]'` |

#### **第一个点** — 等间距断点数据中的第一个点 `10` (默认) | 实数值标量

##### 依赖关系

要启用此参数，请将**设定**设置为**等间距**。

##### 编程用法

|  |
| --- |
| **模块参数**：`BreakpointsFirstPoint` |
| **类型：**字符向量 |
| **值：**实数值标量 |
| **默认值：**`'10'` |

#### **间距** — 等间距断点之间的间距 `10` (默认) | 正实数值标量

##### 依赖关系

要启用此参数，请将**设定**设置为**等间距**。

##### 编程用法

|  |
| --- |
| **模块参数**：`BreakpointsSpacing` |
| **类型：**字符向量 |
| **值：**正实数值标量 |
| **默认值：**`'10'` |

#### **点数** — 等间距点数量 `11` (默认) | 正实数值标量

##### 依赖关系

要启用此参数，请将**设定**设置为**等间距**。

##### 编程用法

|  |
| --- |
| **模块参数**：`BreakpointsNumPoints` |
| **类型：**字符向量 |
| **值：**正实数值标量 |
| **默认值：**`'11'` |

#### **名称** — `Simulink.Breakpoint` 对象的名称 无默认值 | `Simulink.Breakpoint` 对象

指定 `Simulink.Breakpoint` 对象的名称。一个断点对象引用 Simulink 断点对象。如果 `Simulink.Breakpoint` 对象不存在，请点击操作按钮  并选择**创建**。新断点对象的对应参数会自动用模块信息填充。

##### 依赖关系

要启用此参数，请将**设定**设置为**断点对象**。

##### 编程用法

|  |
| --- |
| **模块参数**：`BreakpointObject` |
| **类型：**字符向量 |
| **值：**`Simulink.Breakpoint` 对象 |
| **默认值：**`''` |

##### 算法

#### **输出选择** — 指定模块输出的信号 **索引和区间比** (默认) | **索引和区间比作为总线** | **仅索引**

如果您希望模块输出索引和区间比，可以指定模块是输出单个信号还是输出同时包含索引和区间比信号的总线信号。

- **仅索引**仅输出索引，不输出区间比。此选项的典型应用包括：

  - 馈送给 Direct Lookup Table (n-D) 模块，在区间上无插值
  - 馈送给为 Interpolation Using Prelookup 模块选择的子表的端口
  - 执行非线性量化
- **索引和区间比**输出单个信号形式的索引和区间比。
- **索引和区间比作为总线**输出包含索引和区间比信号的总线信号。对这两种信号使用总线：

  - 通过将这两种信号关联在一起来简化模型
  - 为 AUTOSAR 4.0 库创建测试点 `DpResult` 结构体
  - 对于 AUTOSAR 4.0 库，避免当 Prelookup 和 Interpolation Using Prelookup 模块处于不同模型中时在代码生成过程中创建额外副本

  **注意**

  选择**索引和区间比作为总线**将在**数据类型**窗格中显示**输出**参数，并将**输出**参数设置为 **Inherit: auto**。更改此默认值可指定用户定义的总线对象。有关定义总线对象的详细信息，请参阅**输出**参数描述。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutputSelection` |
| **类型：**字符向量 |
| **值：**`'Index and fraction' | 'Index and fraction as bus' | 'Index only'` |
| **默认值：**`'Index and fraction'` |

#### **索引搜索方法** — 搜索断点数据的方法 **二分搜索** (默认) | **线性搜索** | **等间距点**

每种搜索方法在不同情况下均有各自的速度优势：

- 对于等间距断点集（例如，10、20、30 等），您可以选择**等间距点**来计算表索引，以获得最佳速度。此算法仅使用断点集的前两个断点来确定其余点的偏移量和间距。
- 对于非等间距断点集，请遵循以下原则：

  - 如果 `u` 的输入值在各时间步之间变化不大，选择**线性搜索**和**使用上一个索引结果开始索引搜索**将获得最佳性能。
  - 如果 `u` 的输入值在每个时间步跳过一个或两个以上的表间隔，则选择**二分搜索**将获得最佳性能。

对于严重依赖查找表的模型，选择次优索引搜索方法可能会导致性能下降。

**注意**

在以下情况下，生成的代码只存储第一个断点、间距和断点数量：

- 断点数据不可调。
- 索引搜索方法是**等间距点**。

##### 编程用法

|  |
| --- |
| **模块参数**：`IndexSearchMethod` |
| **类型：**字符向量 |
| **值**：`'Evenly spaced points'` | `'Linear search'` | `'Binary search'` |
| **默认值：**`'Binary search'` |

#### **使用上一个索引结果开始索引搜索** — 使用在上一个时间步中找到的索引开始搜索 `off` (默认) | `on`

对于相对于间隔大小而言变化缓慢的 `u` 输入值，启用此选项可以提高性能。否则，线性搜索和二分搜索方法可能需要更长的时间，尤其是对于大型断点集来说。

##### 编程用法

|  |
| --- |
| **模块参数**：`BeginIndexSearchUsingPreviousIndexResult` |
| **类型：**字符向量 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

#### **外插方法** — 处理超出范围的输入值的方法 **裁剪** (默认) | **线性**

选项包括：

- **裁剪**

  | 模块输入 | 模块输出 |
  | --- | --- |
  | 小于第一个断点 | - 第一个断点的索引（例如 `0`） - 区间比为 `0` |
  | 大于最后一个断点 | - 倒数第二个断点的索引 - 区间比为 `1` |

  假定范围是 `[1 2 3]` 并且您选择了此选项。如果 `u` 是 `0.5`，则索引为 `0`，且区间比为 `0`。如果 `u` 是 `3.5`，则索引为 `1`，且区间比为 `1`。
- **线性**

  | 模块输入 | 模块输出 |
  | --- | --- |
  | 小于第一个断点 | - 第一个断点的索引（例如 `0`） - 表示从 `u` 到第一个断点的线性距离的区间比 |
  | 大于最后一个断点 | - 倒数第二个断点的索引 - 表示从倒数第二个断点到 `u` 的线性距离的区间比 |

  假定范围是 `[1 2 3]` 并且您选择了此选项。如果 `u` 是 `0.5`，则索引为 `0`，且区间比为 `-0.5`。如果 `u` 是 `3.5`，则索引为 `1`，且区间比为 `1.5`。

**注意**

仅当满足以下所有条件时，Prelookup 模块才支持线性外插：

- 输入 `u`、断点数据和小数输出使用浮点数据类型。
- 索引使用内置的整数数据类型。

要使用 Prelookup 和 Interpolation Using Prelookup 模块来复制 n-D Lookup Table 模块行为，用于 Prelookup 和 Interpolation Using Prelookup 模块的**外插方法**必须与仅使用 n-D Lookup Table 模块时相同。例如，要获得与**外插方法**设置为**线性**的 n-D Lookup Table 模块相同的行为，请将 Prelookup 和 Interpolation Using Prelookup 模块的**外插方法**设置为**线性**。

##### 编程用法

|  |
| --- |
| **模块参数**：`ExtrapMethod` |
| **类型：**字符向量 |
| **值：**`'Clip' | 'Linear'` |
| **默认值：**`'Clip'` |

#### **将最后一个断点用于等于或高于上限的输入** — 处理等于或高于上限的输入的方法 `off` (默认) | `on`

指定如何对大于或等于最后一个断点的 `u` 的输入值进行索引。索引值从零开始。当输入等于最后一个断点时，模块输出有所不同，如下所示。

| 复选框 | 模块输出 |
| --- | --- |
| 选中 (`on`) | - 断点数据集中最后一个元素的索引 - 区间比为 `0` |
| 清除 (`off`) | - 倒数第二个断点的索引 - 区间比为 `1` |

**提示**

当您对 Prelookup 模块选择**将最后一个断点用于等于或高于上限的输入**时，还必须对它所连接的 Interpolation Using Prelookup 模块选择**有效的索引输入可到达最后一个索引**。此操作允许模块在访问其断点和表数据集的最后一个元素时使用相同的索引约定。

##### 依赖关系

仅当**外插方法**为**裁剪**时，此参数才可见。

##### 编程用法

|  |
| --- |
| **模块参数**：`UseLastBreakpoint` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **假设输入在范围内** — 检查输入值是否超出范围的选项 `off` (默认) | `on`

*自 R2025a 起*

指定是否包含代码以检查超出范围的输入值。选择此参数意味着您保证该模块没有超出范围的输入，从而使模块能够进一步优化代码和仿真。有效输入范围取决于断点数据和**外插方法**设置。

当您选择**假设输入在范围内**时：

- 在仿真期间，模块假定没有超出范围的输入，并通过对超出范围的输入返回错误来强制实现此假设。
- 对于代码生成，模块不会生成超出范围的输入处理代码，因为它假定不存在超出范围的输入。这意味着，如果模块尝试为因输入超出范围而返回错误的模型生成代码，则当给生成的代码提供相同的输入时，其行为是未定义的，这可能导致严重后果。

  **警告**

  如果模型尝试生成代码，但由于模块检测到输入超出范围而生成错误，则当将相同的超出范围的输入传递给已部署的代码时，行为是未定义的。这种未定义的行为可能导致严重问题。对于安全性至关重要的应用，请不要选择**假设输入在范围内**。

如果您要为了提升效率而选择**假设输入在范围内**参数，请确保模型输入在范围内。例如：

| 参数 | 结果 | 何时使用 |
| --- | --- | --- |
| `on` | 仿真和生成的代码中未包含用来检查超出范围的断点输入的条件语句。  当输入超出范围时，仿真和生成的代码可能会发生未定义的行为。 | 为了提升仿真和代码效率 |
| `off` | 仿真和生成的代码包含用来检查超出范围的输入的条件语句。 | 适用于安全性至关重要的应用领域 |

如果您确信输入在范围内，则可以为了提升效率选择**假设输入在范围内**参数。默认情况下，此参数处于清除状态。对于安全性至关重要的应用，不要选择此参数。如果您要选择**假设输入在范围内**参数，请先检查模型输入是否在范围内。例如：

1. 清除**假设输入在范围内**参数。
2. 将**输入超出范围的诊断**参数设置为 `Error`。
3. 在普通模式下进行模型仿真。
4. 如果存在超出范围错误，模块将返回运行时错误。请将它们更正到范围之内，然后再次运行仿真。
5. 当仿真不再生成超出范围的输入错误时，选择**假设输入在范围内**参数。

   **注意**

   当您选择**假设输入在范围内**参数且输入超出范围时，模块会在仿真时返回运行时错误。生成的代码的行为是未定义的。

根据您的具体应用，您可以运行以下模型顾问检查，以验证此参数的使用：

- **按产品** > **Embedded Coder** > **标识哪些查找表模块会生成检查超范围值的高成本代码**
- **按产品** > **Simulink Check** > **建模标准** > **DO-178C/DO-331 检查** > **检查 Lookup Table 模块的使用**

有关模型顾问的详细信息，请参阅运行模型顾问检查。

此外，要确定选择此参数是否安全，如果您拥有 Simulink Design Verifier™ 许可证，请考虑使用 检测模块输入范围违规 (Simulink Design Verifier) 检查。

##### 编程用法

|  |
| --- |
| **模块参数**：`RemoveProtectionInput` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **输入超出范围的诊断** — 当输入超出范围时的模块操作 **无** (默认) | **警告** | **错误**

选项包括：

- **无** - 不产生任何响应。
- **警告** - 显示警告并继续进行仿真。
- **错误** - 终止仿真并显示错误。

##### 编程用法

|  |
| --- |
| **模块参数**：`DiagnosticForOutOfRangeInput` |
| **类型：**字符向量 |
| **值：**`'None' | 'Warning' | 'Error'` |
| **默认值：**`'None'` |

#### **采样时间(-1 表示继承)** — 采样之间的时间间隔 `-1` (默认) | 标量 | 向量

指定采样时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

##### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时才可见。要了解详细信息，请参阅不建议设置采样时间的模块。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SampleTime` |
| **值:** | `"-1"` (默认) | scalar or vector in quotes |

#### 数据类型

#### **断点** — 断点数据类型 `Inherit: Same as input` (默认) | `Inherit: Inherit from 'Breakpoint data'` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

指定断点数据类型。可以将其设置为：

- 继承数据类型的规则，例如**继承: 与输入相同**
- 内置数据类型的名称，例如 `single`
- 数据类型类的名称，例如枚举数据类型类
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

**提示**

- 对于以下情况，指定不同于输入 `u` 的数据类型的断点数据类型：

  - 使用比输入信号 `u` 的类型更小的数据类型存储断点数据时，对内存的要求较低
  - 在其输入 `u` 具有不同数据类型的两个 Prelookup 模块之间共享预定标的断点数据
  - 在为输入 `u` 具有不同数据类型的模块生成的代码中共享自定义存储断点数据
- 如果断点数据类型或其对应的输入数据类型具有定点数据类型，请为二者指定相同的斜率和偏置。
- 枚举数据：

  - 断点支持无序枚举数据。因此，线性搜索也是无序的，这就提供了灵活性，但可能影响性能。搜索从断点中的第一个元素开始。
  - 如果选中**使用上一个索引结果开始索引搜索**参数，则必须使用有序单调递增数据。这种排序可提高性能。
  - 对于枚举数据，**外插方法**必须是 `Clip`。
  - 因为区间比为 `1` 或 `0`，请选择**输出选择** > **仅索引**。

    如果将仅索引输出选择（即“仅索引”）设置与 Interpolation Using Prelookup 模块结合使用，请考虑使用**子表选择维数**参数。

以下是对此模块使用枚举数据的限制：

- 该模块不支持枚举数据的超出范围的输入。指定枚举数据时，请将整个枚举集包含在断点数据集中。例如，使用 `enumeration` 函数。
- 当断点数据源设置为 `Inport port` 时，枚举数据类型必须将 `0` 设置为默认值。例如，对于此枚举类，`GEAR1` 的默认值必须是 `0`。

  ```
  classdef(Enumeration) Gears < Simulink.IntEnumType
      enumeration
          GEAR1(1),
          GEAR2(2),
          GEAR3(4),
          GEAR4(8),
          SPORTS(16),
          REVERSE(32),
          NEUTRAL(0)
      end
  end
  ```

##### 依赖关系

要启用此参数，请将断点数据**源**设置为**对话框**。

**注意**

将**源**设置为**输入端口**时，模块会继承 `bp` 输入端口的所有断点属性（数据类型、最小值和最大值）。

##### 编程用法

|  |
| --- |
| **模块参数**：`BreakpointDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Same as input' | 'Inherit: Inherit from 'Breakpoint data'' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64'| 'fixdt(1,16)' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)'|'<data type expression>'` |
| **默认值：**`'Inherit: Same as input'` |

#### **索引** — 索引数据类型 `uint32` (默认) | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `<data type expression>`

指定可以对断点数据集中的所有元素进行索引的数据类型。您可以：

- 从列表中选择一种内置整数数据类型。
- 使用定点表示指定一种整数数据类型。

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`IndexDataTypeStr` |
| **类型：**字符向量 |
| **值**：`'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | '<data type expression>'` |
| **默认值：**`'uint32'` |

#### **区间比** — 区间比数据类型 `Inherit: Inherit via internal rule` (默认) | `double` | `single` | `fixdt(1,16,0)` | `<data type expression>`

指定区间比的数据类型。您可以：

- 从列表中选择一种内置数据类型。
- 通过内部规则指定数据类型继承。
- 使用 [斜率 偏置] 或二进制小数点定标表示指定一种定点数据类型。

  - 如果您使用 [斜率 偏置] 表示，则定标必须为平凡 - 即斜率为 `1` 且偏置为 `0`。
  - 如果您使用二进制小数点表示，则固定的二次幂指数必须小于或等于零。

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 依赖关系

仅当将**常设**选项卡上的**输出选择**设置为**索引和区间比**时，才显示此参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`FractionDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Inherit via internal rule' | 'double' | 'single' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值：**`'Inherit: Inherit via internal rule'` |

#### **输出** — 输出数据类型 `Inherit: auto` (默认) | **bus: <object name>**

要输出虚拟总线，请使用 `Inherit: auto` 设置。生成的虚拟总线包含两个元素：索引信号和区间比信号。

要输出和指定非虚拟总线，请使用 **Bus: <object name>** 模板。将 **<object name>** 替换为包含索引和区间比信号的总线对象的名称。

- 总线对象必须包含两个元素。第一个元素对应于索引信号，第二个元素对应于区间比信号。
- 索引和区间比总线元素信号不能是总线信号。
- 如果将**输出选择**设置为**索引和区间比**，则总线元素的数据类型和复杂程度必须也满足应用于索引和区间比信号的约束。

要创建具有索引和区间比总线元素的总线对象，请使用类似于以下代码的 MATLAB® 代码，并自定义总线对象名称以及总线元素的名称和数据类型。

```
% Bus object: kfBus
elems(1) = Simulink.BusElement;
elems(1).Name = 'Index';
elems(1).DataType = 'int8';

elems(2) = Simulink.BusElement;
elems(2).Name = 'Fraction';
elems(2).DataType = 'double';

kfBus = Simulink.Bus;
kfBus.Elements = elems;
clear elems;
```

或者，您可以使用类型编辑器创建或修改要与 Prelookup 模块结合使用的总线对象。

如果将总线输出信号从此模块馈送到 Interpolation Using Prelookup 模块，请选择该模块中的**需要以总线输出的索引和区间比**。

**注意**

使用定点工具数据类型选项会将总线对象覆盖为新总线对象，这些新总线对象将定点数据类型替换为浮点数据类型。

与 Prelookup 模块结合使用的被覆盖总线对象会导致错误，因为该模块不接受总线中的第一个元素为浮点数据类型。

如果您遇到此问题，请使用 **Fix** 按钮重新定义原始总线对象并防止其被覆盖。例如，假设您将总线对象的第一个元素定义为 `int32`。

```
myBus.Elements(1).DataType
```

```
int32
```

点击 **Fix** 按钮会重新定义第一个总线元素：

```
myBus.Elements(1).DataType = 'fixdt(''int32'',''DataTypeOverride'',''Off'')'
```

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 依赖关系

仅当将**常设**选项卡上的**输出选择**设置为**索引和区间比作为总线**时，才显示此参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutputBusDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: auto' | 'Bus: <object name>' | '<data type expression>'` |
| **默认值：**`'Inherit: auto'` |

#### **断点最小值** — 最小值断点数据可以有 `[]` (默认) | 标量

指定断点数据可以具有的最小值。默认值为 `[]`（未指定）。

##### 依赖关系

要启用此参数，请在**常设**选项卡上将断点数据**源**设置为**对话框**。

##### 编程用法

|  |
| --- |
| **模块参数**：`BreakpointMin` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'[]'` |

#### **断点最大值** — 最大值断点数据可以有 `[]` (默认) | 标量

指定断点数据可以具有的最大值。默认值为 `[]`（未指定）。

##### 依赖关系

要启用此参数，请在**常设**选项卡上将断点数据**源**设置为**对话框**。

##### 编程用法

|  |
| --- |
| **模块参数**：`BreakpointMax` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'[]'` |

#### **锁定输出数据类型设置以防止被定点工具更改** — 用于防止定点工具覆盖输出数据类型的选项 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您在模块上指定的**输出**数据类型。有关详细信息，请参阅Use Lock Output Data Type Setting (Fixed-Point Designer)。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `LockScale` |
| **值:** | `'off'` (默认) | `'on'` |

#### **整数舍入模式** — 定点运算的舍入模式 **向下** (默认) | **向上** | **收敛** | **最邻近值** | **舍入** | **最简** | **零**

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最邻近的可表示值。要控制模块参数的舍入方法，请在封装字段中使用 MATLAB 舍入函数输入表达式。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RndMeth` |
| **值:** | `'Floor'` (默认) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

**限制**

**必需的模块设置**

- **断点数据**：对于**源**，选择**对话框**。
- **设定**：您可以选择**显式值**或**等间距**。
- **索引搜索方法**：选择**等距点**、**二分搜索**或**线性搜索**。
- **外插方法**：选择**裁剪**。
- **输入超出范围的诊断**：选择**错误**。
- **将最后一个断点用于等于或高于上限的输入**：选择此参数。
- **断点**：对于**数据类型**，选择**继承: 与输入相同**。
- **整数舍入模式**：选择**零**、**向下**或**最简**。

**表数据定型和调整大小**

- 构建表时，最好使断点之间的间距为 2 的幂。如果断点间距不符合此条件，HDL Coder 会发出警告。当断点间距是 2 的幂时，可以用右移位运算替换 prelookup 步骤中的除法运算。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

Simulink PLC Coder 对查找表模块的支持有限。代码生成器不支持：

- 大于 2 的维数
- 三次样条插值方法
- 使用先前的索引模式开始索引搜索
- 三次样条外插方法

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006b 中推出**

#### R2025a: Prelookup 模块的**删除生成代码中防止超范围输入的代码**参数被取代

**删除生成代码中防止超范围输入的代码**参数已被**假设输入在范围内**取代。编程名称 `RemoveProtectionInput` 保持不变。

如果模型仿真因将超出范围的输入馈送到选中**假设输入在范围内**的模块而生成错误，则当生成的代码在执行期间出现相同的超出范围的输入时，该模型生成的代码具有未定义的行为。这种未定义的行为可能导致严重问题。对于安全性至关重要的应用，请不要选择**删除生成代码中防止超范围输入的代码**。

在 R2025a 之前的版本中，**删除生成代码中防止超范围输入的代码**仅会删除生成代码中对超出范围值的代码检查。模块无法检测到这些问题。作为解决方法，如果您有 R2025a 之前版本的模型且无法迁移到更高版本，请将**输入超出范围的诊断**参数设置为**错误**。下次运行模型时，当输入超出范围时将生成错误。

## Libraries

Simulink / Lookup Tables HDL Coder / Lookup Tables

## Description

The Prelookup block calculates the index and interval fraction that specify how its
input value `u` relates to the breakpoint data set. The Prelookup block
works best with the Interpolation Using Prelookup block. Feed
the resulting index and fraction values into an Interpolation Using Prelookup block to
interpolate an *n*-dimensional table. These two blocks have
distributed algorithms. When combined together, they perform the same operation as the
integrated algorithm in the n-D Lookup Table block. However, the
Prelookup and Interpolation Using Prelookup blocks offer
greater flexibility and more efficient simulation and code generation than the
n-D Lookup Table block. For more information, see Efficiency of Performance.

### Supported Block Operations

To use the Prelookup block, you must specify a set of breakpoint values. You
choose whether to specify the breakpoint values directly on the dialog box or by
feeding the values to a `bp` input port by setting the
**Source** parameter to `Dialog` or
`Input port`. Typically, this breakpoint data set
corresponds to one dimension of the table data in an Interpolation Using Prelookup
block. The Prelookup block generates a pair of outputs for each input value
`u` by calculating:

- The index of the breakpoint set element that is less than or equal to
  `u` and forms an interval containing
  `u`
- The interval fraction in the range 0 ≤ f < 1, representing the
  normalized position of `u` on the breakpoint interval
  between the index and the next index value for in-range input

For example, if the breakpoint data set is `[0 5 10 20 50 100]`
and the input value `u` is 55, the index is 4 and the fractional
value is 0.1. Labels for the index and interval fraction appear as
**k** and **f** on the Prelookup block icon.
The index value is zero based.

The interval fraction can be negative or greater than `1` for
out-of-range input. See the **Extrapolation method** block
parameter for more information.

## Ports

### Input

### **Port\_1** — Input signal, `u` scalar | vector | matrix

The Prelookup block accepts real-valued signals of any numeric data
type that Simulink® supports, except Boolean. The Prelookup block supports
fixed-point data types for signals and breakpoint data.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `enumerated` | `bus`

### **bp** — Breakpoint data 1-D vector of real-valued signals

The Prelookup block accepts real-valued signals as breakpoint data of
any numeric data type that Simulink supports, except Boolean.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `enumerated`
### Output

### **k** — Index of the interval containing the input, `u` scalar | vector | matrix

The zero-based index, *k*, is a real-valued integer
that specifies the interval containing the input,
`u`.

#### Dependencies

To enable this port, set the **Output selection**
to `Index and fraction` or
`Index only`.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **f** — Fraction representing the normalized position of the input, `u`, within the interval, *k* scalar | vector | matrix

Fraction, *f*, represents the normalized position of
the input, `u`, within the interval
*k*.

#### Dependencies

To enable this port, set the **Output selection**
to `Index and fraction`.

**Data Types:** `single` | `double` | `fixed point`

### **Port\_2** — Bus containing index, *k*, and fraction, *f* bus

Outputting the index, *k*, and fraction
*f*, as a bus object can help simplify the
model.

#### Dependencies

To enable this port, set the **Output selection**
to `Index and fraction as bus`.

**Data Types:** `bus`

## Parameters

### Main

#### Breakpoints data

### **Specification** — Choose how to enter breakpoint data `Explicit values` (default) | `Even spacing` | `Breakpoint object`

If you set this parameter to:

- `Explicit values`, the
  **Source** and **Value**
  parameters are visible on the dialog box.
- `Even spacing`, the **First
  point**, **Spacing**, and
  **Number of points** parameters are visible
  on the dialog box.
- `Breakpoint object`, the
  **Name** parameter is visible on the dialog
  box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsSpecification` |
| **Type:** character vector |
| **Values:** `'Explicit values' | 'Even spacing' | 'Breakpoint object'` |
| **Default:** `'Explicit values'` |

To set this parameter from `'Explicit values'` or
`'Even spacing'` to `'Breakpoint
object'`, use the same `set_param`
call to set the `BreakpointObject` parameter. For
example:

```
set_param('myModel/myPrelookupBlock',...
   'BreakpointsSpecification','Breakpoint object',...
   'BreakpointObject','myBPObject')
```

### **Source** — Specify source of breakpoint data `Dialog` (default) | `Input port`

If you set **Source** to:

- `Dialog`, specify breakpoint data
  under **Value**.
- `Input port`, verify that an upstream
  signal supplies breakpoint data to the `bp`
  input port. Each breakpoint data set must be a strictly
  monotonically increasing vector that contains two or more
  elements. For this option, your block inherits breakpoint
  attributes from the `bp` input port.

**Note**

Using the input port to specify table or breakpoint data might
negatively affect block performance for simulation due to runtime
checks. To model dynamics that require breakpoints to change during
simulation, select `Dialog` and change the
breakpoint data using the Parameter Writer block.

#### Dependencies

To enable this parameter, set **Specification**
to `Explicit values`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsDataSource` |
| **Type:** character vector |
| **Values:** `'Dialog' | 'Input port'` |
| **Default:** `'Dialog'` |

### **Value** — Breakpoint data values `[10:10:110]` (default) | vector of strictly monotonically increasing values containing two or more elements

Explicitly specify the breakpoint data. Each breakpoint data set must
be a strictly monotonically increasing vector that contains two or more
elements. For this option, you specify additional breakpoint attributes
on the **Data Types** pane.

To open the Lookup Table Editor, click **Edit**
(see Lookup Table Editor).

**Note**

When you set **Specification** to
`Explicit values` and
**Source** to `Input
port`, verify that an upstream signal supplies
breakpoint data to the `bp` input port. Each
breakpoint data set must be a strictly monotonically increasing
vector that contains two or more elements. For this option, your
block inherits breakpoint attributes (including data type) from the
`bp` input port.

#### Dependencies

To enable this parameter, set **Specification**
to `Explicit values` and
**Source** to
`Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsData` |
| **Type:** character vector |
| **Values:** vector of strictly monotonically increasing values containing two or more elements |
| **Default:** `'[10:10:110]'` |

### **First point** — First point in evenly spaced breakpoint data `10` (default) | real-valued scalar

#### Dependencies

To enable this parameter, set **Specification**
to `Even spacing`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsFirstPoint` |
| **Type:** character vector |
| **Values:** real-valued scalar |
| **Default:** `'10'` |

### **Spacing** — Spacing between evenly spaced breakpoints `10` (default) | real-valued, positive scalar

#### Dependencies

To enable this parameter, set **Specification**
to `Even spacing`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsSpacing` |
| **Type:** character vector |
| **Values:** real-valued, positive scalar |
| **Default:** `'10'` |

### **Number of points** — Number of evenly spaced points `11` (default) | real-valued, positive scalar

#### Dependencies

To enable this parameter, set **Specification**
to `Even spacing`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsNumPoints` |
| **Type:** character vector |
| **Values:** real-valued, positive scalar |
| **Default:** `'11'` |

### **Name** — Name of a `Simulink.Breakpoint` object no default | `Simulink.Breakpoint` object

Specify the name of a `Simulink.Breakpoint` object. A
breakpoint object references Simulink breakpoint objects. If a `Simulink.Breakpoint` object does not exist, click the
action button  and select
**Create**. The corresponding parameters of the
new breakpoint object are automatically populated with the block
information.

#### Dependencies

To enable this parameter, set **Specification**
to `Breakpoint object`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointObject` |
| **Type:** character vector |
| **Values:** `Simulink.Breakpoint` object |
| **Default:** `''` |

#### Algorithm

### **Output selection** — Specify the signals the block outputs `Index and fraction` (default) | `Index and fraction as bus` | `Index only`

If you want the block to output the index and interval fraction, you
can specify whether the block outputs individual signals or a bus signal
that includes both the index and fraction signals.

- `Index only` outputs just the index,
  without the fraction. Typical applications for this option
  include:

  - Feeding a Direct Lookup Table (n-D)
    block, with no interpolation on the interval
  - Feeding selection ports of a subtable selection for an
    Interpolation Using Prelookup
    block
  - Performing nonlinear quantizations
- `Index and fraction` outputs the
  index and fraction as individual signals.
- `Index and fraction as bus` outputs a
  bus signal that includes the index and fraction signals. Using a
  bus for these signals:

  - Simplifies the model by tying these two related
    signals together
  - Creates a test point `DpResult`
    structure for the AUTOSAR 4.0 library
  - For the AUTOSAR 4.0 library, avoids the creation of
    extra copies during code generation when the
    Prelookup and Interpolation
    Using Prelookup blocks are in separate
    models

  **Note**

  Selecting `Index and fraction as
  bus` displays the
  **Output** parameter in the
  **Data Types** pane and sets the
  **Output** parameter to
  `Inherit: auto`. Change this
  default value to specify a user-defined bus object. For
  details about defining the bus object, see the
  **Output** parameter
  description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputSelection` |
| **Type:** character vector |
| **Values:** `'Index and fraction' | 'Index and fraction as bus' | 'Index only'` |
| **Default:** `'Index and fraction'` |

### **Index search method** — Method for searching breakpoint data `Binary search` (default) | `Linear search` | `Evenly spaced points`

Each search method has speed advantages in different
situations:

- For evenly spaced breakpoint sets (for example, 10, 20, 30,
  and so on), you achieve optimal speed by selecting
  `Evenly spaced points` to calculate
  table indices. This algorithm uses only the first two
  breakpoints of a set to determine the offset and spacing of the
  remaining points.
- For unevenly spaced breakpoint sets, follow these
  guidelines:

  - If input values for `u` do not vary
    significantly between time steps, selecting
    `Linear search` with
    **Begin index search using previous index
    result** produces the best
    performance.
  - If input values for `u` jump more
    than one or two table intervals per time step, selecting
    `Binary search` produces
    the best performance.

A suboptimal choice of index search method can lead to slow
performance of models that rely heavily on lookup tables.

**Note**

The generated code stores only the first breakpoint, the spacing,
and the number of breakpoints when:

- The breakpoint data is not tunable.
- The index search method is `Evenly spaced
  points`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IndexSearchMethod` |
| **Type:** character vector |
| **Values:** `'Evenly spaced points'` | `'Linear search'` | `'Binary search'` |
| **Default:** `'Binary search'` |

### **Begin index search using previous index result** — Start search using the index found at the previous time step `off` (default) | `on`

For input values of `u` that change slowly with
respect to the interval size, enabling this option can improve
performance. Otherwise, the linear search and binary search methods can
take longer, especially for large breakpoint sets.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BeginIndexSearchUsingPreviousIndexResult` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Extrapolation method** — Method for handling out-of-range input values `Clip` (default) | `Linear`

Options include:

- `Clip`

  | Block Input | Block Outputs |
  | --- | --- |
  | Less than the first breakpoint | - Index of the first breakpoint (for example,   `0`) - Interval fraction of   `0` |
  | Greater than the last breakpoint | - Index of the next-to-last breakpoint - Interval fraction of   `1` |

  Suppose the range is `[1 2 3]` and you select
  this option. If `u` is `0.5`,
  the index is `0` and the interval fraction is
  `0`. If `u` is
  `3.5`, the index is `1`
  and the interval fraction is `1`.
- `Linear`

  | Block Input | Block Outputs |
  | --- | --- |
  | Less than the first breakpoint | - Index of the first breakpoint (for example,   `0`) - Interval fraction that represents the linear   distance from `u` to the first   breakpoint |
  | Greater than the last breakpoint | - Index of the next-to-last breakpoint - Interval fraction that represents the linear   distance from the next-to-last breakpoint to   `u` |

  Suppose the range is `[1 2 3]` and you select
  this option. If `u` is `0.5`,
  the index is `0` and the interval fraction is
  `-0.5`. If `u` is
  `3.5`, the index is `1`
  and the interval fraction is `1.5`.

**Note**

The Prelookup block supports linear extrapolation
only when all of the following conditions are true:

- The input `u`, breakpoint data, and
  fraction output use floating-point data types.
- The index uses a built-in integer data type.

To use Prelookup and Interpolation Using Prelookup blocks to replicate n-D Lookup Table block behavior, the **Extrapolation method** for both Prelookup and Interpolation Using Prelookup blocks must be the same as if you use only the n-D Lookup Table block. For example, to get the same behavior as the n-D Lookup Table block with **Extrapolation method** set to `Linear`, set **Extrapolation method** to `Linear` for both Prelookup and Interpolation Using Prelookup blocks.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ExtrapMethod` |
| **Type:** character vector |
| **Values:** `'Clip' | 'Linear'` |
| **Default:** `'Clip'` |

### **Use last breakpoint for input at or above upper limit** — Method of handling inputs at or above upper limit `off` (default) | `on`

Specify how to index input values of `u` that are
greater than or equal to the last breakpoint. The index value is zero
based. When input equals the last breakpoint, block outputs differ as
follows.

| Check Box | Block Outputs |
| --- | --- |
| Selected (`on`) | - Index of the last element in the breakpoint   data set - Interval fraction of   `0` |
| Cleared (`off`) | - Index of the next-to-last breakpoint - Interval fraction of   `1` |

**Tip**

When you select **Use last breakpoint for input at or
above upper limit** for a Prelookup
block, you must also select **Valid index input may reach
last index** for the Interpolation Using
Prelookup block to which it connects. This action allows
the blocks to use the same indexing convention when accessing the
last elements of their breakpoint and table data sets.

#### Dependencies

This parameter is visible only when **Extrapolation
method** is `Clip`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UseLastBreakpoint` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Assume input is within range** — Option to check for out-of-range input values `off` (default) | `on`

*Since R2025a*

Specify whether or not to include code that checks for out-of-range input values.
Selecting this parameter means that you guarantee that the block has no out-of-range
inputs, enabling the block to further optimize the code and simulation. The valid input
range depends on the breakpoint data and the **Extrapolation method**
setting.

When you select **Assume input is within range**:

- During simulation, the block assumes that there are no out-of-range inputs and
  enforces this assumption by returning an error for out-of-range inputs.
- For code generation, the block does not generate out-of-range input handling
  code because it assumes there is no out-of-range input. This means that if the
  block tries to generate code for a model that returns an error because of
  out-of-range inputs, when the generated code is given the same input, the
  behavior is undefined, which can lead to severe consequence.

  **Warning**

  If the model tries to generate code and instead generates an error
  because the block detects out-of-range input, the behavior is undefined
  if the same out-of-range input is passed to deployed code. This
  undefined behavior might cause severe issues. For safety critical
  applications, do not select **Assume input is within
  range**.

If you want to select the **Assume input is within range** parameter
for efficiency, ensure that your model inputs are in range. For example:

| Parameter | Result | When to Use |
| --- | --- | --- |
| `on` | Simulation and generated code does not include conditional statements to check for out-of-range breakpoint inputs.  When the input is out-of-range, it may cause undefined behavior for simulation and generated code. | For simulation and code efficiency |
| `off` | Simulation and generated code includes conditional statements to check for out-of-range inputs. | For safety-critical applications |

If you are confident your input is within range, you can select the **Assume
input is within range** parameter for efficiency. By default, this
parameter is cleared. For safety-critical applications, do not select this parameter. If
you want to select the **Assume input is within range** parameter,
first check that your model inputs are in range. For example:

1. Clear the **Assume input is within range** parameter.
2. Set the **Diagnostic for out-of-range input** parameter to
   `Error`.
3. Simulate the model in normal mode.
4. If there are out-of-range errors, the block returns runtime errors. Fix them
   to be in range and run the simulation again.
5. When the simulation no longer generates out-of-range input errors, select the
   **Assume input is within range** parameter.

   **Note**

   When you select the **Assume input is within range**
   parameter and the input is out of range, the block returns a runtime error
   at simulation. The behavior is undefined for generated code.

Depending on your application, you can run the following Model Advisor checks to
verify the usage of this parameter:

- **By Product** > **Embedded Coder** > **Identify lookup table blocks that generate expensive
  out-of-range checking code**
- **By Product** > **Simulink Check** > **Modeling Standards** > **DO-178C/DO-331 Checks** > **Check usage of lookup table blocks**

For more information about the Model Advisor, see Run Model Advisor Checks.

Additionally, to determine if it is safe to select this parameter, if you have a
Simulink
Design Verifier™ license, consider using the Detect Block Input Range Violations (Simulink Design Verifier) check.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RemoveProtectionInput` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Diagnostic for out-of-range input** — Block action when input is out of range `None` (default) | `Warning` | `Error`

Options include:

- `None` — Produce no
  response.
- `Warning` — Display a warning
  and continue the simulation.
- `Error` — Terminate the
  simulation and display an error.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DiagnosticForOutOfRangeInput` |
| **Type:** character vector |
| **Values:** `'None' | 'Warning' | 'Error'` |
| **Default:** `'None'` |

### **Sample time (-1 for inherited)** — Interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples. To inherit the sample time, set this
parameter to `-1`. For more information, see Specify Sample Time.

#### Dependencies

This parameter is visible only if you set it to a value other than
`-1`. To learn more, see Blocks for Which Sample Time Is Not Recommended.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | scalar or vector in quotes |

### Data Types

### **Breakpoint** — Breakpoint data type `Inherit: Same as input` (default) | `Inherit: Inherit from 'Breakpoint data'` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

Specify the breakpoint data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Same as input`
- The name of a built-in data type, for example,
  `single`
- The name of a data type class, for example, an enumerated data
  type class
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

**Tip**

- Specify a breakpoint data type different from the data
  type of input `u` for these cases:

  - Lower memory requirement for storing breakpoint
    data that uses a smaller type than the input signal
    `u`
  - Sharing of prescaled breakpoint data between two
    Prelookup blocks with different
    data types for input `u`
  - Sharing of custom storage breakpoint data in the
    generated code for blocks with different data types
    for input `u`
- Specify the same slope and bias for a breakpoint data type
  and its corresponding input data type if either of them has
  a fixed-point data type.
- Enumerated data:

  - Breakpoints support unordered enumerated data. As
    a result, linear searches are also unordered, which
    offers flexibility but can impact performance. The
    search begins from the first element in the
    breakpoint.
  - If the **Begin index search using previous
    index result** parameter is selected, you
    must use ordered monotonically increasing data. This
    ordering improves performance.
  - For enumerated data, **Extrapolation
    method** must be
    `Clip`.
  - Because the fraction is `1` or
    `0`, select **Output selection** > **Index only**.

    If you are using the index only output selection
    setting with the Interpolation Using
    Prelookup block, consider using the
    **Number of sub-table selection
    dimensions** parameter.

These are limitations for using enumerated data with this
block:

- The block does not support out-of-range input for enumerated
  data. When specifying enumerated data, include the entire
  enumeration set in the breakpoint data set. For example, use the
  `enumeration`
  function.
- When breakpoints data source is set to `Inport
  port`, the enumeration data type must have
  `0` as the default value. For example, for
  this enumeration class, the default value of
  `GEAR1` must be `0`.

  ```
  classdef(Enumeration) Gears < Simulink.IntEnumType
      enumeration
          GEAR1(1),
          GEAR2(2),
          GEAR3(4),
          GEAR4(8),
          SPORTS(16),
          REVERSE(32),
          NEUTRAL(0)
      end
  end
  ```

#### Dependencies

To enable this parameter, set the breakpoints data
**Source** to
`Dialog`.

**Note**

When you set **Source** to `Input
port`, the block inherits all breakpoint
attributes (data type, minimum, and maximum) from the
`bp` input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Same as input' | 'Inherit: Inherit from 'Breakpoint data'' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64'| 'fixdt(1,16)' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)'|'<data type expression>'` |
| **Default:** `'Inherit: Same as input'` |

### **Index** — Index data type `uint32` (default) | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `<data type expression>`

Specify a data type that can index all elements in the breakpoint data
set. You can:

- Select a built-in integer data type from the list.
- Specify an integer data type using a fixed-point
  representation.

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IndexDataTypeStr` |
| **Type:** character vector |
| **Values:** `'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | '<data type expression>'` |
| **Default:** `'uint32'` |

### **Fraction** — Fraction data type `Inherit: Inherit via internal rule` (default) | `double` | `single` | `fixdt(1,16,0)` | `<data type expression>`

Specify the data type of the interval fraction. You can:

- Select a built-in data type from the list.
- Specify data type inheritance through an internal rule.
- Specify a fixed-point data type using the [Slope Bias] or
  binary-point-only scaling representation.

  - If you use the [Slope Bias] representation, the
    scaling must be trivial — that is, the slope is
    `1` and the bias is
    `0`.
  - If you use the binary-point-only representation, the
    fixed power-of-two exponent must be less than or equal
    to zero.

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

This parameter displays only when you set **Output
selection** on the **Main**
tab to `Index and fraction`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FractionDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'double' | 'single' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Output** — Output data type `Inherit: auto` (default) | `bus: <object name>`

To output a virtual bus, use the `Inherit: auto`
setting. The resulting virtual bus contains two elements, the index and
the fraction signals.

To output and specify a nonvirtual bus, use the `Bus:
<object name>` template. Replace
`<object name>` with the name of a
bus object that contains the index and fraction signals.

- The bus object must contain two elements. The first element
  corresponds to the index signal and the second to the fraction
  signal.
- The index and fraction bus element signals cannot be bus
  signals.
- The data type and the complexity of the bus elements must meet
  the same constraints that apply to the index and fraction
  signals if you set **Output selection** to
  `Index and fraction`.

To create the bus object with the index and fraction bus elements, use
MATLAB® code similar to this, customizing the bus object name and
the names and data types of the bus elements.

```
% Bus object: kfBus
elems(1) = Simulink.BusElement;
elems(1).Name = 'Index';
elems(1).DataType = 'int8';

elems(2) = Simulink.BusElement;
elems(2).Name = 'Fraction';
elems(2).DataType = 'double';

kfBus = Simulink.Bus;
kfBus.Elements = elems;
clear elems;
```

Alternatively, you can use the Type Editor to create or modify the bus
object to use with the Prelookup block.

If you feed the bus output signal from this block to an
Interpolation Using Prelookup block, select
**Require index and fraction as bus** in that
block.

**Note**

Use the Fixed-Point Tool data type override option to override bus
objects with new bus objects that replace fixed-point data types
with floating-point data types.

Overridden bus objects used with the Prelookup
block can cause an error because the block does not accept
floating-point data types for the first element in the bus.

If you encounter this issue, use the **Fix**
button to redefine the original bus object and protect it from being
overridden. For example, suppose you define the first element of the
bus object to be an `int32`.

```
myBus.Elements(1).DataType
```

```
int32
```

Clicking the **Fix** button redefines the first
bus element:

```
myBus.Elements(1).DataType = 'fixdt(''int32'',''DataTypeOverride'',''Off'')'
```

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

This parameter displays only when you set **Output
selection** on the **Main**
tab to `Index and fraction as bus`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputBusDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: auto' | 'Bus: <object name>' | '<data type expression>'` |
| **Default:** `'Inherit: auto'` |

### **Breakpoint Minimum** — Minimum value breakpoint data can have `[]` (default) | scalar

Specify the minimum value that the breakpoint data can have. The
default value is `[]` (unspecified).

#### Dependencies

To enable this parameter, set the breakpoints data
**Source** to `Dialog`
on the **Main** tab.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointMin` |
| **Type:** character vector |
| **Value:** scalar |
| **Default:** `'[]'` |

### **Breakpoint Maximum** — Maximum value breakpoint data can have `[]` (default) | scalar

Specify the maximum value that the breakpoint data can have. The
default value is `[]` (unspecified).

#### Dependencies

To enable this parameter, set the breakpoints data
**Source** to `Dialog`
on the **Main** tab.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointMax` |
| **Type:** character vector |
| **Value:** scalar |
| **Default:** `'[]'` |

### **Lock output data type setting against changes by the fixed-point tools** — Option to prevent fixed-point tools from overriding Output data type `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the
**Output** data type you specify on the block. For more
information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LockScale` |
| **Values:** | `'off'` (default) | `'on'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations. For more information, see Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To control the
rounding of a block parameter, enter an expression using a MATLAB rounding function into the mask field.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RndMeth` |
| **Values:** | `'Floor'` (default) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Restrictions**

**Required Block Settings**

- **Breakpoint data**: For
  **Source**, select
  `Dialog`.
- **Specification**: You can select either
  `Explicit values` or `Even
  spacing`.
- **Index search method**: Select
  `Evenly spaced points`,
  `Binary search` or `Linear
  search`.
- **Extrapolation method**: Select
  `Clip`.
- **Diagnostic for out-of-range input**: Select
  `Error`.
- **Use last breakpoint for input at or above upper
  limit**: Select this parameter.
- **Breakpoint**: For **Data
  Type**, select `Inherit: Same as
  input`.
- **Integer rounding mode**: Select
  `Zero`,
  `Floor`, or
  `Simplest`.

**Table Data Typing and Sizing**

- It is good practice to structure your table such that the spacing
  between breakpoints is a power of two. If the breakpoint spacing does
  not meet this condition, HDL Coder issues a warning. When the breakpoint spacing is a power
  of two, you can replace division operations in the prelookup step with
  right-shift operations.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

Simulink PLC Coder has limited support for lookup table blocks. The coder does not
support:

- Number of dimensions greater than 2
- Cubic spline interpolation method
- Begin index search using a previous index mode
- Cubic spline extrapolation method

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2006b**

### R2025a: Prelookup block **Remove protection against out-of-range input in generated code** parameter replaced

The **Remove protection against out-of-range input in generated code**
parameter has been replaced by **Assume input is within range**. The
programmatic name, `RemoveProtectionInput`, remains the same.

If the model simulation generates errors because the out-of-range input is fed to a block with
**Assume input is within range** selected, the code generated by the
model has undefined behavior when the same out-of-range input occurs during execution of the
generated code. This undefined behavior might cause severe issues. For safety critical
applications, do not select **Remove protection against out-of-range input in
generated code**.

In releases prior to R2025a, the **Remove protection against out-of-range input in
generated code** only removed the code checks for out-of-range values for
generated code. The block failed to detect these issues. As a workaround. if you have a
model from a release prior to R2025a and cannot migrate to a later release, set the
**Diagnostic for out-of-range input** parameter to
`Error`. The next time you run the model, an error is generated
when the input is out-of-range.
