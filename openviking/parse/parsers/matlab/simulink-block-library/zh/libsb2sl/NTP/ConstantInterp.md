---
type: simulink-block
title: 'Interpolation Using Prelookup'
family: 'libsb2sl'
product_id: 'libsb2sl'
product_name: 'libsb2sl'
documentation_release: R2025b
official_category: 'NTP'
documentation_page: 'interpolationusingprelookup'
documentation_source_path: '../simulink/slref/interpolationusingprelookup.html'
language: zh-CN
chinese_source: worker-translation
---

# Interpolation Using Prelookup

## 端口

### 输入

### **k1** — 表第一维的索引 `k` 标量 | 向量 | 矩阵

从零开始的索引 `k`，指定包含表第一维输入 `u` 的区间。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **f1** — 表第一维的分数 `f` 标量 | 向量 | 矩阵

分数 `f`，表示输入在表第一维区间 `k` 内的归一化位置。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **kn** — 表第 `n` 维的索引 `k` 标量 | 向量 | 矩阵

从零开始的索引 `k`，指定包含表第 `n` 维输入 `u` 的区间。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **fn** — 表第 `n` 维的分数 `f` 标量 | 向量 | 矩阵

分数 `f`，表示输入在表第 `n` 维区间 `k` 内的归一化位置。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **kf1** — 包含索引 `k` 和分数 `f` 的输入 总线对象

**kf1** 端口的输入包含以总线对象形式指定的索引 `k` 和分数 `f`。

#### 依赖

要启用此端口，请选中 **Require index and fraction as a bus** 复选框。

可用的 `kf` 输入端口数量取决于 **Number of dimensions** 和 **Number of sub-table selection dimensions** 参数的值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`

### **kfn** — 包含索引 `k` 和分数 `f` 的输入 总线对象

**kfn** 端口的输入包含以总线对象形式指定的输入第 n 维的索引 `k` 和分数 `f`。

#### 依赖

要启用此端口，请选中 **Require index and fraction as a bus** 复选框。

可用的 **kf** 输入端口数量取决于 **Number of dimensions** 和 **Number of sub-table selection dimensions** 参数的值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`

### **sm** — 选择并插值表数据的子集 标量 | 向量 | 矩阵

对于列优先算法，模块使用 s*m*、s*m*+1、... s*n* 端口的输入在子表内执行选择和插值。*`m`* 映射到表的第 *m* 维。*n* 等于 **Number of dimensions**。

对于行优先算法，模块使用 s1、s2、...、s*m* 端口的输入在子表内执行选择和插值。*`m`* 映射到表的第 *m* 维。*m* 等于 **Number of sub-table selection dimensions**。

#### 依赖

要启用此端口，**Number of sub-table selection dimensions** 必须为小于或等于 **Number of dimensions** 的正整数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **T** — 表数据 标量 | 向量 | 矩阵 | n 维数组

作为输入提供到端口 **T** 的表数据值。通常，这些表值对应于 Prelookup 模块中指定的断点数据集。Interpolation Using Prelookup 模块根据从 Prelookup 模块馈入的索引（`k`）和区间分数（`f`）值，通过查找或估算表值来生成输出。

#### 依赖

要启用此端口，请将 **Source** 设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — N 维函数的近似值 标量 | 向量 | 矩阵

N 维函数的近似值，通过使用输入索引 `k` 和分数 `f` 的值对表数据进行插值（或外插）计算得出。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### 主要

#### 表数据

### **Number of dimensions** — 表数据的维数 `2`（默认）| 1 到 30 之间的整数

指定表数据必须具有的维数。**Number of dimensions** 定义表的独立变量数量。

