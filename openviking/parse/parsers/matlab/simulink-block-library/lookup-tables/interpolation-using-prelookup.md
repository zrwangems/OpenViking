---
type: simulink-block
title: 'Interpolation Using Prelookup'
family: lookup-tables
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Lookup Tables'
documentation_page: 'interpolationusingprelookup'
---

# Interpolation Using Prelookup

Use precalculated index and fraction values to accelerate approximation of N-dimensional function

## 中文

使用预先计算的索引和区间比值快速逼近 N 维函数。

### 所属库

Simulink / Lookup Tables

### 描述

当与 Prelookup 模块结合使用时，Interpolation Using Prelookup 模块的效率最高。Prelookup 模块计算索引和区间比，这些数据说明输入值 `u` 与断点数据集的相对关系。将生成的索引和区间比值馈送给 Interpolation Using Prelookup 模块，以便对 *n* 维表进行插值。这两个模块采用分布式算法。当二者结合使用时，执行的运算与 n-D Lookup Table 模块中的积分算法相同。但是，Prelookup 和 Interpolation Using Prelookup 模块提供了更大的灵活性，可更高效地进行仿真和代码生成。有关详细信息，请参阅执行效率。

#### 支持的模块运算

要使用 Interpolation Using Prelookup 模块，您可以直接在对话框中指定一组表数据值，或将值馈送到 **T** 输入端口中。通常，这些表值对应于在 Prelookup 模块中指定的断点数据集。Interpolation Using Prelookup 模块基于 Prelookup 模块馈送的索引和区间比值查找或估计表值，进而生成输出。索引和区间比的标签在 Interpolation Using Prelookup 模块图标上显示为 `k` 和 `f`。

| 当索引和区间比的输入属于以下情况时... | Interpolation Using Prelookup 模块... |
| --- | --- |
| 映射到断点数据集中的值 | 输出位于行、列和更高维度断点的交点处的表值 |
| 不映射到断点数据集中的值，但在范围内 | 使用您选择的**内插方法**内插适当的表值 |
| 不映射到断点数据集中的值，并且超出范围 | 使用您选择的**外插方法**外插以获得输出值 |

#### 模块如何对表数据的子集进行插值

您可以使用**子表选择维数**参数指定插值只发生在表数据的子集上。要激活此插值模式，请将此参数设置为正整数。该值定义用于进行子表选择的维数，对于默认的列优先算法，该值从表数据的最高维度起计。因此，该值必须小于或等于**表维数**。

对于行优先算法，插值从表数据的第一个维度或最低维度开始。

当您选择**数学和数据类型** > **使用针对行优先数组布局优化的算法**配置参数时，对于非零值，行优先布局中的子表选择行为会有所优化。

假设您的 Interpolation Using Prelookup 模块中有三维表数据。以下行为适用于列优先算法。

| 所选维度的数量 | 模块的动作 | 模块外观 |
| --- | --- | --- |
| 0 | 对整个表进行插值，并且不激活子表选择 | 不更改 |
| 1 | 对前两个维度进行插值，并选择第三个维度 | 显示标签为 `s3` 的输入端口，用于选择二维表，然后对其插值 |
| 2 | 对第一个维度进行插值，并选择第二个维度和第三个维度 | 显示标签为 `s2` 和 `s3` 的两个输入端口，用于选择一维表，然后对其插值 |

子表选择使用从 0 开始的索引。有关对表数据子集进行插值的示例，请参阅 使用 Prelookup 和 Interpolation 模块。

对于没有子表选择的二维或 n 维插值，列优先算法和行优先算法在输出计算的顺序上可能有所不同，导致数值结果略有不同。

### 端口

#### 输入

#### **k1** — 索引 `k`，用于表的第一个维度 标量 | 向量 | 矩阵

从 0 开始的索引 `k`，指定包含输入 `u` 的区间，用于表的第一个维度。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **f1** — 区间比 `f`，用于表的第一个维度 标量 | 向量 | 矩阵

区间比 `f`，表示输入在区间 `k` 内的归一化位置，用于表的第一个维度。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **kn** — 索引 `k`，用于表的第 `n` 个维度 标量 | 向量 | 矩阵

从 0 开始的索引 `k`，为表的第 `n` 个维度指定包含输入 `u` 的区间。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **fn** — 区间比 `f`，用于表的第 `n` 个维度 标量 | 向量 | 矩阵

区间比 `f`，表示输入在区间 `k` 内的归一化位置，用于表的第 `n` 个维度。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **kf1** — 包含索引 `k` 和区间比 `f` 的输入 总线对象

**kf1** 端口的输入，包含索引 `k` 和区间比 `f`，指定为总线对象。

##### 依赖关系

要启用此端口，请选中**需要以总线输出的索引和区间比**复选框。

可用的 `kf` 输入端口的数量取决于**维数**和**子表选择维数**参数的值。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`

#### **kfn** — 包含索引 `k` 和区间比 `f` 的输入 总线对象

**kfn** 端口的输入，包含输入的第 n 维的索引 `k` 和区间比 `f`，指定为总线对象。

##### 依赖关系

要启用此端口，请选中**需要以总线输出的索引和区间比**复选框。

可用的 **kf** 输入端口的数量取决于**维数**和**子表选择维数**参数的值。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`

#### **sm** — 选择表数据的子集并对其进行插值 标量 | 向量 | 矩阵

对于列优先算法，模块使用 s*m*、s*m*+1、...、s*n* 端口的输入来执行子表选择和插值。*`m`* 映射到表的第 *m*个维度。*n* 等于**维数**。

对于行优先算法，模块使用 s1、s2、...、s*m* 端口的输入来执行子表选择和插值。*`m`* 映射到表的第 *m*个维度。*m* 等于**子表选择维数**。

##### 依赖关系

要启用此端口，**子表选择维数**必须为小于或等于**维数**的正整数。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

#### **T** — 表数据 标量 | 向量 | 矩阵 | N 维数组

表数据值作为端口 **T** 的输入提供。通常，这些表值对应于在 Prelookup 模块中指定的断点数据集。Interpolation Using Prelookup 模块基于从 Prelookup 模块馈送的索引 (`k`) 和区间比 (`f`) 值查找或估计表值，进而生成输出。

