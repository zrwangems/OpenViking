---
type: simulink-block
title: 'Prelookup'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Lookup Tables'
documentation_page: 'prelookup'
documentation_source_path: '../simulink/slref/prelookup.html'
language: zh-CN
chinese_source: worker-translation
---

# Prelookup

## 端口

### 输入

### **Port\_1** — 输入信号，`u` 标量 | 向量 | 矩阵

Prelookup 模块接受 Simulink® 支持的任何数值数据类型的实值信号，但布尔类型除外。Prelookup 模块支持信号和断点数据的定点数据类型。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `enumerated` | `bus`

### **bp** — 断点数据 实值信号的一维向量

Prelookup 模块接受实值信号作为断点数据，数据类型可以是 Simulink 支持的任何数值数据类型，但布尔类型除外。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `enumerated`
### 输出

### **k** — 包含输入 `u` 的区间索引 标量 | 向量 | 矩阵

从零开始的索引 *k* 是一个实值整数，用于指定包含输入 `u` 的区间。

#### 依赖关系

要启用此端口，请将 **Output selection** 设置为 `Index and fraction` 或 `Index only`。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **f** — 表示输入 `u` 在区间 *k* 内归一化位置的小数 标量 | 向量 | 矩阵

小数 *f* 表示输入 `u` 在区间 *k* 内的归一化位置。

#### 依赖关系

要启用此端口，请将 **Output selection** 设置为 `Index and fraction`。

**数据类型：** `single` | `double` | `fixed point`

### **Port\_2** — 包含索引 *k* 和小数 *f* 的总线 总线

将索引 *k* 和小数 *f* 作为总线对象输出有助于简化模型。

#### 依赖关系

要启用此端口，请将 **Output selection** 设置为 `Index and fraction as bus`。

**数据类型：** `bus`

## 参数

### 主要

#### 断点数据

### **Specification** — 选择如何输入断点数据 `Explicit values`（默认）| `Even spacing` | `Breakpoint object`

如果将此参数设置为：

- `Explicit values`，则对话框上会显示 **Source** 和 **Value** 参数。
- `Even spacing`，则对话框上会显示 **First point**、**Spacing** 和 **Number of points** 参数。
- `Breakpoint object`，则对话框上会显示 **Name** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`BreakpointsSpecification` |
| **类型**：character vector |
| **值**：`'Explicit values' | 'Even spacing' | 'Breakpoint object'` |
| **默认值**：`'Explicit values'` |

要将此参数从 `'Explicit values'` 或 `'Even spacing'` 设置为 `'Breakpoint object'`，请使用同一个 `set_param` 调用设置 `BreakpointObject` 参数。例如：

```
set_param('myModel/myPrelookupBlock',...
   'BreakpointsSpecification','Breakpoint object',...
   'BreakpointObject','myBPObject')
```

### **Source** — 指定断点数据的来源 `Dialog`（默认）| `Input port`

如果将 **Source** 设置为：

- `Dialog`，请在 **Value** 下指定断点数据。
- `Input port`，请验证上游信号向 `bp` 输入端口提供断点数据。每个断点数据集必须是包含两个或更多元素的严格单调递增向量。对于此选项，模块从 `bp` 输入端口继承断点属性。

**注意**

使用输入端口指定表或断点数据可能会因运行时检查而对模块的仿真性能产生负面影响。要对需要在仿真期间更改断点的动态行为进行建模，请选择 `Dialog` 并使用 Parameter Writer 模块更改断点数据。

#### 依赖关系

要启用此参数，请将 **Specification** 设置为 `Explicit values`。

#### 编程使用

|  |
| --- |
| **模块参数**：`BreakpointsDataSource` |
| **类型**：character vector |
| **值**：`'Dialog' | 'Input port'` |
| **默认值**：`'Dialog'` |

### **Value** — 断点数据值 `[10:10:110]`（默认）| 包含两个或更多元素的严格单调递增向量

显式指定断点数据。每个断点数据集必须是包含两个或更多元素的严格单调递增向量。对于此选项，请在 **Data Types** 窗格中指定其他断点属性。

