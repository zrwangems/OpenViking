---
type: simulink-block
title: 'Hit Crossing'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'hitcrossing'
documentation_source_path: 'ref/hitcrossing.html'
language: zh-CN
chinese_source: worker-translation
---

# Hit Crossing

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量

模块检测其沿指定方向达到偏移量时的输入信号。

**数据类型：** `double`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 消息 | 函数调用事件

输出，指示输入信号是否越过命中偏移量。仅当选中 **Show output port** 参数复选框时，此端口才可见。

**信号输出**

如果选中 **Show output port** 复选框，并将 **Output type** 参数设置为 `Signal`，则模块输出指示何时发生穿越。

- 如果在沿指定方向检测到命中穿越后，输入信号恰好等于偏移量的值，则模块继续输出值 1。
- 如果两个相邻点处的输入信号包含偏移量值，则模块在第二个时间步输出值 1。
- 如果 **Show output port** 复选框*未*选中，则模块确保仿真找到穿越点，但不生成输出。
- 如果初始信号等于偏移量值，则仅当 **Hit crossing direction** 属性设置为 `either` 时，模块才输出 1。
- 如果启用了布尔逻辑信号，则输出为 `Boolean`。

**消息输出**

当 **Output type** 参数设置为 `Message` 时，Hit Crossing 模块也可以输出消息。

- 如果输入信号沿指定方向越过偏移量值，则模块输出一条消息。
- 如果输入信号沿指定方向达到偏移量值并保持在该处，则模块在命中时刻输出一条消息，并在信号离开偏移量值时输出一条消息。
- 如果初始输入信号等于偏移量值，则仅当 **Hit crossing direction** 设置为 `either` 时，模块才输出一条 `Crossing Type` 值为 `None` 的消息。

消息输出信号是一个包含四个字段的 `struct`。

**注意**

如果消息输出信号跨越模型引用边界，或用作 Stateflow® 图表的输入，则需要为该消息创建总线对象。请参阅提示。

**函数调用输出**

当 **Output type** 参数设置为 `Function-Call` 时，Hit Crossing 模块也可以输出函数调用事件。

- 每当输入信号沿指定方向越过偏移量值时，模块输出单个函数调用事件。
- 函数调用事件可以发送到函数调用子系统或函数调用模型的函数调用输入端口。
- 该输出等效于每个时间步的 Function-Call Generator 模块的输出，且该模块的 **Number of iterations** 参数设置为 `1`。

### **CrossingType** — 过零方向 `None` | `NegativeToPositive` | `NegativeToZero` | `ZeroToPositive` | `PositiveToNegative` | `PositiveToZero` | `ZeroToNegative`

此字段显示信号越过 **Hit crossing offset** 值的方向。
Negative、Zero 和 Positive 是相对于偏移值定义的。数据类型为
`slHitCrossingType`，这是一种
*枚举数据类型*。有关详细信息，请参阅 Use Enumerated Data in Simulink Models。例如，如果
`HitCrossingOffset` 设置为 2，则越过此偏移值的上升信号将被记录
为 `NegativeToPositive` 命中穿越。

**注意**

命中穿越是根据
**Hit crossing direction**
设置记录的。换句话说，如果您将 **Hit
crossing direction** 设置为检测
`falling` 命中穿越，则不会记录
`NegativeToPositive` 命中。

**注意**

在 SimEvents® 模块中，如果实体的 `Crossing
Type` 是
`NegativeToPositive` 命中穿越，
则 `entity.CrossingType ==
slHitCrossingType.NegativeToPositive`
返回逻辑 1 `(true)`。

如果信号达到
`HitCrossingOffset` 值并保持不变，
则在命中穿越发生时，会根据方向注册单个 `NegativeToZero` 或
`PositiveToZero` 命中。

**数据类型：** `slHitCrossingType`

### **Index** — 发生命中穿越事件的输入信号索引 非负整数

