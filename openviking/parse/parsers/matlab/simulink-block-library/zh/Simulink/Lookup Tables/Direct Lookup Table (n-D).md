---
type: simulink-block
title: 'Direct Lookup Table (n-D)'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Lookup Tables'
documentation_page: 'directlookuptablend'
documentation_source_path: 'slref/directlookuptablend.html'
language: zh-CN
chinese_source: worker-translation
---

# Direct Lookup Table (n-D)

## 端口
```yaml
ports:
- name: Port_1
  summary: 索引 i1 输入值 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated
- name: Port_N
  summary: 索引 N 输入值 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated
- name: T
  summary: 表数据 向量 | 矩阵 | N 维数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated
- name: Port_1
  summary: 输出元素、向量或二维矩阵 标量 | 向量 | 二维矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated
```

### 输入

### **Port\_1** — 索引 `i1` 输入值 标量 | 向量

对于默认的列优先算法，第一个输入端口，指定比输出维度高一维（0、1 或 2）的表维度的从零开始的索引。下一个输入指定下一个表维度的从零开始的索引，依此类推。所有索引输入必须为实数值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **Port\_N** — 索引 `N` 输入值 标量 | 向量

对于默认的列优先算法，第 N 个输入端口，指定比输出维度高 N 维（0、1 或 2）的表维度的从零开始的索引。输入的数量随输出的形状而变化。所有索引输入必须为实数值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **T** — 表数据 向量 | 矩阵 | N 维数组

表数据，指定为向量、矩阵或 N 维数组。表大小必须与 **Number of dimensions** 参数的维度匹配。模块的输出数据类型与表数据类型相同。

#### 依赖关系

要启用此端口，请选中 **Make table an input** 复选框。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### 输出

### **Port\_1** — 输出元素、向量或二维矩阵 标量 | 向量 | 二维矩阵

输出切片，以标量、向量或二维矩阵形式提供。模块输出的大小由 **Inputs select this object from table** 参数的设置决定。输出数据类型与表数据类型相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
## 参数
```yaml
parameters:
- name: Number of table dimensions
  summary: 表数据的维度数 2（默认） | 1 | 3 | 4 | ...
  group: 主要
  block_parameter: NumberOfTableDimensions
  type: 字符向量
  values: '''1'' | ''2'' | ''3'' | ''4'' | ... |''30'''
  default: '''2'''
- name: Make table an input
  summary: 将表数据作为模块输入提供 off（默认） | on
  group: 主要
  block_parameter: TableIsInput
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
- name: Table data
  summary: 输出值表 [4 5 6; 16 19 20; 10 18 23]（默认） | 标量 | 向量 | 矩阵 | N 维数组
  group: 主要
  block_parameter: Table
  type: 字符向量
  values: 标量 | 向量 | 矩阵 | N 维数组
  default: '''[4 5 6;16 19 20;10 18 23]'''
- name: Inputs select this object from table
  summary: 指定输出是元素、向量还是二维矩阵 Element（默认） | Vector | 2-D Matrix
  group: 主要
  block_parameter: InputsSelectThisObjectFromTable
  type: 字符向量
  values: '''Element'' | ''Vector'' | ''2-D Matrix'''
  default: '''Element'''
- name: Diagnostic for out-of-range input
  summary: 输入超出范围时的模块操作 Warning（默认） | None | Error
  group: 主要
  block_parameter: DiagnosticForOutOfRangeInput
  type: 字符向量
  values: '''None'' | ''Warning'' | ''Error'''
  default: '''Warning'''
- name: Sample time (-1 for inherited)
  summary: 采样之间的间隔 -1（默认） | 标量 | 向量
  group: 主要
  block_parameter: SampleTime
  values: '"-1"（默认） | 带引号的标量或向量'
- name: Remove protection against out-of-range input in generated code
  summary: 移除检查超出范围输入值的代码 off（默认） | on
  group: 代码生成
  block_parameter: RemoveProtectionInput
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
- name: Table minimum
  summary: 表数据可以具有的最小值 []（默认） | 有限、实数、双精度、标量
  group: 表属性
  block_parameter: TableMin
  type: 字符向量
  values: 标量
  default: '''[]'''
- name: Table maximum
  summary: 表数据可以具有的最大值 []（默认） | 有限、实数、双精度、标量
  group: 表属性
  block_parameter: TableMax
  type: 字符向量
  values: 标量
  default: '''[]'''
- name: Table data type
  summary: '表数据的数据类型 Inherit: Inherit from ''Table data''（默认） | double | single | half | int8 | uint8 | int16 | uint16 | int32
    | uint32 | int64 | uint64 | boolean | fixdt(1,16) | fixdt(1,16,0) | fixdt(1,16,2^0,0) | Enum: <class name> | <data type
    expression>'
  group: 表属性
  block_parameter: TableDataTypeStr
  type: 字符向量
  values: '''Inherit: Inherit from ''Table data'''' | ''double'' | ''single'' | ''half'' | ''int8'' | ''uint8'' | ''int16''
    | ''uint16'' | ''int32'' | ''uint32'' | ''int64'' | ''uint64'' | ''boolean'' | ''fixdt(1,16)'' | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)''|''Enum:
    <class name>''|''<data type expression>'''
  default: '''Inherit: Inherit from ''Table data'''''
- name: Lock data type settings against changes by the fixed-point tools
  summary: 防止定点工具覆盖数据类型 off（默认） | on
  group: 表属性
  block_parameter: LockScale
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
```

