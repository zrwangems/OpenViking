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
chinese_source: worker-translation
---

# Proof Objective

## 端口
```yaml
ports:
- name: Values
  summary: 输入信号 标量 | 元胞数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus
```

### 输入

### **Values** — 输入信号 标量 | 元胞数组

Proof Objective 模块接受 Simulink 软件支持的所有内置数据类型的信号。有关 Simulink 软件支持的数据类型的讨论，请参阅 Simulink 支持的数据类型。该模块不支持复数输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
## 参数
```yaml
parameters:
- name: Enable
  summary: 指定模块是否启用 on（默认）| off
  group: ''
- name: Values
  summary: 指定证明目标 标量 | 元胞数组
  group: ''
- name: Diaplay values
  summary: 显示 values 参数的内容 on（默认）| off
  group: ''
- name: Pass through style
  summary: 指定证明目标 on（默认）| off
  group: ''
- name: Stop simulation when the property is violated
  summary: 指定是否停止仿真 on（默认）| off
  group: ''
```

### **Enable** — 指定模块是否启用 `on`（默认）| `off`

指定模块是否启用。如果选中（默认），Simulink Design Verifier 软件在证明模型属性时使用该模块。清除此选项将禁用该模块，即导致 Simulink Design Verifier 软件的行为如同 Proof Objective 模块不存在一样。如果未选中此选项，该模块在 Simulink 编辑器中显示为灰色。

### **Values** — 指定证明目标 标量 | 元胞数组

指定证明目标（请参阅指定证明目标）。

### **Diaplay values** — 显示 values 参数的内容 `on`（默认）| `off`

指定该模块是否在 Simulink 编辑器中显示其 **Values** 参数的内容。默认情况下，此选项被选中。

### **Pass through style** — 指定证明目标 `on`（默认）| `off`

指定该模块是否在 Simulink 编辑器中显示输出端口。如果选中（默认），该模块显示其输出端口，允许其输入信号作为模块输出传递。如果未选中，该模块隐藏其输出端口并终止输入信号。以下图形说明了每种情况下模块的外观。

**Pass through style：选中**

**Pass through style：未选中**

### **Stop simulation when the property is violated** — 指定是否停止仿真 `on`（默认）| `off`

指定当仿真遇到违反 **Values** 参数中指定属性的信号时是否停止仿真。

如果选中此参数并仿真模型，当遇到违反指定属性的情况时，仿真将停止。
## 所属库

Simulink Design Verifier / Objectives and Constraints

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `No HDL` | 不为该模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | 控制未连接逻辑的移除。默认值为 `off`，这意味着未连接逻辑不会保留在 HDL 代码中。有关更多详细信息，请参阅 PreserveUpstreamLogic (HDL Coder)。 |

## 版本历史

**在 R2007a 中引入**

## 描述

定义信号在证明模型属性时必须满足的目标

在属性证明模式下运行时，Simulink® Design Verifier™ 软件会证明模型的属性满足指定条件（请参阅 Prove Model Properties Using Simulink Design Verifier）。在此模式下，您可以使用 Proof Objective 模块为模型中的信号定义证明目标。

**Values** 参数允许您为模块的输入信号指定可接受的值。如果信号值在*任何*时间步偏离可接受的值，则发生属性违反，证明目标被证伪。该模块将指定的 **Values** 参数应用于其输入信号，Simulink Design Verifier 软件证明或反证模型的属性是否满足指定条件。

该模块的参数对话框允许您

- 启用或禁用目标。
- 指定模块应在 Simulink Editor 中显示其 **Values** 参数。
- 指定模块应显示其输出端口。

**注意**

Simulink 和 Simulink Coder™ 软件在模型仿真和代码生成期间分别忽略 Proof Objective 模块。Simulink Design Verifier 软件仅在证明模型属性时使用 Proof Objective 模块。

### 指定证明目标

使用 **Values** 参数定义信号在证明仿真期间必须达到的值。以 MATLAB® 元胞数组的形式指定标量和区间的任意组合。有关元胞数组的信息，请参阅 Cell Arrays。

**提示**

如果 **Values** 参数仅指定一个标量值，则无需以 MATLAB 元胞数组的形式输入它。

标量值各自构成数组中的单个元胞，例如：

```
{0, 5}
```

闭区间构成数组中的一个双元素向量元胞，其中每个元素指定一个区间端点：

```
{[1, 2]}
```

或者，您可以使用 `Sldv.Point` 构造函数指定标量值，该构造函数接受单个值作为其参数。您可以使用 `Sldv.Interval` 构造函数指定区间，该构造函数需要两个输入参数，即区间的下界和上界。可选地，您可以提供以下值之一作为第三个输入参数，用于指定区间端点的包含或排除：

- `'()'` — 定义开区间。
- `'[]'` — 定义闭区间。
- `'(]'` — 定义左开区间。
- `'[)'` — 定义右开区间。

**注意**

默认情况下，如果省略第三个输入参数，`Sldv.Interval` 将区间视为闭区间。

例如，**Values** 参数

```
{0, [1, 3]}
```

指定：

- `0` — 一个标量
- `[1, 3]` — 一个闭区间

**Values** 参数

```
{Sldv.Interval(0, 1, '[)'), Sldv.Point(1)}
```

指定：

- `Sldv.Interval(0, 1, '[)')` — 右开区间 [0, 1)
- `Sldv.Point(1)` — 一个标量

如果您为 Proof Objective 模块指定多个标量和区间，Simulink Design Verifier 软件在属性证明期间使用逻辑 OR 运算将它们组合。在这种情况下，如果任何单个标量或区间得到满足，软件就认为整个证明目标得到满足。
