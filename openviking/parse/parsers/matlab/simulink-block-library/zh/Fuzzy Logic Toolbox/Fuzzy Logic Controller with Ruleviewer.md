---
type: simulink-block
title: 'Fuzzy Logic Controller with Ruleviewer'
family: 'fuzzy-logic-toolbox'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Fuzzy Logic Toolbox'
documentation_page: 'fuzzylogiccontrollerwithruleviewer'
documentation_source_path: 'fuzzylogiccontrollerwithruleviewer.html'
language: zh-CN
chinese_source: worker-translation
---

# Fuzzy Logic Controller with Ruleviewer

## 端口

### 输入

### **Port\_1(In1)** — 输入信号 标量 | 向量

对于单输入模糊推理系统，输入是标量。
对于多输入模糊系统，使用如下模块将输入合并为向量信号：

- Mux (Simulink)
- Vector Concatenate (Simulink)
- Bus Creator (Simulink)
### 输出

### **Port\_1(Out1)** — 去模糊化输出信号 标量 | 向量

对于单输出模糊推理系统，输出是标量。对于多输出模糊系统，输出是向量。要将系统输出拆分为标量信号，请使用 Demux (Simulink) 模块。

## 参数

### **FIS structure** — 模糊推理系统 `mamfis`object | `sugfis`object

要评估的模糊推理系统，指定为 `mamfis` 或 `sugfis` 对象。在 MATLAB® 工作区中指定 FIS 对象的名称。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `fismatrix` |
| **值：** | `"fis"`（默认） | 带引号的变量名 |

### **Refresh rate** — 规则查看器更新之间的时间，正标量

规则查看器更新之间的时间（以 seconds 为单位），指定为正标量。在仿真期间，Rule Viewer 显示会以指定速率更新，以显示最新输入信号值的推理过程。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `Ts` |
| **值：** | `"2"`（默认） | 带引号的正标量 |

## 所属库

Fuzzy Logic Toolbox

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

用法说明和限制：

- 使用 Fuzzy Logic Controller with Ruleviewer 模块生成代码与使用 Fuzzy Logic Controller 模块生成代码相同。但是，Fuzzy Logic Controller with Ruleviewer 模块不支持：

  - 为 single-point 或 fixed-point 数据生成代码。
  - 更改用于离散化输出变量范围的样本数。

## 版本历史

**在 R2006a 之前引入**

### R2024b：不支持模糊推理系统结构

此模块不再支持模糊推理系统结构。请改用 `mamfis` 和 `sugfis` 对象。要将现有模糊推理系统结构转换为对象，请使用 `convertfis` 函数。

### R2019b：将不再支持模糊推理系统结构

对模糊推理系统结构的支持将在未来版本中移除。此更改已在 R2018b 中宣布。从 R2019b 开始，将此模块与模糊推理系统结构一起使用会发出警告。

## 描述

评估模糊推理系统并查看规则

Fuzzy Logic Controller with Ruleviewer 模块在 Simulink® 中实现模糊推理系统 (FIS)，并在仿真期间在 Rule Viewer 中显示模糊推理过程。使用 **FIS structure** 参数指定要评估的 FIS。要更改 Rule Viewer 更新之间的时间，请以 seconds 为单位指定 **Refresh rate**。

有关模糊推理的更多信息，请参阅 Fuzzy Inference Process。

Fuzzy Logic Controller with Ruleviewer 模块不支持 Fuzzy Logic Controller 模块支持的所有功能。Fuzzy Logic Controller with Ruleviewer 模块：

- 仅支持 double-precision 数据。
- 使用 `101` 个点离散化输出变量范围。
- 仅支持 `Interpreted execution` 仿真模式。
- 没有用于访问中间模糊推理结果的附加输出端口。
