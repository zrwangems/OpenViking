---
type: simulink-block
title: 'Direct Lookup Table (n-D)'
family: lookup-tables
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Lookup Tables'
documentation_page: 'directlookuptablend'
---

# Direct Lookup Table (n-D)

Index into n-dimensional table to retrieve element, vector, or 2-D matrix

## 中文

为 N 维表进行索引，以检索元素、向量或二维矩阵

### 所属库

Simulink / Lookup Tables HDL Coder / Lookup Tables

### 描述

Direct Lookup Table (n-D) 模块为 N 维表进行索引，以检索元素、向量或二维矩阵。第一个选择索引对应于顶部（或左侧）输入端口。您可以选择提供表数据作为模块的输入，或者在模块对话框中定义表数据。输入端口的数量和输出的大小取决于表维度的数量和您选择的输出切片。

如果从二维表中选择向量，则输出向量可以是列或行，具体取决于模型配置参数设置**数学和数据类型** > **使用针对行优先数组布局优化的算法**。模块输入是从 0 开始的索引（有关详细信息，请参阅**输入从表中选择的对象**参数）。

Direct Lookup Table 模块支持符号维度。

#### 模块输入和输出

Direct Lookup Table (n-D) 模块使用输入作为 *n* 维表的索引（从零开始）。输入数目因输出的形状（元素、向量或二维矩阵）不同而不同。

您可以为**表数据**参数定义一组输出值。对于默认列优先算法行为，第一个输入为比输出维度大一的表维度指定从 0 开始的索引。下一个输入为下一个表维度指定从零开始的索引，以此类推。

| 输出形状 | 输出维度 | 对应于第一个输入的表维度 |
| --- | --- | --- |
| 元素 | 0 | 1 |
| 向量 | 1 | 2 |
| 矩阵 | 2 | 3 |

假设您要选择由四维表中的值构成的一个向量。

模块输入端口与表维度之间的对应关系如下表所示。

| 此输入端口... | 是此表维度的索引... |
| --- | --- |
| 1 | 2 |
| 2 | 3 |
| 3 | 4 |

#### 模块图标的外观变化

根据您设置的参数，模块图标的外观会发生变化。对于大于 4 的表维度，图标与四维版本匹配，但在顶部显示确切的维数。

当您使用**表数据**参数时，您将看到以下默认列优先行为的图标。选择配置参数**数学和数据类型** > **使用针对行优先数组布局优化的算法**时，某些图标会有所不同。

| 输入信号从表中选择的对象 | 表维数 | | | |
| --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 |
| 元素 |  |  |  |  |
| 向量 |  |  |  |  |
| 二维矩阵 | 不适用 |  |  |  |

当您使用表输入端口时，您将看到以下图标。

| 输入信号从表中选择的对象 | 表维数 | | | |
| --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 |
| 元素 |  |  |  |  |
| 向量 |  |  |  |  |
| 二维矩阵 | 不适用 |  |  |  |

### 端口

#### 输入

#### **Port\_1** — 索引 `i1` 的输入值 标量 | 向量

对于默认列优先算法，第一个输入端口指定比输出维度（0、1 或 2）大 1 的表维度中从零开始的索引。下一个输入为下一个表维度指定从零开始的索引，以此类推。所有索引输入必须是实数值。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

#### **Port\_N** — 索引 `N` 的输入值 标量 | 向量

对于默认列优先算法，第 N 个输入端口指定比输出维度（0、1 或 2）大 N 的表维度中从零开始的索引。输入数目随输出的形状而有所不同。所有索引输入必须是实数值。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

#### **T** — 表数据 向量 | 矩阵 | N 维数组

表数据，指定为向量，矩阵或 N 维数组。表大小必须与**维数**参数的维度相匹配。模块的输出数据类型与表数据类型相同。

##### 依赖关系

要启用此端口，请选中**将表作为输入**复选框。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
#### 输出

#### **Port\_1** — 输出元素、向量或二维矩阵 标量 | 向量 | 二维矩阵

