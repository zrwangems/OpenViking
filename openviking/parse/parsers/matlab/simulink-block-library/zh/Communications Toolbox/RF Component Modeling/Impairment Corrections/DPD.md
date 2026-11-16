---
type: simulink-block
title: 'DPD'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Component Modeling / Impairment Corrections'
documentation_page: 'dpd'
documentation_source_path: 'ref/dpd.html'
language: zh-CN
chinese_source: worker-translation
---

# DPD

## 端口

### 输入

### **In** — 输入基带信号列向量

输入基带信号，指定为列向量。在 **Coefficient source** 参数设置为 `Input
port` 之前，此端口未命名。

**数据类型：** `double`
**复数支持：** Yes

### **Coef** — 记忆多项式系数矩阵

记忆多项式系数，指定为矩阵。矩阵中的行数必须等于记忆多项式的记忆深度。

- 如果 **Polynomial type** 参数设置为
  `Memory polynomial`，则矩阵中的列数是记忆多项式的阶数。
- 如果 **Polynomial type** 设置为 `Cross-term memory
  polynomial`，则矩阵中的列数必须等于 *m*(*n*-1)+1。*m* 是多项式的记忆深度，
  而 *n* 是记忆多项式的阶数。

**示例：** `complex([1 0 0 0 0; 0 0 0 0 0; 0 0 0 0
0])`

#### 依赖关系

要启用此端口，请将 **Coefficient source** 参数
设置为 `Input port`。

**数据类型：** `double`
**复数支持：** Yes

### 输出

### **Out** — 预失真基带信号列向量

预失真基带信号，返回为与输入信号长度相同的列向量。

## 参数

要交互式编辑模块参数，请使用
Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在
**Prepare** 库中，选择 **Property
Inspector**。

### **Polynomial type** — 多项式类型 `Memory polynomial`（默认）| `Cross-term memory polynomial`

用于预失真的多项式类型，指定为以下值之一：

- `Memory polynomial` — 使用无交叉项的记忆多项式计算预失真系数
- `Cross-term memory polynomial` — 使用带交叉项的记忆多项式计算预失真系数

有关详细信息，请参阅数字预失真。

### **Coefficient source** — 记忆多项式系数的来源 `Property`（默认）| `Input port`

记忆多项式系数的来源，指定为以下值之一：

- `Property` — 指定此值以使用
  **Coefficients** 参数定义记忆多项式系数
- `Input port` — 指定此值以使用
  **Coef** 输入端口定义记忆多项式系数

### **Coefficients** — 记忆多项式系数 `complex([1 0 0 0 0; 0 0 0 0 0; 0 0 0 0 0])`（默认）| 矩阵

记忆多项式系数，指定为矩阵。行数必须等于
记忆多项式的记忆深度。

- 如果 **Polynomial type** 设置为 `Memory
  polynomial`，则列数是记忆多项式的阶数。
- 如果 **Polynomial type** 设置为 `Cross-term
  memory polynomial`，则列数必须等于 *m*(*n*-1)+1。*m* 是多项式的记忆深度，且
  *n* 是记忆多项式的阶数。

有关详细信息，请参阅数字预失真。

#### 依赖关系

要启用此参数，请将 **Coefficient source** 设置为
`Property`。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或
`Interpreted execution`。

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比使用 `Interpreted execution` 选项更快。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但后续仿真的速度比使用 `Code generation` 选项更慢。在此模式下，您可以调试模块的源代码。

有关详细信息，请参阅解释执行与代码生成 (Simulink)。

## 所属库

Communications Toolbox / RF Impairments Correction

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

数字预失真器

使用记忆多项式对复基带信号应用数字预失真 (DPD)，以补偿功率放大器中的非线性。有关详细信息，请参阅数字预失真和优化估计器多项式阶数和记忆深度。

此图标显示启用了所有端口的模块。
