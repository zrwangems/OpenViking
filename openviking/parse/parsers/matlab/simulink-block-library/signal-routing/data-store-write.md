---
type: simulink-block
title: 'Data Store Write'
family: signal-routing
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'datastorewrite'
---

# Data Store Write

Write data to data store

## 中文

向数据存储中写入数据

### 所属库

Simulink / Signal Routing

### 描述

Data Store Write 模块将其输入端口的值复制到指定的数据存储中。由 Data Store Write 模块执行的每个写入操作都会覆盖数据存储或其所选部分，并替换以前的内容。

此模块写入的数据存储由定义数据存储的 Data Store Memory 模块或信号对象的位置决定。有关详细信息，请参阅数据存储和 Data Store Memory。数据存储的大小由定义并初始化数据存储的信号对象或 Data Store Memory 模块决定。写入该数据存储的每个 Data Store Write 模块最多可以写入数据存储中的数据量。

多个 Data Store Write 模块可以写入同一数据存储。但是，如果两个 Data Store Write 模块尝试在同一个仿真步中写入同一个数据存储，将发生不可预知的结果。

要从数据存储获取正确的结果，必须确保数据存储按照预期的顺序进行读取和写入。有关详细信息，请参阅对数据存储访问进行排序和数据存储诊断。

您可以记录某个局部或全局数据存储数据变量在一次仿真过程的所有时间步中的值。有关详细信息，请参阅Log Data Stores。

您可以选择 Data Store Read、Data Store Write 或 Data Store Memory 模块来突出显示与其相关的模块。要在打开的图或新选项卡中显示相关模块，请在选择后出现的省略号上暂停。然后，从操作栏中选择相关模块 。当多个模块对应于所选模块时，将打开一个相关模块列表。您可以通过在文本框中输入搜索词来过滤相关模块列表。从列表中选择相关模块后，窗口焦点转至显示该相关模块的打开的图或新选项卡。

当 Data Store Write 模块写入**维度**参数值设置为 `Inf` 的 Data Store Memory 模块时，不支持**元素赋值**选项卡。换句话说，数据存储设置为接受无界可变大小信号。

### 端口

#### 输入

#### **Port\_1** — 要写入数据存储的值 标量 | 向量 | 矩阵 | N 维数组

要写入指定数据存储的值。Data Store Write 模块接受实信号或复信号。

您可以将总线数组与 Data Store Write 模块结合使用。有关定义和使用总线数组的详细信息，请参阅使用总线数组组合非虚拟总线。

要将总线或矩阵元素的子集赋给相关联的数据存储，请使用**元素赋值**窗格。Data Store Write 模块图标反映您指定的元素。有关详细信息，请参阅访问特定的总线和矩阵元素。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

#### **IdxN** — 第 *N* 个索引信号 标量 | 向量

外部端口，用于指定对应数据存储子元素的赋值的索引。

##### 依赖关系

要启用外部索引端口，请在**元素赋值**选项卡上选择**启用索引**。然后，在**索引选项**表的第 *N* 行中，将**索引选项**设置为**索引向量(端口)** 或**起始索引(端口)**。

**数据类型:** `int8` | `int16` | `int32` | `uint8` | `uint16`

### 参数

#### 参数

#### **数据存储名称** — 模块写入的数据存储的名称 `A` (默认) | 数据存储的名称

指定此模块向其中写入数据的数据存储的名称。旁边的列表列出了模型中与 Data Store Write 模块在同一级别或更高级别的 Data Store Memory 模块的名称。该列表中还包括基础工作区和模型工作区中的所有 `Simulink.Signal` 对象。要更改名称，请从该列表中选择名称，或者直接在编辑字段中输入名称。

