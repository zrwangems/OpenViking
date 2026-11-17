---
type: simulink-block
title: 'LCMV Beamformer'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Beamforming'
documentation_page: 'lcmvbeamformer'
documentation_source_path: 'ref/lcmvbeamformer.html'
language: zh-CN
chinese_source: worker-translation
---

# LCMV Beamformer

## 端口

### 输入

### **X** — 输入信号 *M*×*N* 复值矩阵

波束形成器的输入信号，指定为 *M*×*N* 复值矩阵。*M* 是信号样本数。*N* 是传感器阵列元素数。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，可能发生大小变化。

**数据类型：** `double`
**复数支持：** 是

### **XT** — 训练信号 *P*×*N* 复值矩阵

训练输入信号，指定为 *P*×*N* 复值矩阵。*P* 是训练输入信号中的样本数。*N* 是传感器阵列的元素数。*P* 必须大于 *N*。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，可能发生大小变化。

#### 依赖关系

要启用此端口，请选中 **Enable training data input** 复选框。

**数据类型：** `double`
**复数支持：** 是

### 输出

### **Y** — 波束形成输出 *M*×1 复值列向量

波束形成输出，指定为 *M*×1 复值列向量。*M* 是信号样本数。

**数据类型：** `double`
**复数支持：** 是

### **W** — 波束形成器权重输出 *N*×1 复值列向量

波束形成器权重输出，指定为 *N*×1 复值列向量。*N* 是阵列元素数。

#### 依赖关系

要启用此端口，请选中 **Enable weights output** 复选框。

**数据类型：** `double`
**复数支持：** 是

## 参数

### **Constraint matrix** — LCMV 波束形成器约束矩阵 `complex([1;1])`（默认）| *N*×*K* 复值矩阵

LCMV 波束形成器约束矩阵，指定为 *N*×*K* 复值矩阵。矩阵的每一列是一个约束。*N* 是传感器阵列中的元素数，*K* 是约束数。*K* 必须小于或等于传感器数 *N*，*K ≤ N*

### **Desired response vector** — LCMV 波束形成的期望响应 `1`（默认）| 实值 *K*×1 列向量

LCMV 波束形成器的期望响应，指定为实值 *K*×1 列向量。*K* 是 **Constraint matrix** 中的约束数。向量中的每个元素定义了 **Constraint matrix** 参数对应列中指定约束的期望响应。

### **Diagonal loading factor** — 对角加载因子 正标量

对角加载因子，指定为正标量。对角加载是一种用于实现稳健波束形成性能的技术，特别是在样本支持较小的情况下。

### **Enable training data input** — 启用训练数据输入端口 `off`（默认）| `on`

启用训练数据输入端口，指定为 `off` 或 `on`。要启用训练数据输入端口 `XT`，请选中此复选框。

### **Enable weights output** — 启用波束形成器权重输出 `off`（默认）| `on`

启用波束形成权重输出端口，指定为 `off` 或 `on`。要启用波束形成权重输出端口 `W`，请选中此复选框。

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或
`Code Generation`。如果希望模块使用
MATLAB® 解释器，请选择 `Interpreted Execution`。如果
希望模块作为编译代码运行，请选择 `Code
Generation`。编译代码需要时间编译，但通常运行
更快。

当您开发和调整模型时，解释执行很有用。模块
在 MATLAB 中运行底层 System object™。您可以快速更改和执行模型。当您对
结果满意时，可以使用 `Code
Generation` 运行模块。长时间仿真使用生成代码比在
解释执行中运行更快。您可以重复执行而无需重新编译，但如果您
更改任何模块参数，则模块会在执行前自动重新编译。

此表显示了 **Simulate using** 参数如何影响
整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式
会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`、`Code Generation` |
| **默认：** `Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Beamforming

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

窄带线性约束最小方差 (LCMV) 波束形成器

LCMV Beamformer 模块执行窄带
线性约束最小方差 (LCMV) 波束形成。约束
数量必须小于阵列中的阵元或子阵
数量。