要打开 Lookup Table Editor，请点击 **Edit**（请参阅 Lookup Table Editor）。

**注意**

当您将 **Specification** 设置为 `Explicit values` 并将 **Source** 设置为 `Input port` 时，请验证上游信号向 `bp` 输入端口提供断点数据。每个断点数据集必须是包含两个或更多元素的严格单调递增向量。对于此选项，模块从 `bp` 输入端口继承断点属性（包括数据类型）。

#### 依赖关系

要启用此参数，请将 **Specification** 设置为 `Explicit values`，并将 **Source** 设置为 `Dialog`。

#### 编程使用

|  |
| --- |
| **模块参数**：`BreakpointsData` |
| **类型**：character vector |
| **值**：vector of strictly monotonically increasing values containing two or more elements |
| **默认值**：`'[10:10:110]'` |

### **First point** — 均匀间隔断点数据中的第一个点 `10`（默认）| 实值标量

#### 依赖关系

要启用此参数，请将 **Specification** 设置为 `Even spacing`。

#### 编程使用

|  |
| --- |
| **模块参数**：`BreakpointsFirstPoint` |
| **类型**：character vector |
| **值**：real-valued scalar |
| **默认值**：`'10'` |

### **Spacing** — 均匀间隔断点之间的间距 `10`（默认）| 实值正标量

#### 依赖关系

要启用此参数，请将 **Specification** 设置为 `Even spacing`。

#### 编程使用

|  |
| --- |
| **模块参数**：`BreakpointsSpacing` |
| **类型**：character vector |
| **值**：real-valued, positive scalar |
| **默认值**：`'10'` |

### **Number of points** — 均匀间隔点的数量 `11`（默认）| 实值正标量

#### 依赖关系

要启用此参数，请将 **Specification** 设置为 `Even spacing`。

#### 编程使用

|  |
| --- |
| **模块参数**：`BreakpointsNumPoints` |
| **类型**：character vector |
| **值**：real-valued, positive scalar |
| **默认值**：`'11'` |

### **Name** — `Simulink.Breakpoint` 对象的名称 无默认值 | `Simulink.Breakpoint` 对象

指定 `Simulink.Breakpoint` 对象的名称。断点对象引用 Simulink 断点对象。如果 `Simulink.Breakpoint` 对象不存在，请点击操作按钮  并选择 **Create**。新断点对象的相应参数将自动填充模块信息。

#### 依赖关系

要启用此参数，请将 **Specification** 设置为 `Breakpoint object`。

#### 编程使用

|  |
| --- |
| **模块参数**：`BreakpointObject` |
| **类型**：character vector |
| **值**：`Simulink.Breakpoint` object |
| **默认值**：`''` |

#### 算法

### **Output selection** — 指定模块输出的信号 `Index and fraction`（默认）| `Index and fraction as bus` | `Index only`

如果希望模块输出索引和区间小数，可以指定模块输出单独的信号，还是输出同时包含索引和小数信号的单个总线信号。

- `Index only` 仅输出索引，不输出小数。此选项的典型应用包括：

  - 馈入 Direct Lookup Table (n-D) 模块，不在区间上进行插值
  - 馈入 Interpolation Using Prelookup 模块的子表选择的 selection 端口
  - 执行非线性量化
