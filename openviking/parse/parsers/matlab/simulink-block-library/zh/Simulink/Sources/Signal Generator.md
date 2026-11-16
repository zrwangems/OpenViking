---
type: simulink-block
title: 'Signal Generator'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'signalgenerator'
documentation_source_path: 'slref/signalgenerator.html'
language: zh-CN
chinese_source: official
---

# Signal Generator

## 端口

### 输出

### **Port\_1** — 生成的输出信号 标量 | 向量 | 矩阵

输出信号指定为下列波形之一。

- 正弦波
- 方波
- 锯齿波
- 随机

**数据类型:** `double`

## 参数

### **波形** — 要生成的波形 **正弦** (默认) | **方波** | **锯齿波** | **随机**

指定波形。

#### 编程用法

|  |
| --- |
| **模块参数**：`WaveForm` |
| **类型**：字符向量 |
| **值**：`'sine'` | `'square'` | `'sawtooth'` | `'random'` |
| **默认值**：`'sine'` |

### **时间(t)** — 时间变量的来源 **使用仿真时间** (默认) | **使用外部信号**

指定是使用仿真时间还是外部信号作为波形时间变量值的来源。如果指定外部源，模块将显示一个输入端口用来连接该外部源。

#### 编程用法

|  |
| --- |
| **模块参数**：`TimeSource` |
| **类型**：字符向量 |
| **值**：`'Use simulation time'` | `'Use external signal'` |
| **默认值**：`'Use simulation time'` |

### **振幅** — 信号振幅 `1` (默认) | 标量 | 向量 | 矩阵

指定生成的波形的振幅。

#### 编程用法

|  |
| --- |
| **模块参数**：`Amplitude` |
| **类型**：字符向量 |
| **值**：实数标量 |
| **默认值**：`'1'` |

### **频率** — 信号频率 `1` (默认) | 标量 | 向量 | 矩阵

指定生成的波形的频率。

#### 编程用法

|  |
| --- |
| **模块参数**：`Frequency` |
| **类型**：字符向量 |
| **值**：实数标量 |
| **默认值**：`'1'` |

### **单位** — 信号单位 **rad/sec** (默认) | **Hertz**

指定信号单位是 **Hertz** 还是 **rad/sec**。

#### 编程用法

|  |
| --- |
| **模块参数**：`Units` |
| **类型**：字符向量 |
| **值**：`'rad/sec'` | `'Hertz'` |
| **默认值**：`'rad/sec'` |

### **将向量参数解释为一维向量** — 将向量视为一维 `on` (默认) | `off`

如果**常量值**参数的计算结果为包含 `N` 个元素的行或列向量，选中此复选框将输出长度为 `N` 的向量。

- 如果**常量值**参数的计算结果为包含 `N` 个元素的行或列向量，则选中此复选框时，模块将输出长度为 `N` 的向量。例如，模块将输出 `1-by-N` 维或 `N-by-1` 维矩阵。
- 如果**常量值**参数的计算结果为包含 `N` 个元素的行或列向量，则清除此复选框时，模块不输出长度为 `N` 的向量。

#### 编程用法

|  |
| --- |
| **模块参数**：`VectorParams1D` |
| **类型：**字符向量 |
| **值：**`'on' | 'off'` |
| **默认值：**`'on'` |

## 所属库

Simulink / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不能在触发子系统层次结构中使用。

当配置为基于采样运行时，这些模块不引用绝对时间。在基于时间的运行中，它们依赖于绝对时间。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

**限制**

将 Signal Generator 模块连接到 DUT 端口以在模型中用作源模块，但确保它不放置在 DUT 子系统内。

## 版本历史

**在 R2006a 之前推出**

## 描述

生成各种波形

### 支持的运算

Signal Generator 模块可以产生四种不同波形：

- 正弦波
- 方波
- 锯齿波
- 随机

您可以使用 hertz 或 rad/sec 为单位表示信号参数。使用默认参数值，可以获得下列波形之一：

| 波形 | 波形输出 |
| --- | --- |
| 正弦波 |  |
| 方波 |  |
| 锯齿波 |  |
| 随机波 |  |

为**振幅**参数指定负值将产生 180 度相移。您可以通过多种方式生成除 180 度之外的相移波。例如，您可以将 Clock 模块信号连接到 MATLAB Function 模块，并为特定波形编写方程。

您可以在仿真过程中更改 Signal Generator 模块的输出设置，以快速确定系统对不同类型输入的响应。

**振幅**和**频率**参数确定输出信号的振幅和频率。在进行标量扩展后，这两个参数必须具有相同的维度。如果清除**将向量参数解释为一维向量**复选框，模块将输出与**振幅**和**频率**参数（标量扩展后）具有相同维度的信号。如果选中**将向量参数解释为一维向量**复选框，若**振幅**和**频率**参数是行或列向量，即单行或单列二维数组，模块将输出向量（一维）信号。否则，模块将输出与这两个参数具有相同维度的信号。

### 求解器注意事项

如果您的模型使用定步长求解器，Simulink® 将对整个仿真使用相同的步长。在这种情况下，Signal Generator 模块输出将提供理想波形的均匀采样表示。

如果您的模型使用变步长求解器，Simulink 可能会在仿真过程中使用不同的步长。在这种情况下，Signal Generator 模块输出并不总是提供理想波形的均匀采样表示。为了确保模块输出是均匀采样的表示，请直接在 Signal Generator 模块的下游添加一个 Hit Crossing 模块。以下模型显示了具有和没有 Hit Crossing 模块时 Signal Generator 模块输出的区别。

| 使用变步长求解器的模型 | Signal Generator 模块输出 |
| --- | --- |
|  | Signal Generator with sawtooth wave and variable-step solver |
|  | Signal Generator with sawtooth wave and variable-step solver and Hit Cross |
