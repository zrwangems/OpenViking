---
type: simulink-block
title: 'IFFT'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: 'ifft'
documentation_source_path: 'ref/ifft.html'
language: zh-CN
chinese_source: worker-translation
---

# IFFT

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 向量 | 矩阵 | *N* 维数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: 输入的 IFFT 向量 | 矩阵 | *N* 维数组
  direction: output
  data_types: single | double | int8 | int16 | int32 | fixed point
```

### 输入

### **Port\_1** — 输入信号 向量 | 矩阵 | *N* 维数组

用于计算 IFFT 的输入信号。该模块沿 *N* 维输入信号的第一个维度计算 IFFT。输入可以是浮点或定点、实数或复数，以及共轭对称。

有关该模块如何计算 IFFT 的详细信息，请参阅描述和算法。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** 是
### 输出

### **Port\_1** — 输入的 IFFT 向量 | 矩阵 | *N* 维数组

沿 *N* 维输入数组的第一个维度计算的 IFFT。有关该模块如何计算 IFFT 的详细信息，请参阅描述和算法。

第 *L* 个输出通道的第 *k* 个元素 *y*(*k*,*L*) 等于第 *L* 个输入通道的 *M* 点逆离散傅里叶变换（IDFT）的第 *k* 个点：

y(k,L)=1M∑p=1Pu(p,L)ej2π(p−1)(k−1)/M        k=1,…,M

输出具有与输入相同的维度。如果输入信号具有浮点数据类型，则输出信号的数据类型使用相同的浮点数据类型。否则，输出可以是任何有符号定点数据类型。该模块计算 IFFT 的缩放和非缩放版本。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
## 参数
```yaml
parameters:
- name: FFT implementation
  summary: FFT 实现 Auto（默认）| Radix-2 | FFTW
  group: 主要
- name: Input is in bit-reversed order
  summary: 输入为位反转顺序 off（默认）| on
  group: 主要
- name: Input is conjugate symmetric
  summary: 输入为共轭对称 off（默认）| on
  group: 主要
- name: Divide output by FFT length
  summary: 将输出除以 FFT 长度 on（默认）| off
  group: 主要
- name: Inherit FFT length from input dimensions
  summary: 从输入维度继承 FFT 长度 on（默认）| off
  group: 主要
- name: FFT length
  summary: FFT 长度 64（默认）| 整数
  group: 主要
- name: Wrap input data when FFT length is shorter than input length
  summary: 环绕或截断输入 on（默认）| off
  group: 主要
- name: Rounding mode
  summary: 舍入方法 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型
- name: Saturate on integer overflow
  summary: 整数溢出时饱和 off（默认）| on
  group: 数据类型
- name: Sine table
  summary: '正弦表值的数据类型 Inherit: Same word length as input（默认）| fixdt(1,16)'
  group: 数据类型
- name: Product output
  summary: '乘积输出数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as input | fixdt(1,16,0)'
  group: 数据类型
- name: Accumulator
  summary: '累加器数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as input | Inherit: Same as product output | fixdt(1,16,0)'
  group: 数据类型
- name: Output
  summary: '输出数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as input | fixdt(1,16,0)'
  group: 数据类型
- name: Output Minimum
  summary: 模块应输出的最小值 []（默认）| 标量
  group: 数据类型
- name: Output Maximum
  summary: 模块应输出的最大值 []（默认）| 标量
  group: 数据类型
- name: Lock data type settings against changes by the fixed-point tools
  summary: 防止定点工具覆盖数据类型 off（默认）| on
  group: 数据类型
