---
type: simulink-block
title: 'Varying State Space'
family: 'linear-parameter-varying'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Linear Parameter Varying'
documentation_page: 'varyingstatespace'
documentation_source_path: 'ref/varyingstatespace.html'
language: zh-CN
chinese_source: worker-translation
---

# Varying State Space

## 端口

### 输入

### **u** — 系统输入 scalar | vector

系统输入信号。

### **A** — 状态矩阵 matrix

维度为 *Nx*-by-*Nx* 的状态矩阵，其中 *Nx* 是系统状态数。

### **B** — 输入矩阵 matrix

维度为 *Nx*-by-*Nu* 的输入矩阵，其中 *Nu* 是系统输入数。

### **C** — 输出矩阵 matrix

维度为 *Ny*-by-*Nx* 的输出矩阵，其中 *Ny* 是系统输出数。

### **D** — 前馈矩阵 matrix

维度为 *Ny*-by-*Nu* 的前馈矩阵。

对于零馈通状态空间模型，请清除 **Enable feedthrough** 复选框。清除此复选框将禁用 **D** 输入端口。*（自 R2023a 起）*

### **dx0** — 状态导数偏移量 matrix

*自 R2024a 起*

维度为 *Nx*-by-1 的状态导数偏移量，其中 *Nx* 是系统状态数。

#### 依赖关系

要启用此端口，请选择 **Enable state derivative offsets dx0**。

### **x0** — 状态偏移量 matrix

*自 R2024a 起*

维度为 *Nx*-by-1 的状态偏移量，其中 *Nx* 是系统状态数。

#### 依赖关系

要启用此端口，请选择 **Enable state offsets x0**。

### **u0** — 输入偏移量 matrix

*自 R2024a 起*

维度为 *Nu*-by-1 的输入偏移量，其中 *Nu* 是系统输入数。

#### 依赖关系

要启用此端口，请选择 **Enable input offsets u0**。

### **y0** — 输出偏移量 matrix

*自 R2024a 起*

维度为 *Ny*-by-1 的输出偏移量，其中 *Ny* 是系统输出数。

#### 依赖关系

要启用此端口，请选择 **Enable output offsets y0**。

### **IC** — 初始条件 vector

*自 R2024b 起*

用于局部模型以启动仿真的初始条件，指定为长度等于模型状态数的向量。

#### 依赖关系

要启用此端口，请将 **Initial condition source** 设置为 `external`。

### 输出

### **y** — 系统输出 scalar | vector

系统输出信号。

### **x** — 当前状态向量 vector

当前状态值。

#### 依赖关系

要启用此端口，请选择 **Output states** 参数。

### **dx** — 状态导数 vector

**x** 中相应状态的当前导数。

#### 依赖关系

要启用此端口，请选择 **Output state derivatives** 参数。

## 参数

### Main 选项卡

### **Initial condition source** — 使用外部信号设置初始条件的选项 `internal`（默认）| `external`

*自 R2024b 起*

指定初始条件源。

- `internal` — 使用 **Initial condition** 参数指定状态的初始条件。
- `external` — 在模块的 **IC** 输入端口指定状态的初始条件。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数:** | `InitialConditionSource` |
| **值:** | `internal`（默认）| `external` |

### **Initial conditions** — 系统初始条件 0（默认）| scalar | vector

初始状态值，指定为长度等于模型状态数的向量。

#### 依赖关系

要启用此参数，请将 **Initial condition source** 设置为 `internal`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数:** | `InitialCondition` |
| **值:** | `"0"`（默认）| 用引号括起来的初始状态值 |

**示例：** `set_param(gcb,"InitialCondition","[0
0.1]")`

### **State names** — 系统状态名称 `''`（默认）| character vector | cell array

为标识系统状态，请将状态名称指定为：

- character vector，用于单状态被控对象。
- Cell array of character vectors，用于多状态被控对象。

### **Output states** — 提供状态输出 on（默认）| off

选中此参数可启用状态值输出端口 **x**。

### **Output state derivatives** — 提供状态导数 on（默认）| off

选中此参数可启用状态导数输出端口 **dx**。

### **Enable feedthrough** — 为前馈矩阵添加输入端口 on（默认）| off