当编译包含此模块的模型时，软件从该模块级别向上搜索模型，寻找具有指定数据存储名称的 Data Store Memory 模块。如果软件找不到这样的模块，它将在模型工作区和 MATLAB® 工作区中搜索具有相同名称的 `Simulink.Signal` 对象。如果软件找到 `Signal` 对象，它将在模型的根级创建一个隐藏的 Data Store Memory 模块，此模块的属性由 `Signal` 对象指定，初始值设置全零数组。该数组的维度从 `Signal` 对象的 `Dimensions` 属性继承。

如果软件既找不到 Data Store Memory 模块也找不到 `Signal` 对象，它将停止编译并引发错误。有关搜索路径的详细信息，请参阅符号解析。

##### 编程用法

|  |
| --- |
| **模块参数**：`DataStoreName` |
| **类型**：字符串 | 字符向量 |
| **值**：数据存储名称 |
| **默认值**：`'A'` |

#### **Data Store Memory 模块** — Data Store Memory 模块名称 只读: 模块路径

此 参数 为只读。

此字段列出 Data Store Memory 模块，该模块对它要向其写入数据的存储进行了初始化。

#### **对应的 Data Store Read 模块** — 对应的 Data Store Read 模块列表 只读: 模块路径

此 参数 为只读。

此字段列出符合以下条件的所有 Data Store Read 模块的路径：与此模块具有相同的数据存储名称，且在模型层次结构中位于同一子系统级别或其下的任何子系统中。点击此列表中的任何条目以在模型中突出显示对应的模块。

#### **采样时间** — 采样时间 `-1` (默认) | 标量 | 向量

采样时间，用来控制模块何时写入数据存储。值为 `-1` 表示继承采样时间。有关详细信息，请参阅 指定采样时间。

##### 编程用法

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符串 | 字符向量 |
| **值**：标量 | 向量 |
| **默认值**：`'-1'` |

#### 元素赋值

#### **数组中的元素(总线中的信号)** — 关联的数据存储中的元素 字符串 | 字符向量

关联的数据存储中元素的列表。对于包含数组的数据存储，您可以写入整个数据存储，也可以将一个或多个元素赋给整个数据存储。对于总线数据类型的数据存储，您可以展开树视图以查看并选择总线元素。此列表在括号中显示每个元素的最大维度。

如果未选择**启用索引**，请选择一个元素并使用以下方法之一：

- 点击**选择>>** 在**选定元素**列表中显示该元素及其所有子元素。
- 使用**指定要赋值的元素**编辑框指定您要选择进行写入的子元素。然后点击**选择>>**。

要选择多个元素，请对每个元素重复上述过程。

您也可以选择**启用索引**，然后选择单个元素，并使用**索引选项**参数动态指定子元素。

要刷新显示并反映对数据存储中使用的数组或总线的修改，请点击**刷新**。

##### 依赖关系

对此部分（**数组中的元素**或**总线中的信号**）的提示取决于数据存储中数据的类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`DataStoreElements` |
| **类型**：字符串 | 字符向量 |
| **值**：以井号分隔的元素列表（请参阅使用命令行指定。） |
| **默认值**：`''` |

#### **指定要赋值的元素** — 定义要分配的元素的 MATLAB 表达式 字符串 | 字符向量

输入 MATLAB 表达式以定义要写入的特定元素，然后点击**选择>>** 将该元素添加到**赋值的元素**表中。重复以上操作以选择其他元素。

例如，对于名为 `DSM`、最大维度为 `[3,5]` 的数据存储，您可以在编辑框中输入表达式，如 `DSM(2,4)` 或 `DSM([1 3],2)`。请参阅访问特定的总线和矩阵元素。

要应用元素选择，请点击**确定**或**应用**。

##### 依赖关系

仅当未选择**启用索引**时，才会出现**指定要赋值的元素**编辑框。

##### 编程用法

|  |
| --- |
| **模块参数**：`DataStoreElements` |
| **类型**：字符串 | 字符向量 |
| **值**：以井号分隔的元素列表（请参阅使用命令行指定。） |
| **默认值**：`''` |

#### **赋值的元素** — 选定元素的列表 字符串 | 字符向量