```

### 主要

### **FFT implementation** — FFT 实现 `Auto`（默认）| `Radix-2` | `FFTW`

将此参数设置为 `FFTW` 以支持任意长度的输入信号。该模块将使用 FFTW 实现生成的代码限制为 MATLAB® 主机。

将此参数设置为 `Radix-2` 以进行位反转处理、定点或浮点数据，或使用 Simulink® Coder™ 生成可移植的 C 代码。*M*×*N* 输入矩阵的维度 *M* 必须是 2 的幂。要处理其他输入大小，请使用 Pad 模块将这些维度填充或截断为 2 的幂，或者如果可能，选择 FFTW 实现。有关 `Radix-2` 模式所用算法的详细信息，请参阅 Radix-2 实现。

将此参数设置为 `Auto` 以让模块选择 FFT 实现。对于具有非 2 的幂变换长度的浮点输入，会自动选择 FFTW 算法。否则会自动选择 Radix-2 算法。对于非 2 的幂变换长度，该模块将生成的代码限制为 MATLAB 主机。

### **Input is in bit-reversed order** — 输入为位反转顺序 `off`（默认）| `on`

选中或清除此复选框以指定输入通道元素的顺序。当输入为位反转顺序时选中此复选框，当输入为线性顺序时清除它。如果未正确设置此参数，该模块将产生无效输出。

如果已清除 **Inherit FFT length from input dimensions** 复选框，并且正在使用 **FFT length** 参数指定 FFT 长度，则无法选中此复选框。此外，当 **FFT implementation** 参数设置为 `FFTW` 时，也无法选中此复选框。

有关输出顺序的详细信息，请参阅线性和位反转输出顺序。

#### 依赖关系

要启用此参数，请将 **FFT implementation** 设置为 `Auto` 或 `Radix-2`。

### **Input is conjugate symmetric** — 输入为共轭对称 `off`（默认）| `on`

当模块输入共轭对称数据并且您希望输出为实数值时，选择此选项。选中此复选框可优化模块的计算方法。

当您输入实数值数据时，FFT 模块产生共轭对称输出。对共轭对称输入矩阵进行 IFFT 会产生实数值输出。因此，如果模块的输入既是浮点又是共轭对称的，并且您选中此复选框，则模块产生实数值输出。

如果已清除 **Inherit FFT length from input dimensions** 复选框，并且正在使用 **FFT length** 参数指定 FFT 长度，则无法选中此复选框。

如果向 IFFT 模块输入共轭对称数据但未选中此复选框，则 IFFT 模块输出具有小虚部的复数值信号。如果对非共轭对称输入数据选择此选项，则该模块输出无效数据。

### **Divide output by FFT length** — 将输出除以 FFT 长度 `on`（默认）| `off`

选中此复选框时，该模块根据描述部分中讨论的 IDFT 方程计算其输出。

清除此复选框时，该模块使用 IDFT 的修改版本计算输出：M⋅y(k,l)，由以下方程定义：

M⋅y(k,l)=∑p=1Pu(p,l)ej2π(p−1)(k−1)/Mk=1,...,M

修改后的 IDFT 方程不包含 1/*M* 的乘法因子。

### **Inherit FFT length from input dimensions** — 从输入维度继承 FFT 长度 `on`（默认）| `off`

选择以从输入维度继承 FFT 长度。如果不选择此参数，则 **FFT length** 参数变为可用以指定长度。当您选择 **Input is in bit-reversed order** 或 **Input is conjugate symmetric** 参数时，无法清除此参数。

### **FFT length** — FFT 长度 `64`（默认）| 整数

将 FFT 长度指定为大于或等于 2 的整数。

当您将 **FFT implementation** 参数设置为 `Radix-2`，或选中 **Output in bit-reversed order** 复选框时，此值必须是 2 的幂。

#### 依赖关系

要启用此参数，请清除 **Inherit FFT length from input dimensions** 复选框。

### **Wrap input data when FFT length is shorter than input length** — 环绕或截断输入 `on`（默认）| `off`

根据 FFT 长度选择环绕或截断输入。如果选择此参数，当 FFT 长度短于输入长度时，在 FFT 操作之前进行模长数据环绕。如果清除此参数，在 FFT 操作之前将输入数据截断为 FFT 长度。

#### 依赖关系

要启用此参数，请清除 **Inherit FFT length from input dimensions** 复选框。

### 数据类型

### **Rounding mode** — 舍入方法 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择定点运算的舍入模式。

#### 限制

正弦表值不遵循此参数；它们始终舍入为 `Nearest`。

当满足以下所有条件时，**Rounding mode** 参数对数值结果没有影响：

- **Product output** 数据类型为 `Inherit: Inherit via internal rule`。
- **Accumulator** 数据类型为 `Inherit: Inherit via internal rule`。

使用这些数据类型设置时，该模块以全精度模式运行。

### **Saturate on integer overflow** — 整数溢出时饱和 `off`（默认）| `on`

选中此参数时，该模块对其定点运算的结果进行饱和处理。清除此参数时，该模块对其定点运算的结果进行环绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

#### 限制

当满足以下所有条件时，**Saturate on integer overflow** 参数对数值结果没有影响：

- **Product output** 数据类型为 `Inherit: Inherit via internal rule`。
- **Accumulator** 数据类型为 `Inherit: Inherit via internal rule`。

使用这些数据类型设置时，该模块以全精度模式运行。

### **Sine table** — 正弦表值的数据类型 `Inherit: Same word length as input`（默认）| `fixdt(1,16)`

选择如何指定正弦表值的字长。正弦表值的小数长度始终等于字长减一。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Same word length as input`
- 求值为有效数据类型的表达式，例如 `fixdt(1,16)`

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置 **Sine table** 参数。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 限制

