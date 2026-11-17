---
type: simulink-block
title: 'FIS Tree'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'fistreeblock'
documentation_source_path: 'fistreeblock.html'
language: zh-CN
chinese_source: worker-translation
---

# FIS Tree

## 端口
```yaml
ports:
- name: in
  summary: 输入信号 标量 | 向量
  direction: input
- name: out
  summary: 去模糊化输出信号 标量 | 向量
  direction: output
```

### 输入

### **in** — 输入信号 标量 | 向量

对于单输入 FIS 树，输入为标量信号。对于多输入 FIS 树，使用以下模块将输入合并为向量信号：

- Mux (Simulink)
- Vector Concatenate (Simulink)
- Bus Creator (Simulink)
### 输出

### **out** — 去模糊化输出信号 标量 | 向量

对于单输出 FIS 树，输出为标量信号。对于多输出 FIS 树，输出为向量信号。要将系统输出拆分为标量信号，请使用 Demux (Simulink) 模块。
## 参数
```yaml
parameters:
- name: FIS tree name
  summary: 要评估的 FIS 树 fistree 对象 | 带引号的 MAT 文件名
  group: 常规
  block_parameter: FIS
  values: '''"weightedTipper"''（默认）| 带引号的变量名 | 带引号的文件名'
- name: Number of samples for output discretization
  summary: 输出模糊集中的点数 101（默认）| 大于 1 的整数
  group: 常规
  block_parameter: OutputSampleNumber
  values: '"101"（默认）| 带引号的、大于 1 的整数'
- name: Data type
  summary: 信号数据类型 double（默认）| single | fixed-point | expression
  group: 常规
  block_parameter: DataType
  values: '"double"（默认）| "single" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)"'
- name: Simulate using
  summary: 仿真模式 Interpreted execution（默认）| Code generation
  group: 常规
  block_parameter: SimulateUsing
  values: '"Interpreted execution"（默认） | "Code generation"'
- name: 输入值超出范围
  summary: 输入超出范围时的诊断消息行为 warning（默认） | error | none
  group: 诊断
  block_parameter: OutOfRangeInputValueMessage
  values: '"warning"（默认） | "error" | "none"'
- name: 未触发规则
  summary: 未触发任何规则时的诊断消息行为 warning（默认） | error | none
  group: 诊断
  block_parameter: NoRuleFiredMessage
  values: '"warning"（默认） | "error" | "none"'
- name: 输出模糊集为空
  summary: 输出模糊集为空时的诊断消息行为 warning（默认） | error | none
  group: 诊断
  block_parameter: EmptyOutputFuzzySetMessage
  values: '"warning"（默认） | "error" | "none"'
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink 工具条的**仿真**选项卡中，在**准备**库中选择**属性检查器**。

### 常规

### **FIS tree name** — 要评估的 FIS 树 `fistree` 对象 | 带引号的 MAT 文件名

要评估的 FIS 树，指定为以下之一：

- MATLAB® 工作区中的 `fistree` 对象。
- 当前工作文件夹或 MATLAB 路径上的 MAT 文件（`*.mat`）的名称。该 MAT 文件必须仅包含一个 FIS 对象。文件名中包含文件扩展名是可选的。用引号指定文件名。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `FIS` |
| **值：** | `'"weightedTipper"'`（默认）| 带引号的变量名 | 带引号的文件名 |

### **Number of samples for output discretization** — 输出模糊集中的点数 101（默认）| 大于 `1` 的整数

用于离散化 FIS 输出变量范围的采样数，指定为大于 `1` 的整数。此值对应于每条规则的输出模糊集中的点数。

要在评估 Mamdani FIS 时减少内存使用量，请指定较低的采样数。这样做会牺牲去模糊化输出值的精度。指定较低的采样数可能会使去模糊化的输出面积为零。在这种情况下，去模糊化输出值为输出变量范围的中点。

**注意**

该模块在评估 Sugeno FIS 时忽略此参数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutputSampleNumber` |
| **值：** | `"101"`（默认）| 带引号的、大于 `1` 的整数 |

