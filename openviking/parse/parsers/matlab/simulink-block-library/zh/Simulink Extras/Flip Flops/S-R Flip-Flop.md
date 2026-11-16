---
type: simulink-block
title: 'S-R Flip-Flop'
family: 'simulink-extras'
product_id: 'simulink-extras'
product_name: 'Simulink Extras'
documentation_release: R2025b
official_category: 'Flip Flops'
documentation_page: 'srflipflop'
documentation_source_path: '../simulink/ref_extras/srflipflop.html'
language: zh-CN
chinese_source: official
---

# S-R Flip-Flop

## 端口

### 输入

### **S** — 设置的输入 标量

*设置*的输入，指定为标量、向量或矩阵。

#### 依赖关系

S-R Flip-Flop 模块接受的数据类型取决于**将逻辑信号实现为布尔数据(而不是双精度数据)** 配置参数的设置：

- `On` - S-R Flip-Flop 模块只接受 `boolean` 类型的实数标量信号。
- `Off` - S-R Flip-Flop 模块接受 `boolean` 或 `double` 类型的实数标量信号（两个输入必须具有相同的类型）。

**数据类型:** `double` | `Boolean`

### **R** — 重置的输入 标量

*重置*的输入，指定为标量、向量或矩阵。

#### 依赖关系

S-R Flip-Flop 模块接受的数据类型取决于**将逻辑信号实现为布尔数据(而不是双精度数据)** 配置参数的设置：

- `On` - S-R Flip-Flop 模块只接受 `boolean` 类型的实数标量信号
- `Off` - S-R Flip-Flop 模块接受 `boolean` 或 `double` 类型的实数标量信号（两个输入必须具有相同的类型）。

**数据类型:** `double` | `Boolean`
### 输出

### **Q** — 输出信号 Q 标量

输出信号 **Q**，具有与输入相同的维度和数据类型。

**数据类型:** `double` | `Boolean`

### **!Q** — 输出信号 !Q 标量

输出信号 **!Q**，具有与输入相同的维度和数据类型。

**数据类型:** `double` | `Boolean`

## 参数

### **初始条件(Q 的状态)** — 输出 Q 的初始值 `0` (默认) | 标量

指定输出 **Q** 的初始值。非零值被视为 true (`1`)。

#### 编程用法

|  |
| --- |
| **模块参数**：`initial_condition` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'0'` |

## 所属库

Simulink Extras / Flip Flops

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2008b 中推出**

## 描述

S-R 触发器建模

S-R Flip-Flop 模块对使用 NOR 门构造的简单设置-重置触发器进行建模。

S-R Flip-Flop 模块有两个输入，即 **S** 和 **R**（**S** 表示设置，**R** 表示重置）和两个输出，即 **Q** 及其反值 **!Q**。

S-R Flip-Flop 模块的真值表如下。在此真值表中，**Q**n-1 是前一时间步的输出。

**注意**

S-R Flip-Flop 模块将非零输入视为 true (`1`)。

| S | R | Qn | !Qn |
| --- | --- | --- | --- |
| 0 | 0 | Qn-1 | !Qn-1 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |

当 **S** 为 1 且 **R** 为 0 时，触发器进入设置状态（**Q**n 为 1）。当 **R** 为 1 且 **S** 为 0 时，触发器进入重置状态（**Q**n 为 0）。当 **S** 和 **R** 都为 0 时，触发器停留在先前的状态（**Q**n 为 **Q**n-1）。

**提示**

应避免出现 **R** 和 **S** 都为 1 的状态。在这种状态下，**Q** 和 **!Q** 都为 0。此状态未定义，因为 **!Q** 不是 **Q** 的反值。要处理这种状态，请考虑 J-K Flip-Flop 模块。

### 布尔或双精度数据类型的逻辑信号

**将逻辑信号实现为布尔数据(而不是双精度数据)** 配置参数设置会影响 S-R Flip-Flop 模块的输入和输出数据类型，因为该模块是使用 Combinatorial Logic 模块的封装子系统。有关此配置参数的详细信息，请参阅将逻辑信号实现为布尔数据(而不是双精度数据)。
