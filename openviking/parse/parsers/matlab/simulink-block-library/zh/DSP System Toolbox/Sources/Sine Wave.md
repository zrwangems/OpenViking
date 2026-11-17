---
type: simulink-block
title: 'Sine Wave'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'sinewave'
documentation_source_path: 'ref/sinewave.html'
language: zh-CN
chinese_source: worker-translation
---

# Sine Wave

## 端口

### 输出

### **Port\_1** — 正弦信号 标量 | 向量 | 矩阵

输出正弦信号，可以是标量或向量。有关输出复数的详细信息，请参阅描述。有关多通道支持的信息，请参阅生成多通道输出。

**提示**

要输出定点数据类型，必须将**采样模式**设置为 `Discrete`，并将**计算方法**设置为 `Table lookup`。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** 是

## 参数

### 主要

### **Amplitude** — 正弦波的幅度 `1`（默认）| 标量 | 向量

长度为 *N* 的向量，包含 *N* 个输出通道中每个通道正弦波的幅度，或者一个标量，应用于所有 *N* 个通道。向量长度必须与**Frequency**和**Phase offset**参数指定的长度相同。

**提示**

仅当**计算方法**为 `Trigonometric fcn` 或 `Differential` 时，此参数才可调（Simulink）。

**可调：** 是

### **Frequency (Hz)** — 每个正弦波的频率 `100`（默认）| 标量 | 向量

长度为 *N* 的向量，包含 *N* 个输出通道中每个通道正弦波的频率（以赫兹为单位），或者一个标量，应用于所有 *N* 个通道。向量长度必须与**Amplitude**和**Phase offset**参数指定的长度相同。您可以指定正频率、零频率或负频率。

**提示**

当您进行以下设置时，此参数可调（Simulink）：

- 求解器**Type**设置为 `Fixed-step`。
- **Sample mode**设置为 `Continuous`。
- **Sample mode**设置为 `Discrete`且**Computation method**设置为 `Trigonometric fcn`。

**可调：** 是

### **Phase offset (rad)** — 相位偏移 `0`（默认）| 标量 | 向量

长度为 *N* 的向量，包含 *N* 个输出通道中每个通道正弦波的相位偏移（以弧度为单位），或者一个标量，应用于所有 *N* 个通道。向量长度必须与**Amplitude**和**Frequency**参数指定的长度相同。

**提示**

当您进行以下设置时，此参数可调（Simulink）：

- 求解器**Type**设置为 `Fixed-step`。
- **Sample mode**设置为 `Continuous`。
- **Sample mode**设置为 `Discrete`且**Computation method**设置为 `Trigonometric fcn`。

**可调：** 是

### **Sample mode** — 连续或离散采样模式 `Discrete`（默认）| `Continuous`

将采样模式指定为 `Continuous` 或 `Discrete`：

- `Continuous`

  在连续模式下，第 *i* 个通道中的正弦波 *yi* 作为连续函数计算，

  yi=Aisin(2πfit+ϕi)(real)oryi=Aiej(2πfit+ϕi)(complex)

  并且模块的输出是连续的。在此模式下，模块的操作与 Simulink® Sine Wave 模块将**Sample time**设置为 `0` 时相同。此模式提供高精度，但需要在每个仿真步长进行三角函数计算，计算成本较高。此外，由于此方法跟踪绝对仿真时间，当时间值达到其最大限制时，最终会出现不连续。

  另请注意，许多 DSP System Toolbox™ 模块不接受连续时间输入。
- `Discrete`

  在离散模式下，模块可以通过直接计算三角函数、查表或差分方法生成离散时间输出。有关这些计算方法的更多信息，请参阅算法。

### **Output complexity** — 实数或复数波形 `Real`（默认）| `Complex`

要生成的波形类型：`Real` 指定实数正弦波，`Complex` 指定复指数。

### **Computation method** — 计算离散时间正弦波的方法 `Trigonometric fcn`（默认）| `Table lookup` | `Differential`

生成离散时间正弦波的方法：`Trigonometric fcn`、`Table lookup` 或 `Differential`。有关每个可用选项的更多信息，请参阅算法。

#### 依赖关系

仅当将**Sample mode**设置为 `Discrete` 时，此参数才可见。

**注意**

要生成定点正弦波，必须将**Computation method**设置为 `Table lookup`。

### **Optimize table for** — 优化速度或内存 `Speed`（默认）| `Memory`

针对 `Speed` 或 `Memory` 优化正弦值表。当针对速度优化时，表包含 *k* 个元素；当针对内存优化时，表包含 *k*/4 个元素，其中 *k* 是正弦波一个完整周期内的输入样本数。

#### 依赖关系

仅当将**Computation method**参数设置为 `Table lookup` 时，此参数才可见。

### **Sample time** — 采样周期 `1/1000`（默认）| 标量

正弦波的采样周期 *Ts*，为大于零的有限标量。模块的输出帧周期为 *M**Ts*，其中 *M* 在**Samples per frame**参数中指定。

#### 依赖关系

要启用此参数，请将**Sample mode**设置为 `Discrete`。

### **Samples per frame** — 每帧样本数 `1`（默认）| 正整数

从每个正弦波缓冲到输出帧中的连续样本数 *M*，指定为正标量整数。此参数不可调。

模块输出是一个 *M*×*N* 矩阵，帧周期为 *M**T*s，其中 *T*s 在**Sample time**参数中指定。

#### 依赖关系

要启用此参数，请将**Sample mode**设置为 `Discrete`。

### **Resetting states when re-enabled** — 使能子系统内部的状态行为 `Restart at time zero`（默认）| `Catch up to simulation time`

