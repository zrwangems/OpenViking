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
chinese_source: worker-translation
---

# S-R Flip-Flop

## 端口

### 输入

### **S** — 置位输入标量

*置位*输入，指定为标量、向量或矩阵。

#### 依赖关系

S-R Flip-Flop 模块接受的数据类型取决于 **Implement logic signals as boolean data (vs. double)** 配置参数的设置：

- `On` — S-R Flip-Flop 模块仅接受类型为 `boolean` 的实数标量信号。
- `Off` — S-R Flip-Flop 模块接受类型为 `boolean` 或 `double` 的实数标量信号（两个输入必须具有相同类型）。

**数据类型：** `double` | `Boolean`

### **R** — 复位输入标量

*复位*输入，指定为标量、向量或矩阵。

#### 依赖关系

S-R Flip-Flop 模块接受的数据类型取决于 **Implement logic signals as boolean data (vs. double)** 配置参数的设置：

- `On` — S-R Flip-Flop 模块仅接受类型为 `boolean` 的实数标量信号
- `Off` — S-R Flip-Flop 模块接受类型为 `boolean` 或 `double` 的实数标量信号（两个输入必须具有相同类型）。

**数据类型：** `double` | `Boolean`
### 输出

### **Q** — 输出信号 Q 标量

输出信号 **Q**，具有与输入相同的维度和数据类型。

**数据类型：** `double` | `Boolean`

### **!Q** — 输出信号 !Q 标量

输出信号 **!Q**，具有与输入相同的维度和数据类型。

**数据类型：** `double` | `Boolean`

## 参数

### **Initial condition (state of Q)** — 输出 Q 的初始值 `0`（默认）| 标量

指定输出 **Q** 的初始值。非零值被视为真（`1`）。

#### 程序化使用

|  |
| --- |
| **模块参数：** `initial_condition` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认：** `'0'` |

## 所属库

Simulink Extras / Flip Flops

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2008b 中引入**

## 描述

对 S-R 触发器进行建模

S-R 触发器模块对使用或非门构建的简单置位-复位触发器进行建模。

S-R 触发器模块有两个输入 **S** 和 **R**（**S** 代表置位，**R** 代表复位）以及两个输出 **Q** 及其补码 **!Q**。

S-R 触发器模块的真值表如下。在此真值表中，**Q**n-1 是上一时间步的输出。

**注意**

S-R 触发器模块将非零输入视为真（`1`）。

| S | R | Q n | !Q n |
| --- | --- | --- | --- |
| 0 | 0 | Q n-1 | !Q n-1 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |

当 **S** 为 1 且 **R** 为 0 时，触发器进入置位状态（**Q**n 为 1）。当 **R** 为 1 且 **S** 为 0 时，触发器进入复位状态（**Q**n 为 0）。当 **S** 和 **R** 均为 0 时，触发器保持前一状态（**Q**n 为 **Q**n-1）。

**提示**

避免 **R** 和 **S** 均为 1 的状态。在此状态下，**Q** 和 **!Q** 均为 0。此状态是未定义的，因为 **!Q** 不是 **Q** 的补码。要处理此状态，请考虑使用 J-K 触发器模块。

### 逻辑信号作为布尔或双精度数据类型

**将逻辑信号实现为布尔数据（相对于双精度）** 配置参数设置会影响 S-R 触发器模块的输入和输出数据类型，因为此模块是使用 Combinatorial Logic 模块的掩码子系统。有关此配置参数的详细信息，请参阅将逻辑信号实现为布尔数据（相对于双精度）。
