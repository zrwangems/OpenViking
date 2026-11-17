---
type: simulink-block
title: 'Test Objective'
family: 'sldv'
product_id: 'sldv'
product_name: 'Simulink Design Verifier'
documentation_release: R2025b
official_category: 'Objectives and Constraints'
documentation_page: 'testobjective'
documentation_source_path: 'ref/testobjective.html'
language: zh-CN
chinese_source: worker-translation
---

# Test Objective

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

Test Objective 模块接受 Simulink 软件支持的所有内置数据类型的信号。有关 Simulink 软件支持的数据类型的讨论，请参阅 Data Types Supported by Simulink。该模块不支持复数输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
## 参数
```yaml
parameters:
- name: Enable
  summary: 指定模块是否启用 on（默认）| off
  group: ''
- name: Values
  summary: 指定测试目标 标量 | 元胞数组
  group: ''
  values: 参数
- name: Display values
  summary: 显示 values 参数的内容 on（默认）| off
  group: ''
- name: Pass through style
  summary: 指定模块是否在 Simulink 编辑器中显示输出端口 on（默认）| off
  group: ''
```

### **Enable** — 指定模块是否启用 `on`（默认）| `off`

如果选中（默认），Simulink Design Verifier 软件在为模型生成测试时会使用该模块。清除此选项将禁用该模块，即导致 Simulink Design Verifier 软件的行为如同 Test Objective 模块不存在一样。如果未选中此选项，该模块在 Simulink 编辑器中显示为灰色。

### **Values** — 指定测试目标 标量 | 元胞数组

#### 指定测试目标

使用 **Values** 参数定义信号在测试用例中必须满足的自定义目标。以 MATLAB® 元胞数组的形式指定标量和区间的任意组合。有关元胞数组的信息，请参阅 Cell Arrays。

**提示**

如果 **Values** 参数仅指定一个标量值，则无需以 MATLAB 元胞数组的形式输入它。

标量值各自构成数组中的单个元胞，例如：

```
{0, 5}
```

闭区间由数组中的一个二元向量元胞构成，其中每个元素指定一个区间端点：

```
{[1, 2]}
```

或者，您可以使用 `Sldv.Point` 构造函数指定标量值，该构造函数接受单个值作为其参数。您可以使用 `Sldv.Interval` 构造函数指定区间，该构造函数需要两个输入参数，即区间的下界和上界。您还可以选择提供以下值之一作为第三个输入参数，用于指定区间端点的包含或排除：

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

#### 规范的逻辑行为

如果您为 Test Objective 模块指定多个标量和区间，Simulink Design Verifier 软件在生成测试用例时会使用逻辑 OR 运算将它们组合起来。因此，如果任意单个标量或区间得到满足，软件就认为整个测试目标得到满足。

在单个标量或区间内，测试目标通过逻辑 AND 运算生成。在这种情况下，所有信号都必须满足约束条件，输入才能满足目标。

例如，考虑一个二维开区间：

```
Sldv.Interval([-5 -5],[5 2],'()')
```

零向量 `[0 0]` 满足目标，因为零元素位于区间 `-5` 到 `5` 和 `-5` 到 `2` 之内。

向量 `[0 3]` 不满足目标，因为第二个元素 3 落在区间 `-5` 到 `2` 之外。

### **Display values** — 显示 values 参数的内容 `on`（默认）| `off`

指定模块是否在 Simulink 编辑器中显示其 **Values** 参数的内容。

### **Pass through style** — 指定模块是否在 Simulink 编辑器中显示输出端口 `on`（默认）| `off`

如果选中，模块将显示其输出端口，允许其输入信号作为模块输出通过。如果未选中，模块将隐藏其输出端口并终止输入信号。

**示例：** 以下图形说明了每种情况下模块的外观。

**Pass through style (show Outport)：选中**

**Pass through style (show Outport)：未选中**
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

定义信号在测试用例中必须满足的自定义目标

在测试生成模式下运行时，Simulink® Design Verifier™ 软件会生成满足指定条件的测试用例（请参阅）。在此模式下，您可以使用 Test Objective 模块为模型中的信号定义自定义测试目标。**Values** 参数允许您指定信号在测试用例仿真期间至少一个时间步内必须达到的值。该模块将指定的 **Values** 参数应用于其输入信号，Simulink Design Verifier 软件尝试生成满足该目标的测试用例。

该模块的参数对话框还允许您

- 启用或禁用该目标。
- 指定模块应在 Simulink 编辑器中显示其 **Values** 参数。
- 指定模块应显示其输出端口。

**注意**

Simulink 和 Simulink Coder™ 软件在模型仿真和代码生成期间分别忽略 Test Objective 模块。Simulink Design Verifier 软件仅在为模型生成测试用例时使用 Test Objective 模块。
