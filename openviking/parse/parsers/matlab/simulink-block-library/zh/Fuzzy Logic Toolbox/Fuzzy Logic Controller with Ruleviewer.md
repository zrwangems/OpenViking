---
type: simulink-block
title: 'Fuzzy Logic Controller with Ruleviewer'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'fuzzylogiccontrollerwithruleviewer'
documentation_source_path: 'fuzzylogiccontrollerwithruleviewer.html'
language: zh-CN
chinese_source: worker-translation
---

# Fuzzy Logic Controller with Ruleviewer

## 端口
```yaml
ports:
- name: Port_1(In1)
  summary: 输入信号 标量 | 向量
  direction: input
- name: Port_1(Out1)
  summary: 去模糊化输出信号 标量 | 向量
  direction: output
```

### 输入

### **Port\_1(In1)** — 输入信号 标量 | 向量

对于单输入模糊推理系统，输入为标量。
对于多输入模糊系统，使用以下模块将输入合并为向量信号：

- Mux (Simulink)
- Vector Concatenate (Simulink)
- Bus Creator (Simulink)
### 输出

### **Port\_1(Out1)** — 去模糊化输出信号 标量 | 向量

对于单输出模糊推理系统，输出为标量。对于多输出模糊系统，输出为向量。要将系统输出拆分为标量信号，请使用 Demux (Simulink) 模块。
## 参数
```yaml
parameters:
- name: FIS structure
  summary: 模糊推理系统 mamfis对象 | sugfis对象
  group: ''
  block_parameter: fismatrix
  values: '"fis" (default) | variable name in quotes'
- name: Refresh rate
  summary: 规则查看器更新之间的时间 正标量
  group: ''
  block_parameter: Ts
  values: '"2" (default) | positive scalar in quotes'
```

### **FIS structure** — 模糊推理系统 `mamfis`对象 | `sugfis`对象

要评估的模糊推理系统，指定为 `mamfis` 或 `sugfis` 对象。在 MATLAB® 工作区中指定 FIS 对象的名称。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `fismatrix` |
| **值**：| `"fis"` (default) | variable name in quotes |

### **Refresh rate** — 规则查看器更新之间的时间 正标量

规则查看器更新之间的时间（以秒为单位），指定为正标量。在仿真期间，规则查看器显示按指定速率更新，以显示最新输入信号值的推理过程。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `Ts` |
| **值**：| `"2"` (default) | positive scalar in quotes |
## 所属库

Fuzzy Logic Toolbox

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 使用 Fuzzy Logic Controller with Ruleviewer 模块生成代码所产生的代码与使用 Fuzzy Logic Controller 模块相同。但是，Fuzzy Logic Controller with Ruleviewer 模块不支持：

  - 为单点或定点数据生成代码。
  - 更改用于离散化输出变量范围的采样数。

## 版本历史

**在 R2006a 之前引入**

### R2024b: 不再支持模糊推理系统结构体

此模块不再支持模糊推理系统结构体。请改用 `mamfis` 和 `sugfis` 对象。要将现有的模糊推理系统结构体转换为对象，请使用 `convertfis` 函数。

### R2019b: 将不再支持模糊推理系统结构体

对模糊推理系统结构体的支持将在未来版本中移除。此变更在 R2018b 中宣布。从 R2019b 开始，在此模块中使用模糊推理系统结构体将发出警告。

## 描述

评估模糊推理系统并查看规则

Fuzzy Logic Controller with Ruleviewer 模块在 Simulink® 中实现模糊推理系统 (FIS)，并在仿真期间在规则查看器中显示模糊推理过程。使用 **FIS structure** 参数指定要评估的 FIS。要更改规则查看器更新之间的时间，请以秒为单位指定 **Refresh rate**。

有关模糊推理的详细信息，请参阅 Fuzzy Inference Process。

Fuzzy Logic Controller with Ruleviewer 模块不支持 Fuzzy Logic Controller 模块所支持的所有功能。Fuzzy Logic Controller with Ruleviewer 模块：

- 仅支持双精度数据。
- 使用 `101` 个点对输出变量范围进行离散化。
- 仅支持 `Interpreted execution` 仿真模式。
- 没有用于访问中间模糊推理结果的额外输出端口。
