---
type: simulink-block
title: 'Data Store Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'datastoreread'
documentation_source_path: 'slref/datastoreread.html'
language: zh-CN
chinese_source: worker-translation
---

# Data Store Read

## 端口

### 输入

### **IdxN** — 第 *N* 个索引信号 标量 | 向量

外部端口，用于指定对应数据存储子元素选择的索引。

#### 依赖

要启用外部索引端口，请在**元素选择**选项卡上，选择**启用索引**。然后，在**索引选项**表的第 *N* 行中，将**索引选项**设置为 `Index vector (port)` 或 `Starting index (port)`。

**数据类型：** `int8` | `int16` | `int32` | `uint8` | `uint16`
### 输出

### **Port\_1** — 来自指定数据存储的值 标量 | 向量 | 矩阵 | N 维数组

来自指定数据存储的值，在输出端提供，其数据类型和维度数与数据存储中的相同。该模块支持实信号和复信号。您可以选择该模块提供整个数据存储还是仅提供选定的元素。

您可以将总线数组与 Data Store Read 模块一起使用。有关定义和使用总线数组的详细信息，请参阅 Group Nonvirtual Buses in Arrays of Buses。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## 参数

### 参数

### **Data store name** — 模块读取的数据存储名称 `A`（默认）| 数据存储名称

指定此模块读取数据的数据存储名称。相邻列表提供与 Data Store Read 模块在模型中处于同一层级或更高层级的 Data Store Memory 模块的名称。该列表还包括基础工作区和模型工作区中的所有 `Simulink.Signal` 对象。要更改名称，请从列表中选择一个名称，或直接在编辑字段中输入名称。

在编译包含此模块的模型时，软件从模块所在层级向上搜索模型中具有指定数据存储名称的 Data Store Memory 模块。如果软件未找到此类模块，则会在模型工作区和 MATLAB® 工作区中搜索具有相同名称的 `Simulink.Signal` 对象。如果软件找到该信号对象，则会在模型根层级创建一个隐藏的 Data Store Memory 模块，其属性由 `Signal` 对象指定，初始值设置为零数组。该数组的维度继承自 `Signal` 对象的 `Dimensions` 属性。

如果软件既未找到 Data Store Memory 模块也未找到 `Signal` 对象，则会停止编译并发出错误。有关搜索路径的详细信息，请参阅 Symbol Resolution。

#### 编程使用

|  |
| --- |
| **模块参数**：`DataStoreName` |
| **类型**：string | character vector |
| **值**：数据存储名称 |
| **默认值**：`'A'` |

### **Data store memory block** — Data Store Memory 模块名称 只读：模块路径

此参数为只读。

此字段列出初始化此模块所读取数据存储的 Data Store Memory 模块。

### **Corresponding Data Store Write blocks** — 对应的 Data Store Write 模块列表 只读：模块路径

此参数为只读。

此字段列出与此模块具有相同数据存储名称的所有 Data Store Write 模块的路径，这些模块位于同一子系统或模型层级中其下方的任何子系统中。单击此列表中的任何条目可高亮显示模型中的对应模块。

### **Sample time** — 采样时间 `-1`（默认）| 标量 | 向量

采样时间，用于控制模块何时从数据存储读取。值 `-1` 表示采样时间被继承。有关详细信息，请参阅 Specify Sample Time。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：string | character vector |
| **值**：标量 | 向量 |
| **默认值**：`'-1'` |

### 元素选择

### **Elements in the array (Signals in the bus)** — 关联数据存储中的元素 character vector

关联数据存储中的元素列表。对于包含数组的数据存储，您可以读取整个数据存储，也可以指定数据存储的一个或多个元素。对于具有总线数据类型的数据存储，您可以展开树以查看和选择总线元素。该列表在括号中显示每个元素的最大维度。

如果未选择**启用索引**，请选择一个元素并使用以下方法之一：

- 单击 **Select>>** 以在 **Selected element(s)** 列表中显示该元素及其所有子元素。
- 使用 **Specify element(s) to select** 编辑框指定要选择读取的子元素。然后单击 **Select>>**。