对于传递到
Hit Crossing 模块的 *n* 个信号，此字段表示
哪个信号发生了命中穿越事件。对于矩阵输入，
此字段遵循 MATLAB® 线性索引。请参阅 Array Indexing。

**数据类型：** `uint32`

### **Time** — 命中穿越事件的时间 实数、有限值

命中穿越
事件的时间 *T*。

**数据类型：** `double`

### **Offset** — 用于检测的命中穿越值 `0`（默认）| 实数值

由 Hit crossing offset 参数指定的命中穿越偏移值。

**数据类型：** `double`

**数据类型：** `double` | `Boolean` | `struct`

## 参数

### **Hit crossing offset** — 用于检测的命中穿越值 `0`（默认）| 实数值

指定当输入按 **Hit crossing direction** 指定的方向穿越时，模块检测的值。

#### 编程使用

|  |
| --- |
| **模块参数**：`HitCrossingOffset` |
| **类型**：character vector |
| **值**：real values |
| **默认值**：`'0'` |

### **Hit crossing direction** — 输入信号到达命中穿越的方向 `either`（默认）| `falling` | `rising`

输入信号接近命中穿越偏移值以检测穿越的方向。

当设置为 `either` 时，该模块用作
*几乎相等* 模块，有助于规避
有限数学和计算机精度方面的限制。由于这些
原因使用，此模块可能比在模型中添加逻辑
来检测此条件更方便。

当 **Hit crossing direction** 属性设置为
`either` 且模型使用定步长
求解器时，该模块具有以下行为。如果输出信号为 1，
则模块会在下一个时间步将输出信号设置为 0，除非输入
信号等于偏移值。

#### 编程使用

|  |
| --- |
| **模块参数**：`HitCrossingDirection` |
| **类型**：character vector |
| **值**：`'either'` | `'rising'` | `'falling'` |
| **默认值**：`'either'` |

### **Show output port** — 显示输出端口 `off`（默认）| `on`

如果选中，则在模块图标上创建输出端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`ShowOutputPort` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

### **Output type** — 选择信号、消息或函数调用输出 `Signal`（Simulink® 的默认值）| `Message`（SimEvents 的默认值）| `Function-Call`

当 **Output type** 设置为
`Signal` 时，每当输入信号沿 **Hit crossing
direction** 方向越过 **Hit crossing
offset** 值时，输出信号被置为一，
其他时间为零。

当 **Output type** 设置为 `Message` 时，
输出信号变为消息。

当 **Output type** 设置为 `Function-Call` 时，
输出信号变为函数调用事件。

#### 编程使用

|  |
| --- |
| **模块参数**：`HitCrossingOutputType` |
| **类型**：character vector |
| **值**：`'Signal'` | `'Message'` | `'Function-Call'` |
| **默认值**：`'Signal'` |

### **Enable zero-crossing detection** — 启用过零检测 `on`（默认）| `off`

选择以启用过零检测。有关详细信息，请参阅 Zero-Crossing Detection。

#### 编程使用

|  |
| --- |
| **Parameter:** `ZeroCross` |
| **类型**：character vector, string |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

## 所属库

Simulink / Discontinuities Simulink / Messages & Events HDL Coder / Discontinuities SimEvents

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不推荐用于生产代码生成。

仅支持 `ERT` 目标的浮点数据类型。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL
实现和综合逻辑的额外配置选项。

**HDL Architecture**

此模块具有一个默认 HDL 架构。

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**Restriction**

Hit crossing direction 必须为 `rising` 或
`falling`。

当 `Output Type` 设置为
`Message` 时，不支持 HDL 代码生成。

## 版本历史

**在 R2018a 中引入**

## 描述

检测交叉点

Hit Crossing 模块检测输入何时沿
**Hit crossing direction** 属性指定的方向达到 **Hit
crossing offset** 参数值。

您可以将模块配置为输出 `1` 或 `0` 信号、
消息或函数调用事件。有关更多信息，请参阅
Output。
