---
type: simulink-block
title: 'Dead Zone'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Discontinuities'
documentation_page: 'deadzone'
documentation_source_path: '../simulink/slref/deadzone.html'
language: zh-CN
chinese_source: worker-translation
---

# Dead Zone

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量

死区算法的输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

对输入信号应用死区算法后的输出信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **Start of dead zone** — 指定死区的下界 `'-0.5'`（默认）| 标量 | 向量

指定死区下限。将 **Start of dead zone** 的值设置为小于或等于 **End of dead zone**。当输入值小于 **Start of dead zone** 时，模块将输出值向下偏移 **Start of dead zone** 的值。

#### 编程使用

|  |
| --- |
| **模块参数**：`LowerValue` |
| **类型**：字符向量 |
| **Value**：小于或等于 `UpperValue` 的标量或向量。 |
| **默认值**：`'-0.5'` |

### **End of dead zone** — 指定死区的上限 `'0.5'`（默认）| 标量 | 向量

指定死区上限。将 **End of dead zone** 的值设置为大于或等于 **Start of dead zone**。当输入值大于 **End of dead zone** 时，模块将输出值向下偏移 **End of dead zone** 的值。

#### 编程使用

|  |
| --- |
| **模块参数**：`UpperValue` |
| **类型**：字符向量 |
| **Value**：大于或等于 `LowerValue` 的标量或向量。 |
| **默认值**：`'0.5'` |

### **Saturate on integer overflow** — 溢出操作方式 `on`（默认）| `off`

指定溢出时饱和还是回绕。

- `on` — 溢出饱和到数据类型所能表示的最小值或最大值。
- `off` — 溢出回绕到数据类型所能表示的相应值。

例如，有符号 8 位整数 `int8` 所能表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出饱和在 127。类似地，模块输出饱和在最小输出值 -128。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生非预期的结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 -126。

#### 提示

- 当您的模型可能存在溢出并且您希望在生成的代码中显式添加饱和保护时，请考虑选中此参数。
- 当您希望优化生成代码的效率时，请考虑清除此参数。清除此参数还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors。
- 选中此参数时，饱和适用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter：** | `SaturateOnIntegerOverflow` |
| **值**：| `'on'`（默认）| `'off'` |

### **Treat as gain when linearizing** — 指定增益值 `on`（默认）| `off`

Simulink® 软件中的线性化命令在状态空间中将此模块视为增益。选中此参数可使这些命令将增益视为 1。清除此参数可使这些命令将增益视为 0。

#### 编程使用

|  |
| --- |
| **模块参数**：`LinearizeAsGain` |
| **类型**：字符向量 |
| **Value**：`'off'` | `'on'` |
| **默认值**：`'on'` |

### **Enable zero-crossing detection** — 启用过零检测 `on`（默认）| `off`

选中以启用过零检测。有关详细信息，请参阅 Zero-Crossing Detection。

#### 编程使用

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：字符向量 | 字符串 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

### **Sample time (-1 for inherited)** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter：** | `SampleTime` |
| **值**：| `"-1"`（默认）| 带引号的标量或向量 |

## 所属库

Simulink / Discontinuities HDL Coder / Discontinuities

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

提供零输出区域

Dead Zone 模块在指定区域内生成零输出，该区域称为死区。您将死区的下限（`LL`）和上限（`UL`）分别指定为 **Start of dead zone** 和 **End of dead zone** 参数。模块输出取决于输入（`U`）以及下限和上限的值。

| 输入 | 输出 |
| --- | --- |
| `U >= LL` 且 `U <= UL` | 零 |
| `U > UL` | `U` – `UL` |
| `U < LL` | `U` – `LL` |