输出切片，作为标量、向量或二维矩阵提供。模块输出的大小由**输入从表中选择的对象**参数的设置决定。输出数据类型与表数据类型相同。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### 参数

#### 常设

##### 表

#### **表维数** — 表数据的维数 `2` (默认) | `1` | `3` | `4` | ...

**表数据**参数必须具有的维数。此值决定表的自变量数和模块的输入数目。

| 要指定... | 执行此操作... |
| --- | --- |
| 1、2、3 或 4 | 从菜单中选择值。 |
| 更高的表维数 | 直接在框中输入正整数。  此模块支持的最大表维数为 30。 |

##### 编程用法

|  |
| --- |
| **模块参数**：`NumberOfTableDimensions` |
| **类型：**字符向量 |
| **值：** `'1' | '2' | '3' | '4' | ... |'30'` |
| **默认值：**`'2'` |

#### **将表作为输入** — 提供表数据作为模块输入 `off` (默认) | `on`

选中此复选框可将表数据作为模块输入提供给 Direct Lookup Table (n-D) 模块。当您选中此复选框时，会出现新输入端口 `T`。使用此端口输入表数据。

##### 编程用法

|  |
| --- |
| **模块参数**：`TableIsInput` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **表数据** — 输出值的表 `[4 5 6; 16 19 20; 10 18 23]` (默认) | 标量 | 向量 | 矩阵 | N 维数组

指定输出值表。表大小必须与**表维数**参数的维度相匹配。

**提示**

在编辑模块图的过程中，您可以将**表数据**字段留空。但是，要进行仿真，**表数据**的维数必须与**表维数**匹配。有关如何构造多维 MATLAB® 数组的详细信息，请参阅多维数组。

点击**编辑**以打开查找表编辑器。有关详细信息，请参阅查找表编辑器。

##### 依赖关系

要启用**表数据**字段，请清除**将表作为输入**复选框。

##### 编程用法

|  |
| --- |
| **模块参数**：`Table` |
| **类型：**字符向量 |
| **值：** 标量 | 向量 | 矩阵 | N 维数组 |
| **默认值：**`'[4 5 6;16 19 20;10 18 23]'` |

##### 算法

#### **输入从表中选择的对象** — 指定输出是元素、向量还是二维矩阵 **元素** (默认) | **向量** | **二维矩阵**

指定输出数据是单个元素、向量还是二维矩阵。用于索引的输入端口数取决于您的选择。

| 选择 | 用于索引的输入端口个数 |
| --- | --- |
| **元素** | 表维数 |
| **向量** | 表维数 -1 |
| **二维矩阵** | 表维数 -2 |

这种编号方法与 MATLAB 索引方法相匹配。例如，如果您有一个四维数据表，请按照以下指导准则操作。

| 要访问... | 指定... | 例如... |
| --- | --- | --- |
| 元素 | 四个索引 | `array(1,2,3,4)` |
| 向量 | 三个索引 | `array(:,2,3,4)`（默认列优先算法） |
| 二维矩阵 | 两个索引 | `array(:,:,3,4)`（默认列优先算法） |

##### 提示

设置**数学和数据类型** > **使用针对行优先数组布局优化的算法**配置参数后，Direct Lookup Table 模块行为会从列优先更改为行优先。对于此模块，列优先算法和行优先算法在输出计算中可能有着语义上的不同，从而导致数值不同。例如，假设**输入从表中选择的对象**参数设置为**向量**。所选向量的元素在表存储内存中是连续的。下表列出了不同表维度对应的列优先和行优先算法：

| 表维度 | 列优先算法 | 行优先算法 |
| --- | --- | --- |
| 二维表 | 选择列向量 | 选择行向量 |
| 三维和更高维度的表 | 从表的第一个维度中选择输出向量 | 从表的最后一个维度中选择输出向量 |

例如，使用行优先和列优先直接查找算法，从三维表获取向量输出。最后一个维度是三维表的第三维。由于语义变化，列优先和行优先直接查找可能输出不同的向量大小和数值。

