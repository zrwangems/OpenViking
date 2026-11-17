---
type: simulink-block
title: 'Discrete Varying State Space'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Linear Parameter Varying'
documentation_page: 'discretevaryingstatespace'
documentation_source_path: 'ref/discretevaryingstatespace.html'
language: zh-CN
chinese_source: worker-translation
---

# Discrete Varying State Space

## 端口

### 输入

### **uk** — 系统输入 标量 | 向量

系统输入信号。

### **A** — 状态矩阵 矩阵

状态矩阵，维度为 *Nx*×*Nx*，其中 *Nx* 是系统状态的数量。

### **B** — 输入矩阵 矩阵

输入矩阵，维度为 *Nx*×*Nu*，其中 *Nu* 是系统输入的数量。

### **C** — 输出矩阵 矩阵

输出矩阵，维度为 *Ny*×*Nx*，其中 *Ny* 是系统输出的数量。

### **D** — 前馈矩阵 矩阵

前馈矩阵，维度为 *Ny*×*Nu*。

对于零直通状态空间模型，清除 **Enable feedthrough** 复选框。清除此复选框将禁用 **D** 输入端口。*（自 R2023a 起）*

### **dx0** — 状态导数偏移 矩阵

*自 R2024a 起*

状态导数偏移，维度为 *Nx*×1，其中 *Nx* 是系统状态的数量。

#### 依赖关系

要启用此端口，请选择 **Enable state derivative offsets dx0**。*（自 R2024a 起）*

### **x0** — 状态偏移 矩阵

*自 R2024a 起*

状态偏移，维度为 *Nx*×1，其中 *Nx* 是系统状态的数量。

#### 依赖关系

要启用此端口，请选择 **Enable state offsets x0**。*（自 R2024a 起）*

### **u0** — 输入偏移 矩阵

*自 R2024a 起*

输入偏移，维度为 *Nu*×1，其中 *Nu* 是系统输入的数量。

#### 依赖关系

要启用此端口，请选择 **Enable input offsets u0**。*（自 R2024a 起）*

### **y0** — 输出偏移 矩阵

*自 R2024a 起*

输出偏移，维度为 *Ny*×1，其中 *Ny* 是系统输出的数量。

#### 依赖关系

要启用此端口，请选择 **Enable output offsets y0**。*（自 R2024a 起）*

### **IC** — 初始条件 向量

*自 R2024b 起*

用于启动仿真的局部模型初始条件，指定为长度等于模型状态数量的向量。

#### 依赖关系

要启用此端口，请将 **Initial condition source** 设置为 `external`。
### 输出

### **yk** — 系统输出 标量 | 向量

系统输出信号。

### **xk** — 当前状态向量 向量

当前状态值。

#### 依赖关系

要启用此端口，请选择 **Output states** 参数。

### **xk+1** — 下一状态向量 向量

下一时间步的状态值。

#### 依赖关系

要启用此端口，请选择 **Output state updates** 参数。

## 参数

### 主选项卡

### **Initial condition source** — 使用外部信号设置初始条件的选项 `internal`（默认）| `external`

*自 R2024b 起*

指定初始条件来源。

- `internal` — 使用 **Initial condition** 参数指定状态的初始条件。
- `external` — 在模块的 **IC** 输入端口指定状态的初始条件。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `InitialConditionSource` |
| **值**：| `internal`（默认）| `external` |

### **Initial conditions** — 系统初始条件 0（默认）| 标量 | 向量

初始状态值，指定为长度等于模型状态数量的向量。

#### 依赖关系

要启用此参数，请将 **Initial condition source** 设置为 `internal`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `InitialCondition` |
| **值**：| `"0"`（默认）| 带引号的初始状态值 |

**示例：** `set_param(gcb,"InitialCondition","[0
0.1]")`

### **Sample time (-1 for inherited)** — 模块采样时间 –1（默认）| 正标量

模块采样时间，指定为 –1（继承采样时间）或正标量值。

### **Output states** — 提供状态输出 on（默认）| off

选择以启用状态值输出端口 **x**。

### **Output state derivatives** — 提供状态更新 on（默认）| off

选择以启用状态更新输出端口 **xk+1**。

### **Enable feedthrough** — 为直通矩阵添加输入端口 `on`（默认）| `off`

