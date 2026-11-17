---
type: simulink-block
title: 'Allpass Filter'
family: 'filtering'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Implementations'
documentation_page: 'allpassfilter'
documentation_source_path: 'ref/allpassfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Allpass Filter

## 端口

### 输入

### **x** — 输入数据 列向量 | 行向量 | 矩阵

传递到全通滤波器的输入数据。该模块接受实值或复值多通道输入，即 *m*×*n* 大小的输入，其中 *m* ≥ 1 且 *n* ≥ 1。该模块还接受可变大小输入，即您可以在仿真期间更改每个输入通道的大小。但是，通道数不能更改。

在您将 **Internal allpass structure** 设置为 `Minimum multiplier` 或 `Lattice`，并选中 **Specify coefficients from input port** 参数之前，此端口未命名。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **coeffs** — 全通滤波器系数 列向量 | 行向量 | 矩阵

此端口输入全通滤波器的系数。当您将 **Internal allpass structure** 设置为 `Minimum multiplier` 时，**coeffs** 端口接受大小为 *N*×1 或 *N*×2 的矩阵。当您将 **Internal allpass structure** 设置为 `Lattice` 时，**coeffs** 端口接受 *N*×1 列向量或 1×*N* 行向量。

#### 依赖项

当您将 **Internal allpass structure** 设置为 `Minimum multiplier` 或 `Lattice`，并选中 **Specify coefficients from input port** 参数时，此端口会出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### 输出

### **Port\_1** — 全通滤波器的输出 列向量 | 行向量 | 矩阵

滤波后输出的大小与输入的大小匹配。

**数据类型：** `single` | `double`
**复数支持：** Yes

## 参数

如果某个参数列为可调，则可以在仿真期间更改其值。

### **Internal allpass structure** — 滤波器结构 `Minimum multiplier`（默认）| `Wave Digital Filter` | `Lattice`

- `Minimum multiplier` — 此结构使用所需的最少乘法器数量 *n*，以及 2*n* 个延迟单元和 2*n* 个加法器。此结构的系数通过 **Allpass polynomial coefficients** 参数指定。
- `Wave Digital Filter` — 此结构使用 *n* 个乘法器和 *n* 个延迟单元，代价是 3*n* 个加法器。此结构的系数通过 **Wave Digital Filter allpass coefficients** 参数指定。
- `Lattice` — 此结构使用 2*n* 个乘法器、*n* 个延迟单元和 2*n* 个加法器。此结构的系数通过 **Lattice allpass coefficients** 参数指定。

有关这些结构的更多详细信息，请参阅算法。

### **Specify coefficients from input port** — 用于指定全通多项式系数的标志 off（默认）| on

当您选中此复选框，并将 **Internal allpass structure** 设置为 `Minimum multiplier` 时，全通多项式系数通过 **coeffs** 端口输入。当您清除此复选框时，全通多项式系数通过 **Allpass polynomial coefficients** 参数在模块对话框中指定。

当您选中此复选框，并将 **Internal allpass structure** 设置为 `Lattice` 时，格型全通系数通过 **coeffs** 端口输入。当您清除此复选框时，格型全通系数通过 **Lattice allpass coefficients** 参数在模块对话框中指定。

#### 依赖项

要启用此参数，请将 **Internal allpass structure** 设置为 `Minimum multiplier` 或 `Lattice`。

### **Allpass polynomial coefficients** — 最小乘法器形式的系数 [`-2^(-1/2), 1/2`]（默认）| *N*×1 矩阵 | *N*×2 矩阵 | *N*×4 矩阵

以最小乘法器形式将实数全通多项式滤波器系数指定为 *N*×1 矩阵、*N*×2 矩阵或 *N*×4 矩阵。

- *N*×1 矩阵 — 该模块实现 *N* 个一阶全通节。
- *N*×2 矩阵 — 该模块实现 *N* 个二阶全通节。
- *N*×4 矩阵 — 该模块实现 *N* 个四阶全通节。*（自 R2024a 起）*

默认值 [`-2^(-1/2), 1/2`] 定义一个稳定的二阶全通滤波器，其极点和零点位于 *z* 平面中的 ±π/3 处。

**可调：** Yes

#### 依赖项