您选择要分配的元素。Data Store Write 模块图标为您指定的每个元素显示输入端口。

要更改列表中的总线或矩阵元素的顺序，请在列表中选择元素，然后点击**向上**或**向下**。更改列表中的元素顺序会同时更改端口的顺序。要移除某个元素，请点击**删除**。

##### 依赖关系

要启用此参数，请清除**启用索引**。

##### 编程用法

|  |
| --- |
| **模块参数**：`DataStoreElements` |
| **类型**：字符串 | 字符向量 |
| **值**：以井号分隔的元素列表（请参阅使用命令行指定。） |
| **默认值**：`''` |

#### **启用索引** — 启用索引以指定要写入的数据存储元素的子元素 `off` (默认) | `on`

选中此参数可启用类似于 Assignment 模块所使用的索引，由此您可以使用一个或多个索引输入端口动态指定要写入的子元素的索引，以及使用模块对话框指定索引。选中此参数时，Data Store Write 模块只能写入数据存储的单个元素（即总线中的单个信号）。要使用动态索引写入数据存储的多个元素，请使用多个 Data Store Write 模块。

清除此参数可禁用 Assignment 模块样式索引。您可以选择多个要写入的数据存储元素，但只能通过使用模块对话框指定要写入哪些子元素。

**注意**

如果关联的数据存储只包含一个标量元素，请不要选择**启用索引**。

##### 编程用法

|  |
| --- |
| **模块参数**：`EnableIndexing` |
| **类型**：字符串 | 字符向量 |
| **值**：`"off"` | `"on"` |
| **默认值**：`'off'` |

#### **维数** — 数据存储元素的维数 `1` (默认) | 正整数

所选数据存储元素的维数。您必须显式指示此数目。

##### 依赖关系

要启用此参数，请选择**启用索引**。

##### 编程用法

|  |
| --- |
| **模块参数**：`NumberOfDimensions` |
| **类型**：字符串 | 字符向量 |
| **值**：正整数 |
| **默认值**：`'1'` |

#### **索引模式** — 索引模式 **从 1 开始** (默认) | **从 0 开始**

选择索引模式。如果选择**从 1 开始**，则索引 1 指定输入向量的第一个元素。如果选择**从 0 开始**，则索引 0 指定输入向量的第一个元素。

##### 依赖关系

要启用此参数，请选择**启用索引**。

##### 编程用法

|  |
| --- |
| **参数：**`IndexMode` |
| **类型：**字符串 | 字符向量 |
| **值**：`"Zero-based"` | `"One-based"` |
| **默认值：**`'One-based'` |

#### **索引选项** — 子元素的索引方法 **索引向量(对话框)** (默认) | **全选** | **索引向量(端口)** | **起始索引(对话框)** | **起始索引(端口)**

按维度定义所选数据存储元素的子元素的索引方式。从列表中，选择：

| 菜单项 | 操作 |
| --- | --- |
| **全选** | 禁用**索引**列。所有子元素都被分配。 |
| **索引向量(对话框)** | 启用**索引**列。输入包含要赋值的子元素索引的向量。 |
| **索引向量(端口)** | 禁用**索引**列。相关索引端口定义要赋值的子元素的索引。 |
| **起始索引(对话框)** | 启用**索引**列。输入要赋值的子元素范围的起始索引。范围的大小继承于输入数据信号的相关维度的大小。 |
| **起始索引(端口)** | 禁用**索引**列。相关索引端口定义要赋值的元素范围的起始索引。范围的大小继承于输入数据信号的相关维度的大小。 |

**索引**列显示为相关。

##### 依赖关系

要启用此参数，请选择**启用索引**。

##### 编程用法

|  |
| --- |
| **参数：**`IndexOptionArray` |
| **类型：**字符串 | 字符向量 |
| **值：** `"Select all"` | `"Index vector (dialog)"` | `"Index vector (port)"` | `"Starting index (dialog)"` | `"Starting index (port)"` |
| **默认值：**`'Index vector (dialog)'` |

