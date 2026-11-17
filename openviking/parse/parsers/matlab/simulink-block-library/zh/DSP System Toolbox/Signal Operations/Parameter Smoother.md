---
type: simulink-block
title: 'Parameter Smoother'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'parametersmoother'
documentation_source_path: 'ref/parametersmoother.html'
language: zh-CN
chinese_source: worker-translation
---

# Parameter Smoother

## 端口

### 输入

### **P** — 要平滑的输入参数 标量 | 向量 | 矩阵

将要平滑的输入参数指定为标量、向量或矩阵。如果 **Number of parameters** 的值大于 1，则该模块将输入端口标记为 **P1**、**P2**，依此类推。

在您选择 **Specify smoothing factor from input port** 或 **Specify smoothing time from input port** 参数，或者将 **Number of parameters** 设置为大于 1 的值之前，此端口是未命名的。

**数据类型：** `single` | `double`

### **alpha** — 平滑因子 范围为 [0, 1) 的标量

将平滑因子 *α* 指定为范围为 [0, 1) 的标量。当 *α* = 0 时，该模块不对参数进行平滑。随着 *α* 趋近于 1，平滑程度以及因此重新设计的次数会增加。有关 *α* 对平滑影响的详细信息，请参阅 Parameter Smoothing。

#### 依赖关系

要启用此端口：

- 将 **Smoothing mode** 参数设置为 `Smoothing factor`。
- 选择 **Specify smoothing factor from input port** 参数。

**数据类型：** `single` | `double`

### **tau** — 平滑时间 非负标量

将平滑时间 *τ*（以秒为单位）指定为非负标量。此值表示参数变化到 `exp`(−*T*/*τ*)×当前值 + (1−`exp`(−*T*/*τ*))×目标值所需的时间，其中 *T* 是您在 **Sample time (−1 for inherited)** 参数中指定的值。有关 *τ* 对平滑影响的详细信息，请参阅 Parameter Smoothing。

#### 依赖关系

要启用此端口：

- 将 **Smoothing mode** 参数设置为 `Smoothing time`。
- 选择 **Specify smoothing time from input port** 参数。

**数据类型：** `single` | `double`
### 输出

### **Output** — 平滑后的参数 标量 | 向量 | 矩阵

参数的平滑值，以标量、向量或矩阵形式返回。这是参数的瞬时值，它会不断变化，直到参数达到您在输入端口 **P** 处指定的目标值。

**数据类型：** `single` | `double`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Number of parameters** — 输入参数的数量 `1`（默认）| 正整数

将要平滑的参数数量指定为正整数。此参数的值决定了模块上输入端口的数量。

### **Smoothing mode** — 用于平滑的模式 `Smoothing factor`（默认）| `Smoothing time`

将用于平滑的模式指定为以下之一：

- `Smoothing factor` –– 在模块对话框中或通过 **alpha** 端口指定平滑因子。
- `Smoothing time` –– 在模块对话框中或通过 **tau** 端口指定平滑时间。

有关这两种模式的详细信息，请参阅 Parameter Smoothing。

### **Specify smoothing factor from input port** — 从输入端口指定平滑因子的选项 `off`（默认）| `on`

选择此参数以从输入端口 **alpha** 指定平滑因子。当您清除此参数时，可以使用 **Smoothing factor (between 0 and 1)** 参数在模块对话框中指定平滑因子。

#### 依赖关系

- 要启用此参数，请将 **Smoothing mode** 参数设置为 `Smoothing factor`。

### **Smoothing factor (between 0 and 1)** — 平滑因子 `0.6`（默认）| 范围为 [0, 1) 的标量

将平滑因子 *α* 指定为范围为 [0, 1) 的标量。当 *α* = 0 时，该模块不对参数进行平滑。随着 *α* 趋近于 1，平滑程度以及因此重新设计的次数会增加。有关 *α* 对平滑影响的详细信息，请参阅 Parameter Smoothing。

**可调：** 是

#### 依赖关系

要启用此参数：

- 将 **Smoothing mode** 参数设置为 `Smoothing factor`。
- 清除 **Specify smoothing factor from input port** 参数。

**数据类型：** `single` | `double`

### **Specify smoothing time from input port** — 从输入端口指定平滑时间的选项 `off`（默认）| `on`

选择此参数以从输入端口 **tau** 指定平滑时间。当您清除此参数时，可以使用 **Smoothing time constant (seconds)** 参数在模块对话框中指定平滑时间。

#### 依赖关系

- 要启用此参数，请将 **Smoothing mode** 参数设置为 `Smoothing time`。

### **Smoothing time constant (seconds)** — 以秒为单位的平滑时间 `10`（默认）| 非负标量

将平滑时间 *τ*（以秒为单位）指定为非负标量。此值表示参数变化到 `exp`(−*T*/*τ*)×当前值 + (1−`exp`(−*T*/*τ*))×目标值所需的时间，其中 *T* 是您在 **Sample time (−1 for inherited)** 参数中指定的值。有关 *τ* 对平滑影响的详细信息，请参阅 Parameter Smoothing。

**可调：** 是

#### 依赖关系

要启用此参数：

- 将 **Smoothing mode** 参数设置为 `Smoothing time`。
- 清除 **Specify smoothing time from input port** 参数。

**数据类型：** `single` | `double`

### **Sample time (−1 for inherited)** — 输入参数的采样时间 `-1`（默认）| 正标量

将输入参数 *T* 的采样时间指定为 `-1`（表示继承）或以秒为单位的正标量。此值决定了模块更新输入参数瞬时值的频率，直到达到目标值。

#### 依赖关系

要启用此参数，请将 **Smoothing mode** 参数设置为 `Smoothing time`。

**数据类型：** `single` | `double`

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不发生变化，C 代码将在后续仿真中重用。此选项需要额外的启动时间，但可提供更快的后续仿真。

## 所属库

DSP System Toolbox / Signal Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

使用指数平滑对输入参数进行平滑

Parameter Smoother 模块逐步更新输入滤波器参数，直到参数达到所需值。该模块使用一阶 IIR 滤波器对参数进行平滑。有关详细信息，请参阅 Parameter Smoothing。