下图显示配置有三维表和向量输出的 Direct Lookup Table (n-D) 模块。默认情况下，模块图标显示列优先算法。

要让此模块使用行优先算法，请更改模型的**数学和数据类型** > **使用针对行优先布局优化的算法**配置参数并重新编译。模块图标会发生变化，以反映针对行优先行为优化的算法的更改。

有关行优先支持的详细信息，请参阅Code Generation of Matrices and Arrays (Simulink Coder)。

##### 编程用法

|  |
| --- |
| **模块参数**：`InputsSelectThisObjectFromTable` |
| **类型：**字符向量 |
| **值**：`'Element' | 'Vector' | '2-D Matrix'` |
| **默认值：**`'Element'` |

#### **输入超出范围的诊断** — 当输入超出范围时的模块操作 **警告** (默认) | **无** | **错误**

指定当索引相对于表维度而超出范围时，是否显示警告或错误。选项包括：

- **无** - 不产生任何响应。
- **警告** - 显示警告并继续进行仿真。
- **错误** - 终止仿真并显示错误。

如果您选择了**无**或**警告**，模块将剪切超出范围的索引以满足表维度的要求。例如，如果指定的索引是 5.3，而表维度的最大索引是 4，模块会将索引剪切为 4。

##### 编程用法

|  |
| --- |
| **模块参数**：`DiagnosticForOutOfRangeInput` |
| **类型：**字符向量 |
| **值：**`'None' | 'Warning' | 'Error'` |
| **默认值：**`'Warning'` |

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

#### 代码生成

#### **删除生成代码中防止超范围输入的代码** — 删除检查超出范围的输入值的代码 `off` (默认) | `on`

指定是否包含代码以检查超出范围的输入值。

| 复选框 | 结果 | 何时使用 |
| --- | --- | --- |
| `on` | 生成的代码中未包含用来检查超出范围的断点输入的条件语句。  当输入超出范围时，生成的代码可能会发生未定义的行为。 | 提高代码效率 |
| `off` | 生成的代码包含用来检查超出范围的输入的条件语句。 | 适用于安全性至关重要的应用领域 |

如果您的输入没有超出范围，则可以选中**删除生成代码中防止超范围索引的代码**复选框以提高代码效率。默认情况下，此复选框处于清除状态。对于安全性至关重要的应用，不要选中此复选框。要选中**删除生成代码中防止超范围索引的代码**复选框，请先检查模型输入是否在范围内。例如：

1. 清除**删除生成代码中防止超范围索引的代码**复选框。
2. 将**输入超出范围的诊断**参数设置为 `Error`。
3. 在普通模式下进行模型仿真。
4. 如果发生超出范围错误，请将它们更正到范围之内，然后再次运行仿真。
5. 当仿真不再生成超出范围的输入错误时，选中**删除生成代码中防止超范围索引的代码**复选框。

   **注意**

   如果选中了**删除生成代码中防止超范围索引的代码**复选框而输入超出范围，生成的代码将发生未定义的行为。

根据您的具体应用，您可以运行以下模型顾问检查，以验证此复选框的使用：

- **按产品** > **Embedded Coder** > **标识哪些查找表模块会生成检查超范围值的高成本代码**
- **按产品** > **Simulink Check** > **建模标准** > **DO-178C/DO-331 检查** > **检查 Lookup Table 模块的使用**

有关模型顾问的详细信息，请参阅运行模型顾问检查。

此外，要确定选中此复选框是否安全，如果您拥有 Simulink® Design Verifier™ 许可证，请考虑使用 检测模块输入范围违规 (Simulink Design Verifier) 检查。

##### 编程用法

|  |
| --- |
| **模块参数**：`RemoveProtectionInput` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### 表属性

**注意**

如果您选择了**将表作为输入**，**表属性**窗格中的参数将不可用。这种情况下，模块将从带有 `T` 标签的输入端口继承所有表属性。

#### **表数据最小值** — 表数据可以具有的最小值 `[]` (默认) | 有限双精度实数标量