#### **索引** — 子元素的索引或起始索引 `1` (默认) | 整数 | 整数向量

如果**索引选项**是**索引向量(对话框)**，请输入包含要写入的每个子元素的索引的向量。

如果**索引选项**设置为**起始索引(对话框)**，则输入要写入的子元素范围的起始索引。

##### 依赖关系

要启用此参数，请选择**启用索引**，并将维度的**索引选项**设置为**索引向量(对话框)** 或**起始索引(对话框)**。

##### 编程用法

|  |
| --- |
| **参数：**`IndexParamArray` |
| **类型：**字符向量 |
| **值：**元胞数组 |
| **默认值：**`'{ }'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

#### R2024a: Data Store Write 模块支持对符号索引进行索引

现在，Data Store Write 模块在 Data Store Memory 模块使用符号维度时支持索引。

## Libraries

Simulink / Signal Routing

## Description

The Data Store Write block copies the value at its input to the named
data store. Each write operation performed by a Data Store Write block
writes over the data store or a selected portion thereof and replaces the previous
contents.

The data store to which this block writes is determined by the location of the
Data Store Memory block or signal object that defines the data store.
For more information, see Data Stores and Data Store Memory. The size of the data
store is set by the signal object or the Data Store Memory block that
defines and initializes the data store. Each Data Store Write block that
writes to that data store can write up to the amount of data in the data store.

More than one Data Store Write block can write to the same data store.
However, if two Data Store Write blocks attempt to write to the same data
store during the same simulation step, results are unpredictable.

Obtaining correct results from data stores requires ensuring that data store reads and
writes occur in the expected order. For details, see Order Data Store Access and Data Store Diagnostics.

You can log the values of a local or global data store data variable for all the steps
in a simulation. For details, see Log Data Stores.

You can select a Data Store Read, Data Store Write, or
Data Store Memory block to highlight blocks related to it. To show a
related block in an open diagram or new tab, pause on the ellipsis that appears after
selection. Then, select Related Blocks  from the action bar. When multiple blocks correspond
to the selected block, a list of related blocks opens. You can filter the list of
related blocks by entering a search term in the text box. After you select a related
block from the list, window focus goes to the open diagram or new tab that shows the
related block.

**Element Assignment** tab is not supported when the Data
Store Write block writes to a Data Store Memory block with
the **Dimensions** parameter value set to `Inf`. In
other words, the data store is set to accept unbounded variable-size signals.

## Ports

### Input

### **Port\_1** — Values to write to data store scalar | vector | matrix | N-D array

Values to write to the specified data store. The Data Store
Write block accepts a real or complex signal.

You can use an array of buses with a Data Store Write
block. For details about defining and using an array of buses, see Group Nonvirtual Buses in Arrays of Buses.

To assign a subset of the bus or matrix elements to the associated
data store, use the **Element Assignment** pane. The
Data Store Write block icon reflects the elements
that you specify. For details, see Accessing Specific Bus and Matrix Elements.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### **IdxN** — *N*th index signal scalar | vector

External port that specifies an index for the assignment of the
corresponding data store subelements.

#### Dependencies

To enable an external index port, on the **Element
Assignment** tab, select **Enable
indexing**. Then, in the *N*th row of
the **Index Option** table, set **Index
Option** to `Index vector
(port)` or `Starting index
(port)`.

**Data Types:** `int8` | `int16` | `int32` | `uint8` | `uint16`

## Parameters

### Parameters

### **Data store name** — Name of data store to which block writes `A` (default) | name of data store

Specify the name of the data store to which this block writes data.
The adjacent list provides the names of Data Store Memory
blocks that exist at the same level in the model as the Data
Store Write block or at higher levels. The list also
includes all `Simulink.Signal` objects in the base and
model workspaces. To change the name, select a name from the list or
enter the name directly in the edit field.

When compiling a model that contains this block, the software searches
the model upwards from the level of the block for a Data Store
Memory block having the specified data store name. If the
software does not find such a block, it searches the model workspace and
the MATLAB® workspace for a `Simulink.Signal` object
that has the same name. If the software finds a `Signal`
object, it creates a hidden Data Store Memory block at
the root level of the model with the properties specified by the
`Signal` object and an initial value set to an array
of zeros. The dimensions of that array are inherited from the
`Dimensions` property of the
`Signal` object.

If the software finds neither the Data Store Memory
block nor the `Signal` object, it halts the compilation
and issues an error. See Symbol Resolution for more
information about the search path.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DataStoreName` |
| **Type**: string | character vector |
| **Values**: data store name |
| **Default**: `'A'` |

