---
type: simulink-block
title: 'C Function'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'cfunction'
documentation_source_path: 'slref/cfunction.html'
language: zh-CN
chinese_source: worker-translation
---

# C Function

## 端口

### 输入

### **Port\_1** — 输入端口 标量 | 向量 | 矩阵

输入端口数量由模块参数对话框中 **Symbols** 表格中定义的具有 `Input` 或 `InputOutput` 作用域的符号数量决定。每个输入端口的标签与 `Input` 或 `InputOutput` 符号的名称相同，除非您通过编辑模块对话框 **Symbols** 表格中的 **Label** 字段来更改它。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `enumerated` | `bus` | `fixedpoint`
### 输出

### **Port\_1** — 输出端口 标量 | 向量 | 矩阵

输出端口数量由模块参数对话框中 **Symbols** 表格中定义的具有 `Output` 或 `InputOutput` 作用域的符号数量决定。每个输出端口的标签与 `Output` 或 `InputOutput` 符号的名称相同，除非您通过编辑模块对话框 **Symbols** 表格中的 **Label** 字段来更改它。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `enumerated` | `bus` | `fixedpoint`

## 参数

**Simulation** 和 **Code Generation** 选项卡共有的参数。

### **Configure custom code settings** — 用于指定自定义代码位置的选项 按钮

使用 Configure Custom Code settings 按钮 C Function 模块齿轮图标。来选择是在模块中本地指定自定义代码，还是在 Configuration Parameters 对话框中指定。点击 C Function 模块齿轮图标旁的箭头。图标以选择选项：

- **使用模块自定义代码**

  使用此选项在 C Function 模块中本地指定自定义代码。此设置为默认值。此选项分别启用 **Simulation** 部分中的 **Simulation Custom Code** 和 **Code Generation Custom Code** 参数以及 **Code generation** 部分中的相应参数。

  从 R2025a 开始，本地指定的自定义代码支持代码覆盖率。要使用代码覆盖率，您必须拥有 Simulink Coverage 许可证。
- **Use Configuration Parameters Custom Code**

  使用此选项在模型 Configuration Parameters 对话框的 **Simulation Target** 窗格中指定自定义代码。有关详细信息，请参阅 Model Configuration Parameters: Simulation Target。

#### 编程使用

|  |
| --- |
| **模块参数**：`CustomCodeSettingLocation` |
| **类型**：character vector |
| **Value:**`'BlockSettings'` | `'ModelConfigurationParameters'` |
| **默认值**：`'BlockSettings'` |

### **Port and Parameter Symbols** — 符号和符号属性表

C 代码中使用的符号和符号属性，以表格形式指定。您必须在表格中输入每个符号的以下属性：

- **Name** — 代码中的符号名称。

  如果符号表示 C++ 类对象，则 **Name** 字段用作类构造函数的调用：

  ```
  ObjectName(Argument1,Argument2,...)
  ```
- **Scope** — 符号的作用域。可用的作用域有：

  - `Input` — 模块的输入。
  - `Output` — 模块的输出。
  - `InputOutput` — 模块的输入和输出。

    使用 `InputOutput` 作用域来映射 C 代码中通过指针传递的输入。使用 `InputOutput` 作用域创建的端口具有相同的输入和输出端口名称。`InputOutput` 作用域支持输入和输出端口的缓冲区重用。缓冲区重用可以优化内存使用并提高代码仿真和代码生成效率，具体取决于信号大小和模块布局。限制包括：

    - `InputOutput` 符号不能用于 **Start**、**Initialize Conditions** 或 **Terminate**。
    - `InputOutput` 符号不支持 `void*` 数据类型。
    - `InputOutput` 符号不支持 `size()` 表达式。
  - `Parameter` — 出现在模块参数掩码上的模块参数。参数名称由符号的 **Label** 定义。
  - `Persistent` — 持久性模块数据，在仿真期间从一个时间步保留其值到下一个时间步。

    您可以使用 `Persistent` 作用域定义 void 指针。*void 指针*是一种可以存储您创建或分配的任何类型数据的指针。

    您可以通过定义具有 `Persistent` 作用域的符号并使用 `Class:`*`ClassName`* 作为符号的 **Type** 来实例化自定义代码中定义的 C++ 类的对象。请参阅 Interface with C++ Classes Using C Function Block。
  - `Constant` — 常量值，使用值-大小或数值表达式定义。