要选择多个元素，请对每个元素重复上述过程。

或者，您可以选择**启用索引**，然后选择单个元素并使用**索引选项**参数动态指定子元素。

要刷新显示并反映对数据存储中使用的数组或总线所做的修改，请单击 **Refresh**。

#### 依赖

此部分的提示（**Elements in the array** 或 **Signals in the bus**）取决于数据存储中的数据类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`DataStoreElements` |
| **类型**：string | character vector |
| **值**：以井号分隔的元素列表（参见 Specification using the command line。） |
| **默认值**：`''` |

### **Specify element(s) to select** — 定义要选择的元素的 MATLAB 表达式 character vector

输入 MATLAB 表达式以定义要读取的特定元素，然后单击 **Select>>** 将该元素添加到 **Selected elements(s)** 表。重复此操作以选择其他元素。

例如，对于最大维度为 `[3,5]` 的名为 `DSM` 的数据存储，您可以在编辑框中输入诸如 `DSM(2,4)` 或 `DSM([1 3],2)` 之类的表达式。请参阅 Accessing Specific Bus and Matrix Elements。

要应用元素选择，请单击 **OK** 或 **Apply**。

#### 依赖

**Specify element(s) to select** 编辑框仅在未选择**启用索引**时出现。

#### 编程使用

|  |
| --- |
| **模块参数**：`DataStoreElements` |
| **类型**：string | character vector |
| **值**：以井号分隔的元素列表（参见 Specification using the command line。） |
| **默认值**：`''` |

### **Selected element(s)** — 选定元素列表 character vector

您从数据存储中选择的元素。Data Store Read 模块图标为您指定的每个元素显示一个输出端口。

要更改列表中总线或矩阵元素的顺序，请在列表中选择该元素，然后单击 **Up** 或 **Down**。更改列表中元素的顺序会更改端口的顺序。要移除元素，请单击 **Remove**。

#### 依赖

**Selected element(s)** 表仅在未选择**启用索引**时出现。

#### 编程使用

|  |
| --- |
| **模块参数**：`DataStoreElements` |
| **类型**：string | character vector |
| **值**：以井号分隔的元素列表（参见 Specification using the command line。） |
| **默认值**：`''` |

### **Enable indexing** — 启用索引以指定要读取的数据存储元素的子元素 `off`（默认）| `on`

选择此参数以启用类似于 Selector 模块所使用的索引，由此您可以通过使用一个或多个索引输入端口动态指定要读取的子元素的索引，也可以通过使用模块对话框指定索引。选择此参数时，Data Store Read 模块只能从数据存储的单个元素（即总线中的单个信号）读取。要使用动态索引从数据存储的多个元素读取，请使用多个 Data Store Read 模块。

清除此参数以禁用 Selector 模块风格的索引。您可以选择多个要读取的数据存储元素，但只能通过使用模块对话框指定要读取哪些子元素。

**注意**

如果关联的数据存储仅包含单个标量元素，请勿选择**启用索引**。

#### 编程使用

|  |
| --- |
| **模块参数**：`EnableIndexing` |
| **类型**：string | character vector |
| **值**：`"off"` | `"on"` |
| **默认值**：`"off"` |

### **Number of dimensions** — 数据存储元素的维度数 `1`（默认）| 正整数

选定数据存储元素的维度数。您必须明确指示此数字。

#### 依赖