##### 依赖关系

要启用此端口，请将**源**设置为**输入端口**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
#### 输出

#### **Port\_1** — N 维函数的逼近 标量 | 向量 | 矩阵

N 维函数的逼近，通过使用来自输入索引 `k` 和区间比 `f` 的值内插（或外插）表数据而计算得出。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 参数

#### 常设

##### 表数据

#### **维数** — 表数据的维数 `2` (默认) | 在 1 和 30 之间的整数

指定表数据必须具有的维数。**维数**定义该表的自变量的数目。

| 要指定... | 执行此操作... |
| --- | --- |
| 1、2、3 或 4 | 从下拉列表中选择值。 |
| 更高的表维数 | 直接在字段中输入正整数。  此模块支持的最大表维数为 30。 |

##### 编程用法

|  |
| --- |
| **模块参数**：`NumberOfTableDimensions` |
| **类型：**字符向量 |
| **值：**`'1' | '2' | '3' |'4' | ... | '30'` |
| **默认值：**`'2'` |

#### **需要以总线输出的索引和区间比** — 索引和区间比输入可以合并为一个总线 `off` (默认) | `on`

选中此复选框可在一个总线中合并索引和区间比输入。

要使 Prelookup 模块能够向 Interpolation Using Prelookup 模块提供输入，请进行如下设置：

- 将**输出选择**设置为**索引和区间比作为总线**
- 将**输出**设置为 **Bus: <object name>**，其中 `<object name>` 必须为模型可访问的有效总线对象名称

无论此复选框设置如何，选择端口始终以非总线模式运行。

##### 编程用法

|  |
| --- |
| **模块参数**：`RequireIndexFractionAsBus` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **设定** — 选择如何输入表数据 **显式值** (默认) | **查找表对象**

指定是直接输入表数据还是使用查找表对象。如果将此参数设置为：

- **显式值**，则**源**和**值**参数在对话框中可见。
- **查找表对象**，则**名称**参数在对话框中可见。

##### 编程用法

|  |
| --- |
| **模块参数**：`TableSpecification` |
| **类型：**字符向量 |
| **值：**`'Explicit values' | 'Lookup table object'` |
| **默认值：**`'Explicit values'` |

要将此参数从 `'Explicit values'` 设置为 `'Lookup table object'`，请使用相同的 `set_param` 调用来设置 `LookupTableObject` 参数。例如：

```
set_param('myModel/myInterpBlock',...
   'TableSpecification','Lookup table object',...
   'LookupTableObject','myLUTObject')
```

#### **源** — 表数据源 **对话框** (默认) | **输入端口**

指定是在对话框中输入表数据，还是从输入端口继承数据。如果将**源**设置为：

- **对话框**，则在**值**下的文本框中输入表数据
- **输入端口**，则验证上游信号向表输入端口提供表数据

##### 依赖关系

要启用此参数，请将**设定**设置为**显式值**。

##### 编程用法

|  |
| --- |
| **模块参数**：`TableSource` |
| **类型：**字符向量 |
| **值：**`'Dialog' | 'Input port'` |
| **默认值：**`'Dialog'` |

#### **值** — 指定表数据值 `sqrt([1:11]' * [1:11])` (默认) | 表数据的多维数组

将表数据指定为 `N` 维数组，其中 `N` 是**维数**参数的值。编辑模块图时，您可以在**值**编辑字段中输入空矩阵 (`[]`) 或未定义的工作区变量，而无需指定正确维度的矩阵。有关如何在 MATLAB® 中构造多维数组的信息，请参阅 多维数组。

如果您将**源**设置为**输入端口**，请验证上游信号是否向 **T** 输入端口提供表数据。表数据的大小必须与**表维数**相匹配。对于此选项，模块从 **T** 输入端口继承表属性。

要使用查找表编辑器编辑查找表，请点击**编辑**（请参阅查找表编辑器）。

##### 依赖关系

要启用此参数并在对话框中显式指定表值，您必须将**设定**设置为**显式值**并将**源**设置为**对话框**。

##### 编程用法

|  |
| --- |
| **模块参数**：`Table` |
| **类型：**字符向量 |
| **值：** 标量 | 向量 | 矩阵 | N 维数组 |
| **默认值**：`'sqrt([1:11]' * [1:11])'` |

#### **名称** — `Simulink.LookupTable` 对象的名称 `Simulink.LookupTable object`

指定 `Simulink.LookupTable` 对象的名称。查找表对象引用 Simulink® 断点对象。如果 `Simulink.LookupTable` 对象不存在，请点击操作按钮  并选择**创建**。新查找表对象的对应参数会自动用模块信息填充。

##### 依赖关系

要启用此参数，请将**设定**设置为**查找表对象**。

##### 编程用法

|  |
| --- |
| **模块参数**：`LookupTableObject` |
| **类型：**字符向量 |
| **值：**`Simulink.LookupTable object` |
| **默认值：**`''` |

##### 算法

#### **插值方法** — 选择 `Linear point-slope`、`Flat`、`Nearest` 或 `Linear Lagrange`。 **线性点-斜率** (默认) | **最邻近值** | **均一** | `Linear Lagrange`

指定模块对表数据进行插值的方法。您可以选择 `Linear point-slope`、`Flat`、`Nearest` 或 `Linear Lagrange`。有关详细信息，请参阅内插方法。

##### 编程用法

|  |
| --- |
| **模块参数**：`InterpMethod` |
| **类型：**字符向量 |
| **值：**`'Flat' | 'Linear point-slope' | 'Nearest' | 'Linear Lagrange'` |
| **默认值：**`'Linear point-slope'` |

#### **外插方法** — 处理超出断点数据集范围的输入的方法 **线性** (默认) | **裁剪**

指定模块对断点数据集范围之外的所有输入进行外插的方法。您可以选择**裁剪**或**线性**。有关详细信息，请参阅外插方法。

如果外插方法是**线性**，则基于所选择的线性插值方法计算外插值。例如，如果插值方法是线性拉格朗日，则外插方法继承线性拉格朗日方程以计算外插值。

