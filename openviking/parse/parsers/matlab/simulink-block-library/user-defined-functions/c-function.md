---
type: simulink-block
title: 'C Function'
family: user-defined-functions
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'cfunction'
---

# C Function

Integrate and call external C/C++ code from a Simulink model

## 中文

从 Simulink 模型集成并调用外部 C/C++ 代码

### 库

Simulink / User-Defined Functions

### 描述

C Function block 从 Simulink® 模型集成并调用外部 C/C++ 代码。使用此模块定义外部代码，并通过预处理或后处理数据来自定义代码集成。此外，您可以为仿真和 C 代码生成指定自定义代码。您可以有条件地调用代码中定义的函数，还可以在一个模块中调用多个函数。使用此模块，您可以初始化持久性数据并将其传递给外部函数。

C Function block 支持从模块对话框中初始化持久性数据并调用外部函数。持久性数据可以包括在自定义代码中定义的 C++ 类的对象。请参阅 Interface with C++ Classes Using C Function Block。该模块仅支持初始化和终止持久性数据。该模块不支持在仿真期间更新数据。要对具有连续状态的动态系统建模，请使用 S-Function block。要了解有关 S-function 的更多信息，请参阅 What Is an S-Function?。

**注意**

C99 是支持将自定义 C 代码集成到 Simulink 中的 C 语言标准版本。

#### 指定自定义代码

*自 R2024a 起*

从 R2024a 开始，该模块提供了一系列选项来为该模块指定自定义 C/C++ 代码。

- 您可以在模块本地指定自定义代码，从而集成完全包含在单个模块中的代码组件。例如，如果您希望 C Function block 的行为像使用外部 C/C++ 代码定义的自定义滤波器，请在模块本地指定自定义代码。
- 您可以将自定义代码与模型中的其他模块共享，或跨多个模型共享。要跨多个模型共享自定义代码，您必须在 Simulink 库模型的 Configuration Parameters 对话框中定义自定义代码。然后，在库中的模块内使用该代码，并在其他模型中从该库获取该模块。

有关详细信息，请参阅 **Configure custom code settings**。

#### 调用 C 库函数

您可以直接从 C Function block 调用这些 C Math Library 函数。

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| `abs` | `acos` | `asin` | `atan` | `atan2` | `ceil` |
| `cos` | `cosh` | `exp` | `fabs` | `floor` | `fmod` |
| `labs` | `ldexp` | `log` | `log10` | `pow` | `sin` |
| `sinh` | `sqrt` | `tan` | `tanh` |  |  |

当您调用这些函数时，除非所有输入参数都显式为单精度，否则适用双精度。当发生类型不匹配时，输入参数将被强制转换为预期类型，以替换原始参数。例如，如果您使用整数参数调用 `sin` 函数，则输入参数会被强制转换为类型为 `double` 的浮点数，以替换原始参数。

从 R2025a 开始，您可以在 C function block 内调用这些字符串库函数。

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| `strlen` | `strncpy` | `strncat` | `strcmp` | `strncmp` | `strstr` |

有关详细信息，请参阅 Use Simulink Strings inside C Function Block to Model Scrolling Display。

要调用其他 C 库函数，请创建并调用一个外部包装函数，该函数调用该 C 库函数。

**调用 `abs`、`fabs` 和 `labs` 函数**

C Function block 中对 `abs`、`fabs` 和 `labs` 函数的解释超出了标准 C 版本，包括整数和浮点参数：

- 如果 `x` 是整数，则标准 C 函数 `abs` 适用于 `x`，即 `abs(x)`。
- 如果 `x` 是 double，则标准 C 函数 `labs` 适用于 `x`，即 `labs(x)`。
- 如果 `x` 是 single，则标准 C 函数 `fabs` 适用于 `x`，即 `fabs(x)`。

**基于类型的 Code Replacement Library (CRL)**

对函数的调用应根据传入函数的数据类型调用正确的 CRL。如果未指定 CRL，则对函数的调用应调用类型特定的库。C99 的 CRL 会生成类型特定的函数。例如：

| 传入的类型 | 代码生成调用 |
| --- | --- |
| `sin(doubleIn)` | `sin(doubleIn)` |
| `sin(floatIn)` | `sinf(floatIn)` |

您可以在 C Function block 中调用 `printf`、`memcpy` 和 `memset` 函数。*（自 R2023a 起）*

#### 在 Simulink 中报告运行时错误和警告

*自 R2024a 起*

在您在 C Function block 中指定的自定义 C 代码中，使用 `slError` 和 `slWarning` 函数分别报告运行时错误和警告。错误会终止仿真，并且必须在仿真继续之前解决。警告表示代码可能存在潜在问题，但不会终止仿真。

`slError` 和 `slWarning` 函数都支持不同的数据类型格式说明符（例如，`%d` 用于整数，`%f` 用于浮点数），这些说明符与 C 类似。

示例：

- `slError("Error message");`
- `slError("Input %f should be non-negative", x);`
- `slWarning("Warning message");`
- `slWarning("Input %d should be non-zero", y);`

以下代码在仿真开始时执行。如果数据存储在仿真开始时初始化失败，它将使用 `slError` 函数发出错误消息。

C Function block 使用 slError 在仿真开始时报告错误消息。

#### 在自定义代码中指定行主序和列主序数组布局

*自 R2024a 起*

使用 `slSetRowMajor` 和 `slSetColumnMajor` 函数分别指定行主序和列主序数组布局。在 Configuration Parameters 对话框的 **Simulation Target** 窗格中，使用模块对话框中的 **Use Configuration Parameters Custom Code** 参数指定这些函数。

对于行主序布局，矩阵的行元素在内存中连续存储。类似地，对于列主序布局，矩阵的列元素在内存中连续存储。有关详细信息，请参阅 Row-Major and Column-Major Array Layouts (MATLAB Coder)。

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

- 如果函数位于命名空间内，则所有嵌套命名空间都应包含在函数名字符串中。基于以上代码，对于列主序函数 `foo_col`，在 configuration parameters custom code 中使用 `slSetColumnMajor("NS1::NS2::foo_col")`。
- 对于所有类成员，类名以及任何嵌套命名空间都应包含在函数名字符串中。基于以上代码，对于行主序函数 `foo_row`，在 configuration parameters custom code 中使用 `slSetRowMajor("NS1::ACLASS::foo_row")`。

