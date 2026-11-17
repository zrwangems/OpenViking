---
type: simulink-block
title: 'EVM Measurement'
family: 'utility-blocks'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Utility Blocks'
documentation_page: 'evmmeasurement'
documentation_source_path: 'ref/evmmeasurement.html'
language: zh-CN
chinese_source: worker-translation
---

# EVM Measurement

## 端口

### 输入

### **Ref** — 参考信号数组

参考信号，指定为最多三维的数组。如果指定此输入，则该对象通过将此输入用作参考星座来测量 `Rcv` 输入的 EVM。

此输入的维度必须与 `Rcv` 输入的维度匹配。该对象将此输入的每个元素用作 `Rcv` 输入中对应元素的参考符号。

#### 依赖关系

要启用此端口，请将 **参考信号** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** `Yes`

### **Rcv** — 接收信号数组

接收信号，指定为最多三维的数组。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** `Yes`

### 输出

### **RMS** — 百分比 RMS EVM 标量

在配置的测量区间内，以标量形式返回的百分比 RMS EVM。

**数据类型：** `double`

### **max** — 最大百分比 EVM 标量

在配置的测量区间内，以标量形式返回的最大百分比 EVM。

#### 依赖关系

要启用此端口，请将 **输出最大 EVM** 参数设置为 `On`。

**数据类型：** `double`

### **X%** — *X*% 的 EVM 测量值低于此值的标量，范围为 [0, 100]

自上次重置以来，*X*% 的 EVM 测量值低于此值，以 [0, 100] 范围内的标量形式返回。请在 **X 百分位值 (%)** 参数中设置 *X* 的值。

#### 依赖关系

要启用此端口，请将 **输出 X 百分位 EVM** 参数设置为 `On`。

**数据类型：** `double`

### **nSym** — 符号数，正整数

用于测量 *X* 百分位 EVM 的符号数，以正整数形式返回。

#### 依赖关系

要启用此端口，请将 **输出 X 百分位 EVM** 和 **输出处理的符号数** 参数设置为 `On`。

**数据类型：** `double`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

### **通过以下方式归一化 RMS 误差向量** — 归一化方法 `Average reference signal power`（默认） | `Average constellation power` | `Peak constellation power`

EVM 计算中使用的归一化方法，指定为 `Average reference signal power`、`Average constellation power` 或 `Peak constellation power`。有关详细信息，请参阅算法。

### **平均星座功率** — 平均星座功率 `1`（默认） | 正标量

平均星座功率，以 watts 为单位，指定为正标量。

#### 依赖关系

要启用此参数，请将 **通过以下方式归一化 RMS 误差向量** 参数设置为 `Average constellation power`。

### **峰值星座功率** — 峰值星座功率 `1`（默认） | 正标量

峰值星座功率，以 watts 为单位，指定为正标量。

#### 依赖关系

要启用此参数，请将 **通过以下方式归一化 RMS 误差向量** 参数设置为 `Peak constellation power`。

### **参考信号** — 参考信号源 `Input port` | `Estimated from reference constellation`

参考信号源。要提供用于测量接收信号的显式参考信号，请将此参数设置为 `Input port`。要针对参考星座测量接收信号的 EVM，请将此参数设置为 `Estimated from reference constellation`。

### **参考星座** — 参考星座 `constellation(pskmod((0:3)',4,pi/4,"bin"))`（默认） | 向量

参考星座点，指定为复数值或实数值向量。

#### 依赖关系

要启用此参数，请将 **参考信号** 参数设置为 `Estimated from reference constellation`。

### **测量区间** — 测量区间源 `Input length`（默认） | `Entire history` | `Custom` | `Custom with periodic reset`

用于 RMS 和最大 EVM 测量的测量区间源，指定为以下值之一。

- `Input length` — 仅使用当前样本测量 EVM。
- `Entire history` — 对所有样本测量 EVM。
- `Custom` — 在您指定的区间内测量 EVM，并使用滑动窗口。
- `Custom with periodic reset` — 在您指定的区间内测量 EVM，并在每个区间测量后重置模块。

### **自定义测量区间** — 自定义测量区间 `100`（默认） | 正整数

自定义测量区间，以 samples 为单位，指定为正整数。

#### 依赖关系

要启用此参数，请将 **测量区间** 参数设置为 `Custom` 或 `Custom with periodic reset`。

### **平均维度** — 平均维度 `1`（默认） | 范围 [1, 3] 内的整数向量

模块对 EVM 测量值求平均所沿的维度，指定为范围 [1, 3] 内的整数或整数行向量。例如，要沿行求平均，请将此参数设置为 `2`。

此模块支持沿其进行平均的维度上的可变大小输入。但是，非平均维度的输入大小必须保持不变。例如，如果输入的大小为 `[1000 3 2]`，并且您将此参数设置为 `[1 3]`，则输出大小为 `[1 3 1]`，并且第二个维度中的元素数必须固定为 `3`。

### **输出最大 EVM** — 用于添加 `max` 端口以输出最大 EVM 测量值的选项 `Off`（默认） | `On`

用于添加 `max` 端口以输出最大 EVM 测量值的选项。

### **输出 X 百分位 EVM** — 用于添加 `X%` 端口以输出 *X* 百分位 EVM 测量值的选项 `Off`（默认） | `On`

用于添加 `X%` 端口以输出 *X* 百分位 EVM 测量值的选项。将此参数设置为 `On` 时，*X* 百分位 EVM 测量值会一直保留，直到您重置模块。该模块使用自上次重置以来的所有输入帧执行这些测量。您可以在 **X 百分位值 (%)** 参数中设置 *X* 的值。

### **X 百分位值 (%)** — *X*% 的 EVM 测量值低于此值的数值 `95`（默认） | 范围 [0, 100] 内的标量

*X*% 的 EVM 测量值低于此值，指定为范围 [0, 100] 内的标量。

#### 依赖关系

要启用此参数，请将 **输出 X 百分位 EVM** 参数设置为 `On`。

### **输出处理的符号数** — 用于添加 `nSym` 端口以输出符号数的选项 `Off`（默认） | `On`

用于添加 `nSym` 端口以输出用于测量 *X* 百分位 EVM 的符号数的选项。

#### 依赖关系

要启用此参数，请将 **输出 X 百分位 EVM** 参数设置为 `On`。

### **仿真方式** — 要运行的仿真类型 `Interpreted execution`（默认） | `Code generation`

要运行的仿真类型，指定为 `Interpreted execution` 或 `Code generation`。

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项需要的启动时间较短，但后续仿真的速度比 `Code generation` 选项慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比 `Interpreted execution` 选项快。

有关详细信息，请参阅解释执行与代码生成 (Simulink)。

## 所属库

Communications Toolbox / Utility Blocks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

要在使用此模块的模型中生成代码，必须启用 **Dynamic Memory Allocation in MATLAB Functions**。有关详细信息，请参阅 MATLAB 函数中的动态内存分配 (Simulink)。

## 版本历史

**在 R2009b 中引入**

## 描述

测量误差向量幅度 (EVM)

EVM Measurement 模块测量接收信号的均方根 (RMS) EVM、最大 EVM 和百分位 EVM。EVM 是调制器或解调器性能的指示。

此图标显示启用了所有端口的模块。启用所有端口的 EVM Measurement 模块。
