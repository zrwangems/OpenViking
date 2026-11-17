---
type: simulink-block
title: 'Uncertain State Space'
family: 'robust-control-toolbox'
product_id: 'robust'
product_name: 'Robust Control Toolbox'
documentation_release: R2025b
official_category: 'Robust Control Toolbox'
documentation_page: 'uncertainstatespace'
documentation_source_path: 'ref/uncertainstatespace.html'
language: zh-CN
chinese_source: worker-translation
---

# Uncertain State Space

## 端口

### 输入

### **Port\_1(In1)** — 输入信号 scalar | vector

对于单输入不确定系统，输入信号为 scalar。对于多输入系统，请使用以下模块将系统输入合并为 vector 信号：

- Mux (Simulink)
- Vector Concatenate (Simulink)
- Bus Creator (Simulink)
### 输出

### **Port\_1(Out1)** — 输出信号 scalar | vector

对于单输出不确定系统，输出信号为 scalar。对于多输出系统，输出信号为 vector。要将系统输出拆分为 scalar 信号，请使用以下模块：

- Demux (Simulink)
- Bus Selector (Simulink)

## 参数

### **不确定系统变量 (uss)** — 不确定系统 `ss(ureal('a',-5),5,1,1)`（默认）| `uss` 模型 | 可转换为 `uss` 的模型或元素

使用以下之一，将要求仿真的不确定模型指定为 `uss` 对象：

- 求值结果为 `uss` 对象的函数或表达式。例如：

  - `ss(ureal('a',-5),5,1,1)`
  - `wt*input_unc`，其中 `input_unc` 是 `ultidyn` 对象，且 `wt` 和 `input_unc` 在 MATLAB® 工作区中定义。
- 在 MATLAB 工作区中定义的变量。例如，`unc_sys`，其中在所述工作区中定义 `unc_sys` = `ss(ureal('a',-5),5,1,1)`。
- 任何可转换为 `uss` 模型对象的模型。例如：

  - LTI 模型（`tf`、`zpk` 和 `ss`）
  - 不确定矩阵（`umat`）
  - 不确定实参数（`ureal`）
  - 不确定动态（`ultidyn`、`umargin`）

当该模块位于具有同步状态控制的模型中时（请参阅 State Control (HDL Coder) 模块），必须指定离散时间模型。

#### 编程用法

|  |
| --- |
| **模块参数：** `USystem` |
| **类型：** `uss` 模型，可转换为 `uss` 的模型 |
| **默认：** `ss(ureal('a',-5),5,1,1)` |

### **不确定性值（struct 或 [] 表示使用标称值）** — 用于替换不确定变量的值 `[]`（默认）| structure

您在 **不确定系统变量 (uss)** 参数中指定的 `uss` 模型取决于不确定变量，例如 `ureal` 或 `ultidyn` 不确定性。要仿真或线性化该不确定模型，模块必须将这些不确定变量替换为固定值。使用此参数可为下一次仿真或线性化指定这些固定值。使用一个 structure，其字段是 `uss` 模型中的不确定元素的名称，其值是这些元素的替换值。例如：

- 如果 `uss` 模型具有名为 `a` 和 `b` 的不确定实参数（`ureal`），则将此参数设置为 `struct('a',1,'b',3.5)` 会将 `a` 替换为 1，将 `b` 替换为 3.5。
- 如果 `uss` 模型具有由名为 `'delta'` 的 `ultidyn` 元素表示的动态不确定性，则将此参数设置为 `struct('delta',tf(1,[1 1]))` 会将不确定动态替换为指定的传递函数。

要为 Monte Carlo 仿真生成不确定变量的随机值，请使用 `ufind` 和 `usample`，如示例“在采样参数值处仿真不确定模型”和“在多个不确定模块间改变不确定值”中所示。

默认值 `[]` 将所有不确定元素设置为其标称值。请注意，`ultidyn` 不确定动态的标称值始终为 0，而 `umargin` 增益和相位不确定性的标称值始终为 1。

#### 编程用法

|  |
| --- |
| **模块参数：** `UValue` |
| **类型：** structure |
| **默认：** `[]` |

### **初始状态（标称动态）** — 标称系统的初始状态值 `[]`（默认）| vector

如果您在 **不确定系统变量 (uss)** 参数中指定的不确定系统的标称值具有动态，则可以使用此参数指定这些状态的初始值。将初始状态指定为 vector，其条目数与状态数相同。默认值 `[]` 将所有状态初始化为 0。

#### 编程用法

|  |
| --- |
| **模块参数：** `X0` |
| **类型：** scalar, vector |
| **默认：** `[]` |

### **初始状态（不确定动态）** — 不确定动态的初始状态值 `[]` | vector

如果不确定系统包含某些动态不确定性（`ultidyn` 或 `umargin`），则可以使用 **不确定性值（struct 或 [] 表示使用标称值）** 参数将该不确定性替换为用于仿真的特定动态。使用 **初始状态（不确定动态）** 参数指定这些动态的初始状态。将初始状态指定为 vector，其条目数与状态数相同。默认值 `[]` 将所有状态初始化为 0。

#### 编程用法

|  |
| --- |
| **模块参数：** `uX0` |
| **类型：** scalar, vector |
| **默认：** `[]` |

## 所属库

Robust Control Toolbox

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2009b 中引入**

## 描述

在 Simulink 中仿真不确定系统

Uncertain State Space 模块允许您在 Simulink® 中对参数不确定性和动态不确定性进行建模。该模块接受不确定状态空间（`uss`）模型，或任何可转换为 `uss` 的模型，例如 `umat`、`ureal`、`umargin` 和 `ultidyn` 对象。