- **Label** — 符号的标签。对于具有 `Input`、`InputOutput` 或 `Output` 作用域的符号，标签显示为模块上的端口名称。对于具有 `Parameter` 作用域的符号，标签显示在模块参数掩码上。如果作用域为 `Constant`，则标签为常量表达式。您不能为 `Persistent` 作用域符号定义标签。
- **Type** — 符号的数据类型。从下拉列表中选择数据类型或指定自定义数据类型。

  **注意**

  从 R2025a 开始，模块支持 `Input`、`Output`、`InputOutput` 和 `Persistent` 作用域的 Simulink 字符串类型。

  支持自定义代码中定义的 C++ 类类型，以及 `Simulink.Bus`、Simulink Enum 和 `Simulink.AliasType` 类型。按下表所示输入 **Type**。

  | 自定义类型 | **Type** 字段中的指定方式 |
  | --- | --- |
  | C++ class | `Class:`*`C++ClassName`* |
  | `Simulink.Bus` | `Bus:`*`BusTypeName`* |
  | `Simulink.Enum` | `Enum:`*`EnumTypeName`* |
  | `Simulink.AliasType` | *`AliasTypeName`* |
- **Size** — 符号数据的大小。您可以使用大小表达式来定义输出的大小，或使用 `-1` 来继承大小。
- **Port** — 符号的端口索引。对于 `Input`、`InputOutput` 或 `Output` 符号，**Port** 指定对应于该符号的一个或多个端口在模块上的端口索引。对于 `Parameter` 符号，**Port** 指定该符号在模块参数掩码中出现的顺序。

#### 编程使用

|  |
| --- |
| **模块参数**：`SymbolSpec` |
| **类型**：`SymbolSpec` object |
| **Value:** `SymbolSpec` object |
| **默认值**：Empty array of `Symbol` objects |

### **Sample time** — 采样周期 `-1`（默认）| 标量 | 向量

采样周期，以秒为单位指定。请参阅 Types of Sample Time 和 Specify Sample Time。如果模块定义了持久性符号，则不能指定连续采样时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：string scalar or character vector |
| **默认值**：`"-1"` |

### **Block specified custom code supports multiple instances** — 用于在多个 C Function 模块中本地指定相同自定义代码的选项 `off`（默认）| `on`

*自 R2024a 起*

如果相同的自定义代码可以在模型中的多个 C Function 模块中本地指定而模块之间不会相互干扰，请选择此选项。例如，如果您使用包含内部状态的数学计数器，代码的多个实例可能会相互干扰。

当您选择此选项时，支持以下建模场景：

- 在 C Function 模块中本地指定自定义代码，并在 For Each 子系统内使用该模块。
- 在 C Function 模块中本地指定使用连续采样时间的自定义代码。
- 为相同自定义代码的多个实例生成代码，其中代码的每个实例在模型中的 C Function 模块中本地指定。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程使用

|  |
| --- |
| **模块参数**：`CustomCodeIsMultiInstantiable` |
| **类型**：string scalar or character vector |
| **默认值**：`'off'` |

### 仿真

### **Output** — 输出代码 无默认值