要使用 Prelookup 和 Interpolation Using Prelookup 模块来复制 n-D Lookup Table 模块行为，用于 Prelookup 和 Interpolation Using Prelookup 模块的**外插方法**必须与仅使用 n-D Lookup Table 模块时相同。例如，要获得与**外插方法**设置为**线性**的 n-D Lookup Table 模块相同的行为，请将 Prelookup 和 Interpolation Using Prelookup 模块的**外插方法**设置为**线性**。

##### 依赖关系

要启用**外插方法**参数，请将**内插方法**设置为**线性**。

当输入或输出信号指定整数或定点数据类型时，Interpolation Using Prelookup 模块不支持**线性**外插。

##### 编程用法

|  |
| --- |
| **模块参数**：`ExtrapMethod` |
| **类型：**字符向量 |
| **值：**`'Clip' | 'Linear'` |
| **默认值：**`'Linear'` |

#### **有效的索引输入可到达最后一个索引** — 允许输入访问表数据最后的元素 `off` (默认) | `on`

指定具有索引 (`k`) 和区间比 (`f`) 的模块输入如何访问 *n* 维表数据最后的元素。索引值从 0 开始。

当输入索引等于或大于该维度的表的最后一个索引时，此复选框才有意义。由于舍入，选中和清除此复选框可能会导致仿真和代码生成之间最后一个索引的结果不同。

| 复选框 | 模块行为 |
| --- | --- |
| `on` | 当出现以下情况时，返回表维度中最后一个元素的值：  - `k` 是对应维度中最后一个表元素的索引 - `f` 是 `0` |
| `off` | 当出现以下情况时，返回表维度中最后一个元素的值：  - `k` 是对应维度中倒数第二个表元素的索引 - `f` 是 `1` |

##### 依赖关系

仅在以下情况下，此复选框才可见：

- **内插方法**是**线性点-斜率**或**线性拉格朗日**
- **外插方法**为**裁剪**

**提示**

当您为 Interpolation Using Prelookup 模块选择**有效的索引输入可到达最后一个索引**时，您还必须为向此模块馈送数据的所有 Prelookup 模块选择**将最后一个断点用于等于或高于上限的输入**。此操作允许模块在访问其断点和表数据集的最后一个元素时使用相同的索引约定。

##### 编程用法

|  |
| --- |
| **模块参数**：`ValidIndexMayReachLast` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **假设索引在范围内** — 检查超范围索引值的选项 `off` (默认) | `on`

*自 R2025a 起*

指定是否包含代码以检查超出范围的索引值。选择此参数意味着您保证该模块没有超出范围的索引，从而使模块能够进一步优化代码和仿真。有效索引范围取决于断点数据和**外插方法**设置。

如果您选择**假设索引在范围内**：

- 在仿真期间，模块假定没有超出范围的索引，并通过对超出范围的索引返回错误来强制实现此假设。
- 对于代码生成，模块不会生成超出范围的索引处理代码，因为它假定不存在超出范围的索引。这意味着，如果模块尝试为因索引超出范围而返回错误的模型生成代码，则当给生成的代码提供相同的索引时，其行为是未定义的，这可能导致严重后果。

  **警告**

  如果模型尝试生成代码，但由于模块检测到索引超出范围而生成错误，则当将相同的超出范围的索引传递给已部署的代码时，行为是未定义的。这种未定义的行为可能导致严重问题。对于安全性至关重要的应用，请不要选择**假设索引在范围内**。

如果您要为了提升效率而选择**假设索引在范围内**参数，请确保模型索引在范围内。例如：

| 参数 | 结果 | 何时使用 |
| --- | --- | --- |
| `on` | 仿真和生成的代码中未包含用来检查超出范围的断点索引的条件语句。  当索引超出范围时，仿真和生成的代码可能会发生未定义的行为。 | 为了提升仿真和代码效率 |
| `off` | 仿真和生成的代码包含用来检查超出范围的索引的条件语句。 | 适用于安全性至关重要的应用领域 |

如果您确信索引在范围内，则可以为了提升效率选择**假设索引在范围内**参数。默认情况下，此参数处于清除状态。对于安全性至关重要的应用，不要选择此参数。如果您要选择**假设索引在范围内**参数，请先检查模型索引是否在范围内。例如：

1. 清除**假设索引在范围内**参数。
2. 将**超范围索引的诊断**参数设置为 `Error`。
3. 在普通模式下进行模型仿真。
4. 如果存在超出范围错误，模块将返回运行时错误。请将它们更正到范围之内，然后再次运行仿真。
5. 当仿真不再生成超范围索引错误时，选择**假设索引在范围内**参数。

   **注意**

   当您选择**假设索引在范围内**参数且索引超出范围时，模块会在仿真时返回运行时错误。生成的代码的行为是未定义的。

根据您的具体应用，您可以运行以下模型顾问检查，以验证此参数的使用：

- **按产品** > **Embedded Coder** > **标识哪些查找表模块会生成检查超范围值的高成本代码**
- **按产品** > **Simulink Check** > **建模标准** > **DO-178C/DO-331 检查** > **检查 Lookup Table 模块的使用**

有关模型顾问的详细信息，请参阅运行模型顾问检查。

此外，要确定选择此参数是否安全，如果您拥有 Simulink Design Verifier™ 许可证，请考虑使用 检测模块输入范围违规 (Simulink Design Verifier) 检查。

##### 编程用法

|  |
| --- |
| **模块参数**：`RemoveProtectionIndex` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **输入超出范围的诊断** — 当输入超出范围时的模块操作 **无** (默认) | **警告** | **错误**

指定当输入超出范围时，是否生成警告或错误消息。选项包括：

- **无** - 不产生任何响应。
- **警告** - 显示警告并继续进行仿真。
- **错误** - 终止仿真并显示错误。

##### 依赖关系

要启用此参数，请清除**假设输入在范围内**或**假设索引在范围内**参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`DiagnosticForOutOfRangeInput` |
| **类型：**字符向量 |
| **值：**`'None' | 'Warning' | 'Error'` |
| **默认值：**`'None'` |

