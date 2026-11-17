---
type: simulink-block
title: 'C Function'
family: 'user-defined-functions'
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

输入端口数量由模块参数对话框中 **符号** 表内定义的、作用域为 `Input` 或 `InputOutput` 的符号数量决定。除非您通过编辑模块对话框的 **符号** 表中的 **标签** 字段更改输入端口标签，否则每个输入端口标签都与 `Input` 或 `InputOutput` 符号的名称相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `enumerated` | `bus` | `fixedpoint`

### 输出

### **Port\_1** — 输出端口 标量 | 向量 | 矩阵

输出端口数量由模块参数对话框中 **符号** 表内定义的、作用域为 `Output` 或 `InputOutput` 的符号数量决定。除非您通过编辑模块对话框的 **符号** 表中的 **标签** 字段更改输出端口标签，否则每个输出端口标签都与 `Output` 或 `InputOutput` 符号的名称相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `enumerated` | `bus` | `fixedpoint`

## 参数

**仿真** 和 **代码生成** 选项卡共用的参数。

### **配置自定义代码设置** — 用于指定自定义代码位置的选项按钮

使用配置自定义代码设置按钮（C Function 模块齿轮图标）选择是在模块中本地指定自定义代码，还是在配置参数对话框中指定。单击 C Function 模块齿轮图标旁边的箭头图标以选择选项：

- **使用模块自定义代码**

  使用此选项在 C Function 模块中本地指定自定义代码。此设置为默认值。此选项分别在 **仿真** 部分和 **代码生成** 部分启用 **仿真自定义代码** 和 **代码生成自定义代码** 参数。

  从 R2025a 开始，本地指定的自定义代码支持代码覆盖率。要使用代码覆盖率，您必须具有 Simulink Coverage 许可证。
- **使用配置参数自定义代码**

  使用此选项在模型配置参数对话框的 **仿真目标** 窗格中指定自定义代码。有关详细信息，请参阅模型配置参数：仿真目标。

#### 编程用法

|  |
| --- |
| **模块参数：** `CustomCodeSettingLocation` |
| **类型：** character vector |
| **值：**`'BlockSettings'` | `'ModelConfigurationParameters'` |
| **默认值：** `'BlockSettings'` |

### **端口和参数符号** — 符号和符号属性表

C 代码中使用的符号和符号属性，指定为表。您必须在表中输入每个符号的以下属性：

- **名称** — 代码中的符号名称。

  如果符号表示 C++ 类对象，则 **名称** 字段用作对类构造函数的调用：

  ```
  ObjectName(Argument1,Argument2,...)
  ```
- **作用域** — 符号的作用域。可用的作用域包括：

  - `Input` — 模块的输入。
  - `Output` — 模块的输出。
  - `InputOutput` — 模块的输入和输出。

    使用 `InputOutput` 作用域映射 C 代码中通过指针传递的输入。使用 `InputOutput` 作用域创建的端口，其输入端口和输出端口具有相同名称。`InputOutput` 作用域可为输入端口和输出端口启用缓冲区重用。缓冲区重用可优化内存使用，并提高代码仿真和代码生成效率，具体取决于信号大小和模块布局。限制包括：

    - `InputOutput` 符号不能用于 **启动**、**初始化条件**或 **终止**。
    - `InputOutput` 符号不支持 `void*` 数据类型。
    - `InputOutput` 符号不支持 `size()` 表达式。
  - `Parameter` — 出现在模块参数掩码上的模块参数。参数名称由符号的 **标签** 定义。
  - `Persistent` — 持久模块数据，在仿真期间将其值从一个时间步保留到下一个时间步。

    您可以使用 `Persistent` 作用域定义 void 指针。*void 指针* 是一种指针，可存储您创建或分配的任何类型的数据。

    您可以通过定义具有 `Persistent` 作用域的符号，并使用 `Class:` *`ClassName`* 作为该符号的 **类型**，来实例化自定义代码中定义的 C++ 类对象。请参阅使用 C Function 模块与 C++ 类交互。
  - `Constant` — 常量值，使用值-大小或数值表达式定义。
