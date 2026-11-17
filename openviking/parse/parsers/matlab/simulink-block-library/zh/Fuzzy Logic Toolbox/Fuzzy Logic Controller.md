---
type: simulink-block
title: 'Fuzzy Logic Controller'
family: 'fuzzy-logic-toolbox'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Fuzzy Logic Toolbox'
documentation_page: 'fuzzylogiccontroller'
documentation_source_path: 'fuzzylogiccontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# Fuzzy Logic Controller

## 端口

### 输入

### **in** — 输入信号 标量 | 向量

对于单输入模糊推理系统，输入是标量信号。对于多输入模糊系统，可使用如下模块将各输入合并为向量信号：

- Mux (Simulink)
- Vector Concatenate (Simulink)
- Bus Creator (Simulink)

### 输出

### **out** — 去模糊化输出信号 标量 | 向量

对于单输出 FIS，输出是标量信号。对于多输出 FIS，输出是向量信号。要将系统输出拆分为标量信号，请使用 Demux (Simulink) 模块。

### **fi** — 模糊化输入值 矩阵

模糊化输入值，通过在当前输入值处计算每条规则的输入隶属函数得到。

对于 type-1 FIS，**fi** 是 *NR*×*NU* 矩阵信号，其中 *NR* 是 FIS 规则数。**fi** 的元素 (*i*,*j*) 是第 *i* 条规则中第 *j* 个输入的输入隶属函数值。

对于 type-2 FIS，**fi** 是 *NR*×(2\**NU*) 矩阵信号。前 *NU* 列包含每条规则的上隶属函数的模糊化值，后 *NU* 列包含来自下隶属函数的模糊化值。

有关模糊化输入值的详细信息，请参阅模糊化输入。

#### 依赖关系

要启用此端口，请选择 **模糊化输入 (fi)** 参数。

### **rfs** — 规则触发强度 列向量

规则触发强度，通过计算每条规则的前件得到；也就是说，对模糊化输入值应用模糊算子。

对于 type-1 FIS，**rfs** 是长度为 *NR* 的列向量信号，其中 *NR* 是规则数，元素 *i* 是第 *i* 条规则的触发强度。

对于 type-2 FIS，**rfs** 是 *NR*×2 矩阵信号。第一列包含使用上隶属函数生成的规则触发强度，第二列包含使用下隶属函数生成的规则触发强度。

有关应用模糊算子的详细信息，请参阅应用模糊算子。

#### 依赖关系

要启用此端口，请选择 **规则触发强度 (rfs)** 参数。

### **ro** — 规则输出 矩阵

规则输出，通过使用 FIS 中指定的蕴含方法将规则触发强度应用于输出隶属函数得到。

对于 type-1 Mamdani FIS，**ro** 是 *NS*×(*NR**NY*) 矩阵信号，其中 *NR* 是规则数，*NY* 是输出数，*NS* 是用于计算输出变量范围的样本点数。**ro** 的每一列包含一条规则的输出模糊集。前 *NR* 列包含第一个输出变量的规则输出，接下来的 *NR* 列对应第二个输出变量，依此类推。

对于 type-2 Mamdani FIS，**ro** 是 *NS*×(2\**NR*\**NY*) 矩阵信号。前 *NR*\**NY* 列包含使用上隶属函数生成的规则输出，后 *NR*\**NY* 列包含使用下隶属函数生成的规则输出。

对于 type-1 Sugeno 系统，每条规则输出是一个标量值。在这种情况下，**ro** 是 *NR*×*NY* 矩阵信号。**ro** 的元素 (*j*,*k*) 是第 *j* 条规则的第 *k* 个输出变量的值。

对于 type-2 Sugeno 系统，**ro** 是 *NR*×(3\**NY*) 数组。前 *NY* 列包含规则输出水平。接下来的 *NY* 列包含使用上隶属函数生成的对应规则触发强度。最后 *NY* 列包含使用下隶属函数生成的规则触发强度。例如，在三输出系统中，第 4 列和第 7 列包含第 1 列中输出水平对应的触发强度。

有关模糊蕴含的详细信息，请参阅应用蕴含方法。

#### 依赖关系

- 要启用此端口，请选择 **规则输出 (ro)** 参数。
- 要指定 *NS*，请使用 **输出离散化的样本数** 参数。