#### **子表选择维数** — 用于计算输出的子表维数 `0` (默认) | 正整数，小于或等于表维数

指定模块用于计算输出的子表的维数。请遵循以下规则：

- 要启用子表选择，请输入正整数。

  该整数必须小于或等于**表维数**。
- 要禁用子表选择，请输入 `0` 以对整个表进行插值。

当您选择**数学和数据类型** > **使用针对行优先数组布局优化的算法**配置参数时，对于非零值，行优先布局中的子表选择行为会有所优化。

有关详细信息，请参阅模块如何对表数据的子集进行插值。

##### 编程用法

|  |
| --- |
| **模块参数**：`NumSelectionDims` |
| **类型：**字符向量 |
| **值：**`'0' | '1' | '2' | '3' | '4' | ... | Number of table dimensions` |
| **默认值：**`'0'` |

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

#### **表数据** — 表值的数据类型 **继承: 与输出相同** (默认) | **继承: 从 '表数据' 继承** | **double** | **single** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16)** | **fixdt(1,16,0)** | **fixdt(1,16,2^0,0)** | **<数据类型表达式>**

指定表数据类型。可以将其设置为：

- 继承数据类型的规则，例如**继承: 与输出相同**
- 内置数据类型的名称，例如 `single`
- 数据类型对象的名称，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

点击**显示数据类型助手**按钮  以显示**数据类型助手**，以便设置表数据类型。

**提示**

对于以下情况，指定与输出数据类型不同的表数据类型：

- 存储表数据（使用的类型小于输出信号）的内存要求较低
- 在具有不同输出数据类型的两个 Interpolation Using Prelookup 模块之间共享预缩放的表数据
- 在为具有不同输出数据类型的模块生成的 Simulink Coder™ 代码中共享自定义存储表数据

##### 编程用法

|  |
| --- |
| **模块参数**：`TableDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Inherit from table data' | 'Inherit: Same as output' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | '<data type expression>'` |
| **默认值：**`'Inherit: Same as output'` |

#### **表数据最小值** — 表数据的最小值 `[]` (默认) | 标量

将表数据的最小值指定为有限双精度实数标量。默认值为 `[]`（未指定）。

##### 编程用法

|  |
| --- |
| **模块参数**：`TableMin` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'[]'` |

#### **表数据最大值** — 表数据的最大值 `[]` (默认) | 标量

将表数据的最大值指定为有限双精度实数标量。默认值为 `[]`（未指定）。

##### 编程用法

|  |
| --- |
| **模块参数**：`TableMax` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'[]'` |

#### **中间结果** — 中间结果的数据类型 `Inherit: Inherit via internal rule` (默认) | `Inherit: Same as output` | `double` | `single` | `int8` | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16)** | **fixdt(1,16,0)** | **fixdt(1,16,2^0,0)** | **<数据类型表达式>**

指定中间结果数据类型。可以将其设置为：

- 继承数据类型的规则，例如**继承: 与输出相同**
- 内置数据类型的名称，例如 `single`
- 数据类型对象的名称，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

**提示**

使用此参数为内部计算指定高于表数据或输出数据的精度。

##### 编程用法

|  |
| --- |
| **模块参数**：`IntermediateResultsDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Inherit via internal rule' | 'Inherit: Same as output' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | '<data type expression>'` |
| **默认值：**`'Inherit: Inherit via internal rule'` |

#### **输出** — 输出数据类型 **继承: 从 '表数据' 继承** (默认) | **继承: 通过反向传播继承** | **double** | **single** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16)** | **fixdt(1,16,0)** | **fixdt(1,16,2^0,0)** | **<数据类型表达式>**

指定输出数据类型。可以将其设置为：

- 继承数据类型的规则，例如**继承: 通过反向传播继承**
- 内置数据类型的名称，例如 `single`
- 数据类型对象的名称，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

点击**显示数据类型助手**按钮  可以显示**数据类型助手**，这有助于您设置输出数据类型。

有关详细信息，请参阅 。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Inherit via back propagation' | 'Inherit: Inherit from table data' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | 'fixdt(1,16,2^0,0)' | '<data type expression>'` |
| **默认值**：`'Inherit: Inherit from table data'` |

#### **输出最小值** — 模块可以输出的最小值 `[]` (默认) | 标量

将模块应输出的最小值指定为有限实数值标量。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutMin` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'[]'` |

#### **输出最大值** — 模块可以输出的最大值 `[]` (默认) | 标量

将模块应输出的最大值指定为有限实数值标量。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'[]'` |

#### **内部规则优先级** — 进行中间计算的内部规则 **速度** (默认) | **精度**

指定进行中间计算的内部规则。选择**速度**可以提高计算速度。但这样可能会损失精度，通常最多 2 位。

##### 编程用法

|  |
| --- |
| **模块参数**：`InternalRulePriority` |
| **类型：**字符向量 |
| **值：**`'Speed' | 'Precision'` |
| **默认值：**`'Speed'` |

#### **锁定数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您对此模块指定的数据类型。有关详细信息，请参阅Lock the Output Data Type Setting (Fixed-Point Designer)。

##### 编程用法

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **整数舍入模式** — 定点运算的舍入模式 **向下** (默认) | **收敛** | **向上** | **最邻近值** | **舍入** | **最简** | **零**

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最邻近的可表示值。要控制模块参数的舍入方法，请在封装字段中使用 MATLAB 舍入函数输入表达式。

##### 编程用法

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型：**字符向量 |
| **值：**`'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认值：**`'Floor'` |

#### **对整数溢出进行饱和处理** — 溢出操作的方法 `off` (默认) | `on`

指定对溢出是进行饱和处理还是绕回处理。

- `on` - 将溢出饱和处理为数据类型能够表示的最小值或最大值。
- `off` - 溢出将绕回到数据类型可以表示的合适值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。

- 选择此参数后，模块输出将在达到 127 时饱和。类似地，模块输出将在达到最小输出值 -128 时饱和。
- 清除此参数后，软件会将导致溢出的值解释为 `int8`，这可能产生意外结果。例如，以 `int8` 表示的模块结果 130（二进制 1000 0010）为 -126。

