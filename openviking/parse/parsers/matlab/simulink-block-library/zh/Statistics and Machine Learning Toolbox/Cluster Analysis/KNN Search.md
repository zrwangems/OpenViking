---
type: simulink-block
title: 'KNN Search'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Cluster Analysis'
documentation_page: 'knnsearchblock'
documentation_source_path: 'knnsearchblock.html'
language: zh-CN
chinese_source: worker-translation
---

# KNN Search

## 端口
```yaml
ports:
- name: x
  summary: 查询点行向量
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Idx
  summary: 最近邻的索引 数值行向量 | 1×1 元胞数组
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: D
  summary: 最近邻的距离 数值行向量 | 1×1 元胞数组
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输入

### **x** — 查询点行向量

查询点，指定为行向量。**x** 的列数必须与 **Select nearest neighbor searcher** 指定的 `searcher` 对象中预测变量的数量相同。**x** 的列顺序必须与 `searcher` 对象中的列顺序一致。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Idx** — 最近邻的索引 数值行向量 | 1×1 元胞数组

数据中最近邻的索引，以数值行向量或 1×1 元胞数组形式返回。

- 如果未在“模块参数”对话框的 **Main** 选项卡中选中 **Include ties**，则模块返回一个 1×*k* 数值行向量，其中 *k* 是搜索的最近邻数量。行向量的每一列包含数据中一个最近邻点的索引，按到查询点 **x** 的距离递增排序。
- 如果在“模块参数”对话框的 **Main** 选项卡中选中 **Include ties**，则模块返回一个 1×1 元胞数组，作为可变大小信号，其中包含数据中距离查询点 **x** 最近的至少 *k* 个观测值的索引组成的数值行向量。向量的各列按到查询点的距离递增排序。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **D** — 最近邻的距离 数值行向量 | 1×1 元胞数组

最近邻到查询点的距离，以数值行向量或 1×1 元胞数组形式返回。

- 如果未在“模块参数”对话框的 **Main** 选项卡中选中 **Include ties**，则模块返回一个 1×*k* 数值行向量，其中 *k* 是搜索的最近邻数量。行向量的每一列包含数据中一个最近邻点到查询点 **x** 的距离，依据距离度量计算。行向量的各列按到查询点的距离递增排序。
- 如果在“模块参数”对话框的 **Main** 选项卡中选中 **Include ties**，则模块返回一个 1×1 元胞数组，作为可变大小信号，其中包含数据中距离查询点 **x** 最近的至少 *k* 个观测值的距离组成的数值行向量。向量的各列按到查询点的距离递增排序。

#### 依赖

要启用此端口，请在 KNN Search 模块中选中 **Add output port for nearest neighbor distances**。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## 参数
```yaml
parameters:
- name: Select nearest neighbor searcher
  summary: 最近邻搜索方法 searcher（默认） | ExhaustiveSearcher 对象 | KDTreeSearcher 对象
  group: 主要参数
  block_parameter: NeighborhoodSearcher
  type: 工作区变量
  values: ExhaustiveSearcher 对象 | KDTreeSearcher 对象
  default: '"searcher"'
- name: Add output port for nearest neighbor distances
  summary: 添加用于最近邻距离的第二个输出端口 off（默认） | on
  group: 主要参数
  block_parameter: ShowOutputDistances
  type: 字符向量
  values: '"off" | "on"'
  default: '"off"'
- name: Number of nearest neighbors
  summary: 最近邻数量 1（默认）| 正整数
  group: 主要参数
  block_parameter: NumNeighbors
  type: 正整数
  values: single | double
- name: Include ties
  summary: 包含所有最近邻的标志 off（默认）| on
  group: 主要参数
  block_parameter: IncludeTies
  type: 字符向量
  values: '"off" | "on"'
- name: Distance metric
  summary: 距离度量 euclidean（默认）| chebychev | cityblock | minkowski | correlation | cosine | hamming | jaccard | mahalanobis
    | seuclidean | spearman
  group: 主要参数
  block_parameter: DistanceMetric
  type: 字符向量
  values: '"euclidean" | "chebychev" | "cityblock" | "minkowski" | "correlation" | "cosine" | "hamming" | "jaccard" | "mahalanobis"
    | "seuclidean" | "spearman"'
- name: Covariance matrix
  summary: 马哈拉诺比斯距离度量的协方差矩阵 Computed using data in searcher（默认）| Customized
  group: 主要参数
  block_parameter: CovarianceMatrix
  type: positive definite matrix
  values: '"Computed using data in searcher" | "Customized"'
  default: '"Computed using data in searcher"'
