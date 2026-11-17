---
type: simulink-block
title: 'Fuzzy Logic Controller'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'fuzzylogiccontroller'
documentation_source_path: 'fuzzylogiccontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# Fuzzy Logic Controller

## 端口

### 输入

### **in** — 输入信号 标量 | 向量

对于单输入模糊推理系统，输入为标量信号。对于多输入模糊系统，使用以下模块将输入合并为向量信号：

- Mux (Simulink)
- Vector Concatenate (Simulink)
- Bus Creator (Simulink)
### 输出

### **out** — 去模糊化输出信号 标量 | 向量

对于单输出 FIS，输出为标量信号。对于多输出 FIS，输出为向量信号。要将系统输出拆分为标量信号，请使用 Demux (Simulink) 模块。

### **fi** — 模糊化输入值 矩阵

模糊化输入值，通过在当前输入值下评估每条规则的输入隶属度函数获得。

对于 type-1 FIS，**fi** 是一个 *NR*×*NU* 矩阵信号，其中 *NR* 是 FIS 规则数。**fi** 的元素 (*i*,*j*) 是第 *i* 条规则中第 *j* 个输入的输入隶属度函数值。

对于 type-2 FIS，**fi** 是一个 *NR*×(2\**NU*) 矩阵信号。前 *NU* 列包含每条规则上隶属度函数的模糊化值，后 *NU* 列包含下隶属度函数的模糊化值。

有关模糊化输入值的详细信息，请参阅 Fuzzify Inputs。

#### 依赖

要启用此端口，请选中 **Fuzzified inputs (fi)** 参数。

### **rfs** — 规则触发强度 列向量

规则触发强度，通过评估每条规则的前件获得；即对模糊化输入值应用模糊算子。

对于 type-1 FIS，**rfs** 是长度为 *NR* 的列向量信号，其中 *NR* 是规则数，元素 *i* 是第 *i* 条规则的触发强度。

对于 type-2 FIS，**rfs** 是一个 *NR*×2 矩阵信号。第一列包含使用上隶属度函数生成的规则触发强度，第二列包含使用下隶属度函数生成的规则触发强度。

有关应用模糊算子的详细信息，请参阅 Apply Fuzzy Operator。

#### 依赖

要启用此端口，请选中 **Rule firing strengths (rfs)** 参数。

### **ro** — 规则输出 矩阵

规则输出，通过使用 FIS 中指定的蕴含方法将规则触发强度应用于输出隶属度函数获得。

对于 type-1 Mamdani FIS，**ro** 是一个 *NS*×(*NR*\**NY*) 矩阵信号，其中 *NR* 是规则数，*NY* 是输出数，*NS* 是用于评估输出变量范围的采样点数。**ro** 的每一列包含一条规则的输出模糊集。前 *NR* 列包含第一个输出变量的规则输出，接下来的 *NR* 列对应第二个输出变量，依此类推。

对于 type-2 Mamdani FIS，**ro** 是一个 *NS*×(2\**NR*\**NY*) 矩阵信号。前 *NR*\**NY* 列包含使用上隶属度函数生成的规则输出，后 *NR*\**NY* 列包含使用下隶属度函数生成的规则输出。

对于 type-1 Sugeno 系统，每条规则输出为标量值。在这种情况下，**ro** 是一个 *NR*×*NY* 矩阵信号。**ro** 的元素 (*j*,*k*) 是第 *j* 条规则的第 *k* 个输出变量的值。

对于 type-2 Sugeno 系统，**ro** 是一个 *NR*×(3\**NY*) 数组。前 *NY* 列包含规则输出水平。接下来的 *NY* 列包含使用上隶属度函数生成的对应规则触发强度。最后 *NY* 列包含使用下隶属度函数生成的规则触发强度。例如，在三输出系统中，第 4 列和第 7 列包含第 1 列中输出水平的触发强度。

有关模糊蕴含的详细信息，请参阅 Apply Implication Method。

#### 依赖

- 要启用此端口，请选中 **Rule outputs (ro)** 参数。
- 要指定 *NS*，请使用 **Number of samples for output discretization** 参数。

### **ao** — 聚合输出矩阵 | 行向量

