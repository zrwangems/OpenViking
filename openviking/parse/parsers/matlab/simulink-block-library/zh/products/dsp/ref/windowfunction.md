---
type: simulink-block
title: 'Window Function'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Signal Operations / Signal Operations'
documentation_page: 'windowfunction'
documentation_source_path: 'ref/windowfunction.html'
language: zh-CN
chinese_source: worker-translation
---

# Window Function

## 端口

### 输入

### **In** — 输入信号向量 | 矩阵 | *N* 维数组

输入信号，指定为向量、矩阵或 *N* 维数组。

如果输入是定点，则它必须是有符号整数或具有 2 的幂斜率且零偏置的有符号定点值。

仅当将 **Operation** 设置为 `Apply window to input` 或 `Generate and apply window` 时，此端口才启用。

当将 **Operation** 设置为 `Apply window to input` 时，此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### 输出

### **Out** — 输出向量 | 矩阵 | *N* 维数组

输出信号，以向量、矩阵或 *N* 维数组形式返回。

仅当 **Operation** 设置为以下值时，**Out** 端口才启用：

- `Apply window to input` –– 模块计算 *M*×1 窗向量 *w*，并将其应用于 *M*×*N* 输入，其中 *M* 是输入信号中的行数。
- `Generate and apply window` –– 模块生成 *M*×1 窗向量 *w*，并将其应用于输入。

输出信号与输入信号具有相同的维度。有关更多详细信息，请参阅 Operation。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **Win** — 窗输出向量

窗输出，以向量形式返回。当 **Operation** 设置为 `Apply window to input` 或 `Generate and apply window` 时，窗向量长度与输入信号中的行数相同。当 **Operation** 设置为 `Generate window` 时，窗向量长度由 **Window length** 参数确定。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

## 参数

### Main

### **Operation** — 运算模式 `Apply window to input`（默认） | `Generate window` | `Generate and apply window`

Window Function 模块有三种运算模式，可通过 **Operation** 参数选择。在每种模式下，模块首先通过在 *M* 个离散点处对 **Window type** 参数指定的窗进行采样，创建窗向量 *w*。运算模式包括：

- `Apply window to input`

  在此模式下，模块计算 *M*×1 窗向量 *w*，并将其应用于输入。输出 *y* 始终与输入具有相同维度。

  当输入是 *M*×*N* 矩阵 *u* 时，窗与输入矩阵 *u* 中的 *N* 个通道逐个元素相乘。这等效于以下 MATLAB® 代码：

  ```
  y = repmat(w,1,N) .* u								% Equivalent MATLAB code
  ```

  窗始终应用于第一个维度：

  y(i,j,...,k)=w(i)\*u(i,j,...,k)       i=1,...,M,  j=1,...,N,  ...,  k=1,...,P

  长度为 *M* 的未定向向量输入被视为 *M*×1 向量。
- `Generate window`

  在此模式下，模块生成未定向窗向量 *w*，其长度 *M* 由 **Window length** 参数指定。此模式下 **In** 端口被禁用。
- `Generate and apply window`

  在此模式下，模块生成 *M*×1 窗向量 *w*，并将其应用于输入。模块产生两个输出：

  - 在 **Out** 端口，模块产生乘法结果 *y*，其维度与输入相同。
  - 在 **Win** 端口，模块产生 *M*×1 窗向量 *w*。

  当输入是 *M*×*N* 矩阵 *u* 时，窗与输入矩阵 *u* 中的 *N* 个通道逐个元素相乘。这等效于以下 MATLAB 代码：

  ```
  y = repmat(w,1,N) .* u								% Equivalent MATLAB code
  ```

  窗始终应用于第一个维度：

  y(i,j,...,k)=w(i)\*u(i,j,...,k)       i=1,...,M,  j=1,...,N,  ...,  k=1,...,P

  长度为 *M* 的 1-D 向量输入被视为 *M*×1 向量。

### **Window type** — 窗类型 `Hamming`（默认） | `Bartlett` | `Blackman` | ...