### **Data store memory block** — Data Store Memory block name Read-only: block path

This parameter is read-only.

This field lists the Data Store Memory block that
initialized the store to which this block writes.

### **Corresponding Data Store Read blocks** — List of corresponding Data Store Read blocks Read-only: block path

This parameter is read-only.

This field lists the path to all Data Store Read blocks
with the same data store name as this block that are in the same
subsystem or in any subsystem below it in the model hierarchy. Click any
entry in this list to highlight the corresponding block in your
model.

### **Sample time** — Sample time `-1` (default) | scalar | vector

The sample time, which controls when the block writes to the data
store. A value of `-1` indicates that the sample time
is inherited. See Specify Sample Time
for more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: string | character vector |
| **Values**: scalar | vector |
| **Default**: `'-1'` |

### Element Assignment

### **Elements in the array (Signals in the bus)** — Elements in associated data store string | character vector

List of elements in the associated data store. For data stores with
arrays, you can write the whole data store, or you can assign one or
more elements to the whole data store. For data stores with a bus data
type, you can expand the tree to view and select the bus elements. The
list displays the maximum dimensions for each element in
parentheses.

If **Enable indexing** is not selected, select an
element and use one of the following approaches:

- Click **Select>>** to display that
  element and all its subelements in the **Selected
  element(s)** list.
- Use the **Specify element(s) to assign** edit
  box to specify the subelements that you want to select for
  writing. Then click
  **Select>>**.

To select multiple elements, repeat the above procedure for each
element.

Alternatively, you can select **Enable indexing**,
then select a single element and specify the subelements dynamically
using the **Index Option** parameter.

To refresh the display and reflect modifications to the array or bus
used in the data store, click **Refresh**.

#### Dependencies

The prompt for this section (**Elements in the
array** or **Signals in the bus**)
depends on the type of data in the data store.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DataStoreElements` |
| **Type**: string | character vector |
| **Values**: pound-delimited list of elements (See Specification using the command line.) |
| **Default**: `''` |

### **Specify element(s) to assign** — MATLAB expression defining the elements to assign string | character vector

Enter a MATLAB expression to define the specific element that you want to
write, then click **Select>>** to add the
element to the **Assigned element(s)** table. Repeat to
select additional elements.

For example, for a data store named `DSM` that has
maximum dimensions of `[3,5]`, you could enter
expressions such as `DSM(2,4)` or `DSM([1
3],2)` in the edit box. See Accessing Specific Bus and Matrix Elements.

To apply the element selection, click **OK** or
**Apply**.

#### Dependencies

The **Specify element(s) to assign** edit box
appears only if **Enable indexing** is not
selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DataStoreElements` |
| **Type**: string | character vector |
| **Values**: pound-delimited list of elements (See Specification using the command line.) |
| **Default**: `''` |

### **Assigned element(s)** — List of selected elements string | character vector

Elements that you select for assignment. The Data Store
Write block icon displays an input port for each element
that you specify.

To change the order of bus or matrix elements in the list, select the
element in the list and click **Up** or
**Down**. Changing the order of the elements in
the list changes the order of the ports. To remove an element, click
**Remove**.

#### Dependencies

