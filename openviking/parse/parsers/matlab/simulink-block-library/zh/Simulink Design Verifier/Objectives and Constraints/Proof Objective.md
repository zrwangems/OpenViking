---
type: simulink-block
title: 'Proof Objective'
family: 'sldv'
product_id: 'sldv'
product_name: 'Simulink Design Verifier'
documentation_release: R2025b
official_category: 'Objectives and Constraints'
documentation_page: 'proofobjective'
documentation_source_path: 'ref/proofobjective.html'
language: zh-CN
chinese_source: official
---

# Proof Objective

## 端口

### 输入

### **Values** — 输入信号 标量 | 元胞数组

Proof Objective 模块接受 Simulink 软件支持的所有内置数据类型的信号。有关 Simulink 软件支持的数据类型的讨论，请参阅Simulink 支持的数据类型。该模块不支持复杂的输入信号。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **启用** — 指定是否启用模块 `on` (默认) | `off`

指定该模块是否启用。如果选中（默认），Simulink Design Verifier 软件在证明模型的属性时使用该模块。清除此选项将禁用该模块，也就是说，导致 Simulink Design Verifier 软件的行为就像 Proof Objective 模块不存在一样。如果未选择此选项，则该模块将在 Simulink 编辑器中显示为灰色。

### **值** — 指定证明目标 标量 | 元胞数组

指定证明目标（请参阅指定证明目标）。

### **显示值** — 显示 values 参数的内容 `on` (默认) | `off`

指定模块是否在 Simulink 编辑器中显示其**值**参数的内容。默认情况下，选择此选项。

### **直通模式** — 指定证明目标 `on` (默认) | `off`

指定模块是否在 Simulink 编辑器中显示输出端口。如果选中（默认），该模块将显示其输出端口，允许其输入信号作为模块输出通过。如果未选择，该模块将隐藏其输出端口并终止输入信号。下图说明了每种情况下模块的外观。

**直通模式：已选择**

**直通模式：取消选定**

### **当属性违规时停止仿真** — 指定是否停止仿真 `on` (默认) | `off`

指定如果仿真遇到违反**值**参数中指定的属性的信号是否停止仿真。

如果选择此参数并仿真模型，则当遇到指定属性的违反时，仿真将停止。

## 所属库

Simulink Design Verifier / Objectives and Constraints

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和合成逻辑的附加配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| **无 HDL** | 不要为该模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | 控制不相关逻辑的移除。默认值为 `off`，这意味着未连接的逻辑不会保留在 HDL 代码中。有关更多详细信息，请参阅 PreserveUpstreamLogic (HDL Coder)。 |

## 版本历史

**在 R2007a 中推出**

## 描述

定义信号在证明模型属性时必须满足的目标

在属性证明模式下运行时，Simulink® Design Verifier™ 软件会证明您的模型的属性满足指定的准则（请参阅 使用 Simulink Design Verifier 证明模型属性）。在这种模式下，您可以使用 Proof Objective 模块来定义模型中信号的证明目标。

**值**参数允许您为模块的输入信号指定可接受的值。如果信号值在*任何*时间步内偏离可接受值，则会发生属性违规并且证明目标被证伪。该模块将指定的**值**参数应用于其输入信号，并且 Simulink Design Verifier 软件证明或反驳您的模型的属性是否满足指定的准则。

该模块的参数对话框允许您

- 启用或禁用目标。
- 指定该模块应在 Simulink 编辑器中显示其**值**参数。
- 指定该模块应显示其输出端口。

**注意**

Simulink 和 Simulink Coder™ 软件分别在模型仿真和代码生成期间忽略 Proof Objective 模块。Simulink Design Verifier 软件仅在证明模型属性时使用 Proof Objective 模块。

### 指定证明目标

使用**值**参数来定义信号在验证仿真期间必须达到的值。以 MATLAB® 元胞数组的形式指定标量和区间的任意组合。有关元胞数组的信息，请参阅 元胞数组。

**提示**

如果**值**参数仅指定一个标量值，则无需以 MATLAB 元胞数组的形式输入。

每个标量值构成数组中的一个元胞，例如：

```
{0, 5}
```

闭区间由一个二元素向量作为数组中的一个元胞组成，其中每个元素指定一个区间端点：

```
{[1, 2]}
```

或者，您可以使用 `Sldv.Point` 构造函数指定标量值，该构造函数接受单个值作为其参量。您可以使用 `Sldv.Interval` 构造函数指定间隔，该构造函数需要两个输入参量，即区间的下限和上限。您也可以选择提供以下值之一作为第三个输入参量，用于指定区间端点的包含或排除：

- `'()'` - 定义开区间。
- `'[]'` - 定义闭区间。
- `'(]'` - 定义左开区间。
- `'[)'` - 定义右开区间。

**注意**

默认情况下，如果省略第三个输入参量，`Sldv.Interval` 会认为区间是封闭的。

例如，**值**参数

```
{0, [1, 3]}
```

指定：

- `0` - 标量
- `[1, 3]` - 闭区间

**值**参数

```
{Sldv.Interval(0, 1, '[)'), Sldv.Point(1)}
```

指定：

- `Sldv.Interval(0, 1, '[)')` - 右开区间[0, 1)
- `Sldv.Point(1)` - 标量

如果为 Proof Objective 模块指定多个标量和间隔，则 Simulink Design Verifier 软件会在属性证明过程中使用逻辑或运算将它们组合起来。在这种情况下，如果任何单个标量或区间得到满足，则软件认为整个证明目标得到满足。
