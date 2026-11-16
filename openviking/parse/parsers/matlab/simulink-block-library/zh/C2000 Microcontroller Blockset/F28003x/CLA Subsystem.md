---
type: simulink-block
title: 'CLA Subsystem'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2803x'
documentation_page: 'clasubsystem'
documentation_source_path: 'ref/clasubsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# CLA Subsystem

## 端口

### 输入

### **In** — 子系统的信号输入 标量 | 向量 | 矩阵

将 Inport 模块放置在子系统中会向 Subsystem 模块添加一个外部输入端口。端口标签与 Inport 模块的名称匹配。

使用 Inport 模块从局部环境获取信号。

**数据类型：** `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Out** — 子系统的信号输出 标量 | 向量 | 矩阵

将 Outport 模块放置在子系统中会为 Subsystem 模块添加一个输出端口。Subsystem 模块上的端口标签是 Outport 模块的名称。

使用 Outport 模块将信号发送到局部环境。

**数据类型：** `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

代码生成选项卡上的参数需要 Simulink® Coder™ 或 Embedded Coder® 许可证。

### 主要

### **显示端口标签** — 端口标签的显示选项 `FromPortIcon`（默认） | `FromPortBlockName` | `SignalName`

选择如何在 Subsystem 模块图标上显示端口标签。

`none`
:   不显示端口标签。

`FromPortIcon`
:   如果对应端口图标显示信号名称，则在 Subsystem 模块上显示该信号名称。否则，显示端口模块名称；如果模块名称是默认名称，则显示端口号。

`FromPortBlockName`
:   在 Subsystem 模块上显示对应端口模块的名称。

`SignalName`
:   如果连接到端口的信号已命名，则在 Subsystem 模块上显示该信号的名称。否则，显示对应端口模块的名称。

#### 编程方式使用

|  |
| --- |
| **参数**: `ShowPortLabels` |
| **类型**: character vector |
| **值**: `'FromPortIcon'` | `'FromPortBlockName'` | `'SignalName'` |
| **默认**: `'FromPortIcon'` |

### **读/写权限** — 对子系统内容的访问级别 `ReadWrite`（默认） | `ReadOnly` | `NoReadOrWrite`

控制用户对子系统内容的访问。

`ReadWrite`
:   启用打开和修改子系统内容。

`ReadOnly`
:   启用打开但不允许修改子系统。如果子系统位于模块库中，可以创建并打开指向该子系统的链接，并且可以创建和修改该子系统的本地副本，但不能更改权限或修改原始库实例的内容。

`NoReadOrWrite`
:   禁用打开或修改子系统。如果子系统位于库中，可以在模型中创建指向该子系统的链接，但不能打开、修改、更改权限或创建该子系统的本地副本。

**注意**

如果尝试查看 **读/写权限** 参数设置为 `NoReadOrWrite` 的子系统的内容，则不会收到响应。例如，双击此类子系统时，Simulink 不会打开该子系统，也不会显示任何消息。

#### 编程方式使用

|  |
| --- |
| **参数**: `Permissions` |
| **类型**: character vector |
| **值**: `'ReadWrite'` | `'ReadOnly'` | `'NoReadOrWrite'` |
| **默认**: `'ReadWrite'` |

### **错误回调函数名称** — 发生错误时要调用的函数名称 `''`（默认） | 函数名

输入当 Simulink 执行子系统期间发生错误时要调用的函数名称。

Simulink 向该函数传递两个参数：子系统的句柄和一个指定错误类型的 character vector。如果未指定函数，则当执行子系统导致错误时，Simulink 会显示一般错误消息。

#### 编程方式使用

|  |
| --- |
| **参数**: `ErrorFcn` |
| **类型**: character vector |
| **值**: `''` | `'<function name>'` |
| **默认**: `''` |

### **允许层次化解析** — 工作区变量名称的解析 `All`（默认） | `ExplicitOnly` | `None`

选择是否解析此子系统引用的工作区变量名称。

有关详细信息，请参阅符号解析和符号解析过程。

`All`
:   解析此子系统使用的所有工作区变量名称，包括用于指定模块参数值和 Simulink 数据对象（例如 `Simulink.Signal` 对象）的那些名称。

`ExplicitOnly`
:   仅解析用于指定模块参数值、数据存储内存（不存在对应模块时）、信号以及标记为 “must resolve” 的状态的工作区变量名称。

