---
type: simulink-block
title: 'DPD Coefficient Estimator'
family: 'rf-impairments-correction'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Impairments Correction'
documentation_page: 'dpdcoefficientestimator'
documentation_source_path: 'ref/dpdcoefficientestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# DPD Coefficient Estimator

## 端口

### 输入

### **PA In** — 功率放大器基带等效输入列向量

功率放大器基带等效输入，指定为列向量。

**数据类型：** `double`
**复数支持：** Yes

### **PA Out** — 功率放大器基带等效输出列向量

功率放大器基带等效输出，指定为与 **PA In** 长度相同的列向量。

**数据类型：** `double`
**复数支持：** Yes

### **Forgetting Factor** — 遗忘因子标量，范围为 (0, 1]

递归最小二乘算法使用的遗忘因子，指定为范围 (0, 1] 内的标量。减小遗忘因子可缩短收敛时间，但会导致输出估计的稳定性降低。

#### 依赖关系

要启用此端口，请将 **Algorithm** 设置为 `Recursive least squares`，并将 **Forgetting factor source** 设置为 `Input port`。

**数据类型：** `double`
### 输出

### **Out** — 记忆多项式系数矩阵

记忆多项式系数，以矩阵形式返回。有关详细信息，请参阅数字预失真。

此端口在模块上未命名。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条上的 **Simulation** 选项卡中，在 **Prepare** 库中，选择 **Property Inspector**。

### **Desired amplitude gain (dB)** — 期望幅度增益，单位为 dB `10`（默认）| 标量

期望幅度增益，单位为 dB，指定为标量。此参数值表示补偿后放大器输出处的期望信号增益。

除线性化之外，DPD 还应使 DPD 输入与功率放大器输出之间的组合增益尽可能接近期望增益。因此，请根据您在 PA 表征期间获得的功率放大器期望增益来设置此参数。

**可调：** Yes

### **Polynomial type** — 多项式类型 `Memory polynomial`（默认）| `Cross-term memory polynomial`

用于预失真的多项式类型，指定为以下值之一：

- `Memory polynomial` — 使用不带交叉项的记忆多项式计算预失真系数
- `Cross-term memory polynomial` — 使用带交叉项的记忆多项式计算预失真系数

有关详细信息，请参阅数字预失真。

### **Degree** — 记忆多项式阶数 `5`（默认）| 正整数

记忆多项式阶数，指定为正整数。

### **Memory depth** — 记忆多项式深度 `3`（默认）| 正整数

以采样点表示的记忆多项式深度，指定为正整数。

### **Algorithm** — 估计算法 `Least squares`（默认）| `Recursive least squares`

用于均衡的自适应算法，指定为以下值之一：

- `Least squares` — 使用最小二乘算法估计记忆多项式系数
- `Recursive least squares` — 使用递归最小二乘算法估计记忆多项式系数

有关算法参考资料，请参阅 [1] 和 [2] 中列出的文献。

### **Forgetting factor source** — 遗忘因子的来源 `Property`（默认）| `Input port`

遗忘因子的来源，指定为以下值之一：

- `Property` — 指定此值以使用 **Forgetting factor** 参数指定遗忘因子。
- `Input port` — 指定此值以使用 **Forgetting factor** 输入端口指定遗忘因子。

#### 依赖关系

要启用此参数，请将 **Algorithm** 设置为 `Recursive least squares`。

### **Forgetting factor** — 遗忘因子 `0.99`（默认）| 范围 (0, 1] 内的标量

递归最小二乘算法使用的遗忘因子，指定为范围 (0, 1] 内的标量。减小遗忘因子可缩短收敛时间，但会导致输出估计的稳定性降低。

#### 依赖关系

要启用此参数，请将 **Algorithm** 设置为 `Recursive least squares`，并将 **Forgetting factor source** 设置为 `Property`。

### **Initial coefficient estimate** — 初始系数估计 `[]`（默认）| 矩阵

用于递归最小二乘算法的初始系数估计，指定为实数或复数值组成的矩阵。

- 如果将此值指定为空矩阵，则会自动选择递归最小二乘算法的初始系数估计，以对应于恒等函数的记忆多项式，从而使输出等于输入。
- 如果将此值指定为非空矩阵，则行数必须等于 **Memory depth** 参数值。

  - 如果 **Polynomial type** 参数设置为 `Memory polynomial`，则列数为记忆多项式的阶数。
  - 如果 **Polynomial type** 参数设置为 `Cross-term memory polynomial`，则列数必须等于 *m*(*n*-1)+1。*m* 是多项式的记忆深度，*n* 是记忆多项式的阶数。

有关详细信息，请参阅数字预失真。

#### 依赖关系

要启用此参数，请将 **Algorithm** 设置为 `Recursive least squares`。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度快于 `Interpreted execution` 选项。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但后续仿真的速度慢于 `Code generation` 选项。在此模式下，您可以调试模块的源代码。

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

估计用于数字预失真的记忆多项式系数

给定功率放大器的基带等效输入和基带等效输出，估计用于非线性功率放大器数字预失真（DPD）的记忆多项式系数。有关详细信息，请参阅数字预失真和优化估计器多项式阶数与记忆深度。

此图标显示启用了所有端口的模块。