模块在仿真期间每个时间步执行的输出代码，以字符向量或字符串标量指定。例如，使用此参数从外部 C 代码调用函数、修改结果，并执行操作将结果传递给其他模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputCode` |
| **类型**：character vector or string scalar |
| **Value:** `""` | `C/C++ code` |
| **默认值**：`""` |

### **Start** — 初始化代码 无默认值

模块在仿真开始时执行一次的初始化代码。例如，使用此参数初始化持久性符号。

#### 编程使用

|  |
| --- |
| **模块参数**：`StartCode` |
| **类型**：character vector or string scalar |
| **Value:** `""` | `C/C++ code` |
| **默认值**：`""` |

### **Initialize Conditions** — 重新初始化代码 无默认值

模块在启用包含该模块的子系统或模型时执行的重新初始化代码。该代码在仿真开始时执行一次。如果模块位于包含 Enable 模块且 **States when enabling** 参数设置为 `reset` 的子系统或模型中，则每次子系统或模型从禁用切换到启用时，该代码也会执行。请参阅 Using Enabled Subsystems。例如，您可以使用此代码设置初始输出值或重置持久性变量的值。

#### 编程使用

|  |
| --- |
| **模块参数**：`InitializeConditionsCode` |
| **类型**：character vector or string scalar |
| **Value:** `""` | `C/C++ code` |
| **默认值**：`""` |

### **Terminate** — 终止代码 无默认值

模块在仿真结束时执行一次的终止代码。例如，使用此代码释放缓存在指定为 void 指针的持久性符号上的内存。

#### 编程使用

|  |
| --- |
| **模块参数**：`TerminateCode` |
| **类型**：character vector or string scalar |
| **Value:** `""` | `C/C++ code` |
| **默认值**：`""` |

### **Headers** — 本地指定自定义代码的头文件 无默认值

本地指定自定义代码的头文件。此参数位于 **Simulation Custom Code** 部分。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程使用

|  |
| --- |
| **模块参数**：`SimCustomHeaderFile` |
| **类型**：character vector or string scalar |
| **Value:** header file names or #include statements |
| **默认值**：`""` |

### **Sources** — 本地指定自定义代码的源文件 无默认值

本地指定自定义代码的源文件。此参数位于 **Simulation Custom Code** 部分。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程使用

|  |
| --- |
| **模块参数**：`SimCustomSourceFile` |
| **类型**：character vector or string scalar |
| **Value:** any file name |
| **默认值**：`""` |

### **Libraries** — 本地指定静态或共享库列表 无默认值

本地指定静态或共享库列表。此参数位于 **Simulation Custom Code** 部分。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程使用

|  |
| --- |
| **模块参数**：`SimCustomLibraries` |
| **类型**：character vector or string scalar |
| **Value:** any library file name |
| **默认值**：`""` |

### **Search Directories** — 本地指定包含自定义代码头文件和源文件的目录 无默认值

本地指定包含自定义代码头文件和源文件的目录。此参数在 **Simulation Custom Code** 部分中可用。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程使用

|  |
| --- |
| **模块参数**：`SimCustomSearchDirectory` |
| **类型**：character vector or string scalar |
| **Value:** any folder path |
| **默认值**：`""` |

### **Defines** — 本地指定要添加到编译器命令行的预处理器宏定义 无默认值

本地指定要添加到编译器命令行的预处理器宏定义。此参数在 **Simulation Custom Code** 部分的 **Advanced** 选项卡中可用。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程使用

|  |
| --- |
| **模块参数**：`SimCustomDefines` |
| **类型**：character vector |
| **Value:** preprocessor macro definition |
| **默认值**：`''` |

### **Compiler Flags** — 本地指定要添加到编译器命令行的附加标志 无默认值

本地指定要添加到编译器命令行的附加标志。此参数在 **Simulation Custom Code** 部分的 **Advanced** 选项卡中可用。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程使用

|  |
| --- |
| **模块参数**：`SimCustomCompilerFlags` |
| **类型**：character vector |
| **Value:** compiler flags |
| **默认值**：`''` |

### **Linker Flags** — 本地指定要添加到链接器命令行的附加标志 无默认值

本地指定要添加到链接器命令行的附加标志。此参数在 **Simulation Custom Code** 部分的 **Advanced** 选项卡中可用。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程使用

|  |
| --- |
| **模块参数**：`SimCustomLinkerFlags` |
| **类型**：character vector |
| **Value:** linker flags |
| **默认值**：`''` |

### Code generation

**Code generation** 选项卡上的参数需要 Simulink Coder™ 或 Embedded Coder® 许可证。

### **Use same code as simulation** — 用于为仿真和代码生成使用相同或不同代码的选项 `on`（默认）| `off`

指定是为仿真和代码生成使用相同还是不同的代码。默认情况下，此选项被选中，模块为仿真和代码生成使用相同的代码。清除此选项可为仿真和代码生成使用不同的代码。

#### 编程使用

|  |
| --- |
| **模块参数**：`CodegenUsesSimCustomCode` |
| **类型**：string scalar or character vector |
| **默认值**：`'on'` |

### **Generate code as - is (optimizations off)** — 用于允许对代码生成代码进行解析的选项 `on`（默认）| `off`

指定是否允许对代码生成代码进行解析。默认情况下，此选项被选中，模块将您的代码嵌入生成的代码中而不进行解析。清除此选项可使模块分析代码并报告任何错误。

当您为仿真和代码生成使用不同的代码时，此参数使用其默认设置。

#### 依赖关系

此选项仅在 **Use same code as simulation** 参数被选中时才可选择。

#### 编程使用

|  |
| --- |
| **模块参数**：`GenerateCodeAsIs` |
| **类型**：string scalar or character vector |
| **默认值**：`'on'` |

### **Output** — 输出代码 无值

模块在代码生成期间每个时间步执行的输出代码。例如，使用此参数从外部 C/C++ 代码调用函数、修改结果，并执行操作将结果传递给其他模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`CodegenOutputCode` |
| **类型**：character vector or string scalar |
| **Value:** `""` | `C/C++ code` |
| **默认值**：`""` |

### **Start** — 初始化代码 无默认值

模块在代码生成开始时执行一次的初始化代码。例如，使用此参数初始化持久符号。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CodegenStartCode` |
| **类型：** 字符向量或字符串标量 |
| **值：** `""` | `C/C++ code` |
| **默认值：** `""` |