### **ao** — 聚合输出 矩阵 | 行向量

每个输出变量的聚合输出，通过使用 FIS 中指定的聚合方法合并来自所有规则的对应输出得到。

对于 type-1 Mamdani 模糊推理系统，每个输出变量的聚合结果是一个模糊集。在这种情况下，**ao** 是 *NS*×*NY* 矩阵信号，其中 *NY* 是输出数，*NS* 是用于计算输出变量范围的样本点数。**ao** 的每一列包含一个输出变量的聚合模糊集。

对于 type-2 Mamdani FIS，每个输出变量的聚合结果是一个模糊集。在这种情况下，**ao** 是 *NS*×(2\**NY*) 矩阵信号。前 *NY* 列包含使用上隶属函数生成的聚合输出，后 *NY* 列包含使用下隶属函数生成的聚合输出。

对于 type-1 Sugeno 系统，每个输出变量的聚合结果是一个标量值。在这种情况下，**ao** 是长度为 *NY* 的行向量，其中元素 *k* 是第 *k* 个输出变量的规则输出之和。

对于 type-2 Sugeno 系统，**ao** 是 *NR*×(3\**NY*) 数组。**ro** 包含与 **ao** 相同的数据，其中各列根据输出水平排序。例如，在三输出系统中，当第 1 列中的输出水平被排序时，第 4 列和第 7 列中对应的触发强度会相应调整。

有关模糊聚合的详细信息，请参阅聚合所有输出。

#### 依赖关系

- 要启用此端口，请选择 **聚合输出 (ao)** 参数。
- 要指定 *NS*，请使用 **输出离散化的样本数** 参数。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### 常规

### **FIS 名称** — 要评估的模糊推理系统 `mamfis` 对象 | `sugfis` 对象 | `mamfistype2` 对象 | `sugfistype2` 对象 | 带引号的 FIS 文件名 | 带引号的 MAT 文件名

要评估的模糊推理系统，指定为以下之一：

- `mamfis` 或 `sugfis` 对象 — 指定 MATLAB® 工作区中 type-1 FIS 对象的名称。
- `mamfistype2` 或 `sugfistype2` 对象 — 指定 MATLAB 工作区中 type-2 FIS 对象的名称。
- 当前工作文件夹或 MATLAB 路径中 FIS 文件（`*.fis`）的名称。文件名中可包含文件扩展名，也可不包含。用引号指定文件名。
- 当前工作文件夹或 MATLAB 路径中 MAT 文件（`*.mat`）的名称。MAT 文件必须仅包含一个 FIS 对象。文件名中可包含文件扩展名，也可不包含。用引号指定文件名。*(自 R2024a 起)*

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `FIS` |
| **值：** | `'"tipper.fis"'`（默认） | 带引号的变量名 | 带引号的文件名 |

### **设计** — 打开 Fuzzy Logic Designer 按钮

打开 Fuzzy Logic Designer 以查看和修改 FIS 设计。然后，您可以更新模块以使用修改后的 FIS 设计。有关详细信息，请参阅在 Simulink 中设计模糊推理系统。

### **输出离散化的样本数** — 输出模糊集中的点数 101（默认） | 大于 `1` 的整数

用于离散化 FIS 输出变量范围的样本数，指定为大于 `1` 的整数。此值对应于每条规则的输出模糊集中的点数。

为了在计算 Mamdani FIS 时减少内存使用量，请指定较小的样本数。这样做会牺牲去模糊化输出值的精度。指定过低的样本数可能会使用于去模糊化的输出面积为零。在这种情况下，去模糊化输出值是输出变量范围的中点。

**注意**