`None`
:   不解析任何工作区变量名称。

#### 编程方式使用

|  |
| --- |
| **参数**: `PermitHierarchicalResolution` |
| **类型**: character vector |
| **值**: `'All'` | `'ExplicitOnly'` | `'None'` |
| **默认**: `'All'` |

### 代码生成

### **函数封装** — 代码格式 `Nonreusable function`（默认） | `Inline`

选择要为 CLA 子系统生成的代码格式。

**注意**

CLA Subsystem 模块不支持 `Auto` 和 `Reusable function` 代码格式。

`Inline`
:   Simulink Coder 和 Embedded Coder 无条件地内联该子系统，并且整个算法内联到 CLA 任务 (.cla) 文件。有关更多信息，请参阅 Method 2 - Inline Code Generation for CLA Subsystem

`Nonreusable function`
:   在此子系统中，CLA 中的算法代码与数据一起生成到单独的 `.C` 文件中。有关更多信息，请参阅 Method 1 - Nonreusable Function Code Generation for CLA Subsystem (Recommended)。

    使用此设置的子系统生成的函数可能具有参数，具体取决于 **函数接口** 参数设置。可以使用 **函数名称** 和 **文件名（无扩展名）** 参数命名生成的函数和文件。这些函数不可重入。

#### 依赖关系

- 此参数需要 Simulink Coder 才能进行代码生成。

#### 编程方式使用

|  |
| --- |
| **参数**: `RTWSystemCode` |
| **类型**: character vector |
| **值**: | `'Inline'` | `'Nonreusable function'` | |
| **默认**: `'Nonreusable function'` |

### **函数名称选项** — 如何命名生成的函数 `Auto`（默认） | `Use subsystem name` | `User specified`

选择 Simulink Coder 如何命名其为子系统生成的函数。

如果拥有 Embedded Coder 许可证，可以使用配置参数 **Code Generation** > **Identifiers** 窗格上的选项控制函数名称。

`Auto`
:   使用默认命名约定 `model_subsystem()` 分配唯一函数名称，其中 *`model`* 是模型的名称，*`subsystem`* 是子系统的名称（或代码重用时代码相同子系统的名称）。

`Use subsystem name`
:   将子系统名称用作函数名称。默认情况下，函数名称使用命名约定 `model_subsystem`。

`User specified`
:   启用 **函数名称** 字段。输入任何合法的 C 或 C++ 函数名称，该名称必须唯一。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **函数封装** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 编程方式使用

|  |
| --- |
| **参数**: `RTWFcnNameOpts` |
| **类型**: character vector |
| **值**: `'Auto'` | `'Use subsystem name'` | `'User specified'` |
| **默认**: `'Auto'` |

### **函数名称** — 子系统代码的函数名称 `''`（默认） | 函数名

为子系统代码指定唯一、合法的 C 或 C++ 函数名称。

如果希望为函数指定特定名称，而不是让 Simulink Coder 代码生成器分配其自动生成的名称或使用子系统名称，请使用此参数。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **函数名称选项** 参数设置为 `User specified`。

#### 编程方式使用

|  |
| --- |
| **参数**: `RTWFcnName` |
| **类型**: character vector |
| **值**: `''` | `'<function name>'` |
| **默认**: `''` |

### **文件名选项** — 如何命名生成的文件 `User specified`（默认）

选择 Simulink Coder 如何为其为 CLA 子系统生成的函数命名单独文件。确保为 CLA Subsystem 将 **文件名选项** 参数设置为 `User specified`。

`User specified`
:   此选项启用 **文件名（无扩展名）** 文本输入字段。代码生成器使用您输入的名称作为文件名。输入任何文件名，但不要包含 `.c` 或 `.cpp`（或任何其他）扩展名。此文件名不必唯一。

    **注意**

    虽然子系统源文件名不必唯一，但必须避免使用会导致循环依赖的非唯一名称（例如，`sys_a.h` 包含 `sys_b.h`，`sys_b.h` 包含 `sys_c.h`，`sys_c.h` 包含 `sys_a.h`）。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **函数封装** 设置为 `Nonreusable function`。

#### 编程方式使用

|  |
| --- |
| **参数**: `RTWFileNameOpts` |
| **类型**: character vector |
| **值**: `'User specified'` |
| **默认**: `'User specified'` |

### **文件名（无扩展名）** — 生成文件的名称 `sample_cla`（默认） | 文件名