##### 提示

- 如果您的模型存在可能的溢出，而您希望在生成的代码中进行显式饱和保护，请考虑选中此参数。
- 如果您希望优化生成的代码的效率，请考虑清除此参数。清除此参数还可以帮助您避免过度地指定信号超出范围时模块的处理方式。有关详细信息，请参阅信号范围错误故障排除。
- 如果选中此参数，饱和将应用于模块中的每个内部操作，而不仅仅应用于输出或结果。
- 一般情况下，代码生成进程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SaturateOnIntegerOverflow` |
| **值:** | `'off'` (默认) | `'on'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

Simulink PLC Coder™ 对查询表模块的支持有限。代码生成器不支持：

- 大于 2 的维数
- 三次样条插值方法
- 使用先前的索引模式开始索引搜索
- 三次样条外插方法

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006b 中推出**

#### R2025a: Interpolation Using Prelookup 模块的**删除生成代码中防止超范围索引的代码**参数被取代

**删除生成代码中防止超范围索引的代码**参数已被**假设指标在范围内**取代。编程名称 `RemoveProtectionInput` 保持不变。

如果模型仿真因将超出范围的索引馈送到选中**假设索引在范围内**的模块而生成错误，则当生成的代码在执行期间出现相同的超出范围的索引时，该模型生成的代码具有未定义的行为。此情况可能导致严重问题。这种未定义的行为可能导致严重问题。对于安全性至关重要的应用，请不要选择**删除生成代码中防止超范围索引的代码**。

在 R2025a 之前的版本中，**删除生成代码中防止超范围索引的代码**仅会删除生成代码中对超出范围值的代码检查。模块无法检测到这些问题。作为解决方法，如果您有 R2025a 之前版本的模型且无法迁移到更高版本，请将**输入超出范围的诊断**参数设置为**错误**。下次运行模型时，当索引超出范围时将生成错误。

## Libraries

Simulink / Lookup Tables

## Description

The Interpolation Using Prelookup block is most efficient when used with the Prelookup block. The Prelookup block calculates the index and interval
fraction that specify how its input value `u` relates to the breakpoint
data set. Feed the resulting index and fraction values into an Interpolation Using
Prelookup block to interpolate an *n*-dimensional table. These two
blocks have distributed algorithms. When combined together, they perform the same
operation as the integrated algorithm in the n-D Lookup Table block. However, the
Prelookup and Interpolation Using Prelookup blocks offer greater flexibility that can
provide more efficient simulation and code generation. For more information, see Efficiency of Performance.

### Supported Block Operations

To use the Interpolation Using Prelookup block, you specify a set of table data values
directly on the dialog box or feed values into the **T** input
port. Typically, these table values correspond to the breakpoint data sets specified
in Prelookup blocks. The Interpolation Using Prelookup block generates output by
looking up or estimating table values based on index and interval fraction values
fed from Prelookup blocks. Labels for the index and interval fraction appear as
`k` and `f` on the Interpolation Using
Prelookup block icon.

| When inputs for index and interval fraction... | The Interpolation Using Prelookup block... |
| --- | --- |
| Map to values in breakpoint data sets | Outputs the table value at the intersection of the row, column, and higher dimension breakpoints |
| Do not map to values in breakpoint data sets, but are within range | Interpolates appropriate table values using the **Interpolation method** you select |
| Do not map to values in breakpoint data sets, and are out of range | Extrapolates the output value using the **Extrapolation method** you select |

### How The Block Interpolates a Subset of Table Data

You can use the **Number of sub-table selection dimensions** parameter to
specify that interpolation occur only on a subset of the table data. To activate
this interpolation mode, set this parameter to a positive integer. This value
defines the number of dimensions to select, starting from the highest dimension of
table data for the default column-major algorithm. Therefore, the value must be less
than or equal to the **Number of table dimensions**.

For row-major algorithms, the interpolation starts from the first or lowest
dimension of the table data.

For nonzero values, the subtable selection behavior is optimized for row-major
layout when you select the **Math and Data Types** > **Use algorithms optimized for row-major array layout** configuration parameter.

Suppose that you have 3-D table data in your Interpolation Using Prelookup
block. This behavior applies for the column-major algorithm.

| Number of Selection Dimensions | Action by the Block | Block Appearance |
| --- | --- | --- |
| 0 | Interpolates the entire table and does not activate subtable selection | Does not change |
| 1 | Interpolates the first two dimensions and selects the third dimension | Displays an input port with the label `s3` that you use to select and interpolate 2-D tables |
| 2 | Interpolates the first dimension and selects the second and third dimensions | Displays two input ports with the labels `s2` and `s3` that you use to select and interpolate 1-D tables |

Subtable selection uses zero-based indexing. For an example of interpolating a subset of
table data, see Using the Prelookup and Interpolation Blocks.

For 2-D or n-D interpolation without subtable selection, the column-major and
row-major algorithms may differ in the order of output calculations, causing slight
different numerical results.

## Ports

### Input

### **k1** — Index, `k`, for the first dimension of the table scalar | vector | matrix

Zero-based index, `k`, specifying the interval containing the input
`u` for the first dimension of the table.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **f1** — Fraction, `f`, for the first dimension of the table scalar | vector | matrix

Fraction, `f`, representing the normalized position of the input within
the interval, `k`, for the first dimension of the
table.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **kn** — Index, `k`, for the `n`-th dimension of the table scalar | vector | matrix

Zero-based index, `k`, specifying the interval
containing the input `u` for the
`n`-th dimension of the table.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **fn** — Fraction, `f`, for the `n`-th dimension of the table scalar | vector | matrix

Fraction, `f`, representing the normalized position
of the input within the interval, `k`, for the
`n`-th dimension of the table.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **kf1** — Input containing index `k` and fraction `f` bus object

Inputs to the **kf1** port contain index
`k` and fraction `f` specified as
a bus object.

#### Dependencies

To enable this port, select the **Require index and
fraction as a bus** check box.

