---
type: simulink-block
title: 'Fourth-Order Section Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Implementations'
documentation_page: 'fourthordersectionfilter'
documentation_source_path: 'ref/fourthordersectionfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Fourth-Order Section Filter

## 端口

### 输入

### **x** — 输入信号向量 | 矩阵

输入信号，指定为向量或矩阵。输入可以是可变大小信号。也就是说，信号的帧大小可以在仿真期间改变，但通道数不能改变。

在将 **系数来源** 参数设置为 `Input ports` 之前，此端口未命名。

**数据类型：** `single` | `double`
**复数支持：** 是

### **Num** — 分子系数 *P*×5 矩阵

将四阶节滤波器的分子系数指定为 *P*×5 矩阵，其中 *P* 是滤波器节数。有关此输入端口的更多详细信息，请参见 **滤波器的分子系数**。

在仿真运行时，您可以更改分子系数中的节数（行数）。您还可以更改系数值。

#### 依赖关系

此端口仅在将 **系数来源** 参数设置为 `Input ports` 时出现。

**数据类型：** `single` | `double`
**复数支持：** 是

### **Den** — 分母系数 *P*×5 矩阵 | *P*×4 矩阵

将四阶节滤波器的分母系数指定为 *P*×5 矩阵或 *P*×4 矩阵，其中 *P* 是滤波器节数。有关此输入端口的更多详细信息，请参见 **滤波器的分母系数**。

在仿真运行时，您可以更改分母系数中的节数（行数）。您还可以更改系数值。

#### 依赖关系

此端口仅在将 **系数来源** 参数设置为 `Input ports` 时出现。

**数据类型：** `single` | `double`
**复数支持：** 是

### 输出

### **y** — 滤波后输出向量 | 矩阵

滤波后输出，返回为向量或矩阵。输出的大小和数据类型与输入相同。如果输入信号、分子系数或分母系数中任一项为复数，则输出信号为复数。

在将 **系数来源** 参数设置为 `Input ports` 之前，此端口未命名。

**数据类型：** `single` | `double`
**复数支持：** 是

## 参数

### **系数来源** — 滤波器系数来源 `Dialog parameters`（默认）| `Input ports` | `Filter object`

将滤波器系数来源指定为以下之一：

- `Dialog parameters` –– 在模块对话框中通过 **滤波器的分子系数** 和 **滤波器的分母系数** 参数指定滤波器系数。
- `Input ports` –– 通过 **Num** 和 **Den** 输入端口指定滤波器系数。
- `Filter object` –– 使用 `dsp.FourthOrderSectionFilter` 对象指定滤波器系数。

要查看滤波器响应，请将此参数设置为 `Dialog parameters` 或 `Filter object`，然后单击 **查看滤波器响应** 按钮。

### **滤波器的分子系数** — 分子系数 [`0.07795634 0 -0.15591268 0 0.07795634`; `0.06188520 0 -0.12377039 0 0.06188520`]（默认）| *P*×5 矩阵

将四阶节滤波器的分子系数 **b** 指定为 *P*×5 矩阵，其中 *P* 是滤波器节数。

b=[b01b11b21b31b41b02b12b22b32b42⋮⋮⋮⋱⋮b0Pb1Pb2Pb3Pb4P]

在传递函数形式中，四阶节滤波器可以使用以下方程表示：

H(z)=∏k=1PHk(z)=∏k=1Pb0k+b1kz−1+b2kz−2+b3kz−3+b4kz−4a0k+a1kz−1+a2kz−2+a3kz−3+a4kz−4

其中，

- **a** –– 分母系数矩阵。有关如何指定此矩阵的更多详细信息，请参见 **滤波器的分母系数**。
- *k* –– 行索引。

在仿真期间不能更改此参数的大小，但可以更改其值。

#### 依赖关系

要启用此参数，请将 **系数来源** 设置为 `Dialog parameters`。

**可调：** 是

**数据类型：** `single` | `double`
**复数支持：** 是

### **滤波器的分母系数** — 分母系数 [`1 0 1.32091343 0 0.63273879`; `1 0 1.04859957 0 0.29614035`]（默认）| *P*×5 矩阵 | *P*×4 矩阵

