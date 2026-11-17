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
chinese_source: worker-translation
---

# Signal Generator

## 端口

### 输出

### **Port\_1** — 生成的输出信号 标量 | 向量 | 矩阵

输出信号，指定为以下波形之一。

- sine
- square
- sawtooth
- random

**数据类型：** `double`

## 参数

### **Wave form** — 要生成的波形 `sine`（默认）| `square` | `sawtooth` | `random`

指定波形。

#### 编程使用

|  |
| --- |
| **模块参数**：`WaveForm` |
| **类型**：字符向量 |
| **值**：`'sine'` | `'square'` | `'sawtooth'` | `'random'` |
| **默认值**：`'sine'` |

### **Time (t)** — 时间变量来源 `Use simulation time`（默认）| `Use external signal`

指定是将仿真时间还是外部信号用作波形时间变量的值来源。如果指定外部来源，该模块将显示一个输入端口用于连接该来源。

#### 编程使用

|  |
| --- |
| **模块参数**：`TimeSource` |
| **类型**：字符向量 |
| **值**：`'Use simulation time'` | `'Use external signal'` |
| **默认值**：`'Use simulation time'` |

### **Amplitude** — 信号幅值 `1`（默认）| 标量 | 向量 | 矩阵

指定所生成波形的幅值。

#### 编程使用

|  |
| --- |
| **模块参数**：`Amplitude` |
| **类型**：字符向量 |
| **值**：实标量 |
| **默认值**：`'1'` |

### **Frequency** — 信号频率 `1`（默认）| 标量 | 向量 | 矩阵

指定所生成波形的频率。

#### 编程使用

|  |
| --- |
| **模块参数**：`Frequency` |
| **类型**：字符向量 |
| **值**：实标量 |
| **默认值**：`'1'` |

### **Units** — 信号单位 `rad/sec`（默认）| `Hertz`

将信号单位指定为 `Hertz` 或 `rad/sec`。

#### 编程使用

|  |
| --- |
| **模块参数**：`Units` |
| **类型**：字符向量 |
| **值**：`'rad/sec'` | `'Hertz'` |
| **默认值**：`'rad/sec'` |

### **Interpret vector parameters as 1-D** — 将向量视为一维 `on`（默认）| `off`

如果 **Constant value** 参数求值为 `N` 元素行向量或列向量，则选中此复选框可输出长度为 `N` 的向量。

- 选中此复选框时，如果 **Constant value** 参数求值为 `N` 元素行向量或列向量，则该模块输出长度为 `N` 的向量。例如，该模块输出维度为 `1-by-N` 或 `N-by-1` 的矩阵。
- 清除此复选框时，如果 **Constant value** 参数求值为 `N` 元素行向量或列向量，则该模块不输出长度为 `N` 的向量。

#### 编程使用

|  |
| --- |
| **模块参数**：`VectorParams1D` |
| **类型**：字符向量 |
| **值**：`'on' | 'off'` |
| **默认值**：`'on'` |

## 所属库

Simulink / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不能在触发子系统层级内使用。

这些模块在配置为基于采样的操作时不引用绝对时间。在基于时间的操作中，它们依赖于绝对时间。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

**限制**

将 Signal Generator 模块连接到 DUT 端口以将其用作模型中的源模块，但确保它不放置在 DUT 子系统内。

## 版本历史

**在 R2006a 之前引入**

## 描述

生成各种波形

### 支持的操作

Signal Generator 模块可以生成四种不同波形之一：

- sine
- square
- sawtooth
- random

您可以用赫兹或弧度每秒表示信号参数。使用默认参数值，您将获得以下波形之一：

| 波形 | 示波器输出 |
| --- | --- |
| 正弦波 |  |
| 方波 |  |
| 锯齿波 |  |
| 随机波 |  |

负的 **Amplitude** 参数值会导致 180 度相移。您可以通过多种方式生成非 180 度的相移波。例如，您可以将 Clock 模块信号连接到 MATLAB Function 模块，并编写特定波形的方程。

您可以在仿真进行期间更改 Signal Generator 模块的输出设置，以快速确定系统对不同类型输入的响应。

**Amplitude** 和 **Frequency** 参数决定输出信号的幅值和频率。这些参数在标量扩展后必须具有相同的维度。如果清除 **Interpret vector parameters as 1-D** 复选框，则该模块输出与 **Amplitude** 和 **Frequency** 参数（标量扩展后）具有相同维度的信号。如果选中 **Interpret vector parameters as 1-D** 复选框，则当 **Amplitude** 和 **Frequency** 参数为行向量或列向量（即单行或单列二维数组）时，该模块输出向量（一维）信号。否则，该模块输出与参数具有相同维度的信号。

### 求解器注意事项

如果您的模型使用固定步长求解器，Simulink® 在整个仿真过程中使用相同的步长。在这种情况下，Signal Generator 模块输出提供理想波形的均匀采样表示。

如果您的模型使用可变步长求解器，Simulink 在仿真期间可能使用不同的步长。在这种情况下，Signal Generator 模块输出并不总是提供理想波形的均匀采样表示。为确保模块输出为均匀采样表示，请在 Signal Generator 模块的直接下游添加一个 Hit Crossing 模块。这些模型展示了使用和不使用 Hit Crossing 模块时 Signal Generator 模块输出的差异。

| 使用可变步长求解器的模型 | Signal Generator 模块输出 |
| --- | --- |
|  | 使用锯齿波和可变步长求解器的 Signal Generator |
|  | 使用锯齿波、可变步长求解器和 Hit Cross 的 Signal Generator |