指定表数据的最小值。默认值为 `[]`（未指定）。

##### 编程用法

|  |
| --- |
| **模块参数**：`TableMin` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'[]'` |

#### **表数据最大值** — 表数据可以具有的最大值 `[]` (默认) | 有限双精度实数标量

指定表数据的最大值。默认值为 `[]`（未指定）。

##### 编程用法

|  |
| --- |
| **模块参数**：`TableMax` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'[]'` |

#### **表数据类型** — 表数据的数据类型 **继承: 从 '表数据' 继承** (默认) | **double** | **single** | **half** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **boolean** | **fixdt(1,16)** | **fixdt(1,16,0)** | **fixdt(1,16,2^0,0)** | **Enum: <class name>** | **<数据类型表达式>**

指定表数据类型。可以将其设置为：

- 继承数据类型的规则，例如**继承: 从 '表数据' 继承**
- 内置数据类型的名称，例如 `single`
- 数据类型类的名称，例如枚举数据类型类
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`TableDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Inherit from 'Table data'' | 'double' | 'single' | 'half' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'boolean' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)'|'Enum: <class name>'|'<data type expression>'` |
| **默认值：**`'Inherit: Inherit from 'Table data''` |

#### **锁定数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您对此模块指定的数据类型。有关详细信息，请参阅Lock the Output Data Type Setting (Fixed-Point Designer)。