### 主要

#### 表

### **Number of table dimensions** — 表数据的维度数 `2`（默认） | `1` | `3` | `4` | ...

**Table data** 参数必须具有的维度数。此值决定表的自变量数量以及模块的输入数量。

| 要指定... | 请执行此操作... |
| --- | --- |
| 1、2、3 或 4 | 从菜单中选择值。 |
| 更高的表维度数 | 直接在框中输入正整数。此模块支持的最大表维度数为 30。 |

#### 编程用法

|  |
| --- |
| **模块参数：** `NumberOfTableDimensions` |
| **类型：** 字符向量 |
| **值：** `'1' | '2' | '3' | '4' | ... |'30'` |
| **默认值：** `'2'` |

### **Make table an input** — 将表数据作为模块输入提供 `off`（默认） | `on`

选中此复选框可将表数据作为模块输入提供给 Direct Lookup Table (n-D) 模块。选中此复选框时，会出现一个新的输入端口 `T`。使用此端口输入表数据。

#### 编程用法

|  |
| --- |
| **模块参数：** `TableIsInput` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **Table data** — 输出值表 `[4 5 6; 16 19 20; 10 18 23]`（默认） | 标量 | 向量 | 矩阵 | N 维数组

指定输出值表。表大小必须与 **Number of table dimensions** 参数的维度匹配。

**提示**

在模块图编辑期间，可以将 **Table data** 字段留空。但对于仿真，必须使 **Table data** 中的维度数与 **Number of table dimensions** 匹配。有关如何构造多维 MATLAB® 数组的详细信息，请参阅多维数组。

单击 **Edit** 打开查找表编辑器。有关详细信息，请参阅查找表编辑器。

#### 依赖关系

要启用 **Table data** 字段，请清除 **Make table an input** 复选框。

#### 编程用法

|  |
| --- |
| **模块参数：** `Table` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 | 矩阵 | N 维数组 |
| **默认值：** `'[4 5 6;16 19 20;10 18 23]'` |

#### 算法

### **Inputs select this object from table** — 指定输出是元素、向量还是二维矩阵 `Element`（默认） | `Vector` | `2-D Matrix`

指定输出数据是单个元素、向量还是二维矩阵。用于索引的输入端口数量取决于您的选择。

| 选择 | 用于索引的输入端口数量 |
| --- | --- |
| `Element` | 表维度数 |
| `Vector` | 表维度数 -1 |
| `2-D Matrix` | 表维度数 -2 |

此编号与 MATLAB 索引一致。例如，如果您有一个 4 维数据表，请遵循以下准则。

| 要访问... | 请指定... | 如... |
| --- | --- | --- |
| 一个元素 | 四个索引 | `array(1,2,3,4)` |
| 一个向量 | 三个索引 | `array(:,2,3,4)`（默认列优先算法） |
| 一个二维矩阵 | 两个索引 | `array(:,:,3,4)`（默认列优先算法） |

#### 提示

当 **Math and Data Types** > **Use algorithms optimized for row-major array layout** 配置参数被设置时，Direct Lookup Table 模块的行为从列优先变为行优先。对于此模块，列优先和行优先算法在输出计算中可能在语义上不同，从而导致不同的数值。例如，假设 **Inputs select this object from table** 参数设置为 `Vector`。所选向量的元素在表存储内存中是连续的。此表显示了取决于表维度的列优先和行优先算法：

| 表维度 | 列优先算法 | 行优先算法 |
| --- | --- | --- |
| 二维表 | 选择列向量 | 选择行向量 |
| 三维及更高维表 | 从表的第一个维度选择输出向量 | 从表的最后一个维度选择输出向量 |

考虑从三维表输出向量的行优先和列优先直接查找算法。最后一个维度是三维表的第三个维度。由于语义变化，列优先和行优先直接查找可能输出不同的向量大小和数值。

此图显示了一个配置为三维表和向量输出的 Direct Lookup Table (n-D) 模块。默认情况下，模块图标显示列优先算法。