每个输出变量的聚合输出，通过使用 FIS 中指定的聚合方法将所有规则的相应输出组合而获得。

对于 1 型 Mamdani 模糊推理系统，每个输出变量的聚合结果是一个模糊集。在这种情况下，**ao** 是一个 *NS*×*NY* 矩阵信号，其中 *NY* 是输出数量，*NS* 是用于评估输出变量范围的采样点数量。**ao** 的每一列包含一个输出变量的聚合模糊集。

对于 2 型 Mamdani FIS，每个输出变量的聚合结果是一个模糊集。在这种情况下，**ao** 是一个 *NS*×(2\**NY*) 矩阵信号。前 *NY* 列包含使用上隶属函数生成的聚合输出，后 *NY* 列包含使用下隶属函数生成的聚合输出。

对于 1 型 Sugeno 系统，每个输出变量的聚合结果是一个标量值。在这种情况下，**ao** 是一个长度为 *NY* 的行向量，其中元素 *k* 是第 *k* 个输出变量的规则输出之和。

对于 2 型 Sugeno 系统，**ao** 是一个 *NR*×(3\**NY*) 数组。**ro** 包含与 **ao** 相同的数据，但列按输出水平排序。例如，在一个三输出系统中，当第 1 列中的输出水平被排序时，第 4 列和第 7 列中相应的触发强度会相应调整。

有关模糊聚合的更多信息，请参阅聚合所有输出。

#### 依赖关系

- 要启用此端口，请选择 **Aggregated outputs (ao)** 参数。
- 要指定 *NS*，请使用 **Number of samples for output discretization** 参数。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### 常规

### **FIS name** — 要评估的模糊推理系统 `mamfis` 对象 | `sugfis` 对象 | `mamfistype2` 对象 | `sugfistype2` 对象 | 带引号的 FIS 文件名 | 带引号的 MAT 文件名

要评估的模糊推理系统，指定为以下之一：

- `mamfis` 或 `sugfis` 对象 — 在 MATLAB® 工作区中指定 1 型 FIS 对象的名称。
- `mamfistype2` 或 `sugfistype2` 对象 — 在 MATLAB 工作区中指定 2 型 FIS 对象的名称。
- 当前工作文件夹或 MATLAB 路径上的 FIS 文件（`*.fis`）名称。文件名中包含文件扩展名是可选的。用引号指定文件名。
- 当前工作文件夹或 MATLAB 路径上的 MAT 文件（`*.mat`）名称。MAT 文件必须仅包含一个 FIS 对象。文件名中包含文件扩展名是可选的。用引号指定文件名。*（自 R2024a 起）*

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `FIS` |
| **值：** | `'"tipper.fis"'`（默认）| 带引号的变量名 | 带引号的文件名 |

### **Design** — 打开模糊逻辑设计器按钮

打开模糊逻辑设计器以查看和修改 FIS 设计。然后您可以更新模块以使用修改后的 FIS 设计。有关更多信息，请参阅在 Simulink 中设计模糊推理系统。

### **Number of samples for output discretization** — 输出模糊集的点数 101（默认）| 大于 `1` 的整数

用于离散化 FIS 输出变量范围的采样点数，指定为大于 `1` 的整数。该值对应于每条规则输出模糊集中的点数。

为了在评估 Mamdani FIS 时减少内存使用量，请指定较低的采样点数。这样做会牺牲去模糊化输出值的精度。指定较低的采样点数可能导致去模糊化的输出区域为零。在这种情况下，去模糊化的输出值为输出变量范围的中点。

**注意**

该模块在评估 Sugeno FIS 时忽略此参数。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `OutputSampleNumber` |
| **值**：| `"101"`（默认）| 带引号的大于 `1` 的整数 |

### **Data type** — 信号数据类型 `double`（默认）| `single` | `fixed-point` | `expression`

信号数据类型，指定为以下之一：

- `double` — 双精度信号
- `single` — 单精度信号
- `fixdt(1,16,0)` — 二进制小数点定标的定点信号
- `fixdt(1,16,2^0,0)` — 斜率和偏置定标的定点信号
- Expression — 求值为上述数据类型之一的表达式

对于定点数据类型，您可以使用 **Data Type Assistant** 配置有符号性、字长和定标参数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type (Simulink)。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `DataType` |
| **值**：| `"double"`（默认）| `"single"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` |