- **标签** — 符号的标签。对于作用域为 `Input`、`InputOutput` 或 `Output` 的符号，标签在模块上显示为端口名称。对于作用域为 `Parameter` 的符号，标签显示在模块参数掩码上。如果作用域为 `Constant`，标签就是常量表达式。不能为 `Persistent` 作用域符号定义标签。
- **类型** — 符号的数据类型。从下拉列表中选择数据类型，或指定自定义数据类型。

  **注意**

  从 R2025a 开始，模块支持用于 `Input`、`Output`、`InputOutput` 和 `Persistent` 作用域的 Simulink strings 类型。

  支持自定义代码中定义的 C++ 类类型，也支持 `Simulink.Bus`、Simulink Enum 和 `Simulink.AliasType` 类型。按此表中所示输入 **类型**。

  | 自定义类型 | **类型**字段中的指定 |
  | --- | --- |
  | C++ class | `Class:`*`C++ClassName`* |
  | `Simulink.Bus` | `Bus:`*`BusTypeName`* |
  | `Simulink.Enum` | `Enum:`*`EnumTypeName`* |
  | `Simulink.AliasType` | *`AliasTypeName`* |
- **大小** — 符号数据的大小。您可以使用大小表达式定义输出的大小，或使用 `-1` 继承大小。
- **端口** — 符号的端口索引。对于 `Input`、`InputOutput` 或 `Output` 符号，**端口**指定模块上对应于该符号的一个或多个端口的端口索引。对于 `Parameter` 符号，**端口**指定该符号在模块参数掩码中出现的顺序。

#### 编程用法

|  |
| --- |
| **模块参数：** `SymbolSpec` |
| **类型：** `SymbolSpec` object |
| **值：** `SymbolSpec` object |
| **默认值：** `Symbol` 对象的空数组 |

### **采样时间** — 采样周期 `-1` (默认) | 标量 | 向量

采样周期，以秒为单位指定。请参阅采样时间类型和指定采样时间。如果模块定义了持久符号，则不能指定连续采样时间。

#### 编程用法

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：string scalar 或 character vector |
| **默认值**：`"-1"` |

### **模块指定的自定义代码支持多个实例** — 用于在多个 C Function 模块中本地指定相同自定义代码的选项 `off` (默认) | `on`

*自 R2024a 起*

如果可以在模型内的多个 C Function 模块中本地指定相同的自定义代码，而模块之间不会相互干扰，请选择此选项。例如，如果您使用包含内部状态的数学计数器，代码的多个实例可能会相互干扰。

选择此选项后，支持以下建模场景：

- 在 C Function 模块中本地指定自定义代码，并在 For Each 子系统内使用该模块。
- 在 C Function 模块中本地指定使用连续采样时间的自定义代码。
- 为相同自定义代码的多个实例生成代码，其中每个代码实例都在模型内的 C Function 模块中本地指定。

#### 依赖关系

要启用此参数，请将 **配置自定义代码设置** 参数设置为 `Use Block Custom Code`。

#### 编程用法

|  |
| --- |
| **模块参数**：`CustomCodeIsMultiInstantiable` |
| **类型**：string scalar 或 character vector |
| **默认值**：`'off'` |

### 仿真

### **输出** — 输出代码 无默认值