| 要指定... | 请执行此操作... |
| --- | --- |
| 1、2、3 或 4 | 从下拉列表中选择值。 |
| 更高的表维数 | 直接在字段中输入正整数。此模块支持的最大表维数为 30。 |

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberOfTableDimensions` |
| **类型**：character vector |
| **值**：`'1' | '2' | '3' |'4' | ... | '30'` |
| **默认值**：`'2'` |

### **Require index and fraction as bus** — 索引和分数输入可以组合在总线中 `off`（默认）| `on`

选中此复选框可将索引和分数输入组合在总线中。

要使 Prelookup 模块能够向 Interpolation Using Prelookup 模块提供输入，请设置：

- **Output selection** 为 `Index and fraction as bus`
- **Output** 为 `Bus: <object name>`，其中 `<object name>` 必须是模型可访问的有效总线对象名称

无论此复选框设置如何，选择端口始终以非总线模式运行。

#### 编程使用

|  |
| --- |
| **模块参数**：`RequireIndexFractionAsBus` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

### **Specification** — 选择如何输入表数据 `Explicit values`（默认）| `Lookup table object`

指定是直接输入表数据还是使用查找表对象。如果将此参数设置为：

- `Explicit values`，则 **Source** 和 **Value** 参数在对话框中可见。
- `Lookup table object`，则 **Name** 参数在对话框中可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`TableSpecification` |
| **类型**：character vector |
| **值**：`'Explicit values' | 'Lookup table object'` |
| **默认值**：`'Explicit values'` |

要将此参数从 `'Explicit values'` 设置为 `'Lookup table object'`，请使用同一个 `set_param` 调用设置 `LookupTableObject` 参数。例如：

```
set_param('myModel/myInterpBlock',...
   'TableSpecification','Lookup table object',...
   'LookupTableObject','myLUTObject')