### **Implement FIS as lookup table** — 将 FIS 转换为查找表 `off`（默认）| `on`

*自 R2025a 起*

为了减少控制器的处理时间，您可以将 FIS 表示为查找表。

该模块根据断点数量将每个 FIS 输入的输入范围划分为大小相等的区域，断点数量由 **Number of input breakpoints** 参数指定。

对于每种输入组合，该模块计算相应的 FIS 输出。在评估期间，控制器使用这些预计算的输出，而不是执行模糊推理过程。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `UseLookupTable` |
| **值**：| `"off"`（默认）| `"on"` |

### **Number of input breakpoints (samples)** — 查找表断点数量 `10`（默认）| 正整数

*自 R2025a 起*

查找表断点数量，指定为正整数。增加断点数量可提高查找表的精度，同时增加其内存需求。

#### 依赖关系

- 要启用此参数，请选择 **Implement FIS as lookup table** 参数。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `NumBreakpoints` |
| **值**：| `"10"`（默认）| 带引号的正整数 |

### **Fuzzified inputs (fi)** — 启用 `fi` 输出端口 `off`（默认）| `on`

启用 **fi** 输出端口以访问中间模糊化输入数据。

#### 依赖关系

- 当您选择 **Implement FIS as lookup table** 时，中间推理输出不可用。*（自 R2025a 起）*

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `FuzzifiedInputs` |
| **值**：| `"off"`（默认）| `"on"` |

### **Rule firing strengths (rfs)** — 启用 `rfs` 输出端口 `off`（默认）| `on`

启用 **rfs** 输出端口以访问中间规则触发强度数据。

#### 依赖关系

- 当选择 **Implement FIS as lookup table** 时，中间推理输出不可用。*（自 R2025a 起）*

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RuleFiringStrengths` |
| **值：** | `"off"`（默认）| `"on"` |

### **Rule outputs (ro)** — 启用 `ro` 输出端口 `off`（默认）| `on`

启用 **ro** 输出端口以访问中间规则输出数据。

#### 依赖关系

- 当选择 **Implement FIS as lookup table** 时，中间推理输出不可用。*（自 R2025a 起）*

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RuleOutputs` |
| **值：** | `"off"`（默认）| `"on"` |

### **Aggregated outputs (ao)** — 启用 `ao` 输出端口 `off`（默认）| `on`

启用 **ao** 输出端口以访问中间聚合输出数据。

#### 依赖关系

- 当选择 **Implement FIS as lookup table** 时，中间推理输出不可用。*（自 R2025a 起）*

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `AggregatedOutputs` |
| **值：** | `"off"`（默认）| `"on"` |

### **Simulate using** — 仿真模式 `Interpreted execution`（默认）| `Code generation`

仿真模式，指定为以下值之一：

- `Interpreted execution` — 使用针对 `single` 和 `double` 数据类型的预编译 MEX 文件仿真模糊系统。使用此选项可减少模型的初始编译时间。
- `Code generation` — 不使用预编译 MEX 文件仿真模糊系统。在针对代码生成应用仿真模糊系统时，请使用此选项。

对于定点数据类型，Fuzzy Logic Controller 模块始终使用 `Code generation` 模式进行仿真。

#### 依赖关系

- 当选择 **Implement FIS as lookup table** 时，不支持设置仿真模式。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SimulateUsing` |
| **值：** | `"Interpreted execution"`（默认）| `"Code generation"` |

### 诊断

### **Out of range input value** — 输入超出范围时的诊断消息行为 `warning`（默认）| `error` | `none`

输入超出范围时的诊断消息行为，指定为以下之一：

- `warning` — 将诊断消息报告为警告。
- `error` — 将诊断消息报告为错误。
- `none` — 不报告诊断消息。

当输入值超出范围时，模糊系统中对应的规则可能具有意外的触发强度。

#### 依赖关系

- 仅当 **Simulate using** 参数为 `Interpreted execution` 时，才会提供诊断消息。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutOfRangeInputValueMessage` |
| **值：** | `"warning"`（默认）| `"error"` | `"none"` |

