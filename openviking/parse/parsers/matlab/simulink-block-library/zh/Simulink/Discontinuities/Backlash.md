---
type: simulink-block
title: 'Backlash'
family: 'libsb2sl'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'DYN'
documentation_page: 'backlash'
documentation_source_path: 'slref/backlash.html'
language: zh-CN
chinese_source: worker-translation
---

# Backlash

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量

输入到 backlash 算法的输入信号。该信号的值要么位于死区内，要么沿正方向或负方向与输出啮合。

**数据类型：** `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

将 backlash 算法应用于输入信号后的输出信号。当输入位于死区内时，输出保持不变。如果输入与输出啮合，则输出变化量与输入相同。

**数据类型：** `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **Deadband width** — 指定死区宽度 `1`（默认）| 标量 | 向量

指定以输出值为中心的死区大小。当输入信号位于死区内时，输入的变化不会引起输出的变化。当输入信号位于死区外时，输出变化量与输入相同。

#### 编程使用

|  |
| --- |
| **模块参数**：`BacklashWidth` |
| **类型**：字符向量 |
| **值**：实数标量或向量 |
| **默认值**：`'1'` |

### **Initial output** — 指定初始输出值 0（默认）| 标量 | 向量

指定死区的初始中心。如果初始输入值位于死区内，则输出值等于 **Initial output**。如果初始输入值位于死区外，则输出值为 **Initial output** 加上或减去死区宽度的一半。

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialOutput` |
| **类型**：字符向量 |
| **值**：实数标量或向量 |
| **默认值**：`'0'` |

### **Input processing** — 指定基于采样或基于帧的处理 `Elements as channels (sample based)`（默认）| `Columns as channels (frame based)`

指定模块执行基于采样还是基于帧的处理：

- `Columns as channels (frame based)` — 将输入的每一列视为单独的通道（基于帧的处理）。

  **注意**

  基于帧的处理需要 DSP System Toolbox™ 许可证。

  有关详细信息，请参阅 Sample- and Frame-Based Concepts (DSP System Toolbox)。
- `Elements as channels (sample based)` — 将输入的每个元素视为单独的通道（基于采样的处理）。

使用 **Input processing** 指定模块执行基于采样还是基于帧的处理。有关这两种处理模式的详细信息，请参阅 Sample- and Frame-Based Concepts (DSP System Toolbox)。

#### 编程使用

|  |
| --- |
| **模块参数**：`InputProcessing` |
| **类型**：字符向量 |
| **值**：`'Columns as channels (frame based)'` | `'Elements as channels (sample based)'` |
| **默认值**：`'Elements as channels (sample based)'` |

### **Enable zero-crossing detection** — 启用零交叉检测 `on`（默认）| `off`

选择以启用零交叉检测。有关详细信息，请参阅 Zero-Crossing Detection。

此模块仅在使用可变步长求解器的仿真中支持零交叉检测。当您使用固定步长求解器进行仿真时，软件不会为此模块检测或定位零交叉。

#### 编程使用

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：字符向量 | 字符串 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

## 所属库

Simulink / Discontinuities HDL Coder / Discontinuities

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数（`string.h`）。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

**Deadband width** 和 **Initial output** 参数仅支持标量值。

## 版本历史

**在 R2006a 之前引入**

## 描述

对具有间隙的系统行为进行建模

Backlash 模块实现这样一个系统：输入的变化会引起输出的等量变化，除非输入改变方向。当输入改变方向时，输入的初始变化对输出没有影响。系统中左右两侧的间隙量称为*死区*。死区以输出为中心。下图显示了一个初始状态，其默认死区宽度为 1，初始输出为 0。

具有间隙的系统可以处于以下三种模式之一。

| 模式 | 输入 | 输出 |
| --- | --- | --- |
| 未啮合 | 位于死区内。 | 保持不变。 |
| 正向啮合 | 位于死区外且正在增大。 | 等于输入*减去*死区宽度的一半。 |
| 负向啮合 | 位于死区外且正在减小。 | 等于输入*加上*死区宽度的一半。 |

**Initial output** 参数值定义死区的初始中心。

下表显示当初始条件为：**Deadband width** = `2` 且 **Initial output** = `5` 时的输出值。

| 输出值 | 条件 |
| --- | --- |
| 5 | 4 <= input <= 6 |
| input + 1 | input < 4 |
| input - 1 | input > 6 |

例如，您可以使用 Backlash 模块对两个齿轮的啮合进行建模。输入和输出都是在一端带有齿轮的轴，并且输入轴驱动输出轴。齿轮齿之间的额外空间引入了*间隙*。此间距的宽度即为 **Deadband width** 参数。如果系统初始处于未啮合状态，则 **Initial output** 参数定义输出。

这些图说明了当初始输入位于死区内且系统以未啮合模式开始时的操作。

当输入增大并到达死区末端时，它与输出啮合。输出保持其先前的值。

在输入与输出啮合后，输出的变化量与输入相同。

如果输入反向，则它与输出脱离啮合。输出保持不变，直到输入到达死区末端并再次啮合。