该模块在计算 Sugeno FIS 时会忽略此参数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutputSampleNumber` |
| **值：** | `"101"`（默认） | 带引号的、大于 `1` 的整数 |

### **数据类型** — 信号数据类型 `double`（默认） | `single` | `fixed-point` | `expression`

信号数据类型，指定为以下之一：

- `double` — 双精度信号
- `single` — 单精度信号
- `fixdt(1,16,0)` — 采用二进制小数点缩放的定点信号
- `fixdt(1,16,2^0,0)` — 采用斜率和偏置缩放的定点信号
- Expression — 计算为这些数据类型之一的表达式

对于定点数据类型，您可以使用 **Data Type Assistant** 配置符号性、字长和缩放参数。有关详细信息，请参阅指定定点数据类型 (Simulink)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `DataType` |
| **值：** | `"double"`（默认） | `"single"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` |

### **将 FIS 实现为查找表** — 将 FIS 转换为查找表 `off`（默认） | `on`

*自 R2025a 起*

为减少控制器的处理时间，您可以将 FIS 表示为查找表。

该模块根据断点数将每个 FIS 输入的输入范围划分为大小相等的区域，断点数使用 **输入断点数** 参数指定。

对于每个输入组合，该模块计算相应的 FIS 输出。在计算期间，控制器使用这些预先计算的输出，而不是执行模糊推理过程。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `UseLookupTable` |
| **值：** | `"off"`（默认） | `"on"` |

### **输入断点数（样本数）** — 查找表断点数 `10`（默认） | 正整数

*自 R2025a 起*

查找表断点数，指定为正整数。增加断点数可提高查找表的精度，同时增加其内存需求。

#### 依赖关系

- 要启用此参数，请选择 **将 FIS 实现为查找表** 参数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `NumBreakpoints` |
| **值：** | `"10"`（默认） | 带引号的正整数 |

### **模糊化输入 (fi)** — 启用 `fi` 输出端口 `off`（默认） | `on`

启用 **fi** 输出端口以访问中间模糊化输入数据。

#### 依赖关系

- 当您选择 **将 FIS 实现为查找表** 时，中间推理输出不可用。*(自 R2025a 起)*

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `FuzzifiedInputs` |
| **值：** | `"off"`（默认） | `"on"` |

### **规则触发强度 (rfs)** — 启用 `rfs` 输出端口 `off`（默认） | `on`

启用 **rfs** 输出端口以访问中间规则触发强度数据。

#### 依赖关系

- 当您选择 **将 FIS 实现为查找表** 时，中间推理输出不可用。*(自 R2025a 起)*

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RuleFiringStrengths` |
| **值：** | `"off"`（默认） | `"on"` |

### **规则输出 (ro)** — 启用 `ro` 输出端口 `off`（默认） | `on`

启用 **ro** 输出端口以访问中间规则输出数据。

#### 依赖关系

- 当您选择 **将 FIS 实现为查找表** 时，中间推理输出不可用。*(自 R2025a 起)*

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RuleOutputs` |
| **值：** | `"off"`（默认） | `"on"` |

### **聚合输出 (ao)** — 启用 `ao` 输出端口 `off`（默认） | `on`

启用 **ao** 输出端口以访问中间聚合输出数据。

#### 依赖关系

- 当您选择 **将 FIS 实现为查找表** 时，中间推理输出不可用。*(自 R2025a 起)*

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `AggregatedOutputs` |
| **值：** | `"off"`（默认） | `"on"` |

### **仿真方式** — 仿真模式 `Interpreted execution`（默认） | `Code generation`

仿真模式，指定为以下值之一：

- `Interpreted execution` — 使用针对 `single` 和 `double` 数据类型的预编译 MEX 文件来仿真模糊系统。使用此选项可减少模型的初始编译时间。
- `Code generation` — 不使用预编译 MEX 文件来仿真模糊系统。在为代码生成应用仿真模糊系统时，请使用此选项。

对于定点数据类型，Fuzzy Logic Controller 模块始终使用 `Code generation` 模式进行仿真。

#### 依赖关系

- 当您选择 **将 FIS 实现为查找表** 时，不支持设置仿真模式。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SimulateUsing` |
| **值：** | `"Interpreted execution"`（默认） | `"Code generation"` |

### 诊断

### **输入值超出范围** — 当输入超出范围时的诊断消息行为 `warning`（默认） | `error` | `none`

当输入超出范围时的诊断消息行为，指定为以下之一：

- `warning` — 将诊断消息报告为警告。
- `error` — 将诊断消息报告为错误。
- `none` — 不报告诊断消息。

当输入值超出范围时，模糊系统中对应的规则可能会具有意外的触发强度。

#### 依赖关系

