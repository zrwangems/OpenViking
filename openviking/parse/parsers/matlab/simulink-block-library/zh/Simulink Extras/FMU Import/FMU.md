---
type: simulink-block
title: 'FMU'
family: 'simulink-extras'
product_id: 'simulink-extras'
product_name: 'Simulink Extras'
documentation_release: R2025b
official_category: 'FMU Import'
documentation_page: 'fmu'
documentation_source_path: '../simulink/ref_extras/fmu.html'
language: zh-CN
chinese_source: worker-translation
---

# FMU

## 端口

### 输出

### **Port\_1** — 占位端口 none | | string size limited to 255

占位端口，按原样不产生输出。当实际 FMU 导入到模块中时，输入和输出端口会被配置。输入和输出端口均支持数值和字符串数据类型。

## 参数

### **FMU name** — FMU 名称 字符向量

指定 FMU 的名称，可以带或不带文件扩展名。此条目区分大小写。FMU 必须存在于 MATLAB® 路径上。

要指定 FMU 名称，请在 **FMU name** 文本框中输入名称。

当您点击 **OK** 时，模块会创建一个 `/slprj/_fmu/unique_ID` 文件夹，其中包含解压后的文件，且文件层次结构保持完整。

#### 依赖项

当您指定 FMU 名称时，模块对话框会更新为包含四个选项卡：

- **Parameters**
- **Simulation**
- **Input**
- **Output**

#### 编程用法

|  |
| --- |
| **模块参数：** `FMUName` |
| **类型：** 字符向量 |
| **值：** FMU 的名称，带或不带文件扩展名 |
| **默认值：** `' '` |

### 参数

此选项卡列出 FMU 中定义的参数。

- 要仅显示您感兴趣的参数，请在筛选字段中键入搜索字符串。该字符串可以匹配参数名称或描述中的文本。
- 在参数表中，您可以在 **Value** 字段中更改参数的值。
- 导入的参数名称有 55 个字符的限制。

您可以通过使用 `set_param` 函数设置 `FMUParamMapping` 模块参数来更改结构化模型参数的层次结构。此模块参数可以设置为 `Inherit`、`Flat` 或 `Structured`。默认设置为 `Inherit`。将其设置为 `Flat` 会将结构化模型参数分离为具有相应参数名称和值的单独参数。将其设置为 `Structured` 会将模型参数合并为参数值结构体。

### 输入

此选项卡列出 FMU `modelDescription.xml` 中指定的输入变量。

为结构化输入端口指定变量。

要按名称筛选变量，请在文本框中键入变量名称。

变量表列出了层次结构顶部节点及其子节点的变量及其值，其中许多可以在此选项卡上编辑。

- Name — 变量名称。此内容不可编辑。
- Visibility — 选中此复选框可为该变量启用模块上的输入端口。清除此复选框可移除端口。

  在顶层节点选中此复选框会使子节点作为模块的一个端口可见。

  **注意**

  当您点击 **Apply** 时，模块端口数量会发生变化。请记得相应地添加或移除连接。
- Start — 添加在 `modelDescription.xml` 中定义的起始值。您不能：

  - 在相应输入端口可见时更改起始值。
  - 向非叶节点添加起始值。（您只能编辑叶节点的起始值。）
- Bus object name — 设置与该端口对应的总线对象变量。默认情况下，该变量使用 `modelDescription.xml` 中定义的结构化变量名称。要在工作区中创建新变量，请使用 `fmudialog.createBusType`。

更改任何变量值都会启用 **Restore output to default settings** 按钮，您可以点击该按钮恢复原始设置。

您可以通过使用 `set_param` 函数设置 `FMUInputMapping` 参数来更改 FMU 模块输入端口布局。该参数可以设置为 `Inherit`、`Flat` 或 `Structured`。默认设置为 `Inherit`。将参数设置为 `Flat` 会将总线输入端口分离为单独的总线元素信号输入端口。将参数设置为 `Structured` 会将单独的总线元素输入端口合并为总线输入端口。

### 输出

此选项卡列出 FMU `modelDescription.xml` 中指定的输出变量和内部变量。

指定结构化输出端口的变量。

要按名称筛选变量，请在文本框中键入变量名称。

变量表列出了层次结构顶部节点及其子节点的变量及其值，其中许多变量可在此选项卡上编辑。

- Name — 变量名称。此项不可编辑。
- Visibility — 选中此复选框可为该变量启用模块上的输出端口。清除此复选框可移除端口。如果此 FMU 中存在内部变量，您可以为各个内部变量启用或禁用可见性。如果选中了某个内部变量，则会创建一个额外的输出端口。

  在顶层节点选中此复选框会使子节点作为模块的一个端口可见。

  **注意**

  当您点击 **Apply** 时，模块端口的数量会发生变化。请记得相应地添加或移除连接。