此参数仅在选择了**启用索引**时启用。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberOfDimensions` |
| **类型**：string | character vector |
| **值**：正整数 |
| **默认值**：`'1'` |

### **Index mode** — 索引模式 `One-based`（默认）| `Zero-based`

选择索引模式。如果选择 `One-based`，则索引 `1` 指定输入向量的第一个元素。如果选择 `Zero-based`，则索引 `0` 指定输入向量的第一个元素。

#### 依赖

要启用此参数，请选择**启用索引**。

#### 编程使用

|  |
| --- |
| **参数：** `IndexMode` |
| **类型：** string | character vector |
| **值：** `"Zero-based"` | `"One-based"` |
| **默认值：** `'One-based'` |

### **Index Option** — 子元素的索引方法 `Index vector (dialog)`（默认）| `Select all` | `Index vector (port)` | `Starting index (dialog)` | `Starting index (port)`

按维度定义如何对选定数据存储元素的子元素进行索引。从列表中选择：

| 菜单项 | 操作 |
| --- | --- |
| `Select all` | 读取所有子元素。 |
| `Index vector (dialog)` | 启用 **Index** 列。输入包含要读取的子元素索引的向量。 |
| `Index vector (port)` | 相关索引端口定义要读取的子元素的索引。 |
| `Starting index (dialog)` | 启用 **Index** 和 **Output Size** 列。输入要读取的子元素范围的起始索引和大小。 |
| `Starting index (port)` | 启用 **Output Size** 列。相关索引端口定义要读取的元素范围的起始索引。输入范围的大小。 |

**Index** 和 **Output Size** 列在相关时显示。

#### 依赖

要启用此参数，请选择**启用索引**。

#### 编程使用

|  |
| --- |
| **参数：** `IndexOptionArray` |
| **类型：** string | character vector |
| **值：** `"Select all"` | `"Index vector (dialog)"` | `"Index vector (port)"` | `"Starting index (dialog)"` | `"Starting index (port)"` |
| **默认值：** `'Index vector (dialog)'` |

### **Index** — 子元素的索引或起始索引 `1`（默认）| 整数 | 整数向量

如果**索引选项**为 `Index vector (dialog)`，请输入包含要读取的每个子元素索引的向量。

如果**索引选项**为 `Starting index (dialog)`，请输入要读取的子元素范围的起始索引。

#### 依赖

要启用此参数，请选择**启用索引**，并将该维度的**索引选项**设置为 `Index vector (dialog)` 或 `Starting index (dialog)`。

#### 编程使用

|  |
| --- |
| **参数：** `IndexParamArray` |
| **类型：** character vector |
| **值：** cell array |
| **默认值：** `'{ }'` |

### **Output Size** — 要读取的子元素范围的大小 `1`（默认）| 整数

如果**索引选项**为 `Starting index (dialog)` 或 `Starting index (port)`，请输入要读取的子元素范围的大小。

#### 依赖

要启用此参数，请选择**启用索引**，并将该维度的**索引选项**设置为 `Starting index (dialog)` 或 `Starting index (port)`。

#### 编程使用

|  |
| --- |
| **模块参数：** `OutputSizeArray` |
| **类型：** character vector |
| **值：** cell array |
| **默认值：** `'{ }'` |

## 所属库

Simulink / Signal Routing

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

### R2024a：Data Store Read 模块支持符号索引的索引功能

当 Data Store Memory 模块使用符号维度时，Data Store Read 模块现在支持索引。

## 描述

从数据存储读取数据

Data Store Read 模块将数据从指定的数据存储或其选定部分复制到其输出。多个 Data Store Read 模块可以从同一数据存储读取。

读取数据的数据存储由定义该数据存储的 Data Store Memory 模块或信号对象的位置决定。有关详细信息，请参阅 Data Stores and Data Store Memory。

从数据存储获得正确结果需要确保数据存储的读取和写入按预期顺序发生。有关详细信息，请参阅 Order Data Store Access and Data Store Diagnostics。

您可以选择 Data Store Read、Data Store Write 或 Data Store Memory 模块以高亮显示与其相关的模块。要在打开的图或新选项卡中显示相关模块，请暂停在选中后出现的省略号上。然后，从操作栏中选择 Related Blocks。当多个模块与所选模块对应时，将打开相关模块列表。您可以通过在文本框中输入搜索词来筛选相关模块列表。从列表中选择相关模块后，窗口焦点将转到显示相关模块的打开图或新选项卡。

当 Data Store Read 模块从 **Dimensions** 参数值设置为 `Inf` 的 Data Store Memory 模块读取时，不支持**元素选择**选项卡。换言之，Data Store Read 模块从数据存储读取无界可变大小信号。
