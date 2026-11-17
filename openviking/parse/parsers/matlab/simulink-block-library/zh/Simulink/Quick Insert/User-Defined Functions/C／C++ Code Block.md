---
type: simulink-block
title: 'C Caller'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Quick Insert / User-Defined Functions'
documentation_page: 'ccaller'
documentation_source_path: 'slref/ccaller.html'
language: zh-CN
chinese_source: worker-translation
---

# C Caller

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入端口 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus | string
- name: Port_1
  summary: 输出端口 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated | bus
    | string
```

### 输入

### **Port\_1** — 输入端口 标量 | 向量 | 矩阵

输入端口数量及其名称通过外部 C 代码中所选的函数推断得出。要向 C Caller 模块提供数据，请将输入信号连接到输入端口。

除非在**模块对话框**的**端口规范**下编辑 **Label** 列，否则输入标签与输入端口同名。如果将标签重命名为某个输入端口，C Caller 模块将更改该端口的名称。

对于输入变量，可以使用 **Scope** 列将输入作用域更改为参数或常量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
### 输出

### **Port\_1** — 输出端口 标量 | 向量 | 矩阵

输出端口数量及其名称通过外部 C 代码中所选的函数推断得出。要从 C Caller 模块发送数据，请将模块连接到 C Caller 模块的输出端口。

除非在**模块对话框**的**端口规范**下编辑 **Label** 列，否则输出端口标签与输出端口同名。如果将标签重命名为某个输入端口，C Caller 模块将更改该端口的名称。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string`
## 参数
```yaml
parameters:
- name: Function name
  summary: 函数名称 字符向量 | 字符串标量
  group: ''
  block_parameter: FunctionName
  type: 字符向量或字符串标量
- name: Port specification
  summary: 端口属性 表
  group: ''
  type: FunctionPortSpecification 对象
  block_parameter: FunctionPortSpecification
- name: Available Functions
  summary: 可用函数列表 元胞数组
  group: ''
  block_parameter: AvailableFunctions
  type: 元胞数组
- name: Sample time
  summary: 采样周期 -1（默认）| 标量 | 向量
  group: ''
  block_parameter: SampleTime
  type: 字符串标量或字符向量
  default: '"-1"'
```

### **Function name** — 函数名称 字符向量 | 字符串标量

为 C Caller 模块解析的函数名称，指定为字符向量或字符串标量。有关可用函数的列表，请参阅可用函数。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **模块参数：** `FunctionName` |
| **类型：** 字符向量或字符串标量 |

```
myFunctionName = get_param(gcb,"FunctionName")
```

```
myFunctionName =

    'mean_filter'
```

### **Port specification** — 端口属性 表

端口属性，指定为表。该表指示模块每个输入和输出元素的属性。如果作用域为 `input`，则可以将此变量修改为 `parameter` 或 `constant`。这些属性包括

**Name** — 显示从源代码推断出的变量名称。

粗体参数名称表示该端口或参数为全局参数。

**Scope** — 指示源代码中变量的角色。如果变量是 C Caller 模块源代码中的输入参数，则可以将作用域类型更改为常量或参数。如果变量是源代码中的输出参数，则无法更改作用域类型。

**Label** — 为 Simulink 模型标记输入或输出变量。可以使用此表更改标签。如果作用域为参数，请在此字段中输入参数名称。如果作用域为常量，请输入常量值。

**Type** — 指示来自端口的数据类型。

**Size** — 指示输入和输出数据的大小。

名称、作用域、类型和大小均从源代码推断得出。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FunctionPortSpecification` |
| **类型：** `FunctionPortSpecification` 对象 |

### **Available Functions** — 可用函数列表 元胞数组

可映射到 C Caller 模块的所有可用函数的列表，指定为元胞数组。

模型中的 C Caller 模块会导入外部源代码中的所有函数，并在模块对话框的 Function name 旁边显示函数名称。要在模块中选择并使用某个函数，请确认该函数名称出现在 `Available Functions` 表中。如果缺少某个函数，请单击模块对话框上的 Refresh custom code 按钮重新加载源代码。要更改函数名称，请修改源代码并单击 **Refresh** 按钮重新加载。

#### 程序化使用

|  |
| --- |
| **模块参数：** `AvailableFunctions` |
| **类型：** 元胞数组 |

```
allAvailableFunctions = get_param(gcb, "AvailableFunctions")
```

```
allAvailableFunctions =

  1×1 cell array

    {'add'}
```

### **Sample time** — 采样周期 `-1`（默认）| 标量 | 向量

采样周期，以秒为单位指定。请参阅采样时间类型和指定采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符串标量或字符向量 |
| **默认值**：`"-1"` |
## 所属库

Simulink / User-Defined Functions

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `integera` | `singlea` | `stringa` |
| **直接馈通** | `no` |
| **多维信号** | `yesa` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 实际数据类型或功能支持取决于模块实现。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际数据类型或功能支持取决于模块实现。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2018b 中引入**

### R2024b：与模块和函数接口相关的增强功能

- 当模块调用使用字符指针（`char*`）或字符数组（`char[]`）作为输入或输出数据类型的 C 函数时，模块现在可以在其端口接受 Simulink 字符串。
- 现在可以使用命令行 API 手动将自定义代码中的全局变量作为全局参数添加到模块，或从模块中删除现有的全局参数。此增强功能使您能够更直接地控制模块所调用的自定义代码中全局变量的行为。

## 描述

在 Simulink 中集成 C 代码

C Caller 模块将外部 C 代码集成到 Simulink® 中。此模块导入并列出外部 C 代码中的函数，并使您能够选择已解析的 C 函数以集成到 Simulink 模型中。C Caller 模块独立支持代码生成。对于更复杂的模型，代码生成取决于 Simulink 模型的功能。

要使用 C Caller 模块，请使用**配置参数**下的 **Simulation Target** 定义源代码及任何支持文件。然后，使用**库浏览器** > **Simulink** > **User Defined Functions** 将 C Caller 模块拖到 Simulink 画布上。要更改已定义的源代码文件及其依赖项，请单击模块对话框上的 Configure custom code settings 按钮，转到**配置参数**中的 **Simulation Target** 选项卡。更改源代码或其任何依赖项后，请单击模块对话框上的 Refresh custom code 按钮刷新函数列表。要浏览源代码中的函数定义，请使用 Go to function 按钮图标访问源文件。

可以使用 `addGlobalArg` 函数将自定义代码中的全局变量作为全局参数添加到模块，或使用 `deleteGlobalArg` 函数从模块中删除全局参数。*（自 R2024b 起）*