模块在仿真期间每个时间步执行的输出代码，指定为 character vector 或 string scalar。例如，使用此参数从外部 C 代码调用函数、修改结果，并执行操作以将结果传递给其他模块。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutputCode` |
| **类型：** character vector 或 string scalar |
| **值：** `""` | `C/C++ code` |
| **默认值：** `""` |

### **启动** — 初始化代码 无默认值

模块在仿真开始时执行一次的初始化代码。例如，使用此参数初始化持久符号。

#### 编程用法

|  |
| --- |
| **模块参数：** `StartCode` |
| **类型：** character vector 或 string scalar |
| **值：** `""` | `C/C++ code` |
| **默认值：** `""` |

### **初始化条件** — 重新初始化代码 无默认值

当启用包含该模块的子系统或模型时，模块执行的重新初始化代码。该代码在仿真开始时执行一次。如果模块位于子系统或模型中，且该子系统或模型包含一个 Enable 模块，其 **启用时的状态** 参数设置为 `reset`，则每次子系统或模型从禁用切换到启用时，代码也会执行。请参阅使用启用子系统。例如，您可以使用此代码设置初始输出值或重置持久变量的值。

#### 编程用法

|  |
| --- |
| **模块参数：** `InitializeConditionsCode` |
| **类型：** character vector 或 string scalar |
| **值：** `""` | `C/C++ code` |
| **默认值：** `""` |

### **终止** — 终止代码 无默认值

模块在仿真结束时执行一次的终止代码。例如，使用此代码释放缓存在指定为 void 指针的持久符号上的内存。

#### 编程用法

|  |
| --- |
| **模块参数：** `TerminateCode` |
| **类型：** character vector 或 string scalar |
| **值：** `""` | `C/C++ code` |
| **默认值：** `""` |

### **头文件** — 本地为自定义代码指定头文件 无默认值

本地为自定义代码指定头文件。此参数位于 **仿真自定义代码** 部分。

#### 依赖关系

要启用此参数，请将 **配置自定义代码设置** 参数设置为 `Use Block Custom Code`。

#### 编程用法

|  |
| --- |
| **模块参数：** `SimCustomHeaderFile` |
| **类型：** character vector 或 string scalar |
| **值：** 头文件名或 #include 语句 |
| **默认值：** `""` |

### **源文件** — 本地为自定义代码指定源文件 无默认值

本地为自定义代码指定源文件。此参数位于 **仿真自定义代码** 部分。

#### 依赖关系

要启用此参数，请将 **配置自定义代码设置** 参数设置为 `Use Block Custom Code`。

#### 编程用法

|  |
| --- |
| **模块参数：** `SimCustomSourceFile` |
| **类型：** character vector 或 string scalar |
| **值：** 任意文件名 |
| **默认值：** `""` |

### **库** — 本地指定静态库或共享库的列表 无默认值

本地指定静态库或共享库的列表。此参数位于 **仿真自定义代码** 部分。

#### 依赖关系

要启用此参数，请将 **配置自定义代码设置** 参数设置为 `Use Block Custom Code`。

#### 编程用法

|  |
| --- |
| **模块参数：** `SimCustomLibraries` |
| **类型：** character vector 或 string scalar |
| **值：** 任意库文件名 |
| **默认值：** `""` |

### **搜索目录** — 本地指定包含自定义代码头文件和源文件的目录 无默认值

本地指定包含自定义代码头文件和源文件的目录。此参数在 **仿真自定义代码** 部分中提供。

#### 依赖关系

要启用此参数，请将 **配置自定义代码设置** 参数设置为 `Use Block Custom Code`。

#### 编程用法

|  |
| --- |
| **模块参数：**`SimCustomSearchDirectory` |
| **类型：** character vector 或 string scalar |
| **值：** 任意文件夹路径 |
| **默认值：** `""` |

### **定义** — 本地指定要添加到编译器命令行的预处理器宏定义 无默认值

本地指定要添加到编译器命令行的预处理器宏定义。此参数在 **仿真自定义代码** 部分的 **高级** 选项卡中提供。

#### 依赖关系

要启用此参数，请将 **配置自定义代码设置** 参数设置为 `Use Block Custom Code`。

#### 编程用法

|  |
| --- |
| **模块参数：** `SimCustomDefines` |
| **类型：** character vector |
| **值：** 预处理器宏定义 |
| **默认值：** `''` |

### **编译器标志** — 本地指定要添加到编译器命令行的附加标志 无默认值

本地指定要添加到编译器命令行的附加标志。此参数在 **仿真自定义代码** 部分的 **高级** 选项卡中提供。

#### 依赖关系

要启用此参数，请将 **配置自定义代码设置** 参数设置为 `Use Block Custom Code`。

#### 编程用法

|  |
| --- |
| **模块参数：** `SimCustomCompilerFlags` |
| **类型：** character vector |
| **值：** 编译器标志 |
| **默认值：** `''` |

### **链接器标志** — 本地指定要添加到链接器命令行的附加标志 无默认值

本地指定要添加到链接器命令行的附加标志。此参数在 **仿真自定义代码** 部分的 **高级** 选项卡中提供。

#### 依赖关系

要启用此参数，请将 **配置自定义代码设置** 参数设置为 `Use Block Custom Code`。

#### 编程用法

|  |
| --- |
| **模块参数：** `SimCustomLinkerFlags` |
| **类型：** character vector |
| **值：** 链接器标志 |
| **默认值：** `''` |

### 代码生成

**代码生成** 选项卡上的参数需要 Simulink Coder™ 或 Embedded Coder® 许可证。

### **使用与仿真相同的代码** — 用于选择仿真和代码生成使用相同还是不同代码的选项 `on` (默认) | `off`

指定仿真和代码生成是使用相同代码还是不同代码。默认情况下，此选项处于选中状态，模块使用相同代码进行仿真和代码生成。清除此选项可使用不同代码进行仿真和代码生成。

#### 编程用法

|  |
| --- |
| **模块参数**：`CodegenUsesSimCustomCode` |
| **类型**：string scalar 或 character vector |
| **默认值**：`'on'` |

### **按原样生成代码（关闭优化）** — 用于允许对代码生成代码进行解析的选项 `on` (默认) | `off`

指定是否允许解析代码生成代码。默认情况下，此选项处于选中状态，模块将您的代码嵌入生成的代码中而不进行解析。清除此选项可使模块分析代码并报告任何错误。

当您对仿真和代码生成使用不同代码时，此参数使用其默认设置。

#### 依赖关系

仅当选中 **使用与仿真相同的代码** 参数时，才能选择此选项。

#### 编程用法

|  |
| --- |
| **模块参数**：`GenerateCodeAsIs` |
| **类型**：string scalar 或 character vector |
| **默认值**：`'on'` |

### **输出** — 输出代码 无值

模块在代码生成期间每个时间步执行的输出代码。例如，使用此参数从外部 C/C++ 代码调用函数、修改结果，并执行操作以将结果传递给其他模块。

#### 编程用法

|  |
| --- |
| **模块参数：** `CodegenOutputCode` |
| **类型：** character vector 或 string scalar |
| **值：** `""` | `C/C++ code` |
| **默认值：** `""` |

### **Start** — 初始化代码，无默认值

该模块在代码生成开始时执行一次的初始化代码。例如，使用此参数初始化持久符号。

#### 编程方式使用

|  |
| --- |
| **模块参数：** `CodegenStartCode` |
| **类型：** 字符向量或字符串标量 |
| **值：** `""` | `C/C++ code` |
| **默认值：** `""` |

### **Initialize Conditions** — 重新初始化代码，无默认值

模块在启用其中放置了该模块的子系统或模型时执行的重新初始化代码。该代码在代码生成开始时执行一次。如果该模块位于子系统内，或位于包含 Enable 模块且其 **States when enabling** 参数设置为 `reset` 的模型中，则该代码还会在子系统或模型每次从禁用切换到启用时执行。请参阅 Using Enabled Subsystems。例如，可以使用此代码设置初始输出值或重置持久变量的值。

#### 编程方式使用

|  |
| --- |
| **模块参数：** `CodegenInitializeConditionsCode` |
| **类型：** 字符向量或字符串标量 |
| **值：** `""` | `C/C++ code` |
| **默认值：** `""` |

### **Terminate** — 终止代码，无默认值

模块在代码生成结束时执行一次的终止代码，指定为字符向量或字符串标量。例如，使用此代码释放缓存在指定为 void 指针的持久符号上的内存。

#### 编程方式使用

|  |
| --- |
| **模块参数：** `CodegenTerminateCode` |
| **类型：** 字符向量或字符串标量 |
| **值：** `""` | `C/C++ code` |
| **默认值：** `""` |

### **Headers** — 局部指定用于自定义代码的头文件，无默认值

局部指定用于自定义代码的头文件。此参数位于 **Code Generation Custom Code** 节中。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程方式使用

|  |
| --- |
| **模块参数：** `CustomHeaderFile` |
| **类型：** 字符向量或字符串标量 |
| **值：** 头文件名或 #include 语句 |
| **默认值：** `""` |

### **Sources** — 局部指定用于自定义代码的源文件，无默认值

局部指定用于自定义代码的源文件。此参数位于 **Code Generation Custom Code** 节中。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程方式使用

|  |
| --- |
| **模块参数：** `CustomSourceFile` |
| **类型：** 字符向量或字符串标量 |
| **值：** 任意文件名 |
| **默认值：** `""` |

### **Libraries** — 局部指定静态库或共享库的列表，无默认值

局部指定静态库或共享库的列表。此参数位于 **Code Generation Custom Code** 节中。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程方式使用

|  |
| --- |
| **模块参数：**`CustomLibraries` |
| **类型：** 字符向量或字符串标量 |
| **值：** 任意库文件名 |
| **默认值：** `""` |

### **Search Directories** — 局部指定包含自定义代码头文件和源文件的目录，无默认值

局部指定包含自定义代码头文件和源文件的目录。此参数位于 **Code Generation Custom Code** 节中。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程方式使用

|  |
| --- |
| **模块参数：**`CustomSearchDirectory` |
| **类型：** 字符向量或字符串标量 |
| **值：** 任意文件夹路径 |
| **默认值：** `""` |

### **Defines** — 局部指定要添加到编译器命令行的预处理器宏定义，无默认值

局部指定要添加到编译器命令行的预处理器宏定义。此参数位于 **Code Generation Custom Code** 节中，在 **Advanced** 选项卡中。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程方式使用

|  |
| --- |
| **模块参数：** `CustomDefines` |
| **类型：** 字符向量 |
| **值：** 预处理器宏定义 |
| **默认值：** `''` |

### **Compiler Flags** — 向编译器命令行添加额外标志，无默认值

向编译器命令行添加额外标志。此参数位于 **Code Generation Custom Code** 节中，在 **Advanced** 选项卡中。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程方式使用

|  |
| --- |
| **模块参数：** `CustomCompilerFlags` |
| **类型：** 字符向量 |
| **值：** 编译器标志 |
| **默认值：** `''` |

### **Linker Flags** — 向链接器命令行添加额外标志，无默认值

向链接器命令行添加额外标志。此参数位于 **Code Generation Custom Code** 节中，在 **Advanced** 选项卡中。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程方式使用

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
| **零交叉检测** | `no` |
|  |  |
| --- | --- |
| a 实际数据类型或功能支持取决于模块实现。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际数据类型或功能支持取决于模块实现。

## 版本历史

**在 R2020a 中引入**

### R2025a：与函数接口和自定义代码覆盖率相关的增强功能

- C Function 模块现在支持用于 `Input`、`Output`、`InputOutput` 和 `Persistent` 作用域的 Simulink strings types。
- 现在可以调用字符串库函数的一个子集。有关支持的字符串库函数的详细信息，请参阅调用 C 库函数。
- 现在支持对局部指定的自定义代码进行代码覆盖率分析。要在模块对话框中局部指定自定义代码，请使用 **Use Block Custom Code** 参数。有关详细信息，请参阅 **Configure custom code settings**。

### R2024a：C Function 模块对话框和参数名称的更改

对模块对话框和参数进行了以下更改：

- 模块对话框有两个新选项卡：**Simulation** 和 **Code generation**。
- **Output code**、**Start code**、**Initialize conditions code** 和 **Terminate code** 参数现在分别称为 **Output**、**Start**、**Initialize code** 和 **Terminate**。
- C Function 模块的 Configure custom code settings 齿轮图标按钮列出两个下拉选项：**Use Block Custom Code** 和 **Use Configuration Parameters Custom Code**。使用这些选项可以指定是在模块参数对话框中局部指定自定义代码，还是使用配置参数对话框将自定义代码集成到 Simulink 中。
- **Symbols** 表现在是 **Ports and Parameters** 表。
- **Symbols** 表中的 **Size** 列现在是 **Ports and Parameters** 表中的 **Dimensions** 列。

### R2024a：与自定义代码指定相关的增强功能

- 现在可以为代码生成指定与仿真所用代码不同的目标特定代码。为此，请使用 **Simulation** 和 **Code generation** 节中的参数。
- 可以使用 **Simulation Custom Code** 和 **Code Generation Custom Code** 节中的参数，分别指定用于仿真和代码生成的自定义代码。使用这些参数可局部指定自定义代码，并只指定特定 C Function 模块所需的代码。
- 可以将自定义代码不经过解析直接嵌入生成的代码中（请参阅 **Generate code as - is (optimizations off)**）。此增强功能扩展了 C Function 模块的能力，允许您使用与桌面 MEX 编译器不兼容的自定义 C 代码。
- 在自定义代码中使用 `slError` 和 `slWarning` 消息分别报告错误和警告消息。
- 在自定义代码中使用 `slSetRowMajor` 和 `slSetColumnMajor` 函数分别指定行主序和列主序数组布局。

### R2023a：支持 `printf`、`memcpy` 和 `memset` C 库函数

可以在 C Function 模块的 **Start**、**Initialize Conditions** 和 **Terminate** 代码中使用 `printf`、`memcpy` 和 `memset` 函数。

## 描述

从 Simulink 模型中集成并调用外部 C/C++ 代码

C Function 模块从 Simulink® 模型中集成并调用外部 C/C++ 代码。使用此模块可以定义外部代码，并通过预处理或后处理数据来自定义代码的集成。此外，可以为仿真和 C 代码生成指定自定义代码。可以有条件地调用代码中定义的函数，还可以在一个模块中调用多个函数。使用此模块，可以初始化持久数据并将其传递给外部函数。

C Function 模块支持从模块对话框初始化持久数据并调用外部函数。持久数据可以包含在自定义代码中定义的 C++ 类对象。请参阅 Interface with C++ Classes Using C Function Block。该模块仅支持初始化和终止持久数据。该模块不支持在仿真期间更新数据。要对具有连续状态的动态系统建模，请使用 S-Function 模块。要了解有关 S-Function 的详细信息，请参阅 What Is an S-Function?

**注意**

C99 是支持将自定义 C 代码集成到 Simulink 中的 C 语言标准版本。

### 指定自定义代码

*自 R2024a 起*

从 R2024a 开始，该模块提供了一系列选项来为该模块指定自定义 C/C++ 代码。

- 可以在模块中局部指定自定义代码，因此可以集成完全包含在单个模块中的代码组件。例如，如果希望 C Function 模块的行为像使用外部 C/C++ 代码定义的自定义滤波器，请在模块中局部指定自定义代码。
- 可以将自定义代码与模型中的其他模块共享，或跨多个模型共享。要跨多个模型共享自定义代码，必须在 Simulink 库模型的配置参数对话框中定义自定义代码。然后，在库内的模块中使用该代码，并在其他模型中从该库获取该模块。

有关详细信息，请参阅 **Configure custom code settings**。

### 调用 C 库函数

可以直接从 C Function 模块调用以下 C 数学库函数。

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| `abs` | `acos` | `asin` | `atan` | `atan2` | `ceil` |
| `cos` | `cosh` | `exp` | `fabs` | `floor` | `fmod` |
| `labs` | `ldexp` | `log` | `log10` | `pow` | `sin` |
| `sinh` | `sqrt` | `tan` | `tanh` |  |  |

调用这些函数时，除非所有输入参数都显式为单精度，否则适用双精度。发生类型不匹配时，会将输入参数强制转换为预期类型，以替换原始参数。例如，如果使用整数参数调用 `sin` 函数，则会将输入参数强制转换为类型为 `double` 的浮点数，以替换原始参数。

从 R2025a 开始，可以在 C Function 模块内调用以下字符串库函数。

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| `strlen` | `strncpy` | `strncat` | `strcmp` | `strncmp` | `strstr` |

有关详细信息，请参阅 Use Simulink Strings inside C Function Block to Model Scrolling Display。

要调用其他 C 库函数，请创建并调用一个外部包装函数，由该函数调用 C 库函数。

**调用 `abs`、`fabs` 和 `labs` 函数**

C Function 模块中对 `abs`、`fabs` 和 `labs` 函数的解释超出了标准 C 版本，包含了整数和浮点参数：

- 如果 `x` 是整数，则标准 C 函数 `abs` 适用于 `x`，即 `abs(x)`。
- 如果 `x` 是 double，则标准 C 函数 `labs` 适用于 `x`，即 `labs(x)`。
- 如果 `x` 是 single，则标准 C 函数 `fabs` 适用于 `x`，即 `fabs(x)`。

**基于类型的代码替换库 (CRL)**

对函数的调用应根据传入函数的数据类型调用正确的 CRL。如果未指定 CRL，则该函数调用应调用类型特定的库。C99 的 CRL 会生成类型特定的函数。例如：

| Type passed in | Code generation call |
| --- | --- |
| `sin(doubleIn)` | `sin(doubleIn)` |
| `sin(floatIn)` | `sinf(floatIn)` |

可以在 C Function 模块中调用 `printf`、`memcpy` 和 `memset` 函数。*(自 R2023a 起)*

### 在 Simulink 中报告运行时错误和警告

*自 R2024a 起*

在 C Function 模块中指定的自定义 C 代码中，使用 `slError` 和 `slWarning` 函数分别报告运行时错误和警告。错误会终止仿真，必须先解决才能继续仿真。警告表示代码可能存在潜在问题，但不会终止仿真。

`slError` 和 `slWarning` 函数都支持与 C 类似的不同数据类型格式说明符（例如，`%d` 用于 integer，`%f` 用于 float）。

示例：

- `slError("Error message");`
- `slError("Input %f should be non-negative", x);`
- `slWarning("Warning message");`
- `slWarning("Input %d should be non-zero", y);`

以下代码在仿真开始时执行。如果数据存储在仿真开始时未能初始化，它会使用 `slError` 函数发出错误消息。

C Function 模块使用 slError 在仿真开始时报告错误消息。

### 在自定义代码中指定行主序和列主序数组布局

*自 R2024a 起*

使用 `slSetRowMajor` 和 `slSetColumnMajor` 函数分别指定行主序和列主序数组布局。使用模块对话框中的 **Use Configuration Parameters Custom Code** 参数，在配置参数对话框的 **Simulation Target** 窗格中指定这些函数。

对于行主序布局，矩阵的行元素连续存储在内存中。类似地，对于列主序布局，矩阵的列元素连续存储在内存中。有关详细信息，请参阅行主序和列主序数组布局 (MATLAB Coder)。

函数原型：

- `void slSetRowMajor(const char* functionName)`
- `void slSetColumnMajor(const char* functionName)`

`functionName` 必须是字符串字面量且完全限定。

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

- 如果函数位于命名空间内，则函数名字符串中应包含所有嵌套的命名空间。基于上述代码，对于列主序函数 `foo_col`，在配置参数自定义代码中使用 `slSetColumnMajor("NS1::NS2::foo_col")`。
- 对于所有类成员，函数名字符串中应包含类名以及任何嵌套的命名空间。基于上述代码，对于行主序函数 `foo_row`，在配置参数自定义代码中使用 `slSetRowMajor("NS1::ACLASS::foo_row")`。

对于使用类的 C Function 模块，如果构造函数采用 majority，则必须在 **Start** 代码中指定 majority。