对于使用类的 C Function block，如果构造函数接受 majority，则必须在 **Start** 代码中指定 majority。

### 端口

#### 输入

#### **Port\_1** — 输入端口 scalar | vector | matrix

输入端口数量由模块参数对话框的 **Symbols** 表中定义的具有 `Input` 或 `InputOutput` 作用域的符号数量决定。除非您通过编辑模块对话框 **Symbols** 表中的 **Label** 字段更改，否则每个输入端口标签与 `Input` 或 `InputOutput` 符号的名称相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `enumerated` | `bus` | `fixedpoint`

#### 输出

#### **Port\_1** — 输出端口 scalar | vector | matrix

输出端口数量由模块参数对话框的 **Symbols** 表中定义的具有 `Output` 或 `InputOutput` 作用域的符号数量决定。除非您通过编辑模块对话框 **Symbols** 表中的 **Label** 字段更改，否则每个输出端口标签与 `Output` 或 `InputOutput` 符号的名称相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `enumerated` | `bus` | `fixedpoint`

### 参数

**Simulation** 和 **Code Generation** 选项卡共有的参数。

#### **Configure custom code settings** — 用于指定自定义代码位置的选项按钮

使用 Configure Custom Code settings 按钮 C Function block gear icon. 选择是在模块本地指定自定义代码，还是在 Configuration Parameters 对话框中指定。单击 C Function block gear icon. 图标旁边的箭头以选择选项：

- **Use Block Custom Code**

  使用此选项在 C Function block 本地指定自定义代码。此设置为默认值。此选项分别启用 **Simulation** 部分和 **Code generation** 部分中的 **Simulation Custom Code** 和 **Code Generation Custom Code** 参数。

  从 R2025a 开始，本地指定的自定义代码支持代码覆盖率。要使用代码覆盖率，您必须具有 Simulink Coverage license。
- **Use Configuration Parameters Custom Code**

  使用此选项在模型 Configuration Parameters 对话框的 **Simulation Target** 窗格中指定自定义代码。有关详细信息，请参阅 Model Configuration Parameters: Simulation Target。

#### 编程使用

|  |
| --- |
| **模块参数：** `CustomCodeSettingLocation` |
| **类型：** character vector |
| **值：**`'BlockSettings'` | `'ModelConfigurationParameters'` |
| **默认值：** `'BlockSettings'` |

#### **Port and Parameter Symbols** — 符号和符号属性表

在 C 代码中使用的符号和符号属性，以表格形式指定。您必须在表格中输入每个符号的以下属性：

- **Name** — 代码中的符号名称。

  如果符号表示 C++ 类对象，则 **Name** 字段用作对类构造函数的调用：

  ```
  ObjectName(Argument1,Argument2,...)
  ```
- **Scope** — 符号的作用域。可用的作用域包括：

  - `Input` — 模块的输入。
  - `Output` — 模块的输出。
  - `InputOutput` — 模块的输入和输出。

    使用 `InputOutput` 作用域映射 C 代码中通过指针传递的输入。使用 `InputOutput` 作用域创建的输入端口和输出端口具有相同名称。`InputOutput` 作用域支持输入和输出端口的缓冲区重用。缓冲区重用可能优化内存使用，并提高代码仿真和代码生成效率，具体取决于信号大小和模块布局。限制包括：

    - `InputOutput` 符号不能用于 **Start**、**Initialize Conditions** 或 **Terminate**。
    - `InputOutput` 符号不支持 `void*` 数据类型。
    - `InputOutput` 符号不支持 `size()` 表达式。
  - `Parameter` — 显示在模块参数掩码上的模块参数。参数名称由符号的 **Label** 定义。
  - `Persistent` — 持久性模块数据，在仿真期间从一个时间步到下一个时间步保留其值。

    您可以使用 `Persistent` 作用域定义 void 指针。*void 指针* 是一种可以存储您创建或分配的任何类型数据的指针。

    您可以通过定义具有 `Persistent` 作用域的符号，并使用 `Class:` *`ClassName`* 作为该符号的 **Type**，来实例化自定义代码中定义的 C++ 类的对象。请参阅 Interface with C++ Classes Using C Function Block。
  - `Constant` — 常量值，使用 value-size 或数值表达式定义。
- **Label** — 符号的标签。对于具有 `Input`、`InputOutput` 或 `Output` 作用域的符号，标签在模块上显示为端口名称。对于具有 `Parameter` 作用域的符号，标签显示在模块参数掩码上。如果作用域为 `Constant`，则标签为常量表达式。不能为 `Persistent` 作用域符号定义标签。
- **Type** — 符号的数据类型。从下拉列表中选择数据类型或指定自定义数据类型。

  **注意**

  从 R2025a 开始，该模块支持用于 `Input`、`Output`、`InputOutput` 和 `Persistent` 作用域的 Simulink strings 类型。

  支持自定义代码中定义的 C++ 类类型，也支持 `Simulink.Bus`、Simulink Enum 和 `Simulink.AliasType` 类型。按下表所示输入 **Type**。

  | 自定义类型 | **Type** 字段中的指定 |
  | --- | --- |
  | C++ class | `Class:`*`C++ClassName`* |
  | `Simulink.Bus` | `Bus:`*`BusTypeName`* |
  | `Simulink.Enum` | `Enum:`*`EnumTypeName`* |
  | `Simulink.AliasType` | *`AliasTypeName`* |
- **Size** — 符号数据的大小。您可以使用 size 表达式来定义输出的大小，或使用 `-1` 继承大小。
- **Port** — 符号的端口索引。对于 `Input`、`InputOutput` 或 `Output` 符号，**Port** 指定该符号对应的一个或多个端口在模块上的端口索引。对于 `Parameter` 符号，**Port** 指定该符号在模块参数掩码中出现的顺序。

#### 编程使用

|  |
| --- |
| **模块参数：** `SymbolSpec` |
| **类型：** `SymbolSpec` object |
| **值：** `SymbolSpec` object |
| **默认值：** 空 `Symbol` 对象数组 |

#### **Sample time** — 采样周期 `-1` (default) | scalar | vector

采样周期，以秒为单位指定。请参阅 Types of Sample Time 和 Specify Sample Time。如果模块定义了持久性符号，则不能指定连续采样时间。

#### 编程使用