##### 编程用法

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed pointa` | `half` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |
|  |  |
| --- | --- |
| a 仅当数据为表数据时，此模块才支持定点数据类型。 | |

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

**MAX 10 设备设置**

如果您使用 Intel® MAX 10 设备，要将查找表映射到 RAM，请当在 Quartus 工具中创建工程时添加以下 Tcl 命令：

`set_global_assignment -name INTERNAL_FLASH_UPDATE_MODE "SINGLE IMAGE WITH ERAM"`

**必需的模块设置**

- **表维数**：选择 1 到 30 之间的表维度。
- **将表作为输入**：清除此复选框。
- **输入超出范围的诊断**：选择**无**、**警告**（默认值）或**错误**（推荐）。选择**错误**可高效生成 HDL 代码。如果选择**无**或**警告**，HDL Coder 会生成额外的逻辑来处理超出范围的输入。

**表数据定型和调整大小**

- 最好将表中每个维度的大小调整为 2 的幂。如果维度（*除了*最里面的维度）的长度不是 2 的幂，HDL Coder 会发出警告。这种做法可以避免表索引操作期间的乘法运算，并在硬件中实现更高效的表。
- 模块上的所有端口都需要标量值。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

此模块仅支持对**表数据**使用定点数据类型。除内置数据类型外，索引输入还支持偏置等于 0、斜率等于 1.0、小数长度等于 0、字长小于或等于 65,535 的定点数据类型。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Lookup Tables HDL Coder / Lookup Tables

## Description

The Direct Lookup Table (n-D) block indexes into an n-dimensional table to retrieve an
element, vector, or 2-D matrix. The first selection index corresponds to the top (or
left) input port. You can choose to provide the table data as an input to the block, or
define the table data on the block dialog box. The number of input ports and the size of
the output depend on the number of table dimensions and the output slice you
select.

If you select a vector from a 2-D table, the output vector can be a column or a row,
depending on the model configuration parameter setting **Math and Data Types** > **Use algorithms optimized for row-major array layout**. The block inputs are zero-based indices (for more information, see the
**Inputs select this object from table** parameter.

The Direct Lookup Table block supports symbolic dimensions.

### Block Inputs and Outputs

The Direct Lookup Table (n-D) block uses inputs as zero-based indices into an
*n*-dimensional table. The number of inputs varies with the
shape of the output: an element, vector, or 2-D matrix.

You define a set of output values as the **Table data** parameter. For the
default column-major algorithm behavior, the first input specifies the zero-based
index to the table dimension that is one higher than the output dimensionality. The
next input specifies the zero-based index to the next table dimension, and so
on.

| Output Shape | Output Dimensionality | Table Dimension that Maps to the First Input |
| --- | --- | --- |
| Element | 0 | 1 |
| Vector | 1 | 2 |
| Matrix | 2 | 3 |

Suppose that you want to select a vector of values from a 4-D table.

The following mapping of block input port to table dimension applies.

| This input port... | Is the index for this table dimension... |
| --- | --- |
| 1 | 2 |
| 2 | 3 |
| 3 | 4 |

### Changes in Block Icon Appearance

Depending on parameters you set, the block icon changes appearance. For table dimensions
higher than 4, the icon matches the 4-D version but shows the exact number of
dimensions at the top.

When you use the **Table data** parameter, you see these icons for the
default column-major behavior. Some icons are different when you select the
configuration parameter **Math and Data Types** > **Use algorithms optimized for row-major array layout**.

| Object that Inputs Select from the Table | Number of Table Dimensions | | | |
| --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 |
| Element |  |  |  |  |
| Vector |  |  |  |  |
| 2-D Matrix | Not applicable |  |  |  |

When you use the table input port, you see these icons.

| Object that Inputs Select from the Table | Number of Table Dimensions | | | |
| --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 |
| Element |  |  |  |  |
| Vector |  |  |  |  |
| 2-D Matrix | Not applicable |  |  |  |

## Ports

### Input

### **Port\_1** — Index `i1` input values scalar | vector

For the default column-major algorithm, the first input port, specifying the zero-based
index to the table dimension that is one higher than the output
dimensionality (0, 1, or 2). The next input specifies the zero-based
index to the next table dimension, and so on. All index inputs must be
real-valued.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **Port\_N** — Index `N` input values scalar | vector

For the default column-major algorithm, the N-th input port,
specifying the zero-based index to the table dimension that is N higher
than the output dimensionality (0, 1, or 2). The number of inputs varies
with the shape of the output. All index inputs must be
real-valued.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **T** — Table data vector | matrix | N-D array

Table data, specified as a vector, matrix, or N-D array. The table size must match the
dimensions of the **Number of dimensions** parameter.
The block's output data type is the same as the table data type.

#### Dependencies

To enable this port, select the **Make table an
input** check box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### Output

### **Port\_1** — Output element, vector, or 2-D matrix scalar | vector | 2-D matrix

Output slice, provided as a scalar, vector, or 2-D matrix. The size of the block output
is determined by the setting of the **Inputs select this object
from table** parameter. The output data type is the same as
the table data type.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

## Parameters

### Main

#### Table

### **Number of table dimensions** — Number of dimensions of table data `2` (default) | `1` | `3` | `4` | ...

Number of dimensions that the **Table data** parameter must have. This
value determines the number of independent variables for the table and
the number of inputs to the block.

| To specify... | Do this... |
| --- | --- |
| 1, 2, 3, or 4 | Select the value from the menu. |
| A higher number of table dimensions | Enter a positive integer directly in the box.  The maximum number of table dimensions that this block supports is 30. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumberOfTableDimensions` |
| **Type:** character vector |
| **Values:** `'1' | '2' | '3' | '4' | ... |'30'` |
| **Default:** `'2'` |

### **Make table an input** — Provide table data as a block input `off` (default) | `on`

Select this check box to provide table data to the Direct Lookup Table
(n-D) block as a block input. When you select this check box, a new
input port, `T`, appears. Use this port to input the
table data.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableIsInput` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Table data** — Table of output values `[4 5 6; 16 19 20; 10 18 23]` (default) | scalar | vector | matrix | N-D array

Specify the table of output values. The table size must match the
dimensions of the **Number of table dimensions**
parameter.

**Tip**

During block diagram editing, you can leave the **Table
data** field empty. But for simulation, you must match
the number of dimensions in **Table data** to the
**Number of table dimensions**. For details on
how to construct multidimensional MATLAB® arrays, see Multidimensional Arrays.

Click **Edit** to open the Lookup Table Editor. For more information,
see Lookup Table Editor.

#### Dependencies

To enable the **Table data** field, clear the
**Make table an input** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Table` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix | N-D array |
| **Default:** `'[4 5 6;16 19 20;10 18 23]'` |

