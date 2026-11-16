---
type: simulink-block
title: 'Hit Crossing'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Discontinuities'
documentation_page: 'hitcrossing'
documentation_source_path: 'slref/hitcrossing.html'
language: zh-CN
chinese_source: official
---

# Hit Crossing

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量

输入信号，模块会检测其何时在指定方向上达到偏移值。

**数据类型:** `double`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 消息 | 函数调用事件

输出信号，用于指示输入信号是否穿越了指定的偏移值。仅当您选中**显示输出端口**参数复选框时，此端口才可见。

**信号输出**

如果选中**显示输出端口**复选框并将**输出类型**参数设置为**信号**，则模块输出将指示何时发生穿越。

- 如果在指定方向上检测到穿越之后输入信号刚好等于偏移值，模块将继续输出值 1。
- 如果两个相邻点的输入信号都到达了偏移值，模块将在第二个时间步输出值 1。
- 如果*没有*选中**显示输出端口**复选框，模块会确保仿真找到穿越点，但不生成输出。
- 如果初始信号等于偏移值，则仅当**穿越方向**属性设置为**任一沿**时，模块才输出 1。
- 如果启用布尔逻辑信号，则输出为 `Boolean`。

**消息输出**

当**输出类型**参数设置为**消息**时，Hit Crossing 模块也可以输出消息。

- 如果输入信号在指定方向上穿越偏移值，则模块输出一条消息。
- 如果输入信号在指定方向上达到偏移值并保持在此位置，则模块会在信号到达偏移值时输出一条消息，并在信号离开偏移值时输出一条消息。
- 如果初始输入信号等于偏移值，则仅当**穿越方向**设置为**任一沿**时，模块才会在 `Crossing Type` 值为 `None` 时输出消息。

消息输出信号是具有四个字段的 `struct`。

**注意**

如果消息输出信号穿越模型引用边界或用作 Stateflow® 图的输入，则需要为消息创建总线对象。请参阅提示。

**函数调用输出**

当**输出类型**参数设置为**函数调用**时，Hit Crossing 模块也可以输出函数调用事件。

- 每当输入信号在指定方向上穿越偏移值时，模块就输出一个函数调用事件。
- 函数调用事件可以发送到函数调用子系统或函数调用模型的函数调用输入端口。
- 该输出等效于**迭代次数**参数设置为 `1` 的 Function-Call Generator 模块在每个时间步的输出。

### **CrossingType** — 过零的方向 `None` | `NegativeToPositive` | `NegativeToZero` | `ZeroToPositive` | `PositiveToNegative` | `PositiveToZero` | `ZeroToNegative`

此字段显示信号穿越**穿越偏移量**值的方向。Negative、Zero 和 Positive 相对于偏移值进行定义。数据类型是 `slHitCrossingType`，它是一种*枚举数据类型*。有关详细信息，请参阅在 Simulink 模型中使用枚举数据。例如，如果 `HitCrossingOffset` 设置为 2，则穿越此偏移值的上升信号将记录为 `NegativeToPositive` 穿越。

**注意**

系统会根据**穿越方向**的设置来记录穿越。换句话说，如果将**穿越方向**设置为检测**下降沿**穿越，则不会记录 `NegativeToPositive` 穿越。

**注意**

在 SimEvents® 模块中，如果实体的 `Crossing Type` 是 `NegativeToPositive` 穿越，则 `entity.CrossingType == slHitCrossingType.NegativeToPositive`  返回逻辑值 1 `(true)`。

如果信号到达 `HitCrossingOffset` 值并保持不变，则在发生穿越时会记录单个 `NegativeToZero` 或 `PositiveToZero`（取决于方向）穿越。

**数据类型:** `slHitCrossingType`

### **Index** — 发生穿越事件的输入信号的索引 非负整数

对于传递给 Hit Crossing 模块的 *n* 个信号，此字段表示哪个信号具有穿越事件。对于矩阵输入，该字段遵循 MATLAB® 线性索引。请参阅数组索引。

**数据类型:** `uint32`

### **Time** — 穿越事件的时间 有限实数

发生穿越事件的时间 *T*。

**数据类型:** `double`

### **Offset** — 检测的穿越值 `0` (默认) | 实数值

由 穿越偏移量 参数指定的穿越偏移值。

**数据类型:** `double`

**数据类型:** `double` | `Boolean` | `struct`

## 参数

### **穿越偏移量** — 检测的穿越值 `0` (默认) | 实数值

指定当输入在**穿越方向**指定的方向上穿越时模块检测的值。

#### 编程用法

|  |
| --- |
| **模块参数**：`HitCrossingOffset` |
| **类型**：字符向量 |
| **值**：实数值 |
| **默认值**：`'0'` |

### **穿越方向** — 输入信号的穿越方向 **任一沿** (默认) | **下降沿** | **上升沿**

检测穿越时输入信号接近穿越偏移值的方向。

当设置为**任一沿**时，模块的作用相当于一个*几乎相等*模块，对于规避有限的数学和计算机精度的限制很有用。由于这些原因，此模块可能比在模型中添加逻辑来检测这种情况更方便。

当**穿越方向**属性设置为**任一沿**且模型使用定步长求解器时，此模块具有以下行为。如果输出信号为 1，则模块将下一个时间步的输出信号设置为 0，除非输入信号等于偏移值。

#### 编程用法

|  |
| --- |
| **模块参数**：`HitCrossingDirection` |
| **类型**：字符向量 |
| **值**：`'either'` | `'rising'` | `'falling'` |
| **默认值**：`'either'` |

### **显示输出端口** — 显示输出端口 `off` (默认) | `on`

如果选择，请在模块图标上创建输出端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`ShowOutputPort` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

### **输出类型** — 选择信号、消息或函数调用输出 **信号**（Simulink® 的默认值） | **消息**（SimEvents 的默认值） | **函数调用**

当**输出类型**设置为**信号**时，只要输入信号穿越**穿越方向**中的**穿越偏移量**值且在其他时间为零，输出信号就会设置为 1。

当**输出类型**设置为**消息**时，输出信号变为消息。

当**输出类型**设置为**函数调用**时，输出信号成为函数调用事件。

#### 编程用法

|  |
| --- |
| **模块参数**：`HitCrossingOutputType` |
| **类型**：字符向量 |
| **值**：`'Signal'` | `'Message'` | `'Function-Call'` |
| **默认值**：`'Signal'` |

### **启用过零检测** — 启用过零检测 `on` (默认) | `off`

选择此项以启用过零检测。有关详细信息，请参阅过零检测。

#### 编程用法

|  |
| --- |
| **参数：**`ZeroCross` |
| **类型：**字符向量、字符串 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'on'` |

## 所属库

Simulink / Discontinuities Simulink / Messages & Events HDL Coder / Discontinuities SimEvents

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `是` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不建议用于生产代码生成。

对于 `ERT` 目标，仅支持浮点数据类型。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

**限制**

穿越方向必须为**上升沿**或**下降沿**。

当 `Output Type` 设置为**消息**时，不支持 HDL 代码生成。

## 版本历史

**在 R2006a 之前推出**

## 描述

检测穿越点

Hit Crossing 模块检测输入何时在由**穿越方向**属性指定的方向上到达**穿越偏移量**参数值。

您可以将该模块配置为输出 `1` 或 `0` 信号、消息或函数调用事件。有关详细信息，请参阅输出。