|  |
| --- |
| **模块参数**： `SampleTime` |
| **类型**： string scalar 或 character vector |
| **默认值**： `"-1"` |

#### **Block specified custom code supports multiple instances** — 用于在多个 C Function blocks 中本地指定相同自定义代码的选项 `off` (default) | `on`

*自 R2024a 起*

如果可以在模型中的多个 C Function blocks 中本地指定相同的自定义代码，而模块之间不会相互干扰，请选择此选项。例如，如果您使用包含内部状态的数学计数器，代码的多个实例可能会相互干扰。

选择此选项后，支持以下建模场景：

- 在 C Function block 中本地指定自定义代码，并在 For Each subsystem 内使用该模块。
- 在 C Function block 中本地指定使用连续采样时间的自定义代码。
- 为同一自定义代码的多个实例生成代码，其中代码的每个实例都在模型内的 C Function block 中本地指定。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程使用

|  |
| --- |
| **模块参数**： `CustomCodeIsMultiInstantiable` |
| **类型**： string scalar 或 character vector |
| **默认值**： `'off'` |

#### Simulation

#### **Output** — 输出代码 无默认值

模块在仿真期间每个时间步执行的输出代码，指定为 character vector 或 string scalar。例如，使用此参数调用外部 C 代码中的函数，修改结果，并执行操作将结果传递给其他模块。

#### 编程使用

|  |
| --- |
| **模块参数：** `OutputCode` |
| **类型：** character vector 或 string scalar |
| **值：** `""` | `C/C++ code` |
| **默认值：** `""` |

#### **Start** — 初始化代码 无默认值

模块在仿真开始时执行一次的初始化代码。例如，使用此参数初始化持久性符号。

#### 编程使用

|  |
| --- |
| **模块参数：** `StartCode` |
| **类型：** character vector 或 string scalar |
| **值：** `""` | `C/C++ code` |
| **默认值：** `""` |

#### **Initialize Conditions** — 重新初始化代码 无默认值

当启用模块所在的子系统或模型时，模块要执行的重新初始化代码。该代码在仿真开始时执行一次。如果模块位于子系统或模型中，且该子系统或模型包含一个 Enable block，并且其 **States when enabling** 参数设置为 `reset`，则该代码还会在子系统或模型每次从禁用切换到启用时执行。请参阅 Using Enabled Subsystems。例如，您可以使用此代码设置初始输出值或重置持久性变量的值。

#### 编程使用

|  |
| --- |
| **模块参数：** `InitializeConditionsCode` |
| **类型：** character vector 或 string scalar |
| **值：** `""` | `C/C++ code` |
| **默认值：** `""` |

#### **Terminate** — 终止代码 无默认值

模块在仿真结束时执行一次的终止代码。例如，使用此代码释放缓存在指定为 void 指针的持久性符号上的内存。

#### 编程使用

|  |
| --- |
| **模块参数：** `TerminateCode` |
| **类型：** character vector 或 string scalar |
| **值：** `""` | `C/C++ code` |
| **默认值：** `""` |

#### **Headers** — 本地指定自定义代码的头文件 无默认值

本地指定自定义代码的头文件。此参数位于 **Simulation Custom Code** 部分。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程使用

|  |
| --- |
| **模块参数：** `SimCustomHeaderFile` |
| **类型：** character vector 或 string scalar |
| **值：** header file names 或 #include statements |
| **默认值：** `""` |

#### **Sources** — 本地指定自定义代码的源文件 无默认值

本地指定自定义代码的源文件。此参数位于 **Simulation Custom Code** 部分。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程使用

|  |
| --- |
| **模块参数：** `SimCustomSourceFile` |
| **类型：** character vector 或 string scalar |
| **值：** 任意文件名 |
| **默认值：** `""` |

#### **Libraries** — 本地指定静态库或共享库的列表 无默认值

本地指定静态库或共享库的列表。此参数位于 **Simulation Custom Code** 部分。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程使用

|  |
| --- |
| **模块参数：** `SimCustomLibraries` |
| **类型：** character vector 或 string scalar |
| **值：** 任意库文件名 |
| **默认值：** `""` |

#### **Search Directories** — 本地指定包含自定义代码头文件和源文件的目录 无默认值

本地指定包含自定义代码头文件和源文件的目录。此参数在 **Simulation Custom Code** 部分中提供。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程使用

|  |
| --- |
| **模块参数：**`SimCustomSearchDirectory` |
| **类型：** character vector 或 string scalar |
| **值：** 任意文件夹路径 |
| **默认值：** `""` |

#### **Defines** — 本地指定要添加到编译器命令行的预处理器宏定义 无默认值

本地指定要添加到编译器命令行的预处理器宏定义。此参数在 **Simulation Custom Code** 部分的 **Advanced** 选项卡中提供。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程使用

|  |
| --- |
| **模块参数：** `SimCustomDefines` |
| **类型：** character vector |
| **值：** preprocessor macro definition |
| **默认值：** `''` |

#### **Compiler Flags** — 本地指定要添加到编译器命令行的附加标志 无默认值

本地指定要添加到编译器命令行的附加标志。此参数在 **Simulation Custom Code** 部分的 **Advanced** 选项卡中提供。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程使用

|  |
| --- |
| **模块参数：** `SimCustomCompilerFlags` |
| **类型：** character vector |
| **值：** compiler flags |
| **默认值：** `''` |

#### **Linker Flags** — 本地指定要添加到链接器命令行的附加标志 无默认值

本地指定要添加到链接器命令行的附加标志。此参数在 **Simulation Custom Code** 部分的 **Advanced** 选项卡中提供。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程使用

|  |
| --- |
| **模块参数：** `SimCustomLinkerFlags` |
| **类型：** character vector |
| **值：** linker flags |
| **默认值：** `''` |

#### 代码生成

**Code generation** 选项卡上的参数需要 Simulink Coder™ 或 Embedded Coder® 许可证。

#### **Use same code as simulation** — 用于对仿真和代码生成使用相同或不同代码的选项 `on` (default) | `off`

指定对仿真和代码生成使用相同还是不同的代码。默认情况下，此选项处于选中状态，模块对仿真和代码生成使用相同代码。清除此选项可对仿真和代码生成使用不同代码。

#### 编程使用

|  |
| --- |
| **模块参数**： `CodegenUsesSimCustomCode` |
| **类型**： string scalar 或 character vector |
| **默认值**： `'on'` |