此表列出了可用的窗类型。

| 窗类型 | 描述 |
| --- | --- |
| Bartlett | 计算 Bartlett 窗。  ``` w = bartlett(M) ``` |
| Blackman | 计算 Blackman 窗。  ``` w = blackman(M) ``` |
| Boxcar | 计算矩形窗。  ``` w = rectwin(M) ``` |
| Chebyshev | 计算具有阻带波纹 `R` 的 Chebyshev 窗。  ``` w = chebwin(M,R) ``` |
| Hamming | 计算 Hamming 窗。  ``` w = hamming(M) ``` |
| Hann | 计算 Hann 窗（也称为 Hanning 窗）。  ``` w = hann(M) ``` |
| Hanning | 已过时。包含此窗类型仅为了与旧模型兼容。尽可能使用 `Hann` **Window type** 而不是 `Hanning`。 |
| Kaiser | 计算具有 Kaiser 参数 `beta` 的 Kaiser 窗。  ``` w = kaiser(M,beta) ``` |
| Taylor | 计算 Taylor 窗。  ``` w = taylorwin(M) ``` |
| Triang | 计算三角窗。  ``` w = triang(M) ``` |
| User Defined | 计算由 **Window function name** 参数中的条目 `usrwin` 指定的用户定义窗函数。  ``` w = usrwin(M) % Window takes no extra parameters w = usrwin(M,x1,...,xn) % Window takes extra  parameters {x1 ... xn} ``` |

### **Sampling** — 采样类型 `Symmetric`（默认） | `Periodic`

指定广义余弦窗的窗采样。

对于广义余弦窗（`Blackman`、`Hamming`、`Hann` 和 `Hanning`），**Sampling** 参数确定窗采样是以周期方式还是对称方式计算。例如，当 **Sampling** 设置为 `Symmetric` 时，长度为 *M* 的 Hamming 窗计算如下：

```
w = hamming(M)					% Symmetric (aperiodic) window
```

当 **Sampling** 设置为 `Periodic` 时，同一窗计算如下：

```
w = hamming(M+1)					% Periodic (asymmetric) window
w = w(1:M)
```

仅可在仿真中调整（Simulink）。

#### 依赖关系

仅当为 **Window type** 参数选择 `Blackman`、`Hamming`、`Hann` 或 `Hanning` 时，此参数才可见。

### **Sample mode** — 采样模式 `Continuous`（默认） | `Discrete`

当模块处于 `Generate window` 模式时，指定模块的采样模式，`Continuous` 或 `Discrete`。在 `Apply window to input` 和 `Generate and apply window` 模式下，模块从其驱动模块继承采样模式。

#### 依赖关系

仅当为 **Operation** 参数选择 `Generate window` 时，此参数才可见。

### **Sample time** — 采样时间 `1`（默认） | 实数标量

当 **Operation** 设置为 `Generate window` 且 **Sample mode** 设置为 `Discrete` 时，指定模块的采样时间。当 **Operation** 设置为 `Apply window to input` 和 `Generate and apply window` 时，模块从其驱动模块继承采样时间。

#### 依赖关系

仅当将 **Sample mode** 设置为 `Discrete` 时，此参数才可见。

### **Window length** — 窗长度 `64`（默认） | 正整数

指定要应用的窗长度。

#### 依赖关系

仅当为 **Operation** 参数选择 `Generate window` 时，此参数才可见。否则，窗向量长度将计算为与输入第一个维度的长度匹配。

### **Stopband attenuation in dB** — 阻带衰减，dB `50`（默认） | 非负标量

指定阻带衰减 *R**s* 的电平，以 dB 为单位。

仅可在仿真中调整（Simulink）。

#### 依赖关系

仅当为 **Window type** 参数选择 `Chebyshev` 时，此参数才可见。

### **Beta** — Kaiser 窗 *β* 参数 `10`（默认） | 实数标量