将四阶节滤波器的分母系数 **a** 指定为 *P*×5 矩阵或 *P*×4 矩阵，其中 *P* 是滤波器节数。

a=[a01a11a21a31a41a02a12a22a32a42⋮⋮⋮⋱⋮a0Pa1Pa2Pa3Pa4P]

该模块算法假定首项系数的值始终为 1。如果分母的大小为 *P*×4，则该模块算法会在第一列中放置 1，使分母大小为 *P*×5。如果分母的大小为 *P*×5，且第一列中的元素不等于 1，则该算法忽略第一列中的值，并用 1 替换它们。

在传递函数形式中，四阶节滤波器可以使用以下方程表示：

H(z)=∏k=1PHk(z)=∏k=1Pb0k+b1kz−1+b2kz−2+b3kz−3+b4kz−4a0k+a1kz−1+a2kz−2+a3kz−3+a4kz−4

其中，

- **b** –– 分子系数矩阵。有关如何指定此矩阵的更多详细信息，请参见 **滤波器的分子系数**。
- *k* –– 行索引。

在仿真期间不能更改此参数的大小，但可以更改其值。

#### 依赖关系

要启用此参数，请将 **系数来源** 设置为 `Dialog parameters`。

**可调：** 是

**数据类型：** `single` | `double`
**复数支持：** 是

### **滤波器** — 滤波器对象 `dsp.FourthOrderSectionFilter` 对象

使用 `dsp.FourthOrderSectionFilter` 对象指定滤波器系数。您可以直接在 **滤波器** 参数中输入此对象。或者，您可以在 MATLAB® 工作区或模型工作区中创建此对象，并在 **滤波器** 参数中指定滤波器变量。当您将滤波器指定为变量并仿真模型时，不能在两次仿真之间更改工作区中滤波器系数的复数性、数据类型和大小。

#### 依赖关系

要启用此参数，请将 **系数来源** 设置为 `Filter object`。

### **查看滤波器响应** — 可视化频率响应 `gui button`

单击此按钮会打开滤波器可视化工具，并显示四阶节滤波器的幅值响应。该响应基于您在模块对话框中指定的系数。如果您将 **系数来源** 设置为 `Input ports` 并单击 **应用**，则无法使用此按钮查看幅值响应。

要在可视化工具运行时更新滤波器响应，请修改模块对话框中的系数，并单击 **应用**。

您可以从可视化工具的界面配置绘图设置和频率响应测量。

在 **Scope** 选项卡上，您可以启用图例，指定绘制滤波器的幅值响应和相位响应，修改绘图设置，生成用于重新创建绘图的脚本，甚至保存或共享设置。在 **Measurements** 选项卡上，您可以启用数据游标，并显示滤波器响应的峰值。

有关滤波器可视化工具界面及其工具的更多详细信息，请参见配置滤波器可视化工具。

#### 依赖关系

要启用此按钮，您必须直接在模块对话框中或通过 `dsp.FourthOrderSectionFilter` 对象指定滤波器系数。

### **仿真使用** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` –– 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。此选项需要额外的启动时间，但可提供更快的后续仿真。

## 所属库

DSP System Toolbox / Filtering / Filter Implementations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

### R2022b：Fourth-Order Section Filter 模块增强

从 R2022b 开始，当您通过 Fourth-Order Section Filter 模块的输入端口传递分子和分母系数时，可以在仿真运行时更改滤波器系数中的节数（行数）。

您还可以使用 `dsp.FourthOrderSectionFilter` 对象在模块对话框中指定系数。将 **系数来源** 设置为 `Filter object`，并在 **滤波器** 参数中直接指定 `dsp.FourthOrderSectionFilter` 对象。或者，您可以在 MATLAB 工作区或模型工作区中创建此对象，并在 **滤波器** 参数中指定滤波器变量。

## 描述

实现四阶节滤波器的级联

Fourth-Order Section Filter 模块在 Simulink® 中实现四阶节滤波器的级联。您可以在模块参数对话框中或通过输入端口指定滤波器的分子和分母系数。