To enable this parameter, clear **Enable
indexing**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DataStoreElements` |
| **Type**: string | character vector |
| **Values**: pound-delimited list of elements (See Specification using the command line.) |
| **Default**: `''` |

### **Enable indexing** — Enable indexing to specify subelements of data store element to write `off` (default) | `on`

Select this parameter to enable indexing similar to that used by the
Assignment block,
whereby you can dynamically specify indices of subelements to write by
using one or more index input ports, as well as specifying indices by
using the block dialog. A Data Store Write block can
write to only a single element of a data store (that is, a single signal
in a bus) when this parameter is selected. To write to multiple elements
of a data store using dynamic indexing, use multiple Data Store
Write blocks.

Clear this parameter to disable Assignment block-style
indexing. You can select multiple data store elements to write, but you
can specify which subelements to write only by using the block
dialog.

**Note**

Do not select **Enable indexing** if the
associated data store contains only a single, scalar element.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `EnableIndexing` |
| **Type**: string | character vector |
| **Values**: `"off"` | `"on"` |
| **Default**: `'off'` |

### **Number of dimensions** — Number of dimensions of data store element `1` (default) | positive integer

Number of dimensions of selected data store element. You must
explicitly indicate this number.

#### Dependencies

To enable this parameter, select **Enable
indexing**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberOfDimensions` |
| **Type**: string | character vector |
| **Values**: positive integer |
| **Default**: `'1'` |

### **Index mode** — Index mode `One-based` (default) | `Zero-based`

Select the indexing mode. If `One-based` is
selected, an index of 1 specifies the first element of the input vector.
If `Zero-based` is selected, an index of 0
specifies the first element of the input vector.

#### Dependencies

To enable this parameter, select **Enable
indexing**.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `IndexMode` |
| **Type:** string | character vector |
| **Values:** `"Zero-based"` | `"One-based"` |
| **Default:** `'One-based'` |

### **Index Option** — Index method for subelements `Index vector (dialog)` (default) | `Select all` | `Index vector (port)` | `Starting index (dialog)` | `Starting index (port)`

Define, by dimension, how the subelements of the selected data store
element are to be indexed. From the list, select:

| Menu Item | Action |
| --- | --- |
| `Select all` | Disables the **Index** column. All subelements are assigned. |
| `Index vector (dialog)` | Enables the **Index** column. Enter a vector containing the indices of subelements to be assigned values. |
| `Index vector (port)` | Disables the **Index** column. The relevant index port defines the indices of subelements to be assigned values. |
| `Starting index (dialog)` | Enables the **Index** column. Enter the starting index of the range of subelements to be assigned values. The size of the range is inherited from the size of relevant dimension of the input data signal. |
| `Starting index (port)` | Disables the **Index** column. The relevant index port defines the starting index of the range of elements to be assigned values. The size of the range is inherited from the size of relevant dimension of the input data signal. |

The **Index** column is displayed as relevant.

#### Dependencies

To enable this parameter, select **Enable
indexing**.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `IndexOptionArray` |
| **Type:** string | character vector |
| **Values:** `"Select all"` | `"Index vector (dialog)"` | `"Index vector (port)"` | `"Starting index (dialog)"` | `"Starting index (port)"` |
| **Default:** `'Index vector (dialog)'` |

### **Index** — Indices or starting index of subelements `1` (default) | integer | vector of integers

If the **Index Option** is `Index vector
(dialog)`, enter a vector containing the indices of
each subelement to write.

If the **Index Option** is `Starting
index (dialog)`, enter the starting index of the range
of subelements to write.

#### Dependencies

To enable this parameter, select **Enable
indexing** and set **Index Option**
for the dimension to `Index vector
(dialog)` or `Starting index
(dialog)`.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `IndexParamArray` |
| **Type:** character vector |
| **Values:** cell array |
| **Default:** `'{ }'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2024a: Data Store Write Block Supports Indexing for Symbolic Indexing

The Data Store Write block now supports indexing when the Data Store Memory block uses
symbolic dimensions.