指定 `Kaiser` 窗 *β* 参数。增大 *β* 会加宽主瓣，并降低窗的频率幅度响应中窗旁瓣的幅度。

仅可在仿真中调整（Simulink）。

#### 依赖关系

仅当为 **Window type** 参数选择 `Kaiser` 时，此参数才可见。

### **Number of sidelobes** — 旁瓣数量 4（默认） | 正整数

指定旁瓣数量，为大于零的标量整数值。

#### 依赖关系

仅当为 **Window type** 参数选择 `Taylor` 时，此参数才可见。

### **Maximum sidelobe level relative to mainlobe (dB)** — 相对于主瓣的最大旁瓣电平 `-30`（默认） | 小于或等于零的标量

指定相对于主瓣的最大旁瓣电平，以 dB 为单位。此参数必须是小于或等于零的标量。默认值 –30 产生的旁瓣峰值比主瓣峰值低 30 dB。

#### 依赖关系

仅当为 **Window type** 参数选择 `Taylor` 时，此参数才可见。

### **Window function name** — 窗函数名称 `hamming`（默认） | 字符向量

指定要由模块计算的用户定义窗函数名称。自定义窗函数返回的输出窗向量必须为数据类型 `double`。

#### 依赖关系

仅当为 **Window type** 参数选择 `User defined` 时，此参数才可见。

### **Specify additional arguments to the hamming function** — 指定窗函数的附加参数 off（默认） | on

当用户定义窗需要除窗长度以外的参数时，选择此项以启用 **Cell array of additional arguments** 参数。

#### 依赖关系

仅当为 **Window type** 参数选择 `User defined` 时，此参数才可见。

### **Cell array of additional arguments** — 附加参数 `{'symmetric'}`（默认） | 元胞数组

指定用户定义窗函数除窗长度外所需的额外参数。

#### 依赖关系

仅当选择 **Specify additional arguments to the hamming function** 参数时，此参数才可用。条目必须是元胞数组。

### 数据类型

当 **Main** 选项卡上的 **Operation** 参数设置为 `Generate window` 时，将显示以下参数。

### **Window data type** — 窗数据类型 `double`（默认） | `single` | `Fixed-point` | `User-defined` | `Inherit via back propagation`

通过以下方式之一指定窗数据类型：

- `double`
- `single`
- `Fixed-point` –– 在 **Signed**、**Word length**、**Set fraction length in output to** 和 **Fraction length** 参数中指定窗数据类型和定标。
- `User-defined` –– 在 **User-defined data type**、**Set fraction length in output to** 和 **Fraction length** 参数中指定窗数据类型和定标。
- `Inherit via back propagation` –– 将窗数据类型和定标设置为与下一个模块匹配。

### **Signed** — 窗输出为有符号 on（默认） | off

选择此项以输出有符号定点信号。否则，信号为无符号。

#### 依赖关系

仅当将 **Window data type** 设置为 `Fixed-point` 时，此参数才出现。

### **Word length** — 字长 `16`（默认） | [2 128] 范围内的正整数

指定定点窗数据类型的字长，以 bits 为单位。

#### 依赖关系

仅当将 **Window data type** 设置为 `Fixed-point` 时，此参数才可见。

### **User-defined data type (e.g. sfix(16), float('single))** — 用户定义数据类型 `sfix(16)`（默认） | 内置数据类型 | 定点数据类型

指定任何内置或定点数据类型。可以使用 `fixdt` (Simulink) 函数指定定点数据类型。

#### 依赖关系

仅当将 **Window data type** 设置为 `User-defined` 时，此参数才可见。

### **Set fraction length in output to** — 定点窗数据类型的定标 `Best precision`（默认） | `User-defined`

使用以下任一方法指定定点窗数据类型的定标：

- 选择 `Best precision`，使窗数据类型定标自动设置，以便输出信号具有最佳可能精度。
- 选择 `User-defined`，以在 **Fraction length** 参数中指定窗数据类型定标。

#### 依赖关系