*自 R2023a 起*

为具有直接直通的状态空间模型启用 **D** 输入端口。对于零直通模型，清除此复选框。对于零直通模型禁用该端口在数值上比向端口馈入零常量更可靠。

### 偏移选项卡

### **Enable state offsets x0** — 为状态偏移添加输入端口 off（默认）| on

启用 **x0** 输入端口以指定变化的状​​态偏移。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `InputX0` |
| **值**：| `"off"`（默认）| `"on"` |

### **Enable state derivative offsets dx0** — 为状态导数偏移添加输入端口 off（默认）| on

启用 **dx0** 输入端口以指定变化的状态导数偏移。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `InputDX0` |
| **值**：| `"off"`（默认）| `"on"` |

### **Enable input offsets u0** — 为输入偏移添加输入端口 off（默认）| on

启用 **u0** 输入端口以指定变化的输入偏移。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `InputU0` |
| **值**：| `"off"`（默认）| `"on"` |

### **Enable output offsets y0** — 为输出偏移添加输入端口 off（默认）| on

启用 **y0** 输入端口以指定变化的输出偏移。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `InputY0` |
| **值**：| `"off"`（默认）| `"on"` |

## 所属库

Control System Toolbox / Linear Parameter Varying

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**在 R2017b 中引入**

### R2024b：将初始条件作为模块输入从外部指定

该模块现在允许您在模块输入端口 **IC** 指定初始状态值。要启用此端口，请将 **Initial condition source** 参数设置为 `external`。

### R2024b：初始条件参数 `x0` 重命名为 `InitialCondition`

用于编程的初始状态参数 `x0` 现在称为 `InitialCondition`。如果您的代码以编程方式设置此参数，例如使用 `set_param(blockPath,"x0","[0
0.1]")`，请将代码更新为 `set_param(blockPath,"InitialCondition","[0 0.1]")`。

### R2024a：支持指定偏移

使用模块参数的 **Offsets** 选项卡启用输入端口，以指定变化偏移的瞬时值。

### R2023a：添加了 Enable feedthrough 复选框

对于零直通状态空间模型，清除 **Enable feedthrough** 复选框。清除此复选框将禁用 **D** 输入端口。对于零直通模型禁用该端口在数值上比向端口馈入零常量更可靠。

## 描述

具有变化矩阵值的离散时间状态空间模型

使用此模块实现具有变化矩阵的离散时间状态空间模型。将状态矩阵 *A*、输入矩阵 *B*、输出矩阵 *C* 和前馈矩阵 *D* 的瞬时值馈入相应的输入端口。系统响应由下式给出：

xk+1=Axk+Bukyk=Cxk+Duk，

其中 *uk* 是系统输入，*yk* 是系统输出，*xk* 是当前系统状态，*x**k*+1 是下一时间步的系统状态。

该模块还允许您指定变化的偏移 *（自 R2024a 起）*。此时，系统响应由下式给出：

xk+1=dx0k+A(xk−x0k)+B(uk−u0k)yk=y0k+C(xk−x0k)+D(uk−u0k)，

其中 *u*0*k* 是输入偏移，*y*0*k* 是输出偏移，*x*0*k* 和 *dx*0*k* 分别是状态偏移和状态导数偏移。

使用此模块以及 Linear Parameter Varying 库中的其他模块，可以实现具有可变参数或系数的常见控制元件。有关详细信息，请参阅 Model Gain-Scheduled Control Systems in Simulink。

**注意**

避免使 **C** 和 **D** 矩阵依赖于系统输出 **yk**。如果您有这种依赖关系，则得到的状态空间方程 *yk* = *C*(*yk*)*xk* + *D*(*yk*)*uk* 会创建代数环，因为计算输出值 *yk* 需要知道输出值。此代数环容易产生不稳定和发散。相反，请尝试用时间 *t*、模块输入 **uk** 和状态输出 **xk** 来表示 **C** 和 **D**。

出于类似原因，避免使 **A** 和 **B** 依赖于 **xk+1** 输出。请注意，当 **yk** 是状态和输入的固定组合时（换句话说，当 *yk* = *C**xk* + *D**uk*，其中 *C* 和 *D* 是常量矩阵时），**A** 和 **B** 依赖于 **yk** 是安全的。