The number of available `kf` input ports depends
on the value of the **Number of dimensions** and
**Number of sub-table selection dimensions**
parameters.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`

### **kfn** — Input containing index `k` and fraction `f` bus object

Inputs to the **kfn** port contain index
`k` and fraction `f` for the n-th
dimension of the input, specified as a bus object.

#### Dependencies

To enable this port, select the **Require index and
fraction as a bus** check box.

The number of available **kf** input ports
depends on the value of the **Number of
dimensions** and **Number of sub-table
selection dimensions** parameters.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`

### **sm** — Select and interpolate a subset of the table data scalar | vector | matrix

For column-major algorithm, the block uses inputs to the s*m*,
s*m*+1, ... s*n* port to perform
selection and interpolation within the subtables.
*`m`* maps to the
*m*th dimension of the
table. *n* equals the **Number of
dimensions**.

For row-major algorithm, the block uses inputs to the s1, s2,...
,s*m* port to perform selection and interpolation
within the subtables. *`m`* maps to the
*m*th dimension of the
table. *m* equals the **Number of sub-table
selection dimensions**.

#### Dependencies

To enable this port, the **Number of sub-table selection
dimensions** must be a positive integer less than or
equal to the **Number of dimensions**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **T** — Table data scalar | vector | matrix | n-d array

Table data values provided as input to port **T**.
Typically, these table values correspond to the breakpoint data sets
specified in Prelookup blocks. The Interpolation Using Prelookup block
generates output by looking up or estimating table values based on index
(`k`) and interval fraction (`f`)
values fed from Prelookup blocks.

#### Dependencies

To enable this port, set **Source** to
`Input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Approximation of N-dimensional function scalar | vector | matrix

Approximation of N-dimensional function, computed by interpolating (or
extrapolating) table data using values from the input index,
`k`, and fraction, `f`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### Main

#### Table data

### **Number of dimensions** — Number of table data dimensions `2` (default) | integer between 1 and 30

Specify the number of dimensions that the table data must have. The
**Number of dimensions** defines the number of
independent variables for the table.

| To specify... | Do this... |
| --- | --- |
| 1, 2, 3, or 4 | Select the value from the drop-down list. |
| A higher number of table dimensions | Enter a positive integer directly in the field.  The maximum number of table dimensions that this block supports is 30. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumberOfTableDimensions` |
| **Type:** character vector |
| **Values:** `'1' | '2' | '3' |'4' | ... | '30'` |
| **Default:** `'2'` |

### **Require index and fraction as bus** — Index and fraction inputs can be combined in a bus `off` (default) | `on`

Select this check box to combine index and fraction inputs in a bus.

To enable the Prelookup block to supply input to the
Interpolation Using Prelookup block, set:

- **Output selection** to `Index
  and fraction as bus`
- **Output** to `Bus: <object
  name>`, where `<object
  name>` must be a valid bus object name
  accessible to the model

Regardless of this check box setting, the selection port always
operates in nonbus mode.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RequireIndexFractionAsBus` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Specification** — Choose how to enter table data `Explicit values` (default) | `Lookup table object`

Specify whether to enter table data directly or use a lookup table
object. If you set this parameter to:

- `Explicit values`, the
  **Source** and **Value**
  parameters are visible on the dialog box.
- `Lookup table object`, the
  **Name** parameter is visible on the dialog
  box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableSpecification` |
| **Type:** character vector |
| **Values:** `'Explicit values' | 'Lookup table object'` |
| **Default:** `'Explicit values'` |

To set this parameter from `'Explicit values'` to `'Lookup
table object'`, use the same
`set_param` call to set the
`LookupTableObject` parameter. For
example:

```
set_param('myModel/myInterpBlock',...
   'TableSpecification','Lookup table object',...
   'LookupTableObject','myLUTObject')
```

### **Source** — Source of table data `Dialog` (default) | `Input port`

Specify whether to enter table data in the dialog box or to inherit
the data from an input port. If you set **Source** to:

- `Dialog`, enter table data in the text box under
  **Value**
- `Input port`, verify that an upstream signal supplies table
  data to the table input port

#### Dependencies