- Start — 添加在 `modelDescription.xml` 中定义的起始值。您无法更改或添加输出变量的起始值。
- Bus object name — 设置与该端口对应的总线对象变量。默认情况下，该变量使用 `modelDescription.xml` 中定义的结构化变量名称。要在工作区中创建新变量，请使用 `fmudialog.createBusType`。

更改任何变量值都会启用 **Restore output to default settings** 按钮，您可以点击该按钮恢复原始设置。

您可以通过使用 `set_param` 函数设置 `FMUOutputMapping` 参数来更改 FMU 模块输出端口的布局。该参数可设置为 `Inherit`、`Flat` 或 `Structured`。默认设置为 `Inherit`。将参数设置为 `Flat` 会将总线输出端口分离为各个总线元素信号输出端口。将参数设置为 `Structured` 会将各个总线元素输出端口合并为一个总线输出端口。

### 仿真

### **Enable FMU tolerance** — 启用 FMU 容差 off（默认）| on

选中此复选框可启用向 FMU 指定容差值。否则，清除此复选框。

#### 依赖项

此参数仅在您的 FMU 版本或模式支持容差值时适用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FMUIsToleranceUsed` |
| **类型：** 字符向量 |
| **值：** on | off |
| **默认值：** `'off'` |

### **Relative tolerance** — FMU 相对容差 1E-3（默认）| 标量

FMU 相对容差值（%），指定为标量。

#### 依赖项

此参数仅在您的 FMU 版本或模式支持容差值时适用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FMUToleranceValue` |
| **类型：** 字符向量 |
| **值：** `1E-3` | 标量 |
| **默认值：** `'1E-3'` |

### **Simulate FMU using** — 选择用于仿真的二进制文件 x86\_64-windows（默认）| x86-windows | x86\_64-linux

选择用于仿真 FMU 的二进制文件。当 FMU 包含 Linux® 二进制文件时，在 Windows® 上将此选项设置为 `linux64`。

#### 依赖项

在 Windows 上使用 Linux 二进制文件仿真 FMU 需要安装以下产品：

- Simulink Compiler™
- FMU Builder for Simulink 支持包
- Windows Subsystem for Linux (WSL) 版本 2.0.9.0 或更高版本

有关详细信息，请参阅 Simulate FMU with Linux Binary on Windows (Simulink Compiler)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FMUSelectedBinary` |
| **类型：** 字符向量 |
| **值：** `x86_64-windows` | `x86-windows` | `linux64` |
| **默认值：** `'win64'` |

### **Enable event mode** — FMU 事件模式 on（默认）| off

在事件模式下仿真 FMU。

#### 依赖项

此参数仅在 FMU 支持事件模式时启用，并且仅在您的 FMU 用于联合仿真模式且与 FMI 3.0 标准兼容时适用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CSEventModeEnabled` |
| **类型：** 字符向量 |
| **值：** on | off |
| **默认值：** `'on'` |

### **通信步长** — 协同仿真时间点之间的步长 -1（默认）| 正标量

仿真期间的通信步长，指定为标量。
指定模块仿真时间点之间的时间间隔。有关详细信息，请参阅时序注意事项。

在大多数情况下，为防止意外行为，请将此值设置为正值。若要从驱动模块或模型求解器继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

该模块支持不同类型的采样时间，包括连续、离散和继承。然而，常见的协同仿真 FMU 仅支持无偏移的周期性离散采样时间（如正标量）。

#### 依赖关系

此参数仅在协同仿真模式下适用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FMUSampleTime` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认值：** `'-1'` |

### **启用 FMU 调试日志记录** — 启用 FMU 日志显示以用于调试目的 off（默认）| on

要启用 FMU 调试日志的显示，请选中此复选框。否则，请清除此复选框。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FMUDebugLogging` |
| **类型：** 1xN 字符向量元胞数组 |
| **值：** on | off |
| **默认值：** `'off'` |

### **按返回状态筛选日志** — 筛选调试日志 **OK** | **Warning** | **Discard** | **Error** | **Fatal** | **Pending**

按类型筛选调试日志，通过选中以下复选框指定：

- **OK**
- **Warning**
- **Discard**
- **Error**
- **Fatal**
- **Pending**

#### 程序化使用

|  |
| --- |
| **模块参数：** `FMUDebugLoggingFilter` |
| **类型：** 字符向量 |
| **值：** `OK` | `Warning` | `Discard` | `Error` | `Fatal` | `Pending` |
| **默认值：** `'OK'` | `'Warning'` | `'Discard'` | `'Error'` | `'Fatal'` | `'Pending'` |

### **将调试日志重定向到** — 直接流式输出调试日志 `File`（默认）| `Display`

直接调试日志，指定为：