- name: Scale
  summary: 标准化欧几里得距离度量的尺度参数值 Standard deviation of data in searcher（默认）| Customized
  group: 主要参数
  block_parameter: Scale
  type: nonnegative numeric row vector
  values: '"Standard deviation of data in searcher" | "Customized"'
  default: '"Standard deviation of data in searcher"'
- name: P
  summary: 闵可夫斯基距离度量的指数 2（默认）| 正整数
  group: 主要参数
  block_parameter: MinkExp
  type: positive integer
  values: positive integer
  default: '2'
- name: Integer rounding mode
  summary: 定点运算的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型
  block_parameter: RndMeth
  type: character vector
  values: '"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"'
  default: '"Floor"'
- name: Saturate on integer overflow
  summary: 溢出操作的方法 off（默认）| on
  group: 数据类型
  block_parameter: SaturateOnIntegerOverflow
  type: character vector
  values: '"off" | "on"'
  default: '"off"'
- name: Lock output data type setting against changes by the fixed-point tools
  summary: 防止定点工具覆盖数据类型 off（默认）| on
  group: 数据类型
  block_parameter: LockScale
  type: character vector
  values: '"off" | "on"'
  default: '"off"'
- name: Index data type
  summary: '索引输出的数据类型 Inherit: auto（默认）| double | single | half | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64 |
    uint64 | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: 数据类型
  block_parameter: IndicesDataTypeStr
  type: character vector
  values: '"Inherit: auto" | "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16" | "int32" | "uint32" | "int64"
    | "uint64" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"'
  default: '"Inherit: auto"'
- name: 索引数据类型最小值
  summary: 索引输出的最小值 []（默认）| 标量
  group: 数据类型
  block_parameter: IndicesOutMin
  type: 标量
  values: '"[]" | 标量'
  default: '"[]"'
- name: 索引数据类型最大值
  summary: 索引输出的最大值 []（默认）| 标量
  group: 数据类型
  block_parameter: IndicesOutMax
  type: 标量
  values: '"[]" | 标量'
  default: '"[]"'
- name: 距离数据类型
  summary: '距离输出的数据类型 Inherit: auto（默认）| double | single | half | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64 |
    uint64 | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: 数据类型
  block_parameter: DistanceDataTypeStr
  type: 字符向量
  values: '"Inherit: auto" | "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16" | "int32" | "uint32" | "int64"
    | "uint64" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"'
  default: '"Inherit: auto"'
- name: Distance data type Minimum
  summary: 距离输出的最小值 []（默认）| 标量
  group: 数据类型
  block_parameter: DistanceOutMin
  type: scalar
  values: '"[]" | scalar'
  default: '"[]"'
- name: Distance data type Maximum
  summary: 距离输出的最大值 []（默认）| 标量
  group: 数据类型
  block_parameter: DistanceOutMax
  type: scalar
  values: '"[]" | scalar'
  default: '"[]"'
```

### 主要参数

### **Select nearest neighbor searcher** — 最近邻搜索方法 `searcher`（默认） | `ExhaustiveSearcher` 对象 | `KDTreeSearcher` 对象

指定包含 `ExhaustiveSearcher` 或 `KDTreeSearcher` 对象的工作区变量名称。

**注意**

该软件对“模块参数”对话框中可指定的所有参数使用默认设置。对话框中的参数将覆盖 searcher 对象中的相应参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `NeighborhoodSearcher` |
| **类型：** 工作区变量 |
| **值：** `ExhaustiveSearcher` 对象 | `KDTreeSearcher` 对象 |
| **默认值：** `"searcher"` |

### **Add output port for nearest neighbor distances** — 添加用于最近邻距离的第二个输出端口 `off`（默认） | `on`

选中此复选框可在 KNN Search 模块中包含第二个输出端口 **D**。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowOutputDistances` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **Number of nearest neighbors** — 最近邻数量 `1`（默认）| 正整数

指定在数据中为查询点查找的最近邻数量。

#### 编程用法

|  |
| --- |
| **模块参数：** `NumNeighbors` |
| **类型：** 正整数 |
| **值：** `single` | `double` |
| **默认：** `1` |

### **Include ties** — 包含所有最近邻的标志 `off`（默认）| `on`

如果未在“模块参数”对话框的**主**选项卡中选择 **Include ties**，则模块在距查询点距离相同的观测中选择索引最小的观测。

如果选择 **Include ties**：

- 模块输出包含所有距离等于输出参数中第 *k* 个最小距离的最近邻。如果超过五个最近邻与第 *k* 个最小距离的距离相等，则模块输出仅包含索引值最小的前五个最近邻。
- **Idx** 和 **D** 模块输出为 1×1 元胞数组，其中每个元胞分别包含至少 *k* 个索引和距离的向量。向量中的列按到查询点的距离递增排序。