#### **Generate code as - is (optimizations off)** — 用于允许对代码生成代码进行解析的选项 `on` (default) | `off`

指定是否允许解析代码生成代码。默认情况下，此选项处于选中状态，模块会将您的代码嵌入生成的代码中而不进行解析。清除此选项将使模块能够分析代码并报告任何错误。

当您对仿真和代码生成使用不同代码时，此参数使用其默认设置。

#### 依赖关系

此选项仅在选中 **Use same code as simulation** 参数时才可供选择。

#### 编程使用

|  |
| --- |
| **模块参数**： `GenerateCodeAsIs` |
| **类型**： string scalar 或 character vector |
| **默认值**： `'on'` |

#### **Output** — 输出代码 无值

模块在代码生成期间每个时间步执行的输出代码。例如，使用此参数调用外部 C/C++ 代码中的函数，修改结果，并执行操作将结果传递给其他模块。

#### 编程使用

|  |
| --- |
| **模块参数：** `CodegenOutputCode` |
| **类型：** character vector 或 string scalar |
| **值：** `""` | `C/C++ code` |
| **默认值：** `""` |

#### **Start** — 初始化代码 无默认值

模块在代码生成开始时执行一次的初始化代码。例如，使用此参数初始化持久性符号。

#### 编程使用

|  |
| --- |
| **模块参数：** `CodegenStartCode` |
| **类型：** character vector 或 string scalar |
| **值：** `""` | `C/C++ code` |
| **默认值：** `""` |

#### **Initialize Conditions** — 重新初始化代码 无默认值

当启用模块所在的子系统或模型时，模块要执行的重新初始化代码。该代码在代码生成开始时执行一次。如果模块位于子系统或模型中，且该子系统或模型包含一个 Enable block，并且其 **States when enabling** 参数设置为 `reset`，则该代码还会在子系统或模型每次从禁用切换到启用时执行。请参阅 Using Enabled Subsystems。例如，您可以使用此代码设置初始输出值或重置持久性变量的值。

#### 编程使用

|  |
| --- |
| **模块参数：** `CodegenInitializeConditionsCode` |
| **类型：** character vector 或 string scalar |
| **值：** `""` | `C/C++ code` |
| **默认值：** `""` |

#### **Terminate** — 终止代码 无默认值

模块在代码生成结束时执行一次的终止代码，指定为 character vector 或 string scalar。例如，使用此代码释放缓存在指定为 void 指针的持久性符号上的内存。

#### 编程使用

|  |
| --- |
| **模块参数：** `CodegenTerminateCode` |
| **类型：** character vector 或 string scalar |
| **值：** `""` | `C/C++ code` |
| **默认值：** `""` |

#### **Headers** — 本地指定自定义代码的头文件 无默认值

本地指定自定义代码的头文件。此参数位于 **Code Generation Custom Code** 部分。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程使用

|  |
| --- |
| **模块参数：** `CustomHeaderFile` |
| **类型：** character vector 或 string scalar |
| **值：** header file names 或 #include statements |
| **默认值：** `""` |

#### **Sources** — 本地指定自定义代码的源文件 无默认值

本地指定自定义代码的源文件。此参数位于 **Code Generation Custom Code** 部分。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程使用

|  |
| --- |
| **模块参数：** `CustomSourceFile` |
| **类型：** character vector 或 string scalar |
| **值：** 任意文件名 |
| **默认值：** `""` |

#### **Libraries** — 本地指定静态库或共享库的列表 无默认值

本地指定静态库或共享库的列表。此参数位于 **Code Generation Custom Code** 部分。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程使用

|  |
| --- |
| **模块参数：**`CustomLibraries` |
| **类型：** character vector 或 string scalar |
| **值：** 任意库文件名 |
| **默认值：** `""` |

#### **Search Directories** — 本地指定包含自定义代码头文件和源文件的目录 无默认值

本地指定包含自定义代码头文件和源文件的目录。此参数位于 **Code Generation Custom Code** 部分。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程使用

|  |
| --- |
| **模块参数：**`CustomSearchDirectory` |
| **类型：** character vector 或 string scalar |
| **值：** 任意文件夹路径 |
| **默认值：** `""` |

#### **Defines** — 本地指定要添加到编译器命令行的预处理器宏定义 无默认值

本地指定要添加到编译器命令行的预处理器宏定义。此参数位于 **Code Generation Custom Code** 部分的 **Advanced** 选项卡中。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程使用

|  |
| --- |
| **模块参数：** `CustomDefines` |
| **类型：** character vector |
| **值：** preprocessor macro definition |
| **默认值：** `''` |

#### **Compiler Flags** — 向编译器命令行添加附加标志 无默认值

向编译器命令行添加附加标志。此参数位于 **Code Generation Custom Code** 部分的 **Advanced** 选项卡中。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程使用

|  |
| --- |
| **模块参数：** `CustomCompilerFlags` |
| **类型：** character vector |
| **值：** compiler flags |
| **默认值：** `''` |

#### **Linker Flags** — 向链接器命令行添加附加标志 无默认值

向链接器命令行添加附加标志。此参数位于 **Code Generation Custom Code** 部分的 **Advanced** 选项卡中。

#### 依赖关系

要启用此参数，请将 **Configure Custom Code settings** 参数设置为 `Use Block Custom Code`。

#### 编程使用

|  |
| --- |
| **模块参数：** `CustomLinkerFlags` |
| **类型：** character vector |
| **值：** linker flags |
| **默认值：** `''` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `integera` | `singlea` | `stringa` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 实际数据类型或能力支持取决于模块实现。 | |

#### 扩展能力

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际数据类型或能力支持取决于模块实现。

### 版本历史

**在 R2020a 中引入**

#### R2025a：与函数接口和自定义代码覆盖率相关的增强

- C Function block 现在支持用于 `Input`、`Output`、`InputOutput` 和 `Persistent` 作用域的 Simulink strings 类型。
- 您现在可以调用字符串库函数的一个子集。有关支持的字符串库函数的详细信息，请参阅 Call C Library Functions。
- 现在支持对本地指定的自定义代码进行代码覆盖率。要在模块对话框中本地指定自定义代码，请使用 **Use Block Custom Code** 参数。有关详细信息，请参阅 **Configure custom code settings**。

#### R2024a：C Function block 对话框和参数名称的变更

对模块对话框和参数进行了以下更改：