- `Index and fraction` 将索引和小数作为单独信号输出。
- `Index and fraction as bus` 输出包含索引和小数信号的总线信号。对这些信号使用总线可以：

  - 通过将这两个相关信号绑定在一起来简化模型
  - 为 AUTOSAR 4.0 库创建测试点 `DpResult` 结构体
  - 对于 AUTOSAR 4.0 库，当 Prelookup 和 Interpolation Using Prelookup 模块位于不同模型中时，避免在代码生成期间创建额外副本

  **注意**

  选择 `Index and fraction as bus` 会在 **Data Types** 窗格中显示 **Output** 参数，并将 **Output** 参数设置为 `Inherit: auto`。请更改此默认值以指定用户定义的总线对象。有关定义总线对象的详细信息，请参阅 **Output** 参数说明。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputSelection` |
| **类型**：character vector |
| **值**：`'Index and fraction' | 'Index and fraction as bus' | 'Index only'` |
| **默认值**：`'Index and fraction'` |

### **Index search method** — 搜索断点数据的方法 `Binary search`（默认）| `Linear search` | `Evenly spaced points`

每种搜索方法在不同情况下具有速度优势：

- 对于均匀间隔的断点集（例如 10、20、30 等），通过选择 `Evenly spaced points` 来计算表索引可获得最佳速度。此算法仅使用集合的前两个断点来确定其余点的偏移和间距。
- 对于非均匀间隔的断点集，请遵循以下准则：

  - 如果 `u` 的输入值在时间步之间变化不大，选择 `Linear search` 并启用 **Begin index search using previous index result** 可获得最佳性能。
  - 如果 `u` 的输入值每个时间步跳过一个或两个以上的表区间，选择 `Binary search` 可获得最佳性能。

索引搜索方法的次优选择可能导致严重依赖查找表的模型性能变慢。

**注意**

当满足以下条件时，生成的代码仅存储第一个断点、间距和断点数量：

- 断点数据不可调。
- 索引搜索方法为 `Evenly spaced points`。

#### 编程使用

|  |
| --- |
| **模块参数**：`IndexSearchMethod` |
| **类型**：character vector |
| **值**：`'Evenly spaced points'` | `'Linear search'` | `'Binary search'` |
| **默认值**：`'Binary search'` |

### **Begin index search using previous index result** — 使用上一时间步找到的索引开始搜索 `off`（默认）| `on`

对于相对于区间大小变化缓慢的 `u` 输入值，启用此选项可以提高性能。否则，线性搜索和二分搜索方法可能需要更长时间，尤其是对于大型断点集。

#### 编程使用

|  |
| --- |
| **模块参数**：`BeginIndexSearchUsingPreviousIndexResult` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Extrapolation method** — 处理超出范围输入值的方法 `Clip`（默认）| `Linear`

选项包括：

- `Clip`

  | 模块输入 | 模块输出 |
  | --- | --- |
  | 小于第一个断点 | - 第一个断点的索引（例如 `0`） - 区间小数为 `0` |
  | 大于最后一个断点 | - 倒数第二个断点的索引 - 区间小数为 `1` |

  假设范围为 `[1 2 3]` 且您选择此选项。如果 `u` 为 `0.5`，则索引为 `0`，区间小数为 `0`。如果 `u` 为 `3.5`，则索引为 `1`，区间小数为 `1`。
- `Linear`

  | 模块输入 | 模块输出 |
  | --- | --- |
  | 小于第一个断点 | - 第一个断点的索引（例如 `0`） - 表示从 `u` 到第一个断点的线性距离的区间小数 |
  | 大于最后一个断点 | - 倒数第二个断点的索引 - 表示从倒数第二个断点到 `u` 的线性距离的区间小数 |

  假设范围为 `[1 2 3]` 且您选择此选项。如果 `u` 为 `0.5`，则索引为 `0`，区间小数为 `-0.5`。如果 `u` 为 `3.5`，则索引为 `1`，区间小数为 `1.5`。

**注意**

Prelookup 模块仅在满足以下所有条件时支持线性外插：

- 输入 `u`、断点数据和小数输出使用浮点数据类型。
- 索引使用内置整数数据类型。

要使用 Prelookup 和 Interpolation Using Prelookup 模块复现 n-D Lookup Table 模块的行为，Prelookup 和 Interpolation Using Prelookup 模块的 **Extrapolation method** 必须与仅使用 n-D Lookup Table 模块时相同。例如，要获得与 **Extrapolation method** 设置为 `Linear` 的 n-D Lookup Table 模块相同的行为，请将 Prelookup 和 Interpolation Using Prelookup 模块的 **Extrapolation method** 都设置为 `Linear`。

#### 编程使用

|  |
| --- |
| **模块参数**：`ExtrapMethod` |
| **类型**：character vector |
| **值**：`'Clip' | 'Linear'` |
| **默认值**：`'Clip'` |

### **Use last breakpoint for input at or above upper limit** — 处理等于或高于上限的输入的方法 `off`（默认）| `on`

指定如何索引大于或等于最后一个断点的 `u` 输入值。索引值从零开始。当输入等于最后一个断点时，模块输出如下所示不同。

| 复选框 | 模块输出 |
| --- | --- |
| 选中（`on`） | - 断点数据集中最后一个元素的索引 - 区间小数为 `0` |
| 清除（`off`） | - 倒数第二个断点的索引 - 区间小数为 `1` |

**提示**

当您为 Prelookup 模块选择 **Use last breakpoint for input at or above upper limit** 时，还必须为其连接的 Interpolation Using Prelookup 模块选择 **Valid index input may reach last index**。此操作允许模块在访问其断点和表数据集的最后一个元素时使用相同的索引约定。

#### 依赖关系

此参数仅在 **Extrapolation method** 为 `Clip` 时可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`UseLastBreakpoint` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

### **Assume input is within range** — 用于检查超出范围输入值的选项 `off`（默认）| `on`

*自 R2025a 起*

指定是否包含检查超出范围输入值的代码。选择此参数意味着您保证模块没有超出范围的输入，从而使模块能够进一步优化代码和仿真。有效输入范围取决于断点数据和 **Extrapolation method** 设置。

当您选择 **Assume input is within range** 时：

- 在仿真期间，模块假定不存在超出范围的输入，并通过返回超出范围输入的错误来强制执行此假设。
- 对于代码生成，模块不会生成超出范围输入处理代码，因为它假定不存在超出范围的输入。这意味着，如果模块尝试为因超出范围输入而返回错误的模型生成代码，当生成的代码被赋予相同的输入时，行为是未定义的，这可能导致严重后果。

  **警告**

  如果模型尝试生成代码，但因模块检测到超出范围输入而生成错误，则将相同的超出范围输入传递给部署代码时，行为是未定义的。这种未定义行为可能导致严重问题。对于安全关键应用，请勿选择 **Assume input is within range**。

如果您为了效率而想选择 **Assume input is within range** 参数，请确保您的模型输入在范围内。例如：

| 参数 | 结果 | 使用时机 |
| --- | --- | --- |
| `on` | 仿真和生成的代码不包含用于检查超出范围断点输入的条件语句。当输入超出范围时，可能导致仿真和生成代码的未定义行为。 | 用于仿真和代码效率 |
| `off` | 仿真和生成的代码包含用于检查超出范围输入的条件语句。 | 用于安全关键应用 |

如果您确信输入在范围内，可以选择 **Assume input is within range** 参数以提高效率。默认情况下，此参数处于清除状态。对于安全关键应用，请勿选择此参数。如果您想选择 **Assume input is within range** 参数，请先检查您的模型输入是否在范围内。例如：

1. 清除 **Assume input is within range** 参数。
2. 将 **Diagnostic for out-of-range input** 参数设置为 `Error`。
3. 在正常模式下仿真模型。
4. 如果存在超出范围错误，模块将返回运行时错误。修复这些错误使其在范围内，然后再次运行仿真。
5. 当仿真不再生成超出范围输入错误时，选择 **Assume input is within range** 参数。

   **注意**

   当您选择 **Assume input is within range** 参数且输入超出范围时，模块在仿真时会返回运行时错误。对于生成的代码，行为是未定义的。

根据您的应用，您可以运行以下 Model Advisor 检查来验证此参数的使用：

- **按产品** > **Embedded Coder** > **识别生成昂贵越界检查代码的查找表模块**
- **按产品** > **Simulink Check** > **建模标准** > **DO-178C/DO-331 检查** > **检查查找表模块的使用**

有关 Model Advisor 的更多信息，请参阅 Run Model Advisor Checks。

此外，如果您拥有 Simulink
Design Verifier™ 许可证，为了确定选择此参数是否安全，请考虑使用 Detect Block Input Range Violations (Simulink Design Verifier) 检查。

#### 编程使用

|  |
| --- |
| **模块参数**：`RemoveProtectionInput` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

### **Diagnostic for out-of-range input** — 输入超出范围时的模块操作 `None`（默认）| `Warning` | `Error`

选项包括：

- `None` — 不产生任何响应。
- `Warning` — 显示警告并继续仿真。
- `Error` — 终止仿真并显示错误。

#### 编程使用

|  |
| --- |
| **模块参数**：`DiagnosticForOutOfRangeInput` |
| **类型**：character vector |
| **值**：`'None' | 'Warning' | 'Error'` |
| **默认值**：`'None'` |

### **Sample time (-1 for inherited)** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关更多信息，请参阅 Specify Sample Time。

#### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **值**：| `"-1"`（默认）| 带引号的标量或向量 |

### 数据类型

### **Breakpoint** — 断点数据类型 `Inherit: Same as input`（默认）| `Inherit: Inherit from 'Breakpoint data'` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

指定断点数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Same as input`
- 内置数据类型的名称，例如 `single`
- 数据类型类的名称，例如枚举数据类型类
- 求值为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant。