#### 编程用法

|  |
| --- |
| **模块参数：** `IncludeTies` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认：** `"off"` |

### **Distance metric** — 距离度量 `euclidean`（默认）| `chebychev` | `cityblock` | `minkowski` | `correlation` | `cosine` | `hamming` | `jaccard` | `mahalanobis` | `seuclidean` | `spearman`

指定用于在数据中查找查询点最近邻的距离度量。

对于 `ExhaustiveSearcher` 和 `KDTreeSearcher` 对象，模块支持以下距离度量。

| 值 | 描述 |
| --- | --- |
| `"chebychev"` | Chebychev 距离（最大坐标差） |
| `"cityblock"` | City block 距离 |
| `"euclidean"` | 欧几里得距离 |
| `"minkowski"` | Minkowski 距离。默认指数为 2。您可以在“模块参数”对话框中指定不同的指数。 |

对于 `ExhaustiveSearcher` 对象，模块还支持以下距离度量。

| 值 | 描述 |
| --- | --- |
| `"correlation"` | 1 减去观测之间的样本线性相关性（视为值序列） |
| `"cosine"` | 1 减去观测之间夹角的余弦（视为行向量） |
| `"hamming"` | Hamming 距离，即不同坐标的百分比 |
| `"jaccard"` | 1 减去 Jaccard 系数，即不同的非零坐标的百分比 |
| `"mahalanobis"` | Mahalanobis 距离，使用正定协方差矩阵计算。默认情况下，模块从 `searcher` 对象中的数据计算协方差矩阵。您可以在“模块参数”对话框中指定自定义协方差矩阵。 |
| `"seuclidean"` | 标准化欧几里得距离。查询点 **x** 与数据之间的每个坐标差通过除以从数据计算的标准差的对应元素进行缩放。您可以在“模块参数”对话框中指定不同的缩放方法。 |
| `"spearman"` | 1 减去观测之间的样本 Spearman 秩相关（视为值序列） |

**注意**

- 距离度量设置会覆盖指定 `searcher` 对象的 `Distance` 属性。
- KNN Search 模块不支持 `"fasteuclidean"` 或 `"fastseuclidean"` 距离度量（请参阅 Distance Metrics）。

#### 编程用法

|  |
| --- |
| **模块参数：** `DistanceMetric` |
| **类型：** 字符向量 |
| **值：** `"euclidean" | "chebychev" | "cityblock" | "minkowski" | "correlation" | "cosine" | "hamming" | "jaccard" | "mahalanobis" | "seuclidean" | "spearman"` |
| **默认：** `"euclidean"` |

### **Covariance matrix** — 马哈拉诺比斯距离度量的协方差矩阵 `Computed using data in searcher`（默认）| `Customized`

默认情况下，该模块从 `searcher` 对象中的数据计算协方差矩阵。您可以通过选择 `Customized` 并在 **Customized matrix** 框中输入正定矩阵来指定自定义协方差矩阵。

**注意**

此设置会覆盖指定 `searcher` 对象的 `DistParameter` 属性。

#### 编程使用

|  |
| --- |
| **模块参数**：`CovarianceMatrix` |
| **类型**：positive definite matrix |
| **值**：`"Computed using data in searcher"` | `"Customized"` |
| **默认值**：`"Computed using data in searcher"` |

#### 依赖关系

要启用此参数，请将 **Distance Metric** 设置为 `"mahalanobis"`。

### **Scale** — 标准化欧几里得距离度量的尺度参数值 `Standard deviation of data in searcher`（默认）| `Customized`

默认情况下，该模块从 `searcher` 对象中的数据计算尺度参数值。您可以通过选择 `Customized` 并在 **Customized scale** 文本框中输入非负数值行向量来指定自定义尺度参数值。该行向量的列数必须与 `searcher` 对象中预测变量的数量相同。当模块计算标准化欧几里得距离时，数据的每个坐标以及查询点都会按 `Scale` 中对应元素进行缩放。

**注意**

此设置会覆盖指定 `searcher` 对象的 `DistParameter` 属性。

#### 编程使用

|  |
| --- |
| **模块参数**：`Scale` |
| **类型**：nonnegative numeric row vector |
| **值**：`"Standard deviation of data in searcher"` | `"Customized"` |
| **默认值**：`"Standard deviation of data in searcher"` |

#### 依赖关系

要启用此参数，请将 **Distance Metric** 设置为 `"seuclidean"`。

### **P** — 闵可夫斯基距离度量的指数 `2`（默认）| 正整数

指定闵可夫斯基距离度量的指数。对于 *P* = 2 的默认情况，闵可夫斯基距离给出欧几里得距离。对于 *P* = 1 的特殊情况，闵可夫斯基距离给出城市街区距离。对于 *P* = ∞ 的特殊情况，闵可夫斯基距离给出切比雪夫距离。