此参数确定使能子系统重新使能时 Sine Wave 模块的行为。模块可以重置为起始状态（`Restart at time zero`），或者根据当前仿真时间继续生成正弦波（`Catch up to simulation time`）。

#### 依赖关系

此参数仅在 Sine Wave 模块位于使能子系统内部且 Enable (Simulink) 模块的**States when enabling**参数设置为 `reset` 时适用。

### 数据类型

### **Output data type** — 输出数据类型 `double`（默认）| `single` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>` | `Inherit:Inherit via back propagation`

选择您希望如何指定**Output data type**的数据类型属性。您可以选择：

- `Inherit` — 允许您指定继承数据类型的规则，例如 `Inherit: Inherit via back propagation`
- `Built in`— 允许您指定内置数据类型，例如 `double`
- `Fixed point` — 允许您指定数据类型的定点属性。
- `Expression` — 允许您指定求值为有效数据类型的表达式，例如 `fixdt(1,16)`

### 数据类型助手

### **Mode** — 数据类型模式 `Built in`（默认）| `Inherit` | `Fixed point` | `Expression`

选择您希望如何指定**Output data type**的数据类型属性。您可以选择：

- `Inherit` — 允许您指定继承数据类型的规则，例如 `Inherit: Inherit via back propagation`
- `Built in`— 允许您指定内置数据类型，例如 `double`
- `Fixed point` — 允许您指定数据类型的定点属性。
- `Expression` — 允许您指定求值为有效数据类型的表达式，例如 `fixdt(1,16)`

有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Signedness** — 定点数据的有符号性 `Signed`（默认）

指定定点输出的有符号性。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 限制

Sine Wave 仅支持 `Signed` 数据类型。

### **Scaling** — 定点数据的定标方法 `Best precision`（默认）| `Binary point`

指定定点数据的定标方法，以避免溢出条件并最小化量化误差。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 依赖关系

要启用此参数，请将**Mode**设置为 `Fixed point`

### **Word length** — 保存量化整数的字长位数 `16`（默认）| 2 到 128 的整数

将保存量化整数的字长位数指定为 2 到 128 的正整数。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 依赖关系

要启用此参数，请将**Mode**设置为 `Fixed point`

### **Fraction length** — 定点数据类型的小数长度 `0`（默认）| 整数标量

将定点数据类型的小数长度指定为正或负整数标量。

#### 依赖关系

要启用此参数，请将**Mode**设置为 `Fixed point`，并将**Scaling**设置为 `Binary point`。

### **Data type override** — 数据类型覆盖模式 `Inherit`（默认）| `Off`

选择此信号的数据类型覆盖模式。您可以选择：

- `Inherit` — 继承为模型指定的数据类型覆盖设置。
- `Off` — 忽略为模型指定的数据类型覆盖设置，并使用您指定的定点数据类型。

#### 依赖关系

要启用此参数，请将**Mode**设置为 `Built in` 或 `Fixed point`。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

## 所属库

DSP System Toolbox / Sources DSP System Toolbox HDL Support / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

当配置为连续采样模式时，Sine Wave 模块引用绝对仿真时间。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

**注意**

有关针对 HDL 代码生成优化且具有硬件友好控制信号的正弦波发生器，请参阅 NCO (DSP HDL Toolbox) 和 Generate Sine Wave (DSP HDL Toolbox)。DSP HDL Toolbox™ 模块提供 HDL 优化算法，具有硬件友好的控制信号，并在 Simulink 中模拟 HDL 算法的延迟。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**限制**

对于 HDL 代码生成，您必须选择以下 Sine Wave 模块设置：

- **Computation method**：`Table lookup`
- **Sample mode**：`Discrete`

输出：

- 输出端口不能具有 `single` 或 `double` 数据类型。
- 此模块在 HDL 代码生成期间不支持基于帧的向量输出。支持来自幅度和频率数组的向量输出。

**复数数据支持**

此模块支持复数信号的代码生成。

## 版本历史

**在 R2006a 之前推出**

## 描述

生成连续或离散正弦波

Sine Wave 模块生成多通道实数或复数正弦信号，每个输出通道具有独立的幅度、频率和相位。该模块支持浮点和有符号定点数据类型。

当您将**Output complexity**参数设置为 `Real` 时，模块生成实数正弦信号。实数正弦输出由以下类型的表达式定义

y=Asin(2πft+ϕ)

其中 *A* 在**Amplitude**参数中指定，*f* 以赫兹为单位在**Frequency**参数中指定，*ϕ* 以弧度为单位在**Phase offset**参数中指定。

当您将**Output complexity**参数设置为 `Complex` 时，模块生成复指数信号。此复指数信号由以下类型的表达式定义

y=Aej(2πft+ϕ)=A{cos(2πft+ϕ)+jsin(2πft+ϕ)}

### 生成多通道输出

对于实数和复数正弦波，**Amplitude**、**Frequency**和**Phase offset**参数值（*A*、*f* 和 *ϕ*）可以是标量或长度为 *N* 的向量，其中 *N* 是输出中所需的通道数。当您将这些参数中的至少一个指定为长度为 *N* 的向量时，为其他参数指定的标量值将应用于每个通道。

例如，要生成包含以下实数正弦波的三通道输出，请按所示设置模块参数：

y={sin(2000πt)  (channel 1)2sin(1000πt)   (channel 2)3sin(500πt+π2)   (channel 3)

- **Output complexity** = `Real`
- **Amplitude** = `[1 2 3]`
- **Frequency** = `[1000 500 250]`
- **Phase offset** = `[0 0 pi/2]`