**提示**

- 对于以下情况，请指定与输入 `u` 的数据类型不同的断点数据类型：

  - 存储使用比输入信号 `u` 更小类型的断点数据时，降低内存需求
  - 在两个具有不同输入 `u` 数据类型的 Prelookup 模块之间共享预缩放断点数据
  - 在生成的代码中，为具有不同输入 `u` 数据类型的模块共享自定义存储断点数据
- 如果断点数据类型及其对应的输入数据类型中的任一个具有定点数据类型，请为二者指定相同的斜率和偏置。
- 枚举数据：

  - 断点支持无序枚举数据。因此，线性搜索也是无序的，这提供了灵活性，但可能影响性能。搜索从断点中的第一个元素开始。
  - 如果选择了 **Begin index search using previous index result** 参数，则必须使用有序单调递增数据。这种排序可提高性能。
  - 对于枚举数据，**Extrapolation method** 必须为 `Clip`。
  - 由于小数部分为 `1` 或 `0`，请选择 **Output selection** > **Index only**。

    如果您将仅索引输出选择设置与 Interpolation Using Prelookup 模块一起使用，请考虑使用 **Number of sub-table selection dimensions** 参数。

以下是将枚举数据与此模块一起使用的限制：

- 模块不支持枚举数据的超出范围输入。指定枚举数据时，请在断点数据集中包含整个枚举集。例如，使用 `enumeration` 函数。
- 当断点数据源设置为 `Inport port` 时，枚举数据类型的默认值必须为 `0`。例如，对于此枚举类，`GEAR1` 的默认值必须为 `0`。

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