#### Algorithm

### **Inputs select this object from table** — Specify whether output is an element, vector, or 2-D matrix `Element` (default) | `Vector` | `2-D Matrix`

Specify whether the output data is a single element, a vector, or a
2-D matrix. The number of input ports for indexing depends on your
selection.

| Selection | Number of Input Ports for Indexing |
| --- | --- |
| `Element` | Number of table dimensions |
| `Vector` | Number of table dimensions -1 |
| `2-D Matrix` | Number of table dimensions -2 |

This numbering matches MATLAB indexing. For example, if you have a 4-D table of data,
follow these guidelines.

| To access... | Specify... | As in... |
| --- | --- | --- |
| An element | Four indices | `array(1,2,3,4)` |
| A vector | Three indices | `array(:,2,3,4)` (default column-major algorithm) |
| A 2-D matrix | Two indices | `array(:,:,3,4)` (default column-major algorithm) |

#### Tips

When the **Math and Data Types** > **Use algorithms optimized for row-major array
layout** configuration parameter is set, the Direct Lookup
Table block behavior changes from column-major to row-major. For
this block, the column-major and row-major algorithms may differ
semantically in output calculations, resulting in different
numerical values. For example, assume that **Inputs select
this object from table** parameter is set to
`Vector`. The elements of the selected
vector are contiguous in the table storage memory. This table shows
the column-major and row-major algorithm depending on the table
dimension:

| Table Dimension | Column-Major Algorithm | Row-Major Algorithm |
| --- | --- | --- |
| 2-D table | Column vector is selected | Row vector is selected |
| 3-D and higher table | Output vector is selected from the first dimension of the table | Output vector is selected from the last dimension of the table |

Consider the row-major and column-major direct lookup algorithms
with vector output from a 3-D table. The last dimension is the third
dimension of a 3-D table. Due to semantic changes, column-major and
row-major direct lookup may output different vector size and
numerical values.

This figure shows a Direct Lookup Table (n-D) block configured with a
3-D table and a vector output. By default, the block icon shows the
column-major algorithm.

To have the same block use the row-major algorithm, change the **Math and Data Types** > **Use algorithm optimized for row-major
layout** configuration parameter of the model and recompile.
The block icon changes to reflect the change to the algorithm
optimized for row-major behavior.