CLA 内部的算法生成在源文件中。（例如 `sample_cla.c`，它包含 `sample_cla.h`）。指定的文件名不必唯一。但是，避免使用会导致循环依赖的非唯一名称（例如，`sys_a.h` 包含 `sys_b.h`，`sys_b.h` 包含 `sys_c.h`，`sys_c.h` 包含 `sys_a.h`）。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **文件名选项** 设置为 `User specified`。

#### 编程方式使用

|  |
| --- |
| **参数**: `RTWFileName` |
| **类型**: character vector |
| **值**: `''` | `'<file name>'` |
| **默认**: `''` |

### **函数接口** — 选择生成的函数是否使用参数 `void_void`（默认）

选择生成的函数是否使用参数。确保为 CLA Subsystem 将 **函数接口** 参数设置为 `void_void`。

`void_void`
:   生成一个不带参数的函数，并将数据作为全局变量传递。例如：

    ```
    void subsystem_function(void)
    ```

有关更多信息，请参阅：

- Reduce Global Variables in Nonreusable Subsystem Functions (Embedded Coder)
- Generate Modular Function Code for Nonvirtual Subsystems (Embedded Coder)

#### 依赖关系

- 要启用此参数，请将 **函数封装** 设置为 `Nonreusable function`。

#### 编程方式使用

|  |
| --- |
| **参数**: `FunctionInterfaceSpec` |
| **类型**: character vector |
| **值**: `'void_void'` |
| **默认**: `'void_void'` |

### **具有单独数据的函数** — 控制子系统的代码生成 on（默认） | off

生成子系统函数代码，其中原子子系统的内部数据与其父模型分离，并由该子系统拥有。

off
:   不生成这样的子系统函数代码：其中原子子系统的内部数据与其父模型分离并由该子系统拥有。

on
:   生成子系统函数代码，其中原子子系统的内部数据与其父模型分离，并由该子系统拥有。子系统数据结构独立于父模型数据结构进行声明。具有单独数据的子系统拥有自己的模块 I/O 和 `DWork` 数据结构。因此，为子系统生成的代码更易于跟踪和测试。数据分离还倾向于减小整个模型中全局数据结构的最大大小，因为它们被拆分为多个数据结构。

    **注意**

    建议将 **具有单独数据的函数** 参数设置为 `on`。

有关如何为原子子系统生成模块化函数代码的详细信息，请参阅 Generate Modular Function Code for Nonvirtual Subsystems (Embedded Coder)。

有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 要启用此参数，请将 **函数封装** 设置为 `Nonreusable function`。

#### 编程方式使用

|  |
| --- |
| **参数**: `FunctionWithSeparateData` |
| **类型**: character vector |
| **值**: `'off'` | `'on'` |
| **默认**: `'on'` |

### **初始化/终止函数的内存段** — 选择如何应用内存段 `C28xFunction`（默认）

选择 Embedded Coder 如何将内存段应用于子系统初始化函数和终止函数。对于 CLA Subsystem，请选择 `C28xFunction`。使用此选择后，初始化函数和终止函数会受到 CLA 编译器标签保护，因此仅由 C28x 编译器编译。

**注意**

确保模型加载了定义了 C28xFunction 的 **tic2000demospkg** 包。

例如，如果初始化函数的名称是 `subsystem_initialize`，则

```
#ifndef __TMS320C28XX_CLA__
void subsystem_initialize()
{
//body of the function
}
#endif
```

#### 依赖关系

- 要启用此参数，请将 **函数封装** 设置为 `Nonreusable function`。

#### 编程方式使用

|  |
| --- |
| **参数**: `RTWMemSecFuncInitTerm` |
| **类型**: character vector |
| **值**: `C28xFunction` |
| **默认**: `C28xFunction` |

### **执行函数的内存段** — 选择如何应用内存段 `ClaFunction`（默认）

选择 Embedded Coder 如何将内存段应用于子系统执行函数。对于 CLA Subsystem，请选择 `ClaFunction`。使用此选择后，执行函数会受到 CLA 编译器标签保护，因此仅由 CLA 编译器编译。

**注意**

确保模型加载了定义了 ClaFunction 的 **tic2000demospkg** 包。

例如，如果执行函数的名称是 `subsystem`，则

```
#ifdef __TMS320C28XX_CLA__
void subsystem()
{
//body of the function
}
#endif
```