- 模块对话框新增了两个选项卡：**Simulation** 和 **Code generation**。
- **Output code**、**Start code**、**Initialize conditions code** 和 **Terminate code** 参数现在分别称为 **Output**、**Start**、**Initialize code** 和 **Terminate**。
- Configure custom code settings C Function block gear icon. 按钮列出了两个下拉选项：**Use Block Custom Code** 和 **Use Configuration Parameters Custom Code**。使用这些选项可指定是在模块参数对话框中本地指定自定义代码，还是使用 configuration parameters 对话框将自定义代码集成到 Simulink 中。
- **Symbols** 表现在是 **Ports and Parameters** 表。
- **Symbols** 表中的 **Size** 列现在是 **Ports and Parameters** 表中的 **Dimensions** 列。

#### R2024a：与自定义代码指定相关的增强

- 您现在可以为代码生成指定不同于仿真所用代码的目标特定代码。为此，请使用 **Simulation** 和 **Code generation** 部分中的参数。
- 您可以使用 **Simulation Custom Code** 和 **Code Generation Custom Code** 部分中的参数分别指定用于仿真和代码生成的自定义代码。使用这些参数在本地指定自定义代码，并且仅指定特定 C Function block 所需的代码。
- 您可以将自定义代码嵌入生成的代码中而不进行解析（请参阅 **Generate code as - is (optimizations off)**）。此增强扩展了 C Function block 的能力，允许您使用与桌面 MEX 编译器不兼容的自定义 C 代码。
- 在自定义代码中使用 `slError` 和 `slWarning` 消息分别报告错误和警告消息。
- 在自定义代码中使用 `slSetRowMajor` 和 `slSetColumnMajor` 函数分别指定行主序和列主序数组布局。

#### R2023a：支持 `printf`、`memcpy` 和 `memset` C 库函数

您可以在 C Function block 的 **Start**、**Initialize Conditions** 和 **Terminate** 代码中使用 `printf`、`memcpy` 和 `memset` 函数。

## Libraries

Simulink / User-Defined Functions

## Description

The C Function block integrates and calls external C/C++ code from a
Simulink® model. Use this block to define external code and customize the integration of
your code by preprocessing or postprocessing the data. In addition, you can specify customized
code for simulation and C code generation. You can conditionally call functions defined in
your code, and you can also call multiple functions in one block. Using this block, you can
initialize persistent data and pass it to an external function.

The C Function block supports initializing persistent data and calling
external functions from the block dialog box. Persistent data can include an object of a C++
class defined in your custom code. See Interface with C++ Classes Using C Function Block. The block supports only
initializing and terminating persistent data. The block does not support updating the data
during simulation. To model a dynamic system with continuous states, use an
S-Function block. To learn more about S-functions, see What Is an S-Function?

**Note**

C99 is the standard version of C language supported for custom C code integration into
Simulink.

### Specify Custom Code

*Since R2024a*

Starting in R2024a, the block provides you with a range of options to specify custom C
/C++ code for the block.

- You can specify the custom code locally in the block, so you can integrate a code
  component that is fully contained in a single block. For example, if you want a
  C Function block to behave like a custom filter which is defined
  using external C/C++ code, specify the custom code locally in the block.
- You can share the custom code with other blocks in a model or across multiple
  models. To share the custom code across multiple models you must define the custom
  code in the Configuration Parameters dialog box of a Simulink library model. Then, use
  the code in a block within the library and fetch that block from that library in other
  models.

For more information, see **Configure custom code
settings**.

### Call C Library Functions

You can call these C Math Library functions directly from the C Function
block.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| `abs` | `acos` | `asin` | `atan` | `atan2` | `ceil` |
| `cos` | `cosh` | `exp` | `fabs` | `floor` | `fmod` |
| `labs` | `ldexp` | `log` | `log10` | `pow` | `sin` |
| `sinh` | `sqrt` | `tan` | `tanh` |  |  |

When you call these functions, double precision applies unless all the input arguments
are explicitly single precision. When a type mismatch occurs, a cast of the input arguments
to the expected type replaces the original arguments. For example, if you call the
`sin` function with an integer argument, a cast of the input argument to
a floating-point number of type `double` replaces the original
argument.

Starting in R2025a, you can call these string library functions inside the C
function block.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| `strlen` | `strncpy` | `strncat` | `strcmp` | `strncmp` | `strstr` |

For more information, see Use Simulink Strings inside C Function Block to Model Scrolling Display.

To call other C library functions, create and call an external wrapper function that
calls the C library function.

**Call the `abs`, `fabs`, and `labs`
Functions**

Interpretation of the `abs`, `fabs`, and
`labs` functions in C Function block goes beyond the
standard C version to include integer and floating-point arguments:

- If `x` is an integer, the standard C function
  `abs` applies to `x`, or
  `abs(x)`.
- If `x` is a double, the standard C function
  `labs` applies to `x`, or
  `labs(x)`.
- If `x` is a single, the standard C function
  `fabs` applies to `x`, or
  `fabs(x)`.

**Code Replacement Library (CRL) Based on Type**

The call to the function should call the correct CRL based on the type of data passed
into the function. If no CRL is specified, the call to the function should call to
type-specific library. The CRL for C99 generates a type-specific function. For
example:

| Type passed in | Code generation call |
| --- | --- |
| `sin(doubleIn)` | `sin(doubleIn)` |
| `sin(floatIn)` | `sinf(floatIn)` |

You can call `printf`,
`memcpy` and `memset` functions in the C
Function block. *(since R2023a)*

### Report Run-time Errors and Warnings in Simulink

*Since R2024a*

In custom C code that you specify in the C Function block , use the
`slError` and `slWarning` functions to report
run-time errors and warnings, respectively. An error terminates the simulation and must be
resolved before simulation continues. A warning indicates a potential issue with the code
but does not terminate the simulation.

Both `slError` and `slWarning` functions support
different data type format specifiers (for example, `%d`  for integer,
`%f`  for float) that are similar to C.

Examples :

- `slError("Error message");`
- `slError("Input %f should be non-negative", x);`
- `slWarning("Warning message");`
- `slWarning("Input %d should be non-zero", y);`

The following code executes at the start of the simulation. It uses the
`slError` function to issue an error message if the data store fails to
initialize at the start of simulation.

C Function block uses slError to report an error message at the start of simulation.