正弦表值不遵循 **Rounding mode** 和 **Saturate on integer overflow** 参数；它们始终饱和并舍入为 `Nearest`。

### **Product output** — 乘积输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `fixdt(1,16,0)`

指定乘积输出数据类型。有关描述此模块中乘积输出数据类型使用的图示，请参阅定点数据类型和乘法数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`。有关此规则的详细信息，请参阅 Inherit via Internal Rule。
- 求值为有效数据类型的表达式，例如 `fixdt(1,16,0)`

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置 **Product output** 参数。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Accumulator** — 累加器数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

指定累加器数据类型。有关描述此模块中累加器数据类型使用的图示，请参阅定点数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`。有关此规则的详细信息，请参阅 Inherit via Internal Rule。
- 求值为有效数据类型的表达式，例如 `fixdt(1,16,0)`

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置 **Accumulator** 参数。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Output** — 输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `fixdt(1,16,0)`

指定输出数据类型。有关描述此模块中输出数据类型使用的图示，请参阅定点数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`。

  当您选择 `Inherit: Inherit via internal rule` 时，该模块自动计算输出字长和小数长度。该模块用于计算理想输出字长和小数长度的方程取决于 **Divide output by FFT length** 复选框的设置。

  - 当您选中 **Divide output by FFT length** 复选框时，理想输出字长和小数长度与输入字长和小数长度相同。
  - 当您清除 **Divide output by FFT length** 复选框时，该模块根据以下方程计算理想输出字长和小数长度：

    WLideal output=WLinput+floor(log2(FFT length−1))+1

    FLideal output=FLinput

  使用这些理想结果，内部规则随后选择适合您硬件的字长和小数长度。有关详细信息，请参阅 Inherit via Internal Rule。
- 求值为有效数据类型的表达式，例如 `fixdt(1,16,0)`

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置 **Output** 参数。

有关详细信息，请参阅 Control Data Types of Signals (Simulink)。

### **Output Minimum** — 模块应输出的最小值 `[]`（默认）| 标量

指定模块应输出的最小值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink)）
- 定点数据类型的自动缩放

### **Output Maximum** — 模块应输出的最大值 `[]`（默认）| 标量

指定模块应输出的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink)）
- 定点数据类型的自动缩放

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数以防止定点工具覆盖您在模块对话框中指定的数据类型。
## 所属库

DSP System Toolbox / Transforms

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `yesa` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 仅当选中 Inherit FFT length from input dimensions 复选框时，才支持可变大小信号。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 当以下条件适用时，从此模块生成的可执行文件依赖于 MATLAB 附带的预构建动态库文件（`.dll` 文件）：

  - **FFT implementation** 设置为 `FFTW`。
  - **Inherit FFT length from input dimensions** 已清除，并且 **FFT length** 设置为非 2 的幂的值。

  使用 `packNGo` 函数将此模块生成的代码及所有相关文件打包到一个压缩 zip 文件中。使用此 zip 文件，您可以在未安装 MATLAB 的另一个开发环境中重新定位、解包并重建您的项目。有关更多详细信息，请参阅 How To Run a Generated Executable Outside MATLAB。
- 当 FFT 长度为 2 的幂时，您可以从此模块生成独立的 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

输入的逆快速傅里叶变换（IFFT）

IFFT 模块沿 *N* 维输入数组的第一个维度计算逆快速傅里叶变换（IFFT）。该模块使用两种可能的 FFT 实现之一。您可以选择基于 FFTW 库的实现或基于一组 Radix-2 算法的实现。要允许模块选择实现，您可以选择 `Auto`。有关 FFT 实现的详细信息，请参阅算法。

当您指定的 FFT 长度不等于输入向量的长度（或输入数组的第一个维度）时，该模块实现零填充、截断或模 *M*（FFT 长度）数据环绕。这发生在 IFFT 操作之前。对于 *P* ≤ *M* 的 IFFT：

```
y = ifft(u,M) % P ≤ M
```

环绕：

```
y(:,L) = ifft(datawrap(u(:,L),M)) % P > M; L = 1,...,N
```

截断：

```
y (:,L) = ifft(u,M) % P > M; L = 1,...,N
```

**提示**

当输入长度 *P* 大于 FFT 长度 *M* 时，您可能会看到 IFFT 输出中的幅度增加。这些幅度增加的发生是因为 IFFT 模块使用模 *M* 数据环绕来保留所有可用的输入样本。

为避免此类幅度增加，您可以将输入样本的长度 *P* 截断为 FFT 长度 *M*。为此，请在模型中的 IFFT 模块之前放置一个 Pad 模块。