### **Initialize Conditions** — 重新初始化代码 无默认值

当启用模块所在的子系统或模型时，模块执行的重新初始化代码。该代码在代码生成开始时执行一次。如果模块位于子系统内或位于包含 Enable 模块的模型中，且该 Enable 模块的 **States when enabling** 参数设置为 `reset`，则该代码还会在子系统或模型每次从禁用切换到启用时执行。请参阅 Using Enabled Subsystems。例如，您可以使用此代码设置初始输出值或重置持久变量的值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CodegenInitializeConditionsCode` |
| **类型：** 字符向量或字符串标量 |
| **值：** `""` | `C/C++ code` |
| **默认值：** `""` |

### **Terminate** — 终止代码 无默认值

模块在代码生成结束时执行一次的终止代码，指定为字符向量或字符串标量。例如，使用此代码释放缓存在指定为 void 指针的持久符号上的内存。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CodegenTerminateCode` |
| **类型：** 字符向量或字符串标量 |
| **值：** `""` | `C/C++ code` |
| **默认值：** `""` |

### **Headers** — 本地指定自定义代码的头文件 无默认值

本地指定自定义代码的头文件。此参数位于 **Code Generation Custom Code** 部分。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CustomHeaderFile` |
| **类型：** 字符向量或字符串标量 |
| **值：** 头文件名或 #include 语句 |
| **默认值：** `""` |

### **Sources** — 本地指定自定义代码的源文件 无默认值

本地指定自定义代码的源文件。此参数位于 **Code Generation Custom Code** 部分。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CustomSourceFile` |
| **类型：** 字符向量或字符串标量 |
| **值：** 任意文件名 |
| **默认值：** `""` |

### **Libraries** — 本地指定静态库或共享库的列表 无默认值

本地指定静态库或共享库的列表。此参数位于 **Code Generation Custom Code** 部分。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 程序化使用

|  |
| --- |
| **模块参数：**`CustomLibraries` |
| **类型：** 字符向量或字符串标量 |
| **值：** 任意库文件名 |
| **默认值：** `""` |

### **Search Directories** — 本地指定包含自定义代码头文件和源文件的目录 无默认值

本地指定包含自定义代码头文件和源文件的目录。此参数位于 **Code Generation Custom Code** 部分。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 程序化使用

|  |
| --- |
| **模块参数：**`CustomSearchDirectory` |
| **类型：** 字符向量或字符串标量 |
| **值：** 任意文件夹路径 |
| **默认值：** `""` |

### **Defines** — 本地指定要添加到编译器命令行的预处理器宏定义 无默认值

本地指定要添加到编译器命令行的预处理器宏定义。此参数位于 **Code Generation Custom Code** 部分的 **Advanced** 选项卡中。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CustomDefines` |
| **类型：** 字符向量 |
| **值：** 预处理器宏定义 |
| **默认值：** `''` |

### **Compiler Flags** — 向编译器命令行添加额外标志 无默认值

向编译器命令行添加额外标志。此参数位于 **Code Generation Custom Code** 部分的 **Advanced** 选项卡中。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CustomCompilerFlags` |
| **类型：** 字符向量 |
| **值：** 编译器标志 |
| **默认值：** `''` |

### **Linker Flags** — 向链接器命令行添加额外标志 无默认值

