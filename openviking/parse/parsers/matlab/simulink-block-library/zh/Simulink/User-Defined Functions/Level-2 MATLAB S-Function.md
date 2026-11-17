---
type: simulink-block
title: 'Level-2 MATLAB S-Function'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'level2matlabsfunction'
documentation_source_path: 'slref/level2matlabsfunction.html'
language: zh-CN
chinese_source: worker-translation
---

# Level-2 MATLAB S-Function

## 端口
```yaml
ports:
- name: In
  summary: Level-2 MATLAB S-Function 模块的信号输入 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Out
  summary: Level-2 MATLAB S-Function 模块的信号输出 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus
```

### 输入

### **In** — Level-2 MATLAB S-Function 模块的信号输入 标量 | 向量 | 矩阵

Level-2 MATLAB S-Function 模块接受模块特性表中列出的类型的输入。有关详细信息，请参阅 Simulink 支持的数据类型。您可以使用 `setup` 回调函数配置输入端口。使用 `setup` 函数指定输入端口数量、输入信号的维度、每个端口的采样时间，以及端口是否为直接馈通。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Out** — Level-2 MATLAB S-Function 模块的信号输出 标量 | 向量 | 矩阵

Level-2 MATLAB S-Function 模块返回的信号输出。您可以使用 `setup` 回调函数配置输入端口。使用 `setup` 函数指定输入端口数量、输入信号的维度以及每个端口的采样时间。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
## 参数
```yaml
parameters:
- name: S-Function Name
  summary: 指定 S-Function 名称 matlabfile（默认）| S-Function 名称
  group: ''
  block_parameter: FunctionName
  type: character vector
  values: '''matlabfile'' | S-Function 名称'
  default: '''matlabfile'''
- name: Parameters
  summary: 指定此模块的参数值 无默认值（默认）
  group: ''
  block_parameter: Parameters
  type: character vector
  values: 模块参数的值
  default: ''' '''
```

### **S-Function Name** — 指定 S-Function 名称 `matlabfile`（默认）| S-Function 名称

指定定义此模块行为的 MATLAB 函数的名称。该 MATLAB 函数必须遵循编写 MATLAB S-Function 的 Level-2 标准（有关详细信息，请参阅编写 Level-2 MATLAB S-Function）。

#### 编程使用

|  |
| --- |
| **模块参数**：`FunctionName` |
| **类型**：character vector |
| **值**：`'matlabfile'` | S-Function 名称 |
| **默认值**：`'matlabfile'` |

### **Parameters** — 指定此模块的参数值 无默认值（默认）

指定此模块的参数值。

#### 编程使用

|  |
| --- |
| **模块参数**：`Parameters` |
| **类型**：character vector |
| **值**：模块参数的值 |
| **默认值**：`' '` |
## 所属库

Simulink / User-Defined Functions

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `doublea` | `fixed pointa` | `integera` | `singlea` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Level-1 MATLAB S-Function 仅支持 double 数据类型。Level-2 MATLAB S-Function 支持 Simulink 支持的所有数据类型。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

- 如果有对应的 TLC 文件可用，Level-2 MATLAB S-Function 模块将使用该 TLC 文件生成代码，否则代码生成将抛出错误。
- 实时代码生成不支持调用 MATLAB 的 S-Function。
- 实际的数据类型或功能支持取决于模块实现。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

Level-1 MATLAB S-Function 仅支持 `double` 数据类型。
Level-2 MATLAB S-Function 支持 Simulink 支持的所有数据类型。

## 版本历史

**在 R2010b 中引入**

## 描述

在模型中使用 Level-2 MATLAB S-Function

此模块允许您在模型中使用 Level-2 MATLAB® S-Function（请参阅编写 Level-2 MATLAB S-Function）。为此，请在模型中创建此模块的实例。然后，在模块参数对话框的 **S-function name** 字段中输入 Level-2 MATLAB S-Function 的名称。

**注意**

使用 S-Function 模块将 Level-1 MATLAB S-Function 包含在模块中。

如果 Level-2 MATLAB S-Function 定义了任何附加参数，您可以在模块参数对话框的 **Parameters** 字段中输入它们。按照 MATLAB S-Function 定义的顺序，将参数输入为求值后等于其值的 MATLAB 表达式。使用逗号分隔每个表达式。

如果模型包含 Level-2 MATLAB S-Function 模块，并且 S-Function 中发生错误，Level-2 MATLAB S-Function 模块将在对话框中显示该错误的 MATLAB 堆栈跟踪信息。单击 **OK** 关闭对话框。
