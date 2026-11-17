---
type: simulink-block
title: 'HDL Counter'
family: 'sources'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'hdlcounter'
documentation_source_path: 'ref/hdlcounter.html'
language: zh-CN
chinese_source: worker-translation
---

# HDL Counter

## 端口

### 输入

### **rst** — 本地复位端口标量

计数器的本地复位端口，当其为高电平时复位计数值。

#### 依赖关系

要启用此端口，请设置 **本地复位端口**。

**数据类型：** `Boolean`

### **load** — 加载端口标量

加载端口，当其为高电平时将计数器设置为加载值 `load_val`。

#### 依赖关系

要启用此端口，请设置 **加载端口**。

**数据类型：** `Boolean`

### **load\_val** — 加载端口值标量

当向加载端口提供高输入时，用于设置计数值的加载数据值。

#### 依赖关系

要启用此端口，请设置 **加载端口**。

**数据类型：** `Boolean`

### **enb** — 计数使能端口标量

使能信号，用于指定计数器是否应从先前值开始计数。当此信号为高电平时，计数器根据方向继续向上或向下计数。当此信号为低电平时，计数器保持先前值。

#### 依赖关系

要启用此端口，请设置 **计数使能端口**。

**数据类型：** `Boolean`

### **dir** — 计数方向端口标量

计数方向，用于指定向上计数还是向下计数。此端口与 **步长值** 交互以确定计数方向。

- `1`：此值为默认值，会得到向上计数器。将 **步长值** 加到当前计数值以计算下一个值。
- `0`：此值会得到向下计数器。从当前计数值减去 **步长值** 以计算下一个值。

#### 依赖关系

要启用此端口，请设置 **计数方向端口**。

**数据类型：** `Boolean`

### 输出

### **count** — 计数值标量

这是计数值。默认情况下，如果未启用输入端口，计数器会根据 **计数器类型**、**计数目标值** 和 **字长** 向上计数到某个值。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **count\_hit** — 计数器限制指示标量

计数器限制指示，以 Boolean 标量形式返回。

- `1`：表示计数器达到其限制。
- `0`：表示计数器未达到其限制。

#### 依赖关系

要启用此端口，请选择 **计数命中输出端口** 参数。

**数据类型：** `Boolean`

## 参数

### **计数器类型** — 计数器行为 `Free running` (默认) | `Count limited` | `Modulo`

计数器行为，用于确定是对自由运行、计数受限还是取模硬件计数器建模。

- `Free running` (默认)：计数器继续按 **步长值** 递增或递减，直到复位。
- `Count limited`：计数器按 **步长值** 递增或递减，直到恰好等于 **计数目标值**。如果 **步长值** 的值使得计数值不恰好等于 **计数目标值**，则它可以继续计数到一个由字长确定的阈值。
- `Modulo`：计数器按 **步长值** 递增或递减，直到达到 **计数目标值**。如果 **步长值** 的值使得计数值不恰好等于 **计数目标值**，则计数器回绕到一个由回绕步长值确定的值。

#### Programmatic Use

|  |
| --- |
| **模块参数：** `CountType` |
| **类型：** character vector |
| **值：** `'Free running'` | `'Count limited'` | `'Modulo'` |
| **默认值：** `'Free running'` |

### **初始值** — 复位后的计数值 `0` (默认)

计数器复位到的值。默认值为 `0`。

#### Programmatic Use

|  |
| --- |
| **模块参数：** `CountInit` |
| **类型：** character vector |
| **值：** 大于或等于零的整数 |
| **默认值：** `'0'` |

### **步长值** — 计数的步长值 `1` (默认)

在每个采样时间添加到计数器的值。默认值为 `1`。

#### Programmatic Use

|  |
| --- |
| **模块参数：** `CountStep` |
| **类型：** character vector |
| **值：** 大于或等于零的整数 |
| **默认值：** `'1'` |

### **计数目标值** — 阈值计数值 `25` (默认)

当使用 `Count limited` 计数器时，如果计数恰好等于 **计数目标值**，则计数从 **初始值** 重新开始。如果计数值超过 **计数目标值**，则计数器继续计数到一个取决于 **字长** 的阈值。默认值为 `25`。

当使用 `Modulo` 计数器时，如果计数达到 **计数目标值**，则计数从一个由回绕步长值确定的值重新开始。

#### 依赖关系

要启用此参数，请将 **计数器类型** 设置为 `Count limited` 或 `Modulo`。

#### Programmatic Use

|  |
| --- |
| **模块参数：** `CountMax` |
| **类型：** character vector |
| **值：** 大于或等于零的整数 |
| **默认值：** `'25'` |

### **计数起始** — 计数起始值的判定条件 `Initial value` (默认) | `Specify`