#### 依赖关系

- 要启用此参数，请将 **函数封装** 设置为 `Nonreusable function`。

#### 编程方式使用

|  |
| --- |
| **参数**: `RTWMemSecFuncExecute` |
| **类型**: character vector |
| **值**: `ClaFunction` |
| **默认**: `ClaFunction` |

### **常量的内存段** — 选择如何应用内存段 `ClaDataRAM`（默认）

选择 Embedded Coder 如何将内存段应用于子系统常量。对于 CLA Subsystem，请选择 `ClaDataRAM`。常量的内存段参数允许将常量存储在 CLA 数据 RAM 中。

确保模型加载了定义了 ClaDataRAM 的 **tic2000demospkg** 包。

#### 依赖关系

- 要启用此参数，请将 **函数封装** 设置为 `Nonreusable function`，并选择 **具有单独数据的函数** 参数。

#### 编程方式使用

|  |
| --- |
| **参数**: `RTWMemSecDataConstants` |
| **类型**: character vector |
| **值**: `ClaDataRAM` |
| **默认**: `ClaDataRAM` |

### **内部数据的内存段** — 选择如何应用内存段 `ClaDataRAM`（默认）

选择 Embedded Coder 如何将内存段应用于子系统内部数据。对于 CLA Subsystem，请选择 `ClaDataRAM`。内部数据的内存段参数允许将内部数据存储在 CLA 数据 RAM 中。

#### 依赖关系

- 要启用此参数，请将 **函数封装** 设置为 `Nonreusable function`，并选择 **具有单独数据的函数** 参数。

#### 编程方式使用

|  |
| --- |
| **参数**: `RTWMemSecDataInternal` |
| **类型**: character vector |
| **值**: `ClaDataRAM` |
| **默认**: `ClaDataRAM` |

### **参数的内存段** — 选择如何应用内存段 `ClaDataRAM`（默认）

选择 Embedded Coder 如何将内存段应用于子系统参数。对于
CLA Subsystem，选择 `ClaDataRAM`。参数的内存段
允许参数存储在 CLA 数据
RAM 中

#### 依赖项

- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function`，并选择
  **具有独立数据的函数** 参数。

#### 编程用法

|  |
| --- |
| **参数**：`RTWMemSecDataParameters` |
| **类型**：character vector |
| **值**：`ClaDataRAM` |
| **默认值**：`ClaDataRAM` |

### 子系统引用

### **子系统文件名** — 被引用子系统的文件名 string | character vector

#### 依赖项

要访问此参数，请点击 **Convert**
按钮。

有关如何将子系统转换为引用子系统的更多信息，请参阅 Convert Subsystem to a Referenced Subsystem。

## 所属库

C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2021b 中引入**

## 描述

对模块进行分组以在 CLA 内执行算法

CLA Subsystem 模块包含模型或系统中的一部分模块。CLA Subsystem 是由 CLA Task 模块触发的触发子系统。

CLA Subsystem 模块只能与 CLA Task 模块一起使用。

CLA Subsystem 要求在具有有效 TI C2000™ 硬件板的模型中加载 `tic2000demospkg` 包。要在模型中加载 `tic2000demospkg` 包，请遵循以下步骤。

- 在 Simulink 工具条中，导航到 **Apps**，然后点击
  **Embedded Coder**。

  CLA-APPS
- 转到 **C Code**  > **Code Interface**，然后点击 **Embedded Coder Dictionary
  (Model)**。

  Code-Interface
- 在 Embedded Coder Dictionary 窗口中，转到 **Storage
  Class**，然后点击 **Manage Packages**。如果
  找不到 `tic2000demospkg`，请点击
  **Refresh** 并加载包。有关更多信息，
  请参阅 Data Exchange Between CLA and C28x CPU。

  Manage packages

**注意**

- 要详细了解如何将子系统用于 CLA，请参阅 Overview of CLA Configuration for C2000 Processors Using Subsystem。
- CLA Subsystem 模块派生自 Subsystem 模块，并具有特定于 CLA 的附加参数配置。建议使用此模块中提供的选项，以便成功使用 CLA Subsystem。
- 并非所有 TI C2000 硬件板变体都支持 CLA。例如，在 TI Piccolo F2805x 处理器系列中，只有 F28055 和 F28053 处理器支持 CLA，而 F28054、F28052、F28051 和 F28050 处理器不支持。