For more information on row-major support, see Code Generation of Matrices and Arrays (Simulink Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputsSelectThisObjectFromTable` |
| **Type:** character vector |
| **Values:** `'Element' | 'Vector' | '2-D Matrix'` |
| **Default:** `'Element'` |

### **Diagnostic for out-of-range input** — Block action when input is out of range `Warning` (default) | `None` | `Error`

Specify whether to show a warning or error when an index is out of
range with respect to the table dimension. Options include:

- `None` — Produce no
  response.
- `Warning` — Display a warning
  and continue the simulation.
- `Error` — Terminate the
  simulation and display an error.

When you select `None` or
`Warning`, the block clamps out-of-range
indices to fit table dimensions. For example, if the specified index is
5.3 and the maximum index for that table dimension is 4, the block
clamps the index to 4.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DiagnosticForOutOfRangeInput` |
| **Type:** character vector |
| **Values:** `'None' | 'Warning' | 'Error'` |
| **Default:** `'Warning'` |

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

### Code generation

### **Remove protection against out-of-range input in generated code** — Remove code that checks for out-of-range input values `off` (default) | `on`

Specify whether or not to include code that checks for out-of-range
input values.

| Check Box | Result | When to Use |
| --- | --- | --- |
| `on` | Generated code does not include conditional statements to check for out-of-range breakpoint inputs.  When the input is out-of-range, it may cause undefined behavior for generated code. | For code efficiency |
| `off` | Generated code includes conditional statements to check for out-of-range inputs. | For safety-critical applications |

If your input is not out of range, you can select the **Remove
protection against out-of-range index in generated code**
check box for code efficiency. By default, this check box is cleared.
For safety-critical applications, do not select this check box. If you
want to select the **Remove protection against out-of-range
index in generated code** check box, first check that your
model inputs are in range. For example:

1. Clear the **Remove protection against out-of-range
   index in generated code** check box.
2. Set the **Diagnostic for out-of-range input**
   parameter to `Error`.
3. Simulate the model in normal mode.
4. If there are out-of-range errors, fix them to be in range and
   run the simulation again.
5. When the simulation no longer generates out-of-range input
   errors, select the **Remove protection against
   out-of-range index in generated code** check
   box.

   **Note**

   When you select the **Remove protection against
   out-of-range index in generated code** check
   box and the input is out of range, the behavior is undefined
   for generated code.

Depending on your application, you can run the following Model Advisor
checks to verify the usage of this check box:

- **By Product** > **Embedded Coder** > **Identify lookup table blocks that generate
  expensive out-of-range checking code**
- **By Product** > **Simulink Check** > **Modeling Standards** > **DO-178C/DO-331 Checks** > **Check usage of lookup table
  blocks**

For more information about the Model Advisor, see Run Model Advisor Checks.

Additionally, to determine if it is safe to select this check box, if
you have a Simulink®
Design Verifier™ license, consider using the Detect Block Input Range Violations (Simulink Design Verifier)
check.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RemoveProtectionInput` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### Table Attributes

**Note**

The parameters in the **Table Attributes** pane are not
available if you select **Make table an input**. In this case,
the block inherits all table attributes from the input port with the label
`T`.

### **Table minimum** — Minimum value table data can have `[]` (default) | finite, real, double, scalar

Specify the minimum value for table data. The default value is
`[]` (unspecified).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableMin` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Table maximum** — Maximum value table data can have `[]` (default) | finite, real, double, scalar

Specify the maximum value for table data. The default value is
`[]` (unspecified).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableMax` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Table data type** — Data type of table data `Inherit: Inherit from 'Table data'` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

Specify the table data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit from 'Table
  data'`
- The name of a built-in data type, for example,
  `single`
- The name of a data type class, for example, an enumerated data
  type class
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit from 'Table data'' | 'double' | 'single' | 'half' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'boolean' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)'|'Enum: <class name>'|'<data type expression>'` |
| **Default:** `'Inherit: Inherit from 'Table data''` |

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types you specify on this block. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LockScale` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed pointa` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a This block supports fixed-point data types for 'Table' data only. | |

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

**MAX 10 Device Settings**

If you use Intel® MAX 10 device, to map the lookup table to RAM, add this Tcl
command when creating the project in the Quartus tool:

`set_global_assignment -name INTERNAL_FLASH_UPDATE_MODE "SINGLE IMAGE
WITH ERAM"`

**Required Block Settings**

- **Number of table dimensions**: Select the table
  dimension between 1 to 30.
- **Make table an input**: Clear this check
  box.
- **Diagnostic for out-of-range input**: Select
  `None`,
  `Warning` (default), or
  `Error` (recommended). Select
  `Error` for efficient HDL code
  generation. If you select `None` or
  `Warning`, HDL Coder generates additional logic to handle out-of-range
  inputs.

**Table Data Typing and Sizing**

- It is good practice to size each dimension in the table to be a
  power of two. If the length of a dimension
  (*except* the innermost dimension) is not a
  power of two, HDL Coder issues a warning. By following this practice, you can
  avoid multiplications during table indexing operations and realize a
  more efficient table in hardware.
- All ports on the block require
  scalar values.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

This block supports fixed-point data types for **Table data** only. In
addition to built-in data types, the index input also supports fixed-point data type
with bias equal to 0, slope equal to 1.0, fractional length equal to 0, and word
length less than or equal to 65,535.

## Version History

**Introduced before R2006a**
