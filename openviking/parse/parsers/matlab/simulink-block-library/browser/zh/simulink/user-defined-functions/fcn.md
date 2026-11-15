---
type: simulink-block
title: 'Fcn'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / User-Defined Functions'
documentation_page: 'fcn'
documentation_source_path: 'slref/fcn.html'
language: zh-CN
chinese_source: official
---

# Fcn

## 端口

### 输入

### **In** — Fcn 模块的输入 标量 | 向量

Fcn 模块接受并输出 `single` 或 `double` 类型的信号。

有关详细信息，请参阅 Simulink® 文档中的 Simulink 支持的数据类型。

**数据类型:** `single` | `double`
### 输出

### **Out** — Fcn 模块的输出 标量

Fcn 模块接受并输出 `single` 或 `double` 类型的信号。

有关详细信息，请参阅 Simulink 文档中的 Simulink 支持的数据类型。

**数据类型:** `single` | `double`

## 参数

### **表达式** — 指定数学表达式 数学表达式

指定要应用于输入的数学表达式。上面列出了表达式组件。表达式必须在数学上格式正确（使用匹配的括号、适当数目的函数参量等）。表达式对可调性有限制（请参阅限制）。

#### 编程用法

|  |
| --- |
| **模块参数**：`Expr` |
| **类型：**字符向量 |
| **值：**数学表达式 |
| **默认值：**`'sin(u(1)*exp(2.3*(-u(2))))'` |

### **采样时间** — 指定模块中的采样时间 标量

**注意**

此参数在模块对话框中不可见，除非将其显式设置为 `-1` 以外的值。要了解详细信息，请参阅不建议设置采样时间的模块。

## 所属库

Simulink / User-Defined Functions

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| **模块**（默认值） | 为子系统和子系统内的模块生成代码。 |

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **BalanceDelays** | 检测沿一条路径引入的新延迟，并在其他路径上插入匹配的延迟。默认值为 **inherit**。另请参阅BalanceDelays (HDL Coder)。 |
| **ClockRatePipelining** | 以较快的时钟频率而不是较慢的数据速率插入流水线寄存器。默认值为 **inherit**。另请参阅ClockRatePipelining (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **DistributedPipelining** | 流水线寄存器分配或寄存器重定时。默认值为 **inherit**。另请参阅DistributedPipelining (HDL Coder)。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中删除子系统层次结构。默认值为 **inherit**。另请参阅FlattenHierarchy (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的功能等效的资源的数量。默认值为 0。另请参阅Resource Sharing (HDL Coder)。 |

## 版本历史

**在 R2006a 之前推出**

### R2023a: Fcn 模块已还原到用户定义的库中

Fcn 模块已还原到 **Simulink** > **User-Defined**库中。

## 描述

将指定的表达式应用于输入

Fcn 模块将指定的数学表达式应用于其输入。表达式可以包括以下一个或多个组件：

- `u` - 模块的输入。如果 `u` 是向量，则 `u(i)` 表示向量的第 *i* 个元素；`u(1)` 或单独一个 `u` 表示第一个元素。
- 数值常量。
- 算术运算符 (+ - `*` / ^)。
- 关系运算符 (`== != > < >= <=`) - 如果关系为 true，则表达式返回 1；否则，返回 0。
- 逻辑运算符 (&& || !) - 如果关系为 true，则表达式返回 1；否则，返回 0。
- 括号。
- 数学函数 - `abs`、`acos`、`asin`、`atan`、`atan2`、`ceil`、`cos`、`cosh`、`exp`、`floor`、`hypot`、`log`、`log10`、`power`、`rem`、`sgn`（等效于 MATLAB® 中的 `sign`）、`sin`、`sinh`、`sqrt`、`tan` 和 `tanh`。

  **注意**

  Fcn 模块不支持 `round` 和 `fix`。使用 Rounding Function 模块应用这些舍入模式。
- 工作区变量 - 在前面的项目列表中未识别的变量名称传递给 MATLAB 进行计算。矩阵或向量元素必须特意引用。例如，对于矩阵中的第一个元素，须使用 `A(1,1)` 而不是 `A`。

Fcn 模块遵循以下运算符优先级规则：

1. `( )`
2. `^`
3. `+ -` （一元）
4. `!`
5. `* /`
6. `+ -`
7. `> < <= >=`
8. `== !=`
9. `&&`
10. `||`

该表达式不同于 MATLAB 表达式，因为该表达式无法执行矩阵计算。此外，此模块不支持冒号运算符 (`:`)。

模块输入可以是标量或向量。输出始终为标量。对于向量输出，可考虑使用 Math Function 模块。如果模块输入是向量，并且函数对输入元素分别进行操作（例如 `sin` 函数），则该模块只对第一个向量元素进行操作。