*自 R2023a 起*

为具有直接馈通的状态空间模型启用 **D** 输入端口。对于零馈通模型，请清除此复选框。对于零馈通模型，禁用该端口比向该端口馈入零常量在数值上更可靠。

### Offsets 选项卡

### **Enable state offsets x0** — 为状态偏移量添加输入端口 off（默认）| on

启用 **x0** 输入端口，以指定可变状态偏移量。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数:** | `InputX0` |
| **值:** | `"off"`（默认）| `"on"` |

### **Enable state derivative offsets dx0** — 为状态导数偏移量添加输入端口 off（默认）| on

启用 **dx0** 输入端口，以指定可变状态导数偏移量。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数:** | `InputDX0` |
| **值:** | `"off"`（默认）| `"on"` |

### **Enable input offsets u0** — 为输入偏移量添加输入端口 off（默认）| on

启用 **u0** 输入端口，以指定可变输入偏移量。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数:** | `InputU0` |
| **值:** | `"off"`（默认）| `"on"` |

### **Enable output offsets y0** — 为输出偏移量添加输入端口 off（默认）| on

启用 **y0** 输入端口，以指定可变输出偏移量。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数:** | `InputY0` |
| **值:** | `"off"`（默认）| `"on"` |

## 所属库

Control System Toolbox / Linear Parameter Varying

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**引入于 R2017b**

### R2024b: 将初始条件从外部指定为模块输入

此模块现在允许您在模块输入端口 **IC** 处指定初始状态值。要启用此端口，请将 **Initial condition source** 参数设置为 `external`。

### R2024b: 初始条件参数 `x0` 重命名为 `InitialCondition`

用于编程的初始状态参数 `x0` 现在称为 `InitialCondition`。如果您的代码以编程方式设置此参数（例如使用 `set_param(blockPath,"x0","[0
0.1]")`），请将代码更新为 `set_param(blockPath,"InitialCondition","[0 0.1]")`。

### R2024a: 支持指定偏移量

使用模块参数的 **Offsets** 选项卡启用输入端口，以指定可变偏移量的瞬时值。

### R2023a: 添加了 Enable feedthrough 复选框

对于零馈通状态空间模型，请清除 **Enable feedthrough** 复选框。清除此复选框将禁用 **D** 输入端口。对于零馈通模型，禁用该端口比向该端口馈入零常量在数值上更可靠。

## 描述

矩阵值可变的状态空间模型

使用此模块可实现具有可变矩阵的连续时间状态空间模型。将状态矩阵 *A*、输入矩阵 *B*、输出矩阵 *C* 和前馈矩阵 *D* 的瞬时值馈送到相应的输入端口。系统响应由下式给出：

dx=Ax+Buy=Cx+Du,

其中，*u* 是系统输入，*y* 是系统输出，*x* 和 *dx* 分别是状态向量和状态导数。

该模块还允许您指定可变偏移量 *（自 R2024a 起）*。此时，系统响应由下式给出：

dx=dx0+A(x−x0)+B(u−u0)y=y0+C(x−x0)+D(u−u0),

其中，*u*0 是输入偏移量，*y*0 是输出偏移量，*x*0 和 *dx*0 分别是状态偏移量和状态导数偏移量。

使用此模块以及 Linear Parameter Varying 库中的其他模块，可实现具有可变参数或系数的常用控制元素。有关详细信息，请参阅“在 Simulink 中对增益调度控制系统建模”。

**注意**

避免使 **C** 和 **D** 矩阵依赖于系统输出 **y**。如果存在这种依赖关系，则得到的状态空间方程 *y* = *C*(*y*)*x* + *D*(*y*)*u* 会创建代数环，因为计算输出值 *y* 需要知道输出值本身。此代数环容易导致不稳定和发散。相反，请尝试用时间 *t*、模块输入 **u** 和状态输出 **x** 来表示 **C** 和 **D**。

出于类似原因，请避免使 **A** 和 **B** 依赖于 **dx** 输出。请注意，当 **y** 是状态和输入的固定组合时（换言之，当 *y* = *C**x* + *D**u*，其中 *C* 和 *D* 是常量矩阵时），**A** 和 **B** 依赖于 **y** 是安全的。