### **No rule fired** — 没有规则触发时的诊断消息行为 `warning`（默认）| `error` | `none`

给定输出变量没有规则触发时的诊断消息行为，指定为以下之一：

- `warning` — 将诊断消息报告为警告。
- `error` — 将诊断消息报告为错误。
- `none` — 不报告诊断消息。

当 **No rule fired** 为 `warning` 或 `none` 且给定输出没有规则触发时，去模糊化输出值设置为其范围均值。

#### 依赖关系

- 仅当 **Simulate using** 参数为 `Interpreted execution` 时，才会提供诊断消息。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `NoRuleFiredMessage` |
| **值：** | `"warning"`（默认） | `"error"` | `"none"` |

### **Empty output fuzzy set** — 输出模糊集为空时的诊断消息行为 `warning`（默认） | `error` | `none`

输出模糊集为空时的诊断消息行为，指定为以下选项之一：

- `warning` — 将诊断消息报告为警告。
- `error` — 将诊断消息报告为错误。
- `none` — 不报告诊断消息。

当 **Empty output fuzzy set** 为 `warning` 或 `none` 且输出模糊集为空时，相应输出的去模糊化值设置为其范围均值。

#### 依赖关系

- 此诊断消息仅适用于 Mamdani 系统。
- 仅当 **Simulate using** 参数为 `Interpreted execution` 时，才会提供诊断消息。

#### 编程用法

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

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

### R2025a：从模块打开 Fuzzy Logic Designer

现在，您可以通过点击 **Design** 从 Fuzzy Logic Controller 模块打开 Fuzzy Logic Designer。该应用会打开并导入由 **FIS name** 参数指定的 FIS。

### R2025a：将 FIS 实现为查找表

您可以将 FIS 表示为查找表，从而减少处理时间。要使用查找表，请选择 **Implement FIS as lookup table** 参数。该模块根据断点数量将每个 FIS 输入的输入范围划分为等大小的区域，断点数量通过 **Number of input breakpoints** 参数指定。

### R2024b：不支持模糊推理系统结构体

此模块不再支持模糊推理系统结构体。请改用 `mamfis` 和 `sugfis` 对象。要将现有的模糊推理系统结构体转换为对象，请使用 `convertfis` 函数。

### R2024a：使用 MAT 文件指定 FIS

您可以使用当前工作文件夹或 MATLAB 路径中的 MAT 文件指定要评估的 FIS。该 MAT 文件必须仅包含一个 FIS 对象。

### R2019b：将不再支持模糊推理系统结构体

对模糊推理系统结构体的支持将在未来版本中移除。此变更已在 R2018b 中宣布。从 R2019b 开始，在此模块中使用模糊推理系统结构体将发出警告。

### R2017b：访问中间模糊推理结果

使用 Fuzzy Logic Controller 模块，您可以通过启用以下输出端口来访问中间模糊推理结果。

- `fi` — 模糊化输入值
- `rfs` — 规则触发强度
- `ro` — 规则输出
- `ao` — 每个输出变量的聚合隶属度函数

### R2017b：扩展的数据类型支持

Fuzzy Logic Controller 模块支持双精度、单精度和定点数据类型。

### R2017b：改进的代码生成支持

使用 Simulink
Coder™ 生成代码时，Fuzzy Logic Controller 模块支持为使用以下内容的模糊系统生成代码：

- 单精度数据。
- 定点数据。要为定点数据生成代码，您需要 Fixed-Point Designer™ 软件。
- 自定义隶属度函数和自定义推理函数。有关为模糊系统指定自定义函数的详细信息，请参阅 Build Fuzzy Systems Using Custom Functions。

### R2017b：PLC 代码生成支持

Fuzzy Logic Controller 模块支持使用 Simulink
PLC Coder™ 软件生成用于 PLC 部署的 IEC 61131-3
结构化文本。

## 描述

评估模糊推理系统

Fuzzy Logic Controller 模块在 Simulink® 中实现模糊推理系统（FIS）。
您可以使用 **FIS name** 参数指定要评估的 FIS。

有关模糊推理的详细信息，请参阅 Fuzzy Inference Process。

要在仿真期间显示模糊推理过程，请使用 Fuzzy Logic
Controller with Ruleviewer 模块。