#### 依赖关系

要启用此参数，请将断点数据 **Source** 设置为 `Dialog`。

**注意**

当您将 **Source** 设置为 `Input port` 时，模块将从 `bp` 输入端口继承所有断点属性（数据类型、最小值和最大值）。

#### 编程使用

|  |
| --- |
| **模块参数**：`BreakpointDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Same as input' | 'Inherit: Inherit from 'Breakpoint data'' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64'| 'fixdt(1,16)' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)'|'<data type expression>'` |
| **默认值**：`'Inherit: Same as input'` |

### **Index** — 索引数据类型 `uint32`（默认）| `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `<data type expression>`

指定可为断点数据集中的所有元素编制索引的数据类型。您可以：

- 从列表中选择内置整数数据类型。
- 使用定点表示指定整数数据类型。

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程使用

|  |
| --- |
| **模块参数**：`IndexDataTypeStr` |
| **类型**：character vector |
| **值**：`'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | '<data type expression>'` |
| **默认值**：`'uint32'` |

### **Fraction** — 小数部分数据类型 `Inherit: Inherit via internal rule`（默认）| `double` | `single` | `fixdt(1,16,0)` | `<data type expression>`

指定区间小数部分的数据类型。您可以：

- 从列表中选择内置数据类型。
- 通过内部规则指定数据类型继承。
- 使用 [Slope Bias] 或仅二进制点缩放表示指定定点数据类型。

  - 如果使用 [Slope Bias] 表示，则缩放必须是平凡的——即斜率为 `1`，偏置为 `0`。
  - 如果使用仅二进制点表示，则固定二次幂指数必须小于或等于零。

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