仅当将 **Window data type** 设置为 `Fixed-point` 或 `User-defined`，并且指定的窗数据类型是定点数据类型时，此参数才可见。

### **Fraction length** — 用户定义小数长度 `15`（默认） | 整数

指定定点窗数据类型的小数长度，以 bits 为单位。

#### 依赖关系

仅当将 **Window data type** 设置为 `Fixed-point` 或 `User-defined`，并且将 **Set fraction length in output to** 设置为 `User-defined` 时，此参数才可见。

当 **Main** 选项卡上的 **Operation** 参数设置为 `Apply window to input` 或 `Generate and apply window` 时，将显示以下参数。

### **Rounding mode** — 舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择定点运算的舍入模式。

窗向量 *w* 不遵循此参数。它始终舍入到 `Nearest`。

**注意**

当以下两个条件同时存在时，**Rounding mode** 和 **Overflow mode** 设置对数值结果没有影响：

- **Product output** 为 `Inherit via internal rule`
- **Output** 为 `Same as product output`

使用这些数据类型设置时，模块实际上以全精度模式运行。

### **Overflow mode** — 溢出模式 `Wrap`（默认） | `Saturate`

选择定点运算的溢出模式。

窗向量 *w* 不遵循此参数。它始终饱和。

### **Window** — 窗数据类型 `Same word length as input`（默认） | `Specify word length` | `Binary point scaling` | `Slope and bias scaling`

选择如何指定窗向量 *w* 的字长和小数长度。

选择时：

- `Same word length as input` –– 窗向量元素的字长与输入的字长相同。小数长度自动设置为最佳可能精度。
- `Specify word length` –– 可以输入窗向量元素的字长，以 bits 为单位。小数长度自动设置为最佳可能精度。
- `Binary point scaling` –– 可以输入窗向量元素的字长和小数长度，以 bits 为单位。
- `Slope and bias scaling` –– 可以输入窗向量元素的字长（以 bits 为单位）和斜率。此模块要求 2 的幂斜率和零偏置。

窗向量不遵循 **Rounding mode** 和 **Overflow mode** 参数。它始终饱和并舍入到 `Nearest`。

### **Product output** — 乘积输出数据类型 `Inherit via internal rule`（默认） | `Same as input` | `Binary point scaling` | `Slope and bias scaling`

使用此参数指定希望如何指定乘积输出的字长和小数长度。

选择时：

- `Inherit via internal rule` –– 乘积输出字长和小数长度会自动计算。有关使用内部规则时如何计算乘积输出字长和小数长度的信息，请参阅 Inherit via Internal Rule。
- `Same as input` –– 这些特性与模块输入的相应特性匹配。
- `Binary point scaling` –– 可以输入乘积输出的字长和小数长度，以 bits 为单位。
- `Slope and bias scaling` –– 可以输入乘积输出的字长（以 bits 为单位）和斜率。此模块要求 2 的幂斜率和零偏置。

### **Output** — 输出数据类型 `Same as product output`（默认） | `Same as input` | `Binary point scaling` | `Slope and bias scaling`

选择如何指定模块输出的字长和小数长度。

选择时：

- `Same as product output` –– 这些特性与乘积输出的相应特性匹配。
- `Same as input` –– 这些特性与模块输入的相应特性匹配。
- `Binary point scaling` –– 可以输入输出的字长和小数长度，以 bits 为单位。
- `Slope and bias scaling` –– 可以输入输出的字长（以 bits 为单位）和斜率。此模块要求 2 的幂斜率和零偏置。

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认） | `on`

选择此参数以防止定点工具覆盖您在模块对话框中指定的数据类型。

## 所属库

DSP System Toolbox / Signal Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

在某些条件下，生成的代码依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算窗并将其应用于输入信号

Window Function 模块具有三种运算模式，可用于对输入信号应用窗、计算窗，或计算并应用窗。您可以通过 **Operation** 参数选择模式。在每种模式下，模块首先通过对 **Window type** 参数指定的窗进行采样来创建窗向量 *w*。