- `File` — 流式输出到 `slprj/_fmu/_logs_modelname/modelname_FMUblockname.txt`。
- `Display` — 流式输出到 MATLAB 命令窗口。

#### 依赖关系

将此参数设置为 `File` 会启用 **Open FMU Log File...** 链接。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FMUDebugLoggingRedirect` |
| **类型：** 字符向量 |
| **值：** `File`| `Display` |
| **默认值：** `'File'` |

### 代码生成

### **调用 FMU 函数使用** — 为生成的代码指定 FMI API 的来源 auto | source code | shared library

为 FMU 模块的生成代码指定 FMI API 的来源。说明生成的代码是使用从源代码内联的 FMU 函数，还是使用函数指针引用来自编译二进制的 FMI API。基于源代码的代码生成是嵌套 FMU、ERT 目标、GRT 目标和快速加速仿真模式的默认选项。有关示例，请参阅使用 FMU 源代码或二进制文件将 FMI API 集成到生成的代码中。

#### 提示

将此选项设置为 `source code`，以使生成的代码能够跨多个平台编译。

#### 依赖关系

此选项仅在 FMU 包包含从 Simulink 生成的源代码时有效。当您的 FMU 仅包含来自外部工具的二进制文件或源代码时，该选项无效，代码生成将使用编译的二进制文件。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FMUCGType` |
| **类型：** 字符向量 |
| **值：** `source code` | `shared library` | `auto` |

## 所属库

Simulink Extras / FMU Import

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `logicala` | `busa` | `doublea` | `integera` | `singlea` | `stringa` |
| **直接馈通** | `yesa` |
| **多维信号** | `yesa` |
| **可变大小信号** | `yesa` |
| **过零检测** | `yesa` |
|  |  |
| --- | --- |
| a 实际数据类型或功能支持取决于模块实现。 | |

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2017b 中引入**

### R2025a：导入并仿真包含 windows 32 位 DLL 的 FMU

在 Simulink 中导入并仿真包含 windows 32 位 DLL 的 FMU。为此，在 FMU 模块对话框的 **Simulation** 选项卡中，将 **Simulate FMU using:** 参数设置为 `x86-windows`。

### R2025a：从其源代码为 FMU 生成代码

使用其打包的源代码为从 Simulink 生成的 FMU 生成代码。基于源代码的代码生成是嵌套 FMU、ERT 目标、GRT 目标和快速加速仿真模式的默认设置。在此之前，为 FMU 生成的代码依赖于其平台特定的已编译二进制文件。

### R2025a：使用恒定周期时钟部署和仿真 FMU 的增强功能

具有恒定周期时钟的独立协同仿真 FMU 模块在仿真和性能方面得到增强。您现在可以：

- 为包含该 FMU 的模型生成代码。
- 在快速加速模式下使用该 FMU 仿真模型。
- 将该 FMU 包含在模型引用中并在加速模式下仿真。
- 生成嵌套 FMU。

### R2024b：基于时间的时钟支持

FMU Import 模块支持导入具有基于时间的时钟的独立协同仿真 FMU。Simulink 将基于时间的 FMU 时钟变量注册为 FMU 模块的采样时间，使该模块能够处理时钟事件更新并与 FMU 同步。

带时钟的 FMU 仿真仅在普通模式仿真中受支持。该模块不支持代码生成。

### R2023b：FMI 3.0 支持

FMU Import 模块支持以下 FMI 3.0 功能：

- 引入新的整数和浮点数据类型。
- 原生支持向量和矩阵。
- 协同仿真模式的事件模式支持。
- 二进制数据类型支持。

### R2023b：模型交换 FMU 中的离散输入值变化触发事件模式

FMU Import 模块检测模型交换 FMU 的离散输入值变化并触发事件迭代。

### R2023b：枚举数据类型支持

FMU Import 模块支持模块输入和输出的枚举数据类型。

## 描述

在模型中包含功能样机单元（FMU）

FMU 模块将现有的功能样机单元（FMU）导入 Simulink®。该模块根据您要导入的现有 FMU 自动选择 FMU 模式：

- `Co-Simulation` — 集成实现功能样机接口（FMI）协同仿真接口的 FMU。这些 FMU 可能包含用于工具耦合的本地求解器。
- `Model Exchange` — 集成实现 FMI 模型交换接口的 FMU。这些 FMU 不包含本地求解器。相反，它们从 Simulink 继承求解器。

该模块支持 FMI 版本 1.0、2.0 和 3.0。对于 FMI 版本 2.0 和 3.0，如果您的 FMU 同时包含协同仿真和模型交换元素，该模块会检测到它们并提示您选择希望该模块运行的模式。

要使用此模块，您必须首先拥有一个现有的 FMU，它可以从其他工具导出，或用 C 语言编写。