仅当您将 **Main** 选项卡上的 **Output selection** 设置为 `Index and fraction` 时，此参数才会显示。

#### 编程使用

|  |
| --- |
| **模块参数**：`FractionDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule' | 'double' | 'single' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Output** — 输出数据类型 `Inherit: auto`（默认）| `bus: <object name>`

要输出虚拟总线，请使用 `Inherit: auto` 设置。生成的虚拟总线包含两个元素：索引信号和小数部分信号。

要输出并指定非虚拟总线，请使用 `Bus: <object name>` 模板。将 `<object name>` 替换为包含索引信号和小数部分信号的总线对象的名称。

- 总线对象必须包含两个元素。第一个元素对应索引信号，第二个元素对应小数部分信号。
- 索引和小数部分总线元素信号不能是总线信号。
- 如果您将 **Output selection** 设置为 `Index and fraction`，则总线元素的数据类型和复杂度必须满足适用于索引和小数部分信号的相同约束。

要创建包含索引和小数部分总线元素的总线对象，请使用类似以下的 MATLAB® 代码，并自定义总线对象名称以及总线元素的名称和数据类型。

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

或者，您可以使用 Type Editor 创建或修改要与 Prelookup 模块一起使用的总线对象。

如果您将此模块的总线输出信号馈送到 Interpolation Using Prelookup 模块，请在该模块中选择 **Require index and fraction as bus**。

**注意**

使用 Fixed-Point Tool 数据类型覆盖选项，用新的总线对象覆盖总线对象，从而将定点数据类型替换为浮点数据类型。

与 Prelookup 模块一起使用的被覆盖总线对象可能导致错误，因为该模块不接受总线中第一个元素的浮点数据类型。

如果遇到此问题，请使用 **Fix** 按钮重新定义原始总线对象并保护其不被覆盖。例如，假设您将总线对象的第一个元素定义为 `int32`。

```
myBus.Elements(1).DataType
```

```
int32
```

单击 **Fix** 按钮会重新定义第一个总线元素：

```
myBus.Elements(1).DataType = 'fixdt(''int32'',''DataTypeOverride'',''Off'')'
```

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

仅当您将 **Main** 选项卡上的 **Output selection** 设置为 `Index and fraction as bus` 时，此参数才会显示。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputBusDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: auto' | 'Bus: <object name>' | '<data type expression>'` |
| **默认值**：`'Inherit: auto'` |

### **Breakpoint Minimum** — 断点数据可以具有的最小值 `[]`（默认）| 标量

指定断点数据可以具有的最小值。默认值为 `[]`（未指定）。

#### 依赖关系

要启用此参数，请在 **Main** 选项卡上将断点数据 **Source** 设置为 `Dialog`。

#### 编程使用

|  |
| --- |
| **模块参数**：`BreakpointMin` |
| **类型**：character vector |
| **Value:** scalar |
| **默认值**：`'[]'` |

### **Breakpoint Maximum** — 断点数据可以具有的最大值 `[]`（默认）| 标量

指定断点数据可以具有的最大值。默认值为 `[]`（未指定）。

#### 依赖关系

要启用此参数，请在 **Main** 选项卡上将断点数据 **Source** 设置为 `Dialog`。

#### 编程使用

