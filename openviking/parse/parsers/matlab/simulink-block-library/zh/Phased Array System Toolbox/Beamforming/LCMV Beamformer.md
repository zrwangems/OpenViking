---
type: simulink-block
title: 'LCMV Beamformer'
family: 'beamforming'
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

### **X** — 输入信号 *M*×*N* 复数值矩阵

波束形成器的输入信号，指定为 *M*×*N* 复数值矩阵。*M* 是信号样本数。*N* 是传感器阵列阵元数。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，大小可能发生变化。

**数据类型：** `double`
**复数支持：** Yes

### **XT** — 训练信号 *P*×*N* 复数值矩阵

训练输入信号，指定为 *P*×*N* 复数值矩阵。*P* 是训练输入信号中的样本数。*N* 是传感器阵列的阵元数。*P* 必须大于 *N*。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，大小可能发生变化。

#### 依赖关系

要启用此端口，请选中 **启用训练数据输入** 复选框。

**数据类型：** `double`
**复数支持：** Yes
### 输出

### **Y** — 波束形成输出 *M*×1 复数值列向量

波束形成输出，指定为 *M*×1 复数值列向量。*M* 是信号样本数。

**数据类型：** `double`
**复数支持：** Yes

### **W** — 波束形成器权值输出 *N*×1 复数值列向量

波束形成器权值输出，指定为 *N*×1 复数值列向量。*N* 是阵列阵元数。

#### 依赖关系

要启用此端口，请选中 **启用权值输出** 复选框。

**数据类型：** `double`
**复数支持：** Yes

## 参数

### **约束矩阵** — LCMV 波束形成器约束矩阵 `complex([1;1])`（默认） | *N*×*K* 复数值矩阵

LCMV 波束形成器约束矩阵，指定为 *N*×*K* 复数值矩阵。矩阵的每一列是一个约束。*N* 是传感器阵列中的阵元数，*K* 是约束数量。*K* 必须小于或等于传感器数量，*N*，*K* ≤ *N*

### **期望响应向量** — LCMV 波束形成的期望响应 `1`（默认） | 实数值 *K*×1 列向量

LCMV 波束形成器的期望响应，指定为实数值 *K*×1 列向量。*K* 是 **约束矩阵** 中的约束数量。该向量中的每个元素定义 **约束矩阵** 参数对应列中指定的约束的期望响应。

### **对角加载因子** — 对角加载因子 正标量

对角加载因子，指定为正标量。对角加载是一种用于实现稳健波束形成性能的技术，尤其是在样本支持较小时。

### **启用训练数据输入** — 启用训练数据输入端口 `off`（默认） | `on`

启用训练数据输入端口，指定为 `off` 或 `on`。要启用训练数据输入端口 `XT`，请选中此复选框。

### **启用权值输出** — 启用波束形成器权值的输出 `off`（默认） | `on`

启用波束形成权值输出端口，指定为 `off` 或 `on`。要启用波束形成权值输出端口 `W`，请选中此复选框。

### **仿真方式** — 模块仿真方法 `Interpreted Execution`（默认） | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

解释执行在开发和调整模型时非常有用。该模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意时，可以使用 `Code Generation` 运行该模块。长时间仿真使用生成代码比解释执行运行得更快。您可以重复执行而无需重新编译，但如果您更改任何模块参数，则该模块会在执行前自动重新编译。

此表显示 **仿真方式** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **仿真方式** 指定的模块模式会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 该模块使用 MATLAB 解释器执行。 | 该模块使用 MATLAB 解释器执行。 | 从模型创建独立的可执行文件。 |
| `Code Generation` | 该模块经过编译。 | 模型中的所有模块都会编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认值：** `Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Beamforming

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2014b 中引入**

## 描述

窄带线性约束最小方差 (LCMV) 波束形成器

LCMV Beamformer 模块执行窄带线性约束最小方差 (LCMV) 波束形成。约束数量必须小于阵列中阵元或子阵的数量。