指定当使用 `Count limited` 或 `Free running` 计数器时，用于设置翻转后起始值的参数。使用 `Modulo` 计数器时，计数器可以翻转到与计数起始值不同的回绕步长值。设置为 `Specify` 时，**计数起始值** 参数为翻转后的起始值。默认值为 `Initial value`。

#### Programmatic Use

|  |
| --- |
| **模块参数：** `CountFromType` |
| **类型：** character vector |
| **值：** `'Initial value'` | `'Specify'` |
| **默认值：** `'Initial value'` |

### **计数起始值** — 计数起始的初始值 `0` (默认)

当 **计数起始** 设置为 `Specify` 时翻转后的计数器值。默认值为 0。

#### Programmatic Use

|  |
| --- |
| **模块参数：** `CountFrom` |
| **类型：** character vector |
| **值：** `'Initial value'` | `'Specify'` |
| **默认值：** `'Initial value'` |

### **本地复位端口** — 用于复位计数器的本地端口 `off` (默认) | `on`

选中时，创建本地复位端口 `rst`。

#### Programmatic Use

|  |
| --- |
| **模块参数：** `CountResetPort` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **加载端口** — 用于加载值的端口 `off` (默认) | `on`

选中时，创建加载数据端口 `load_val` 和加载触发端口 `load`。

#### Programmatic Use

|  |
| --- |
| **模块参数：** `CountLoadPort` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **计数使能端口** — 用于使能计数的端口 `off` (默认) | `on`

选中时，创建计数使能端口 `enb`。

#### Programmatic Use

|  |
| --- |
| **模块参数：** `CountEnbPort` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **计数方向端口** — 用于计数方向的端口 `off` (默认) | `on`

选中时，创建计数方向端口 `dir`。

启用此参数会禁用 **计数命中输出端口** 参数。

#### Programmatic Use

|  |
| --- |
| **模块参数：** `CountDirPort` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **计数命中输出端口** — 用于计数限制的端口 `off` (默认) | `on`

选择此参数以启用 **count\_hit** 输出端口。

启用此参数会清除 **计数方向端口** 参数。

#### Programmatic Use

|  |
| --- |
| **模块参数：** `CountHitOutputPort` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **计数器输出数据为** — 输出数据类型符号性 `Unsigned` (默认) | `Signed`

输出数据类型符号性。默认值为 `Unsigned`。

#### Programmatic Use

|  |
| --- |
| **模块参数：** `CountDataType` |
| **类型：** character vector |
| **值：** `'Unsigned'` | `'Signed'` |
| **默认值：** `'off'` |

### **字长** — 计数器字长 `8` (默认)

整数计数器的位宽（包括符号位）；定点数据类型计数器的字长。如果 **输出数据类型** 为 `Unsigned`，最小值为 `1`；如果为 `Signed`，则为 `2`。最大值为 `125`。默认值为 `8`。

#### Programmatic Use

|  |
| --- |
| **模块参数：** `CountWordLen` |
| **类型：** character vector |
| **值：** 大于或等于 1 的整数 |
| **默认值：** `'8'` |

### **小数长度** — 计数器小数长度 `0` (默认)

定点数据类型的小数长度。默认值为 `0`。

#### Programmatic Use

|  |
| --- |
| **模块参数：** `CountFracLen` |
| **类型：** character vector |
| **值：** 大于或等于零的整数 |
| **默认值：** `'0'` |

### **采样时间** — 计数器采样时间 `1` (默认)

采样时间。默认值为 `1`。当选择以下任一参数时，此参数不可用，模块将从输入端口继承其采样时间：

- **本地复位端口**
- **加载端口**
- **计数使能端口**
- **计数方向端口**

#### Programmatic Use

|  |
| --- |
| **模块参数：** `CountSampTime` |
| **类型：** character vector |
| **值：** 大于或等于 1 的整数 |
| **默认值：** `'1'` |

## 所属库

HDL Coder / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |

**限制**

- 如果 HDL Counter 的输入信号位宽超过数据类型限制，生成的 HDL 代码可能会产生不正确的仿真结果。为容纳更大的位宽，请使用更大的数据类型。
- 此模块不支持向量。模块输入和输出仅支持标量类型。
- 在 `Modulo` 计数器模式下使用的加载值必须位于 **计数起始** 和 **计数目标值** 的范围内，以避免仿真不匹配。

## 版本历史

**在 R2014a 中引入**

## 描述

自由运行或计数受限硬件计数器

HDL Counter 模块对自由运行、计数受限或取模硬件计数器建模，支持有符号和无符号整数以及定点数据类型。计数器输出当前采样时间的值。在仿真期间，此模块不会因溢出回绕而报告警告或错误。要报告这些警告，请参阅 `Simulink.restoreDiagnostic`。

默认情况下，计数器没有输入端口。计数器根据 **计数器类型**、**计数目标值** 和 **字长**，从初始值向上计数到阈值。计数器的输出数据类型取决于 **计数器输出数据**、**字长** 和 **小数长度**。
