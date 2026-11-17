---
type: simulink-block
title: 'Uncertain State Space'
family: 'robust'
product_id: 'robust'
product_name: 'Robust Control Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'uncertainstatespace'
documentation_source_path: 'ref/uncertainstatespace.html'
language: zh-CN
chinese_source: worker-translation
---

# Uncertain State Space

## 端口

### 输入

### **Port\_1(In1)** — 输入信号 标量 | 向量

对于单输入不确定系统，输入信号为标量。对于多输入系统，使用以下模块将系统输入合并为向量信号：

- Mux (Simulink)
- Vector Concatenate (Simulink)
- Bus Creator (Simulink)
### 输出

### **Port\_1(Out1)** — 输出信号 标量 | 向量

对于单输出不确定系统，输出信号为标量。对于多输出系统，输出信号为向量。要将系统输出拆分为标量信号，请使用以下模块：

- Demux (Simulink)
- Bus Selector (Simulink)

## 参数

### **Uncertain system variable (uss)** — 不确定系统 `ss(ureal('a',-5),5,1,1)`（默认）| `uss` 模型 | 可转换为 `uss` 的模型或元素

使用以下方式之一将要仿真的不确定模型指定为 `uss` 对象：

- 求值为 `uss` 对象的函数或表达式。例如：

  - `ss(ureal('a',-5),5,1,1)`
  - `wt*input_unc`，其中 `input_unc` 是 `ultidyn` 对象，`wt` 和 `input_unc` 在 MATLAB® 工作区中定义。
- 在 MATLAB 工作区中定义的变量。例如，`unc_sys`，其中你在工作区中定义 `unc_sys` = `ss(ureal('a',-5),5,1,1)`。
- 可转换为 `uss` 模型对象的任何类型的模型。例如：

  - LTI 模型（`tf`、`zpk` 和 `ss`）
  - 不确定矩阵（`umat`）
  - 不确定实参数（`ureal`）
  - 不确定动态（`ultidyn`、`umargin`）

当该模块位于具有同步状态控制的模型中时（请参阅 State Control (HDL Coder) 模块），必须指定离散时间模型。

#### 编程使用

|  |
| --- |
| **模块参数**：`USystem` |
| **类型**：`uss` model, model that can be converted to `uss` |
| **默认值**：`ss(ureal('a',-5),5,1,1)` |

### **Uncertainty value (struct or [] to use nominal value)** — 用于替换不确定变量的值 `[]`（默认）| 结构体

你在 **Uncertain system variable (uss)** 参数中指定的 `uss` 模型依赖于不确定变量，例如 `ureal` 或 `ultidyn` 不确定性。要仿真或线性化该不确定模型，模块必须将这些不确定变量替换为固定值。使用此参数为下一次仿真或线性化指定这些固定值。使用一个结构体，其字段为 `uss` 模型中不确定元素的名称，其值为这些元素的替换值。例如：

- 如果 `uss` 模型具有名为 `a` 和 `b` 的不确定实参数（`ureal`），则将此参数设置为 `struct('a',1,'b',3.5)` 会将 `a` 替换为 1，将 `b` 替换为 3.5。
- 如果 `uss` 模型具有由名为 `'delta'` 的 `ultidyn` 元素表示的不确定动态，则将此参数设置为 `struct('delta',tf(1,[1 1]))` 会将不确定动态替换为指定的传递函数。

要为 Monte Carlo 仿真生成不确定变量的随机值，请使用 `ufind` 和 `usample`，如示例 Simulate Uncertain Model at Sampled Parameter Values 和 Vary Uncertain Values Across Multiple Uncertain Blocks 所示。

默认值 `[]` 将所有不确定元素设置为其标称值。请注意，`ultidyn` 不确定动态的标称值始终为 0，而 `umargin` 增益和相位不确定性的标称值始终为 1。

#### 编程使用

|  |
| --- |
| **模块参数**：`UValue` |
| **类型**：structure |
| **默认值**：`[]` |

### **Initial states (nominal dynamics)** — 标称系统的初始状态值 `[]`（默认）| 向量

如果你在 **Uncertain system variable (uss)** 参数中指定的不确定系统的标称值具有动态，则可以使用此参数为这些状态指定初始值。将初始状态指定为一个向量，其条目数与状态数相同。默认值 `[]` 将所有状态初始化为 0。

#### 程序化使用

|  |
| --- |
| **模块参数：** `X0` |
| **类型：** 标量、向量 |
| **默认值：** `[]` |

### **初始状态（不确定动态）** — 不确定动态的初始状态值 `[]` | 向量

如果不确定系统包含某些动态不确定性
（`ultidyn` 或 `umargin`），则可以使用
**不确定性值（结构体或 [] 以使用标称值）** 参数
将该不确定性替换为特定动态以进行仿真。使用
**初始状态（不确定动态）** 参数来指定这些动态的
初始状态。将初始状态指定为一个向量，其元素数量与状态数量相同。默认值 `[]` 将所有
状态初始化为 0。

#### 程序化使用

|  |
| --- |
| **模块参数：** `uX0` |
| **类型：** 标量、向量 |
| **默认值：** `[]` |

## 所属库

Robust Control Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2009b 中引入**

## 描述

在 Simulink 中仿真不确定系统

Uncertain State Space 模块允许您在
Simulink® 中对参数不确定性和动态不确定性进行建模。该模块接受不确定状态空间（`uss`）模型或任何可转换为 `uss` 的模型，例如
`umat`、`ureal`、`umargin` 和
`ultidyn` 对象。