### Specify Row-Major and Column-Major Array Layouts in Custom Code

*Since R2024a*

Use the `slSetRowMajor` and `slSetColumnMajor`
functions to specify row-major and column-major array layouts, respectively. Specify these
functions in the **Simulation Target** pane of the Configuration Parameters
dialog box using **Use Configuration Parameters Custom Code** parameter
from block dialog box.

For a row-major layout, the row elements of a matrix are stored contiguously in memory.
Similarly, for a column-major layout, the column elements of a matrix are stored
contiguously in memory. For more information, see Row-Major and Column-Major Array Layouts (MATLAB Coder).

Function prototypes:

- `void slSetRowMajor(const char* functionName)`
- `void slSetColumnMajor(const char* functionName)`

`functionName` must be a string literal and fully qualified.

For example, consider the following code:

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

For a fully qualified function name.

- If the function is inside a namespace, all the nested namespaces should be included
  in the function name string. Based on the above code, for the column-major function,
  `foo_col`, use
  `slSetColumnMajor("NS1::NS2::foo_col")` in the configuration
  parameters custom code.
- For all class members, the class name along with any nested namespaces should be
  included in the function name string. Based on the above code, for the row-major
  function `foo_row`, use
  `slSetRowMajor("NS1::ACLASS::foo_row")` in the configuration
  parameters custom code.

For a C Function block that uses classes, if the constructor takes
majority, the majority must be specified in the **Start** code.

## Ports

### Input

### **Port\_1** — Input port scalar | vector | matrix

The number of input ports is determined by the number of symbols with
`Input` or `InputOutput` scope
defined in the **Symbols** table in the block parameters dialog box.
Each input port label is the same as the name of the `Input`
or `InputOutput` symbol unless you change it by editing the
**Label** field in the **Symbols** table of the
block dialog box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `enumerated` | `bus` | `fixedpoint`
### Output

### **Port\_1** — Output port scalar | vector | matrix

The number of output ports is determined by the number of symbols with
`Output` or `InputOutput` scope
defined in the **Symbols** table in the block parameters dialog box.
Each output port label is the same as the name of the
`Output` or `InputOutput` symbol
unless you change it by editing the **Label** field in the
**Symbols** table of the block dialog box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `enumerated` | `bus` | `fixedpoint`

## Parameters

Parameters common to both **Simulation** and **Code
Generation** tabs.

### **Configure custom code settings** — Option to specify custom code location button

Use the Configure Custom Code settings button C Function block gear icon. to choose whether to specify the custom code in the
block locally or in the Configuration Parameters dialog box. Click the arrow next to the C Function block gear icon. icon to select an option:

- **Use Block Custom Code**

  Use this option to specify the custom code locally in the C
  Function block. This setting is default. This option enables the
  **Simulation Custom Code** and the **Code Generation
  Custom Code** parameters in the **Simulation** section
  and the **Code generation** section, respectively.

  Starting in R2025a, code coverage is supported for locally specified custom
  code. To use code coverage, you must have Simulink
  Coverage license.
- **Use Configuration Parameters Custom Code**

  Use this option to specify the custom code in the **Simulation
  Target** pane of the model Configuration Parameters dialog box. For more
  information, see Model Configuration Parameters: Simulation Target.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CustomCodeSettingLocation` |
| **Type:** character vector |
| **Value:**`'BlockSettings'` | `'ModelConfigurationParameters'` |
| **Default:** `'BlockSettings'` |

### **Port and Parameter Symbols** — Symbols and symbol properties table

Symbols and symbol properties used in the C code, specified as a table. You must
enter the following attributes of each symbol in the table:

- **Name** — Symbol name in the code.

  If the symbol represents a C++ class object, the **Name**
  field serves as a call to the class
  constructor:

  ```
  ObjectName(Argument1,Argument2,...)
  ```
- **Scope** — Scope of the symbol. These scopes are available:

  - `Input` — Input to the block.
  - `Output` — Output to the block.
  - `InputOutput` — Both input and output to the
    block.

    Use the `InputOutput` scope to map an input
    passed by a pointer in your C code. Ports created using an
    `InputOutput` scope have the same name for input
    and output ports. `InputOutput` scope enables
    buffer reuse for input and output ports. Buffer reuse may optimize memory
    use and improve code simulation and code generation efficiency, depending on
    the signal size and the block layout. Limitations include:

    - An `InputOutput` symbol cannot be used in
      **Start**, **Initialize
      Conditions**, or **Terminate**.
    - `InputOutput` symbols do not support the
      `void*` data type.
    - `InputOutput` symbols do not support
      `size()`  expressions.
  - `Parameter` — Block parameter that appears on the block
    parameter mask. The parameter name is defined by the
    **Label** of the symbol.
  - `Persistent` — Persistent block data, which retains its
    value from one time step to the next during simulation.

    You can define a void pointer using the `Persistent`
    scope. A *void pointer* is a pointer that can store any
    type of data that you create or allocate.

    You can instantiate an object of a C++ class defined in your custom code
    by defining a symbol with `Persistent` scope and using
    `Class:`
    *`ClassName`* as the **Type** for
    the symbol. See Interface with C++ Classes Using C Function Block.
  - `Constant` — Constant value, defined using value-size
    or numeric expressions.
- **Label** — Label of the symbol. For a symbol
  with `Input`, `InputOutput`, or
  `Output` scope, the label appears as the port name on
  the block. For a symbol with `Parameter` scope, the label
  appears on the block parameter mask. If the scope is
  `Constant`, the label is the constant expression. You
  cannot define a label for `Persistent` scope
  symbols.
- **Type** — Data type of the symbol. Select a data
  type from the drop-down list or specify a custom data type.

  **Note**

  Starting in R2025a, the block supports Simulink strings types for `Input`,
  `Output`, `InputOutput` and
  `Persistent` scopes.

  C++ class types defined in your custom code are supported, as are `Simulink.Bus`, Simulink Enum, and `Simulink.AliasType` types. Enter the
  **Type** as shown in this table.

  | Custom type | Specification in **Type** field |
  | --- | --- |
  | C++ class | `Class:`*`C++ClassName`* |
  | `Simulink.Bus` | `Bus:`*`BusTypeName`* |
  | `Simulink.Enum` | `Enum:`*`EnumTypeName`* |
  | `Simulink.AliasType` | *`AliasTypeName`* |
- **Size** — Size of the symbol data. You can use a
  size expression to define the size of an output or use `-1` to
  inherit size.
- **Port** — Port index of the symbol. For an
  `Input`, `InputOutput`, or
  `Output` symbol, **Port**
  specifies the port index on the block of the port or ports corresponding to the
  symbol. For a `Parameter` symbol, **Port** specifies the order that the symbol appears in the block
  parameter mask.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SymbolSpec` |