要使同一模块使用行优先算法，请更改模型的 **Math and Data Types** > **Use algorithm optimized for row-major layout** 配置参数并重新编译。模块图标会更改以反映针对行优先行为优化的算法的变化。

有关行优先支持的详细信息，请参阅矩阵和数组的代码生成 (Simulink Coder)。

#### 编程用法

|  |
| --- |
| **模块参数：** `InputsSelectThisObjectFromTable` |
| **类型：** 字符向量 |
| **值：** `'Element' | 'Vector' | '2-D Matrix'` |
| **默认值：** `'Element'` |

### **Diagnostic for out-of-range input** — 输入超出范围时的模块操作 `Warning`（默认） | `None` | `Error`

指定当索引相对于表维度超出范围时是显示警告还是错误。选项包括：

- `None` — 不产生任何响应。
- `Warning` — 显示警告并继续仿真。
- `Error` — 终止仿真并显示错误。

当您选择 `None` 或 `Warning` 时，模块会将超出范围的索引钳制以适合表维度。例如，如果指定的索引为 5.3 且该表维度的最大索引为 4，则模块会将索引钳制为 4。

#### 编程用法

|  |
| --- |
| **模块参数：** `DiagnosticForOutOfRangeInput` |
| **类型：** 字符向量 |
| **值：** `'None' | 'Warning' | 'Error'` |
| **默认值：** `'Warning'` |

### **Sample time (-1 for inherited)** — 采样之间的间隔 `-1`（默认） | 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

#### 依赖关系

仅当您将其设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅不建议使用采样时间的模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认） | 带引号的标量或向量 |

### 代码生成

### **Remove protection against out-of-range input in generated code** — 移除检查超出范围输入值的代码 `off`（默认） | `on`

指定是否包含检查超出范围输入值的代码。

| 复选框 | 结果 | 何时使用 |
| --- | --- | --- |
| `on` | 生成的代码不包含用于检查超出范围断点输入的条件语句。当输入超出范围时，可能导致生成代码出现未定义行为。 | 为了提高代码效率 |
| `off` | 生成的代码包含用于检查超出范围输入的条件语句。 | 用于安全关键型应用 |

如果您的输入未超出范围，可以选中 **Remove protection against out-of-range index in generated code** 复选框以提高代码效率。默认情况下，此复选框处于清除状态。对于安全关键型应用，请勿选中此复选框。如果要选中 **Remove protection against out-of-range index in generated code** 复选框，请先检查模型输入是否在范围内。例如：

1. 清除 **Remove protection against out-of-range index in generated code** 复选框。
2. 将 **Diagnostic for out-of-range input** 参数设置为 `Error`。
3. 在正常模式下仿真模型。
4. 如果存在超出范围的错误，请修复使其在范围内，然后再次运行仿真。
5. 当仿真不再生成超出范围输入错误时，选中 **Remove protection against out-of-range index in generated code** 复选框。

   **注意**

   当您选中 **Remove protection against out-of-range index in generated code** 复选框且输入超出范围时，生成代码的行为是未定义的。

根据您的应用，可以运行以下模型顾问检查来验证此复选框的使用情况：

- **按产品** > **Embedded Coder** > **识别生成高开销越界检查代码的查找表模块**
- **按产品** > **Simulink Check** > **建模标准** > **DO-178C/DO-331 检查** > **检查查找表模块的使用情况**

有关模型顾问的详细信息，请参阅运行模型顾问检查。

此外，要确定选中此复选框是否安全，如果您有 Simulink® Design Verifier™ 许可证，请考虑使用 Detect Block Input Range Violations (Simulink Design Verifier) 检查。

#### 编程用法

|  |
| --- |
| **模块参数：** `RemoveProtectionInput` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### 表属性

**注意**

如果选中 **Make table an input**，则 **Table Attributes** 窗格中的参数不可用。在这种情况下，模块从标签为 `T` 的输入端口继承所有表属性。

### **Table minimum** — 表数据可以具有的最小值 `[]`（默认） | 有限、实数、双精度、标量

指定表数据的最小值。默认值为 `[]`（未指定）。

#### 编程用法

|  |
| --- |
| **模块参数：** `TableMin` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认值：** `'[]'` |

### **Table maximum** — 表数据可以具有的最大值 `[]`（默认） | 有限、实数、双精度、标量

指定表数据的最大值。默认值为 `[]`（未指定）。

#### 编程用法

|  |
| --- |
| **模块参数：** `TableMax` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认值：** `'[]'` |

### **Table data type** — 表数据的数据类型 `Inherit: Inherit from 'Table data'`（默认） | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