向链接器命令行添加额外标志。此参数位于 **Code Generation Custom Code** 部分的 **Advanced** 选项卡中。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CustomLinkerFlags` |
| **类型：** 字符向量 |
| **值：** 链接器标志 |
| **默认值：** `''` |

## 所属库

Simulink / User-Defined Functions

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `integera` | `singlea` | `stringa` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 实际数据类型或功能支持取决于模块实现。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际数据类型或功能支持取决于模块实现。

## 版本历史

**在 R2020a 中引入**

### R2025a：与函数接口和自定义代码覆盖率相关的增强

- C Function 模块现在支持 `Input`、`Output`、`InputOutput` 和 `Persistent` 作用域的 Simulink 字符串类型。
- 您现在可以调用字符串库函数的子集。有关支持的字符串库函数的更多信息，请参阅 Call C Library Functions。
- 现在支持本地指定的自定义代码的代码覆盖率。要在模块对话框中本地指定自定义代码，请使用 **Use Block Custom Code** 参数。有关更多信息，请参阅 **Configure custom code settings**。

### R2024a：C Function 模块对话框和参数名称的更改

对模块对话框和参数进行了以下更改：

- 模块对话框有两个新选项卡：**Simulation** 和 **Code generation**。
- **Output code**、**Start code**、**Initialize conditions code** 和 **Terminate code** 参数现在分别称为 **Output**、**Start**、**Initialize code** 和 **Terminate**。
- Configure custom code settings C Function 模块齿轮图标。按钮列出了两个下拉选项：**Use Block Custom Code** 和 **Use Configuration Parameters Custom Code**。使用这些选项可以指定是在模块参数对话框中本地指定自定义代码，还是使用配置参数对话框将自定义代码集成到 Simulink 中。
- **Symbols** 表现在是 **Ports and Parameters** 表。
- **Symbols** 表中的 **Size** 列现在是 **Ports and Parameters** 表中的 **Dimensions** 列。

### R2024a：与自定义代码指定相关的增强

- 您现在可以为代码生成指定与仿真所用代码不同的目标特定代码。为此，请使用 **Simulation** 和 **Code generation** 部分中的参数。
- 您可以使用 **Simulation Custom Code** 和 **Code Generation Custom Code** 部分中的参数分别指定用于仿真和代码生成的自定义代码。使用这些参数在本地指定自定义代码，并且仅指定特定 C Function 模块所需的代码。
- 您可以将自定义代码嵌入生成的代码中而无需解析（请参阅 **Generate code as-is (optimizations off)**）。此增强扩展了 C Function 模块的功能，允许您使用与桌面 MEX 编译器不兼容的自定义 C 代码。
- 在自定义代码中使用 `slError` 和 `slWarning` 消息分别报告错误和警告消息。
- 在自定义代码中使用 `slSetRowMajor` 和 `slSetColumnMajor` 函数分别指定行主序和列主序数组布局。

### R2023a：支持 `printf`、`memcpy` 和 `memset` C 库函数

您可以在 C Function 模块的 **Start**、**Initialize Conditions** 和 **Terminate** 代码中使用 `printf`、`memcpy` 和 `memset` 函数。

## 描述

从 Simulink 模型集成和调用外部 C/C++ 代码

C Function 模块从 Simulink® 模型集成和调用外部 C/C++ 代码。使用此模块可以定义外部代码，并通过预处理或后处理数据来自定义代码的集成。此外，您可以为仿真和 C 代码生成指定自定义代码。您可以有条件地调用代码中定义的函数，也可以在一个模块中调用多个函数。使用此模块，您可以初始化持久数据并将其传递给外部函数。

C Function 模块支持从模块对话框初始化持久数据和调用外部函数。持久数据可以包括自定义代码中定义的 C++ 类对象。请参阅 Interface with C++ Classes Using C Function Block。该模块仅支持初始化和终止持久数据。该模块不支持在仿真期间更新数据。要对具有连续状态的动态系统进行建模，请使用 S-Function 模块。要了解有关 S-Function 的更多信息，请参阅 What Is an S-Function?

**注意**

C99 是支持将自定义 C 代码集成到 Simulink 中的 C 语言标准版本。

### 指定自定义代码

*自 R2024a 起*

从 R2024a 开始，该模块为您提供了一系列选项来为模块指定自定义 C/C++ 代码。

- 您可以在模块中本地指定自定义代码，从而集成完全包含在单个模块中的代码组件。例如，如果您希望 C Function 模块像使用外部 C/C++ 代码定义的自定义滤波器一样工作，请在模块中本地指定自定义代码。
- 您可以与模型中的其他模块或多个模型共享自定义代码。要在多个模型之间共享自定义代码，必须在 Simulink 库模型的配置参数对话框中定义自定义代码。然后，在库中的模块中使用该代码，并在其他模型中从该库获取该模块。

有关更多信息，请参阅 **Configure custom code settings**。

### 调用 C 库函数

您可以直接从 C Function 模块调用以下 C 数学库函数。

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| `abs` | `acos` | `asin` | `atan` | `atan2` | `ceil` |
| `cos` | `cosh` | `exp` | `fabs` | `floor` | `fmod` |
| `labs` | `ldexp` | `log` | `log10` | `pow` | `sin` |
| `sinh` | `sqrt` | `tan` | `tanh` |  |  |

调用这些函数时，除非所有输入参数都显式为单精度，否则适用双精度。当发生类型不匹配时，将输入参数强制转换为预期类型以替换原始参数。例如，如果使用整数参数调用 `sin` 函数，则将输入参数强制转换为 `double` 类型的浮点数以替换原始参数。

从 R2025a 开始，您可以在 C Function 模块内调用以下字符串库函数。

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| `strlen` | `strncpy` | `strncat` | `strcmp` | `strncmp` | `strstr` |

有关更多信息，请参阅 Use Simulink Strings inside C Function Block to Model Scrolling Display。

要调用其他 C 库函数，请创建并调用一个调用该 C 库函数的外部包装函数。

**调用 `abs`、`fabs` 和 `labs` 函数**

C Function 模块中对 `abs`、`fabs` 和 `labs` 函数的解释超出了标准 C 版本的范围，包括整数和浮点参数：

- 如果 `x` 是整数，则标准 C 函数 `abs` 应用于 `x`，即 `abs(x)`。
- 如果 `x` 是 double，则标准 C 函数 `labs` 应用于 `x`，即 `labs(x)`。
- 如果 `x` 是 single，则标准 C 函数 `fabs` 应用于 `x`，即 `fabs(x)`。

**基于类型的代码替换库（CRL）**

对函数的调用应根据传入函数的数据类型调用正确的 CRL。如果未指定 CRL，则对函数的调用应调用类型特定的库。C99 的 CRL 生成类型特定的函数。例如：

| 传入类型 | 代码生成调用 |
| --- | --- |
| `sin(doubleIn)` | `sin(doubleIn)` |
| `sin(floatIn)` | `sinf(floatIn)` |

您可以在 C Function 模块中调用 `printf`、`memcpy` 和 `memset` 函数。*（自 R2023a 起）*

### 在 Simulink 中报告运行时错误和警告

*自 R2024a 起*

在 C Function 模块中指定的自定义 C 代码中，使用 `slError` 和 `slWarning` 函数分别报告运行时错误和警告。错误会终止仿真，必须在仿真继续之前解决。警告表示代码存在潜在问题，但不会终止仿真。

`slError` 和 `slWarning` 函数都支持类似于 C 的不同数据类型格式说明符（例如，`%d` 用于整数，`%f` 用于浮点数）。

示例：

- `slError("Error message");`
- `slError("Input %f should be non-negative", x);`
- `slWarning("Warning message");`
- `slWarning("Input %d should be non-zero", y);`

以下代码在仿真开始时执行。如果数据存储在仿真开始时初始化失败，它将使用 `slError` 函数发出错误消息。

C Function 模块使用 slError 在仿真开始时报告错误消息。

### 在自定义代码中指定行主序和列主序数组布局

*自 R2024a 起*

使用 `slSetRowMajor` 和 `slSetColumnMajor` 函数分别指定行主序和列主序数组布局。在配置参数对话框的 **Simulation Target** 窗格中，通过模块对话框中的 **Use Configuration Parameters Custom Code** 参数指定这些函数。

对于行主序布局，矩阵的行元素在内存中连续存储。类似地，对于列主序布局，矩阵的列元素在内存中连续存储。有关详细信息，请参阅 Row-Major and Column-Major Array Layouts (MATLAB Coder)。

函数原型：

- `void slSetRowMajor(const char* functionName)`
- `void slSetColumnMajor(const char* functionName)`

`functionName` 必须是字符串字面量并且完全限定。

例如，考虑以下代码：

```
namespace NS1 {
	class ACLASS{
		public:
			void foo_row();
	};
	namespace NS2{
		void foo_col(double*, double*);
	}
}
```

对于完全限定的函数名。

- 如果函数位于命名空间内，则所有嵌套命名空间都应包含在函数名字符串中。基于上述代码，对于列主序函数 `foo_col`，在配置参数自定义代码中使用 `slSetColumnMajor("NS1::NS2::foo_col")`。
- 对于所有类成员，类名以及任何嵌套命名空间都应包含在函数名字符串中。基于上述代码，对于行主序函数 `foo_row`，在配置参数自定义代码中使用 `slSetRowMajor("NS1::ACLASS::foo_row")`。

对于使用类的 C Function 模块，如果构造函数采用 majority，则必须在 **Start** 代码中指定 majority。