- 仅当 **仿真方式** 参数为 `Interpreted execution` 时才提供诊断消息。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutOfRangeInputValueMessage` |
| **值：** | `"warning"`（默认） | `"error"` | `"none"` |

### **未触发规则** — 当没有规则触发时的诊断消息行为 `warning`（默认） | `error` | `none`

当给定输出变量没有规则触发时的诊断消息行为，指定为以下之一：

- `warning` — 将诊断消息报告为警告。
- `error` — 将诊断消息报告为错误。
- `none` — 不报告诊断消息。

当 **未触发规则** 为 `warning` 或 `none`，且给定输出没有规则触发时，去模糊化输出值设置为其范围平均值。

#### 依赖关系

- 仅当 **仿真方式** 参数为 `Interpreted execution` 时才提供诊断消息。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `NoRuleFiredMessage` |
| **值：** | `"warning"`（默认） | `"error"` | `"none"` |

### **Empty output fuzzy set** — 当输出模糊集为空时的诊断消息行为 `warning` (default) | `error` | `none`

当输出模糊集为空时的诊断消息行为，指定为以下之一：

- `warning` — 将诊断消息报告为警告。
- `error` — 将诊断消息报告为错误。
- `none` — 不报告诊断消息。

当 **Empty output fuzzy set** 为 `warning` 或 `none` 且输出模糊集为空时，相应输出的去模糊化值设置为其范围平均值。

#### 依赖项

- 此诊断消息仅适用于 Mamdani 系统。
- 仅当 **Simulate using** 参数为 `Interpreted execution` 时，才提供诊断消息。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `EmptyOutputFuzzySetMessage` |
| **值：** | `"warning"` (default) | `"error"` | `"none"` |

## 所属库

Fuzzy Logic Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真 fixed-point 系统。

## 版本历史

**早于 R2006a 引入**

### R2025a：从模块打开 Fuzzy Logic Designer

现在，您可以通过点击 **Design** 从 Fuzzy Logic Controller 模块打开 Fuzzy Logic Designer。该 App 会打开并导入由 **FIS name** 参数指定的 FIS。

### R2025a：将 FIS 实现为查找表

您可以将 FIS 表示为查找表，从而减少处理时间。要使用查找表，请选择 **Implement FIS as lookup table** 参数。该模块根据断点数量将每个 FIS 输入的输入范围划分为大小相等的区域，断点数量使用 **Number of input breakpoints** 参数指定。

### R2024b：不支持模糊推理系统结构

此模块不再支持模糊推理系统结构。请改用 `mamfis` 和 `sugfis` 对象。要将现有的模糊推理系统结构转换为对象，请使用 `convertfis` 函数。

### R2024a：使用 MAT 文件指定 FIS

您可以使用当前工作文件夹中或 MATLAB 路径上的 MAT 文件指定要评估的 FIS。MAT 文件必须仅包含一个 FIS 对象。

### R2019b：将不再支持模糊推理系统结构

对模糊推理系统结构的支持将在未来版本中移除。此变更已在 R2018b 中宣布。从 R2019b 开始，将此模块与模糊推理系统结构一起使用会发出警告。

### R2017b：访问中间模糊推理结果

使用 Fuzzy Logic Controller 模块，您可以通过启用以下输出端口访问中间模糊推理结果。

- `fi` — 模糊化输入值
- `rfs` — 规则触发强度
- `ro` — 规则输出
- `ao` — 每个输出变量的聚合隶属函数

### R2017b：扩展的数据类型支持

Fuzzy Logic Controller 模块支持 double-precision、single-precision 和 fixed-point 数据类型。

### R2017b：改进的代码生成支持

使用 Simulink Coder™ 生成代码时，Fuzzy Logic Controller 模块支持为使用以下内容的模糊系统生成代码：

- Single-precision 数据。
- Fixed-point 数据。要为 fixed-point 数据生成代码，需要 Fixed-Point Designer™ 软件。
- 自定义隶属函数和自定义推理函数。有关为模糊系统指定自定义函数的详细信息，请参阅使用自定义函数构建模糊系统。

### R2017b：PLC 代码生成支持

Fuzzy Logic Controller 模块支持使用 Simulink PLC Coder™ 软件生成用于 PLC 部署的 IEC 61131-3 Structured Text。

## 描述

评估模糊推理系统

Fuzzy Logic Controller 模块在 Simulink® 中实现模糊推理系统 (FIS)。您使用 **FIS name** 参数指定要评估的 FIS。

有关模糊推理的详细信息，请参阅模糊推理过程。

要在仿真期间显示模糊推理过程，请使用 Fuzzy Logic Controller with Ruleviewer 模块。