指定表数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit from 'Table data'`
- 内置数据类型的名称，例如 `single`
- 数据类型类的名称，例如枚举数据类型类
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关详细信息，请参阅使用 Data Type Assistant 指定数据类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `TableDataTypeStr` |
| **类型：** 字符向量 |
| **值：** `'Inherit: Inherit from 'Table data'' | 'double' | 'single' | 'half' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'boolean' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)'|'Enum: <class name>'|'<data type expression>'` |
| **默认值：** `'Inherit: Inherit from 'Table data''` |

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认） | `on`

选中此参数可防止定点工具覆盖您在此模块上指定的数据类型。有关详细信息，请参阅锁定输出数据类型设置 (Fixed-Point Designer)。

#### 编程用法

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |
## 所属库

Simulink / Lookup Tables HDL Coder / Lookup Tables

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed pointa` | `half` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 此模块仅支持 'Table' 数据的定点数据类型。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

**MAX 10 设备设置**

如果您使用 Intel® MAX 10 设备，要将查找表映射到 RAM，请在 Quartus 工具中创建工程时添加以下 Tcl 命令：

`set_global_assignment -name INTERNAL_FLASH_UPDATE_MODE "SINGLE IMAGE
WITH ERAM"`

**必需的模块设置**

- **Number of table dimensions**：选择 1 到 30 之间的表维度。
- **Make table an input**：清除此复选框。
- **Diagnostic for out-of-range input**：选择 `None`、`Warning`（默认）或 `Error`（推荐）。选择 `Error` 以实现高效的 HDL 代码生成。如果选择 `None` 或 `Warning`，HDL Coder 会生成额外的逻辑来处理超出范围的输入。

**表数据类型和大小**

- 良好的做法是将表中的每个维度大小设为 2 的幂。如果某个维度（*除*最内层维度外）的长度不是 2 的幂，HDL Coder 会发出警告。遵循此做法，您可以避免表索引操作期间的乘法运算，并在硬件中实现更高效的表。
- 模块上的所有端口都要求标量值。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

此模块仅对 **Table data** 支持定点数据类型。除了内置数据类型外，索引输入还支持偏置等于 0、斜率等于 1.0、小数长度等于 0、字长小于或等于 65,535 的定点数据类型。

## 版本历史

**在 R2006a 之前引入**

## 描述

索引 n 维表以检索元素、向量或二维矩阵

Direct Lookup Table (n-D) 模块索引 n 维表以检索元素、向量或二维矩阵。第一个选择索引对应于顶部（或左侧）输入端口。您可以选择将表数据作为模块的输入提供，或在模块对话框中定义表数据。输入端口数量和输出大小取决于表维度和您选择的输出切片。

如果从二维表中选择向量，输出向量可以是列或行，具体取决于模型配置参数 **Math and Data Types** > **Use algorithms optimized for row-major array layout** 的设置。模块输入是从零开始的索引（有关更多信息，请参阅 **Inputs select this object from table** 参数。

Direct Lookup Table 模块支持符号维度。

### 模块输入和输出

Direct Lookup Table (n-D) 模块使用输入作为 *n* 维表中从零开始的索引。输入数量随输出形状而变化：元素、向量或二维矩阵。

您将一组输出值定义为 **Table data** 参数。对于默认的列优先算法行为，第一个输入指定比输出维度高一维的表维度的从零开始的索引。下一个输入指定下一个表维度的从零开始的索引，依此类推。

| 输出形状 | 输出维度 | 映射到第一个输入的表维度 |
| --- | --- | --- |
| 元素 | 0 | 1 |
| 向量 | 1 | 2 |
| 矩阵 | 2 | 3 |

假设您想从四维表中选择一个值向量。

以下模块输入端口到表维度的映射适用。

| 此输入端口... | 是此表维度的索引... |
| --- | --- |
| 1 | 2 |
| 2 | 3 |
| 3 | 4 |

### 模块图标外观的变化

根据您设置的参数，模块图标外观会发生变化。对于高于 4 的表维度，图标与四维版本匹配，但在顶部显示确切的维度数。

当您使用 **Table data** 参数时，对于默认的列优先行为，您会看到这些图标。当您选择配置参数 **Math and Data Types** > **Use algorithms optimized for row-major array layout** 时，某些图标会有所不同。

| 输入从表中选择的对象 | 表维度数 | | | |
| --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 |
| 元素 |  |  |  |  |
| 向量 |  |  |  |  |
| 二维矩阵 | 不适用 |  |  |  |

当您使用表输入端口时，您会看到这些图标。

| 输入从表中选择的对象 | 表维度数 | | | |
| --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 |
| 元素 |  |  |  |  |
| 向量 |  |  |  |  |
| 二维矩阵 | 不适用 |  |  |  |
