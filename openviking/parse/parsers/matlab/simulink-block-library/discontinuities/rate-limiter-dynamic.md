---
type: simulink-block
title: 'Rate Limiter Dynamic'
family: discontinuities
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Discontinuities'
documentation_page: 'ratelimiterdynamic'
---

# Rate Limiter Dynamic

Limit rate of change of signal

## 中文

限制信号变化的速率

### 所属库

Simulink / Discontinuities

### 描述

Rate Limiter Dynamic 模块限制信号的上升和下降速率。

- 外部信号 `up` 设置信号上升沿速率的上限。
- 外部信号 `lo` 设置信号下降沿速率的下限。

使用 Rate Limiter Dynamic 模块时，请遵循以下指导原则：

- 确保 `up` 和 `lo` 的数据类型与输入信号 `u` 的数据类型相同。

  如果下限使用有符号类型，而输入信号使用无符号类型，则输出信号将一直增加，而不管输入信号和限制。
- 使用定步长求解器仿真包含此模块的模型。

  因为 Rate Limiter Dynamic 模块仅支持离散采样时间。

### 端口

#### 输入

#### **u** — 输入信号 标量

要应用速率限制器算法的输入信号。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **lo** — 递减输入的导数的限制 标量

动态值，用于提供输入信号的下降沿速率的限制。`lo` 的信号数据类型需要与输入信号 `u` 的数据类型相同。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **up** — 递增输入的导数的限制 标量

动态值，用于提供输入信号的上升沿速率的限制。`up` 的信号数据类型需要与输入信号 `u` 的数据类型相同。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
#### 输出

#### **Y** — 输出信号 标量

经过速率限制器算法处理后的输出信号。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `enumerated` | `bus`

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

代码生成器不会在生成的代码中将构成非原子封装子系统模块的原始模块显式组合在一起。这种灵活性可以提高代码生成效率。在某些情况下，通过选择**视为原子单元**选项，可以通过将封装子系统模块配置为以原子单元执行来进行组合。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Discontinuities

## Description

The Rate Limiter Dynamic block limits the rising and falling rates of
the signal.

- The external signal `up` sets the upper limit on the rising
  rate of the signal.
- The external signal `lo` sets the lower limit on the falling
  rate of the signal.

Follow these guidelines when using the Rate Limiter Dynamic
block:

- Ensure that the data types of `up` and `lo`
  are the same as the data type of the input signal `u`.

  When the lower limit uses a signed type and the input signal uses an unsigned
  type, the output signal keeps increasing regardless of the input and the
  limits.
- Use a fixed-step solver to simulate models that contain this block.

  Because the Rate Limiter Dynamic block supports only discrete
  sample time.

## Ports

### Input

### **u** — Input signal scalar

Input signal to the rate limiter algorithm.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **lo** — Limit of derivative for decreasing input scalar

Dynamic value providing the limit of the falling rate of the input
signal. Make the signal data type of `lo`the same data
type of the input signal `u`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **up** — Limit of derivative for increasing input scalar

Dynamic value providing the limit of the rising rate of the input
signal. Make the signal data type of `up`the same data
type of the input signal `u`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Y** — Output signal scalar

Output signal from the rate limiter algorithm.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `enumerated` | `bus`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The code generator does not explicitly group primitive blocks that constitute a
nonatomic masked subsystem block in the generated code. This flexibility allows for
more efficient code generation. In certain cases, you can achieve grouping by
configuring the masked subsystem block to execute as an atomic unit by selecting the
**Treat as atomic unit** option.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