|  |
| --- |
| **模块参数**：`BreakpointMax` |
| **类型**：character vector |
| **Value:** scalar |
| **默认值**：`'[]'` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖 Output data type 的选项 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在模块上指定的 **Output** 数据类型。有关更多信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `LockScale` |
| **值**：| `'off'`（默认）| `'on'` |

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关更多信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB 舍入函数的表达式。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RndMeth` |
| **值：** | `'Floor'`（默认） | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

## 所属库

Simulink / Lookup Tables HDL Coder / Lookup Tables

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

**必需的模块设置**

- **断点数据**：对于 **Source**，选择 `Dialog`。
- **规格**：可以选择 `Explicit values` 或 `Even spacing`。
- **索引搜索方法**：选择 `Evenly spaced points`、`Binary search` 或 `Linear search`。
- **外插方法**：选择 `Clip`。
- **越界输入诊断**：选择 `Error`。
- **对等于或高于上限的输入使用最后一个断点**：选择此参数。
- **断点**：对于 **Data Type**，选择 `Inherit: Same as input`。
- **整数舍入模式**：选择 `Zero`、`Floor` 或 `Simplest`。

**表数据类型和大小**

- 良好的做法是将表结构设计为断点之间的间距为 2 的幂。如果断点间距不满足此条件，HDL Coder 会发出警告。当断点间距为 2 的幂时，可以将预查找步骤中的除法运算替换为右移运算。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

Simulink PLC Coder 对查找表模块的支持有限。该代码生成器不支持：

- 维度数大于 2
- 三次样条插值方法
- 使用先前索引模式开始索引搜索
- 三次样条外插方法

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006b 中引入**

### R2025a：Prelookup 模块 **Remove protection against out-of-range input in generated code** 参数已替换

**Remove protection against out-of-range input in generated code** 参数已替换为 **Assume input is within range**。编程名称 `RemoveProtectionInput` 保持不变。

如果模型仿真因为越界输入被馈送到选择了 **Assume input is within range** 的模块而产生错误，则当生成的代码执行期间出现相同的越界输入时，模型生成的代码具有未定义行为。此未定义行为可能导致严重问题。对于安全关键应用，请勿选择 **Remove protection against out-of-range input in generated code**。

在 R2025a 之前的版本中，**Remove protection against out-of-range input in generated code** 仅移除生成代码中越界值的代码检查。模块无法检测这些问题。作为解决方法，如果您有来自 R2025a 之前版本的模型且无法迁移到更高版本，请将 **Diagnostic for out-of-range input** 参数设置为 `Error`。下次运行模型时，当输入越界时会生成错误。

## 描述

为 Interpolation Using Prelookup 模块计算索引和分数

Prelookup 模块计算索引和区间分数，用于指定其输入值 `u` 与断点数据集的关系。Prelookup 模块与 Interpolation Using Prelookup 模块配合使用效果最佳。将得到的索引和分数值馈送到 Interpolation Using Prelookup 模块以对 *n* 维表进行插值。这两个模块具有分布式算法。当组合在一起时，它们执行与 n-D Lookup Table 模块中集成算法相同的操作。但是，Prelookup 和 Interpolation Using Prelookup 模块比 n-D Lookup Table 模块提供更大的灵活性和更高效的仿真及代码生成。有关更多信息，请参阅 Efficiency of Performance。

### 支持的模块操作

要使用 Prelookup 模块，必须指定一组断点值。您可以选择直接在对话框中指定断点值，或者通过将 **Source** 参数设置为 `Dialog` 或 `Input port` 将值馈送到 `bp` 输入端口。通常，此断点数据集对应于 Interpolation Using Prelookup 模块中表数据的一个维度。Prelookup 模块通过计算以下内容为每个输入值 `u` 生成一对输出：

- 断点集合中小于或等于 `u` 且构成包含 `u` 的区间的元素的索引
- 范围在 0 ≤ f < 1 内的区间分数，表示 `u` 在索引与下一个索引值之间的断点区间上对于范围内输入的归一化位置

例如，如果断点数据集为 `[0 5 10 20 50 100]` 且输入值 `u` 为 55，则索引为 4，分数值为 0.1。索引和区间分数的标签在 Prelookup 模块图标上显示为 **k** 和 **f**。索引值从零开始。

对于越界输入，区间分数可以为负数或大于 `1`。有关更多信息，请参阅 **Extrapolation method** 模块参数。