| **Type:** `SymbolSpec` object |
| **Value:** `SymbolSpec` object |
| **Default:** Empty array of `Symbol` objects |

### **Sample time** — Sample period `-1` (default) | scalar | vector

Sample period, specified in seconds. See Types of Sample Time
and Specify Sample Time. If the block
defines persistent symbols, you cannot specify a continuous sample time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: string scalar or character vector |
| **Default**: `"-1"` |

### **Block specified custom code supports multiple instances** — Option to specify the same custom code locally in multiple C Function blocks `off` (default) | `on`

*Since R2024a*

Select this option if the same custom code can be locally specified in multiple
C Function blocks within a model without the blocks interfering with
each other. For example, if you use a mathematical counter that contains internal
states, multiple instances of the code can interfere with each other.

When you select this option, these modeling scenarios are supported:

- Specify custom code locally in a C Function block and use the
  block within a For Each subsystem.
- Specify custom code locally in a C Function block that uses
  continuous sample time.
- Generate code for multiple instances of the same custom code, where each
  instance of the code is specified locally in a C Function block
  within a model.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CustomCodeIsMultiInstantiable` |
| **Type**: string scalar or character vector |
| **Default**: `'off'` |

### Simulation

### **Output** — Output code no default

Output code that the block executes at each time step during simulation, specified
as a character vector or string scalar. For example, use this parameter to call a
function from external C code, make modifications to the results, and perform
operations to pass the results to other blocks.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputCode` |
| **Type:** character vector or string scalar |
| **Value:** `""` | `C/C++ code` |
| **Default:** `""` |

### **Start** — Initialization code no default

Initialization code that the block executes one time at the start of simulation.
For example, use this parameter to initialize persistent symbols.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StartCode` |
| **Type:** character vector or string scalar |
| **Value:** `""` | `C/C++ code` |
| **Default:** `""` |

### **Initialize Conditions** — Reinitialization code no default

Reinitialization code for the block to execute when enabling a subsystem or model
in which the block is placed. The code executes one time at the start of simulation.
If the block is inside a subsystem or a model that contains an Enable block with the **States when enabling** parameter
set to `reset`, the code also executes each time the
subsystem or model switches from disabled to enabled. See Using Enabled Subsystems. You can use this code, for example, to set an initial output value or reset the
value of a persistent variable.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitializeConditionsCode` |
| **Type:** character vector or string scalar |
| **Value:** `""` | `C/C++ code` |
| **Default:** `""` |

### **Terminate** — Termination code no default

Termination code that the block executes one time at the end of simulation. For
example, use this code to free the memory cached on persistent symbols specified as
void pointers.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TerminateCode` |
| **Type:** character vector or string scalar |
| **Value:** `""` | `C/C++ code` |
| **Default:** `""` |

### **Headers** — Locally specify header files for custom code no default

Locally specify header files for custom code. This parameter is in the
**Simulation Custom Code** section.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SimCustomHeaderFile` |
| **Type:** character vector or string scalar |
| **Value:** header file names or #include statements |
| **Default:** `""` |

### **Sources** — Locally specify source files for the custom code no default

Locally specify source files for the custom code. This parameter is in the
**Simulation Custom Code** section.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SimCustomSourceFile` |
| **Type:** character vector or string scalar |
| **Value:** any file name |
| **Default:** `""` |

### **Libraries** — Locally specify a list of static or shared libraries no default

Locally specify a list of static or shared libraries. This parameter is in the
**Simulation Custom Code** section.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SimCustomLibraries` |
| **Type:** character vector or string scalar |
| **Value:** any library file name |
| **Default:** `""` |

### **Search Directories** — Locally specify directories containing header and source files for custom code no default

Locally specify directories containing header and source files for custom code.
This parameter is available in the **Simulation Custom Code**
section.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`SimCustomSearchDirectory` |
| **Type:** character vector or string scalar |
| **Value:** any folder path |
| **Default:** `""` |

### **Defines** — Locally specify preprocessor macro definition to be added to the compiler command line no default

Locally specify preprocessor macro definition to be added to the compiler command
line. This parameter is available in the **Simulation Custom Code**
section, in the **Advanced** tab.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SimCustomDefines` |
| **Type:** character vector |
| **Value:** preprocessor macro definition |
| **Default:** `''` |

### **Compiler Flags** — Locally specify additional flags to be added to the compiler command line no default

Locally specify additional flags to be added to the compiler command line. This
parameter is available in the **Simulation Custom Code** section,
in the **Advanced** tab.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SimCustomCompilerFlags` |
| **Type:** character vector |
| **Value:** compiler flags |
| **Default:** `''` |

### **Linker Flags** — Locally specify additional flags to be added to the linker command line no default

Locally specify additional flags to be added to the linker command line. This
parameter is available in the **Simulation Custom Code** section,
in the **Advanced** tab.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SimCustomLinkerFlags` |
| **Type:** character vector |
| **Value:** linker flags |
| **Default:** `''` |

### Code generation

Parameters on the **Code generation** tab require a Simulink
Coder™ or Embedded Coder® license.

### **Use same code as simulation** — Option to use same or different codes for simulation and code generation `on` (default) | `off`

Specify whether to use same or different codes for simulation and code generation.
By default, this option is selected and the block uses the same code for simulation
and code generation. Clear this option to use different code for simulation and code
generation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CodegenUsesSimCustomCode` |
| **Type**: string scalar or character vector |
| **Default**: `'on'` |

### **Generate code as - is (optimizations off)** — Option to allow parsing for code generation code `on` (default) | `off`

Specify whether to allow parsing for code generation code. By default, this option
is selected and the block embeds your code in the generated code without parsing.
Clearing this option enables the block to analyze the code and report any
errors.

When you use different code for simulation and code generation, this parameter
uses its default settings.

#### Dependencies

This option is only available for selection when the **Use same code as
simulation** parameter is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `GenerateCodeAsIs` |
| **Type**: string scalar or character vector |
| **Default**: `'on'` |