**注意**

此设置会覆盖指定 `searcher` 对象的 `DistParameter` 属性。

#### 编程使用

|  |
| --- |
| **模块参数**：`MinkExp` |
| **类型**：positive integer |
| **值**：`positive integer` |
| **默认值**：`2` |

#### 依赖关系

要启用此参数，请将 **Distance Metric** 设置为 `"minkowski"`。

### 数据类型

#### Fixed-Point Operational Parameters

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请使用 MATLAB® 舍入函数在掩码字段中输入表达式。

#### 编程使用

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型**：character vector |
| **值**：`"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"` |
| **默认值**：`"Floor"` |

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

指定溢出是饱和还是回绕。

| 操作 | 理由 | 对溢出的影响 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框（`on`）。 | 您的模型可能存在溢出，并且您希望在生成的代码中显式添加饱和保护。 | 溢出饱和到数据类型所能表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型能表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中该复选框后，模块输出饱和于 127。类似地，模块输出饱和于最小值 –128。 |
| 清除此复选框（`off`）。 | 您希望优化生成代码的效率。您希望避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。 | 溢出回绕到数据类型所能表示的相应值。 | `int8`（有符号 8 位整数）数据类型能表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除该复选框后，软件将导致溢出的值解释为 `int8`，这可能会产生非预期的结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。 |

#### 编程使用

|  |
| --- |
| **模块参数**：`SaturateOnIntegerOverflow` |
| **类型**：character vector |
| **值**：`"off" | "on"` |
| **默认值**：`"off"` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选中此参数可防止定点工具覆盖您为模块指定的数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型**：character vector |
| **值**：`"off" | "on"` |
| **默认值**：`"off"` |

#### 数据类型

### **Index data type** — 索引输出的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **Idx** 输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`IndicesDataTypeStr` |
| **类型**：character vector |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **索引数据类型最小值** — 索引输出的最小值 `[]`（默认）| 标量

指定 Simulink® 检查的 **Idx** 输出范围的最小值。

Simulink 使用最小值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可以移除算法代码并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**索引数据类型最小值** 参数不会饱和或裁剪实际的 **Idx** 输出信号。要执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`IndicesOutMin` |
| **类型**：标量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **索引数据类型最大值** — 索引输出的最大值 `[]`（默认）| 标量

指定 Simulink 检查的 **Idx** 输出范围的最大值。

Simulink 使用最大值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可以移除算法代码并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**索引数据类型最大值** 参数不会饱和或裁剪实际的 **Idx** 输出信号。要执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`IndicesOutMax` |
| **类型**：标量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **距离数据类型** — 距离输出的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定距离（**D**）输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`DistanceDataTypeStr` |
| **类型**：字符向量 |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

**注意**

Spearman 距离度量不支持定点数据类型。

#### 依赖关系

要启用此参数，请在“模块参数”对话框的 **Main** 选项卡上选择 **Add output port for nearest neighbor distances**。

### **Distance data type Minimum** — 距离输出的最小值 `[]`（默认）| 标量

指定 Simulink 检查的距离（**D**）输出范围的最小值。

Simulink 使用最小值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Distance data type Minimum** 参数不会饱和或裁剪实际的 **D** 输出信号。要执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`DistanceOutMin` |
| **类型**：scalar |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |

#### 依赖关系

要启用此参数，请在 Block Parameters 对话框的 **Main** 选项卡上选择 **Add output port for nearest neighbor distances**。

### **Distance data type Maximum** — 距离输出的最大值 `[]`（默认）| 标量

指定 Simulink 检查的距离（**D**）输出范围的最大值。

Simulink 使用最大值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Distance data type Maximum** 参数不会饱和或裁剪实际的 **D** 输出信号。要执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`DistanceOutMax` |
| **类型**：scalar |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |

#### 依赖关系

要启用此参数，请在 Block Parameters 对话框的 **Main** 选项卡上选择 **Add output port for nearest neighbor distances**。
## 所属库

Statistics and Machine Learning Toolbox / Neighborhood Searcher

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2023b 中引入**

## 描述

使用搜索器对象查找 k 最近邻

KNN Search 模块使用最近邻搜索器对象（`ExhaustiveSearcher` 或 `KDTreeSearcher`）在数据中查找与查询点最近的邻居。

通过指定包含已训练搜索器对象的工作区变量名称，将包含观测数据的已训练搜索器对象导入模块。输入端口 **x** 接收查询点，输出端口 **Idx** 返回数据中 *k* 最近邻点的索引。可选输出端口 **D** 返回查询点与最近邻点之间的距离。