To enable this parameter, set **Specification** to
`Explicit values`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableSource` |
| **Type:** character vector |
| **Values:** `'Dialog' | 'Input port'` |
| **Default:** `'Dialog'` |

### **Value** — Specify table data values `sqrt([1:11]' * [1:11])` (default) | multidimensional array of table data

Specify table data as an `N`-D array, where `N` is the
value of the **Number of dimensions** parameter. You
can edit the block diagram without specifying a correctly dimensioned
matrix by entering an empty matrix (`[]`) or an
undefined workspace variable in the **Value** edit
field. For information about how to construct multidimensional arrays in
MATLAB®, see Multidimensional Arrays.

If you set **Source** to `Input port`, verify
that an upstream signal supplies table data to the
**T** input port. The size of table data must match
the **Number of table dimensions**. For this option,
the block inherits table attributes from the **T**
input port.

To edit lookup tables using the Lookup Table Editor, click **Edit**
(see Lookup Table Editor).

#### Dependencies

To enable this parameter and explicitly specify table values on
the dialog box, you must set **Specification** to
`Explicit values` and
**Source** to
`Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Table` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix | N-D array |
| **Default:** `'sqrt([1:11]' * [1:11])'` |

### **Name** — Name of a `Simulink.LookupTable` object `Simulink.LookupTable object`

Specify the name of a `Simulink.LookupTable` object. A
lookup table object references Simulink® breakpoint objects. If a `Simulink.LookupTable` object does not exist, click the
action button  and select
**Create**. The corresponding parameters of the
new lookup table object are automatically populated with the block
information.

#### Dependencies

To enable this parameter, set **Specification**
to `Lookup table object`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LookupTableObject` |
| **Type:** character vector |
| **Value:** `Simulink.LookupTable object` |
| **Default:** `''` |

#### Algorithm

### **Interpolation method** — Select `Linear point-slope`, `Flat`, `Nearest`, or `Linear Lagrange` `Linear point-slope` (default) | `Nearest` | `Flat` | `Linear Lagrange`

Specify the method the block uses to interpolate table data. You can
select `Linear point-slope`, `Flat`,
`Nearest`, or `Linear Lagrange`.
See Interpolation Methods for
more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InterpMethod` |
| **Type:** character vector |
| **Values:** `'Flat' | 'Linear point-slope' | 'Nearest' | 'Linear Lagrange'` |
| **Default:** `'Linear point-slope'` |

### **Extrapolation method** — Method of handling input that falls outside the range of the breakpoint data set `Linear` (default) | `Clip`

Specify the method the block uses to extrapolate values for all inputs
that fall outside the range of the breakpoint data set. You can select
`Clip` or
`Linear`. See Extrapolation Methods for
more information.

If the extrapolation method is `Linear`, the
extrapolation value is calculated based on the selected linear
interpolation method. For example, if the interpolation method is Linear
Lagrange, the extrapolation method inherits the Linear Lagrange equation
to compute the extrapolated value.

To use Prelookup and Interpolation Using Prelookup blocks to replicate n-D Lookup Table block behavior, the **Extrapolation method** for both Prelookup and Interpolation Using Prelookup blocks must be the same as if you use only the n-D Lookup Table block. For example, to get the same behavior as the n-D Lookup Table block with **Extrapolation method** set to `Linear`, set **Extrapolation method** to `Linear` for both Prelookup and Interpolation Using Prelookup blocks.

#### Dependencies

To enable the **Extrapolation method** parameter,
set the **Interpolation method** to
`Linear`.

The Interpolation Using Prelookup block does not support
`Linear` extrapolation when the input
or output signals specify integer or fixed-point data types.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ExtrapMethod` |
| **Type:** character vector |
| **Values:** `'Clip' | 'Linear'` |
| **Default:** `'Linear'` |

### **Valid index input may reach last index** — Allow inputs to access the last elements of table data `off` (default) | `on`

Specify how block inputs for index (`k`) and interval fraction
(`f`) access the last elements of
*n*-dimensional table data. Index values are zero
based.

This check box is relevant if the input index is equal to or larger
than the table's last index for that dimension. Due to rounding,
selecting and clearing this check box may result in differing results
for the last index between simulation and code generation.

| Check Box | Block Behavior |
| --- | --- |
| `on` | Returns the value of the last element in a dimension of its table when:  - `k` indexes the last table   element in the corresponding dimension - `f` is   `0` |
| `off` | Returns the value of the last element in a dimension of its table when:  - `k` indexes the   next-to-last table element in the corresponding   dimension - `f` is   `1` |

#### Dependencies

This check box is visible only when:

- **Interpolation method** is
  `Linear point-slope` or
  `Linear Lagrange`
- **Extrapolation method** is
  `Clip`

**Tip**

When you select **Valid index input may reach last
index** for an Interpolation Using Prelookup block,
you must also select **Use last breakpoint for input at
or above upper limit** for all Prelookup blocks
that feed it. This action allows the blocks to use the same
indexing convention when accessing the last elements of their
breakpoint and table data sets.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ValidIndexMayReachLast` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Assume index is within range** — Option to check for out-of-range index values `off` (default) | `on`

*Since R2025a*

Specify whether or not to include code that checks for out-of-range index values.
Selecting this parameter means you guarantee that the block has no out-of-range indices,
enabling the block to further optimize the code and simulation. The valid index range
depends on the breakpoint data and the **Extrapolation method**
setting.

When you select **Assume index is within range**:

- During simulation, the block assumes that there are no out-of-range indices
  and enforces this assumption by returning an error for out-of-range
  indices.
- For code generation, the block does not generate out-of-range index handling
  code because it assumes there is no out-of-range index. This means that if the
  block tries to generate code for a model that returns an error because of
  out-of-range indices, when the generated code is given the same index, the
  behavior is undefined, which can lead to severe consequence.

  **Warning**

  If the model tries to generate code and instead generates an error
  because the block detects out-of-range indices, the behavior is
  undefined if the same out-of-range index is passed to deployed code.
  This undefined behavior might cause severe issues. For safety critical
  applications, do not select **Assume index is within
  range**.

If you want to select the **Assume index is within range** parameter
for efficiency, ensure that your model indices are in range. For example:

| Parameter | Result | When to Use |
| --- | --- | --- |
| `on` | Simulation and generated code does not include conditional statements to check for out-of-range breakpoint indices.  When the index is out-of-range, it may cause undefined behavior for simulation and generated code. | For simulation and code efficiency |
| `off` | Simulation and generated code includes conditional statements to check for out-of-range indices. | For safety-critical applications |

If you are confident your indices is within range, you can select the **Assume
index is within range** parameter for efficiency. By default, this
parameter is cleared. For safety-critical applications, do not select this parameter. If
you want to select the **Assume index is within range** parameter,
first check that your model indices are in range. For example:

1. Clear the **Assume index is within range** parameter.
2. Set the **Diagnostic for out-of-range index** parameter to
   `Error`.
3. Simulate the model in normal mode.
4. If there are out-of-range errors, the block returns runtime errors. Fix them
   to be in range and run the simulation again.
5. When the simulation no longer generates out-of-range index errors, select the
   **Assume index is within range** parameter.

   **Note**

   When you select the **Assume index is within range**
   parameter and the index is out of range, the block returns a runtime error
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
| **Block Parameter:** `RemoveProtectionIndex` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Diagnostic for out-of-range input** — Block action when input is out of range `None` (default) | `Warning` | `Error`

Specify whether to produce a warning or error when the input is out of range. Options include:

- `None` — Produce no response.
- `Warning` — Display a warning and continue the simulation.
- `Error` — Terminate the simulation and display an error.

#### Dependencies

To enable this parameter, clear the **Assume input is within
range** or **Assume index is within range**
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DiagnosticForOutOfRangeInput` |
| **Type:** character vector |
| **Values:** `'None' | 'Warning' | 'Error'` |
| **Default:** `'None'` |

### **Number of sub-table selection dimensions** — Number of dimensions of the output computation subtable `0` (default) | positive integer, less than or equal to the number of table dimensions

Specify the number of dimensions of the subtable that the block uses
to compute the output. Follow these rules:

- To enable subtable selection, enter a positive integer.

  This integer must be less than or equal to the
  **Number of table dimensions**.
- To disable subtable selection, enter `0` to
  interpolate the entire table.

For nonzero values, the subtable selection behavior is optimized for
row-major layout when you select the **Math and Data Types** > **Use algorithms optimized for row-major array
layout** configuration parameter.

For more information, see How The Block Interpolates a Subset of Table Data.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumSelectionDims` |
| **Type:** character vector |
| **Values:** `'0' | '1' | '2' | '3' | '4' | ... | Number of table dimensions` |
| **Default:** `'0'` |

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

### **Table data** — Data type of table values `Inherit: Same as output` (default) | `Inherit: Inherit from 'Table data'` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the table data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Same as output`
- The name of a built-in data type, for example,
  `single`
- The name of a data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the table data
type.

**Tip**

Specify a table data type different from the output data type for
these cases:

- Lower memory requirement for storing table data that uses
  a smaller type than the output signal
- Sharing of prescaled table data between two
  Interpolation Using Prelookup blocks with
  different output data types
- Sharing of custom storage table data in Simulink
  Coder™ generated code for blocks with different
  output data types

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit from table data' | 'Inherit: Same as output' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Same as output'` |

### **Table minimum** — Minimum value of table data `[]` (default) | scalar

Specify the minimum value for table data as a finite, real, double, scalar. The default
value is `[]` (unspecified).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableMin` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Table maximum** — Maximum value of table data `[]` (default) | scalar

Specify the maximum value for table data as a finite, real, double, scalar. The default
value is `[]` (unspecified).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableMax` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Intermediate results** — Data type of intermediate results `Inherit: Inherit via internal rule` (default) | `Inherit: Same as output` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the intermediate results data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Same as output`
- The name of a built-in data type, for example,
  `single`
- The name of a data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

**Tip**

Use this parameter to specify higher precision for internal
computations than for table data or output data.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IntermediateResultsDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'Inherit: Same as output' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Output** — Output data type `Inherit: Inherit from 'Table data'` (default) | `Inherit: Inherit via back propagation` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the output data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via back
  propagation`
- The name of a built-in data type, for example,
  `single`
- The name of a data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the output data
type.

See Control Data Types of Signals for more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via back propagation' | 'Inherit: Inherit from table data' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | 'fixdt(1,16,2^0,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Inherit from table data'` |

### **Output minimum** — Minimum value the block can output `[]` (default) | scalar

Specify the minimum value that the block should output as a finite, real-valued scalar.
The default value is `[]` (unspecified). Simulink software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters).
- Simulation range checking (see Specify Signal Ranges).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. For more
  information, see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutMin` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Output maximum** — Maximum value the block can output `[]` (default) | scalar

Specify the maximum value that the block should output as a finite,
real-valued scalar. The default value is `[]`
(unspecified). Simulink software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters).
- Simulation range checking (see Specify Signal Ranges).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model.
  This optimization can remove algorithmic code and affect the
  results of some simulation modes such as SIL or external mode.
  For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutMax` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Internal rule priority** — Internal rule for intermediate calculations `Speed` (default) | `Precision`