### **Output** — Output code no value

Output code that the block executes at each time step during code generation. For
example, use this parameter to call a function from external C/C++ code, make
modifications to the results, and perform operations to pass the results to other
blocks.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CodegenOutputCode` |
| **Type:** character vector or string scalar |
| **Value:** `""` | `C/C++ code` |
| **Default:** `""` |

### **Start** — Initialization code no default

Initialization code that the block executes one time at the start of code
generation. For example, use this parameter to initialize persistent symbols.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CodegenStartCode` |
| **Type:** character vector or string scalar |
| **Value:** `""` | `C/C++ code` |
| **Default:** `""` |

### **Initialize Conditions** — Reinitialization code no default

Reinitialization code for the block to execute when enabling a subsystem or model
in which the block is placed. The code executes one time at the start of code
generation. If the block is inside a subsystem or in a model that contains an Enable block with the **States when enabling** parameter
set to `reset`, the code also executes each time the
subsystem or model switches from disabled to enabled. See Using Enabled Subsystems. You can use this code, for example, to set an initial output value or reset the
value of a persistent variable.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CodegenInitializeConditionsCode` |
| **Type:** character vector or string scalar |
| **Value:** `""` | `C/C++ code` |
| **Default:** `""` |

### **Terminate** — Termination code no default

Termination code that the block executes one time at the end of code generation,
specified as a character vector or string scalar. For example, use this code to free
the memory cached on persistent symbols specified as void pointers.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CodegenTerminateCode` |
| **Type:** character vector or string scalar |
| **Value:** `""` | `C/C++ code` |
| **Default:** `""` |

### **Headers** — Locally specify header files for custom code no default

Locally specify header files for custom code. This parameter is in the
**Code Generation Custom Code** section.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CustomHeaderFile` |
| **Type:** character vector or string scalar |
| **Value:** header file names or #include statements |
| **Default:** `""` |

### **Sources** — Locally specify source files for the custom code no default

Locally specify source files for the custom code. This parameter is in the
**Code Generation Custom Code** section.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CustomSourceFile` |
| **Type:** character vector or string scalar |
| **Value:** any file name |
| **Default:** `""` |

### **Libraries** — Locally specify a list of static or shared libraries no default

Locally specify a list of static or shared libraries. This parameter is in the
**Code Generation Custom Code** section.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`CustomLibraries` |
| **Type:** character vector or string scalar |
| **Value:** any library file name |
| **Default:** `""` |

### **Search Directories** — Locally specify Directories that contain header and source files for custom code no default

Locally specify Directories that contain header and source files for custom code.
This parameter is in the **Code Generation Custom Code**
section.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`CustomSearchDirectory` |
| **Type:** character vector or string scalar |
| **Value:** any folder path |
| **Default:** `""` |

### **Defines** — Locally specify preprocessor macro definition to be added the compiler command line no default

Locally specify preprocessor macro definition to be added the compiler command
line. This parameter is in the **Code Generation Custom Code**
section, in the **Advanced** tab.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CustomDefines` |
| **Type:** character vector |
| **Value:** preprocessor macro definition |
| **Default:** `''` |

### **Compiler Flags** — Add Additional flags to compiler command line no default

Add additional flags to compiler command line. This parameter is in the
**Code Generation Custom Code** section, in the
**Advanced** tab.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CustomCompilerFlags` |
| **Type:** character vector |
| **Value:** compiler flags |
| **Default:** `''` |

### **Linker Flags** — Add additional flags to linker command line no default

Add additional flags to linker command line. This parameter is in the
**Code Generation Custom Code** section, in the
**Advanced** tab.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CustomLinkerFlags` |
| **Type:** character vector |
| **Value:** linker flags |
| **Default:** `''` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `integera` | `singlea` | `stringa` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Actual data type or capability support depends on block implementation. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual data type or capability support depends on block implementation.

## Version History

**Introduced in R2020a**

### R2025a: Enhancements related to function interface and custom code coverage

- The C Function block now supports Simulink strings types for `Input`, `Output`,
  `InputOutput` and `Persistent` scopes.
- You can now call a subset of string library functions. For more information about
  supported string library functions, see Call C Library Functions.
- Code coverage is now supported for locally specified custom code. To locally
  specify custom code in the block dialog box, use the **Use Block Custom
  Code** parameter. For more information, see **Configure custom
  code settings**.

### R2024a: Changes to C Function block dialog box and parameter names

These changes are made to block dialog box and parameters:

- The block dialog box has two new tabs, **Simulation** and
  **Code generation**.
- The **Output code**, **Start code**,
  **Initialize conditions code**, and **Terminate
  code** parameters are now called **Output**,
  **Start**, **Initialize code**, and
  **Terminate**, respectively.
- The Configure custom code settings C Function block gear icon. button lists two drop-down options, **Use Block
  Custom Code** and **Use Configuration Parameters Custom
  Code**. Use these options to specify whether to specify the custom code
  locally in the block parameters dialog box or use the configuration parameters dialog
  box to integrate your custom code into Simulink.
- The **Symbols** table is now the **Ports and
  Parameters** table.
- The **Size** column in the **Symbols** table is
  now the **Dimensions** column in the **Ports and
  Parameters** table.

### R2024a: Enhancements related to custom code specification

- You can now specify target-specific code for code generation that is different from
  the code you use for simulation. To do so, use the parameters in the
  **Simulation** and **Code generation**
  sections.
- You can use the parameters in the **Simulation Custom Code** and
  **Code Generation Custom Code** sections to specify your custom code
  for simulation and code generation, respectively. Use these parameters to specify custom
  code locally and only specify the code that is required for a particular C
  Function block.
- You can embed your custom code in the generated code without parsing (see **Generate code as -
  is (optimizations off)**). This enhancement extends the capability of the
  C Function block by allowing you to use custom C code that is not
  compatible with desktop MEX compilers.
- Use `slError` and `slWarning` messages in your
  custom code to report error and warning messages, respectively.
- Use `slSetRowMajor` and `slSetColumnMajor`
  functions in your custom code to specify row-major and column-major array layouts,
  respectively.

### R2023a: Support for `printf`, `memcpy` and `memset` C library functions

You can use `printf`, `memcpy` and
`memset` functions in the **Start**,
**Initialize Conditions**, and **Terminate** codes of
the C Function block.