要启用此参数，请将 **Internal allpass structure** 设置为 `Minimum multiplier`，并清除 **Specify coefficients from input port** 参数。

### **Wave Digital Filter allpass coefficients** — 波数字滤波器形式的系数 [`1/2, -2^(1/2)/3`]（默认）| *N*×1 矩阵 | *N*×2 矩阵

以波数字滤波器形式指定实数全通滤波器系数。系数可以是 *N*×1 矩阵，用于 *N* 个一阶全通节；也可以是 *N*×2 矩阵，用于 *N* 个二阶全通节。默认值 [`1/2, -2^(1/2)/3`] 是全通多项式系数默认值的变换版本。此值使用 `allpass2wdf(Allpass polynomial coefficients)` 计算。这些系数定义与全通结构设置为 `Minimum multiplier` 时相同的稳定二阶全通滤波器。

**可调：** Yes

#### 依赖项

要启用此参数，请将 **Internal allpass structure** 设置为 `Wave Digital Filter`。

### **Indicate if last section is first order** — 最后一个节是否为一阶 `off`（默认）| `on`

- `on` — 当选中此复选框时，最后一个节被视为一阶。此外，*N*×2 矩阵最后一行的第二个元素将被忽略。对于最小乘法器结构，如果指定 *N*×4 矩阵，此参数对滤波器系数没有影响。
- `off` — 当不选中此复选框时，最后一个节被视为二阶。

#### 依赖项

要启用此参数，请将 **Internal allpass structure** 设置为 `Minimum multiplier` 或 `Wave Digital Filter`。

### **Lattice allpass coefficients** — 格型形式的系数 `[-2^(1/2)/3, 1/2]`（默认）| *N*×1 列向量 | 1×*N* 行向量

将实数或复数全通系数指定为格型反射系数。默认值 `[-2^(1/2)/3, 1/2]` 是全通多项式系数默认值的变换并转置版本。此值使用 `transpose(tf2latc(1, [1 A]))` 计算，其中 *A* 是在 **Allpass polynomial coefficients** 中指定的值。

**可调：** Yes

#### 依赖项

要启用此参数，请将 **Internal allpass structure** 设置为 `Lattice`，并清除 **Specify coefficients from input port** 参数。

### **View Filter Response** — 可视化滤波器响应按钮

打开滤波器可视化工具 `fvtool`，并显示全通滤波器的幅值响应。响应基于这些参数。对这些参数所做的更改会更新 `fvtool`。

要在 `fvtool` 运行期间更新幅值响应，请修改模块参数，然后点击 **Apply**。

要同时查看幅值响应和相位响应，请点击工具栏上的 **Magnitude and Phase responses** 按钮。

在此示例中，幅值响应是平坦的，而相位响应随频率变化。这种变化的相位响应可用于相位均衡、陷波滤波和多速率滤波。您可以使用两个彼此具有 180 degrees 相移的全通滤波器的并联组合来实现低通滤波器。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码就会在后续仿真中复用。此选项需要额外的启动时间，但可提供更快的后续仿真。

## 所属库

DSP System Toolbox / Filtering / Filter Implementations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `No` |
| **可变大小信号** | `Yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

### R2024a：**Simulate using** 参数默认值的更改

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此更改，该模块默认使用 MATLAB 解释器进行仿真。

### R2024a：最小乘法器结构支持四阶全通节

当您将 **Internal allpass structure** 参数设置为 `Minimum multiplier` 时，可以在 **Allpass polynomial coefficients** 参数中指定滤波器系数的 *N*×4 矩阵，其中 *N* 是滤波器节数。

## 描述

单节或多节全通滤波器

Allpass Filter 模块使用单节或多节（级联）全通滤波器对输入信号的每个通道独立进行滤波。您可以使用最小乘法器、波数字滤波器或格型结构来实现全通滤波器。

在最小乘法器形式中，该模块使用所需的最少乘法器数量 *n*，以及 2*n* 个延迟单元和 2*n* 个加法器。在波数字滤波器形式中，该模块仅使用 *n* 个乘法器和 *n* 个延迟单元，代价是 3*n* 个加法器。格型结构使用 2*n* 个乘法器、*n* 个延迟单元和 2*n* 个加法器。有关这些结构的更多详细信息，请参阅算法。