Specify the internal rule for intermediate calculations. Select
`Speed` for faster calculations. If you do,
a loss of accuracy might occur, usually up to 2 bits.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InternalRulePriority` |
| **Type:** character vector |
| **Values:** `'Speed' | 'Precision'` |
| **Default:** `'Speed'` |

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types you specify on this block. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LockScale` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Convergent` | `Ceiling` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations. For more
information, see Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To
control the rounding of a block parameter, enter an expression using a
MATLAB rounding function in the mask field.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **Default:** `'Floor'` |

### **Saturate on integer overflow** — Method of overflow action `off` (default) | `on`

Specify whether overflows saturate or wrap.

- `on` — Overflows saturate to either the minimum or maximum
  value that the data type can represent.
- `off` — Overflows wrap to the appropriate value that the data
  type can represent.

For example, the maximum value that the signed 8-bit integer `int8`
can represent is 127. Any block operation result greater than this maximum value causes
overflow of the 8-bit integer.

- With this parameter selected, the block output saturates at 127.
  Similarly, the block output saturates at a minimum output value of
  -128.
- With this parameter cleared, the software interprets the overflow-causing
  value as `int8`, which can produce an unintended result.
  For example, a block result of 130 (binary 1000 0010) expressed as
  `int8` is -126.

#### Tips

- Consider selecting this parameter when your model has a possible overflow
  and you want explicit saturation protection in the generated code.
- Consider clearing this parameter when you want to optimize efficiency of
  your generated code. Clearing this parameter also helps you to avoid
  overspecifying how a block handles out-of-range signals. For more
  information, see Troubleshoot Signal Range Errors.
- When you select this parameter, saturation applies to every internal
  operation on the block, not just the output or result.
- In general, the code generation process can detect when overflow is not
  possible. In this case, the code generator does not produce saturation
  code.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **Values:** | `'off'` (default) | `'on'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

Simulink
PLC Coder™ has limited support for lookup table blocks. The coder does not
support:

- Number of dimensions greater than 2
- Cubic spline interpolation method
- Begin index search using a previous index mode
- Cubic spline extrapolation method

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2006b**

### R2025a: Interpolation Using Prelookup block **Remove protection against out-of-range index in generated code** parameter replaced

The **Remove protection against out-of-range index in generated code**
parameter has been replaced by **Assume index is within range**.
The programmatic name, `RemoveProtectionInput`, remains the
same.

If the model simulation generates errors because the out-of-range index is fed to
a block with **Assume index is within range** selected, the code
generated by the model has undefined behavior when the same out-of-range index
occurs during execution of the generated code. This situation might cause severe
issues. This undefined behavior might cause severe issues. For safety critical
applications, do not select **Remove protection against out-of-range index
in generated code**.

In releases prior to R2025a, the **Remove protection against out-of-range
index in generated code** only removed the code checks for
out-of-range values for generated code. The block failed to detect these issues. As
a workaround. if you have a model from a release prior to R2025a and cannot migrate
to a later release, set the **Diagnostic for out-of-range input**
parameter to `Error`. The next time you run the model, an
error is generated when the index is out-of-range.