### **Data type** — 信号数据类型 `double`（默认）| `single` | `fixed-point` | `expression`

信号数据类型，指定为以下之一：

- `double` — 双精度信号
- `single` — 单精度信号
- `fixdt(1,16,0)` — 采用二进制小数点定标的定点信号
- `fixdt(1,16,2^0,0)` — 采用斜率和偏置定标的定点信号
- Expression — 求值为上述数据类型之一的表达式

对于定点数据类型，您可以使用**数据类型助手**配置符号性、字长和定标参数。有关详细信息，请参阅指定定点数据类型 (Simulink)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `DataType` |
| **值：** | `"double"`（默认）| `"single"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` |

### **Simulate using** — 仿真模式 `Interpreted execution`（默认）| `Code generation`

仿真模式，指定为以下值之一：

- `Interpreted execution` — 使用针对 `single` 和 `double` 数据类型的预编译 MEX 文件仿真模糊系统。使用此选项可减少模型的初始编译时间。
- `Code generation` — 在不使用预编译 MEX 文件的情况下仿真模糊系统。在针对代码生成应用仿真模糊系统时使用此选项。

对于定点数据类型，FIS Tree 模块始终使用 `Code generation` 模式进行仿真。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SimulateUsing` |
| **值：** | `"Interpreted execution"`（默认） | `"Code generation"` |

### 诊断

### **输入值超出范围** — 输入超出范围时的诊断消息行为 `warning`（默认） | `error` | `none`

输入超出范围时的诊断消息行为，指定为以下之一：

- `warning` — 将诊断消息报告为警告。
- `error` — 将诊断消息报告为错误。
- `none` — 不报告诊断消息。

当输入值超出范围时，模糊系统中相应的规则可能具有意外的触发强度。

#### 依赖关系

- 仅当 **Simulate using** 参数为 `Interpreted execution` 时，才提供诊断消息。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutOfRangeInputValueMessage` |
| **值：** | `"warning"`（默认） | `"error"` | `"none"` |

### **未触发规则** — 未触发任何规则时的诊断消息行为 `warning`（默认） | `error` | `none`

当给定输出变量未触发任何规则时的诊断消息行为，指定为以下之一：

- `warning` — 将诊断消息报告为警告。
- `error` — 将诊断消息报告为错误。
- `none` — 不报告诊断消息。

当 **No rule fired** 为 `warning` 或 `none` 且给定输出未触发任何规则时，去模糊化输出值设置为其范围均值。

#### 依赖关系

- 仅当 **Simulate using** 参数为 `Interpreted execution` 时，才提供诊断消息。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `NoRuleFiredMessage` |
| **值：** | `"warning"`（默认） | `"error"` | `"none"` |

### **输出模糊集为空** — 输出模糊集为空时的诊断消息行为 `warning`（默认） | `error` | `none`

输出模糊集为空时的诊断消息行为，指定为以下之一：

- `warning` — 将诊断消息报告为警告。
- `error` — 将诊断消息报告为错误。
- `none` — 不报告诊断消息。

当 **Empty output fuzzy set** 为 `warning` 或 `none` 且输出模糊集为空时，相应输出的去模糊化值设置为其范围均值。

#### 依赖关系

- 此诊断消息仅适用于 Mamdani 系统。
- 仅当 **Simulate using** 参数为 `Interpreted execution` 时，才提供诊断消息。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `EmptyOutputFuzzySetMessage` |
| **值：** | `"warning"`（默认） | `"error"` | `"none"` |
## 所属库

Fuzzy Logic Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2024a 中引入**

## 描述

评估模糊推理系统树

FIS Tree 模块在 Simulink® 中实现模糊推理系统（FIS）树。您使用 **FIS tree name** 参数指定要评估的 FIS 树。

有关 FIS 树的详细信息，请参阅 FIS Trees。