```

### **Source** — 表数据的来源 `Dialog`（默认）| `Input port`

指定是在对话框中输入表数据还是从输入端口继承数据。如果将 **Source** 设置为：

- `Dialog`，请在 **Value** 下的文本框中输入表数据
- `Input port`，请验证上游信号向表输入端口提供表数据

#### 依赖

要启用此参数，请将 **Specification** 设置为 `Explicit values`。

#### 编程使用

|  |
| --- |
| **模块参数**：`TableSource` |
| **类型**：character vector |
| **值**：`'Dialog' | 'Input port'` |
| **默认值**：`'Dialog'` |

### **Value** — 指定表数据值 `sqrt([1:11]' * [1:11])`（默认）| 表数据的多维数组

将表数据指定为 `N` 维数组，其中 `N` 是 **Number of dimensions** 参数的值。您可以通过在 **Value** 编辑字段中输入空矩阵（`[]`）或未定义的工作区变量来编辑模块图，而无需指定维度正确的矩阵。有关如何在 MATLAB® 中构造多维数组的信息，请参阅 Multidimensional Arrays。

如果将 **Source** 设置为 `Input port`，请验证上游信号向 **T** 输入端口提供表数据。表数据的大小必须与 **Number of table dimensions** 匹配。对于此选项，模块从 **T** 输入端口继承表属性。

要使用 Lookup Table Editor 编辑查找表，请点击 **Edit**（请参阅 Lookup Table Editor）。

#### 依赖

要在对话框中启用此参数并显式指定表值，必须将 **Specification** 设置为 `Explicit values`，并将 **Source** 设置为 `Dialog`。

#### 编程使用

|  |
| --- |
| **模块参数**：`Table` |
| **类型**：character vector |
| **值**：scalar | vector | matrix | N-D array |
| **默认值**：`'sqrt([1:11]' * [1:11])'` |

### **Name** — `Simulink.LookupTable` 对象的名称 `Simulink.LookupTable object`

指定 `Simulink.LookupTable` 对象的名称。查找表对象引用 Simulink® 断点对象。如果 `Simulink.LookupTable` 对象不存在，请点击操作按钮 并选择 **Create**。新查找表对象的相应参数将自动填充模块信息。

#### 依赖

要启用此参数，请将 **Specification** 设置为 `Lookup table object`。

#### 编程使用

|  |
| --- |
| **模块参数**：`LookupTableObject` |
| **类型**：character vector |
| **Value:** `Simulink.LookupTable object` |
| **默认值**：`''` |

#### 算法

### **Interpolation method** — 选择 `Linear point-slope`、`Flat`、`Nearest` 或 `Linear Lagrange` `Linear point-slope`（默认）| `Nearest` | `Flat` | `Linear Lagrange`

指定模块用于对表数据进行插值的方法。您可以选择 `Linear point-slope`、`Flat`、`Nearest` 或 `Linear Lagrange`。有关详细信息，请参阅 Interpolation Methods。

#### 编程使用

|  |
| --- |
| **模块参数**：`InterpMethod` |
| **类型**：character vector |
| **值**：`'Flat' | 'Linear point-slope' | 'Nearest' | 'Linear Lagrange'` |
| **默认值**：`'Linear point-slope'` |

### **Extrapolation method** — 处理超出断点数据集范围的输入的方法 `Linear`（默认）| `Clip`

指定模块用于对所有超出断点数据集范围的输入进行外插的方法。您可以选择 `Clip` 或 `Linear`。有关详细信息，请参阅 Extrapolation Methods。

如果外插方法为 `Linear`，则外插值基于所选的线性插值方法计算。例如，如果插值方法为 Linear Lagrange，则外插方法继承 Linear Lagrange 方程来计算外插值。

要使用 Prelookup 和 Interpolation Using Prelookup 模块复现 n-D Lookup Table 模块的行为，Prelookup 和 Interpolation Using Prelookup 模块的 **Extrapolation method** 必须与仅使用 n-D Lookup Table 模块时相同。例如，要获得与 **Extrapolation method** 设置为 `Linear` 的 n-D Lookup Table 模块相同的行为，请将 Prelookup 和 Interpolation Using Prelookup 模块的 **Extrapolation method** 都设置为 `Linear`。

#### 依赖

要启用 **Extrapolation method** 参数，请将 **Interpolation method** 设置为 `Linear`。

当输入或输出信号指定整数或定点数据类型时，Interpolation Using Prelookup 模块不支持 `Linear` 外插。

#### 编程使用

|  |
| --- |
| **模块参数**：`ExtrapMethod` |
| **类型**：character vector |
| **值**：`'Clip' | 'Linear'` |
| **默认值**：`'Linear'` |

### **Valid index input may reach last index** — 允许输入访问表数据的最后一个元素 `off`（默认）| `on`

指定索引（`k`）和区间分数（`f`）的模块输入如何访问 *n* 维表数据的最后一个元素。索引值从零开始。

如果输入索引等于或大于该维度的表最后一个索引，则此复选框相关。由于舍入，选中和清除此复选框可能会导致仿真和代码生成之间最后一个索引的结果不同。

| 复选框 | 模块行为 |
| --- | --- |
| `on` | 在以下情况下返回其表某一维度中最后一个元素的值： - `k` 索引对应维度中的最后一个表元素 - `f` 为 `0` |
| `off` | 在以下情况下返回其表某一维度中最后一个元素的值： - `k` 索引对应维度中的倒数第二个表元素 - `f` 为 `1` |

#### 依赖

此复选框仅在以下情况下可见：

- **Interpolation method** 为 `Linear point-slope` 或 `Linear Lagrange`
- **Extrapolation method** 为 `Clip`

**提示**

当您为 Interpolation Using Prelookup 模块选中 **Valid index input may reach last index** 时，还必须为所有馈入它的 Prelookup 模块选中 **Use last breakpoint for input at or above upper limit**。此操作允许模块在访问其断点和表数据集的最后一个元素时使用相同的索引约定。

#### 编程使用

|  |
| --- |
| **模块参数**：`ValidIndexMayReachLast` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

### **Assume index is within range** — 用于检查索引值是否越界的选项 `off`（默认）| `on`

*自 R2025a 起*

指定是否包含检查索引值是否越界的代码。
选择此参数意味着您保证模块没有越界索引，
使模块能够进一步优化代码和仿真。有效索引范围
取决于断点数据和 **Extrapolation method**
设置。

当您选择 **Assume index is within range** 时：

- 在仿真期间，模块假定不存在越界索引，
  并通过返回越界索引错误来强制执行此假设。
- 对于代码生成，模块不会生成越界索引处理
  代码，因为它假定不存在越界索引。这意味着如果
  模块尝试为因越界索引而返回错误的模型生成代码，
  当生成的代码被赋予相同的索引时，行为是未定义的，这可能导致严重后果。

  **警告**

  如果模型尝试生成代码，但因模块检测到越界索引而生成错误，
  则将相同的越界索引传递给部署代码时，行为是
  未定义的。此未定义行为可能导致严重问题。对于安全关键
  应用，请勿选择 **Assume index is within
  range**。

如果您希望出于效率考虑选择 **Assume index is within range** 参数，
请确保您的模型索引在范围内。例如：

| 参数 | 结果 | 使用时机 |
| --- | --- | --- |
| `on` | 仿真和生成的代码不包含用于检查越界断点索引的条件语句。当索引越界时，可能导致仿真和生成代码的未定义行为。 | 用于仿真和代码效率 |
| `off` | 仿真和生成的代码包含用于检查越界索引的条件语句。 | 用于安全关键应用 |

如果您确信索引在范围内，可以选择 **Assume
index is within range** 参数以提高效率。默认情况下，此
参数处于清除状态。对于安全关键应用，请勿选择此参数。如果您
希望选择 **Assume index is within range** 参数，
请先检查您的模型索引是否在范围内。例如：

1. 清除 **Assume index is within range** 参数。
2. 将 **Diagnostic for out-of-range index** 参数设置为
   `Error`。
3. 在正常模式下仿真模型。
4. 如果存在越界错误，模块将返回运行时错误。修复这些错误
   使其在范围内，然后再次运行仿真。
5. 当仿真不再生成越界索引错误时，选择
   **Assume index is within range** 参数。

   **注意**

   当您选择 **Assume index is within range**
   参数且索引越界时，模块在仿真时返回运行时错误。
   对于生成的代码，行为是未定义的。

根据您的应用，您可以运行以下 Model Advisor 检查来
验证此参数的使用：

- **按产品** > **Embedded Coder** > **识别生成高成本查找表的模块**
  out-of-range checking code**
- **按产品** > **Simulink Check** > **建模标准** > **DO-178C/DO-331 检查** > **检查查找表模块的使用情况**

有关 Model Advisor 的更多信息，请参阅 Run Model Advisor Checks。

此外，如果您拥有 Simulink
Design Verifier™ 许可证，为了确定选择此参数是否安全，请考虑使用 Detect Block Input Range Violations (Simulink Design Verifier) 检查。

#### 编程使用

|  |
| --- |
| **模块参数**：`RemoveProtectionIndex` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

### **Diagnostic for out-of-range input** — 输入越界时的模块操作 `None`（默认）| `Warning` | `Error`

指定当输入越界时是否产生警告或错误。选项包括：

- `None` — 不产生响应。
- `Warning` — 显示警告并继续仿真。
- `Error` — 终止仿真并显示错误。

#### 依赖关系

要启用此参数，请清除 **Assume input is within
range** 或 **Assume index is within range**
参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`DiagnosticForOutOfRangeInput` |
| **类型**：character vector |
| **值**：`'None' | 'Warning' | 'Error'` |
| **默认值**：`'None'` |

### **Number of sub-table selection dimensions** — 输出计算子表的维度数 `0`（默认）| 正整数，小于或等于表维度数

指定模块用于计算输出的子表维度数。遵循以下规则：

- 要启用子表选择，请输入一个正整数。

  此整数必须小于或等于
  **Number of table dimensions**。
- 要禁用子表选择，请输入 `0` 以
  对整个表进行插值。

对于非零值，当您选择 **Math and Data Types** > **Use algorithms optimized for row-major array
layout** 配置参数时，子表选择行为针对行优先布局进行了优化。

有关更多信息，请参阅 How The Block Interpolates a Subset of Table Data。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumSelectionDims` |
| **类型**：character vector |
| **值**：`'0' | '1' | '2' | '3' | '4' | ... | Number of table dimensions` |
| **默认值**：`'0'` |

### **Sample time (-1 for inherited)** — 采样之间的时间间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此
参数设置为 `-1`。有关更多信息，请参阅 Specify Sample Time。

#### 依赖关系

仅当您将其设置为 `-1` 以外的值时，此参数才可见。
要了解更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **值**：| `"-1"`（默认）| 带引号的标量或向量 |

### 数据类型

### **Table data** — 表值的数据类型 `Inherit: Same as output`（默认）| `Inherit: Inherit from 'Table data'` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定表数据类型。您可以将其设置为：

- 继承数据类型的规则，例如，
  `Inherit: Same as output`
- 内置数据类型的名称，例如，
  `single`
- 数据类型对象的名称，例如，
  `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如，
  `fixdt(1,16,0)`

点击 **Show data type assistant** 按钮
以显示 **Data Type
Assistant**，它可帮助您设置表数据
类型。

**提示**

在以下情况下指定与输出数据类型不同的表数据类型：

- 使用比输出信号更小的类型存储表数据以降低内存需求
- 在两个具有不同输出数据类型的
  Interpolation Using Prelookup 模块之间
  共享预缩放表数据
- 在 Simulink
  Coder™ 生成的代码中为具有不同
  输出数据类型的模块共享自定义存储表数据

#### 编程使用

|  |
| --- |
| **模块参数**：`TableDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit from table data' | 'Inherit: Same as output' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | '<data type expression>'` |
| **默认值**：`'Inherit: Same as output'` |

### **Table minimum** — 表数据的最小值 `[]`（默认）| 标量

将表数据的最小值指定为有限、实数、双精度标量。默认
值为 `[]`（未指定）。

#### 编程使用

|  |
| --- |
| **模块参数**：`TableMin` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'[]'` |

### **Table maximum** — 表数据的最大值 `[]`（默认）| 标量

将表数据的最大值指定为有限、实数、双精度标量。默认
值为 `[]`（未指定）。

#### 编程使用

|  |
| --- |
| **模块参数**：`TableMax` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'[]'` |

### **Intermediate results** — 中间结果的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as output` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定中间结果数据类型。您可以将其设置为：

- 继承数据类型的规则，例如，
  `Inherit: Same as output`
- 内置数据类型的名称，例如，
  `single`
- 数据类型对象的名称，例如，
  `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如，
  `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据
属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant。

**提示**

使用此参数为内部计算指定比表数据或输出数据更高的精度。

#### 编程使用

|  |
| --- |
| **模块参数**：`IntermediateResultsDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule' | 'Inherit: Same as output' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | '<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Output** — 输出数据类型 `Inherit: Inherit from 'Table data'`（默认）| `Inherit: Inherit via back propagation` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定输出数据类型。您可以将其设置为：

- 继承数据类型的规则，例如，
  `Inherit: Inherit via back
  propagation`
- 内置数据类型的名称，例如，
  `single`
- 数据类型对象的名称，例如，
  `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如，
  `fixdt(1,16,0)`

点击 **Show data type assistant** 按钮
以显示 **Data Type
Assistant**，它可帮助您设置输出数据
类型。

有关更多信息，请参阅 Control Data Types of Signals。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via back propagation' | 'Inherit: Inherit from table data' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | 'fixdt(1,16,2^0,0)' | '<data type expression>'` |
| **默认值**：`'Inherit: Inherit from table data'` |

### **Output minimum** — 模块可以输出的最小值 `[]`（默认）| 标量

将模块应输出的最小值指定为有限、实值标量。
默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（请参阅 Specify Signal Ranges）。
- 定点数据类型的自动缩放。
- 从模型生成的代码的优化。此优化可以
  移除算法代码并影响某些
  仿真模式（如 SIL 或外部模式）的结果。有关
  更多信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutMin` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'[]'` |

### **Output maximum** — 模块可以输出的最大值 `[]`（默认）| 标量

将模块应输出的最大值指定为有限、
实值标量。默认值为 `[]`
（未指定）。Simulink 软件使用此值执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（请参阅 Specify Signal Ranges）。
- 定点数据类型的自动缩放。
- 从模型生成的代码的优化。
  此优化可以移除算法代码并影响某些
  仿真模式（如 SIL 或外部模式）的结果。
  有关更多信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'[]'` |

### **Internal rule priority** — 中间计算的内部规则 `Speed`（默认）| `Precision`

指定中间计算的内部规则。选择
`Speed` 以加快计算速度。如果这样做，
可能会发生精度损失，通常最多 2 位。

#### 编程使用

|  |
| --- |
| **模块参数**：`InternalRulePriority` |
| **类型**：character vector |
| **值**：`'Speed' | 'Precision'` |
| **默认值**：`'Speed'` |

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数以防止定点工具覆盖您在此模块上指定的数据类型。有关更多信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Convergent` | `Ceiling` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关更多
信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要
控制模块参数的舍入，请在掩码字段中输入使用
MATLAB 舍入函数的表达式。

#### 编程使用

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型**：character vector |
| **值**：`'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认值**：`'Floor'` |

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

指定溢出是饱和还是回绕。

- `on` — 溢出饱和到数据类型可以表示的
  最小值或最大值。
- `off` — 溢出回绕到数据类型可以表示的
  适当值。

例如，有符号 8 位整数 `int8`
可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致
8 位整数溢出。

- 选择此参数时，模块输出饱和于 127。
  类似地，模块输出饱和于最小输出值
  -128。
- 清除此参数时，软件将导致溢出的
  值解释为 `int8`，这可能会产生意外结果。
  例如，模块结果 130（二进制 1000 0010）表示为
  `int8` 时为 -126。

#### 提示

- 当你的模型可能发生溢出，并且你希望在生成的代码中显式添加饱和保护时，考虑选择此参数。
- 当你希望优化生成代码的效率时，考虑清除此参数。清除此参数还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors。
- 当你选择此参数时，饱和会应用于模块上的每个内部操作，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **值**：| `'off'` (default) | `'on'` |

## 所属库

Simulink / Lookup Tables

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

Simulink
PLC Coder™ 对查找表模块的支持有限。该代码生成器不支持：

- 维度数大于 2
- Cubic spline interpolation method
- Begin index search using a previous index mode
- Cubic spline extrapolation method

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006b 中引入**

### R2025a: Interpolation Using Prelookup 模块 **Remove protection against out-of-range index in generated code** 参数已替换

**Remove protection against out-of-range index in generated code**
参数已替换为 **Assume index is within range**。
编程名称 `RemoveProtectionInput` 保持不变。

如果模型仿真生成错误，因为超出范围的索引被馈送到选择了 **Assume index is within range** 的模块，那么当生成的代码执行期间出现相同的超出范围索引时，模型生成的代码具有未定义行为。这种情况可能导致严重问题。此未定义行为可能导致严重问题。对于安全关键应用，不要选择 **Remove protection against out-of-range index
in generated code**。

在 R2025a 之前的版本中，**Remove protection against out-of-range
index in generated code** 仅移除了生成代码中对超出范围值的代码检查。模块未能检测到这些问题。作为一种变通方法，如果你有一个来自 R2025a 之前版本的模型并且无法迁移到更高版本，请将 **Diagnostic for out-of-range input**
参数设置为 `Error`。下次运行模型时，当索引超出范围时会生成错误。

## 描述

使用预计算的索引和小数部分值来加速 N 维函数的逼近

Interpolation Using Prelookup 模块与 Prelookup 模块一起使用时效率最高。Prelookup 模块计算索引和区间小数部分，用于指定其输入值 `u` 与断点数据集的关系。将得到的索引和小数部分值馈送到 Interpolation Using Prelookup 模块，以对 *n* 维表进行插值。这两个模块具有分布式算法。当组合在一起时，它们执行与 n-D Lookup Table 模块中的集成算法相同的操作。但是，Prelookup 和 Interpolation Using Prelookup 模块提供了更大的灵活性，可以提供更高效的仿真和代码生成。有关详细信息，请参阅 Efficiency of Performance。

### 支持的模块操作

要使用 Interpolation Using Prelookup 模块，你可以直接在对话框中指定一组表数据值，或将值馈送到 **T** 输入端口。通常，这些表值对应于 Prelookup 模块中指定的断点数据集。Interpolation Using Prelookup 模块通过根据从 Prelookup 模块馈送的索引和区间小数部分值查找或估计表值来生成输出。索引和区间小数部分的标签在 Interpolation Using Prelookup 模块图标上显示为 `k` 和 `f`。

| 当索引和区间小数部分的输入... | 则 Interpolation Using Prelookup 模块... |
| --- | --- |
| 映射到断点数据集中的值 | 输出行、列和更高维断点交点处的表值 |
| 不映射到断点数据集中的值，但在范围内 | 使用你选择的 **Interpolation method** 对适当的表值进行插值 |
| 不映射到断点数据集中的值，并且超出范围 | 使用你选择的 **Extrapolation method** 外推输出值 |

### 模块如何对表数据子集进行插值

你可以使用 **Number of sub-table selection dimensions** 参数来指定仅对表数据的子集进行插值。要激活此插值模式，请将此参数设置为正整数。此值定义要选择的维度数，对于默认的列优先算法，从表数据的最高维度开始。因此，该值必须小于或等于 **Number of table dimensions**。

对于行优先算法，插值从表数据的第一个或最低维度开始。

对于非零值，当你选择 **Math and Data Types** > **Use algorithms optimized for row-major array layout** 配置参数时，子表选择行为会针对行优先布局进行优化。

假设你的 Interpolation Using Prelookup 模块中有 3-D 表数据。此行为适用于列优先算法。

| 选择维度数量 | 模块执行的操作 | 模块外观 |
| --- | --- | --- |
| 0 | 对整个表进行插值，不激活子表选择 | 不改变 |
| 1 | 对前两个维度进行插值，并选择第三个维度 | 显示一个标签为 `s3` 的输入端口，你可以使用它来选择和插值 2-D 表 |
| 2 | 对第一个维度进行插值，并选择第二个和第三个维度 | 显示两个标签为 `s2` 和 `s3` 的输入端口，你可以使用它们来选择和插值 1-D 表 |

子表选择使用从零开始的索引。有关对表数据子集进行插值的示例，请参阅 Using the Prelookup and Interpolation Blocks。

对于不带子表选择的 2-D 或 n-D 插值，列优先和行优先算法在输出计算顺序上可能不同，从而导致轻微的数值结果差异。
