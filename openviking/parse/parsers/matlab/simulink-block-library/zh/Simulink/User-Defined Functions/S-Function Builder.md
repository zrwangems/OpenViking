---
type: simulink-block
title: 'S-Function Builder'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'sfunctionbuilder'
documentation_source_path: 'slref/sfunctionbuilder.html'
language: zh-CN
chinese_source: worker-translation
---

# S-Function Builder

## 端口
```yaml
ports:
- name: Port_1
  summary: S-function 输入 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    bus
- name: Out
  summary: S-function 输出 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    bus
```

### 输入

### **Port\_1** — S-function 输入 标量 | 向量 | 矩阵

S-Function Builder 模块可以接受实数和复数、一维或二维信号以及非虚拟总线。对于每种情况，信号必须具有 Simulink 支持的数据类型。

有关详细信息，请参阅 Simulink 文档中的 Simulink 支持的数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`
### 输出

### **Out** — S-function 输出 标量 | 向量 | 矩阵

S-Function Builder 可以生成实数和复数、一维或二维信号以及非虚拟总线。对于每种情况，信号必须具有 Simulink 支持的数据类型。

有关详细信息，请参阅 Simulink 文档中的 Simulink 支持的数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`
## 参数
```yaml
parameters:
- name: S-function name
  summary: S-function 的名称 system（默认）| S-function 名称
  group: ''
  block_parameter: FunctionName
  values: '''system''（默认）| 带引号的 S-function 名称'
- name: S-function parameters
  summary: 附加 S-function 参数 MATLAB® 表达式 | 逗号分隔的变量
  group: ''
  block_parameter: Parameters
  values: '''''（默认）| 带引号的 S-function 参数'
- name: S-function modules
  summary: 用于代码生成的附加文件 ''（默认）| 文件名
  group: ''
  block_parameter: SFunctionModules
  values: '''''（默认）| 带引号的文件名'
```

使用 S-Function Builder 编辑器创建用户定义的参数。有关从编辑器创建用户定义参数的详细信息，请参阅 Specify Ports and Parameters for the S-Function。

**注意**

您无需使用模块对话框为此模块设置这些列出的 Simulink 模块参数。Simulink 模块参数使用来自 S-Function Builder 编辑器的信息进行设置。

### **S-function name** — S-function 的名称 `system`（默认）| S-function 名称

使用此参数指定 S-function 的名称。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FunctionName` |
| **值：** | `'system'`（默认）| 带引号的 S-function 名称 |

### **S-function parameters** — 附加 S-function 参数 MATLAB® 表达式 | 逗号分隔的变量

指定附加的 S-function 参数。

函数参数可以指定为 MATLAB 表达式或逗号分隔的变量。例如：

```
A, B, C, D, [eye(2,2);zeros(2,2)]
```

虽然各个参数可以用方括号括起来，但参数列表不得用方括号括起来。

#### 编程方式使用

|  |  |
| --- | --- |
| **参数：** | `Parameters` |
| **值：** | `''`（默认）| 带引号的 S-function 参数 |

### **S-function modules** — 用于代码生成的附加文件 `''`（默认）| 文件名

此参数仅当此模块表示 C MEX S-function 并且您打算使用 Simulink Coder™ 软件从包含该模块的模型生成代码时适用。如果使用它，当您准备生成代码时，必须强制代码生成器重新构建顶层模型，如 Control Regeneration of Top Model Code (Simulink Coder) 中所述。

有关使用此参数的详细信息，请参阅 Specify Additional Source Files for an S-Function (Simulink Coder)。

#### 编程方式使用

|  |  |
| --- | --- |
| **参数：** | `SFunctionModules` |
| **值：** | `''`（默认）| 带引号的文件名 |
## 所属库

Simulink / User-Defined Functions

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

调用 MATLAB 的 S-function 不支持代码生成。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

集成 C 或 C++ 代码以创建 S-function

S-function Builder 模块集成新的或现有的 C 或 C++ 代码，并根据您提供的规范创建 C MEX S-function（系统函数）。C MEX S-function 是用 C 或 C++ 编写的 Simulink® 模块的计算机语言描述。S-function 使用称为 S-function API 的特殊调用语法，使您能够与 Simulink 引擎交互。这种交互与引擎和内置 Simulink 模块之间发生的交互非常相似。要了解有关 C MEX S-function 的更多信息，请参阅 What Is an S-Function?。要了解有关使用 S-function Builder 模块构建 C MEX S-function 的更多信息，请参阅 Build S-Functions Automatically Using S-Function Builder。有关包含逐步过程的示例，请参阅 Use a Bus with S-Function Builder to Create an S-Function。

S-Function Builder 模块的实例还充当 Simulink 模型中生成的 S-function 的包装器。当仿真包含 S-Function Builder 模块实例的模型时，Simulink 调用生成的 C MEX S-function，以在 `mdlStart`、`mdlOutputs`、`mdlDerivatives`、`mdlUpdate` 和 `mdlTerminate` 方法的实例中调用您的 C 或 C++ 代码。要了解 Simulink 引擎如何与 S-function 交互，请参阅 Simulink Engine Interaction with C S-Functions。

**注意**

S-Function Builder 模块不支持封装。但是，您可以封装包含 S-Function Builder 模块的 Subsystem 模块。有关详细信息，请参阅 Create Library Blocks Using Self-Modifiable Masks and Variant Blocks。
